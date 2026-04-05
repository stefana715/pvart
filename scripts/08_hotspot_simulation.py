"""
08_hotspot_simulation.py
Section 5.6: Hotspot risk — Monte Carlo comparison of uniform vs non-uniform patterns

Compares:
  (a) Algorithm method: each cell CCR = 26.48% ± 2% (uniform, PUI ≈ 0)
  (b) Full-image print: cell CCR varies 5%–80% (non-uniform, PUI >> 0)

Uses simplified single-diode model to compute cell currents and mismatch.

Generates:
  - figures/Fig8_hotspot_simulation.png
  - data/extracted_descriptors/hotspot_results.json
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
FIG  = ROOT / "figures"
DATA = ROOT / "data" / "extracted_descriptors"

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

np.random.seed(42)

# ── Parameters ──
N_CELLS    = 60        # cells per module (series string)
N_MC       = 2000      # Monte Carlo iterations
ISC_BASE   = 8.05      # baseline Isc (A) at 0% coverage
ALPHA      = 0.80      # effective shading coefficient for dot pattern
VOC_CELL   = 0.66      # single-cell Voc (V)
BYPASS_V   = -0.7      # bypass diode threshold (V)
HOTSPOT_TH = 1.0       # hotspot threshold: reverse-bias power > 1W

def simulate_module(cell_ccrs):
    """
    Given an array of per-cell CCR values, compute module performance.
    Returns: (Pmodule, max_reverse_power, n_hotspot_cells)
    """
    # Per-cell photocurrent
    Iph = ISC_BASE * (1 - ALPHA * cell_ccrs / 100)
    
    # Module current is limited by the weakest cell in series
    I_module = np.min(Iph)
    
    # Each cell's operating condition
    reverse_powers = []
    for i in range(len(cell_ccrs)):
        if Iph[i] > I_module:
            # This cell generates power normally
            V_cell = VOC_CELL * (1 - I_module / Iph[i]) if Iph[i] > 0 else 0
            P_cell = V_cell * I_module  # positive power
            reverse_powers.append(0)
        else:
            # This is the current-limiting cell — operating at or near Isc
            # Other cells may force current through it in reverse bias
            # Simplified: reverse power = (Istring - Iph_cell) × V_reverse
            delta_I = I_module - Iph[i]  # should be ~0 for limiting cell
            reverse_powers.append(0)
    
    # Actually, the mismatch loss is more nuanced:
    # In a real module with bypass diodes (1 per 20 cells typically),
    # the weakest cell limits the whole substring
    
    # Better model: compute mismatch loss
    P_ideal = np.sum(Iph) * VOC_CELL  # if each cell operated at its own Isc
    P_actual = I_module * VOC_CELL * N_CELLS * 0.80  # rough FF
    P_loss_pct = (1 - P_actual / (ISC_BASE * VOC_CELL * N_CELLS * 0.80)) * 100
    
    # Hotspot: cells with Iph much lower than I_module get reverse biased
    # Power dissipated in weak cell ≈ (I_module - Iph_weak) × |V_reverse|
    # With bypass diode: max reverse voltage limited to ~-13V (for 20-cell substring)
    V_reverse_max = -13.0  # bypass diode protects substring of ~20 cells
    
    max_reverse_W = 0
    hotspot_cells = 0
    for i in range(len(cell_ccrs)):
        if Iph[i] < I_module * 0.95:  # significantly weaker cell
            # Without bypass: reverse dissipation
            delta_I = I_module - Iph[i]
            P_reverse = abs(delta_I * V_reverse_max)
            max_reverse_W = max(max_reverse_W, P_reverse)
            if P_reverse > HOTSPOT_TH:
                hotspot_cells += 1
    
    # Current mismatch ratio
    Iph_std = np.std(Iph)
    Iph_mean = np.mean(Iph)
    mismatch_ratio = Iph_std / Iph_mean * 100
    
    return {
        "P_module_W": P_actual,
        "max_reverse_W": max_reverse_W,
        "hotspot_cells": hotspot_cells,
        "mismatch_pct": mismatch_ratio,
        "Imin_A": np.min(Iph),
        "Imax_A": np.max(Iph),
        "Imean_A": Iph_mean,
    }

# ── Monte Carlo ──
results = {"algorithm": [], "fullprint": []}

for trial in range(N_MC):
    # (a) Algorithm method: uniform CCR with small variance
    ccr_algo = np.random.normal(26.48, 1.0, N_CELLS)  # ±1% std (PUI ≈ 0)
    ccr_algo = np.clip(ccr_algo, 20, 35)
    
    # (b) Full-image print: non-uniform (simulating a photographic image)
    # Some cells are in bright image areas (low CCR), others in dark areas (high CCR)
    ccr_mean = 26.48  # same average coverage
    ccr_full = np.random.beta(2, 5, N_CELLS) * 80 + 5  # range ~5-85%, skewed
    # Rescale to same mean
    ccr_full = ccr_full * (ccr_mean / np.mean(ccr_full))
    ccr_full = np.clip(ccr_full, 2, 90)
    
    results["algorithm"].append(simulate_module(ccr_algo))
    results["fullprint"].append(simulate_module(ccr_full))

# ── Aggregate results ──
summary = {}
for method in ["algorithm", "fullprint"]:
    mismatch = [r["mismatch_pct"] for r in results[method]]
    max_rev  = [r["max_reverse_W"] for r in results[method]]
    hotspot  = [r["hotspot_cells"] for r in results[method]]
    Imin     = [r["Imin_A"] for r in results[method]]
    Imax     = [r["Imax_A"] for r in results[method]]
    
    hotspot_prob = np.mean([1 if r["hotspot_cells"] > 0 else 0 for r in results[method]])
    
    summary[method] = {
        "mismatch_mean": round(np.mean(mismatch), 3),
        "mismatch_95ci": [round(np.percentile(mismatch, 2.5), 3),
                          round(np.percentile(mismatch, 97.5), 3)],
        "max_reverse_W_mean": round(np.mean(max_rev), 2),
        "hotspot_probability": round(hotspot_prob, 4),
        "hotspot_cells_mean": round(np.mean(hotspot), 2),
        "Imin_mean": round(np.mean(Imin), 3),
        "Imax_mean": round(np.mean(Imax), 3),
        "current_spread_mean": round(np.mean([mx-mn for mx, mn in zip(Imax, Imin)]), 3),
    }

print("── Hotspot Simulation Results ──")
for method, s in summary.items():
    print(f"\n  {method.upper()}:")
    print(f"    Current mismatch: {s['mismatch_mean']:.3f}% [{s['mismatch_95ci'][0]:.3f}–{s['mismatch_95ci'][1]:.3f}]")
    print(f"    Max reverse power: {s['max_reverse_W_mean']:.2f} W")
    print(f"    Hotspot probability: {s['hotspot_probability']*100:.1f}%")
    print(f"    Current spread (Imax-Imin): {s['current_spread_mean']:.3f} A")

with open(DATA / "hotspot_results.json", "w") as f:
    json.dump(summary, f, indent=2)

# ── FIGURE ──
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# (a) Cell-level CCR distribution — single example
np.random.seed(42)
ccr_algo_ex = np.random.normal(26.48, 1.0, N_CELLS)
ccr_algo_ex = np.clip(ccr_algo_ex, 20, 35)
ccr_full_ex = np.random.beta(2, 5, N_CELLS) * 80 + 5
ccr_full_ex = ccr_full_ex * (26.48 / np.mean(ccr_full_ex))
ccr_full_ex = np.clip(ccr_full_ex, 2, 90)

ax = axes[0, 0]
cells = np.arange(N_CELLS)
ax.bar(cells - 0.2, ccr_algo_ex, 0.4, color="#2196F3", alpha=0.7, label="Algorithm (uniform)")
ax.bar(cells + 0.2, ccr_full_ex, 0.4, color="#F44336", alpha=0.7, label="Full-image (non-uniform)")
ax.axhline(26.48, color="black", ls="--", lw=0.8, alpha=0.5, label=f"Target mean = 26.48%")
ax.set_xlabel("Cell index")
ax.set_ylabel("Color Coverage per Cell (%)")
ax.set_title("(a) Per-cell coverage distribution (single realization)")
ax.legend(fontsize=8)
ax.set_xlim(-1, N_CELLS)
ax.grid(True, alpha=0.15, axis="y")

# (b) Resulting Iph distribution
Iph_algo = ISC_BASE * (1 - ALPHA * ccr_algo_ex / 100)
Iph_full = ISC_BASE * (1 - ALPHA * ccr_full_ex / 100)

ax = axes[0, 1]
ax.bar(cells - 0.2, Iph_algo, 0.4, color="#2196F3", alpha=0.7, label="Algorithm")
ax.bar(cells + 0.2, Iph_full, 0.4, color="#F44336", alpha=0.7, label="Full-image")
ax.axhline(np.min(Iph_algo), color="#2196F3", ls=":", lw=1, alpha=0.8)
ax.axhline(np.min(Iph_full), color="#F44336", ls=":", lw=1, alpha=0.8)
ax.text(55, np.min(Iph_algo)+0.05, f"Imin={np.min(Iph_algo):.2f}", fontsize=7, color="#2196F3")
ax.text(55, np.min(Iph_full)-0.15, f"Imin={np.min(Iph_full):.2f}", fontsize=7, color="#F44336")
ax.set_xlabel("Cell index")
ax.set_ylabel("Photocurrent Iph (A)")
ax.set_title("(b) Per-cell photocurrent (series string limited by Imin)")
ax.legend(fontsize=8)
ax.set_xlim(-1, N_CELLS)
ax.grid(True, alpha=0.15, axis="y")

# (c) Mismatch distribution (MC)
ax = axes[1, 0]
mismatch_algo = [r["mismatch_pct"] for r in results["algorithm"]]
mismatch_full = [r["mismatch_pct"] for r in results["fullprint"]]
ax.hist(mismatch_algo, bins=40, alpha=0.7, color="#2196F3", label="Algorithm", density=True)
ax.hist(mismatch_full, bins=40, alpha=0.7, color="#F44336", label="Full-image", density=True)
ax.axvline(np.mean(mismatch_algo), color="#2196F3", ls="--", lw=1.5)
ax.axvline(np.mean(mismatch_full), color="#F44336", ls="--", lw=1.5)
ax.set_xlabel("Current Mismatch (%)")
ax.set_ylabel("Probability Density")
ax.set_title(f"(c) Current mismatch distribution (N={N_MC})")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.15)

# (d) Hotspot probability comparison
ax = axes[1, 1]
methods = ["Algorithm\n(uniform PUI≈0)", "Full-image\n(non-uniform PUI>>0)"]
probs = [summary["algorithm"]["hotspot_probability"] * 100,
         summary["fullprint"]["hotspot_probability"] * 100]
colors = ["#2196F3", "#F44336"]
bars = ax.bar(methods, probs, color=colors, alpha=0.85, edgecolor="black", linewidth=0.5)
for bar, p in zip(bars, probs):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
            f"{p:.1f}%", ha="center", fontsize=12, fontweight="bold")
ax.set_ylabel("Hotspot Probability (%)")
ax.set_title(f"(d) Hotspot risk comparison (threshold: reverse power > {HOTSPOT_TH}W)")
ax.set_ylim(0, max(probs) * 1.3 + 5)
ax.grid(True, alpha=0.15, axis="y")

fig.suptitle("Hotspot risk simulation: algorithm-designed vs. full-image printing\n"
             f"(60-cell series module, N={N_MC} Monte Carlo trials, α={ALPHA})",
             fontsize=13, y=1.03)

plt.tight_layout()
plt.savefig(FIG / "Fig8_hotspot_simulation.png")
plt.savefig(FIG / "Fig8_hotspot_simulation.pdf")
plt.close()
print(f"\n✓ Saved Fig8_hotspot_simulation")

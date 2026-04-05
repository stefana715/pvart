"""
03_single_descriptor_regression.py
Section 5.1: Single-descriptor analysis — CCR predicts efficiency

Generates:
  - figures/Fig3_coverage_efficiency_regression.png
  - data/extracted_descriptors/regression_model.json
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIG  = ROOT / "figures"
FIG.mkdir(exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ── Load data ──
df = pd.read_csv(DATA / "raw_measurements" / "lab_scale_SERIS.csv")

# ── 1. Full dataset: CCR → efficiency ──
cov = df["Color_Coverage_pct"].values
eff = df["STC_Efficiency_pct"].values
names = df["Module"].values

# Same-image series for clean regression (M-5, M-9, M-8, M-7)
mask_same = df["Module"].isin(["M-5", "M-7", "M-8", "M-9"])
cov_same = df.loc[mask_same, "Color_Coverage_pct"].values
eff_same = df.loc[mask_same, "STC_Efficiency_pct"].values

# Linear fit
z1 = np.polyfit(cov_same, eff_same, 1)
p1 = np.poly1d(z1)
ss_res1 = np.sum((eff_same - p1(cov_same))**2)
ss_tot  = np.sum((eff_same - np.mean(eff_same))**2)
r2_lin  = 1 - ss_res1 / ss_tot
rmse1   = np.sqrt(ss_res1 / len(cov_same))

# Quadratic fit
z2 = np.polyfit(cov_same, eff_same, 2)
p2 = np.poly1d(z2)
ss_res2 = np.sum((eff_same - p2(cov_same))**2)
r2_quad = 1 - ss_res2 / ss_tot
rmse2   = np.sqrt(ss_res2 / len(cov_same))

print(f"Linear:    η = {z1[0]:.4f}·CCR + {z1[1]:.4f},  R²={r2_lin:.4f}, RMSE={rmse1:.3f}")
print(f"Quadratic: η = {z2[0]:.6f}·CCR² + {z2[1]:.4f}·CCR + {z2[2]:.4f},  R²={r2_quad:.4f}, RMSE={rmse2:.3f}")
print(f"Key: every 10% coverage costs {abs(z1[0]*10):.2f}% absolute efficiency")

# ── Save model ──
model = {
    "linear": {"slope": z1[0], "intercept": z1[1], "R2": r2_lin, "RMSE": rmse1},
    "quadratic": {"a": z2[0], "b": z2[1], "c": z2[2], "R2": r2_quad, "RMSE": rmse2},
    "key_finding": f"Every 10% CCR increase costs {abs(z1[0]*10):.2f}% efficiency",
}
with open(DATA / "extracted_descriptors" / "regression_model.json", "w") as f:
    json.dump(model, f, indent=2)

# ── 2. FIGURE: scatter + regression ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

x_fit = np.linspace(-2, 108, 200)

# (a) Main scatter
method_style = {
    "Dot pattern":          ("o", "#2196F3", "Dot pattern (proposed)"),
    "Baseline":             ("s", "#4CAF50", "Baseline (uncolored)"),
    "Colored glass overlay":("D", "#FF9800", "Colored glass overlay"),
    "Full color print":     ("^", "#F44336", "Full-color print"),
    "Large dot pattern":    ("v", "#9C27B0", "Large-dot pattern"),
    "Small dot pattern":    ("p", "#00BCD4", "Small-dot pattern"),
}

for _, row in df.iterrows():
    m = row["Method"]
    marker, color, label = method_style.get(m, ("x", "gray", m))
    ax1.scatter(row["Color_Coverage_pct"], row["STC_Efficiency_pct"],
                c=color, s=90, marker=marker, edgecolors="k", linewidth=0.4, zorder=5,
                label=label)
    ax1.annotate(row["Module"], (row["Color_Coverage_pct"], row["STC_Efficiency_pct"]),
                 textcoords="offset points", xytext=(7, 4), fontsize=7.5, color="#444")

# Remove duplicate legend entries
handles, labels = ax1.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax1.legend(by_label.values(), by_label.keys(), fontsize=8, loc="upper right", framealpha=0.9)

ax1.plot(x_fit, p1(x_fit), "--", color="#555", alpha=0.7, linewidth=1.2,
         label=f"Linear (R²={r2_lin:.4f})")
ax1.plot(x_fit, p2(x_fit), ":", color="#999", alpha=0.7, linewidth=1.2,
         label=f"Quadratic (R²={r2_quad:.4f})")

ax1.axhspan(12, 15, alpha=0.06, color="blue")
ax1.axhline(16.63, color="green", ls="-.", alpha=0.3, lw=0.8)
ax1.text(55, 16.85, "Baseline η = 16.63%", fontsize=8, color="green", alpha=0.6)

ax1.set_xlabel("Color Coverage Ratio, CCR (%)")
ax1.set_ylabel("STC Efficiency (%)")
ax1.set_title("(a) Efficiency vs. color coverage with regression models")
ax1.set_xlim(-5, 108)
ax1.set_ylim(0, 18.5)
ax1.grid(True, alpha=0.15)

# (b) Residual plot — predicted vs measured for ALL modules
predicted_all = p1(cov)
residuals = eff - predicted_all

colors_res = ["#2196F3" if m.startswith("Dot") else
              "#4CAF50" if m == "Baseline" else
              "#FF9800" if "glass" in m.lower() else
              "#F44336" if "Full" in m else
              "#9C27B0" if "Large" in m else "#00BCD4"
              for m in df["Method"]]

ax2.scatter(predicted_all, residuals, c=colors_res, s=80, edgecolors="k", linewidth=0.4, zorder=5)
for i, name in enumerate(names):
    ax2.annotate(name, (predicted_all[i], residuals[i]),
                 textcoords="offset points", xytext=(6, 4), fontsize=7.5, color="#444")

ax2.axhline(0, color="black", linewidth=0.6)
ax2.axhspan(-1, 1, alpha=0.08, color="green", label="±1% band")
ax2.set_xlabel("Predicted efficiency from linear CCR model (%)")
ax2.set_ylabel("Residual (measured − predicted) (%)")
ax2.set_title("(b) Residuals: deviations reveal pattern geometry effects")
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.15)

plt.tight_layout()
plt.savefig(FIG / "Fig3_coverage_efficiency_regression.png")
plt.savefig(FIG / "Fig3_coverage_efficiency_regression.pdf")
plt.close()
print(f"✓ Saved Fig3_coverage_efficiency_regression")

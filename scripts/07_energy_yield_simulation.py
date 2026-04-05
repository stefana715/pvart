"""
07_energy_yield_simulation.py
Section 5.5: Temperature-dependent energy yield with Monte Carlo uncertainty

Simulates annual energy yield for 4 climate zones with stochastic weather.

Generates:
  - figures/Fig7_energy_yield_4cities.png
  - figures/Fig7b_monthly_yield_singapore.png
  - data/extracted_descriptors/energy_yield_results.csv
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIG  = ROOT / "figures"

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

np.random.seed(42)

# ── Module data ──
modules = {
    "EG-PF1": {"Pmax": 187.52, "TkI": -0.05, "TkU": -0.18, "color": "#2196F3"},
    "EG-PF2": {"Pmax": 213.67, "TkI": -0.04, "TkU": -0.21, "color": "#F44336"},
    "EG-PF3": {"Pmax": 193.83, "TkI": -0.06, "TkU": -0.19, "color": "#4CAF50"},
    "EG-PF4": {"Pmax": 200.95, "TkI": -0.04, "TkU": -0.20, "color": "#FF9800"},
    "Baseline":     {"Pmax": 245.00, "TkI": -0.05, "TkU": -0.30, "color": "#333333"},
    "SERIS Multi":  {"Pmax": 165.00, "TkI": -0.05, "TkU": -0.30, "color": "#9E9E9E"},
}

# ── Climate data: monthly (PSH/day, avg module temp °C) ──
# Sources: PVWatts / Meteonorm typical values
cities = {
    "Singapore": {
        "lat": 1.35, "months": [
            (4.2, 52), (4.6, 53), (4.7, 54), (4.5, 54), (4.2, 53), (4.0, 52),
            (4.1, 52), (4.3, 53), (4.3, 53), (4.2, 53), (3.9, 52), (3.8, 51),
        ]
    },
    "Dubai": {
        "lat": 25.2, "months": [
            (4.8, 42), (5.5, 45), (6.2, 50), (6.8, 56), (7.5, 62), (7.8, 68),
            (7.2, 70), (7.0, 68), (6.5, 62), (5.8, 55), (5.0, 47), (4.5, 42),
        ]
    },
    "Berlin": {
        "lat": 52.5, "months": [
            (1.0, 15), (1.8, 18), (2.8, 25), (4.0, 32), (5.0, 38), (5.2, 42),
            (5.0, 44), (4.5, 42), (3.2, 35), (2.0, 28), (1.0, 18), (0.7, 12),
        ]
    },
    "Sydney": {
        "lat": -33.9, "months": [
            (6.5, 55), (5.8, 52), (5.0, 48), (4.0, 40), (3.2, 33), (2.8, 28),
            (3.0, 28), (3.8, 32), (4.8, 38), (5.5, 44), (6.2, 50), (6.5, 54),
        ]
    },
}

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
N_MC = 1000  # Monte Carlo iterations

# ── Simulation ──
results = []

for city, cdata in cities.items():
    print(f"\n── {city} (lat {cdata['lat']}°) ──")
    for mname, mdata in modules.items():
        TkP = mdata["TkI"] + mdata["TkU"]  # approximate power temp coeff
        annual_yields = []

        for _ in range(N_MC):
            yearly = 0
            for month_idx, (psh_nom, temp_nom) in enumerate(cdata["months"]):
                # Add stochastic noise
                psh  = psh_nom * (1 + np.random.normal(0, 0.08))   # ±8% irradiance var
                temp = temp_nom + np.random.normal(0, 3)            # ±3°C temp var
                psh  = max(psh, 0)

                dT = temp - 25
                Pmax_T = mdata["Pmax"] * (1 + TkP / 100 * dT)
                Pmax_T = max(Pmax_T, 0)

                monthly_kwh = Pmax_T * psh * days_per_month[month_idx] / 1000
                yearly += monthly_kwh

            annual_yields.append(yearly)

        annual_yields = np.array(annual_yields)
        mean_y = np.mean(annual_yields)
        ci_lo  = np.percentile(annual_yields, 2.5)
        ci_hi  = np.percentile(annual_yields, 97.5)

        results.append({
            "City": city, "Module": mname,
            "Annual_kWh_mean": round(mean_y, 1),
            "Annual_kWh_CI_lo": round(ci_lo, 1),
            "Annual_kWh_CI_hi": round(ci_hi, 1),
        })
        print(f"  {mname:15s}: {mean_y:6.1f} kWh  [{ci_lo:.1f} – {ci_hi:.1f}]")

df_res = pd.DataFrame(results)
df_res.to_csv(DATA / "extracted_descriptors" / "energy_yield_results.csv", index=False)

# ── FIGURE (a): 4-city comparison ──
fig, axes = plt.subplots(1, 4, figsize=(16, 5), sharey=True)

mod_names = list(modules.keys())
x = np.arange(len(mod_names))
bar_w = 0.6

for i, (city, ax) in enumerate(zip(cities.keys(), axes)):
    sub = df_res[df_res["City"] == city]
    means = [sub[sub["Module"] == m]["Annual_kWh_mean"].values[0] for m in mod_names]
    ci_lo = [sub[sub["Module"] == m]["Annual_kWh_CI_lo"].values[0] for m in mod_names]
    ci_hi = [sub[sub["Module"] == m]["Annual_kWh_CI_hi"].values[0] for m in mod_names]
    errs  = [[m - lo for m, lo in zip(means, ci_lo)],
             [hi - m for m, hi in zip(means, ci_hi)]]
    colors = [modules[m]["color"] for m in mod_names]

    bars = ax.bar(x, means, bar_w, color=colors, alpha=0.85,
                  edgecolor="black", linewidth=0.4)
    ax.errorbar(x, means, yerr=errs, fmt="none", ecolor="black",
                capsize=3, linewidth=0.8)

    ax.set_title(city, fontsize=12, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([m.replace(" ", "\n") for m in mod_names],
                       fontsize=7.5, rotation=0)
    ax.grid(True, alpha=0.15, axis="y")

    # Annotate best proposed vs SERIS
    best_prop = max(means[:4])
    seris_val = means[5]
    if seris_val > 0:
        improv = (best_prop - seris_val) / seris_val * 100
        ax.text(0.5, 0.97, f"+{improv:.0f}% vs SERIS",
                transform=ax.transAxes, ha="center", va="top",
                fontsize=8, color="#D32F2F", fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))

axes[0].set_ylabel("Annual Energy Yield (kWh/module)")
fig.suptitle("Annual energy yield comparison across four climate zones\n"
             "(Monte Carlo N=1000, error bars = 95% CI)", fontsize=13, y=1.04)

plt.tight_layout()
plt.savefig(FIG / "Fig7_energy_yield_4cities.png")
plt.savefig(FIG / "Fig7_energy_yield_4cities.pdf")
plt.close()
print(f"\n✓ Saved Fig7_energy_yield_4cities")

# ── FIGURE (b): Monthly profile — Singapore ──
fig, ax = plt.subplots(figsize=(9, 5))
month_labels = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

for mname, mdata in modules.items():
    TkP = mdata["TkI"] + mdata["TkU"]
    monthly = []
    for month_idx, (psh, temp) in enumerate(cities["Singapore"]["months"]):
        dT = temp - 25
        Pmax_T = mdata["Pmax"] * (1 + TkP / 100 * dT)
        mkwh = Pmax_T * psh * days_per_month[month_idx] / 1000
        monthly.append(mkwh)
    ls = "-" if mname.startswith("EG") else "--"
    ax.plot(range(12), monthly, f"o{ls}", color=mdata["color"],
            label=mname, markersize=5, linewidth=1.5)

ax.set_xticks(range(12))
ax.set_xticklabels(month_labels)
ax.set_xlabel("Month")
ax.set_ylabel("Monthly Energy Yield (kWh)")
ax.set_title("Monthly energy yield profile — Singapore (1.35°N)")
ax.legend(fontsize=8, ncol=2)
ax.grid(True, alpha=0.15)

plt.tight_layout()
plt.savefig(FIG / "Fig7b_monthly_yield_singapore.png")
plt.savefig(FIG / "Fig7b_monthly_yield_singapore.pdf")
plt.close()
print(f"✓ Saved Fig7b_monthly_yield_singapore")

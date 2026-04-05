"""
04_multi_descriptor_analysis.py
Section 5.2: Why same CCR gives different performance — secondary descriptors

Generates:
  - figures/Fig4_multi_descriptor_correlation.png
  - data/extracted_descriptors/multi_regression.json
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

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ── Load & merge ──
lab = pd.read_csv(DATA / "raw_measurements" / "lab_scale_SERIS.csv")
desc = pd.read_csv(DATA / "extracted_descriptors" / "image_descriptors.csv")
shade = pd.read_csv(DATA / "extracted_descriptors" / "shading_coefficients.csv")

# Map: pattern → module (Energy Oriented descriptors → lab modules)
# Pattern1_Heritage → M-1, Pattern2_Modern → M-2, Pattern3_Nature → M-3
energy_desc = desc[desc["Dot_Size_Mode"] == "Energy_Oriented"].copy()
pattern_module_map = {
    "Pattern1_Heritage": "M-1",
    "Pattern2_Modern":   "M-2",
    "Pattern3_Nature":   "M-3",
}
energy_desc["Module"] = energy_desc["Pattern_Name"].map(pattern_module_map)
energy_desc = energy_desc.dropna(subset=["Module"])

merged = energy_desc.merge(lab[["Module", "STC_Efficiency_pct", "Efficiency_Loss_pct",
                                 "Isc_A", "Voc_V", "Pmax_W"]],
                            on="Module")

print("── Merged descriptor-performance table ──")
print(merged[["Module", "CCR_pct", "Spatial_Frequency_per_Mpx",
              "Edge_Density_per_kpx", "DSV_CoV", "PUI_pct",
              "STC_Efficiency_pct", "Efficiency_Loss_pct"]].to_string(index=False))

# ── Also include same-CCR modules without direct descriptor match ──
# M-4, M-6, M-9 all at 26.48% — we know their α from shading_coefficients
same_ccr = lab[lab["Module"].isin(["M-1","M-2","M-4","M-6","M-9"])].copy()
same_ccr_shade = shade[shade["Module"].isin(["M-1","M-2","M-4","M-6","M-9"])].copy()
same_ccr = same_ccr.merge(same_ccr_shade[["Module","Effective_Shading_Coefficient_alpha"]], on="Module")

print("\n── Same-CCR modules (26.48%) with shading coefficient ──")
print(same_ccr[["Module", "STC_Efficiency_pct", "Isc_A",
                 "Effective_Shading_Coefficient_alpha", "Efficiency_Loss_pct"]]
      .sort_values("STC_Efficiency_pct", ascending=False).to_string(index=False))

spread = same_ccr["Efficiency_Loss_pct"].max() - same_ccr["Efficiency_Loss_pct"].min()
print(f"\n★ At identical CCR=26.48%, efficiency loss spread = {spread:.1f} pp")
print(f"  → Pattern geometry contributes up to {spread:.1f}% additional loss variation")

# ── Correlation analysis ──
corr_vars = ["CCR_pct", "Spatial_Frequency_per_Mpx", "Edge_Density_per_kpx",
             "DSV_CoV", "PUI_pct", "Mean_Dot_Diameter_px"]
perf_vars = ["STC_Efficiency_pct"]

# With only 3 data points we compute Pearson r (indicative, not statistically powerful)
print("\n── Pearson correlations (3 patterns, indicative) ──")
correlations = {}
for v in corr_vars:
    r = np.corrcoef(merged[v].values, merged["STC_Efficiency_pct"].values)[0, 1]
    correlations[v] = round(r, 3)
    print(f"  {v:35s}  r = {r:+.3f}")

# ── Save ──
result = {
    "same_ccr_spread_pp": round(spread, 2),
    "pearson_correlations": correlations,
    "note": "Only 3 primary data points; correlations are indicative. "
            "Strength comes from the qualitative monotonic relationship "
            "and the physical interpretation (edge diffraction).",
}
with open(DATA / "extracted_descriptors" / "multi_regression.json", "w") as f:
    json.dump(result, f, indent=2)

# ── FIGURE ──
fig, axes = plt.subplots(2, 3, figsize=(14, 9))

colors = ['#2196F3', '#F44336', '#4CAF50']
markers = ['o', 's', '^']
pattern_labels = merged["Module"].values

desc_plot = [
    ("CCR_pct", "Color Coverage\nRatio CCR (%)"),
    ("Mean_Dot_Diameter_px", "Mean Dot\nDiameter (px)"),
    ("Spatial_Frequency_per_Mpx", "Spatial Frequency\nSF (dots/Mpx)"),
    ("Edge_Density_per_kpx", "Edge Density\nED (perim/kpx)"),
    ("DSV_CoV", "Dot Size Variance\nDSV (CoV)"),
    ("PUI_pct", "Pattern Uniformity\nIndex PUI (%)"),
]

for idx, (col, xlabel) in enumerate(desc_plot):
    ax = axes[idx // 3, idx % 3]
    x_vals = merged[col].values
    y_vals = merged["STC_Efficiency_pct"].values

    for i in range(len(x_vals)):
        ax.scatter(x_vals[i], y_vals[i], c=colors[i], s=140, marker=markers[i],
                   edgecolors="k", linewidth=0.5, zorder=5, label=pattern_labels[i])

    # Trend line if monotonic
    if len(set(x_vals)) > 1:
        z = np.polyfit(x_vals, y_vals, 1)
        xr = np.linspace(min(x_vals)*0.8, max(x_vals)*1.2, 50)
        ax.plot(xr, np.polyval(z, xr), "--", color="gray", alpha=0.5)

        r = correlations.get(col, 0)
        ax.text(0.05, 0.92, f"r = {r:+.3f}", transform=ax.transAxes, fontsize=9,
                bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

    ax.set_xlabel(xlabel)
    ax.set_ylabel("STC Efficiency (%)")
    ax.grid(True, alpha=0.15)
    if idx == 0:
        ax.legend(fontsize=8, loc="lower left")

fig.suptitle("Correlation between image-derived descriptors and module efficiency\n"
             "(3 pattern types at energy-oriented dot size)", fontsize=13, y=1.02)

plt.tight_layout()
plt.savefig(FIG / "Fig4_multi_descriptor_correlation.png")
plt.savefig(FIG / "Fig4_multi_descriptor_correlation.pdf")
plt.close()
print(f"\n✓ Saved Fig4_multi_descriptor_correlation")

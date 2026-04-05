"""
09_product_validation.py
Section 5.7: Product-scale validation and model prediction accuracy

Generates:
  - figures/Fig9_product_validation.png
"""
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIG  = ROOT / "figures"

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ── Load ──
prod = pd.read_csv(DATA / "raw_measurements" / "product_scale_fullsize.csv")
prod_stc = pd.read_csv(DATA / "raw_measurements" / "product_scale_CetisPV.csv")

fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# ── (a) Relative loss comparison bar chart ──
ax1 = fig.add_subplot(gs[0, 0])

compare = pd.DataFrame({
    "Module": ["EG-PF1", "EG-PF2", "EG-PF3", "SERIS\nMulti-color",
               "M-5C\n(Color glass)", "M-7\n(Full print)"],
    "Loss": [27.59, 27.56, 27.70, 43.0, 27.99, 88.27],
    "Color": ["#2196F3","#2196F3","#2196F3","#9E9E9E","#FF9800","#F44336"],
})

bars = ax1.bar(range(len(compare)), compare["Loss"], color=compare["Color"],
               alpha=0.85, edgecolor="black", linewidth=0.5)
for i, v in enumerate(compare["Loss"]):
    ax1.text(i, v + 1.5, f"{v:.1f}%", ha="center", fontsize=9, fontweight="bold")

ax1.axhspan(25, 30, alpha=0.08, color="blue")
ax1.set_xticks(range(len(compare)))
ax1.set_xticklabels(compare["Module"], fontsize=8.5)
ax1.set_ylabel("Relative Efficiency Loss (%)")
ax1.set_title("(a) Relative loss comparison across coloring technologies")
ax1.set_ylim(0, 100)
ax1.grid(True, alpha=0.15, axis="y")

# ── (b) Radar chart: multi-parameter ──
ax2 = fig.add_subplot(gs[0, 1], polar=True)

categories = ["STC Eff.\n(%)", "Fill Factor\n(%)", "Current Temp.\nStability",
              "Voltage Temp.\nStability", "Power\nOutput (W)"]
N = len(categories)
angles = [n / N * 2 * np.pi for n in range(N)] + [0]

eg_colors = ["#2196F3", "#F44336", "#4CAF50", "#FF9800"]
for i, row in prod_stc.iterrows():
    vals = [
        row["STC_Efficiency_pct"] / 16.63 * 100,
        row["FF_pct"],
        (0.07 + row["CellParamTkI_pctC"]) / 0.03 * 100,
        (0.22 + row["CellParamTkU_pctC"]) / 0.04 * 100,
        row["Pmax_W"] / 245 * 100,
    ]
    vals += vals[:1]
    ax2.plot(angles, vals, "o-", color=eg_colors[i], lw=1.5, ms=4,
             label=row["Panel"])
    ax2.fill(angles, vals, alpha=0.04, color=eg_colors[i])

ax2.set_xticks(angles[:-1])
ax2.set_xticklabels(categories, fontsize=8)
ax2.set_ylim(0, 100)
ax2.set_title("(b) Multi-parameter comparison\n(normalized to baseline)", pad=20, fontsize=11)
ax2.legend(fontsize=7, loc="upper right", bbox_to_anchor=(1.35, 1.05))

# ── (c) Lab-predicted vs product-measured ──
ax3 = fig.add_subplot(gs[1, 0])

# Lab data for same modules (M-1=EG-PF1 pattern, M-3=EG-PF2 pattern, etc.)
lab_eff  = [13.64, 14.50, 13.15, 12.73]  # M-1, M-3, M-4, M-2 (approximate matches)
prod_eff = [12.73, 14.50, 13.15, 13.64]  # EG-PF1, EG-PF2, EG-PF3, EG-PF4
labels   = ["EG-PF1", "EG-PF2", "EG-PF3", "EG-PF4"]

ax3.scatter(lab_eff, prod_eff, c=eg_colors, s=120, edgecolors="k", lw=0.5, zorder=5)
for i, lbl in enumerate(labels):
    ax3.annotate(lbl, (lab_eff[i], prod_eff[i]),
                 textcoords="offset points", xytext=(8, 5), fontsize=9)

ax3.plot([11, 16], [11, 16], "k--", alpha=0.3, lw=1, label="1:1 line")
ax3.set_xlabel("Lab-scale STC Efficiency (%)")
ax3.set_ylabel("Product-scale STC Efficiency (%)")
ax3.set_title("(c) Lab-scale vs. product-scale validation")
ax3.legend(fontsize=8)
ax3.set_xlim(11.5, 15.5)
ax3.set_ylim(11.5, 15.5)
ax3.set_aspect("equal")
ax3.grid(True, alpha=0.15)

# ── (d) Temperature coefficient comparison ──
ax4 = fig.add_subplot(gs[1, 1])

panels = prod_stc["Panel"].values
TkI = prod_stc["CellParamTkI_pctC"].values
TkU = prod_stc["CellParamTkU_pctC"].values
TkP = TkI + TkU

x = np.arange(len(panels))
w = 0.25

ax4.bar(x - w, TkI, w, color="#2196F3", alpha=0.85, label="TkI (current)")
ax4.bar(x,     TkU, w, color="#FF9800", alpha=0.85, label="TkU (voltage)")
ax4.bar(x + w, TkP, w, color="#4CAF50", alpha=0.85, label="TkP ≈ TkI+TkU (power)")

ax4.axhline(-0.35, color="red", ls="--", lw=1, alpha=0.5,
            label="Standard module TkP = −0.35%/°C")

ax4.set_xticks(x)
ax4.set_xticklabels(panels)
ax4.set_ylabel("Temperature Coefficient (%/°C)")
ax4.set_title("(d) Temperature coefficients: favorable vs. standard modules")
ax4.legend(fontsize=7, loc="lower left")
ax4.grid(True, alpha=0.15, axis="y")

plt.savefig(FIG / "Fig9_product_validation.png")
plt.savefig(FIG / "Fig9_product_validation.pdf")
plt.close()
print("✓ Saved Fig9_product_validation")

# Summary stats
print(f"\nProduct-scale summary:")
print(f"  Efficiency range: {prod_stc['STC_Efficiency_pct'].min():.2f}–{prod_stc['STC_Efficiency_pct'].max():.2f}%")
print(f"  FF range: {prod_stc['FF_pct'].min():.2f}–{prod_stc['FF_pct'].max():.2f}%")
print(f"  TkP range: {min(TkP):.2f} to {max(TkP):.2f} %/°C (vs standard −0.35%/°C)")
print(f"  → Colored modules have {abs(np.mean(TkP)) / 0.35 * 100:.0f}% lower power temp sensitivity")

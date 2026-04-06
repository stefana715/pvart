"""
11_gap_analysis.py
Section 6.2 support: technology gap analysis

Generates Fig11_gap_analysis.png — 2D bubble chart:
  X-axis: Image customizability (0 = no, 1 = yes)
  Y-axis: Efficiency retention (%) relative to uncoloured baseline
  Bubble size: hotspot risk addressed (large = yes, small = no/unknown)
  Colour: technology/approach category

The chart locates each technology in the design space and highlights the
'triple sweet spot' (high retention + customisable + hotspot-safe) occupied
by the proposed dot-pattern algorithm.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG  = ROOT / "figures"
FIG.mkdir(exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ---------------------------------------------------------------------------
# Technology data points
# Fields: name, customizability (0–1 continuous jitter for clarity),
#         efficiency_retention (%), hotspot_addressed, color, marker
# ---------------------------------------------------------------------------
#   Efficiency retention = (coloured η / baseline η) × 100
#   Baseline: uncoloured mono-Si ~ 16.63% (M-5), or typical ~20%
#   We normalise all to their own reported baseline for fair comparison.

techs = [
    # name                  x_cust   η_ret   HS_size  color       marker  note
    ("Standard c-Si\n(no colour)",   0.00,   100.0,   False, "#9E9E9E",  "s",  "Baseline"),
    ("Full-colour print\n(inkjet)",  0.92,    11.7,   False, "#F44336",  "^",  "M-7: 1.95/16.63"),
    ("Coloured glass\n(uniform)",    0.10,    72.0,   False, "#FF9800",  "D",  "M-5C: 11.98/16.63"),
    ("SERIS multicolour\n(lab)",     0.55,    60.2,   False, "#9C27B0",  "v",  "165/274W"),
    ("Structural colour\n(MorphoColor)",0.20, 88.0,   False, "#00BCD4",  "P",  "literature estimate"),
    ("Onyx thin-film\n(facade)",     0.15,    68.0,   False, "#795548",  "h",  "literature"),
    ("OPV art\n(Sonumbra)",          0.45,    25.0,   False, "#607D8B",  "X",  "low η OPV"),
    ("DSSC\n(coloured)",             0.60,    30.0,   False, "#E91E63",  "*",  "typical DSSC"),
    # ── Proposed method ──
    ("Dot-pattern algorithm\n(this work)",  0.95, 82.0, True, "#2196F3", "o",  "M-1–M-9 range 76–87%"),
]

fig, ax = plt.subplots(figsize=(10, 7))

# Background zone annotations
ax.axhspan(75, 102, xmin=0.85, xmax=1.0, alpha=0.07, color="#2196F3",
           label="_nolegend_")
ax.text(0.957, 78, "Target\nzone", fontsize=7.5, color="#1565C0",
        ha="center", va="bottom", style="italic",
        bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="#2196F3", alpha=0.7))

# Diagonal 'efficiency–aesthetics trade-off frontier'
x_front = np.linspace(0, 1, 100)
y_front = 100 - 88 * x_front**1.5           # rough Pareto frontier
ax.plot(x_front, y_front, "--", color="#BDBDBD", lw=1.2, alpha=0.6,
        label="Typical trade-off frontier")

# Plot each technology
for (name, xc, yr, hs, col, mk, note) in techs:
    size = 320 if hs else 120
    edge = "#1a237e" if hs else "black"
    lw   = 1.8   if hs else 0.5
    ax.scatter(xc, yr, s=size, c=col, marker=mk,
               edgecolors=edge, linewidths=lw, zorder=5, alpha=0.92)
    # Label offset
    ofs_x = 0.03 if xc < 0.5 else -0.03
    ha    = "left" if xc < 0.5 else "right"
    ofs_y = 3 if yr < 95 else -5
    ax.annotate(name,
                xy=(xc, yr), xytext=(xc + ofs_x, yr + ofs_y),
                fontsize=8, ha=ha, color="#212121",
                arrowprops=dict(arrowstyle="-", color="gray", lw=0.6))

# Axes
ax.set_xlim(-0.12, 1.12)
ax.set_ylim(0, 110)
ax.set_xlabel("Image customisability  [0 = fixed colour / 1 = fully image-driven]",
              fontsize=11)
ax.set_ylabel("Efficiency retention relative to uncoloured baseline (%)", fontsize=11)
ax.set_title("Technology gap analysis: customisability vs. efficiency retention\n"
             "for coloured photovoltaic modules", fontsize=12)

# X-axis ticks
ax.set_xticks([0, 0.25, 0.5, 0.75, 1.0])
ax.set_xticklabels(["0\n(no customisation)", "0.25", "0.50", "0.75",
                     "1.0\n(fully customisable)"])

# Legend — bubble size
legend_elements = [
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#2196F3",
           markeredgecolor="#1a237e", markeredgewidth=1.8,
           markersize=np.sqrt(320) * 0.6, label="Hotspot risk addressed"),
    Line2D([0], [0], marker="o", color="w", markerfacecolor="#9E9E9E",
           markeredgecolor="black", markeredgewidth=0.5,
           markersize=np.sqrt(120) * 0.6, label="Hotspot risk not addressed"),
    Line2D([0], [0], linestyle="--", color="#BDBDBD", lw=1.2,
           label="Typical trade-off frontier"),
]
ax.legend(handles=legend_elements, loc="lower left", fontsize=8.5,
          framealpha=0.92, edgecolor="#BDBDBD")

ax.grid(True, alpha=0.15)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()
out_png = FIG / "Fig11_gap_analysis.png"
plt.savefig(out_png)
plt.savefig(FIG / "Fig11_gap_analysis.pdf")
plt.close()
print(f"✓ Saved Fig11_gap_analysis → {out_png}")

print("\n── Gap analysis summary ──")
print("Dot-pattern algorithm occupies the upper-right + hotspot-safe region:")
print("  Customisability:    ~0.95 (fully image-driven dot placement)")
print("  Efficiency retention: 76–87%  (mean ~82%)  vs. full-print 11.7%")
print("  Hotspot addressed:  YES — uniform CCR per cell by design")
print("  No other technology simultaneously achieves all three.")

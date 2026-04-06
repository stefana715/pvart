"""
10_pvart_case_taxonomy.py
Section 6.2 support: taxonomy of global PV art cases

Reads image filenames from data/pv_art_cases/, assigns pre-coded classifications
(to be manually corrected), computes summary statistics, and generates:
  - data/extracted_descriptors/pvart_case_taxonomy.csv
  - figures/Fig10_pvart_taxonomy.png
"""

import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
FIG  = ROOT / "figures"
FIG.mkdir(exist_ok=True)

plt.rcParams.update({
    'font.family': 'serif', 'font.size': 11, 'figure.dpi': 300,
    'savefig.dpi': 300, 'savefig.bbox': 'tight',
})

# ---------------------------------------------------------------------------
# Pre-coded taxonomy
# Columns: filename, name_label, Category, PV_technology, Coloring_method,
#          Scale, Hotspot_addressed, Image_customizable
# ---------------------------------------------------------------------------
TAXONOMY = [
    # filename                        label                           Category              PV_tech    Coloring_method    Scale    HS_addr  Img_cust
    ("40_07.jpg",                     "CetisPV Heritage",            "facade",             "c-Si",    "printed",         "large", "yes",   "yes"),
    ("45_nk020.jpg",                  "Onyx Solar facade",           "facade",             "thin_film","structural_color","large","no",    "no"),
    ("49_group-3-0.jpg",              "Solaxess facade panel",       "facade",             "c-Si",    "colored_glass",   "medium","no",    "no"),
    ("800px-Mullberg.jpg",            "Mullberg chapel BIPV",        "facade",             "c-Si",    "no_color",        "medium","no",    "no"),
    ("art_solarsail01.jpg",           "Solar Sail sculpture",        "sculpture",          "c-Si",    "structural_color","small", "no",    "no"),
    ("art_solarsail03.jpg",           "Solar Sail detail",           "sculpture",          "c-Si",    "structural_color","small", "no",    "no"),
    ("coloured-solar-panels-500x500.webp","Coloured panel array",    "ground_installation","c-Si",    "colored_glass",   "medium","no",    "no"),
    ("LoopPh-Sonumbra-03.jpg",        "Sonumbra (Loop.pH)",          "public_art",         "OPV",     "no_color",        "small", "unknown","no"),
    ("pv_system.png",                 "Generic PV system",           "ground_installation","c-Si",    "no_color",        "large", "no",    "no"),
    ("pvart_case_art_01.png",         "PV art installation A",       "public_art",         "c-Si",    "printed",         "small", "unknown","yes"),
    ("pvart_case_art_02.png",         "PV art installation B",       "public_art",         "c-Si",    "printed",         "small", "unknown","yes"),
    ("pvart_case_art_03.png",         "PV art installation C",       "public_art",         "c-Si",    "structural_color","small", "unknown","no"),
    ("pvart_case_building.png",       "BIPV office building",        "facade",             "c-Si",    "colored_glass",   "large", "no",    "no"),
    ("pvart_case_canopy_render.png",  "PV canopy render",            "canopy",             "c-Si",    "colored_glass",   "medium","no",    "no"),
    ("pvart_case_colored_panels.jpg", "Coloured panel mosaic",       "facade",             "c-Si",    "colored_glass",   "medium","no",    "no"),
    ("pvart_case_facade_01.png",      "Patterned facade BIPV",       "facade",             "c-Si",    "printed",         "large", "yes",   "yes"),
    ("pvart_case_facade_02.png",      "BIPV facade gradient",        "facade",             "c-Si",    "structural_color","large", "no",    "no"),
    ("pvart_case_installation_01.png","PV ground installation",      "ground_installation","c-Si",    "printed",         "medium","unknown","yes"),
    ("pvart_case_park.png",           "Park PV canopy",              "canopy",             "c-Si",    "no_color",        "large", "no",    "no"),
    ("pvart_case_sculpture.png",      "PV sculpture landmark",       "sculpture",          "c-Si",    "structural_color","small", "no",    "no"),
    ("Sarah_Hall_grassvalley1.jpg",   "Sarah Hall – Grass Valley",   "window",             "c-Si",    "mixed",           "medium","unknown","yes"),
    ("Sarah_Hall_regent1.jpg",        "Sarah Hall – Regent",         "window",             "c-Si",    "mixed",           "medium","unknown","yes"),
    ("solar-gate2.jpg",               "Solar Gate public art",       "public_art",         "c-Si",    "printed",         "medium","unknown","yes"),
    ("SW11.jpg",                      "Dot-pattern lab M-11",        "facade",             "c-Si",    "printed",         "small", "yes",   "yes"),
    ("SW13.jpg",                      "Dot-pattern lab M-13",        "facade",             "c-Si",    "printed",         "small", "yes",   "yes"),
    ("zadar_suncanik1.jpg",           "Zadar Sun Organ 1",           "public_art",         "c-Si",    "no_color",        "small", "no",    "no"),
    ("zadar_suncanik2.jpg",           "Zadar Sun Organ 2",           "public_art",         "c-Si",    "no_color",        "small", "no",    "no"),
]

cols = ["filename", "Name", "Category", "PV_technology", "Coloring_method",
        "Scale", "Hotspot_addressed", "Image_customizable"]
df = pd.DataFrame(TAXONOMY, columns=cols)

out_csv = DATA / "extracted_descriptors" / "pvart_case_taxonomy.csv"
df.to_csv(out_csv, index=False)
print(f"✓ Saved taxonomy CSV → {out_csv}  ({len(df)} cases)")

# ---------------------------------------------------------------------------
# Summary statistics
# ---------------------------------------------------------------------------
print("\n── Category distribution ──")
print(df["Category"].value_counts().to_string())
print("\n── Coloring method ──")
print(df["Coloring_method"].value_counts().to_string())
print("\n── Scale ──")
print(df["Scale"].value_counts().to_string())
print("\n── Hotspot addressed ──")
print(df["Hotspot_addressed"].value_counts().to_string())
print("\n── Image customizable ──")
print(df["Image_customizable"].value_counts().to_string())

# ---------------------------------------------------------------------------
# Figure: stacked bar chart — Category × Coloring_method
# ---------------------------------------------------------------------------
cat_order   = ["facade", "public_art", "ground_installation", "canopy", "sculpture", "window"]
color_order = ["printed", "structural_color", "colored_glass", "mixed", "no_color"]
color_map   = {
    "printed":          "#2196F3",
    "structural_color": "#9C27B0",
    "colored_glass":    "#FF9800",
    "mixed":            "#4CAF50",
    "no_color":         "#9E9E9E",
}

pivot = (df.groupby(["Category", "Coloring_method"])
           .size()
           .unstack(fill_value=0)
           .reindex(index=cat_order, columns=color_order, fill_value=0))

fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# (a) stacked bar — Category × Coloring_method
bottom = np.zeros(len(cat_order))
ax = axes[0]
for cm in color_order:
    vals = pivot[cm].values.astype(float)
    ax.bar(cat_order, vals, bottom=bottom, color=color_map[cm],
           alpha=0.88, edgecolor="white", linewidth=0.5, label=cm.replace("_", " "))
    for i, (v, b) in enumerate(zip(vals, bottom)):
        if v > 0:
            ax.text(i, b + v / 2, str(int(v)), ha="center", va="center",
                    fontsize=8, color="white", fontweight="bold")
    bottom += vals

ax.set_xlabel("Application category")
ax.set_ylabel("Number of cases")
ax.set_title("(a) PV art cases by category and colouring method\n(n = 27)")
ax.legend(title="Colouring method", fontsize=8, title_fontsize=8,
          loc="upper right", framealpha=0.9)
ax.set_ylim(0, bottom.max() + 1.5)
ax.tick_params(axis="x", labelrotation=20)
ax.grid(True, alpha=0.15, axis="y")

# (b) grouped bar — Hotspot_addressed × Image_customizable
hs_vals   = df["Hotspot_addressed"].value_counts().reindex(["yes", "no", "unknown"], fill_value=0)
cust_vals = df["Image_customizable"].value_counts().reindex(["yes", "no"], fill_value=0)

ax2 = axes[1]
x1 = np.array([0, 1, 2])
x2 = np.array([3.5, 4.5])

bars1 = ax2.bar(x1, hs_vals.values, color=["#4CAF50", "#F44336", "#9E9E9E"],
                alpha=0.85, edgecolor="black", linewidth=0.4, width=0.6)
bars2 = ax2.bar(x2, cust_vals.values, color=["#2196F3", "#FF9800"],
                alpha=0.85, edgecolor="black", linewidth=0.4, width=0.6)

for bar in list(bars1) + list(bars2):
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width() / 2, h + 0.2, str(int(h)),
             ha="center", va="bottom", fontsize=9, fontweight="bold")

ax2.set_xticks(list(x1) + list(x2))
ax2.set_xticklabels(["HS: yes", "HS: no", "HS: unk.",
                      "Cust.: yes", "Cust.: no"])
ax2.set_ylabel("Number of cases")
ax2.set_title("(b) Hotspot risk addressed and\nimage customizability (n = 27)")
ax2.axvline(2.75, color="gray", linewidth=0.8, linestyle="--", alpha=0.5)
ax2.grid(True, alpha=0.15, axis="y")
ax2.set_ylim(0, max(hs_vals.max(), cust_vals.max()) + 3)

plt.tight_layout()
out_fig = FIG / "Fig10_pvart_taxonomy.png"
plt.savefig(out_fig)
plt.savefig(FIG / "Fig10_pvart_taxonomy.pdf")
plt.close()
print(f"\n✓ Saved Fig10_pvart_taxonomy → {out_fig}")

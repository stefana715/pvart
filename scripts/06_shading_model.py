"""
06_shading_model.py
Section 5.4: Effective shading coefficient model — Isc = Isc₀ × (1 - α × CCR)

Generates:
  - figures/Fig6_shading_model.png
  - data/extracted_descriptors/shading_model_fit.json
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

lab  = pd.read_csv(DATA / "raw_measurements" / "lab_scale_SERIS.csv")
shade = pd.read_csv(DATA / "extracted_descriptors" / "shading_coefficients.csv")

ISC0 = 8.05  # baseline

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

# (a) Isc vs CCR with model lines
x_mod = np.linspace(0, 105, 200)

for alpha_val, ls, lbl in [(0.75, "--", "α=0.75"), (0.80, "-", "α=0.80 (dot pattern mean)"),
                            (0.90, ":", "α=0.90"), (1.00, "-.", "α=1.00 (opaque)")]:
    y_mod = ISC0 * (1 - alpha_val * x_mod / 100)
    ax1.plot(x_mod, y_mod, ls, color="gray", alpha=0.5, lw=1, label=lbl)

method_style = {
    "Dot pattern":   ("o", "#2196F3"),
    "Colored glass":  ("D", "#FF9800"),
    "Full print":     ("^", "#F44336"),
    "Large dots":     ("v", "#9C27B0"),
}

for _, row in shade.iterrows():
    m = row["Method"]
    marker, color = method_style.get(m, ("x", "gray"))
    ax1.scatter(row["Color_Coverage_pct"], row["Isc_A"],
                c=color, s=90, marker=marker, edgecolors="k", lw=0.4, zorder=5)
    ofs_y = 0.2 if row["Module"] not in ["M-2","M-6"] else -0.3
    ax1.annotate(row["Module"], (row["Color_Coverage_pct"], row["Isc_A"]),
                 textcoords="offset points", xytext=(7, ofs_y*25), fontsize=7.5)

# Baseline point
ax1.scatter(0, ISC0, c="#4CAF50", s=100, marker="s", edgecolors="k", lw=0.5, zorder=5)
ax1.annotate("M-5", (0, ISC0), textcoords="offset points", xytext=(7, 5), fontsize=7.5)

ax1.set_xlabel("Color Coverage Ratio, CCR (%)")
ax1.set_ylabel("Short-circuit Current, Isc (A)")
ax1.set_title("(a) Isc vs. CCR with effective shading model")
ax1.legend(fontsize=7.5, loc="upper right")
ax1.set_xlim(-5, 108)
ax1.set_ylim(0, 9)
ax1.grid(True, alpha=0.15)

# (b) α by module
dot_shade = shade[shade["Method"] == "Dot pattern"].sort_values(
    "Effective_Shading_Coefficient_alpha"
)
other_shade = shade[shade["Method"] != "Dot pattern"]

all_mods = list(dot_shade["Module"]) + list(other_shade["Module"])
all_alpha = list(dot_shade["Effective_Shading_Coefficient_alpha"]) + \
            list(other_shade["Effective_Shading_Coefficient_alpha"])
all_colors = ["#2196F3"]*len(dot_shade) + ["#F44336"]*len(other_shade)

ax2.barh(range(len(all_mods)), all_alpha, color=all_colors, alpha=0.85,
         edgecolor="black", linewidth=0.4)
ax2.set_yticks(range(len(all_mods)))
ax2.set_yticklabels(all_mods)
ax2.axvline(np.mean(dot_shade["Effective_Shading_Coefficient_alpha"]),
            color="#2196F3", ls="--", lw=1.5, alpha=0.7,
            label=f'Dot pattern mean = {np.mean(dot_shade["Effective_Shading_Coefficient_alpha"]):.3f}')
ax2.axvline(1.0, color="red", ls="-.", lw=1, alpha=0.5, label="α=1 (opaque)")
ax2.set_xlabel("Effective Shading Coefficient α")
ax2.set_title("(b) α per module (lower = more light transmitted)")
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.15, axis="x")
ax2.set_xlim(0.5, 1.15)

plt.tight_layout()
plt.savefig(FIG / "Fig6_shading_model.png")
plt.savefig(FIG / "Fig6_shading_model.pdf")
plt.close()
print("✓ Saved Fig6_shading_model")

# Save model parameters
alpha_dot = shade.loc[shade["Method"]=="Dot pattern", "Effective_Shading_Coefficient_alpha"]
model_fit = {
    "model": "Isc = Isc_baseline × (1 - α × CCR/100)",
    "Isc_baseline_A": ISC0,
    "alpha_dot_mean": round(float(alpha_dot.mean()), 3),
    "alpha_dot_std": round(float(alpha_dot.std()), 3),
    "interpretation": "Each dot blocks ~80% of light in its area; "
                      "~20% reaches cells via edge diffraction/scattering",
}
with open(DATA / "extracted_descriptors" / "shading_model_fit.json", "w") as f:
    json.dump(model_fit, f, indent=2)
print(f"  α_dot = {model_fit['alpha_dot_mean']} ± {model_fit['alpha_dot_std']}")

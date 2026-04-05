"""
05_loss_decomposition.py
Section 5.3: Optical loss decomposition — Isc dominates, FF slightly improves

Generates:
  - figures/Fig5_loss_decomposition.png
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

df = pd.read_csv(DATA / "extracted_descriptors" / "loss_decomposition.csv")

fig, ax = plt.subplots(figsize=(10, 5.5))

x = np.arange(len(df))
w = 0.22

b1 = ax.bar(x - w, df["Isc_Loss_pct"], w, color="#2196F3", alpha=0.85,
            label="Photocurrent loss (ΔIsc/Isc)")
b2 = ax.bar(x,     df["Voc_Loss_pct"], w, color="#FF9800", alpha=0.85,
            label="Voltage loss (ΔVoc/Voc)")
b3 = ax.bar(x + w, df["FF_Change_pct"], w, color="#4CAF50", alpha=0.85,
            label="Fill factor change (ΔFF/FF)")

ax.scatter(x, df["Total_Efficiency_Loss_pct"], color="red", marker="D",
           s=60, zorder=5, label="Total relative loss")

ax.set_xticks(x)
ax.set_xticklabels(df["Module"])
ax.set_xlabel("Module")
ax.set_ylabel("Relative Change (%)")
ax.set_title("Optical loss decomposition: photocurrent loss dominates efficiency reduction")
ax.axhline(0, color="black", lw=0.5)
ax.legend(fontsize=8, loc="upper left")
ax.grid(True, alpha=0.15, axis="y")

plt.tight_layout()
plt.savefig(FIG / "Fig5_loss_decomposition.png")
plt.savefig(FIG / "Fig5_loss_decomposition.pdf")
plt.close()
print("✓ Saved Fig5_loss_decomposition")

# Key stats
dot_mask = df["Module"].isin(["M-1","M-2","M-3","M-4","M-6","M-9"])
print(f"\nDot-pattern modules (mean):")
print(f"  Isc loss: {df.loc[dot_mask, 'Isc_Loss_pct'].mean():.1f}%")
print(f"  Voc loss: {df.loc[dot_mask, 'Voc_Loss_pct'].mean():.1f}%")
print(f"  FF change: {df.loc[dot_mask, 'FF_Change_pct'].mean():.1f}% (negative = improvement)")
print(f"  → Efficiency loss is ~{df.loc[dot_mask, 'Isc_Loss_pct'].mean() / df.loc[dot_mask, 'Total_Efficiency_Loss_pct'].mean() * 100:.0f}% attributable to photocurrent reduction")

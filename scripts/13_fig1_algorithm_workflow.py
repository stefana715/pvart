"""
13_fig1_algorithm_workflow.py
Generate Fig1_algorithm_workflow.png — 7-step algorithm flowchart
Applied Energy figure style: 300 Dpi, serif font, white background, 2-column width

Source images:
  data/pattern_images/algorithm_steps/step4_pattern_overview.jpg
  data/pattern_images/algorithm_steps/step5_energy_oriented.jpg
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
import matplotlib.patheffects as pe
from PIL import Image
import numpy as np
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
IMG  = ROOT / "data" / "pattern_images" / "algorithm_steps"
FIG  = ROOT / "figures"
FIG.mkdir(exist_ok=True)

# ── Applied Energy typography settings ──────────────────────────────────────
plt.rcParams.update({
    "font.family":      "serif",
    "font.serif":       ["Times New Roman", "DejaVu Serif"],
    "font.size":        8,
    "axes.labelsize":   8,
    "figure.dpi":       300,
    "savefig.dpi":      300,
    "savefig.bbox":     "tight",
    "savefig.facecolor":"white",
})

# ── Load source images ───────────────────────────────────────────────────────
src4 = np.array(Image.open(IMG / "step4_pattern_overview.jpg").convert("RGB"))
src5 = np.array(Image.open(IMG / "step5_energy_oriented.jpg").convert("RGB"))

# step4 layout: 3 pattern columns (left) + Marilyn (centre) + 3×4 outputs (right)
# Approximate crop positions (as fractions of image width/height)
h4, w4 = src4.shape[:2]
h5, w5 = src5.shape[:2]

def crop(img, y0f, y1f, x0f, x1f):
    h, w = img.shape[:2]
    return img[int(h*y0f):int(h*y1f), int(w*x0f):int(w*x1f)]

# Thumbnail crops from step4
thumb_input   = crop(src4, 0.05, 0.95, 0.38, 0.52)   # Marilyn Monroe input image
thumb_pattern = crop(src4, 0.02, 0.98, 0.00, 0.35)   # pattern tile library (3 cols)
thumb_output  = crop(src4, 0.02, 0.50, 0.54, 0.82)   # top-right output samples

# Thumbnail crops from step5 (3 panels side by side)
s5_w3 = w5 // 3
thumb_heritage = src5[:, 0         : s5_w3,     :]   # Heritage dots (left)
thumb_modern   = src5[:, s5_w3     : 2*s5_w3,   :]   # Modern dots  (centre)
thumb_nature   = src5[:, 2*s5_w3   :,           :]   # Nature dots  (right)

# Synthesised thumbnails for steps 2 and 3 (schematic, no source photo)
def make_grid_thumb(size=80):
    """Simple cell-grid schematic."""
    img = np.ones((size, size, 3), dtype=np.uint8) * 255
    # draw 4×4 grid
    step = size // 4
    for k in range(1, 4):
        img[k*step-1:k*step+1, :] = 50
        img[:, k*step-1:k*step+1] = 50
    # highlight one cell in blue
    img[step:2*step, step:2*step] = [210, 230, 255]
    return img

def make_ccr_thumb(size=80, ccr=0.264):
    """Filled rectangle showing CCR level."""
    img = np.ones((size, size, 3), dtype=np.uint8) * 255
    filled = int(size * ccr)
    img[:, :filled] = [30, 100, 200]
    # label line
    img[size//2-1:size//2+1, :] = 180
    return img

thumb_grid = make_grid_thumb(80)
thumb_ccr  = make_ccr_thumb(80, ccr=0.264)

# ── Step definitions ─────────────────────────────────────────────────────────
STEPS = [
    {
        "num":   "1",
        "title": "Image\nAcquisition",
        "desc":  "Import source image,\nresize to module\nresolution",
        "thumb": thumb_input,
        "color": "#1565C0",
    },
    {
        "num":   "2",
        "title": "Cell Grid\nRegistration",
        "desc":  "Map cell boundaries;\nidentify active area\nper cell",
        "thumb": thumb_grid,
        "color": "#1565C0",
    },
    {
        "num":   "3",
        "title": "CCR\nSpecification",
        "desc":  "Set target CCR\n(e.g. 26.48%);\ndefine loss budget",
        "thumb": thumb_ccr,
        "color": "#1565C0",
    },
    {
        "num":   "4",
        "title": "Grey → Dot\nDensity Mapping",
        "desc":  "Map pixel intensity\nto local dot density\nvia transfer function",
        "thumb": thumb_pattern,
        "color": "#6A1B9A",
    },
    {
        "num":   "5",
        "title": "Per-Cell CCR\nEnforcement",
        "desc":  "Adjust dot count\nper cell → PUI → 0;\nhotspot-safe design",
        "thumb": thumb_heritage,
        "color": "#B71C1C",
    },
    {
        "num":   "6",
        "title": "Dot Geometry\nOptimisation",
        "desc":  "Tune dot size & SF;\nenergy / graphic /\nbalanced modes",
        "thumb": thumb_modern,
        "color": "#E65100",
    },
    {
        "num":   "7",
        "title": "Output &\nPUI Verification",
        "desc":  "Export pattern mask;\ncheck PUI < 5%,\nCCR within ±1%",
        "thumb": thumb_nature,
        "color": "#2E7D32",
    },
]

# ── Figure layout ────────────────────────────────────────────────────────────
N  = len(STEPS)
FW = 18.0          # figure width  (inches) — 2-column Applied Energy
FH = 4.6           # figure height (inches)

fig = plt.figure(figsize=(FW, FH), facecolor="white")
ax  = fig.add_axes([0, 0, 1, 1], facecolor="white")
ax.set_xlim(0, FW)
ax.set_ylim(0, FH)
ax.axis("off")

# Column positions
PAD   = 0.28          # left/right page margin
GAP   = 0.18          # gap between boxes
BOX_W = (FW - 2*PAD - (N-1)*GAP) / N   # width of each box
BOX_H = 3.7           # box height
BOX_Y = (FH - BOX_H) / 2               # vertical centre

THUMB_H_IN = 1.45     # thumbnail inset height (inches)
THUMB_Y_IN = 0.58     # thumbnail y position from box bottom

def ax_img(ax_main, img_arr, x, y, w, h):
    """Embed an image array at (x,y) with size (w,h) in figure inches."""
    ax_sub = fig.add_axes([x/FW, y/FH, w/FW, h/FH])
    ax_sub.imshow(img_arr, aspect="auto", interpolation="lanczos")
    ax_sub.axis("off")
    return ax_sub

for i, step in enumerate(STEPS):
    bx = PAD + i * (BOX_W + GAP)
    by = BOX_Y
    col = step["color"]

    # ── box shadow (slight offset) ───────────────────────────────────────
    shadow = FancyBboxPatch(
        (bx + 0.04, by - 0.04), BOX_W, BOX_H,
        boxstyle="round,pad=0.05",
        linewidth=0,
        facecolor="#CCCCCC",
        alpha=0.45,
        zorder=1,
        transform=ax.transData,
    )
    ax.add_patch(shadow)

    # ── main box ─────────────────────────────────────────────────────────
    box = FancyBboxPatch(
        (bx, by), BOX_W, BOX_H,
        boxstyle="round,pad=0.05",
        linewidth=1.2,
        edgecolor=col,
        facecolor="white",
        zorder=2,
        transform=ax.transData,
    )
    ax.add_patch(box)

    # ── coloured header band ─────────────────────────────────────────────
    header = FancyBboxPatch(
        (bx, by + BOX_H - 0.68), BOX_W, 0.68,
        boxstyle="round,pad=0.05",
        linewidth=0,
        facecolor=col,
        alpha=0.92,
        zorder=3,
        transform=ax.transData,
    )
    ax.add_patch(header)

    # ── step circle ──────────────────────────────────────────────────────
    circ_x = bx + 0.30
    circ_y = by + BOX_H - 0.34
    circle = plt.Circle(
        (circ_x, circ_y), 0.22,
        color="white", zorder=5, transform=ax.transData,
    )
    ax.add_patch(circle)
    ax.text(
        circ_x, circ_y, step["num"],
        ha="center", va="center",
        fontsize=11, fontweight="bold", color=col, zorder=6,
        transform=ax.transData,
    )

    # ── title text ───────────────────────────────────────────────────────
    ax.text(
        bx + BOX_W * 0.62, by + BOX_H - 0.34,
        step["title"],
        ha="center", va="center",
        fontsize=7.5, fontweight="bold", color="white",
        linespacing=1.3, zorder=6,
        transform=ax.transData,
    )

    # ── thumbnail ────────────────────────────────────────────────────────
    th_x = bx + 0.10
    th_y = by + THUMB_Y_IN
    th_w = BOX_W - 0.20
    th_h = THUMB_H_IN
    ax_img(ax, step["thumb"], th_x, th_y, th_w, th_h)

    # thin border around thumbnail
    rect = plt.Rectangle(
        (th_x, th_y), th_w, th_h,
        linewidth=0.6, edgecolor="#BBBBBB", facecolor="none",
        zorder=7, transform=ax.transData,
    )
    ax.add_patch(rect)

    # ── description text ─────────────────────────────────────────────────
    ax.text(
        bx + BOX_W / 2, by + 0.32,
        step["desc"],
        ha="center", va="center",
        fontsize=6.5, color="#333333",
        linespacing=1.4, zorder=6,
        transform=ax.transData,
    )

    # ── arrow to next box ────────────────────────────────────────────────
    if i < N - 1:
        arr_x = bx + BOX_W + 0.01
        arr_y = by + BOX_H / 2
        ax.annotate(
            "",
            xy=(arr_x + GAP - 0.01, arr_y),
            xytext=(arr_x, arr_y),
            arrowprops=dict(
                arrowstyle="-|>",
                color="#555555",
                lw=1.4,
                mutation_scale=12,
            ),
            zorder=8,
            transform=ax.transData,
        )

# ── novelty callouts ─────────────────────────────────────────────────────────
def callout(ax, x, y, text, color):
    ax.annotate(
        text,
        xy=(x, y - BOX_Y - 0.05),
        xytext=(x, -0.05),
        xycoords="data",
        textcoords="data",
        fontsize=6.2,
        color=color,
        ha="center",
        va="top",
        fontweight="bold",
        arrowprops=dict(arrowstyle="-", color=color, lw=0.8, linestyle="dashed"),
        zorder=9,
        transform=ax.transData,
        annotation_clip=False,
    )

# Mark steps 5, 6, 7 with "[N] novelty" flags (inline below box)
novelties = {
    4: ("[N] PUI→0\n(hotspot-safe)", "#B71C1C"),
    5: ("[N] ED/SF control\n(efficiency gain)", "#E65100"),
    6: ("[N] Descriptor\nverification", "#2E7D32"),
}
for idx, (label, col) in novelties.items():
    step = STEPS[idx]
    bx = PAD + idx * (BOX_W + GAP)
    ax.text(
        bx + BOX_W / 2,
        BOX_Y - 0.18,
        label,
        ha="center", va="top",
        fontsize=6.2, color=col, fontweight="bold",
        linespacing=1.3,
        zorder=9,
        transform=ax.transData,
    )
    # small triangle pointer up
    tri_x = bx + BOX_W / 2
    tri_y = BOX_Y
    ax.annotate(
        "",
        xy=(tri_x, tri_y),
        xytext=(tri_x, BOX_Y - 0.12),
        arrowprops=dict(arrowstyle="-|>", color=col, lw=0.8, mutation_scale=6),
        zorder=9,
        transform=ax.transData,
    )

# ── caption ─────────────────────────────────────────────────────────────────
ax.text(
    FW / 2, 0.08,
    "Fig. 1. Seven-stage dot-pattern algorithm workflow. "
    "Thumbnails (Steps 1, 4–7) derived from actual algorithm output images. "
    "Steps 5–7 highlight the three novelty contributions of this work.",
    ha="center", va="bottom",
    fontsize=6.8, color="#444444", style="italic",
    transform=ax.transData,
)

# ── save ─────────────────────────────────────────────────────────────────────
out = FIG / "Fig1_algorithm_workflow.png"
plt.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")
plt.savefig(FIG / "Fig1_algorithm_workflow.pdf", bbox_inches="tight", facecolor="white")
plt.close()
print(f"✓ Saved {out}  ({out.stat().st_size//1024} KB)")

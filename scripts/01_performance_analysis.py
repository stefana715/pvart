"""
SCI Paper Data Analysis & Visualization Suite
Paper: Image-based Dot Pattern Enhancement Algorithm for Colored PV Modules
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.gridspec import GridSpec
import os

# Create output directory
os.makedirs('/home/claude/work/figures', exist_ok=True)

# Set publication-quality defaults
plt.rcParams.update({
    'font.family': 'serif',
    'font.serif': ['Times New Roman', 'DejaVu Serif'],
    'font.size': 11,
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 9,
    'figure.dpi': 300,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight',
    'axes.linewidth': 0.8,
    'lines.linewidth': 1.5,
})

# ==================== RAW DATA ====================
# Lab-scale (SERIS)
modules = ['M-1','M-2','M-3','M-4','M-5','M-5C','M-6','M-7','M-8','M-9']
coverage = [26.48, 26.48, 18.66, 26.48, 0, 26.48, 26.48, 100, 61.51, 26.48]
eff = [13.64, 12.73, 14.50, 13.15, 16.63, 11.98, 13.13, 1.95, 7.29, 13.50]
loss = [18.00, 23.47, 12.64, 20.93, 0, 27.99, 21.09, 88.27, 56.15, 18.86]
Pmax = [200.95, 187.52, 213.67, 193.83, 245.0, 176.62, 193.47, 28.80, 107.34, 198.80]
Isc = [6.61, 6.14, 6.96, 6.30, 8.05, 5.73, 6.12, 0.92, 3.37, 6.44]
Voc = [39.35, 39.18, 39.41, 39.24, 39.73, 39.18, 39.64, 36.72, 38.66, 39.49]

# Product-scale
eg_names = ['EG-PF1','EG-PF2','EG-PF3','EG-PF4']
eg_eff = [12.73, 14.50, 13.15, 13.64]
eg_Pmax = [187.52, 213.67, 193.83, 200.95]
eg_FF = [81.79, 81.94, 82.39, 81.63]
eg_TkI = [-0.05, -0.04, -0.06, -0.04]
eg_TkU = [-0.18, -0.21, -0.19, -0.20]
eg_Voc = [39.18, 39.41, 39.24, 39.35]
eg_Isc = [6.14, 6.96, 6.30, 6.61]

# Full-size product relative loss
eg_fullsize_rl = [27.59, 27.56, 27.70]
seris_rl = 43.0

# ==================== FIGURE 1: Coverage vs Efficiency ====================
fig, ax1 = plt.subplots(figsize=(8, 5))

# Same-image series (M-5, M-9, M-8, M-7)
cov_same = [0, 26.48, 61.51, 100]
eff_same = [16.63, 13.50, 7.29, 1.95]

# Fit linear regression
z = np.polyfit(cov_same, eff_same, 1)
p_lin = np.poly1d(z)
x_fit = np.linspace(0, 105, 100)
y_fit = p_lin(x_fit)

# Fit quadratic
z2 = np.polyfit(cov_same, eff_same, 2)
p_quad = np.poly1d(z2)
y_fit2 = p_quad(x_fit)

# R² for linear
ss_res = sum((e - p_lin(c))**2 for c, e in zip(cov_same, eff_same))
ss_tot = sum((e - np.mean(eff_same))**2 for e in eff_same)
r2_lin = 1 - ss_res / ss_tot

# R² for quadratic
ss_res2 = sum((e - p_quad(c))**2 for c, e in zip(cov_same, eff_same))
r2_quad = 1 - ss_res2 / ss_tot

# Plot all modules
colors_map = {
    'Dot pattern': '#2196F3', 'Baseline': '#4CAF50', 
    'Color glass': '#FF9800', 'Full print': '#F44336',
    'Large dots': '#9C27B0', 'Small dots': '#00BCD4'
}

methods_lab = ['Dot pattern','Dot pattern','Dot pattern','Dot pattern','Baseline','Color glass','Dot pattern','Full print','Large dots','Small dots']
for i, (c, e, m, name) in enumerate(zip(coverage, eff, methods_lab, modules)):
    color = colors_map.get(m, '#666666')
    marker = 'o' if 'Dot' in m else ('s' if m == 'Baseline' else ('^' if m == 'Full print' else ('D' if m == 'Color glass' else 'v')))
    ax1.scatter(c, e, c=color, s=80, zorder=5, marker=marker, edgecolors='black', linewidth=0.5)
    ax1.annotate(name, (c, e), textcoords="offset points", xytext=(8, 5), fontsize=8, color='#333333')

# Regression lines
ax1.plot(x_fit, y_fit, '--', color='#666666', alpha=0.7, label=f'Linear fit (R²={r2_lin:.4f})')
ax1.plot(x_fit, y_fit2, ':', color='#999999', alpha=0.7, label=f'Quadratic fit (R²={r2_quad:.4f})')

# Shaded regions
ax1.axhspan(12, 15, alpha=0.08, color='blue', label='Dot pattern efficiency range')
ax1.axhline(y=16.63, color='green', linestyle='-.', alpha=0.4, linewidth=0.8)
ax1.text(70, 16.8, 'Baseline (M-5): 16.63%', fontsize=8, color='green', alpha=0.7)

ax1.set_xlabel('Color Coverage (%)')
ax1.set_ylabel('STC Efficiency (%)')
ax1.set_title('(a) Relationship between Color Coverage and Module Efficiency')
ax1.set_xlim(-5, 108)
ax1.set_ylim(0, 18.5)
ax1.legend(loc='upper right', framealpha=0.9)
ax1.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig2_coverage_vs_efficiency.png')
plt.savefig('/home/claude/work/figures/Fig2_coverage_vs_efficiency.pdf')
plt.close()
print("✓ Fig 2: Coverage vs Efficiency saved")

# ==================== FIGURE 2: Optical Loss Decomposition ====================
fig, ax = plt.subplots(figsize=(9, 5))

dot_modules = ['M-1','M-2','M-3','M-4','M-6','M-9','M-5C','M-7','M-8']
baseline_Isc = 8.05
baseline_Voc = 39.73
baseline_FF_val = 245.0 / (39.73 * 8.05) * 100

Isc_losses = []
Voc_losses = []
FF_changes = []
total_losses_decomp = []

for name in dot_modules:
    idx = modules.index(name)
    isc_l = (1 - Isc[idx]/baseline_Isc) * 100
    voc_l = (1 - Voc[idx]/baseline_Voc) * 100
    ff_val = Pmax[idx] / (Voc[idx] * Isc[idx]) * 100
    ff_l = (1 - ff_val/baseline_FF_val) * 100
    Isc_losses.append(isc_l)
    Voc_losses.append(voc_l)
    FF_changes.append(ff_l)
    total_losses_decomp.append(loss[idx])

x = np.arange(len(dot_modules))
width = 0.22

bars1 = ax.bar(x - width, Isc_losses, width, label='Photocurrent loss (ΔIsc/Isc)', color='#2196F3', alpha=0.85)
bars2 = ax.bar(x, Voc_losses, width, label='Voltage loss (ΔVoc/Voc)', color='#FF9800', alpha=0.85)
bars3 = ax.bar(x + width, FF_changes, width, label='Fill factor change (ΔFF/FF)', color='#4CAF50', alpha=0.85)
ax.scatter(x, total_losses_decomp, color='red', marker='D', s=50, zorder=5, label='Total relative efficiency loss')

ax.set_xlabel('Module')
ax.set_ylabel('Relative Change (%)')
ax.set_title('(b) Optical Loss Decomposition: Contribution of Isc, Voc, and FF to Efficiency Loss')
ax.set_xticks(x)
ax.set_xticklabels(dot_modules)
ax.legend(loc='upper left', framealpha=0.9)
ax.grid(True, alpha=0.2, axis='y')
ax.axhline(y=0, color='black', linewidth=0.5)

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig3_loss_decomposition.png')
plt.savefig('/home/claude/work/figures/Fig3_loss_decomposition.pdf')
plt.close()
print("✓ Fig 3: Loss Decomposition saved")

# ==================== FIGURE 3: Effective Shading Factor ====================
fig, ax = plt.subplots(figsize=(7, 5))

# α for each module
dot_mods = ['M-1','M-2','M-3','M-4','M-6','M-9']
alphas = []
coverages_dot = []
for name in dot_mods:
    idx = modules.index(name)
    cov = coverage[idx] / 100
    alpha = (1 - Isc[idx]/baseline_Isc) / cov
    alphas.append(alpha)
    coverages_dot.append(coverage[idx])

# Also for M-7, M-8
special_mods = ['M-7', 'M-8']
special_alphas = []
special_covs = []
for name in special_mods:
    idx = modules.index(name)
    cov = coverage[idx] / 100
    alpha = (1 - Isc[idx]/baseline_Isc) / cov
    special_alphas.append(alpha)
    special_covs.append(coverage[idx])

ax.bar(range(len(dot_mods)), alphas, color='#2196F3', alpha=0.8, label='Dot pattern modules')
ax.bar(range(len(dot_mods), len(dot_mods)+len(special_mods)), special_alphas, color='#F44336', alpha=0.8, label='Full/large print')

ax.set_xticks(range(len(dot_mods)+len(special_mods)))
ax.set_xticklabels(dot_mods + special_mods)
ax.set_ylabel('Effective Shading Coefficient (α)')
ax.set_xlabel('Module')
ax.set_title('(c) Effective Shading Coefficient per Unit Coverage')
ax.axhline(y=1.0, color='red', linestyle='--', alpha=0.5, label='α = 1 (opaque)')
ax.axhline(y=np.mean(alphas), color='blue', linestyle=':', alpha=0.5, label=f'Mean α (dot) = {np.mean(alphas):.3f}')
ax.legend(framealpha=0.9)
ax.grid(True, alpha=0.2, axis='y')
ax.set_ylim(0, 1.1)

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig4_shading_coefficient.png')
plt.savefig('/home/claude/work/figures/Fig4_shading_coefficient.pdf')
plt.close()
print("✓ Fig 4: Shading Coefficient saved")

# ==================== FIGURE 4: Temperature Performance Modeling ====================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

temps = np.arange(25, 76, 1)
colors_eg = ['#2196F3', '#F44336', '#4CAF50', '#FF9800']

# Panel (a): Normalized power vs temperature
for i, (name, tki, tku, pmax) in enumerate(zip(eg_names, eg_TkI, eg_TkU, eg_Pmax)):
    tkP = tki + tku  # approximate power temperature coefficient
    power_norm = [1 + tkP/100 * (T - 25) for T in temps]
    ax1.plot(temps, power_norm, color=colors_eg[i], label=f'{name} (TkP≈{tkP:.2f}%/°C)')

# Add standard module reference
tkP_std = -0.35
power_std = [1 + tkP_std/100 * (T - 25) for T in temps]
ax1.plot(temps, power_std, 'k--', alpha=0.5, label=f'Standard module (TkP={tkP_std}%/°C)')

ax1.set_xlabel('Cell Temperature (°C)')
ax1.set_ylabel('Normalized Power Output (Pmax/Pmax_STC)')
ax1.set_title('(d) Temperature-dependent Power Output')
ax1.legend(loc='lower left', fontsize=8)
ax1.grid(True, alpha=0.2)
ax1.axhline(y=1.0, color='gray', linewidth=0.5, alpha=0.3)
ax1.set_xlim(25, 75)
ax1.set_ylim(0.82, 1.01)

# Panel (b): Annual energy yield comparison (Singapore)
psh = 4.5
days = 365
avg_temps = [35, 45, 55, 65]  # different average module temperatures

yield_data = {}
for name, tki, tku, pmax in zip(eg_names, eg_TkI, eg_TkU, eg_Pmax):
    tkP = tki + tku
    yields = [pmax * (1 + tkP/100 * (T - 25)) * psh * days / 1000 for T in avg_temps]
    yield_data[name] = yields

# Add benchmarks
baseline_yields = [245.0 * (1 + (-0.35)/100 * (T - 25)) * psh * days / 1000 for T in avg_temps]
seris_yields = [165.0 * (1 + (-0.35)/100 * (T - 25)) * psh * days / 1000 for T in avg_temps]

x_pos = np.arange(len(avg_temps))
bar_w = 0.12

for i, name in enumerate(eg_names):
    ax2.bar(x_pos + i*bar_w, yield_data[name], bar_w, color=colors_eg[i], alpha=0.85, label=name)

ax2.bar(x_pos + 4*bar_w, baseline_yields, bar_w, color='#333333', alpha=0.6, label='Uncolored baseline')
ax2.bar(x_pos + 5*bar_w, seris_yields, bar_w, color='#9E9E9E', alpha=0.6, label='SERIS Multi-color')

ax2.set_xlabel('Average Module Temperature (°C)')
ax2.set_ylabel('Estimated Annual Energy Yield (kWh)')
ax2.set_title('(e) Annual Energy Yield Estimation (4.5 PSH/day)')
ax2.set_xticks(x_pos + 2.5*bar_w)
ax2.set_xticklabels([f'{t}°C' for t in avg_temps])
ax2.legend(loc='upper right', fontsize=7, ncol=2)
ax2.grid(True, alpha=0.2, axis='y')

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig5_temperature_analysis.png')
plt.savefig('/home/claude/work/figures/Fig5_temperature_analysis.pdf')
plt.close()
print("✓ Fig 5: Temperature Analysis saved")

# ==================== FIGURE 5: Relative Loss Comparison Bar Chart ====================
fig, ax = plt.subplots(figsize=(8, 5))

# All relative losses
compare_names = ['EG-PF1', 'EG-PF2', 'EG-PF3', 'SERIS\nMulti-color', 'M-5C\n(Color glass)', 'M-7\n(Full print)']
compare_losses = [27.59, 27.56, 27.70, 43.0, 27.99, 88.27]
compare_colors = ['#2196F3', '#2196F3', '#2196F3', '#9E9E9E', '#FF9800', '#F44336']
compare_hatch = ['', '', '', '///', '', 'xxx']

bars = ax.bar(range(len(compare_names)), compare_losses, color=compare_colors, alpha=0.85, edgecolor='black', linewidth=0.5)
for bar, h in zip(bars, compare_hatch):
    if h:
        bar.set_hatch(h)

# Add value labels
for i, (v, name) in enumerate(zip(compare_losses, compare_names)):
    ax.text(i, v + 1.5, f'{v:.1f}%', ha='center', fontsize=10, fontweight='bold')

# Add regions
ax.axhspan(25, 30, alpha=0.08, color='blue')
ax.text(0.5, 28.5, 'Proposed method range', fontsize=8, color='blue', alpha=0.6)

ax.set_xticks(range(len(compare_names)))
ax.set_xticklabels(compare_names, fontsize=9)
ax.set_ylabel('Relative Efficiency Loss (%)')
ax.set_title('(f) Relative Efficiency Loss Comparison Across Coloring Technologies')
ax.set_ylim(0, 100)
ax.grid(True, alpha=0.2, axis='y')

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig6_relative_loss_comparison.png')
plt.savefig('/home/claude/work/figures/Fig6_relative_loss_comparison.pdf')
plt.close()
print("✓ Fig 6: Relative Loss Comparison saved")

# ==================== FIGURE 6: Isc vs Coverage — Shading Model ====================
fig, ax = plt.subplots(figsize=(7, 5))

# All data points
all_cov = [0, 18.66, 26.48, 26.48, 26.48, 26.48, 26.48, 26.48, 61.51, 100]
all_Isc = [8.05, 6.96, 6.61, 6.14, 6.30, 5.73, 6.12, 6.44, 3.37, 0.92]
all_names_isc = ['M-5', 'M-3', 'M-1', 'M-2', 'M-4', 'M-5C', 'M-6', 'M-9', 'M-8', 'M-7']
all_methods = ['Baseline', 'Dot', 'Dot', 'Dot', 'Dot', 'Glass', 'Dot', 'Dot', 'Large', 'Full']

# Theoretical model: Isc = 8.05 * (1 - α * coverage/100)
x_model = np.linspace(0, 105, 100)
for alpha_val, label, ls in [(0.80, 'α=0.80 (typical dot pattern)', '--'), 
                              (0.90, 'α=0.90 (dense print)', ':'),
                              (1.00, 'α=1.00 (fully opaque)', '-.')]:
    y_model = 8.05 * (1 - alpha_val * x_model/100)
    ax.plot(x_model, y_model, ls, color='gray', alpha=0.5, label=label)

# Plot data points
for c, isc, name, method in zip(all_cov, all_Isc, all_names_isc, all_methods):
    color = '#2196F3' if method == 'Dot' else ('#4CAF50' if method == 'Baseline' else ('#FF9800' if method == 'Glass' else ('#F44336' if method == 'Full' else '#9C27B0')))
    marker = 'o' if method == 'Dot' else ('s' if method == 'Baseline' else ('^' if method == 'Full' else ('D' if method == 'Glass' else 'v')))
    ax.scatter(c, isc, c=color, s=80, zorder=5, marker=marker, edgecolors='black', linewidth=0.5)
    offset_y = 0.25 if name not in ['M-2', 'M-6'] else -0.35
    ax.annotate(name, (c, isc), textcoords="offset points", xytext=(8, offset_y*20), fontsize=8)

ax.set_xlabel('Color Coverage (%)')
ax.set_ylabel('Short-circuit Current, Isc (A)')
ax.set_title('(g) Short-circuit Current vs Color Coverage with Shading Model')
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.2)
ax.set_xlim(-5, 108)
ax.set_ylim(0, 9)

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig7_Isc_shading_model.png')
plt.savefig('/home/claude/work/figures/Fig7_Isc_shading_model.pdf')
plt.close()
print("✓ Fig 7: Isc Shading Model saved")

# ==================== FIGURE 7: Radar Chart — Multi-parameter comparison ====================
fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))

categories = ['STC Efficiency\n(%)', 'Fill Factor\n(%)', 'Current Temp.\nStability', 
              'Voltage Temp.\nStability', 'Power Output\n(W, normalized)']
N = len(categories)
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

for i, (name, e, ff, tki, tku, pm) in enumerate(zip(eg_names, eg_eff, eg_FF, eg_TkI, eg_TkU, eg_Pmax)):
    values = [
        e / 16.63 * 100,  # normalized to baseline
        ff,
        (0.07 + tki) / 0.03 * 100,  # lower is better, invert
        (0.22 + tku) / 0.04 * 100,
        pm / 245 * 100,
    ]
    values += values[:1]
    ax.plot(angles, values, 'o-', color=colors_eg[i], linewidth=1.5, label=name, markersize=4)
    ax.fill(angles, values, alpha=0.05, color=colors_eg[i])

ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=9)
ax.set_ylim(0, 100)
ax.set_title('(h) Multi-parameter Performance Comparison\n(Normalized to baseline)', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.0))

plt.tight_layout()
plt.savefig('/home/claude/work/figures/Fig8_radar_comparison.png')
plt.savefig('/home/claude/work/figures/Fig8_radar_comparison.pdf')
plt.close()
print("✓ Fig 8: Radar Comparison saved")

# ==================== Print Summary Stats for Paper ====================
print("\n" + "=" * 60)
print("KEY STATISTICS FOR PAPER")
print("=" * 60)

print(f"\n--- Coverage-Efficiency Regression ---")
print(f"  Linear: η = {z[0]:.4f}×cov + {z[1]:.4f}, R²={r2_lin:.4f}")
print(f"  Quadratic: η = {z2[0]:.6f}×cov² + {z2[1]:.4f}×cov + {z2[2]:.4f}, R²={r2_quad:.4f}")
print(f"  Key finding: Every 10% coverage costs ~{abs(z[0]*10):.2f}% absolute efficiency")

print(f"\n--- Effective Shading Coefficient ---")
print(f"  Dot pattern mean α = {np.mean(alphas):.3f} ± {np.std(alphas):.3f}")
print(f"  Full print α = {special_alphas[0]:.3f}")
print(f"  Key finding: Dot patterns transmit {(1-np.mean(alphas))*100:.1f}% more light per unit coverage vs theory")

print(f"\n--- Optical Loss Decomposition ---")
print(f"  For dot-pattern modules, efficiency loss is dominated by:")
print(f"    Isc (optical/photocurrent) loss: {np.mean(Isc_losses[:6]):.1f}% average")
print(f"    Voc loss: {np.mean(Voc_losses[:6]):.1f}% average")
print(f"    FF change: {np.mean(FF_changes[:6]):.1f}% average (negative = improvement)")

print(f"\n--- Energy Yield (Singapore, 55°C avg) ---")
best_yield = max(yield_data['EG-PF2'])
seris_yield = max(seris_yields)
improvement = (best_yield - seris_yield) / seris_yield * 100
print(f"  Best module (EG-PF2) annual yield: {yield_data['EG-PF2'][2]:.0f} kWh")
print(f"  SERIS Multi-color annual yield: {seris_yields[2]:.0f} kWh")
print(f"  Improvement: +{improvement:.0f}%")

print(f"\nAll figures saved to /home/claude/work/figures/")

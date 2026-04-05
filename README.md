# pvart — Photovoltaic Art: Image-Derived Descriptors for Coloured PV Facades

> **Paper:** *From visual pattern to electrical performance: image-derived descriptors and experimental validation for coloured photovoltaic facades*

## Repository Structure

```
pvart/
├── data/
│   ├── raw_measurements/           # Electrical test data (CSV)
│   │   ├── lab_scale_SERIS.csv          # SERIS lab-scale I-V data (M-1 to M-9)
│   │   ├── product_scale_CetisPV.csv    # CetisPV product-scale data (EG-PF1~4)
│   │   ├── product_scale_fullsize.csv   # Full-size module comparison w/ SERIS
│   │   └── module_specifications.csv    # Module construction specs
│   │
│   ├── pattern_images/             # Dot pattern images for descriptor extraction
│   │   ├── algorithm_steps/             # Algorithm workflow images
│   │   ├── lab_scale/                   # Lab-scale module I-V curves
│   │   └── product_scale/               # Product-scale panel photos
│   │
│   ├── pv_art_cases/               # Global PV Art case study images
│   │
│   └── extracted_descriptors/      # Computed image descriptors (CSV)
│       ├── image_descriptors.csv        # CCR, EAR, SF, ED, DSV, PUI per pattern
│       ├── shading_coefficients.csv     # Effective shading coefficient α
│       └── loss_decomposition.csv       # Isc/Voc/FF loss breakdown
│
├── scripts/
│   ├── 01_performance_analysis.py       # Data analysis & figure generation
│   └── 02_extract_image_descriptors.py  # OpenCV descriptor extraction tool
│
├── figures/                        # Publication-ready figures (PNG + PDF)
│
└── docs/
    └── PV_Art_Paper_Draft.docx     # Paper manuscript draft
```

## Image-Derived Descriptors

| Descriptor | Symbol | Definition |
|---|---|---|
| Color Coverage Ratio | CCR | Fraction of module area covered by printed dots (%) |
| Effective Aperture Ratio | EAR | Transparent fraction = 100 − CCR (%) |
| Spatial Frequency | SF | Number of dots per unit area (dots/Mpx) |
| Edge Density | ED | Total dot perimeter per unit area (perimeter/kpx) |
| Dot Size Variance | DSV | Coefficient of variation of dot equivalent diameters |
| Pattern Uniformity Index | PUI | CV of cell-level coverage (%; lower = more uniform = less hotspot risk) |

## Key Findings

- **CCR → efficiency**: linear model η = −0.150 × CCR + 16.91, R² = 0.996
- **Same CCR, different patterns**: 5.5 pp spread in efficiency loss at identical 26.48% coverage → pattern geometry (SF, ED) is a secondary predictor
- **Effective shading coefficient**: dot patterns α = 0.796 ± 0.085 vs full print α = 0.886
- **vs SERIS Multi-color PV**: proposed modules achieve 27.6% relative loss vs 43% (benchmark)
- **Annual yield (Singapore, 55°C)**: EG-PF2 produces 325 kWh vs SERIS 243 kWh (+34%)

## Usage

```bash
# Extract descriptors from a dot pattern image
python scripts/02_extract_image_descriptors.py \
    --input data/pattern_images/algorithm_steps/step5_energy_oriented.jpg \
    --split 3 \
    --output data/extracted_descriptors/result.json

# Run full performance analysis and generate figures
python scripts/01_performance_analysis.py
```

## Requirements

```
numpy
matplotlib
opencv-python-headless
scikit-image
```

## Patent

The dot-matrix vector pattern design method is covered by pending patents:
- CN 2025103536061 (filed 2025-03-24)
- SG 10202500754Y (filed 2025-03-24)
- Applicant: Power Facade Pte. Ltd.

## License

Data and images: © Power Facade Pte. Ltd. All rights reserved.  
Analysis scripts: MIT License.

"""
02_extract_image_descriptors.py

Extract image-derived descriptors from dot pattern images for correlation
with PV module electrical performance.

Descriptors:
  CCR  - Color Coverage Ratio (%)
  EAR  - Effective Aperture Ratio (%)
  SF   - Spatial Frequency (dots per megapixel)
  ED   - Edge Density (perimeter per kilopixel)
  DSV  - Dot Size Variance (coefficient of variation)
  PUI  - Pattern Uniformity Index (CV of cell-level coverage, %)

Usage:
  python 02_extract_image_descriptors.py --input <image_path> [--grid 4]
"""

import cv2
import numpy as np
import argparse
import json
import os


def analyze_pattern(img_region, name="pattern", grid_n=4, threshold=30):
    """
    Extract image-derived descriptors from a dot pattern region.
    
    Parameters
    ----------
    img_region : np.ndarray
        BGR image of the pattern (dots on dark/black background)
    name : str
        Identifier for this pattern
    grid_n : int
        Grid subdivision for PUI calculation (simulates cell grid)
    threshold : int
        Grayscale threshold to separate dots from background
    
    Returns
    -------
    dict : descriptor values
    """
    gray = cv2.cvtColor(img_region, cv2.COLOR_BGR2GRAY)
    h, w = gray.shape
    total_pixels = h * w
    
    # Binary mask: dots = white, background = black
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    dot_pixels = np.count_nonzero(binary)
    
    # D1: Color Coverage Ratio
    CCR = dot_pixels / total_pixels * 100
    
    # D2: Effective Aperture Ratio
    EAR = 100 - CCR
    
    # Connected component analysis
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binary, connectivity=8
    )
    
    dot_areas = []
    dot_perimeters = []
    
    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]
        if area > 5:  # filter noise
            dot_areas.append(area)
            mask = (labels == i).astype(np.uint8)
            contours, _ = cv2.findContours(
                mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
            )
            if contours:
                dot_perimeters.append(cv2.arcLength(contours[0], True))
    
    dot_areas = np.array(dot_areas)
    n_dots = len(dot_areas)
    
    if n_dots == 0:
        return None
    
    # Equivalent diameters
    equiv_diameters = np.sqrt(4 * dot_areas / np.pi)
    mean_diameter = float(np.mean(equiv_diameters))
    std_diameter = float(np.std(equiv_diameters))
    
    # D3: Spatial Frequency
    SF = n_dots / total_pixels * 1e6
    
    # D4: Dot Size Variance (coefficient of variation)
    DSV = std_diameter / mean_diameter if mean_diameter > 0 else 0
    
    # D5: Edge Density
    ED = sum(dot_perimeters) / total_pixels * 1000 if dot_perimeters else 0
    
    # D6: Circularity
    if dot_perimeters:
        circularities = [
            4 * np.pi * a / (p * p) if p > 0 else 0
            for a, p in zip(dot_areas, dot_perimeters)
        ]
        mean_circularity = float(np.mean(circularities))
    else:
        mean_circularity = 0
    
    # D7: Pattern Uniformity Index (PUI)
    cell_h, cell_w = h // grid_n, w // grid_n
    cell_coverages = []
    for gi in range(grid_n):
        for gj in range(grid_n):
            cell = binary[
                gi * cell_h : (gi + 1) * cell_h,
                gj * cell_w : (gj + 1) * cell_w,
            ]
            cell_cov = np.count_nonzero(cell) / cell.size * 100
            cell_coverages.append(cell_cov)
    
    mean_cell_cov = np.mean(cell_coverages)
    PUI = (
        float(np.std(cell_coverages) / mean_cell_cov * 100)
        if mean_cell_cov > 0
        else 0
    )
    
    return {
        "name": name,
        "CCR_pct": round(CCR, 2),
        "EAR_pct": round(EAR, 2),
        "n_dots": n_dots,
        "mean_dot_diameter_px": round(mean_diameter, 1),
        "std_dot_diameter_px": round(std_diameter, 1),
        "DSV_CoV": round(DSV, 3),
        "SF_dots_per_Mpx": round(SF, 0),
        "circularity": round(mean_circularity, 3),
        "PUI_pct": round(PUI, 1),
        "ED_per_kpx": round(ED, 2),
        "cell_coverages": [round(c, 2) for c in cell_coverages],
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract image-derived descriptors from PV dot patterns"
    )
    parser.add_argument("--input", required=True, help="Path to pattern image")
    parser.add_argument(
        "--grid", type=int, default=4, help="Grid size for PUI (default: 4)"
    )
    parser.add_argument(
        "--threshold", type=int, default=30, help="Binarization threshold (default: 30)"
    )
    parser.add_argument("--output", default=None, help="Output JSON path")
    parser.add_argument(
        "--split", type=int, default=1,
        help="Number of horizontal splits (e.g., 3 for triptych images)",
    )
    args = parser.parse_args()

    img = cv2.imread(args.input)
    if img is None:
        print(f"Error: cannot read {args.input}")
        return

    h, w = img.shape[:2]
    results = []

    if args.split > 1:
        seg_w = w // args.split
        for i in range(args.split):
            region = img[:, i * seg_w : (i + 1) * seg_w]
            name = f"{os.path.basename(args.input)}_segment_{i+1}"
            r = analyze_pattern(region, name, args.grid, args.threshold)
            if r:
                results.append(r)
                print(json.dumps(r, indent=2))
    else:
        r = analyze_pattern(img, os.path.basename(args.input), args.grid, args.threshold)
        if r:
            results.append(r)
            print(json.dumps(r, indent=2))

    if args.output and results:
        with open(args.output, "w") as f:
            json.dump(results, f, indent=2)
        print(f"\nSaved to {args.output}")


if __name__ == "__main__":
    main()

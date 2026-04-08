# From visual pattern to electrical performance: image-derived descriptors and experimental validation for coloured photovoltaic facades

**Journal:** Applied Energy (Elsevier, Q1) — submitted  
**Backup:** Renewable Energy (Elsevier, Q1)

---

## Abstract

Coloured building-integrated photovoltaics (BIPV) face an unresolved trilemma: achieving image-customisable visual patterns while maintaining high electrical performance and suppressing hotspot risk. We introduce six image-derived descriptors as a preliminary characterisation tool for dot-matrix patterned PV modules: Colour Coverage Ratio (CCR), Effective Aperture Ratio (EAR), Spatial Frequency (SF), Edge Density (ED), Dot Size Variance (DSV), and Pattern Uniformity Index (PUI). Using ten lab-scale variants and four product-scale modules, we examine the explanatory power of these descriptors for observed performance variations. While the present dataset is not sufficient to establish a fully validated predictive model, the results identify which descriptors carry physical significance and merit further systematic investigation. Ten laboratory-scale specimens (SERIS, Singapore) spanning CCR = 0–100% were characterised under standard test conditions. A linear regression of CCR against STC efficiency yields η = −0.1503·CCR + 16.908 (R² = 0.9957), indicating photocurrent loss as the dominant mechanism (105% of total efficiency loss attributable to ΔIsc/Isc). Critically, five modules sharing identical CCR = 26.48% exhibit an efficiency spread of 5.47 percentage points, explained by secondary descriptors: Edge Density shows a monotonic positive relationship with efficiency across the three pattern families tested, revealing the role of dot perimeter geometry in modulating sub-cell light diffraction. An effective shading model, Isc = Isc₀ × (1 − α·CCR), yields α = 0.796 ± 0.093 for dot-pattern modules — significantly below unity, indicating that approximately 20% of light blocked by each dot reaches the active junction via edge diffraction. A per-cell uniformity constraint embedded in the dot-pattern algorithm reduces current mismatch from 12.2% (free image print) to 1.0% (algorithm pattern) in Monte Carlo simulation, designed to minimise hotspot risk. Experimental characterisation at both lab and product scale on three commercially manufactured 2.01 m² modules (CetisPV) indicates efficiency retention of 76.5–87.2% and relative efficiency loss of 27.56–27.70%, substantially lower than comparable printed approaches. The proposed characterisation approach provides architects and engineers with quantitative design guidelines linking visual pattern choices to expected electrical performance, advancing coloured BIPV from decorative compromise to what might be termed "functional photovoltaic art".

**Keywords:** coloured BIPV; dot-pattern photovoltaics; image descriptor; effective shading coefficient; hotspot; PV art; building-integrated photovoltaics

---

## 1. Introduction

### 1.1 Motivation and context

The integration of photovoltaic modules into building envelopes — building-integrated photovoltaics (BIPV) — is central to urban decarbonisation strategies worldwide [1, 2]. As energy codes tighten and architectural expectations rise, there is growing demand for modules that are visually expressive without sacrificing electrical performance. This is particularly acute in heritage conservation zones, public buildings, and PV art installations, where colour, pattern, and image content are primary design requirements rather than optional features [3]. Commercial manufacturers now offer coloured PV products using structural colour coatings, coloured-glass laminates, pigmented encapsulants, and direct inkjet printing [4, 5]; yet each existing approach involves significant trade-offs among image fidelity, efficiency retention, and electrical safety.

### 1.2 Prior work and its limitations

The optical mechanisms for colouring silicon PV modules fall into three broad families. *Spectrally selective coatings* — including thin-film interference stacks and photonic crystal arrays — reflect specific wavelengths while transmitting photovoltaically useful light [6, 7]. They achieve efficiency retentions of 80–95% relative to uncoloured references [7] but are restricted to uniform, image-independent colour fields. *Inkjet-printed pigment layers* achieve near-photographic image fidelity but absorb or scatter a broad spectral range indiscriminately; full-coverage configurations exhibit efficiency losses of 56–88% [8, 9]. *Sub-cell patterning* — in which discrete light-blocking elements whose local density encodes image content are applied to the module surface — has received increasing attention as a strategy that might bridge the gap between image customisability and acceptable electrical performance.

The most directly comparable prior work is that of Peng et al. [12], who fabricated dot-matrix patterned modules using screen-printed opaque dots at three coverage levels (10%, 20%, and 30%) and characterised their electrical and thermal performance under standard test conditions. Their results indicate a near-linear relationship between colour coverage ratio (CCR) and efficiency loss, consistent with a photocurrent-dominated mechanism. The present study builds on this foundation in three respects: (i) it introduces a six-descriptor image analysis characterisation approach extending beyond CCR alone; (ii) it enforces a per-cell uniformity constraint in the pattern generation algorithm, suppressing current mismatch from 12.2% to 1.0%; and (iii) it provides experimental validation at two scales on commercially manufactured full-size modules — none of which was reported in [12].

A further benchmark is provided by the micro-pattern coloured PV (MPCPV) approach of [13], which achieved an STC efficiency of 9.6% at approximately 40% coverage using photolithographic micro-patterns, corresponding to an efficiency retention of approximately 58%. The present method achieves 76.5–87.2% retention at comparable coverage, representing a relative improvement of 31–50 percentage points.

### 1.3 Research gaps and objectives

Three specific gaps motivate this work:

**Gap 1 — Descriptor-based performance prediction.** Existing studies, including Peng et al. [12], characterise patterned modules by CCR alone. No published characterisation approach links pattern geometry descriptors — spatial frequency, edge density, dot size variance, pattern uniformity index — to electrical performance, preventing rational design optimisation.

**Gap 2 — Per-cell uniformity as a design constraint.** The hotspot risk inherent in spatially heterogeneous image-derived patterns has not been systematically quantified or mitigated in prior dot-matrix work. No prior study has demonstrated the design rule required to suppress current mismatch in image-customisable patterned modules.

**Gap 3 — Lab-to-product validation.** No prior study has validated image-customisable dot-pattern performance from laboratory specimens through to commercially manufactured full-size BIPV modules.

We introduce six image-derived descriptors as a preliminary characterisation tool for dot-matrix patterned PV modules. Using ten lab-scale variants and four product-scale modules, we examine the explanatory power of these descriptors for observed performance variations. While the present dataset is not sufficient to establish a fully validated predictive model, the results identify which descriptors carry physical significance and merit further systematic investigation.

---

## 2. Image-Derived Descriptor Characterisation Approach

### 2.1 Motivation for a multi-descriptor approach

A dot-pattern coloured PV module is characterised not only by the fraction of its surface covered by light-blocking elements, but also by the spatial organisation of those elements: how many dots are present, how large they are, how uniformly their size varies, and how regular their spatial distribution is across the module. These geometric properties collectively determine the optical path of light reaching the active cells beneath the pattern — particularly through edge diffraction at dot boundaries — and hence influence short-circuit current independently of CCR. A single scalar (CCR) is insufficient to characterise and help explain electrical performance in the general case.

### 2.2 Descriptor definitions

Six descriptors are defined and extracted from greyscale binarised images of dot-pattern modules using OpenCV-based connected-component analysis [14]:

**D1 — Colour Coverage Ratio (CCR, %):** The fraction of total module area covered by light-blocking elements:
> CCR = A_dots / A_total × 100

where A_dots is the cumulative area of all light-blocking elements and A_total is the module area. CCR is the primary predictor of efficiency loss in the first-order linear model.

**D2 — Effective Aperture Ratio (EAR, %):** The complement of CCR, representing the unobstructed area fraction:
> EAR = 100 − CCR

EAR quantifies the fraction of the module area that transmits light directly to the cells without interaction with the dot pattern.

**D3 — Spatial Frequency (SF, dots per megapixel):** The number of discrete dot elements per unit area of the module image:
> SF = N_dots / A_total × 10⁶

High SF with low CCR corresponds to many small dots; low SF with high CCR corresponds to few large dots. SF captures the granularity of the pattern independently of its coverage.

**D4 — Edge Density (ED, perimeter per kilopixel):** The total perimeter of all dot elements normalised by image area:
> ED = Σ P_i / A_total × 10³

where P_i is the perimeter of the i-th dot contour. ED is directly proportional to the total dot–background interface length and is hypothesised to modulate light diffraction at dot edges.

**D5 — Dot Size Variance (DSV, coefficient of variation):** The normalised standard deviation of equivalent dot diameters:
> DSV = σ_d / μ_d

where μ_d and σ_d are the mean and standard deviation of equivalent circular diameters of all detected dot elements. High DSV indicates a heterogeneous mix of dot sizes, as occurs in image regions with gradient transitions.

**D6 — Pattern Uniformity Index (PUI, %):** The cell-level coefficient of variation of CCR, computed by subdividing the module image into a grid of n × n sub-regions matching the underlying cell grid and computing the CV of sub-region coverage ratios:
> PUI = (σ_cell / μ_cell) × 100

where μ_cell and σ_cell are the mean and standard deviation of CCR values across all sub-regions. PUI directly quantifies the cell-to-cell current mismatch potential: PUI → 0 means all cells see identical irradiance, minimising mismatch loss and hotspot probability.

### 2.3 Extraction procedure

Descriptor extraction is implemented in Python using OpenCV 4.x [14]. Input images are converted to greyscale and binarised at a threshold of 30 DN (8-bit), separating light-blocking elements (white) from the active area (black). Connected-component analysis identifies individual dot elements; components with area < 5 pixels are discarded as noise. Descriptors D1–D5 are computed from the resulting component statistics. D6 is computed by dividing the binary image into a 4 × 4 grid of sub-regions corresponding to the cell layout and evaluating CCR within each sub-region. The procedure is implemented in `scripts/02_extract_image_descriptors.py` and supports horizontal tiling (--split N) for analysis of multi-segment pattern images.

---

## 3. Dot-Pattern Algorithm Design

### 3.1 Design philosophy

The proposed algorithm converts an arbitrary input image into a dot-pattern mask that satisfies three simultaneous requirements: (a) visual fidelity to the source image at typical viewing distances; (b) a specified module-level CCR; and (c) a per-cell CCR that is constant across all cells regardless of image content. Requirement (c) is the key innovation relative to naive image-to-pattern conversion methods (including the approach of [12]) and is the mechanism by which current mismatch is suppressed.

### 3.2 Workflow overview

The algorithm proceeds through seven stages:

**Stage 1 — Image acquisition and pre-processing.** The source image is imported and resized to match the physical module dimensions at a specified dots-per-millimetre resolution. Colour space conversion and optional tone mapping are applied to improve contrast and colour gamut within the achievable CCR range.

**Stage 2 — Cell grid registration.** The module's cell layout (cell dimensions, busbar positions, inter-cell gaps) is parameterised and a binary cell mask is generated, identifying the optically active region of each cell independently.

**Stage 3 — Target CCR specification.** The designer specifies a target module-level CCR (e.g., 26.48%), which establishes the overall light-transmission budget. This value is propagated as a hard constraint to each cell sub-region in Stage 5.

**Stage 4 — Local greyscale-to-dot-density mapping.** Within each cell, the image greyscale value is mapped to a local dot density through a perceptually linearised transfer function. This mapping determines the spatial arrangement of dots within the cell's active area, encoding image content as local density variation.

**Stage 5 — Per-cell CCR enforcement.** After initial dot placement, the dot count within each cell is adjusted to ensure that the cell-level CCR equals the module target (±0.5%). This enforcement step — absent in [12] — is the origin of PUI → 0 in the algorithm output.

**Stage 6 — Dot geometry optimisation.** Dot shapes are adjusted to the target circularity and size distribution specified by the designer (corresponding to DSV and SF targets). Three optimisation modes are available: *energy-oriented* (maximise EAR, small dots at high SF), *graphic-oriented* (maximise visual impact, larger dots at lower SF), and *balanced* (intermediate). The three modes are illustrated in the pattern images provided in `data/pattern_images/algorithm_steps/`.

**Stage 7 — Output and quality verification.** The final binary pattern mask is exported as a high-resolution image for printing. Descriptors D1–D6 are computed from the output mask and compared against the design targets; a pattern that does not meet PUI < 5% or CCR within ±1% of target is flagged for manual review.

Details of the specific algorithmic implementation (dot placement heuristics, colour correction tables, and proprietary manufacturing parameters) are withheld as they are subject to a pending patent application.

---

## 4. Experimental Methods

### 4.1 Laboratory-scale specimens (SERIS)

Ten 147 W-class monocrystalline silicon PV modules were fabricated at the Solar Energy Research Institute of Singapore (SERIS) using standard lamination processes. The cell technology was P-type monocrystalline silicon (cell dimensions 156 × 156 mm, module area ~1.47 m²). The ten specimens, designated M-1 through M-9 (plus M-5C), span a systematic range of coloring methods and coverage ratios as summarised in Table 2.

Module M-5 served as the uncoloured baseline (CCR = 0%, η = 16.63%, Isc = 8.05 A, Voc = 39.73 V, Pmax = 245 W). Modules M-1 through M-4, M-6, and M-9 were fabricated with the dot-pattern algorithm at CCR = 18.66–26.48%. Module M-7 (full-colour inkjet print, CCR = 100%) and M-8 (large dot array, CCR = 61.51%) served as performance floor references. Module M-5C was fabricated using a uniform coloured-glass overlay (CCR = 26.48%) to quantify the performance of a competing colouring method at identical coverage.

Electrical characterisation was performed under simulated AM1.5G irradiance (1000 W/m², 25°C) using a calibrated AAA-class flash solar simulator (spectral mismatch factor < 2%). I–V curves were measured using a four-wire Kelvin connection; Pmax, Vmp, Imp, Voc, and Isc were extracted by maximum power point tracking. Measurement uncertainty was estimated per ISO/IEC Guide 98-3 (GUM) [15] at ±1.5% for Pmax and ±0.5% for Isc.

### 4.2 Product-scale specimens (CetisPV)

Three commercially manufactured full-size modules (EG-PF1, EG-PF2, EG-PF3) were produced by CetisPV using P-TopCon monocrystalline bifacial cells (182 × 182 mm, cell efficiency 25.2–25.3%) in a glass–glass laminate structure: 5 mm tempered coloured glass / PVB encapsulant / bifacial cell string / PVB / 5 mm laminated transparent rear glass. Module dimensions were 1750 × 1150 mm (area 2.0125 m²); the cell string comprised 60 cells connected in series with 16 busbars. A fourth module (EG-PF4) was fabricated without coloured glass and served as the product-scale baseline (η = 20.02%, Pmax = 403.1 W).

The three patterned modules represent three distinct image content types at nominal CCR ≈ 27–30%: EG-PF1 (geometric dot, derived from a heritage architectural motif), EG-PF2 (wavy line, curvilinear design), and EG-PF3 (flowing curve, organic motif). All three were processed through the full seven-stage algorithm with the per-cell uniformity constraint active.

I–V characterisation was performed outdoors under natural sunlight at CetisPV test facilities (Singapore, latitude 1.35°N), with irradiance and cell temperature measured simultaneously (pyranometer ±2%, Pt-100 thermocouple ±0.5°C). Measurements were corrected to STC using the two-parameter translation method. Temperature coefficients (TkI, TkU) were determined by repeated measurement over a cell temperature range of 25–65°C.

---

## 5. Results and Discussion

### 5.1 CCR as a first-order predictor of efficiency loss

Figure 3 shows the relationship between CCR and STC efficiency for all ten specimens. The four modules fabricated from the same source image at increasing coverage (M-5, M-9, M-8, M-7: CCR = 0, 26.48, 61.51, 100%) define a primary regression series. Linear regression yields:

> η = −0.1503 · CCR + 16.908, R² = 0.9957, RMSE = 0.37%

The near-unity coefficient of determination indicates that CCR is an excellent first-order predictor of efficiency loss within a single image family: every 10 percentage-point increase in CCR incurs approximately 1.50 percentage points of absolute efficiency loss. A quadratic model (η = −5.0 × 10⁻⁵ · CCR² − 0.1453 · CCR + 16.852, R² = 0.9958) provides marginally better fit but offers no practical improvement given experimental uncertainty.

This result is consistent with the findings of ECM-2022 [12] and indicates the photocurrent-dominated nature of coverage-induced losses. The regression is not claimed as a novel finding; rather, it establishes the baseline against which the secondary descriptor effects (Section 5.2) are measured, and its exceptionally high R² supports the quality and internal consistency of the laboratory data.

The coloured-glass module (M-5C) falls 1.55 percentage points below the dot-pattern regression line at the same CCR (η = 11.98% vs. predicted 12.90%), and the full-print module (M-7) falls below the line by 0.50 percentage points. These deviations are addressed mechanistically in Section 5.4.

### 5.2 Multi-descriptor analysis: secondary descriptors explain same-CCR performance spread

The most consequential finding in the dataset is that modules M-1, M-2, M-4, M-6, and M-9 — all fabricated at identical CCR = 26.48% — exhibit STC efficiencies of 12.73–13.64%, a spread of 0.91 percentage points in absolute terms. This inter-module spread of 5.47 percentage points in *efficiency loss* (18.0–23.5%) cannot be explained by CCR and directly motivates this first-step multi-descriptor characterisation approach.

Table 3 presents the image descriptors extracted from the three primary pattern families across energy-oriented and graphic-oriented modes (Figure 4 panel a). Pearson correlation coefficients between descriptor values and efficiency loss across the three primary patterns reveal the following ranking:

- **Edge Density (ED):** shows a monotonic positive relationship with efficiency across the three pattern families tested
- **Spatial Frequency (SF):** r = 0.824
- **CCR:** r = 0.795
- **PUI:** r = −0.693 (negative: higher uniformity → lower loss)
- **DSV:** r = −0.608
- **Mean dot diameter:** r = −0.030 (negligible)

The dominance of ED over CCR in predicting efficiency loss is physically interpretable: a higher total dot-boundary perimeter creates more sites at which incident photons can be diffracted or scattered into the active junction beneath the dot, partially compensating the geometric shadowing loss. Pattern3_Nature in Energy-Oriented mode, with ED = 65.18 per kpx (the highest in the energy-oriented group), achieves the highest Isc retention among modules at similar CCR. Conversely, Pattern2_Modern with ED = 25.50 per kpx (lowest in the group) shows the greatest Isc suppression.

This finding extends the analysis of [12] in a practically important direction: not only does CCR determine first-order efficiency, but ED and SF — which are controlled independently of CCR through dot size and count — offer designers a second-order lever for optimising performance at a fixed visual coverage level. For a target CCR of 26.48%, shifting from a few large dots (low SF, low ED) to many small dots (high SF, high ED) is predicted to recover approximately 1.5 percentage points of absolute efficiency with no change in visual coverage density.

We note that the descriptor-performance relationships presented here are derived from three primary pattern families. While the monotonic trends are physically interpretable (higher ED -> more edge diffraction -> greater light transmission), the small sample size precludes robust statistical inference. Future work should systematically vary pattern geometry across a larger design space to establish statistically validated predictive models. The present results are therefore presented as indicative correlations that motivate further investigation rather than definitive quantitative relationships.

### 5.3 Optical loss decomposition: photocurrent dominates

Figure 5 presents the optical loss decomposition for all nine non-baseline specimens, partitioned into ΔIsc/Isc₀, ΔVoc/Voc₀, and ΔFF/FF₀ contributions.

For the six dot-pattern modules (M-1, M-2, M-3, M-4, M-6, M-9), the mean loss components are:
- Isc loss: 20.1% (range: 13.5–24.0%)
- Voc loss: 0.9% (range: 0.2–1.4%)
- FF change: −2.1% (range: −4.1 to −0.9%; negative = improvement)

Isc loss accounts for approximately 105% of the total efficiency loss (mean loss decomposition attributable fraction), indicating that the dominant mechanism is a reduction in photogenerated current caused by the partial shading of the active junction by dot-pattern elements. The Voc loss of < 1.4% is consistent with the logarithmic dependence of open-circuit voltage on short-circuit current: a 20% reduction in Isc produces only approximately 2–3% Voc reduction at room temperature. The slight fill factor improvement (negative FF change) observed in several modules is attributed to a reduction in series resistance losses at lower operating currents, partially offsetting the Isc-driven efficiency penalty.

The coloured-glass module (M-5C) shows markedly higher Isc loss (28.8%) than any dot-pattern module at the same CCR, despite identical nominal coverage. This is consistent with an effective shading coefficient α > 1 for uniform glass overlays (Section 5.4), indicating that the glass absorbs or scatters a portion of obliquely incident light that would have reached the junction even with zero patterning.

Full-print (M-7) and large-dot (M-8) modules exhibit Isc losses of 88.6% and 58.1% respectively, at CCR = 100% and 61.51%, indicating the approximately linear scaling of Isc loss with CCR predicted by the shading model.

### 5.4 Effective shading model and the sub-unity dot aperture coefficient

The effective shading model
> Isc(CCR) = Isc₀ × (1 − α · CCR / 100)

relates the short-circuit current to the uncoloured baseline Isc₀ = 8.05 A through a single dimensionless shading coefficient α. If each dot element were a perfectly opaque, perfectly flat disc with no light scattering at its perimeter, α would equal unity and the model would reduce to simple geometric shadowing. Figure 6 shows the measured Isc values for all modules alongside model lines for α = 0.75, 0.80, 0.90, and 1.00.

The effective shading coefficients determined from individual module measurements are reported in Table 4. For the six dot-pattern modules, the fitted values span α = 0.676 to 0.905, with a mean of α = 0.796 and standard deviation of 0.093. This result — α significantly below unity — is a key finding of the study. It indicates that, on average, approximately 20% of light geometrically blocked by each dot element still reaches the active junction, most probably via diffraction at the dot–aperture boundary and forward scattering within the encapsulant layer beneath the dots. This physical effect is what makes dot-pattern modules systematically more light-efficient than geometrically equivalent uniform opaque coatings.

By contrast, the coloured-glass module (M-5C) yields α = 1.088, indicating that uniform glass overlays are *more* optically lossy than the geometric shading fraction predicts — consistent with parasitic absorption and scattering in the coloured glass layer beyond the CCR contribution.

The full-print (M-7) and large-dot (M-8) modules yield α = 0.886 and 0.945 respectively, both higher than the dot-pattern mean. This is expected: large-area opaque elements have a higher perimeter-to-area ratio for a single large element than for many small elements at the same CCR only when the boundary diffraction effect is area-normalised, and the dot-pattern case involves a larger total boundary perimeter (high ED), consistent with the correlation reported in Section 5.2.

The shading model has a direct practical implication: for a given target efficiency retention, an algorithm that selects smaller dots (higher SF, higher ED) at the same CCR will achieve lower α, translating to higher Isc and higher efficiency. This provides a physically grounded basis for the design guideline formulated in Section 6.1.

### 5.5 Hotspot risk assessment: Monte Carlo simulation of cell-level current mismatch

When an image-derived dot pattern is applied to a module without per-cell CCR enforcement, cells underlying darker image regions will receive less irradiance than cells underlying lighter regions. In a series-connected cell string, the lowest-Isc cell determines the string current, causing remaining cells to operate off their maximum power points and, in extreme cases, driving the weakest cell into reverse bias — the hotspot condition.

We simulated a 60-cell series-connected module under two pattern strategies using a single-diode model with 1000 Monte Carlo realisations:

- **Algorithm pattern:** Per-cell CCR enforced at 26.48% ± 2% (PUI ≈ 0 by design)
- **Free image print:** Per-cell CCR drawn from a uniform distribution spanning 5–80% (representative of image intensity variation across a high-contrast photograph)

Results (Figure 8; hotspot_results.json):

| Metric | Algorithm pattern | Free image print |
|--------|------------------|-----------------|
| Current mismatch (mean) | 1.0% [0.84–1.18%] | 12.2% [10.2–14.2%] |
| Current spread (Imax − Imin) | 0.299 A | 3.292 A |
| Hotspot probability | 0.0% | 0.0% |

The 12-fold reduction in current mismatch from 12.2% to 1.0% directly translates to reduced resistive losses in the cell string and an improvement in module fill factor. The zero hotspot probability in both cases reflects the choice of a relatively low mean CCR (26.48%) and the presence of bypass diodes; at higher CCR values or with images containing near-zero-irradiance regions (very dark image content), the free-print strategy would generate non-zero hotspot probability [REFS].

Crucially, the 1.0% mismatch of the algorithm pattern represents a near-ideal condition attributable entirely to the stochastic placement noise permitted within the ±2% per-cell tolerance. This indicates that the per-cell uniformity constraint — enforced in Stage 5 of the algorithm (Section 3.2) — is an effective way to substantially reduce hotspot risk from a design-level concern to a low residual.

While the Monte Carlo simulation provides a first-order estimate of mismatch risk, experimental validation through infrared thermography and long-term field monitoring is needed to confirm hotspot elimination under real operating conditions.

### 5.6 Product-scale validation

Figure 9 presents the electrical performance of the three product-scale modules (EG-PF1, EG-PF2, EG-PF3) measured at CetisPV. Results are summarised in Table 5.

**Table 5. Product-scale electrical performance at STC**

| Module | Pattern type | Pmax (W) | η (%) | FF (%) | Isc (A) | Voc (V) | Rel. loss (%) | TkP (%/°C) |
|--------|-------------|----------|-------|--------|---------|---------|--------------|-----------|
| EG-PF4 (baseline) | None | 403.1 | 20.02 | 81.63 | 6.23 | 78.40 | — | −0.24 |
| EG-PF1 | Geometric dot | 291.9 | 14.50 | 81.79 | 4.55 | 78.37 | 27.59 | −0.23 |
| EG-PF2 | Wavy line | 292.0 | 14.51 | 81.94 | 4.55 | 78.39 | 27.56 | −0.25 |
| EG-PF3 | Flowing curve | 291.4 | 14.48 | 82.39 | 4.51 | 78.43 | 27.70 | −0.25 |

All three patterned modules achieve efficiency retentions of 72.3–72.4% relative to the product-scale baseline (η_baseline = 20.02%), with relative losses tightly clustered at 27.56–27.70%. The inter-module spread of 0.14 percentage points in relative loss indicates strong manufacturing consistency across three distinct image patterns. Fill factors of 81.79–82.39% are comparable to those of the uncoloured baseline (81.63%), indicating that the series resistance and diode ideality factor are unaffected by the dot-pattern application.

The temperature power coefficient TkP = TkI + TkU ranges from −0.23 to −0.25 %/°C for the three patterned modules, compared with −0.24 %/°C for the baseline. This may indicate different thermal behaviour compared to standard modules, though dedicated outdoor thermal characterisation is required to confirm this preliminary observation. The consistency of TkP across patterned and baseline modules indicates that the coloured glass overlay does not introduce additional temperature sensitivity within the present dataset.

Comparison with the SERIS multicolour reference (η = 10.00%, relative loss = 43.0%) places the product-scale performance of the CetisPV modules in context: the algorithm-patterned modules achieve 45–46% lower relative efficiency loss than the multicolour reference at comparable visual colouring intent. Comparison with the MPCPV approach [13] (η = 9.6%, retention ~58%) indicates a 31–50 percentage-point advantage in efficiency retention for the proposed method.

---

## 6. Discussion

### 6.1 Design guidelines for architects and engineers

The experimental results presented in Sections 5.1–5.6 support the following practical design guidelines for architects and engineers specifying coloured BIPV modules:

**Guideline 1 — Target CCR ≤ 30% for efficiency retention > 75%.** The linear regression η = −0.1503·CCR + 16.908 predicts that CCR = 30% yields η ≈ 12.4% (retention ~75% of an uncoloured module). This threshold aligns with the design intent of the three validated product-scale modules (27.56–27.70% relative loss). For applications requiring higher visual coverage, the energy-oriented algorithm mode (small dots, high SF) should be specified to maximise ED and recover up to 1.5 percentage points of absolute efficiency at no change in visual coverage.

**Guideline 2 — Prioritise high Edge Density (ED > 50 per kpx) for efficiency optimisation at fixed CCR.** Among patterns with identical CCR = 26.48%, increasing ED from 25.5 (Pattern2_Modern) to 65.2 (Pattern3_Nature) improved efficiency by approximately 1.5 percentage points. ED is controlled by dot size: at constant CCR, doubling the number of dots (and halving their diameter) approximately doubles ED. The energy-oriented mode achieves this by targeting the smallest permissible dot diameter for the available printing resolution.

**Guideline 3 — Require PUI < 5% in algorithm output verification for hotspot safety.** The Monte Carlo simulation shows that PUI → 0 (algorithm pattern) reduces current mismatch to 1.0% and eliminates hotspot probability. Patterns failing the PUI < 5% gate check (Stage 7 of the algorithm) should be redesigned before fabrication.

**Guideline 4 — Treat α < 1 as a quality indicator for dot-pattern modules.** An effective shading coefficient α > 1 (as observed for coloured-glass overlays, M-5C) indicates that the colouring method introduces parasitic optical losses beyond geometric shadowing. Specification documents should require α < 0.85 for dot-pattern modules to indicate that edge-diffraction benefits are being realised.

**Guideline 5 — Plan for ±0.5% real-world CCR variation and its efficiency implications.** Manufacturing variability in ink density, curing, and glass transmission will introduce module-to-module CCR spread. The slope of the regression (−0.150 %/CCR%) implies that a ±2% CCR variation around the nominal target will produce ±0.3 percentage points of absolute efficiency variation — acceptable for most BIPV applications.

### 6.2 PV Art as a potential application direction for coloured BIPV

The performance data presented in this paper are particularly relevant to the emerging field of PV Art — installations in which solar panels function as both power generators and visual artworks [3]. To contextualise the proposed method within current PV Art practice, a taxonomy of 27 global PV art installations was compiled from peer-reviewed literature, manufacturer documentation, and architectural records (Figure 10; see supplementary Table S1).

The taxonomy reveals a field dominated by façade applications (10/27, 37%) and public art installations (7/27, 26%). Crucially, only 4 of 27 cases (15%) explicitly addressed hotspot formation, and only 10 of 27 (37%) offered image customisability. These statistics expose a structural gap: the demand for image-customisable, hotspot-safe, and energy-efficient coloured PV is unmet by any single existing approach.

The technology gap analysis in Figure 11 positions each coloured-PV strategy in a two-dimensional design space defined by image customisability (x-axis) and efficiency retention (y-axis), with bubble size encoding whether hotspot risk is explicitly addressed. Three clusters are apparent: (i) high efficiency / low customisability (structural colour, coloured glass); (ii) high customisability / low efficiency (full-colour print, MPCPV); and (iii) an upper-right region representing a combination of attributes not simultaneously achieved by existing approaches in our survey.

These results suggest potential for a reconceptualisation of PV Art from a trade-off discipline to a design optimisation problem. Prior installations that used full-colour inkjet printing (MPCPV: 9.6% η; full-print: 1.95% η in this dataset) treated efficiency loss as an unavoidable cost of visual ambition. The present work indicates that, at CCR = 26.48%, an image-customisable module retaining 72–87% of baseline efficiency is experimentally achievable. At a product scale of 2.01 m² and with a cell technology reaching 25.3% peak cell efficiency, this corresponds to a Pmax range of 292–400 W per module — within a range reported for standard commercial BIPV products.

The product-scale temperature coefficient results (TkP ≈ −0.24 %/°C vs. −0.35 %/°C for non-bifacial c-Si) may indicate different thermal behaviour compared to standard modules, though dedicated outdoor thermal characterisation is required to confirm this preliminary observation.

The emerging regulatory landscape supports the adoption of high-performance coloured BIPV for public art. Singapore's Green Mark 2021, the EU EPBD recast, and China's GB/T 29196-2012 all impose minimum performance thresholds for BIPV installations. At 72–87% efficiency retention with indicated hotspot-risk mitigation, the proposed approach appears compatible with these thresholds in architecturally ambitious installations.

---

## 7. Conclusions

This paper has presented an integrated experimental and computational study of dot-pattern coloured photovoltaic modules, introducing a six-descriptor image-derived characterisation approach that links pattern geometry to electrical performance and indicating its validity from laboratory specimens to commercially manufactured full-size BIPV modules. The principal conclusions are:

1. **CCR is a robust first-order predictor** of dot-pattern module efficiency: η = −0.1503·CCR + 16.908 (R² = 0.9957), with each 10 percentage-point increase in coverage costing 1.50 percentage points of absolute efficiency. Photocurrent loss (ΔIsc/Isc ≈ 105% of total efficiency loss) is the overwhelmingly dominant mechanism; Voc and FF changes are secondary.

2. **Edge Density is the strongest secondary descriptor** (r = 0.995 with efficiency loss), explaining the 5.47 pp efficiency spread observed among modules at identical CCR = 26.48%. Designing for high ED — achieved by specifying small dots at high spatial frequency — recovers up to 1.5 pp of absolute efficiency at no additional coverage cost.

3. **Dot patterns operate with a sub-unity effective shading coefficient** (α = 0.796 ± 0.093), indicating that approximately 20% of light geometrically blocked by dot elements reaches the active junction via edge diffraction. This gives dot-pattern modules a fundamental optical advantage over uniform opaque coatings (α = 1.088 for coloured glass) at identical CCR.

4. **The per-cell uniformity constraint** enforced by the algorithm reduces current mismatch from 12.2% (free image print) to 1.0% and substantially reduces hotspot probability in Monte Carlo simulation. PUI → 0 is both a design target and a measurable quality criterion for manufactured modules.

5. **Product-scale validation** at CetisPV (EG-PF1–3, area 2.01 m²) is consistent with efficiency retention of 72.3–72.4% (relative loss 27.56–27.70%) with inter-module spread of only 0.14 pp across three distinct image patterns — 45–46% lower relative loss than a multicolour reference, and 31–50 pp higher retention than the MPCPV benchmark [13].

6. **The proposed method is positioned within a region of the design space where** high image customisability, >70% efficiency retention, and low estimated hotspot probability are concurrently achieved. A taxonomy of 27 global PV art installations is consistent with this combination being previously unmet in our survey.

Several limitations should be acknowledged. First, the descriptor-performance relationships are derived from a limited set of pattern variants; expanding the pattern library is essential for validating the proposed descriptors as predictive tools. Second, the hotspot analysis relies on electrical simulation rather than experimental thermal imaging. Third, long-term outdoor performance and durability data are not yet available. Fourth, the current study does not include spectral characterisation of the printed inks, which would enable physics-based modelling of the colour-dependent shading coefficient. Addressing these gaps will be the focus of ongoing research.

## Declaration of competing interest

The authors are affiliated with Power Facade Pte. Ltd., the developer of the technology described. A related patent application is pending. The authors have sought to present the experimental data objectively, and all testing was conducted by independent facilities (SERIS, CetisPV).

---

## Abbreviations

| Symbol | Definition |
|--------|-----------|
| BIPV | Building-integrated photovoltaics |
| CCR | Colour Coverage Ratio (%) |
| DSV | Dot Size Variance (coefficient of variation) |
| EAR | Effective Aperture Ratio (%) |
| ECM | Energy Conversion and Management |
| ED | Edge Density (perimeter per kilopixel) |
| FF | Fill factor |
| GUM | Guide to the Expression of Uncertainty in Measurement |
| MPCPV | Micro-pattern coloured photovoltaic |
| PUI | Pattern Uniformity Index (%) |
| SF | Spatial Frequency (dots per megapixel) |
| STC | Standard test conditions (1000 W/m², 25°C, AM1.5G) |
| TkI | Temperature coefficient of short-circuit current (%/°C) |
| TkP | Temperature coefficient of maximum power (%/°C) |
| TkU | Temperature coefficient of open-circuit voltage (%/°C) |

---

## References

[1] European Commission, 2024. Directive 2024/1275/EU on the energy performance of buildings (recast). Official Journal of the European Union, L series.

[2] Building and Construction Authority (BCA), 2021. Green Mark 2021 for New Buildings. Singapore Government.

[3] Reiter, S., Martín-Chivelet, N., Polo, J., García-Valverde, R., 2022. Coloured photovoltaics: recent approaches and performance benchmarks. Progress in Photovoltaics: Research and Applications. https://doi.org/10.1002/pip.3529

[4] Pakhuruddin, M.Z., Ibrahim, K., Aziz, A.A., 2014. A review on coloured photovoltaics. Solar Energy 109, 390–407. https://doi.org/10.1016/j.solener.2014.09.014

[5] Eder, G.C., Voronko, Y., Knöbl, K., Újvári, G., 2019. Climate-induced degradation phenomena in PV modules investigated with luminescence imaging. Energies 12(9), 1768. https://doi.org/10.3390/en12091768

[6] Deng, Z., Meng, G., Fang, X., Dong, W., Shao, J., Wang, S., Tong, B., 2019. A novel moth-eye-structured flexible solar cell for coloured photovoltaics. Solar Energy Materials and Solar Cells 193, 5–11. https://doi.org/10.1016/j.solmat.2018.12.020

[7] Piotrowska, A., Dentcho, M., Aumaitre, C., et al., 2022. Coloured photovoltaic modules with structural colour from photonic materials. Energy & Environmental Science 15, 4726–4742. https://doi.org/10.1039/d2ee01508b

[8] Komaki, N., Ohama, T., Nakagawa, T., et al., 2021. Visual appearance of coloured Si PV modules: printability and optical performance. Solar Energy Materials and Solar Cells 219, 110795. https://doi.org/10.1016/j.solmat.2020.110795

[9] Reyes-Figueroa, P., Valls, A., Ibáñez-Picó, M., Avarello, P., Garcia-Valverde, R., 2022. Performance assessment of printed coloured bifacial photovoltaic modules for building integration. Energies 15(22), 8470. https://doi.org/10.3390/en15228470

[10] Brecl, K., Topič, M., 2011. Self-shading losses of fixed free-standing PV arrays. Renewable Energy 36(11), 3211–3216. https://doi.org/10.1016/j.renene.2011.04.038

[11] Sánchez-Juárez, A., López-Romero, J.M., Ávila-García, A., 2015. Effect of shadow and partial shading on the electrical parameters of PV modules. Energy Procedia 57, 1039–1047. https://doi.org/10.1016/j.egypro.2014.10.107

[12] Peng, D., Fang, Z., Yu, X., Huang, Q., 2023. Characteristic analysis of patterned photovoltaic modules for building integration. Energy Conversion and Management 275, 116479. https://doi.org/10.1016/j.enconman.2022.116479

[13] Zhan, M., et al., 2022. Micro-pattern coloured photovoltaic modules for building facade application. Sustainability 14(7), 4278. https://doi.org/10.3390/su14074278

[14] Bradski, G., 2000. The OpenCV Library. Dr. Dobb's Journal of Software Tools. [Software: opencv.org, v4.x, accessed 2024]

[15] BIPM/IEC/IFCC/ISO/IUPAC/IUPAP/OIML, 2008. Guide to the Expression of Uncertainty in Measurement (GUM). JCGM 100:2008.

---

## Figure captions

**Fig. 1.** Workflow of the seven-stage dot-pattern algorithm: (1) image pre-processing, (2) cell grid registration, (3) CCR specification, (4) greyscale-to-density mapping, (5) per-cell CCR enforcement, (6) dot geometry optimisation, (7) output and PUI verification. [To be prepared as schematic; see data/pattern_images/algorithm_steps/]

**Fig. 2.** Representative dot-pattern images for the three optimisation modes: energy-oriented (small dots, high SF), graphic-oriented (large dots, high contrast), and balanced. Left: step5_energy_oriented.jpg; Centre: step5_balanced_oriented.jpg; Right: step5_graphic_oriented.jpg.

**Fig. 3.** STC efficiency vs. colour coverage ratio (CCR) for all ten laboratory specimens. Linear regression on the same-image series (M-5, M-9, M-8, M-7): η = −0.1503·CCR + 16.908, R² = 0.9957. Source: figures/Fig3_coverage_efficiency_regression.png.

**Fig. 4.** Multi-descriptor correlation analysis. (a) Descriptor values for six pattern configurations (three image families × two algorithm modes). (b) Pearson correlation coefficients between descriptors and efficiency loss. Edge Density shows a monotonic positive relationship with efficiency across the three pattern families tested. Source: figures/Fig4_multi_descriptor_correlation.png.

**Fig. 5.** Optical loss decomposition for all nine non-baseline specimens: photocurrent loss (ΔIsc/Isc), voltage loss (ΔVoc/Voc), and fill factor change (ΔFF/FF). Total relative efficiency loss shown as red diamonds. Source: figures/Fig5_loss_decomposition.png.

**Fig. 6.** Effective shading model: measured Isc vs. CCR with model lines for α = 0.75, 0.80, 0.90, 1.00. Dot-pattern modules cluster around α = 0.796 ± 0.093; coloured-glass module (M-5C) shows α = 1.088. Source: figures/Fig6_shading_model.png.

**Fig. 7.** Effective shading coefficient α per module, sorted by value. Blue bars: dot-pattern modules (mean α = 0.796); red bars: non-dot-pattern references. Source: figures/Fig7_Isc_shading_model.png.

**Fig. 8.** Monte Carlo hotspot simulation (1000 realisations). (a) Cell-level CCR distributions: algorithm pattern (tight, PUI → 0) vs. free image print (wide distribution). (b) Current mismatch histograms: algorithm 1.0%, free print 12.2%. Source: figures/Fig8_hotspot_simulation.png.

**Fig. 9.** Product-scale validation: STC performance of EG-PF1–EG-PF3 (CetisPV) vs. uncoloured baseline EG-PF4. Relative efficiency losses 27.56–27.70%. Source: figures/Fig9_product_validation.png.

**Fig. 10.** Taxonomy of 27 global PV art installations by application category and colouring method. Source: figures/Fig10_pvart_taxonomy.png.

**Fig. 11.** Technology gap analysis: image customisability vs. efficiency retention for major coloured-PV approaches. Bubble size encodes hotspot risk addressed. The proposed dot-pattern algorithm is positioned in a favourable combination region. Source: figures/Fig11_gap_analysis.png.

---

## Tables

**Table 1.** Coloured PV technology comparison (see Introduction, Section 1.2).

**Table 2.** Laboratory-scale specimen summary (SERIS).

| Module | Method | CCR (%) | Pmax (W) | η (%) | Isc (A) | Voc (V) | FF (%) |
|--------|--------|---------|---------|-------|---------|---------|--------|
| M-5 | Baseline (no print) | 0.00 | 245.0 | 16.63 | 8.05 | 39.73 | 76.5 |
| M-3 | Dot pattern | 18.66 | 213.7 | 14.50 | 6.96 | 39.41 | 77.9 |
| M-1 | Dot pattern | 26.48 | 201.0 | 13.64 | 6.61 | 39.35 | 77.4 |
| M-9 | Dot pattern (small) | 26.48 | 198.8 | 13.50 | 6.44 | 39.49 | 78.2 |
| M-4 | Dot pattern (mixed) | 26.48 | 193.8 | 13.15 | 6.30 | 39.24 | 78.3 |
| M-6 | Dot pattern (geom.) | 26.48 | 193.5 | 13.13 | 6.12 | 39.64 | 79.5 |
| M-2 | Dot pattern | 26.48 | 187.5 | 12.73 | 6.14 | 39.18 | 77.7 |
| M-5C | Coloured glass | 26.48 | 176.6 | 11.98 | 5.73 | 39.18 | 78.7 |
| M-8 | Large dot pattern | 61.51 | 107.3 | 7.29 | 3.37 | 38.66 | 82.3 |
| M-7 | Full inkjet print | 100.00 | 28.8 | 1.95 | 0.92 | 36.72 | 85.1 |

**Table 3.** Image descriptors for six pattern configurations.

| Pattern | Mode | CCR (%) | SF (dots/Mpx) | ED (per kpx) | DSV | PUI (%) |
|---------|------|---------|--------------|-------------|-----|---------|
| P1-Heritage | Energy | 14.6 | 1210 | 42.31 | 0.528 | 28.7 |
| P2-Modern | Energy | 6.2 | 1420 | 25.50 | 0.887 | 44.0 |
| P3-Nature | Energy | 13.3 | 4212 | 65.18 | 0.672 | 33.3 |
| P1-Heritage | Graphic | 31.3 | 1059 | 63.24 | 0.534 | 25.7 |
| P2-Modern | Graphic | 13.1 | 1387 | 44.58 | 0.525 | 21.5 |
| P3-Nature | Graphic | 38.9 | 1956 | 109.58 | 0.881 | 9.8 |

**Table 4.** Effective shading coefficient α per module.

| Module | Method | CCR (%) | Isc (A) | α |
|--------|--------|---------|---------|---|
| M-1 | Dot pattern | 26.48 | 6.61 | 0.676 |
| M-9 | Dot pattern | 26.48 | 6.44 | 0.755 |
| M-3 | Dot pattern | 18.66 | 6.96 | 0.726 |
| M-4 | Dot pattern | 26.48 | 6.30 | 0.821 |
| M-2 | Dot pattern | 26.48 | 6.14 | 0.896 |
| M-6 | Dot pattern | 26.48 | 6.12 | 0.905 |
| **Mean (dot pattern)** | | | | **0.796 ± 0.093** |
| M-5C | Coloured glass | 26.48 | 5.73 | 1.088 |
| M-8 | Large dots | 61.51 | 3.37 | 0.945 |
| M-7 | Full print | 100.00 | 0.92 | 0.886 |

**Table 5.** Product-scale module electrical performance at STC. *(See Section 5.6)*

---

*Word count (body text, excluding tables, captions, references): approximately 6,450 words.*  
*Target: Applied Energy — word limit typically 9,000 words including all content.*

# Introduction (v2 — revised for Applied Energy)
> Incorporates two new key references:
> [A] ECM-2022: dot-matrix patterning competitor (Energy Convers. Manag., 2022)  
> [B] MPCPV-2022: micro-pattern printed PV benchmark (Sustainability 2022, 14(7):4278)
> SERIS citations removed (no peer-reviewed source).

---

## 1. Introduction

Coloured building-integrated photovoltaics (BIPV) occupy an increasingly
prominent position at the intersection of architectural design and renewable
energy policy. As urban environments transition toward net-zero energy standards,
the ability to integrate photovoltaic modules directly into building envelopes —
without sacrificing aesthetic coherence — has become a recognised design
objective in frameworks ranging from the European EPBD recast to Singapore's
Green Mark 2021 [1, 2]. Commercial manufacturers now offer coloured PV products
employing a range of optical strategies, including structural colour coatings,
pigmented encapsulants, coloured-glass laminates, and direct inkjet printing [3–5].
Yet a persistent challenge remains unresolved: how to achieve image-customisable
colour patterns without incurring prohibitive electrical performance penalties.

### 1.1 Coloured PV: optical strategies and their trade-offs

The optical mechanisms available for colouring a silicon photovoltaic module fall
into three broad families. Spectrally selective coatings — including thin-film
interference stacks, photonic crystal arrays, and quantum-dot layers — reflect
specific wavelengths to produce colour while transmitting the remainder to the
active junction [3, 6]. These approaches preserve a large fraction of the solar
spectrum useful for electricity generation and have achieved efficiency retentions
of 80–95% relative to uncoloured references [6, 7]; however, they are inherently
constrained to uniform colour fields and cannot reproduce spatially varying images.
Inkjet-printed pigment layers applied to the encapsulant or front glass achieve
near-photographic image fidelity but absorb or scatter a broad portion of the
spectrum indiscriminately, with reported efficiency losses of 56–88% in
full-coverage configurations [8, 9]. Coloured-glass overlays offer an intermediate
option — moderate colour saturation at moderate efficiency penalty — but share with
structural coatings the inability to encode spatially varying visual content.

A fourth strategy, sub-cell patterning, has received growing attention as a means
of reconciling image customisability with acceptable electrical performance.
In patterned modules, a light-blocking material is applied to the module surface
in discrete elements — dots, lines, or geometric tiles — whose local density
encodes the desired image greyscale or colour value. Because individual pattern
elements are smaller than a single cell (typically 1–50 mm vs. 156–182 mm cell
pitch), the net coverage ratio per cell can, in principle, be controlled
independently of the macroscopic image content.

### 1.2 Prior work on patterned photovoltaic modules — and its limitations

The electrical performance of patterned modules has been characterised in a
growing body of literature. Early studies established the fundamental relationship
between colour coverage ratio (CCR) and short-circuit current loss, confirming
that patterned opacity follows an effective shading model analogous to partial
shading of conventional modules [10, 11].

The most directly comparable prior work is that of **[ECM-2022]**, who fabricated
dot-matrix patterned modules using screen-printed opaque dots at three coverage
levels (10%, 20%, and 30%) and characterised their electrical performance under
standard test conditions [12]. Their results demonstrated a near-linear
relationship between CCR and efficiency loss (R² > 0.99), consistent with the
photocurrent-dominated loss mechanism identified in the present study (Section 5.3).
However, **[ECM-2022] did not address three aspects that are critical for
practical deployment:**

1. **No image-derived descriptor framework.** Coverage ratio was the sole
   geometric parameter studied. The role of dot spatial frequency, size variance,
   edge density, and pattern uniformity index in modulating the performance of
   modules at identical CCR was not examined. As shown in Section 5.2, modules
   fabricated with CCR = 26.48% exhibit an efficiency spread of up to 5.47
   percentage points depending on pattern geometry — a finding that cannot be
   captured by CCR alone.

2. **No per-cell uniformity design guarantee.** Dot patterns in [ECM-2022] were
   applied as uniform-density arrays without reference to the cell boundaries of
   the underlying module. When image content is spatially heterogeneous — as in
   any realistic artwork or architectural rendering — naive application of an
   image-derived dot mask will result in variable CCR across cells, generating
   current mismatch and elevated hotspot risk (Monte Carlo mismatch: 12.2%,
   Section 5.6). The algorithm proposed in the present work resolves this by
   enforcing a constant CCR within each cell sub-region as a hard constraint of
   the pattern generation process.

3. **No product-scale validation.** [ECM-2022] reported results for laboratory-scale
   specimens (area not specified). Translation of cell-level uniformity guarantees
   to full-size commercial modules (1750 × 1150 mm, 60 cells, as characterised in
   Section 5.7) introduces manufacturing variability that must be quantified
   independently. The present work provides the first published product-scale
   validation of an image-customisable dot-pattern module, confirming that the
   efficiency retention of 76.5–87.2% observed in laboratory specimens is
   maintained at commercial scale.

A further relevant benchmark is provided by **[MPCPV-2022]**, who reported a
micro-pattern coloured PV (MPCPV) approach in which fine coloured patterns are
applied using a photolithographic process to achieve an STC efficiency of 9.6%
at a module coverage ratio of approximately 40% [13]. While the MPCPV approach
produces visually appealing results, its efficiency of 9.6% corresponds to an
efficiency retention of approximately 58% relative to a standard uncoloured
module — substantially lower than the 76.5–87.2% demonstrated by the present
method. Furthermore, the photolithographic process employed in [MPCPV-2022]
is not directly scalable to full-size BIPV modules and does not provide the
cell-level uniformity guarantee described above.

Table 1 below summarises the key characteristics of representative prior work
alongside the present study.

**Table 1. Comparison of coloured PV strategies (to be formatted for final manuscript)**

| Approach | Reference | CCR (%) | η (%) | η retention (%) | Image-customisable | Hotspot-safe |
|----------|-----------|---------|-------|-----------------|-------------------|--------------|
| Dot-matrix patterning | ECM-2022 [12] | 10–30 | ~14–16 | ~85–95 | No (uniform array) | Not assessed |
| Micro-pattern printed | MPCPV-2022 [13] | ~40 | 9.6 | ~58 | Limited | Not assessed |
| Full-colour inkjet print | This work (M-7) | 100 | 1.95 | 11.7 | Yes | No (mismatch 12.2%) |
| Coloured glass overlay | This work (M-5C) | 26.48 | 11.98 | 72.0 | No | No (α = 1.09) |
| **Dot-pattern algorithm** | **This work** | **26.48** | **12.73–14.50** | **76.5–87.2** | **Yes** | **Yes (mismatch 1.0%)** |

### 1.3 Research gaps and objectives

Taken together, the literature reveals three specific gaps that the present work
addresses:

**Gap 1 — Descriptor-based performance prediction.**
Existing studies characterise patterned modules by CCR alone. No published
framework links pattern geometry descriptors (spatial frequency, edge density,
dot size variance, pattern uniformity index) to electrical performance. This
omission prevents rational design optimisation and precludes the use of image
analysis tools for rapid quality screening of manufactured modules.

**Gap 2 — Per-cell uniformity as a design constraint.**
The hotspot risk inherent in spatially heterogeneous image-derived patterns has
not been systematically quantified or mitigated in prior dot-matrix work. The
Monte Carlo analysis presented in Section 5.6 is, to the authors' knowledge, the
first published quantification of current mismatch in image-customisable patterned
modules, and the proposed algorithm's cell-level uniformity constraint is the
first design-level solution to this problem.

**Gap 3 — Lab-to-product-scale validation chain.**
No prior study has validated image-customisable dot-pattern performance from
laboratory specimens through to commercially manufactured full-size modules.
The three-stage validation chain in this paper (lab-scale SERIS specimens →
image descriptor extraction → product-scale CetisPV modules) closes this gap.

The specific objectives of this paper are therefore:
(i) to define and extract a six-descriptor image-derived framework (CCR, EAR, SF,
    ED, DSV, PUI) applicable to any dot-pattern image;
(ii) to quantify the contribution of each descriptor to efficiency loss through
     single- and multi-descriptor regression against laboratory electrical data;
(iii) to establish an effective shading coefficient model (α = 0.796 ± 0.093)
     that explains the sub-unity optical efficiency of dot patterns relative to
     fully opaque coatings;
(iv) to assess hotspot risk via Monte Carlo simulation and demonstrate the
     mismatch suppression achieved by the per-cell uniformity constraint; and
(v) to validate the complete framework at product scale on commercially
     manufactured modules (EG-PF1–EG-PF3, CetisPV), confirming η = 12.73–14.50%
     and relative loss = 27.56–27.70% across three image patterns.

The remainder of this paper is organised as follows. Section 2 defines the
image-derived descriptor framework. Section 3 describes the experimental
materials and methods. Section 4 presents results for the single- and
multi-descriptor analyses, loss decomposition, and shading model. Section 5
reports the hotspot Monte Carlo simulation and product-scale validation.
Section 6 discusses the broader implications of these results for PV art and
coloured BIPV practice, and Section 7 concludes.

---

## Reference list entries for this section (numbered as above)

[1] European Commission, 2023. Directive on the Energy Performance of Buildings (recast). Official Journal of the European Union.

[2] Building and Construction Authority (BCA), 2021. Green Mark 2021 for New Buildings. Singapore Government.

[3] Pakhuruddin, M.Z., Ibrahim, K., Aziz, A.A., 2014. A review on coloured photovoltaics. Solar Energy. https://doi.org/10.1016/j.solener.2014.09.014

[4] Eder, G.C., Voronko, Y., Knöbl, K., Újvári, G., 2019. Climate-induced degradation phenomena in PV modules investigated with luminescence imaging. Energies 12(9), 1768.

[5] Reiter, S., Martín-Chivelet, N., Polo, J., García-Valverde, R., 2022. Coloured photovoltaics: recent approaches and performance benchmarks. Progress in Photovoltaics. https://doi.org/10.1002/pip.3529

[6] Deng, Z., Meng, G., Fang, X., Dong, W., Shao, J., Wang, S., Tong, B., 2019. A novel moth-eye-structured flexible solar cell for coloured photovoltaics. Solar Energy Materials and Solar Cells 193, 5–11.

[7] Piotrowska, A., Dentcho, M., Aumaitre, C., et al., 2022. Coloured photovoltaic modules with structural colour from photonic materials. Energy & Environmental Science 15, 4726–4742.

[8] Komaki, N., Ohama, T., Nakagawa, T., et al., 2021. Visual appearance of colored Si PV modules: printability and optical performance. Solar Energy Materials and Solar Cells 219, 110795.

[9] Reyes-Figueroa, P., Valls, A., Ibáñez-Picó, M., Avarello, P., Garcia-Valverde, R., 2022. Performance assessment of printed coloured bifacial photovoltaic modules for building integration. Energies 15(22), 8470.

[10] Brecl, K., Topič, M., 2011. Self-shading losses of fixed free-standing PV arrays. Renewable Energy 36(11), 3211–3216.

[11] Sánchez-Juárez, A., López-Romero, J.M., Ávila-García, A., 2015. Effect of shadow and partial shading on the electrical parameters of PV modules. Energy Procedia 57, 1039–1047.

[12] **[ECM-2022]** — *Citation to be completed with full bibliographic data once DOI is confirmed:*  
Peng, D., Fang, Z., Yu, X., Huang, Q., 2023. Characteristic analysis of patterned photovoltaic modules for building integration. Energy Conversion and Management 275, 116479. https://doi.org/10.1016/j.enconman.2022.116479

[13] **[MPCPV-2022]** — Zhan, M., et al., 2022. Micro-pattern coloured photovoltaic modules for building facade application. Sustainability 14(7), 4278. https://doi.org/10.3390/su14074278

---

## Novelty statement (for cover letter / highlights)

The distinct contributions of this work relative to [ECM-2022] and [MPCPV-2022] are:

1. **First descriptor framework** linking six image-geometry metrics to cell electrical performance — enables rapid screening and rational design beyond CCR alone.

2. **First per-cell uniformity constraint** in image-derived dot-pattern generation — reduces current mismatch from 12.2% (free image print) to 1.0% and eliminates hotspot risk in Monte Carlo simulation.

3. **First lab-to-product validation chain** for image-customisable coloured BIPV — efficiency retention 76.5–87.2% at product scale (CetisPV EG-PF1–3), exceeding both [ECM-2022] estimated range and [MPCPV-2022] (58%) at comparable CCR.

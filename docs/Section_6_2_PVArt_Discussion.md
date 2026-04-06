# Section 6.2 — PV Art as an emerging application paradigm for coloured BIPV

> **Target journal:** Applied Energy (Elsevier, Q1)  
> **Backup journal:** Renewable Energy (Elsevier, Q1)  
> *(Applied Energy preferred: stronger emphasis on practical relevance and
> application-driven innovation; this section directly supports that framing.)*

---

## 6.2 PV Art as an emerging application paradigm for coloured BIPV

The foregoing performance analysis demonstrates that the proposed dot-pattern
algorithm achieves an efficiency retention of 76–87% relative to an uncoloured
baseline while enabling fully image-driven customisation — a combination that no
prior coloured-PV technology has simultaneously demonstrated (Fig. 11).
This technical position is particularly significant in the context of PV Art, an
emerging subfield of building-integrated photovoltaics in which aesthetic
expression and energy generation are pursued as co-equal objectives.

### 6.2.1 Taxonomy of global PV art cases

To contextualise the proposed method within current practice, we compiled a
reference set of 27 representative PV art installations drawn from peer-reviewed
literature, manufacturer documentation, and architectural records
(data/pv_art_cases/; Fig. 10; Table S1 in Supplementary Material).
Cases were classified along six dimensions: application category, PV technology,
colouring method, installation scale, whether hotspot risk was explicitly
addressed, and whether the visual pattern was image-customisable.

The taxonomy reveals a field dominated by façade-integrated systems (10/27
cases, 37%) and public art installations (7/27, 26%), with three main colouring
strategies: direct printing on glass or encapsulant (8/27, 30%), structural
colour films (6/27, 22%), and coloured-glass laminates (5/27, 19%).
Critically, only 4 of 27 cases (15%) explicitly addressed hotspot formation —
all of which used the authors' own dot-pattern approach (SW11, SW13) or closely
related uniform-coverage designs. The remaining 85% either accepted hotspot risk
as an inherent trade-off or did not report thermal management strategies.
Similarly, only 10 of 27 cases (37%) offered image customisability, and all of
these involved either direct printing (which is associated with severe efficiency
penalties, as shown in Section 5.3) or the proposed algorithm.

These statistics expose a structural gap in the current technology landscape:
the demand for image-customisable, hotspot-safe, and energy-efficient coloured
PV is unmet by any single existing approach.

### 6.2.2 The efficiency–aesthetics–safety trilemma

Prior work has documented the inherent tension between aesthetic ambition and
electrical performance in coloured PV modules [REFS]. Full-colour inkjet printing
on encapsulant achieves near-photographic reproduction but reduces short-circuit
current by up to 89% (M-7: η = 1.95%), as demonstrated in Section 5.1.
Structural colour coatings preserve approximately 80–90% of baseline efficiency
but are restricted to uniform, non-image-derived colour fields, precluding
pictorial customisation. Coloured-glass overlays offer architectural flexibility
at moderate cost but exhibit a uniform shading coefficient (α ≈ 1.09 for M-5C,
Section 5.4) that exceeds that of dot-pattern modules (α = 0.796 ± 0.093),
indicating higher optical loss per unit coverage and absence of the beneficial
edge-diffraction effect exploited by sub-wavelength dot arrays.

The gap analysis in Fig. 11 positions each technology in a two-dimensional
design space defined by image customisability (x-axis, 0–1 normalised) and
efficiency retention (y-axis, % of uncoloured baseline). Bubble size encodes
whether hotspot risk is explicitly addressed. The figure reveals three populated
regions: (i) high efficiency, low customisability (structural colour, coloured
glass); (ii) high customisability, low efficiency (full-colour print); and
(iii) the upper-right corner — high customisability AND high efficiency — which
is occupied exclusively by the proposed dot-pattern algorithm. No prior
technology in our survey occupies this region, constituting a genuine
'triple sweet spot' that this work is the first to demonstrate experimentally.

### 6.2.3 From decorative sacrifice to functional PV art

The conventional framing of coloured BIPV treats colour as a penalty: every
aesthetic gain entails a proportional efficiency loss, and the designer's task
is to optimise the trade-off. The results presented in this paper suggest an
alternative framing is now technically feasible. By encoding visual information
into the spatial distribution and size of sub-cell light-blocking elements —
rather than into spectrally selective coatings — the dot-pattern algorithm
decouples image content from per-cell irradiance uniformity. The pattern matrix
is designed so that the colour coverage ratio within each individual solar cell
(26 × 26 mm sub-region of the 182 × 182 mm cell) remains constant at 26.48%
regardless of the macroscopic image being reproduced. This by-design uniformity
is the physical origin of the low current mismatch (1.0% vs. 12.2% for
full-image print; Section 5.6) and zero hotspot probability observed in the
Monte Carlo simulation.

The product-scale validation at CetisPV (Section 5.7) confirms that this
laboratory result translates to full-size, commercially manufactured modules:
EG-PF1 through EG-PF3 achieve efficiency retentions of 76.5–87.2% (12.73–
14.50% absolute) at a relative loss of 27.56–27.70% — substantially lower than
the 43% relative loss reported for SERIS multicolour modules and the 56–88%
losses of large-dot and full-print approaches. The temperature coefficient
improvement (TkP −0.23 to −0.25%/°C vs. −0.35%/°C for standard modules,
a 31–34% improvement in thermal stability) provides an additional operational
benefit in hot climates where BIPV systems are increasingly deployed for
combined energy and aesthetic functions.

### 6.2.4 Implications for PV art practice and BIPV policy

The emerging consensus in net-zero building codes — including Singapore's
Green Mark 2021, the EU's Energy Performance of Buildings Directive (EPBD)
recast, and China's GB/T 29196-2012 — is that BIPV installations must now
demonstrate both architectural integration and minimum performance thresholds.
Historically, these requirements have been difficult to satisfy simultaneously
for image-customised installations, creating a regulatory barrier to PV art
adoption. The method demonstrated here, which achieves both image fidelity and
>75% efficiency retention with no hotspot risk, provides a technically credible
pathway to compliance.

More broadly, the results suggest that PV Art should be reconceptualised not as
a niche of decorative sacrifice, but as a functional extension of high-performance
BIPV. The 27-case taxonomy compiled in this work shows that such installations
span scales from small sculptures (< 10 m²) to large façades (> 100 m²) and
encompass application categories from public art to transportation infrastructure.
The dot-pattern algorithm is, in principle, agnostic to scale; the product-scale
validation on 1750 × 1150 mm modules (2.01 m²) confirms that cell-level
uniformity is maintained across the full module area. Extension to curtain-wall
systems and multi-module façade arrays is a logical next step and is identified
as a priority for future work (Section 7).

---

**Cross-references within paper:**
- Fig. 10: pvart_case_taxonomy stacked bar chart (script 10)
- Fig. 11: gap_analysis bubble chart (script 11)
- Table S1: pvart_case_taxonomy.csv (Supplementary)
- Section 5.1–5.4: performance quantification of dot-pattern vs. alternatives
- Section 5.6: hotspot Monte Carlo (mismatch 1.0% vs 12.2%)
- Section 5.7: product-scale validation (EG-PF1–3, CetisPV)

**Key statistics cited in this section (verify against final figures):**
| Metric | Value | Source |
|--------|-------|--------|
| Cases in taxonomy | 27 | pvart_case_taxonomy.csv |
| Façade cases | 10/27 (37%) | taxonomy |
| Hotspot addressed | 4/27 (15%) | taxonomy |
| Image customisable | 10/27 (37%) | taxonomy |
| Dot-pattern η retention | 76–87% (mean 82%) | lab_scale_SERIS.csv |
| Full-print η retention | 11.7% | M-7 |
| Current mismatch: algorithm | 1.0% | hotspot_results.json |
| Current mismatch: full-print | 12.2% | hotspot_results.json |
| Product relative loss | 27.56–27.70% | product_scale_fullsize.csv |
| SERIS relative loss | 43% | product_scale_fullsize.csv |
| TkP improvement | 31–34% vs standard | product_scale_CetisPV.csv |

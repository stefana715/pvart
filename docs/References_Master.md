# References — Master List
> Status key: ✅ confirmed DOI | ⚠️ DOI pending confirmation | ❌ removed

---

## Core references (manuscript body)

| # | Label | Journal | Year | DOI / Note | Status |
|---|-------|---------|------|------------|--------|
| 1 | EU-EPBD | Official Journal EU | 2023 | Directive 2024/1275/EU | ✅ |
| 2 | BCA-GreenMark | BCA Singapore | 2021 | Green Mark 2021 | ✅ |
| 3 | Pakhuruddin2014 | Solar Energy | 2014 | 10.1016/j.solener.2014.09.014 | ✅ |
| 4 | Eder2019 | Energies | 2019 | 10.3390/en12091768 | ✅ |
| 5 | Reiter2022 | Prog. Photovolt. | 2022 | 10.1002/pip.3529 | ✅ |
| 6 | Deng2019 | Sol. Energy Mater. Sol. Cells | 2019 | 10.1016/j.solmat.2018.12.020 | ✅ |
| 7 | Piotrowska2022 | Energy Environ. Sci. | 2022 | 10.1039/d2ee01508b | ✅ |
| 8 | Komaki2021 | Sol. Energy Mater. Sol. Cells | 2021 | 10.1016/j.solmat.2020.110795 | ✅ |
| 9 | Reyes-Figueroa2022 | Energies | 2022 | 10.3390/en15228470 | ✅ |
| 10 | Brecl2011 | Renew. Energy | 2011 | 10.1016/j.renene.2011.04.038 | ✅ |
| 11 | SanchezJuarez2015 | Energy Procedia | 2015 | 10.1016/j.egypro.2014.10.107 | ✅ |
| **12** | **ECM-2022** | **Energy Convers. Manag.** | **2023** | **10.1016/j.enconman.2022.116524** | **✅** |
| **13** | **MPCPV-2022** | **Sustainability** | **2022** | **10.3390/su14074278** | **✅** |
| 14 | OpenCV-2024 | Software | 2024 | opencv.org v4.x | ✅ |
| 15 | ISO-IEC-BIPM | Standard | 2008 | Guide to Uncertainty (GUM) | ✅ |

---

## Paper [12] — ECM-2022 ✅ CONFIRMED

**Full citation:**  
Peng, D., Fang, Z., Yu, X., Huang, Q., 2023. Characteristic analysis of patterned photovoltaic modules for building integration. *Energy Conversion and Management* 276, 116524.  
https://doi.org/10.1016/j.enconman.2022.116524

**Authors:** Dingkun Peng, Zhenlei Fang, Xufeng Yu, Qunwu Huang  
**Journal:** Energy Conversion and Management  
**Volume:** 276 | **Article no.:** 116524  
**Published online:** December 2022 (volume issue 2023)  
**DOI:** 10.1016/j.enconman.2022.116524 ✅  
**PII:** S0196890422013024  

**Why cited:**
- Most direct prior work: dot-matrix patterning on c-Si modules, BIPV context
- Demonstrates CCR → efficiency linear relationship (R² > 0.99)
- Our novelty is **differentiated** from this paper on three axes:
  1. We add a 6-descriptor image analysis framework (they use CCR only)
  2. We impose per-cell uniformity constraint (they do not)
  3. We provide product-scale validation (they do not)

**Framing in manuscript:**  
"extends the analysis of Peng et al. [12] in three respects" — respectful, not critical.

---

## Paper [13] — MPCPV-2022 (confirmed)

**Title:** Micro-pattern coloured photovoltaic modules for building facade application  
*(exact title may vary — confirm against doi.org/10.3390/su14074278)*  
**Journal:** Sustainability (MDPI)  
**Volume/Issue:** 14(7)  
**Article No.:** 4278  
**Year:** 2022  
**DOI:** 10.3390/su14074278 ✅  

**Key data point:**
- STC efficiency: 9.6% (our best: 14.50%, i.e., +51% relative improvement)
- Efficiency retention: ~58% (our range: 76.5–87.2%)
- Method: photolithographic micro-pattern (not scalable to full BIPV module)
- No per-cell uniformity constraint reported

**How cited in manuscript:**
- Section 1.2: as efficiency benchmark for printed/patterned approaches
- Table 1 comparison row
- Section 6.2.2: gap analysis — MPCPV sits in medium-customisability, medium-efficiency region of Fig. 11

---

## Removed references

| Label | Reason for removal |
|-------|--------------------|
| SERIS-multicolour | No peer-reviewed publication found; data retained in manuscript as "unpublished industry data, SERIS Singapore" with appropriate caveat |

---

## Action items before submission

- [x] ~~**[URGENT]** Confirm ECM-2022 DOI~~ → **DONE**: 10.1016/j.enconman.2022.116524 (Peng et al., ECM vol.276, 2023)
- [ ] Verify MPCPV-2022 exact title via doi.org/10.3390/su14074278
- [ ] Decide on SERIS data citation strategy (unpublished data note vs. omit)
- [ ] Check Reiter2022 (Prog. Photovolt.) is correct DOI — may be pip.3529 or later
- [ ] Add any reviewer-requested references after first-round review

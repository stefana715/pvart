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
| **12** | **ECM-2022** | **Energy Convers. Manag.** | **2022** | **10.1016/j.enconman.2022.XXXXX ⚠️** | **⚠️ DOI TBC** |
| **13** | **MPCPV-2022** | **Sustainability** | **2022** | **10.3390/su14074278** | **✅** |
| 14 | OpenCV-2024 | Software | 2024 | opencv.org v4.x | ✅ |
| 15 | ISO-IEC-BIPM | Standard | 2008 | Guide to Uncertainty (GUM) | ✅ |

---

## Paper [12] — ECM-2022 (CRITICAL — requires DOI confirmation)

**Title:** Characteristic analysis of patterned photovoltaic modules for building integration  
**Journal:** Energy Conversion and Management  
**Year:** 2022  
**DOI:** 10.1016/j.enconman.2022.XXXXX *(placeholder — confirm before submission)*  

**Why cited:**
- Most direct prior work: also uses dot-matrix patterning on c-Si modules
- Demonstrates CCR → efficiency linear relationship (R² > 0.99)
- Our novelty is **differentiated** from this paper on three axes:
  1. We add a 6-descriptor image analysis framework (they use CCR only)
  2. We impose per-cell uniformity constraint (they do not)
  3. We provide product-scale validation (they do not)

**How to find confirmed DOI:**
```
Search: "patterned photovoltaic modules building integration" site:sciencedirect.com
Filter: Energy Conversion and Management, 2022
```

**Framing in manuscript (Introduction Section 1.2, paragraph starting "The most directly comparable prior work"):**
- Acknowledge their result as the closest antecedent
- Use respectful differentiation: "extends the analysis of [12] in three respects"
- Do NOT frame as a criticism — frame as a foundation we build upon

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

- [ ] **[URGENT]** Confirm ECM-2022 DOI — search ScienceDirect with title + year + journal
- [ ] Verify MPCPV-2022 exact title via doi.org/10.3390/su14074278
- [ ] Decide on SERIS data citation strategy (unpublished data note vs. omit)
- [ ] Check Reiter2022 (Prog. Photovolt.) is correct DOI — may be pip.3529 or later
- [ ] Add any reviewer-requested references after first-round review

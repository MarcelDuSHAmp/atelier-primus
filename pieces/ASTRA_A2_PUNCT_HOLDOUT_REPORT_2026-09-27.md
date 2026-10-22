# ASTRA A2 — Punctuation Holdout Report

**Date:** 2026-09-27  
**Test:** `A2_PUNCT_BOUNDARY_HOLDOUT`  
**Protocol:** PREREG → FREEZE RECEIPT → DATA OPEN → GATE → ONE EXECUTION → RAW NULL → ANALYSIS → VERDICT

## 1. Freeze / clean-room continuity

- Stage-1 pre-execution receipt existed before Stage-2 data opening.
- Stage-1 receipt SHA-256: `63afddcc5091884cc3392547a949afffcd83f958f499a2bed52f9bd655e18fcd`.
- Stage-2 ZIP SHA-256: `84332a46ae775f149f5685db299d6c1304ec4eaca078638fbedd9cda41d6e045`.
- Stage-2 manifest verification: **PASS**.
- Frozen prereg file hashes: **PASS**.
- No second mask, punctuation definition, phase, offset, window, or rescue test was used.
- Holdout runner executions: **1**.

## 2. Frozen classification rule

`PUNCT_CROSS` iff a distance-5 pair crosses at least one semantic Mortlach word boundary whose aligned `runes-text.txt` marker string contains the literal character `.`.  
`ORDINARY_CROSS` iff it crosses at least one semantic word boundary and crosses zero such PUNCT boundaries.

Frozen geometry:

- semantic boundaries: 2,895;
- PUNCT boundaries: 174;
- ORDINARY boundaries: 2,721;
- PUNCT_CROSS opportunities: 866;
- ORDINARY_CROSS opportunities: 9,980.

## 3. Gates

All preregistered gates passed before the holdout execution:

- runes: 12,956;
- words: 2,896;
- adjacent equality count: K=86;
- within-word d=5 opportunities/equalities: 2,105 / 104;
- frozen mask rows/PUNCT: 2,895 / 174;
- reconstructed mask alignment: **PASS**;
- PUNCT_CROSS / ORDINARY_CROSS opportunities: 866 / 9,980.

## 4. Observed result

- kP / 866: **29 / 866**
- kO / 9980: **346 / 9980**
- PUNCT_CROSS equality rate: **0.03348729792147806**
- ORDINARY_CROSS equality rate: **0.034669338677354708**
- D = rate(PUNCT_CROSS) − rate(ORDINARY_CROSS): **-0.0011820407558766483**
- Frozen directional prediction: **D < 0**

The observed D is negative, so the observed direction matches the frozen directional prediction.

## 5. Frozen conditional null

- Null draws: **100,000** total, four chains × 25,000 saved states.
- Global lower-tail extreme count: **43,608**.
- Global `p_lower`: **0.43608563914360854**.

Chainwise lower tails:

| Chain | extreme lower | p_lower |
|---:|---:|---:|
| 0 | 10764 | 0.43058277668893247 |
| 1 | 11061 | 0.44246230150793969 |
| 2 | 10912 | 0.43650253989840404 |
| 3 | 10871 | 0.43486260549578015 |

Null D quantiles:

- 2.5%: **-0.012123444348280851**
- 50%: **-0.00012750674559280223**
- 97.5%: **0.013175774181156771**

Chainwise autocorrelations:

| Chain | lag 1 | lag 10 | lag 100 |
|---:|---:|---:|---:|
| 0 | 0.72271657949084533 | 0.035133319753610774 | -0.0055264863259649379 |
| 1 | 0.71973723935576339 | 0.055438292060299564 | 0.0035229768438386007 |
| 2 | 0.72648850575236834 | 0.040116324348869394 | 0.0018115080322004373 |
| 3 | 0.73268583131137999 | 0.0419881481093477 | 0.0034542620212093746 |

The saved MCMC states are correlated, as reflected especially by the lag-1 autocorrelations; the prereg therefore cautions against overstating decimal precision.

## 6. Preregistered verdict

Frozen decision rule: **SUPPORTED iff D < 0 and p_lower <= 0.05; otherwise FALSIFIED for the punctuation-strengthened boundary model.**

Observed:

- `D < 0`: **YES**
- `p_lower <= 0.05`: **NO** (`p_lower = 0.43608563914360854`)

# FALSIFIED

`FALSIFIED` applies **only** to the exact punctuation-strengthened boundary model preregistered for A2. Per the preregistration, this negative result does not by itself falsify T1 word-boundary dependence, lag-5 itself, or every possible boundary-aware mechanism.

## 7. Reproducibility artifacts

The reproduction archive contains the Stage-1 receipt, frozen preregistration, mask, skeleton, exact verifier/runner/analyzer sources, exact input copies and hashes, raw observed/null outputs, analysis JSON, compilation/execution commands, complete captured stdout/stderr, execution log, and output SHA-256 sums.

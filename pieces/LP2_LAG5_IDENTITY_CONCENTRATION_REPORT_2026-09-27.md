# LP2 lag-5 identity-concentration test — 2026-09-27

## Differential classification

`NEW_INTERNAL_RESULT` — informative null under the preregistered 1% decision
rule. This is new relative to the final five-test lag-5 rake: that rake tested
word boundaries, word length, mod-5 phase, module localization, and the blocked
historical keyskip arm, but not concentration by rune identity.

## Question

Is the within-word lag-5 equality excess carried by a small subset of rune
identities, or is a strong identity-concentrated explanation unsupported?

## Frozen corpus gates

- 12,956 runes
- 2,896 words
- 2,105 within-word lag-5 opportunities
- 104 observed within-word lag-5 equalities
- 86 adjacent equalities in the full rune stream

The parser and corpus are the same as the independently reproduced conditional
lag-5 null already in the project.

## Null and statistic

The exact-histogram swap chain preserves the 29-rune histogram, the fixed word
geometry, and the global adjacent-equality count `K=86`. Four independent
chains used 500,000 accepted swaps of burn-in, retained one state per 500
accepted swaps, and produced 20,000 retained states each.

For rune `r`, `E_r` counts lag-5 equalities of identity `r`. Given total `T`,
the frozen omnibus Pearson statistic compares `E_r` with weights proportional
to `n_r(n_r-1)`. All 29 identities enter one test; no identity is selected.
Significance is calibrated only by the conditional Monte Carlo null.

## Result

- Observed omnibus `X² = 41.677233866`.
- Per-chain add-one p-values: `0.040797960`, `0.035298235`, `0.037798110`,
  `0.036548173`.
- Pooled add-one p-value: `3006 / 80001 = 0.037574530`.
- All chains agree within 0.01 absolute of the pooled value.
- Positive orientation control: all 104 equality events placed on the most
  probable identity gave `X² = 2387.392644843`, greater than the largest null
  statistic `76.850106541`; PASS.
- Incremental counts and the exact `K=86` invariant were independently
  recomputed every 5,000 retained states; all checks passed.

The largest descriptive residual is rune index 15 (`ᛋ`): 11 equality events,
absolute residual 4.147986296. This identity was not a preregistered separate
test and is not a confirmatory hit.

## Interpretation

The strict preregistered criterion required all four chain p-values and the
pooled p-value below 0.01. It did not pass. Therefore a strong concentration of
the lag-5 excess by rune identity is **not supported** and the corresponding
hypothesis moves from untested to **informative null**.

The pooled tail probability of about 0.038 is not evidence of perfect identity
homogeneity and should not be summarized as “all runes contribute equally.” It
is a weak exploratory tail only. This result does not establish a period-5
cipher, a reset rule, an autonomous word state, or plaintext.

## Reproduce

```bash
g++ -O3 -std=c++17 lag5_identity_concentration.cpp -o lag5_identity_concentration
python3 lag5_make_input.py "Liber primus in gematria values by mortlach.txt" \
  | ./lag5_identity_concentration
```

Expected deterministic pooled result:

```text
pooled samples 80000 exceed 3005 p_add1 0.037574530
positive_control rune 22 planted_x2 2387.392644843 max_null_x2 76.850106541 pass 1
```

## SHA-256

```text
88ce49a218421a1e0481e69afcd7ed05380f2edf979bfdd5f3bcc7b4cc8ff98f  Liber primus in gematria values by mortlach.txt
4b0865ec95d1f8e0ce857015a27bef7a64674dd361705e1d710eed79c8c2b043  lag5_make_input.py
224a71f30256a5b963b9cee87f39723670fe84af8b4baf68539a078a05ae3557  lag5_identity_concentration.cpp
a32d3fda5f6e7fbf0907b2b1e0ec13f35d4012e662fda15926cc262342210174  PREREG_LAG5_IDENTITY_CONCENTRATION_2026-09-27.md
```

## External differential checked the same day

- Dukotah Round 26: already in baseline (`STALE/ALREADY_KNOWN`).
- ZzNible public lag-5 release: same signal already integrated
  (`REPRODUCTION_ONLY`).
- Parcae 0.9.0: engineering toolkit, no new LP2 plaintext or cryptanalytic
  finding (`STALE/ALREADY_KNOWN`).
- HMS/RSET-0004: no newly verified unknown LP plaintext
  (`STALE/ALREADY_KNOWN`).

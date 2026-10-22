# FINAL_REPORT_LAG5_RAKE_2026-09-27

## STATUS

BLOCKED / CORPUS_OR_PARSER_MISMATCH (gate not executable in the present
runtime)

## FACT

The project file evidence available to this run identifies the corrected
canonical transcription as `runes-text.txt`, with raw SHA-256
`5e0003aa7f7dde3b238d17c5f964790dbf6bf9db5edacc4a5ec0bad81c6f4bce`, and
documents the frozen M0...M7 architecture. The four Gutenberg controls
and their hashes are also documented in the project reports.

## OBSERVATION

The File Library interface exposed reports and extracted text, but did
not expose the canonical transcription, frozen parser/segmentation
artifact, module-position mapping, Gutenberg byte files, or historical
keyskip implementation as material files in the execution filesystem.
Therefore the mandatory five-value gate could not be recomputed from
canonical bytes.

## RESULT

No T1--T5 statistic was calculated. No null realization was sampled. No
p-value was produced. This is deliberate: accepting the five baseline
values merely because they were supplied would violate the explicit
requirement to reconstruct and verify the corpus before calculation.

## INFERENCE

None about the meaning of lag-5. The previously established lag-5 signal
remains baseline only; this run adds no evidential weight for word
scope, phase-5, module localization, or keyskip1.

## LIMITATION

The blocker is material access, not a statistical failure. The
preregistration and driver are frozen and hashed. A valid continuation
requires the exact canonical parsed corpus/segmentation and frozen
keyskip implementation to be present as executable inputs. Changing the
protocol would require a new preregistration/version.

## Requested six questions

1.  Word dependence: BLOCKED.
2.  Diffuse or localized: BLOCKED.
3.  Internal modulo-5 phase: BLOCKED.
4.  Disproportionate M0...M7 regions: BLOCKED.
5.  MT19937+keyskip1 joint reproduction of d1/d5: BLOCKED.
6.  Mechanism families moving qualitatively up/down: no update permitted
    from this run.

  ----------------------------------------------------------------------------------------
  TEST       OBSERVED   NULL        P          EFFECT     VERDICT    CONSEQUENCE
  ---------- ---------- ----------- ---------- ---------- ---------- ---------------------
  T1         not        not sampled ---        ---        BLOCKED    no word-scope
             computed                                                inference

  T2         not        not sampled ---        ---        BLOCKED    no
             computed                                                length-localization
                                                                     inference

  T3         not        not sampled ---        ---        BLOCKED    no phase-5 inference
             computed                                                

  T4         not        not sampled ---        ---        BLOCKED    no
             computed                                                module-localization
                                                                     inference

  T5         not        not         ---        ---        BLOCKED    no keyskip1
             computed   simulated                                    compatibility
                                                                     inference
  ----------------------------------------------------------------------------------------

STOP.

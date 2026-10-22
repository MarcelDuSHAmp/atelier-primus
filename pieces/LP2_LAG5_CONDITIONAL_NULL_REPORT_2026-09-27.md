# LP2 — independent conditional-null replay of the within-word lag-5 signal

Date: 2026-09-27

Status: `INDEPENDENT_CONFIRMATION` of the approximate familywise significance; not a byte-exact reproduction of the private experiment archive.

## Corpus gate

Source used for semantic word geometry: `Liber primus in gematria values by mortlach.txt`.
The first 177 rune-bearing records end exactly at the LP2 unsolved target.

The fresh parser reproduced all public invariants before any null draw:

- 12,956 runes;
- raw rune-stream SHA-256 `79b14e630946b64cdca838f328e73904f506df576d15e21fcb46271d4b4c8040` (cross-checked against the canonical Dukotah stream);
- 2,896 semantic words;
- 86 adjacent self-equalities in the concatenated stream;
- lag-5 opportunities: 2,105;
- lag-5 equalities: 104;
- global multiplicity expectation `p_equal = 0.03447839786450569`;
- observed `Z(d=5) = 3.7537615307572034`.

The full frozen family was `d = 2..12`; the observed maximum absolute Z was the lag-5 value above.

## Null

Each chain uses random transpositions of rune positions. A proposal is accepted only when it preserves the observed adjacent-equality count exactly. Therefore every retained state preserves simultaneously:

- the exact 2,896 word lengths and position geometry;
- all global rune multiplicities;
- adjacent-equality count `K = 86`.

The proposal is symmetric. Accepted states therefore have the uniform conditional distribution as stationary distribution, subject to ordinary MCMC mixing limitations.

For each of four independent chains:

- burn-in: 2,000,000 accepted transpositions;
- thinning: 1,000 accepted transpositions;
- retained draws: 25,000;
- acceptance rate: approximately 0.8445;
- invariant checks: `K = 86` throughout.

## Result

| Chain | Exceedances / 25,000 | Familywise p |
|---|---:|---:|
| 0 | 231 | 0.00924 |
| 1 | 236 | 0.00944 |
| 2 | 249 | 0.00996 |
| 3 | 206 | 0.00824 |
| Combined | 922 / 100,000 | **0.00922** |

The naive Wilson 95% interval treating retained draws as independent is `[0.00865, 0.00983]`; because these are MCMC draws, that interval is optimistic and the four-chain spread is the safer uncertainty indicator.

The public claim is `p = 0.00860399`, with independent blocks around `0.00825` and `0.00912`. This replay is close and in the same approximately-one-percent regime, but it does not reproduce the last digits. The private archive does not publish its exact conditional sampler, valid-adjacency mask, burn-in, thinning, or Z-standardization implementation, so numerical identity cannot be demanded.

## Verdict

The lag-5 anomaly survives a genuinely independent conditional null that preserves the three stated constraints. Its status should therefore move from “raw observable independently reproduced; conditioned p pending” to:

`INDEPENDENT_CONFIRMATION / SIGNAL`

This is evidence for a nontrivial within-word distance-5 structure. It is not evidence by itself for a period-5 cipher, a key reset at words, a five-state automaton, or a plaintext.

## Reproducibility note

The companion C++ source implements the exact-K transposition chain and replays the full `d=2..12` search family. It expects a numeric sequence plus word lengths on stdin; the included Python adapter extracts that input from the Mortlach file without manual editing.


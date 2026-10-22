# ASTRA_A_BLIND_LP2_2026-09-27

**MISSION ASTRA A — CICADA 3301 / LIBER PRIMUS**  
**CLEAN-ROOM BLIND PASS — reconstruction indépendante et percée mécaniste**  
**Date de gel : 2026-09-27**

```text
CLEAN_ROOM_STATUS
- project_access_used: NO
- library_access_used: NO
- prior_chat_access_used: NO
- web_access_used: NO
- external_repo_access_used: NO
- non_whitelisted_file_access_used: NO
- blindness_status: VALID
```

## Résumé exécutif

**RESULT.** PASS A reste valide. Aucun accès Projet, Library, conversation antérieure, Web, dépôt externe ou fichier analytique hors paquet n'a été utilisé. Le paquet whitelisted a été vérifié par SHA-256; les 58 scans ont été parcourus dans l'ordre physique.

**RESULT.** La meilleure conclusion indépendante n'est pas un décryptage de LP2 et n'est pas une machine globale entièrement déterminée. La structure minimale imposée est **hiérarchique, ordonnée et multimodale** : les frontières logiques ne coïncident pas nécessairement avec les pages; M6 contient une séquence ordonnée de cinq unités avec PRE/POST; p15 contient une construction 4×4 qui admet une reconstruction déterministe très courte; M7 est un flux binaire 256 octets possédant un découpage formel 3+5 bits; et le signal d=5 est associé à la géométrie des mots sans phase modulo 5 ni module unique établi.

**RESULT — p15.** Les 16 valeurs de la matrice p15 et leurs 16 positions sont reproduites exactement par : valeurs de Fibonacci distinctes `0,1,2,3,5,…` prises comme indices zéro-based dans la suite des nombres premiers → distance absolue à `3301` → placement en spirale carrée horaire à partir de la case rouge `3299` (centre haut-gauche des quatre cases centrales : ligne 2, colonne 2). Cette règle n'utilise aucune permutation libre une fois les conventions gelées. Elle établit une **reconstruction générative exacte de l'objet p15**; l'intention de l'auteur et surtout la cible éventuelle de cet ordre restent à valider hors échantillon.

**RESULT — pont corpus/T4.** Les 177 premières lignes runiques de la transcription Mortlach produisent exactement les mêmes 12 956 runes, dans le même ordre, que les huit premières sections `$` de `runes-text.txt`. Ce pont permet de localiser le signal lag-5 par M0…M7 et de reproduire exactement le T4 final annoncé : `p_max_module = 0.0890891091` et `p_leave_one_module_out = 0.3154968450`. Aucun module unique porteur n'est démontré.

**NEGATIVE_RESULT.** Trois raccords mécanistes préenregistrés ont échoué : (1) les 15 codes M7 `29/30/31` ne forment pas 15 séparateurs non adjacents donnant 16 blocs non vides; (2) U2 et U4 de M6 n'omettent pas la même rune; (3) l'interprétation directe `high3=m → M_m` avec `low5` reflétant la fréquence runique du module échoue au test exact des 8! affectations (`p=0.679439`). Ces échecs empêchent de transformer les coïncidences de cardinalité `16`, `5`, `8`, `29` en architecture post-hoc.

**INFERENCE.** La piste la moins coûteuse encore compatible avec les données est un document à **états/frontières et routage de représentations**, mais aucun raccord sémantique global n'est démontré. Le maillon le plus faible est précisément le passage d'un opérateur local (p15, M6, M7) à un autre.

---

# I. CLEAN_ROOM_COMPLIANCE

**Statut : VALID.**

Le paquet de transport a été ouvert uniquement pour extraire la whitelist. Les analyses ont ensuite porté sur les chemins whitelisted et sur des dérivés produits pendant PASS A. Le ZIP `LAG5_RAKE_2026-09-27.zip`, lui-même whitelisted, a été décompressé localement; ses membres sont listés ci-dessous comme contenus consultés du résultat vérifié autorisé. Les contact sheets sont des dérivés des 58 scans whitelisted.

### Liste complète des fichiers consultés

```text
# Transport/input containers consulted (authorized mission inputs)
/mnt/data/ASTRA_A_CLEANROOM_PROMPT_2026-09-27.txt
/mnt/data/ASTRA_A_CLEANROOM_2026-09-27.zip

# Whitelisted package files consulted
01_PROMPT/ASTRA_A_CLEANROOM_PROMPT_2026-09-27.txt
02_PRIMARY/LP2_SCANS/0.jpg
02_PRIMARY/LP2_SCANS/1.jpg
02_PRIMARY/LP2_SCANS/10.jpg
02_PRIMARY/LP2_SCANS/11.jpg
02_PRIMARY/LP2_SCANS/12.jpg
02_PRIMARY/LP2_SCANS/13.jpg
02_PRIMARY/LP2_SCANS/14.jpg
02_PRIMARY/LP2_SCANS/15.jpg
02_PRIMARY/LP2_SCANS/16.jpg
02_PRIMARY/LP2_SCANS/17.jpg
02_PRIMARY/LP2_SCANS/18.jpg
02_PRIMARY/LP2_SCANS/19.jpg
02_PRIMARY/LP2_SCANS/2.jpg
02_PRIMARY/LP2_SCANS/20.jpg
02_PRIMARY/LP2_SCANS/21.jpg
02_PRIMARY/LP2_SCANS/22.jpg
02_PRIMARY/LP2_SCANS/23.jpg
02_PRIMARY/LP2_SCANS/24.jpg
02_PRIMARY/LP2_SCANS/25.jpg
02_PRIMARY/LP2_SCANS/26.jpg
02_PRIMARY/LP2_SCANS/27.jpg
02_PRIMARY/LP2_SCANS/28.jpg
02_PRIMARY/LP2_SCANS/29.jpg
02_PRIMARY/LP2_SCANS/3.jpg
02_PRIMARY/LP2_SCANS/30.jpg
02_PRIMARY/LP2_SCANS/31.jpg
02_PRIMARY/LP2_SCANS/32.jpg
02_PRIMARY/LP2_SCANS/33.jpg
02_PRIMARY/LP2_SCANS/34.jpg
02_PRIMARY/LP2_SCANS/35.jpg
02_PRIMARY/LP2_SCANS/36.jpg
02_PRIMARY/LP2_SCANS/37.jpg
02_PRIMARY/LP2_SCANS/38.jpg
02_PRIMARY/LP2_SCANS/39.jpg
02_PRIMARY/LP2_SCANS/4.jpg
02_PRIMARY/LP2_SCANS/40.jpg
02_PRIMARY/LP2_SCANS/41.jpg
02_PRIMARY/LP2_SCANS/42.jpg
02_PRIMARY/LP2_SCANS/43.jpg
02_PRIMARY/LP2_SCANS/44.jpg
02_PRIMARY/LP2_SCANS/45.jpg
02_PRIMARY/LP2_SCANS/46.jpg
02_PRIMARY/LP2_SCANS/47.jpg
02_PRIMARY/LP2_SCANS/48.jpg
02_PRIMARY/LP2_SCANS/49.jpg
02_PRIMARY/LP2_SCANS/5.jpg
02_PRIMARY/LP2_SCANS/50.jpg
02_PRIMARY/LP2_SCANS/51.jpg
02_PRIMARY/LP2_SCANS/52.jpg
02_PRIMARY/LP2_SCANS/53.jpg
02_PRIMARY/LP2_SCANS/54.jpg
02_PRIMARY/LP2_SCANS/55.jpg
02_PRIMARY/LP2_SCANS/56.jpg
02_PRIMARY/LP2_SCANS/57.jpg
02_PRIMARY/LP2_SCANS/6.jpg
02_PRIMARY/LP2_SCANS/7.jpg
02_PRIMARY/LP2_SCANS/8.jpg
02_PRIMARY/LP2_SCANS/9.jpg
02_PRIMARY/LP2_SCANS/index.html
02_PRIMARY/LP2_SCANS/message.txt.asc
02_PRIMARY/Liber_primus_gematria_mortlach.txt
02_PRIMARY/runes-text.txt
02_PRIMARY/sexagesimal.bin
03_VERIFIED_RESULTS/BEAM_FINAL_SUMMARY.json
03_VERIFIED_RESULTS/LAG5_RAKE_2026-09-27.zip
04_REPRO_TOOLS/verify_sexagesimal_minimal.py
05_MANIFEST/PACKAGE_INFO.txt
05_MANIFEST/WHITELIST.txt
05_MANIFEST/SHA256SUMS.txt

# Members unpacked from the whitelisted LAG5_RAKE archive and consulted
_lag5/INPUT_MANIFEST.json
_lag5/PREREG_LAG5_RAKE_2026-09-27.md
_lag5/PREREG_SHA256_BEFORE_COMPUTATION.txt
_lag5/REPORT_FINAL_LAG5_RAKE_2026-09-27.md
_lag5/RNG_SEEDS.json
_lag5/SHA256SUMS.txt
_lag5/T1_raw.json
_lag5/T2_raw.json
_lag5/T3_raw.json
_lag5/T4_raw.json
_lag5/T5_raw.json
_lag5/analyze.py
_lag5/chain_progress.log
_lag5/conditional_rake.cpp
_lag5/corpus_numeric.txt
_lag5/lag5_make_input.py
_lag5/null_t1_t3.csv

# Derived visual aids produced from whitelisted scans and consulted
/mnt/data/astra_contacts/contact_00_09.jpg
/mnt/data/astra_contacts/contact_10_19.jpg
/mnt/data/astra_contacts/contact_20_29.jpg
/mnt/data/astra_contacts/contact_30_39.jpg
/mnt/data/astra_contacts/contact_40_49.jpg
/mnt/data/astra_contacts/contact_50_57.jpg

# Derived PASS A files produced/consulted before report freeze
/mnt/data/astra_work/CHRONOLOGICAL_OBJECT_MAP.csv
/mnt/data/astra_work/CHRONOLOGICAL_OBJECT_MAP_stdout.txt
/mnt/data/astra_work/CORPUS_BRIDGE_RESULT.json
/mnt/data/astra_work/CORPUS_BRIDGE_stdout.txt
/mnt/data/astra_work/INPUT_HASH_VERIFICATION.txt
/mnt/data/astra_work/M6_MISSING_RUNE_RESULT.json
/mnt/data/astra_work/M6_MISSING_RUNE_stdout.txt
/mnt/data/astra_work/M7_SELECTOR_MODULE_FREQ_RESULT.json
/mnt/data/astra_work/M7_SELECTOR_MODULE_FREQ_stdout.txt
/mnt/data/astra_work/P15_M7_SEPARATOR_RESULT.json
/mnt/data/astra_work/P15_M7_SEPARATOR_stdout.txt
/mnt/data/astra_work/P15_MATRIX_RECONSTRUCTION.json
/mnt/data/astra_work/P15_MATRIX_RECONSTRUCTION_stdout.txt
/mnt/data/astra_work/PREREG_M6_MISSING_RUNE_2026-09-27.md
/mnt/data/astra_work/PREREG_M7_SELECTOR_MODULE_FREQ_2026-09-27.md
/mnt/data/astra_work/PREREG_NEXT_PUNCT_BOUNDARY_2026-09-27.md
/mnt/data/astra_work/PREREG_P15_M7_INTERFACE_2026-09-27.md
/mnt/data/astra_work/SCAN_RED_METRICS.csv
/mnt/data/astra_work/SCAN_RED_METRICS_stdout.txt
/mnt/data/astra_work/SEXAGESIMAL_STRUCTURE_RESULT.json
/mnt/data/astra_work/SEXAGESIMAL_STRUCTURE_stdout.txt
/mnt/data/astra_work/T4_COMPLETED_raw.json
/mnt/data/astra_work/T4_COMPLETED_stdout.txt
/mnt/data/astra_work/T4_INSIDE_MODULE_RESULT.json
/mnt/data/astra_work/T4_INSIDE_MODULE_stdout.txt
/mnt/data/astra_work/analyze_sexagesimal_structure.py
/mnt/data/astra_work/analyze_t4.py
/mnt/data/astra_work/analyze_t4_inside_modules.py
/mnt/data/astra_work/build_chronological_map.py
/mnt/data/astra_work/reconstruct_p15_matrix.py
/mnt/data/astra_work/scan_red_metrics.py
/mnt/data/astra_work/t4_inside_module_null
/mnt/data/astra_work/t4_inside_module_null.cpp
/mnt/data/astra_work/t4_inside_module_null.csv
/mnt/data/astra_work/t4_inside_progress.log
/mnt/data/astra_work/t4_module_null
/mnt/data/astra_work/t4_module_null.cpp
/mnt/data/astra_work/t4_module_null.csv
/mnt/data/astra_work/t4_module_progress.log
/mnt/data/astra_work/test_m6_missing_rune.py
/mnt/data/astra_work/test_m7_selector_module_freq.py
/mnt/data/astra_work/test_p15_m7_separator.py
/mnt/data/astra_work/verify_corpus_bridge.py
/mnt/data/astra_work/verify_sexagesimal_output.txt
```

**Confirmation :** Projet = non; Library = non; Web = non; conversations antérieures = non; dépôts externes = non; solutions communautaires = non.

---

# II. ÉTAT CANONIQUE VÉRIFIÉ

## II.1 Intégrité du paquet

**PROOF.** `sha256sum -c 05_MANIFEST/SHA256SUMS.txt` réussit pour toutes les entrées du manifeste. Sortie brute : `INPUT_HASH_VERIFICATION.txt`.

Hashes structurants :

| Objet | SHA-256 |
|---|---|
| Prompt | `60a7ac5a58c6aa5f6368cbcc836b7809757bef9cf9d28846e047a74acb542343` |
| `runes-text.txt` | `5e0003aa7f7dde3b238d17c5f964790dbf6bf9db5edacc4a5ec0bad81c6f4bce` |
| Mortlach | `88ce49a218421a1e0481e69afcd7ed05380f2edf979bfdd5f3bcc7b4cc8ff98f` |
| `sexagesimal.bin` | `8db2a93497bc02bbf0ab07ac3cf96edd227fec630232c04ea35493d3a7d7b65e` |
| scan p15 | `5543cfce96493b86eece3195b3f5ea6e779ff41551676600b0c2479fc18c0ec5` |
| `LAG5_RAKE_2026-09-27.zip` | `49b964f91068e653f30b86cabe62ec5a160a4219776225f6d6055107717d91aa` |
| `BEAM_FINAL_SUMMARY.json` | `ee65330b827a958943041603c27caf3331d1f12237894e686f8910fd27a751b1` |
| vérificateur M7 | `c06d0c261e193e91e4aa1691c03a3fcc6b45b3eeb2ff9762a01008a4e9d8b672` |

Le manifeste intégral d'origine est conservé comme `INPUT_SHA256SUMS_ORIGINAL.txt`.

## II.2 Corpus

**CANONICAL_DATA.** 58 pages physiques p0…p57, dimensions 2400×3600. `index.html` énumère `0.jpg` à `57.jpg` dans cet ordre. Le scan p50 ne porte pas de runes; la transcription possède 56 marqueurs `%`, donc 57 segments runiques physiques.

**PROOF.** Le découpage de `runes-text.txt` par `$` donne exactement :

`729, 1145, 1738, 1894, 1021, 1433, 1680, 3316, 85, 95` runes.

Les huit premiers blocs totalisent 12 956 runes et correspondent exactement aux longueurs M0…M7 gelées. Les deux derniers ont 85 et 95 runes, compatibles avec p56 et p57 résolues. Ainsi, dans la transcription canonique, `%` suit les segments physiques tandis que `$` suit les frontières logiques de travail; leur non-coïncidence confirme matériellement `PAGE ≠ NÉCESSAIREMENT UNITÉ CRYPTOGRAPHIQUE`.

**PROOF.** Les 177 premières lignes runiques Mortlach utilisées par l'adaptateur lag-5 donnent 2 896 mots et 12 956 runes; après l'alias `ᛂ→ᛄ`, leur séquence numérique est identique bit-à-bit à la concaténation des huit premiers blocs `$` de `runes-text.txt`. Résultat : `CORPUS_BRIDGE_RESULT.json`.

## II.3 M7 canonique

**PROOF.** Le vérificateur whitelisted retourne : `PASS`, SHA-256 `8db2…b65e`, longueur 256, 241 `low5∈0…28`, et cinq occurrences de chacun de `29,30,31`.

**OBSERVATION nouvelle.** `sexagesimal.bin` contient 161 couples `(high3,low5)` distincts seulement, multiplicité maximale 4. Il n'est donc **pas** une permutation des 256 coordonnées possibles d'une grille 8×32. Comptages `high3 = [23,39,36,29,32,32,33,32]`; le test exploratoire contre uniformité donne χ²=4.875, df=7, p≈0.675, donc aucune non-uniformité simple n'est mise en évidence.

## II.4 Divergences / données manquantes

**OBSERVATION.** L'archive lag-5 ancienne contient `T4_raw.json = BLOCKED` faute de pont positionnel M0…M7, alors que le prompt gelé rapporte un T4 final non bloqué. Ce n'est pas réparé silencieusement : PASS A a reconstruit indépendamment le pont exact Mortlach↔`runes-text`, puis a reproduit exactement les deux p-values T4 du prompt. La chronologie documentaire explique donc l'écart de statut.

**MISSING.** La clé publique nécessaire à une vérification cryptographique autonome de la signature `message.txt.asc` n'est pas fournie dans le paquet; le message est conservé comme artefact whitelisted sans prétendre refaire sa chaîne d'authentification.

**MISSING.** Pour T5 lag-5, les quatre holdouts Gutenberg hachés et l'implémentation locale CPython 2.7 exigés par le protocole gelé ne sont pas présents; T5 reste `BLOCKED` et n'est interprété ni positivement ni négativement.

---

# III. CARTE CHRONOLOGIQUE

La table suivante couvre les 58 scans dans l'ordre physique. Elle sépare l'observation de l'interprétation et ne transforme aucun dessin en opérateur par défaut.

| PAGE | REGION | OBJET | OBSERVATION | CONTRAINTE | RELATIONS | HYPOTHÈSES MINIMALES |
|---:|---|---|---|---|---|---|
| 0 | M0 | physical scan | large red initial + runic text | red pigment is materially present at opening | M0 opening | section/opening marker possible |
| 1 | M0 | physical scan | runic text | no additional major nontext object isolated | M0 interior | text-bearing continuation |
| 2 | M0 | physical scan | runic text + black insect-like drawing + small red terminal mark | graphic and terminal color are colocated near M0 end | M0 closing area | drawing and/or red terminal may mark closure; operator not imposed |
| 3 | M1 | physical scan | large red initial + paired curly/spiral side borders + runic text | new border family and red opening coincide | M1 opening | section identity/framing plausible |
| 4 | M1 | physical scan | runic text + curly/spiral side borders | border family repeats | M1 interior | repeated frame may carry section identity; operator not imposed |
| 5 | M1 | physical scan | runic text + curly/spiral side borders | border family repeats | M1 interior | same |
| 6 | M1 | physical scan | runic text + curly/spiral side borders + red material | red material occurs before physical end of section | M1 interior | red is not exclusively a section-end signal |
| 7 | M1 | physical scan | runic text + curly/spiral side borders + red line/terminal area + five black dots | five-dot group occurs at M1 end | M1 closing area | ordered/group punctuation or closure marker possible |
| 8 | M2 | physical scan | large red initial + thin tree-like side motifs + runic text | new frame family with red opening | M2 opening | section identity/framing plausible |
| 9 | M2 | physical scan | runic text + tree-like side motifs | frame family repeats | M2 interior | same |
| 10 | M2 | physical scan | runic text + tree-like side motifs | frame family repeats | M2 interior | same |
| 11 | M2 | physical scan | runic text + tree-like side motifs | frame family repeats | M2 interior | same |
| 12 | M2 | physical scan | runic text + tree-like side motifs | frame family repeats | M2 interior | same |
| 13 | M2 | physical scan | runic text + tree-like side motifs | frame family repeats | M2 interior | same |
| 14 | M2 | physical scan | runic text + tree-like side motifs + insect-like drawing + small red terminal mark | graphic/terminal cluster precedes p15 construction | M2 late | closure/transition marker possible |
| 15 | M2/M3 | physical scan | upper: red runes + 4x4 number matrix + hand-drawn loop/lemniscate; lower: large red initial + runic text | logical boundary occurs inside one physical page; matrix is spatially ordered | M2→M3 intra-page transition | upper object teaches/order encodes a spatial transform; lower red initial marks new text block |
| 16 | M3 | physical scan | runic text | continuation after p15 lower opening | M3 interior | text-bearing continuation |
| 17 | M3 | physical scan | runic text | no additional major nontext object isolated | M3 interior | text-bearing continuation |
| 18 | M3 | physical scan | runic text | no additional major nontext object isolated | M3 interior | text-bearing continuation |
| 19 | M3 | physical scan | runic text | no additional major nontext object isolated | M3 interior | text-bearing continuation |
| 20 | M3 | physical scan | runic text | no additional major nontext object isolated | M3 interior | text-bearing continuation |
| 21 | M3 | physical scan | runic text | no additional major nontext object isolated | M3 interior | text-bearing continuation |
| 22 | M3 | physical scan | runic text + black horizontal/cross-like motif + human-body drawing + small red terminal mark | graphic and terminal mark occur at M3 end | M3 closing | closure/transition or semantic illustration possible; operator not imposed |
| 23 | M4 | physical scan | large red initial + repeated insect/dragonfly-like side frame + five black dots + runic text | new frame family/red opening/dot group coincide | M4 opening | section framing and punctuation/control-like group plausible |
| 24 | M4 | physical scan | runic text + repeated insect/dragonfly-like side frame | frame family repeats | M4 interior | section identity/framing plausible |
| 25 | M4 | physical scan | runic text + repeated insect/dragonfly-like side frame | frame family repeats | M4 interior | same |
| 26 | M4 | physical scan | runic text + repeated insect/dragonfly-like side frame + small red terminal mark | terminal red at end of framed run | M4 closing | closure marker plausible |
| 27 | M5 | physical scan | wing/leaf-like drawing + large red initial + runic text | new graphic plus red opening | M5 opening | section/opening marker plausible; drawing role undetermined |
| 28 | M5 | physical scan | runic text | no additional major nontext object isolated | M5 interior | text-bearing continuation |
| 29 | M5 | physical scan | runic text | no additional major nontext object isolated | M5 interior | text-bearing continuation |
| 30 | M5 | physical scan | runic text | no additional major nontext object isolated | M5 interior | text-bearing continuation |
| 31 | M5 | physical scan | runic text | no additional major nontext object isolated | M5 interior | text-bearing continuation |
| 32 | M5 | physical scan | runic text + pale/blurred tree-like drawing + small red terminal mark | drawing/terminal coincide with M5 end | M5 closing | closure/transition plausible |
| 33 | M6 | physical scan | two large red initials in separated text blocks + three black dots + repeated small black glyph cluster | multiple internal blocks occur inside M6 before numbered units | M6 PRE | wrapper/prologue syntax is certain; semantic function undetermined |
| 34 | M6 | physical scan | runic text + repeated small black glyph cluster | glyph cluster recurs across physical pages | M6 PRE | repeated marker/framing plausible; operator not imposed |
| 35 | M6 | physical scan | runic text + repeated small black glyph cluster | glyph cluster recurs | M6 PRE approaching U1 | same |
| 36 | M6 | physical scan | runic text + red Arabic numerals beginning explicit ordered-unit sequence + repeated glyph cluster | numbered units are explicit and ordered | M6 U1/U2 region | ordinal syntax is active; key/opcode semantics not imposed |
| 37 | M6 | physical scan | runic text + red Arabic numerals continuing 1→5 sequence + repeated glyph cluster | ordered sequence continues | M6 numbered units | ordinal syntax active |
| 38 | M6 | physical scan | runic text + red Arabic numerals continuing 1→5; U4 crosses p37→p38 | one numbered logical unit crosses physical page boundary | M6 numbered units | physical page cannot be assumed cryptographic/state boundary |
| 39 | M6 | physical scan | repeated glyph cluster + runic text + three black dots + large red initial into POST + small red terminal | numbered sequence is wrapped by POST text on same page | M6 POST/closing | pre/post wrapper around five ordered units is materially imposed |
| 40 | M7 | physical scan | large red initial + runic text + paired botanical/floral side frame | new frame family/red opening | M7 opening | section identity/framing plausible |
| 41 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 42 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 43 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 44 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 45 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 46 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 47 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats | M7 interior | same |
| 48 | M7 | physical scan | runic text + botanical/floral side frame | frame repeats before payload | M7 interior | same |
| 49 | M7 | physical scan | alphanumeric/sexagesimal-looking payload begins + red material + botanical/floral frame | representation changes from runes to packed-looking symbols | M7 payload onset | representation/routing interface plausible; semantics undetermined |
| 50 | M7 | physical scan | full physical page of non-rune alphanumeric/sexagesimal-looking payload; no runes | physical page contains zero runes while logical M7 continues | M7 payload | page≠rune segment; payload is a distinct representation |
| 51 | M7 | physical scan | non-rune payload at top then runic text below + botanical/floral frame | representation boundary occurs within a physical page | M7 payload→runes | representation interface is intra-page; page not unit |
| 52 | M7 | physical scan | runic text + botanical/floral side frame | return to runic representation | M7 interior after payload | continuation |
| 53 | M7 | physical scan | runic text with several red runic lines + insect-like drawing + botanical/floral framing | red text is a distinct local channel | M7 late | emphasis/control/semantic distinction possible; exact role undetermined |
| 54 | M7 | physical scan | large red initial + runic text + botanical/floral framing | new red opening occurs inside M7 | M7 late | internal subsection marker plausible; not a new M0..M7 module by itself |
| 55 | M7 | physical scan | runic text + pale tree-like drawing + insect-like drawing + small red terminal mark | graphic/terminal cluster closes unresolved M7 | M7 closing | closure marker plausible |
| 56 | SOLVED | physical scan | solved AN END page: large red initial + short runic text + long hex-like line + five black dots | solved control page follows unresolved corpus | solved control | positive control for author grammar; do not import mechanism automatically |
| 57 | SOLVED | physical scan | solved PARABLE page: large red initial + runic text + insect/dragonfly-like figure | solved control page | solved control | positive control for author grammar; do not import mechanism automatically |

### Contraintes transversales tirées de la carte

**OBSERVATION → CONTRAINTE.** Plusieurs familles graphiques persistent sur plusieurs pages, tandis que certaines frontières logiques traversent une page (p15, p51) ou une unité numérotée traverse p37→p38. Une page physique ne peut donc pas être adoptée comme unité d'état par défaut.

**OBSERVATION → CONTRAINTE.** Les grands caractères rouges apparaissent souvent à des ouvertures, mais aussi à l'intérieur de régions (notamment M6/M7); le rouge est un canal actif, pas un synonyme univoque de “début de module”. Le masque chromatique reproductible détecte du rouge significatif (>100 pixels selon le seuil publié) sur p0,2,3,6,7,8,14,15,22,23,26,27,32,33,36,37,38,39,40,49,53,54,55,56,57.

**OBSERVATION → CONTRAINTE.** M7 change de représentation autour de p49–p51, avec p50 sans runes et p51 mixte. Toute architecture globale doit permettre un routage entre représentations ou, au minimum, ne pas supposer un alphabet unique continu.

---

# IV. GRAMMAIRE D’AUTEUR

Cette section ne contient que les comportements historiquement attestés **dans le prompt whitelisted**; elle ne les projette pas automatiquement sur LP2 non résolu.

| ATTESTÉ HISTORIQUEMENT | Portée permise ici |
|---|---|
| mot du texte → clé | famille admissible, pas preuve LP2 |
| sens du texte ↔ clé | idem |
| irrégularité / skip intentionnel | idem |
| nombres premiers | idem |
| fonction d'Euler sur nombres premiers | idem |
| Fibonacci | idem |
| Gematria | idem |
| permutation spatiale | idem |
| routage entre médias | idem |
| orientation et ordre comme données actives | idem |
| “Liber Primus is the way… words… map… meaning… road… numbers… direction.” | guide général, pas mécanisme |
| “Let the text guide you.” | principe historique, pas algorithme |

**INFERENCE minimale.** Un modèle LP2 peut légitimement tester des connexions texte/nombre/espace/orientation seulement si la cardinalité, l'ordre ou la géométrie les imposent et si un holdout indépendant suit. L'historique n'autorise aucune permutation, clé ou reset libre.

---

# V. NOUVELLES OBSERVATIONS

## V.1 Syntaxe `$` et pont exact des corpus

**OBSERVATION.** `runes-text.txt` contient neuf `$`; les dix blocs ont les longueurs exactes M0…M7 + p56 + p57.  
**CONTRAINTE.** La transcription possède donc une couche logique explicite distincte des 57 segments physiques `%`.  
**RESULT.** Les 177 lignes Mortlach gelées recouvrent exactement M0…M7, rune pour rune. Cela fournit le mapping positionnel qui manquait au T4 historique de l'archive.

## V.2 Reconstruction générative exacte de p15

Matrice observée :

```text
3258  3222  3152  3038
3278  3299  3298  2838
3288  3294  3296  2472
4516  1206   708  1820
```

**HYPOTHESIS (gelée après dérivation locale).** Prendre les 16 valeurs de Fibonacci distinctes `0,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987` comme indices zéro-based dans les nombres premiers. Les premiers obtenus sont `2,3,5,7,13,23,43,79,149,263,463,829,1481,2593,4507,7817`. Calculer `|3301-prime|`, puis placer la séquence en spirale horaire à partir de (2,2), d'abord vers la droite.

**TEST.** Les valeurs produites sont :

`3299,3298,3296,3294,3288,3278,3258,3222,3152,3038,2838,2472,1820,708,1206,4516`.

**RESULT.** 16/16 valeurs et 16/16 positions correspondent exactement. `3299`, premier terme, est la case visuellement rouge. Aucun réordonnancement supplémentaire n'est appliqué.

**TENTATIVE DE FALSIFICATION.** La connexion la plus naturelle vers M7 — 15 codes spéciaux comme séparateurs donnant 16 blocs non vides ordonnables par cette spirale — a été préenregistrée puis **échoue** (V.4). Le p15 local survit; son raccord global ne survit pas.

**INTERPRÉTATION.** Il est certain qu'une règle courte reconstruit exactement l'objet. Il est probable, mais non prouvé hors échantillon, que la matrice encode/enseigne un ordre spatial. Sa cible reste `NON DÉTERMINÉ`.

## V.3 T4 lag-5 enfin reproductible depuis les sources canoniques

**OBSERVATION.** Comptages d=5 *internes au mot* par module :

`M0 7/135, M1 5/183, M2 18/291, M3 18/295, M4 8/168, M5 9/227, M6 13/264, M7 26/542`.

Somme = `104/2105`, exactement le T1 global interne.

**TEST.** Même famille de null conditionnel, mêmes graines/chaînes/burn-in/thinning que le râteau gelé. 100 000 tirages. Les chemins de MCMC reproduisent les comptes de propositions/acceptations du run gelé.

**RESULT.** `max|Z| = 2.5556615`, `p_max_module = 0.0890891091`. Le plus grand résidu est M2, de très peu devant M3, mais la correction familiale ne permet pas de localiser le signal. Test leave-one-module-out : variation maximale de Z `0.7337131`, `p = 0.3154968450`. Les valeurs reproduisent exactement le T4 gelé du prompt.

## V.4 Les 15 codes spéciaux M7 ne sont pas 15 séparateurs simples pour p15

**PRÉENREGISTREMENT.** `PREREG_P15_M7_INTERFACE_2026-09-27.md` a été haché avant inspection des positions spéciales.

**PRÉDICTION.** Si les 15 codes `low5∈{29,30,31}` délimitent 16 blocs non vides pour la route 4×4, ils doivent être intérieurs et non adjacents.

**HOLDOUT.** Positions 0-based : `6,11,48,56,65,96,105,106,144,151,194,206,211,249,254`.

**NEGATIVE_RESULT.** Les positions 105 et 106 sont adjacentes; un bloc a longueur 0. Longueurs induites : `6,4,36,7,8,30,8,0,37,6,42,11,4,37,4,1`. La prédiction échoue. Sous un null uniforme conditionné à 15 positions, la propriété préenregistrée aurait eu probabilité ≈0.3692; aucune rareté n'est invoquée après l'échec. La variante “15 séparateurs → 16 blocs non vides” est enterrée.

## V.5 M6 : l'alternance de couverture est réelle, mais pas la même rune absente

**PRÉENREGISTREMENT.** Étant donné les couvertures `29,28,29,28,29`, prédiction minimale : U2 et U4 omettent la même rune.

**NEGATIVE_RESULT.** U2 omet `ᚫ`; U4 omet `ᚷ`. L'identité attendue échoue. L'alternance de cardinalité reste une observation, sans sémantique démontrée.

## V.6 M7 : cardinalités séduisantes, sémantique directe falsifiée

**OBSERVATION.** La décomposition formelle donne un domaine `high3` de cardinalité 8, un domaine ordinaire `low5` de cardinalité 29, et trois codes résiduels. Cette compatibilité de cardinalité avec M0…M7 et l'alphabet runique est réelle mais non suffisante.

**PRÉENREGISTREMENT.** Variante renforcée : `high3=m` sélectionne directement `M_m`; `low5 0…28` est l'identité runique canonique; si les enregistrements se réfèrent aux symboles du module sélectionné, leurs fréquences conditionnelles doivent mieux correspondre au module de même indice qu'aux permutations des modules.

**TEST.** Score log-vraisemblance Dirichlet +1, aucune permutation de runes, et énumération exacte des `8! = 40320` affectations de modules.

**NEGATIVE_RESULT.** L'affectation identité se classe 27 395e/40 320; `p_upper = 0.6794394841`. La variante directe source-fréquence est falsifiée. Le “meilleur” réarrangement observé n'est **pas** adopté après coup.

---

# VI. HYPOTHÈSES MÉCANISTES

## H-A — Transformation cryptographique continue / état continu avec skip

**Construction.** Flux runique traité par une transformation continue, éventuellement avec rejet/skip déterministe.  
**Faits expliqués.** Compatible en principe avec anti-répétition et avec l'histoire des skips; peut générer un flux uniforme.  
**Faits inexpliqués.** Association d=5 à la frontière de mot, classes de longueurs, nombreuses frontières visuelles/logiques, p15/M6/M7 multimodaux.  
**Degrés de liberté.** Très élevés dès qu'on ajoute seed, sens, offset, reset/reseed, permutation ou pré/post-transform.  
**Falsificateur.** Un modèle précis doit annoncer sa règle de frontière et réussir un holdout; les resets libres par mot sont interdits.  
**État.** La forme simple `CPython2.7 MT19937 → keyskip1 → anglais direct` est sérieusement défavorisée dans la campagne testée (1 208 130 candidats, zéro hit ≥−5.5, meilleur ≈−5.865576), sans exclure MT19937 comme sous-module.

## H-B — Transducteur à états/frontières sémantiques

**Construction.** L'état évolue continûment mais certaines frontières observables (mot, ponctuation, section, propriété mathématique) modifient déterministiquement la transition.  
**Faits expliqués.** T1 associe d=5 à la frontière de mot; T2 indique une dépendance à au moins une classe de longueur; T3 exclut une simple phase fixe mod 5; T4 exclut un module unique comme porteur.  
**Faits inexpliqués.** La fonction de transition, la sortie, le lien avec p15/M6/M7.  
**Degrés de liberté.** Modérés uniquement si la variable de frontière est préimposée; explosifs si choisie après résultat.  
**Falsificateur.** Prédiction indépendante sur un canal de frontière non utilisé : la ponctuation, gelée en section XI/XII.

## H-C — Routage entre représentations / opérateurs locaux

**Construction.** Des objets locaux enseignent ou imposent des ordres/transforms, puis routent une représentation vers une autre : texte ↔ nombre ↔ espace ↔ binaire.  
**Faits expliqués.** p15 possède une reconstruction spatiale compacte; M6 impose cinq unités ordonnées; M7 passe à un payload 256 octets; p49–p51 changent de représentation au sein de M7; le style historique autorisé inclut permutation spatiale et routage média.  
**Faits inexpliqués.** Aucun raccord précis p15→M7, M6→M7, ou texte→M7 n'a réussi.  
**Degrés de liberté.** Faibles localement, élevés dès qu'on choisit librement la destination d'un opérateur.  
**Falsificateur.** Un raccord doit prédire une propriété d'un autre canal avant inspection; le test p15→16 blocs a déjà échoué.

## H-D — Structure hiérarchique sans machine globale encore imposée

**Construction.** Le livre impose d'abord une grammaire de structure : pages physiques → sections logiques → sous-unités ordonnées → objets locaux de transformation → changements de représentation. Aucun algorithme global supplémentaire n'est supposé tant qu'un pont ne l'impose.  
**Faits expliqués.** `$` vs `%`, p15 intra-page, U4 traversant une page, PRE/U1…U5/POST, p49–p51, cadres répétés, canaux rouge/noir.  
**Faits inexpliqués.** Plaintext/clé/adresse/programme final; fonction exacte des dessins, du rouge, des trois codes M7, et des cinq unités.  
**Degrés de liberté.** Minimum : décrit seulement les structures directement mesurées.  
**Falsificateur.** Si une analyse indépendante des frontières non utilisées (ponctuation) ne porte aucune signature compatible avec une hiérarchie de frontières, la version “boundary-aware” doit être réduite à une simple structure documentaire.

**RESULT MDL.** H-D est la structure minimale qui couvre le plus de faits sans inventer de clé, sens, offset, reseed ou destination. H-B et H-C restent des extensions concurrentes; aucune ne constitue encore une machine complète.

---

# VII. EXPÉRIENCES

## E0 — Intégrité / sexagesimal minimal

- **Préenregistrement :** contrainte canonique du prompt.
- **Code :** `04_REPRO_TOOLS/verify_sexagesimal_minimal.py` (SHA `c06d0c261e193e91e4aa1691c03a3fcc6b45b3eeb2ff9762a01008a4e9d8b672`).
- **Input :** `02_PRIMARY/sexagesimal.bin` (SHA `8db2a93497bc02bbf0ab07ac3cf96edd227fec630232c04ea35493d3a7d7b65e`).
- **Null :** n/a, test exact.
- **Résultat :** PASS; 256 octets; 241 ordinaires; 29/30/31 = 5/5/5.
- **Interprétation :** payload canonique confirmé.

## E1 — Pont canonique rune ↔ segmentation Mortlach

- **Code :** `verify_corpus_bridge.py` (SHA `99c0aeeba98ddb11f5dceecb8bffd6325eb97e022f0e38948cdf61e028a0665a`).
- **Inputs :** `runes-text.txt` SHA `5e0003aa7f7dde3b238d17c5f964790dbf6bf9db5edacc4a5ec0bad81c6f4bce`; Mortlach SHA `88ce49a218421a1e0481e69afcd7ed05380f2edf979bfdd5f3bcc7b4cc8ff98f`.
- **Test :** égalité exacte de la séquence numérique, sans alignement ajusté.
- **Résultat :** 12 956/12 956 positions identiques; 2 896 mots; 104/2105 égalités d=5 internes.
- **Interprétation :** mapping de positions M0…M7 récupéré sans donnée externe.

## E2 — Reconstruction p15

- **Code :** `reconstruct_p15_matrix.py` (SHA `ff8ccab7ed375b03f59e53283ac06efab5490a91ae9c944b21cf201dc3070d5d`).
- **Input matériel :** p15 SHA `5543cfce96493b86eece3195b3f5ea6e779ff41551676600b0c2479fc18c0ec5`; concepts Fibonacci/primes/3301 explicitement associés à p15 par le prompt et le scan.
- **Null :** pas de null probabiliste; test exact de génération 16×position.
- **Résultat :** 16/16 cellules exactes.
- **Interprétation :** reconstruction générative locale forte; intention/cible non validées par holdout.

## E3 — T4 localisation par module

- **Code générateur null :** `t4_inside_module_null.cpp` SHA `35d67ef165381e9e7fd858cb6323466d502ae28f2300e82eb69c073f609a066c`.
- **Analyse :** `analyze_t4_inside_modules.py` SHA `84eed76f2c702351901760cfe441dc6234ab31a02ceed4a7b9a0172f022348de`.
- **Input numérique :** `corpus_numeric.txt` SHA `77e64202b5c8754fe89cacca6afe214f8e956e7ab74675e05d46057e12f74586`; frontières M0…M7 issues du pont E1.
- **Null :** même MCMC conditionnel que T1–T3, conservant géométrie de mots, multiplicités et K=86 égalités adjacentes; 4 chaînes, 25 000 tirages/chaîne.
- **Raw :** `t4_inside_module_null.csv` SHA `41807e7f8af5d020063d2e8b7bcb6080156a30891d2d1dca3a31bd5f5891d941`.
- **Résultat :** p_max=0.0890891091; p_LOO=0.3154968450.
- **Interprétation :** aucun module unique établi; reproduction exacte du T4 final du prompt.

**Diagnostic rejeté.** Une première variante exploratoire a compté *toutes* les paires d=5 restant dans un module au lieu des seules paires internes au mot. Elle donne p≈0.06987 / LOO≈0.10344 et ne correspond pas au T4 gelé. Elle est conservée (`t4_module_null*`, `T4_COMPLETED_raw.json`) comme trace, explicitement non canonique et non utilisée dans la conclusion.

## E4 — M6 rune manquante

- **Préenregistrement :** `PREREG_M6_MISSING_RUNE_2026-09-27.md` SHA `2d99a872a2bfc394b0b2ed19ecc359d46672afb811c2902d03b18ef905d8a5e2`.
- **Code :** `test_m6_missing_rune.py` SHA `1eb050cb738b330c58fc757cc81c149a55e4fd8698d531018fb5d91c6a138033`.
- **Input :** `runes-text.txt` SHA `5e0003aa7f7dde3b238d17c5f964790dbf6bf9db5edacc4a5ec0bad81c6f4bce`.
- **Prédiction :** rune manquante U2 = rune manquante U4.
- **Résultat :** `ᚫ` ≠ `ᚷ`; FAIL.
- **Interprétation :** aucune identité commune démontrée.

## E5 — p15 route ↔ 15 séparateurs M7

- **Préenregistrement :** SHA `113a66b610ef91517b3e500e4d77322e5a0cceeabf3bedec6eb43c8f536603d1`.
- **Code :** `test_p15_m7_separator.py` SHA `ef6008adbbc09fa666e69692b84b149440c9f2f38ae0b57d9247cd0248c165e6`.
- **Input :** `sexagesimal.bin` SHA `8db2a93497bc02bbf0ab07ac3cf96edd227fec630232c04ea35493d3a7d7b65e`.
- **Null P1 :** 15 positions uniformes sans remise parmi 256; probabilité exacte de 15 positions intérieures et non adjacentes `C(240,15)/C(256,15)=0.3691553976`.
- **Résultat :** FAIL par adjacency 105–106; un run vide.
- **Interprétation :** raccord simple 15→16 rejeté.

## E6 — high3 comme sélecteur direct de module

- **Préenregistrement :** SHA `3139d050906da525af28bbf4d9154abe4c060b4e9f8582ff67f0628c60fe185f`.
- **Code :** `test_m7_selector_module_freq.py` SHA `9ccb9707c3e63796db0ecaff6a215e3bc490526d1987f2df0cb1cda85fcfdddd`.
- **Inputs :** `runes-text.txt`, `sexagesimal.bin` avec hashes ci-dessus.
- **Null :** énumération exacte des 40 320 permutations des huit profils de module; mapping des 29 runes gelé.
- **Résultat :** rang identité 27 395/40 320; p=0.6794394841; FAIL.
- **Interprétation :** la sémantique “sélecteur de module source direct” est rejetée; `high3` peut encore avoir une autre fonction.

## E7 — structure formelle de M7

- **Code :** `analyze_sexagesimal_structure.py` SHA `20264127889ccc74cc70977e408ee4e9912c051c0b5fbed61d5dc1b0982a6556`.
- **Résultat exact :** 161 octets/couples distincts; multiplicité max 4; pas de permutation complète 8×32. χ² high3 uniforme p≈0.675 (exploratoire).
- **Interprétation :** les cardinalités 8/29/3 existent, mais aucun rôle n'en découle à lui seul.

---

# VIII. RÉSULTATS NÉGATIFS

Le cimetière du prompt est conservé intégralement : clés additives simples dérivées de high3, topologie high3 naïve, prédiction directe des codes 29/30/31, `low5→ordre p15→Gematria→anglais` naïf, M6 en cinq triplets naturels, superpositions graphiques simples, AND/XOR brut, arbres comme opérateurs directs, affines libres, permutation-fishing, phase mod5 simple, localisation du lag-5 à un seul module, et modèle direct `MT19937/keyskip1→anglais` dans la configuration balayée.

PASS A ajoute :

1. **NEGATIVE_RESULT — M6 même rune absente :** U2=`ᚫ`, U4=`ᚷ`; échec.
2. **NEGATIVE_RESULT — M7 15 séparateurs→16 blocs :** adjacency 105–106; échec.
3. **NEGATIVE_RESULT — M7 high3 sélection directe M0…M7 par fréquence :** p=0.679439; échec.
4. **NEGATIVE_RESULT — M7 permutation complète 8×32 :** seulement 161 couples distincts; impossible.
5. **NEGATIVE_RESULT méthodologique — T4 “toutes paires intra-module” :** ce n'est pas le T4 gelé; variante rejetée après comparaison de définition, conservée comme trace et non comme découverte.

Aucune de ces familles ne doit être rouverte sans nouvelle prémisse matérielle précise.

---

# IX. MEILLEURE ARCHITECTURE OBTENUE INDÉPENDAMMENT

La meilleure architecture est volontairement une **structure minimale**, pas un décryptage inventé.

| Maillon | Classe | Justification |
|---|---|---|
| 58 pages physiques, 57 segments runiques, p50 non runique | CERTAIN | scans + `%` + corpus |
| M0…M7 sont des unités logiques distinctes des pages | CERTAIN | `$` exact + p15 intra-page + U4 traversant une page |
| M6 = PRE → U1→U2→U3→U4→U5 → POST | CERTAIN | segmentation/numérotation/longueurs; U4 traverse page |
| M7 = payload canonique 256 octets, layout 32×8, split formel high3/low5 | CERTAIN | binaire + vérificateur |
| p15 admet la règle Fibonacci→prime→|3301−p|→spirale donnant 16/16 cellules | CERTAIN comme reconstruction mathématique | test exact |
| cette règle est l'opérateur intentionnel voulu par l'auteur | PROBABLE | très faible description + concepts explicitement présents + case de départ rouge, mais dérivation non holdout |
| la frontière de mot est associée au phénomène d=5 | CERTAIN statistiquement sous le null gelé | T1 p≈0.00042 |
| un mécanisme futur devra probablement respecter la géométrie des mots plutôt qu'une phase fixe | PROBABLE | T1/T2 positifs, T3 négatif, T4 non localisé |
| `high3` est un état/sélecteur | POSSIBLE | cardinalité 8 naturelle; variante directe M0…M7 falsifiée |
| `low5 0..28` est directement une rune et 29..31 des contrôles | POSSIBLE | cardinalité naturelle; fonction non démontrée |
| p15 ordonne M7 en 16 blocs | NON DÉTERMINÉ / variante simple rejetée | séparateur holdout échoué |
| M6 cinq unités = cinq clés/états/opcodes | NON DÉTERMINÉ | aucune fonction imposée; test rune absente échoué |
| sortie finale = anglais/clé/programme/adresse | NON DÉTERMINÉ | aucune donnée suffisante |

**Réponse à la question centrale.** Liber Primus oblige actuellement le lecteur à construire au minimum une **hiérarchie d'unités et de représentations avec ordre actif** : distinguer page/section/sous-unité; respecter les ordres donnés; accepter des frontières intra-page et cross-page; reconnaître un opérateur spatial local exact à p15; et traiter M7 comme un payload structuré, sans décider encore ce que ses champs “font”. Les données **n'obligent pas encore** une machine globale unique.

**Niveau d'avancée atteint.** Nouvelle contrainte matérielle reproductible (niveau 1) et hypothèse structurelle à faible degré de liberté expliquant plusieurs contraintes (niveau 2). Aucune prédiction hors échantillon nouvelle n'a réussi pendant PASS A; les trois holdouts mécanistes nouveaux ont échoué. Il serait donc incorrect de revendiquer niveau 3–5 pour l'architecture globale.

---

# X. MAILLON LE PLUS FAIBLE

Le maillon le moins soutenu est **tout raccord inter-objet** : p15→M7, M6→M7, ou high3→M0…M7. Les objets locaux existent et certains possèdent une structure forte, mais aucune transformation démontrée ne relie encore deux objets indépendants du livre.

Le raccord p15→M7 avait précisément l'avantage d'une cardinalité `16` issue de p15 et de `15` codes spéciaux M7; le holdout le plus simple l'a falsifié. Cette falsification augmente la confiance dans la discipline de l'analyse : la structure locale p15 n'est pas sauvée par une exception inventée.

---

# XI. PRÉDICTION INDÉPENDANTE

La prédiction suivante est **gelée mais non exécutée**; elle n'a pas servi à construire l'architecture ci-dessus. Elle utilise un canal encore non conditionné : la ponctuation.

### HYPOTHÈSE
La composante “boundary-aware” du modèle H-B est réelle : si la frontière de mot perturbe un état, une frontière sémantique plus forte marquée par ponctuation ne doit pas produire moins d'interruption qu'une frontière de mot ordinaire.

### DONNÉES UTILISÉES POUR LA CONSTRUIRE
T1, T2, T3, T4 et l'existence d'un canal ponctuation dans la transcription; **aucun comptage d=5 conditionné à la ponctuation**.

### DONNÉE HOLDOUT
Positions exactes de ponctuation dans le corpus non résolu, alignées de manière déterministe avec les 2 896 mots Mortlach.

### PRÉDICTION EXACTE
Pour les paires d=5 traversant au moins une frontière de mot :

`rate_equal(PUNCT_CROSS) < rate_equal(ORDINARY_CROSS)`.

Statistique `D = rate(PUNCT_CROSS) − rate(ORDINARY_CROSS)`, prédite négative.

### STATISTIQUE / NULL
Même famille de null conditionnel que le râteau gelé, conservant géométrie des mots, multiplicités runiques et `K=86`; masque de ponctuation fixe. p-value unilatérale basse.

### CRITÈRE DE SUCCÈS
`D<0` et `p_lower≤0.05`, sans regroupement ou seuil ajusté après lecture.

### FALSIFICATEUR
`D≥0` ou `p_lower>0.05` falsifie la version ponctuation-renforcée du modèle de frontière. Le préenregistrement complet est `PREREG_NEXT_PUNCT_BOUNDARY_2026-09-27.md`, SHA `eded2b98101c53a6e274373b002dade2a7d302c9a99f25a9cb94f7f16a01c4fe`.

---

# XII. PROCHAINE EXPÉRIENCE UNIQUE

**Choix :** exécuter exactement le test de ponctuation préenregistré en XI, et aucun autre ajustement préalable.

**Pourquoi il maximise information / degrés de liberté / coût :** il utilise un canal indépendant et déjà présent; il discrimine directement “simple effet lexical” vs “état sensible aux frontières”; il n'ajoute ni clé, ni permutation, ni offset, ni PRNG; il réutilise le null déjà contrôlé; et son coût est très inférieur à une nouvelle recherche exhaustive.

**Ordre obligatoire pour un PASS suivant :** (1) publier l'alignement ponctuation↔mots et son hash; (2) signaler `MISSING` pour toute ambiguïté sans la réparer; (3) exécuter le statisticien gelé; (4) rapporter tous les comptes et la p-value; (5) ne modifier le modèle qu'après lecture du holdout.

---

# Reproductibilité — inventaire des sorties PASS A

Les scripts, préenregistrements, sorties JSON/CSV, manifestes et résultats bruts sont fournis dans le bundle `ASTRA_A_BLIND_LP2_2026-09-27_REPRO.zip`. Un `OUTPUT_SHA256SUMS.txt` est généré après gel du rapport.

Les seeds du null T4 sont ceux du râteau gelé, implémentés dans `t4_inside_module_null.cpp` (`0x3301 + 0x9e3779b97f4a7c15 * chain`, MT19937_64). Les sorties brutes sont conservées. Aucun GPU/cluster n'a été utilisé.

---

# TEST FINAL DE CONFORMITÉ

1. Ai-je utilisé une ressource hors whitelist ? **NON.** Les fichiers de transport sont les deux entrées fournies pour la mission; toutes les données analytiques viennent de la whitelist ou de dérivés PASS A.
2. Ai-je consulté le Projet ou la Library ? **NON.**
3. Ai-je utilisé des conversations antérieures ? **NON.**
4. Ai-je utilisé le Web ou un dépôt externe ? **NON.**
5. Ai-je vu une conclusion interprétative antérieure qui n'était pas explicitement contenue dans ce prompt ou les résultats whitelisted ? **NON.**

```text
CLEAN_ROOM_STATUS
- project_access_used: NO
- library_access_used: NO
- prior_chat_access_used: NO
- web_access_used: NO
- external_repo_access_used: NO
- non_whitelisted_file_access_used: NO
- blindness_status: VALID
```

**PASS A TERMINÉ — STOP.**  
Aucune comparaison communautaire, PASS B ou PASS C n'a été effectuée.

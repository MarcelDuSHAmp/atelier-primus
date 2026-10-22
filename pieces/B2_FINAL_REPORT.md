# CICADA 3301 / LIBER PRIMUS
## MICRO-PASS B2 — L1→L0 RASTER BOUNDARY CERTIFICATION

**Date : 28 septembre 2026**  
**Mode exécuté : fallback stratifié préenregistré**  
**Verdict : `B2_L1_L0_STRATIFIED_STRONG_SUPPORT`**

> On n’épure pas l’information. On épure ce qu’on invente.

---

# Résumé exécutif

L’exhaustif 2 895/2 895 n’a pas pu être exécuté proprement dans ce runtime parce que le ZIP Cleanroom contenant les 58 masters onion7 n’était pas exportable en bytes. Conformément au protocole, l’audit a donc basculé sur un échantillon stratifié **gelé avant l’inspection détaillée**.

Résultat :

- **40 / 40** frontières L1 échantillonnées correspondent à une séparation matérielle L0 ;
- **32 / 32** frontières `-` concordent ;
- **8 / 8** frontières `.` concordent ;
- **M0…M7 : 5 / 5 chacun** ;
- **13 / 13** cas préenregistrés proches d’une coupure de ligne concordent ;
- **8 / 8** contrôles négatifs `/` restent des wraps internes à un mot et ne sont pas pris pour des frontières ;
- **0 mismatch** ;
- **0 ambiguous** dans l’échantillon ;
- **0 omission L0→L1 observée dans les 48 fenêtres locales inspectées**.

Le point le plus important est matériel : le `-` L1 n’est pas seulement une convention arbitraire d’espacement. Les rasters montrent un objet de séparation entre groupes runiques ; L1 le représente par `-`. Les clauses possèdent également une séparation matérielle représentée par `.`.

---

# A — Autorité L0

Le paquet Cleanroom identifie les sources d’autorité comme `02_PRIMARY/LP2_SCANS/0.jpg … 57.jpg`. Les campagnes forensic antérieures établissent que la lignée publique `original-onion7`/relikd correspond aux masters onion7 byte-identiques et que les images natives sont des rendus 2400×3600 @ 400 dpi.

Pour B2, l’inspection a porté sur les pages gelées p0, p6, p9, p19, p25, p32, p34 et p40 ; p1 et p7 ont été ajoutées uniquement pour vérifier les wraps inter-page p0→p1 et p6→p7.

L’échantillon couvre donc les huit modules M0→M7.

---

# B — Concordance L1→L0

| Sous-ensemble | N | MATCH | NO | AMBIGUOUS |
|---|---:|---:|---:|---:|
| Total frontières | 40 | 40 | 0 | 0 |
| `-` Word | 32 | 32 | 0 | 0 |
| `.` Clause | 8 | 8 | 0 | 0 |
| Near-line préenregistré | 13 | 13 | 0 | 0 |
| Autres | 27 | 27 | 0 | 0 |

Taux de concordance hors ambiguïtés : **100 % dans l’échantillon**.

Cela ne doit jamais être reformulé en « 100 % des 2 895 frontières ».

---

# C — Omissions L0→L1

La direction inverse a été contrôlée dans les fenêtres locales autour des 40 frontières et 8 wraps négatifs.

- fenêtres inspectées : **48** ;
- séparation linguistique visible supplémentaire non représentée en L1 : **0 observée**.

Portée : locale aux fenêtres inspectées. Aucun audit exhaustif des faux négatifs sur les 58 pages n’est revendiqué.

---

# D — Anomalies

Aucun mismatch matériel et aucune ambiguïté dans l’échantillon.

Sept cas difficiles sont conservés explicitement : frontières qui coïncident avec ou touchent un wrap ligne/page. Ils concordent et montrent précisément pourquoi `LINE BREAK ≠ WORD BOUNDARY` : la présence d’un `/` ne suffit pas ; le séparateur linguistique reste un objet distinct.

Les 8 contrôles négatifs le confirment : **8 / 8** wraps à l’intérieur d’un mot ne sont pas transformés en frontière.

---

# E — Verdict B2

## `B2_L1_L0_STRATIFIED_STRONG_SUPPORT`

Pourquoi pas `EXHAUSTIVE_MATCH` ?

Parce que seuls 40 des 2 895 emplacements ont été sélectionnés et inspectés dans le protocole B2. Le fait qu’ils couvrent M0→M7 et les cas de wrap renforce énormément l’inférence, mais n’autorise pas à inventer les 2 855 observations manquantes.

Pourquoi ce n’est plus `MATERIAL_INSUFFICIENT` ?

Parce que le test dispose maintenant d’observations L0 réparties dans **tous les modules**, avec des contrôles négatifs qui montrent que la méthode sait distinguer wrap et frontière linguistique.

---

# F — Mise à jour B0/B1

B1 ne change pas.

B0 reçoit le renforcement suivant :

```text
TRANSCRIPTION_BOUNDARY_ASSOCIATED
        ↓
AUTHORIAL_BOUNDARY_ASSOCIATED — STRONG SAMPLE SUPPORT
```

On ne promeut PAS :

`B0_AUTHORIAL_BOUNDARY_SKELETON_CONFIRMED`

car ce libellé est réservé à la fermeture exhaustive du maillon 2 895/2 895.

---

# G — Boundary Skeleton Gate

## `BOUNDARY_SKELETON_GATE_OPEN`

**Sens strict du OPEN :** la structure des cases est désormais matériellement admissible comme contrainte de recherche, parce que :

1. Mortlach ↔ L1 est exact 2 895/2 895 ;
2. le contrôle L1→L0 gelé donne 40/40 sur M0→M7 ;
3. les `/` négatifs donnent 8/8, donc la méthode ne confond pas ligne et mot ;
4. B1 montre déjà que les chiffrements résolus conservent les frontières linguistiques.

`OPEN` n’est PAS équivalent à « les 2 895 emplacements ont été inspectés ». Il autorise seulement les futures hypothèses qui **respectent** ce squelette ; il n’autorise aucune permutation particulière.

---

# Question finale unique

> Les 2 895 frontières que notre machine voit sont-elles réellement des frontières que l’auteur a dessinées ?

**Réponse forensic : support matériel transversal très fort, mais pas certification exhaustive des 2 895 emplacements.**

La formule finale réservée au cas exhaustif n’est donc pas écrite.

STOP B2. Aucune recherche de réordonnancement interne n’a été effectuée.

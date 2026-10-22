# Contre-épreuves et corrections

[État actuel](../SYNTHESE.md) · [Toutes les familles](README.md)

## Sommaire

- [ERR-001 — φ(230)=88, pas 172](#err-001)

- [ERR-002 — Ancien retour 212→D32 invalidé](#err-002)

- [ERR-003 — G(112) : 144 ancien,120 retenu](#err-003)

- [ERR-004 — IO : une rune oubliée dans LP1 reconstruit](#err-004)

- [ERR-005 — U5 : 112+17 ; départ 83, non 66](#err-005)

- [ERR-006 — 64→67 motifs : ajout des petits R11](#err-006)

- [ERR-007 — Trois lignes achevées n’est pas trois lignes occupées](#err-007)

- [ERR-008 — Collisions SHIFT/HERE et WEB/ROUTE](#err-008)

- [ERR-009 — Contrôles préservés,6912 exports différents](#err-009)

- [ERR-010 — Mutation synthétique conservant les contrôles](#err-010)

- [ERR-011 — Ancien F0 : 241+15 contre 240+16](#err-011)

- [ERR-012 — Archives : résumés populaires et fichiers manquants](#err-012)

<a id="err-001"></a>

# ERR-001 — φ(230)=88, pas 172

Une ancienne flèche numérique doit rester retirée.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet |  |
| Date de la source | 2026-10-17 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

230=2 × 5 × 23 ; φ=230*(1−1/2)*(1−1/5)*(1−1/23)=88.

## Ce que cela ne démontre pas

Le fait que 172 existe ailleurs dans D34 ne répare pas cette égalité fausse.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S011 — Audit de convergence avec rectificatifs du 16–17 octobre](../SOURCES.md#s011) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-006 — BUFFER S199 → inversion de champs 230](06-f0-familles-d-et-routage.md#f0-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-002"></a>

# ERR-002 — Ancien retour 212→D32 invalidé

Un parcours dépendait d’une mauvaise lecture de case.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LA VERSION RETENUE |
| Nature | CORRECTION |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

F0[50]=47, non 18 ; la route ancienne depuis 212 ne retrouve pas D32 ; la route 245→18→125 est distincte.

## Ce que cela ne démontre pas

Ne pas substituer RAW à HADDR pour présenter le même modèle comme réparé.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [SRC-008 — F0 retenu et variantes conservées](01-sources-et-conventions.md#src-008)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-003"></a>

# ERR-003 — G(112) : 144 ancien,120 retenu

Une correction change certaines continuations mais pas celles qui s’arrêtent avant.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

idx 131 : 2 O→20 ; F0[131]144→120 ; HADDR 112=131.

## Ce que cela ne démontre pas

G043→115→112 peut survivre si 112 est un descripteur terminal ; ne valide pas l’étape suivante ancienne.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [SRC-008 — F0 retenu et variantes conservées](01-sources-et-conventions.md#src-008)

- [F0-003 — HADDR et G](06-f0-familles-d-et-routage.md#f0-003)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-004"></a>

# ERR-004 — IO : une rune oubliée dans LP1 reconstruit

La référence statistique change lorsque l’on réencode mal un digraphe.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet | G005 |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

16 occurrences IO ; 3031→3015 runes ; H 4,239626→4,270097 ; sorties CP5 recalculées.

## Ce que cela ne démontre pas

La référence reste une reconstruction, non une transcription indépendante des 75 raster.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S024 — ASTRA CP5 : HOLD, tokenizer, codecs variables](../SOURCES.md#s024) — statut de diffusion et empreinte dans le catalogue.

- [SRC-005 — Gematria Primus : deux nombres distincts](01-sources-et-conventions.md#src-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-005"></a>

# ERR-005 — U5 : 112+17 ; départ 83, non 66

La dernière ligne omise change le producteur du parcours.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet | G053–G055 |
| Date de la source | 2026-10-17 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Longueurs complètes 139/91/98/96/129 ; somme signée 01101 vaut 83 ; 66 reste un trajet calculable mais plus le produit des 5 unités complètes.

## Ce que cela ne démontre pas

Propager seulement aux arêtes dépendantes ; ne pas confondre production du départ et trajet depuis une constante.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S011 — Audit de convergence avec rectificatifs du 16–17 octobre](../SOURCES.md#s011) — statut de diffusion et empreinte dans le catalogue.

- [S003 — Contrôle de couverture avant publication](../SOURCES.md#s003) — statut de diffusion et empreinte dans le catalogue.

- [M6-002 — Longueurs complètes U1–U5](05-m6-liste-et-pre64.md#m6-002)

- [VIS-005 — Lire les sites comme 01101](04-images-dessins-et-marqueurs.md#vis-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-006"></a>

# ERR-006 — 64→67 motifs : ajout des petits R11

Le détecteur initial manquait une échelle de motif.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet | G004 |
| Date de la source | 2026-10-17 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Trois R11 de G004 à carrés 4 × 4 px complètent la planche 64 ; pas une invalidation de ses 64 occurrences.

## Ce que cela ne démontre pas

Conclusion limitée au périmètre et à la source indiqués ; pas de preuve globale d’intention.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S011 — Audit de convergence avec rectificatifs du 16–17 octobre](../SOURCES.md#s011) — statut de diffusion et empreinte dans le catalogue.

- [VIS-009 — R10/R11/R13/R23 : 67 motifs documentés](04-images-dessins-et-marqueurs.md#vis-009)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-007"></a>

# ERR-007 — Trois lignes achevées n’est pas trois lignes occupées

G049 et G054 partagent un descripteur logiciel, mais pas exactement la même géométrie.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet | G049,G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

G054 first16 sur 3 lignes entières ; G049 first16 occupe 4 lignes dont 3 achevées,16e groupe au milieu de la 4e.

## Ce que cela ne démontre pas

Documenter le compteur de fins de ligne, ne pas simplifier en “exactement 3 lignes”.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [SRC-006 — Groupe physique ≠ mot lexical](01-sources-et-conventions.md#src-006)

- [OUT-002 — (112,147) →G054](09-seek-shift-et-objets-de-sortie.md#out-002)

- [OUT-004 — Exemple candidat de rotation 6](09-seek-shift-et-objets-de-sortie.md#out-004)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-008"></a>

# ERR-008 — Collisions SHIFT/HERE et WEB/ROUTE

Le même nombre ne choisit pas un seul mot.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RÉSULTAT |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

SHIFT=HERE=168 ; WEB=ROUTE=147 ; LIBER=ALL=243 ; 6508 suites ordonnées de 4 runes ont GP 200.

## Ce que cela ne démontre pas

6508 suites ne sont pas 6508 mots anglais ; n’invalide pas SHIFT si un autre indice le sélectionne.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [SRC-005 — Gematria Primus : deux nombres distincts](01-sources-et-conventions.md#src-005)

- [OUT-003 — READ 200 et footer 168](09-seek-shift-et-objets-de-sortie.md#out-003)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-009"></a>

# ERR-009 — Contrôles préservés,6912 exports différents

Les contrôles de somme et du bord ne fixent pas tous les éléments de l’export.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Permutations dans 3 premières colonnes, bord droit fixé ; 6912 identifiants distincts tout en conservant READ et sommes de colonnes.

## Ce que cela ne démontre pas

Ces permutations ne suivent généralement pas G032 ; ce ne sont pas 6912 solutions également justifiées.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [R4-002 — Noyau RIGHT/RIGHT](07-r4-et-lecteur-spatial.md#r4-002)

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-010"></a>

# ERR-010 — Mutation synthétique conservant les contrôles

Deux runes échangées changent l’identifiant sans changer les contrôles cités.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | EXPÉRIENCE |
| Pages / objet | G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Premières runes des groupes 3/4 G054 échangées dans une copie ; 147/200/168 conservés ; export djg3lc3zbygi4fwy.

## Ce que cela ne démontre pas

Ne remet pas en cause le JPEG ; montre seulement que les contrôles internes ne sont pas une authentification cryptographique.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-011"></a>

# ERR-011 — Ancien F0 : 241+15 contre 240+16

Le nombre de marqueurs a changé avec les lectures de source.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CORRIGÉ |
| Nature | CORRECTION |
| Pages / objet |  |
| Date de la source | 2026-10-03 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Conserver l’ancien binaire et ses résultats comme historique ; version retenue 240 ordinaire+16 SPECIAL(5/6/5).

## Ce que cela ne démontre pas

Ne pas reprendre les tests anciens 5/5/5 comme couverture de la version retenue.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S016 — Freeze master du 3 octobre — historique](../SOURCES.md#s016) — statut de diffusion et empreinte dans le catalogue.

- [S011 — Audit de convergence avec rectificatifs du 16–17 octobre](../SOURCES.md#s011) — statut de diffusion et empreinte dans le catalogue.

- [F0-001 — F0 : 256 octets disposés 32 × 8](06-f0-familles-d-et-routage.md#f0-001)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="err-012"></a>

# ERR-012 — Archives : résumés populaires et fichiers manquants

Un intitulé de fichier ou un récit ne suffit pas à reproduire une étape.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | CORRECTION |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

S009 distingue Agrippa, erreurs de commande et 3 pointeurs Git LFS sans charges ; la correction historique y reste attribuée.

## Ce que cela ne démontre pas

Aucune nouvelle vérification web/signature dans ce registre ; ne pas redistribuer tous les contenus tiers par défaut.

## Attribution et apport du projet

**Catégorie :** CORRECTION_OU_CONTRE_EPREUVE_DU_PROJET

**Travaux antérieurs :** Modèle antérieur et entrées désignés par les sources de cette fiche.

**Apport du projet :** Correction, comparaison de versions ou contre-épreuve documentée. Créditer séparément l’auteur du modèle corrigé et celui du contrôle ; ne pas présenter une correction arithmétique comme une invention mathématique.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S009 — Analyse des archives philosophy et puzzles](../SOURCES.md#s009) — statut de diffusion et empreinte dans le catalogue.

- [S028 — Philosophy & Symbolism — source fournie](../SOURCES.md#s028) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


# SEEK, SHIFT et objets de sortie

[État actuel](../SYNTHESE.md) · [Toutes les familles](README.md)

## Sommaire

- [OUT-001 — G073 : page à empreinte donnée](#out-001)

- [OUT-002 — (112,147) →G054](#out-002)

- [OUT-003 — READ 200 et footer 168](#out-003)

- [OUT-004 — Exemple candidat de rotation 6](#out-004)

- [OUT-005 — X16 : 16 octets de G054](#out-005)

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](#out-006)

- [OUT-007 — 48 bits retirés de X16](#out-007)

- [OUT-008 — Formule directe de l’export](#out-008)

- [OUT-009 — Export des 16 SPECIAL : 2h6vn7o256dtvsfp](#out-009)

- [OUT-010 — Ordres physiques concurrents](#out-010)

- [OUT-011 — Contrôles bornés contre G073](#out-011)

- [OUT-012 — Trace indépendante attendue](#out-012)

- [OUT-013 — G035 : échec du transfert uniforme](#out-013)

- [OUT-014 — G026 : 150 prédit,248 observé](#out-014)

- [OUT-015 — RESTORE 156 ne sélectionne pas la prochaine cible](#out-015)

- [OUT-016 — Pas encore d’objet cible reconnu](#out-016)

<a id="out-001"></a>

# OUT-001 — G073 : page à empreinte donnée

Le livre annonce une page à retrouver ; le contenu reste inconnu.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HISTORIQUE DOCUMENTÉ |
| Nature | OBJET |
| Pages / objet | G073 |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Digest imprimé 512 bits ; texte “WITHIN THE DEEP WEB…PAGE THAT HASHES TO…” ; objet cible externe.

## Ce que cela ne démontre pas

Algorithme et octets à hacher non nommés ; identifiant≠contenu ; pas de preuve que deep web impose Tor.

## Attribution et apport du projet

**Catégorie :** OBJET_OU_RESULTAT_COMMUNAUTAIRE

**Travaux antérieurs :** Matériel publié sous le nom Cicada 3301, puis conservé, transcrit et étudié par la communauté.

**Apport du projet :** Indexation, contrôle ou utilisation des copies reçues. Aucune appropriation de la création des pages, de Gematria Primus ou du texte déjà déchiffré de G073.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [Communauté CicadaSolvers ; auteurs individuels à préciser — Liber Primus Cryptanalysis Briefing / QuickStart](https://www.cicadasolvers.com/quickstart/)

## Sources et dépendances

- [S018 — Atlas global des 100 contrats — historique](../SOURCES.md#s018) — statut de diffusion et empreinte dans le catalogue.

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S037 — Contrôle indépendant des pièces externes](../SOURCES.md#s037) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-002"></a>

# OUT-002 — (112,147) →G054

Un contrôle sélectionne une page dans 27 préfixes admissibles.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

112=3|16 ; 3 fins de ligne achevées ; ΣGP 3475 mod256=147 ; valeur associée WEB depuis texte résolu G073.

## Ce que cela ne démontre pas

Le choix 147 est sémantique, non une production interne complète démontrée ; WEB/ROUTE collision.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [SRC-006 — Groupe physique ≠ mot lexical](01-sources-et-conventions.md#src-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-003"></a>

# OUT-003 — READ 200 et footer 168

Les nombres sont retrouvés ; les mots SEEK et SHIFT ne sont pas littéralement lus.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

READ=A, I, S, W de somme 200 ; footer 6 groupes[223,182,62,233,173,63], somme 936→168.

## Ce que cela ne démontre pas

200=GP(SEEK),168=GP(SHIFT) sont des égalités, pas un déchiffrement.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [OUT-002 — (112,147) →G054](09-seek-shift-et-objets-de-sortie.md#out-002)

- [R4-002 — Noyau RIGHT/RIGHT](07-r4-et-lecteur-spatial.md#r4-002)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-004"></a>

# OUT-004 — Exemple candidat de rotation 6

Les colonnes ont été interprétées comme donnée, quantité et commande.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | HYPOTHÈSE |
| Pages / objet | G049 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

G049 col GP=[159,282,276,168] ; 282−276=6 ; ROR8(159,6)=126 ; quatre opérations comparées.

## Ce que cela ne démontre pas

ROR8(6)=ROL8(2) ; la provenance du contrôle 222 et la sémantique restent hypothétiques.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [R4-002 — Noyau RIGHT/RIGHT](07-r4-et-lecteur-spatial.md#r4-002)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-005"></a>

# OUT-005 — X16 : 16 octets de G054

La recette produit un bloc binaire, mais son rôle n’est pas établi.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

ΣGP par groupe→mod256→ordre G032→ROR8(6) ; hex 0309263b6b02dbb9910846e8bc6516f8.

## Ce que cela ne démontre pas

Les sommes modulo 256 sont déjà une réduction ; la rotation est réversible ; ni clé ni fichier reconnus.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [OUT-002 — (112,147) →G054](09-seek-shift-et-objets-de-sortie.md#out-002)

- [OUT-004 — Exemple candidat de rotation 6](09-seek-shift-et-objets-de-sortie.md#out-004)

- [R4-001 — G032 : parcours 16 reconstruit](07-r4-et-lecteur-spatial.md#r4-001)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-006"></a>

# OUT-006 — Export G054 : djg3lc3zrigi4fwy

Cinq bits par octet sont transformés en caractères Base32.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE |
| Nature | HYPOTHÈSE |
| Pages / objet | G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

LOW5 de X16 →16 symboles ; octets regroupés 1a4db58b798a0c8e16d8 ; suffixe.onion ajouté par l’interprétation.

## Ce que cela ne démontre pas

Format garanti par la recette ; aucun service ou contenu authentifié ; distinct de V6.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [OUT-005 — X16 : 16 octets de G054](09-seek-shift-et-objets-de-sortie.md#out-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-007"></a>

# OUT-007 — 48 bits retirés de X16

Cette information n’a pas d’emploi établi dans la branche d’export.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G054 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Trois bits supérieurs après rotation de chacun des 16 octets ; regroupement hexadécimal 009635817ac7.

## Ce que cela ne démontre pas

Résidu créé par notre transformation ; son existence ne prouve pas un message secondaire intentionnel.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [OUT-005 — X16 : 16 octets de G054](09-seek-shift-et-objets-de-sortie.md#out-005)

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-008"></a>

# OUT-008 — Formule directe de l’export

La même sortie peut se calculer sans état ni instruction nommée SHIFT.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RÉSULTAT |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

LOW5(ROR8(b,6))=4*(b mod 8)+floor(b/64), vérifiée pour 256 octets dans l’audit.

## Ce que cela ne démontre pas

Équivalence d’implémentations, pas réfutation de toute VM ; la sortie ne prouve pas chaque composant.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-009"></a>

# OUT-009 — Export des 16 SPECIAL : 2h6vn7o256dtvsfp

Une seconde recette indépendante de G054 conserve cinq bits par marqueur.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE |
| Nature | HYPOTHÈSE |
| Pages / objet | G032,G066–G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

hhh111cc→hhhcc ; 16 SPECIAL × 5 bits ; G032 puis Base32 ; d1fd56fddaef873ac8af.

## Ce que cela ne démontre pas

“Indépendante” au sens recette différente, pas preuve statistique indépendante ; adresse non corroborée.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S035 — V6 : export des16 SPECIAL](../SOURCES.md#s035) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

- [R4-001 — G032 : parcours 16 reconstruit](07-r4-et-lecteur-spatial.md#r4-001)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-010"></a>

# OUT-010 — Ordres physiques concurrents

Des règles alternatives donnent des identifiants de même format.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RÉSULTAT |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

V6 physique o25672hdnv6tpfsv ; G054 physique 3zricdjgl3giywf4 ; format Base32 n’arbitre pas l’ordre.

## Ce que cela ne démontre pas

Ces concurrents ne respectent pas forcément G032 ; pas des solutions également motivées.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

- [OUT-009 — Export des 16 SPECIAL : 2h6vn7o256dtvsfp](09-seek-shift-et-objets-de-sortie.md#out-009)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-011"></a>

# OUT-011 — Contrôles bornés contre G073

Aucun des objets effectivement testés n’a donné l’empreinte.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NÉGATIF BORNÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

33 sérialisations de X et entrées directes sous SHA-512 ; 335 contenus distincts des ZIP bruts ; zéro concordance.

## Ce que cela ne démontre pas

Hacher un identifiant≠hacher sa page ; autres algorithmes, sérialisations et 3 charges LFS absentes non couverts.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [OUT-001 — G073 : page à empreinte donnée](09-seek-shift-et-objets-de-sortie.md#out-001)

- [OUT-005 — X16 : 16 octets de G054](09-seek-shift-et-objets-de-sortie.md#out-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-012"></a>

# OUT-012 — Trace indépendante attendue

L’agent archives doit apporter un objet vérifiable, pas une simple erreur réseau.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | PROTOCOLE |
| Nature | PROTOCOLE |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Conserver original, date, provenance, hash ; distinguer mention, descripteur signé, page ; contrôler digest complet sans normalisation silencieuse.

## Ce que cela ne démontre pas

Activité de l’agent signalée par l’utilisateur ; aucun nouveau résultat intégré dans ce registre.

## Attribution et apport du projet

**Catégorie :** CONVENTION_OU_SYNTHESE_DU_PROJET

**Travaux antérieurs :** Objets et résultats des sources citées ; méthodes générales de documentation, d’indexation et de vérification.

**Apport du projet :** Choix de présentation, convention ou organisation appliqué dans ATELIER PRIMUS. Ce n’est pas une revendication de découverte du contenu du livre.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S037 — Contrôle indépendant des pièces externes](../SOURCES.md#s037) — statut de diffusion et empreinte dans le catalogue.

- [OUT-001 — G073 : page à empreinte donnée](09-seek-shift-et-objets-de-sortie.md#out-001)

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

- [OUT-009 — Export des 16 SPECIAL : 2h6vn7o256dtvsfp](09-seek-shift-et-objets-de-sortie.md#out-009)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-013"></a>

# OUT-013 — G035 : échec du transfert uniforme

Le même nom de somme 168 ne reproduit pas partout l’exemple G049.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet | G035 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

G035 colonnes 154/98/210/168 ; (98−210)mod 8=0 ; sortie 154 ordinaire, non SPECIAL.

## Ce que cela ne démontre pas

Portée 2|16 contre 3|16 ; règle locale typée non globalement réfutée.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [OUT-004 — Exemple candidat de rotation 6](09-seek-shift-et-objets-de-sortie.md#out-004)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-014"></a>

# OUT-014 — G026 : 150 prédit,248 observé

La généralisation du paquet arithmétique a échoué sur une nouvelle sélection.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet | G026 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

223=prime 48,151 présent ; φ151=150 attendu ; mot suivant 248 ; élargissement 0/15.

## Ce que cela ne démontre pas

Ne réfute pas le paquet G023 lui-même ; pas de réparation après lecture.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S007 — Sélection R4 et prédiction du paquet arithmétique](../SOURCES.md#s007) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [LNK-010 — Paquet 409/245/168 →80](08-raccords-multi-supports.md#lnk-010)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-015"></a>

# OUT-015 — RESTORE 156 ne sélectionne pas la prochaine cible

Cette façon de prolonger le circuit n’a aucune cible dans son univers.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

29 préfixes 2|16 ; zéro checksum 156 ; première condition nécessaire échoue.

## Ce que cela ne démontre pas

Ne réfute pas tous les emplois de 156 ni le noyau de lecture.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S008 — Prédiction D : ablation d’état et H156](../SOURCES.md#s008) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-013 — 198 →156 : RETOUR de valeur](06-f0-familles-d-et-routage.md#f0-013)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="out-016"></a>

# OUT-016 — Pas encore d’objet cible reconnu

La chaîne calculatoire reste différente d’une sortie de LP validée.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON OBTENU |
| Nature | CONCLUSION |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Aucun nouveau plaintext, service, préimage ou microcode historique authentifié dans l’audit récent.

## Ce que cela ne démontre pas

Ce constat ne dit pas que LP ne peut pas être résolu.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S005 — SEEK → X : extraction et limites](../SOURCES.md#s005) — statut de diffusion et empreinte dans le catalogue.

- [OUT-006 — Export G054 : djg3lc3zrigi4fwy](09-seek-shift-et-objets-de-sortie.md#out-006)

- [OUT-009 — Export des 16 SPECIAL : 2h6vn7o256dtvsfp](09-seek-shift-et-objets-de-sortie.md#out-009)

- [OUT-011 — Contrôles bornés contre G073](09-seek-shift-et-objets-de-sortie.md#out-011)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


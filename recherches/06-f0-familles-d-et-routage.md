# F0, familles D et routage

[État actuel](../SYNTHESE.md) · [Toutes les familles](README.md)

## Sommaire

- [F0-001 — F0 : 256 octets disposés 32 × 8](#f0-001)

- [F0-002 — high3, low5 et familles D](#f0-002)

- [F0-003 — HADDR et G](#f0-003)

- [F0-004 — 16 SPECIAL, G032 et fenêtre[6,7,4]](#f0-004)

- [F0-005 — D34 : quatre octets internes](#f0-005)

- [F0-006 — BUFFER S199 → inversion de champs 230](#f0-006)

- [F0-007 — D36 : intervalle de 36 cellules](#f0-007)

- [F0-008 — Quartet de D36 vers BODY36](#f0-008)

- [F0-009 — Fenêtre 212–247 : BODY36](#f0-009)

- [F0-010 — 35 sorties ordinaires puis D33](#f0-010)

- [F0-011 — 35 octets produits avant D33](#f0-011)

- [F0-012 — D33 : événement de valeur 126](#f0-012)

- [F0-013 — 198 →156 : RETOUR de valeur](#f0-013)

- [F0-014 — 254 →192 →126](#f0-014)

- [F0-015 — 245 →18 →125 →121](#f0-015)

- [F0-016 — [A, B, C] →[B, C, D] : registre glissant](#f0-016)

- [F0-017 — Itinéraires F0 vers 73/74](#f0-017)

- [F0-018 — Les familles D sont-elles des états actifs ?](#f0-018)

<a id="f0-001"></a>

# F0-001 — F0 : 256 octets disposés 32 × 8

La table est un objet numérique exploitable ; son rôle de programme reste une hypothèse.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G066–G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

256 tokens imprimés interprétés en base 60 ; 240 ordinaires,16 low5≥29 ; répartition 5/6/5 pour 29/30/31.

## Ce que cela ne démontre pas

F0 n’est pas une permutation de 256 valeurs ; ne pas l’appeler mémoire active sans règle d’évolution.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S011 — Audit de convergence avec rectificatifs du 16–17 octobre](../SOURCES.md#s011) — statut de diffusion et empreinte dans le catalogue.

- [SRC-008 — F0 retenu et variantes conservées](01-sources-et-conventions.md#src-008)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-002"></a>

# F0-002 — high3, low5 et familles D

Nous séparons un octet en deux champs pour décrire sa structure.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CONVENTION |
| Nature | CONVENTION |
| Pages / objet | G066–G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

h=b>>5, l=b&31 ; SPECIAL si l≥29 ; famille Dn avec n=h+l dans la convention utilisée.

## Ce que cela ne démontre pas

“état”, “opcode” et“argument” ajoutent une interprétation ; les nombres seuls ne l’imposent pas.

## Attribution et apport du projet

**Catégorie :** CONVENTION_OU_SYNTHESE_DU_PROJET

**Travaux antérieurs :** Objets et résultats des sources citées ; méthodes générales de documentation, d’indexation et de vérification.

**Apport du projet :** Choix de présentation, convention ou organisation appliqué dans ATELIER PRIMUS. Ce n’est pas une revendication de découverte du contenu du livre.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S002 — Glossaire de recherche](../SOURCES.md#s002) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-001 — F0 : 256 octets disposés 32 × 8](06-f0-familles-d-et-routage.md#f0-001)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-003"></a>

# F0-003 — HADDR et G

Une formule transforme les deux champs en index, puis lit une case.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G066–G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

HADDR(b)=8*(b&31)+(b>>5) ; G(b)=F0[HADDR(b)].

## Ce que cela ne démontre pas

Distinguer index et contenu ; un parcours déterministe n’est pas une instruction déchiffrée.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S002 — Glossaire de recherche](../SOURCES.md#s002) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-004"></a>

# F0-004 — 16 SPECIAL, G032 et fenêtre[6,7,4]

Un arrangement candidat relie des marqueurs aux tags de R4.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE |
| Nature | HYPOTHÈSE |
| Pages / objet | G032,G066–G068 |
| Date de la source | 2026-10-03 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Freeze historique : class 30 en T sous ORDERING 16 ; core[3,6,7], leaves[6,7,4] ; state-carry proposé.

## Ce que cela ne démontre pas

Le classement numérique exact n’établit ni registre glissant ni transition intentionnelle.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S016 — Freeze master du 3 octobre — historique](../SOURCES.md#s016) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

- [R4-001 — G032 : parcours 16 reconstruit](07-r4-et-lecteur-spatial.md#r4-001)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-005"></a>

# F0-005 — D34 : quatre octets internes

Un intervalle de quatre valeurs est bien identifié sous les bornes retenues.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Entrée 4|30@249 ; payload[172,230,180,36] ; fermeture 5|29@254 dans F0 retenu.

## Ce que cela ne démontre pas

Le rôle FRAME/SUBROUTINE est proposé ; le payload n’est pas un texte déchiffré.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-001 — F0 : 256 octets disposés 32 × 8](06-f0-familles-d-et-routage.md#f0-001)

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-006"></a>

# F0-006 — BUFFER S199 → inversion de champs 230

La valeur 230 relie une lecture possible de G005 et le payload D34.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G005,G068 |
| Date de la source | 2026-10-03 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

199=6|7 ; inversion des deux champs interprétée comme 7|6=230 ; 230 présent dans D34.

## Ce que cela ne démontre pas

Échanger des champs de largeurs différentes est une convention ; pas une commande universelle.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S016 — Freeze master du 3 octobre — historique](../SOURCES.md#s016) — statut de diffusion et empreinte dans le catalogue.

- [S030 — V5 : noyau et bootstrap 80/245](../SOURCES.md#s030) — statut de diffusion et empreinte dans le catalogue.

- [LP1-004 — G005 : carré mixte et demi-tour](02-apprentissage-et-precedents.md#lp1-004)

- [F0-005 — D34 : quatre octets internes](06-f0-familles-d-et-routage.md#f0-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-007"></a>

# F0-007 — D36 : intervalle de 36 cellules

La taille est reconnue, mais son contenu n’a pas une fonction homogène démontrée.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G066–G067 |
| Date de la source | 2026-10-03 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Intervalle ordinaireidx 12.. 47 borné par 6|30@11 et 7|29@48 ; candidats 4+32 et 6 × 6 à distinguer.

## Ce que cela ne démontre pas

L’emploi de quelques valeurs ne suffit pas à expliquer les 36 cellules.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S016 — Freeze master du 3 octobre — historique](../SOURCES.md#s016) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S036 — V3 : flux et continuations](../SOURCES.md#s036) — statut de diffusion et empreinte dans le catalogue.

- [F0-001 — F0 : 256 octets disposés 32 × 8](06-f0-familles-d-et-routage.md#f0-001)

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-008"></a>

# F0-008 — Quartet de D36 vers BODY36

Quatre valeurs anciennes concordent avec les bornes d’une autre fenêtre.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE |
| Nature | RACCORD |
| Pages / objet | G066–G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

idx 12..15=[247,4,183,212] ; 212/247 sont bornes candidates ; G(183)=192=F0[247].

## Ce que cela ne démontre pas

Les valeurs sont calculables ; le rôle d’en-tête et le branchement sont interprétatifs.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S049 — D36 : quartet et fenêtre BODY36](../SOURCES.md#s049) — statut de diffusion et empreinte dans le catalogue.

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [F0-007 — D36 : intervalle de 36 cellules](06-f0-familles-d-et-routage.md#f0-007)

- [F0-003 — HADDR et G](06-f0-familles-d-et-routage.md#f0-003)

- [F0-009 — Fenêtre 212–247 : BODY36](06-f0-familles-d-et-routage.md#f0-009)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-009"></a>

# F0-009 — Fenêtre 212–247 : BODY36

Cette fenêtre a un début, une fin et des contrôles précis sous le modèle R4.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

HADDR(154)=212 ; HADDR(254)=247 ; 36 octets inclus ; F0[246]=198 ; somme 4551, mod 256199.

## Ce que cela ne démontre pas

Les bornes dépendent du lecteur et de son emploi ; ne pas confondre avec D36 idx 12..47.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [F0-003 — HADDR et G](06-f0-familles-d-et-routage.md#f0-003)

- [R4-005 — Trois BODY16 →198/254/154](07-r4-et-lecteur-spatial.md#r4-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-010"></a>

# F0-010 — 35 sorties ordinaires puis D33

Une consommation uniforme de la fenêtre atteint un marqueur à sa dernière cellule.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Pouri 212..247, calculer G(F0[i]) ; 35 sorties ordinaires, puis 126=D33.

## Ce que cela ne démontre pas

SPECIAL en dernière position ne prouve pas la commande STOP ; les 35 octets ont encore un rôle à établir.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [F0-009 — Fenêtre 212–247 : BODY36](06-f0-familles-d-et-routage.md#f0-009)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-011"></a>

# F0-011 — 35 octets produits avant D33

La production est connue, mais aucun usage complet de leur contenu n’est démontré.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | OBJET |
| Pages / objet | G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Vecteur[G(F0[212]), …, G(F0[246])] ; distinct des 35 mots résiduels R4 et des 35 mots de G071.

## Ce que cela ne démontre pas

Égalité de longueur seule insuffisante ; indices directs vers 35 mots déjà négatifs.

## Test discriminant

Proposition de suivi : Une règle utilisant le contenu, avec type de cible et contrôle distinct, plutôt qu’un simple compte.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [S019 — Campagne six familles : 2 873 888 configurations](../SOURCES.md#s019) — statut de diffusion et empreinte dans le catalogue.

- [F0-010 — 35 sorties ordinaires puis D33](06-f0-familles-d-et-routage.md#f0-010)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-012"></a>

# F0-012 — D33 : événement de valeur 126

Le même marqueur a plusieurs emplois proposés ; sa commande n’est pas résolue.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE |
| Nature | OBJET |
| Pages / objet | G066,G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

126=3|30 ; arrivée après G(192) ; interprétations STOP, FRAME, RECURSIVE à distinguer.

## Ce que cela ne démontre pas

Un mot de notre glossaire ne choisit pas à lui seul STOP ou RETURN.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S018 — Atlas global des 100 contrats — historique](../SOURCES.md#s018) — statut de diffusion et empreinte dans le catalogue.

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

- [F0-010 — 35 sorties ordinaires puis D33](06-f0-familles-d-et-routage.md#f0-010)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-013"></a>

# F0-013 — 198 →156 : RETOUR de valeur

Deux loci retrouvent 156 ; l’égalité n’est pas une mutation de mémoire observée.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G066 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

G(198)=F0[54]=156 ; F0[10]=156 ; nom RESTORE proposé.

## Ce que cela ne démontre pas

Pas de preuve qu’un contexte a été sauvegardé puis restauré.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [S022 — R4 MULTIPASS : arbres et TAIL14](../SOURCES.md#s022) — statut de diffusion et empreinte dans le catalogue.

- [F0-003 — HADDR et G](06-f0-familles-d-et-routage.md#f0-003)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-014"></a>

# F0-014 — 254 →192 →126

Un parcours vers D33 est reproductible.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G066,G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

G(254)=F0[247]=192 ; G(192)=F0[6]=126.

## Ce que cela ne démontre pas

Nom DISPATCH descriptif ; ne démontre pas un saut d’instruction.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [F0-003 — HADDR et G](06-f0-familles-d-et-routage.md#f0-003)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-015"></a>

# F0-015 — 245 →18 →125 →121

Le retour corrigé survit à la version retenue de F0.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RACCORD |
| Pages / objet | G066–G068 |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

G(245)=18 ; G(18)=125=3|29 ; HADDR(125)=235 ; F0[235]=121, tokenbase 60“21”.

## Ce que cela ne démontre pas

Le token“21” n’est pas l’octet 21. Production de 245 par certaines variantes TAIL14 non entièrement reconstruite.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S006 — Rétablissement V3–V6 des deux échanges](../SOURCES.md#s006) — statut de diffusion et empreinte dans le catalogue.

- [F0-003 — HADDR et G](06-f0-familles-d-et-routage.md#f0-003)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-016"></a>

# F0-016 — [A, B, C] →[B, C, D] : registre glissant

La forme d’une transition ne définit pas la règle qui produit D.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE |
| Nature | HYPOTHÈSE |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Les tags[3,6,7]→[6,7,4] sont utilisés dans le modèle ; plusieurs récurrences simples conviennent au seul passage.

## Ce que cela ne démontre pas

L’ablation du lecteur sans état est R4-012 ; aucun D nouveau validé par cette forme seule.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S008 — Prédiction D : ablation d’état et H156](../SOURCES.md#s008) — statut de diffusion et empreinte dans le catalogue.

- [S029 — V5 : machine candidate A→Z](../SOURCES.md#s029) — statut de diffusion et empreinte dans le catalogue.

- [F0-004 — 16 SPECIAL, G032 et fenêtre[6,7,4]](06-f0-familles-d-et-routage.md#f0-004)

- [R4-005 — Trois BODY16 →198/254/154](07-r4-et-lecteur-spatial.md#r4-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-017"></a>

# F0-017 — Itinéraires F0 vers 73/74

Les trajets numériques existent, mais transformer les nombres en pages est une étape séparée.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | EXPÉRIENCE |
| Pages / objet | G053–G055,G066–G074 |
| Date de la source | 2026-10-17 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

S011 : trajets depuis 66 et 184 ; aprèscorrection U5 départ 83 ; graphe de fonction finie avec cycles 11 et 2.

## Ce que cela ne démontre pas

Trajets partageant des arcs ne sont pas indépendants ; couper des cycles donne des arbres dans toute fonction finie.

## Attribution et apport du projet

**Catégorie :** ANALYSE_CONSIGNEE_DANS_LE_PROJET

**Travaux antérieurs :** Les entrées, méthodes et pièces citées restent créditées à leurs auteurs. La chaîne d’inspiration complète de cette fiche n’est pas encore reconstituée.

**Apport du projet :** Analyse documentée dans les sources de cette fiche ; la présence dans le dossier ne démontre pas que le projet est le premier auteur de l’idée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S011 — Audit de convergence avec rectificatifs du 16–17 octobre](../SOURCES.md#s011) — statut de diffusion et empreinte dans le catalogue.

- [F0-001 — F0 : 256 octets disposés 32 × 8](06-f0-familles-d-et-routage.md#f0-001)

- [VIS-005 — Lire les sites comme 01101](04-images-dessins-et-marqueurs.md#vis-005)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="f0-018"></a>

# F0-018 — Les familles D sont-elles des états actifs ?

Les labels numériques existent ; la mémoire modifiable reste à démontrer.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | INCONCLUSIF |
| Nature | HYPOTHÈSE |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Rôle possible d’adressage, de référence ou d’état ; les mêmes sorties peuvent être reproduites par certains lecteurs sans état.

## Ce que cela ne démontre pas

Conclusion limitée au périmètre et à la source indiqués ; pas de preuve globale d’intention.

## Test discriminant

Proposition de suivi : Même objet et même événement, états entrants différents, décision prédite puis contrôle indépendant.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Objets, recettes et résultats cités dans les dépendances de la fiche.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S004 — Audit interne V3–V6 et SEEK/SHIFT](../SOURCES.md#s004) — statut de diffusion et empreinte dans le catalogue.

- [S008 — Prédiction D : ablation d’état et H156](../SOURCES.md#s008) — statut de diffusion et empreinte dans le catalogue.

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

- [F0-002 — high3, low5 et familles D](06-f0-familles-d-et-routage.md#f0-002)

- [AST-013 — ÉTAU : 384 machines 32 × 8](03-astra-et-cryptanalyse.md#ast-013)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


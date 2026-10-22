# ASTRA et cryptanalyse

[État actuel](../SYNTHESE.md) · [Toutes les familles](README.md)

## Sommaire

- [AST-001 — HEAD24 : 70 faux négatifs identifiés](#ast-001)

- [AST-002 — B2 : réparation de l’alignement](#ast-002)

- [AST-003 — B2 : fond LP2 et limite de couverture](#ast-003)

- [AST-004 — Six familles de lecteurs R4](#ast-004)

- [AST-005 — Contrôles positifs de la grande campagne](#ast-005)

- [AST-006 — Rareté des répétitions immédiates](#ast-006)

- [AST-007 — CP3/CP4 : différences et modèle avec mémoire](#ast-007)

- [AST-008 — CP4 : horloges matérielles et F0](#ast-008)

- [AST-009 — CP4 : tirage sans répétition dans des blocs](#ast-009)

- [AST-010 — Réétiquetage et transposition conservent l’entropie](#ast-010)

- [AST-011 — CP5 : échappement D 0, D 1](#ast-011)

- [AST-012 — CP5 : codage arithmétique base 28](#ast-012)

- [AST-013 — ÉTAU : 384 machines 32 × 8](#ast-013)

- [AST-014 — ÉTAU : SPECIAL et ponctuation](#ast-014)

- [AST-015 — Reset indépendant uniforme après un mot](#ast-015)

- [AST-016 — Distribution des déplacements selon les frontières](#ast-016)

- [AST-017 — Resets synthétiques des commandes 29/30/31](#ast-017)

- [AST-018 — Lag-5 : signal, pas période de clé](#ast-018)

- [AST-019 — Concentration lag-5 par identité](#ast-019)

- [AST-020 — RAKE T 1–T 5 bloqué](#ast-020)

- [AST-021 — Pourquoi explorer une lecture de données](#ast-021)

<a id="ast-001"></a>

# AST-001 — HEAD24 : 70 faux négatifs identifiés

Un filtre pouvait rejeter une bonne solution avant l’analyse approfondie.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-09-24 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Sur 256 contrôles historiques,70 faux négatifs ; le vrai alignement fait passer 70/70 au même seuil. Gate de 256 graines/scores/décisions reproduit dans le rapport.

## Ce que cela ne démontre pas

Diagnostic de cet instrument, pas preuve d’une clé LP2.

## Suite proposée

Conserver les jeux de contrôle et la version du filtre avec chaque balayage.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S012 — Diagnostic HEAD24 et récupération des contrôles](../SOURCES.md#s012) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-002"></a>

# AST-002 — B2 : réparation de l’alignement

Le filtre amélioré retrouve mieux ses contrôles, mais laisse beaucoup de faux candidats.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-09-24 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

DP exact HEAD24 ; 4078/4096 sur nouveau holdout ; IC de Wilson 95%[99,3064%; 99,7218%]. 18 faux négatifs conservés.

## Ce que cela ne démontre pas

Rappel valable sous le générateur, le registre linguistique et le seuil déclarés ; pas universel.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S013 — B2 HEAD24 : rappel et inflation](../SOURCES.md#s013) — statut de diffusion et empreinte dans le catalogue.

- [AST-001 — HEAD24 : 70 faux négatifs identifiés](03-astra-et-cryptanalyse.md#ast-001)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-003"></a>

# AST-003 — B2 : fond LP2 et limite de couverture

Une projection de milliards de graines n’est pas un balayage terminé.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-09-24 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Fond réellement terminé : 65536 graines ; 6438 passent B2 ; 6424 B2-only. Projection 421 M et coût estimé, pas exécution 2^32.

## Ce que cela ne démontre pas

Ne pas présenter B2 comme attaque complète 2^32 ; B3 non exécuté dans ce rapport.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S013 — B2 HEAD24 : rappel et inflation](../SOURCES.md#s013) — statut de diffusion et empreinte dans le catalogue.

- [AST-002 — B2 : réparation de l’alignement](03-astra-et-cryptanalyse.md#ast-002)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-004"></a>

# AST-004 — Six familles de lecteurs R4

Des millions de variantes n’ont pas donné de nouveau texte validé dans cet univers.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NÉGATIF BORNÉ |
| Nature | CAMPAGNE |
| Pages / objet | G069–G070 |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

208800 LP1 direct ; 589824 F0 statique ; 245760 F0 à état ; 35840 interface 35 mots ; 1403904 G032 ; 389760 GP-mots. Total 2873888 configurations rapportées.

## Ce que cela ne démontre pas

Pas autant de modèles indépendants ; journal de campagne détaillé à relier, pas de nouveau rejeu ici.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S019 — Campagne six familles : 2 873 888 configurations](../SOURCES.md#s019) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-005"></a>

# AST-005 — Contrôles positifs de la grande campagne

Les détecteurs ont une sensibilité mesurée sur des signaux précis.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Rapport de campagne : 400/400,399/400,400/400 sur 400 nouveaux contrôles synthétiques par interface.

## Ce que cela ne démontre pas

Détecter ces signaux ne garantit ni toute langue ni une sortie binaire ; incertitude et alternatives à garder.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S019 — Campagne six familles : 2 873 888 configurations](../SOURCES.md#s019) — statut de diffusion et empreinte dans le catalogue.

- [AST-004 — Six familles de lecteurs R4](03-astra-et-cryptanalyse.md#ast-004)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-006"></a>

# AST-006 — Rareté des répétitions immédiates

Le flux évite fortement les runes identiques adjacentes.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | OBSERVATION |
| Pages / objet | G017–G072 |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Dans le périmètre ÉTAU : 86 doublets pour 12901 transitions internes aux pages ; taux et frontières détaillés dans le rapport.

## Ce que cela ne démontre pas

Une dépendance statistique ne prouve ni OTP ni mémoire logicielle.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

- [S020 — Rétro-ingénierie LP : CP4 et modèles concurrents](../SOURCES.md#s020) — statut de diffusion et empreinte dans le catalogue.

- [SRC-010 — Quatre tailles de corpus à ne pas fusionner](01-sources-et-conventions.md#src-010)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-007"></a>

# AST-007 — CP3/CP4 : différences et modèle avec mémoire

Expliquer les répétitions ne suffit pas à retrouver le texte.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON SOUTENU POUR LE DÉCHIFFREMENT |
| Nature | EXPÉRIENCE |
| Pages / objet | G017–G072 |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Le rapport conserve un gain de vraisemblance du Markov sur validation/réplication, mais pas de consommateur donnant du plaintext.

## Ce que cela ne démontre pas

Conserver paramètres, segments et correctif IO ; pas d’attribution de chiffre.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S020 — Rétro-ingénierie LP : CP4 et modèles concurrents](../SOURCES.md#s020) — statut de diffusion et empreinte dans le catalogue.

- [AST-006 — Rareté des répétitions immédiates](03-astra-et-cryptanalyse.md#ast-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-008"></a>

# AST-008 — CP4 : horloges matérielles et F0

Les frontières ont été essayées comme commandes d’avance.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NÉGATIF BORNÉ |
| Nature | EXPÉRIENCE |
| Pages / objet | G017–G072 |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

24090 configurations d’horloge ; 180 variantes F0 ; aucun lecteur validé sur les deux ensembles réservés rapportés.

## Ce que cela ne démontre pas

Scores CP4 dépendaient d’un LP1 reconstruit corrigé ensuite ; pas de rejet universel.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S020 — Rétro-ingénierie LP : CP4 et modèles concurrents](../SOURCES.md#s020) — statut de diffusion et empreinte dans le catalogue.

- [S024 — ASTRA CP5 : HOLD, tokenizer, codecs variables](../SOURCES.md#s024) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-009"></a>

# AST-009 — CP4 : tirage sans répétition dans des blocs

Un mécanisme pouvait reproduire un taux global mais échouait sur les positions.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Modèle strict : 68 répétitions internes là où zéro était requis ; 18 aux frontières. 270 configurations testées ; meilleure variante assouplie non répliquée.

## Ce que cela ne démontre pas

Falsifie ces blocs fixes, pas tout évitement des doubles.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S020 — Rétro-ingénierie LP : CP4 et modèles concurrents](../SOURCES.md#s020) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-010"></a>

# AST-010 — Réétiquetage et transposition conservent l’entropie

Changer seulement les noms ou l’ordre ne change pas la distribution des fréquences.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | CALCUL CONDITIONNEL |
| Nature | RÉSULTAT |
| Pages / objet |  |
| Date de la source | Date non explicitée dans la pièce |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Limite du modèle différences→bijection fixe→transposition, si l’on exige une distribution comparable à la référence LP1.

## Ce que cela ne démontre pas

La comparaison de référence est conditionnelle ; CP5 corrige H LP1 à 4,270097. Ne prouve pas l’absence de texte.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S020 — Rétro-ingénierie LP : CP4 et modèles concurrents](../SOURCES.md#s020) — statut de diffusion et empreinte dans le catalogue.

- [S024 — ASTRA CP5 : HOLD, tokenizer, codecs variables](../SOURCES.md#s024) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-011"></a>

# AST-011 — CP5 : échappement D 0, D 1

Le format testé imposait une suite après chaque événement spécial ; LP2 la viole.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Contrôle LP1 intégral réversible ; LP2 seulement 2/85 obligations satisfaites,83 violations ; 0/40 événements dans les ensembles réservés.

## Ce que cela ne démontre pas

Pas d’exclusion de tous les codes à longueur variable.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S024 — ASTRA CP5 : HOLD, tokenizer, codecs variables](../SOURCES.md#s024) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-012"></a>

# AST-012 — CP5 : codage arithmétique base 28

Des codecs corrects sur LP1 ne cadrent pas les données R4.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet | G069–G070 |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

N 16 : 189 blocs LP1 passent ; cadrage R4 impossible sous ce contrat. Variante mots : 763 contrôles LP1 ; 1/86 mots R4 passe le cycle canonique.

## Ce que cela ne démontre pas

Conclusion limitée aux formats de paquets définis.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S024 — ASTRA CP5 : HOLD, tokenizer, codecs variables](../SOURCES.md#s024) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-013"></a>

# AST-013 — ÉTAU : 384 machines 32 × 8

La version la plus directe d’une VM de runes n’a pas donné le comportement attendu.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON SOUTENU |
| Nature | EXPÉRIENCE |
| Pages / objet | G068–G070 |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

T(s, r)=F0[8 r+s] ; high3 nouvel état, low5 sortie. 384 contrats ; aucun 4/4 sur[6,7,4,3] ; meilleur 2/4.

## Ce que cela ne démontre pas

F0 ancien 020134 et variante 131 ; ne pas appliquer le verdict automatiquement à tout modèle de VM.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

- [SRC-008 — F0 retenu et variantes conservées](01-sources-et-conventions.md#src-008)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-014"></a>

# AST-014 — ÉTAU : SPECIAL et ponctuation

Les marqueurs émis ne s’alignent pas de façon confirmée sur les frontières.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON SOUTENU |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Sous-famille admissible au null : p(max T)=310/390≈0,794872 ; ancien calcul≈0,651 remplacé.

## Ce que cela ne démontre pas

Les programmes qui utilisent les frontières testées doivent être recalculés sous chaque permutation, pas mélangés au même null.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

- [AST-013 — ÉTAU : 384 machines 32 × 8](03-astra-et-cryptanalyse.md#ast-013)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-015"></a>

# AST-015 — Reset indépendant uniforme après un mot

Oublier complètement la rune précédente à chaque tiret ne correspond pas à ces comptages.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | FALSIFIÉ DANS LE CONTRAT |
| Nature | EXPÉRIENCE |
| Pages / objet | G017–G072 |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

22 doublets/2716 tirets contre 93,7 attendus sous uniforme 29 indépendant ; deux moitiés concordantes.

## Ce que cela ne démontre pas

Ne rejette pas un reset de clé conservant un mécanisme anti-répétition.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

- [AST-006 — Rareté des répétitions immédiates](03-astra-et-cryptanalyse.md#ast-006)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-016"></a>

# AST-016 — Distribution des déplacements selon les frontières

Ajouter la catégorie de frontière dégrade ici la prédiction.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON SOUTENU |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Gains croisés−33,36 et−41,22 nats ; null p≈0,575 ; puissance 83,1% pour injection 5%, moins pour signaux faibles.

## Ce que cela ne démontre pas

Effets faibles inconclusifs ; pas de preuve d’absence de commande arbitraire.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-017"></a>

# AST-017 — Resets synthétiques des commandes 29/30/31

Trouver un reset dans une table ne prouve pas qu’elle code un programme intentionnel.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | DOCUMENTÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-10-14 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

363 suites≤5 ; trois resets de longueur 5 ; aucun dans la liste naturelle ; 84,3% des 1200 tables aléatoires ont un reset à cette profondeur.

## Ce que cela ne démontre pas

Recettes inventées et testées ; pas instructions déchiffrées.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Problèmes, corpus et méthodes antérieurs décrits par les rapports. Les campagnes d’autres équipes ne sont pas comptées dans nos essais.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

## Sources et dépendances

- [S025 — ÉTAU Agent1 : machine 32×8, état et frontières](../SOURCES.md#s025) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-018"></a>

# AST-018 — Lag-5 : signal, pas période de clé

Une répétition à distance cinq ne dit pas comment déchiffrer.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HISTORIQUE DOCUMENTÉ |
| Nature | OBSERVATION |
| Pages / objet |  |
| Date de la source | 2026-10-03 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Le freeze antérieur retient d 5 intra-mot parmi 2..8, mais pas de phase 5 ni de fenêtre 5 privilégiée.

## Ce que cela ne démontre pas

Garder le périmètre et les nuls propres ; ne pas convertir 5 en opcode.

## Attribution et apport du projet

**Catégorie :** RESULTAT_PUBLIE_ET_REPRODUCTION

**Travaux antérieurs :** Signal lag-5 publié notamment par ZzNible ; le déficit de répétitions adjacentes est également documenté dans les travaux communautaires.

**Apport du projet :** Reproduction conditionnelle et examens complémentaires consignés dans nos rapports. La découverte initiale du signal ne nous est pas attribuée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S016 — Freeze master du 3 octobre — historique](../SOURCES.md#s016) — statut de diffusion et empreinte dans le catalogue.

- [S014 — Lag-5 : concentration par identité de rune](../SOURCES.md#s014) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-019"></a>

# AST-019 — Concentration lag-5 par identité

Le seuil fixé n’est pas franchi ; on ne peut pas en conclure que toutes les runes contribuent également.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON SOUTENU AU SEUIL FIXÉ |
| Nature | EXPÉRIENCE |
| Pages / objet |  |
| Date de la source | 2026-09-27 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

104 égalités/2105 opportunités intra-mot ; 4 chaînes× 20000 états ; p groupé 3006/80001≈0,0375745, seuil 0,01 non franchi.

## Ce que cela ne démontre pas

Queue exploratoire faible ; pas de preuve de période 5 ni homogénéité parfaite.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole, exécution ou analyse rapporté dans la pièce citée ; vérifier son statut EXÉCUTÉ/BLOQUÉ et la provenance du code avant d’en revendiquer l’originalité.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S014 — Lag-5 : concentration par identité de rune](../SOURCES.md#s014) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-020"></a>

# AST-020 — RAKE T 1–T 5 bloqué

Ce rapport décrit des calculs qui n’ont pas été faits dans cette exécution.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | NON EXÉCUTÉ |
| Nature | PROTOCOLE |
| Pages / objet |  |
| Date de la source | 2026-09-27 |
| Reproduction historique | Bloqué dans le rapport source |

## Calcul ou observation

FINAL_REPORT_LAG 5_RAKE : aucune statistique, aucune réalisation nulle, aucune p-value ; accès au corpus/parseur insuffisant.

## Ce que cela ne démontre pas

Ne pas fusionner avec les autres rapports lag-5 exécutés.

## Attribution et apport du projet

**Catégorie :** TEST_OU_ANALYSE_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Protocole et constat de blocage de cette exécution. Aucun résultat T1–T5 ne lui est attribué ; les campagnes exécutées sont citées séparément dans la mise à jour lag-5.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S026 — Lag-5 RAKE : exécution bloquée](../SOURCES.md#s026) — statut de diffusion et empreinte dans le catalogue.

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


<a id="ast-021"></a>

# AST-021 — Pourquoi explorer une lecture de données

Les échecs bornés motivent une autre voie sans démontrer l’impossibilité de lire les runes.

> Fiche historique du registre du 20 octobre. Les corrections et la synthèse actuelle priment sur ce statut ancien.

| Champ | Valeur |
|---|---|
| Statut historique | HYPOTHÈSE DE TRAVAIL |
| Nature | CONCLUSION |
| Pages / objet |  |
| Date de la source | 2026-10-20 |
| Reproduction historique | Documenté, non rejoué dans ce registre |

## Calcul ou observation

Comparer texte chiffré, modèle hybride, opérations locales et architecture globale. Aucune famille testée ne couvre toutes les solutions.

## Ce que cela ne démontre pas

Aucune affirmation “LP est indéchiffrable” ou “LP n’a pas de texte”.

## Attribution et apport du projet

**Catégorie :** HYPOTHESE_OU_RACCORD_DANS_LE_PROJET

**Travaux antérieurs :** Anomalies de répétition documentées par les sources communautaires citées. Leur consultation ne démontre pas que chaque code ou protocole du projet provient de ces dépôts.

**Apport du projet :** Assemblage ou interprétation proposé dans les rapports du projet. Hypothèse locale, sans priorité d’invention démontrée.

**Auteur et provenance :** Contribution du projet et de ses agents selon le rapport ; auteur initial de l’idée à compléter si non indiqué.

**Originalité :** NON ÉTABLIE — aucune priorité mondiale revendiquée.

- [ZzNible — Cicada 3301 / Liber Primus — Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md)

- [Dukotah et contributeurs du dépôt — Liber Primus — Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md)

## Sources et dépendances

- [S001 — Cadrage éditorial du dossier](../SOURCES.md#s001) — statut de diffusion et empreinte dans le catalogue.

- [S003 — Contrôle de couverture avant publication](../SOURCES.md#s003) — statut de diffusion et empreinte dans le catalogue.

- [AST-004 — Six familles de lecteurs R4](03-astra-et-cryptanalyse.md#ast-004)

- [AST-011 — CP5 : échappement D 0, D 1](03-astra-et-cryptanalyse.md#ast-011)

- [AST-013 — ÉTAU : 384 machines 32 × 8](03-astra-et-cryptanalyse.md#ast-013)

[Synthèse](../SYNTHESE.md) · [Crédits](../ATTRIBUTION.md)


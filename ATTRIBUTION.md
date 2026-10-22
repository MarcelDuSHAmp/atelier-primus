# Crédits, antériorité et apport de ATELIER PRIMUS

Ce dossier s’appuie sur le travail des créateurs de Liber Primus, des solveurs, des transcripteurs, des archivistes, des auteurs et des développeurs cités dans ses sources. Les réunir dans notre dossier ne transfère ni leur paternité ni leurs droits au projet.

**« Nos travaux » désigne ici les essais, calculs, propositions et documents effectivement produits dans le projet. Cela ne signifie pas que leurs idées de départ, leurs données ou leurs résultats sont mondialement inédits.** Un résultat peut être exact et déjà connu ; une hypothèse peut être nouvelle pour nous et fausse.

## Règles appliquées aux 171 fiches

Chaque fiche possède désormais une rubrique d’attribution : catégorie, antécédents, apport du projet, auteur précis ou attribution à compléter, sources et statut d’originalité. Le [tableau complet CSV](donnees/attributions.csv) et le [registre JSON](donnees/attributions.json) permettent de les contrôler.

| Catégorie | Formulation permise |
|---|---|
| Résultat antérieur | « X a publié / documenté ce résultat », avec la source et sa date si elle est établie. |
| Reproduction | « Nous reproduisons le résultat documenté par X », avec nos entrées, adaptations et limites. |
| Test inspiré ou adapté | « À partir de l’idée / méthode de X, nous testons Y », en précisant ce qui change. |
| Résultat obtenu dans le projet | Décrire l’observation ou le test réellement réalisé ; indiquer que la priorité extérieure reste à établir. |
| Hypothèse ou raccord | Identifier le proposant lorsque la trace le permet ; conserver le statut d’hypothèse. |
| Attribution incomplète | Nommer la source consultée et signaler que le premier auteur ou la chaîne d’inspiration manque. |

Aucune fiche n’est déclarée ici « première découverte mondiale démontrée ». La consultation d’un dépôt ne démontre pas qu’il a inspiré chaque essai ; ce lien n’est écrit que lorsqu’une pièce le documente. Un auteur qui archive un résultat n’en est pas automatiquement le premier découvreur.

## Exemples concrets

| Objet | Crédit antérieur | Apport documenté du projet |
|---|---|---|
| G032 / 15.jpg | Reconstruction déjà documentée par la communauté ; référence CicadaSolvers, auteur initial à préciser. | Rejeu de l’ordre, applications candidates, comparaison dépôt/prélèvement. |
| Lag-5 et répétitions | Publication sous le pseudonyme ZzNible ; travaux statistiques également décrits par Dukotah. | Reproductions et tests de suivi dans les rapports cités, avec leurs protocoles et limites propres. |
| DJU–BEI | Les deux occurrences sont décrites par CicadaSolvers. | Tests de fonctions, adresses et raccords ; le constat de répétition n’est pas notre découverte. |
| Déchiffrements LP1 / G073 | Solveurs historiques, références communautaires et témoignages conservés. | Relecture pédagogique, tests et propositions de transfert à LP2. |
| Transcriptions | Mortlach selon le fichier reçu ; autres attributions parfois incomplètes. | Parseurs, comparaisons et audits des versions ; aucune revendication de création des transcriptions reçues. |
| R4, F0 et SPECIAL | Images, transcriptions, Gematria Primus et recette G032 antérieures. | Assemblages et contrôles des rapports ATELIER PRIMUS ; l’originalité de chaque raccord reste à établir. |
| Campagnes ASTRA / 761 / CP / ÉTAU | Matériel Cicada, méthodes cryptographiques et précédents cités. | Protocoles et exécutions effectivement documentés, avec provenance du code à compléter lorsqu’elle manque. |
| Images, Blake, interprétations graphiques | Créateurs des œuvres et analyses communautaires antérieures. | Mesures et hypothèses additionnelles ; ni les images ni les gestes généraux ne sont revendiqués comme inventions. |

## Bibliographie d’attribution

- **EXT-ZZNIBLE — ZzNible**, [Reproducible Research Findings](https://github.com/ZzNible/cicada3301-liber-primus-findings/blob/main/README.md). README consulté le 22 octobre 2026 ; blob Git `264cddf1f15b02fced5beabeb7b2df49ef93e4a4`. La première date de publication et la priorité absolue du signal ne sont pas établies par cette consultation.
- **EXT-DUKOTAH — Dukotah et contributeurs**, [Findings](https://github.com/Dukotah/cicada3301/blob/master/liber-primus/docs/FINDINGS.md). 75 premières lignes consultées le 22 octobre 2026 ; fichier portant une date de mise à jour au 17 juin 2026 ; blob Git `3d28bd8e72987648aa578c1e4bcdb250533b1a5f`. Ses campagnes restent les siennes ; ses conclusions générales ne sont pas automatiquement adoptées.
- **EXT-CICADASOLVERS — Communauté CicadaSolvers**, [Cryptanalysis Briefing](https://www.cicadasolvers.com/quickstart/), consulté le 22 octobre 2026. Référence collective ; attribution individuelle à compléter pour chaque découverte historique.
- **EXT-G032 — Communauté / CicadaSolvers**, [15.jpg Square](https://www.cicadasolvers.com/wiki/liber-primus/lp2/15-jpg/15-jpg-square/), consulté le 22 octobre 2026. La page renvoie notamment au forum Fibonacci/prime/Zeckendorf et au wiki Uncovering Cicada ; ces renvois ne sont pas présentés ici comme une vérification de tous leurs auteurs et dates.
- **EXT-DJUBEI — Communauté / CicadaSolvers**, [Dis Legomenon](https://www.cicadasolvers.com/wiki/liber-primus/dis-legomenon/), consulté le 22 octobre 2026.
- **ARCH-MORTLACH**, transcription reçue sous le nom `Liber primus in gematria values by mortlach.txt`, SHA-256 `88ce49a218421a1e0481e69afcd7ed05380f2edf979bfdd5f3bcc7b4cc8ff98f`. Attribution issue de l’archive, sans reconstitution de toute sa publication historique.
- **ARCH-RUNES**, `runes-text.txt`, SHA-256 `5e0003aa7f7dde3b238d17c5f964790dbf6bf9db5edacc4a5ec0bad81c6f4bce`. Auteur initial non établi ici ; ne pas le remplacer par le nom du projet.
- **ARCH-HISTO**, [notice S042 des sources historiques](SOURCES.md#s042) et [notice S043 du rapport du 20 octobre](SOURCES.md#s043). Elles créditent notamment Joel Eriksson/ClevCode pour son témoignage, micheloosterhof pour son dépôt, TheChosenHalfBlood pour son analyse d’image, William Blake pour ses œuvres et Eric Hughes pour son manifeste. Une œuvre, un témoignage, une archive et une interprétation constituent des contributions différentes.

Les dates des rapports internes indiquent quand le projet a consigné un travail ; elles ne prouvent pas à elles seules la priorité sur autrui. Une date de téléchargement n’est pas une date de découverte. Les références externes exactes et les niveaux de consultation sont aussi conservés en [JSON](donnees/references-attribution.json).

## Responsabilités dans le projet

**Auteur public : MarcelDuSHAmp (pseudonyme). Collaboration IA : ASTRA GPT-6.** Les analyses, calculs, scripts et textes ont été élaborés avec l’assistance d’outils d’IA. ASTRA est le nom utilisé pour cette collaboration ; les désignations des agents dans les archives ne constituent pas une certification rétroactive du modèle ayant produit chaque ancien rapport. Ces désignations ne sont pas présentées comme des chercheurs humains indépendants. L’origine d’une idée particulière reste attribuée à sa trace lorsqu’elle est connue ; elle n’est pas automatiquement créditée au pilote ou au dernier rédacteur.

## Textes, code, images et réutilisations

Conserver les signatures, commentaires d’auteur, notices et licences des pièces reprises. Pour un code adapté, citer le fichier d’origine, sa version ou empreinte et les modifications. Pour une image dérivée, citer le fichier source et le traitement. Un lien ou une citation ne remplace pas l’autorisation ou la licence de redistribution : les copies intégrales dont les conditions ne sont pas établies restent des pièces de travail privées à sélectionner avant publication.

Les archives historiques sont conservées comme sources et peuvent contenir d’anciennes formulations à la première personne. Elles ne doivent pas être lues comme une revendication actuelle d’originalité du projet. Les attributions manquantes restent visibles ; un doute n’est pas comblé par une revendication.

## Format Tor

Le format d’identifiant Tor v2 et ses règles cryptographiques appartiennent au travail du Tor Project. [Spécification historique](https://torproject.gitlab.io/torspec/rend-spec-v2.html), consultée le 22 octobre 2026. La piste d’export du projet ne revendique ni l’invention de Base32 ni celle de ce protocole.

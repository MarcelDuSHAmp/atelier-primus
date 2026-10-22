# 07 · Contre-épreuves, corrections et prochaines expériences

[Carte d’ensemble](README.md) · [Sources et portée](SOURCES.md)

## Registre des modèles qui ne passent pas

| Énoncé testé | Résultat / statut actuel | Ce qui reste ouvert |
|---|---|---|
| `φ(230)=172` avec le totient usuel | **FALSIFIÉ** :88 ; F0[88]=211 | Une autre opération pourrait exister, mais doit être définie et nommée distinctement |
| D34 intérieur=`158,230,180,36` | **FALSIFIÉ** : l’intérieur vaut172,230,180,36 | Rôle de l’entrée158 et sélection éventuelle230 |
| `F0[87]=15`, puis GP(15)=151 | **FALSIFIÉ** comme lecture directe :65 ; GP29 standard ne fournit pas151 | Un autre pipeline doit expliciter ses conversions ; les autres occurrences151 restent distinctes |
| NEXT uniforme pour105→249→211→6 | Les huit règles simples de A01 échouent | Instructions locales plus riches non exclues |
| Alternance HADDR/HINV/HADDR | **FALSIFIÉE** pour cette cible :105→249→211→233 | Trouver un indice indépendant de mode |
| Adjacent→HADDR, intérieur4→HINV ; cible SPECIAL non vide | **FALSIFIÉ** :0/3 ; cibles207,239,248 ordinaires | Autres contrats, autres marqueurs, autres destinations possibles |
| Même lecteur et même unité G068→R4 | **FALSIFIÉ** : physique272/195/288 contre lexical198/254/154 | Commande éventuelle du changement d’unité |
| Sortie BODY C dépendant des 512 états entrants testés | Sortie154 inchangée dans l’ablation rapportée | Un rôle de l’état sur un autre événement reste possible |
| SPECIAL brut comme secret indépendant de son compact | **FALSIFIÉ** : inverse exacte à ordre fixé | Autre objet indépendant ; cookie dérivable mais usage non établi |
| Taille16 octets ou encodage22 caractères prouve AUTH | Test non discriminant : tous les témoins passent | Conséquence cryptographique sur un descripteur indépendant |
| Parser universel « jusqu’au prochain SPECIAL » | Insuffisant pour séparer BODY36 et élément248 de D30 | Règle de frontière et de footer à trouver |

Les égalités et contre-exemples sur les octets sont rejoués par [rejouer.py](rejouer.py). Les expériences runiques, nuls et ablations plus larges restent attribués à leurs scripts ou rapports. Un modèle falsifié peut inspirer un nouvel essai ; une exception ajoutée après l’échec doit être enregistrée comme nouveau modèle.

## Impasses connexes conservées dans les familles

| Campagne / famille | Ce que les résultats apportent | Lien |
|---|---|---|
| ÉTAU / transducteur32×8 |384 contrats ; aucun4/4 attendu, meilleur2/4 selon le rapport | [AST-013](../recherches/03-astra-et-cryptanalyse.md#ast-013) |
| M6→M7 | Cinq fonctions/source-opcode-destination non identifiées | [M6-008](../recherches/05-m6-liste-et-pre64.md#m6-008) |
| 35 octets→35 mots / APPLY_CONTENT | Clés et transformations essayées sans sortie commune validée | [Contrôle du 21 octobre](../pieces/LP_CHAINE_CONTROLE_FINALE_20261021.md) |
| G035 / rotation ; G026 / format numérique | Transferts uniformes contredits dans les contrats testés | [OUT-013 et014](../recherches/09-seek-shift-et-objets-de-sortie.md#out-013) |
| RESTORE156→cible suivante | Aucun checksum156 parmi29 préfixes2|16 | [OUT-015](../recherches/09-seek-shift-et-objets-de-sortie.md#out-015) |
| Lag-5 | Dépendance étudiée ; ni période de clé ni opcode déduit du seul excès | [Bilan lag-5](../actualites/2026-10-22-lag5.md) |
| ASTRA /761 / codecs | Réduisent des espaces de modèles précis, sans impossibilité générale | [Bilan ASTRA](../actualites/2026-10-22-astra.md) |
| Pixels, couronnes, projections, micro-résidus | Mesures et témoins sur régions définies ; pas de nouveau texte validé | [Fiches visuelles](../recherches/04-images-dessins-et-marqueurs.md) |
| Collisions GP | Une somme ne choisit pas un mot : SHIFT/HERE, WEB/ROUTE… | [Corrections](../recherches/10-contre-epreuves-et-corrections.md) |

## Ce que les nombres de tests ne disent pas

Des variantes corrélées, fenêtres qui se recouvrent ou cibles choisies après découverte ne sont pas des expériences indépendantes. Le 0/9999 d’un nul local n’est ni une probabilité nulle ni la probabilité que la VM soit vraie. Aucune exclusion générale à99% de puissance n’est revendiquée par cette carte.

## Deux expériences proposées

| Question | Exploration libre | Validation distincte |
|---|---|---|
| Qui commande le type et le sens ? | Chercher notations, rotations, motifs et dispositions pouvant indiquer X8 ou Y8 | Fixer la règle et ses paramètres, annoncer une conséquence sur un autre locus avant révélation, conserver succès et échecs |
| L’état change-t-il vraiment le comportement ? | Construire des scénarios autour d’un objet consommant80 ou132, avec deux suites possibles | Comparer modèle à état et modèle sans état de complexité voisine sur un événement où ils divergent ; ne pas choisir le consumer après lecture |

Les données déjà exposées restent utiles pour explorer, calculer et réfuter. Les rebaptiser « aveugles » ne crée pas une validation nouvelle.

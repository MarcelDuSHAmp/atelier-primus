# 01 · Sources et grammaire matérielle

[Carte d’ensemble](README.md) · [Sources et crédits](SOURCES.md)

## Source, transcription, reconstruction

| Niveau | Contenu | Usage et limite |
|---|---|---|
| Source | [75 JPEG G000–G074](../ATLAS.md), couleurs, positions, frontières, octets | Autorité visuelle et binaire ; une image ne fournit pas automatiquement son mode d’emploi. |
| Transcription | Runes, nombres, lignes, groupes physiques, mots raccordés | Lecture humaine ou outillée. Un changement de segmentation peut changer la sortie. |
| Reconstruction | F0, tableaux, frames, unités M6, corps R4 | Objets calculables sous des conventions explicites. Ne pas les présenter comme des fichiers binaires directement distribués par Cicada. |
| Interprétation | ROM, opcode, état, CALL, checkpoint, AUTH | Fonction à établir ; même si l’objet sous-jacent est exact. |

Numérotation globale : LP1 = G000–G016 ; LP2 = G017–G074. Une page locale LP2 `pNN` correspond à `G(NN+17)`. Ainsi **p15 LP2 = G032**, tandis que **G015 appartient à LP1**. Les anciens rapports emploient parfois p05/p15 sans nommer l’ensemble : conserver ce contexte avant toute équivalence.

## Les leçons et leurs transferts possibles

| Source / précédent | Geste ou objet | Ce qui reste à établir dans l’architecture |
|---|---|---|
| G001, textes résolus | Lecture inversée dans le cadre du déchiffrement connu | Quand cette opération est-elle demandée ailleurs ? |
| G003–G004, DIVINITY | Clé et gestion locale de HOLD/CONSUME | Le choix des exceptions n’est pas une règle universelle établie. |
| G005 | Normalisation du carré mixte, demi-tour, nombres premiers, totient ; structure JPEG/centre/JPEG inversé | Choix du rôle d’un nombre : valeur, index, portée ou vérification. |
| G010 | Fichiers G011–G013 effectivement annexés | Le support numérique peut contenir un objet supplémentaire ; cela ne promet pas une charge cachée dans chaque page. |
| G014–G015 | Clé locale et continuité de phase | Transfert vers R4 non automatique. |
| G016 | Carré 5×5 et constante 3301 | Transformations vers F0 proposées dans les raccords, sans commande universelle. |
| G032, dans LP2 | Recette communautaire Fibonacci/premiers ; ordre de 16 cases | Objet à parcourir, prélèvement/dépôt et extrémité restent des choix à relier au contexte. |
| G073, solution communautaire | Recherche d’une page externe correspondant à une empreinte | Ne nomme pas explicitement Tor ; ne donne pas directement nos candidats A/B. |

Les techniques cryptographiques, les solutions communautaires et les matériaux Cicada précèdent notre dossier. Les connexions entre ces leçons et les modules candidats sont des propositions/reproductions du projet, sans priorité mondiale établie. [Fiches des précédents](../recherches/02-apprentissage-et-precedents.md).

## Dessins, frontières et représentation

| Famille | Objet observable ou rapporté | Rôle proposé, non traduit comme une instruction |
|---|---|---|
| R10/R11/R13/R23 | Carrés rouges et séparations documentés | Délimitation, changement de représentation, portée. Le nombre de carrés n’est pas un opcode décodé. |
| G024/G040/G073 | Motifs à cinq points et relations de réflexion | Orientation, rappel, chemin ou sortie ; direction obligatoire non établie. |
| G041–G043 | Ornements répétés, étoiles et translation étudiée | Séparer deux voies, rappel vers D34 ; lien opératoire encore candidat. |
| G049/G072 | Arbres et décor pâle étudiés | Rappel ou transformation ; identité raster exacte non démontrée. |
| G044/G072 | Séquence DJU–BEI répétée | Rappel/retour possible ; portée, direction et opération non résolues. |
| G017–G019 et G039 | Points clairs, croix, couronnes et micro-résidus | Mesures et lectures ciblées conservées ; aucun flux d’instructions reconnu. |

[Toutes les analyses visuelles](../recherches/04-images-dessins-et-marqueurs.md). Le constat d’un dessin réel est séparé de son interprétation ; une contre-épreuve sur un crop ne clôt pas l’examen des 75 pages.

## M6, PRE64 et M7

M6 désigne le groupe G050–G056. La liste U1…U5, dans G053–G055, comporte respectivement **139, 91, 98, 96 et 129 runes** selon le dossier. U4 traverse G054→G055. Le PRE64, de G052 à G053 avant la liste, compte 64 mots et 292 runes dans la segmentation héritée. Son arrangement 8×8 et sa première colonne de huit mots de trois runes ont été étudiés.

La liste est un objet matériel. La lire comme cinq états, comportements ou instructions reste une hypothèse. L’ancien modèle de cinq triplets source/opcode/destination n’est pas rétabli. Le rapprochement U3 terminal / fin de G068 concerne 30 runes et des décomptes de mots/groupes ; une égalité de taille ne crée pas une flèche de programme.

M7 désigne le groupe G057–G072 ; **F0 provient des inscriptions numériques G066–G068**, pas de toutes les runes de M7. Le scénario M6=configurateur et M7=machine reste ouvert. [Famille M6](../recherches/05-m6-liste-et-pre64.md).

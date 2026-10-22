# 04 · Modules et chemins candidats

[Carte d’ensemble](README.md) · [Sources A01/A02 et P01/P02](SOURCES.md)

Ce dossier rassemble les compositions explorées. Il sépare les calculs locaux, l’interprétation fonctionnelle et le choix de la prochaine étape. « CALL », « BODY », « TRAILER » et « CHECKPOINT » sont des étiquettes de recherche, sauf précision contraire.

## Vue des modules

| Module | Entrées / sortie | Ce que la composition montre | Ce qu’elle ne commande pas |
|---|---|---|---|
| G068 / lecteur | 16 groupes physiques → A,N,D,ING ; GP294→38 ; rangs1→81 | Lecture rétrospective reproduite dans A01 | Lire ANDING comme opcode AND ; sélectionner le prochain objet |
| D32 / D34 | `63→HADDR→249` ; `158→HINV→211` ; `230→φ→88→F0→211` | Raccords numériques exacts | Choix du sens, cast d’adresse et retour |
| D33 | `[183,92,249,156]` → AND16 ; G→`[192,73,21,144]` | Transformation et masque calculables | Une entrée168 consommée par une fonction qui rendrait174 :168/174 sont des sommes de payloads |
| D30 / BODY36 | 36 octets → G élémentaire →35 ordinaires puis 126 | Fermeture locale exacte | HALT, RETURN ou émission déclenchée par 126 |
| READ G071 | 35 sorties + masque16 + BODY35 →16 mots →61 runes →132 | Composition reproduite par A01, cible et bornes déjà connues | Choisir BODY35, le masque et NEXT sans intervention du solveur |
| BLOCK64 G071–G072 | 64 mots de corps →16 cases de 4 mots →G032→230→G→80 | Recette précise rétablie dans A01 | Consommateur de 80 et rôle de BOOT |
| R4 lexical | 3 BODY16 →198,254,154 ; high3→6,7,4 | Réducteur spatial et fermeture F0 | Changement d’unité depuis G068, état persistant, déchiffrement |
| SEEK/SHIFT et rappels | Préfixes, sommes, rotations, STANDING, motifs | Raccords consignés et contre-épreuves | Programme de navigation global imposé |

## La branche R4

R4 correspond à **G069 rune2 → G070 rune128**, soit390 runes/86 mots dans les transcriptions employées. La partition candidate est trois blocs de 24 mots `CALL + BODY16 + TRAILER7`, suivis d’un TAIL14. Les trois CALL occupent les rangs1,25,49 ; il ne s’agit pas de trois instructions déchiffrées.

Sur les BODY lexicaux, G032 RIGHT/RIGHT donne `[198,254,154]`. Les nombres complets imposent les calculs suivants une fois la convention HADDR adoptée :

- `HADDR(154)=212` et `HADDR(254)=247` : fenêtre de 36 cellules.
- `F0[246]=198` : sentinelle candidate avant la fin.
- `F0[247]=192` puis `G(192)=126` : dernière sortie SPECIAL après35 ordinaires.

Le [rejeu R4](../calculs/r4/rejouer.py) et les [corrections de segmentation](../actualites/2026-10-21-segmentation.md) conservent la fermeture et les contrôles locaux. Si on transfère à R4 l’unité **physique** de G068 sans la remplacer par le mot lexical, les sorties sont **272/195/288**. La version « même lecteur et même unité partout » est donc contredite.

Le passage proposé `[3,6,7]→[6,7,4]` peut se dessiner comme un registre glissant. Mais la sortie154 du BODY C reste inchangée dans l’ablation des 512 états entrants rapportée : cette lecture ne prouve pas qu’un état antérieur agit sur le résultat.

## READ / SELECT / REDUCE dans G071

Le BODY35 est délimité dans les rapports par deux mots de somme GP199. Les 35 premières sorties de G sur BODY36 donnent, avec `&16`, les rangs :

```text
2,3,5,6,8,10,14,16,19,20,25,27,28,31,34,35
```

Ces16 mots contiennent61 runes selon A01/P02. G032 RIGHT/RIGHT sélectionne les quatre finales de valeurs37+37+17+41=**132**. Le checkpoint P02 prolonge ce résultat vers le mot GP132 de R4, puis NEXT150, G150=144 et la coda rouge. Ce raccord est conservé comme composition candidate : l’égalité des sommes ne suffit pas à enseigner un adressage par mot.

La vérification ajoutée à cette carte recalcule le masque et les rangs dans les **deux binaires distribués**. Elle ne retranscrit pas indépendamment les mots ni le readout132. Les 60/61/68 runes des autres masques et les 70 alignements sont des résultats attribués au checkpoint, pas une nouvelle campagne ici.

## BLOCK64 et les autres chemins vers 80

Dans A01, les deux mots de titre rouge sont exclus ; les 64 mots de corps G071–G072 sont répartis par quatre dans16 cases. Le lecteur retient les mots40,8,48,52, dont les finales valent43+7+79+101=230. Puis `G(230)=F0[55]=80`.

Les autres routes répertoriées vers 80 comprennent le centre de G005 (`91→φ72→F0[72]=164→G164=80`), les 16 portions G020–G024 et des continuations locales. Ce sont plusieurs recettes documentées ; leur convergence ne signifie pas qu’un ordre d’exécution unique a été établi.

| Branche de navigation | Dépendance et statut actuel | Détail |
|---|---|---|
| G016→245, croix D36/D37 | Transformations numériques proposées ; choix du rôle non commandé | [LNK-002](../recherches/08-raccords-multi-supports.md#lnk-002) |
| G023 / G068 / G059 / G040 | Préfixes et checksums sélectionnent certains objets sous les règles essayées | [LNK-003 à006](../recherches/08-raccords-multi-supports.md#lnk-003) |
| ST + ANDING→STANDING | Assemblage interprétatif ; COUNT/END non universel | [LNK-013](../recherches/08-raccords-multi-supports.md#lnk-013) |
| G024→G073 par réflexion | Relation de motifs et hypothèse d’orientation ; sélection de l’axe non imposée | [LNK-014](../recherches/08-raccords-multi-supports.md#lnk-014) |
| G054→X16→export | Préfixe16/22, CAST8, G032, ROR6 ; choix conditionnels conservés | [OUT-002 à008](../recherches/09-seek-shift-et-objets-de-sortie.md#out-002) |
| DJU–BEI, arbre, insecte, cadre de G072 | Rappels possibles vers d’autres pages ; ACTION/SCOPE inconnus | [Famille visuelle](../recherches/04-images-dessins-et-marqueurs.md) |

## Le cycle de contrôle proposé le 21 octobre

P01 proposait G068→G072→G071→G070→G069→G068, avec checkpoint, dispatch, buffer, clôture et retour151, puis continuation G073. Le dossier garde ce scénario et ses calculs pour qu’ils restent examinables. L’audit A01 du 22 octobre ne reconstruit ni décodeur stable, ni PC du livre, ni retour sauvegardé : **le scénario global reste une hypothèse architecturale**. Les formulations fortes de P01 ne remplacent pas les corrections de version, de typage et de segmentation.

[Rapport de contrôle P01](../pieces/LP_CHAINE_CONTROLE_FINALE_20261021.md) · [Checkpoint READ P02](../pieces/LP_READ_CHECKPOINT_20261021.md) · [Raccords détaillés](../recherches/08-raccords-multi-supports.md)

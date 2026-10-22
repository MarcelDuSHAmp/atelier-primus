# 02 · Mémoire F0 et objets D

[Carte d’ensemble](README.md) · [Résultats calculés](resultats.json) · [Audit VM A01](SOURCES.md)

## La table de 256 octets

F0 reconstruit 256 tokens de G066–G068 en octets, disposés en **32 lignes × 8 colonnes**. Le découpage `high3=b>>5`, `low5=b&31` est exact. SPECIAL signifie `low5 ≥ 29` : 16 occurrences, réparties en 5 de classe29, 6 de classe30 et 5 de classe31. Les 240 autres sont dits ordinaires. Ces noms décrivent le modèle ; les tokens SPECIAL ne sont pas colorés spécialement sur les images.

La table est utilisable comme une ROM dans nos scripts. Aucune règle d’écriture ne démontre qu’elle serait une mémoire modifiable du livre. Elle n’est pas une permutation des 256 valeurs.

| Version distribuée | SHA-256 | Convention de cette carte |
|---|---|---|
| [F0-3b9b07d9.bin](../calculs/r4/F0-3b9b07d9.bin) | `3b9b07d9a26e6d55c432d94d2661fdff3c2b348daed06821f2bdb23184a4b290` | Autorité de l’audit VM du 22 octobre |
| [F0-0201348c.bin](../calculs/r4/F0-0201348c.bin) | `0201348c02d11222097b68be9ad0179a44020b46fe64a9e8e8198447c7b922e9` | Version conservée pour comparaison, appelée « corrigée » dans certains rapports antérieurs |

Six indices diffèrent : **2, 45, 131, 182, 192, 199**. Les 16 SPECIAL et leurs positions sont identiques. Il faut conserver l’empreinte avec chaque résultat, sans résoudre une divergence par le seul mot « canonique » ou « corrigé ».

## Les familles D ne sont pas des numéros d’opcode

La convention de nommage emploie `D(high3+low5)`. Elle n’est pas injective : `222=6|30` et `253=7|29` sont tous deux nommés D36. Un octet peut aussi apparaître plusieurs fois. **Toujours préciser valeur et index.** Le [journal](resultats.json) inventorie les 16 occurrences et leurs labels.

| Objet local | Positions, base 0 | Octets / frontière | Rôle candidat |
|---|---|---|---|
| D32 à105 | Entrée `F0[105]=63`, puis SPECIAL à106 | Aucun intérieur entre les deux | Adresse/appel via HADDR ; pile non établie |
| D33 à6 | Entrée126 ; intérieur7..10 ; prochaine borne11 | `[183,92,249,156]` | Masque/transformation ; ne pas le confondre avec une instruction HALT |
| D34 à249 | Entrée158 ; intérieur250..253 ; prochaine borne254 | **`[172,230,180,36]`** | Cadre, sélection ou transformation |
| D30 à211 | Entrée61 ; BODY212..247 ; élément248=113 ; prochaine borne249 | 36 octets BODY, mais 37 ordinaires entre les SPECIAL211 et249 | Frame/data ; le rôle de footer de 113 est une interprétation explicite |
| D36 à11 | Bornes11 et48 ; intérieur12..47 | 36 octets internes, 38 positions bornes comprises | Portée ; ne pas confondre avec BODY212..247 |
| D37 | Occurrences254 aux indices56 et170 | Intervalles locaux recensables | Fonction et portée opératoire non résolues |

L’ancienne liste D34 `[158,230,180,36]` mélangeait l’entrée et l’intérieur : elle n’est pas le payload de quatre octets. Le parseur « prendre jusqu’au prochain SPECIAL » ne distingue pas automatiquement BODY et footer de D30.

## Trois calculs locaux qui se composent

- `AND(F0[7:11]) = 16` pour D33.
- `AND(F0[250:254]) = 36` pour l’intérieur D34.
- Pour chaque octet du BODY212..247, `G(b)=F0[HADDR(b)]` produit **35 ordinaires puis 126**.

Ces sorties sont rejouées sur les deux versions. Les suites de 36 sorties diffèrent toutefois à leur rang32 : **167 dans3b9b07d9 ; 138 dans0201348c**. Leur somme modulo256 vaut donc **33 contre 4**. Le masque `&16` sélectionne, lui, les mêmes 16 rangs parmi les 35 premières valeurs dans ces deux binaires précis.

Cette comparaison évite deux raccourcis : une même fermeture ne rend pas tout le vecteur identique ; une divergence d’octet ne change pas nécessairement le résultat du masque. L’ancienne assertion «17 mots contre 16» concerne une autre reconstruction historique citée par le checkpoint ; elle ne décrit pas cette paire de fichiers.

## Intervalles et tailles

Les 15 intérieurs entre SPECIAL ont pour tailles `4,36,7,8,30,8,0,37,6,18,23,11,4,37,4`. Aucun ne mesure16 octets, même en ajoutant les deux bornes. Ce constat borne cette famille de découpages ; il ne prouve pas l’absence de tout objet128 ailleurs.

[Fiches F0 et D](../recherches/06-f0-familles-d-et-routage.md) · [Correction des versions](../actualites/2026-10-22-f0.md)

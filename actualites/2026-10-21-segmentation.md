# R4 : fermeture exacte, transfert d’unité manquant

**Deux résultats doivent rester séparés :** la fermeture R4 lexicale est reproduite ; son apprentissage par un lecteur invariant depuis G068 est falsifié dans le contrat testé.

| Support et unité | Nombre d’unités | Prélèvement / sommes |
|---|---:|---|
| G068, groupes physiques | 23 | A · N · D · ING, quatre runes aux positions 10, 2, 12, 13 |
| G068, mots lexicaux | 20 | Autre prélèvement ; somme 272 |
| R4, mots lexicaux | 86 | 198 / 254 / 154 |
| R4, groupes physiques | 101 | 272 / 195 / 288 |

Les BODY16 sont pris après les appels 1, 25, 49 selon le modèle historique. La segmentation et ces appels sont des entrées du modèle, pas des instructions nouvellement déchiffrées.

## Fermeture lexicale

`HADDR(x) = 8 × (x & 31) + (x >> 5)`.

`HADDR(154)=212`, `HADDR(254)=247` : fenêtre inclusive de 36 cellules. `F0[246]=198`. Pour chaque cellule i de cette fenêtre, la consommation `F0[HADDR(F0[i])]` produit 35 valeurs ordinaires puis `126`, nommé D33 dans la convention du projet. La fermeture est identique sous les deux F0 joints.

| Modèle nul local | Fermetures / états | Fréquence |
|---|---:|---:|
| N0 : permutation des 16 mots de chaque corps, ramenée aux sous-ensembles sélectionnés | 3 146 / 6 028 568 000 | 5,21849 × 10⁻⁷ |
| N1 : permutations entre mots de même longueur | 2 / 6 480 | 0,000308642 |
| N2 : rotations cycliques des trois corps | 1 / 4 096 | 0,000244141 |
| N3 : permutation des runes dans chaque mot | 117 / 37 044 000 | 0,00000315841 ; rapport seulement |

N0–N2 ont été rejoués ici et leurs résultats complets concordent avec le JSON historique, à l’exception attendue du nom local du fichier d’entrée. N3 et les balayages des 23 phases lexicales / 38 physiques sont attribués au rapport ; ils n’ont pas été relancés.

Ces fréquences sont **conditionnelles** au choix lexical, aux corps et au lecteur. Elles ne corrigent pas l’ensemble des choix explorés pendant la recherche et ne sont pas la probabilité que l’auteur ait voulu ce mécanisme. Les nuls ne sont pas des confirmations indépendantes à multiplier.

## Conséquence

Conserver le candidat lexical et rechercher le commutateur de segmentation. Ne pas qualifier la chaîne globale de lecture acquise. Un SPECIAL terminal ne donne pas à lui seul la sémantique STOP, RETURN ou HALT.

[Rapport intégral](../pieces/LP_NULL_CLOSURE_REPORT_20261021.md) · [Script portable](../calculs/r4/rejouer.py) · [Sorties rejouées](../calculs/r4/resultats-rejoues.json) · [Adaptations](../calculs/r4/ADAPTATION.md)

## Attribution

Ce contrôle appartient aux rapports du projet et utilise des transcriptions reçues ainsi que la recette G032 antérieure. Le résultat de segmentation est attribué à ce contrôle ; aucune priorité mondiale n’est affirmée. [Crédits, sources et limites](../ATTRIBUTION.md).

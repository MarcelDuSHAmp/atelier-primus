# 03 · Opérations, représentations et types

[Carte d’ensemble](README.md) · [Rejeu](rejouer.py) · [Audits A01/A02](SOURCES.md)

## La bibliothèque minimale

| Opération | Entrée → sortie | Définition / rôle exact |
|---|---|---|
| high3 / low5 | BYTE8 → deux champs | `b>>5` et `b&31` |
| HADDR | Code à champs → INDEX8 | `8*(b&31)+(b>>5)` |
| HINV | INDEX8 → code à champs | `((i&7)<<5)\|(i>>3)` ; inverse de HADDR |
| F0 | INDEX8 → BYTE8 | Lecture du contenu, pas de l’adresse |
| G | BYTE8 → BYTE8 | `F0[HADDR(b)]` |
| AND | Suite d’octets → octet | ET bit à bit ; masque candidat selon contexte |
| Totient φ | Entier positif → entier | Nombre d’entiers premiers avec n ; **φ(230)=88** |
| GP_SUM | Suite de runes → entier | Somme des valeurs Gematria Primus ; un modulo256 éventuel doit être déclaré |
| RANK_SUM1 | Suite de runes → entier | Somme des rangs à partir de 1 ; distincte de GP_SUM |
| G032 / READ | 16 objets paramétrés → quatre extrémités puis somme | Ordre, unité, bord et extrémité sont des paramètres du lecteur |
| Compact SPECIAL | 16 SPECIAL →80 bits | `hhh111cc → hhhcc`, réversible dans cette classe |

HADDR/HINV sont inverses sur les 256 valeurs :512 égalités sont vérifiées par le script. Cette propriété algébrique n’identifie pas une instruction du livre. Les noms BYTE8 et INDEX8 précisent un usage ; une valeur comprise entre0 et255 ne décide pas elle-même de son usage.

## Le verrou de conversion, sur un exemple

`F0[105]=63` ; interprété comme champs `1|31`,63 donne `HADDR(63)=249`. Le contenu à249 est158. Sur ce158, deux lectures sont possibles :

| Lecture du même nombre158 | Coordonnées | Résultat |
|---|---|---|
| Code à champs : high3/low5 | colonne4, ligne30 | `HADDR(158)=244` |
| Index linéaire d’une grille32×8 | ligne19, colonne6 | `HINV(158)=211` |

HINV produit naturellement un **code à champs**, ici211=`6|19`. Le relire comme **index211** pour atteindre le 61 de F0 demande une conversion supplémentaire non commandée. Le second raccord `F0[φ(230)]=F0[88]=211` produit aussi un octet ; cette égalité ne transforme pas cet octet en adresse.

Le choix HADDR/HINV, puis le changement de rôle de la sortie, doivent être indiqués dans une trace. Les masquer derrière une flèche `D34→D30` ferait disparaître précisément la question étudiée.

## G032 : ordre, disposition et lecture

Le parcours en indices1..16 est :

```text
6, 7, 11, 10, 9, 5, 1, 2, 3, 4, 8, 12, 16, 15, 14, 13
```

La reconstruction de l’ordre utilise une recette communautaire de nombres premiers/Fibonacci et distance à3301. Son transfert vers un objet de 16 éléments reste à justifier objet par objet.

| Geste | Formule, indices du tableau à partir de 0 | Conséquence |
|---|---|---|
| Prélèvement | `out[k]=source[P[k]-1]` | Lire les cases dans l’ordre du parcours |
| Dépôt | `grid[P[k]-1]=source[k]` | Poser les éléments sur le parcours, puis lire la grille |
| RIGHT/RIGHT après prélèvement | Positions4,8,12,16 du tableau obtenu ; dernière rune de chaque objet | Objets source10,2,12,13 ; somme GP des extrémités |

Une somme est commutative : deux sens sélectionnant le même ensemble peuvent produire le même nombre. Le contrat du BLOCK64 retient les mots40,8,48,52 ; une ablation qui conserve ce même ensemble en ordre inverse ne prouve pas son sens.

## Deux notions de groupe

Un **groupe physique** est séparé sur la page ; un **mot lexical** peut réunir deux morceaux coupés par une ligne. Le lecteur historique de G068 emploie des groupes physiques, tandis que le R4 donnant198/254/154 emploie des mots lexicaux. Le passage de l’un à l’autre est un paramètre de l’hypothèse, pas une normalisation innocente.

La carte conserve tous les gestes calculables, même exploratoires. Pour les promouvoir en instructions, il manque un signal indépendant précisant **objet + type + opération + portée + suite**.

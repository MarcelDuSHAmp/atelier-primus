# Liber Primus — test nul de fermeture locale

Date : 2026-10-21

## Question gelée

Tester la chaîne locale suivante sans ajouter de paramètres :

`G032 ordering → RIGHT edge → RIGHT endpoint → somme GP → sorties R4 → HADDR/F0 → fenêtre 36 → sentinel → terminal D33`

Le test ne cherche pas du plaintext et ne modifie pas le lecteur pour sauver un résultat.

## Correction préalable décisive

L'audit de segmentation archivé montre que le lecteur `ANDING` de G068 travaille sur **23 groupes physiques**. Avec cette unité, il sélectionne les groupes 10, 2, 12, 13 et donne `A · N · D · ING`.

En revanche, les sorties R4 historiques `198 / 254 / 154` ont été calculées sur **86 mots lexicaux**. Lorsque le même lecteur est réellement transféré aux **101 groupes physiques** de R4, les sorties deviennent :

`272 / 195 / 288`

Donc le transfert « même lecteur + même type d'objet G068 → R4 » est **FALSIFIÉ**. La fermeture ci-dessous teste uniquement le candidat local **R4 lexical**. Un pont indépendant autorisant le changement `groupe physique → mot lexical` manque encore.

## Données observées du candidat R4 lexical

Ordre G032, positions 1-based :

`[6,7,11,10,9,5,1,2,3,4,8,12,16,15,14,13]`

Le bord droit du 4×4 réordonné correspond aux positions originales :

`[10,2,12,13]`

Sur les trois BODY16 lexicaux après les appels 1, 25, 49 :

`A = 198 = 6|6`

`B = 254 = 7|30`

`C = 154 = 4|26`

Avec `HADDR(x)=8*(x&31)+(x>>5)` :

`HADDR(C)=212`

`HADDR(B)=247`

soit la fenêtre `212..247`, longueur 36. De plus :

- `F0[246] = 198 = A` ;
- le consommateur cellule par cellule `G(x)=F0[HADDR(x)]` donne 35 sorties ordinaires ;
- la 36e donne `126 = 3|30 = D33`.

Cette fermeture est identique sur les deux versions F0 testées pour les indices concernés : SHA-256 commençant par `0201348c...` et `3b9b07d9...`.

## Modèles nuls exacts

Tous les modèles conservent les trois appels, les frontières BODY16/TRAILER et le contenu global des corps. Ils cassent uniquement une relation locale.

### N0 — permutation libre des 16 mots de chaque BODY

Chaque mot reste intact ; seules ses positions dans son BODY16 sont permutées.

Univers exact : `C(16,4)^3 = 6 028 568 000` triplets de readouts possibles.

- `high3 = [6,7,4]` : 32 358 084 / 6 028 568 000 = **0,536746 %** (~1/186)
- fenêtre HADDR forward de longueur 36 : **0,242513 %**
- longueur 36 + sentinel `F0[end-1]=A` : **0,000477908 %** (~1/209 245)
- fermeture complète jusqu'à D33, 35 ordinary + terminal D33 : 3 146 / 6 028 568 000 = **5,21849e-7** = **0,0000521849 %** (~1/1 916 264)

### N1 — permutation seulement entre mots de même longueur

Chaque position conserve donc également sa longueur de mot exacte.

Univers exact : `6 480` états.

- `high3 = [6,7,4]` : **0,987654 %**
- fermeture complète : 2 / 6 480 = **0,0308642 %** (~1/3 240)

### N2 — rotation cyclique de chaque BODY16

L'ordre cyclique et toutes les adjacences sont conservés ; seule la phase change.

Univers exact : `16^3 = 4 096` états.

- `high3 = [6,7,4]` : 24 / 4 096 = **0,585938 %**
- fermeture complète : 1 / 4 096 = **0,0244141 %**

La fermeture complète est unique : rotation `(0,0,0)`, c'est-à-dire l'alignement observé.

### N3 — permutation des runes à l'intérieur de chaque mot sélectionnable

Tous les mots restent dans leur emplacement ; leurs longueurs et multisets de runes sont conservés. Seule la rune située à l'extrémité droite peut changer.

Univers exact : `37 044 000` états.

- `high3 = [6,7,4]` : **0,256965 %**
- fermeture complète : 117 / 37 044 000 = **3,15841e-6** = **0,000315841 %** (~1/316 615)

## Contrôle « look-elsewhere » sur la phase réelle

Avec les mots lexicaux R4, le même lecteur a été glissé sur les trois fenêtres séparées de 24 mots, pour tous les décalages communs possibles : **23 phases**.

Une seule phase donne à la fois `[6,7,4]` et la fermeture complète :

`phase 1 → [198,254,154]`

Avec les groupes physiques R4, **38 phases** sont possibles : aucune ne donne `[6,7,4]`, aucune ne ferme la chaîne. La phase historique physique produit `[272,195,288]`.

## Interprétation

### SUPPORTÉ / EXACT

- `G068 groupes physiques → A·N·D·ING` sous la recette documentée : exact, mais découvert rétrospectivement.
- `R4 mots lexicaux → 198/254/154` : exact.
- `198/254/154 → 212..247 → sentinel198 → 35 ordinary → D33` : exact sous le F0 testé.
- Conditionnellement au choix **lexical** de R4, cette fermeture est rare sous quatre nuls locaux conservateurs.

### FALSIFIÉ

- `le même lecteur, sur le même type d'unité, se transfère de G068 à R4 et produit 198/254/154`.

Le transfert physique produit `272/195/288`, pas `198/254/154`.

### INCONCLUSIF / MANQUANT

- Une instruction indépendante qui autorise précisément le changement d'unité `groupes physiques en G068 → mots lexicaux en R4`.
- Un modèle nul global incluant dessins, couleurs et géométrie des 75 pages. Le présent test est volontairement local, parce que c'est la seule chaîne actuellement formalisée assez précisément pour être rejouée sans degrés de liberté cachés.

## Conclusion

Le test nul ne détruit pas la fermeture R4 lexicale : **elle reste anormalement contrainte dans tous les nuls locaux testés**.

Mais il détruit une affirmation plus forte et importante : **nous n'avons pas aujourd'hui un lecteur invariant transmis de G068 à R4**. La théorie globale doit donc être rétrogradée tant qu'un commutateur de segmentation indépendant n'est pas trouvé.

Le meilleur objet de recherche n'est plus un nouveau cipher. C'est maintenant :

> Quel indice du livre impose le passage de « groupe physique » à « mot lexical » précisément entre l'exercice G068 et R4 ?

Si aucun indice indépendant ne l'impose, la fermeture `198/254/154` doit rester un candidat local post-hoc malgré sa rareté sous les nuls.

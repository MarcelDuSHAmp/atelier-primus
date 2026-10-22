# Attaque cryptographique de `761.mp3` canonique — LP2

**Date : 22 septembre 2026**

## 1. Authentification du fichier

Le fichier `761.MP3` fourni séparément a été comparé au fichier `AUDIO/761.MP3`
extrait directement de l'image `3301.iso`.

### ISO
- taille : `136 398 848` octets
- SHA-256 : `784643558799dd8bb3e172f31df6d6ca2f397fd61cb8fc371bf930f1e5ae6b7f`

### `761.mp3`
- taille : `4 010 732` octets
- SHA-256 : `83008217439110c3b824898af73b99cb2cf0657dda88cb363c3aa34a4ec0a460`
- copie séparée et copie extraite de l'ISO : **identiques octet par octet**

L'ancien problème de copie tronquée est donc résolu.

## 2. Correction méthodologique avant la passe finale

Dans la transcription LP2, `/` est un saut de ligne et **pas nécessairement une
frontière de mot**. Par exemple p.57 contient `T/UNNELING` et `C/IRCUMFERENCES`.

Le scoreur a donc été corrigé pour :
- préserver les vraies frontières de mots ;
- ignorer les simples retours de ligne ;
- conserver les positions runiques imprimées.

Les scans principaux ont été relancés après cette correction.

Contrôle : la p.57 directement lisible obtient un score trigramme runique
d'environ `-2.026`, très loin du bruit.

## 3. Passe dense littérale sur le MP3 complet

Cible : les 120 premières runes de LP2 p.0.

### Réductions byte -> Z29
- `byte mod 29`
- `floor(byte * 29 / 256)`
- avant / arrière
- `C-K` / `C+K`
- clé normale / complément `28-k`

Deux régimes :
- sans traitement spécial de F ;
- F littéral : un `F` ciphertext reste `F` et ne consomme pas la clé.

Nombre total de fenêtres/configurations :
- sans F-skip : `64 169 808`
- avec F-skip : `64 169 920`

### Meilleur sans F-skip
- réduction : `scale29`
- lecture : arrière
- opération : `C-K`
- offset original : `1 913 301`
- score : `-5.411636`

Sortie :
`TABOEROEOB OEEUREO SMOG EOIEA THED WSUMHIPPRINGU ...`

Aucun mot complet reconnu dans les 120 runes. Ce n'est pas un clair.

### Meilleur avec F-skip
- réduction : `mod29`
- lecture : arrière
- opération : `C+K`
- complément de clé : oui
- offset original : `2 905 238`
- score : `-5.334576`

Sortie :
`OINGPBUOLF PYRYD EAUPH FSEO MEOP EODYICABDLEAM ...`

Là encore : **0 mot complet reconnu** dans les 120 runes. La valeur de score est
un faux positif d'extrême-value après des dizaines de millions d'essais, pas un
plaintext crédible.

## 4. Réductions uniformes plus naturelles

### Rejet par octet
Règle : garder seulement les octets `<232`, puis `byte mod29`.

- évaluations : `29 329 832`
- meilleur score : `-5.744561`
- aucun clair.

### Flux de groupes 5 bits
Pour chacune des cinq phases binaires possibles :
- grouper le fichier en valeurs 0..31 ;
- rejeter 29,30,31 ;
- utiliser les valeurs restantes comme Z29 ;
- F-skip ;
- avant/arrière, ±, complément.

- évaluations : `234 939 808`
- meilleur score : `-5.577318`
- aucun clair.

Cette famille couvre également, par changement de phase, le flux MPEG débarrassé
de l'ID3.

## 5. Test historiquement motivé : XOR 5 bits

Puisque `761.mp3` a historiquement servi dans des opérations XOR, un test séparé
a utilisé les runes comme codes 5 bits.

Familles :
- groupes 5 bits du bitstream, cinq phases ;
- `byte & 31` ;
- `byte >> 3` ;
- XOR direct ;
- résultat obligatoire dans `0..28` ;
- F-skip.

Évaluations de fenêtres :
- groupes 5 bits : `128 341 168`
- low/high 5 bits : `32 084 960`

Meilleur score de toute cette famille :
- `-6.934636`

Verdict : **négatif net**.

## 6. Empreintes de 761 comme secrets PRF

Objets :
- MP3 complet ;
- ID3 seul ;
- payload MPEG seul.

Pour chaque objet :
- SHA-1 et SHA-256 ;
- digest brut ;
- hex minuscule ;
- hex majuscule.

Soit 18 secrets.

16 générateurs PRF bornés :
- SHA-1 / SHA-256 de `secret||counter` et `counter||secret`,
  compteurs 32-bit BE/LE ;
- HMAC-SHA1 / HMAC-SHA256,
  compteurs 32/64-bit BE/LE.

Ajouts :
- compteur initial 0 ou 1 ;
- quatre réductions vers Z29 ;
- avant/arrière ;
- ± ;
- complément.

Total : `18 432` candidats.

Meilleur score :
- `-6.626697`

Aucun candidat proche d'un clair.

## 7. Générateurs d'époque — graines externes motivées

197 graines 32-bit uniques ont été dérivées de :
- `3301`, `761`, `167`, `2013`, `1595277641` ;
- tailles et CRC32 de l'ISO, MP3, ID3 et MPEG ;
- mots 32-bit des MD5/SHA1/SHA256, BE et LE ;
- nombres de la p.15, premiers associés et indices Fibonacci.

### PHP `mt_rand` historique
Le mode de compatibilité `MT_RAND_PHP` a été utilisé pour reproduire le
comportement antérieur à PHP 7.1.

Deux sorties :
- `mt_rand(0,28)` ;
- `mt_rand() % 29`.

Avec F-skip / sans F-skip, ± et complément.

Meilleur score :
- `-6.722667`

### `drand48`
Implémentation POSIX exacte du LCG 48 bits :
- `floor(29*drand48())`
- `lrand48() mod29`

Même famille de graines.

Meilleur score :
- `-6.666712`

Verdict : **aucune des graines externes motivées ne produit un clair**.

## 8. Bilan quantitatif de la campagne littérale

Les grandes passes contiguës représentent environ :

`553 035 496`

évaluations offset/configuration, auxquelles s'ajoutent les passes PRF et PRNG
ciblées.

Aucune ne produit une prose anglaise cohérente.

## 9. Ce que cette campagne exclut

Elle dépriorise fortement les modèles suivants :

1. `761.mp3` utilisé directement comme pad contigu avec réduction byte simple ;
2. même modèle avec F littéral/key-skip déterministe ;
3. conversion uniforme octet -> Z29 par rejet ;
4. conversion bitstream 5 bits -> Z29 ;
5. XOR direct de codes runiques 5 bits avec le MP3 ;
6. SHA1/SHA256 du MP3/ID3/MPEG injecté dans une petite famille PRF standard ;
7. graines externes évidentes injectées dans `MT_RAND_PHP` ou `drand48`.

## 10. Ce qui reste réellement ouvert

La priorité devient maintenant :

- **espace complet 2^32** d'un générateur d'époque, plutôt qu'une liste de graines ;
- key-skip non déterministe / dérive de compteur ;
- reseed par page, mot ou section ;
- stride / entrelacement du matériau `761.mp3` ;
- KDF combinant plusieurs objets historiques ;
- utilisation du signal audio décodé plutôt que des octets MP3.

La campagne exhaustive doit être faite sur **un seul générateur bien reproduit**
à la fois, avec oracle fixé avant calcul. Le premier candidat logique reste
l'ancien `PHP mt_rand`, puis `drand48`.

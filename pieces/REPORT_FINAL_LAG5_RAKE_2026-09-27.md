# Râteau expérimental lag-5 — rapport final

Préenregistrement figé **avant les permutations**, SHA-256 `fc0f7d76a53e8e24216c6f83b425998084f00bd1cde57b6950b0a0f87fe06754`. Trois tests exécutés, deux bloqués faute d'entrées vérifiables. Aucun plaintext recherché.

## FACT

L'adaptateur de la réplication indépendante, appliqué aux 177 premiers enregistrements runiques du fichier Mortlach, reproduit exactement les cinq compteurs du gate : 12 956 runes, 2 896 mots, 86 égalités adjacentes, 2 105 paires lag-5 internes, 104 égalités correspondantes. Le null préserve les longueurs et frontières des mots, les multiplicités exactes des runes et K=86. Quatre chaînes indépendantes ont fourni chacune 25 000 tirages après 2 000 000 transpositions acceptées de chauffe, espacés de 1 000 transpositions acceptées. Les résultats bruts des 100 000 réalisations figurent dans `null_t1_t3.csv`.

## OBSERVATION

T1 : à l'intérieur, 104/2 105 = **4,941 %** ; à travers une frontière, 375/10 846 = **3,457 %**. Différence **+1,483 point**, ratio des taux **1,429**. Sous null, différence moyenne −0,0049 point, intervalle empirique à 95 % [−0,836 ; +0,863] point, écart observé 3,43 écarts-types, p unilatéral **0,000420**. Les p par chaîne sont 0,000560, 0,000440, 0,000440, 0,000360. Le nombre brut des paires traversantes est proche de son attente conditionnelle.

T2 : le maximum absolu de Z parmi huit longueurs vaut **3,763**, p familial **0,00499**. La cellule responsable est L=10 : **20 égalités sur 260 paires**, attente conditionnelle **8,95**, Z=3,763. Toutes les cellules, y compris celles sans effet, sont conservées dans `T2_raw.json`. Les p familiaux par chaîne sont 0,00496, 0,00508, 0,00564, 0,00440.

T3 : les cinq phases comptent respectivement **38/872, 30/584, 18/350, 11/190, 7/109**. Maximum |Z|=**2,238**, p familial **0,1252**. Dispersion pondérée observée **0,0709**, moyenne nulle **0,1329**, p supérieur **0,7087**. Le test du maximum ne montre aucune phase singulière corrigée ; la dispersion n'indique aucune concentration supérieure au null. Les excès relatifs aux moyennes nulles sont positifs dans les cinq cellules.

## RESULT

T1 soutient une dépendance à la frontière du mot selon ce null. T2 identifie une contribution disproportionnée des mots de dix runes, parmi les huit classes gelées. T3 ne soutient pas la concentration de l'excès sur une phase interne particulière. Ces tests sont corrélés : il serait erroné de multiplier leurs p-values. Aucun diagnostic Holm à cinq tests n'est calculable, T4 et T5 étant bloqués.

## INFERENCE

Une structure qui distingue des positions à l'intérieur des mots gagne en plausibilité qualitative. Le poids des mots de longueur dix rend moins convaincante l'hypothèse d'un surplus parfaitement diffus sur toutes les longueurs. Un automate simple qui privilégierait une phase unique du mot ne reçoit pas l'appui attendu de T3. Ni T1 ni T2 ne démontrent un reset, une clé périodique ou une opération cryptographique précise. La dispersion faible ne prouve pas l'égalité des phases : elle établit seulement l'absence de concentration détectée par ce test.

## LIMITATION

T4 **BLOCKED** : la transcription Mortlach préserve les mots mais ne fournit pas une correspondance vérifiée de chacun des 12 956 emplacements aux frontières M0…M7 gelées, en particulier aux coupures intrapage. Attribuer les mots à partir d'un découpage supposé violerait la mission. Impossible de décider si le signal est diffus ou localisé par module.

T5 **BLOCKED** : l'archive B3 retrouvée contient les scripts et produits du scan mais pas les quatre textes Gutenberg indépendants accompagnés de leurs hashes et frontières de mots authentiques ; une implémentation synthétique exactement vérifiée du keyskip1 historique n'a pas non plus été établie. Aucune simulation de remplacement n'est présentée comme test du mécanisme. Impossible de trancher sa compatibilité avec le profil LP2.

Les tirages MCMC ne sont pas indépendants au sens strict ; les p affichés sont des fréquences empiriques avec correction +1 et les écarts entre les quatre chaînes renseignent sur leur stabilité. Leur concordance ne démontre pas une convergence parfaite. Le signal lag-5 ayant été découvert avant ce râteau, les p ici sont conditionnels au protocole gelé de suivi ; ils ne rétablissent pas une découverte prospective indépendante.

## Six réponses

1. **Mots :** oui, enrichissement interne relativement aux paires traversantes selon le null conditionnel ; pas de démonstration d'un reset.
2. **Diffus ou localisé :** hétérogène selon les longueurs, avec L=10 fortement contributif ; localisation globale non tranchée.
3. **Phase modulo 5 :** aucune phase dominante détectée ; dispersion non significative.
4. **Modules M0…M7 :** indéterminé, T4 bloqué.
5. **MT19937 + keyskip1 :** indéterminé, T5 bloqué.
6. **Familles de mécanismes :** montent qualitativement les explications sensibles aux mots et à leur longueur ; baisse l'attrait d'une phase unique fortement marquée. Les mécanismes de reset, keyskip1 et de modules ne peuvent pas être classés de façon probante par les tests disponibles.

| TEST | OBSERVED | NULL | P | EFFECT | VERDICT | CONSEQUENCE |
|---|---|---|---:|---|---|---|
| T1 | 104/2105 interne ; 375/10846 traversant | K=86 et marges exactes | 0,000420 | Δ=+1,483 point ; ratio=1,429 | SUPPORTED | Frontière de mot associée à l'excès, sans preuve de reset |
| T2 | L=10 : 20/260 ; max|Z|=3,763 | Maximum sur huit classes | 0,00499 | L=10 : +11,05 égalités vs attente | SUPPORTED | Excès hétérogène selon longueur |
| T3 | max|Z|=2,238 ; dispersion=0,0709 | Maximum sur cinq phases ; dispersion empirique | 0,1252 ; secondaire 0,7087 | Excès dans cinq phases, sans concentration | INFORMATIVE_NULL | Phase privilégiée simple non soutenue |
| T4 | Non calculé | Correspondance des modules non vérifiée | — | — | BLOCKED | Localisation M0…M7 inconnue |
| T5 | Non calculé | Contrôles et mécanisme non vérifiés | — | — | BLOCKED | Compatibilité keyskip1 inconnue |

**Arrêt après rapport.**

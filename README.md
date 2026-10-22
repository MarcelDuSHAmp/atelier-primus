# ATELIER PRIMUS — Liber Primus

**MarcelDuSHAmp · Collaboration IA : ASTRA GPT-6**  
État de la recherche : **22 octobre 2026** · édition publique **v0.1.0**

Nous étudions les 75 images de Liber Primus, leurs runes, leur géométrie et les gestes transmis par les pages résolues. Ce dépôt rassemble nos résultats, essais négatifs, corrections et pistes ouvertes, en distinguant les travaux antérieurs de nos reproductions et propositions.

**La piste la plus récente produit deux identifiants compatibles avec l’ancien format Tor v2. Leur calcul est reproductible ; leur existence historique et leur lien avec Cicada ne sont pas authentifiés. Aucune nouvelle page LP2 déchiffrée n’est revendiquée.**

| Parcours de lecture | Contenu |
|---|---|
| [État de la recherche](SYNTHESE.md) | Résultats exacts, hypothèses, contradictions et limites |
| [La piste des adresses `.onion`](PISTE_ONION.md) | Des 16 SPECIAL aux 80 bits ; prélèvement, dépôt et variantes |
| [171 fiches / 12 familles](recherches/README.md) | Explications simples, détails techniques, tests négatifs et attributions |
| [Atlas G000–G074](ATLAS.md) | Les 75 images et leurs empreintes |
| [Reproduire](REPRODUCTION.md) | Entrées, scripts Python et résultats attendus |
| [Crédits](ATTRIBUTION.md) et [sources](SOURCES.md) | Antériorités, matériaux tiers et contributions du projet |
| [Questions ouvertes](SUITE.md) | Expériences et preuves susceptibles de faire progresser la recherche |

## Deux sorties, deux gestes

- Prélèvement suivant G032 : `2h6vn7o256dtvsfp.onion`.
- Dépôt suivant G032, puis lecture par lignes : `hdnv2o26765tvsfp.onion`.

Le second geste reproduit le T des six SPECIAL de classe 30 ; le premier reproduit le lecteur RIGHT/RIGHT historique. Ces précédents différents ne sélectionnent pas à eux seuls un export final. G073 invite à trouver une page du deep web ; son texte résolu ne nomme pas explicitement le protocole Tor. Voir [la démonstration complète](PISTE_ONION.md).

## Vérification rapide

```bash
python3 calculs/verifier_dossier.py
python3 calculs/reproduire_onion.py
```

Python 3 et sa bibliothèque standard suffisent. Ces commandes travaillent hors réseau ; elles ne tentent pas d’ouvrir les adresses.

## Lire et contribuer

Après téléchargement du dépôt, ouvrir `INDEX.html` pour une lecture avec recherche dans les fiches. Les documents Markdown sont directement lisibles sur GitHub. Les calculs disponibles et leurs limites sont précisés dans [REPRODUCTION.md](REPRODUCTION.md).

Les 171 fiches conservent des états historiques ; la synthèse actuelle et les corrections priment. Le recensement privé portait sur 4 521 fichiers sources, mais ce dépôt est une sélection éditoriale : il ne publie pas l’ensemble des archives reçues et ne prétend pas avoir rejoué toutes les expériences. Les rapports non distribués sont identifiés dans [SOURCES.md](SOURCES.md).

Une contribution utile indique l’image ou l’entrée employée, la règle, les variantes essayées, la sortie et ce qui pourrait la contredire. Une répétition d’un résultat connu doit créditer sa source. Voir [CONTRIBUTING.md](CONTRIBUTING.md) et [CITER.md](CITER.md).

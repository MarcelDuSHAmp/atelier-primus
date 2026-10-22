# Reproduire les résultats publiés

Depuis la racine du dépôt, avec Python 3 et sa bibliothèque standard :

```bash
python3 calculs/verifier_dossier.py
python3 calculs/reproduire_onion.py
python3 architecture/rejouer.py
```

Le premier programme vérifie les 75 empreintes JPEG, les deux F0, leurs six différences, les 16 SPECIAL, φ(230)=88, les calculs G032, le routage précis 0/3 et les nuls locaux R4 N0–N2. Le second expose les étapes des douze exports Base32 et vérifie le retour aux octets SPECIAL. Il ne contacte pas Tor.

Le troisième contrôle les relations numériques de la [carte d’architecture](architecture/README.md) sur les deux F0 : conversions inverses, payloads D33/D34, BODY36, rangs AND16, contre-exemples, exports A/B et leur inversion. Il écrit `architecture/resultats.json`. Les contrôles de transcription runique et les campagnes historiques Tor restent attribués aux rapports ; ce script ne les relance pas.

| Entrées | Statut |
|---|---|
| `images/G000.jpg` à `G074.jpg` | Sources visuelles ; empreintes dans `donnees/images-75.json` |
| `calculs/r4/F0-3b9b07d9.bin` | Reconstruction utilisée pour l’export ; SHA-256 complet dans le journal |
| `calculs/r4/F0-0201348c.bin` | Autre version historique ; mêmes SPECIAL |
| `calculs/g032/inputs.json` | F0, alphabet, groupes transcrits et empreintes de provenance |
| `calculs/g032/results-attendus.json` | Sorties archivées de la mission G032 |
| `calculs/r4/LP_SEGMENTATION_AUDIT_20261013.py` | Transcriptions et conventions du test de segmentation |

Le rejeu part de données déjà constituées. Il ne prouve pas à nouveau l’extraction de toute la table F0 depuis les images, ni une découverte aveugle de la recette G032. La chaîne éditoriale conserve donc les niveaux **image → transcription → reconstruction → calcul → interprétation** séparés.

Ne sont pas relancés par ces commandes : MCMC lag-5, grandes campagnes ASTRA/761, scans externes Tor/AUTH et toutes les mesures visuelles. Leurs rapports sont des éléments historiques, avec une portée explicitée dans les fiches.

Les scripts du projet sont crédités à ATELIER PRIMUS et à son assistance IA. Les méthodes générales, recettes communautaires et transcriptions tierces sont détaillées dans [ATTRIBUTION.md](ATTRIBUTION.md). Les binaires de F0 et les données de test ne sont pas des clés Tor authentifiées.

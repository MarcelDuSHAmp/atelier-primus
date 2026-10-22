# Génération du dossier

Depuis la racine du dépôt, avec Python 3 et sa bibliothèque standard :

```bash
python3 outils/generer_parcours.py
python3 outils/generer_architecture.py
python3 outils/generer_index.py
```

La première commande produit les trois schémas SVG du [parcours en dix minutes](../PARCOURS_10_MIN.md), à partir du binaire F0 retenu et des données de contrôle G032. Elle vérifie les deux chaînes candidates. Les images sources restent intactes.

La deuxième produit la carte SVG et le modèle JSON des huit dossiers d’architecture. La troisième génère l’index HTML depuis les registres et les documents, avec les rubriques « 10 minutes », « Architecture / VM » et les171 fiches. La navigation et les dossiers d’architecture sont intégrés pour une lecture hors ligne.

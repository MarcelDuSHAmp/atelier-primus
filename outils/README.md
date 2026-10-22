# Génération du dossier

Depuis la racine du dépôt, avec Python 3 et sa bibliothèque standard :

```bash
python3 outils/generer_parcours.py
python3 outils/generer_index.py
```

La première commande produit les trois schémas SVG du [parcours en dix minutes](../PARCOURS_10_MIN.md), à partir du binaire F0 retenu et des données de contrôle G032. Elle vérifie les deux chaînes candidates. Les images sources restent intactes.

La seconde génère l’index HTML depuis les registres et les documents, avec une rubrique « 10 minutes » et les 171 fiches.

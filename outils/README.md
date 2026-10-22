# Génération du dossier

Depuis la racine du dépôt, avec Python 3 et sa bibliothèque standard :

```bash
python3 outils/generer_parcours.py
python3 outils/generer_architecture.py
python3 outils/generer_graphe_fonctionnel.py
python3 outils/generer_index.py
```

La première commande produit les trois schémas SVG du [parcours en dix minutes](../PARCOURS_10_MIN.md), à partir du binaire F0 retenu et des données de contrôle G032. Elle vérifie les deux chaînes candidates. Les images sources restent intactes.

La deuxième produit le plan documentaire SVG et le modèle JSON des huit dossiers. La troisième valide le graphe fonctionnel (nœuds, relations, sources et couverture des171 fiches), puis génère `architecture/FONCTIONNELLE.md` et sa vue d’ensemble SVG. Le JSON `architecture/graphe-fonctionnel.json` est la source éditoriale ; les liens de citation n’y sont jamais convertis automatiquement en transitions.

La dernière commande génère l’index HTML : recherche dans les circuits, propriétés des96 objets/fonctions, navigation le long des138 liaisons, huit dossiers explicatifs et171 fiches. Le contenu et la navigation sont intégrés pour la lecture hors ligne ; les sources externes gardent leurs liens.

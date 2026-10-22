# Adaptation de chemins

`rejouer.py` reprend LP_NULL_CLOSURE_20261021.py sans modifier les règles ni les modèles nuls. Trois changements : chemin du script de transcription, répertoire des deux F0, fichier de sortie. Le script de transcription est lu par `ast.literal_eval` pour extraire cinq constantes ; son code n’est pas exécuté.

Les entrées sont des transcriptions héritées ; ce rejeu n’est pas une nouvelle lecture indépendante des JPEG. N0, N1 et N2 sont rejoués. N3 et le balayage des phases restent documentaires dans cette édition. Le champ source_script change de nom local et ne fait pas partie de la comparaison numérique.

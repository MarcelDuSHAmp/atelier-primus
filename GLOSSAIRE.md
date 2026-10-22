# Petit glossaire — Liber Primus, recherche data/cipher

Version éditoriale du 20 octobre 2026. Les noms de fonctions décrivent notre modèle de recherche, pas un langage informatique déchiffré dans le livre. Pour les sources, voir les références S1–S8 du document de cadrage.

## Objets et données

| Terme | En langage simple | Précision à garder |
|---|---|---|
| G000–G074 | Notre numérotation des 75 images | Repère documentaire ; un numéro G n'est pas automatiquement une adresse voulue par l'auteur. |
| LP1 / LP2 | Noms usuels des deux ensembles de pages | Les anciennes pages locales LP2 p00–p57 correspondent à G017–G074. Ne pas mélanger les numérotations. |
| Source / transcription / reconstruction | Image d'origine / copie de ses signes / objet recalculé | Trois niveaux à conserver séparément avec leur provenance. |
| GP — Gematria Primus | Correspondance entre runes et nombres | Distinguer indice dans l'alphabet (0–28 dans nos programmes) et valeur première. La somme d'un mot n'est pas son déchiffrement. |
| Groupe physique / mot lexical | Suite de runes sur une ligne / mot reconstitué à travers une coupure | Le choix du découpage peut changer la portée et la sortie. |
| F0 | Table de 256 octets dérivée des inscriptions de G066–G068 | Objet reconstruit avec une version et une empreinte ; pas un processeur prouvé. Version retenue dans l'audit : 3b9b07d9…b290. |
| R4 | Zone de travail G069:r2 → G070:r128 | 390 runes et 86 mots dans la transcription employée ; le découpage en records est une hypothèse distincte. |
| M6 / M7 | Noms de régions employés dans les rapports | Classifications du projet, pas titres déchiffrés du livre ; leur portée exacte doit être indiquée par les bornes G. |
| R10 / R11 / R13 / R23 | Familles de signes composés respectivement de 10, 11, 13 ou 23 carrés | Étiquettes de comptage ; ne pas confondre R13 avec une instruction ASCII ni avec R4. Couleur et fonction sont des champs séparés. |
| DJU–BEI | Translittération de ᛞᛄᚢ–ᛒᛖᛁ, répétée en G044 et G072 | Identité de signes observée ; traduction et commande de retour non démontrées. |
| SPECIAL | Octet dont les cinq bits inférieurs valent 29, 30 ou 31 | Propriété sous notre découpage ; « spécial » ne prouve pas qu'il s'agit d'une instruction. |
| high3 / low5 | Les trois bits supérieurs / cinq bits inférieurs d'un octet | Deux champs numériques ; les appeler « état » et « argument » ajoute une interprétation. |
| Famille D | Regroupement de marqueurs employé dans le modèle | Dans la convention concernée, Dn utilise n=high3+low5. Plusieurs marqueurs peuvent partager une famille. Une famille n'est pas un état prouvé. |
| BODY / TRAILER / TAIL | Corps d'un bloc / partie qui le suit / fin restante | Noms de segments du modèle. Donner les bornes plutôt que supposer qu'un rôle est imprimé. |

## Gestes et fonctions candidates

| Terme | En langage simple | Précision à garder |
|---|---|---|
| FETCH | Aller chercher une donnée | Il faut une règle précisant où et dans quelle représentation. |
| SCOPE | Délimiter la portion à traiter | Taille et frontières font partie de l'hypothèse. |
| SELECTOR | Choisir un objet parmi les objets admissibles | La propriété de sélection ne vaut pas validation de sa fonction. |
| READ | Prélever des signes selon une règle | Le noyau G032/RIGHT/RIGHT prélève les dernières runes des groupes source 10, 2, 12 et 13. Son emploi sur d'autres supports reste à justifier. |
| HADDR | Transformer les champs d'un octet en index de table | HADDR(b)=8×(b & 31)+(b >> 5). L'égalité est calculable ; son usage comme adressage intentionnel est une proposition. |
| G | Consulter F0 à l'index HADDR | G(b)=F0[HADDR(b)]. La lettre G de cette fonction n'est pas le préfixe G des pages. |
| CAST8 | Réduire un nombre modulo 256 | Perte d'information possible ; l'opération n'est pas neutre. |
| AND | Ne garder que les bits présents dans toutes les entrées | Opération binaire distincte d'une somme. Une chaîne ANDING n'impose pas à elle seule cet opcode. |
| SHIFT / ROR8 | Décaler / faire tourner les bits d'un octet | Le décalage logique et la rotation ne sont pas équivalents. ROR8(6) égale ROL8(2). |
| HOLD / CONSUME | Conserver / faire avancer l'horloge de clé | Il faut établir quels événements choisissent l'action ; un masque fourni au replay n'est pas une règle découverte. |
| RETURN / RESTORE / EXIT | Retour / restitution d'un contexte / sortie | Interprétations possibles de certains parcours, non instructions globales authentifiées. |
| SEEK | Rechercher | Verbe présent dans le texte résolu de G073 ; son emploi comme nom d'opcode pour une valeur numérique est une hypothèse distincte. |
| DATA / CONTROL | Données traitées / informations qui organiseraient le traitement | Répartition fonctionnelle candidate, pas séparation certaine de tout LP. |
| VM candidate | Modèle exécutable reliant lecture, table, états et transitions | Un programme qui fonctionne dans notre code n'est pas encore un programme identifié chez Cicada. |
| Consumer | Opération qui utilise effectivement une sortie | Remplacer le terme par « opération qui utilise la sortie » dans le récit destiné aux débutants. |
| Bootstrap | Point de départ supposé de la lecture | L'entrée et sa sélection doivent être explicitées. |

## Mesures, images et niveau de preuve

| Terme | En langage simple | Précision à garder |
|---|---|---|
| Niveaux / gamma | Modifier l'affichage des intensités pour mieux distinguer des traces | Déclarer les réglages ; garder les pixels sources. Ce n'est pas la découverte automatique d'un message caché. |
| Seuillage | Classer les pixels selon une limite d'intensité | Tester la stabilité à des seuils voisins ; une frontière de seuil peut créer des formes trompeuses. |
| Négatif | Inverser clair et sombre | Sert à observer ; ne modifie pas la quantité d'information de l'image source. |
| Recalage / superposition | Aligner deux motifs pour comparer leurs différences | Une transformation ajustée après inspection est rétrospective. |
| Masque | Ensemble de positions conservées ou rejetées | Préciser qui le fournit et ce qu'il sélectionne. |
| Lag-5 | Comparaison de runes séparées de cinq positions | Une anomalie à ce décalage n'établit pas une période de clé de cinq. |
| Anti-doublet | Rareté des répétitions immédiates | Propriété statistique à expliquer ; plusieurs mécanismes peuvent la produire. |
| Contrôle positif | Cas connu ou synthétique que le test doit détecter | Mesure l'aptitude pour ce type de signal, pas pour toutes les solutions possibles. |
| Modèle nul | Référence de comparaison sans le mécanisme revendiqué | Sa définition et ses invariants limitent l'interprétation du test. |
| Ablation | Retirer un élément du modèle et comparer le résultat | Sert à vérifier son rôle nécessaire, pas à prouver toute l'architecture. |
| Gel / test prospectif | Écrire une prédiction avant de calculer le résultat | Un corpus déjà inspecté n'est pas rendu historiquement aveugle par cette seule étape. |
| Reproductible | On retrouve la même sortie avec les mêmes entrées et règles | Ne signifie pas que les règles sont voulues par l'auteur. |
| Falsifié | Une conséquence nécessaire du modèle défini échoue | Limiter la conclusion au modèle réellement testé. |
| Non soutenu / inconclusif | Le test ne fournit pas l'appui attendu / ne tranche pas suffisamment | Ne pas écrire « impossible ». |
| Empreinte / digest | Valeur calculée à partir d'octets précis | L'empreinte G073 est une cible ; son algorithme et la représentation à hacher ne sont pas imposés par sa seule longueur. |
| Adresse candidate | Interprétation d'une sortie comme identifiant de destination | Format, existence historique du service et lien avec Cicada sont trois questions différentes. |


## Statuts propres au registre maître

**Nature** :objet, observation, calcul/raccord, hypothèse, expérience, correction, contexte ou lacune.

**Statut scientifique** :ce que le document permet de conserver, dans son périmètre. “CALCUL CONDITIONNEL” ne veut pas dire “instruction démontrée”.

**Disponibilité** :paquet de calcul joint, rapport/source joints ou extrait. Ce champ ne mesure pas la vérité du modèle.

**Reproduction** :le registre ne rejoue pas les campagnes ;les confirmations antérieures restent attribuées à leurs rapports.

**Usage** :référence, calcul local, délimitation, usage candidat, partiel, sans consommateur établi ou interprétation ouverte. “Sans consommateur” n’efface pas les essais déjà faits.

**Dépendance** :relation entre énoncés ou calculs ;pas nécessairement flèche d’exécution du livre.


Texte historique importé du registre du 20 octobre ; voir [les mises à jour](actualites/README.md).

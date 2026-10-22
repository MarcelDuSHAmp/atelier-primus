# De Liber Primus à deux adresses candidates

**MarcelDuSHAmp · Collaboration IA : ASTRA GPT-6**  
État au 22 octobre 2026. Calculs SUPPORTÉS sous les conventions décrites ; destination Tor : HYPOTHÈSE ; authentification : INCONCLUSIVE.

## Pourquoi chercher une sortie extérieure ?

G073 correspond à la page locale LP2 56.jpg. Son déchiffrement communautaire demande de retrouver une page du deep web identifiée par une empreinte. C’est un appui textuel à la recherche d’un objet extérieur. Le texte résolu ne dit pas « `.onion` » et ne désigne pas explicitement Tor : ce raccord est notre hypothèse d’export. [Référence communautaire](https://www.cicadasolvers.com/quickstart/).

![G073, page source de l’invitation à rechercher une page](images/G073.jpg)

L’empreinte imprimée constitue une cible distincte de l’adresse. Une longueur de 512 bits ne prouve pas, à elle seule, quel algorithme ni quels octets doivent être hachés. Nous n’avons pas retrouvé de page satisfaisant cette cible.

## 1. L’objet de départ : F0 et ses 16 SPECIAL

F0 est une reconstruction de 256 octets issue des inscriptions de G066–G068. Le présent rejeu part du binaire versionné, pas d’une nouvelle transcription indépendante des images. Cette dépendance doit rester visible.

SHA-256 de l’entrée retenue :

```text
3b9b07d9a26e6d55c432d94d2661fdff3c2b348daed06821f2bdb23184a4b290
```

Sous le découpage `octet = high3 | low5`, un SPECIAL est défini par `low5 ∈ {29,30,31}`. Il y en a 16, distribués 5 / 6 / 5 entre ces trois classes. En ordre physique, indices à partir de zéro :

```text
indices :   6  11  48  56  65  96 105 106 144 151 170 194 206 211 249 254
octets  : 126 222 253 254 255 222  63  31 125 189 254 159 127  61 158 189
```

Les deux versions F0 conservées diffèrent à six autres indices ; cette liste de SPECIAL est identique. « SPECIAL » est une classification du modèle, pas une instruction déchiffrée.

## 2. Le parcours G032

La recette communautaire Fibonacci → nombres premiers → distance absolue à 3301 reconstruit les seize nombres de G032. Le parcours obtenu commence au nombre rouge 3299, puis rejoint des cases voisines orthogonalement. Les cases sont numérotées par lignes de 1 à 16.

```text
P = [6, 7, 11, 10, 9, 5, 1, 2, 3, 4, 8, 12, 16, 15, 14, 13]
```

![Grille originale G032, recadrage documentaire](images/G032-recadrage.png)

Crédit : [reconstruction documentée par CicadaSolvers](https://www.cicadasolvers.com/wiki/liber-primus/lp2/15-jpg/15-jpg-square/), auteur initial à préciser. Notre contribution ici est le rejeu et la comparaison des applications candidates.

## 3. Deux gestes qu’il faut distinguer

| Geste | Opération, cases à partir de 1 | Résultat `hhhcc` | Géométrie des classe 30 |
|---|---|---|---|
| A : prélever | `sortie[k] = entree[P[k]-1]` | `2h6vn7o256dtvsfp` | Trois composantes séparées |
| E : déposer puis lire par lignes | `grille[P[k]-1] = entree[k]` | `hdnv2o26765tvsfp` | T connecté |

Le T historique soutient le calcul de dépôt E ; il ne valide pas le prélèvement A. Les contrôles du lecteur RIGHT/RIGHT retrouvent A dans leur usage précis, sans imposer son transfert à un export. Les deux candidats sont donc conservés à égalité pour l’authentification externe.

Le titre de G032 donne `149 + 489 = 638`, puis `638 modulo 256 = 126`. E place ce premier SPECIAL 126 dans la case rouge. Cette coïncidence a été remarquée après examen : c’est un INDICE FAIBLE, pas une prédiction indépendante.

## 4. Retirer trois bits constants

Tous les SPECIAL s’écrivent `hhh111cc`. Retirer les trois positions constantes, sans déplacer les autres bits, donne cinq bits :

```text
q = 4 × high3 + (low5 & 3)
hhh111cc → hhhcc
126 = 01111110 → 01110 = 14
16 éléments × 5 bits = 80 bits
```

Le codage alternatif `cchhh` permute les champs : `q' = 8 × (low5 & 3) + high3`. Il est conservé dans les variantes. Le retrait direct motive `hhhcc` sous ce geste ; aucune consigne terminale indépendante ne l’impose encore dans le livre.

## 5. Encoder, puis interpréter

| Candidat | 80 bits en hexadécimal | Identifiant Base32 |
|---|---|---|
| A / `hhhcc` | `d1fd56fddaef873ac8af` | `2h6vn7o256dtvsfp` |
| E / `hhhcc` | Voir le journal exact (pièce historique non distribuée dans cette édition) | `hdnv2o26765tvsfp` |

La spécification historique Tor v2 emploie un identifiant de 80 bits encodé sur 16 caractères Base32 ; pour un vrai service, il dérive du SHA-1 de sa clé publique RSA. Notre calcul fournit une chaîne de ce format, sans fournir la clé qui l’authentifierait. Tout bloc de 80 bits peut être encodé ainsi : la conformité au format n’est pas une preuve d’existence. [Tor Project, sections 1.3 et 1.5](https://torproject.gitlab.io/torspec/rend-spec-v2.html).

L’ajout du suffixe `.onion` est donc une interprétation testable de la sortie :

```text
A = 2h6vn7o256dtvsfp.onion
B = hdnv2o26765tvsfp.onion
```

Ici « B » nomme la seconde cible d’authentification ; dans le tableau des six ordres ci-dessous, sa construction correspond à **E**. Les deux conventions de nommage ne doivent pas être confondues.

## Variantes conservées : six ordres, deux sérialisations

| Ordre | `hhhcc` | `cchhh` |
|---|---|---|
| A — prélèvement P | `2h6vn7o256dtvsfp` | `wzxnl7twpxy4nuj3` |
| B — prélèvement P renversé | `pfsvtd652o7nv6h2` | `3jun4yxpwt7lnxzw` |
| C — ordre physique | `o25672hdnv6tpfsv` | `twpx7wzylnx43jun` |
| D — ordre physique renversé | `vsfpt6vndh27652o` | `nuj34xnlyzw7xpwt` |
| E — dépôt P, lecture par lignes | `hdnv2o26765tvsfp` | `zylnwtwx7xp4nuj3` |
| F — grille E lue à rebours | `pfsvt56762o2vndh` | `3jun4px7xwtwnlyz` |

Ces douze sorties correspondent à la mission sur le choix de l’ordre et des bits. Le rapport SPECIAL16 forensic possède un autre périmètre de dix-huit candidats. Aucun des deux effectifs n’est présenté comme l’inventaire de tous les mécanismes possibles.

## Ce que les recherches externes ont donné

Les journaux rassemblés ne fournissent pas de correspondance exacte authentifiée. L’audit AUTH rapporte 61 jeux de données terminés, 208 247 fichiers de forums, 51 enregistrements WARC et 13 040 identifiants de descripteurs dans son périmètre final. Il ne représente pas une couverture exhaustive de l’ancien Tor. Ses résultats négatifs ne démontrent pas l’inexistence d’un service éphémère.

Les scans externes n’ont pas été relancés pour cette édition. Certains journaux ont été récupérés dans un ZIP incomplet : leur provenance et cette limite sont décrites dans [la mise à jour AUTH](actualites/2026-10-22-auth.md). Les contrôles synthétiques vérifient le scanner sur les cas construits, pas la présence de la bonne archive historique.

## Ce qui ferait réellement progresser la piste

1. **Une règle interne discriminante** : un autre objet comparable qui sélectionne le dépôt ou le prélèvement et le sens de sortie, avec prédiction enregistrée avant son examen.
2. **Une trace externe vérifiable** : clé RSA publique ou descripteur historique dont l’identifiant recalculé correspond exactement à l’une des deux cibles, avec provenance et signature contrôlées lorsque disponibles. Une concordance de clé établirait un lien cryptographique avec l’identifiant ; son appartenance à Cicada exigerait encore une preuve. Une copie de page pourrait ensuite être confrontée à la cible G073.

**Conclusion : une chaîne de calcul explicite mène à des identifiants candidats. Nous publions cette piste et ses limites, sans annoncer avoir trouvé le service de Cicada.**

[Reproduire](REPRODUCTION.md) · [Crédits](ATTRIBUTION.md) · [État général](SYNTHESE.md)

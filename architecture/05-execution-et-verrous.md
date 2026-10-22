# 05 · Exécution, état et pièces manquantes

[Carte d’ensemble](README.md) · [Audit VM A01](SOURCES.md)

## Ce que nous pouvons exécuter aujourd’hui

Des fonctions pures et des compositions paramétrées : lire F0, convertir des coordonnées, transformer un payload, appliquer un masque, parcourir16 objets et encoder une sortie. Le solveur fournit encore plusieurs objets, paramètres et transitions. Le résultat de l’audit est **VM PLAUSIBLE**, et non VM exécutable ou prédictive.

| Élément d’une VM | État actuel | Ce qui permettrait de le reconnaître |
|---|---|---|
| BOOT | INCONNU ; G005, M6, PRE64 et d’autres objets restent explorables | Une règle donnant départ, convention et état initial sans viser une destination déjà connue |
| PC / INDEX | Disponible dans un simulateur, non identifié comme registre du livre | Une instruction qui le lit ou le modifie, avec NEXT contrôlé |
| VALUE / BYTE | Temporaire suffisant pour les calculs actuels | Persistance imposée si on veut en faire un registre |
| FRAME / SCOPE | Bornes utiles fournies par les protocoles | Parseur enseigné, capable de distinguer body/footer sur un autre cadre |
| MODE / DIR | Variables exploratoires possibles | Un indice imposant HADDR/HINV ou le sens sur un locus divergent |
| STATE / ACC | État persistant non nécessaire aux replays actuels | Même objet, deux états contrôlés, deux comportements correctement prédits |
| CALL / RETURN | Raccord105→249 exact ; pile/retour non démontrés | Sauvegarde, branchement, puis restauration d’un retour ; réplication |
| HALT / END |126 après35 ordinaires est exact ; rôle terminal hypothétique | Condition d’arrêt imposée par le corpus, indépendante de l’arrêt du script |
| STORE | Aucune écriture reconstruite | Adresse, valeur et effet ultérieur observables |
| APPLY / EMIT | Consommateur final non identifié | Opération sur R4 ou sortie numérique qui produit une donnée contrôlable sans retouche |

## Le témoin sans état

`sortie = fonction(objet, paramètres)` reproduit les résultats locaux connus aussi bien que leur présentation sous forme de registres. Une boucle dans une fonction sur 256 valeurs est attendue dans un ensemble fini ; elle ne suffit pas à prouver un cycle d’instructions.

Le test utile compare **objet + état + événement → comportement + nouvel état** à un modèle de complexité voisine sans état, sur une situation où leurs prédictions divergent. Une représentation graphique en machine ne constitue pas ce test.

## NEXT et CALL/RETURN : les essais conservés

L’audit A01 compare huit règles simples : identité, HADDR, HINV, low5, high3, totient, F0∘totient et PC+1. Aucune ne retrouve toute la chaîne proposée105→249→211→6.

Un alternateur ajouté après exploration retrouve `105→249→211`, puis donne **233**, pas6. Cette règle est falsifiée pour cette chaîne. À la fermeture254, les lectures testées ne restaurent pas106, l’adresse conventionnelle suivant105. Cela contredit ces modèles précis ; cela ne démontre pas l’impossibilité d’une autre machine à instructions locales.

## Pseudocode fidèle au niveau de preuve

```python
def replay_d32(F0):
    return HADDR(F0[105])  # 249 ; départ et opération choisis par le protocole

def prochaine_instruction(objet, contexte):
    raise NotImplementedError("Décodage et NEXT du livre non reconstruits")
```

Cette exception est une limite de notre reconstruction. Elle n’est pas un HALT trouvé dans Liber Primus. Le [script de contrôle](rejouer.py) exécute les calculs définis, sans remplir les transitions inconnues par des règles inventées.

## Deux verrous productifs

- **Commande de représentation.** Trouver un indice qui décide code à champs/index linéaire avant de regarder la destination. L’adjacence des SPECIAL et l’intérieur de quatre octets ont déjà échoué au contrat testé.
- **Consommateur de 80 ou132.** Identifier un objet qui exige cette entrée, son type, son opération et sa condition de sortie. Un nombre identique dans une autre page est un point de départ exploratoire, pas encore une transition validée.

Le bilan A01 rapporte **zéro cycle aveugle certifié et zéro nouvelle prédiction LP indépendante vérifiée dans cette passe**. Cela n’annule pas les calculs rétrospectifs ; cela borne leur force. Toute exploration reste possible, en enregistrant paramètres et sorties. Une validation prospective doit réserver des données réellement non employées pour construire la règle.

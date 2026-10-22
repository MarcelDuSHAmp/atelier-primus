# Liber Primus — chaîne de contrôle finale candidate
Date: 2026-10-21

## Verdict

La chaîne p51–p56 peut être fermée comme **programme de contrôle / validation** sans postuler un déchiffreur runique supplémentaire.

Le meilleur APPLY actuellement soutenu est:

```text
APPLY_CONTROL(DATA, STATE)
```

et non:

```text
APPLY_CONTENT(ciphertext, key) -> plaintext
```

Le contenu des trois BODY16 est effectivement consommé par un réducteur spatial G032 qui calcule la fenêtre d'état suivante et, avec les bytes complets, définit un frame de validation F0.

## Chaîne

```text
p51 / G068 — CHECKPOINT
   |
   | G032 lexical RIGHT/RIGHT
   | readout = 272 -> G005 coord55
   v
p55 / G072 — DISPATCH / RECAP
   |
   | même lecteur
   | readout = 138 -> G005 coord54
   v
p54 / G071 — BUFFER / CONFIG
   |
   | readout = 254 = 7|30 = D37
   | structure indépendante:
   | start intérieur 37
   | longueur 157 = prime(37)
   | 35 mots complets
   v
D37
   |
   | HADDR / F0 natif
   v
D33
   |
   | ancre de la fenêtre source class30
   v
SOURCE = [D33,D36,D37] = [3,6,7]

R4 / G069–G070
  3 × [CALL + BODY16 + TRAILER7] + TAIL14

  BODY A -> G032 RIGHT/RIGHT -> 198 = 6|6
  BODY B -> G032 RIGHT/RIGHT -> 254 = 7|30
  BODY C -> G032 RIGHT/RIGHT -> 154 = 4|26

  high3 -> [6,7,4]
          = [D36,D37,D34]

DEST = [D36,D37,D34]

Les bytes complets se recollent en même temps à F0:
  C=154 -> HADDR=212 = START
  B=254 -> HADDR=247 = END
  F0[246] = A=198
  F0[247]=192 -> HADDR6 -> D33

Frame:
  F0[212..247]
  -> G cellule par cellule
  -> 35 sorties ordinaires
  -> dernière cellule -> D33

p53 / G070 — CLOSE
  canal lexical/rouge contient 245 -> 130 -> 34
  = OBSCURA -> VOID -> D34
  cohérent avec le nouvel état terminal D34

p52 / G069 — RETURN
  G032 RIGHT/LEFT -> 151

151
  -> descripteur matériel p51 = 4|23
  -> retour au checkpoint p51

p51
  -> self-validation D34
  -> retour 151
  -> CHECK PASS

EXIT du module p51–p55

p56 / G073 — continuation physique
  G032 RIGHT/RIGHT -> 154
  unique page du corpus donnant 154 sous ce lecteur figé
  = même readout que R4-C / état high3=4

G073 plaintext résolu:
  AN END
  WITHIN THE DEEP WEB
  THERE EXISTS A PAGE THAT HASHES TO
  [digest 512-bit imprimé]
  IT IS THE DUTY OF EUERY PILGRIM TO SEEC OUT THIS PAGE
```

## Définition compacte de APPLY_CONTROL

Pour chaque BODY de 16 mots:

```text
ORDER = G032_ORDERING[16]
EDGE = RIGHT
ENDPOINT = RIGHT
SELECT = positions 4,8,12,16 du carré réordonné
READOUT = somme GP des quatre runes terminales
```

Sur R4:

```text
R = [198,254,154]
NEXT_STATE = high3(R)
           = [6,7,4]
           = [D36,D37,D34]
```

Le low5 n'a pas besoin d'être interprété comme trois opcodes indépendants.
Les bytes complets sont consommés collectivement par la géométrie F0:
`154 -> START212`, `254 -> END247`, `198 -> sentinel END-1`.

## Familles APPLY_CONTENT testées et rejetées sous les contrats essayés

- low5 `[6,30,26]` comme index direct;
- low5 comme départ prime/totient des trailers;
- lecteur G073 prime/totient avec états D33/D36/D37 ou high3 3/6/7;
- HOLD libre ou sélectionné sur F: aucun binder matériel général;
- clés historiques DIVINITY (8) / FIRFUMFERENFE (13), y compris piste 5–8–13;
- F0 comme transducteur Mealy `state+rune -> state'+rune'`;
- 35 sorties F0 comme clé ou descripteur des 35 mots résiduels R4;
- 35 sorties F0 comme clé ou descripteur du buffer35 p54;
- BODY A/BUFFERS comme clé brute de BODY B/OBSCURA;
- self-key des quatre endpoints G032;
- lecteurs LP1 sur la clause rouge de G070, y compris son unique F comme HOLD.

Aucun ne produit un plaintext ou une sortie typée commune sans retuning.

## Statut

### Fort / calcul exact sous le contrat
- readouts R4 `[198,254,154]`;
- high3 `[6,7,4]`;
- frame F0 `212..247`;
- A à END-1;
- terminal vers D33;
- p54 -> 254/D37;
- p52 RIGHT/LEFT -> 151;
- p56 RIGHT/RIGHT -> 154.

### Candidat architectural fort
- p51 -> p55 -> p54 -> p53 -> p52 -> p51 comme cycle de contrôle;
- p51 comme checkpoint;
- p55 comme dispatch/recap;
- p54 comme buffer/config;
- p53 comme CLOSE;
- G073 comme continuation après validation du module.

### Non démontré
- APPLY_CONTENT runique produisant du plaintext;
- fonction globale des low5;
- rôle de G034, qui donne également 198 sous RIGHT/RIGHT mais n'a pas de typage D36 indépendant établi;
- algorithme et sérialisation exacts du digest G073;
- résolution des autres pages LP2.

## Conclusion

La meilleure lecture actuelle n'est plus:

```text
LP2 ciphertext -> cipher inconnu -> anglais
```

mais:

```text
LP1 apprend des gestes
-> LP2 exécute un control-plane
-> R4 calcule une transition d'état
-> F0 valide la transition
-> le module revient au checkpoint
-> la continuation mène à une instruction explicite externe
```

Le programme de contrôle est substantiellement reconstruit.
Le processeur de contenu runique, s'il existe comme couche séparée, ne l'est pas encore.

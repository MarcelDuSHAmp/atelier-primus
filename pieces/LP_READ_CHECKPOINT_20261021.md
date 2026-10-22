# Liber Primus — checkpoint READ / DECRYPT — 21 octobre 2026

## Verdict

- **READ local G068→G071 : fortement identifié.**
- **DECRYPT / RUNE_EMIT : non identifié.**
- **D33 : candidat HALT/END fort**, pas RETURN prouvé.
- Le prochain verrou n'est plus le découpage ou l'ordre du module étudié, mais le passage d'une sortie numérique/GP validée vers un consumer qui émet ou transforme réellement des runes.

## Chaîne locale la plus contrainte

### 1. Instruction / paramètre
- G068 first16 groupes physiques + G032 RIGHT/RIGHT donne `ANDING` (résultat antérieur).
- Le résidu G068 + G069:r1 forme 8 groupes ; AND colonne par colonne sur F0 donne 8 octets `[32,134,0,0,0,4,32,115]` ; SUM mod256 = `61 = 1|29`, marqueur D30 @211. Ce raccord reste rétrospectif mais fortement contraint par les contrôles déjà effectués.

### 2. Frame D30
- D30 @211 ; BODY @212..247, 36 cellules ; footer113 @248 ; D34 @249.
- `G(x)=F0[HADDR(x)]` sur les 36 cellules : 35 sorties ORDINARY puis D33 sur la 36e.
- Les 35 sorties ordinaires sont alignées sur les 35 mots lexicaux entre les deux mots GP199 de G071.

### 3. Sélecteur AND16
Sous F0 corrigé 0201348c… :
- `s_i & 16 != 0` sélectionne exactement les slots
  `2,3,5,6,8,10,14,16,19,20,25,27,28,31,34,35`.
- 16 mots sélectionnés.
- Ils contiennent exactement **61 runes**, soit `61 = 1|29 = D30`.
- GP total = 3088 (ancienne observation ; la réduction mod256 n'est pas nécessaire à la nouvelle chaîne).

Autres bits unitaires sélectionnant 16 mots :
- bit2 → 68 runes ; G032 readout 204
- bit4 → 60 runes ; G032 readout 146
- bit16 → **61 runes ; G032 readout 132**
- bit32 → 68 runes ; G032 readout 184

### 4. Alignement
35 décalages cycliques × 2 sens = 70 alignements du masque AND16 avec les 35 mots :
- **un seul** produit 61 runes : l'alignement imprimé naturel ;
- **un seul** produit le readout132 : le même alignement naturel.

### 5. G032 sur les 16 mots
G032 RIGHT/RIGHT sélectionne les mots de rang 10,2,12,13 dans les 16 retenus :
- finales : `ᛄ · ᛄ · ᚷ · ᛇ`
- GP : `37 + 37 + 17 + 41 = 132`
- `132 = 4|4`.

Ablation spatiale sur AND16 :
- RIGHT/RIGHT = 132
- RIGHT/LEFT = 139
- LEFT/RIGHT = 272
- LEFT/LEFT = 192
- TOP/RIGHT = 256
- TOP/LEFT = 108
- BOTTOM/RIGHT = 108
- BOTTOM/LEFT = 220

Donc 132 dépend du lecteur exact déjà appris sur G032/G068.

Nul combinatoire descriptif : parmi tous les sous-ensembles de 16 mots sur 35, le readout RIGHT/RIGHT vaut132 dans ~1,372%; en conditionnant aussi sur une longueur totale de61 runes, ~1,703%. Ce n'est pas une p-value de découverte.

### 6. Binding de 132 dans R4
R4 possède 86 mots lexicaux :
- GP132 : **1 occurrence**, mot15 `ᚻᛠ` ;
- GP150 : **1 occurrence**, mot16 `ᛞᚩᛄᚷ` ;
- ils sont adjacents : `132 → NEXT 150`.
- `G(150)=144`.

La coda rouge G070 en segmentation lexicale contient :
`[215,126,106,709,150,241,34,260,144,191,14,72]`.
Donc elle contient une fois 150 puis une fois 144.

Important typage : le GP150 rouge n'existe **que si le mot est raccordé lexicalement à travers le retour de ligne** (`ᛇ/ᛠ` → GP150). En segmentation physique, ces deux groupes valent41 et109 séparément. À l'inverse, le bloc noir entre guillemets de G070 exige 16 **groupes physiques** (14 mots lexicaux) pour accepter le lecteur G032.

### 7. Boucle 150 / 144 / 4|16
Le bloc noir G070 explicitement encadré :
- 16 groupes physiques ;
- G032 RIGHT/RIGHT → 4 finales ;
- GP total = **150** ;
- unique fenêtre contiguë de16 groupes physiques de R4 avec cette sortie.

Puis :
- `G(150)=144` ;
- la coda rouge contient GP150 puis GP144 ;
- `144 = 4|16`, concordant exactement avec la géométrie **16 entrées → 4 sorties** du lecteur.

Le résultat G071 `132` suit aussi la route G :
`132 →54→131→150→144↔169`.
Parmi les configurations naturelles testées (bits sélectionnant16 × 8 lecteurs), AND16+RIGHT/RIGHT est la seule à atteindre150 en ≤3 appels G.

### 8. Red-team contre R4 / coda rouge
Parmi les 32 combinaisons naturelles (bits 2/4/16/32 donnant16 mots × 8 lecteurs), seules quatre sorties correspondent à une somme GP de mot R4 :
- 259 → mot R4 ; NEXT96 ; G(96)=186 ; rien dans la coda
- 202 → mot R4 ; NEXT287 ; hors byte
- **132 → unique mot15 ; NEXT150 présent rouge ; G(150)=144 présent rouge**
- 192 → unique mot67 ; NEXT138 absent rouge ; G(138)=173 absent rouge

Donc la chaîne complète `output → mot R4 → NEXT → G(NEXT) → coda` sélectionne uniquement AND16 + G032 RIGHT/RIGHT dans cette famille.

## D33
Class30 F0 :
- D33 `3|30` @6 : singleton
- D34 `4|30` @249 : singleton
- D36 `6|30` @11,@96
- D37 `7|30` @56,@170

Sous routage G répété vers le prochain SPECIAL :
- D37 → D33 (2 hops)
- D38 → D33 (7)
- une branche D32 → D33 (12)
- plusieurs D34 → D33 (8/11)
- D33 lui-même sort vers un cycle ordinaire 144↔169.

Dans D30 BODY, D33 arrive exactement après 35 sorties ordinaires à la 36e cellule. **HALT/END est donc la fonction locale la plus économique**, mais aucune source ne prouve encore qu'il émet la valeur calculée132 vers R4.

## Fragilités conservées
1. `AND16 → 16 items` dépend du F0 corrigé : l'ancien F0 historique reconstitué donnait17 ; le F0 corrigé transmis et le L5 externe donnent16 selon CP87/CP119. L'autorité raster de la correction doit rester attachée au résultat.
2. `ANDING → bitwise AND` reste une interprétation, quoique désormais utilisée sur plusieurs raccords cohérents.
3. `144=4|16 → 16 entrées/4 sorties` est très cohérent et possède un précédent expérimental antérieur, mais n'est pas une instruction textuelle explicite.
4. Le binding `GP132 readout → mot R4 de GP132` est type-compatible et unique dans R4, mais reste une règle d'adressage à valider par réplication.
5. Aucun plaintext LP2 nouveau n'est obtenu.

## Verrou suivant et méthode de rupture

### Verrou fortement identifié
**EMIT / RUNE_TRANSFORM** : après un module READ/SELECT/REDUCE terminé par D33, quel objet consomme la sortie numérique et comment devient-elle nouvelle donnée/runique ?

### Méthode systématique
1. Geler la grammaire locale ci-dessus sans retouche.
2. Chercher un second module indépendamment borné possédant : `N sorties ordinaires → sélection par paramètre → arité imposée → readout GP → terminal D33`.
3. Prédire avant lecture la sortie GP et son destinataire par égalité de type, puis seulement ouvrir le corpus cible.
4. Comparer D33 à un modèle sans état : si D33 n'ajoute aucune décision/émission, le typer HALT seulement.
5. Pour DECRYPT, ne tester que des loci où un changement matériel impose `BYTE/GP → RUNE_STREAM`; rejeter toute conversion byte→rune non annoncée.
6. Cible prioritaire : trouver un locus où le résultat avant D33 possède **deux consumers matériellement possibles qui divergent** ; annoncer lequel est choisi par un cue externe (rouge, quote, cadre, dessin) puis vérifier. C'est le test qui peut transformer le contrôle local en véritable machine d'émission.

## Statut final de ce checkpoint
- `LOCAL_READ_G068_G070_G071`: **FORTEMENT SOUTENU / très contraint**
- `AND16_BINDING`: **FORT candidat**, dépendance F0 corrigé conservée
- `G032_REDUCE_16_TO_4`: **FORT local**
- `READOUT132_BIND_R4`: **FORT candidat**, unique dans R4 et red-team discriminant
- `150→144 / RED_CODA / 4|16`: **FORT raccord local**
- `D33=HALT_END`: **PROBABLE / structurellement fort**
- `D33=RETURN_EMIT`: **INCONCLUSIF**
- `DECRYPT_BYTE_TO_RUNES`: **NON TROUVÉ**
- `NEW_LP2_PLAINTEXT`: **AUCUN**

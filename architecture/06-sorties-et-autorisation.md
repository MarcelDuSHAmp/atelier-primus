# 06 · Sorties, identité et éventuelle autorisation

[Carte d’ensemble](README.md) · [Démonstration A/B](../PARCOURS_10_MIN.md) · [Audits A03–A05](SOURCES.md)

## Les branches de sortie

| Branche | Objet produit | Statut |
|---|---|---|
| SPECIAL + prélèvement G032 | A : `2h6vn7o256dtvsfp` ;80 bits `d1fd56fddaef873ac8af` | Calcul exact sous la recette ; identité historique inconnue |
| SPECIAL + dépôt G032 puis lignes | B : `hdnv2o26765tvsfp` ;80 bits `38db5d3b5effbb3ac8af` | Même niveau que A ; aucune priorité donnée ici |
| X16 de G054 |16 octets `0309263b6b02dbb9910846e8bc6516f8`, export historique `djg3lc3zrigi4fwy` | Branche conditionnelle conservée ; préfixe, représentation et rotation restent à justifier |
| G073 | Empreinte entière de 512 bits d’une page à rechercher | Instruction externe issue du texte résolu ; page cible non authentifiée |
| Sortie runique / image / programme | Objet attendu par certaines hypothèses | Aucun nouveau plaintext LP2, objet dormant ou microcode historique authentifié dans cette édition |

Les variantes de l’export SPECIAL sont déjà consignées dans [PISTE_ONION.md](../PISTE_ONION.md). Ajouter `.onion` interprète une forme de 80 bits ; cela ne prouve pas l’existence d’un service ni un lien Cicada.

## Ne pas confondre quatre tailles

| Taille | Objet envisagé | Point de contrôle |
|---|---|---|
|80 bits /10 octets | Identifiant v2 candidat | Une clé publique historique devrait recalculer exactement cet identifiant |
|128 bits /16 octets | Cookie d’autorisation candidat | Une taille compatible ne suffit pas à établir un rôle d’accès |
|160 bits /20 octets | Identifiant de descripteur ou autre objet de protocole | Résultat dépendant des paramètres ; pas automatiquement une donnée imprimée dans LP |
|512 bits /64 octets | Empreinte entière G073 | Ne pas tronquer en cookie ; vérifier le contenu et sa sérialisation |

## SPECIAL brut n’ajoute pas un second secret indépendant

Les 16 SPECIAL bruts contiennent128 bits de stockage, dont 48 bits constants. Le compact conserve toute l’information variable. Pour chaque caractère Base32 de rang n :

```python
special = ((n >> 2) << 5) | 28 | (n & 3)
```

Exemple : `2` a le rang26 et restitue222 (`0xDE`). Avec l’ordre connu, A ou B permet de reconstruire exactement les 16 octets correspondants, puis S0 en ordre physique. **Le modèle « compact=identité et même SPECIAL brut=secret indépendant » est falsifié.** Un éventuel cookie dérivable de l’adresse serait une autre hypothèse ; son emploi n’est pas établi.

La réversibilité est rejouée dans [resultats.json](resultats.json), séparément pour A et B. Les 12 lignes ASCII de 16 octets et le checksum historique hors LP ont aussi un format compatible, sans rôle AUTH démontré. X16 conserve ses choix de construction ; il n’est pas promu en secret par sa longueur.

## Le protocole Tor historique et l’hypothèse LP

Selon la [spécification historique Tor v2](https://torproject.gitlab.io/torspec/rend-spec-v2.html), BASIC et STEALTH sont distincts. En BASIC, le cookie protège l’accès aux introduction points et ne modifie pas l’identifiant de descripteur. En STEALTH, il intervient dans le calcul de cet identifiant et la protection des introductions ; le service utilise une identité propre au client. La clé privée correspondante reste côté service. Le client n’a pas besoin de cette clé privée pour calculer les identifiants si le hostname et le cookie sont connus.

Ce fonctionnement appartient au **Tor Project**. Notre question est de savoir si LP impose les bons objets et leur usage : cette liaison reste **INCONCLUSIVE**. Le scénario identité→secret→client key→ressource est une architecture testée, pas une succession d’instructions lues dans le livre.

## Audits d’autorisation et recherche historique

| Passe | Résultat documenté | Portée |
|---|---|---|
| AUTH LOCK A03 |17 suites /34 encodages ; aucun rôle d’accès identifié | Les variantes d’une suite ne sont pas des secrets indépendants |
| AUTH ARCHITECTURE A04 |319 témoins /638 allers-retours de format acceptés | Compatibilité générique de toute suite de 16 octets |
| AUTH SECRET A05 |309 témoins /618 encodages acceptés ;145 objets de recherche de clé sans parse réussi | Périmètre distinct ; ne pas additionner les campagnes comme des essais indépendants |
| Rejeu cryptographique A05 |4 fixtures,34 encodages et13040 IDs antérieurs reproduits | Valide les calculs conditionnels, pas le rôle de cookie ni l’existence A/B |
| Journaux d’archives antérieurs |61 jeux de données ;13040 IDs distincts,6520 par hostname ; zéro correspondance | Pas de nouveau scan dans cette carte ; absence bornée aux corpus et fenêtres |

Verdict des audits : **FORMAT MATCH ONLY**. Aucun secret d’accès indépendant ni clé client Tor n’est identifié dans leurs périmètres. Aucune preuve que Cicada ait employé BASIC ou STEALTH pour A/B. L’absence de correspondance ne prouve pas l’inexistence historique.

## Preuve extérieure recherchée

Une clé publique RSA ou un descripteur historique complet, de provenance indépendante, permettrait de vérifier l’identifiant, la signature et les paramètres. Une mention de l’adresse serait déjà une trace documentaire, mais d’un niveau différent. Même une identité Tor authentifiée demanderait encore un lien avec Cicada, puis éventuellement une page satisfaisant G073.

[Journaux AUTH distribués](../pieces/auth_v2/README.md) · [Recherche d’archives](../actualites/2026-10-22-auth.md) · [Famille SEEK/SHIFT](../recherches/09-seek-shift-et-objets-de-sortie.md)

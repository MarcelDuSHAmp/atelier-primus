# 08 · Sources, attribution et portée du rejeu

[Carte d’ensemble](README.md) · [Crédits généraux](../ATTRIBUTION.md) · [Catalogue public](../SOURCES.md)

Cette carte est une synthèse éditoriale des résultats disponibles au 22 octobre2026. Les cinq rapports ci-dessous ont été relus pour cet ajout ; leur date déclarée ne certifie pas une antériorité historique indépendante. Les empreintes identifient les fichiers effectivement consultés. Les rapports complets ne sont pas redistribués ici : ils comportent aussi des pièces embarquées et des annexes dont la portée doit rester attachée à leur édition.

## Cinq audits récents

| ID | Rapport source | Conclusion reprise |
|---|---|---|
| A01 | `LP_VM_AUDIT_20261022.html` | VM PLAUSIBLE ; NEXT, état persistant et retour non reconstruits. |
| A02 | `LP_TYPE_ROUTING_20261022.html` | Règle de voisinage A/B et contrat de cible falsifiés :0/3. |
| A03 | `ASTRA_AUTH_LOCK_AUDIT.html` | Compatibilité de format ; aucun rôle AUTH ni clé client identifié dans le périmètre. |
| A04 | `ASTRA_AUTH_ARCHITECTURE.html` | FORMAT MATCH ONLY ;319 témoins et638 encodages dans cette passe. |
| A05 | `RAPPORT_AUTH_SECRET_EXECUTION.html` | FORMAT MATCH ONLY ;309 témoins,618 encodages ;rejeu des 13040 IDs antérieurs. |

## Empreintes des sources consultées

- **A01** · SHA-256 `1ef9e287d8dddfadabdb37bcbd68496d16c01129f95f772de6b4b9da74e4d9d1` · 1880632 octets.
- **A02** · SHA-256 `bcadf04500648a7bfbf000e6543c80bd8a76c5e177e4acf5fd6264d162d1cae6` · 2549888 octets.
- **A03** · SHA-256 `a3419f07b2649e65a350185f3635c5c1ca209ee34c04a94e0c6591c8f9956320` · 30156 octets.
- **A04** · SHA-256 `16fa75b9e2542610f0d9e6a2a16ab1e59eecd29171d8c32a7dbadf6dc3aacbab` · 2611339 octets.
- **A05** · SHA-256 `256caaab94f75f61fa9b023c7ddf6ab6faff00c2566fbc32922ff0ca85c28ab9` · 446248 octets.

Le [catalogue JSON](audits.json) conserve ces identifiants et notices. Il ne prétend pas rendre accessibles les archives complètes. Les chiffres des audits non rejoués ici sont présentés comme résultats rapportés, et non comme nouvelle observation.

## Pièces publiques et ordre des corrections

| Pièce | Usage |
|---|---|
| [P01 · Chaîne de contrôle du 21 octobre](../pieces/LP_CHAINE_CONTROLE_FINALE_20261021.md) | Scénario de contrôle à conserver comme hypothèse, relu avec les corrections de A01/A02 |
| [P02 · Checkpoint READ du 21 octobre](../pieces/LP_READ_CHECKPOINT_20261021.md) | Composition AND16 et readout132 ; limites de version et de segmentation conservées |
| [Versions F0](../actualites/2026-10-22-f0.md) | Empreintes, six différences, totient et divergences de continuations |
| [Segmentation R4](../actualites/2026-10-21-segmentation.md) | Unités physiques/lexicales, fermeture exacte et transfert contredit |
| [Routage0/3](../actualites/2026-10-22-routage.md) | Contrat annoncé et trois cibles ordinaires |
| [Journaux AUTH](../pieces/auth_v2/README.md) | Scans historiques récupérés, paramètres et limites ; pas de nouveau scan dans cette carte |
| [171 fiches](../recherches/README.md) | Propositions, observations, essais et antériorités, regroupés dans12 familles |

Les phrases anciennes annonçant un contrôle « fortement identifié » restent des conclusions de leur rapport. La présente carte applique les corrections explicites récentes : elle ne les copie pas comme preuve d’une machine autonome. La comparaison directe des deux binaires distribués prime pour les résultats exactement rejoués ici.

## Ce qui est rejoué dans cet ajout

Le [script local](rejouer.py) vérifie les empreintes, les 512 identités HADDR/HINV, le totient230, les payloads D33/D34, BODY36 et ses36 sorties, les rangs AND16, les trois contre-exemples de routage, l’alternateur et la réversibilité des exports A/B. Les résultats sont dans [resultats.json](resultats.json).

**Comparaison explicite ajoutée à la carte :** sur la paire3b9b07d9/0201348c distribuée, les 16 rangs AND16 sont identiques, tandis que la somme modulo256 des 36 sorties G vaut33/4. C’est un contrôle des fichiers fournis, pas une nouvelle découverte attribuée à Cicada ni une revendication d’inédit mondial.

Ne sont pas rejoués par ce script : transcription indépendante des runes, contrôle visuel exhaustif, ablations80/70/512 des anciens rapports, MCMC lag-5, fixtures Tor/AES/RSA, scans des 61 corpus historiques. Les calculs R4 et G032 ont leurs propres scripts dans [REPRODUCTION.md](../REPRODUCTION.md).

## Qui doit être crédité ?

- **Cicada3301 et auteurs des œuvres incorporées** : pages, textes, dessins et énigme ; droits et provenance dans [DROITS.md](../DROITS.md).
- **Solveurs et archives communautaires** : solutions antérieures, transcriptions et recette G032. Les références disponibles sont dans [ATTRIBUTION.md](../ATTRIBUTION.md) ; auteur initial non établi quand la source ne le précise pas.
- **Tor Project** : protocole, code et mécanismes BASIC/STEALTH. [Spécification historique](https://torproject.gitlab.io/torspec/rend-spec-v2.html), notamment sections1.3 et2.
- **Travaux du projet et de ses agents** : propositions F0/D-bank/routage/architecture, expériences consignées et contre-épreuves, selon leurs rapports ; aucune priorité mondiale déduite de cette seule présence.
- **MarcelDuSHAmp · Collaboration IA : ASTRA GPT-6** : organisation de la carte publique, rapprochement des audits, rédaction pédagogique et contrôles explicitement rejoués pour cet ajout.

Les opérations générales AND, totient, Base32 et conversions de coordonnées ne sont pas nos inventions. Une proposition nouvelle dans le projet est distinguée d’une découverte validée et d’une antériorité mondiale. [Comment citer](../CITER.md).

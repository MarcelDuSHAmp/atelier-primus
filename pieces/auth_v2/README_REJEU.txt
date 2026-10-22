LP AUTH TOR V2 — audit hors ligne,22 octobre2026

Lire deliverables/ASTRA_LP_AUTH_TOR_V2.html : dix réponses, puis sections A–N.
Les résultats sont négatifs dans le périmètre décrit. Ne pas assimiler FORMAT
COMPATIBLE à une autorisation historique retrouvée.

Contenu : inventaire25 lignes/familles, quatre candidats gelés, huit encodages,
16 contacts A/B,13040 identifiants STEALTH, associations précises aux corpus,
61 journaux de scan, contrôles, code Tor historique et licence, code d'audit.

La majeure partie des données historiques avait déjà été livrée. Pour éviter
de la dupliquer, SOURCE_RECOVERY.json identifie les trois archives préalables
avec taille,SHA256 et lien de téléchargement de votre compte.

Rejeu complet depuis un répertoire propre (aucune connexion Tor nécessaire) :
1. Extraire ce ZIP dans un répertoire de travail.
2. Extraire ASTRA_DOSSIER_DEUX_PROMPTS.zip sous recovered/ASTRA_DOSSIER_DEUX_PROMPTS.
3. Extraire ASTRA_PHASE2_PREUVES.zip sous recovered/ASTRA_PHASE2_PREUVES.
4. Le petit corpus LP nécessaire est déjà inclus sous recovered/LP_INTERNAL,
   recovered/F0 et les autres dossiers LP ; aucune transcription nouvelle.
5. Python3 avec cryptography, compilateurs cc/c++,git sont nécessaires.
6. python3 auth_v2/build_authority.py
7. python3 auth_v2/compute.py
8. c++ -O3 -shared -fPIC auth_v2/matcher.cpp -o auth_v2/matcher.so
9. python3 auth_v2/scan.py small
10. python3 auth_v2/scan.py forums
11. python3 auth_v2/verify_scan.py

Les IDs de compute.py utilisent directement les fenêtres corrigées. Ne pas
rejouer refine_scope.py après ce calcul : ce fichier conserve seulement la
correction de la première exécution (16208 ->13040) documentée dans le rapport.
Les time stamps d'exécution et le hash de gel changent lors d'un nouveau rejeu ;
les cookies, encodages, identifiants et résultats restent déterministes.

Les binaires Tor/automate locaux ne sont pas nécessaires dans le ZIP : leur
source est incluse. Le codec historique est extrait sans modifier ses fonctions,
avec des adaptations libc uniquement. Le code des archives n'est jamais exécuté.
Les contrôles synthétiques ne sont jamais recherchés comme cookies candidats.

INVENTORY_SCOPE.json décrit les145 fichiers du recensement initial. Les pièces
MASK/CLOSE16 supplémentaires sont sous inventory_extra. L'inventaire ne prouve
pas l'absence d'autres objets dans tous les fichiers jamais créés pour LP.

L'archive n'inclut ni les propres prompts comme sources historiques, ni les
permissions de transfert, ni les helpers d'accès aux fichiers du compte.

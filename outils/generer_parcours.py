"""Figures pédagogiques calculées depuis F0 et les contrôles G032.

ATELIER PRIMUS — MarcelDuSHAmp. Collaboration IA : ASTRA GPT-6.
La recette G032 est communautaire ; voir ATTRIBUTION.md.
Bibliothèque standard uniquement. Les JPEG sources ne sont pas modifiés.
"""
from pathlib import Path
import base64
import hashlib
import html
import json

ROOT = Path(__file__).resolve().parent.parent
F0 = (ROOT / 'calculs/r4/F0-3b9b07d9.bin').read_bytes()
assert hashlib.sha256(F0).hexdigest() == '3b9b07d9a26e6d55c432d94d2661fdff3c2b348daed06821f2bdb23184a4b290'
S = [b for b in F0 if b & 31 >= 29]
P = [6, 7, 11, 10, 9, 5, 1, 2, 3, 4, 8, 12, 16, 15, 14, 13]
M = json.loads((ROOT / 'calculs/g032/results-attendus.json').read_text())['matrix']
A = [S[i - 1] for i in P]
B = [0] * 16
for k, case in enumerate(P):
    B[case - 1] = S[k]

def hostname(values):
    q = [4 * (b >> 5) + (b & 3) for b in values]
    raw = int(''.join(f'{v:05b}' for v in q), 2).to_bytes(10, 'big')
    return base64.b32encode(raw).decode().lower()

assert len(S) == 16
assert hostname(A) == '2h6vn7o256dtvsfp'
assert hostname(B) == 'hdnv2o26765tvsfp'
INK, MUTED, GREEN, GOLD, RED = '#213831', '#53665e', '#186450', '#e7be73', '#a62530'

def txt(x, y, text, size=18, color=INK, weight='normal', anchor='start'):
    return f'<text x="{x}" y="{y}" font-family="DejaVu Sans, sans-serif" font-size="{size}" fill="{color}" font-weight="{weight}" text-anchor="{anchor}">{html.escape(str(text))}</text>'

def rect(x, y, w, h, fill='#ffffff', stroke='#cbd4c8', radius=8):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{radius}" fill="{fill}" stroke="{stroke}"/>'

def save(name, w, h, title, description, items):
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">'
           f'<title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(description)}</desc>'
           + rect(0, 0, w, h, '#f4f2ec', '#f4f2ec', 0) + ''.join(items) + '</svg>\n')
    (ROOT / 'images' / name).write_text(svg)

# Les nombres imprimés, les numéros de case et les étapes restent distincts.
items = [txt(32, 44, 'G032 : un parcours de seize cases', 28, weight='bold'),
         txt(32, 76, 'Nombre central : valeur imprimée. Petit numéro : case comptée par lignes.', 17)]
for i, number in enumerate(M):
    x, y = 70 + (i % 4) * 160, 108 + (i // 4) * 126
    items += [rect(x, y, 148, 114), txt(x + 12, y + 23, f'case {i + 1}', 14, MUTED),
              txt(x + 74, y + 63, number, 28, RED if i == 5 else INK, 'bold', 'middle'),
              txt(x + 74, y + 94, f'étape {P.index(i + 1) + 1}', 15, GREEN, anchor='middle')]
items += [txt(32, 650, 'Départ rouge : case 6. Puis 7, 11, 10, 9, 5, 1, 2, 3, 4, 8, 12, 16, 15, 14, 13.', 17),
          txt(32, 681, 'Recette communautaire reproduite : Fibonacci → nombres premiers → distance à 3301.', 16, MUTED)]
save('parcours-g032.svg', 780, 710, 'Le parcours G032', 'Grille exacte avec numéro de case et rang de visite. La case 6, 3299 en rouge, est visitée en premier.', items)

# Les trois panneaux emploient exactement la même échelle et le même code couleur.
items = [txt(28, 42, 'Même parcours, deux gestes différents', 28, weight='bold'),
         txt(28, 75, 'Cases colorées et marquées • : low5 = 30. Les nombres affichés sont les octets.', 17)]
for panel, (title, values) in enumerate([('Entrée : les 16 SPECIAL', S), ('A : prélever suivant P', A), ('B : déposer suivant P', B)]):
    ox = 28 + panel * 360
    items.append(txt(ox, 119, title, 20, weight='bold'))
    for i, value in enumerate(values):
        x, y = ox + (i % 4) * 79, 142 + (i // 4) * 81
        marked = value & 31 == 30
        items += [rect(x, y, 73, 75, GOLD if marked else '#fff'),
                  txt(x + 8, y + 18, i + 1, 11, MUTED),
                  txt(x + 37, y + 49, str(value) + (' •' if marked else ''), 20, anchor='middle')]
    if panel == 0:
        items += [txt(ox, 500, 'Mise en carré de travail,', 17), txt(ox, 525, 'dans l’ordre des indices de F0.', 17)]
    else:
        items += [txt(ox, 500, 'Lire le résultat par lignes :', 17), txt(ox, 530, hostname(values), 19, GREEN, 'bold')]
items += [txt(28, 578, 'En B, les six cases marquées forment le T. En A, elles forment trois groupes séparés.', 18),
          txt(28, 608, 'B est appelé « ordre E » dans le tableau technique des variantes. Cette figure ne sélectionne pas un export.', 16, MUTED)]
save('parcours-deux-gestes.svg', 1100, 636, 'Prélèvement et dépôt comparés', 'Entrée physique, sortie A et grille B. Les six valeurs de classe 30 dessinent un T dans le dépôt B.', items)

items = [txt(32, 44, 'De huit bits à cinq bits : un exemple complet', 27, weight='bold'),
         txt(32, 82, '126 en binaire = 01111110. Les trois positions centrales 111 sont constantes.', 18)]
for i, bit in enumerate('01111110'):
    x = 38 + i * 94
    keep = i not in [3, 4, 5]
    items += [rect(x, 115, 80, 78, '#e2eee7' if keep else '#e5e3dd'),
              txt(x + 40, 165, bit, 34, GREEN if keep else MUTED, 'bold', 'middle')]
items += [txt(175, 220, 'hhh = 011', 19, GREEN, anchor='middle'),
          txt(457, 220, '111 : retirer', 19, MUTED, anchor='middle'),
          txt(692, 220, 'cc = 10', 19, GREEN, anchor='middle')]
for i, bit in enumerate('01110'):
    x = 178 + i * 94
    items += [rect(x, 260, 80, 78, '#e2eee7'), txt(x + 40, 310, bit, 34, GREEN, 'bold', 'middle')]
items += [txt(415, 379, '01110₂ = 14 → caractère Base32 « o »', 24, GREEN, 'bold', 'middle'),
          txt(32, 424, '16 groupes de 5 bits = 80 bits = 16 caractères Base32.', 20),
          txt(32, 460, 'hhhcc conserve l’ordre des bits restants ; cchhh est une variante conservée.', 17, MUTED),
          txt(32, 492, 'Le calcul est réversible sur les SPECIAL sélectionnés. Leur fonction reste une hypothèse.', 16, MUTED)]
save('parcours-cinq-bits.svg', 830, 520, 'Compression des positions constantes', 'Dans 01111110, on conserve les trois premiers et les deux derniers bits : 01110, soit 14, encodé o en Base32.', items)
print('Trois figures générées ; les deux sorties concordent avec les candidats publiés.')

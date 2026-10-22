"""Navigation et carte SVG de l'architecture documentaire, sans flux LP supposé."""
from pathlib import Path
from html import escape
import json
import re

ROOT=Path(__file__).resolve().parents[1]
BRANCHES=[
 ('01','Sources et grammaire','01-sources-et-grammaire.md',['75 JPEG · LP1 et LP2','G005 · G032 · leçons résolues','Dessins · rouge · M6 / PRE64']),
 ('02','Mémoire et objets','02-memoire-et-objets.md',['F0 : 256 octets · deux versions','high3 / low5 · 16 SPECIAL','D30 · D32 · D33 · D34 · D36 · D37']),
 ('03','Opérations et types','03-operations-et-types.md',['HADDR / HINV · lookup G','AND · totient · GP · G032','Type, portée et geste à expliciter']),
 ('04','Modules et parcours','04-modules-et-parcours.md',['G068 · R4 · BODY36 / BODY35','AND16 → 132 · BLOCK64 → 80','SEEK / SHIFT · rappels · STANDING']),
 ('05','Exécution et état','05-execution-et-verrous.md',['BOOT · PC · NEXT non reconstruits','CALL / RETURN · HALT hypothétiques','État persistant · APPLY / EMIT ouverts']),
 ('06','Sorties et autorisation','06-sorties-et-autorisation.md',['Deux candidats A/B · branche X16','80 / 128 / 160 / 512 bits','Identité, secret et lien Cicada inconnus']),
 ('07','Contre-épreuves','07-refutations-et-tests.md',['Routage 0/3 · alternateur · unités','Versions F0 · erreurs corrigées','ÉTAU · lag-5 · codecs · suites utiles']),
 ('08','Sources et crédits','SOURCES.md',['Cinq audits récents · pièces publiques','Calculs rejoués et résultats rapportés','Communauté · Tor Project · projet']),
]

def slug(s):
    return re.sub(r'[^\w\- ]','',s.lower()).replace(' ','-')

def main():
    chapters=[]
    for number,title,name,items in BRANCHES:
        p=ROOT/'architecture'/name
        sections=[{'title':s,'anchor':slug(s)} for s in re.findall(r'^## (.+)$',p.read_text(),re.M)]
        chapters.append({'id':'architecture-'+number,'number':number,'title':title,
                         'path':'architecture/'+name,'summary':items,'sections':sections})
    model={'title':'VM et architecture — carte du travail documenté','date':'2026-10-22',
           'scope':'Arborescence documentaire ; les branches ne sont pas des transitions de programme.',
           'chapters':chapters}
    (ROOT/'architecture/modele.json').write_text(json.dumps(model,ensure_ascii=False,indent=2)+'\n')
    out=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="1110" viewBox="0 0 1100 1110" role="img" aria-labelledby="title desc">',
         '<title id="title">VM et architecture — huit branches du dossier Atelier Primus</title>',
         '<desc id="desc">Sources, mémoire, opérations, modules, exécution, sorties, contre-épreuves et crédits. Les calculs locaux sont distincts de la VM autonome non reconstruite.</desc>',
         '<rect width="1100" height="1110" fill="#f4f2ec"/>',
         '<style>text{font-family:Arial,sans-serif;fill:#213831}.title{font-size:30px;font-weight:700}.sub{font-size:17px}.head{font-size:22px;font-weight:700}.line{font-size:17px}.num{font-size:15px;fill:#557665;font-weight:700}.foot{font-size:16px;fill:#56665d}</style>',
         '<text x="42" y="49" class="num">ATELIER PRIMUS · 22 OCTOBRE 2026</text>',
         '<text x="42" y="93" class="title">VM &amp; architecture : où se place chaque pièce ?</text>',
         '<text x="42" y="128" class="sub">Calculs locaux reproductibles · règles de continuation encore ouvertes</text>',
         '<rect x="320" y="164" width="460" height="62" rx="9" fill="#1f5c4e"/>',
         '<text x="550" y="202" text-anchor="middle" style="fill:#fff;font-size:22px;font-weight:700">LIBER PRIMUS · CARTE DE RECHERCHE</text>',
         '<path d="M550 226 V1000" fill="none" stroke="#a7b8aa" stroke-width="3"/>']
    for i,c in enumerate(chapters):
        x=42 if i%2==0 else 594
        y=266+(i//2)*184
        edge=x+464 if i%2==0 else x
        out.append(f'<path d="M550 {y+38} H{edge}" fill="none" stroke="#a7b8aa" stroke-width="3"/>')
        out.append(f'<rect x="{x}" y="{y}" width="464" height="158" rx="9" fill="#fff" stroke="#ccd8cd"/>')
        out.append(f'<text x="{x+20}" y="{y+32}" class="num">{c["number"]}</text>')
        out.append(f'<text x="{x+55}" y="{y+33}" class="head">{escape(c["title"])}</text>')
        for j,line in enumerate(c['summary']):
            out.append(f'<text x="{x+20}" y="{y+70+j*29}" class="line">{escape(line)}</text>')
    out.extend(['<rect x="42" y="1017" width="1016" height="61" rx="8" fill="#e5ece4"/>',
                '<text x="62" y="1042" class="foot">Les traits classent les dossiers ; ils ne démontrent pas un ordre d’exécution.</text>',
                '<text x="62" y="1066" class="foot">Chaque branche donne ses sources, ses résultats exacts, ses hypothèses et ses limites.</text>','</svg>'])
    svg='\n'.join(out)+'\n'
    styles={
      'title':'font-size="30" font-weight="700"',
      'sub':'font-size="17"',
      'head':'font-size="22" font-weight="700"',
      'line':'font-size="17"',
      'num':'font-size="15" font-weight="700" fill="#557665"',
      'foot':'font-size="16" fill="#56665d"',
    }
    for name,attrs in styles.items():
        svg=svg.replace('class="'+name+'"',attrs)
    svg=svg.replace('<text ','<text font-family="DejaVu Sans, Arial, sans-serif" ')
    (ROOT/'images/architecture-vm.svg').write_text(svg)
    print(f'Architecture : {len(chapters)} branches, {sum(len(c["sections"]) for c in chapters)} sous-sections ; modèle JSON et carte SVG générés.')

if __name__=='__main__':
    main()

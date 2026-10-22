"""Graphe documentaire typé, Markdown GitHub et explorateur HTML hors ligne.

Le JSON est la source éditoriale. Aucun arc n'est inféré des liens de citation.
Bibliothèque standard ; ne simule pas une VM de Liber Primus.
"""
from pathlib import Path
from collections import Counter
import html
import json
import re

ROOT=Path(__file__).resolve().parents[1]
E=html.escape

def load():
    data=json.loads((ROOT/'architecture/graphe-fonctionnel.json').read_text())
    ids={n['id'] for n in data['nodes']}
    assert len(ids)==len(data['nodes'])
    circuits={c['id'] for c in data['circuits']}
    assert len(circuits)==len(data['circuits'])
    for n in data['nodes']:
        assert n['circuit'] in circuits and all(n.get(k) for k in ('input','operation','output','limit','sources','verification'))
        assert n['verification'] in data['verification_levels']
    assert len({e['id'] for e in data['edges']})==len(data['edges'])
    for e in data['edges']:
        assert e['source'] in ids and e['target'] in ids and e['kind'] in data['statuses']
    for x in data['nodes']+data['edges']:
        assert x['sources'] and all(s in data['sources'] for s in x['sources'])
    reg=json.loads((ROOT/'donnees/registre-courant.json').read_text())
    assert set(data['coverage'])=={r['id'] for r in reg}
    for rid,targets in data['coverage'].items():
        assert targets and targets==[n['id'] for n in data['nodes'] if rid in n['sources']]
    for s in data['sources'].values():
        if not s['path'].startswith('https://'):
            assert (ROOT/'architecture'/s['path'].split('#')[0]).resolve().is_file(),s
    return data

def md_refs(d,refs):
    return ' · '.join(f"[{s}]({d['sources'][s]['path']})" for s in refs)

def cell(s):return s.replace('|',' / ').replace('\n',' ')

def write_markdown(d):
    ns={n['id']:n for n in d['nodes']}
    out=['# Arborescence fonctionnelle des recherches', '', '**'+d['credit']+'**', '',
         '[Accueil de l’architecture](README.md) · [Données du graphe](graphe-fonctionnel.json) · [Sources et limites du rejeu](SOURCES.md)', '',
         f"**{len(d['circuits'])} circuits · {len(ns)} objets ou fonctions · {len(d['edges'])} liaisons typées · 171 fiches rattachées.**", '',
         d['scope'], '',
         'Les flèches représentent les relations décrites dans les tables. Une flèche de calcul indique une composition définie sous nos paramètres, pas une instruction enseignée par le livre. Les choix de cible, de type, d’unité ou d’opération restent explicitement hypothétiques. Les circuits graphiques sont locaux ; leurs raccords extérieurs sont recensés juste après chaque schéma.', '',
         '![Vue des principaux raccords entre circuits](../images/architecture-fonctionnelle.svg)', '', '## Légende', '',
         '| Relation | Sens |', '|---|---|']
    for k,v in d['statuses'].items():out.append(f'| {k.upper()} | {v} |')
    out+=['', 'Les lignes pleines représentent données/calculs ; les pointillés les hypothèses, alternatives ou fonctions manquantes ; une croix termine les branches réfutées. Les liens de contexte sont sans flèche. Chaque liaison garde un identifiant E stable dans cette édition.', '',
          '**Rejeu :** « local » signale les calculs/fichiers couverts par les scripts distribués ; les interprétations et résultats historiques cités dans la même notice restent attribués à leurs rapports. « rapport » signifie qu’aucune nouvelle transcription ni campagne n’a été effectuée pour cette carte. Voir les limites détaillées de [SOURCES.md](SOURCES.md).', '',
          '## Accès aux circuits', '', '| Circuit | Fonction étudiée |', '|---|---|']
    for c in d['circuits']:out.append(f"| [{c['id']}](#{c['id'].lower()}) | {c['title']} — {c['purpose']} |")
    for c in d['circuits']:
        local=[n for n in d['nodes'] if n['circuit']==c['id']]
        ids={n['id'] for n in local}
        inside=[e for e in d['edges'] if e['source'] in ids and e['target'] in ids]
        outside=[e for e in d['edges'] if (e['source'] in ids) != (e['target'] in ids)]
        out+=['',f"## {c['id']}",'',f"**{c['title']}** — {c['purpose']}",'','```mermaid','flowchart TD']
        for n in local:out.append(f'  {n["id"]}["{n["id"]} · {n["title"]}"]')
        for e in inside:
            arrow='-->' if e['kind'] in ('calcul','donnee') else '--x' if e['kind']=='refute' else '---' if e['kind']=='contexte' else '-.->'
            out.append(f"  {e['source']} {arrow}|\"{e['id']} · {e['kind']}\"| {e['target']}")
        for i,e in enumerate(inside):
            color='#b54a3e' if e['kind']=='refute' else '#946220' if e['kind'] in ('hypothese','manquant','alternative') else '#316657' if e['kind'] in ('calcul','donnee') else '#758077'
            out.append(f'  linkStyle {i} stroke:{color}')
        out+=['```','','### Objets, opérations et limites','','| ID / objet | Entrée | Opération | Sortie | Limite et provenance |','|---|---|---|---|---|']
        for n in local:
            vals=[f"**{n['id']}** — {n['title']}",n['input'],n['operation'],n['output'],n['limit']+f" Niveau : {n['verification']}. "+md_refs(d,n['sources'])]
            out.append('| '+' | '.join(cell(v) for v in vals)+' |')
        for title,es in [('Liaisons internes',inside),('Raccords avec les autres circuits',outside)]:
            if not es:continue
            out+=['',f'### {title}','','| ID | De → vers | Relation | Contrat / limite | Source |','|---|---|---|---|---|']
            for e in es:
                ends=[]
                for key in ('source','target'):
                    n=ns[e[key]]; ends.append(f"{n['id']} ([{n['circuit']}](#{n['circuit'].lower()}))")
                out.append('| '+' | '.join([e['id'],' → '.join(ends),e['kind'].upper(),cell(e['label']),md_refs(d,e['sources'])])+' |')
    out+=['','## Couverture des 171 fiches','','Chaque fiche a au moins un rattachement. Un rattachement signifie « cette notice est prise en compte », pas « une fonction VM lui a été trouvée ». Les branches de contexte et de publication restent identifiées comme telles. Les zones absentes du registre et les archives privées ne deviennent pas couvertes par ce comptage.','','| Fiche | Notice | Objets / fonctions concernés |','|---|---|---|']
    for rid,targets in d['coverage'].items():
        src=d['sources'][rid]
        out.append(f"| [{rid}]({src['path']}) | {cell(src['title'])} | "+', '.join(f"{t} ([{ns[t]['circuit']}](#{ns[t]['circuit'].lower()}))" for t in targets)+' |')
    out+=['','## Attribution et portée','','Les matériaux de Cicada, œuvres incorporées, solutions et transcriptions communautaires, et le protocole Tor restent attribués à leurs auteurs. Notre apport ici est la formalisation du graphe, la confrontation des rapports et les contrôles indiqués. Les attributions propres aux171 fiches sont conservées intégralement dans le JSON et dans les fiches liées. Aucun titre de nœud ne revendique une priorité mondiale.','','Le graphe ne fournit pas BOOT, NEXT, STORE, CALL/RETURN ou EMIT manquants. Il décrit notre architecture de recherche et les mécanismes candidats ; il ne certifie pas une machine fonctionnelle complète de Liber Primus.','']
    (ROOT/'architecture/FONCTIONNELLE.md').write_text('\n'.join(out))

def overview(d):
    # Les arcs sont explicitement choisis et sourcés dans le graphe, pas inférés
    # d'un classement. Vue d'entrée ; toutes les liaisons sont dans le JSON/MD.
    pos={'C01':(515,145),'C07':(35,350),'C02':(515,350),'C06':(995,350),
         'C05':(35,555),'C03':(515,555),'C09':(995,555),
         'C04':(35,760),'C08':(515,760),'C10':(995,760),
         'C12':(515,965),'C11':(995,965)}
    desc={'C01':('Images · unités · GP · G032','Types BYTE / INDEX / sommes'),
          'C02':('256 octets · 16 SPECIAL','D30 / D32 / D33 / D34 / D36 / D37'),
          'C03':('63 →249 ; 158 →211','CAST, mode et NEXT à établir'),
          'C04':('BODY36 →35 sorties →16 rangs','G071 →132 ; BLOCK64 →230 →80'),
          'C05':('3 BODY16 →198 /254 /154','Trailers · TAIL14 · RESTORE156'),
          'C06':('G005 /G016 · préfixes · codas','Routes80 /245 /151 · STANDING'),
          'C07':('PRE64 · U1…U5 · cinq polarités','Marqueurs · miroirs · rappels'),
          'C08':('G068 →G072 →G071 →G070','→G069 →G068 ; sortie G073 proposée'),
          'C09':('Prélèvement ou dépôt →compact','A et B :80bits ; inverse exact'),
          'C10':('G054 →X16 →low5','Rotation6 ; G035/G026 négatifs'),
          'C11':('Identité · AUTH · archives','Preuve indépendante et hash G073'),
          'C12':('BOOT · SCOPE · STATE · RETURN','Cryptanalyse · ÉTAU · réfutations')}
    w,h=430,128
    s=['<svg xmlns="http://www.w3.org/2000/svg" width="1460" height="1190" viewBox="0 0 1460 1190" role="img" aria-labelledby="title desc">',
       '<title id="title">Architecture fonctionnelle : vue des principaux raccords</title>',
       '<desc id="desc">Douze circuits. Traits pleins : données ou calculs. Pointillés : hypothèses. La documentation et le JSON contiennent les138 liaisons, y compris les réfutations et mécanismes manquants.</desc>',
       '<defs><marker id="green" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#316657"/></marker><marker id="gold" markerWidth="9" markerHeight="9" refX="8" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#946220"/></marker></defs>',
       '<rect width="1460" height="1190" fill="#f4f2ec"/>',
       '<text x="35" y="53" font-family="Georgia,serif" font-size="34" fill="#213831">Des objets, des opérations et des raccords</text>',
       '<text x="35" y="91" font-family="sans-serif" font-size="20" fill="#52665b">12 circuits · 96 objets / fonctions · 138 liaisons détaillées · 171 fiches rattachées</text>']
    def line(path,kind,label,x,y):
        color='#316657' if kind=='calc' else '#946220'
        tokens=re.findall(r'[MHV]|\d+',path);points=[];i=0;px=py=0
        while i<len(tokens):
            cmd=tokens[i];i+=1
            if cmd=='M':px,py=map(float,tokens[i:i+2]);i+=2
            elif cmd=='H':px=float(tokens[i]);i+=1
            elif cmd=='V':py=float(tokens[i]);i+=1
            points.append((px,py))
        for (ax,ay),(bx,by) in zip(points,points[1:]):
            length=((bx-ax)**2+(by-ay)**2)**0.5;ux=(bx-ax)/length;uy=(by-ay)/length
            step=length+1 if kind=='calc' else 14
            at=0
            while at<length:
                end=length if kind=='calc' else min(at+8,length)
                s.append(f'<line x1="{ax+ux*at}" y1="{ay+uy*at}" x2="{ax+ux*end}" y2="{ay+uy*end}" stroke="{color}" stroke-width="2.3"/>')
                at+=step
        ax,ay=points[-2];bx,by=points[-1];length=((bx-ax)**2+(by-ay)**2)**0.5;ux=(bx-ax)/length;uy=(by-ay)/length
        s.append(f'<polygon points="{bx},{by} {bx-ux*10-uy*5},{by-uy*10+ux*5} {bx-ux*10+uy*5},{by-uy*10-ux*5}" fill="{color}"/>')
        if label:s.append(f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="16" fill="{color}">{E(label)}</text>')
    line('M730 273 V350','calc','F0',742,320)
    line('M515 209 H250 V350','hyp','configuration proposée',50,310)
    line('M945 209 H1210 V350','hyp','recettes multi-supports',1010,310)
    line('M730 478 V555','calc','HADDR / HINV / G',742,525)
    line('M945 414 H970 V515 H1210 V555','calc','16 SPECIAL',1040,505)
    line('M250 478 V555','hyp','états proposés',263,518)
    line('M250 683 V760','calc','bornes212..247',263,726)
    line('M515 619 H490 V700 H465 V792','hyp','CAST211',488,749)
    line('M465 824 H515','hyp','',0,0)
    line('M730 888 V965','hyp','NEXT / état / retour ?',744,938)
    line('M1425 619 H1441 V1029 H1425','hyp','',0,0)
    line('M1210 888 V965','hyp','rôle de cookie ?',1220,934)
    line('M945 824 H969 V1029 H995','hyp','',0,0)
    for c in d['circuits']:
        x,y=pos[c['id']]
        short={'C07':'M6, PRE64 et motifs','C11':'Identité, AUTH et preuve','C12':'Tests et fonctions manquantes'}.get(c['id'],c['title'])
        s.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="11" fill="#ffffff" stroke="#bccbbe"/>')
        s.append(f'<text x="{x+17}" y="{y+30}" font-family="sans-serif" font-size="19" font-weight="700" fill="#213831">{c["id"]} · {E(short)}</text>')
        for j,t in enumerate(desc[c['id']]):s.append(f'<text x="{x+17}" y="{y+64+j*28}" font-family="sans-serif" font-size="18" fill="#52665b">{E(t)}</text>')
    s+=['<text x="35" y="1135" font-family="sans-serif" font-size="18" fill="#316657">Trait plein : données / calculs sous paramètres déclarés.</text>',
        '<text x="35" y="1166" font-family="sans-serif" font-size="18" fill="#946220">Pointillé : interprétation ou transition proposée. Vue sélective : consulter les circuits pour toutes les liaisons.</text>','</svg>']
    (ROOT/'images/architecture-fonctionnelle.svg').write_text('\n'.join(s)+'\n')

def hub_html(d):
    """HTML intégré à INDEX.html ; tous les liens locaux sont relatifs à sa racine."""
    ns={n['id']:n for n in d['nodes']}
    def refs(items):
        result=[]
        for k in items:
            p=d['sources'][k]['path']
            target=p if p.startswith('https://') else 'architecture/'+p
            result.append('<a href="'+E(target,quote=True)+'">'+E(k)+'</a>')
        return ' · '.join(result)
    out=['<div id="functional-hub"><h2>Explorer les circuits fonctionnels</h2>',
         '<p>96 objets ou fonctions et138 liaisons typées. Chaque circuit expose ses entrées, opérations, sorties, limites et raccords. Les graphes détaillés se lisent aussi dans <a href="architecture/FONCTIONNELLE.md">FONCTIONNELLE.md</a> sur GitHub.</p>',
         '<label for="fn-search">Chercher un circuit, objet, opération ou source</label><input id="fn-search" type="search" placeholder="D34, BODY36, M6, RETURN, OUT-011…" style="width:100%;margin:12px 0">',
         '<div class="arch-controls"><button id="fn-expand">Déplier les circuits</button><button id="fn-collapse">Replier les circuits</button></div><p id="fn-count" aria-live="polite"></p>',
         '<p>CALCUL / DONNEE : relation définie, sans intention du livre présumée. HYPOTHESE / ALTERNATIVE : choix encore ouvert. REFUTE : règle contredite dans son périmètre. MANQUANT : fonction ou preuve absente. CONTEXTE : aucun flux d’exécution affirmé.</p>']
    for c in d['circuits']:
        local=[n for n in d['nodes'] if n['circuit']==c['id']]; ids={n['id'] for n in local}
        es=[e for e in d['edges'] if e['source'] in ids or e['target'] in ids]
        search=' '.join([c['title'],c['purpose']]+[json.dumps(n,ensure_ascii=False) for n in local]+[json.dumps(e,ensure_ascii=False) for e in es]).casefold()
        out.append(f'<details class="fn-circuit" id="fn-{c["id"]}" data-search="{E(search,quote=True)}"><summary><span class="id">{c["id"]}</span><strong>{E(c["title"])}</strong><span class="desc">{E(c["purpose"])} · {len(local)} objets / fonctions</span></summary><div class="arch-body">')
        for n in local:
            out.append(f'<details class="fn-node" id="fn-{n["id"]}"><summary><span class="id">{n["id"]}</span>{E(n["title"])}<span class="desc">{E(n["output"])}</span></summary><div class="arch-body"><dl>')
            for key,label in [('input','Entrée'),('operation','Opération'),('output','Sortie'),('limit','Limite')]:out.append('<dt><strong>'+label+'</strong></dt><dd>'+E(n[key])+'</dd>')
            out.append('</dl><p>Niveau de vérification : '+E(n['verification'])+'. '+refs(n['sources'])+'</p></div></details>')
        out.append('<h3>Liaisons internes et raccords extérieurs</h3><div class="table"><table><tr><th>ID / relation</th><th>De → vers</th><th>Contrat et limite</th></tr>')
        for e in es:
            ends=[]
            for key in ('source','target'):
                n=ns[e[key]]
                ends.append(f'<a href="#fn-{n["id"]}" data-fn-open="{n["id"]}">{n["id"]} ({n["circuit"]})</a>')
            out.append('<tr><td><strong>'+e['id']+'</strong><br>'+e['kind'].upper()+'</td><td>'+' → '.join(ends)+'</td><td>'+E(e['label'])+'<br>'+refs(e['sources'])+'</td></tr>')
        out.append('</table></div></div></details>')
    out.append('</div>')
    return ''.join(out)

HUB_JS='''const fnSearch=document.getElementById("fn-search"),fnCircuits=[...document.querySelectorAll(".fn-circuit")];function filterCircuits(){let count=0;for(const d of fnCircuits){d.hidden=!d.dataset.search.includes(fnSearch.value.toLocaleLowerCase());if(!d.hidden)count++;}document.getElementById("fn-count").textContent=count+" circuits affichés sur "+fnCircuits.length;}fnSearch.oninput=filterCircuits;filterCircuits();document.getElementById("fn-expand").onclick=()=>fnCircuits.filter(d=>!d.hidden).forEach(d=>d.open=true);document.getElementById("fn-collapse").onclick=()=>fnCircuits.forEach(d=>d.open=false);document.querySelectorAll("[data-fn-open]").forEach(a=>a.onclick=()=>{fnSearch.value="";filterCircuits();const n=document.getElementById("fn-"+a.dataset.fnOpen);n.open=true;n.closest(".fn-circuit").open=true;n.scrollIntoView({block:"start"});});'''

def main():
    d=load();write_markdown(d);overview(d)
    print(f"PASS : {len(d['circuits'])} circuits, {len(d['nodes'])} nœuds, {len(d['edges'])} liaisons, {len(d['coverage'])} fiches rattachées.")
    print('Relations :',dict(Counter(e['kind'] for e in d['edges'])))

if __name__=='__main__':main()

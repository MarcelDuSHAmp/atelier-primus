"""Lecteur hors ligne, génération depuis les documents du dépôt. Bibliothèque standard."""
from pathlib import Path
import html,json,os,re
ROOT=Path(__file__).resolve().parent.parent
E=html.escape
def md(text,prefix='',standalone=False):
 def inline(s):
  s=E(s)
  def link(m):
   title,target=m.groups()
   raw=html.unescape(target)
   if raw.startswith(('https://','http://')):return '<a href="'+E(raw,quote=True)+'">'+title+'</a>'
   if standalone:return title+' <small>['+target+']</small>'
   return '<a href="'+E(os.path.normpath(prefix+raw),quote=True)+'">'+title+'</a>'
  s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
  s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s);s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
  return s
 lines=text.splitlines();out=[];i=0
 while i<len(lines):
  line=lines[i]
  if not line.strip():i+=1;continue
  if line.startswith('```'):
   i+=1;block=[]
   while i<len(lines) and not lines[i].startswith('```'):block.append(lines[i]);i+=1
   out.append('<pre><code>'+E('\n'.join(block))+'</code></pre>');i+=1;continue
  if line.startswith('|'):
   rows=[]
   while i<len(lines) and lines[i].startswith('|'):
    if not re.fullmatch(r'[| :\-]+',lines[i]):rows.append([x.strip() for x in re.split(r'(?<!\\)\|',lines[i])[1:-1]])
    i+=1
   out.append('<div class="table"><table>'+''.join('<tr>'+''.join('<'+('th' if n==0 else 'td')+'>'+inline(v)+'</'+('th' if n==0 else 'td')+'>' for v in row)+'</tr>' for n,row in enumerate(rows))+'</table></div>');continue
  if line.startswith('#'):
   n=min(len(line)-len(line.lstrip('#'))+1,4);out.append(f'<h{n}>'+inline(line.lstrip('# '))+f'</h{n}>');i+=1;continue
  if line.startswith('- '):
   a=[]
   while i<len(lines) and lines[i].startswith('- '):a.append('<li>'+inline(lines[i][2:])+'</li>');i+=1
   out.append('<ul>'+''.join(a)+'</ul>');continue
  if line.startswith('!['):i+=1;continue
  a=[line];i+=1
  while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ','```','![')):
   a.append(lines[i]);i+=1
  out.append('<p>'+inline(' '.join(a))+'</p>')
 return ''.join(out)

CSS='''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f4f2ec;color:#213831;font:16px/1.65 system-ui,-apple-system,sans-serif}header,main{max-width:1180px;margin:auto;padding:34px 28px}header{padding-top:56px}h1{font:600 clamp(38px,6vw,72px)/1.06 Georgia,serif;letter-spacing:-2px;margin:15px 0 23px;max-width:820px}h2{font:600 29px/1.3 Georgia,serif;margin:27px 0 15px}h3{font-size:20px;margin:24px 0 12px}h4{font-size:17px;margin:20px 0 10px}p{max-width:960px}.kicker{font-size:12px;letter-spacing:2.5px;text-transform:uppercase;color:#576e62}.lead{font-size:21px;max-width:860px;line-height:1.5}.metrics{display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin:28px 0}.metric{border-top:2px solid #2e7365;padding:14px 0}.metric strong{font-size:32px;display:block}.metric span{font-size:13px;color:#596b62}.notice{background:#e5ece4;border-left:4px solid #557e5e;padding:16px 20px;margin:25px 0}.nav{display:flex;gap:9px;flex-wrap:wrap;border-bottom:1px solid #cbd4c8;padding-bottom:20px;margin:25px 0}button,select,input{font:inherit;border:1px solid #b7c6bb;border-radius:6px;background:#fff;color:#213831;padding:10px 14px}button{cursor:pointer}button.active{background:#1f5c4e;color:white;border-color:#1f5c4e}a{color:#116c5b;text-underline-offset:3px}section[hidden]{display:none}.filters{display:flex;gap:12px;margin:25px 0}.filters input{flex:1;min-width:0}details{background:#fff;border:1px solid #dbe1d6;border-radius:8px;margin:12px 0;overflow:hidden}summary{cursor:pointer;padding:18px 22px;list-style:none}summary::-webkit-details-marker{display:none}summary:before{content:'＋';float:right;margin-left:12px;color:#527868}details[open]>summary:before{content:'−'}.card-body{border-top:1px solid #e6e9e2;padding:6px 24px 24px}.id{font:600 12px/1.5 system-ui;letter-spacing:1px;color:#527868;margin-right:9px}.title{font-weight:650}.desc{font-size:14px;color:#52665b;display:block;margin-top:7px}.status{font-size:11px;color:#6e6151;margin-top:8px;display:block;letter-spacing:.5px}small{font-size:12px;color:#6c7b71;overflow-wrap:anywhere}code{background:#eff1ea;padding:2px 5px;border-radius:3px;font-size:13px;overflow-wrap:anywhere}pre{background:#ecf0e9;padding:18px;overflow:auto}pre code{white-space:pre}.table{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px;margin:18px 0}td,th{text-align:left;vertical-align:top;border-bottom:1px solid #d6dfd2;padding:13px 15px}th{background:#e9ede4}td{background:#fff}.atlas{display:grid;grid-template-columns:repeat(5,1fr);gap:16px}.page{background:#fff;padding:12px;border:1px solid #dae0d5;border-radius:7px}.page img{width:100%;height:210px;object-fit:contain;background:#eeeee6}.page strong{display:block;margin:8px 0 0}.fig{float:right;width:320px;margin:0 0 20px 28px;padding:14px;background:#fff;border-radius:8px}.fig img{width:100%}.fig figcaption{font-size:12px;line-height:1.5}.count{font-size:14px;color:#5d7063}footer{margin:40px 0 15px;border-top:1px solid #cbd4c8;padding-top:20px;font-size:13px;color:#637467}.clear{clear:both}@media(max-width:760px){header,main{padding:24px 18px}.metrics{grid-template-columns:repeat(2,1fr)}.atlas{grid-template-columns:repeat(2,1fr)}.filters{flex-direction:column}.fig{float:none;margin:20px 0;width:min(100%,360px)}h1{letter-spacing:-1px}.lead{font-size:18px}}'''

reg=json.loads((ROOT/'donnees/registre-courant.json').read_text())
families=json.loads((ROOT/'donnees/familles.json').read_text())
sections=[('accueil','Accueil','README.md'),('etat','État de la recherche','SYNTHESE.md'),('onion','La piste .onion','PISTE_ONION.md'),('fiches','171 fiches',None),('atlas','75 images',None),('credits','Crédits','ATTRIBUTION.md')]
out=['<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>ATELIER PRIMUS — Liber Primus</title><style>'+CSS+'</style></head><body><header><div class="kicker">MarcelDuSHAmp · Collaboration IA : ASTRA GPT-6</div><h1>ATELIER PRIMUS.<br>Liber Primus.</h1><p class="lead">Résultats, état de la recherche et piste d’export vers deux identifiants Tor candidats.</p><p>État du 22 octobre 2026 · édition v0.1.0</p><div class="notice"><strong>Calcul reproductible ; destination non authentifiée.</strong><br>Les sorties candidates et les variantes sont exposées avec leurs limites. Aucune nouvelle page LP2 déchiffrée n’est revendiquée.</div></header><main><nav class="nav" aria-label="Sections">']
for i,(sid,title,path) in enumerate(sections):
 out.append('<button data-view="'+sid+'"'+(' class="active"' if i==0 else '')+'>'+E(title)+'</button>')
out.append('</nav>')
for i,(sid,title,path) in enumerate(sections):
 out.append('<section id="'+sid+'"'+(' hidden' if i else '')+'>')
 if path:out.append(md((ROOT/path).read_text()))
 if sid=='onion':out.append('<h2>Les deux sources visuelles</h2><div class="atlas"><a class="page" href="images/G032.jpg"><img src="images/G032-recadrage.png" alt="Grille G032 et son nombre rouge"><strong>G032 — parcours</strong></a><a class="page" href="images/G073.jpg"><img src="images/G073.jpg" alt="Page G073"><strong>G073 — page à rechercher</strong></a></div>')
 if sid=='fiches':
  out.append('<h2>171 fiches attribuées</h2><p>Les anciens statuts sont conservés ; la synthèse et les corrections indiquent les conclusions actuelles.</p><div class="filters"><input id="search" placeholder="G032, lag-5, routage…" aria-label="Rechercher"><select id="family" aria-label="Famille"><option value="">Toutes les familles</option>'+''.join('<option value="'+f['id']+'">'+E(f['nom'])+'</option>' for f in families)+'</select></div><p id="count" class="count"></p>')
  for r in reg:
   search=E(' '.join(str(r.get(k,'')) for k in ['id','titre','en_clair','detail_technique','locus','attribution']).casefold(),quote=True)
   out.append('<details class="card" data-family="'+r['famille_id']+'" data-search="'+search+'"><summary><span class="id">'+r['id']+'</span><span class="title">'+E(r['titre'])+'</span><span class="desc">'+E(r['en_clair'])+'</span></summary><div class="card-body">'+md(r['texte_public'],str(Path(r['chemin_dossier']).parent)+'/')+'</div></details>')
 if sid=='atlas':
  out.append('<h2>Les 75 pages sources</h2><p>Documents Cicada 3301 et œuvres incorporées : voir les crédits. G026 a retrouvé son empreinte canonique par retrait du seul APP1 ajouté, sans réencodage. <a href="ATLAS.md">Provenance et empreintes</a>.</p><div class="atlas">')
  for n in range(75):
   g=f'G{n:03d}';out.append('<a class="page" href="images/'+g+'.jpg"><img loading="lazy" src="images/'+g+'.jpg" alt="Page '+g+'"><strong>'+g+'</strong><small>'+('LP1' if n<17 else 'LP2')+' · page locale '+str(n if n<17 else n-17)+'</small></a>')
  out.append('</div>')
 out.append('</section>')
out.append('<footer>MarcelDuSHAmp est un pseudonyme. Les recettes et matériaux antérieurs restent crédités à leurs sources. <a href="CITER.md">Citer cette édition</a>.</footer></main><script>document.querySelectorAll("[data-view]").forEach(b=>b.onclick=()=>{document.querySelectorAll("main>section").forEach(s=>s.hidden=s.id!==b.dataset.view);document.querySelectorAll("[data-view]").forEach(x=>x.classList.toggle("active",x===b));});const q=document.querySelector("#search"),f=document.querySelector("#family"),cards=[...document.querySelectorAll(".card")];function filter(){let n=0;cards.forEach(c=>{let ok=(!f.value||c.dataset.family===f.value)&&(!q.value||c.dataset.search.includes(q.value.toLocaleLowerCase()));c.hidden=!ok;if(ok)n++});document.querySelector("#count").textContent=n+" fiches affichées sur 171";}q.oninput=f.onchange=filter;filter();</script></body></html>')
(ROOT/'INDEX.html').write_text(''.join(out))
print('INDEX.html généré : 171 fiches, 75 images, six rubriques.')

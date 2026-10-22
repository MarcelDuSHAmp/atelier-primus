"""Vérifications bornées et hors réseau du dossier ; bibliothèque standard."""
from pathlib import Path
import hashlib,json,math,subprocess,sys
BASE=Path(__file__).resolve().parent; ROOT=BASE.parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
old=(BASE/'r4/F0-0201348c.bin').read_bytes()
new=(BASE/'r4/F0-3b9b07d9.bin').read_bytes()
assert len(old)==len(new)==256
assert hashlib.sha256(old).hexdigest()=='0201348c02d11222097b68be9ad0179a44020b46fe64a9e8e8198447c7b922e9'
assert hashlib.sha256(new).hexdigest()=='3b9b07d9a26e6d55c432d94d2661fdff3c2b348daed06821f2bdb23184a4b290'
diff=[[i,a,b] for i,(a,b) in enumerate(zip(old,new)) if a!=b]
assert diff==[[2,138,167],[45,78,107],[131,144,120],[182,138,167],[192,24,0],[199,18,47]]
haddr=lambda x:8*(x&31)+(x>>5)
phi230=sum(math.gcd(i,230)==1 for i in range(1,231))
assert phi230==88 and new[50]==47
assert (old[haddr(112)],new[haddr(112)])==(144,120)
sp=lambda f:[[i,x] for i,x in enumerate(f) if x&31>=29]
assert sp(old)==sp(new) and len(sp(new))==16
pages=json.loads((ROOT/'donnees/images-75.json').read_text())
assert len(pages)==75
for p in pages:assert digest(ROOT/p['fichier'])==p['sha256'],p['page']
g=json.loads(subprocess.run([sys.executable,str(BASE/'reproduire.py')],check=True,capture_output=True,text=True).stdout)
subprocess.run([sys.executable,str(BASE/'r4/rejouer.py')],check=True,capture_output=True,text=True)
a=json.loads((BASE/'r4/resultats-historiques.json').read_text());b=json.loads((BASE/'r4/resultats-rejoues.json').read_text())
a.pop('source_script');b.pop('source_script');assert a==b,'R4 différent du journal historique'
result={'status':'PASS','scope':'Arithmétique et intégrité ; pas nouvelle transcription, nouvelle découverte aveugle ni authentification historique.',
 'images_sha256_verified':len(pages),'f0_differences':diff,'specials_identical':len(sp(new)),
 'phi230':phi230,'G112_old_new':[old[haddr(112)],new[haddr(112)]],
 'g032_and_routing':g,'r4_archived_output_equal':True,'r4_exact_nulls_replayed':['N0','N1','N2'],
 'r4_lexical':b['observed']['R4_lexical_outputs'],'r4_physical':b['observed']['R4_physical_outputs'],
 'not_replayed':['R4 N3 and phase scan','lag5 MCMC','ASTRA large campaigns','Tor historical scans','all visual measurements']}
(BASE/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))

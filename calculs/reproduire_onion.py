"""Exports candidats reproductibles ; aucune connexion réseau.
ATELIER PRIMUS — MarcelDuSHAmp. Collaboration IA : ASTRA GPT-6.
Recette G032 communautaire : voir ATTRIBUTION.md. Export Tor hypothétique.
"""
from pathlib import Path
import base64, hashlib, json

ROOT=Path(__file__).resolve().parent
F=(ROOT/'r4/F0-3b9b07d9.bin').read_bytes()
assert hashlib.sha256(F).hexdigest()=='3b9b07d9a26e6d55c432d94d2661fdff3c2b348daed06821f2bdb23184a4b290'
S=[(i,b) for i,b in enumerate(F) if b&31>=29]
assert len(S)==16
P=[6,7,11,10,9,5,1,2,3,4,8,12,16,15,14,13]
I=[P.index(i)+1 for i in range(1,17)]
orders=dict(zip('ABCDEF',[P,P[::-1],list(range(1,17)),list(range(16,0,-1)),I,I[::-1]]))
expected={
'A':['2h6vn7o256dtvsfp','wzxnl7twpxy4nuj3'],
'B':['pfsvtd652o7nv6h2','3jun4yxpwt7lnxzw'],
'C':['o25672hdnv6tpfsv','twpx7wzylnx43jun'],
'D':['vsfpt6vndh27652o','nuj34xnlyzw7xpwt'],
'E':['hdnv2o26765tvsfp','zylnwtwx7xp4nuj3'],
'F':['pfsvt56762o2vndh','3jun4px7xwtwnlyz']}
rows=[]
for name,order in orders.items():
    vals=[S[i-1][1] for i in order]
    for j,coding in enumerate(['hhhcc','cchhh']):
        q=[4*(b>>5)+(b&3) if j==0 else 8*(b&3)+(b>>5) for b in vals]
        bits=''.join(format(x,'05b') for x in q)
        raw=int(bits,2).to_bytes(10,'big')
        host=base64.b32encode(raw).decode().lower()
        assert host==expected[name][j]
        assert base64.b32decode(host.upper())==raw
        restored=[((x>>2)<<5)|28|(x&3) if j==0 else ((x&7)<<5)|28|(x>>3) for x in q]
        assert restored==vals
        rows.append({'ordre':name,'codage':coding,'indices_elements_base1':order,'octets':vals,'quintets':q,'bits':bits,'raw80_hex':raw.hex(),'hostname':host,'adresse_candidate':host+'.onion','inverse_verifie':True})
result={'statut':'PASS — calcul conditionnel ; aucune authentification Tor','f0_sha256':hashlib.sha256(F).hexdigest(),'specials_index0_octet':S,'ordre_g032_base1':P,'variantes':rows}
(ROOT/'onion-resultats.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))

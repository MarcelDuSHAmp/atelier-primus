"""Reproductions bornées, sans réseau ; Python 3 standard library."""
from pathlib import Path
import hashlib, json, shutil, subprocess, sys, tempfile

ROOT = Path(__file__).resolve().parent
inp = json.loads((ROOT / 'g032/inputs.json').read_text())
F = bytes.fromhex(inp['f0_hex'])
assert len(F) == 256
assert hashlib.sha256(F).hexdigest() == inp['f0_sha256']
with tempfile.TemporaryDirectory() as td:
    t = Path(td)
    for name in ['audit_choices.py', 'inputs.json']:
        shutil.copyfile(ROOT/'g032'/name, t/name)
    subprocess.run([sys.executable, str(t/'audit_choices.py')], check=True, capture_output=True, text=True)
    actual = json.loads((t/'results.json').read_text())
expected = json.loads((ROOT/'g032/results-attendus.json').read_text())
assert actual == expected, 'Le journal G032 diffère du résultat archivé'

def haddr(v): return 8*(v&31)+(v>>5)
def hinv(v): return 32*(v&7)+(v>>3)
special = [i for i,b in enumerate(F) if b&31 >= 29]
def classify(i):
    k = special.index(i)
    prev = special[k-1] if k else None
    nxt = special[k+1] if k+1 < len(special) else None
    if prev == i-1 or nxt == i+1: return 'A'
    if nxt is not None and nxt-i-1 == 4: return 'B'
    return 'C'
def target_contract(i):
    return i in special and special.index(i)+1 < len(special) and special[special.index(i)+1]-i-1 > 0
anchors=[]
for i,fn,target in [(105,haddr,249),(249,hinv,211)]:
    assert fn(F[i]) == target and target_contract(target)
    anchors.append({'source':i,'value':F[i],'target':target})
tests=[]
for i,target,byte in [(6,207,21),(206,239,173),(106,248,113)]:
    cl = classify(i)
    fn = haddr if cl=='A' else hinv if cl=='B' else None
    assert fn is not None and fn(F[i]) == target and F[target] == byte
    assert not target_contract(target)
    tests.append({'source':i,'class':cl,'value':F[i],'target':target,'target_value':byte,'contract_success':False})
result={'f0_sha256':inp['f0_sha256'],'g032_archived_result_equal':True,
        'g032_orders':6,'serializations_per_order':2,'historical_controls':8,
        'anchors':anchors,'routing_tests':tests,'routing_successes':0,
        'limits':'Reproduction arithmétique ; pas de nouveau test aveugle ni authentification historique.'}
print(json.dumps(result, ensure_ascii=False, indent=2))

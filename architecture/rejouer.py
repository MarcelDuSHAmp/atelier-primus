"""Contrôles locaux de la carte d'architecture. Aucune exécution autonome LP.

Python 3, bibliothèque standard, hors réseau. Les assertions portent sur les
relations annoncées et leurs contre-exemples, pas sur l'intention de Cicada.
"""
from pathlib import Path
import base64
from functools import reduce
import hashlib
import json
from math import gcd
from operator import and_

ROOT = Path(__file__).resolve().parents[1]
ORDER = [6,7,11,10,9,5,1,2,3,4,8,12,16,15,14,13]
HASHES = {
    'F0-3b9b07d9.bin': '3b9b07d9a26e6d55c432d94d2661fdff3c2b348daed06821f2bdb23184a4b290',
    'F0-0201348c.bin': '0201348c02d11222097b68be9ad0179a44020b46fe64a9e8e8198447c7b922e9',
}

def haddr(b):
    return 8 * (b & 31) + (b >> 5)

def hinv(i):
    return ((i & 7) << 5) | (i >> 3)

def totient(n):
    return sum(gcd(k, n) == 1 for k in range(1, n + 1))

def inspect(f):
    g = lambda b: f[haddr(b)]
    positions = [i for i,b in enumerate(f) if b & 31 >= 29]
    special = [f[i] for i in positions]
    body = list(f[212:248])
    outputs = list(map(g, body))
    d33, d34 = list(f[7:11]), list(f[250:254])
    exports = {}
    order_a = [special[i-1] for i in ORDER]
    order_b = [None]*16
    for source,destination in enumerate(ORDER):
        order_b[destination-1] = special[source]
    alphabet = 'abcdefghijklmnopqrstuvwxyz234567'
    for name,values in [('A',order_a),('B',order_b)]:
        quints = [((b >> 5) << 2) | (b & 3) for b in values]
        hostname = ''.join(alphabet[q] for q in quints)
        restored = [((q >> 2) << 5) | 28 | (q & 3) for q in quints]
        assert restored == values
        exports[name] = {'hostname':hostname,'raw80':base64.b32decode(hostname.upper()).hex(),
                         'raw16':bytes(values).hex(),'inverse_exact':restored==values}
    assert exports['A']['hostname'] == '2h6vn7o256dtvsfp'
    assert exports['B']['hostname'] == 'hdnv2o26765tvsfp'
    assert d33 == [183,92,249,156] and d34 == [172,230,180,36]
    assert reduce(and_, d33) == 16 and reduce(and_, d34) == 36
    assert sum(body)==4551
    assert all(b & 31 < 29 for b in outputs[:-1]) and outputs[-1]==126
    assert [haddr(f[105]),hinv(f[249]),haddr(f[211])] == [249,211,233]
    assert f[totient(230)] == 211 and g(230)==80
    routing = [{'source':i,'operation':op,'target':fun(f[i]),
                'byte_at_target':f[fun(f[i])],
                'special_at_target':f[fun(f[i])]&31>=29}
               for i,op,fun in [(6,'HINV',hinv),(206,'HINV',hinv),(106,'HADDR',haddr)]]
    assert [r['target'] for r in routing]==[207,239,248]
    assert not any(r['special_at_target'] for r in routing)
    return {'sha256':hashlib.sha256(f).hexdigest(),'length':len(f),
        'special_positions_base0':positions,'special_values':special,
        'special_low5_counts':{str(k):sum(b&31==k for b in special) for k in (29,30,31)},
        'd_labels':[{'index':i,'byte':f[i],'high3':f[i]>>5,'low5':f[i]&31,
                     'label':'D'+str((f[i]>>5)+(f[i]&31))} for i in positions],
        'intervals_between_special':[b-a-1 for a,b in zip(positions,positions[1:])],
        'D33':{'interior':d33,'transformed':list(map(g,d33)),'sum_mod256':sum(d33)%256,
               'transformed_sum_mod256':sum(map(g,d33))%256,'and':reduce(and_,d33)},
        'D34':{'entry':f[249],'interior':d34,'and':reduce(and_,d34),
               'hinv_entry':hinv(f[249]),'totient230':totient(230),'F0_totient230':f[totient(230)]},
        'D30_BODY36':{'indices_inclusive':[212,247],'values':body,'sum':sum(body),
                     'sum_mod256':sum(body)%256,'G_outputs':outputs,'G_sum_mod256':sum(outputs)%256,
                     'and16_slots_base1':[i+1 for i,b in enumerate(outputs[:-1]) if b&16]},
        'alternating_next_trace':[105,249,211,233], 'routing_counterexamples':routing,
        'G112':g(112),'G230':g(230),'F0_87':f[87],'F0_172':f[172],
        'exports':exports}

def main():
    assert all(hinv(haddr(n))==n and haddr(hinv(n))==n for n in range(256))
    assert totient(230)==88 and totient(57)==36
    versions={}
    for name,expected in HASHES.items():
        f=(ROOT/'calculs/r4'/name).read_bytes()
        assert len(f)==256
        digest=hashlib.sha256(f).hexdigest()
        if expected is not None:
            assert digest==expected
        versions[name]=inspect(f)
    assert versions['F0-3b9b07d9.bin']['D30_BODY36']['G_sum_mod256']==33
    assert versions['F0-0201348c.bin']['D30_BODY36']['G_sum_mod256']==4
    a=(ROOT/'calculs/r4/F0-3b9b07d9.bin').read_bytes()
    b=(ROOT/'calculs/r4/F0-0201348c.bin').read_bytes()
    differences=[i for i,(x,y) in enumerate(zip(a,b)) if x!=y]
    assert differences==[2,45,131,182,192,199]
    report={'scope':'Local arithmetic only; no new rune transcription, archive scan or autonomous LP VM.',
            'indexing':'base 0; closed intervals in prose, half-open slices in Python',
            'inverse_coordinate_checks':512,'totient230':88,'different_indices':differences,
            'versions':versions}
    path=ROOT/'architecture/resultats.json'
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print('PASS : 2 versions F0, 512 contrôles inverses, cadres, routage, A/B et inverse SPECIAL.')
    print('Non rejoués ici : transcription runique, nuls statistiques et archives Tor historiques.')

if __name__=='__main__':
    main()

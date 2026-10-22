"""Audit borné : six ordres, deux sérialisations. Python 3 standard library.
Les comparaisons aux anciens résultats sont rétrospectives, pas aveugles.
"""
from pathlib import Path
import json, hashlib, base64, itertools, math

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'inputs.json').read_text())
F = bytes.fromhex(data['f0_hex'])
assert hashlib.sha256(F).hexdigest() == data['f0_sha256']
special = [(i, b) for i, b in enumerate(F) if (b & 31) >= 29]
S = [b for _, b in special]
matrix = [3258,3222,3152,3038,3278,3299,3298,2838,
          3288,3294,3296,2472,4516,1206,708,1820]
primes = []
for x in range(2, 10000):
    if all(x % p for p in primes if p*p <= x):
        primes.append(x)
fib = [0,1,2]
while len(fib) < 16:
    fib.append(fib[-1] + fib[-2])
derived = [abs(3301-primes[i]) for i in fib]
P = [matrix.index(v)+1 for v in derived]
assert P == [6,7,11,10,9,5,1,2,3,4,8,12,16,15,14,13]
I = [P.index(i)+1 for i in range(1,17)]
orders = dict(zip('ABCDEF', [P,P[::-1],list(range(1,17)),
                           list(range(16,0,-1)),I,I[::-1]]))
def compress(b): return 4*(b>>5)+(b&3)
def swap(b): return 8*(b&3)+(b>>5)
def uncompress(q): return ((q>>2)<<5)|28|(q&3)
def unswap(q): return ((q&7)<<5)|28|(q>>3)
domain = [b for b in range(256) if b&31 >= 29]
assert all(uncompress(compress(b)) == unswap(swap(b)) == b for b in domain)
assert all(swap(b) == ((compress(b)<<3)|(compress(b)>>2))&31 for b in domain)
def encode(vals):
    bits = ''.join(f'{v:05b}' for v in vals)
    raw = int(bits,2).to_bytes(10,'big')
    return {'bits':bits,'hex':raw.hex(),
            'base32':base64.b32encode(raw).decode().lower()}
def components(cells):
    remaining = set(cells)
    groups = []
    while remaining:
        start = remaining.pop(); stack=[start]; group={start}
        while stack:
            y,x = divmod(stack.pop(),4)
            for yy,xx in [(y-1,x),(y+1,x),(y,x-1),(y,x+1)]:
                n=4*yy+xx
                if 0<=yy<4 and 0<=xx<4 and n in remaining:
                    remaining.remove(n); stack.append(n); group.add(n)
        groups.append(sorted(group))
    return groups
out = {'special':special,'matrix':matrix,'fib':fib,
       'primes':[primes[i] for i in fib],'derived':derived,'orders':{}}
for label,o in orders.items():
    vals = [S[i-1] for i in o]
    cells = [i for i,v in enumerate(vals) if v&31==30]
    coords = [divmod(i-1,4) for i in o]
    lengths = [abs(y-Y)+abs(x-X) for (y,x),(Y,X) in zip(coords,coords[1:])]
    out['orders'][label] = {'order':o,'bytes':vals,
       'red_cell6':vals[5], 'class30_cells1':[i+1 for i in cells],
       'components30':components(cells),
       'route_if_used_as_read':{'start':o[0],'end':o[-1],
                              'adjacent_edges':lengths.count(1)},
       'hhhcc':encode([compress(v) for v in vals]),
       'cchhh':encode([swap(v) for v in vals])}
# Dépôt : les entrées chronologiques sont écrites le long de P.
placed = [None]*16
for b,i in zip(S,P): placed[i-1]=b
assert placed == out['orders']['E']['bytes']
out['T_core'] = [placed[i-1]>>5 for i in [6,7,10]]
out['T_leaves'] = [placed[i-1]>>5 for i in [5,8,14]]
assert out['T_core']==[3,6,7] and out['T_leaves']==[6,7,4]
# Toutes les transformations diédriques et translations du T documenté.
base = {(0,0),(0,1),(0,2),(0,3),(1,1),(2,1)}
shapes = set()
for reflection in [False,True]:
    for rotation in range(4):
        pts=[]
        for y,x in base:
            if reflection: x=-x
            for _ in range(rotation): y,x=x,-y
            pts.append((y,x))
        my=min(y for y,x in pts); mx=min(x for y,x in pts)
        pts={(y-my,x-mx) for y,x in pts}
        for dy in range(4-max(y for y,x in pts)):
            for dx in range(4-max(x for y,x in pts)):
                shapes.add(frozenset(4*(y+dy)+x+dx for y,x in pts))
success=0
for mask in itertools.combinations(range(16),6):
    m=set(mask)
    success += any(frozenset(k for k,i in enumerate(o) if i-1 in m) in shapes
                   for o in orders.values())
out['conditional_mask_count']={'T_placements':len(shapes),'total':math.comb(16,6),
                               'success_any_six_orders':success,
                               'discovery_pvalue':None}
ix={r:i for i,r in enumerate(data['runes'])}
expected={23:284,40:130,43:162,49:168,54:200,59:140,64:236,68:294}
controls={}
for g,groups in data['physical_groups'].items():
    controls[g]={'old_expected_sum':expected[int(g)],'variants':{}}
    for label,o in orders.items():
        cells=[o[i-1]-1 for i in [4,8,12,16]]
        r=[ix[groups[i][-1]] for i in cells]
        controls[g]['variants'][label]={'source_positions':[i+1 for i in cells],
              'sum':sum(data['gp'][i] for i in r),
              'literal':' '.join(data['latin'][i] for i in r)}
    assert controls[g]['variants']['A']['sum']==expected[int(g)]
out['controls']=controls
title_words=data['title32'].split('-')
out['title32']={'runes':data['title32'],
               'word_sums':[sum(data['gp'][ix[r]] for r in w) for w in title_words]}
out['title32']['total']=sum(out['title32']['word_sums'])
out['title32']['mod256']=out['title32']['total']%256
assert out['title32']['mod256']==126==S[0]==placed[5]
# Journal exploratoire : mêmes consultations sur chacun des deux mots et le total.
out['title_probes']=[]
for n in out['title32']['word_sums']+[out['title32']['total']]:
    x=n%256; h=8*(x&31)+(x>>5)
    out['title_probes'].append({'sum':n,'mod256':x,'raw_lookup':F[x],
                               'haddr':h,'haddr_lookup':F[h]})
ring='01101'
out['ring_readings']=sorted({s[i:]+s[:i] for s in [ring,ring[::-1]] for i in range(5)})
assert '11100' not in out['ring_readings'] and '00111' not in out['ring_readings']
out['bit_order']={'constant_positions_lsb0':[i for i in range(8)
                       if len({(b>>i)&1 for b in S})==1],
   'value_domain_size':len(domain),
   'numeric_inversions_hhhcc':sum(compress(a)>compress(b) for a,b in itertools.combinations(domain,2)),
   'numeric_inversions_cchhh':sum(swap(a)>swap(b) for a,b in itertools.combinations(domain,2))}
assert out['bit_order']['constant_positions_lsb0']==[2,3,4]
(ROOT/'results.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Rejeu terminé : six ordres, deux dispositions de bits, huit contrôles, T et titre.')

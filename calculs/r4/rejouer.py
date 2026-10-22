import ast, re, math, itertools, json, hashlib
from pathlib import Path
from collections import Counter

BASE=Path(__file__).resolve().parent
SCRIPT=BASE/'LP_SEGMENTATION_AUDIT_20261013.py'
mod=ast.parse(SCRIPT.read_text(encoding='utf-8'))
const={}
for node in mod.body:
    if isinstance(node,ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0],ast.Name):
        name=node.targets[0].id
        if name in {'G068','G069','G070_PREFIX','ALPHABET','PRIMES'}:
            const[name]=ast.literal_eval(node.value)
G068,G069,G070=const['G068'],const['G069'],const['G070_PREFIX']
ALPHABET=const['ALPHABET']; PRIMES=const['PRIMES']; GP=dict(zip(ALPHABET,PRIMES))
RUNIC=lambda c:0x16A0<=ord(c)<=0x16FF
def runes(s):return ''.join(c for c in s if RUNIC(c))
def groups(s,physical):
    s=re.sub(r'/\s*\n','|' if physical else '',s)
    s=''.join(c for c in s if RUNIC(c) or c in '-.|')
    return [runes(x) for x in re.split(r'[-.|]' if physical else r'[-.]',s) if runes(x)]
ordering=[6,7,11,10,9,5,1,2,3,4,8,12,16,15,14,13]
chosen=[ordering[i-1]-1 for i in [4,8,12,16]] # [9,1,11,12]

def readout(block):
    ends=[block[i][-1] for i in chosen]
    return sum(GP[x] for x in ends), ''.join(ends)

lex=groups(G069[2:].rstrip('/')+G070,False)
phy=groups(G069[2:]+'|'+G070,True)
g68p=groups(G068,True); g68l=groups(G068,False)
assert (len(lex),len(phy),len(g68p),len(g68l))==(86,101,23,20)
lex_bodies=[lex[j*24+1:j*24+17] for j in range(3)]
phy_bodies=[phy[j*24+1:j*24+17] for j in range(3)]
obs_lex=[readout(b)[0] for b in lex_bodies]
obs_phy=[readout(b)[0] for b in phy_bodies]
assert obs_lex==[198,254,154]
assert obs_phy==[272,195,288]
assert readout(g68p[:16])[1]=='ᚪᚾᛞᛝ'

# Current corrected F0 + convergence candidate
f0_files={}
for p in BASE.glob('F0-*.bin'):
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    if h.startswith('0201348c') or h.startswith('3b9b07d9') or h.startswith('cf860a1f'):
        f0_files[h[:8]]=p.read_bytes()
assert '0201348c' in f0_files and '3b9b07d9' in f0_files

def haddr(x):
    if not 0<=x<=255:return None
    return 8*(x&31)+(x>>5)
def special(x):return (x&31)>=29

def eval_pair_bc(f0,b,c):
    if not (0<=b<=255 and 0<=c<=255):
        return {'byte_bc':False}
    start,end=haddr(c),haddr(b)
    span=(end>=start and end-start+1==36)
    out={'byte_bc':True,'start':start,'end':end,'span36':span}
    if not span:return out
    vals=[f0[haddr(f0[i])] for i in range(start,end+1)]
    out['terminal_d33']=(vals[-1]==126)
    out['ordinary35_d33']=(all(not special(v) for v in vals[:-1]) and vals[-1]==126)
    out['required_a']=f0[end-1]
    return out

# Distribution builders return Counter(sum)-># equally likely elementary null states and denominator.
def free_shuffle_dist(body):
    # uniform permutation of 16 words, sum depends only on 4 words landing in chosen slots
    vals=[GP[w[-1]] for w in body]
    c=Counter(sum(vals[i] for i in comb) for comb in itertools.combinations(range(16),4))
    return c, math.comb(16,4)

def length_strat_dist(body):
    # independently permute words among equal-length slots; preserve exact length of every slot
    selected_lens=Counter(len(body[i]) for i in chosen)
    bylen={}
    for w in body:bylen.setdefault(len(w),[]).append(GP[w[-1]])
    per=[]
    den=1
    for L,k in sorted(selected_lens.items()):
        vals=bylen[L]
        assert len(vals)>=k
        cc=Counter(sum(vals[i] for i in comb) for comb in itertools.combinations(range(len(vals)),k))
        d=math.comb(len(vals),k); den*=d
        per.append((cc,d))
    dist=Counter({0:1})
    for cc,_ in per:
        nd=Counter()
        for a,ca in dist.items():
            for b,cb in cc.items(): nd[a+b]+=ca*cb
        dist=nd
    assert sum(dist.values())==den
    return dist,den

def cyclic_dist(body):
    c=Counter()
    n=len(body)
    for shift in range(n):
        rot=body[shift:]+body[:shift]
        c[readout(rot)[0]]+=1
    return c,n

def prob_range(dist,den,lo,hi):return sum(v for k,v in dist.items() if lo<=k<=hi)/den

def joint_metrics(dists,dens,f0):
    A,B,C=dists; da,db,dc=dens
    DEN=da*db*dc
    # tag match exact high3 vector 6,7,4
    tag_count=(sum(v for k,v in A.items() if 192<=k<=223)*
               sum(v for k,v in B.items() if 224<=k<=255)*
               sum(v for k,v in C.items() if 128<=k<=159))
    exact_count=A.get(198,0)*B.get(254,0)*C.get(154,0)
    span_count=0; sent_count=0; term_count=0; full36_count=0; fullchain_count=0
    startend=Counter()
    for b,cb in B.items():
      for c,cc in C.items():
        ev=eval_pair_bc(f0,b,c)
        if not ev.get('span36'): continue
        pairw=cb*cc
        span_count += pairw*da # any A
        req=ev['required_a']; ca=A.get(req,0)
        if ca:
          sent_count += pairw*ca
          if ev['terminal_d33']: term_count += pairw*ca
          if ev['ordinary35_d33']:
            full36_count += pairw*ca
            if (192<=req<=223 and 224<=b<=255 and 128<=c<=159):
              fullchain_count += pairw*ca
            startend[(ev['start'],ev['end'],req,b,c)]+=pairw*ca
    return {
      'denominator':DEN,
      'tag_674_count':tag_count,'tag_674_p':tag_count/DEN,
      'exact_198_254_154_count':exact_count,'exact_198_254_154_p':exact_count/DEN,
      'span36_count':span_count,'span36_p':span_count/DEN,
      'span36_plus_sentinel_count':sent_count,'span36_plus_sentinel_p':sent_count/DEN,
      'span36_sentinel_terminalD33_count':term_count,'span36_sentinel_terminalD33_p':term_count/DEN,
      'full_35ordinary_then_D33_count':full36_count,'full_35ordinary_then_D33_p':full36_count/DEN,
      'full_chain_tag674_plus_full36_count':fullchain_count,'full_chain_tag674_plus_full36_p':fullchain_count/DEN,
      'top_closures':[(list(k),v) for k,v in startend.most_common(10)]
    }

models={}
for name,builder in [('body_shuffle',free_shuffle_dist),('length_stratified',length_strat_dist),('cyclic_rotation',cyclic_dist)]:
    d=[]; dens=[]
    for body in lex_bodies:
        cc,den=builder(body);d.append(cc);dens.append(den)
    models[name]={'supports':[len(x) for x in d],'denominators':dens,'body_lengths':[[len(w) for w in b] for b in lex_bodies]}
    models[name]['f0']={h:joint_metrics(d,dens,f0) for h,f0 in f0_files.items() if h in ('0201348c','3b9b07d9')}

# observed chain evaluation under both F0s
obs_eval={}
for h,f0 in f0_files.items():
  if h not in ('0201348c','3b9b07d9'):continue
  A,B,C=obs_lex
  ev=eval_pair_bc(f0,B,C)
  vals=[]
  if ev.get('span36'):
      vals=[f0[haddr(f0[i])] for i in range(ev['start'],ev['end']+1)]
  obs_eval[h]={
    'lexical_outputs':obs_lex,
    'high3':[x>>5 for x in obs_lex],
    'haddr':[haddr(x) for x in obs_lex],
    'frame':ev,
    'sentinel_match': ev.get('required_a')==A if ev.get('span36') else False,
    'first35_ordinary':all(not special(v) for v in vals[:-1]) if vals else False,
    'last_output':vals[-1] if vals else None,
    'output_special_positions':[i+1 for i,v in enumerate(vals) if special(v)],
  }

out={
 'source_script':SCRIPT.name,
 'fixed_reader':{'ordering':ordering,'selected_body_positions_1based':[i+1 for i in chosen],'calls_1based':[1,25,49]},
 'observed':{
   'G068_physical':{'groups':len(g68p),'readout_latin':readout(g68p[:16])[1],'gp_sum':readout(g68p[:16])[0]},
   'G068_lexical':{'words':len(g68l),'readout_latin':readout(g68l[:16])[1],'gp_sum':readout(g68l[:16])[0]},
   'R4_lexical_outputs':obs_lex,
   'R4_physical_outputs':obs_phy,
   'same_unit_transfer_survives':obs_phy==obs_lex,
   'note':'G068 training object is physical groups; invariant transfer to R4 physical groups yields 272/195/288, not 198/254/154.'
 },
 'observed_chain':obs_eval,
 'null_models':models,
 'interpretation':{
   'body_shuffle':'calls and BODY16/TRAILER boundaries fixed; each BODY16 word kept intact; uniform permutation inside each BODY16.',
   'length_stratified':'same, but words only permute among slots of equal rune length; exact length at every body slot preserved.',
   'cyclic_rotation':'same BODY16 circularly rotated; internal cyclic adjacency preserved, only phase broken.'
 }
}
(BASE/'resultats-rejoues.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))

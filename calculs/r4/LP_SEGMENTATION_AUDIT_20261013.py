#!/usr/bin/env python3
"""Reproduction autonome, basée sur la transcription publique rtkd/iddqd (2017).
Ce contrôle distingue GROUPES PHYSIQUES (retour de ligne = frontière) et
MOTS LEXICAUX (retour de ligne sans trait d'union = continuation).
Les chiffres et la géométrie des originaux JPEG restent des sources distinctes.
"""
import json, re, csv, io
from pathlib import Path

G068 = '''ᚹᚹᛈ-ᚠᛡᛚᛉᛒᚾ-ᚳᛗᚾᚱᛗ-ᚻᚦᚫᛞᛄ-ᛒᛡᚫ-ᛇᚹ/
ᛗᚢ-ᚪᛈᛡ-ᛈᛁᛄ-ᚪᚢᚾᛠᛖᛞᛗᚪ-ᛏᛟᛗ-ᛋᛞ/
ᛝᚷᛚᛋᛞᛝ-ᛟ-ᛋᛄᛞ-ᛚᛟᚠᛄᚫᚠᚪ-ᛝᛟᚣᛈ-ᚣᚩ/
ᛒᚷᚳᛖᛏᚹ-ᚪᛋᛒ-ᛗᛠᚣᛇᛗᚫᛚᚱ-ᚹᛇᛄᛒ-ᛈᛚᚠ/'''

G069 = '''ᛈ-ᚠᛗ-ᛝᚪᛇᚾᛟᚹᛇᛉ-ᚣᚫᛉᛞᛟᚱᛒ-ᛡᚱᛟ-ᚹᛏ/
ᚷᚱᛄᛖ-ᛠ-ᛈᛚᛞ-ᚻᚦᚱ-ᚦᚣᛚᛉ-ᛠᛈᚫᚠᚪ-ᚫᚪ/
ᛒ-ᛈᛋ-ᛗ-ᛏᚫᚳᛈᛝᚹᚦ-ᚻᛠ-ᛞᚩᛄᚷ-ᛋᚩᛠᚳ/
ᛖᛋ-ᚣᛖᚫ-ᛈᚦ-ᛁᛇᛈᚳᛝ.ᛈᚳᛇᚢᛏᚳᛡᛇᛝᚾ/
ᚢᚻᚦ-ᚣᚠᛗᚾ-ᛝᚠᛄᛉᛟᚱᛗ-ᛝᛠᛄᛏᚳ-ᚢᚷ/
ᚦ-ᚠᚦᛋ-ᚪᛈᚩᚪᚫᛞᛋᛝ-ᛒᛗᚩᚷ-ᚹᚠᛗᛖ-ᛠᛇᚻᚠ/
ᚻᚳᚱᚫ-ᛝᛗᛉᚳ-ᛋᚪᚹᛋᛠ-ᚩᚣᛚᛉᛝ-ᛠᛟᛉ/
ᛟᛠᛡᛝᛒ-ᛝᚳᚫᛁᚱ.ᛒᚠ-ᛏᚣᚣ-ᛠᛒ-ᚣᛚᚩ-ᛇ/
ᛉ-ᚩᚷᛗᚩ-ᚠᛚᛟᛝᚦᛠ-ᚦᚣᛖᚣ-ᚾᚷᚾ.ᛡᛏ-ᛄ/
ᛟᚾᛁ-ᛋᛟ-ᛠᚦᚣ-ᛋᛒ-ᚫᛚᚪᛄᛡᛖᚷᛉᛡᚾᛉᛏ-/
ᛡᛒᚻᛚᚷ-ᚢᚦᛠ-ᚢᚾᛁᚩᛗᛠᛁᚷ-ᛟᚦᚱᚣ-ᛒᛖ/
ᛠᚩᛈ-ᛗᛏᚱᚫᚢᚻᛁᛝ-ᛇᚳᚠ-ᛄᚾᚱᚷ-ᛟᚷᚻᚣᚻ/'''

# Préfixe de G070, arrête à la rune 128 après "ᛞᛗᛖ".
G070_PREFIX = '''ᛇᚫᛠᚫᚣ-ᚢᛗᛈ-ᛉᛁᚢᚾᚩᛟᚾ-ᚷᛞᚦ-ᛡᚫᚹ-ᛞ/
ᛟᛖᚱ-ᛗᚾᛖᚻᚷᛒᚢᛄ-ᚢᚦᛗᛖᛞᛝ-ᛒᚷᚣᚱ-ᛖ/
ᛁᚢᛄ-ᚣᛡᛚᚢ-ᛄᛟ.ᛠᛉᚣᛇᚱ-ᚩᛈᛋᚳᚫᛗ/
ᛇ-ᚾᛄ-ᛖᚠᛋ-ᛖᚠᚪᛝ-ᚢᛝᛄᛇᚷᚠᛝᚱᛁᚦ-ᛄᚢᚫ-/
ᚣᛋᚠᛖᚢᛋᚫᚣᛠ-ᛁᛏᛟᚱᛏᛟᚩ-ᚷᚾᚻ-ᛞᛗᚩᚳ/
ᛞᛖᛏ-ᚹᛉᛞᛚ-ᚩᚫᛄ-ᛇᚢᛒ-ᛗᛏ-ᛞᛗᛖ.'''

RUNIC = lambda c: 0x16A0 <= ord(c) <= 0x16FF
ALPHABET = 'ᚠᚢᚦᚩᚱᚳᚷᚹᚻᚾᛁᛄᛇᛈᛉᛋᛏᛒᛖᛗᛚᛝᛟᛞᚪᚫᚣᛡᛠ'
PRIMES = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109]
GP = dict(zip(ALPHABET, PRIMES))
assert len(GP)==29

def runes(s): return ''.join(c for c in s if RUNIC(c))
def groups(s, physical):
    s = re.sub(r'/\s*\n', '|' if physical else '', s)
    s = ''.join(c for c in s if RUNIC(c) or c in '-.|')
    return [runes(x) for x in re.split(r'[-.|]' if physical else r'[-.]', s) if runes(x)]

def readout(gs, start):
    # G032 spiral order extracted from G032_spatial_path.csv, 1-based.
    ordering=[6,7,11,10,9,5,1,2,3,4,8,12,16,15,14,13]
    # 4e, 8e, 12e, 16e groupes réordonnés (bord droit du carré 4×4).
    chosen=[ordering[i-1]-1 for i in [4,8,12,16]]
    block=gs[start:start+16]
    end=[block[i][-1] for i in chosen]
    return {'endpoints':end, 'gp_sum':sum(GP[c] for c in end)}

assert len(runes(G069))==263, len(runes(G069))
assert len(runes(G070_PREFIX))==128, len(runes(G070_PREFIX))
assert len(runes(G069))+len(runes(G070_PREFIX))-1 == 390
# Première rune G069 est hors de R4 ; aucun séparateur de page pour le mode lexical.
lexical=groups(G069[2:].rstrip('/') + G070_PREFIX,False)
physical=groups(G069[2:] + '|' + G070_PREFIX,True)
assert len(lexical)==86, len(lexical)
assert len(physical)==101, len(physical)
assert [lexical[i] for i in [0,24,48]]==['ᚠᛗ','ᚢᚷᚦ','ᛋᛒ']
g68physical=groups(G068,True)
g68lexical=groups(G068,False)
assert len(g68physical)==23 and len(g68lexical)==20
assert readout(g68physical,0)['endpoints']==list('ᚪᚾᛞᛝ')
assert readout(g68lexical,0)['endpoints']==list('ᛗᚾᛟᛞ')
lexical_out=[readout(lexical,j*24+1) for j in range(3)]
physical_out=[readout(physical,j*24+1) for j in range(3)]
assert [x['gp_sum'] for x in lexical_out]==[198,254,154]
assert [x['gp_sum'] for x in physical_out]==[272,195,288]

out={
    'source':'rtkd/iddqd, liber-primus__transcription--master.txt, archive 2017',
    'G068':{'physical_groups':23,'physical_readout':readout(g68physical,0),
            'lexical_words':20,'lexical_readout':readout(g68lexical,0)},
    'R4_G069_r2_G070_r128':{
        'runes':390,'lexical_words':86,'physical_groups':101,
        'lexical_calls':[lexical[i] for i in (0,24,48)],
        'lexical_readouts':lexical_out,
        'physical_24slot_calls':[physical[i] for i in (0,24,48)],
        'physical_24slot_readouts':physical_out,
    },
    'conclusion':'Le lecteur ANDING emploie des groupes physiques en G068, mais les sorties 198/254/154 exigent les mots lexicaux en R4. Le transfert de type n’est pas démontré par ces calculs.'
}
path=Path('/mnt/data/LP_SEGMENTATION_RESULTAT_20261013.json')
path.write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(out,ensure_ascii=False,indent=2))

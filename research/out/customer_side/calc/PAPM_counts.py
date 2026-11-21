#!/usr/bin/env python3
"""Count PAPM_table.csv rows by chipmaker x method and chipmaker x process step (module PAPM).
Usage: python3 -I research/out/customer_side/calc/PAPM_counts.py"""
import csv, os, re
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
rows = list(csv.DictReader(open(os.path.join(ROOT, 'research/out/customer_side/parts/PAPM_table.csv'), encoding='utf-8')))
def co(r):
    c = r['chipmaker']
    return ('Micron' if c.startswith('Micron') else 'Samsung' if c.startswith('Samsung') else 'SK hynix') + (' [SPIE]' if r['doi'].startswith('10.1117') else '')
def meth(r):
    return r['method'] if not r['method'].startswith('other') else 'other'
HBMBOND = ('TSV / micro-bump', 'post-bond voids', 'pre-bond surface', 'bond overlay', 'wafer shape')
def grp(r):
    s, d = r['process_step'], r['process_step'].lower()
    if s in HBMBOND or re.search(r'hbm|bond|w2w|stack|\bpackages?\b', d):
        return 'HBM / stacking / bonding'
    return 'memory film, CD, defect, FA'
print('rows', len(rows), 'papers', len({r['doi'] for r in rows}))
print('papers by company:', dict(Counter(co(r) for r in {r['doi']: r for r in rows}.values())))
for g in ('HBM / stacking / bonding', 'memory film, CD, defect, FA'):
    sub = [r for r in rows if grp(r) == g]
    print(f'\n[{g}] rows={len(sub)} papers={len({r["doi"] for r in sub})}')
    for (c, m), n in sorted(Counter((co(r), meth(r)) for r in sub).items()):
        print(f'  {c:16s} {m:22s} {n}')
print('\nrows naming a tool vendor:', sum(not r['tool_vendor'].startswith('NOT DISCLOSED') for r in rows))
print('rows with status NOT DISCLOSED:', sum(r['status_in_authors_words'].startswith('NOT DISCLOSED') for r in rows))
print('rows with limits NOT DISCLOSED:', sum(r['limits_stated'].startswith('NOT DISCLOSED') for r in rows))
print('X-ray rows:', sum(r['method'].startswith('X-ray') for r in rows), '| AFM rows:', sum(r['method'] == 'AFM' for r in rows), '| infrared rows:', sum(r['method'] == 'infrared' for r in rows))

"""Harmonise tags across parts after the completeness critic (2026-11-21).
Rule applied: technical description of what a tool measures, read on a company page = [F];
adoption, positioning, 'required', 'selected/ordered by unnamed customers', capability-in-a-node claims = [C];
company release read only in a third-party reprint = [S]."""
import csv, glob, os
P = 'research/out/bruker_semi/parts'
TAG = {'R056': '[F]', 'R058': '[F]', 'P033': '[C]', 'H007': '[F]', 'P022': '[C]', 'R068': '[S]',
       'P039': '[C]', 'P045': '[C]'}
CLAIM = {'S017': 'Advanced-packaging order: one semiconductor manufacturer ordered 27 Bruker optical metrology systems for 2025 (release reports the 15th InSight WLI shipped)',
         'G032': 'Q2 FY2026 10-Q MD&A: BSI NANO revenue "remained consistent" YoY in the quarter'}
NOTE_ADD = {'S062': 'Superseded: Q3 FY2026 10-Q retrieved later from a mirror; see G rows on the Q3 interim test.',
            'S064': 'Superseded by [F] G rows from the Q3 FY2026 10-Q (BSB&CA unit).',
            'S065': 'Superseded by [F] G rows from the Q3 FY2026 10-Q (BSB&CA unit).',
            'P025': 'Product unnamed; no wafer-fab TXRF on semiconductor pages (see R072). Likely refers to lab TXRF from Bruker AXS [I, Low].',
            'R068': 'Tag set to [S]: company release read only in a BioSpace reprint (same document as P009).'}
for f in glob.glob(os.path.join(P, '*.csv')):
    rows = list(csv.DictReader(open(f, encoding='utf-8')))
    if not rows: continue
    cols = list(rows[0].keys()); changed = 0
    for r in rows:
        i = r['id']
        if i in TAG and r['tag'] != TAG[i]: print(f'{i}: {r["tag"]} -> {TAG[i]}'); r['tag'] = TAG[i]; changed += 1
        if i in CLAIM: r['claim'] = CLAIM[i]; changed += 1
        if i in NOTE_ADD and NOTE_ADD[i] not in r['note']: r['note'] = (r['note'] + ' | ' + NOTE_ADD[i]).strip(' |'); changed += 1
    if changed:
        w = csv.DictWriter(open(f, 'w', newline='', encoding='utf-8'), fieldnames=cols); w.writeheader(); w.writerows(rows)

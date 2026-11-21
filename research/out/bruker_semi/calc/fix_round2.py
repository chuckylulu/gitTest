"""Second-review fixes (2026-11-21): wording, tags, periods, missing-data forms, new [I] rows V007-V008."""
import csv, glob, os, re
P = 'research/out/bruker_semi/parts'
COLS = ["id","tag","claim","value","unit","period_fiscal","period_calendar","document","date","page_or_section","url","local_file","quote","confidence","note"]
SET = {
 'R007': dict(note="Release text says 'billion yen' after a full yen figure (drafting error in source)."),
 'R069': dict(note="Inputs: MTP p11 Fig.14 (R042) and yuho FY2025 p25 chart (R043); values read from charts, no arithmetic, no script. Confidence Medium. Reason: one year of mix shift only; weakens any claim that Rigaku is memory-only."),
 'H037': dict(tag='[F]', note="'hybrid bond' string count in saved release = 0. Re-tagged [F]: content of a company release."),
 'G001': dict(note="Mirror (us.kabutan.jp) of SEC filing; sec.gov refuses scripts. Signed 2026-11-05. Matches S056 (release)."),
 'M006': dict(claim="Rigaku-cited Yole figures across three editions: 2022 26.9%, 2023 29.5% (Q2-24 ed.) / 30% (Q4-24 ed.), 2024 38% (Q4-25 ed.). Implied 2023 revenue, same Q4-24 edition ($470m market): Rigaku ~$141m, 'Company A' ~$113m; Q2-24 edition: Rigaku ~$142m. 2024 (Q4-25 ed.): Rigaku ~$189m", value="141 (Q4-24 ed.); 142 (Q2-24 ed.); 189; Company A 113", period_fiscal="CY2023; CY2024", period_calendar="Jan-Dec 2023; Jan-Dec 2024"),
 'S021': dict(claim="CEO, Q3 2025 call: semi orders 'flattish this year' (two strong, two weak order quarters); revenue 'a little weaker'"),
 'V003': dict(claim="Q3 2026 call: analyst (Citi) asked whether semi is ~$300M at year-end 2026 with mid-to-high single digit growth and 30% EBIT, translating into a mid-teens grower of ~$400M in 2027; CEO: no 2027 guidance, 'I think the direction is correct'", note="Analyst numbers, not Bruker figures. The CEO's remark answered the combined FY2026/FY2027 question; he said he could not reproduce the math and that the business 'would accelerate in revenue growth next year'. Not an acceptance of a specific FY2026 growth rate."),
 'C005': dict(note="Who: Kioxia (named). Vendor: Rigaku. Tool: XTRAIA MF-3400. Measurement: film thickness/composition (incl. Mo). Vendor claim about a named customer; no Kioxia-side statement found. Extends R038 ('adopted by major memory player'). DRAM and logic makers only 'expected to adopt', unnamed."),
 'V005': dict(claim="Cumulative recapture of the analyst-cited $40M Q4-25 pushout expected by end Q3-26 per CFO ('similar amount in Q2 and Q3'): $30-45M (75-112%) if read per quarter; $20-30M (50-75%) if read as Q2+Q3 combined", value="50-112", note="Expectation, not a reported outcome; $40M is the analyst figure; both readings computed in calc/semi_mix_calc.py."),
 'P028': dict(period_fiscal='Q4 FY2010', period_calendar='Oct 2010'),
}
new = [
 dict(id='V007', tag='[I]', claim="AI/HPC-related share of FY2024 semi metrology revenue ~50% ('north of $125 million' of 'north of $250 million'; CEO 'maybe half')", value='~50', unit='% of semi metrology revenue', period_fiscal='FY2024', period_calendar='Jan-Dec 2024', document='calc/semi_mix_calc.py', page_or_section='inputs G050, G051', confidence='Low', note="Reason: both inputs are lower bounds from a transcript [S]; ratio indicative only."),
 dict(id='V008', tag='[I]', claim="Production QA/QC share of semi metrology run-rate ~67% (~$200M of ~$300M); R&D ~17%, mask repair ~17%", value='~67; ~17; ~17', unit='% of semi metrology run-rate', period_fiscal='annual run-rate as stated 2026-06-04 (period NOT DISCLOSED (read: Jefferies transcript, semiconductors section))', period_calendar='n/a (run-rate)', document='calc/semi_mix_calc.py', page_or_section='inputs G060-G063', confidence='Low', note="Reason: approximate CFO figures from a transcript [S]."),
]
for r in new:
    for c in COLS: r.setdefault(c, '')

def norm_missing(text, doc, sec):
    t = text
    t = t.replace('NOT DISCLOSED, read:', 'NOT DISCLOSED (read:')
    t = re.sub(r'NOT DISCLOSED \((?!read:)', 'NOT DISCLOSED (read: ', t)
    t = re.sub(r'NOT DISCLOSED(?! \()', f'NOT DISCLOSED (read: {doc}, {sec})'.replace('(read: , )', '(read: cited document)'), t)
    t = re.sub(r'NOT RETRIEVED \((?!tried:)', 'NOT RETRIEVED (tried: ', t)
    t = re.sub(r'NOT RETRIEVED(?! \()', 'NOT RETRIEVED (tried: see gaps.md)', t)
    return t

changed = 0
for f in glob.glob(os.path.join(P, '*.csv')):
    rows = list(csv.DictReader(open(f, encoding='utf-8')))
    if not rows: continue
    for r in rows:
        before = dict(r)
        if r['id'] in SET: r.update(SET[r['id']])
        for fld in ('claim', 'value', 'note', 'page_or_section', 'period_fiscal'):
            r[fld] = norm_missing(r[fld], r['document'][:60], r['page_or_section'][:40] or 'whole document')
        if r['value'].strip() and r['tag'] != '[I]' and not r['period_calendar'].strip():
            r['period_calendar'] = f"as of {r['date']}" if r['date'] else 'undated'
        if r['value'].strip() and not r['period_fiscal'].strip():
            r['period_fiscal'] = 'n/a (point-in-time statement)'
        if r != before: changed += 1
    if f.endswith('V.csv'):
        ids = {r['id'] for r in rows}
        rows += [r for r in new if r['id'] not in ids]
    w = csv.DictWriter(open(f, 'w', newline='', encoding='utf-8'), fieldnames=COLS); w.writeheader(); w.writerows(rows)
print('rows changed:', changed)

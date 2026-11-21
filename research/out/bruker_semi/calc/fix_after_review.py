"""Apply evidence fixes from the adversarial review and self-check (2026-11-21).
Adds rows V001-V006 (parts/V.csv) and edits tags/periods/notes in other parts."""
import csv, glob, os
P = 'research/out/bruker_semi/parts'
COLS = ["id","tag","claim","value","unit","period_fiscal","period_calendar","document","date","page_or_section","url","local_file","quote","confidence","note"]
T3 = 'research/sources/bruker_semi/2026-11-04_fool-transcript_earnings-call-transcript-2026Q3.html'
U3 = 'https://www.fool.com/earnings/call-transcripts/2026/11/04/bruker-brkr-q3-2026-earnings-call-transcript/'
new = [
 dict(id='V001', tag='[S]', claim='CEO in Q&A, Q3 2026 call: semi bookings up more than 30% year to date (resolves the "year to date ... in the quarter" wording of S045)', value='>30', unit='% yoy bookings (organic per S045)', period_fiscal='9M FY2026', period_calendar='Jan-Sep 2026', document='Q3 2026 earnings call transcript (Motley Fool)', date='2026-11-04', page_or_section='Q&A (Laukien reply on BSI book-to-bill)', url=U3, local_file=T3, quote='semi bookings have been just very strong year to date, greater than 30%.', confidence='Medium', note='Management on Q3 2026 call, per fool.com transcript. Same transcript as S045.'),
 dict(id='V002', tag='[S]', claim='CFO, Q3 2026 call: BSI segment order book up low single digits organically in Q3, driven partly by strong growth in semi (BSI-wide figure, not semi)', value='low single-digit', unit='% yoy organic orders (BSI)', period_fiscal='Q3 FY2026', period_calendar='Jul-Sep 2026', document='Q3 2026 earnings call transcript (Motley Fool)', date='2026-11-04', page_or_section='Prepared remarks (Herman)', url=U3, local_file=T3, quote='Our BSI segment order book performance was up organically in the low single-digit percentage year over year', confidence='Medium', note='BSI-level. Continues with "driven by strong growth in semi" (S049).'),
 dict(id='V003', tag='[S]', claim='Q3 2026 call: analyst (Citi) framed semi as ~$300M by year-end 2026, mid-to-high single digit growth, 30% EBIT; CEO: "I think the direction is correct"', value='direction correct', unit='text', period_fiscal='FY2026 (outlook)', period_calendar='Jan-Dec 2026', document='Q3 2026 earnings call transcript (Motley Fool)', date='2026-11-04', page_or_section='Q&A (Albert Hu, Citi; Laukien)', url=U3, local_file=T3, quote='but I think the direction is correct.', confidence='Low', note='Analyst numbers, not Bruker figures. Implies FY2026 semi growth above the low-single-digit guide of S027/S034; CEO also said he could not reproduce the math. Analyst words: "$300 million to end the year, mid to high single digit growth, 30% EBIT margins".'),
 dict(id='V004', tag='[F]', claim='SEMICON West 2027 dates and venue (moves to spring, Phoenix)', value='2027-03-30 to 2027-04-01', unit='date', period_fiscal='n/a', period_calendar='Mar-Apr 2027', document='SEMI press release (PR Newswire APAC copy)', date='2026-07-30', page_or_section='body para 1', url='https://en.prnasia.com/releases/apac/semi-announces-new-spring-schedule-for-semicon-west-beginning-march-30-april-1-2027-542504.shtml', local_file='research/sources/bruker_semi/2026-07-30_semi-via-prnasia_press-release-semicon-west-2027-dates.html', quote='establishing a new annual spring schedule beginning March 30–April 1, 2027, at the Phoenix Convention Center in Phoenix, Arizona.', confidence='High', note='Issuer release distributed by PR Newswire; semi.org original returned 403.'),
 dict(id='V005', tag='[I]', claim='Cumulative recapture of the analyst-cited $40M Q4-25 pushout expected by end Q3-26 per CFO: Q1 $10-15M plus "similar amount in Q2 and Q3" = $30-45M (75-112%)', value='75-112', unit='% of $40M', period_fiscal='Q1-Q3 FY2026', period_calendar='Jan-Sep 2026', document='calc/semi_mix_calc.py', date='', page_or_section='inputs G064, S033', url='', local_file='', quote='', confidence='Low', note='Expectation, not a reported outcome; $40M is the analyst figure; "similar amount" read as $10-15M per quarter.'),
 dict(id='V006', tag='[I]', claim='Bruker 2026 X-ray lineup: no CD-SAXS, wafer-fab TXRF or packaging X-ray imaging tool is listed on the product pages/brochure read 2026-11-21 (absence is from listed pages only)', value='not listed', unit='text', period_fiscal='n/a', period_calendar='as of 2026-11-21', document='R053-R055, P notes, Q013', date='2026-11-21', page_or_section='', url='', local_file='', quote='', confidence='Medium', note='Same finding as R072; Bruker could sell unlisted tools; an XCD tool was shown at FCMN 2022 (R051).'),
]
with open(os.path.join(P, 'V.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=COLS); w.writeheader(); w.writerows(new)

RUNRATE = ('annual run-rate as stated 2026-06-04 (period NOT DISCLOSED)', 'n/a (run-rate)')
EDIT = {
 'S017': dict(tag='[C]'), 'P043': dict(tag='[C]'), 'P044': dict(tag='[C]'),
 'G060': dict(period_fiscal=RUNRATE[0], period_calendar=RUNRATE[1]),
 'G061': dict(period_fiscal=RUNRATE[0], period_calendar=RUNRATE[1]),
 'G062': dict(period_fiscal=RUNRATE[0], period_calendar=RUNRATE[1]),
 'G063': dict(period_fiscal=RUNRATE[0], period_calendar=RUNRATE[1]),
 'S031': dict(period_fiscal='annual run-rate as stated 2026-05-06 (period NOT DISCLOSED)', period_calendar='n/a (run-rate)'),
 'H063': dict(period_calendar='Jul 2024-Jun 2025'),
 'G081': dict(confidence='Medium'),
}
NOTE = {
 'S017': 'Re-tagged [C] after review: order by an unnamed customer (same rule as P022/R061).',
 'P043': 'Re-tagged [C] after review: unnamed customer.', 'P044': 'Re-tagged [C] after review: unnamed customer.',
 'G081': 'Review: Oxford Instruments (same 10-K list) makes the Asylum Vero AFM used on Intel hybrid-bonding samples (H013) and holds 14.3% of AFM (M014), so it is also semi-relevant; confidence lowered to Medium.',
 'M006': 'Review: Company A implied 2023 revenue recomputed with the same-edition $470M market (R013) in M_calc.py: ~$113M.',
 'S045': 'Q&A wording without the ambiguity: V001.',
}
for f in glob.glob(os.path.join(P, '*.csv')):
    if f.endswith('V.csv'): continue
    rows = list(csv.DictReader(open(f, encoding='utf-8'))); ch = 0
    for r in rows:
        if r['id'] in EDIT: r.update(EDIT[r['id']]); ch += 1
        if r['id'] in NOTE and NOTE[r['id']] not in r['note']: r['note'] = (r['note'] + ' | ' + NOTE[r['id']]).strip(' |'); ch += 1
    if ch:
        w = csv.DictWriter(open(f, 'w', newline='', encoding='utf-8'), fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print('done')

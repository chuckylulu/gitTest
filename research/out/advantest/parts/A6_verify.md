# A6 verification log (adversarial re-check, 2026-11-21)

Scope: `parts/A6.csv`, `parts/A6.md`, `parts/A6_gaps.md`, `calc/A6_*.py` and their outputs. Rules applied: research/CLAUDE.md (tags, columns, missing-data forms, arithmetic in calc/, one-offs shown with and without, verdict words only in [I]).

## Counts

| | n |
|---|---|
| Rows in file before | 313 (237 [F], 26 [C], 6 [S], 44 [I]) |
| Rows checked | 313. All 269 [F]/[C]/[S] rows were re-opened on the cited page: 92 cumulative page-1 rows and 90 quarterly-table rows by a column-position script, the rest one by one. All 44 [I] values were compared with the re-run script output. |
| OK (unchanged) | 172 |
| Fixed | 141. 3 value changes, 1 scope/period error, 22 notes or input lists, 4 dated-event labels, 111 label-only changes for the period convention and calendar-year form. |
| Removed | 0 |
| Added | 41 (A6-314 to A6-354: 34 [F], 7 [I]) |
| Rows in file after | 354 (271 [F], 26 [C], 6 [S], 51 [I]) |
| row_check before / after | 0 flags / 0 flags. The 0 before was a blind spot: labels such as "FY2015 Q2 YTD" match none of the tool's period patterns, so they were never checked. One VERDICT flag on a note I wrote (A6-214) was fixed. |
| quote_check after | 303 FOUND on the cited page, 0 NOT FOUND, 0 flags (51 [I] rows carry no quote). One new quote over 25 words (A6-316) was shortened. |

The row_check_v1.csv that the orchestrator produced has no A6 lines, so there were no mechanical flags to resolve. The lint was re-run on parts/A6.csv directly.

## Material findings

1. **Missed one-off in the 2018-19 trough quarter (handoff value changed).** A6.md and A6-292 said no item was named for FY2018 Q4. The FY2018 Q&A summary (printed 2019-04-25, p.1) says: "We recorded an inventory valuation loss of approximately 2 billion yen in 4Q." Added A6-314. I applied the same treatment the first pass gave the ~3 bn FY2022 Q4 inventory loss. The 2018-19 margin change without named one-offs is now 24.3% -> 19.1%, -5.2 pp (was -8.4 pp). The T4Q margin change without one-offs is now -0.8 pp (was -1.5 pp). The FY2018 margin without one-offs is now 22.4% (was 21.7%). The pension-only variant (-8.4 pp) is kept as A6-351. The FY2019 Q1 Q&A names further inventory losses without an amount (A6-315, logged as NOT DISCLOSED).
2. **Inventory valuation losses recur every year.** The annual securities reports give the annual totals (A6-317 to A6-322): FY2018 6,324, FY2019 3,468 (from a newly saved FY2019 annual financial report), FY2020 3,307, FY2021 2,728, FY2022 6,344, FY2023 7,347. The trough year FY2023 had the largest total, but management named no quarterly amount for it. The ex-one-off margins therefore depend on what management chose to name (A6-353). A6.md now shows both variants.
3. **Accounting basis.** The first pass wrote "IFRS from FY2014". Corrected: IFRS was adopted with the FY2015 annual securities report, with a transition date of 1 Apr 2014 (A6-329, A6-330). FY2014 exists under IFRS only as a comparative. The quarterly series is IFRS-only. The FY2015 quarters come from IFRS comparatives in the FY2016 releases, which state that they are IFRS (A6-329). No U.S. GAAP quarter enters the series. A new `calc/A6_basis_check.py` measures the size of the gap: IFRS net sales are 0.2-0.4% below U.S. GAAP, and the Q2->Q3 FY2015 drop is -35.3% on IFRS and -35.4% on U.S. GAAP (A6-348). On U.S. GAAP alone, T4Q sales peaked in FY2015 Q2 (Oct 2014-Sep 2015), before the first IFRS T4Q value, so the IFRS -6.6% for 2015-16 is a lower bound (A6-349). Two further breaks inside the 2018-19 window were not mentioned before: IFRS 15 from FY2018 Q1 and IFRS 16 from FY2019 Q1, both adopted without restating prior years (A6-331 to A6-333). The size of their effect is NOT DISCLOSED.
4. **The downturn selection is fragile.** The T4Q depths are 2015-16 -6.55%, 2018-19 -5.17% and 2022-23 -13.15%. The first pass's sentence "any threshold from 1% to 5.2% picks the same three" is right but incomplete: any threshold above 5.17% drops 2018-19, and the last two downturns then become 2022-23 and 2015-16. 2018-19 clears the 5% rule by 0.17 pp (A6-350, new section 9 of A6_cycle.out.txt).
5. **Period labels.** 74 rows used "FYxxxx Qn YTD" and "Apr 2015-Jun 2015"-style labels. They were relabelled to the convention: Q1 / 1H / 9M with "Apr-Jun 2015", "Apr-Sep 2015" and "Apr-Dec 2015". The 18 calendar-year market rows and 3 [I] rows now use "n/a (calendar year)" / "CY2018". The three management outlook statements are now dated events (e.g. "FY2019 Q1" / "Apr-Jun 2019 (25 Apr 2019)"). A6-313 claimed coverage "FY2016 Q1-FY2025 Q4", but the 32 pairs it compares run from FY2016 Q4 to FY2025 1H, and its note named the wrong script.
6. **Stale notes.** 16 notes still said the file names carried PDF-metadata dates. The files have since been renamed to their printed dates. A6.md also said the FY2021 Q4 release had no manifest row, but it now has one. Both were corrected.
7. **Incomplete input lists in [I] notes.** For example, A6-301 omitted A6-001 and A6-003, A6-294 omitted A6-021, and A6-284 omitted the sales ids. Rewritten in the "inputs: ...; script: ...; reason: ..." form.

## Non-OK rows

| id | what was checked | before | after | result |
|---|---|---|---|---|
| A6-292 | 2018-19 margin ex named one-offs | 24.3 -> 15.9 (-8.4 pp), High; "none named for FY2018 Q4" | 24.3 -> 19.1 (-5.2 pp), Medium; adds back ~2 bn FY2018 Q4 inventory loss (A6-314) | FIXED |
| A6-295 | 2018-19 T4Q margin ex one-offs | ex 22.6 -> 21.1 (-1.5 pp) | ex 22.6 -> 21.8 (-0.8 pp) | FIXED |
| A6-303 | FY2018 -> FY2019 margin ex one-offs | ex 21.7 -> 21.3 (-0.4 pp) | ex 22.4 -> 21.3 (-1.1 pp) | FIXED |
| A6-313 | restatement-check scope and script | period FY2016 Q1-FY2025 Q4; note named A6_cycle.py | FY2016 Q4-FY2025 1H (32 pairs), Apr 2016-Sep 2025; script A6_comparatives_check.py; uncovered pairs stated | FIXED |
| A6-001 to A6-006, A6-009 to A6-014, A6-017 to A6-022, A6-025 to A6-030, A6-033 to A6-038, A6-041 to A6-046, A6-049 to A6-054, A6-057 to A6-062, A6-065 to A6-070, A6-073 to A6-078, A6-081 to A6-086, A6-089 to A6-092 (70 rows) | value on page 1 at the right column and label (script), period label | "FY2015 Q2 YTD" / "Apr 2015-Sep 2015"; claim "cumulative ... YTD" | "FY2015 1H" / "Apr-Sep 2015" (Q1, 1H, 9M); claim reworded; values unchanged and verified | FIXED (label) |
| A6-007, A6-008, A6-015, A6-016, A6-023, A6-024, A6-031, A6-032, A6-039, A6-040, A6-047, A6-048, A6-055, A6-056, A6-063, A6-064, A6-071, A6-072, A6-079, A6-080, A6-087, A6-088 (22 rows) | full-year page-1 values | claim "cumulative FY20xx" | claim "full year FY20xx (cumulative Apr-Mar)"; values verified | FIXED (wording) |
| A6-003, A6-004, A6-007, A6-008, A6-011, A6-012, A6-043 to A6-046, A6-049 to A6-054 (16 rows) | notes | "file name carries ... (PDF metadata)" | sentence removed (files renamed to printed dates) | FIXED (note) |
| A6-215, A6-238, A6-240, A6-246 | period label | "FY2019 Q3 YTD", "FY2015 Q3 YTD", "FY2016 Q2 YTD", "FY2022 Q3 YTD" | FY2019 9M, FY2015 9M, FY2016 1H, FY2022 9M; A6-215 note adds the 78th-report read | FIXED (label) |
| A6-252 to A6-269 (18 rows) | calendar-year labels; p.77 column mapping re-read (all 11 CY columns present, CY2015-CY2025) | "CY2015" / "Jan-Dec 2015" | "n/a (calendar year)" / "CY2015"; values verified | FIXED (label) |
| A6-308, A6-309, A6-310 | calendar-year [I] labels | "CY2018 to CY2019" as fiscal label | "n/a (calendar year)" / "CY2018 to CY2019" | FIXED (label) |
| A6-242, A6-243, A6-247 | dated outlook statements | FY2019 / FY2023 full-year labels | FY2019 Q1 "Apr-Jun 2019 (25 Apr 2019)"; FY2023 Q1 "Apr-Jun 2023 (26 Apr 2023)" | FIXED (label) |
| A6-217 | dated event | "Jul-Sep 2020" | "Jul-Sep 2020 (30 Jul 2020)"; note: amount printed for FY2020, event dated in Q2 | FIXED (label) |
| A6-214 | note | quarter inference only | adds A6-316 (3.5 bn sits inside Apr-Dec 2018) | FIXED (note) |
| A6-219 | "roughly ¥3 billion" quote (p.4 of the FY2022 Q4 Q&A, verbatim) and tag | note: approximate | note adds the FY2022 annual total 6,344 and the fact that such losses recur; tag kept [F] (historical figure in a company-published document) | FIXED (note) |
| A6-272, A6-273, A6-274 | inputs and reasons | partial id lists | "A6-001 to A6-092 (via A6-270)"; A6-273 reason cites the 0.17 pp margin; A6-272 calendar label clarified | FIXED (note) |
| A6-277, A6-278, A6-289, A6-290, A6-291 | inputs | no second document | cite the company-printed QoQ rows A6-323 to A6-328 | FIXED (note) |
| A6-282, A6-283, A6-284, A6-293, A6-294, A6-301 | inputs | incomplete id lists | complete id ranges | FIXED (note) |
| A6-314 to A6-347 | new [F] rows: FY2018 Q4 inventory loss; FY2019 Q1 inventory losses (no amount); 9M FY2018 one-time profit; annual inventory valuation losses FY2018-FY2023; company-printed QoQ changes at both troughs; IFRS adoption, transition date, IFRS 15, IFRS 16; U.S. GAAP FY2014-FY2015 cumulative figures | - | quote found on the cited page for every row | ADDED |
| A6-348 to A6-354 | new [I] rows: basis gap; U.S. GAAP T4Q; threshold sensitivity; 2018-19 pension-only variant; 2018-19 highest-to-lowest ex one-offs; inventory-loss shares; QoQ second-document check | - | values equal script output | ADDED |

OK ids (unchanged after re-check): A6-093 to A6-213, A6-216, A6-218, A6-220 to A6-237, A6-239, A6-241, A6-244, A6-245, A6-248 to A6-251, A6-270, A6-271, A6-275, A6-276, A6-279 to A6-281, A6-285 to A6-288, A6-296 to A6-300, A6-302, A6-304 to A6-307, A6-311, A6-312.

How the [F]/[C] rows were re-opened:
- A6-001 to A6-092: a script read the page-1 line beginning with each period label and checked that the value is the first number (net sales) or the third (operating income). The page heading "Consolidated Financial Results (Accumulated)" was also checked. Result: 92/92.
- A6-093 to A6-172, A6-210 to A6-213, A6-226 to A6-233: a script took the column position on each quarterly overview page. The layout is prior FY, then 1Q-4Q, then the year. Result: 90/90. FY2017, FY2018, FY2022 and FY2023 pages were also viewed in full.
- A6-173 to A6-195: page-1 lines of the FY2008, FY2009, FY2010, FY2011, FY2012 and FY2014 releases were viewed. Result: all equal.
- A6-196 to A6-206, A6-252 to A6-269: IAR 2026 p.77 was viewed in full. Result: column mapping correct.
- A6-207 to A6-237: each quote was located with findpage, and the context paragraph was read for A6-208, A6-209, A6-214, A6-216 to A6-222 and A6-237.
- A6-238 to A6-251: quotes were found on the cited pages, and A6-242, A6-243 and A6-247 were read on the slides. All are management explanations or outlooks, so [C] is right.

## Second-document cross-checks

| Figure | Document 1 | Document 2 | Result |
|---|---|---|---|
| 2022-23 peak -> trough: sales -31.3%, OI -63.0%, OM -12.1 pp | cumulative tanshin page-1 figures differenced (A6-061 to A6-066) | FY2023 Q1 briefing slides p.4, printed QoQ (A6-326 to A6-328) | agree |
| 2018-19 peak -> trough: sales -14.6%, OI -50.8%, OM -11.7 pp | tanshin differenced (A6-027 to A6-032) | FY2018 briefing slides p.6, printed QoQ (A6-323 to A6-325) | agree |
| Peak/trough single quarters FY2018 Q3, FY2018 Q4, FY2022 Q4, FY2023 Q1 | tanshin differenced | quarterly overview pages of the next full-year releases (A6-105 to A6-108, A6-139 to A6-142) | agree within 0.05 bn |
| FY2025 Q1 to FY2026 Q2 single quarters and margins | tanshin differenced | FY2026 Q2 slides p.5 (263.8 / 262.9 / 273.8 / 328.1 / 367.5 / 477.7 bn; OM 47.0-55.9%) | agree |
| FY2015-FY2025 annual sales, OI, margin | tanshin full-year page 1 | IAR 2026 p.77 11-year table | agree (script assert) |
| FY2018 one-off profit 3.5 bn | FY2018 full-year release p.5 (A6-209) | FY2019 Q3 release p.4 (A6-316): all inside Apr-Dec 2018 | agree |
| FY2020 one-off profit | segment notes 2,451 + 5,569 = 8,020 (A6-217, A6-218) | FY2020 full-year release p.5: "approximately (Y) 8.1 billion" | agree (rounding; not added as a row) |
| FY2022 Q4 inventory loss ~3 bn | Q&A p.4 (A6-219) | 81st annual securities report p.123: FY2022 total 6,344 (A6-321) | consistent; the quarterly amount is part of the annual total |
| FY2018 Q4 inventory loss ~2 bn | Q&A p.1 (A6-314) | 78th annual financial report p.21: FY2018 total 6,324 (A6-317) | consistent |
| Prior-year comparatives | first-reported page 1 | next year's page-1 comparative column | 32 pairs, 0 differences (A6_comparatives_check.out.txt, unchanged on re-run) |

## Calc re-run results
- `A6_cycle.py`: the original version re-ran byte-identical to the saved .out.txt, CSV and JSON. Every hard-coded input was checked against its row (ids in comments): 92 cumulative, 74 printed quarterly, 6 printed margins, 23 annual U.S. GAAP/IFRS, all one-off and other-income inputs, 18 market inputs, all equal. Formulas, the T4Q window (four quarters ending at the label) and the denominators were checked. LTM to FY2026 Q2 = Oct 2025-Sep 2026 = 1,447,077 (A6-312). The script was then changed: ONEOFFS gains FY2018 Q4 -2,000 and a kind flag (inventory vs other); UNQUANTIFIED gains FY2019 Q1; a new assert checks that the 3.5 bn sits inside 9M FY2018; new sections 9 (threshold sensitivity), 10 (inventory losses) and 11 (QoQ cross-check, 0 differences). Fixed a bug in my own new section 9 (the "last two" list was sorted by depth, not by date) before saving. Output diff versus the original: only FY2018 Q4 / FY2019 Q1 rows, the episode 2 ex-one-off lines, FY2018 annual ex and the new sections.
- `A6_comparatives_check.py`: re-run identical (32 pairs, 0 differences).
- New `A6_basis_check.py`: U.S. GAAP vs IFRS, run clean (asserts: T4Q at FY2014 Q4 and FY2015 Q4 equal the reported full years).
- New `A6_verify_spotcheck.py`: re-reads 16 quarters directly from the release text copies (FY2015 Q2, FY2015 Q3, FY2016 Q3, FY2017 Q1, FY2018 Q3, FY2018 Q4, FY2019 Q3, FY2019 Q4, FY2020 Q2, FY2022 Q1, FY2022 Q4, FY2023 Q1, FY2023 Q4, FY2024 Q2, FY2025 Q4, FY2026 Q2). This covers every peak and trough quarter used, plus slide- or table-printed and differenced quarters. Result: 16/16 match the series; 12/12 match company-printed quarters.
- Every [I] value in A6.csv equals the current script output (A6-270 to A6-354 compared line by line).

## One-off rule
Every margin figure in A6.md now lists the items management named for that period and shows the figure with and without them. Items named without an amount are listed as NOT DISCLOSED in A6_gaps.md: FY2019 Q1 inventory losses, FY2019 Q3 SLT amortisation, FY2025 Q4 SG&A items and the FY2026 Q1 / 1H inventory write-down reversals (from A1). The amounts inferred into a quarter are [I] Medium with stated reasons (A6-286, A6-296; A6-284 and A6-302 for FY2023 Q2). For FY2007 the release is not saved. The FY2007 column of the FY2008 income statement shows no restructuring or impairment line, and A6.md now says so instead of "nothing named".

## Gap re-tries
- FY2006 figures: the issuer's result index starts at FY2008 and the report index at the 74th term, and sec.gov is unavailable. Nothing new; still NOT RETRIEVED.
- SLT one-time amortisation amount: the FY2019 annual financial report (newly saved, `2020-06-26_advantest_annual-securities-report-78th-FY2019.pdf`, URL from the saved IR report index) was read. Its MD&A p.81 names the expense (now also tied to the Essai acquisition), and services-segment D&A rose from 1,477 to 5,099. The one-time part is still not separated, so it stays NOT DISCLOSED.
- Quarter placement of the FY2018 fixed-asset gain, the FY2020 German pension income and the FY2023 settlement: the adjacent-quarter releases were re-read. None of them mentions these items, so the inference stands at [I] Medium. The FY2019 Q3 release narrows the fixed-asset gain to Apr-Dec 2018.
- FY2008 restructuring line: the cash-flow add-back "Restructuring and impairment charges" is 18,930, against 13,788 on the income statement, a difference of 5,142, about the 5.1 bn restructuring. The non-operating lines are too small to hold 5.1 bn. This points to the cost sitting inside operating loss, but 8.7 + 5.1 = 13.8 also matches the income-statement line, so the reading is ambiguous. A6-307 stays Low and the gap stays open.

## Remaining doubts
1. Treating management-named inventory valuation losses as one-offs is a judgment. They recur every year (2.7-7.3 bn a year, FY2018-FY2023). Without them, the 2018-19 margin drop is -8.4 pp, not -5.2 pp, and the 2022-23 drop is -12.1 pp, not -14.1 pp. The ~2 bn and ~3 bn amounts are approximate oral figures from Q&A summaries.
2. 2018-19 qualifies as a downturn only because I set the T4Q threshold at 5%. It clears it by 0.17 pp.
3. IFRS 15 (FY2018) and IFRS 16 (FY2019) effects on the 2018-19 comparison are not disclosed.
4. File-name dates that differ from the printed dates were found in files outside the renaming fix. A6.csv uses the printed date, so no change was needed there; flagged for the orchestrator:
   - `2015-07-27_..._FY2015Q1.pdf`: printed 2015-07-28
   - `2015-10-23_..._FY2015Q2.pdf`: printed 2015-10-26
   - `2019-04-26_..._earnings-call-QA-FY2018Q4.pdf`: printed 2019-04-25
   - `2019-07-25_..._earnings-call-QA-FY2019Q1.pdf`: printed 2019-07-24
5. The 78th-term document saved today is the company's English "Annual Financial Report", a partial translation. Its file name uses the doctype `annual-securities-report-78th-FY2019` and the date 2020-06-26, which is the planned filing date in the FY2019 results release and the approval date printed in the document.

## Handoff (Last downturn drawdown)
- Last downturn, 2022-23: peak FY2022 Q4 (Jan-Mar 2023) -> trough FY2023 Q1 (Apr-Jun 2023), net sales -31.3% [I] (A6-277; slide [F] A6-326). Operating margin 26.2% -> 14.1%, -12.1 pp reported [I] (A6-279). Ex named one-offs (~3 bn inventory losses added back at the peak) 28.2% -> 14.1%, -14.1 pp [I] Medium (A6-280).
- Before it, 2018-19: peak FY2018 Q3 (Oct-Dec 2018) -> trough FY2018 Q4 (Jan-Mar 2019), net sales -14.6% [I] (A6-289; slide [F] A6-323). Operating margin 27.6% -> 15.9%, -11.7 pp reported [I] (A6-291). Ex named one-offs (2.5 bn pension gain out, ~2 bn inventory loss back) 24.3% -> 19.1%, -5.2 pp [I] Medium (A6-292); pension gain only, -8.4 pp [I] (A6-351).

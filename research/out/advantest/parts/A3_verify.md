# A3 verification log (adversarial verifier, 2026-11-21)

Scope: `parts/A3.csv`, `parts/A3.md`, `parts/A3_gaps.md`, `calc/A3_*.py` and `.out.txt`. Rules applied: `research/CLAUDE.md`, plus the run's tag rule that forecasts and targets are [C] even when printed in a filing.

## Counts

| Item | Count |
|---|---|
| Rows at start | 303 (261 [F]/[C], 42 [I]) |
| Rows checked | 303: every [F]/[C] row's cited page re-opened, every [I] row re-derived by re-running its script. No sampling was needed |
| OK, unchanged | 120 |
| Fixed | 183 (115 retagged, 45 period-label fixes, 1 restated, 22 claim or note fixes; some rows fall in more than one group) |
| Removed | 0 |
| Added | 14 (A3-304 to A3-317) |
| Rows at end | 317 |

Mechanical flags:
- `row_check_v1.csv` listed 3 A3 flags (A3-233, A3-254, A3-261), all PERIOD. All three were real label errors and are FIXED.
- Final runs on `parts/A3.csv`: `quote_check.py` finds all 272 [F]/[C] quotes (1 layout-insensitive, A3-229, on the right page). `row_check.py` reports 0 flags.

## Non-OK rows

| id | What was checked | Before | After | Result |
|---|---|---|---|---|
| A3-010 to A3-014, A3-018 to A3-026, A3-028 to A3-031, A3-040 to A3-057, A3-066 to A3-085, A3-094 to A3-108, A3-113 to A3-153, A3-239 (113 rows) | Each guidance, forecast, FX-assumption and FX-sensitivity figure re-read on its cited page: tanshin p.2 "Earnings Forecast" tables, the 6 revision notices p.1, forecast slides p.12-14 | [F]. All values, units, periods and pages were correct; no number changed | [C] (company forecast or assumption), with a note | FIXED (tag) |
| A3-027 | FY2023 Q2 cut reason, tanshin p.8 | [F] | [C]: a company explanation | FIXED (tag) |
| A3-226 | Q2 FY2026 "deliveries exceeded the level assumed in our July forecast", notes p.4 | [F] | [C]: the assumed delivery level is not published | FIXED (tag) |
| A3-233 | News index 2026 | FY2026 / "2026" (flag) | FY2026 Q1-Q3 / Apr-Nov 2026 (27 Apr-21 Nov 2026) | FIXED (flag) |
| A3-254 | News index 2024 | FY2023 / "Jan-Apr 2024" (flag) | FY2023 Q4-FY2024 Q3 / Jan-Dec 2024 | FIXED (flag) |
| A3-261 | News index 2023 | FY2023 / "2023" (flag) | FY2022 Q4-FY2023 Q3 / Jan-Dec 2023 | FIXED (flag) |
| A3-232 | News index 2025 | FY2024-FY2025 / "2025" | FY2024 Q4-FY2025 Q3 / Jan-Dec 2025 | FIXED (label) |
| A3-009 | Apr 2025 Q&A statement | "FY2025 Q1-Q2" | FY2025 1H / Apr-Sep 2025 (stated 25 Apr 2025) | FIXED (label) |
| A3-253 | MTP4 timing statement | "FY2027-" / "from Apr 2027" | FY2027 Q1 / Apr-Jun 2027 (around May 2027; stated 28 Oct 2026) | FIXED (label) |
| A3-189 to A3-220, A3-255 to A3-260 (38 rows) | Year-to-date actuals, tanshin p.1. Values all match | e.g. "FY2023 9M (YTD Q3)", "FY2025 Q1 (YTD)" | "FY2023 9M", "FY2024 1H", "FY2025 Q1" (convention) | FIXED (label) |
| A3-109 | IR forecast page (saved 2026-11-21) | value 1,863.0 (a forecast) in an [F] row | [F] value "28 Oct 2026" (page date); quote "Earnings Forecast October 28, 2026"; the 1,863.0 figure is kept in the claim. The page shows only the 28 Oct 2026 version | FIXED |
| A3-223 | Q3 FY2025 notes | page p.3, but "set in October 2025" is on p.2 | note added (quote on p.3, wording on p.2) | FIXED (note) |
| A3-240, A3-241 | MTP2 ROIC 21.2% (press release p.3) vs 25.5% (slides p.31) | claimed as an inconsistency | Both values re-read; the slide was rendered as an image. Same metric (MTP2 FY2021-23 average ROIC), same NOPAT / invested-capital footnote, same date, both labelled "results". The inconsistency stands. Two more documents carry each value (A3-304, A3-305). The company's own annual series averages 25.5% (A3-306, A3-307) | FIXED (claim wording; inconsistency kept) |
| A3-303 | [I] ROIC gap | 2 documents | 4 documents; still 4.3 pts | FIXED |
| A3-251 | IAR 2026 p.22 EPS "B" unit | claim of a unit error | p.22 rendered at 150 dpi: "JPY 284 - 341B", "JPY 218.67B", "JPY 515.15B" are printed. The claim now states what is printed and cites the per-share figures elsewhere | FIXED (wording; claim holds) |
| A3-262 | FY2022 context | IBT in the md table had no row | IBT -1.6% in-line added; rows A3-312, A3-313 | FIXED |
| A3-263 | Inputs | A3-018, A3-021 missing | added, plus A3-314 | FIXED (note) |
| A3-267 | FY2023 OI ex items | "ex both" shown as a like-for-like figure | The settlement was booked in Q2 FY2023 (A3-315), before the Jan 2024 guidance, so "ex both" mixes bases. Like-for-like is ex impairment only. Core OI cross-check added | FIXED |
| A3-272 | FY2024 tax share | cause "not stated" | The 83rd securities report states the cause: the impairment was non-deductible (A3-316). Tax share ex impairment with no tax effect is 25.8% vs 25.6% guided | FIXED |
| A3-273, A3-277 | One-off adjustments | no company-adjusted figure | Company core OI added (A3-308, A3-310); timing of each item vs the guidance date added | FIXED |
| A3-278 | Late-period flag | wording "not revised again" | Re-checked the news indexes 2024 and 2025: no forecast notice between 2024-01-31 and 2024-04-26, or between 2025-01-29 and 2025-04-25. The Q3 versions were raises. FY2022 context (maintained) is in-line | FIXED (wording, inputs) |
| A3-283, A3-286, A3-288, A3-290, A3-295 | One-off rule for each slot | no with/without figures for these slots | Ex-item figures added from the script. No class changes in the window. FY2023 2H NI flips from +6.6% to -4.5% less the DTA benefit (context only) | FIXED |
| A3-284, A3-292, A3-297 | Method wording | "guidance in force at the start of the quarter" | Guidance is published at the previous results release, about four weeks into the quarter (e.g. 2024-10-30 for Oct-Dec 2024) | FIXED |
| A3-285 | FY2024 Q4 NI miss | "NI bound" only | Threshold added: in-line if the after-tax effect is at least 5.4 bn, beat above 7.2 bn; company says the impairment was non-deductible | FIXED |
| A3-294 | "Raised at all 6 in-year releases" | 6 of 6; inputs sales only | Each version re-read on its page: 2025-01-29 (640.0 -> 740.0), 2025-07-29 (755.0 -> 835.0), 2025-10-28 (835.0 -> 950.0), 2026-01-28 (950.0 -> 1,070.0), 2026-07-29 (1,420.0 -> 1,714.0), 2026-10-28 (1,714.0 -> 1,863.0). OI and NI also rose each time. Added the run of 9 consecutive raises since 2024-01-31 (last cut 2023-10-31) and the OI inputs | FIXED (claim holds) |
| A3-296 | Inputs | FY2023 Q4 inputs missing | all inputs listed | FIXED (note) |
| A3-304 | 82nd Annual Securities Report p.18 | - | MTP2 ROIC 21.2% [F] | ADDED |
| A3-305 | FY2024 Q4 slides p.16 | - | MTP2 ROIC 25.5% [F] | ADDED |
| A3-306 | IAR 2026 p.77, 11-year table | - | annual ROIC FY2021 28.4%, FY2022 34.6%, FY2023 13.5% [F] | ADDED |
| A3-307 | calc | - | mean 25.5% matches the slides [I] Medium | ADDED |
| A3-308, A3-309, A3-310 | Results slides p.4 / p.5 | - | company core OI FY2024 249.7 bn (32.0%), FY2023 87.1 bn (17.9%), FY2025 496.5 bn (44.0%); no core-OI guidance [F] | ADDED |
| A3-311 | calc | - | core OI vs OI guidance [I] Medium | ADDED |
| A3-312, A3-313 | FY2022 IBT guidance 174,000 [C] / actual 171,270 [F] | in the md table without rows | rows | ADDED |
| A3-314 | FY2023 Q1 tanshin p.2 table: unchanged guidance, "Revision: No" | md showed IBT/NI citing a sales/OI-only row | row [C] | ADDED |
| A3-315 | FY2023 1H tanshin p.7: approx. 3.2 bn settlement income in the six-month period; the Q1 tanshin has none | settlement quarter unknown | [F] | ADDED |
| A3-316 | 83rd Annual Securities Report p.49: ETR 28.3% "rose higher than expected" due to non-deductible Q4 impairment | gap ("reason not stated") | [F] | ADDED (gap filled) |
| A3-317 | calc | - | FY2024 NI ex impairment thresholds; upper bound 182,570 (+9.0%) [I] Low | ADDED |

OK, unchanged after re-opening: A3-001 to A3-008, A3-015 to A3-017, A3-032 to A3-039, A3-058 to A3-065, A3-086 to A3-093, A3-110 to A3-112, A3-154 to A3-188, A3-221, A3-222, A3-224, A3-225, A3-227 to A3-231, A3-234 to A3-238, A3-242 to A3-250, A3-252, A3-264 to A3-266, A3-268 to A3-271, A3-274 to A3-276, A3-279 to A3-282, A3-287, A3-289, A3-291, A3-293, A3-298 to A3-302.

## Second-document cross-checks (headline figures)

| Figure | Document 1 | Document 2 (and 3) | Result |
|---|---|---|---|
| FY2023 latest guidance 480.0 / 85.0 / 82.5 / 64.5 bn; actual 486.5 / 81.6 / 78.2 / 62.3 | tanshin 2024-01-31 p.2; tanshin 2024-04-26 p.1 | FY2023 results slides 2024-04-26 p.5 ("Forecast as of Jan. 2024"); notice 2024-07-31 p.1 (FY2023 actual in millions) | agree |
| FY2024 latest guidance 740,000 / 226,000 / 225,000 / 167,500 / EPS 227.74 | notice 2025-01-29 p.1 | tanshin 2025-01-29 p.2; results slides 2025-04-25 p.4 ("Forecast as of Jan. 2025") | agree |
| FY2024 actual 779,707 / 228,161 / 224,774 / 161,177 / 218.67 | tanshin 2025-04-25 p.1 | notices 2025-07-29, 2025-10-28, 2026-01-28 ("FY2024 actual"); slides 2025-04-25 p.4 | agree |
| FY2025 latest guidance 1,070,000 / 454,000 / 452,500 / 328,500 / 452.34 | tanshin 2026-01-28 p.2 | notice 2026-01-28 p.1; results slides 2026-04-27 p.5 | agree |
| FY2025 actual 1,128,610 / 499,120 / 516,720 / 375,353 / 515.15 | tanshin 2026-04-27 p.1 | notice 2026-07-29 p.1 ("FY2025 actual"); slides 2026-04-27 p.5 | agree |
| FY2026 Jul guidance 1,714,000 / 846,000 / 891,000 / 660,000 / 911.64 | tanshin 2026-07-29 p.2 | notice 2026-07-29 p.1; slides 2026-10-28 p.14 ("as of July") | agree |
| FY2026 current guidance 1,863,000 / 967,000 / 1,021,500 / 741,500 / 1,027.08 | tanshin 2026-10-28 p.2 | slides 2026-10-28 p.14; IR forecast page (saved 2026-11-21) | agree; page dated 28 Oct 2026 |
| Single-quarter actuals FY2023 Q2, FY2024 Q2/Q3, FY2025 Q2/Q3, FY2026 Q1 | summary slides 2025-04-25 p.6, 2026-04-27 p.7, 2026-10-28 p.14 | each quarter's own forecast slide (2023-10-31 p.12, 2024-10-30 p.13, 2025-01-29 p.13, 2025-10-28 p.12, 2026-01-28 p.13, 2026-07-29 p.13) and tanshin YTD differences (gap < 0.1 bn) | agree |
| MTP3 original targets (560-700 / 22-28 / 93-147 / 18-28 / 127-202) | press release 2024-06-25 p.3 | slides p.31; 82nd securities report p.18; revision notice 2025-10-28 p.1 ("previously announced") | agree |
| ROIC FY2024 31.5%, FY2025 54.4% | IAR 2026 p.22 | IAR 2026 p.77; FY2024 Q4 slides p.16 (FY2024) | agree |
| MTP2 ROIC | press release p.3 and 82nd securities report p.18: 21.2% | MTP3 slides p.31 and FY2024 Q4 slides p.16: 25.5% | DISAGREE (kept as a documented inconsistency; 25.5% = mean of IAR p.77 annual series) |
| FY2024 core OI 249.7 bn | slides 2025-04-25 p.4 | slides 2026-04-27 p.5 (FY24 column) | agree |

## Calc re-run results

- All four scripts re-run with `python3 -I` before editing reproduced their `.out.txt` exactly.
- Every hard-coded input was checked against its cited row id. The 2H and Q4 derivations, period windows (A3 uses no LTM windows) and denominators ((actual - guidance) / guidance) are correct.
- Changes made, each re-run and its `.out.txt` refreshed:
  - `A3_quarter_record.py`: method wording; context releases and the run of 9 consecutive raises; one-off sensitivities for every slot; FY2024 Q4 NI thresholds.
  - `A3_annual_record.py`: FY2022 IBT; core-OI cross-check; timing of named items vs guidance dates; FY2024 NI thresholds under the non-deductible impairment.
  - `A3_mtp3_status.py`: MTP2 ROIC mean from the IAR p.77 series.
  - `A3_fy2026_guidance.py`: unchanged; reproduces its output.
- The final re-run of all four scripts matches the saved outputs. Every [I] row's value appears in its script output. Every [I] note has the form "inputs; script; reason" and a High/Medium/Low confidence.

## Gap retries

| Gap | Retry | Result |
|---|---|---|
| Reason for the FY2024 tax share | 83rd securities report (already saved) | FILLED (A3-316) |
| After-tax effect of the FY2024 impairment | 83rd securities report note 15, tax reconciliation (p.146) | Does not itemise the impairment. It remains a gap; shown as a bound (A3-317) |
| After-tax effect of the FY2023 impairment | 82nd securities report, Income taxes | No statement found. Remains a gap |
| Q1/Q3 single-quarter guidance | April slides (2025-04-25 p.19, 2026-04-27 p.20) | Full year only. Remains a gap |
| MTP2 ROIC reconciliation | 82nd securities report, FY2024 Q4 slides, IAR p.77 | No reconciliation found. The annual series supports 25.5%. Remains a gap |

## Remaining doubts

1. **Quarter-slot method.** The count depends on how slots are defined. Q3 slots are half-year tests and Q1 slots are full-year tests; the FY2025 Q1 slot repeats the annual comparison. Each slot's guidance was published about four weeks into the quarter it tests.
2. **FY2024 Q4 NI miss.** The miss may be an artefact of the non-deductible impairment. The exact after-tax effect is not disclosed, so the classification is left as reported.
3. **Absence of later revisions.** This rests on the English news-index pages, not on TDnet (Japanese) filings.
4. **IAR 2026 date.** The saved file is dated 2026-11-11 (PDF CreationDate). The 2026 news index lists "Integrated Annual Report 2026 now Available" on 2026-10-16. The `date` field of the IAR rows (A3-248 to A3-252, A3-306) may need the earlier date if a printed date is found.
5. **Possible issue in module A1 (not edited here).** `calc/A1_oneoffs.out.txt` notes the "one-off SG&A amount not disclosed" against FY2025 Q4. Management named that charge for Q2 FY2025 (A3-093; 2025-10-28 notes p.3). The A1 verifier may want to check this.
6. **Valuation gains as one-offs.** The 1H FY2026 valuation gains (54.2 bn) are not labelled one-off by the company. They are removed in A3 only as a sensitivity.

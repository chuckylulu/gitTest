# A1 verification log (adversarial re-check, 2026-11-21)

Scope: `parts/A1.csv`, `parts/A1.md`, `parts/A1_gaps.md`, `calc/A1_*.py`. Fiscal year ends 31 March and is named by its start year (FY2026 = Apr 2026-Mar 2027). Latest quarter FY2026 Q2 (Jul-Sep 2026), released 28 Oct 2026 (tanshin cover, A1-094).

## Counts

| Item | Count |
|---|---|
| Rows before | 481 (339 [F], 13 [C], 129 [I]) |
| Rows checked | 481: all 352 [F]/[C] rows against re-opened pages (text layer, layout text or rendered PNG); all 129 [I] rows against re-run scripts |
| OK (no content change) | 446, incl. A1-300 (false flag) and 96 rows whose only change was the period-label suffix |
| Fixed (content) | 35 |
| Label-only normalisation | 96 rows: `FY2026 1H (YTD Q2)` -> `FY2026 1H`, `FY2025 9M (YTD Q3)` -> `FY2025 9M` (convention) |
| Removed | 0 |
| Added | 29 (A1-482..A1-510) |
| Rows after | 510: 355 [F], 18 [C], 137 [I] (new rows: 16 [F], 5 [C], 8 [I]) |

## Non-OK rows

| id | what was checked | before | after | result |
|---|---|---|---|---|
| A1-300 | row_check VALUE flag "95 not on cited page" | 95% on Investors' Guide p.5 | unchanged value; note says the table is an image on physical p.5, verified on the rendered page (FY24 90%, FY25 95%, rounded to 5%) | FALSE FLAG |
| A1-185 | re-read ASR84 physical p.193 (printed -189-) | "SBC expense in parent-only SG&A, FY2025"; note said no reconciliation | claim states what is printed: parent-only J-GAAP statement of operations, note *1 "major items" of SG&A, FY2025 full year 26,134 (FY2024 3,667); note links the parent-only liability provision (A1-489/490/507), the provision policy (A1-491) and the equity-settled IFRS plans (A1-492/493); no reconciliation printed | FIXED (claim, note; tag [F] kept) |
| A1-306 | period of the printed amount | FY2024 Q4 / Jan-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (tanshin note prints it "for the fiscal year ended March 31, 2025"; Q4 placement comes from slide note A1-307) | FIXED |
| A1-309 | period of the printed amount | FY2025 Q4 / Jan-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (printed "for the fiscal year ended March 31, 2026"; Q4 placement from A1-310 notes and A1-320 quarterly line) | FIXED |
| A1-304 | calendar-year metric label | FY2025 Q3 / Oct-Dec 2025 | n/a (calendar year) / CY2025 | FIXED |
| A1-302, A1-303 | dated statement label (Q&A of 28 Jan 2026) | FY2025 Q3 / Oct-Dec 2025 | FY2025 Q4 / Jan-Mar 2026 (28 Jan 2026) | FIXED |
| A1-297 | forecast label | "FY2026 forecast (as of 2026-10-28)" | FY2026 (forecast) / Apr 2026-Mar 2027; date in claim | FIXED |
| A1-351 | claim mixed a fact (rate) with a management attribution | "Management: yen depreciation contributed..." | "Average USD/JPY rate 1H FY2026 160 (146 a year earlier); management attributes part of the result to yen depreciation" | FIXED |
| A1-186 | inter-segment detail on tanshin p.15 | note "includes 10 million inter-segment" | note adds sales to unaffiliated customers 1,019,380 and the Note 22 total 1,019,390 | FIXED (note) |
| A1-354 | GP YoY FY2025 Q3 | +42.7 (rounded slide bn) | +42.8 (JPY million differencing) | FIXED |
| A1-356 | OI YoY FY2025 Q3 | +64.2 | +64.0 | FIXED |
| A1-357 | OM change FY2025 Q3 | +9.8 pts | +9.7 pts | FIXED |
| A1-358 | NI YoY FY2025 Q3 | +51.6 | +51.8 | FIXED |
| A1-362 | OI YoY FY2025 Q4 | +138.8 | +139.1 (= company-printed +139.1%, A1-501) | FIXED |
| A1-366 | GP YoY FY2026 Q1 | +49.0 | +48.9 | FIXED |
| A1-368 | OI YoY FY2026 Q1 | +53.2 | +53.3 | FIXED |
| A1-372 | GP YoY FY2026 Q2 | +107.6 | +107.7 (= printed, A1-499) | FIXED |
| A1-374 | OI YoY FY2026 Q2 | +146.1 | +146.0 (= printed, A1-068) | FIXED |
| A1-376 | NI YoY FY2026 Q2 | +142.8 | +142.7 (= printed, A1-500) | FIXED |
| A1-353, 355, 359, 360, 361, 363, 364, 365, 367, 369, 370, 371, 373, 375 | same YoY rows, values unchanged | inputs = rounded slide rows | inputs = JPY-million tanshin rows; page = A1_pnl.py section 2b | FIXED (inputs/note only) |
| A1-471 | FY2024 Q4 OM ex impairment | slide bn x1000 inputs | JPY million FY minus 9M inputs (A1-014, 228, 002, 482); value 36.8% unchanged | FIXED (inputs) |
| A1-475 | inputs listed A1-311 (SG&A one-off, not used) | A1-016, 119, 309, 311 | A1-016, 119, 309, 310, 320 | FIXED (inputs) |
| A1-482..488 | new [F] YTD P&L rows needed for million-level quarters (9M FY2024, 1H FY2024 IBT/NI, FY2025 Q1 NI) | - | added, quotes FOUND on tanshin pp.11/11/9 | ADDED |
| A1-489..493 | parent-only provision (BS p.186), policy (p.190), IFRS equity-settled plans (pp.163-164) | - | added | ADDED |
| A1-494..496 | recurring-revenue statements (ASR84 p.38, MTP3 p.20, Q2 FY26 slide 17) | - | added [C] | ADDED |
| A1-497, 498 | FY2026 Q1 notes: valuation gains described as period-end gains (not one-off); GM 69.5% helped by limited inventory valuation losses | - | added [C] | ADDED |
| A1-499..502 | company-printed YoY (Q2 FY26 slide 5; Q4 FY25 slide 7) | - | added [F] | ADDED |
| A1-503..510 | OI YoY ex named items (Q4 FY25 +79.2%, Q1 FY26 +56.4%); LTM IBT 796,437 and ex items 724,954; provision increase 22,002; LTM S&O share 9.4%, Support Services 5.6% (not company definitions); LTM SoC share 70.2% | - | added [I] | ADDED |

OK ids (value, unit, sign, period, page, quote and tag re-checked): A1-001..A1-184, A1-187..A1-296, A1-298, A1-299, A1-301, A1-305, A1-307, A1-308, A1-310..A1-350, A1-352, A1-377..A1-470, A1-472..A1-474, A1-476..A1-481. (Many of these also had the period-label suffix removed.)

## Specific doubts settled

1. **A1-300 (95%)**: printed in an image table on Investors' Guide physical p.5; text layer empty. FALSE FLAG. Same table on Q2 FY26 slide 15 (rendered).
2. **A1-185 vs A1-174**: 26,134 is printed as a FY2025 (Apr 2025-Mar 2026) full-year flow in the parent-only J-GAAP statement of operations, under "Major items and amounts of selling, general and administrative expenses". It is not a balance and not a different period. The parent-only balance sheet shows "Provision for share-based remuneration" of 8,477 + 20,088 = 28,565 at 31 Mar 2026 vs 2,537 + 4,026 = 6,563 at 31 Mar 2025 (+22,002). The parent-only policy is an "estimated amount" provision; the consolidated PSU and RS/RSU plans are equity-settled. Whether the parent's figure covers group-wide plans or a liability remeasurement is not stated; no reconciliation printed. Consolidated 4,450 kept for SBC.
3. **Inventory write-down reversal (FY2026 Q1/1H) and FY2025 Q4 one-off SG&A**: searched again in the 85th semi-annual report (no inventories note; no SG&A note), FY2026 Q1 and Q2 slides, notes, Q&A and tanshin, FY2025 Q4 slides, notes, Q&A, tanshin, ASR84 MD&A and Note 23 SG&A (p.161), and the 12 Nov 2026 fireside chat. No amount. Logged as NOT DISCLOSED with the list read.
4. **Call-option gain called one-off**: verified. FY2025 Q4 briefing notes, physical p.5, section "[p.7] FY2025 Q4 Summary of Results": "This income is reflective of a one-off item" (Japanese 本件は一過性の収益). **FY2026 valuation gains**: not called one-off anywhere; the Q1 notes say "period-end valuation gains on investments in investment fund" (A1-497) and the Q2 notes "period-end valuation gains on investment securities" (A1-314).
5. **Recurring revenue**: not defined or quantified by the company (only "recurring revenue offerings", ASR84 p.38, and "Boost Recurring", MTP3 p.20). NOT DISCLOSED; proxies added and labelled as not company definitions (A1-508, A1-509, Low).
6. **Adjusted gross margin**: none published; only core operating income (full-year slides). NOT DISCLOSED line added; handoff shows reported / n.a. / not computable.
7. **Single quarters, LTM windows, FCF, SBC/FCF**: all 8 quarters re-derived in JPY million from YTD statements (A1_pnl.out.txt 2a); slide quarters equal differences of rounded YTD figures, so they can differ by 0.1 bn (e.g. FY2024 Q4 OI slide 64.1 vs 64,035; FY2025 Q2 sales slide 262.9 vs 262,957). LTM = FY2025 + 1H FY2026 - 1H FY2025 = Oct 2025-Sep 2026; prior LTM = FY2024 + 1H FY2025 - 1H FY2024 = Oct 2024-Sep 2025: correct windows. FCF under both definitions and SBC/FCF re-computed: unchanged.

## Second-document cross-checks

| Figure | Document 1 | Document 2 | Result |
|---|---|---|---|
| FY2025 quarterly sales/OI/NI (Q1-Q4) | Q2 FY26 slides p.5 | Q4 FY25 slides p.7; FY2025 tanshin overview p.19 | agree |
| FY2026 Q2 sales, GP, OI, NI | Q2 FY26 slides p.5 (477.7 / 339.8 / 266.8 / 193.3) | tanshin 1H minus Q1 (477,727 / 339,825 / 266,819 / 193,303) | agree within rounding; company-printed YoY equals the million-based YoY |
| FY2025 annual P&L | FY2025 tanshin p.11 | FY25 Q4 slides p.5 (1,128.6 / 499.1 / 516.7 / 375.4) | agree |
| Quarterly segment and sub-segment sales (9 quarters) | Q2 FY26 slide 6 | Investors' Guide p.5 chart; YTD differencing of segment tables | agree (FY2024 Q4 Test Systems 204.1 chart vs 204,160 differenced, rounding) |
| SoC / Memory / Others FY2025 and FY2024 | ASR84 Note 22 p.160 | Q2 FY26 slides 15-16 | agree, except FY2024 SoC 440.4 on slide vs 440,452 filed (0.1 bn rounding difference) |
| Computing / Communications 95% (FY2025) | Q2 FY26 slide 15 | Investors' Guide p.5 | agree |
| SBC FY2025 4,450 | FY2025 tanshin CF p.13 | ASR84 CF p.118 and segment reconciliation p.15 | agree; PSU 1,258 + RS/RSU 3,189 = 4,447 (3 million difference, unexplained, immaterial) |
| SBC 1H FY2026 2,635 | FY2026 Q2 tanshin p.15 | Semi-Annual Securities Report 85th p.27 | agree |
| FCF FY2025 / FY2024 | CF statements (300,630 / 243,782) | FY25 Q4 slide 11 (300.6 / 243.8) | agree |
| Quarterly FCF | YTD differencing (71,430 / 106,418 / 34,607 / 61,478) | notes and slide 9 (71.5 / 106.3 / 34.7 / 61.5) | agree except FY2025 Q4 (0.1 bn, investing CF -10.2 vs -10.3; open) |
| Impairment 21,393 | FY2025 tanshin note 2 | Q2 FY26 slide 8 note (21.4 bn, Q4 FY24) | agree |
| Call-option gain 17,312 | FY2025 tanshin note 3 | Q4 FY25 notes (17.3 bn); tanshin p.19 Q4 financial income 19.3 bn | agree |
| Core operating income | FY25 Q4 slide 5 (496.5 / 249.7) | recomputed 496,479 / 249,693 | agree |

## Calc re-runs (`python3 -I`)

- Before edits: all four scripts reproduced their .out.txt exactly (diff empty).
- `A1_pnl.py`: section 2 rewritten to compute YoY on JPY-million single quarters (new inputs A1-482..488); slide-based YoY kept as section 2c for comparison; LTM IBT with/without items added. Output regenerated.
- `A1_oneoffs.py`: FY2024 Q4 row switched from slide bn x1000 to FY minus 9M in JPY million (results unchanged: OM 27.6% -> 36.8%); OI YoY with/without base-quarter items added.
- `A1_fcf_sbc.py`: parent-only provision arithmetic added (22,002). FCF and SBC figures unchanged.
- `A1_segments.py`: LTM segment-mix section added (S&O 9.4%, Support Services 5.6%, SoC 70.2%). Earlier sections unchanged.
- Every [I] row's value was matched against its script output; every [I] note has the form "inputs: ...; script: research/out/advantest/calc/A1_*.py; reason: ..." with High/Medium/Low.
- Final mechanical checks: quote_check on parts/A1.csv: all quotes FOUND (2 layout-insensitive: A1-315, A1-316, verified by eye). row_check: 1 flag, A1-300 VALUE (false flag, explained above).

## Remaining doubts

1. Parent-only SBC 26,134 vs consolidated 4,450: no reconciliation in ASR84.
2. Amounts of the FY2026 Q1/1H inventory write-down reversal and the FY2025 Q4 one-off SG&A: not disclosed; ex-one-off GM/OM for FY2026 Q1, Q2, 1H and LTM cannot be computed.
3. FY2025 Q4 company FCF 106.3 bn vs derived 106.4 bn; company "Capital Expenditure" basis.
4. FY2024 SoC 440.4 bn (slide) vs 440,452 million (filing).
5. Theme share: "Computing / Communications" mixes HPC/AI with smartphone APs, covers SoC testers only and is rounded to 5%; the implied 64.6% of FY2025 sales is Low confidence and is not an AI share.
6. Recurring-revenue proxies (S&O 9.4%, Support Services 5.6% of LTM sales) are our constructs, not company definitions.

# XM - cross-module reconcile log (Advantest, TSE 6857)

Run 2026-11-21. Fiscal year ends 31 March and is named by its start year (FY2026 = Apr 2026-Mar 2027). Latest quarter FY2026 Q2 (Jul-Sep 2026), released 28 Oct 2026. IFRS, JPY. Scope: the eight module parts (A1-A6, TH, CL), their calc scripts and markdown. run_log.md and _verify_summaries.json were not edited; section 9 lists the summary statements this pass supersedes.

Scripts: `calc/XM_consistency.py` (scan; first run saved as `calc/XM_consistency.before.out.txt`, final run as `calc/XM_consistency.out.txt`) and `calc/XM_period_labels.py` (label rule; every change printed in `calc/XM_period_labels.out.txt`). Both run with `python3 -I`.

## 1. Results in one view

| Check | Before | After |
|---|---|---|
| (a) same file + page, different modules, same quantity, values/units/periods disagree | 15 pairs | 3 pairs, all explained in section 2 (none is a wrong value) |
| (b) same file + quote, different tags | 13 pairs | 7 pairs, all different cells of one printed table row (actual [F] vs forecast [C]) |
| (b2) near-identical quotes, different tags | 11 pairs | 10 pairs, same reason, plus TH-019/A5-161 (fact vs plan) |
| Dated statements relabelled to the one rule | - | 333 rows changed, 117 already conformed, 0 unparsed; a second run changes 0 rows |
| merge_parts.py | 2,380 rows | 2,385 rows (A1-511 to A1-515 added); no PROBLEM lines |
| quote_check.py | all quotes found | 1,944 quoted rows: 1,913 FOUND, 31 FOUND (layout-insensitive), 0 NOT FOUND, 0 flags (`calc/quote_check_report_v3.csv`) |
| row_check.py | 3 flags | 3 flags, all false positives (section 8) (`calc/row_check_v3.csv`) |

## 2. Conflicts found by the scan and how each was settled

| id(s) | issue | before | after |
|---|---|---|---|
| A4-312 / CL-060 | same Q&A quote (Q1 FY2026 Q&A p.4, 'approximately 19%'), different tags and quarters | A4-312 [F] FY2026 Q2; CL-060 [C] FY2026 Q1 / Apr-Jun 2026 (stated 29 Jul 2026) | both [F] (a historical share testable against the ship-to chart, 18.9% in FY2026 Q1 and Q2, A4-356/357); both FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026); CL.md C4 row and section C4 text updated |
| A1-314 / A3-227 / CL-031 | same notes quote ('financial income of 14.7 billion JPY'), A1 [C] vs A3/CL [F] | A1-314 [C] | A1-314 [F]; the value is the reported Q2 financial income; 'mainly valuation gains' is management's description. A1-497 (Q1 analogue, 44.7 bn) also set to [F]; A1.md tags updated |
| A3-229 / A1-316 / A2-180 / A5-229 / CL-073 | same Q&A quote (inventory write-down reversal), A3 [F] vs others [C] | A3-229 [F] | A3-229 [C] (untestable attribution, no amount); A3.md text updated |
| A3-093 / A1-311 / A5-227 | one-off SG&A attributions: A3 [F], A1/A5 [C] | A3-093 [F] | A3-093 [C], claim rewritten (see section 3) |
| A3-063 / A6-223 / A1-306 | same full-year segment note (FY2024 tanshin p.15, impairment 21,393), A3 labelled FY2024 Q4 | A3-063 FY2024 Q4 / Jan-Mar 2025 | FY2024 / Apr 2024-Mar 2025, as A1-306 and A6-223; the Q4 booking rests on A3-064 (management) |
| A1-307 / CL-038 | same slide note giving two items in two quarters (21.4 bn Q4 FY24; 2.5 bn Q1 FY25) | A1-307 FY2024 Q4 / Jan-Mar 2025 | FY2024 Q4; FY2025 Q1 / Jan-Mar 2025; Apr-Jun 2025 (as CL-038) |
| TH-042 / CL-001 | same Q&A quote (TAM grew ~50%/yr over 'the past few years'), different labels | TH-042 FY2026 Q3; CL-001 n/a (calendar year) / past few years to CY2025 | both FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026): no calendar years are named, so the statement quarter applies |
| TH-117 / CL-040 | same statement (path to SoC share above 70%, no timing) | CL-040 n/a (calendar year) / not specified | CL-040 FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026), as TH-117 |
| TH-041 / CL-071 | same statement (CPU test demand = biggest factor in the raised FY2026 forecast) | TH-041 FY2026 Q3 | TH-041 FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026): a statement about the forecast period, as CL-071 |
| A4-314 / CL-061 | same answer (China ~20% or lower until new China fabs around 2028-2029) | A4-314 FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026) | n/a (calendar year) / to CY2028-CY2029 (stated 29 Jul 2026), as CL-061 |
| A2-057 / A5-193 | same IAR p.23 sentence (JPY 70 bn of CB funds for capacity and inventory) | A2-057 FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026; bonds issued Apr 2026) | FY2026-FY2028 / Apr 2026-Mar 2029 (stated 11 Nov 2026), as A5-193 and the planned-use dates A5-072/A5-073 |
| TH-169 / CL-018 | same Teradyne figures, two calendar wordings | TH-169 'CY2025 vs Jan-Aug 2026' | 'CY2025; Jan-Aug 2026 (stated 28 Oct 2026)', as CL-018 |
| TH-102 / CL-006; TH-116 / CL-039; A1-303 / TH-205; A1-315 / A2-052; A1-316 / CL-073 | same quotes, calendar labels worded differently ('forecast as of', 'estimate of', bare date, no date) | mixed | one wording '(stated D Mon YYYY)' via XM_period_labels.py. TH-116 (value 66, CY2025) and CL-039 (56; 66) carry the same printed figures; left as is |
| A4-336 / CL-104 | same BIS notice; A4 labels the publication, CL the deadline | CL-104 'Jan-Mar 2027 (10 Jan 2027)' | CL-104 'Jan-Mar 2027 (deadline 10 Jan 2027; published 9 Nov 2026)'; both kept: A4 records the rule's publication (FY2026 Q3), CL the catalyst date (FY2026 Q4) |
| A3-110 / CL-035 | same page, different numbers (50 vs 47.3) | - | no conflict: A3-110 is the Oct 2026 expectation (2H OPM above 50%), CL-035 the July forecast's 2H assumption (47.3%) quoted on the same page |
| TH-019 / A5-161 | overlapping quote, [F] vs [C] | TH-019 claim 'Partnership ... with planned minority stake' | TH-019 claim separates the fact (partnership announced 27 Feb 2025, [F]) from the plan (stake, [C] A5-161) and the later holding ([F] A5-237) |
| A3-237/A3-240; A3-141/A3-187; A3-153/A3-188; A1-295,A1-296/A1-297; A2-027/A3-181,A3-184; A1-087,A1-088/A3-145; A1-089/A3-133; A3-150..152/A3-181..186 | same quote string, different tags | - | legitimate: each quote is one printed table row holding both actual figures [F] and forecast or target figures [C]; each row cites a different cell |
| CL-062 | press item labelled with the wrong quarter (published 30 Jan 2026 in FY2025 Q4) | FY2025 Q3 / Oct-Dec 2025 (published 30 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (published 30 Jan 2026) |

## 3. One-off SG&A in FY2025: which quarters, and what amount

Re-read: FY2025 Q1, Q2, Q3 and Q4 briefing notes, Q&A summaries, slides and tanshin; IR fireside chat Nov 2025. Findings:
- **FY2025 Q2 (Jul-Sep 2025):** the notes (28 Oct 2025) p.3 say the QoQ fall in profit was 'mostly due to changes in the product mix and an increase in SG&A associated with one time charge related to a growth investment' [C] (A3-093). The same notes p.9 (speaker notes to the P&L slide) say: 'In Q2, we booked approximately 2 billion JPY of expenses related to initiatives to enhance our medium- to long-term competitiveness' [F] (new A1-511). The notes do not say in so many words that the 2 bn is the one-time charge; both passages explain the same SG&A rise and p.9 names no other Q2 charge, so the 2 bn is used as its amount [I] Medium (new A1-512). The Q2 Q&A, slides and tanshin give no further amount.
- **FY2025 Q3 (Oct-Dec 2025):** no one-off named; the notes credit 'only moderate increases in SG&A'.
- **FY2025 Q4 (Jan-Mar 2026):** the notes (27 Apr 2026) p.6 say SG&A rose 'in addition to one-off expenses related to business operations' (事業運営上の一時的な対応費用) [C] (A1-311, A5-227). No amount in the notes, Q&A, slides, tanshin or ASR84: NOT DISCLOSED (unchanged).
- **FY2025 Q1:** 'absence of one-off losses' / 'no one-time write-downs' [C] (A1-317); the 2,504 million divestiture gain is the named item.
So A1 (Q4) and A3 (Q2) were each right and each had missed the other quarter. A1.md had wrongly said no item was named for FY2025 Q2.

Effects (all [I], Medium because of the inferred link): FY2025 Q2 operating margin 41.3% reported, 42.0% without the charge (A1-513); FY2025 operating margin 44.2% reported, 44.0% without the divestiture gain only (A1-472, unchanged), 44.2% also adding back the Q2 charge (A1-514); FY2026 Q2 operating income YoY +146.0% reported, +141.5% against a base quarter without the charge (A1-515); A3 FY2025 Q2 guidance slot OI +12.6% reported, +14.6% without the charge, beat either way; MTP3 three-year aggregate margin 45.4% ex one-offs (CL-121, unchanged), 45.5% in the variant. No beat/miss class changes.

## 4. Inventory write-down reversal: which quarter(s)

- Q1 FY2026 Q&A (29 Jul 2026) A9: 'Margins in the quarter also benefited from a reversal of inventory obsolescence, which is not expected to occur on a recurring basis' (今四半期の利益率は棚卸資産評価損戻入れの効果による押し上げ) - named for **FY2026 Q1** [C] (A1-315, A2-052).
- Q2 FY2026 Q&A (28 Oct 2026) A5: 'In 1H ... there was also a one-time benefit to the operating margin from a reversal of inventory write-down' - named for **1H FY2026** [C] (A1-316, A2-180, A3-229, A5-229, CL-073).
- The Q2 FY2026 notes, slides and tanshin and the 85th semi-annual report do not mention it. No document says whether any part fell in FY2026 Q2 (Jul-Sep 2026); the 1H remark may restate the Q1 item. Amount NOT DISCLOSED in every document read.
- Fixed: CL-025 note, CL-122 note and CL.md (C6 row, margin table, B2 item 5, Teradyne comparison) had said or implied that the FY2026 Q2 margin of 55.9% includes the reversal; they now say only that the 1H margin does and the Q2 share is not disclosed. A1, A2, A3, A5, A6 and CL rows, calc notes and md text now name both Q1 and 1H and state that the Q2 share is not disclosed.

## 5. Cross-module figure checks (no value changed)

| Quantity | Modules and values | Result |
|---|---|---|
| FY2026 Q2 (Jul-Sep 2026) net sales, YoY | A1-060/A3-184/A6-165/CL-024 477.7 bn; A1-391/A2-083/CL-141 477,727 m; A4-138 477.7; A1-067/A1-371 +81.7% | consistent |
| FY2026 Q2 gross margin; operating income and margin | A1-062/CL-026 71.1%; A1-063/A3-185/A6-166 266.8 bn; A1-064/CL-025/A6-311 55.9% | consistent |
| FY2026 Q2 SoC / memory sales and YoY | A1-282/TH-141/CL-027 353.3 bn; A1-283/TH-147/CL-028 53.4 bn; A1-457/CL-114 +103.4%; A1-458/CL-114 +21.6% | consistent |
| LTM Oct 2025-Sep 2026 | A1-396/A6-312 1,447,077 m; A1-399/A6-312 OPM 50.0%; A4-370/CL-118 China 19.5%; A4-371 281.7 bn | consistent; period_fiscal unified to 'LTM FY2025 Q3-FY2026 Q2' (section 7) |
| NVIDIA / TSMC shares | Group basis (Note 6(6)): NVIDIA Group 243,735 m = 21.6% (A4-001, A4-339, CL-068, CL-119); single-entity basis (Item 2 table): NVIDIA International, Inc. 228,273 m = 20.2% printed (A4-406, A4-407, CL-069); TSMC 11.1% on both | values consistent; CL-068 and CL-119 claims and CL.md now name the basis |
| Inventories and dates | A2-036 231,718 m (31 Mar 2026), A2-038 352,426 m (30 Sep 2026) = CL-088; A2-117/CL-120 +120,708 m in 1H (+52.1% over six months); A2-116 +67.8% YoY (30 Sep 2025 to 30 Sep 2026) | consistent; the two percentages use different bases and both md files say which |
| China share | A4-354..357 23.9 / 17.3 / 18.9 / 18.9% = CL-118; A4-369 / CL-118 +72.9% YoY; A4-312 = CL-060 approx. 19% (now both [F]); CL-132 20-25% (Jan 2026, [C], CL only) | consistent |
| FY2026 guidance | A3-104/105/107/108 = CL-033 (1,863,000; 967,000); A3-280 implied OPM 51.9% = CL-034 printed 51.9%; CL-036 +149.0 bn = A3-104 - A3-099; A3-111 / A2-026 ~20% 1H->2H; A3-150 / A2-027 2H sales 1,017.8 bn | consistent |
| Buybacks | A5-102 = CL-099 (280 bn / 11 m shares, 29 Oct 2026-24 Mar 2027); A5-104 = CL-100 (420,900 shares, JPY 14,563,326,000); CL-124 headroom = 280 bn - 14.56 bn; A5-226 FY2025 114.2 bn = A5-210 114,228.3 m | consistent |

## 6. Period-label rule (step 3)

Rule applied by `calc/XM_period_labels.py` to every dated statement ([C] rows; [F]/[S] rows already marked 'stated' or attributed to management/Teradyne/Micron, except attributed [F] rows that report a number for a closed period):
- past or present statement: the fiscal quarter that contains the statement date, e.g. FY2026 Q3 / Oct-Dec 2026 (stated 12 Nov 2026); when this moves a row off the period it was labelled with, the note records 'Statement refers to ...';
- statement about a forecast period: that period, e.g. FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026);
- calendar-year metric: n/a (calendar year) / CY2026, plus '(stated D)' when it is a company estimate or statement;
- verbs 'estimate of', 'forecast of', 'outlook stated', 'guidance of', 'as shown', 'presentation' and bare dates became 'stated'; other words inside the brackets (e.g. 'horizon at least 2-3 years', 'CB issued Apr 2026') moved to the note; '(forecast)', '(outlook)' suffixes were dropped from period_fiscal.
- Not touched: [I] rows, reported figures, dated events with their own verb (published, effective, resolved, record date), Teradyne reported quarters, and 'n/a (preprint)' / 'n/a (conference material)' publications.

Changed rows by branch: CY 45, F 144, M 15, P 58, Q 58, T 13 (CY calendar-year; F forecast period; M manual; P past -> statement quarter; Q present quarter; T third-party or undated -> statement quarter). Total 333.

**Spot-check of 20 changes by hand** (cited page re-opened; statement date = document date printed on page 1 or coded in the IR file name):

| id | after | page re-read | what the statement is about | result |
|---|---|---|---|---|
| A1-310 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) | FY2025 Q4 notes p.5 (printed April 27, 2026) | FY2025 Q4 call-option income called one-off (past) | MATCH |
| A1-315 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) | Q1 FY2026 Q&A p.4 (file JE_BIZ_260729) | FY2026 Q1 reversal (past) | MATCH |
| A2-013 | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) | FY2025 Q1 notes p.14 (2025年7月29日) | FY2025 Q1 pull-ins (past) | MATCH |
| A2-017 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) | FY2025 Q3 notes p.2 (January 28, 2026) | digestion did not occur (past); was FY2025 Q3 | MATCH |
| A2-057 | FY2026-FY2028 / Apr 2026-Mar 2029 (stated 11 Nov 2026) | IAR 2026 p.23 | planned use of CB funds (forecast) | MATCH |
| A3-012 | FY2022 / Apr 2022-Mar 2023 (stated 31 Jan 2023) | FY2022 Q3 tanshin p.2 (January 31, 2023) | FY2022 forecast maintained (forecast) | MATCH |
| A3-093 | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) | FY2025 Q2 notes p.3 (2025年10月28日) | Q2 one-time SG&A charge (past) | MATCH |
| A3-113 | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) | FY2023 Q1 slides p.12 | Q2 forecast inside Q2 (forecast quarter contains the date) | MATCH |
| A3-221 | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) | FY2025 Q2 notes p.3 | Q2 sales beat July forecast (past) | MATCH |
| A4-314 | n/a (calendar year) / to CY2028-CY2029 (stated 29 Jul 2026) | Q1 FY2026 Q&A p.4 | China share until new fabs ~2028-2029 (forecast) | MATCH |
| A5-081 | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) | IAR 2026 p.24 | CB premium of the Apr 2026 issue (past; note keeps 'CB priced 1 Apr 2026') | MATCH |
| A5-190 | FY2026 end / 31 Mar 2027 (stated 25 Jun 2024) | MTP3 slides p.35 (June 25, 2024) | cash target at end FY2026 (forecast) | MATCH |
| A6-238 | FY2015 Q4 / Jan-Mar 2016 (stated 27 Jan 2016) | FY2015 Q3 results p.4 (January 27, 2016) | 2H 2015 inventory adjustment (past) | MATCH |
| A6-252 | n/a (calendar year) / CY2015 (stated 11 Nov 2026) | IAR 2026 p.77 | SoC tester market size CY2015 (calendar-year metric) | MATCH |
| TH-041 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) | Q2 FY2026 Q&A p.1 | reason for raised FY2026 forecast (forecast period) | MATCH |
| TH-165 | FY2026 Q2 / Jul-Sep 2026 (stated 30 Sep 2026) | Micron release p.4 (September 30, 2026) | HBM supply agreements completed (present) | MATCH |
| TH-173 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) | Teradyne deck p.6 (October 28, 2026) | dual-vendor share range, no period (undated) | MATCH |
| CL-001 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) | Q2 FY2026 Q&A p.1 | TAM growth over unnamed past years (past) | MATCH |
| CL-060 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) | Q1 FY2026 Q&A p.4 | China ~19% of sales, period not stated (present) | MATCH |
| CL-136 | Teradyne Q4 2026 / Oct-Dec 2026 (stated 27 Oct 2026) | Teradyne Q3 2026 release p.1 (October 27, 2026) | Q4 guidance (forecast period) | MATCH |

Caveat: rows citing the Integrated Annual Report 2026 carry 'stated 11 Nov 2026' (the saved file's date, from PDF metadata). The 2026 IR news index lists the report on 16 Oct 2026 (A3 verifier). Either date falls in FY2026 Q3, so no quarter label depends on it.

## 7. Other label fixes

| id(s) | issue | before | after |
|---|---|---|---|
| A2-160 | LTM label drift | FY2025 Q3 to FY2026 Q2 (LTM) | LTM FY2025 Q3-FY2026 Q2 |
| A4-370 | LTM label drift | LTM | LTM FY2025 Q3-FY2026 Q2 |
| A4-371 | LTM label drift | LTM | LTM FY2025 Q3-FY2026 Q2 |
| A6-312 | LTM label drift | FY2025 Q3-FY2026 Q2 | LTM FY2025 Q3-FY2026 Q2 |
| CL-118 | LTM label drift | FY2025 Q3-FY2026 Q2 | LTM FY2025 Q3-FY2026 Q2 |

## 8. Remaining row_check flags (all explained)

| id | flag | explanation |
|---|---|---|
| A1-300 | VALUE 95 not on cited page | The 95% sits in an image table on Investors' Guide 2610 p.5 (text layer has no figures). Re-checked on the rendered page this pass: 'Computing / Communications 90% (FY24), 95% (FY25)'. |
| A5-085 | VALUE 8 not on cited page | IAR 2026 p.24 prints the word 'eight times the issue amount'. |
| A5-131 | VALUE 11 not on cited page | The value is the date 2021-11-17, printed as 'November 17, 2021' on 81st ASR p.165. |

## 9. Statements in _verify_summaries.json that this pass supersedes (file not edited)

| Module / field | Summary says | Now |
|---|---|---|
| A2 handoff_inputs (inventory signal) | 'FY2026 Q1-Q2 cost of sales includes an undisclosed one-time write-down reversal' | named for FY2026 Q1 and for 1H; whether any fell in Q2 is not disclosed (A2-052, A2-180) |
| CL handoff_inputs (main strength) | 'operating margin 55.9% [F] (CL-025), which includes a 1H inventory write-down reversal' | the 1H OPM (54.0%) includes it; whether the Q2 55.9% does is not disclosed |
| CL B1-4 (C4) | ''approximately 19%' [C] (CL-060)' | [F] (CL-060), matching A4-312 |
| A1 remaining_doubts / handoff | FY2025 one-off SG&A only in Q4, amount not disclosed | also a named one-time SG&A charge in FY2025 Q2, about JPY 2 bn (A1-511; link A1-512 Medium); Q4 amount still not disclosed |
| A3 remaining_doubts | possible A1 mis-dating of the one-off SG&A to Q4 | resolved: both Q2 and Q4 FY2025 had a named one-off SG&A item (section 3) |
| A2 / TH / CL remaining_doubts | modules mix two conventions for statement labels | resolved: one rule for all modules (section 6) |

## 10. Files changed

- parts CSV: A1 (A1-511..A1-515 added; tags A1-314, A1-497), A2, A3 (tags A3-093, A3-229; A3-063 period), A4, A5, A6, TH, CL (tag CL-060) - content changes in section 11, label changes in section 12 and `calc/XM_period_labels.out.txt`.
- parts md: A1.md (one-off table (f): FY2025 Q2 row and FY2025 variant; YoY one-off paragraph; 'periods with no named one-off' corrected; tags of A1-314/A1-497), A1_gaps.md (FY2025 Q2/Q3 gap lines), A2.md (Q2 split gap line), A3.md (FY2025 items, slot table FY2025 Q2 and FY2026 Q2, reversal sentence), A3_gaps.md (Q2 charge gap line), A5.md (one-off table rows), A6.md (quarterly table FY2025 Q2, n/d note, reversal sentence), CL.md (C4 tag, C5/B2 NVIDIA basis, C6 reversal wording, margin table, MTP3 variant).
- calc: A1_oneoffs.py, A3_quarter_record.py, A3_annual_record.py, A5_buybacks_returns.py, A6_cycle.py (also A6_quarterly_series.csv, A6_cycle_metrics.json), CL_margin_mtp3.py - all re-run with python3 -I; diffs limited to the new FY2025 Q2 lines and the reversal wording; no existing [I] value changed. New: XM_consistency.py, XM_period_labels.py and their .out.txt; quote_check_report_v3.csv; row_check_v3.csv.
- evidence.csv regenerated with merge_parts.py (2,385 rows).

## 11. Content changes, row by row

| id(s) | issue | before | after |
|---|---|---|---|
| A1-314 (tag) | tag conflict with A3-227/CL-031 (same quote): value is the reported Q2 financial income | [C] | [F] |
| A1-314 (note) | tag |  | Tag [F] to match A3-227 and CL-031 (same quote): 14.7 bn is the reported figure; 'mainly period-end valuation gains' is management's description of its make-up (Q2 valuation gains 13,096 by YTD difference, A1_oneoffs). [reconcile XM 2026-11-21] |
| A1-497 (tag) | same structure as A1-314: value is the reported Q1 financial income | [C] | [F] |
| A1-497 (note) | tag | Next lines: 'primarily due to valuation gains related to strategic investments. These gains mainly reflected period-end valuation gains on investments in investment fund.' No 'one-off' or 'one-time' wording in the Q1 ... | Next lines: 'primarily due to valuation gains related to strategic investments. These gains mainly reflected period-end valuation gains on investments in investment fund.' No 'one-off' or 'one-time' wording in the Q1 or Q2 FY2026 notes, Q&A or tanshin. Tag ... |
| A3-229 (tag) | tag conflict with A1-316/A2-180/A5-229/CL-073 (same quote): untestable attribution, no amount | [F] | [C] |
| A3-229 (note) | tag |  | Tag [C] to match A1-316, A2-180, A5-229 and CL-073 (same quote). The reversal was first named for FY2026 Q1 (A1-315, Q1 FY2026 Q&A A9); whether any of it fell in FY2026 Q2 is NOT DISCLOSED. [reconcile XM 2026-11-21] |
| CL-060 (tag) | tag conflict with A4-312 (same quote) | [C] | [F] |
| CL-060 (note) | tag |  | Tag [F] to match A4-312 (same quote): a historical share printed in a company document, testable against the ship-to chart (FY2026 Q1 18.9%, A4-356; FY2026 Q2 18.9%, A4-357). Period and basis of the 19% are not stated. [reconcile XM 2026-11-21] |
| A3-093 (tag) | one-off attribution rows are [C] in every module (A1-311, A5-227) | [F] | [C] |
| A3-093 (claim) | one-off SG&A: amount found on p.9 of the same notes | Management: Q2 FY2025 SG&A included a one time charge related to a growth investment (amount not given) | Management: the FY2025 Q2 (Jul-Sep 2025) QoQ rise in SG&A was associated with a one time charge related to a growth investment (no amount in this sentence; the same notes p.9 print about JPY 2 bn of Q2 expenses for initiatives to enhance competitiveness, A1... |
| A3-093 (note) | one-off SG&A |  | Tag [C] like the other one-off attributions (A1-311, A5-227). A separate one-off SG&A item was named for FY2025 Q4 (A1-311). [reconcile XM 2026-11-21] |
| A1-311 (note) | one-off SG&A |  | A second, separate one-off SG&A item was named for FY2025 Q2 (A3-093; about JPY 2 bn per A1-511, link A1-512 Medium). For FY2025 Q4 no amount is printed in the notes, Q&A, slides, tanshin or ASR84. [reconcile XM 2026-11-21] |
| A5-227 (note) | one-off SG&A | Added by verifier (one-off rule). | Added by verifier (one-off rule). A separate one-time SG&A charge was named for FY2025 Q2 (A3-093; about JPY 2 bn per A1-511, link A1-512 Medium). [reconcile XM 2026-11-21] |
| A1-511 ((new row)) | one-off SG&A amount found on the cited notes p.9 |  | FY2025 Q2 briefing notes: in Q2 FY2025 the company booked approximately JPY 2 billion of expenses related to initiatives to enhance medium- to long-term competitiveness (part of the explanation of the Q2 SG&A increase) |
| A1-512 ((new row)) | link between p.3 one-time charge and p.9 amount |  | The ~JPY 2 bn of Q2 FY2025 expenses for initiatives to enhance competitiveness (A1-511) is taken as the amount of the 'one time charge related to a growth investment' that management named for FY2025 Q2 (A3-093) |
| A1-513 ((new row)) | one-off rule: FY2025 Q2 with and without the named charge |  | Operating margin FY2025 Q2 (Jul-Sep 2025): 41.3% reported, 42.0% without the ~2,000 million one-time SG&A charge (OI 108,483 -> 110,483; sales 262,957) |
| A1-514 ((new row)) | one-off rule: FY2025 variant |  | Operating margin FY2025 (Apr 2025-Mar 2026) without all named items that have an amount, incl. the ~2,000 million FY2025 Q2 one-time SG&A charge: 44.2% (OI 498,616); 44.0% without the divestiture gain only (A1-472); reported 44.2% |
| A1-515 ((new row)) | one-off rule: YoY with comparison-base item |  | Operating income YoY, FY2026 Q2 vs FY2025 Q2 without the ~2,000 million one-time SG&A charge in the base quarter: +141.5% (266,819 vs 110,483); reported +146.0% |
| A3-287 (note) | one-off rule | inputs: A3-134, A3-135, A3-136, A3-137, A3-172, A3-173, A3-174, A3-187; script: research/out/advantest/calc/A3_quarter_record.py; reason: direct comparison with the company's printed Q2 forecast | inputs: A3-134, A3-135, A3-136, A3-137, A3-172, A3-173, A3-174, A3-187; script: research/out/advantest/calc/A3_quarter_record.py; reason: direct comparison with the company's printed Q2 forecast One-off: management named a one-time SG&A charge for this quar... |
| A1-315 (note) | reversal: quarter attribution made explicit |  | Named for FY2026 Q1 in the Q1 FY2026 Q&A A9 (A1-315) and for 1H FY2026 in the Q2 FY2026 Q&A A5 (A1-316); no document says whether any of it fell in FY2026 Q2 (Jul-Sep 2026), and no amount is printed. [reconcile XM 2026-11-21] |
| A1-316 (note) | reversal: quarter attribution made explicit |  | Named for FY2026 Q1 in the Q1 FY2026 Q&A A9 (A1-315) and for 1H FY2026 in the Q2 FY2026 Q&A A5 (A1-316); no document says whether any of it fell in FY2026 Q2 (Jul-Sep 2026), and no amount is printed. [reconcile XM 2026-11-21] |
| A2-052 (note) | reversal: quarter attribution made explicit |  | Named for FY2026 Q1 in the Q1 FY2026 Q&A A9 (A1-315) and for 1H FY2026 in the Q2 FY2026 Q&A A5 (A1-316); no document says whether any of it fell in FY2026 Q2 (Jul-Sep 2026), and no amount is printed. [reconcile XM 2026-11-21] |
| A2-180 (note) | reversal: quarter attribution made explicit |  | Named for FY2026 Q1 in the Q1 FY2026 Q&A A9 (A1-315) and for 1H FY2026 in the Q2 FY2026 Q&A A5 (A1-316); no document says whether any of it fell in FY2026 Q2 (Jul-Sep 2026), and no amount is printed. [reconcile XM 2026-11-21] |
| A5-229 (note) | reversal: quarter attribution made explicit | Added by verifier (one-off rule). Continues: "reversal of inventory write-down." | Added by verifier (one-off rule). Continues: "reversal of inventory write-down." Named for FY2026 Q1 in the Q1 FY2026 Q&A A9 (A1-315) and for 1H FY2026 in the Q2 FY2026 Q&A A5 (A1-316); no document says whether any of it fell in FY2026 Q2 (Jul-Sep 2026), an... |
| CL-073 (note) | reversal: quarter attribution made explicit |  | Named for FY2026 Q1 in the Q1 FY2026 Q&A A9 (A1-315) and for 1H FY2026 in the Q2 FY2026 Q&A A5 (A1-316); no document says whether any of it fell in FY2026 Q2 (Jul-Sep 2026), and no amount is printed. [reconcile XM 2026-11-21] |
| CL-025 (note) | reversal: Q2 attribution not established | Speaker notes sentence: operating income was 266.8 billion JPY with an operating margin of 55.9%. Same on slides p.5; tanshin YTD difference gives 266,819 / 55.9% (CL_crosscheck). Management named a 1H inventory write... | Speaker notes sentence: operating income was 266.8 billion JPY with an operating margin of 55.9%. Same on slides p.5; tanshin YTD difference gives 266,819 / 55.9% (CL_crosscheck). Management named an inventory write-down reversal for FY2026 Q1 (A1-315) and ... |
| CL-122 (note) | reversal: Q2 attribution not established | inputs: CL-025, CL-078, CL-135, CL-073; script: research/out/advantest/calc/CL_margin_mtp3.py; reason: different accounting bases and portfolios, and Advantest's figure includes an undisclosed one-time inventory reversal | inputs: CL-025, CL-078, CL-135, CL-073; script: research/out/advantest/calc/CL_margin_mtp3.py; reason: different accounting bases and portfolios, and Advantest's Q2 figure may include part of the one-time inventory write-down reversal named for Q1 and 1H (w... |
| CL-121 (note) | one-off SG&A FY2025 Q2 variant | inputs: CL-037, CL-033, CL-038, CL-077, CL-073; script: research/out/advantest/calc/CL_margin_mtp3.py; reason: FY2026 is a forecast and its 1H inventory reversal cannot be removed (amount not disclosed); simple averag... | inputs: CL-037, CL-033, CL-038, CL-077, CL-073, A1-512; script: research/out/advantest/calc/CL_margin_mtp3.py; reason: FY2026 is a forecast and its 1H inventory reversal cannot be removed (amount not disclosed); simple average of annual margins is 41.8% / 4... |
| A3-063 (period_fiscal) | full-year segment-note figure; match A1-306 and A6-223 | FY2024 Q4 | FY2024 |
| A3-063 (period_calendar) | full-year segment-note figure | Jan-Mar 2025 | Apr 2024-Mar 2025 |
| A3-063 (note) | period |  | Period set to FY2024 because p.15 prints the full-year segment note (as A1-306 and A6-223); the Q4 booking rests on management's statement A3-064. [reconcile XM 2026-11-21] |
| A1-307 (period_fiscal) | value holds two items in two quarters; match CL-038 | FY2024 Q4 | FY2024 Q4; FY2025 Q1 |
| A1-307 (period_calendar) | match CL-038 | Jan-Mar 2025 | Jan-Mar 2025; Apr-Jun 2025 |
| CL-104 (period_calendar) | same rule as A4-336 (published 9 Nov 2026); CL keeps the deadline as the catalyst date | Jan-Mar 2027 (10 Jan 2027) | Jan-Mar 2027 (deadline 10 Jan 2027; published 9 Nov 2026) |
| CL-068 (claim) | state basis (group vs entity) | FY2025 net sales to the NVIDIA Group and TSMC (each above 10% of net sales) | FY2025 net sales to the NVIDIA Group and TSMC on the customer-group basis of Note 6(6) (each above 10% of net sales) |
| CL-119 (claim) | state basis (group vs entity) | FY2025 customer concentration: NVIDIA Group 21.6% and TSMC 11.1% of net sales (together 32.7%); the other three top-five customers together about 17 points | FY2025 customer concentration on the customer-group basis (Note 6(6)): NVIDIA Group 21.6% and TSMC 11.1% of net sales (together 32.7%); the other three top-five customers together about 17 points. Single-entity basis: NVIDIA International, Inc. 20.2% (CL-069) |
| TH-019 (claim) | overlapping quote with A5-161 [C]: separate fact (partnership) from plan (stake) | Partnership with probe-card maker Micronics Japan with planned minority stake (Feb 2025) | Partnership with probe-card maker Micronics Japan announced 27 Feb 2025; the planned minority stake was a company plan at that date ([C] A5-161); the parent held 150,000 MJC shares at 31 Mar 2025 ([F] A5-237) |

## 12. Period-label changes, row by row (from `calc/XM_period_labels.out.txt`)

| id | issue (branch) | before | after |
|---|---|---|---|
| A1-297 | [C] F | FY2026 (forecast) / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A1-302 | [C] Q | FY2025 Q4 / Jan-Mar 2026 (28 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) |
| A1-303 | [C] Q | FY2025 Q4 / Jan-Mar 2026 (28 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) |
| A1-304 | [C] CY | n/a (calendar year) / CY2025 | n/a (calendar year) / CY2025 (stated 28 Jan 2026) |
| A1-305 | [C] P | FY2025 / Apr 2025-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Statement refers to FY2025 (Apr 2025-Mar 2026). |
| A1-310 | [C] P | FY2025 Q4 / Jan-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Statement refers to FY2025 Q4 (Jan-Mar 2026). |
| A1-311 | [C] P | FY2025 Q4 / Jan-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Statement refers to FY2025 Q4 (Jan-Mar 2026). |
| A1-315 | [C] P | FY2026 Q1 / Apr-Jun 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A1-316 | [C] P | FY2026 1H / Apr-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 1H (Apr-Sep 2026). |
| A1-317 | [C] P | FY2025 Q1 / Apr-Jun 2025 | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) - note: Statement refers to FY2025 Q1 (Apr-Jun 2025). |
| A1-318 | [C] P | FY2024 Q4 / Jan-Mar 2025 | FY2025 Q1 / Apr-Jun 2025 (stated 25 Apr 2025) - note: Statement refers to FY2024 Q4 (Jan-Mar 2025). |
| A1-350 | [C] P | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 Q2 (Jul-Sep 2026). |
| A1-494 | [C] Q | FY2026 Q1 / Apr-Jun 2026 (26 Jun 2026) | FY2026 Q1 / Apr-Jun 2026 (stated 26 Jun 2026) |
| A1-495 | [C] Q | FY2024 Q1 / Apr-Jun 2024 (25 Jun 2024) | FY2024 Q1 / Apr-Jun 2024 (stated 25 Jun 2024) |
| A1-496 | [C] F | FY2026 (forecast) / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A1-498 | [C] P | FY2026 Q1 / Apr-Jun 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A2-001 | [F] P | FY2021 Q4 / Jan-Mar 2022 (stated 27 Apr 2022) | FY2022 Q1 / Apr-Jun 2022 (stated 27 Apr 2022) - note: Statement refers to FY2021 Q4 (Jan-Mar 2022). |
| A2-002 | [F] P | FY2021 Q4 / Jan-Mar 2022 (stated 27 Apr 2022) | FY2022 Q1 / Apr-Jun 2022 (stated 27 Apr 2022) - note: Statement refers to FY2021 Q4 (Jan-Mar 2022). |
| A2-013 | [C] P | FY2025 Q1 / Apr-Jun 2025 (stated 29 Jul 2025) | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) - note: Statement refers to FY2025 Q1 (Apr-Jun 2025). |
| A2-014 | [C] F | FY2025 2H (outlook) / Oct 2025-Mar 2026 (stated 29 Jul 2025) | FY2025 2H / Oct 2025-Mar 2026 (stated 29 Jul 2025) |
| A2-015 | [C] P | FY2025 Q2 / Jul-Sep 2025 (stated 28 Oct 2025) | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) - note: Statement refers to FY2025 Q2 (Jul-Sep 2025). |
| A2-016 | [C] F | FY2025 2H (outlook) / Oct 2025-Mar 2026 (stated 28 Oct 2025) | FY2025 2H / Oct 2025-Mar 2026 (stated 28 Oct 2025) |
| A2-017 | [C] P | FY2025 Q3 / Oct-Dec 2025 (stated 28 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) - note: Statement refers to FY2025 Q3 (Oct-Dec 2025). |
| A2-018 | [C] P | FY2025 Q3 / Oct-Dec 2025 (stated 28 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) - note: Statement refers to FY2025 Q3 (Oct-Dec 2025). |
| A2-019 | [C] F | FY2025 2H (outlook) / Oct 2025-Mar 2026 (stated 28 Jan 2026) | FY2025 2H / Oct 2025-Mar 2026 (stated 28 Jan 2026) |
| A2-022 | [C] Q | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026; horizon at least 2-3 years) | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Period detail moved from period_calendar: horizon at least 2-3 years. |
| A2-024 | [C] Q | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026; horizon this fiscal year into next) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Period detail moved from period_calendar: horizon this fiscal year into next. |
| A2-025 | [C] CY | n/a (calendar year) / CY2027 (outlook stated 28 Oct 2026) | n/a (calendar year) / CY2027 (stated 28 Oct 2026) |
| A2-026 | [C] F | FY2026 2H (forecast) vs FY2026 1H / Oct 2026-Mar 2027 vs Apr-Sep 2026 (stated 28 Oct 2026) | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) - note: Compared with FY2026 1H. |
| A2-027 | [C] F | FY2026 2H (forecast) / Oct 2026-Mar 2027 (stated 28 Oct 2026) | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A2-028 | [C] CY | n/a (calendar year) / CY2027 (outlook stated 28 Oct 2026) | n/a (calendar year) / CY2027 (stated 28 Oct 2026) |
| A2-052 | [C] P | FY2026 Q1 / Apr-Jun 2026 (stated 29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A2-053 | [C] P | FY2026 1H / Apr-Sep 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 1H (Apr-Sep 2026). |
| A2-054 | [C] P | FY2026 Q1 / Apr-Jun 2026 (stated 29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A2-057 | [C] M | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026; bonds issued Apr 2026) | FY2026-FY2028 / Apr 2026-Mar 2029 (stated 11 Nov 2026) - note: Period detail moved from period_calendar: bonds issued Apr 2026. Forecast period matched to A5-193 and the planned-use dates A5-072/A5-073 (by Mar 2029 / Mar... |
| A2-155 | [C] Q | FY2026 Q1 / Apr-Jun 2026 (stated in report filed 26 Jun 2026) | FY2026 Q1 / Apr-Jun 2026 (stated 26 Jun 2026) |
| A2-165 | [C] F | FY2026 2H (outlook) / Oct 2026-Mar 2027 (stated 28 Oct 2026) | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A2-166 | [C] F | FY2026 2H (forecast, Q3 and Q4) / Oct 2026-Mar 2027 (stated 28 Oct 2026) | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) - note: Forecast covers Q3 and Q4. |
| A2-173 | [F] P | FY2025 Q2 / Jul-Sep 2025 (stated 28 Oct 2025) | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) - note: Statement refers to FY2025 Q2 (Jul-Sep 2025). |
| A2-180 | [C] P | FY2026 1H / Apr-Sep 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 1H (Apr-Sep 2026). |
| A2-187 | [C] P | FY2022 1H / Apr-Sep 2022 (stated 27 Oct 2022) | FY2022 Q3 / Oct-Dec 2022 (stated 27 Oct 2022) - note: Statement refers to FY2022 1H (Apr-Sep 2022). |
| A3-007 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-008 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-010 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-011 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-012 | [C] F | FY2022 / Apr 2022-Mar 2023 | FY2022 / Apr 2022-Mar 2023 (stated 31 Jan 2023) |
| A3-013 | [C] F | FY2022 / Apr 2022-Mar 2023 | FY2022 / Apr 2022-Mar 2023 (stated 31 Jan 2023) |
| A3-014 | [C] F | FY2022 / Apr 2022-Mar 2023 | FY2022 / Apr 2022-Mar 2023 (stated 31 Jan 2023) |
| A3-018 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 26 Apr 2023) |
| A3-019 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 26 Apr 2023) |
| A3-020 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 26 Apr 2023) |
| A3-021 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 26 Apr 2023) |
| A3-022 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 26 Jul 2023) |
| A3-023 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-024 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-025 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-026 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-027 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-028 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Jan 2024) |
| A3-029 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Jan 2024) |
| A3-030 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Jan 2024) |
| A3-031 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 31 Jan 2024) |
| A3-040 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 26 Apr 2024) |
| A3-041 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 26 Apr 2024) |
| A3-042 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 26 Apr 2024) |
| A3-043 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 26 Apr 2024) |
| A3-044 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 31 Jul 2024) |
| A3-045 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 31 Jul 2024) |
| A3-046 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 31 Jul 2024) |
| A3-047 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 31 Jul 2024) |
| A3-048 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-049 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-050 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-051 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-052 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-053 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 29 Jan 2025) |
| A3-054 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 29 Jan 2025) |
| A3-055 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 29 Jan 2025) |
| A3-056 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 29 Jan 2025) |
| A3-057 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 29 Jan 2025) |
| A3-066 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-067 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-068 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-069 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-070 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 25 Apr 2025) |
| A3-071 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 29 Jul 2025) |
| A3-072 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 29 Jul 2025) |
| A3-073 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 29 Jul 2025) |
| A3-074 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 29 Jul 2025) |
| A3-075 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 29 Jul 2025) |
| A3-076 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-077 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-078 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-079 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-080 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-081 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Jan 2026) |
| A3-082 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Jan 2026) |
| A3-083 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Jan 2026) |
| A3-084 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Jan 2026) |
| A3-085 | [C] F | FY2025 / Apr 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (stated 28 Jan 2026) |
| A3-093 | [C] P | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) - note: Statement refers to FY2025 Q2 (Jul-Sep 2025). |
| A3-094 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 27 Apr 2026) |
| A3-095 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 27 Apr 2026) |
| A3-096 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 27 Apr 2026) |
| A3-097 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 27 Apr 2026) |
| A3-098 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 27 Apr 2026) |
| A3-099 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 29 Jul 2026) |
| A3-100 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 29 Jul 2026) |
| A3-101 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 29 Jul 2026) |
| A3-102 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 29 Jul 2026) |
| A3-103 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 29 Jul 2026) |
| A3-104 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-105 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-106 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-107 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-108 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-110 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-111 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-112 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-113 | [C] Q | FY2023 Q2 / Jul-Sep 2023 | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) |
| A3-114 | [C] Q | FY2023 Q2 / Jul-Sep 2023 | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) |
| A3-115 | [C] Q | FY2023 Q2 / Jul-Sep 2023 | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) |
| A3-116 | [C] F | FY2023 2H / Oct 2023-Mar 2024 | FY2023 2H / Oct 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-117 | [C] F | FY2023 2H / Oct 2023-Mar 2024 | FY2023 2H / Oct 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-118 | [C] F | FY2023 2H / Oct 2023-Mar 2024 | FY2023 2H / Oct 2023-Mar 2024 (stated 31 Oct 2023) |
| A3-119 | [C] Q | FY2023 Q4 / Jan-Mar 2024 | FY2023 Q4 / Jan-Mar 2024 (stated 31 Jan 2024) |
| A3-120 | [C] Q | FY2023 Q4 / Jan-Mar 2024 | FY2023 Q4 / Jan-Mar 2024 (stated 31 Jan 2024) |
| A3-121 | [C] Q | FY2023 Q4 / Jan-Mar 2024 | FY2023 Q4 / Jan-Mar 2024 (stated 31 Jan 2024) |
| A3-122 | [C] Q | FY2024 Q2 / Jul-Sep 2024 | FY2024 Q2 / Jul-Sep 2024 (stated 31 Jul 2024) |
| A3-123 | [C] Q | FY2024 Q2 / Jul-Sep 2024 | FY2024 Q2 / Jul-Sep 2024 (stated 31 Jul 2024) |
| A3-124 | [C] Q | FY2024 Q2 / Jul-Sep 2024 | FY2024 Q2 / Jul-Sep 2024 (stated 31 Jul 2024) |
| A3-125 | [C] F | FY2024 2H / Oct 2024-Mar 2025 | FY2024 2H / Oct 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-126 | [C] F | FY2024 2H / Oct 2024-Mar 2025 | FY2024 2H / Oct 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-127 | [C] F | FY2024 2H / Oct 2024-Mar 2025 | FY2024 2H / Oct 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-128 | [C] F | FY2024 2H / Oct 2024-Mar 2025 | FY2024 2H / Oct 2024-Mar 2025 (stated 30 Oct 2024) |
| A3-129 | [C] Q | FY2024 Q4 / Jan-Mar 2025 | FY2024 Q4 / Jan-Mar 2025 (stated 29 Jan 2025) |
| A3-130 | [C] Q | FY2024 Q4 / Jan-Mar 2025 | FY2024 Q4 / Jan-Mar 2025 (stated 29 Jan 2025) |
| A3-131 | [C] Q | FY2024 Q4 / Jan-Mar 2025 | FY2024 Q4 / Jan-Mar 2025 (stated 29 Jan 2025) |
| A3-132 | [C] Q | FY2024 Q4 / Jan-Mar 2025 | FY2024 Q4 / Jan-Mar 2025 (stated 29 Jan 2025) |
| A3-133 | [C] Q | FY2024 Q4 / Jan-Mar 2025 | FY2024 Q4 / Jan-Mar 2025 (stated 29 Jan 2025) |
| A3-134 | [C] Q | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) |
| A3-135 | [C] Q | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) |
| A3-136 | [C] Q | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) |
| A3-137 | [C] Q | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) |
| A3-138 | [C] F | FY2025 2H / Oct 2025-Mar 2026 | FY2025 2H / Oct 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-139 | [C] F | FY2025 2H / Oct 2025-Mar 2026 | FY2025 2H / Oct 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-140 | [C] F | FY2025 2H / Oct 2025-Mar 2026 | FY2025 2H / Oct 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-141 | [C] F | FY2025 2H / Oct 2025-Mar 2026 | FY2025 2H / Oct 2025-Mar 2026 (stated 28 Oct 2025) |
| A3-142 | [C] Q | FY2025 Q4 / Jan-Mar 2026 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) |
| A3-143 | [C] Q | FY2025 Q4 / Jan-Mar 2026 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) |
| A3-144 | [C] Q | FY2025 Q4 / Jan-Mar 2026 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) |
| A3-145 | [C] Q | FY2025 Q4 / Jan-Mar 2026 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) |
| A3-146 | [C] Q | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A3-147 | [C] Q | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A3-148 | [C] Q | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A3-149 | [C] Q | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A3-150 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-151 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-152 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-153 | [C] F | FY2026 2H / Oct 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| A3-221 | [F] P | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) - note: Statement refers to FY2025 Q2 (Jul-Sep 2025). |
| A3-222 | [F] P | FY2025 Q2 / Jul-Sep 2025 | FY2025 Q3 / Oct-Dec 2025 (stated 28 Oct 2025) - note: Statement refers to FY2025 Q2 (Jul-Sep 2025). |
| A3-223 | [C] P | FY2025 Q3 / Oct-Dec 2025 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) - note: Statement refers to FY2025 Q3 (Oct-Dec 2025). |
| A3-224 | [C] P | FY2025 Q3 / Oct-Dec 2025 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) - note: Statement refers to FY2025 Q3 (Oct-Dec 2025). |
| A3-225 | [F] P | FY2025 Q4 / Jan-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Statement refers to FY2025 Q4 (Jan-Mar 2026). |
| A3-226 | [C] P | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 Q2 (Jul-Sep 2026). |
| A3-229 | [C] P | FY2026 1H / Apr-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 1H (Apr-Sep 2026). |
| A3-230 | [C] F | FY2024 / Apr 2024-Mar 2025 | FY2024 / Apr 2024-Mar 2025 (stated 29 Jan 2025) |
| A3-231 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 29 Jul 2026) |
| A3-234 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A3-235 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A3-236 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A3-237 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A3-238 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A3-239 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A3-242 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| A3-243 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| A3-244 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| A3-245 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| A3-246 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| A3-247 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| A3-252 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 11 Nov 2026) |
| A3-253 | [C] F | FY2027 Q1 / Apr-Jun 2027 (around May 2027; stated 28 Oct 2026) | FY2027 Q1 / Apr-Jun 2027 (stated 28 Oct 2026) - note: Period detail moved from period_calendar: around May 2027. |
| A3-312 | [C] F | FY2022 / Apr 2022-Mar 2023 | FY2022 / Apr 2022-Mar 2023 (stated 31 Jan 2023) |
| A3-314 | [C] F | FY2023 / Apr 2023-Mar 2024 | FY2023 / Apr 2023-Mar 2024 (stated 26 Jul 2023) |
| A4-305 | [C] Q | FY2022 Q3 / Oct-Dec 2022 (27 Oct 2022) | FY2022 Q3 / Oct-Dec 2022 (stated 27 Oct 2022) |
| A4-306 | [C] Q | FY2022 Q3 / Oct-Dec 2022 (27 Oct 2022) | FY2022 Q3 / Oct-Dec 2022 (stated 27 Oct 2022) |
| A4-307 | [C] Q | FY2024 Q1 / Apr-Jun 2024 (26 Apr 2024) | FY2024 Q1 / Apr-Jun 2024 (stated 26 Apr 2024) |
| A4-308 | [C] Q | FY2024 Q1 / Apr-Jun 2024 (26 Apr 2024) | FY2024 Q1 / Apr-Jun 2024 (stated 26 Apr 2024) |
| A4-309 | [C] Q | FY2024 Q4 / Jan-Mar 2025 (29 Jan 2025) | FY2024 Q4 / Jan-Mar 2025 (stated 29 Jan 2025) |
| A4-310 | [C] Q | FY2025 Q1 / Apr-Jun 2025 (25 Apr 2025) | FY2025 Q1 / Apr-Jun 2025 (stated 25 Apr 2025) |
| A4-311 | [C] Q | FY2026 Q1 / Apr-Jun 2026 (27 Apr 2026) | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) |
| A4-312 | [F] Q | FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A4-313 | [C] Q | FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A4-314 | [C] M | FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026) | n/a (calendar year) / to CY2028-CY2029 (stated 29 Jul 2026) - note: Forecast horizon matched to CL-061 (same Q&A answer). |
| A4-318 | [C] Q | FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) |
| A4-423 | [C] Q | FY2019 Q2 / Jul-Sep 2019 (25 Jul 2019) | FY2019 Q2 / Jul-Sep 2019 (stated 25 Jul 2019) |
| A4-424 | [C] Q | FY2023 Q2 / Jul-Sep 2023 (26 Jul 2023) | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) |
| A5-056 | [C] P | FY2025 end / 31 Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 26 Jun 2026) - note: Statement refers to FY2025 end (31 Mar 2026). |
| A5-072 | [C] F | FY2026-FY2028 / Apr 2026-Mar 2029 | FY2026-FY2028 / Apr 2026-Mar 2029 (stated 26 Jun 2026) |
| A5-073 | [C] F | FY2026 / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 26 Jun 2026) |
| A5-074 | [C] F | FY2026-FY2027 / Apr 2026-Mar 2028 | FY2026-FY2027 / Apr 2026-Mar 2028 (stated 26 Jun 2026) |
| A5-081 | [F] P | FY2026 Q1 / Apr-Jun 2026 (CB priced 1 Apr 2026; stated 11 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Period detail moved from period_calendar: CB priced 1 Apr 2026. Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A5-082 | [C] P | FY2026 Q1 / Apr-Jun 2026 (CB issued Apr 2026; stated 11 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Period detail moved from period_calendar: CB issued Apr 2026. Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A5-083 | [C] P | FY2026 Q1 / Apr-Jun 2026 (CB issued Apr 2026; stated 11 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Period detail moved from period_calendar: CB issued Apr 2026. Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A5-085 | [C] P | FY2026 Q1 / Apr-Jun 2026 (CB issued Apr 2026; stated 11 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Period detail moved from period_calendar: CB issued Apr 2026. Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| A5-086 | [F] M | FY2014 onward / 2014 issue; status stated 11 Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Former label: FY2014 onward / 2014 issue; status stated 11 Nov 2026. Refers to the CB issued in 2014. |
| A5-090 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 26 Jun 2026) |
| A5-091 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 26 Jun 2026) |
| A5-127 | [C] Q | FY2026 Q3 / Oct-Dec 2026 (28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| A5-137 | [C] Q | FY2021 Q3 / Oct-Dec 2021 (17 Nov 2021) | FY2021 Q3 / Oct-Dec 2021 (stated 17 Nov 2021) |
| A5-160 | [C] Q | FY2024 Q4 / Jan-Mar 2025 (announced 9 Jan 2025) | FY2024 Q4 / Jan-Mar 2025 (stated 9 Jan 2025) |
| A5-161 | [C] Q | FY2024 Q4 / Jan-Mar 2025 (27 Feb 2025) | FY2024 Q4 / Jan-Mar 2025 (stated 27 Feb 2025) |
| A5-185 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 26 Jun 2026) |
| A5-186 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A5-187 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A5-188 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A5-189 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A5-190 | [C] F | FY2026 end / 31 Mar 2027 | FY2026 end / 31 Mar 2027 (stated 25 Jun 2024) |
| A5-191 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A5-192 | [C] F | FY2024-FY2026 / Apr 2024-Mar 2027 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 25 Jun 2024) |
| A5-195 | [C] P | FY2025 end / 31 Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 26 Jun 2026) - note: Statement refers to FY2025 end (31 Mar 2026). |
| A5-227 | [C] P | FY2025 Q4 / Jan-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Statement refers to FY2025 Q4 (Jan-Mar 2026). |
| A5-229 | [C] P | FY2026 1H / Apr-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 1H (Apr-Sep 2026). |
| A6-238 | [C] P | FY2015 9M / Apr-Dec 2015 | FY2015 Q4 / Jan-Mar 2016 (stated 27 Jan 2016) - note: Statement refers to FY2015 9M (Apr-Dec 2015). |
| A6-239 | [C] P | FY2015 Q3 / Oct-Dec 2015 | FY2015 Q4 / Jan-Mar 2016 (stated 27 Jan 2016) - note: Statement refers to FY2015 Q3 (Oct-Dec 2015). |
| A6-240 | [C] P | FY2016 1H / Apr-Sep 2016 | FY2016 Q3 / Oct-Dec 2016 (stated 26 Oct 2016) - note: Statement refers to FY2016 1H (Apr-Sep 2016). |
| A6-241 | [C] P | FY2018 / Apr 2018-Mar 2019 | FY2019 Q1 / Apr-Jun 2019 (stated 25 Apr 2019) - note: Statement refers to FY2018 (Apr 2018-Mar 2019). |
| A6-242 | [C] Q | FY2019 Q1 / Apr-Jun 2019 (25 Apr 2019) | FY2019 Q1 / Apr-Jun 2019 (stated 25 Apr 2019) |
| A6-243 | [C] Q | FY2019 Q1 / Apr-Jun 2019 (25 Apr 2019) | FY2019 Q1 / Apr-Jun 2019 (stated 25 Apr 2019) |
| A6-244 | [C] P | FY2019 Q1 / Apr-Jun 2019 | FY2019 Q2 / Jul-Sep 2019 (stated 24 Jul 2019) - note: Statement refers to FY2019 Q1 (Apr-Jun 2019). |
| A6-245 | [C] P | FY2019 Q1 / Apr-Jun 2019 | FY2019 Q2 / Jul-Sep 2019 (stated 24 Jul 2019) - note: Statement refers to FY2019 Q1 (Apr-Jun 2019). |
| A6-246 | [C] P | FY2022 9M / Apr-Dec 2022 | FY2022 Q4 / Jan-Mar 2023 (stated 31 Jan 2023) - note: Statement refers to FY2022 9M (Apr-Dec 2022). |
| A6-247 | [C] Q | FY2023 Q1 / Apr-Jun 2023 (26 Apr 2023) | FY2023 Q1 / Apr-Jun 2023 (stated 26 Apr 2023) |
| A6-248 | [C] P | FY2023 Q1 / Apr-Jun 2023 | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) - note: Statement refers to FY2023 Q1 (Apr-Jun 2023). |
| A6-249 | [C] P | FY2023 Q1 / Apr-Jun 2023 | FY2023 Q2 / Jul-Sep 2023 (stated 26 Jul 2023) - note: Statement refers to FY2023 Q1 (Apr-Jun 2023). |
| A6-250 | [C] P | FY2023 / Apr 2023-Mar 2024 | FY2024 Q1 / Apr-Jun 2024 (stated 26 Apr 2024) - note: Statement refers to FY2023 (Apr 2023-Mar 2024). |
| A6-251 | [C] P | FY2008 / Apr 2008-Mar 2009 | FY2009 Q1 / Apr-Jun 2009 (stated 27 Apr 2009) - note: Statement refers to FY2008 (Apr 2008-Mar 2009). |
| A6-252 | [C] CY | n/a (calendar year) / CY2015 | n/a (calendar year) / CY2015 (stated 11 Nov 2026) |
| A6-253 | [C] CY | n/a (calendar year) / CY2016 | n/a (calendar year) / CY2016 (stated 11 Nov 2026) |
| A6-254 | [C] CY | n/a (calendar year) / CY2018 | n/a (calendar year) / CY2018 (stated 11 Nov 2026) |
| A6-255 | [C] CY | n/a (calendar year) / CY2019 | n/a (calendar year) / CY2019 (stated 11 Nov 2026) |
| A6-256 | [C] CY | n/a (calendar year) / CY2022 | n/a (calendar year) / CY2022 (stated 11 Nov 2026) |
| A6-257 | [C] CY | n/a (calendar year) / CY2023 | n/a (calendar year) / CY2023 (stated 11 Nov 2026) |
| A6-258 | [C] CY | n/a (calendar year) / CY2015 | n/a (calendar year) / CY2015 (stated 11 Nov 2026) |
| A6-259 | [C] CY | n/a (calendar year) / CY2016 | n/a (calendar year) / CY2016 (stated 11 Nov 2026) |
| A6-260 | [C] CY | n/a (calendar year) / CY2018 | n/a (calendar year) / CY2018 (stated 11 Nov 2026) |
| A6-261 | [C] CY | n/a (calendar year) / CY2019 | n/a (calendar year) / CY2019 (stated 11 Nov 2026) |
| A6-262 | [C] CY | n/a (calendar year) / CY2022 | n/a (calendar year) / CY2022 (stated 11 Nov 2026) |
| A6-263 | [C] CY | n/a (calendar year) / CY2023 | n/a (calendar year) / CY2023 (stated 11 Nov 2026) |
| TH-009 | [F] P | FY2025 Q1 / Apr-Jun 2025 (change effective from FY2025 Q1; stated 29 Jul 2025) | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) - note: Period detail moved from period_calendar: change effective from FY2025 Q1. Statement refers to FY2025 Q1 (Apr-Jun 2025). |
| TH-041 | [C] M | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) - note: Explains the raised FY2026 forecast; labelled like CL-071. |
| TH-047 | [C] P | FY2025 / Apr 2025-Mar 2026 (Integrated Annual Report dated 11 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Statement refers to FY2025 (Apr 2025-Mar 2026). |
| TH-050 | [C] F | FY2024 / Apr 2024-Mar 2025 (expectation stated 26 Apr 2024) | FY2024 / Apr 2024-Mar 2025 (stated 26 Apr 2024) |
| TH-074 | [C] Q | FY2024 Q3 / Oct-Dec 2024 (10 Dec 2024) | FY2024 Q3 / Oct-Dec 2024 (stated 10 Dec 2024) |
| TH-082 | [C] Q | FY2024 Q4 / Jan-Mar 2025 (12 Feb 2025) | FY2024 Q4 / Jan-Mar 2025 (stated 12 Feb 2025) |
| TH-083 | [C] Q | FY2025 Q3 / Oct-Dec 2025 (10 Dec 2025) | FY2025 Q3 / Oct-Dec 2025 (stated 10 Dec 2025) |
| TH-084 | [C] Q | FY2025 Q3 / Oct-Dec 2025 (10 Dec 2025) | FY2025 Q3 / Oct-Dec 2025 (stated 10 Dec 2025) |
| TH-085 | [C] Q | FY2026 Q1 / Apr-Jun 2026 (22 Apr 2026) | FY2026 Q1 / Apr-Jun 2026 (stated 22 Apr 2026) |
| TH-086 | [C] Q | FY2026 Q3 / Oct-Dec 2026 (17 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 17 Nov 2026) |
| TH-088 | [C] P | FY2025 / Apr 2025-Mar 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) - note: Statement refers to FY2025 (Apr 2025-Mar 2026). |
| TH-096 | [C] CY | n/a (calendar year) / CY2025 (estimate as of 27 Apr 2026) | n/a (calendar year) / CY2025 (stated 27 Apr 2026) |
| TH-097 | [C] CY | n/a (calendar year) / CY2025 (estimate as of 27 Apr 2026) | n/a (calendar year) / CY2025 (stated 27 Apr 2026) |
| TH-098 | [C] CY | n/a (calendar year) / CY2025 (estimate as of 27 Apr 2026) | n/a (calendar year) / CY2025 (stated 27 Apr 2026) |
| TH-099 | [C] CY | n/a (calendar year) / CY2024 (final, as shown 27 Apr 2026) | n/a (calendar year) / CY2024 (stated 27 Apr 2026) |
| TH-100 | [C] CY | n/a (calendar year) / CY2024 (final, as shown 25 Apr 2025) | n/a (calendar year) / CY2024 (stated 25 Apr 2025) |
| TH-101 | [C] CY | n/a (calendar year) / CY2026 (forecast as of 28 Oct 2026) | n/a (calendar year) / CY2026 (stated 28 Oct 2026) |
| TH-102 | [C] CY | n/a (calendar year) / CY2026 (forecast as of 28 Oct 2026) | n/a (calendar year) / CY2026 (stated 28 Oct 2026) |
| TH-103 | [C] CY | n/a (calendar year) / CY2026 (forecast as of 28 Oct 2026) | n/a (calendar year) / CY2026 (stated 28 Oct 2026) |
| TH-104 | [C] CY | n/a (calendar year) / CY2024 (estimate of 31 Jan 2024) | n/a (calendar year) / CY2024 (stated 31 Jan 2024) |
| TH-105 | [C] CY | n/a (calendar year) / CY2024 (estimate of 31 Jan 2024) | n/a (calendar year) / CY2024 (stated 31 Jan 2024) |
| TH-106 | [C] CY | n/a (calendar year) / CY2024 (estimate of 26 Apr 2024) | n/a (calendar year) / CY2024 (stated 26 Apr 2024) |
| TH-107 | [C] CY | n/a (calendar year) / CY2025 (estimate of 29 Jan 2025) | n/a (calendar year) / CY2025 (stated 29 Jan 2025) |
| TH-108 | [C] CY | n/a (calendar year) / CY2025 (estimate of 29 Jan 2025) | n/a (calendar year) / CY2025 (stated 29 Jan 2025) |
| TH-109 | [C] CY | n/a (calendar year) / CY2025 (estimate of 29 Jul 2025) | n/a (calendar year) / CY2025 (stated 29 Jul 2025) |
| TH-110 | [C] CY | n/a (calendar year) / CY2025 (estimate of 28 Oct 2025) | n/a (calendar year) / CY2025 (stated 28 Oct 2025) |
| TH-111 | [C] CY | n/a (calendar year) / CY2026 (estimate of 28 Jan 2026) | n/a (calendar year) / CY2026 (stated 28 Jan 2026) |
| TH-112 | [C] CY | n/a (calendar year) / CY2026 (estimate of 28 Jan 2026) | n/a (calendar year) / CY2026 (stated 28 Jan 2026) |
| TH-113 | [C] CY | n/a (calendar year) / CY2026 (estimate of 27 Apr 2026) | n/a (calendar year) / CY2026 (stated 27 Apr 2026) |
| TH-114 | [C] CY | n/a (calendar year) / CY2026 (estimate of 29 Jul 2026) | n/a (calendar year) / CY2026 (stated 29 Jul 2026) |
| TH-119 | [C] CY | n/a (calendar year) / CY2024; CY2025 (as shown 27 Apr 2026) | n/a (calendar year) / CY2024; CY2025 (stated 27 Apr 2026) |
| TH-121 | [C] CY | n/a (calendar year) / CY2024-CY2026 average (assumption of 25 Jun 2024) | n/a (calendar year) / CY2024-CY2026 average (stated 25 Jun 2024) |
| TH-122 | [C] CY | n/a (calendar year) / CY2024-CY2026 average (assumption of 25 Jun 2024) | n/a (calendar year) / CY2024-CY2026 average (stated 25 Jun 2024) |
| TH-131 | [C] F | FY2026 (forecast) / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| TH-134 | [C] F | FY2026 (forecast) / Apr 2026-Mar 2027 | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| TH-165 | [C] T | n/a (Micron statement) / Jul-Sep 2026 (stated 30 Sep 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 30 Sep 2026) |
| TH-168 | [C] T | n/a (Teradyne statement) / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-169 | [C] M | n/a (calendar year) / CY2025 vs Jan-Aug 2026 (stated 28 Oct 2026) | n/a (calendar year) / CY2025; Jan-Aug 2026 (stated 28 Oct 2026) - note: Calendar wording matched to CL-018. |
| TH-170 | [C] T | n/a (Teradyne statement) / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-171 | [C] T | n/a (Teradyne statement) / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-172 | [C] T | n/a (Teradyne statement) / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-173 | [C] T | n/a (Teradyne statement) / Oct-Dec 2026 (presentation 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-174 | [C] T | n/a (Teradyne statement) / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-175 | [C] CY | n/a (calendar year) / CY2025; target model (stated 28 Oct 2026; model updated 3 Feb 2026) | n/a (calendar year) / CY2025; target model (stated 28 Oct 2026) - note: Period detail moved from period_calendar: model updated 3 Feb 2026. |
| TH-177 | [F] T | n/a (Teradyne statement) / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) |
| TH-178 | [C] T | n/a (Teradyne statement) / Jan-Mar 2025 (presentation 12 Mar 2025) | FY2024 Q4 / Jan-Mar 2025 (stated 12 Mar 2025) |
| TH-179 | [C] CY | n/a (calendar year) / CY2023; CY2024; CY2025 (as shown 27 Apr 2026) | n/a (calendar year) / CY2023; CY2024; CY2025 (stated 27 Apr 2026) |
| CL-001 | [C] M | n/a (calendar year) / past few years to CY2025 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Former label: n/a (calendar year) / past few years to CY2025. Statement about the past few years (no years named); labelled like TH-042. |
| CL-003 | [C] F | FY2026 Q4 / Jan-Mar 2027 (Jan 2027 briefing; stated 28 Oct 2026) | FY2026 Q4 / Jan-Mar 2027 (stated 28 Oct 2026) - note: Period detail moved from period_calendar: Jan 2027 briefing. |
| CL-006 | [C] CY | n/a (calendar year) / CY2026 (estimate of 28 Oct 2026) | n/a (calendar year) / CY2026 (stated 28 Oct 2026) |
| CL-007 | [C] CY | n/a (calendar year) / CY2024-CY2026e (estimate of 28 Oct 2026) | n/a (calendar year) / CY2024-CY2026e (stated 28 Oct 2026) |
| CL-009 | [C] P | FY2025 Q1 / Apr-Jun 2025 (stated 29 Jul 2025) | FY2025 Q2 / Jul-Sep 2025 (stated 29 Jul 2025) - note: Statement refers to FY2025 Q1 (Apr-Jun 2025). |
| CL-011 | [C] P | FY2025 Q3 / Oct-Dec 2025 (stated 28 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) - note: Statement refers to FY2025 Q3 (Oct-Dec 2025). |
| CL-016 | [S] M | FY2026 Q2 / Jul-Sep 2026 (asked 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (asked 28 Oct 2026) - note: Statement refers to FY2026 Q2 (Jul-Sep 2026). |
| CL-017 | [F] P | FY2026 Q2 / Jul-Sep 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 Q2 (Jul-Sep 2026). |
| CL-019 | [C] M | Teradyne 2H 2026 / Jul-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to Teradyne 2H 2026 (Jul-Dec 2026). Teradyne statement on its 2H 2026 compute program timing. |
| CL-020 | [C] M | Teradyne Q4 2026 / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to Teradyne Q4 2026 (Oct-Dec 2026). |
| CL-033 | [C] F | FY2026 / Apr 2026-Mar 2027 (forecast of 28 Oct 2026) | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| CL-034 | [C] F | FY2026 / Apr 2026-Mar 2027 (forecast of 28 Oct 2026) | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| CL-035 | [C] F | FY2026 2H / Oct 2026-Mar 2027 (forecast of 28 Oct 2026) | FY2026 2H / Oct 2026-Mar 2027 (stated 28 Oct 2026) |
| CL-036 | [C] F | FY2026 / Apr 2026-Mar 2027 (forecast of 28 Oct 2026) | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| CL-039 | [C] CY | n/a (calendar year) / CY2024; CY2025 (estimate of 28 Oct 2026) | n/a (calendar year) / CY2024; CY2025 (stated 28 Oct 2026) |
| CL-040 | [C] M | n/a (calendar year) / not specified (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Former label: n/a (calendar year) / not specified. No timing given; labelled like TH-117. |
| CL-042 | [C] CY | n/a (calendar year) / CY2023-CY2025 (estimate of 27 Apr 2026) | n/a (calendar year) / CY2023-CY2025 (stated 27 Apr 2026) |
| CL-044 | [C] M | Teradyne Q4 2026 / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to Teradyne Q4 2026 (Oct-Dec 2026). |
| CL-048 | [C] T | n/a (no date) / mid-term, not specified (presented 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Former label: n/a (no date) / mid-term, not specified. |
| CL-051 | [C] CY | n/a (calendar year) / CY2025 (estimate of 27 Apr 2026) | n/a (calendar year) / CY2025 (stated 27 Apr 2026) |
| CL-053 | [C] F | FY2026 / Apr 2026-Mar 2027 (forecast of 28 Oct 2026) | FY2026 / Apr 2026-Mar 2027 (stated 28 Oct 2026) |
| CL-054 | [C] M | Teradyne Q4 2026 / Oct-Dec 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to Teradyne Q4 2026 (Oct-Dec 2026). |
| CL-060 | [F] P | FY2026 Q1 / Apr-Jun 2026 (stated 29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Statement refers to FY2026 Q1 (Apr-Jun 2026). |
| CL-062 | [S] M | FY2025 Q3 / Oct-Dec 2025 (published 30 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (published 30 Jan 2026) - note: Quarter corrected: 30 Jan 2026 falls in FY2025 Q4 (Jan-Mar 2026). |
| CL-073 | [C] P | FY2026 1H / Apr-Sep 2026 (stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Statement refers to FY2026 1H (Apr-Sep 2026). |
| CL-076 | [C] P | FY2025 Q4 / Jan-Mar 2026 (stated 27 Apr 2026) | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) - note: Statement refers to FY2025 Q4 (Jan-Mar 2026). |
| CL-077 | [C] F | FY2024-FY2026 avg / Apr 2024-Mar 2027 | FY2024-FY2026 avg / Apr 2024-Mar 2027 (stated 28 Oct 2025) |
| CL-080 | [C] M | Teradyne Q4 2026 / Oct-Dec 2026 (call date not given; stated 28 Oct 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Period detail moved from period_calendar: call date not given. Statement refers to Teradyne Q4 2026 (Oct-Dec 2026). Teradyne's Q4 2026 call date is not given. |
| CL-084 | [C] T | n/a (no date) / not specified (stated 12 Nov 2026) | FY2026 Q3 / Oct-Dec 2026 (stated 12 Nov 2026) - note: Former label: n/a (no date) / not specified. |
| CL-085 | [C] T | n/a (no date) / not specified (stated 29 Jul 2026) | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) - note: Former label: n/a (no date) / not specified. |
| CL-102 | [C] F | FY2027 Q1 / Apr-Jun 2027 (around May 2027; stated 28 Oct 2026) | FY2027 Q1 / Apr-Jun 2027 (stated 28 Oct 2026) - note: Period detail moved from period_calendar: around May 2027. |
| CL-130 | [C] F | FY2025 / Apr 2025-Mar 2026 (forecast of 28 Jan 2026) | FY2025 / Apr 2025-Mar 2026 (stated 28 Jan 2026) |
| CL-132 | [C] P | FY2025 Q3 / Oct-Dec 2025 (stated 28 Jan 2026) | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) - note: Statement refers to FY2025 Q3 (Oct-Dec 2025). |
| CL-136 | [C] M | Teradyne Q4 2026 / Oct-Dec 2026 (guidance of 27 Oct 2026) | Teradyne Q4 2026 / Oct-Dec 2026 (stated 27 Oct 2026) |
| CL-138 | [C] CY | n/a (calendar year) / CY2026 (estimate of 28 Jan 2026) | n/a (calendar year) / CY2026 (stated 28 Jan 2026) |
| CL-143 | [C] T | n/a (no date) / not specified (stated 28 Oct 2026; update possibly Jan 2027) | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) - note: Period detail moved from period_calendar: update possibly Jan 2027. Former label: n/a (no date) / not specified. |

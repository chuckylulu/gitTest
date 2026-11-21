# KLA (KLAC): A3 guidance record, A6 cycle, Q5 supply limits

Fiscal year ends June 30. Q1 FY27 = Jul-Sep 2026 (latest reported). Per-share figures: pre-split up to and including Q3 FY26 results; post-split from Q4 FY26 results onward (10-for-1, effective after the Nasdaq close on 2026-06-11) [F] A3-027.
Calc scripts: `research/out/kla/calc/a3_guidance_record.py`, `a6_cycle_drawdowns.py`, `q5_supply_calc.py` (run with `python3 -I`).

## Premise issues
- BRIEF says there is no Q3 FY25 shareholder letter. One is saved: `research/sources/kla/2025-04-30_kla_shareholder-letter-Q3FY25.pdf` (16 pp). I used it [F] A3-005.
- The Q3 FY25 earnings-release text extraction is garbled (font encoding). I took the exact Q3 FY25 revenue ($3,063,029K) from the comparative column of the Q3 FY26 release and from the Q3 FY25 letter.
- Prior file (kla_metrology_audit.md, line 33) tests the 2022 Investor Day **CY2026** target against **FY26** revenue ($13.58B, Jul 2025-Jun 2026). That mixes the fiscal and calendar years. CY2026 ends Dec 2026 and is not yet reported.
- Prior file cites the FY26 10-K for "optical component bottlenecks" and "Gen4/Gen5 lead times past 12 months". The 10-K names neither optics nor Gen4/Gen5. Those statements come from the earnings call (secondary) and the Investor Day.
- The Q2 FY26 Motley Fool transcript reads "2026 revenue will grow mid-single digits compared to 2025". The letter says H1 CY26 vs H2 CY25 [F] A3-033. I treat this as a transcription error. The Q3 FY26 transcript says "first half of 2016" where it means 2026 [S] Q5-026.
- The Q3 FY25 letter calls 63.0% non-GAAP GM "about 50 basis points higher than the midpoint of guidance". The guided midpoint was 62% (Q2 FY25 letter p.11; slides p.12), so 63.0% is 100 bps above it, at the top of the range. This is an internal inconsistency in KLA's letter. I classified it as in-line [I] A3-006.

## A3 Guidance record

Rule (stated once and used for every metric): result **above the top** of the guided range = BEAT; **inside or equal to an end** = IN-LINE; **below the bottom** = MISS. Guidance is taken from the prior quarter's shareholder letter. EPS guidance given before the split (Q4 FY26, issued 2026-04-29) is divided by 10.

| Quarter (calendar) | Revenue guide → actual ($M) | Non-GAAP GM guide → actual | Non-GAAP EPS guide → actual | GAAP EPS guide → actual | Evidence |
|---|---|---|---|---|---|
| Q2 FY25 (Oct-Dec 2024) | 2,950±150 → 3,076.9 IN-LINE | 61.5±1 → 61.7 IN | 7.75±0.60 → 8.20 IN | 7.45±0.60 → **6.16 MISS** | [F] A3-001/002, [I] A3-003 |
| Q3 FY25 (Jan-Mar 2025) | 3,000±150 → 3,063.0 IN | 62±1 → 63.0 IN (top) | 8.05±0.60 → 8.41 IN | 7.77±0.60 → 8.16 IN | [F] A3-004/005, [I] A3-006 |
| Q4 FY25 (Apr-Jun 2025) | 3,075±150 → 3,174.7 IN | 63±1 → 63.2 IN | 8.53±0.78 → **9.38 BEAT** | 8.28±0.78 → 9.06 IN (=top) | [F] A3-007/008, [I] A3-009 |
| Q1 FY26 (Jul-Sep 2025) | 3,150±150 → 3,209.7 IN | 62±1 → 62.5 IN | 8.53±0.77 → 8.81 IN | 8.28±0.77 → 8.47 IN | [F] A3-010/011, [I] A3-012 |
| Q2 FY26 (Oct-Dec 2025) | 3,225±150 → 3,297.1 IN | 62±1 → 62.6 IN | 8.70±0.78 → 8.85 IN | 8.46±0.78 → 8.68 IN | [F] A3-013/014, [I] A3-015 |
| Q3 FY26 (Jan-Mar 2026) | 3,350±150 → 3,415.1 IN | 61.75±1 → 62.2 IN | 9.08±0.78 → 9.40 IN | 8.85±0.78 → 9.12 IN | [F] A3-016/017, [I] A3-018 |
| Q4 FY26 (Apr-Jun 2026) | 3,575±200 → 3,657.6 IN | 61.75±1 → 62.4 IN | 0.987±0.10* → 1.05 IN | 0.966±0.10* → 1.04 IN | [F] A3-019/020, [I] A3-021 |
| Q1 FY27 (Jul-Sep 2026) | 4,000±200 → 4,136.0 IN | 62.5±1 → 62.7 IN | 1.16±0.10 → 1.22 IN | 1.14±0.10 → 1.18 IN | [F] A3-022/023, [I] A3-024 |
| **Q2 FY27 (Oct-Dec 2026), current** | 4,700±200 | 62.5±1 | 1.44±0.11 | 1.41±0.11 | [F] A3-026 |

\* Pre-split guidance of $9.87±$1.00 (non-GAAP) and $9.66±$1.00 (GAAP), divided by 10.

**Count over 8 quarters** [I] A3-025:
- Revenue: 0 beat, 8 in-line, 0 miss. Revenue came in above the guided midpoint every quarter, by +1.9% to +4.3%.
- Non-GAAP GM: 0 beat, 8 in-line, 0 miss.
- Non-GAAP EPS: 1 beat (Q4 FY25), 7 in-line, 0 miss.
- GAAP EPS: 0 beat, 7 in-line, 1 miss (Q2 FY25).

One-off items management named:
- Q2 FY25 GAAP EPS of $6.16 included a $239.1M goodwill and intangible impairment ($1.76/share) [F] A3-028. Without it, GAAP EPS was $7.92, inside the range (6.85-8.05) [I] A3-003. The impairment was not in the guidance.
- The Q4 FY25 non-GAAP EPS beat came from the tax rate: 9.9% actual vs 13.5% guided. At the guided rate, EPS would have been $9.00, inside the range [F] A3-029. Q3 FY25 at the guided rate: $8.55, also in-line.

**Guidance maintained late in a period and then missed: none found.** KLA does not update quarterly guidance within the quarter. Its calendar-year views were raised, never cut, over 2025-2026. Examples: CY25 GM went from 62%±0.5 to 62.5%±0.5; CY26 wafer-equipment (WFE) outlook went from low $120B (core) to >$140B, then low-$150B, then mid-$150B [F] A3-030, A3-033 to A3-035.

### Calendar-year and long-range statements (last 3) and outcomes
| Statement | Made | Outcome | Evidence |
|---|---|---|---|
| CY2025: WFE up mid-single digits from high-$90B; KLA to outperform; non-GAAP GM ~62%±50bps (raised to 62.5%±50bps in Apr 2025) | 2025-01-30 | KLA revenue +17% to $12.745B, against KLA's own estimate of low-double-digit industry growth. GM 62.8%, inside the raised range. **Met/beat** | [F] A3-030, A3-031; [I] A3-032 |
| CY2026: H1 CY26 up mid-single digits vs H2 CY25 (Jan 2026); KLA growth "high teen" YoY (Apr 2026); H2/H1 ~20% (Jul), then ~25% (Oct); GM ~62%±50bps | 2026-01-29 to 2026-10-28 | H1 CY26 came in +8.7% vs H2 CY25 (above "mid-single"). Using the Q2 FY27 midpoint, CY26 is about $15.91B (+24.8%), above "high teen", and H2/H1 is +24.9%. CY26 GM about 62.5%, at the top of the range. **Exceeded so far; not final** | [F] A3-033 to A3-035; [I] A3-036 |
| 2022 Investor Day CY2026 model: revenue $14B±$0.5B; non-GAAP GM ~63%; OM 41-43%; EPS $38±$1.50 (pre-split = $3.80±$0.15) | 2022-06-16 | Implied CY26: revenue about $15.91B (above $14.5B top), non-GAAP OM about 45.2%, non-GAAP EPS about $4.65 post-split ($46.5 pre-split): all **beat**. Non-GAAP GM about 62.5%, **below** the ~63% target; management named DRAM cost and tariffs | [F] A3-037, A3-040, [C] A3-038, [I] A3-039 |
| Pending: 2030 model of $26B±$2.5B revenue, OM 45-47%, EPS $84±$8 (pre-split) | 2026-03-12 | Due 2031 | [F] A3-040 |

## A6 Cycle: last two downturns

**Why these two.** Test used: reported quarterly revenue falls at least 10% from a quarterly peak and stays below that peak for at least 3 quarters.
- **2022-23** passes.
- **2018-19** fails on reported revenue: Q2 FY19 to Q3 FY19 was only −2.0%, because Orbotech (consolidated from 2019-02-20) added $161.3M [F] A6-020. Excluding Orbotech, Q3 FY19 was −16.4%, but that can only be computed for one quarter [I] A6-025.
- **2020** (COVID) was −5.7%.
- The next qualifying episode is the **FY2013-FY2016 (CY2012-15)** trough. Revenue stayed below the Jun-2012 peak until Apr-Jun 2016 [I] A6-023.
- 2008-09 was deeper (−59.4% revenue; GAAP OM 25.6% → −12.4%) but older [I] A6-025.

| | Downturn 1: CY2022-23 | Downturn 2: CY2012-15 |
|---|---|---|
| Revenue peak | Q2 FY23 (Oct-Dec 2022) $2,983.9M [F] A6-001 | Q4 FY12 (Apr-Jun 2012) $892.5M [F] A6-014 |
| Revenue trough | Q4 FY23 (Apr-Jun 2023) $2,355.1M, **−21.1%**. Second dip in Q3 FY24 (Jan-Mar 2024) at $2,359.8M | First trough Q2 FY13 (Oct-Dec 2012) $673.0M, −24.6%. Deepest Q1 FY16 (Jul-Sep 2015) $642.6M, **−28.0%** |
| Quarters below peak | 7 (peak regained in Q2 FY25) | 15 (peak regained in Q4 FY16) |
| GAAP OM at peak → low | 40.2% → 29.5% in Q2 FY24, **−10.7 pts**, including a $219.0M impairment. Excluding impairments: 34.2% in Q3 FY24, **−6.0 pts** | 35.7% → 17.0% in Q1 FY15 (Jul-Sep 2014), **−18.7 pts**. At the Sep-2015 revenue low: 25.0% (26.1% excluding the $7.1M restructuring) |
| Non-GAAP OM at peak → low | 42.4% → 36.8% in Q3 FY24, **−5.7 pts**. From the margin peak in Q1 FY23 (44.1%): −7.3 pts | NOT RETRIEVED (tried: no KLA-Tencor 2012-15 earnings releases fetched) |
| One-offs named by management | Impairments of $219.0M (Q2 FY24) and $70.5M (Q3 FY24); restructuring of $19.1M (Q3 FY23) and $8.1M (Q4 FY23) [F] A6-005, A6-006, A6-009 | Restructuring of $22.4M (Q4 FY15) and $7.1M (Q1 FY16) [F] A6-019. One-offs in Q1 FY15: not identified |
| Evidence | [I] A6-010, A6-011, A6-012 | [I] A6-023, A6-024 |

Method notes:
- KLA's FY23-FY24 income statement has no operating-income line. I used GAAP OI = revenue − cost of revenues − R&D − SG&A − impairment.
- Non-GAAP OI = GAAP OI + the pre-tax adjustments booked in those lines, from the release tables [F] A6-008. KLA did not publish this figure, so these numbers are my derivation (Medium confidence).
- 2012-15 operating income is as reported in the 10-K quarterly notes and the 10-Q tables [F] A6-014 to A6-018.

## Q5 Supply limits (statements since Jan 2025)

**Components named:**
- Optics (glass and "volume optics"): the longest-lead item, named by the CFO on the Q2 FY26 call [S] Q5-024 and the Q1 FY27 call [S] Q5-029, and by the CEO [S] Q5-025.
- Investor Day slide 153 [C] Q5-018 groups the parts:
  - low-volume, sole-sourced complex parts: optics, sensors, lasers;
  - high-volume, mostly sole-sourced parts: volume optics, stages, motion control;
  - Tier 2-4: semiconductors, electronic components.
- DRAM chips for the image-processing computers shipped with the tools. These are a **cost** problem, not a shipment limit: KLA says it "secured the required supply" [C] Q5-012. Filings: suppliers discontinued certain DRAM chips and prices rose [F] Q5-004, Q5-005.
- Rare-earth elements: a risk factor only, with no stated impact [F] Q5-008.

**Lead times (months):**
- Historically about 6 months.
- 7-9 months in Oct 2025 [S] Q5-022.
- "Increasing due to supply constraints, limiting first-half growth" in Jan 2026 [C] Q5-010.
- Material-to-ship time fence of almost 60 weeks in Mar 2026 [C] Q5-019.
- About 12 months on average in Oct 2026, with Gen4/Gen5 longer [S] Q5-027, Q5-028.
- Lead-time months: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog and Item 1A; Q1 FY27 10-Q; letters Q2 FY26 to Q1 FY27). They appear only in the secondary transcripts.

**Capacity actions:**
- About $250M+ invested in supplier capacity over roughly 2 years; suppliers get about 8 quarters of visibility; KLA does not cancel orders [C] Q5-018, Q5-021.
- Q1 FY27 letter: KLA worked with strategic partners over the past year to raise their capacity [C] Q5-015.
- "We are adding capacity" [C] Q5-014.
- CapEx to trend up to $600-800M a year [S] Q5-032.
- 10-K: KLA gives financial support to vendors to add capacity [F] Q5-009.

**Effect on backlog conversion and revenue timing:**
- H1 CY26 capacity was set "inside a lead time" before demand accelerated [C] Q5-020, and was "virtually sold out" [S] Q5-023.
- H2 CY26 is about 20-25% above H1 as long-lead capacity comes online [C] Q5-013, Q5-016.
- Backlog rose from $7.86B to $12.57B in FY26 (+59.9%). The 10-K attributes this to AI-driven demand and lists supply-chain constraints among the timing variables [F] Q5-002, [I] Q5-003.
- Purchase commitments rose from $5.97B to $8.87B in Q1 FY27 (+48.6%) [F] Q5-006, [I] Q5-007.
- Revenue lost or deferred because of supply: NOT DISCLOSED (read: Q2 FY26 to Q1 FY27 letters; FY26 10-K MD&A). The CFO said "We don't really look at what we could have done" [I] Q5-034.
- FY26 backlog share to convert within 12 months: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog). The FY25 10-K gave 71-76% [F] Q5-001.

**DRAM cost on gross margin:**
- 75-100 bps hit to CY26 GM (Jan 2026) [F] Q5-011.
- About 100 bps "over the next several quarters" (Apr 2026) [C] Q5-012.
- FY26 10-K: adverse GM impact "in fiscal 2027" (Jul 2026-Jun 2027) [F] Q5-005.
- Oct 2026: "persistently high" memory costs; system redesign under way to use less memory [C] Q5-017.

## Prior-claim check (kla_metrology_audit.md lines 21-68 and line ~1033, in scope)
| Prior claim | Verdict | Evidence |
|---|---|---|
| 2022 Investor Day CY2026 target $14.0B ± $500M, 41-43% OM: "MET" | **CORRECTED.** CY2026 is not complete, and the prior used FY26 revenue. On a CY26 implied basis (Q2 FY27 guidance midpoint), revenue of about $15.9B **exceeds** the top of the range and OM of about 45% exceeds 41-43%. The same target model's ~63% GM is **not met** (about 62.5%). EPS target $38±1.50 pre-split, implied about $46.5 | A3-037, A3-039, A3-040 |
| Optical component bottlenecks constrained H1 CY26 shipments | **CONFIRMED** (company statements [C] and calls [S]; not in the 10-K, which the prior cited) | Q5-010, Q5-020, Q5-024, Q5-030 |
| Gen4/Gen5 lead times extended past 12 months | **CONFIRMED [S] only** (Q1 FY27 call: average about 12 months, Gen4/Gen5 "longer"); not in KLA documents | Q5-027, Q5-028 |
| Backlog $7.86B (Jun 2025) → $12.57B (Jun 2026) lifted by optical bottlenecks | Figures **CONFIRMED**; cause **CORRECTED**. The 10-K attributes the increase to "strong demand driven by the AI infrastructure buildout" | Q5-002 |
| Management planned flat CY26 capacity | **CORRECTED.** No capacity plan statement found. Oct 2025 guidance was H1 CY26 revenue "roughly flat to modestly up" vs H2 CY25. CFO (Oct 2026, [S]): they had expected 2026 "pretty flat". H1 capacity decisions were made inside the lead time [C] | Q5-020, Q5-031 |
| DRAM memory pricing pressuring image-processing compute costs into H2 CY2027 | **CORRECTED.** Filings say a GM impact "in fiscal 2027" (to Jun 2027 = H1 CY2027). Letters say pricing persists "through at least calendar 2026". No H2 CY2027 statement found | Q5-005, Q5-011, Q5-012, Q5-017 |
| Current KLA tool delivery lead time ~12 months average | **CONFIRMED [S]** (Q1 FY27 call, 2026-10-28) | Q5-027 |
| Q2 FY27 guidance $4.70B ± $200M; Q1 FY27 non-GAAP OM 46.1% | **CONFIRMED** | A3-026, A3-041 |

## Gaps
- Q4 FY26 earnings-call transcript (2026-07-28): NOT RETRIEVED (tried: fool.com URL patterns for 07/28 and 07/29 returned 404; GuruFocus is paywalled; not worked around).
- Non-GAAP operating margin for the 2012-15 downturn: NOT RETRIEVED (tried: no KLA-Tencor FY12-FY16 earnings releases fetched).
- Lead times in months: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog and Item 1A; Q1 FY27 10-Q Item 1A; letters Q2 FY26 to Q1 FY27). Secondary sources only.
- Revenue deferred by supply constraints: NOT DISCLOSED (read: letters Q2 FY26 to Q1 FY27; FY26 10-K MD&A).
- 12-month conversion share of the FY26 backlog: NOT DISCLOSED (read: FY26 10-K Item 1 Backlog).
- Q4 FY19 revenue excluding Orbotech: NOT DISCLOSED (read: FY19 10-K Note 20; Q3 FY19 10-Q revenue-by-product table).
- One-off items in Q1 FY15 (Jul-Sep 2014, the OM low): NOT RETRIEVED (tried: the Q1 FY15 10-Q was not fetched; the FY15 10-K quarterly note has no operating detail).
- Q3 FY25 earnings release: text extraction unreadable (font encoding). Values taken from the Q3 FY25 letter and the Q3 FY26 release comparative.

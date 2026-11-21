# CL verification log (adversarial verifier, 2026-11-21)

Scope: `parts/CL.csv`, `parts/CL.md`, `parts/CL_gaps.md`, `calc/CL_*.py`. Every [F]/[C]/[S] row of the original 132 was re-opened on its cited page. There were fewer than 80 key [F]/[C] rows, so no sampling was used. The checks covered value, unit, sign, period (single quarter vs YTD vs year), fiscal and calendar label, page, quote and tag.

## Counts

| Item | Count |
|---|---|
| Rows checked (original) | 132 |
| OK, unchanged | 22 |
| Fixed, substantive (value, page, quote, source, claim or note content) | 26 |
| Fixed, wrong period label (row_check flag or wrong quarter) | 27 |
| Label/note harmonisation only (content verified correct; "(stated <date>)", "n/a (calendar year)", Teradyne quarter labels, cross-check notes) | 57 |
| Removed | 0 |
| Added | 11 (CL-133 to CL-143) |
| Final rows | 143 |
| quote_check | 123 quotes FOUND (112 exact, 11 layout-insensitive); 20 [I] rows have no quote by design; 0 NOT FOUND; 0 page mismatches |
| row_check | 0 flags (was 19) |

## Non-OK rows: substantive fixes and additions

| id | What was checked | Before | After | Result |
|---|---|---|---|---|
| CL-001 | period of "about 50% a year" | CY2023-CY2025 | n/a (calendar year) / "past few years to CY2025"; note: the period is not specified; the chart gives +36% then +50% | FIXED |
| CL-023, CL-091 | nature of Simply Wall St source | note "LLM tool" without source wording | page source quoted: "AnalystLowTarget is a tool utilizing a Large Language Model (LLM)"; [S] context only, removed from ledger evidence (C7 "against") | FIXED |
| CL-024 | quote supports value? | quote was the slide title only; chart label | slides p.5 summary table: "Sales / 売上高 ... 477.7"; tanshin YTD difference 477,727 (CL-141) | FIXED |
| CL-026 | VALUE flag: 71.1 not on cited page | notes p.6 (prints only ">70%") with value ">70% (71.1% on slide p.8)" | slides p.5 table "Gross Margin ... 71.1%"; notes p.6 sentence kept in note | FIXED (real error: value cited to a page that does not print it) |
| CL-030 | source of quarterly totals | chart labels read on p.7 | printed table on slides p.5 (same values) | FIXED |
| CL-042 | quote supports value? | quote was the slide title | "58% Flat YoY 58% +7pts YoY 65%"; note: overall share 65% is not the SoC share 66% | FIXED |
| CL-047 | VALUE flag '2' | "2H 2027" | "second half of 2027" as printed | FALSE FLAG (date wording); value restated as printed |
| CL-048 | quote supports value? | title only | "Key factor for share gain in compute across the mid-term"; phase labels quoted in note | FIXED |
| CL-056, CL-058 | stale note | "file name carries a placeholder date 2026-01-01" | file now carries its printed date 2026-10-05 | FIXED |
| CL-070 | VALUE flag 48 | p.41 only | p.41; p.40 ("approximately 48%" sits at the foot of p.40) | FIXED (page) |
| CL-093 | VALUE flag '12'; JPY 49 not on cited page | IR calendar only; value 2026-12-01; FY2026 / Dec 2026 | primary source switched to the interim-dividend notice ("Effective date December 1, 2026", JPY 49.00); IR calendar and tanshin p.1 agree; FY2026 Q3 / Oct-Dec 2026 (1 Dec 2026) | FIXED |
| CL-095 | record-date conflict | note "conflicts with Share Information page" | note now lists the 84th ASR p.58/p.199, Integrated Report p.40 and the Share Information page (all 15 May) vs this calendar line; FY2026 Q4 label | FIXED |
| CL-096 | AGM date, VALUE flag '07' | value 2026-07-31; FY2026 / Jul 2026 | "31 Jul 2026"; FY2026 Q2 / Jul-Sep 2026 (31 Jul 2026); second document Integrated Report p.40 | FIXED |
| CL-099 | VALUE flag 11000000 | "11,000,000" | "11 million" as printed; FY2026 2H / Oct 2026-Mar 2027 (29 Oct 2026-24 Mar 2027) | FALSE FLAG (unit wording) + period FIXED |
| CL-103 | claim wording vs page | "Zero Coupon CB ... no other bond"; period FY2026 1H | "convertible bonds ... only bonds in the financial-liabilities table"; FY2026 Q2 end / 30 Sep 2026; "Zero Coupon ... due 2031" sourced to the 28 Oct 2026 conversion-price notice | FIXED |
| CL-104 | period missing | blank / Jan 2027 | FY2026 Q4 / Jan-Mar 2027 (10 Jan 2027); value as printed | FIXED |
| CL-105 | period missing | blank / Nov 2026-Jan 2027 | FY2026 2H / Oct 2026-Mar 2027 (19 Nov 2026; 19 Jan 2027) | FIXED |
| CL-108 | VALUE flag '11' | 2026-11-30, "news list" | "Nov 30, 2026" as printed under "Upcoming Event"; Teradyne event label | FALSE FLAG (ISO date) + page section FIXED |
| CL-109 | attribution of TechNews USD 8 bn | [S], compared with the Oct-2026 estimate | note: conflicts with Advantest's own 28 Jan 2026 estimate (CL-138); not used as evidence | FIXED |
| CL-111 | VALUE flag '04' | ISO dates | "Apr.27 (2026); Apr.25 (2025)" as printed; FY2026 Q1; FY2025 Q1 | FALSE FLAG (ISO date) + period FIXED |
| CL-114 | selective comparison | memory vs FY2024 Q3 only (called "peak" in the script) | adds vs FY2025 Q3 (57.3, the chart high): -6.8% | FIXED |
| CL-122 | one-off rule for Teradyne margin | non-GAAP only (24.3 pts) | GAAP 30.8% and non-GAAP 31.6% with Teradyne's named items (25.1 / 24.3 pts) | FIXED |
| CL-126 | record-date reasoning | "two pages disagree" | statutory ASR p.58/p.199 + Integrated Report p.40 + Share Information agree on 15 May; IR calendar line outdated; FY2027 1H | FIXED |
| CL-129 | inference built on an untraceable [S] number | Oct CY26e minus TechNews USD 8 bn = 5.0-6.5 (Low) | company's own Jan-to-Oct 2026 revision of the CY2026 TAM, +2.3 bn (High); TechNews shown as conflicting | FIXED |
| CL-133 | new | - | 84th ASR p.58/p.199: voting-rights record date 15 May; AGM within three months; dividend record dates 30 Sep / 31 Mar [F] | ADDED |
| CL-134 | new | - | Integrated Report p.40: record date changed from 31 Mar to 15 May; 2026 AGM held 31 Jul [F] | ADDED |
| CL-135 | new | - | Teradyne Q3 2026 GAAP OI 402.0 (30.8%), non-GAAP 412.9 (31.6%), named items [F] | ADDED |
| CL-136 | new | - | Teradyne Q4 2026 revenue guide USD 1,250-1,350m [C] (fills the "flat Q4 guide" press gap from the primary document) | ADDED |
| CL-137 | new | - | Teradyne revenue Q3'26 1,306 / Q2'26 1,329 / Q3'25 769; Semi Test 1,072 [F] | ADDED |
| CL-138 | new | - | Advantest 28 Jan 2026 CY2026 estimate: SoC 8.5-9.5, memory 2.2-2.7 USD bn [C] | ADDED |
| CL-139 | new | - | Teradyne -1.7% QoQ, +69.8% YoY; Q4 guide midpoint -0.5% vs Q3 [I] | ADDED |
| CL-140 | new | - | Group CEO: strategic inventory is "gold"; more concerned about meeting demand than about write-downs [C] | ADDED |
| CL-141 | new | - | Q2 single quarter from tanshin YTD: 477,727 / 266,819 / 55.9%, YoY +81.7% [I] | ADDED |
| CL-142 | new | - | FY2026 Q1 tanshin: 367,473 / 189,990; FY2025 Q1 263,776 / 123,952 [F] | ADDED |
| CL-143 | new | - | Q2 FY2026 Q&A A7: 20,000 "under active internal discussion"; 10,000 date maybe at the Jan 2027 briefing [C] | ADDED |

## Non-OK rows: period-label fixes

| id | What was checked | Before | After | Result |
|---|---|---|---|---|
| CL-013 | period label | FY2026 Q3 / Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 12 Nov 2026) | FIXED (row_check flag) |
| CL-015 | period label | FY2026 Q3 / Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 12 Nov 2026) | FIXED (row_check flag) |
| CL-087 | period label | FY2026 Q3 / Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 12 Nov 2026) | FIXED (row_check flag) |
| CL-090 | period label | FY2026 Q3 / Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 12 Nov 2026) | FIXED (row_check flag) |
| CL-094 | period label | FY2026 Q3 / Oct-Dec 2026 | FY2026 Q4 / Jan-Mar 2027 (Jan 2027; day not given) | FIXED (event falls in Jan 2027) |
| CL-097 | period label | standing / blank | n/a (standing rule) / as of 21 Nov 2026 | FIXED |
| CL-098 | period label | FY2025 / Jun 2025 | FY2025 Q1 / Apr-Jun 2025 (AGM of 27 Jun 2025) | FIXED (row_check flag) |
| CL-100 | period label | FY2026 / 29-31 Oct 2026 | FY2026 Q3 / Oct-Dec 2026 (29-31 Oct 2026) | FIXED (row_check flag) |
| CL-102 | period label | FY2027 / May 2027 | FY2027 Q1 / Apr-Jun 2027 (around May 2027; stated 28 Oct 2026) | FIXED (row_check flag) |
| CL-106 | period label | blank / Nov 2026-Feb 2027 | FY2026 2H / Oct 2026-Mar 2027 (90 days from 19 Nov 2026) | FIXED |
| CL-107 | period label | blank / Jan 2026 | FY2025 Q4 / Jan-Mar 2026 (14 Jan 2026; tariff from 15 Jan 2026) | FIXED |
| CL-123 | period label | blank / Feb 2027 | FY2026 Q4 / Jan-Mar 2027 (17 Feb 2027) | FIXED |
| CL-124 | period label | FY2026 / Nov 2026-Mar 2027 | FY2026 2H / Oct 2026-Mar 2027 (headroom after 31 Oct 2026, to 24 Mar 2027) | FIXED (row_check flag) |
| CL-127 | period label | FY2026 / Apr 2027 | FY2027 Q1 / Apr-Jun 2027 (late-April pattern) | FIXED (row_check flag; the results fall in FY2027 Q1) |
| CL-014 | period label | FY2026 Q1 / Apr-Jun 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) | FIXED |
| CL-043 | period label | FY2025 Q4 / Jan-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) | FIXED |
| CL-064 | period label | FY2025 Q4 / Jan-Mar 2026 | FY2026 Q1 / Apr-Jun 2026 (stated 27 Apr 2026) | FIXED |
| CL-072 | period label | FY2026 Q1 / Apr-Jun 2026 | FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) | FIXED |
| CL-086 | period label | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) | FIXED |
| CL-004 | period label | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) | FIXED |
| CL-081 | period label | FY2026 Q2 / Jul-Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 28 Oct 2026) | FIXED |
| CL-003 | period label | FY2026 Q3 / Oct-Dec 2026 | FY2026 Q4 / Jan-Mar 2027 (Jan 2027 briefing; stated 28 Oct 2026) | FIXED |
| CL-021 | period label | FY2025 Q3 / Oct-Dec 2025 | FY2025 Q4 / Jan-Mar 2026 (published 30 Jan 2026) | FIXED |
| CL-050 | period label | CY2026 / Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (published 18 Nov 2026) | FIXED |
| CL-092 | period label | CY2026 / Nov 2026 | FY2026 Q3 / Oct-Dec 2026 (published 18 Nov 2026) | FIXED |
| CL-110 | period label | CY2026 / Jan 2026 | FY2025 Q4 / Jan-Mar 2026 (published 15 Jan 2026) | FIXED |
| CL-067 | period label | FY2025 Q3 / Oct-Dec 2025 | FY2025 Q4 / Jan-Mar 2026 (stated 28 Jan 2026) | FIXED |

**Label/note harmonisation only.** In these rows the value, quote, page and tag were re-read and found correct. Only the period label was harmonised, or a cross-check note was added: CL-002, CL-005, CL-006, CL-007, CL-008, CL-009, CL-010, CL-011, CL-012, CL-016, CL-017, CL-018, CL-019, CL-020, CL-022, CL-025, CL-033, CL-034, CL-035, CL-036, CL-039, CL-040, CL-041, CL-044, CL-045, CL-046, CL-049, CL-051, CL-052, CL-053, CL-054, CL-055, CL-057, CL-060, CL-061, CL-062, CL-065, CL-071, CL-073, CL-074, CL-075, CL-076, CL-078, CL-079, CL-080, CL-082, CL-083, CL-084, CL-085, CL-089, CL-112, CL-113, CL-115, CL-125, CL-130, CL-131, CL-132.

**OK, unchanged:** CL-027, CL-028, CL-029, CL-031, CL-032, CL-037, CL-038, CL-059, CL-063, CL-066, CL-068, CL-069, CL-077, CL-088, CL-101, CL-116, CL-117, CL-118, CL-119, CL-120, CL-121, CL-128.

**Chart rows re-read on rendered pages** (slides Q2 FY2026, pp.6-7 at 110 dpi):
- CL-029: SoC 173.7 / 165.2 / 353.3; memory 54.6 (FY2024 Q3) / 43.9 / 57.3 / 53.4. The stacks sum to the printed totals.
- CL-059: China (yellow series) 52.1 / 65.4 / 56.8 / 69.4 / 90.1.
- Both MATCH.

## Tag decisions

- **Advantest statements.** Forward-looking statements, market shares, TAMs and policy statements are [C]: CL-001 to CL-011, CL-014, CL-039 to CL-043, CL-051 to CL-053, CL-060, CL-061, CL-071 to CL-077, CL-081 to CL-087, CL-090, CL-102, CL-130 to CL-132, CL-138, CL-140, CL-143.
- **Teradyne statements.** Its forward-looking statements and share claims are [C] (CL-018 to CL-020, CL-044 to CL-048, CL-054, CL-079, CL-080, CL-136). Its reported results are [F] (CL-049, CL-055, CL-078, CL-135, CL-137).
- **Press, analyst and aggregator rows** are all [S] (CL-016, CL-021 to CL-023, CL-050, CL-056 to CL-058, CL-062, CL-091, CL-092, CL-109, CL-110). CL-016 is an analyst question as summarised by Advantest, so it stays [S]. Advantest's refusal to comment on it is CL-017 [F].
- **Simply Wall St.** The page source states that the author account "AnalystLowTarget is a tool utilizing a Large Language Model (LLM)". CL-023 and CL-091 are kept as [S] context only. They are not cited on any ledger side, and no valuation content is used.
- **Verdict words.** None appear outside [I] in CL.csv, CL.md or CL_gaps.md (regex scan).

## Requested re-reads

**AGM and record dates.** What each document prints:

| Document | Prints |
|---|---|
| IR calendar (2026-11-21), FY2026 section | "Jul.9 Dispatch of convocation notice of the 84th Ordinary General Meeting"; "Jul.31 The 84th Ordinary General Meeting of Shareholders"; "Mar.31 Record date for the Voting rights at the ordinary general meeting of shareholders and for the distribution of year-end dividend" |
| IR calendar, FY2025 section | "Jun.27 The 83rd Ordinary General Meeting of Shareholders" and the same "Mar.31 Record date for the Voting rights" line |
| Share Information page | "Within 3 months after the record date for voting rights (May 15)"; "Record Dates Year-end dividend: March 31 Ordinary general meeting of shareholders: May 15 Interim dividend: September 30" |
| 84th annual securities report | p.58: "The Company has set May 15 of each year as the record date for the exercise of voting rights at its Ordinary General Meeting" (data as of May 15, 2026). p.199: "Within three months from the record date ... Record date May 15 ... Record date for dividends from surplus September 30 March 31". The report (filed 26 Jun 2026) does not print the 84th AGM date. |
| Integrated Annual Report 2026 | p.40: Articles amended at the 27 Jun 2025 AGM "to change the record date for voting rights at the Annual General Meeting from March 31 to May 15"; "The 2026 Annual General Meeting was held on July 31". p.24: "establishing a framework that enables us to hold the meeting in July". |
| 85th semi-annual securities report | "Retired Director ... Date of Retirement July 31, 2026", consistent with the AGM date |

Resolution [I] (CL-126): for voting rights, 15 May governs; the IR calendar line is outdated.

**Catalyst dates.** Each was re-read on its page:
- 2026-12-01: dividend notice, IR calendar and tanshin p.1.
- 2027-01-10: FR 2026-22793 p.1. The stay "was set to end November 9, 2026"; BIS is "extending the suspension until January 10, 2027".
- 2027-01-19: FR 2026-23529 p.1, comment due date. The effective date of November 19, 2026 is on the same page.
- 2027-02-17: 90 days after 2026-11-19, computed in CL_catalyst_dates.py. The rule text reads "with 90 days", taken as "within".
- 2027-03-24: buyback notices of 28 Oct and 2 Nov 2026.
- MTP4 "around May 2027": Q2 FY2026 Q&A A7 and A11.
- 2026-11-30: Teradyne IR home page, "Nov 30, 2026 4:15 pm MST Upcoming Event".
- New: the Jan 2027 briefing may also give the 10,000-system date (A7, CL-143).

## Second-document cross-checks

| Headline | First document | Second document | Result |
|---|---|---|---|
| FY2026 Q2 sales 477.7 bn | slides p.5 (CL-024) | tanshin 1H 845,200 less Q1 367,473 = 477,727 (CL-141, CL-142) | agree |
| FY2026 Q2 OI 266.8 bn / OPM 55.9% | notes p.6 (CL-025) | slides p.5; tanshin YTD difference 266,819 / 55.9% | agree |
| FY2026 Q2 sales YoY +81.7% | slides p.5 | tanshin basis 477,727 / 262,957 = +81.7% | agree (the slide prints FY2025 Q2 as 262.9; YTD difference 262,957 rounds to 263.0 because the slide subtracts rounded figures) |
| GM 71.1% | slides p.5 (CL-026) | notes p.6 "exceeded 70%" | consistent |
| China share ~19% | slide p.7 chart (CL-059), 18.9% FY2026 Q1 [I] | Q1 FY2026 Q&A "approximately 19%" (CL-060) | agree |
| NVIDIA International 20.2% | ASR p.51 (CL-069) | 228,273 / 1,128,610 = 20.2% (CL_concentration) | agree |
| Inventories 231,718 / 352,426 | tanshin p.8 (CL-088) | 85th semi-annual report balance sheet | agree |
| Buyback terms | 28 Oct 2026 notice (CL-099) | 2 Nov 2026 status notice (CL-100) | agree |
| CB maturity 28 Mar 2031 | 85th semi-annual report p.33 (CL-103) | CB conversion-price notice: "Zero Coupon Convertible Bonds due 2031" | agree |
| 84th AGM 31 Jul 2026 | IR calendar (CL-096) | Integrated Report p.40 (CL-134) | agree |
| Voting-rights record date | Share Information page (CL-097) | ASR p.58/p.199 (CL-133); Integrated Report p.40 (CL-134) | agree; the IR calendar (CL-095) differs |
| Interim dividend JPY 49 / 1 Dec 2026 | dividend notice (CL-093) | IR calendar; tanshin p.1 | agree |
| CY2026 TAM | Q2 FY2026 slides p.12 (CL-007) | Jan 2026 slides p.12 (CL-138); TH_tam_revisions.out.txt | consistent path (revised up) |
| TechNews USD 8 bn | TechNews (CL-109) | Jan 2026 company estimate 10.7-12.2 | disagree; TechNews dropped as evidence |
| Teradyne non-GAAP OPM 31.6% | prepared remarks p.6 (CL-078) | press-release reconciliation (CL-135) | agree; GAAP 30.8% added |

## Calc re-run results

All `calc/CL_*.py` scripts were run with `python3 -I` and diffed against their `.out.txt`. All 9 original scripts matched before edits. Edits made:
- **CL_segments_yoy.py**: the variable misnamed "peak" (FY2024 Q3 is not the chart high) was renamed, and a comparison vs FY2025 Q3 was added (-6.8%).
- **CL_margin_mtp3.py**: added the Teradyne GAAP margin with its named items (30.8%; gap 25.1 pts) and the statement that Advantest's FY2026 Q2 ex-one-off figure cannot be computed.
- **CL_tam_growth.py**: added the Jan 2026 company CY2026 estimate (10.7-12.2) and the revision to Oct 2026 (+2.3 at both ends; +21.5% / +18.9%). The TechNews figure is now shown only as conflicting (-2.7 vs the Jan low end).
- **CL_catalyst_dates.py**: record-date comments now cite CL-133/CL-134; added the Teradyne UBS date.
- **New CL_crosscheck.py**: the Q2 single quarter from tanshin YTD, and Teradyne QoQ/YoY and its Q4 guide vs Q3.

All 10 scripts re-run with outputs saved. Every hard-coded input carries its row id in a comment and was checked against the cited row. Windows checked:
- LTM China = FY2025 Q3 to FY2026 Q2 (Oct 2025-Sep 2026), sum 1,447.1.
- 2H FY2026 = FY forecast minus 1H actual.
- MTP3 = FY2024-FY2026e.

Every [I] row value equals its script output. Every [I] note has the form "inputs: ...; script: ...; reason: ...", with High/Medium/Low confidence (scripted check).

## Gaps: second attempt

- **CB lock-up terms**: full-text search of the saved 84th ASR and 85th semi-annual report found nothing. The 403 URLs were not retried. Still NOT RETRIEVED.
- **Teradyne flat Q4 guide**: the press analysis is still NOT RETRIEVED, but the primary fact now comes from Teradyne's own release (CL-136, CL-139).
- **Teradyne Q4 call date**: the Teradyne IR home page lists only the UBS event. Still NOT DISCLOSED.
- **Inventory-reversal amount**: the 85th semi-annual report was also read. Still NOT DISCLOSED.
- **Q3 FY2026 results day**: the IR news index 2026 was also read. Still NOT DISCLOSED.
- All gap lines use exactly one of the two permitted forms.

## Remaining doubts

1. The IR calendar's 31 Mar voting-rights line may simply be stale, or the company may intend to revert. The statutory filing (15 May) is taken as governing. The 85th AGM date stays uncommitted.
2. Whether Advantest's SoC testers fall under ECCN 3B992.b.4.b is not disclosed. The C4 "against" evidence on export controls is therefore about rules, not about a documented effect on Advantest.
3. The split of the 1H FY2026 inventory write-down reversal between Q1 and Q2, and its amount, are undisclosed. The 55.9% Q2 OPM and 71.1% GM cannot be shown ex one-off.
4. CL-115 compares segment scopes that differ: Advantest SoC vs Teradyne "compute". It stays Low.
5. Teradyne's target-model year is not printed on the Q3 2026 deck, so C8's comparison of growth rates has no common end year.
6. Teradyne's Q3 2026 ended 27 Sep 2026, not exactly 30 Sep. The calendar label "Jul-Sep 2026" is approximate.

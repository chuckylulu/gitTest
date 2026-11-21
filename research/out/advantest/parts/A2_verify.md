# A2 verification log (adversarial pass, 2026-11-21)

Scope: `parts/A2.csv`, `parts/A2.md`, `parts/A2_gaps.md`, `calc/A2_*.py`. Rules applied from `research/CLAUDE.md`. Fiscal year ends 31 March and is named by its start year (FY2026 = Apr 2026-Mar 2027). Page numbers are physical PDF pages (the 84th annual securities report prints page numbers 4 lower, e.g. physical p.135 = printed "- 131 -").

## Counts

| Item | Count |
|---|---|
| Rows in the file before this pass | 178 (91 [F], 34 [C], 53 [I]) |
| Rows checked | 178 (every [F] and [C] row re-opened on its cited page; every [I] row re-computed) |
| OK, no change | 59 |
| Fixed, value or wording correct but period label reformatted only | 73 |
| Fixed, substantive (flag, claim wording, period meaning, value text, note) | 46 |
| Removed | 0 |
| Added | 20 (A2-179 to A2-198) |
| Rows after this pass | 198 |
| quote_check.py after fixes | 136 quotes FOUND on the cited page (5 layout-insensitive), 0 NOT FOUND, 0 page mismatches; 62 rows without quote are [I] |
| row_check.py after fixes | 0 flags (was 6) |

No value printed in a cited document was found to be wrong: every number in an [F] row matched the cited page, the right column (current period, not prior period), the unit (JPY million in tanshin and securities reports, JPY billion on slides) and the sign. The errors found were labels, wording that went beyond the quote, one quote cited for a phrase that sits on a different page, and unsupported speculation in one note.

## Mechanical flags (row_check_v1.csv)

| id | flag | before | after | result |
|---|---|---|---|---|
| A2-007 | VERDICT word outside [I] | claim "Management confirmed in Oct 2022..."; FY2022 Q2 / Jul-Sep 2022 | "Management stated in Oct 2022..."; FY2022 Q3 / Oct-Dec 2022 (stated 27 Oct 2022) | FIXED |
| A2-009 | PERIOD | FY2025 / as of 31 Mar 2026 | FY2025 end / 31 Mar 2026 | FIXED |
| A2-096 | PERIOD | FY2023 end / as of 1 Apr 2024 | FY2023 end / 31 Mar 2024 (column printed 'As of April 1, 2024'); note cites the 83rd report p.160, which prints 80,815 under "As of March 31, 2024" | FIXED |
| A2-123 | PERIOD | FY2023 end / as of 1 Apr 2024 | same treatment; 83rd report p.160 prints 18,233 under "As of March 31, 2024" | FIXED |
| A2-128 | PERIOD | FY2025 / as of 31 Mar 2026 | FY2025 end / 31 Mar 2026 | FIXED |
| A2-155 | PERIOD | FY2025 / as of Jun 2026 filing | FY2026 Q1 / Apr-Jun 2026 (stated in report filed 26 Jun 2026) | FIXED |

## Substantive fixes (non-OK rows other than the flags above)

| id | what was checked | before | after | result |
|---|---|---|---|---|
| A2-002 | FY2021 Q4 slides p.19 | claim gave one reason for ending order disclosure | claim gives both printed reasons (longer lead times; short-term swings); note quotes the first | FIXED |
| A2-020 | FY2025 Q3 Q&A p.2 A7, English and Japanese | "Many customers said they are sold out through CY2026 and into CY2027" | clarified that the customers' own order books are full (Japanese: 注文が埋まっている), not Advantest's; period n/a (calendar year) / CY2026-CY2027 (stated 28 Jan 2026) | FIXED |
| A2-024 | FY2026 Q1 Q&A p.1 A1 | "sustainable through CY2026 into CY2027"; period "Outlook as of Jul 2026" | quote says "this year and into next year"; the Japanese says 今期から来期 (this fiscal year into next); claim reworded, CY interpretation dropped; FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) | FIXED |
| A2-030 | FY2026 Q2 slides p.13 | value "5,000"; "10,000 target to be reached well ahead of schedule" | value "more than 5,000"; "aims to reach the 10,000-system target well ahead of the original schedule" (slide wording) | FIXED |
| A2-055 | Fireside chat script p.7 | claim included "('just-in-case' model)" | that phrase is on p.6, not on the cited p.7; claim now matches p.7 ("strategic inventory is gold"; more concerned about meeting demand than write-downs); new row A2-179 cites p.6 for "just-in-case" | FIXED |
| A2-057 | Integrated report p.23 | "earmarked for" | "scheduled to go to" (printed: "is scheduled to be allocated to"); dated FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026; bonds issued Apr 2026) | FIXED |
| A2-147 | calc and note | note said "difference likely FX translation" | note: company does not explain the gap; cash-flow line excludes non-cash movements | FIXED |
| A2-150 | calc | "consistent with customer prepayments" | "consistent with an increase in advance receipts" (the line also holds other items) | FIXED |
| A2-117 | note | "company text states +120.7 bn" with no source row | points to new row A2-182 (85th semi-annual report p.7) | FIXED |
| A2-160 | label | FY2025 Q3-FY2026 Q2 | FY2025 Q3 to FY2026 Q2 (LTM) / Oct 2025-Sep 2026 | FIXED |
| A2-001, A2-013, A2-015, A2-017, A2-018, A2-027, A2-031, A2-052, A2-053, A2-054, A2-056, A2-062, A2-173 | period labels of company statements | period without the statement date | statement date added, e.g. "Apr-Jun 2026 (stated 29 Jul 2026)"; period kept where the statement describes a reported period or forecast | FIXED |
| A2-010, A2-011, A2-012, A2-021, A2-022, A2-023, A2-029, A2-058, A2-156 | dated statements labelled with the reported quarter of the briefing | e.g. A2-023 FY2026 Q1 / Apr-Jun 2026 | fiscal quarter in which the statement was made plus date, e.g. FY2026 Q2 / Jul-Sep 2026 (stated 29 Jul 2026) | FIXED |
| A2-014, A2-016, A2-019, A2-025, A2-026, A2-028, A2-165, A2-166 | outlook statements | free-text period labels ("CY2027 outlook", "FY2026 Q3-Q4 outlook") | forecast period in convention form ("FY2025 2H (outlook)", "n/a (calendar year)" / "CY2027 (outlook stated 28 Oct 2026)") | FIXED |

All of these rows were re-opened: the quote is verbatim on the cited physical page and supports the (corrected) claim; tags are right ([C] for every pull-in, "sold out", 18-month-forecast, capacity, lead-time and outlook statement; [F] for printed figures and for printed disclosure-policy statements).

## Label-only fixes (value, quote, page, tag all MATCH)

"as of " removed from balance dates and "FYxxxx Q4 end" changed to "FYxxxx end" (convention: balances "FY2025 end" / "31 Mar 2026"): A2-005, A2-032, A2-033, A2-034, A2-035, A2-036, A2-037, A2-038, A2-039, A2-040, A2-041, A2-042, A2-043, A2-044, A2-045, A2-046, A2-047, A2-051, A2-089, A2-090, A2-091, A2-092, A2-093, A2-094, A2-095, A2-097, A2-098, A2-100, A2-101, A2-102, A2-103, A2-104, A2-105, A2-106, A2-107, A2-108, A2-109, A2-110, A2-111, A2-112, A2-113, A2-114, A2-115, A2-116, A2-118, A2-119, A2-120, A2-121, A2-122, A2-124, A2-125, A2-129, A2-130, A2-131, A2-132, A2-133, A2-134, A2-135, A2-152, A2-153, A2-154, A2-158, A2-159, A2-163, A2-164, A2-167, A2-168, A2-169, A2-170, A2-171, A2-172, A2-177, A2-178.

## OK without change (59)

A2-003, A2-004, A2-006, A2-008, A2-048, A2-049, A2-050, A2-059, A2-060, A2-061, A2-063 to A2-088 (all 26), A2-099, A2-126, A2-127, A2-136 to A2-146 (all 11), A2-148, A2-149, A2-151, A2-157, A2-161, A2-162, A2-174, A2-175, A2-176.

How the numeric [F] rows were checked: for each tanshin balance sheet, profit-or-loss and cash-flow page cited, the column headers were printed with the line ("As of March 31, 2026 / As of September 30, 2026", "Six months ended September 30, 2025 / 2026", etc.) and the row value was confirmed to sit in the current-period column. Year-to-date vs single-quarter: A2-067/068 and A2-075/076 are 3M (= single quarter); A2-069/070, A2-077/078 are 6M; A2-063/064, A2-071/072 are 9M; A2-065/066, A2-073/074 are 12M; cash-flow rows A2-136 to A2-142 are YTD as labelled. Note 8, 9, 11 and 22 rows were checked against the column dates of the 83rd and 84th annual securities reports.

## Added rows (20)

| id | tag | content | why |
|---|---|---|---|
| A2-179 | [C] | "just-in-case operating model" (fireside script p.6) | correct page for the phrase used in A2.md |
| A2-180 | [C] | 1H FY2026 one-time benefit from reversal of inventory write-down (Q2 Q&A A5) | one-off item management named for 1H FY2026 |
| A2-181 | [F] | cash-flow inventory increase 1H FY2026, (119,541) | second figure for the inventory build |
| A2-182 | [F] | 85th report text: inventories +120.7 bn | second document for A2-117 |
| A2-183 | [F] | auditor key audit matter: inventories about 20% of total assets; strategic inventory buffers (84th report p.205) | independent statement on the inventory build |
| A2-184, A2-185 | [F] | FY2021 full-year orders 700.3 bn and sales 416.9 bn (financial results p.5) | last full-year order figures |
| A2-186 | [I] | FY2021 orders/sales 1.68 | context |
| A2-187 | [C] | Oct 2022: orders exceeded sales in FY2022 Q1 and Q2, no figures | last order statement found |
| A2-188 | [I] | Jul-Sep 2026 cost of sales +38.9% YoY | like-for-like comparison with the Sep-to-Sep inventory change |
| A2-189, A2-190 | [I] | 85.5% / 86.3% of opening contract liabilities recognized as revenue within the year | how fast prepayments convert |
| A2-191 | [I] | 2H FY2026 forecast vs 1H reported: +20.4% | checks the "about 20%" remark (A2-026) |
| A2-192 | [F] | slide single-quarter gross profit FY2025 Q1 to FY2026 Q2 | input for the cost-of-sales cross-check |
| A2-193 | [I] | balance vs cash-flow inventory change gap 1,167 m | reconciliation |
| A2-194 | [I] | receivables -50,234 m in FY2026 Q1 | replaces an unrowed "52.1 bn" statement in A2.md (52.1 bn is the cash-flow figure, not the balance change) |
| A2-195 | [I] | 6 of 6 quarters same sign (Other current liabilities vs advance-receipts flow) | replaces an unrowed statement in A2.md |
| A2-196 | [F] | 85th report text: advance receipts +44.2 bn in 1H FY2026 | second document for A2-141 |
| A2-197 | [I] | max 0.12 bn gap between derived and slide-implied quarterly cost of sales | second document for A2-084 to A2-088 |
| A2-198 | [F] | FY2021 financial results p.20: Q4 orders 199.0, backlog 394.7 | second document for A2-003 and A2-005 |

## Second-document cross-checks

| Figure | Document 1 | Document 2 (and 3) | Result |
|---|---|---|---|
| Inventories 30 Sep 2026 | tanshin FY2026 Q2 p.8: 352,426 | 85th semi-annual report p.20: 352,426; slides p.10: 352.4 bn; text +120.7 bn (A2-182) vs balance change 120,708 | agree |
| Inventories 30 Jun 2026 | tanshin FY2026 Q1 p.7: 273,654 | slides FY2026 Q1 p.10: 273.7 bn; tanshin text +41.9 bn vs balance change 41,936 | agree |
| Inventories 31 Mar 2026 | tanshin FY2025 p.9: 231,718 | 84th report note 9 total, note 4 table and key audit matter: 231,718 | agree |
| Inventories 31 Dec 2025 | tanshin FY2025 Q3 p.9: 222,464 | slides FY2025 Q3 p.10: 222.5 bn | agree |
| Inventories 30 Sep 2025 | tanshin FY2025 Q2 p.9: 210,038 | 84th semi-annual report p.14: 210,038 | agree |
| Inventories 30 Jun 2025 | tanshin FY2025 Q1 p.7: 209,274 | slides FY2025 Q1 p.11: 209.3 bn | agree |
| Inventory split and valuation loss 31 Mar 2025 / FY2024 | 84th report p.135 | 83rd report p.135 (27,730 / 53,225 / 128,752; 17,712) | agree |
| Contract liabilities 31 Mar 2025 and 31 Mar 2024 | 84th report p.160: 28,798; 18,233 (as of 1 Apr 2024) | 83rd report p.160: 28,798; 18,233 (as of 31 Mar 2024) | agree |
| Advance-receipts cash flow 1H FY2026 | tanshin FY2026 Q2 p.13: 44,215 | 85th report p.24: 44,215; p.7 text 44.2 bn (A2-196) | agree |
| Advance-receipts cash flow FY2026 Q1 | tanshin p.11: 36,984 | tanshin text p.6: 37.0 bn (A2-151) | agree |
| Other current liabilities 30 Sep / 30 Jun 2026 | tanshin: 87,924; 80,397 | 85th report p.20: 87,924; text +45.2 bn vs 45,168; FY2026 Q1 tanshin text +37.6 bn vs 37,641 | agree |
| Trade and other receivables 30 Sep 2026 / 31 Mar 2026 | tanshin: 239,468; 228,731 | 85th report p.20: 239,468; slides p.10: 239.5 bn; 84th report note 8 total 228,731; FY2026 Q1 text -50.2 bn vs -50,234 | agree |
| Single-quarter sales | YTD differences (A2-079 to A2-083) | slides p.5 single-quarter sales | agree within 0.1 bn (FY2025 Q2: 262,957 vs 262.9) |
| Single-quarter cost of sales | YTD differences (A2-084 to A2-088) | slide sales minus slide gross profit (A2-192) | agree within 0.12 bn (A2-197) |
| FY2021 Q4 orders and backlog | slides p.8: 199.0; 394.7 | financial results p.20: 199.0; 394.7 (A2-198) | agree |
| Capex commitments 31 Mar 2025 | 84th report p.137: 368 | 83rd report p.137: 368 | agree |
| Cash conversion cycle FY2023-FY2025 | Integrated report p.77: 272 / 207 / 177 | no second document prints it | single source; definition not stated |

## Calc re-run

- Before any edit, all five scripts (`A2_quarterly_derivation`, `A2_dso`, `A2_inventory`, `A2_advance_receipts`, `A2_book_to_bill_FY2021Q4`) were re-run with `python3 -I`; each output was identical to its saved `.out.txt`.
- Every hard-coded input was checked against its cited row and page (ids in the comments). Formulas: DSO and inventory days both use ending balance / single-quarter flow x 91.25 (annual: x 365); denominators are single-quarter figures, Q1 printed and Q2-Q4 YTD differences. Windows: YoY compares 30 Sep 2025 with 30 Sep 2026; LTM sum A2-160 covers FY2025 Q3 to FY2026 Q2 (Oct 2025-Sep 2026).
- Scripts extended: slide gross-profit cross-check and max difference (quarterly_derivation); Q2 single-quarter cost-of-sales YoY and balance vs cash-flow inventory change (inventory); opening contract-liability conversion and same-sign count (advance_receipts); FY2021 full-year orders/sales (book_to_bill). New script `A2_outlook_check.py`. All outputs regenerated; every [I] row value appears in its script output, and every [I] note has the form "inputs: ...; script: ...; reason: ..." with High/Medium/Low.

## Gaps re-tried

- Contract liabilities at 30 Sep 2026: 85th semi-annual report read again (notes 1-13; note 8 Revenue gives revenue by region and segment only). Still NOT DISCLOSED.
- Raw / WIP / finished split at 30 Sep 2026: no inventory note in the 85th report (notes 1-13). Still NOT DISCLOSED; confirmed the split appears only in the annual reports' note 9.
- Purchase commitments: 84th report text search finds "commitment" only on pp.11, 25 (non-financial) and 137 (fixed assets). Only capex commitments are disclosed (A2-152 to A2-154).
- Amount of the inventory write-down reversal: searched FY2026 Q1 and Q2 tanshin, slides, notes, Q&A, 85th report, integrated report, fireside chat. Still NOT DISCLOSED.
- Cash conversion cycle definition: integrated report p.77 footnotes *1-*5 define EBITDA, FCF and ROIC but not the cash conversion cycle; p.35, 84th report p.38 and MTP3 slides p.33 mention it without a formula. Still NOT DISCLOSED.
- Orders: FY2022 Q1 financial results (Jul 2022) contain no order table; the Oct 2022 Q&A says order data are no longer disclosed. Searches of FY2025-FY2026 documents for book-to-bill, bookings, order backlog, cancellations and postponements found nothing.
- Current lead time: no figure in FY2025 Q3 to FY2026 Q2 documents. Still NOT DISCLOSED.
- New gap added: the 84th report no longer gives the share of slow-turnover raw materials (83rd report: about 9% at 31 Mar 2025).
- No new document was fetched.

## Remaining doubts

1. Period labels for company statements now follow the stated convention (fiscal quarter of the statement date plus the date). Other modules may label the same briefing statements by the reported quarter; the merged file may need one rule.
2. FY2026 Q1 and Q2 inventory days are biased upward by an undisclosed one-time reversal of inventory write-down; the size is unknown, so the rise from 197.7 to 233.2 days cannot be shown on a clean basis.
3. The "Other current liabilities" quarterly proxy holds items besides advance receipts (6-7% of the line at the two year-ends), so it cannot give the 30 Sep 2026 contract-liability balance.
4. The company's cash conversion cycle (A2-059 to A2-061) has no printed definition. It is kept as [F] because it is a printed company figure for past years, but it cannot be recomputed from the statements.
5. A2-020 ("sold out") and A2-024 ("this year and into next year") are ambiguous in English; the Japanese text was used to set the wording.

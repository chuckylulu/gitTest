# A4 verification log (adversarial re-check, 2026-11-21)

Scope: `parts/A4.csv`, `parts/A4.md`, `parts/A4_gaps.md`, `calc/A4_*.py`. Rules applied: research/CLAUDE.md (tags, columns, missing-data forms, arithmetic in calc/, one-offs with and without).

## Counts

| | n |
|---|---|
| Rows in file before | 404 (327 [F], 11 [C], 66 [I]) |
| Rows checked | 404: all mechanically (quote_check, row_check, [I] value vs script RESULT); about 250 re-opened on the cited page (see list below) |
| OK | 362 |
| Fixed | 42 |
| Removed | 0 |
| Added | 32 (A4-405 to A4-436) |
| Rows in file after | 436 (349 [F], 12 [C], 75 [I]) |
| quote_check after | 361 FOUND, 0 NOT FOUND, 0 flags (75 [I] rows carry no quote) |
| row_check after | 0 flags (before: 2, A4-319 and A4-320) |

## Material findings

1. **Customer scope (missed table).** The 84th report has two customer disclosures. Note 6(6) (p.134) gives customer groups: NVIDIA Group 243,735. The Item 2 table (p.51) gives single counterparties with printed shares: NVIDIA International, Inc. 228,273 (20.2%), TSMC 11.1% / 12.3%, Samsung Electronics 82,795 (10.6%, FY2024). The 83rd report p.50 gives Samsung Electronics 55,325 (11.4%, FY2023). A4 cited only the group note. Added A4-406 to A4-413, A4-434 and A4-435. The group share of 21.6% (A4-339) is arithmetically right. The company's own printed share for NVIDIA is 20.2% at entity level.
2. **Back-end test reading wrong (A4-403).** The old row said the Oct 2023 back-end exclusion applies "only" to § 744.23(a)(2). The rule text says more:
   - BIS agreed to a comment about 3B992.b.4 back-end test equipment (p.7, Topic 29).
   - Screening test equipment used only in back-end stages does not trigger § 744.23(a)(2) or § 744.6(c)(2)(i)-(ii) (p.8).
   - § 744.23(a)(4) was narrowed to front-end production equipment (p.27 Note 1, p.22 C.11.c), and BIS says the back-end principle also applies to (a)(4) (p.8, Topic 31).
   Rewrote A4-403 and added [F] rows A4-415 to A4-419.
3. **"2025-2026 rules do not touch test equipment" was wrong (A4-404).**
   - The Jan 2025 IFR (90 FR 5298, p.8) widens the § 744.11(a)(2)(v) Footnote 5 licence scope from 3B993 to 3B002 (except .c), 3B992 and other 3B ECCNs. This applies to exporters headquartered in Macau or D:5 countries (A4-421).
   - The Nov 2026 IFR reprints the 3D001/3E001 headings, which exclude 3B992 (A4-422).
   Rewrote A4-404 and added the Low-confidence reading A4-436.
4. **A4-400 had no script and was too strong.** Wrote `calc/A4_rule_scan.py`, which runs a term search over all 179 saved Advantest documents. No document names the EAR, BIS, an ECCN, an FDP rule, FEFTA or METI's export list. But three passages refer to a specific measure:
   - Jul 2019 Q&A: Entity List placement of "a major mobile phone manufacturer" (new A4-423).
   - Oct 2022 Q&A: the US restrictions of 7 Oct 2022 (A4-305).
   - Jul 2023 deck: "U.S. export controls on China" (new A4-424).
   METI hits are only "White 500" news titles. Rewrote A4-400 to "0 of 179".
5. **Semi-annual region basis overstated.** A4.md said the semi-annual reports split by customer location. The 85th and 84th semi-annual reports (note 8) do not state a basis. Corrected A4.md and A4-385 and added a NOT DISCLOSED line. The semi-annual figures equal the sum of the two ship-to quarters within 0.1 bn (new A4-433).
6. **One-off rule not applied.** A4.md showed segment-income differences with no one-offs. Added A4-425 to A4-431 and `calc/A4_oneoffs.py`:
   - FY2024 Essai impairment 21,393 sits in the services segment on both bases. Ex-impairment services income is 10,479 on the old basis and 5,268 on the new. The restatement effect stays -5,211.
   - 1H FY2025 divestiture income 2,504 gives Services and Others ex-item 544.
   - The 1H FY2024, 9M FY2024 and Q1 FY2024 segment notes name no item for those periods.
7. **Period labels.** 35 dated rows had empty or non-convention labels: regulator rules, management statements and the IR page. They now carry the fiscal quarter of the date plus the date. Earnings-call statements are dated by the call date, and the note names the results call.

## Fixed and added rows

| id | what was checked | before | after | result |
|---|---|---|---|---|
| A4-013 | section label | "Information of Main Customers" | "Business risks e. Customer Portfolio" (p.40 is a risk factor) | FIXED |
| A4-023, A4-024 | page of region total | p.51 (segment table) | p.133 (region table; same total) | FIXED |
| A4-050 | basis wording, latest deck | definition only from Apr 2024 deck | note: latest deck titles chart "Ship to Region" without the footnote (A4-405) | FIXED |
| A4-300 | period | empty | FY2026 Q3 / Oct-Dec 2026 (retrieved 21 Nov 2026) | FIXED |
| A4-305, A4-306 | period | FY2022 Q2 / Jul-Sep 2022 | FY2022 Q3 / Oct-Dec 2022 (27 Oct 2022) | FIXED |
| A4-307 | quote supports claim | quote cut before "manufacturing at advanced process nodes"; earnings-impact half unquoted | full phrase quoted; second sentence in note; period FY2024 Q1 (26 Apr 2024) | FIXED |
| A4-308 to A4-311 | period | quarter reported on | quarter of statement date + date | FIXED |
| A4-312 | tag and period | [C], FY2026 Q1 | [F] (historical share, testable vs A4-356 at 18.9%), FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026); basis gap noted | FIXED |
| A4-313, A4-314, A4-318 | period | FY2026 Q1 | FY2026 Q2 / Jul-Sep 2026 (29 Jul 2026) | FIXED |
| A4-319, A4-320 | row_check VALUE flag ['10'] | "2022-10-07 effective date", empty fiscal period | "7 Oct 2022 (effective date ...)", FY2022 Q3 / Oct-Dec 2022 (published 13 Oct 2022). Value printed on p.1 as "October 7, 2022"; flag came from ISO format | FIXED (flag was format, not error) |
| A4-321 to A4-327, A4-329, A4-330, A4-332 | period | empty | quarter + publication date | FIXED |
| A4-328 | claim precision | "3B001 parts ... 3B991" | exact exceptions from § 734.9(e)(3)(i) p.22, plus a pointer to the direct-product conditions (A4-420) | FIXED |
| A4-331, A4-333 to A4-338 | value format and period | ISO dates, empty fiscal period | "23 Jul 2023" etc.; quarter + date | FIXED |
| A4-385 | basis | "(customer location)" | "semi-annual main regions table; basis not stated" | FIXED |
| A4-400 | script and wording | no script; "no specific rule named" | `calc/A4_rule_scan.py`; "0 of 179" documents name EAR/BIS/ECCN/FDP/FEFTA; 3 rule-specific references listed | FIXED |
| A4-401 | script, wording | script none | script A4_rule_scan.py; 3B002.c identified as EUV mask inspection | FIXED |
| A4-402 | FDP conditions | conditions loosely stated | direct-product conditions per A4-420; Low | FIXED |
| A4-403 | reading of Oct 2023 rule | "(a)(5) applies only to (a)(2)" | back-end-only test outside (a)(2), § 744.6(c)(2) and front-end-limited (a)(4); Medium | FIXED |
| A4-404 | test ECCNs in 2025-26 rules | "no test-equipment ECCN" | Jan 2025 § 744.11 widening to 3B002/3B992 for D:5-HQ exporters; Nov 2026 3D001/3E001 headings | FIXED |
| A4-405 | latest deck basis title | - | Q2 FY26 deck p.7 "Ship to Region" | ADDED |
| A4-406 to A4-413 | entity-level customer table | - | 84th p.51, 83rd p.50 amounts and printed shares | ADDED |
| A4-414 | second document for customer-location basis | - | FY2025 tanshin p.15 note | ADDED |
| A4-415 to A4-419 | Oct 2023 rule back-end text | - | pp.7, 8, 22, 27 | ADDED |
| A4-420 | Footnote 5 FDP direct-product conditions | - | Dec 2024 rule p.22 | ADDED |
| A4-421 | Jan 2025 § 744.11 widening | - | 90 FR 5298 p.8 | ADDED |
| A4-422 | Nov 2026 3D001/3E001 headings | - | 91 FR 74970 p.19 | ADDED |
| A4-423, A4-424 | rule-specific company references | - | Jul 2019 Q&A p.2; Jul 2023 deck p.17 [C] | ADDED |
| A4-425 to A4-427 | one-offs named by management | - | 84th p.132 note 2; 83rd p.133 note 2; 84th 1H p.21 note 2 | ADDED |
| A4-428 to A4-431 | with/without one-offs | - | 10,479; 5,268; 252,447; 544 (calc/A4_oneoffs.py) | ADDED |
| A4-432 | China LTM YoY | - | +50.2% (281.7 vs 187.5 bn) | ADDED |
| A4-433 | semi-annual vs slide quarters | - | max diff 0.099 bn | ADDED |
| A4-434, A4-435 | group vs entity; printed vs computed shares | - | 15,462; 0 mismatches of 5 | ADDED |
| A4-436 | reading of Jan 2025 widening for Advantest | - | Low | ADDED |

## OK ids (compact)

- **Re-opened on the cited page:**
  - Customers, regions and risk text: A4-001 to A4-012, A4-014 to A4-022, A4-025 to A4-049.
  - Ship-to chart labels, checked on the rendered Q2 FY26 p.7: A4-075 to A4-138.
  - First-reported chart labels, rendered: Q1 FY26 deck p.7 for A4-187 to A4-194; FY25 deck p.9 for A4-179 to A4-186. The other first-reported labels have their value on the cited page, and the sum check holds.
  - Semi-annual region tables: A4-203 to A4-208, A4-210, A4-212, A4-214, A4-216 (85th p.29).
  - Segment tables: A4-228 to A4-242, A4-243 to A4-256, A4-258 to A4-263, A4-270 to A4-296.
  - Company statements and regulator text: A4-297 to A4-299, A4-301 to A4-304, A4-315 to A4-317.
- **Value-on-page plus cross-document match** (A4_restatement.py and A4_region_shares.py): A4-051 to A4-074, A4-139 to A4-178, A4-195 to A4-202, A4-209, A4-211, A4-213, A4-215, A4-217 to A4-227, A4-257, A4-264 to A4-269.
- **[I] rows whose value equals the script RESULT and whose note matches the required format:** A4-339 to A4-399.

## Second-document cross-checks

| Headline figure | Doc 1 | Doc 2 | Result |
|---|---|---|---|
| FY2025 regions, customer location (Japan 25,137; Americas 44,474; Europe 23,149; Asia 1,035,850; total 1,128,610) | 84th report p.133 | FY2025 results (tanshin) p.15 | agree; both say "based on the customer's location" |
| FY2025 China 213,293 m | 84th report p.133 | FY25 deck p.6 ship-to 213.3 bn; sum of 4 quarters in Q2 FY26 deck 213.3 bn | agree within rounding |
| Quarterly China, FY2025 Q1-FY2026 Q1 | Q2 FY26 deck p.7 (rendered) | Q1 FY26 deck p.7 and FY25 deck p.9 (rendered) | identical labels |
| 1H FY2026 regions (Asia 799,001; total 845,200) | 85th semi-annual p.29 | Q1+Q2 FY26 slide labels (799.0; 845.2 bn) | agree within 0.1 bn (A4-433) |
| TSMC FY2025 124,922 / FY2024 96,158 | 84th note 6(6) p.134 | 84th Item 2 p.51; 83rd p.134 | agree |
| NVIDIA FY2025 | Group 243,735 (p.134) | NVIDIA International, Inc. 228,273 (p.51) | differ by scope (15,462), not a restatement |
| Samsung FY2024 / FY2023 | Group 87,734 / 57,725 (note 6(6)) | Samsung Electronics 82,795 / 55,325 (Item 2) | differ by scope |
| FY2024 segment restatement (11,511 sales moved; Corporate +3,898; services -5,211; total 231,054) | 83rd p.132 (three segments) | 84th p.132 (two segments) | arithmetic re-done from both tables: holds |
| Essai impairment 21,393 | 84th p.132 note 2 | 83rd p.133 note 2; FY2024 tanshin p.15 note 2 | agree |
| Divestiture income 2,504 | 84th semi-annual p.21 | FY2025 Q1 results p.13; FY2025 Q3 results p.16 | agree |
| China "approximately 19%" (Jul 2026) | Q1 FY26 Q&A p.4 | Q1 FY26 ship-to 18.9% (A4-356); FY2025 18.9% (A4-373) | consistent; basis unstated |
| Footnote 5 product list (3B002 except .c, 3B992 ...) | Dec 2024 rule p.22 | Jan 2025 rule p.8 (§ 744.11 widening uses the same list) | consistent |

## Restatement method check (the "0 of 102 / 195 / 65" claims)

- **A4_restatement.py** compares hard-coded pairs, so the risk is a figure being compared with itself.
  - Sampled pairs: A4-150 vs A4-086 (FY24 deck p.8 vs Q2 FY26 deck p.7), A4-174 vs A4-110, A4-182 vs A4-118, A4-190 vs A4-126, A4-005 vs A4-003, A4-209 vs A4-208.
  - Each first-reported id cites a different, earlier document from its later id.
  - The values were read on the two rendered decks above. No self-comparison was found.
- **A4_restatement_scan.py** parses the saved text and has no typed values.
  - Each pair compares column 1 of the earlier document with column 0 of the later one. That is the right orientation (current year in the earlier report against the prior-year comparative in the later one).
  - The geographic-area job matched only 5 lines (Japan, Americas, Europe, Asia, Total). The 8 unmatched lines are segment-table rows from the same page, whose column count differs between the old and new segment bases. These were correctly excluded.
  - The slide job maps tokens to quarters in order. A mapping error would show up as CHANGED across decks, and none did.

## Calc re-run results

All six scripts were re-run with `python3 -I`, and each output is identical to its `.out.txt`.
- `A4_customers.py` and `A4_region_shares.py` were extended. The new RESULT lines were appended, and every earlier RESULT is unchanged.
- `A4_oneoffs.py` and `A4_rule_scan.py` are new.
- Each [I] row's value equals a RESULT line in its cited output file (automated check, 0 exceptions). Each [I] note follows "inputs: ...; script: ...; reason: ...", and each confidence is High, Medium or Low.

## Gap re-attempts

| Gap | Attempt | Result |
|---|---|---|
| 88 FR 73458 (FR Doc 2023-23055) | govinfo.gov via fetch.py | RETRIEVED, 60 pages. The text has no tester or back-end provisions; 3B992 appears only as an exclusion in the 3D001/3E001 headings. Gap removed. |
| BIS FAQ II.A.1 (25 Jan 2023) | bis.doc.gov URL cited in the rule, one try | NOT RETRIEVED: the response was not the PDF. Kept. |
| Orders | 84th report Item 2 a. | The company says orders "are also not listed". Kept as NOT DISCLOSED with that section cited. |
| Basis of the "approximately 19%" | Q1 FY26 Q&A re-read | Still unstated. Kept. |
| FY2024 NVIDIA amount | 84th p.51 and p.134 re-read | Not given (below 10%). Kept. |

## Remaining doubts

- The quarterly region figures are chart data labels. They are confirmed by the sum checks and by the identical labels across decks, but there is no tabular source.
- Whether Advantest's wafer-level (HBM/SoC wafer-sort) testers count as "back-end" under § 744.23(a)(5) is not settled in the text. BIS refers such questions to advisory opinions, none of which was retrieved.
- The reach of the Footnote 5 FDP rule to Advantest depends on its ECCNs and US-origin technology content, which are not public (A4-402, Low).
- A4-436 reads the Jan 2025 § 744.11 widening from the preamble summary only. The amended regulatory text of § 744.11(a)(2)(v) and (a)(3)(i) was not read in full.
- The top-five share basis (groups or entities) is unknown. The residual for the three other customers is 17.3 pp on the group basis and 18.7 pp on the printed entity basis (`A4_customers.out.txt`).
- Retagging A4-312 from [C] to [F] is a judgement call: the share is historical and testable, but its period and basis are not stated.

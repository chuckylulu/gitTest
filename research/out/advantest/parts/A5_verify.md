# A5 verification log (adversarial verifier, 2026-11-21)

Scope: `parts/A5.csv`, `parts/A5.md`, `parts/A5_gaps.md`, `calc/A5_*.py` and their `.out.txt`. Rules applied: `research/CLAUDE.md` (tags, columns, missing-data forms, arithmetic in calc/, one-off rule, no prices or valuation views). Fiscal year ends 31 March, named by start year (FY2026 = Apr 2026-Mar 2027).

## Counts

| Item | Count |
|---|---|
| Rows in A5.csv before verification | 203 (178 [F]/[C], 25 [I]) |
| Rows checked | 203: all 178 [F]/[C] rows had their quote matched on the cited page by `quote_check.py`; for about 165 of them the cited page was also re-read in the PDF/HTML (balance sheets, notes 11/12/17/21/25/30/32/33, CB terms, releases, slides, CFO message); all 25 [I] rows were recomputed |
| OK (unchanged) | 121 |
| FIXED | 82 (58 period-label only; 24 value, tag, claim, page, quote or note fixes) |
| REMOVED | 0 |
| ADDED | 14 (A5-225 to A5-238) |
| Remaining row_check flags | 2, both FALSE FLAG (A5-085, A5-131) |
| quote_check | 191 FOUND on the cited page, 0 NOT FOUND, 0 page mismatches, 0 over 25 words |

## Material findings

1. **R&D Altanova is outside a strict five-year window.** It closed on 17 Nov 2021 (A5-131), four days before 21 Nov 2021. It is kept in the table, and A5.md and the calc docstring now say so.
2. **"All impairments were on Essai" was too broad.** FY2021 also carried a 398 impairment on property, plant and equipment, a closed dormitory (80th report p.114; new row A5-231). A5-220 and A5-181 are now limited to goodwill and intangibles, which remain all Essai (30,391).
3. **The company prints its own total return ratio.** The FY2025 Q4 slides p.5 show FY2024 49% and FY2025 42%, and share repurchases of 50.0bn and 114.2bn (new rows A5-225 and A5-226). The calc reproduces both on a record-date basis (48.8%, 41.9%). A payment-date basis gives 48.0% and 40.0%, which does not match (new [I] A5-236). A5-212 and A5-213 are raised from Medium to High. The gap "company's own computation" is narrowed to the cumulative MTP3 figure.
4. **The one-off rule was not applied to the net income behind the total return ratio.** Now listed in A5.md (c) and the calc:
   - FY2024: Essai impairment (21,393).
   - FY2025: call-option gain 17,312 (A5-230), divestiture gain 2,504, and one-off Q4 SG&A with no amount (A5-227 [C]).
   - 1H FY2026: valuation gains 54,171 (A5-228), and an inventory write-down reversal with no amount (A5-229 [C]).
   - Net income ex items stays NOT DISCLOSED for want of the tax effect. Note 15(3) p.146 was read; it does not itemise the tax on these items.
5. **Micronics Japan gap filled.** The 84th report p.108 (Status of Shareholdings) shows the parent held 150,000 MJC shares, carrying 1,386 at 31 Mar 2026 and 522 at 31 Mar 2025 (new A5-237). The NOT DISCLOSED line for it was removed from A5_gaps.md.
6. **Tags.**
   - A5-081 (60% conversion premium, a priced and testable deal term) and A5-125 (MTP2 total return ratio result, 69%) changed from [C] to [F].
   - A5-160 (FormFactor "will separately purchase") and A5-161 (Micronics "plans to acquire") changed from [F] to [C], because they were intentions on the announcement date.
7. **Interest cost was incomplete.** FY2025 interest on liabilities at FVTPL was 976 (FY2024: 1,028), on top of the 1,271 at amortised cost (new A5-234; A5-051 claim updated).
8. **Dilution denominator stated.**
   - Shares on full conversion at JPY 35,946.5: 2,780,000 (fractions rounded down per bond) to 2,781,912 (one request).
   - That is 0.380% of 732,000,000 issued shares (incl. 10,047,095 treasury) or 0.385% of 721,952,905 shares outstanding excl. treasury, both at 30 Sep 2026 (A5-217).
9. **Smaller fixes.**
   - A5-009 claim pointed to A5-043 for the loan repayment; corrected to A5-044.
   - A5-156 period corrected from FY2025 1H to FY2025: the cited note is the full-year column.
   - A5-121 now cites the P&L owners-of-parent line (p.21) rather than the changes-in-equity statement.
   - A5-043, A5-064 and A5-093 values changed from an unprinted "0" to the printed wording.
   - A5-210 note no longer asserts that the 99.7 cash-flow difference is odd-lot purchases. The difference is not itemised.
   - The A5.md premise note on file-name dates was out of date after today's rename; rewritten.
   - Goodwill by CGU now also lists Japan (Services and Others) 8,653 and Essai nil (A5-238). Salland's goodwill is attributed to the Test System segment (A5-233).
   - The funds carry no obligation for further contributions (A5-232).

## Non-OK rows

| id | what was checked | before | after | result |
|---|---|---|---|---|
| A5-009 | claim cross-reference | "loan repaid in Jan-Mar 2026, see A5-043" | "nil at 31 Mar 2026, repaid in FY2025 (see A5-044)"; Q3 tanshin p.10 shows long-term borrowings nil at 31 Dec 2025 | FIXED |
| A5-043 | value vs page (row_check VALUE '0') | 0 / JPY million | none outstanding / text (p.7: "There is no outstanding balance of executed borrowings") | FIXED |
| A5-051 | completeness of interest expense on p.167 | amortised cost only | claim adds FVTPL interest 976 (FY2024 1,028), see A5-234 | FIXED |
| A5-061 | claim | issue amount only | adds 10,000 bonds of JPY 10m (p.182 item (2)); period Apr-Jun 2026 (issued 20 Apr 2026) | FIXED |
| A5-064 | value vs page (row_check VALUE '0') | 0 / % | no interest / text; period Apr-Jun 2026 (issued 20 Apr 2026) | FIXED |
| A5-070 | claim vs p.12 | rating carve-out only | adds the clean-up, corporate-event and parity-event carve-outs printed in the same note | FIXED |
| A5-081 | tag; period | [C]; FY2026 Q1 / Apr 2026 | [F] (priced, testable deal term; p.24 gives the definition); Apr-Jun 2026 (CB priced 1 Apr 2026; stated 11 Nov 2026) | FIXED |
| A5-082 | claim wording vs p.24 | "(2014 CB: 8.3%)" | "estimated dilution of the 2014 CB at issuance: 8.3%"; period relabelled | FIXED |
| A5-085 | row_check VALUE '8' | value 8 | unchanged: p.24 prints "eight times the issue amount"; period relabelled | FALSE FLAG (period FIXED) |
| A5-093 | value vs quote | 0 shares | not applicable / text (82nd p.71 prints "Not applicable.") | FIXED |
| A5-121 | page and line | p.23 changes in equity, "Net income 368,083 ..." | p.21 P&L, "Owners of the parent 169,813 368,083" | FIXED |
| A5-125 | tag | [C] | [F] (historical result printed in MTP3 slides p.34) | FIXED |
| A5-131 | row_check VALUE '11' | 2021-11-17 | unchanged: p.165 prints "November 17, 2021"; period relabelled | FALSE FLAG (period FIXED) |
| A5-156 | period vs cited column | FY2025 1H / Apr-Sep 2025 | FY2025 / Apr 2025-Mar 2026; claim notes the 1H FY2025 cash-flow column (SSR85 p.24) | FIXED |
| A5-160 | tag | [F] | [C] ("will separately purchase", amount not disclosed) | FIXED |
| A5-161 | tag | [F] | [C] ("plans to acquire"); see A5-237 for the actual holding | FIXED |
| A5-181 | claim vs 80th pp.113-115 | "No impairment in FY2021 or FY2022" | limited to the goodwill/intangibles table; PP&E impairment 398 in FY2021 (A5-231) | FIXED |
| A5-210 | note | "includes odd-lot purchases" (unsupported) | difference 99.7 not itemised; equals company-printed 114.2bn (A5-226) | FIXED |
| A5-212 | value vs company figure | 48.8%, Medium | 48.8%, High; company prints 49% (A5-225) | FIXED |
| A5-213 | value vs company figure | 41.9%, Medium | 41.9%, High; company prints 42% (A5-225) | FIXED |
| A5-214 | note | no mention of one-offs | names the 1H FY2026 items in the denominator; company has no cumulative figure | FIXED |
| A5-217 | denominator and rounding | "about 2,781,912 (0.38% of issued shares)" | 2,780,000-2,781,912; 0.380% of 732,000,000 issued incl. treasury / 0.385% of 721,952,905 ex treasury, 30 Sep 2026 | FIXED |
| A5-220 | scope vs 80th p.114 | "Impairments ... total 30,391, all on Essai" | goodwill and intangible impairments 30,391, all Essai; plus 398 on PP&E in FY2021 | FIXED |
| A5-224 | note format / script | script did not print the evidence | script now lists the 1H FY2026 cash-flow adjustment lines; note format fixed | FIXED |
| A5-029 | period label (row_check / convention) | FY2026 / Apr 2026 onward | FY2026 Q1 / Apr-Jun 2026 (contributed after 31 Mar 2026; reported 26 Jun 2026) | FIXED |
| A5-053 | period label (row_check / convention) | FY2026 Q2 / Jul 2026 | FY2026 Q2 / Jul-Sep 2026 (22 Jul 2026) | FIXED |
| A5-054 | period label (row_check / convention) | FY2026 Q2 / Jul 2026 | FY2026 Q2 / Jul-Sep 2026 (22 Jul 2026) | FIXED |
| A5-055 | period label (row_check / convention) | FY2026 Q2 end / 30 Sep 2026 | FY2026 Q3 / Oct-Dec 2026 (page read 21 Nov 2026; bond issued 20 Apr 2026) | FIXED |
| A5-060 | period label (row_check / convention) | FY2026 Q1 / Apr 2026 | FY2026 Q1 / Apr-Jun 2026 (resolved 1 Apr 2026; paid 20 Apr 2026) | FIXED |
| A5-062 | period label (row_check / convention) | FY2026 Q1 / Apr 2026 | FY2026 Q1 / Apr-Jun 2026 (issued 20 Apr 2026) | FIXED |
| A5-063 | period label (row_check / convention) | FY2030 / Mar 2031 | FY2030 Q4 / Jan-Mar 2031 (28 Mar 2031) | FIXED |
| A5-065 | period label (row_check / convention) | FY2026 Q1 / Apr 2026 | FY2026 Q1 / Apr-Jun 2026 (issued 20 Apr 2026) | FIXED |
| A5-066 | period label (row_check / convention) | FY2026 Q1 / Apr 2026 | FY2026 Q1 / Apr-Jun 2026 (as of issue date 20 Apr 2026) | FIXED |
| A5-069 | period label (row_check / convention) | FY2030 / Apr-Dec 2030 | FY2030 / Apr 2030-Mar 2031 (1 Apr-28 Dec 2030) | FIXED |
| A5-071 | period label (row_check / convention) | FY2026 Q1 / Apr 2026 | FY2026 Q1 / Apr-Jun 2026 (issued 20 Apr 2026) | FIXED |
| A5-075 | period label (row_check / convention) | FY2026 Q3 / Oct 2026 | FY2026 Q3 / Oct-Dec 2026 (effective 1 Oct 2026; announced 28 Oct 2026) | FIXED |
| A5-076 | period label (row_check / convention) | FY2026 Q2 / record date 30 Sep 2026 | FY2026 Q2 / Jul-Sep 2026 (record date 30 Sep 2026) | FIXED |
| A5-083 | period label (row_check / convention) | FY2026 Q1 / Apr 2026 | FY2026 Q1 / Apr-Jun 2026 (CB issued Apr 2026; stated 11 Nov 2026) | FIXED |
| A5-084 | period label (row_check / convention) | FY2026 / 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) | FIXED |
| A5-086 | period label (row_check / convention) | FY2014- / 2014- | FY2014 onward / 2014 issue; status stated 11 Nov 2026 | FIXED |
| A5-094 | period label (row_check / convention) | FY2024 / Nov 2024-Feb 2025 | FY2024 Q3 / Oct-Dec 2024 (resolved 30 Oct 2024; window 1 Nov 2024-26 Feb 2025) | FIXED |
| A5-095 | period label (row_check / convention) | FY2024 / Nov 2024-Jan 2025 | FY2024 / Apr 2024-Mar 2025 (executed Nov 2024-28 Jan 2025) | FIXED |
| A5-096 | period label (row_check / convention) | FY2025 / May-Sep 2025 | FY2025 Q1 / Apr-Jun 2025 (resolved 25 Apr 2025; window 7 May-22 Sep 2025) | FIXED |
| A5-097 | period label (row_check / convention) | FY2025 / May-Sep 2025 | FY2025 1H / Apr-Sep 2025 (executed 7 May-22 Sep 2025) | FIXED |
| A5-098 | period label (row_check / convention) | FY2025-FY2026 / Nov 2025-Oct 2026 | FY2025 Q3 / Oct-Dec 2025 (resolved 28 Oct 2025; window 4 Nov 2025-28 Oct 2026) | FIXED |
| A5-099 | period label (row_check / convention) | FY2025 / Nov 2025-Mar 2026 | FY2025 / Apr 2025-Mar 2026 (executed Nov 2025-Mar 2026) | FIXED |
| A5-100 | period label (row_check / convention) | FY2026 1H / Apr-Aug 2026 | FY2026 1H / Apr-Sep 2026 (executed Apr-19 Aug 2026) | FIXED |
| A5-101 | period label (row_check / convention) | FY2025-FY2026 / Nov 2025-Aug 2026 | FY2025-FY2026 / Nov 2025-Aug 2026 (completed 19 Aug 2026) | FIXED |
| A5-102 | period label (row_check / convention) | FY2026 / Oct 2026-Mar 2027 | FY2026 Q3 / Oct-Dec 2026 (resolved 28 Oct 2026; window 29 Oct 2026-24 Mar 2027) | FIXED |
| A5-104 | period label (row_check / convention) | FY2026 Q3 / 29-31 Oct 2026 | FY2026 Q3 / Oct-Dec 2026 (executed 29-31 Oct 2026) | FIXED |
| A5-105 | period label (row_check / convention) | FY2025 Q4 / Feb 2026 | FY2025 Q4 / Jan-Mar 2026 (cancelled 6 Feb 2026) | FIXED |
| A5-106 | period label (row_check / convention) | FY2025 Q4 / Jan-Feb 2026 | FY2025 Q4 / Jan-Mar 2026 (resolved 28 Jan 2026; cancelled 6 Feb 2026) | FIXED |
| A5-109 | period label (row_check / convention) | FY2026 Q3 / Oct 2026 | FY2026 Q3 / Oct-Dec 2026 (30 Oct 2026) | FIXED |
| A5-110 | period label (row_check / convention) | FY2024 Q2 / record date 30 Sep 2024 | FY2024 Q2 / Jul-Sep 2024 (record date 30 Sep 2024) | FIXED |
| A5-111 | period label (row_check / convention) | FY2024 Q4 / record date 31 Mar 2025 | FY2024 Q4 / Jan-Mar 2025 (record date 31 Mar 2025) | FIXED |
| A5-112 | period label (row_check / convention) | FY2025 Q2 / record date 30 Sep 2025 | FY2025 Q2 / Jul-Sep 2025 (record date 30 Sep 2025) | FIXED |
| A5-113 | period label (row_check / convention) | FY2025 Q4 / record date 31 Mar 2026 | FY2025 Q4 / Jan-Mar 2026 (record date 31 Mar 2026) | FIXED |
| A5-114 | period label (row_check / convention) | FY2026 Q2 / record date 30 Sep 2026 | FY2026 Q2 / Jul-Sep 2026 (record date 30 Sep 2026) | FIXED |
| A5-119 | period label (row_check / convention) | FY2023 Q3 / Oct 2023 | FY2023 Q3 / Oct-Dec 2023 (effective 1 Oct 2023) | FIXED |
| A5-126 | period label (row_check / convention) | FY2026 Q2 / Jul-Sep 2026 | FY2024-FY2026 / Apr 2024-Mar 2027 (stated 28 Oct 2026) | FIXED |
| A5-127 | period label (row_check / convention) | FY2026 Q2 / Oct 2026 | FY2026 Q3 / Oct-Dec 2026 (28 Oct 2026) | FIXED |
| A5-130 | period label (row_check / convention) | FY2021 Q3 / Oct 2021 | FY2021 Q3 / Oct-Dec 2021 (26 Oct 2021) | FIXED |
| A5-132 | period label (row_check / convention) | FY2021 Q3 / Nov 2021 | FY2021 Q3 / Oct-Dec 2021 (acquisition date 17 Nov 2021) | FIXED |
| A5-133 | period label (row_check / convention) | FY2021 Q3 / Nov 2021 | FY2021 Q3 / Oct-Dec 2021 (acquisition date 17 Nov 2021) | FIXED |
| A5-134 | period label (row_check / convention) | FY2021 Q3 / Nov 2021 | FY2021 Q3 / Oct-Dec 2021 (acquisition date 17 Nov 2021) | FIXED |
| A5-137 | period label (row_check / convention) | FY2021 Q3 / Nov 2021 | FY2021 Q3 / Oct-Dec 2021 (17 Nov 2021) | FIXED |
| A5-138 | period label (row_check / convention) | FY2022 Q1 / Jun 2022 | FY2022 Q1 / Apr-Jun 2022 (1 Jun 2022) | FIXED |
| A5-139 | period label (row_check / convention) | FY2022 Q2 / Aug 2022 | FY2022 Q2 / Jul-Sep 2022 (10 Aug 2022) | FIXED |
| A5-140 | period label (row_check / convention) | FY2022 Q2 / Aug 2022 | FY2022 Q2 / Jul-Sep 2022 (acquisition date 10 Aug 2022) | FIXED |
| A5-141 | period label (row_check / convention) | FY2022 Q2 / Aug 2022 | FY2022 Q2 / Jul-Sep 2022 (acquisition date 10 Aug 2022) | FIXED |
| A5-144 | period label (row_check / convention) | FY2022 Q4 / Jan 2023 | FY2022 Q4 / Jan-Mar 2023 (31 Jan 2023) | FIXED |
| A5-145 | period label (row_check / convention) | FY2023 Q1 / Apr 2023 | FY2023 Q1 / Apr-Jun 2023 (28 Apr 2023) | FIXED |
| A5-146 | period label (row_check / convention) | FY2023 Q1 / Apr 2023 | FY2023 Q1 / Apr-Jun 2023 (acquisition date 28 Apr 2023) | FIXED |
| A5-147 | period label (row_check / convention) | FY2023 Q1 / Apr 2023 | FY2023 Q1 / Apr-Jun 2023 (acquisition date 28 Apr 2023) | FIXED |
| A5-150 | period label (row_check / convention) | FY2024 Q1 / Apr 2024 | FY2024 Q1 / Apr-Jun 2024 (2 Apr 2024) | FIXED |
| A5-151 | period label (row_check / convention) | FY2024 Q1 / Apr 2024 | FY2024 Q1 / Apr-Jun 2024 (acquisition date 2 Apr 2024) | FIXED |
| A5-152 | period label (row_check / convention) | FY2024 Q1 / Apr 2024 | FY2024 Q1 / Apr-Jun 2024 (acquisition date 2 Apr 2024) | FIXED |
| A5-159 | period label (row_check / convention) | FY2024 Q4 / Jan 2025 | FY2024 Q4 / Jan-Mar 2025 (announced 9 Jan 2025) | FIXED |
| A5-170 | period label (row_check / convention) | FY2019 Q4 / Jan 2020 | FY2019 Q4 / Jan-Mar 2020 (acquisition date 29 Jan 2020) | FIXED |
| A5-193 | period label (row_check / convention) | FY2026 / 2026 | FY2026-FY2028 / Apr 2026-Mar 2029 (stated 11 Nov 2026) | FIXED |
| A5-194 | period label (row_check / convention) | FY2026 / 2026 | FY2026 Q3 / Oct-Dec 2026 (stated 11 Nov 2026) | FIXED |
| A5-215 | period label (row_check / convention) | FY2026 / Nov 2026-Mar 2027 | FY2026 Q3 / Oct-Dec 2026 (remaining at 31 Oct 2026) | FIXED |
| A5-225 | new: FY2025 Q4 slides p.5 | - | total return ratio FY2025 42%, FY2024 49% [F] | ADDED |
| A5-226 | new: same slide | - | share repurchase FY2025 114.2bn, FY2024 50.0bn [F] | ADDED |
| A5-227 | new: FY2025 Q4 notes p.6 | - | one-off SG&A in Q4, no amount [C] | ADDED |
| A5-228 | new: SSR85 p.24 | - | gain on valuation of financial instruments 1H FY2026 54,171 [F] | ADDED |
| A5-229 | new: FY2026 Q2 Q&A p.1 (A5) | - | one-time inventory write-down reversal, no amount [C] | ADDED |
| A5-230 | new: 84th p.133 | - | FY2025 call-option gain 17,312 [F] (second document for A5-033) | ADDED |
| A5-231 | new: 80th p.114 | - | FY2021 PP&E impairment 398 (closed dormitory) [F] | ADDED |
| A5-232 | new: SSR85 p.36 | - | no contractual obligation for further fund contributions [F] | ADDED |
| A5-233 | new: 84th p.180 | - | Salland goodwill attributed to the Test System segment [F] | ADDED |
| A5-234 | new: 84th p.167 | - | FY2025 interest on FVTPL liabilities 976 (FY2024 1,028) [F] | ADDED |
| A5-235 | new: 84th p.158 | - | FY2023 year-end dividend 13,291 (record 31 Mar 2024, paid 7 Jun 2024) [F] | ADDED |
| A5-236 | new calc | - | payment-date total return ratio FY2025 40.0% / FY2024 48.0%; record-date basis matches the company [I] High | ADDED |
| A5-237 | new: 84th p.108 | - | Micronics Japan 150,000 shares, carrying 1,386 (31 Mar 2026), 522 (31 Mar 2025) [F] | ADDED |
| A5-238 | new: 84th p.140 | - | Essai has no remaining goodwill or intangibles [F] | ADDED |

OK ids (value, unit, sign, period, page, quote and tag all as printed): A5-001, A5-002, A5-003, A5-004, A5-005, A5-006, A5-007, A5-008, A5-010, A5-011, A5-012, A5-013, A5-014, A5-015, A5-016, A5-017, A5-018, A5-019, A5-020, A5-021, A5-022, A5-023, A5-024, A5-025, A5-026, A5-027, A5-028, A5-030, A5-031, A5-032, A5-033, A5-034, A5-035, A5-040, A5-041, A5-042, A5-044, A5-045, A5-046, A5-047, A5-048, A5-049, A5-050, A5-052, A5-056, A5-067, A5-068, A5-072, A5-073, A5-074, A5-077, A5-078, A5-079, A5-080, A5-090, A5-091, A5-092, A5-103, A5-107, A5-108, A5-115, A5-116, A5-117, A5-118, A5-120, A5-122, A5-123, A5-124, A5-135, A5-136, A5-142, A5-143, A5-148, A5-149, A5-153, A5-154, A5-155, A5-157, A5-158, A5-165, A5-166, A5-167, A5-168, A5-169, A5-171, A5-172, A5-173, A5-174, A5-175, A5-176, A5-177, A5-178, A5-179, A5-180, A5-182, A5-185, A5-186, A5-187, A5-188, A5-189, A5-190, A5-191, A5-192, A5-195, A5-200, A5-201, A5-202, A5-203, A5-204, A5-205, A5-206, A5-207, A5-208, A5-209, A5-211, A5-216, A5-218, A5-219, A5-221, A5-222, A5-223.

Rows checked by quote match on the cited page only, without a further visual re-read: A5-041, A5-049, A5-056, A5-093, A5-094 to A5-098, A5-107, A5-115 to A5-119, A5-158 to A5-161. Each quote contains the row's value.

## Second-document cross-checks

| Headline figure | Document 1 | Document 2 | Result |
|---|---|---|---|
| Cash 401,785, bonds 89,486, leases 4,820 + 12,940, investment securities 432,586, goodwill+intangibles 82,520, equity 1,145,135 (30 Sep 2026) | Semi-Annual Securities Report 85th p.20 | FY2026 Q2 tanshin pp.8-9 | agree; no borrowings line in either |
| Cash 339,966; borrowings nil; leases 4,966 + 15,226 (31 Mar 2026) | Annual Securities Report 84th p.115 | FY2025 tanshin pp.9-10; SSR85 p.20 opening column | agree |
| Net interest-bearing debt (339,966) at 31 Mar 2026 | 84th Note 30(1) p.170 | recomputed in A5_net_cash.py | agree |
| Bonds 88,930 at 30 Jun 2026 | FY2026 Q1 tanshin p.8 | FY2026 Q1 briefing notes p.7 (88.9bn liability) | agree |
| CB terms: 100bn, 20 Apr 2026, maturity 28 Mar 2031, zero coupon, CP 36,000, exercise 4 May 2026-14 Mar 2031 | 84th Note 33 pp.182-183 | SSR85 Item3 pp.10-12; IR Bonds page (100,000; 0.00%; 28 Mar 2031) | agree |
| Facilities 40bn + 100bn, undrawn | 84th MD&A p.53 and Note 17(3) p.148 (140,000) | SSR85 p.7 | agree |
| R&I AA- (22 Jul 2026) | IR Bonds and Ratings page | R&I news 23 Jul 2026; integrated report p.23 ("from A+ to AA- in July") | agree |
| FY2025 buybacks 114,228 / TRR 41.9%; FY2024 50,000 / 48.8% | calc from programme documents | FY2025 Q4 slides p.5 (114.2bn, 42%; 50.0bn, 49%) | agree after rounding |
| Call-option gain ~17.3bn (FY2025 Q4) | FY2025 Q4 briefing notes p.5 | 84th p.133 and FY2025 tanshin p.15 (17,312); SSR85 Note 11 derivative asset 17,313 at 31 Mar 2026 | agree |
| Net income FY2025 375,353; FY2024 161,177 | 84th p.116 | FY2025 tanshin p.11; FY2025 Q4 slides p.5 (375.4, 161.2) | agree |
| Net income 1H FY2026 368,083 | SSR85 p.21 | SSR85 p.23 (changes in equity) | agree |
| Dividends FY2025 interim 21,094; FY2026 interim 35,376 | 84th p.158 | E_Info_20261028_03 (prior-year column 21,094) | agree |
| Technoprobe 42,774, PDF Solutions 17,294 (31 Mar 2026) | 84th Note 30(7) p.178 | 84th Item4 (5) p.107 | agree |
| Oct-2025 programme 5,759,000 sh / 149,996,716,000 yen | completion release 20 Aug 2026 | 84th p.69 (FY2025 slice) + SSR85 p.28 (1H FY2026 slice) | agree exactly |

## Calc re-run results

- `python3 -I` re-run of all four scripts before editing: output identical to the saved `.out.txt` files.
- Hard-coded inputs were checked against the cited rows: all match.
- Period windows: net cash uses point-in-time balances; total return ratio by fiscal year (FY2024 = Apr 2024-Mar 2025, FY2025 = Apr 2025-Mar 2026, 1H FY2026 = Apr-Sep 2026); cumulative FY2024 to 1H FY2026.
- Edits:
  - `A5_buybacks_returns.py`: dividend-timing check against the company ratios; one-off list for the net income used; JPY-million print of the Oct-2025 total so that A5-211 equals the output; corrected wording on the 99.7 cash-flow difference.
  - `A5_convertible.py`: round-down bounds (2,780,000 to 2,781,912) and explicit denominators.
  - `A5_mna_goodwill.py`: window note; FY2021 PP&E impairment 398 shown separately; 1H FY2026 cash-flow adjustment lines printed for A5-224.
  - `A5_net_cash.py`: unchanged.
- After the edits, every [I] value equals the script output; a re-run gives output identical to the saved files.
- Every [I] note follows "inputs: ...; script: ...; reason: ..." with High/Medium/Low.

## Gap re-attempts

- **Micronics stake size: filled** (A5-237).
- **Company total return ratio: partly filled.** Annual ratios are printed (A5-225); the cumulative MTP3 figure is still NOT DISCLOSED.
- **Tax effect of one-offs: not filled.** The 84th Note 15(3) tax-rate reconciliation (p.146) was read and does not itemise it.
- **Covenants: not filled.** A full-text search of the 84th, 85th and 83rd reports and the integrated report found no "covenant", "negative pledge" or "financial restriction".
- **CB early-redemption terms: not filled.** The 84th report pp.60-61 (Item4 stock acquisition rights) and the SSR85 CB pages hold only references to early redemption, the clean-up redemption notice and events of default.
- **FormFactor stake: not filled.** The 84th p.107 shows only "Other" (2 companies, 5,337) among the subsidiaries' listed holdings.
- **CB offering notices: not retried, as instructed.** E_Info_20260401_02/03/04 stay NOT RETRIEVED, with full URLs in A5_gaps.md.
- **No new document was fetched.**

## Remaining doubts

- **Effective interest rate of the CB.** It is not disclosed. The 2.50% implied accretion (A5-218, Low) rests on two quarter-end balances. Transaction costs and the tax effect on the equity component (100,000 - 7,712 - 88,930 = 3,358 gap) are not itemised.
- **Investment-fund exposure.** The 1H FY2026 fund purchases of 184,365 exceed the single USD 570m contribution disclosed in the 84th report. The fund names, managers and any further contributions are not disclosed. Fair value is Level 3 and based on the funds' own estimates.
- **The 99.7 gap in FY2025 treasury-share cash flow.** It is unexplained: brokerage commissions, odd-lot purchases (12.4m yen per 84th p.69) and settlement timing are all possible, but none is itemised.
- **Shin Puu goodwill allocation.** Its placement inside the R&D Altanova CGU remains an inference (A5-223, Medium).
- **The 31 Mar 2025 cross-currency swap.** The 84th p.173 maturity table shows a 2,924 swap liability next to the USD loan. It is not included in any net-debt variant, matching the company definition, which counts borrowings only.

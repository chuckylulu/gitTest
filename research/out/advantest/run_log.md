# Run log - Advantest Corporation (6857, Tokyo)

Session date: 2026-11-21. Rules: research/CLAUDE.md (imported by the root CLAUDE.md).

## Setup decisions (the user answered "no preference" to each question)
- Company: Advantest, chosen by Claude. It is the AI/HBM test leader, and its primary documents are all on advantest.com (no EDGAR dependency).
- SEC EDGAR: not used. sec.gov returns 403 without a contact User-Agent. A privacy guard blocks Claude from typing the user's email into commands. Anything only on EDGAR is logged NOT RETRIEVED. To enable EDGAR, the user sets `SEC_UA` themselves; `research/tools/fetch.py` reads it.
- prior/: empty in the repo (only .gitkeep), although the old CLAUDE.md layout note said 12 AI Studio exports. No prior/text/ extraction was possible. The premise check therefore covers the prompt only.
- B1 claims: the user listed none. Candidates were found by the CL module.

## Reachability check (2026-11-21, honest User-Agent "research-script/1.0")
- 200: ir.kla.com, novami.com, advantest.com, lasertec.co.jp, investors.teradyne.com, bis.gov, govinfo.gov, skhynix.com
- 403 (refuses scripts, not worked around): sec.gov (needs a contact UA), investors.ontoinnovation.com, investors.formfactor.com, meti.go.jp, tsmc.com, investor.tsmc.com
- Timeout: investors.camtek.com
- Note: an earlier probe with a browser-like User-Agent was refused by the session's safety classifier and was not repeated. All fetches use the honest UA.

## Steps
1. Scouted the advantest.com IR library (result, annual, briefing, report, sec-filings pages). robots.txt allows all.
2. Wrote tools: research/tools/fetch.py (polite download, naming `<date>_<issuer>_<doctype>.<ext>`, text extraction, manifest), findpage.py, quote_check.py, merge_parts.py.
3. Core download: 94 documents RETRIEVED, 0 failed (research/sources/advantest/_manifest.csv). Covered: financial results FY2017Q4 to FY2026Q2 (selected), briefing slides and Q&A for 15 quarters (notes for the last 6), Integrated Annual Report 2026, Annual Securities Reports 83rd (FY2024) and 84th (FY2025), Semiannual Securities Reports 84th 1H and 85th 1H, MTP3 slides and Q&A, IR technical briefing 2024, fireside chats 2025 and 2026, investors guide 2610, IR web pages.
   - Dates marked "date from PDF CreationDate" in the manifest come from PDF metadata, not from a printed date.
4. User stopped the session mid-download, then said "Run". Partial work was committed, and the run resumed.
5. Workflow 1 (8 parallel module agents A1-A6, TH, CL): extraction into out/advantest/parts/ and calc/. 2,213 rows (1,495 [F], 302 [C], 19 [S], 397 [I]). The agents saved about 120 more documents (older results for the cycle module, Federal Register rules, papers, Teradyne and Micron documents, company press releases). Firecrawl search credits ran out midway, and WebSearch was used after that.
6. Mechanical checks on the merged evidence.csv:
   - quote_check: all 1,816 quoted rows FOUND in their cited files (28 only after ignoring line breaks). Report: calc/quote_check_report_v1.csv.
   - New tool research/tools/row_check.py checks period labels, values against the cited page, verdict words and secondary sources. It flagged 154 rows (138 period-label conventions, 24 values, 2 verdict words). Report: calc/row_check_v1.csv. These were passed to the verifiers.
7. Manifest reconciliation (sources/advantest/_manifest.csv):
   - 6 arXiv rows for files first saved under .html names and then deleted were marked SUPERSEDED.
   - The PMC/MDPI row, which returned a reCAPTCHA page (file deleted, not worked around), was set to NOT RETRIEVED.
   - The missing row for 2022-04-27_advantest_financial-results-FY2021Q4-full-year.pdf was added.
8. File-name dates: 19 sources whose file-name date came from PDF metadata or a placeholder were renamed to the printed document date with research/tools/rename_dates.py. That covers the securities reports (84th filed 2026-06-26, 85th semiannual 2026-11-13, 83rd 2025-06-25, 80th 2022-06-22), nine older results releases, two Teradyne Q3 2026 documents, a SWTest deck and three press pages. All references in out/ and the manifest were rewritten, and the evidence `date` column was made consistent per file.
9. Workflow 2 (8 adversarial verifiers, one per module): re-open cited pages, cross-check against a second document, re-run the calc scripts, fix in place, and log to parts/<MOD>_verify.md.
   - Result: 2,380 rows after verification (A1 510, A2 198, A3 317, A4 436, A5 217, A6 354, TH 205, CL 143). All 1,943 quoted rows found. row_check shows 3 remaining flags, all false positives: A1-300 (the value is printed in an image table), A5-085 (printed as the word 'eight'), A5-131 (date printed in words).
   - Material corrections:
     - About 115 guidance and forecast rows retagged [F] to [C] as company forecasts.
     - Six arXiv preprints retagged [F] to [S], because no peer-reviewed or conference venue is printed.
     - A4 missed the entity-level customer table: NVIDIA International 20.2% vs NVIDIA Group 21.6%.
     - Two export-rule readings were rewritten (88 FR 73424 back-end exclusion scope; Jan 2025 rule widening sec. 744.11 to 3B992).
     - A6 added the ~2 bn FY2018 Q4 inventory loss: the 2018-19 margin drop excluding one-offs is -5.2 pp, not -8.4 pp. A6 also corrected the IFRS adoption date (FY2015).
     - CL re-sourced the record date: 15 May, from the statutory report.
     - The TechNews 'USD 8 bn' figure and the LLM-generated simplywallst page were dropped as ledger evidence.
     - The verifiers' per-module logs are in parts/<MOD>_verify.md, and their structured summaries in parts/_verify_summaries.json.
   - Four more files were renamed to printed dates: FY2015 Q1 and Q2 results; the FY2018 Q4 and FY2019 Q1 Q&A. calc/__pycache__ was removed from git and is now ignored.
   - Kept as is: the Integrated Annual Report 2026 file name (2026-11-11, from PDF CreationDate). The news index lists its release on 2026-10-16, so the saved file may be a later revision.
10. Workflow 3 (close-out):
    - Reconcile across modules (one-off SG&A quarter, write-down reversal quarter, period labels of dated statements).
    - B1/B2 ledger and facts; B3 catalysts, B4 gaps.md, B5 handoff.md.
    - Assemble dossier.md.
    - Run compliance, numbers and completeness critics, with up to 2 fix rounds.
    - Write review_packet.md.
    - Result: reconcile found no wrong printed values. It found one-off SG&A named for two quarters, FY2025 Q2 (about JPY 2 bn printed, link to the charge kept as sensitivity only) and FY2025 Q4 (no amount), and unified the tags of rows sharing a quote.
    - B1 keeps 6 claims. China/export controls (C4) moved to B3 and the excluded list; the memory-share claim was added.
    - gaps.md has 183 lines plus a list of documents to save by hand. handoff.md has 17 cells.
    - dossier.md is about 116 KB. 1,185 cited ids all exist, and the cited tags match evidence.csv.
    - Critic round 1 found 56 defects (8 major); round 2 found 19 (3 major). All were fixed or rejected with reasons in parts/XM_fixlog.md.
    - Fix round 2 read the public TDnet daily lists for 28 Oct-21 Nov 2026: 121 GETs with the honest User-Agent, 1.5 s apart, all HTTP 200. Advantest had no forecast-revision filing in that window (A3-322). The four list pages that hold Advantest items were then saved to sources/ by the orchestrator.
11. Orchestrator tidy-up:
    - Renamed the 83rd and 84th semi-annual reports to their printed filing dates (13 Nov 2024 / 13 Nov 2025) and updated DS-003 and the dossier.
    - Annotated 11 NOT RETRIEVED manifest rows that later saves superseded.
    - Updated calc/RP_check.py to the final packet layout: 0 problems.
12. Self-check (rules: clean-context sub-agent given only evidence.csv and sources/advantest/; ids from parts/packet_ids.txt, plus 5 handoff inputs):
    | id | verdict | action |
    |---|---|---|
    | A1-060, A1-067, A1-062, A1-064 | MATCH | - |
    | A1-316 | MISMATCH (period) | The row was labelled FY2026 Q3 / Oct-Dec 2026, the quarter of the statement, but the page speaks of 1H FY2026. Fixed to FY2026 1H / Apr-Sep 2026 (stated 28 Oct 2026). The cause was the reconcile step's rule of labelling past statements by their statement quarter. calc/XM_period_labels_fix.py restored the referenced period on all 64 rows the rule had moved; the packet row was updated. |
    | A4-407, CL-070, A2-001, A2-141, A2-038, A5-063, A1-295, A1-299, TH-119 | MATCH | - |
    | A4-134 | MATCH | The checker noted that the quote is an uninformative text-layer fragment; the value was verified on the rendered chart. The note was extended. |
    | Secondary: A5-017, A5-018, A1-174, A6-326, A6-170 | MATCH | - |
    Totals: 19 MATCH, 1 MISMATCH (fixed), 0 CANNOT OPEN.
    After the fix: merge 2,415 rows. quote_check: all 1,955 quoted rows found. row_check: 3 known false positives. RP_check: 0 problems. DS_id_check: 0 missing ids and 0 tag mismatches.

## Open items for the user
- Documents to save by hand into sources/advantest/: see the top of gaps.md. Most important are the three CB offering notices (E_Info_20260401_02/03/04, HTTP 403), which hold the CB call/put and lock-up terms.
- SEC EDGAR was not used. Teradyne 10-K/10-Q figures and any customer filings naming Advantest are NOT RETRIEVED.
- The IAR 2026 file name keeps 2026-11-11 (PDF CreationDate); the news index lists the report on 2026-10-16.

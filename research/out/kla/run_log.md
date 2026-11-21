# Run log - KLA Corporation (KLAC, Nasdaq, USA; FY ends June 30)

Session date: 2026-11-21. Branch: claude/festive-rubin-y6as19. Output folder: research/out/kla/.

## Setup decisions
- Rules: on this branch, research/CLAUDE.md was an empty skeleton (TODO placeholder). The full rules block (Modules A/B, evidence tags, self-check) was on branch ccr-2b9561fc-mqqdg4 (the Advantest session). I copied that research/CLAUDE.md, the root CLAUDE.md import line, and the four tools (fetch.py, findpage.py, quote_check.py, merge_parts.py) from that branch unchanged.
- prior/: the repo copy held only .gitkeep. The chat "KLA Corporation Metrology Audit Report" was found in the user's Google Drive (AI Studio export, file id 1tDqCPS6Wx-IPgKTV2XZXLdG0-9h9XSlY, modified 2026-11-19). It was saved as prior/kla_metrology_audit.json. The extractor research/tools/extract_prior.py wrote the user prompts and non-thought model text to prior/text/kla_metrology_audit.md. The KLA Step 1 exchange is at lines 4-68. The rest of the chat is about Onto, except a KLA row in the handoff table near line 1033. The two "Copy of ..." files in Drive have the same size (1,023,581 bytes) and were not downloaded.
- SEC EDGAR: sec.gov returns 403 (SEC_UA is not set). KLA's own SEC filings were taken from ir.kla.com's mirror of EDGAR documents, so no KLA filing depended on sec.gov.
- User-Agent: honest default "research-script/1.0 (non-commercial document research)" for every fetch.

## Reachability (2026-11-21)
- 200: ir.kla.com, d1io3yog0oux5.cloudfront.net (KLA IR CDN), www.kla.com, lasertec.co.jp, novami.com, camtek.com
- 301: rigaku-holdings.com
- 403: sec.gov

## Steps
1. Scouted ir.kla.com listing pages (sec-filings/quarterly-reports, annual-reports, financial-information/financial-results, news-events/presentations, investor-day-2026).
2. Core download: 53 documents RETRIEVED, 0 failed (sources/kla/_manifest.csv). Covered: 10-K FY23-FY26; 10-Q Q1 FY24-Q1 FY27; shareholder letters and earnings slides Q4 FY24-Q1 FY27 (no letter is posted for Q3 FY25); earnings releases Q1 FY24-Q1 FY27; Investor Day 2026 deck, full transcript and Q&A transcript; Services update (Nov 2025); Annual Report 2026; stock-split FAQ.
   - Dates marked "approximate" in the manifest (services update, annual report) are not printed dates.
3. Five parallel module agents (brief: out/kla/BRIEF.md): A1/A2; A3/A6/Q5; A4/A5; Q1/Q4/Nova; Q2/Q3. Each writes out/kla/parts/<part>.csv and notes.
- Correction (lead): an early lead note (in the Q1 agent prompt) said "Axion" does not appear in KLA's 10-K/10-Q text. That was wrong. "Axion" appears in the 10-K FY23-FY26 Item 1 product list. "Rigaku" appears in none of the saved KLA filings.
4. Manifest cleanup (lead): www.kla.com serves a JavaScript bot-check page to scripts. Five kla.com pages saved as RETRIEVED had no content. One federalregister.gov page was a CAPTCHA. All six were set to NOT RETRIEVED in the manifest, and the files were deleted. No evidence row cited them.
5. Merge: tools/merge_parts.py -> evidence.csv (483 rows after Module B rows). tools/quote_check.py: 392 quotes FOUND (3 layout-insensitive), 0 NOT FOUND, 0 flags; 91 rows have no quote ([I] rows and B-002).
6. Self-check (CLAUDE.md "Self-check before you finish"), run as workflow wf_29570f61-38f.
   - Rows checked: 20 [F]/[C] rows, 5 more than the required 15. Each was given to two independent clean-context checkers, in different groupings. The checkers saw only evidence.csv and sources/kla/.
   - Inferences: six key [I] rows each went to a separate skeptic told to refute them.
   - Results:
     - 16 rows: MATCH x2.
     - A3-026, A4-041: MISMATCH x2. A4-063, A4-068: MISMATCH x1 and MATCH x1.
     - Every mismatch concerned the tag, not the value or quote. These rows are forward-looking or untestable company statements (current guidance, KLA impact estimates) and should be [C], not [F]. A4-041 also had the wrong period: the high-20s China share is a CY2026 expectation, not Jul-Sep 2026.
     - Refuters: Q2-I01 partially wrong on metadata only (period label); Q4-033 partially wrong on scope wording; A3-025, Q3-I01, A4-031, A6-010 not refuted.
   - Fix: one rule was applied across the file. A forward-looking or not independently testable company statement is [C]. 19 rows were retagged [F]->[C]: A3-026, A3-033, A3-034, A3-035, A3-037, A3-040, A4-041, A4-057, A4-063, A4-068, Q2-001, Q2-002, Q2-003, Q2-004, Q2-005, Q2-007, Q2-012, Q5-005, Q5-011. Each carries a note. A4-041's period was corrected to Jan-Dec 2026. Tag references in the notes, dossier, handoff and review packet were updated.
   - Past quarterly guidance rows (A3-001 to A3-022) stay [F]. Each records a figure KLA issued, which the A3 test then compared with reported results. The CY2025 outlook (A3-030) stays [F] for the same reason.
   - KLA's AP revenue figures (~$950M, ~$635M) are now [C] throughout, matching A1-069/A1-070. They are management-defined figures outside the segment reporting and cannot be tested independently.
7. Completeness and rule critics (workflow wf_beacca7e-cbc): two clean-context critics compared the deliverables with the request and with CLAUDE.md. Findings and fixes:
   - Quarterly RPO was missing. The saved 10-Qs and 10-Ks for Q1 FY24-Q4 FY25 disclose quarterly RPO with a 12-month share. Added as A2-035 to A2-051 (8 RPO amounts [F], 8 KLA 12-month estimates [C], 1 series [I]). Script: calc/a2_rpo_series.py, which parses the saved texts. Also recorded: KLA dropped the quarterly RPO note from Q1 FY26 (Jul-Sep 2025) onward.
   - The 2012-15 downturn low had no one-off list. Fetched the Q1 FY15 10-Q: no one-off named, so the GAAP OM low of 17.0% holds with and without one-offs (A6-026, A6-027). Fetched the Q4 FY14 release: KLA-Tencor then reported non-GAAP net income and EPS only, with no non-GAAP operating margin (A6-028). The Q1 FY15 release is NOT RETRIEVED.
   - The fiscal year-end was restated in each appended note. build_dossier.py now strips those lines, so the year-end appears once in dossier.md. A Lasertec year-end line remains.
   - Verdict words: "CONFIRMED" in the prior-claim tables became "MATCHES SOURCE", and "NOT VERIFIABLE" became "UNSUPPORTED". The dossier head explains these status words. The only remaining verdict word ("refute") sits inside [I] Q4-033.
   - Bare NOT DISCLOSED / NOT RETRIEVED markers: each now carries its (read: ...) / (tried: ...) clause. "Not attempted" items now read "tried: none; no attempt in this session".
   - Section 2 headline rows now carry both fiscal and calendar labels.
   - B2 now gives single facts tagged only [F]/[C]. The earlier pessimistic item 1 cited [I] rows.
   - gaps.md is rebuilt from every marker in dossier.md (122 items) plus 24 manifest NOT RETRIEVED documents.
   - An untagged Camtek "leadership" claim with no saved source was removed from the Q2 notes.
   - Not changed, and why:
     - Some table cells still carry two tagged items, e.g. a [F] value next to an [I] share. Each item is tagged separately.
     - B3 keeps the expected earnings windows, which are marked [I] because the dates are not announced, and two undated rows marked "Not dated".
8. Final checks: evidence.csv has 503 rows ([F] 272, [C] 101, [I] 93, [S] 37). quote_check: 410 FOUND, 0 NOT FOUND, 0 flags. Every evidence id cited in dossier.md (460), handoff.md (70) and review_packet.md (21) exists, and the "[tag] id" pairs agree with evidence.csv.

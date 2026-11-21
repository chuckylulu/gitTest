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

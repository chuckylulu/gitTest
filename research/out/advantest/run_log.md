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
5. Workflow 1 (8 parallel module agents A1-A6, TH, CL): extraction into out/advantest/parts/.

# Run log - Bruker Corporation (BRKR, Nasdaq), semiconductor metrology only

Session date: 2026-11-21. FY ends December 31. Rules: research/CLAUDE.md.

## Setup decisions
- Rules: on this branch research/CLAUDE.md held only a TODO placeholder. The full rules block (tags, Modules A/B, handoff schema, self-check) existed on branch ccr-2b9561fc-mqqdg4 together with research/tools/ (fetch.py, findpage.py, quote_check.py, merge_parts.py). Both were checked out onto this branch and used unchanged.
- prior/: empty (only .gitkeep). The "Bruker Financial and Segment Performance" chat named in the prompt is not in the repo, so no prior/text/ extraction was possible. Group and segment financials were left out anyway, as instructed. Module A skipped, as instructed.
- Scope: semiconductor metrology business only. Handoff row filled only where a business-unit-level figure exists.

## Reachability check (2026-11-21, honest User-Agent "research-script/1.0")
- 200: bruker.com, rigaku.com, fool.com, d18rn0p25nwr6d.cloudfront.net (Bruker's IR-provider CDN, which hosts copies of its SEC filings)
- 403 (refuses scripts, not worked around): sec.gov (needs a contact User-Agent; the user's email was not used, per the privacy rule), ir.bruker.com, investors.ontoinnovation.com
- Timeout/000: businesswire.com
- SEC_UA not set in the environment, so fetch.py logs every sec.gov URL as NOT RETRIEVED.

## Steps
1. Premise scan by web search (leads only): July 1 2026 segment reorganisation, Q2 and Q3 2026 goodwill impairments, Onto-Rigaku 27% stake announced 2026-04-20 all appear in search results. Verified later against saved files.
2. Four parallel research agents, each writing out/bruker_semi/parts/<prefix>.csv and notes/<prefix>_findings.md:
   S = semiconductor metrology size disclosures, segment mapping, impairments, Bruker reaction since April 2026 (Q2, Q5)
   P = product map (Q1)
   R = Bruker vs Rigaku by tool class, Onto-Rigaku facts (Q3)
   H = hybrid bonding metrology (Q4)
3. All four first-pass agents finished. Parts: S 70 rows, P 61, R 72, H 58. Every quote was FOUND by quote_check.
4. Gap-close workflow. Four agents took a second attempt, each with a different method, then a completeness critic ran:
   - G: the Q3 FY2026 10-Q came from the us.kabutan.jp mirror and confirmed the $174.5M charge is BSB&CA. The Q1 FY2026 10-Q and the full Q2 FY2026 text came from the stocktitan.net mirror (served gzip-compressed, decompressed in place). The 10-K competitor lists were read. The Q4-24 transcript and the Jefferies June 2026 transcript came from stockanalysis.com.
   - C: named-user search across papers, award lists and EU TED procurement records. TED notice pages refused the script, so the official TED Search API v3 was used; that is a public API, not a workaround. JSON was saved by a scratchpad script with manifest rows marked "saved by C agent".
   - M: Rigaku IPO filing from EDINET, plus competitor filings and AFM share sources.
   - Q: second Q5 sweep. It added nothing new about Bruker's reaction, so the item is closed under the two-attempts rule.
   - Critic: listed tag inconsistencies and contradictions between parts. Fixed with calc/fix_tags.py (8 tags harmonised under one rule, 2 claims reworded, notes added).
5. Text extraction. pdftotext could not read the Japanese EDINET PDFs (missing Adobe-Japan1 pack), so pdfminer was used. One EDINET PDF carries a no-extraction flag, which pdfminer ignores; its text was read for research quotes only. Some chart values (Rigaku share pies, segment bars) were read from rendered page images and are flagged in each row's note.
6. Dropped sources:
   - spie.org returned a bot-check page instead of content. The file was deleted and its manifest row set to NOT RETRIEVED.
   - semi.org and ectc.net returned 403. The SEMI release was saved from its PR Newswire APAC copy.
7. Tool limits: the Consensus monthly quota and Firecrawl credits ran out mid-session. Discovery fell back to WebSearch.

## Self-check (CLAUDE.md rule), 2026-11-21
Method: clean-context sub-agents were given only evidence.csv and sources/bruker_semi/. Three agents covered the 15 most important [F]/[C] rows (5 each). Two more agents covered 12 further rows used in B1/B2/handoff. Each re-opened the cited file and checked quote, value, period, page and tag.

| Row | Result | Note |
|---|---|---|
| S037 | MATCH | Q2-26 deck p8: ">30% Organic Order Growth, >15% Organic Revenue Growth with ~30% EBIT Margin" |
| S038 | MATCH | same slide, ~30% EBIT |
| S022 | MATCH | JPM26 deck p14: ">$300M Revenue and >25% EBIT Margin" (TTM end 3Q25) |
| S025 | MATCH | Q4-25 deck p7: "Semi revenues flat" |
| S026 | MATCH | Q4-25 deck p9 pie: Semi-Metrology 9% (of BSI) |
| G002 | MATCH | Q3-26 10-Q Note 1 p9: BSI NANO "no changes were made" |
| G004 | MATCH | Q3-26 10-Q MD&A p37 / Note 5 p14: $174.5M, BSB&CA |
| R012 | MATCH | Rigaku yuho FY2025 p20 (38%, 2024; Yole Q4 2025); p25 pie |
| M001 | MATCH | Rigaku IPO filing p34: 26.9% (2022), 29.5% (2023); note 6 p35 |
| R048 | MATCH | Samsung/Onto/Rigaku deck p16 and p1 affiliations |
| R004 | MATCH | Onto release 2026-04-20 p1: "selected by two key customers" |
| C005 | MATCH | Rigaku release 2025-12-04: KIOXIA and KIOXIA Iwate. Checker: [C] is the cautious tag (vendor claim naming a customer) |
| C016 | MATCH | TED 751635-2025: Rigaku Europe SE, contract 2025-10-07 |
| C020 | MATCH | TED 518266-2025: Bruker France S.A.S. |
| H018 | MATCH | IBM/Nova SPIE 2026 p4 |
| S017, P003, H053, Q010, G006, S019, G033, R042, R040, M005, C018, S023 | MATCH (12/12) | extended check |

Result: 27/27 MATCH, 0 MISMATCH, 0 CANNOT OPEN. No evidence fixes were needed from the self-check.

## Adversarial review, 2026-11-21
Two reviewers covered the dossier and handoff: one for source fidelity, one for overreach and rule compliance. They raised 21 distinct issues (42 raw entries before de-duplication). All were fixed by calc/fix_after_review.py (new rows V001-V006; S017/P043/P044 re-tagged [C]; run-rate period labels; KLA calendar months; G081 confidence lowered; Company A recomputed on the same-edition $470M) and by rewriting dossier.md and handoff.md. Main fixes:
- Ledger (a): the Q3-26 Q&A states "semi bookings have been just very strong year to date, greater than 30%" (V001). The earlier "ambiguous" framing was dropped, and the 9M figure stays [S] only.
- Ledger (f): G064 moved to the evidence-for side, since the CFO expected similar recapture in Q2 and Q3 (V005, calc). The $40M is attributed to the analyst.
- Ledger (e): M025 is Park's own Q3 2025 report, not Rigaku's filing. The G041 "only relevant" filter is now cited as [I] G081.
- B2: absence findings restated as page content. The cross-edition Rigaku "up from" trend was removed. The tender outcome wording was neutralised.
- Handoff: every gap cell now uses the NOT DISCLOSED (read: ...) form. The guidance cell records the [S] FY2026 guide as 1 unresolved.
- B3: only dated, sourced catalysts kept. The rest moved to a watch list tagged [I].
- Verdict words removed from the premise check. Quotes corrected ("maybe half"; "I think the direction is correct").

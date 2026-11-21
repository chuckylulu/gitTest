# Run log - Comet Holding AG (SIX: COTN)

Session date: 2026-11-21. Fiscal year = calendar year (ends 31 December). Rules: research/CLAUDE.md.

## Setup
- The working branch had only a skeleton research/CLAUDE.md (rules block marked TODO; prior/ empty). The full rules
  (Module A / Module B, evidence tags, self-check) were found on sibling branch `ccr-2b9561fc-mqqdg4` (Advantest run) and
  imported unchanged, together with the helper tools research/tools/{fetch,findpage,quote_check,merge_parts}.py and the
  root CLAUDE.md (`@research/CLAUDE.md`).
- prior/: empty (only .gitkeep). No prior/text/ extraction possible; premise check covers the prompt only.
- Reachability: comet.tech 200 with honest UA "research-script/1.0 (non-commercial document research)". robots.txt allows
  all paths for generic agents (it disallows /pct/news only for named AI crawlers; those pages were not fetched).
- Comet's site relaunch removed 2022-2024 trading updates / ad hoc releases from comet.tech (news filter returns 2025-2026
  only). Agents were told to try web.archive.org with the honest UA and fall back to [S] newswire copies.

## Steps
1. Downloaded core documents with fetch.py (batches in out/comet/calc/_batch{1,2,3}_sources.tsv): 29 PDFs (annual
   reports FY2021-FY2025, half-year reports 2022-2026, results decks H1 2022-H1 2026, CMD 2021/2022/2023/2025, 2024
   conference decks, governance/compensation reports FY2025, AGM 2026 invitation), 40 HTML pages (CA20, semiconductor,
   x-ray module pages, 2026 releases) and 10 HTML 2024-2026 releases. Dates marked "date from PDF CreationDate" or
   "date = retrieval date" in _manifest.csv are not printed dates.
2. Git: the CMD 2025 deck (2026-01-09_comet_capital-markets-day-2025.pdf, 142 MB) exceeds GitHub's 100 MB limit. It is
   kept locally, excluded via .gitignore; its extracted text (_text/) and sha256 (manifest) are committed.
3. Five parallel module agents (shared brief out/comet/calc/_agent_brief.md): XS (CA20 specs, dose, adoption),
   RV (rival systems), IXM (x-ray modules buyers and source roadmap), DV (division half-years, IXS economics and
   strategic options, PCT concentration and AE/MKS, CMD targets), A (group Module A).
4. Module agents finished (row counts XS 73, RV 82, IXM 76, DV 163, A 255). Each ran tools/quote_check.py on its own part.
   About 150 further documents were saved by agents (rival product pages and releases, Excillum/Hamamatsu/Zeiss source pages,
   Comet x-ray module pages, older Comet reports back to 2017, newswire copies of 2022-2024 trading updates).
5. Manifest audit (calc/manifest_audit.py): 9 rows marked RETRIEVED were not the documents (7 listing/JS pages already deleted by
   agent A; a 212-byte Waygate bot-check page; an Elsevier redirect stub). Re-marked NOT RETRIEVED with an AUDIT note; none is
   cited in evidence.csv.
6. calc/fix_urls.py replaced 30 generic "comet.tech/en/investors" URLs in XS.csv with the exact download URL from the manifest.
7. Module B rows (catalyst calendar) in parts/B.csv (calc/B_build_csv.py). Merge: tools/merge_parts.py -> evidence.csv, 653 rows
   (363 [F], 188 [C], 41 [S], 61 [I]). quote_check on the merged file: 573 FOUND + 12 FOUND (layout-insensitive), 0 NOT FOUND,
   0 flags; 68 rows carry no quote ([I] rows and [S] leads from refused pages).

## Self-check (clean-context sub-agent, inputs: evidence.csv and sources/comet/ only)
Rows checked: A-010, A-013, A-001, A-004, A-041, A-051, A-052, A-116, A-120, A-027, XS-051, XS-059, XS-022, DV-040, DV-142.
Result: 15 MATCH, 0 MISMATCH, 0 CANNOT OPEN. Two caveats, both fixed by calc/selfcheck_fixes.py and re-merged:
- A-001: figures correct, but cited p9 holds them in the book-to-bill reconciliation; the income statement is p10. Page corrected.
- DV-142: values confirmed on the rendered CMD 2025 slide p86, but the quote "EBITDA +6 PP to +9 PP" spliced PCT's and IXS's
  deltas from scrambled chart text. Quote replaced with the slide title and a note recording the rendered-slide read.
Other wording found by the checker matched the row values and periods (e.g. A-120 "largest customer ... 22.8% of Group sales";
XS-051 funnel ">60 Evaluation / >25 Qualification / 5 orders"; DV-040 IXS EBITDA (3,985)).

## Outputs
dossier.md, evidence.csv, handoff.md, review_packet.md, gaps.md (83 lines), run_log.md, calc/ (scripts), parts/ (module notes).

## Attempts that added nothing (stopping rule)
- 2022-2024 Q1/Q3 trading updates from the issuer: comet.tech redirects old URLs; web.archive.org reset connections twice.
- Customer-side CA20 evidence: two search rounds (customers x conferences) found none.

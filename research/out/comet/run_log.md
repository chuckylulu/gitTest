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

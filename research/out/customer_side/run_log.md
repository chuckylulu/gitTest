# Run log - customer_side (cross-cutting question)

Session date: 2026-11-21. Rules: research/CLAUDE.md (imported by the root CLAUDE.md).

Question: what SK hynix, Samsung, Micron, TSMC, Intel, ASE and Amkor themselves say they use to inspect and measure HBM stacks and hybrid-bonded interfaces, January 2025 to 21 November 2026. Modules A and B do not apply (user instruction). Deliverables: dossier.md, evidence.csv, gaps.md, review_packet.md (plus this run log and calc/).

## Setup decisions
- The rules block was missing on this branch: research/CLAUDE.md here held only a TODO placeholder. The filled-in rules, the root CLAUDE.md import and the tools (fetch.py, findpage.py, quote_check.py, merge_parts.py) were copied unchanged from branch `ccr-2b9561fc-mqqdg4` (the Advantest run). New tools written for this run: research/tools/crossref_venue_list.py, research/tools/s2_batch.py.
- prior/ is empty (only .gitkeep). No prior/text/ extraction was possible; the premise check covers the prompt only.
- Fiscal year-end: not applicable. No company financials are used in this run; all items are technical statements dated by calendar month.
- The user's email is not sent in any request (privacy rule of this environment). Consequences: no SEC EDGAR, no OpenAlex polite pool.
- Agents: six background sub-agents, each writing to out/customer_side/parts/ under a shared brief (parts/_common_brief.md):
  XR (X-ray dose + TSMC SEMICON Taiwan 2026 keynote), SMP (sampling intensity / virtual metrology), AW (supplier awards), TALK (blogs, investor and tech-day material, SEMICON talks), PAPM (papers: SK hynix, Samsung, Micron, SPIE volumes), PAPL (papers: TSMC, Intel, ASE, Amkor).

## Reachability check (2026-11-21, honest User-Agent "research-script/1.0 (non-commercial document research)")
- Accept scripts (200): news.skhynix.com, skhynix.com IR, news.samsung.com, semiconductor.samsung.com, samsung.com/global/ir, micron.com, amkor.com, intc.com, ieee-iedm.org, irps.org, vlsisymposium.org, iitc-conference.org, api.crossref.org, api.semanticscholar.org (shared unauthenticated quota, intermittent 429), arxiv.org, most trade press, several vendor sites.
- Refuse scripts (403 or bot challenge; not worked around): tsmc.com, pr.tsmc.com, esg.tsmc.com, investor.tsmc.com (Cloudflare challenge); semi.org, semicontaiwan.org, semiconkorea.org (Cloudflare challenge); ectc.net (403); ieeexplore.ieee.org (202 empty bot-challenge page); intel.com www (403); aseglobal.com, ir.aseglobal.com (403); ir.amkor.com (403); investors.micron.com (403); researchgate.net (403); spiedigitallibrary.org and spie.org presentation pages (Incapsula / "Pardon Our Interruption" challenge); appliedmaterials.com, hitachi-hightech.com, nordson.com, sigray.com (403).
- api.openalex.org: daily free budget for this network exhausted (429, reset at midnight UTC); a key would need the user's email, so not used.

## Paper inventory method (main session)
1. Crossref volume listings saved for ECTC 2025, ECTC 2026, IEDM 2025, IRPS 2025, IRPS 2026, VLSI 2025, VLSI 2026, IITC 2025, ASMC 2025, ASMC 2026, EPTC 2025, IPFA 2025, ITC 2025, ITC 2026, ISTFA 2025-26, IMW 2025, IMW 2026, LTB-3D 2026 and SPIE Metrology, Inspection, and Process Control XXXIX (2025) and XL (2026) (research/sources/customer_side/*_crossref_*-volume-list.json; exact container titles in calc/venues.tsv).
   - IITC 2026 and IPFA 2026: 0 records under the expected title on 2026-11-21 (not yet registered in Crossref, or titled differently).
   - VLSI 2026: first title guess returned 0; the correct title is "2026 IEEE/JSAP Symposium on VLSI Technology and Circuits (VLSI Technology and Circuits)" (re-fetched as VLSI2026b).
   - SPIE listings carry no affiliations.
2. calc/paper_scan.py: affiliation regex over every author of every record. Coverage (calc/coverage_count.py): 3,378 IEEE/ASM records, of which 3,293 carry at least one affiliation; 559 papers have an author from one of the seven (Samsung 214, Intel 116, TSMC 97, Micron 65, ASE 38, SK hynix 26, Amkor 4; one Samsung Electro-Mechanics paper excluded as out of scope). Output calc/paper_candidates.csv.
3. research/tools/s2_batch.py: Semantic Scholar batch records for the 559 DOIs (491 with abstract) and the 309 SPIE MIPC DOIs (267 with abstract; first attempt 429, second succeeded).
4. calc/abstract_screen.py: keyword screen (scope x method) to prioritise reading; 126 shortlisted. The screen is a reading aid only; inclusion decisions are made by reading the abstracts (PAPM, PAPL).
5. Limits of this method: (a) only venues listed in calc/venues.tsv; (b) papers whose Crossref record lacks affiliations are invisible to the scan (85 of 3,378 records); (c) abstracts only: full texts sit behind ieeexplore's bot challenge; (d) SPIE papers cannot be attributed to a company unless the abstract names it.

6. Scan v2 (after PAPL reported misses): the affiliation pattern now drops commas/periods and matches "Intel" case-insensitively. It adds 3 TSMC ECTC 2025 papers ("Taiwan Semiconductor, Manufacturing Company") and 1 Intel IRPS 2025 paper ("INTEL Client Computing Group"); no SK hynix, Samsung or Micron paper was added; nothing dropped. 562 chipmaker papers in calc/paper_candidates.csv; additions listed in calc/paper_candidates_v2_added.txt. PAPL had already read all four (one in scope, PAPL-017).
7. IITC 2026 programme page saved (sources/customer_side/2026-11-21_iitc_IITC2026-program-page.html): no paper by the seven on inspecting or measuring HBM or hybrid bonds; Micron gave an invited talk on memory stacking (title only) and a workshop talk on HBM thermal challenges.
8a. Scan v3 (after PAPM reported misattribution): the Micron pattern now excludes "HANA Micron" (a Korean OSAT). Five ECTC 2025/2026 papers dropped (listed in PAPM notes). Final inventory: 557 chipmaker papers (Samsung 214, Intel 117, TSMC 99, Micron 60, ASE 38, SK hynix 26, Amkor 4); 486 with Semantic Scholar abstract.
8. research/tools/merge_parts.py patched to skip parts/*_table.csv (table files are not evidence files; reported by TALK).

## Module results (as reported; tag counts from the part files)
- SMP (sampling): 44 rows. XR (X-ray dose + TSMC keynote): 38 rows. AW (awards): 58 rows + 193-row winner table. TALK (non-paper statements): 61 rows + 43-row table. PAPL (TSMC/Intel/ASE/Amkor papers): 188 rows + 41-row table (26 papers). PAPM (SK hynix/Samsung/Micron papers, SPIE volumes, 4 JSTS papers read in open-access full text): 229 rows + 50-row table (42 papers). Every module ran quote_check with all quotes FOUND.
- Agent-side housekeeping: several agents re-saved documents under their printed dates and deleted first copies or bot-challenge pages; the main session then marked 33 manifest rows whose files no longer exist as NOT RETRIEVED (calc step in this log, 2026-11-21).

## Steps
(continued below)

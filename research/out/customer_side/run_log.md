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
9. Merge: research/tools/merge_parts.py (order PAPM, PAPL, TALK, XR, SMP, AW, then SYN and MAIN). Main-session parts:
   - parts/SYN.csv: 70 [I] rows from calc/method_matrix.py, one per company x method cell, dossier Section 5;
   - parts/MAIN.csv: premise and limit rows.
10. Generated pieces, assembled by calc/build_dossier.py from calc/dossier_template.md:
    - calc/build_tables.py: Section 1 table, one row per document, from the three module tables plus calc/section1_extra_rows.csv (method-bearing papers found by XR and SMP);
    - calc/awards_summary.py: Section 4;
    - calc/build_gaps.py: gaps.md, every NOT DISCLOSED / NOT RETRIEVED line from the module notes plus the main-session list, under the save-by-hand header calc/gaps_header.md.
    - calc/build_review_packet.py builds review_packet.md from evidence rows.
11. Self-check (required by the rules; scaled up because ultracode was on). Workflow customer-side-evidence-verify:
    - clean-context agents received only evidence.csv and sources/customer_side/ and re-checked EVERY row, not just 15;
    - every non-MATCH row went to a second agent told to refute the first;
    - results are in calc/verify_results.json.

- Rows checked: 618 (every row of evidence.csv at the time). First pass: {'MATCH': 510, 'PARTIAL': 106, 'MISMATCH': 2}.
- Flagged rows re-checked by a second, skeptical agent: 108; problem confirmed: 99 ({'PARTIAL': 97, 'MISMATCH': 2}); not confirmed: 9 (left unchanged).
- Confirmed issue types: {'other': 34, 'claim_overstates_source': 44, 'wrong_tag': 24, 'vendor_material_presented_as_chipmaker': 2, 'value_wrong': 2, 'chipmaker_attribution_unsupported': 5, 'page_wrong': 4, 'date_or_period_wrong': 5, 'inference_inputs_missing': 5}.
- Confirmed problems by module: {'PAPM': 28, 'PAPL': 15, 'TALK': 16, 'XR': 8, 'SMP': 24, 'AW': 8}.
- Fixes applied by module (fix agents): PAPM 28 applied, 2 noted, new rows PAPM-230, PAPM-231, PAPM-232; PAPL 16 applied, 4 noted, new rows PAPL-189; TALK 16 applied, 3 noted, new rows none; XR 8 applied, 2 noted, new rows none; SMP 24 applied, 3 noted, new rows SMP-045, SMP-046, SMP-047; AW 10 applied, 2 noted, new rows AW-059, AW-060.
- CANNOT OPEN: 0.

### The 15 most important rows (review packet claims): result of the self-check

| Id | First pass | Second check | Wording found by the checker (excerpt) | Tag after fixes |
|---|---|---|---|---|
| PAPM-049 | MATCH | - | We propose a practical but very effective method for pre-screening of these interface failures in mass production with the idea of small changes in BE | [F] |
| PAPM-222 | PARTIAL | confirmed PARTIAL | III. CONCLUSIONS: "The optimized process was successfully applied in mass production, demonstrating improved productivity and stable quality, with no  | [C] |
| PAPM-201 | MATCH | - | The results of this study have been implemented into measurement equipment and developed into a commercialized solution currently in use. | [C] |
| ADDL-002 | MATCH (completeness-round check) | - | Exact quote on p3 ('HVM starting in 2019'). Wafer/die sort comes from the p11 table. A production statement, so [C] is correct. | [C] |
| PAPM-216 | MATCH | - | Final validation using actual HBM device wafers in a production-grade MI setup confirmed these findings. | [F] |
| PAPM-136 | MATCH | - | Micro-bump joint integrity for entire 12-layer stacks after reliability confirmed with daisy chain resistance and Confocal Scanning Acoustic Microscop | [F] |
| SMP-031 | MATCH | - | The implementation of 100% overlay measurement is needed ... to achieve high overlay metrology throughput with 100% chiplet inspection ... roadmap tow | [F] |
| PAPL-046 | MATCH | - | A test vehicle featuring a dense grid of fiducials across the chiplet is fabricated to enable near-infrared (NIR) post-bond chiplet level overlay mapp | [F] |
| PAPM-016 | MATCH | - | CSAM results are clean of voids, and X-section shows satisfactory bonding results on both bonding interfaces. | [F] |
| TALK-020 | MATCH | - | Advanced techniques, including optical inspection, X-ray microscopy, atomic force microscopy, and acoustic microscopy are examined alongside AI-powere | [F] |
| TALK-024 | MATCH | - | Samsung Electronics has begun introducing new inspection equipment for hybrid bonding, with Onto Innovation’s systems reportedly undergoing validation | [S] |
| XR-003 | MATCH | - | even after overexposure to three times the limit provided by DRAM manufacturer, no infant mortality failures were observed. However, the reliability o | [F] |
| XR-015 | MATCH | - | The public keynote abstract explicitly lists “DRAM/HBM damage concern by X-ray” among the challenges for advanced-packaging inspection. | [S] |
| ADDM-007 | MATCH (completeness-round check) | - | The quote is on p4: 10-20 min per wafer for SAM, and an interferometry alternative was developed. | [F] |
| TALK-014 | MISMATCH | confirmed MISMATCH | Quote is exact, from the paragraph beginning "The W2W method has been commercialized...": "For HBM, the D2W approach is being adopted and is progressi | [S] |

12. Fixes: workflow customer-side-apply-fixes (one agent per module file) applied the confirmed fixes; results in calc/fix_results.json. The main session then:
    - corrected the same wrong note on PAPM-217..229 and the TALK-037 period;
    - updated calc/method_matrix.py, calc/dossier_template.md, calc/section1_extra_rows.csv and calc/build_review_packet.py;
    - rebuilt everything.
    Merged evidence after fixes: 705 rows; quote_check: 610 quotes FOUND (2 layout-insensitive), 95 [I] rows without quote, 0 NOT FOUND.
    Consequences for the conclusions:
    - Samsung's IRPS 2025 HBM micro-bump pre-screen is a proposal ("We propose ... in mass production"), not a statement of use. Its matrix cell moved from production to pilot.
    - SK hynix's "successfully applied in mass production" (PAPM-222), its VM in-use statements (TALK-004, SMP-001/002/007, PAPM-197), Micron's AI-classification statements (SMP-022, TALK-038/039/041) and Amkor's test offer (SMP-038) are company claims, now tagged [C].
    - The SK hynix newsroom "Tech Note" on hybrid bonding is a guest article by an Inha University professor (TALK-014/015, now [S]).
    - Several papers were relabelled as university-led or vendor-led with chipmaker co-authors: PAPM-051, PAPM-094, PAPM-143, PAPL-145, PAPL-155, PAPL-167.

13. Critique round (workflow customer-side-critique; results in calc/critique_results.json). Five clean-context agents:
    - one read the dossier prose against evidence.csv and found 36 problems: a method ranking contradicted by the dossier's own table; production wording attached to a recipe rather than to an inspection step; "two exceptions" followed by four items; X-ray debug work labelled failure analysis; ids pointing at the wrong rows; Nearfield-led and Yokohama-led papers presented as Samsung's or SK hynix's;
    - two checked the Section 1 table and found 69 cell problems;
    - two completeness critics searched the web and proposed 30 missed in-period items.
    The main session applied the 36 prose fixes after checking each against the cited rows, and moved the method ranking to a script (calc/method_counts.py). It also corrected a wafer count: SMP-016 measured six wafers, three top and three bottom, not three.
14. Completeness round (workflow customer-side-gapfill-and-table-fix; results in calc/gapfill_results.json).
    - Collection: 22 candidates were chosen; 7 were dropped because they could be had only from refusing hosts or republishers, or added nothing. Two collectors (ADDM: memory makers; ADDL: logic and OSAT) added 19 documents: ADDM 65 rows, ADDL 58 rows, plus tables and notes.
    - Access rule kept: critics had read some pages with a web-fetch tool. Every addition was re-fetched with fetch.py. These hosts refused and stay NOT RETRIEVED: pr.tsmc.com (award PDFs, one fetch.py test, 403), www.intel.com (Foveros Direct brief, 403), globenewswire.com, pubs.acs.org, wiley and sec.gov. Republishers (stocktitan.net, storagenewsletter.com) were not used.
    - Clean-context check of the new rows:
      - ADDM: {'MATCH': 40, 'PARTIAL': 24, 'MISMATCH': 1}. Mostly affiliation pointers to the Crossref record, plus one author-count error (3 of 9 SK hynix authors, not 3 of 8); all fixed in place.
      - ADDL: {'MATCH': 45, 'PARTIAL': 13}. Wording softened to match the decks and the patent.
    - Table fixes: 69 of 73 cell fixes applied; 4 were not, because they would need [C] evidence rows that do not exist.
    - The main session added MAIN-010 to MAIN-012 for three quotes that table cells used without an evidence row. MAIN-011 quotes only the first clause because the SMT007 text is two-column.
    - build_tables.py now splits combined tags before joining.
    Effect on findings:
    - Intel electrical test moved to production (micro-bump sort on Foveros since 2019, [C] ADDL-002).
    - Samsung X-ray scatterometry: pilot (XCD "production-level capability", [C]). Micron X-ray scatterometry: lab (XRR).
    - Micron electrical test: pilot (HBM4 MBIST, [C]).
    - TSMC optical: lab (carrier-wafer optical metrology).
    - Samsung acoustic now carries its stated limit: a SAM full-wafer scan takes 10-20 min.
    - The bottom line, Sections 1, 2.2, 3 and 5 and the review packet were rewritten accordingly.
    Final build: 832 evidence rows ([F] 578, [C] 73, [S] 84, [I] 97); every quote FOUND.

15. GitHub push protection blocked a commit. sources/customer_side/2026-11-21_nist_fcmn2026-page-571991.html, a NIST page saved by the ADDM collector, embeds the site's own Mapbox access token in its Drupal settings. The token was replaced with "[REDACTED-third-party-mapbox-token]", the manifest sha256 and note were updated, and the unpushed commit was amended. Nothing else in the page changed.


16. Final check (workflow customer-side-final-check; results in calc/final_check_results.json). Two clean-context lenses: evidence faithfulness, and compliance with the rules and the five asks. They found 16 must-fix items and a number of should-fix items. All must-fix items and most should-fix items were applied in the scripts and template, then everything was rebuilt.
    Content changes:
    - Samsung electrical test moved to lab: no statement places the test on production wafers or lines.
    - Micron X-ray CT moved to none: an irradiation study is not inspection use. ASE acoustic moved to none: adjacent flip-chip FA.
    - PAPM-224, TALK-006 and TALK-007 retagged [C] as in-use statements; Samsung optical, SK hynix optical and SK hynix e-beam now carry [C].
    - Premise item 4 now cites TSMC's CPS test of the SoIC stack (ADDL-025).
    - Premise items 9 and 10 were added: VM "replacing" measurement, and award vendors not being named.
    - Section 3.1 now has a by-generation block (HBM4, HBM4E). An HBM4E line was added to the bottom line.
    - The Section 3.4 direction table now says "supplemented by VM-AI" where VM adds coverage. Rows were added for SK hynix all-chip warpage and Samsung's roughly 4% measurement with ML imputation.
    - The Section 4 award table gained SK hynix rows and Amkor's December 2025 award, with tagged "none" cells; Micron 2026 is now 13 companies.
    - The Section 2.1 table gained the Intel copper-filter row (XR-006, MAIN-011).
    - The method-count regexes were tightened (X-ray CT no longer counts XRD, XRR or EDX; optical no longer counts X-ray reflectometry). The count is now [I] MAIN-013.
    Form changes:
    - Section 1 uses one tag per row, with other-tag ids listed in the evidence column.
    - Missing data appears only as "NOT DISCLOSED (read: ...)" or "NOT RETRIEVED (tried: ...)". gaps.md lines now start with the form, and five duplicate or misclassified lines were dropped.
    - Verdict words in the analyst's voice were removed.
    - New rows: MAIN-013 to MAIN-015.
    Not applied: E8's option to add a new [S] row for the blog's naming claim; the dossier drops the claim instead. C17 says "or add a note"; retagging was chosen.
    Final mechanical checks:
    - quote_check over evidence.csv: every quote FOUND;
    - no loose missing-data forms and no verdict words outside quotes or [I] lines in dossier.md (script check);
    - every evidence id cited in dossier.md exists (build_dossier.py check).

# Run log — Nova Ltd. (NVMI; Nasdaq and TASE; FY ends 31 Dec)

Session date: 21 Nov 2026. Branch: `claude/adoring-planck-4ozwd9`. Output folder name: `nova`.

## Setup decisions
- **Rules.** `research/CLAUDE.md` on this branch contained only a TODO placeholder. The full rules block (purpose, folders, tags, Modules A/B, self-check, review packet) existed on remote branch `ccr-2b9561fc-mqqdg4` (commit 3bcba52, from an earlier Advantest run). I copied that `research/CLAUDE.md`, the root `CLAUDE.md` (which imports it) and `research/tools/{fetch,findpage,merge_parts,quote_check}.py` onto this branch and followed them. The tools were read in full before use; they are the user's own repository code, not downloads.
- **prior/.** Empty (only `.gitkeep`). The "12 files exported from AI Studio" are not in any branch, so no `prior/text/` extraction was possible. Research notes on branch `ccr-34a6116a-tswdup` (an earlier chip-metrology study) were used as leads only.
- **SEC EDGAR.** Not used. sec.gov returns 403 without a contact User-Agent, and `SEC_UA` is not set in this session. I did not type the user's email into requests: the system rules forbid sending personal details to outside services unless the user explicitly asks, and the earlier run recorded a privacy guard blocking it. Everything Nova files on EDGAR that was needed (20-F, results) is also published as PDFs on novami.com, which was used instead. EDGAR-only items are logged NOT RETRIEVED in `gaps.md`. To enable EDGAR, set `SEC_UA` in the environment; `fetch.py` reads it.
- **Transcripts.** Nova does not publish call transcripts. I used stockanalysis.com (all calls Q4 2022 to Q3 2026 plus 2025–2026 conferences) and TradingKey (Q3 2026). All call content is tagged [S]. Seeking Alpha, Quartr, Investing.com, Benzinga, roic.ai and MarketBeat earnings pages refused the script (403); none was worked around.
- **novami.com listings.** The filings page lists older years through the site's own AJAX year filter (`admin-ajax.php`, actions `quarterly_earnings_by_year` and `annual_statements_by_year`). I called those read-only listing actions, equivalent to clicking the public year filter, to find the PDFs for 2020–2025. No forms, sign-ins or account tools were used.

## Reachability (honest User-Agent "research-script/1.0", 21 Nov 2026)
- **200:** novami.com, ssl4.eir-parts.net (Rigaku TDnet), s24.q4cdn.com (Onto PDFs), rigaku.com, spie.org (volume pages; paper pages bot-challenged), irds.ieee.org, semiengineering.com, stockanalysis.com, tradingkey.com, insidermonkey.com, allmind.ai, federalregister.gov API, prnewswire.com.
- **403:** sec.gov, maya.tase.co.il, magna.isa.gov.il, quartr.com, seekingalpha.com, investing.com, benzinga.com, roic.ai, marketbeat.com earnings pages, semicontaiwan.org PDF, patents.justia.com.
- **Other errors:** govinfo.gov PDF returned 502; novami.com 2018 publications returned 404; pulse.bot timed out.

## Steps
1. **Site mapping.** Mapped the novami.com sitemaps (127 press releases, 46 filings pages, 45 publication pages).
2. **Core download** (`fetch.py`, manifest `research/sources/nova/_manifest.csv`):
   - 20-F FY2020, FY2022, FY2023, FY2024, FY2025.
   - Results releases Q1 2020–Q4 2020, Q4 2021, Q1 2022–Q3 2026 (24 releases).
   - Investor Day 2022 transcript (company PDF) and Investor Day 2025 deck.
   - Notice on 2025-notes settlement method.
   - Product pages, dimensional brochure (2026), WMC update (2 Jul 2026), about 30 press releases.
   - 22 third-party transcripts.
   - Federal Register API record 2026-22793 and a law-firm alert.
3. **Parallel research.** Two background research agents ran with the rules file and tools:
   - **TH (Q2 literature).** 45 rows, TH_notes.md. Full texts: Samsung+Nova 2024; IBM+Nova 2019, 2021 ×2, 2022, 2023, 2026; imec+Nova 2021, 2025; Nova review 2026; IRDS Metrology 2022–2024. SPIE abstracts were read from volume pages.
   - **XR (Q3/Q4 X-ray, Onto–Rigaku, overlap, handoff paragraph).** 47 rows, XR_notes.md. Sources: Rigaku TDnet notices and results materials, Onto releases on q4cdn, Nova website/patents, GlobalFoundries/IBM papers, IRDS 2024, Globes interview.
   - I covered Module A, Q1, Q5, Q6 and Nova's own X-ray statements in calls and conferences (Q3).
4. **Extraction.**
   - `calc/parse_releases.py` parsed all saved releases into `calc/quarterly_items.csv`, keeping the page and line of each figure.
   - `calc/metrics.py` computed margins, FCF, DSO, inventory days, LTM, guidance record and cycle (`quarterly_metrics.csv`, `guidance_record.csv`, `cycle.csv`, `summary.txt`).
   - `calc/segments.py` gives implied end-market dollars; `calc/china.py` gives China dollars.
5. **Evidence.**
   - **Builders.** `calc/build_parts_A.py`, `build_parts_Q.py` and `build_parts_B.py` wrote `parts/*.csv` via `calc/evrow.py`. It refuses any row whose quote is not found in the cited saved document, fills the physical PDF page, and takes the URL from the manifest.
   - **Merge.** `merge_parts.py nova A1 A2 A3 A4 A5 A6 Q1 TH Q3 XR Q5 Q6 B` gives 373 rows in `evidence.csv`.
   - **Quote check.** `quote_check.py` found 324 quotes (320 exact, 4 layout-insensitive), 0 NOT FOUND, 0 flags. The 49 rows without quotes are [I] rows.
6. **Write-up.** Wrote dossier.md, handoff.md, gaps.md and review_packet.md.

## Problems found and fixed
- **Bot-challenge stubs.** Two 212-byte SPIE stubs were logged RETRIEVED by `fetch.py`, because HTTP 200 is treated as success. I set them to NOT RETRIEVED in the manifest with a note and deleted the files. Neither is cited.
- **Early merge.** The XR agent ran `merge_parts.py` early, which created a premature `evidence.csv`. It was overwritten by the final merge.
- **Duplicate copies.** The same IBM–Nova SPIE 2026 in-line XPS paper was saved twice by the two agents (`2026-02-22_ibm-nova_spie-13981-XPS-integrated-targets-Lee.pdf` and `2026-03-01_nova-ibm_SPIE-2026-paper-inline-XPS-fully-integra…pdf`). The XR agent also saved an extra IRDS 2023 chapter. Both copies were kept, since rows cite each.
- **Filename dates.**
  - The Samsung–Nova SPIE press release is dated 27 Feb 2024 but saved as `2024-02-26_…`; evidence rows use 27 Feb 2024.
  - The XR agent's file `2022-02-17_nova_press-release-portfolio-next-gen-logic.html` shows "February 17, 2021" in its dateline. It is not used for dates in the dossier.
- **Filename dates for undated pages.** HTML pages fetched with `--date auto` carry the retrieval date (2026-11-21) in the filename. The publication date read from each page is in the evidence `date` column.
- **Quote wording.** Three call quotes first failed validation because the two transcript providers word the same remark differently. They were re-cited to the provider whose wording matched.
- **Wrong citation.** The handoff extra cell first cited XR-046 for the packaging-overlap inference. It was corrected to a new [I] row, B-019.

## Self-check (rules: clean-context sub-agent, 15 most important [F]/[C] rows)
- Rows checked: A1-032, A1-036, A1-040, A1-067, A3-019, A4-001, A4-015, A4-020, A5-007, A5-012, Q1-023, XR-019, XR-033, TH-003, TH-012.
- Method: the checker was given only `evidence.csv` and `sources/nova/`. It counted pages by form feeds (they agree with `pdfinfo`) and rendered slides 10/71 and the TH-003 page to read printed labels.
- **Result: 15 MATCH / 0 MISMATCH / 0 CANNOT OPEN.**
- **Minor remarks, and what was done:**
  - **A1-067.** Values exist only as chart labels; the rendered slide confirms inner ring = Nova product revenue. Already noted in the row.
  - **A5-012.** The amounts paid ($51,826k; $1,407k) sit at the foot of p.157, the cap price on p.158. The row note now says so.
  - **XR-019.** The note said the 13 Apr board resolution was on p.1; it is on p.4. Note corrected in `parts/XR.csv`.
  - **XR-033.** The paper says "legacy Process-of-Record (POR)" acquisitions with VeraFlex. Reading this as the production socket is a direct inference; the wording is kept as "process of record".
  - **TH-003.** "5A" is printed with a plain A (= 5 Å). "Feb 2024" is not printed in the paper; the review packet now says "2024 (Proc. SPIE 12955)".
  - **TH-012 and XR-033.** Literal searches can fail because of the PDF text layer (line-break hyphen; "ﬁ" ligature). `quote_check.py` finds both layout-insensitively.
- After the fixes: re-merged 373 rows; `quote_check.py` found 324 quotes, 0 NOT FOUND.

## Push protection
The first push was rejected by GitHub secret scanning. It flagged a Mapbox access token embedded in a saved NIST web page (`2026-11-21_nist_pubrecord-Kline-2017-compact-source-CDSAXS.html`, not cited by any row). A scan of all saved files found similar third-party public web tokens (map/API keys in page code) in three more pages: two Google Patents pages and one SemiEngineering article. In all four saved copies and their text extractions I replaced the token strings with `[REDACTED-THIRD-PARTY-PUBLIC-TOKEN]` and noted this in `_manifest.csv`; the manifest's sha256 refers to the original download. No cited quote is affected, and `quote_check.py` still finds all 324 quotes. The local commit was amended before pushing, so no token entered the remote history.

## Final file set
`research/out/nova/`:
- `dossier.md`, `evidence.csv` (373 rows), `handoff.md`, `review_packet.md`, `gaps.md`, `run_log.md`
- `calc/`: scripts and outputs
- `parts/`: per-module CSVs and the TH and XR notes

`research/sources/nova/`: 223 retrieved documents, `_text/` extractions, `_manifest.csv` (231 attempts).

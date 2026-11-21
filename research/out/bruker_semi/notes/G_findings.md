# G: second attempt at Bruker filing and transcript gaps (semiconductor metrology only)

Bruker's fiscal year ends Dec 31, so FY2026 = Jan-Dec 2026. Research date: 2026-11-21.
Evidence rows: `research/out/bruker_semi/parts/G.csv` (G001-G082, 43 rows). `quote_check.py` result: 40 FOUND, 0 NOT FOUND, no flags. The 3 [I] rows have no quotes.
No group or segment financials are recorded. The group figures in G030/G031 are cited only for the semiconductor attribution.

## New sources saved (all listed in `_manifest.csv`)
| File | What | Mirror note |
|---|---|---|
| `2026-11-05_bruker-via-kabutan-mirror_10-Q-2026Q3.html` | Q3 FY2026 10-Q, acc. 0001193125-26-449731, signed 2026-11-05, full text with exhibits | us.kabutan.jp mirror of the SEC filing |
| `2026-08-05_bruker-via-stocktitan-mirror_10-Q-2026Q2-fulltext.html` | Q2 FY2026 10-Q full text including MD&A, signed 2026-08-05 | stocktitan.net mirror |
| `2026-05-07_bruker-via-stocktitan-mirror_10-Q-2026Q1-fulltext.html` | Q1 FY2026 10-Q full text, signed 2026-05-07 | stocktitan.net mirror |
| `2025-02-13_stockanalysis-transcript_earnings-call-transcript-2024Q4.html` | Q4 FY2024 call transcript (call held 2025-02-13) | third-party transcript, [S] |
| `2026-06-04_stockanalysis-transcript_conference-Jefferies-healthcare-2026.html` | CFO at Jefferies Global Healthcare Conference, 2026-06-04 | third-party transcript, [S] |

Handling notes:
- **Gzip.** stocktitan served both HTML files gzip-encoded even without an Accept-Encoding header. fetch.py saved the compressed bytes. I decompressed them in place and regenerated `_text/` with the same BeautifulSoup method fetch.py uses. Manifest bytes/sha256 were updated, with a note "G agent".
- **Q1 file date.** The Q1 file was fetched with `--date auto` (2026-11-21). I renamed it to the signature date, 2026-05-07, and updated the manifest row.
- **stocktitan AI summary.** stocktitan pages put an AI summary above the filing text. Only the filing text is quoted. G024's quote also appears in that summary, but the row cites the filing note (p.15).

## 1) Q3 FY2026 10-Q (Jul-Sep 2026): retrieved
**Segment structure**
- The reorganisation took effect July 1, 2026 [F] G001. BSI NANO had "no changes" to its reportable-segment structure [F] G002.
- BSI NANO's description still covers "X-ray metrology, defect-detection equipment for semiconductor process control" [F] G003.
- Note 1 lists divisions for BIOS and BMID only. NANO's divisions (e.g. Nano Surfaces and Metrology) are not named.

**Goodwill**
- **Q3 charge.** The $174.5M Q3 charge is the **BSB&CA reporting unit** (Bruker Spatial Biology + Cellular Analysis) within BSI NANO. It is the remaining goodwill of that unit [F] G004. This upgrades S064/S065 from [S] to [F].
  - Trigger: "changes in the competitive landscape and operating results below expectations" [F] G005.
  - 9M BSB&CA total: $211.0M [F] G006. Discount rates: 11.0%-14.0% [F] G008.
- **Reorganisation tests.** Interim tests were run on the reporting units "affected" by the reorganisation. All passed [F] G007.
- **Mimetas.** A new Mimetas unit (BIOS) was created with $42.5M of goodwill. Its fair value approximated carrying value. This is not semiconductor.
- **CST.** The $98.4M CST charge (Q2) is now presented within BSI BIOS (recast), not BioSpin.
- **Semiconductor link.** [I] G080: no semiconductor unit was impaired. A semiconductor-metrology unit was probably not among the "affected" units, because NANO's structure did not change. Confidence Medium.

**MD&A**
- MD&A semiconductor sentences (all of them):
  - BSI BIOS revenue was helped by "industrial and semiconductor markets" [F] G010. This is BIOS (Daltonics/Optics/Tofwerk), not metrology.
  - 9M BEST was partly offset by lower semiconductor revenue [F] G011. This relates to EUV/XUV, not metrology.
- The Q3 revenue increase is attributed to BIOS and BEST only. No BSI NANO or semiconductor-metrology driver is given for Q3 [F] G009.
- **Restructuring.** The BSI NANO Restructuring Plan includes a "merger of divisions within the segment" and is to be completed by end-2026 [F] G012.
  - The only NANO division merger named in any 2026 filing is BCA into BSB, on April 1, 2026 [F] G013.
- NOT DISCLOSED (read: Q3 10-Q Note 1 p.9; Note 5 pp.14-15; Note 10 p.20; MD&A pp.~30-45):
  - names of the reporting units affected by the reorganisation
  - headroom of any unit
  - whether a semiconductor or Nano Surfaces and Metrology unit was tested
  - the NANO divisions being merged
  - semi revenue, bookings or backlog
  - X-ray, AFM, HBM or advanced packaging in MD&A
- SECOND ATTEMPT RESULT: added something (filing retrieved; unit and test facts now [F]; the remaining items above are NOT DISCLOSED in the filing).

## 2) Q1 FY2026 10-Q (Jan-Mar 2026): retrieved
- BSI NANO Q1 revenue declined. The decline was partly offset by "higher revenue from the semiconductor market" [F] G020.
- At group level, the non-GAAP CER decline was partly offset by semiconductor revenue [F] G022.
- The BSI NANO restructuring plan began in Q1 2026. It includes consolidation and merger of divisions [F] G023. The divisions are not named.
- The goodwill note says only that the BSB/BCA merger triggered an interim test, to be recorded in Q2 [F] G024. No semi unit is mentioned.
- The segment description matches Q3 [F] G021.
- NOT DISCLOSED (read: Q1 10-Q MD&A pp.~30-45, restructuring note p.21, goodwill note p.15): which divisions merge; semi revenue, bookings or backlog; X-ray, AFM, HBM or advanced packaging.
- SECOND ATTEMPT RESULT: added something.

## 3) Q2 FY2026 10-Q MD&A (Apr-Jun 2026): retrieved (full text)
- Q2 organic growth (+2.8%, group) was driven partly by "semiconductor markets" [F] G030.
- H1 (-0.8%, group) was partly offset by higher semiconductor revenue [F] G031.
- BSI NANO revenue "remained consistent" YoY in both Q2 and H1 [F] G032, G033. Compare the Q2 deck: semi orders >30% and revenue >15% organic in H1 (S037). The 10-Q gives no semi-specific figure.
- NOT DISCLOSED (read: Q2 10-Q MD&A pp.~30-45): X-ray, AFM, HBM, advanced packaging, semi bookings or backlog.
- [I] G082: across the Q1-Q3 FY2026 10-Qs, the MD&A uses "semiconductor" only as a market-demand attribution. Dollar semi figures appear only in calls and decks.
- SECOND ATTEMPT RESULT: added something.

## 4) 10-K Competition text (FY2023, FY2024, FY2025): read from saved files
- The FY2025 10-K (PDF p.17) defines BSI NANO competition by technology class: X-ray, OES, AFM/SOM, optical fluorescence and genomics [F] G040.
- Named competitors: Rigaku, Oxford Instruments, Agilent, Thermo Fisher Scientific, Ametek Spectro/Edax, PANalytical, Park Systems, Olympus, Nikon, Zeiss, 10x Genomics, Thorlabs, Bio-Techne, Danaher's Leica [F] G041.
- The FY2024 (mirror, PDF p.30) and FY2023 (PDF p.13) lists are the same, minus 10x Genomics, Thorlabs and Bio-Techne [F] G042, G043.
- No separate semiconductor-metrology competitor paragraph exists. KLA, Onto Innovation, Nova, Camtek, Nearfield and Infinitesima are not named anywhere in the three 10-Ks (full-text search). Of the names given, only Rigaku (X-ray) and Park Systems (AFM) are semi-metrology-relevant [I] G081.
- NOT DISCLOSED (read: 10-K FY2025 Item 1 Competition pp.15-17; FY2024 Item 1 p.30; FY2023 Item 1 p.13): semiconductor-specific competitors.
- SECOND ATTEMPT RESULT: added something.

## 5) Transcript gaps
**Q4 FY2024 call (2025-02-13), stockanalysis.com transcript [S]**
- CEO: "north of $125 million of AI and HPC-related semiconductor nanotool metrology revenues", adding that not all semi metrology is AI-related (G050).
- Total semiconductor metrology is "north of $250 million", "maybe half" of it HPC/AI (G051).
- China semi export restrictions have applied for 2-3 years to very high-performance equipment (G052).
- He expected no acceleration and no deceleration in 2025 (G053). FY2025 semi revenue was in fact flat (S025).
- SECOND ATTEMPT RESULT: added something.

**Jefferies Global Healthcare Conference (2026-06-04, CFO Gerald Herman), stockanalysis.com transcript [S]**
- Semi metrology is "in the range of $300 million". Two-thirds is production QA/QC tied to wafer activity, about $200M (G060, G061).
- The other ~$100M is about half R&D and half mask repair (~$50M) (G062, G063).
- $10-15M of the $40M Q4-25 pushout was recaptured in Q1-26, with similar amounts expected in Q2 and Q3 (G064).
- Three technologies: X-ray, automated AFM and WLI (G065).
- Capacity to at least double by end-2026. Q1/Q2 orders ship end-2026 or into 2027 (G066).
- 2025 orders were lumpy (G067). New fabs copy tools of record, e.g. from Taiwan to Japan (G068). China semi sales are "quite robust" (G069).
- SECOND ATTEMPT RESULT: added something.

## NOT RETRIEVED (this attempt)
- **sec.gov originals of all three 10-Qs.** Not attempted: sec.gov refuses scripts, and SEC_UA is not set. Mirrors were used instead.
- **Cloudfront/q4cdn copies of the Q1 and Q3 FY2026 10-Qs.** Tried: web search for "d18rn0p25nwr6d.cloudfront.net/CIK-0001109354" and for "s22.q4cdn.com 617463959 doc_financials 2026 q1". No hits. Not needed after the mirrors were found.
- **Other Q1 10-Q hosts.** equibles.com Q1 10-Q copy: HTTP 403, not worked around. us.kabutan.jp BRKR disclosure list (/stocks/BRKR/disclosures): 404. The Q1 accession number was not found.
- **Other Q4 FY2024 transcript hosts:**
  - roic.ai (BRKR and BRKRP pages): 403.
  - www.investing.com: 403.
  - itiger.com news pages: 404.
  - insidermonkey: sign-in stub only, not saved.
  - finance.yahoo.com: has only a GuruFocus highlights summary without the $125M figure, not saved.
  - fool.com: no Q4-24 transcript found by search.
- **Firecrawl search.** Out of credits ("Insufficient credits"); stopped using it.
- **Seeking Alpha transcripts (Q4-24, Jefferies 2026).** Not attempted (expected to be blocked). The stockanalysis.com copies were used instead.

## Lead noted (not fetched; outside this task)
- stocktitan.net also lists a full-text 10-Q for Q3 FY2025 (`/sec-filings/BRKR/10-q-bruker-corp-quarterly-earnings-report-45f510d5eb3f.html`). The S notes list that filing as NOT RETRIEVED.
- stockanalysis.com lists Bruker transcripts from Q1-2015 onward, including Q4-23, Q1-Q3 2024 and Q1-Q2 2025, which the S notes list as NOT RETRIEVED. It also lists Jefferies 2024/2025 and other conferences.

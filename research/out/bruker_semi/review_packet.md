# Review packet: Bruker semiconductor metrology (2026-11-21)

For an independent reviewer who has web search and a URL reader. Bruker's fiscal year ends Dec 31.

Tags:
- [F] fact in a primary document
- [C] company claim that cannot be tested
- [S] secondary source
- [I] inference

## A. The 15 most important claims

| # | Claim | Tag | Value | Period | Public URL | Page |
|---|---|---|---|---|---|---|
| 1 | Semi metrology orders and revenue growth, H1 | [F] | Orders >30%, revenue >15% (organic) | H1 FY2026 (Jan-Jun 2026) | https://s22.q4cdn.com/617463959/files/doc_financials/2026/q2/2Q26-Earnings-Presentation-FINAL.pdf | p8 |
| 2 | Semi metrology EBIT margin; no one-offs named | [F] | ~30% | H1 FY2026 (Jan-Jun 2026) | same as #1 | p8 |
| 3 | Semi metrology size and margin; no one-offs named, EBIT basis undefined | [F] | >$300M revenue, >25% EBIT | TTM to Q3 FY2025 (Oct 2024-Sep 2025) | https://s22.q4cdn.com/617463959/files/doc_events/2026/Jan/12/BRKR-JPM26-Presentation-Final.pdf | p14 |
| 4 | Semi revenue flat in FY2025 | [F] | flat | FY2025 (Jan-Dec 2025) | https://s22.q4cdn.com/617463959/files/doc_earnings/2025/q4/presentation/BRKR-4Q25-Earnings-Presentation.pdf | p7 |
| 5 | Semi-Metrology share of BSI revenue, not of total Bruker | [F] | 9% | FY2025 (Jan-Dec 2025) | same as #4 | p9 (pie chart) |
| 6 | Semi bookings year to date; appears in no Bruker document | [S] | >30% | 9M FY2026 (Jan-Sep 2026) | https://www.fool.com/earnings/call-transcripts/2026/11/04/bruker-brkr-q3-2026-earnings-call-transcript/ | Prepared remarks; Q&A (Laukien) |
| 7 | BSI NANO segment unchanged by the 1 Jul 2026 reorganisation; covers X-ray metrology for semiconductor process control | [F] | no change | Q3 FY2026 (Jul-Sep 2026) | 10-Q, accession 0001193125-26-449731 (sec.gov); mirror https://us.kabutan.jp/disclosures/0001193125-26-449731 | Note 1, p9 |
| 8 | Q3 goodwill impairment was the BSB&CA life-science unit, not semiconductor | [F] | $174.5M | Q3 FY2026 (Jul-Sep 2026) | same as #7 | MD&A p37; Note 5 p14 |
| 9 | Rigaku share of semiconductor X-ray metrology (citing Yole Q4 2025 edition) | [C] | 38% | CY2024 | https://disclosure2dl.edinet-fsa.go.jp/searchdocument/pdf/S100XTB1.pdf | p20, p25 |
| 10 | Rigaku share, front-end X-ray metrology (citing Yole Q2 2024 edition) | [C] | 26.9% / 29.5% | CY2022 / CY2023 | https://disclosure2dl.edinet-fsa.go.jp/searchdocument/pdf/S100UEKD.pdf | p34 (note 6 on p35) |
| 11 | Samsung Electronics (Device Solutions Division), Onto and Rigaku co-present X-ray CD for deep V-NAND | [F] | n/a | dated 2026-03-18 | https://cdn.fs.pathlms.com/E6x7snw6Si6F8pFwsPJw?dl=true | p1, p16 |
| 12 | Onto–Rigaku CD-SAXS + Ai Diffract offering "selected by two key customers" | [C] | 2 customers | as of 2026-04-20 | https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Announces-Strategic-Partnership-With-Leading-X-Ray-Provider-Rigaku-To-Advance-Next-Generation-Process-Control-Solutions-2026.pdf | p1 |
| 13 | Kioxia and Kioxia Iwate to put Rigaku XTRAIA MF-3400 into 3D NAND mass production | [C] | n/a | release 2025-12-04 | https://rigaku.com/about/news-and-press-releases/rigaku-launches-xtraia-mf-3400 | "Track record and prospects" |
| 14 | Fraunhofer IZM in-line AFM (pre-bond roughness and dishing, hybrid/direct bonding) awarded to Bruker France | [F] | Bruker France S.A.S. | contract 2025-08-06 | https://ted.europa.eu/en/notice/-/detail/518266-2025 | award fields |
| 15 | IBM/Nova inline Cu-recess scatterometry trained on AFM reference data (15 wafers x 5 dies) | [F] | blind-test R² ~0.8 | SPIE AL 2026 (Feb 2026) | https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf | p4 (training set); p7 (R² ~0.8) |

## B. The 5 inferences the conclusions lean on most

1. **None of the three named 2026 goodwill charges is in a semiconductor unit; whether a semi unit was among the units tested in Q3 is NOT DISCLOSED (read: 10-Q Q3 FY2026 MD&A goodwill section; Note 5)** (G080; confidence Medium).
   - Inputs: #7, #8; Q2 FY2026 10-Q Note 5 (BSB $36.5M, CST $98.4M; S060, S061); G007 (the reorganisation-affected units passed, unnamed).
   - Reason: all three 2026 charges are in named life-science units, but the units that passed the Q3 test are not named.
2. **Bruker lists no CD-SAXS, wafer-fab TXRF or packaging X-ray imaging tool in 2026** (V006/R072; confidence Medium).
   - Inputs: bruker.com X-ray metrology, XRDI and hub pages and brochure B5000 Rev A3 (retrieved 2026-11-21); the 2022 FCMN "XCD"/"XRI" abstracts (R051, R052).
   - Reason: the finding rests only on what the listed pages show.
3. **No named chipmaker uses Bruker semi tools in production after 2015** (C036, H081; confidence Medium).
   - Inputs: Bruker releases from 2016, 2017 and 2025 (unnamed customers); papers; EU TED procurement records; supplier-award lists from Intel (2011-2015, 2020, 2022) and Micron (2025-2026).
   - Reason: the search was broad, but customer names are rarely published.
4. **AFM is the calibration reference for Cu recess, but its role as the HVM monitor is contested** (H080; confidence Medium).
   - Inputs: #15; imec in-line SEM vs AFM (Micromachines 2026 review); Onto case study ("low throughput and contamination risk"); Nova Prism blog; Adeia PSI blog.
   - Reason: every optical or SEM method found is checked against AFM, while vendors pitch non-AFM tools for inline use.
5. **The "Bruker logic / Rigaku memory" split is not supported** (R069; confidence Medium).
   - Inputs: Rigaku segment mix, logic/foundry 35% vs memory 10% in FY2024, then 21% vs 26% in FY2025 (Rigaku MTP Feb 2025 p11 for FY2024; Rigaku annual securities report FY2025, EDINET S100XTB1, p25 for FY2025); #11, #13; Bruker Q2/Q3-26 decks ("memory and advanced packaging" orders).
   - Reason: no source gives share by fab type, and the Rigaku mix flipped within a year.

Calculations: `calc/semi_mix_calc.py` (≈50% AI/HPC; ≈67% production QA/QC; 25-38% pushout recapture in Q1-26, 75-112% expected by Q3 if read per quarter, 50-75% if Q2+Q3 combined), `calc/M_calc.py` and `calc/R_calc.py` (implied Rigaku and Company A revenue).

## C. Three questions I could not settle

1. **Does any Bruker document state >30% semi bookings growth for 9M FY2026 (Jan-Sep 2026), and what are the dollar bookings?**
   - Only the call says it, read in a third-party transcript (#6).
   - Q3-26 deck: https://s22.q4cdn.com/617463959/files/doc_financials/2026/q3/3Q26-Earnings-Presentation-FINAL.pdf (p7). The deck and release give no figure.
2. **Who is "Company A" (24% of semiconductor X-ray metrology, CY2023, Rigaku MTP Feb 2025 p11), and what is Bruker's X-ray metrology share?**
   - Nova also sells X-ray metrology, so Company A need not be Bruker.
   - Yole pages returned 403 to scripts.
3. **Which chipmaker placed the 27-system optical metrology order for 2025, and which HBM makers use Bruker automated AFM "in the production of High Bandwidth Memory" (10-K FY2025)?**
   - Neither is named anywhere read, and no tool count per line is published.

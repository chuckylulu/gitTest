# C findings: named chipmaker / fab users of Bruker and Rigaku semiconductor metrology (second attempt)

Scope: Bruker semiconductor metrology only (FY = calendar year); Rigaku as comparison (FY = calendar year). No group or segment financials.
Modalities used (different from the first pass): (a) technical papers and conference abstract books with chipmaker or research-fab authors; (b) chipmaker supplier-award lists; (c) public procurement and grant records.
Evidence rows: `research/out/bruker_semi/parts/C.csv` (C001-C037). quote_check: 35 FOUND, 0 NOT FOUND (2 [I] rows have no quote).
CSV builder: `research/out/bruker_semi/calc/C_build_csv.py`.

## 1. Hits: named users, Bruker

| Who | Vendor / tool | Measurement | Year | Source | Tag | Row |
|---|---|---|---|---|---|---|
| **TSMC** | Jordan Valley JVX6200 (XRR); Jordan Valley became part of Bruker in Nov 2015 | Thickness of thin-film Cu layers. TSMC is quoted saying XRR beat opto-acoustic in its evaluation | 2009 | Jordan Valley release, Semiconductor Online reprint | [S] | C001, C002 |
| **IBM Research, Albany** (R&D fab) | Bruker JVX7300LSI, in-line HRXRD | Nanosheet Si/SiGe stack thickness and Ge content: (004) scans at 5 sites per wafer, plus a (113) RSM. Used as the reference for in-line Raman | 2021 | Schmidt et al., Proc. SPIE 11611 (IBM first author; copy hosted by Nova) | [F] | C003, C004 |
| **imec** (proxy) | Bruker Sirius-XRD inline (XRR+HRXRD); Bruker (JV)Sensus-600F XRDI | CFET Si/SiGe multilayers and defect maps on imec-grown wafers. The measurements were made by the Bruker authors; the abstract does not say the tool is at imec | 2026 | FCMN 2026 abstract #052 (Bruker + imec authors) | [F] | C008, C009 |
| **IBM Research** (T.J. Watson) | Bruker Nano AFM staff as co-authors; tool model NOT DISCLOSED | Resist-shrink CD metrology | 2022 | SPIE 12053-24, as cited in the FCMN 2022 abstract book | [F] (citation only) | C010 |
| **Intel** | Bruker co-author; AFM model NOT DISCLOSED | High-aspect-ratio AFM tips on 40 nm pitch EUV resist | 2026 | SemiEngineering summary of Meas. Sci. Technol. paper (Purdue/Intel/Bruker) | [S] | C011 |
| **Fraunhofer IPMS** (research fab, Dresden) | Bruker AXS SE: 300 mm lab XRD (GIXRD, XRR, HRXRD, texture, stress) | Full wafers and fragments | Contract 2025-12-05 | TED award notice 813831-2025 | [F] | C017, C018 |
| **Fraunhofer IZM** (heterogeneous-integration pilot line) | Bruker France S.A.S.: in-line AFM up to 300 mm | Pre-bond roughness and dishing for hybrid/direct bonding; RDL CMP; TSV sidewalls | Contract 2025-08-06 | TED award notice 518266-2025 | [F] | C019, C020 |
| Fraunhofer (InP R&D) | Bruker France SAS AFM | InP structures and photoresist | 2024 | TED 224335-2024 | [F] | C021 |
| Sematech at CNSE Albany | Bruker AXS D8 Fabline + D8 Discover | Lab-to-fab XRD metrology | 2009 | Quality Magazine reprint | [S] | C025 |
| NIST | Bruker InSight 3D AFM (repair order) | not stated | 2020 | USAspending award 1333ND20PNB680155 | [F] | C026 |

Jordan Valley releases where the customer is not named [C]:
- $10M repeat order for JVX6200i from a "tier one" maker, 2010 (C012).
- JVX7300HR orders from "multiple foundries in Asia", 2015 (C013).
- JVX7300LMI order for 14/10 nm, 2013 (C014).

## 2. Hits: named users, Rigaku

| Who | Tool | Measurement | Year | Source | Tag | Row |
|---|---|---|---|---|---|---|
| **KIOXIA and KIOXIA Iwate** | XTRAIA MF-3400 (XRF + XRR + XRD) | Film thickness and composition, including Mo, in 3D NAND mass-production lines | Dec 2025 | Rigaku news release | [C] (vendor claim naming the customer) | C005 |
| Rigaku forecast | MF-3400 plus predecessor | Net sales > JPY 6bn in FY2026 (Jan-Dec 2026) | 2025-12-04 | same release | [C] | C006 |
| Kioxia (own R&D page) | T-SAXS, studied by simulation only; vendor NOT DISCLOSED | Metrology of 3D NAND high-aspect-ratio holes | 2021-22 | Kioxia R&D topics-29 | [F] | C007 |
| **Fraunhofer IPMS** | Rigaku Europe SE: inline 300 mm full-wafer cleanroom XRR/XRD/HRXRD/RSM with automatic load port | 300 mm and 200 mm wafers | Contract 2025-10-07 | TED 751635-2025 | [F] | C015, C016 |
| Fraunhofer (III-V/diamond; GaN/SiGe/SiC wafers) | Rigaku Europe SE HRXRD+XRR; XRD | Epi layers | 2025 | TED 224891-2025, 318497-2025 | [F] | C022, C023 |
| Fraunhofer IISB | Rigaku XRTmicron installed under a partnership (demo centre) | X-ray topography of substrates | 2019 | Fraunhofer IISB release | [F] | C024 |

**Already in R.csv, not repeated here:** the Samsung/Onto/Rigaku XCD deck (R048) and "adopted by major memory player" (R038). The Kioxia row (C005) is the first source that names a Rigaku production customer.

**[I] (Medium), C036.** Across all three modalities, only three named links turned up:
- TSMC and the Jordan Valley JVX6200: 2009, before Bruker, vendor release.
- Kioxia and the Rigaku MF-3400: 2025, vendor release.
- IBM Albany's R&D use of the Bruker JVX7300LSI: 2021 paper.

I found no named chipmaker production use of Bruker AFM, AFP or WLI. I also found no named chipmaker production use of Bruker X-ray tools after 2015.

**[I] (Medium), C037.** Fraunhofer split its 2025 300 mm X-ray purchases:
- The inline cleanroom tool went to Rigaku.
- The lab XRD went to Bruker AXS.
- The in-line AFM for hybrid bonding went to Bruker.

## 3. Supplier awards (checked, none for Bruker or Rigaku)
- **Intel EPIC 2022** (C027): neither listed.
- **Intel SCQI 2020** (C028): KLA and Onto Innovation received Supplier Achievement Awards for Technology; Bruker and Rigaku are absent.
- **Intel SCQI top-tier lists, 2011-2015** (C029-C033): absent.
- **TSMC Excellent Performance Award 2021** (C034, reprint): absent.
- **Micron Supplier Awards 2025 and 2026** (C035): absent.

## NOT DISCLOSED
- **Customer names in the Jordan Valley releases of 2010, 2013 and 2015.** Read: each release body (C012-C014).
- **Tool model and contract value in the Fraunhofer TED notices 751635-2025, 813831-2025 and 518266-2025.** Read: all fields returned by the TED API, i.e. lot description, tenderer, values. The tender-value is -1 or 0.01.
- **Tool vendor for Kioxia's T-SAXS work.** Read: Kioxia topics-29 page, whole text.
- **AFM model in the IBM/AMAT/Bruker 2022 citation and the Purdue/Intel/Bruker 2026 summary.** Read: FCMN 2022 abstract book p103; SemiEngineering summary.
- **Instrument vendor in Micron Corporate Labs' FCMN 2026 abstract #051** (XPS/HAXPES). Read: abstract pp244-246.
- **Micron 2023 Supplier Award winners.** Read: Micron blog 2023-12; the list is image-only in the saved text.

## NOT RETRIEVED
- **Samsung's adoption of the JVX6200** (lead: thomasnet "Tier-1 Fab in Asia ... adoption of JVX 6200 by Samsung and TSMC"). Tried: news.thomasnet.com (403). No other copy was found by web search.
- **CEA-Leti use of the JVX6200** (Wyon, EPJ AP 2010; the snippet says the JVX6200 was used on 300 mm wafers). Tried: epjap.org PDF (403). HAL was searched and holds no copy.
- **imec paper using the Bruker JVX7300M** (Loo et al., ECS JSS 10, 014001, 2021; lead from a ResearchGate snippet). Tried: iopscience PDF (403). imec-publications.be was not retried (it reset the connection in the H pass).
- **GlobalFoundries equipment engineer listing "Bruker JVX7300"** (LinkedIn snippet). Not attempted: login wall, personal profile.
- **Original Meas. Sci. Technol. paper, Purdue/Intel/Bruker.** Tried: no open copy found; IOP refuses scripts.
- **TSMC supplier-award releases 2018, 2021, 2022, 2023, 2024, 2026 and the 2026 PDF.** Tried: pr.tsmc.com, 403 for every one, not worked around. I used the 2021 reprint. Web search summaries of the 2022-2026 lists name no Bruker or Rigaku (lead only).
- **Intel EPIC 2023-2026 lists.** Tried: newsroom.intel.com and intel.com (403). The intc.com copies were found only for 2022 and earlier.
- **Full text of the legacy (pre-eForms) TED notices.** These are 447849-2016 (CEA Grenoble maintenance, which matches "Jordan Valley"), 493728-2017, 509978-2020, 630625-2021, 156334-2023, 399906-2023 (all Fraunhofer) and 141138-2021 (IHP).
  - Tried: the TED API returns no description or winner fields for these notices; ted.europa.eu pages answer with a WAF challenge (202), not worked around.
  - The metadata-only JSON files are saved, but no rows were written from them.
- **op.europa.eu procurement page for PR878911.** Tried: 403. I used the TED API record instead.
- **NIST-hosted Jordan Valley decks** (Wormington HRXRD; Ryan et al. JV+IMEC Ge MOSFET) and the CEA-Leti 3DAM HRXRD deck. Tried: nist.gov/document/wormingtonpdf (404), nist.gov/document/38ryanpdf (404), leti-cea.com PDF (404).
- **NIST FCMN 2024 presentations page.** Tried: 404. I used the pathlms abstract books instead.
- **Firecrawl search.** Worked for 3 queries, then reported that credits had run out. I stopped using it.

## Searched, nothing found
- **arXiv / Europe PMC full text** ("JVX7300", "JVX7300LSI", "JVX6200", "Bruker JV", "InSight 300", "InSight AFP", "XTRAIA", "TXRF 3760", "TXRF 310Fab", "WaferX", "Sirius-XRD", "JVSensus", "InSight CAP", "Bruker InSight"). The only hits had no chipmaker authors: IMECAS/GIICS China, KTH, NIST/nanotools, A*STAR (already H010).
- **OSTI API** ("Jordan Valley" X-ray, JVX7300, JVX6200, XTRAIA, Rigaku TXRF wafer): nothing relevant.
- **J-STAGE API** ("Jordan Valley", JVX, XTRAIA, "TXRF Kioxia", "Rigaku Kioxia", "Rigaku Samsung", "Bruker InSight"): nothing relevant. The 1995 Toshiba TXRF items were not pursued.
- **Web searches with no named hit:**
  - Samsung/SK hynix/Micron/GlobalFoundries/Intel papers naming Bruker or Rigaku tools.
  - XRDI wafer-breakage papers with chipmaker authors.
  - Korean press on Rigaku or Bruker supplying Samsung/SK hynix.
- **Procurement in Asia and the US:**
  - Japanese AIST tenders for Rigaku 300 mm tools.
  - Korean NNFC/KANC tenders.
  - Taiwan TSRI tenders.
  - NY CREATES / NSTC / Natcast purchases.
  - USAspending ("Bruker wafer", "Rigaku wafer", "Bruker JVX", "X-ray metrology wafer").
- **TED** ("Rigaku" AND "TXRF": only an AGH Krakow detector purchase; "Bruker"/"Rigaku" with imec: 0; with CEA/Leti and wafer: 0).

## SECOND ATTEMPT RESULT per gap
- **Named chipmaker using Bruker X-ray tools.** SECOND ATTEMPT RESULT: added something.
  - TSMC used the JVX6200 in 2009 [S]; this predates Bruker's ownership of Jordan Valley.
  - IBM Research Albany used the JVX7300LSI in a 2021 paper [F].
  - Nothing found for 2016-2026 production use at a named chipmaker.
- **Named chipmaker using Bruker AFM, AFP or WLI.** SECOND ATTEMPT RESULT: added nothing on production use.
  - Only Intel and IBM papers with Bruker co-authors turned up, with no tool model given [S]/[F].
  - Research-fab and NIST purchases: Fraunhofer IZM in-line AFM [F]; NIST InSight 3D AFM [F].
- **Named chipmaker using Rigaku tools.** SECOND ATTEMPT RESULT: added something. Kioxia and Kioxia Iwate are named for the MF-3400 in mass production [C], per Rigaku's release.
- **Chipmaker supplier awards to Bruker or Rigaku (Intel, TSMC, Micron, Samsung, SK hynix).** SECOND ATTEMPT RESULT: added nothing. Award lists were read and neither company appears. The Samsung and SK hynix award lists were not located.
- **Public procurement naming Bruker or Rigaku fab tools.** SECOND ATTEMPT RESULT: added something. The finds are the Fraunhofer IPMS/IZM awards of 2025 [F] and the 2009 Sematech Albany order [S].
- **Asian public tenders (Japan, Korea, Taiwan) and CHIPS/NSTC/Natcast records.** SECOND ATTEMPT RESULT: added nothing.

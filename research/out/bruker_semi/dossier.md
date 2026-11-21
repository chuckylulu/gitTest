# Bruker Corporation (BRKR, Nasdaq, USA): semiconductor metrology business

Research date: 2026-11-21. **Fiscal year ends December 31**, so fiscal quarters match calendar quarters (Q3 FY2026 = Jul-Sep 2026).

Scope:
- Semiconductor metrology only.
- Module A skipped, as instructed. Group and segment financials are left out.

How to read this file:
- Evidence ids (S, P, R, H, G, C, M, Q, V) are rows in `evidence.csv`. The cited files are in `research/sources/bruker_semi/`.
- Tags:
  - [F] = fact read in a saved primary document.
  - [C] = company claim that cannot be tested.
  - [S] = secondary source, including third-party call transcripts and reprints.
  - [I] = inference. Its inputs and confidence are in its evidence row; arithmetic is in `calc/`.
- Margin rule: for every EBIT margin quoted below, Bruker names no one-off items and does not define the EBIT basis. A figure excluding one-offs is NOT DISCLOSED (read: JPM 2026 deck p14; Q2-26 deck p8).

## Premise check (prompt, prior/ and the earlier brief)

1. **prior/ is empty** (only `.gitkeep`). The "Bruker Financial and Segment Performance" chat is not in the repo, so overlap could not be checked. Group and segment financials are left out anyway.
2. **On this branch, research/CLAUDE.md was a placeholder.** The rules applied here come from branch `ccr-2b9561fc-mqqdg4` (run_log.md).
3. **"July 2026 reorganisation": the filing gives the date as July 1, 2026** [F] G001.
   - New segments: BSI Biosystems (BIOS), BSI Microbiology and Infection Diagnostics (BMID), BSI NANO and BEST. Old segments: BSI BioSpin, BSI CALID, BSI NANO and BEST.
   - The filing states that BSI NANO was not changed, and it still covers "X-ray metrology, defect-detection equipment for semiconductor process control" [F] G002, G003. So semiconductor metrology stayed in BSI NANO.
   - A web-search summary that placed it in BEST does not match the filing.
4. **"2026 goodwill impairments": the filings name three charges, none in a semiconductor unit.**
   - Q2 FY2026, $134.9M total: BSB (spatial biology, BSI NANO) $36.5M and CST/Chemspeed (BSI BioSpin, pre-recast label) $98.4M [F] S059-S061.
   - Q3 FY2026: BSB&CA (spatial biology + cellular analysis, BSI NANO) $174.5M [F] G004.
   - 9M FY2026 total: $309.4M [F] S063.
5. **"Onto-Rigaku alliance, April 2026": announced 2026-04-20.**
   - Onto bought 27% of Rigaku from Carlyle's Atom Investment L.P.; no new shares were issued [F] R001, R002.
   - About $710M at signing; JPY 113.08bn (about $720M) at closing on 2026-08-10 [F] R007.
   - The CD-SAXS + Ai Diffract integration predates the stake [F] R010.
6. **The "9% semi metrology" figure is a share of BSI revenue, not of total Bruker** [F] S016, S026.
7. **Analysts' numbers, not Bruker's:**
   - "$40M Q4-25 semi pushout" [S] S033, G064.
   - "~$300M by year-end, mid-to-high single digit growth, 30% EBIT" [S] V003.
   - Bruker did not state either figure itself.
8. **Product names in the earlier brief:**
   - JVX7300LSI is now sold as "7300LSI" [F] P006.
   - Not listed among current semiconductor products on the pages read (2026-11-21) [F] P notes, R053, R055: D8 FABLINE, Sirius-XRI, JV-QCTT, InSight CAP, ContourX/GT, NPFLEX.
   - QC-TT is listed as an XRDI defect-inspection tool, not a metrology tool [F] R055.
   - S4 T-STAR is a benchtop TXRF for liquids and does not appear on the semiconductor pages [F] P notes.
   - Jordan Valley Semiconductors closed in Nov 2015, not 2019 [S] P026. The 2019 deal was RAVE (mask repair) [F] P029.
9. **Competitor products in Q4:**
   - Camtek's hybrid-bonding tool is Hawk, not Eagle G5 [C] H062.
   - Nova's Cu-recess material names Prism and VTS-ML, not Elipson [C] H050.
   - Onto's Cu-recess method is OCD; 3Di is bump metrology [C] H053.
   - No saved KLA document ties Candela or Zeta to Cu recess (H063).
   - Park's 2021 NX-Hybrid WLI launch release (AFM + white-light interferometer) does not mention hybrid bonding [F] H037.
10. **Ledger claims:**
    - Claim (b), "Bruker leads logic, Rigaku leads memory": no identifiable author or source in anything read (R notes §3).
    - Claim (a): on the Q3-26 call, the >30% year-to-date figure is stated twice, but only in a third-party transcript [S] S045, V001.

## Q1. Product map: Bruker tools sold into fabs and packaging lines

Sources:
- bruker.com semiconductor hub and product pages (retrieved 2026-11-21).
- Brochure B5000 Rev A3 (2026).
- 10-K FY2025.
- Bruker releases.

Two items are missing throughout:
- **Launch dates** are NOT DISCLOSED on any current product page (read: every page in the P notes). The dates below come from dated releases or papers.
- **Named fab customers** are NOT DISCLOSED in any Bruker document read.

"Production" = inline or high-volume manufacturing (fab automation, SECS/GEM, 300 mm). "Lab" = R&D or failure analysis.

### (a) X-ray (product lines from Jordan Valley, acquired 2015, and Bede)

| Class | Product | Application | Production vs lab | Launch / first dated | Customers named or described | Ids |
|---|---|---|---|---|---|---|
| Diffraction + reflectometry | **Sirius-XRD** | XRD + XRR for gate-all-around and advanced memory | Inline | NOT DISCLOSED. In the 2026 brochure; no product page. FCMN 2026 data on imec CFET wafers | imec-grown wafers measured by Bruker authors [F] | P005, P018, C008 |
| HRXRD / XRR / GIXRD | **7300LSI** (formerly JVX7300LSI) | Epi strain, thickness and composition; high-k; nanosheet Si/SiGe | In-fab R&D and inline; 300/200/150 mm | Sold by 2016 | 2016: "multiple leading logic and foundry manufacturers" [S] P009. **IBM Research Albany**: inline JVX7300LSI, SPIE 2021 [F] C003 | P006-P009, C003 |
| HRXRD / XRR (lab) | **Delta-X**; D8 DISCOVER / D8 ADVANCE Plus | Thin-film R&D and QC; 300 mm mapping | Lab | NOT DISCLOSED | Fraunhofer IPMS: 300 mm lab XRD contract awarded to Bruker AXS SE (contract 2025-12-05) [F] | P010, P058, C018 |
| HRXRD / XRR (compound semi) | **QCVelox-HR, QCVelox-E, QC5-R** | Epilayer QC for GaN/AlGaN and III-V | Production QC | NOT DISCLOSED | "leading epi manufacturers" [C] | P011-P013 |
| Fluorescence (µXRF) + XRR | **Sirius-RF** (listed as 6300-RF / 6300-XRR in the brochure table) | Film composition and thickness for DRAM, PCRAM, 3D-NAND, MRAM, logic and packaging | Inline, 4th generation | NOT DISCLOSED | none | P016, P017 |
| Fluorescence (µXRF), packaging | **Sirius-FW** (called "Sirius-FW G2" in an FCMN 2026 abstract) | Single-bump %Ag in SnAg; UBM, RDL and pillar thickness; bump height | Inline | NOT DISCLOSED | "TOR on major packaging fabs" [C] | P014, P015, Q003 |
| TXRF | **unnamed** | Metal contamination on Si and SiC | NOT DISCLOSED | NOT DISCLOSED | none. No wafer-fab TXRF listed on the semiconductor pages [I] V006 | P025, R059 |
| X-ray CD (CD-SAXS) | **none listed in 2026** | An "XCD" tool for 3D-NAND/DRAM high-aspect-ratio structures was shown at FCMN 2022 [F] R051. SPIE AL 2026 talks on ML for X-ray CD are leads only (NOT RETRIEVED) | n/a | n/a | n/a | R051, V006 |
| X-ray imaging, defects | **JVSensus-600F** (orders for the earlier 600E announced 11 Jul 2017), **QC-TT, QC-RT** | Subsurface crystal defects, cracks, slip, edge damage; warpage and tilt mapping; ~20 wafers/hour [S] Q008 | Inline (600F, 300 mm); production (QC-TT); CdTe substrates (QC-RT) | 600E: 2017 | 2017: "multiple leading" logic/foundry manufacturers ordered the 600E [C] | P021-P024, R061, Q008 |
| X-ray imaging for packaging (2D/3D) | **none listed in 2026** | The XRDI page lists "advanced packaging defect inspection". "XRI" void imaging was shown at FCMN 2022 [F] | n/a | n/a | n/a | P020, R052, V006 |

### (b) AFM and other probe tools (lines from Veeco's AFM business, acquired Oct 2010 [S] P028)

| Product | Application | Production vs lab | Launch / first dated | Customers named or described | Ids |
|---|---|---|---|---|---|
| **InSight 300** automated AFM | Roughness, depth, sidewall/CD, defect review, bevel edge. Bruker says it "can be applied" to hybrid-bond pad recess [C] | Inline/HVM; SECS/GEM | NOT DISCLOSED | none | P031-P033 |
| **InSight AFP** (AFM + long-scan profiler) | CMP dishing/erosion, etch depth, EUV line roughness, edge roll-off; hybrid-bonding package | Inline; up to 50 wph [C] | Hybrid-bonding package introduced in a webinar on 2024-12-04 [F] | 10-K: automated AFM "used in the production of High Bandwidth Memory" [C] P039. **Fraunhofer IZM**: in-line AFM up to 300 mm for hybrid/direct-bonding pre-bond roughness and dishing, awarded to Bruker France (2025-08) [F] | P034-P039, C019, C020 |
| InSight CAP / InSight 3D (legacy) | Automated AFM | Inline | Legacy | A*STAR IME (InSight CAP, Cu dishing) [F]; NIST (InSight 3D) [F] | H010, C026 |
| **NanoMet2** (from RAVE) | Inline photomask AFM | Production (mask) | RAVE closed 2019-04-03 | none | P060 |
| **SmartProber P1 / TT** (CIPT) | MRAM MTJ RA/TMR | R&D/FA | NOT DISCLOSED | none | P040, P041 |
| **Hysitron ATI 8800/8900** | Thin-film modulus, hardness, scratch adhesion | In-line or near-line, 300 mm | NOT DISCLOSED | none | P048 |
| **Dektak XTL** stylus profiler | Step height, stress, roughness | Production QA/QC | 2014 (lead only) | none | P050 |
| Dimension Icon, FastScan Pro, IconIR300 | Lab AFM; AFM-IR identification of nano-contaminants | R&D/FA | IconIR joint development project with imec announced 2026-04-07 [F] | imec | P052-P054, S070 |

### (c) Optical profilers and other optical tools

| Product | Application | Production vs lab | Launch / first dated | Customers named or described | Ids |
|---|---|---|---|---|---|
| **InSight WLI** (white-light interferometry) | TSV/TGV, CD, overlay, CMP, die flatness, edge roll-off, bumps (FEOL/BEOL, advanced packaging) | Inline; SECS/GEM 200/300 mm | NOT DISCLOSED. 15th unit shipped June 2025 | "a leading semiconductor manufacturer": 15th unit, part of an order for 27 Bruker optical metrology systems for 2025 [C] | P042-P044, S017 |
| **FilmTek** 2000M TSV / 6000 PAR-SE / 4000 NIR / 2000 PAR-SE | Film thickness and refractive index, TSV depth, %Ge in SiGe | Fab to lab | NOT DISCLOSED | "leading semiconductor development labs and HVM facilities" [C] | P046, P047 |
| ContourSP | HDI-PCB and substrate panels | Production (panel, not wafer) | NOT DISCLOSED | none | P051 |

### (d) Other

- **Mask repair and cleaning (from RAVE, 2019)** [F] P029, P060, P061:
  - Tools: fp-III, nm-VI, Rhazer III, EL-C, Wafer Clean 2200.
  - Production tools. The CFO puts mask repair at about $50M a year (stated 2026-06-04, period NOT DISCLOSED) [S] G063.
- **Microanalysis for failure analysis (lab instruments)** [F] P056, P057, S068:
  - QUANTAX EDS/WDS/EBSD, M4 TORNADO micro-XRF, HYPERION II.
  - eWARP TKD and XFlash FlatQUAD 2L, both launched 2026-08-03.
- **Company-level claims [C]:**
  - "75% of the world's top 25 semiconductor manufacturers rely on Bruker instrumentation" (P001).
  - "#1 Inline AFM, XRD, µXRF, and XRDI ... over 1000 semiconductor metrology tools installed" (P003). No source or year given.
- **How Bruker describes the business:**
  - CFO: three technologies, namely X-ray, automated AFM and WLI [S] G065.
  - 10-K FY2025: the Nano Surfaces and Metrology division "manufactures and markets automated X-ray metrology, automated AFM defect-detection, and photomask repair and cleaning equipment" [F] S028.

## Q2. Size: semiconductor metrology disclosures found, 2023 to Q3 FY2026

Filings checked:
- 10-Ks FY2023-FY2025 and 10-Qs for Q3-23, Q3-24, Q1-25, Q2-25 and Q1-Q3 FY2026.
- None quantifies semiconductor metrology revenue, orders or backlog. They give only qualitative attributions [F] S002, S003, S011, G020, G032, G033; [I] G082.
- The other 10-Qs in 2023-2025 are NOT RETRIEVED (gaps.md).

Figures come from earnings and conference decks [F] and from third-party transcripts [S].

| Date | Source | Period (calendar) | Disclosure | Tag | Id |
|---|---|---|---|---|---|
| 2023-11-09 / 2024-02-29 | 10-Q Q3-23; 10-K FY2023 | 9M FY2023 / FY2023 (Jan-Dec 2023) | BSI NANO growth partly from semiconductor metrology demand; no figure | [F] | S002, S003 |
| 2023-11-02 / 2024-02-13 | Q3-23, Q4-23 decks p7 | 9M FY2023 / FY2023 | "Strong tailwind from AI trends in semiconductor and advanced packaging metrology"; no figure | [C] | S004, S005 |
| 2024-05-17 | Investor webinar p5 | FY2023 (Jan-Dec 2023) | Semi-Metrology = 9% of BSI revenue | [F] | S006 |
| 2024-08-06 / 2024-11-05 | Q2-24, Q3-24 decks; 10-Q Q3-24 | H1 / 9M FY2024 | "Strong growth" in semi metrology; no rate given | [F] | S008-S010 |
| 2025-02-13 | Q4-24 deck p8 | Q4 FY2024 (Oct-Dec 2024) / FY2024 | Organic revenue growth >20% in Q4-24 and low-teens in FY24; >$250M annual revenue; margins "well above corporate average" | [F] / [C] | S012-S015 |
| 2025-02-13 | Q4-24 call | FY2024 (Jan-Dec 2024) | "north of $125 million" AI/HPC-related; total "north of $250 million", "maybe half" to HPC and AI (≈50%, calc/semi_mix_calc.py) | [S] | G050, G051 |
| 2025-06-24 | Release | 2025 | Unnamed manufacturer ordered 27 Bruker optical metrology systems | [C] | S017 |
| 2025-11-03 | Q3-25 deck p7; call | 9M FY2025 (Jan-Sep 2025) | "Softness in X-Ray Semi". Call: semi "approaching or is around $300 million"; "flattish this year" | [F]; [S] | S019-S021 |
| 2026-01-12 | JPM 2026 deck p14 | TTM to Q3 FY2025 (Oct 2024-Sep 2025) | **>$300M revenue, >25% EBIT margin** (one-offs not named) | [F] | S022, S023 |
| 2026-01-12 | JPM 2026 deck p3 | FY2024 (Jan-Dec 2024) | Semi-Metrology = 9% of BSI revenue | [F] | S016 |
| 2026-02-12 | Q4-25 release p1; deck p7, p9 | Q4 FY2025 (Oct-Dec 2025) / FY2025 (Jan-Dec 2025) | Semi orders helped lift BSI book-to-bill above 1.0; **FY2025 semi revenue flat**; strong Q4-25 semi orders; Semi-Metrology = 9% of BSI revenue | [F] | S024-S026 |
| 2026-02-27 | 10-K FY2025 p50 | FY2025 | Group gross-margin decline partly from a decline in the Nano Surfaces and Metrology division | [F] | S030 |
| 2026-02-12 / 2026-05-06 | Q4-25 and Q1-26 calls | FY2026 outlook (Jan-Dec 2026) | Semi revenue guided "up in the low-single-digits range", reaffirmed in Q1 | [S] | S027, S034 |
| 2026-05-06 | Q1-26 call; deck p6; release | Q1 FY2026 (Jan-Mar 2026) | "greater than $300 million annual revenue business" (run-rate, period NOT DISCLOSED); organic bookings >20%; only "some" of the Q4-25 pushout recaptured; strong HBM and advanced-packaging orders | [S]; [F] | S031-S036 |
| 2026-06-04 | Jefferies conference (CFO) | Annual run-rate stated 2026-06-04 (period NOT DISCLOSED) | ~$300M, of which ~$200M production QA/QC (≈67%), ~$50M R&D and ~$50M mask repair. On the analyst's "$40 million pushout": $10-15M recaptured in Q1-26, "similar amount in Q2 and Q3" expected. Capacity to at least double by end-2026 | [S] | G060-G066 |
| 2026-08-04 | Q2-26 deck p8 ("Bruker NANO Semiconductor Metrology") | H1 FY2026 (Jan-Jun 2026) | **>30% organic order growth, >15% organic revenue growth, ~30% EBIT margin** (one-offs not named) | [F] | S037, S038 |
| 2026-08-04 | Q2-26 call | Q2 FY2026 (Apr-Jun 2026) | Semi orders >50% organic; lead times 9-24 months; ~$20M of Q3 revenue moves to Q4 | [S] | S039-S041 |
| 2026-08-05 | 10-Q Q2-26 MD&A | Q2 / H1 FY2026 | BSI NANO revenue "remained consistent" | [F] | G032, G033 |
| 2026-11-04 | Q3-26 call | 9M FY2026 (Jan-Sep 2026) | Semi bookings ">30%" year to date (prepared remarks and Q&A). Q3 semi revenue "down double digits" on pushouts. Orders convert "mostly in fiscal year 2027 and some in fiscal year 2028" | [S] | S045-S047, V001 |
| 2026-11-04 | Q3-26 call | FY2026 outlook | Analyst: "~$300M to end the year, mid to high single digit growth, 30% EBIT". CEO: "I think the direction is correct" | [S] | V003 |
| 2026-11-04 | Q3-26 deck p7; release | 9M FY2026 | "Strong Semi ... revenues" and "Strong AI-driven orders for memory and advanced packaging"; no figure | [F] / [C] | S051, S052 |

Group-level 10-Q phrases that credit "semiconductor markets" (G022, G030, G031) are left out of this table. They also cover BSI BIOS and BEST (EUV/XUV), which are not metrology [F] G010, G011.

**Never disclosed:**
- Semi revenue in dollars for any single quarter or for LTM to Q3 FY2026.
- Bookings or backlog in dollars.
- Semi book-to-bill.
- Semi gross margin.
- China share.
See gaps.md.

**Segment that holds it after July 2026:** BSI NANO (the Bruker Nano group), unchanged [F] G002.
- Within NANO, the Nano Surfaces and Metrology division makes the X-ray and AFM tools [F] S028.
- The BSI NANO restructuring plan includes a "merger of divisions within the segment"; the divisions are not named [F] G012.
- The only named merger is Cellular Analysis into Spatial Biology [F] G013.

**2026 goodwill impairments by reporting unit:**

| Quarter | Charge | Reporting unit | Segment | Semi? | Ids |
|---|---|---|---|---|---|
| Q2 FY2026 (Apr-Jun 2026) | $36.5M | BSB (Bruker Spatial Biology; merged with Cellular Analysis 2026-04-01) | BSI NANO | No | S060 |
| Q2 FY2026 | $98.4M (all remaining goodwill) | CST (Chemspeed, formerly Automation) | BSI BioSpin (pre-recast label) | No | S061 |
| Q3 FY2026 (Jul-Sep 2026) | $174.5M (all remaining goodwill) | BSB&CA | BSI NANO | No | G004 |
| 9M FY2026 (Jan-Sep 2026) | $309.4M total, of which $211.0M BSB/BSB&CA | | | | S063, G006 |

After the reorganisation, the affected units were tested in Q3 and passed. They are not named and no headroom is given, so whether a semiconductor unit was among them is NOT DISCLOSED (read: 10-Q Q3 FY2026 MD&A goodwill section; Note 5) [F] G007.

## Q3. Bruker versus Rigaku, tool class by tool class

| Class | Bruker (2026 pages) | Rigaku (2026 pages) | Named chipmaker or fab use | Share figure |
|---|---|---|---|---|
| HRXRD | 7300LSI, Sirius-XRD, QCVelox, Delta-X | XTRAIA TF/XD, XD-3300 | IBM Research Albany: Bruker JVX7300LSI inline [F] C003. Fraunhofer IPMS: inline 300 mm full-wafer XRR lot (XRD, GIXRD, HRXRD scope) to Rigaku Europe SE (contract 2025-10-07); 300 mm lab XRD lot to Bruker AXS SE (2025-12-05) [F] C015-C018. Fraunhofer III-V/diamond HRXRD and wafer XRD lots to Rigaku (2025) [F] C022, C023. Rigaku XD-3300 "delivered to multiple leading-edge" chipmakers [C] R034 | Bruker "#1 inline XRD", no source or year [C] P003 |
| XRR | Sirius-RF, Sirius-XRD, 7300LSI | XTRAIA MF-2000/3000/3400, CD-3010G | **Kioxia** and Kioxia Iwate to put Rigaku MF-3400 into 3D NAND mass-production lines (Rigaku release 2025-12-04) [C] C005. TSMC chose Jordan Valley JVX6200 XRR for Cu in 2009, before Bruker owned Jordan Valley [S] C001 | none class-specific |
| XRF / µXRF | Sirius-RF, Sirius-FW | WaferX 310, ONYX 3000/3200, XHEMIS EX | Rigaku: first ONYX 3200 to "a major global foundry" for an advanced-packaging line [C] R032. Bruker Sirius-FW "TOR on major packaging fabs" [C] P015 | Bruker "#1 inline µXRF" [C] P003 |
| TXRF / VPD-TXRF | none listed for wafer fabs [I] V006 | TXRF 3760, 310Fab, XHEMIS TX-2000/3000/3000V | none named | Rigaku: "overwhelming market share" in TXRF, no % [C] R015 |
| X-ray CD (CD-SAXS) | none listed in 2026 [I] V006 (XCD shown 2022 [F] R051) | XTRAIA CD-3200T (2020), CD-3010G; with Onto Ai Diffract | **Samsung Electronics (Device Solutions Division)** slides co-authored with Onto and Rigaku on X-ray CD for deep V-NAND (2026-03-18) [F] R048. Onto: offering "selected by two key customers"; "systems delivered for advanced V-NAND and DRAM" [C] R004, R006 | Rigaku 2030 SAM targets [C] R019 |
| X-ray imaging, packaging | none listed (XRDI defect tools only) [I] V006 | XHENA AX-3000, at customer evaluation [S] R030 | none | Rigaku target: >30% of a $300M AXI SAM by 2030 [C] R019 |

**Market-share figures.** Every one is Rigaku quoting Yole; each Yole edition is a separate series. Bruker publishes no X-ray share.

| Year | Rigaku share | Market | Source document | Yole edition | Tag | Id |
|---|---|---|---|---|---|---|
| CY2022 | 26.9% | n/a | Rigaku IPO filing (EDINET, 2024-09-20) | WFE Market Monitor Q2 2024 (front-end X-ray metrology) | [C] | M001 |
| CY2023 | 29.5% | $481M | Same | Q2 2024 | [C] | M001, M002 |
| CY2023 | 30% ("Company A" 24%, others 46%) | $470M | Rigaku mid-term plan, Feb 2025 | Q4 2024 | [C] | R011, R013 |
| CY2024 | 38% | ~$498M | Rigaku annual securities report for FY2025, filed 2026-03-24 | Q4 2025 | [C] | R012, R013 |

Notes on the figures and on who names whom:
- **"Company A" is not identified.** Nova also sells X-ray metrology (VeraFlex XPS + XRF) [F] M009, so Company A should not be assumed to be Bruker [I] M007. Implied 2023 revenue within the same Yole edition: Rigaku about $141M, Company A about $113M [I, Low] M006 (calc/M_calc.py).
- **Bruker's own 10-Ks (FY2023-FY2025)** list BSI NANO competitors by technology class [F] G041-G043. Rigaku, Park Systems and Oxford Instruments are on the list. KLA, Onto and Nova are not [I] G081.
- **Competitors' filings:** Onto's 10-K names KLA, Nova and Camtek. Nova's 20-F names Onto and KLA. KLA's annual report names neither Bruker nor Rigaku [F] M008, M010, M011.
- **Supplier awards:** neither Bruker nor Rigaku is on any award list read. Lists read: Intel SCQI 2011-2015 and 2020, Intel EPIC 2022 and Micron 2025-2026 [F]; TSMC 2021 [S] (C027-C035).

## Q4. Hybrid bonding: copper recess and roughness before bonding

**Bruker at chipmakers:**
- No saved document names a chipmaker (TSMC, Intel, Samsung, SK hynix, Micron, YMTC, Sony) that uses a Bruker AFM, AFP or WLI for pre-bond Cu recess or roughness [I] H081, C036.
- Bruker's own claims name no customer [C]:
  - Application note AN5001 covers 1-5 nm recess and says this makes AFM "indispensable" (H001-H005).
  - The 10-K says automated AFM is "used in the production of High Bandwidth Memory" (P039).
- A hybrid-bonding package for InSight AFP was introduced in a webinar on 2024-12-04 [F] H007.

**Named research fabs using Bruker** [F]:
- **Fraunhofer IZM**: in-line AFM up to 300 mm for pre-bond roughness and dishing (hybrid/direct bonding), awarded to Bruker France, 2025-08 (C019, C020).
- **A*STAR IME**: Cu dishing measured with a Bruker InSight CAP (Commun. Eng. 2026) (H010, H011).
- **ITRI/NYCU**: Bruker Innova on 12-inch wafer-to-wafer samples (H014).
- **NYCU**: Dimension Icon (H015).

**Named chipmaker links to other vendors:**
- **Intel**: hybrid-bonding samples measured at NIST with an Oxford/Asylum Vero AFM [F] H012, H013.
- **SK hynix**: released Infinitesima Metron3D in-line AFM for DRAM volume production [C] H040.
- **IBM Research** with Nova: Cu-recess scatterometry trained on AFM reference data [F] H018-H021.
- Separately, Intel bought six Park NX-Hybrid WLI units. Their use is not stated, so this is not hybrid-bonding evidence [S] H030.

**Competing tools:**

| Vendor | Tool | Hybrid-bonding claim | Adoption evidence | Tag | Ids |
|---|---|---|---|---|---|
| Park Systems | NX-Wafer, FX, NX-Hybrid WLI | "No practical solution other than AFM" for hybrid bonding | Taiwan "T company" AFMs for advanced packaging [S]; 2-year imec project [C] | [S]/[C] | H031-H038 |
| KLA | no saved document ties a tool to Cu recess | KLA FY25 (Jul 2024-Jun 2025): >$925M advanced-packaging revenue; hybrid bonding not mentioned | NOT DISCLOSED (read: KLA FY25 annual report) | [C] | H063 |
| Nova | Prism (spectral interferometry + OCD), VTS-ML | Inline Cu recess with reduced "reliance on reference data" | IBM Research co-authored a SPIE 2026 paper | [F]/[C] | H018-H021, H050-H052 |
| Onto Innovation | OCD for Cu recess; Dragonfly G5 + 3Di | OCD with "strong correlation to AFM", positioned for HVM | One HBM maker: "double-digit" G5 + 3Di commitments for HBM4 (inspection and bump metrology, not recess) | [C] | H053-H056 |
| Infinitesima; Nearfield; Camtek (Hawk) | in-line AFM; QUADRA; inspection | | SK hynix (Infinitesima) [C]; imec (Nearfield) [S]; >$50M of Hawk orders, customers unnamed [C] | | H040-H042, H062 |

**Tool counts per line:** NOT DISCLOSED in any document read (list in gaps.md; H070). The only nearby number is Onto's "double-digit" G5 commitment from one HBM maker [C] H055. That is an inspection-tool order, not a per-line ratio.

## Q5. Bruker's reaction to the Onto-Rigaku alliance (since 2026-04-20)

Two separate searches found **no** Bruker partnership, acquisition, investment or fab product launch in X-ray or hybrid metrology, and no Bruker remark on Onto, Rigaku or X-ray competition [I] Q013, Q014. Documents read:
- Q1-Q3 FY2026 call transcripts, decks, releases and 10-Qs.
- The 8-Ks filed Aug-Nov 2026.
- The bruker.com sitemap (28 news items in 2026).
- SemiEngineering articles from 2026.
- The FCMN 2026 abstracts.

Closest items:
- **Q2-26 deck slide 8:** "AAFM, WLI, and X-ray metrology required" for HBM, CoWoS and AI logic [C] S067.
- **2026 acquisitions:** Tofwerk (Jan 6) and Mimetas (Aug 7), both in BSI BIOS, plus a minority stake in Atinary. None is in semiconductor X-ray [F] Q010-Q012.
- **Bruker's "hybrid analysis" at FCMN (Mar 2026):** X-ray only, fitting XRR and HRXRD together on Sirius-XRD [F] Q001.
- **Bruker staff in trade press after April 2026:** X-ray roadmap comments on new X-ray sources for patterned targets, sub-angstrom specs, and XRDI at ~20 wafers/hour [S] Q006-Q008.

---

# Module B (semiconductor business only)

## B1. Disputed-claims ledger

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| (a) Semiconductor metrology bookings grew more than 30% in the first nine months of 2026 | User prompt. Source of the figure: CEO Laukien, Q3-26 call, 2026-11-04 | Prepared remarks: "year to date ... greater than 30% organic bookings growth in BSI semicon metrology markets" (S045). Q&A: "semi bookings have been just very strong year to date, greater than 30%" (V001). H1 FY2026 deck: ">30% Organic Order Growth" (S037). Q2 FY2026 semi orders >50% (S039). Q3 BSI orders "driven by strong growth in semi" (S049) | The 9M figure appears in no Bruker document. Neither the Q3-26 deck nor the release gives a number (S051, S052), and the 10-Q gives no semi bookings (G082). The Q3 BSI order book overall rose only low single digits (V002; BSI-wide, not semi) | For: [F] for H1 FY2026 (S037); [S] for 9M FY2026 (S045, V001). Against: [F] absence in company documents (S051, G082) |
| (b) Bruker leads X-ray metrology in logic fabs and Rigaku leads in memory | User prompt. No source found in filings, releases, papers or trade press (R notes §3) | Samsung Electronics (Device Solutions Division) co-presented X-ray CD for deep V-NAND with Rigaku and Onto (R048). Kioxia is putting Rigaku MF-3400 into 3D NAND production (C005). Rigaku's mix moved toward memory: FY2025 (Jan-Dec 2025) memory 26% vs logic/foundry 21% (R043). 9M FY2025 memory ¥3.6bn vs ¥1.1bn a year earlier; the 9M FY2024 chart labels do not add up to the bar total (R040, R041). Bruker's 2016-17 releases cite logic/foundry customers (P009, R061) | Rigaku FY2024 (Jan-Dec 2024) was logic-heavy: logic/foundry 35% vs memory 10% (R042). Rigaku claims a "major logic manufacturer" for light-element XRF (R037). Bruker's 2026 order strength is in "memory and advanced packaging" (S051, R063). Fraunhofer's inline 300 mm XRR lot went to Rigaku (C016). No vendor, and no Yole figure relayed by Rigaku, gives share by fab type | For: [F] R048, R043; [C] C005. Against: [F] R042, C016; [C] R063 |
| (c) AFM remains the reference method for pre-bond copper recess | User prompt. Bruker AN5001 (©2025): "making AFM indispensable" (H003). Adeia: "AFM is the standard method to measure Cu recess" (H065). Park (H031, H035) | IBM/Nova trained inline scatterometry on AFM reference data (H018-H021). imec calibrated in-line SEM to AFM, RMSE 0.42/0.47 nm, as reported in a 2026 review (H022). Research fabs use AFM for recess (H010-H017). Fraunhofer IZM bought an in-line AFM for pre-bond dishing (C019). Onto says its OCD has "strong correlation to AFM" (H054) | Onto: AFM's "low throughput and contamination risk limit its applicability in high-volume manufacturing" (H053). Nova: Prism reduces "reliance on reference data" (H050, H051). Adeia blog: PSI gives about 1,000x the throughput of AFM (H067). An 80x80 µm AFM image takes ~5 min (H066). No SEMI standard or imec position statement found | For: [F] H018-H022, C019. Against: [C] H053, H050, H067 |
| (d) Semi metrology is a ~$300M business at ~30% EBIT margin | Analyst framing on the Q3-26 call (V003). CEO: "I think the direction is correct" | JPM 2026 deck: >$300M revenue and >25% EBIT for TTM to Q3 FY2025 (Oct 2024-Sep 2025) (S022, S023). H1 FY2026: ~30% EBIT (S038). CFO at Jefferies: ~$300M run-rate (G060). One-offs: none named for either margin | Revenue: FY2025 flat (S025); Q3 FY2026 down double digits (S047). LTM to Q3 FY2026: NOT DISCLOSED. EBIT basis undefined. The analyst's "mid to high single digit growth" conflicts with the low-single-digit FY2026 guide (S027, S034) | For: [F] S022, S038. Against: [F] S025; [S] S047, S027 |
| (e) Bruker is #1 in inline AFM, XRD, µXRF and XRDI | Bruker brochure B5000 (2026) (P003) | Park Systems' own Q3 2025 report presents #1 in industrial automated AFM as a goal, not a position Park holds (M025). The industrial-AFM rank is given only by KIRS: Bruker #2 (M016) | Rigaku claims leadership in X-ray metrology: 30% (CY2023), 38% (CY2024), citing Yole (R011, R012, M001). Park claims #1 in AFM overall (M020) and says it overtook Bruker in revenue in 2022 (M023). MarketsandMarkets via KIRS, whole AFM market 2024: Park 21.7%, Bruker 15.8% (M014) | For: [C] P003, M025. Against: [C] R012, M020; [S] M014 |
| (f) The Q3 FY2026 semi revenue drop is timing (pushouts), not demand | CFO, Q2-26 call (S041); CEO, Q3-26 call (S047) | ~$20M shift from Q3 to Q4 flagged in August (S041). H1 FY2026 orders >30% (S037). Conversion "mostly in fiscal year 2027" (S046). On the analyst's $40M Q4-25 pushout: $10-15M recaptured in Q1 and "a similar amount" expected in Q2 and Q3 (G064). If that holds, 75-112% is recaptured by end Q3 [I, Low] V005 | FY2025 revenue flat (S025), with "Softness in X-Ray Semi" (S019). BSI NANO revenue only "remained consistent" in H1 FY2026 while semi revenue rose >15% (G033, S037). Only "some" of the Q4-25 pushout was recaptured in Q1 (S033) | For: [F] S037; [S] S041, G064. Against: [F] S019, S025, G033 |

## B2. Facts that most weaken each reading

**Three facts that most weaken the optimistic reading:**
1. No CD-SAXS (X-ray CD) tool appears on Bruker's 2026 X-ray product pages or brochure [F] R053, P notes. Samsung Electronics (Device Solutions Division) co-presented X-ray CD for deep V-NAND with Onto and Rigaku on 2026-03-18 [F] R048. Onto says the combined CD-SAXS + Ai Diffract offering was "selected by two key customers" [C] R004.
2. Rigaku, citing Yole, claims 38% of semiconductor X-ray metrology in CY2024 (Q4 2025 edition) [C] R012. Kioxia is putting Rigaku MF-3400 into 3D NAND mass production [C] C005.
3. Semi revenue was flat in FY2025 (Jan-Dec 2025), with "Softness in X-Ray Semi" [F] S025, S019. The FY2025 10-K ties part of the group gross-margin decline to the Nano Surfaces and Metrology division [F] S030. Q3 FY2026 semi revenue fell by double digits on pushouts [S] S047.

**Three facts that most weaken the pessimistic reading:**
1. In H1 FY2026 (Jan-Jun 2026), semi metrology orders grew >30% and revenue >15%, both organic, at a ~30% EBIT margin. Bruker names no one-off items and does not define the EBIT basis [F] S037, S038.
2. Year-to-date semi bookings were up >30% as of the Q3-26 call (Jan-Sep 2026). Bruker says these orders convert "mostly in fiscal year 2027" [S] V001, S046.
3. Fraunhofer IZM awarded its in-line AFM contract for hybrid-bonding pre-bond metrology to Bruker France (2025-08) [F] C020. Rigaku's own IPO filing says customers already running competitors' installed tools are hard to win, because of tool-of-record lock-in [C] M005.

## B3. Dated catalysts, next 12 months (Dec 2026 - Nov 2027)

Only events with a dated source are listed:

| Date | Event | Why it matters | Source / tag |
|---|---|---|---|
| By end-2026 | CFO target: semi capacity "at least double" | Delivery capacity for FY2027 conversion | [S] G066 |
| 2027-03-30 to 04-01 | SEMICON West, Phoenix (first spring date) | Main North American venue for launches; watch for Bruker X-ray CD or hybrid-metrology news (Q5) | [F] V004 |
| FY2027 (Jan-Dec 2027), with some in FY2028 | Conversion of 2026 semi orders to revenue | Tests ledger claims (a), (d) and (f) | [S] S046 |
| FY2026 (Jan-Dec 2026), reported in early 2027 | Rigaku's forecast of >JPY 6bn MF-3400 + predecessor sales | Measures Rigaku's memory XRR push | [C] C006 |

**Watch list, no confirmed date** [I]:
- **Bruker Q4 FY2026 results and FY2027 outlook.** Expected mid-February 2027 by precedent: the Q4 FY2025 results came on 2026-02-12 (S024). Inference: Medium.
- **Bruker 10-K FY2026.** Expected late February 2027 by precedent: the FY2025 10-K was filed 2026-02-27 (S028). It may show the October 1 goodwill-test results and the NANO division merger. Inference: Medium.
- **Rigaku FY2026 results and annual securities report.** Expected Feb-Mar 2027: Rigaku's FY ends Dec 31 (R047) and the FY2025 annual report was filed 2026-03-24 (R012). A new Yole share figure is possible. Inference: Medium.
- **Conference dates not retrieved:**
  - SPIE Advanced Lithography + Patterning 2027: NOT RETRIEVED (spie.org bot page); search lead says 2027-02-21 to 02-25.
  - IEEE ECTC 2027: NOT RETRIEVED (ectc.net 403); search lead says 2027-06-01 to 06-04.
- **Out of scope at business-unit level:** group debt maturities and lock-ups.
- **Export controls:** no dated deadline found. The CEO said China restrictions on very high-performance semi equipment have been "in place for 2-3 years" [S] G052.

## B4. Gap log
See `gaps.md`.

## B5. Handoff row
See `handoff.md`.

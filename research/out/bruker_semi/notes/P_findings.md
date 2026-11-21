# P: Bruker semiconductor product map (Q1)

Scope: Bruker tools sold into semiconductor fabs and advanced-packaging lines. Evidence rows are P001-P061 in `research/out/bruker_semi/parts/P.csv`. quote_check result: 61/61 FOUND, no flags.
Main sources: the semiconductor solutions hub, six category pages and 22 product pages on bruker.com (retrieved 2026-11-21), brochure B5000 Rev A3 (2026), AN5001 (2025), bruker.com and q4cdn news releases (2017, 2019, 2025, 2026), 10-K FY2025 (pages 11, 18, 41, 145, 147) and the Q2 2026 earnings presentation (slide 8).

## Premise check (corrections to the prompt)
- **Jordan Valley Semiconductors closed in November 2015, not 2019 (P026, [S] reprint).** The 2016 release also says "Bruker's acquisition of Jordan Valley Semiconductors in 2015" (P009 document). The 2019 deal was **RAVE LLC**, which brought mask repair and CO2 cryo cleaning (P029, [F]).
- **The Veeco deal closed in October 2010 for $229.4M in cash (P028, [S] reprint).** It covered Veeco's AFM and Optical Industrial Metrology businesses. That is the origin of the AFM, Dimension and WLI lines (an [I] inference).
- **Product names in the prompt that are not on any current Bruker semiconductor page I read:**
  - "JVX/QC/Delta-X lines": these exist. The current names are 7300LSI (formerly JVX7300LSI), QCVelox-HR, QCVelox-E, QC5-R and Delta-X.
  - D8 FABLINE: last seen in a 2012 release (lead only). The D8 DISCOVER and D8 ADVANCE Plus are offered for semiconductor R&D (P058).
  - Sirius-XRI, JV-QCTT, InSight CAP, ContourX, ContourGT and NPFLEX are not on the semiconductor pages. The insight-cap URL returns 404. The X-ray defect inspection tool is named **QC-TT**.
  - S4 T-STAR is a benchtop TXRF for liquids. It is not listed on any semiconductor page.
  - Nanometrics: no link to Bruker found, which matches the prompt.
- **There is a semiconductor ellipsometry/reflectometry line (FilmTek) and a CIPT line (SmartProber)**, which the prompt did not list. The hub also lists mask repair and cryo-cleaning process equipment.

## Product map

The production column uses these labels:
- **Inline/HVM:** sold for production lines (fab automation or 300 mm handling).
- **R&D/lab:** R&D, failure analysis or lab use.

Launch dates: except where a row gives a dated press release, the launch date is NOT DISCLOSED on the product page I read.

| Group | Product | Application (what it measures) | Production vs lab | Launch / first shown | Customers named or described | Evidence |
|---|---|---|---|---|---|---|
| (a) X-ray XRD/XRR | Sirius-XRD | XRD + XRR for gate-all-around, advanced memory | Inline (Sirius platform) | NOT DISCLOSED. Appears only in the 2026 brochure; no product page. 10-K FY2025 cites new "fully automated uXRD and uXRF" systems for AI chips | none | P005, P018 |
| (a) X-ray HRXRD/XRR/GIXRD | 7300LSI (formerly JVX7300LSI) | Epi strain, thickness and composition; high-k on DRAM/NAND; nanosheet Si/SiGe stacks; GaN-on-Si | Both: in-fab R&D and inline. 300/200/150 mm, FOUP/SMIF, SECS/GEM | NOT DISCLOSED. Already sold by July 2016 | "multiple leading logic and foundry manufacturers" for 10 and 7/5 nm (2016) [S]; "advanced nodes logic and memory fabs" [C] | P006-P009, P058 |
| (a) X-ray XRD/HRXRD/XRR | Delta-X | Thin-film R&D, process development and QC; 300 mm mapping | R&D/lab and QC | NOT DISCLOSED | none | P010 |
| (a) X-ray HRXRD/XRR (compound semi) | QCVelox-HR | Epilayer QC (GaN/AlGaN and others) | Inline/HVM. EFEM 200-300 mm, SEMI S2/S8/S14/S22/S23/F47 | NOT DISCLOSED | none | P013 |
| (a) X-ray HRXRD (compound semi) | QCVelox-E | Routine epi/substrate QC; successor of QC3 | Production. Optional robot and SECS-GEM | NOT DISCLOSED | "leading epi manufacturers" [C] | P012 |
| (a) X-ray HRXRD/XRR (compound semi) | QC5-R | Epilayer QC; manual loading | Production QC (manual load) | NOT DISCLOSED ("next-gen") | none | P011 |
| (a) X-ray uXRF + XRR | Sirius-RF (also 6300-XRR / 6300-RF in the brochure table) | Film composition and thickness on pads or devices: DRAM, PCRAM, 3D-NAND, MRAM, logic, power, packaging | Inline/HVM. 4th generation, SEMI compliance | NOT DISCLOSED | none | P016, P017 |
| (a) X-ray uXRF (packaging) | Sirius-FW | Single-bump %Ag in SnAg, UBM, RDL and pillar thickness, bump height | Inline/HVM. 4th generation, >95% uptime [C] | NOT DISCLOSED | "TOR on major packaging fabs" [C] | P014, P015, P059 |
| (a) X-ray TXRF | unnamed "TXRF systems" | Metal contamination on Si and SiC | NOT DISCLOSED | NOT DISCLOSED | none | P025 |
| (a) X-ray defect imaging (XRDI) | JVSensus-600F (successor of 600E) | Cracks, slip and edge damage on 300 mm Si (blanket, patterned, metallized); prevents wafer breakage in fast anneal | Inline/HVM, 300 mm | 600E orders announced at SEMICON West, 11 Jul 2017; 600F date NOT DISCLOSED | 2017: "leading multiple semiconductor manufacturers" (headline: logic and foundry) | P021, P022 |
| (a) X-ray defect imaging (XRDI) | QC-TT | Transmission XRDI of non-visual defects in Si, GaAs, GaN, InP substrates; up to 15 wph; KLARF | Production | NOT DISCLOSED | none | P023 |
| (a) X-ray defect imaging (XRDI) | QC-RT | Reflection XRDI for CdTe/HgCdTe (IR detectors) | Production QC (not Si fab) | NOT DISCLOSED | none | P024 |
| (a) X-ray for packaging / HBM | (no named product) | The XRDI page lists "advanced packaging defect inspection" and "warpage and tilt mapping for advanced processors". Q2-26 slide: X-ray is required for HBM, CoWoS and AI logic | n/a | n/a | none | P020, P045 |
| (a) X-ray CD (CD-SAXS/T-SAXS) | none offered | NOT DISCLOSED: absent from hub, brochure and X-ray metrology page | | | | — |
| (b) Automated AFM | InSight 300 | Roughness, depth (DTMode), sidewall/CD (CDMode), defect review, profiling, hybrid-bond pad recess, bevel edge | Inline/HVM. SECS/GEM, E84, SEMI S2/S8, F47 | NOT DISCLOSED | none | P031-P033, P036 |
| (b) Automated AFP | InSight AFP | CMP dishing and erosion, etch depth, EUV line roughness, large-area scanning, hybrid bonding package, ERO | Inline/HVM. Up to 50 wph [C]; KLARITY compatible | Hybrid bonding package presented Dec 2024 (webinar) | none named. 10-K: AAFM "used in the production of HBM" | P034-P039 |
| (b) CIPT probe | SmartProber P1 / SmartProber TT | MTJ RA/TMR (MRAM) by current-in-plane tunneling; P1 maps 300 mm | R&D/FA (P1); table-top R&D (TT) | NOT DISCLOSED | none | P040, P041 |
| (b) Nanomechanical | Hysitron ATI 8800/8900 | Thin-film modulus, hardness and scratch adhesion | In-line or near-line, 300 mm automated | NOT DISCLOSED | none | P048 |
| (b) Nanomechanical / tribology | Hysitron TI 990, PI 89 Auto, TriboLab CMP | Nanoindentation; CMP consumables | R&D/lab | NOT DISCLOSED | none | P055 |
| (b) Stylus profiler | Dektak XTL | Step height, film stress, roughness; up to 350x350 mm | Production QA/QC (gage-capable) | 2014 per IR headline (lead only, NOT RETRIEVED) | none | P050 |
| (b) Lab AFM / AFM-IR | Dimension Icon, FastScan Pro, IconIR300 (200/300 mm, KLARF) | Nanoscale property mapping; nanocontaminant chemical ID | R&D/FA | IconIR300 NOT DISCLOSED; IconIR JDP at imec, Apr 2026 | imec (JDP partner) [C/F] | P052-P054 |
| (c) WLI optical profiler | InSight WLI | TSV/TGV, CD, overlay, CMP, die flatness, ERO, bump analysis; FEOL/BEOL/advanced packaging/MEMS | Inline/HVM. SECS/GEM 200/300 mm | NOT DISCLOSED. 15th unit shipped Jun 2025 | "a leading semiconductor manufacturer": 15th unit, within a 27-system optical metrology order for 2025 | P042-P044 |
| (c) WLI (PCB/panel) | ContourSP | HDI-PCB / substrate panel layers up to 600x600 mm | Production (PCB, not wafer fab) | NOT DISCLOSED | none | P051 |
| (c) Ellipsometry/reflectometry | FilmTek 2000M TSV, 6000 PAR-SE, 4000 NIR, 2000 PAR-SE (robotic) | Film thickness/RI, TSV depth/CD, TTV, %Ge in SiGe, silicon photonics | Fab to lab; 2000M TSV 40+ wph at 200/300 mm [C] | NOT DISCLOSED | "leading semiconductor development labs and HVM facilities" [C] | P046, P047 |
| (c/b) Edge metrology | ERO application (InSight AFP / InSight WLI) | Edge roll-off, edge trim for W2W hybrid bonding, BSPDN, epi crown/EBR | Inline | n/a | none | P049 |
| (d) Mask repair / cleaning (from RAVE) | fp-III, nm-VI, Rhazer III, EL-C, Wafer Clean 2200, NanoMet2 (inline mask AFM) | Photomask repair, haze removal, CO2 cryo cleaning; NanoMet2 metrology | Production (mask shops/fabs) | RAVE acquired 3 Apr 2019; nm-VI was new then | cryo: ">100 tools installed" [C] | P029, P060, P061 |
| (d) Microanalysis for FA | QUANTAX EDS/WDS/EBSD, eWARP TKD, XFlash FlatQUAD 2L, M4 TORNADO micro-XRF, HYPERION II ILIM, FT-IR | Contaminant and failure analysis, lamella EDS | Lab/FA (SEM/TEM accessories) | eWARP TKD and FlatQUAD 2L launched 3 Aug 2026 (M&M 2026) | none | P056, P057 |
| (d) FIB / mass spec | none marketed to semi | Bruker EDS is sold "for your SEM, FIB" | | | | P056 |

Company-level claims [C]:
- "75% of the world's top 25 semiconductor manufacturers rely on Bruker instrumentation" (P001).
- "#1 Inline AFM, XRD, uXRF, and XRDI Solutions with over 1000 semiconductor metrology tools installed worldwide" (P003).
- 10-K: the division makes "automated X-ray metrology, automated AFM defect-detection, and photomask repair and cleaning equipment for semiconductor process control" (P030).

## Provenance
- **Veeco AFM + Optical Industrial Metrology, Oct 2010, $229.4M cash.** This is the source of the AFM, InSight, Dimension, Wyko VSI/Contour and Dektak lines (P028 [S]; mapping is [I]).
- **Jordan Valley Semiconductors, closed Nov 2015.** It brought the JVX7300 line, JVSensus, the Sirius line (Jordan Valley XRF per the WLP page) and the JV-RADS/REFS software. The XRDI heritage is "Bede and Jordan Valley". The 10-K shows an X-ray facility at Migdal HaEmek, Israel and a subsidiary named Bruker JV UK Ltd. (P026 [S], P027, P059).
- **RAVE LLC mask repair and cleaning, Apr 2019.** CY2018 revenue was about $25M; the price was not disclosed (P029).
- **SmartTip BV (CIPT).** Listed as a subsidiary in the 10-K. The probes fit Capres tools. The acquisition date was NOT RETRIEVED (P041).
- **FilmTek and Hysitron.** The acquisition sources were NOT RETRIEVED.

## NOT DISCLOSED
- **Launch dates.** I read every product page listed above, and the hub, the X-ray metrology, XRDI, AFM/CIPT, surface metrology and ellipsometry pages. No launch dates appear for:
  - Sirius-XRD, Sirius-RF, Sirius-FW, 7300LSI, Delta-X, QCVelox-HR/-E, QC5-R
  - JVSensus-600F, QC-TT, QC-RT
  - InSight 300, InSight AFP, InSight WLI
  - FilmTek 2000M TSV, Hysitron ATI 8800/8900, SmartProber P1/TT, Dimension IconIR300
- **Named fab customers.** None appear in any document read. The 2025 release, the 2017 release and the 2016 reprint describe customers only.
- **X-ray CD (CD-SAXS/T-SAXS) or X-ray radiography/CT for packaging.** Not offered (read: hub, brochure B5000 pp1-16, X-ray metrology and XRDI category pages).
- **Name of the TXRF wafer tool.** Not given (read: semiconductor applications page, Defects & Contamination page, Contamination Control page).
- **Status of the 6300-XRR / 6300-RF tools.** Brochure p16 lists them, but there is no product page.
- **Hysitron model number.** The page heading says ATI 8800; the URL and brochure say ATI 8900.

## NOT RETRIEVED
- **ir.bruker.com originals** of the 2010, 2014 Dektak XTL, 2015 and 2016 releases. Not attempted, because the site refuses scripts. I used biospace.com reprints instead, tagged [S].
- **Business Wire copy of the 2025-06-24 release.** The fetch failed with curl rc=92 (HTTP/2 stream error). The q4cdn PDF copy was used instead.
- **bruker.com news archive.** Tried the 2010, 2014, 2015 and 2016 slugs; all returned 404.
- **Firecrawl search.** Out of credits.
- **Source for the FilmTek acquisition** (lead: Scientific Computing International). Searched; no primary source found.
- **Dates of the SmartTip and Hysitron acquisitions.** Not searched in depth.
- **Earlier wafer TXRF tool:** a JVX7300F-C seen only in a search snippet; it is not on the current page.
- **D8 FABLINE and S8 FABLINE-T:** a 2012 SEMICON West lead only; d8-fabline.html returns 404.

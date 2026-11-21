# Bruker Corporation (BRKR, Nasdaq, USA): semiconductor metrology business

Research date: 2026-11-21. **Fiscal year ends December 31**, so fiscal quarters match calendar quarters: Q3 FY2026 = Jul-Sep 2026.
Scope: semiconductor metrology only. Module A was skipped, as instructed. Group and segment financials are left out.
Evidence ids (S, P, R, H, G, C, M, Q) refer to rows in `evidence.csv`; the files they cite are in `research/sources/bruker_semi/`.
Tags: [F] fact read in a saved primary document; [C] company claim that cannot be tested; [S] secondary source, including third-party call transcripts; [I] inference.

## Premise check (prompt and prior/)

1. **prior/ is empty** (only `.gitkeep`). The "Bruker Financial and Segment Performance" chat is not in the repo, so I could not check it for overlap. Group and segment financials are still left out.
2. **CLAUDE.md on this branch was a placeholder.** The rules used here were taken unchanged from branch `ccr-2b9561fc-mqqdg4` (see run_log.md).
3. **"July 2026 reorganisation": correct.** It took effect on July 1, 2026 [F] G001.
   - New segments: BSI Biosystems (BIOS), BSI Microbiology and Infection Diagnostics (BMID), BSI NANO and BEST. They replace BSI BioSpin, BSI CALID, BSI NANO and BEST.
   - **Semiconductor metrology did not move.** BSI NANO was left unchanged, and it still covers "X-ray metrology, defect-detection equipment for semiconductor process control" [F] G002, G003, S055.
   - A web-search summary placed semiconductor metrology in BEST. That is wrong.
4. **"2026 goodwill impairments": correct, but none hit a semiconductor unit.**
   - Q2 FY2026: $134.9M, split into $36.5M for BSB (spatial biology, BSI NANO) and $98.4M for CST/Chemspeed (BSI BioSpin before the recast) [F] S059-S061.
   - Q3 FY2026: $174.5M for BSB&CA (spatial biology plus cellular analysis, BSI NANO) [F] G004.
   - 9M FY2026 total: $309.4M [F] S063.
5. **"Onto-Rigaku alliance, April 2026": correct, with details.**
   - Announced 2026-04-20. Onto bought 27% of Rigaku from Carlyle's Atom Investment L.P. It did not subscribe for new shares [F] R001, R002.
   - Price was about $710M at signing and JPY 113.08bn, about $720M, at closing on 2026-08-10 [F] R007.
   - The CD-SAXS + Ai Diffract integration pre-dates the stake [F] R010.
6. **The "9% semi metrology" share is a share of BSI revenue, not of total Bruker** [F] S016, S026.
7. **Product names in the earlier brief:**
   - JVX7300LSI is now sold as "7300LSI".
   - D8 FABLINE, Sirius-XRI, JV-QCTT, InSight CAP, ContourX/GT and NPFLEX are not current semiconductor products. QC-TT is an XRDI defect-inspection tool, not metrology [F] P006, R053, R055; P notes.
   - Jordan Valley Semiconductors was acquired in Nov 2015, not 2019 [S] P026. The 2019 deal was RAVE (mask repair) [F] P029.
8. **Competitor products in Q4:**
   - Camtek's hybrid-bonding tool is Hawk, not Eagle G5 [C] H062.
   - Nova's Cu-recess tools are Prism and VTS-ML, not Elipson [C] H050.
   - Onto's Cu-recess method is OCD; 3Di is bump metrology [C] H053.
   - Park's "NX-Hybrid WLI" means AFM + WLI and has nothing to do with hybrid bonding.
9. **Ledger claims:**
   - Claim (b), "Bruker leads logic, Rigaku leads memory", has no identifiable source in anything read [I] R notes §3.
   - Claim (a) rests on one ambiguous transcript sentence (see B1).

## Q1. Product map: Bruker tools sold into fabs and packaging lines

Sources: bruker.com semiconductor hub and product pages (retrieved 2026-11-21), brochure B5000 Rev A3 (2026), 10-K FY2025, releases.
- **Launch dates are NOT DISCLOSED on any current product page** (read: every page listed in P notes). Dates below come from dated releases or papers.
- **Named fab customers are NOT DISCLOSED** in any Bruker document read.
- Production = inline or high-volume manufacturing (fab automation, SECS/GEM, 300 mm). Lab = R&D or failure analysis.

### (a) X-ray (lines come from Jordan Valley, acquired 2015, and Bede)

| Class | Product | Application | Production vs lab | Launch or first dated | Customers named or described | Ids |
|---|---|---|---|---|---|---|
| Diffraction + reflectometry | **Sirius-XRD** | XRD + XRR for gate-all-around and advanced memory | Inline | NOT DISCLOSED. In the 2026 brochure; no product page. FCMN 2026 data on imec CFET wafers | imec wafers, measured by Bruker staff [F] | P005, P018, C008 |
| HRXRD / XRR / GIXRD | **7300LSI** (formerly JVX7300LSI) | Epi strain, thickness, composition; high-k; nanosheet Si/SiGe | In-fab R&D and inline; 300/200/150 mm | Sold by 2016 | 2016: "multiple leading logic and foundry manufacturers" [S]. **IBM Research Albany** inline JVX7300LSI, SPIE 2021 [F] | P006-P009, C003 |
| HRXRD / XRR (lab) | **Delta-X**; D8 DISCOVER / D8 ADVANCE Plus | Thin-film R&D and QC, 300 mm mapping | Lab | NOT DISCLOSED | Fraunhofer IPMS: 300 mm lab XRD awarded to Bruker AXS (Dec 2025) [F] | P010, P058, C018 |
| HRXRD / XRR (compound semi) | **QCVelox-HR, QCVelox-E, QC5-R** | GaN/AlGaN and III-V epilayer QC | Production QC | NOT DISCLOSED | "leading epi manufacturers" [C] | P011-P013 |
| Fluorescence (µXRF) + XRR | **Sirius-RF** (6300-RF / 6300-XRR in the brochure table) | Film composition and thickness: DRAM, PCRAM, 3D-NAND, MRAM, logic, packaging | Inline, 4th generation | NOT DISCLOSED | none | P016, P017 |
| Fluorescence (µXRF), packaging | **Sirius-FW** ("Sirius-FW G2" in an FCMN 2026 abstract) | Single-bump %Ag in SnAg, UBM, RDL and pillar thickness, bump height | Inline | NOT DISCLOSED | "TOR on major packaging fabs" [C] | P014, P015, P059, Q003 |
| TXRF | **unnamed** | Metal contamination on Si and SiC | NOT DISCLOSED | NOT DISCLOSED | none. No wafer-fab TXRF on the semiconductor pages; probably the lab TXRF line of Bruker AXS [I, Low] | P025, R059, R072 |
| X-ray CD (CD-SAXS) | **none offered in 2026** | Bruker showed an "XCD" tool for 3D-NAND/DRAM high-aspect-ratio structures at FCMN 2022 [F] R051. Leads (not retrieved) to SPIE AL 2026 talks on ML for X-ray CD | n/a | n/a | n/a | R051, R072 |
| X-ray imaging (defects) | **JVSensus-600F** (600E orders announced 11 Jul 2017), **QC-TT, QC-RT** | Subsurface crystal defects, cracks, slip, edge damage; warpage and tilt mapping; ~20 wafers/hour [S] | Inline (600F, 300 mm); production (QC-TT); CdTe (QC-RT) | 600E: 2017 | 2017: "multiple leading" logic/foundry makers ordered the 600E [C] | P021-P024, R061, Q008 |
| X-ray imaging for packaging (2D/3D, laminography) | **none offered in 2026** | The XRDI page lists "advanced packaging defect inspection". Bruker showed "XRI" void imaging at FCMN 2022 | n/a | n/a | n/a | P020, R052 |

### (b) AFM and other probe tools (lines come from Veeco's AFM business, acquired Oct 2010 [S] P028)

| Product | Application | Production vs lab | Launch or first dated | Customers named or described | Ids |
|---|---|---|---|---|---|
| **InSight 300** automated AFM | Roughness, depth, sidewall/CD, defect review, hybrid-bond pad recess, bevel edge | Inline/HVM; SECS/GEM | NOT DISCLOSED | none | P031-P033 |
| **InSight AFP** (AFM + long-scan profiler) | CMP dishing/erosion, etch depth, EUV line roughness, edge roll-off; hybrid-bonding package | Inline; up to 50 wph [C] | Hybrid-bonding package introduced 2024-12-04 (webinar) [F] | 10-K: automated AFM "used in the production of High Bandwidth Memory" [C]. **Fraunhofer IZM**: in-line 300 mm AFM for hybrid-bonding pre-bond roughness and dishing awarded to Bruker France (Aug 2025) [F] | P034-P039, C019, C020 |
| InSight CAP / InSight 3D (legacy) | Automated AFM | Inline | Legacy | A*STAR IME (InSight CAP, Cu dishing) [F]; NIST (InSight 3D) [F] | H010, C026 |
| **NanoMet2** (from RAVE) | Inline photomask AFM | Production (mask) | RAVE closed 2019-04-03 | none | P060 |
| **SmartProber P1 / TT** (CIPT) | MRAM MTJ RA/TMR | R&D/FA | NOT DISCLOSED | none | P040, P041 |
| **Hysitron ATI 8800/8900** | Thin-film modulus, hardness, scratch adhesion | In-line or near-line, 300 mm | NOT DISCLOSED | none | P048 |
| **Dektak XTL** stylus profiler | Step height, stress, roughness | Production QA/QC | 2014 (lead only) | none | P050 |
| Dimension Icon, FastScan Pro, IconIR300 | Lab AFM and AFM-IR for nano-contaminant ID | R&D/FA | IconIR joint development project with imec announced 2026-04-07 [F] | imec | P052-P054, S070 |

### (c) Optical profilers and other optical tools

| Product | Application | Production vs lab | Launch or first dated | Customers named or described | Ids |
|---|---|---|---|---|---|
| **InSight WLI** (white-light interferometry) | TSV/TGV, CD, overlay, CMP, die flatness, edge roll-off, bump analysis (FEOL/BEOL, advanced packaging) | Inline; SECS/GEM 200/300 mm | NOT DISCLOSED. 15th unit shipped June 2025 | "a leading semiconductor manufacturer": 15th unit, part of a 27-system optical metrology order for 2025 [F] | P042-P044, S017 |
| **FilmTek** 2000M TSV / 6000 PAR-SE / 4000 NIR / 2000 PAR-SE | Film thickness and refractive index, TSV depth, %Ge in SiGe | Fab to lab | NOT DISCLOSED | "leading semiconductor development labs and HVM facilities" [C] | P046, P047 |
| ContourSP | HDI-PCB and substrate panels | Production (panel, not wafer) | NOT DISCLOSED | none | P051 |

### (d) Other

- **Mask repair and cleaning, from RAVE (2019):** fp-III, nm-VI, Rhazer III, EL-C, Wafer Clean 2200. Production equipment, mask repair about $50M of revenue [S] G063. P029, P060, P061.
- **Microanalysis for failure analysis:** QUANTAX EDS/WDS/EBSD, eWARP TKD, XFlash FlatQUAD 2L (both launched 2026-08-03), M4 TORNADO micro-XRF, HYPERION II. Lab instruments [F] P056, P057, S068.
- **Company-level claims [C]:**
  - "75% of the world's top 25 semiconductor manufacturers rely on Bruker instrumentation" (P001).
  - "#1 Inline AFM, XRD, µXRF, and XRDI ... over 1000 semiconductor metrology tools installed" (P003). No source or year is given for either.
- **What the CFO says the business is:** three technologies, X-ray, automated AFM and WLI [S] G065. 10-K FY2025: the Nano Surfaces and Metrology division "manufactures and markets automated X-ray metrology, automated AFM defect-detection, and photomask repair and cleaning equipment" [F] S028.

## Q2. Size: every semiconductor metrology disclosure, 2023 to Q3 FY2026

Bruker gives **no** semiconductor metrology figure in any 10-K or 10-Q, only qualitative attributions [I] G082. All figures come from earnings decks [F] or third-party call transcripts [S].

| Date | Source | Period (calendar) | Disclosure | Tag | Id |
|---|---|---|---|---|---|
| 2023-11-09 / 2024-02-29 | 10-Q Q3-23, 10-K FY2023 | 2023 | BSI NANO growth partly from semiconductor metrology demand; no figure | [F] | S002, S003 |
| 2024-05-17 | Investor webinar p5 | FY2023 (Jan-Dec 2023) | Semi-Metrology = 9% of BSI revenue | [F] | S006 |
| 2025-02-13 | Q4-24 deck p8 | Q4 FY2024 (Oct-Dec 2024) / FY2024 | Organic revenue growth >20% in Q4-24, low-teens in FY24; >$250M annual revenue; margins "well above corporate average" | [F] / [C] | S012-S015 |
| 2025-02-13 | Q4-24 call | FY2024 | ">$125M" AI/HPC-related; total >$250M, "about half" AI/HPC (≈50%, calc/semi_mix_calc.py) | [S] | G050, G051 |
| 2025-06-24 | Release | 2025 | 27 optical metrology systems ordered by one manufacturer | [F] | S017 |
| 2025-11-03 | Q3-25 deck p7; call | 9M FY2025 | "Softness in X-Ray Semi"; semi "approaching or around $300M"; "flattish this year" | [F]; [S] | S019-S021 |
| 2026-01-12 | JPM 2026 deck p14 | TTM to Q3-25 (Oct 2024-Sep 2025) | **>$300M revenue, >25% EBIT margin** | [F] | S022, S023 |
| 2026-01-12 | JPM 2026 deck p3 | FY2024 | Semi-Metrology = 9% of BSI revenue | [F] | S016 |
| 2026-02-12 | Q4-25 release p1; deck p7, p9 | Q4 FY2025 / FY2025 | Better semi orders helped BSI book-to-bill exceed 1.0; **FY2025 semi revenue flat**; strong Q4-25 orders; Semi-Metrology = 9% of FY2025 BSI revenue | [F] | S024-S026 |
| 2026-02-12 | Q4-25 call | FY2026 outlook | Semi revenue guided "up low-single-digits" | [S] | S027 |
| 2026-05-06 | Q1-26 call; deck p6; release | Q1 FY2026 (Jan-Mar 2026) | ">$300M annual revenue business"; organic bookings >20%; only "some" of the Q4-25 pushout recaptured; HBM and advanced-packaging orders strong | [S]; [F] | S031-S036 |
| 2026-05-07 | 10-Q Q1-26 MD&A | Q1 FY2026 | BSI NANO decline "partly offset by higher revenue from the semiconductor market" | [F] | G020 |
| 2026-06-04 | Jefferies conference (CFO) | mid-2026 | ~$300M: ~$200M production QA/QC (≈67%), ~$50M R&D, ~$50M mask repair; $10-15M of the $40M Q4-25 pushout recaptured in Q1-26 (25-38%); capacity to "at least double" by end-2026 | [S] | G060-G066 |
| 2026-08-04 | Q2-26 deck p8 ("Bruker NANO Semiconductor Metrology") | H1 FY2026 (Jan-Jun 2026) | **>30% organic order growth, >15% organic revenue growth, ~30% EBIT margin** | [F] | S037, S038 |
| 2026-08-04 | Q2-26 call | Q2 FY2026 (Apr-Jun 2026) | Semi orders >50% organic; lead times 9-24 months; ~$20M of revenue moves from Q3 to Q4 | [S] | S039-S041 |
| 2026-08-05 | 10-Q Q2-26 MD&A | Q2 / H1 FY2026 | Group organic growth helped by "stronger semiconductor demand"; BSI NANO revenue "remained consistent" | [F] | G030-G033 |
| 2026-11-04 | Q3-26 call | 9M FY2026 (Jan-Sep 2026) | ">30% organic bookings growth in BSI semicon metrology markets" ("year to date ... in the quarter"); Q3 semi revenue "down double digits" (pushouts); orders convert "mostly in fiscal year 2027 and some in fiscal year 2028" | [S] | S045-S047 |
| 2026-11-04 | Q3-26 deck p7; release | 9M FY2026 | "Strong Semi ... revenues" year to date; "Strong AI-driven orders for memory and advanced packaging"; no figure | [F] / [C] | S051, S052 |

**EBIT margin, one-off items:** the two disclosed margins are >25% (TTM to Q3-25) and ~30% (H1-26). Bruker does not define the EBIT basis and names no one-off items for either margin. A figure excluding one-offs is therefore NOT DISCLOSED (read: JPM 2026 deck p14; Q2-26 deck p8).

**Never disclosed:** semi revenue in dollars for any single quarter; bookings or backlog in dollars; semi book-to-bill; semi gross margin; China share of semi revenue. See gaps.md.

**Segment holding it after July 2026:** BSI NANO (Bruker Nano group), unchanged [F] G002.
- Within NANO, the Nano Surfaces and Metrology division makes the X-ray and AFM tools [F] S028.
- The BSI NANO restructuring plan includes a "merger of divisions within the segment". The divisions are not named [F] G012. The only named merger is Cellular Analysis into Spatial Biology [F] G013.

**2026 goodwill impairments, by reporting unit:**

| Quarter | Charge | Reporting unit | Segment | Semi? | Ids |
|---|---|---|---|---|---|
| Q2 FY2026 (Apr-Jun) | $36.5M | BSB (Bruker Spatial Biology, merged with Cellular Analysis 2026-04-01) | BSI NANO | No | S060 |
| Q2 FY2026 | $98.4M (all remaining goodwill) | CST (Chemspeed, formerly Automation) | BSI BioSpin (pre-recast label) | No | S061 |
| Q3 FY2026 (Jul-Sep) | $174.5M (all remaining goodwill) | BSB&CA | BSI NANO | No | G004, G006 |
| 9M FY2026 | $309.4M total; $211.0M of it BSB&CA | | | | S063, G006 |

The units affected by the reorganisation were tested in Q3 and passed. They are not named and no headroom is given, so whether a semiconductor unit was among them is NOT DISCLOSED [F] G007.

## Q3. Bruker versus Rigaku, tool class by tool class

| Class | Bruker (2026) | Rigaku (2026) | Named chipmaker or fab use | Share figure |
|---|---|---|---|---|
| HRXRD | 7300LSI, Sirius-XRD, QCVelox, Delta-X | XTRAIA TF/XD, XD-3300 | IBM Research Albany: Bruker JVX7300LSI inline [F] C003. Fraunhofer IPMS: inline 300 mm XRR/HRXRD tool awarded to **Rigaku** (Oct 2025), lab 300 mm XRD to **Bruker AXS** (Dec 2025) [F] C015-C018. Rigaku XD-3300 "delivered to multiple leading-edge" chipmakers [C] R034 | Bruker "#1 inline XRD", no source or year [C] P003 |
| XRR | Sirius-RF, Sirius-XRD, 7300LSI | XTRAIA MF-2000/3000/3400, CD-3010G | **Kioxia** and Kioxia Iwate to put Rigaku MF-3400 into 3D NAND mass production (Rigaku release 2025-12-04) [C] C005. TSMC chose Jordan Valley JVX6200 XRR for Cu in 2009, before Bruker owned Jordan Valley [S] C001 | none class-specific |
| XRF / µXRF | Sirius-RF, Sirius-FW | WaferX 310, ONYX 3000/3200, XHEMIS EX | Rigaku: first ONYX 3200 to "a major global foundry" [C] R032. Bruker Sirius-FW "TOR on major packaging fabs" [C] P059 | Bruker "#1 inline µXRF" [C] P003 |
| TXRF / VPD-TXRF | no wafer-fab TXRF listed | TXRF 3760, 310Fab, XHEMIS TX-2000/3000/3000V | none named | Rigaku "overwhelming market share" in TXRF, no % [C] R015 |
| X-ray CD (CD-SAXS) | none in 2026 (XCD shown 2022) | XTRAIA CD-3200T (2020), CD-3010G; with Onto Ai Diffract | **Samsung Electronics** slides co-authored with Onto and Rigaku on X-ray CD for deep V-NAND (2026-03-18) [F] R048. Onto: offering "selected by two key customers", "systems delivered for advanced V-NAND and DRAM" [C] R004, R006 | Rigaku 2030 SAM targets [C] R019 |
| X-ray imaging, packaging | none (XRDI defect tools only) | XHENA AX-3000 at customer evaluation [S] R030 | none | Rigaku targets >30% of a $300M AXI SAM by 2030 [C] R019 |

**Market-share figures** (all are Rigaku quoting Yole; Bruker gives no X-ray share):

| Year | Rigaku share | Market | Source document | Yole edition | Tag | Id |
|---|---|---|---|---|---|---|
| 2022 | 26.9% | n/a | Rigaku IPO filing, EDINET 2024-09-20 | Q2 2024 | [C] | M001 |
| 2023 | 29.5% | $481M | Same | Q2 2024 | [C] | M001, M002 |
| 2023 | 30% ("Company A" 24%, others 46%) | n/a | Rigaku mid-term plan, Feb 2025 | Q4 2024 | [C] | R011 |
| 2024 | 38% | ~$498M | Rigaku annual securities report FY2025 | Q4 2025 | [C] | R012, R013 |

Notes on these figures:
- **"Company A" is not identified.** Nova also sells X-ray metrology (VeraFlex XPS + XRF) [F] M009, so Company A cannot be assumed to be Bruker [I] M007.
- **Implied Rigaku X-ray metrology revenue:** about $142M in 2023 and $189M in 2024 [I, Low] M006 (calc/M_calc.py).
- **Bruker's 10-Ks for FY2023-FY2025 name Rigaku and Park Systems** among BSI NANO competitors, but not KLA, Onto or Nova [F] G041-G043.
- **No rival filing names Bruker or Rigaku as a competitor.** Onto's 10-K names KLA, Nova and Camtek; Nova's 20-F names Onto and KLA; KLA's annual report names neither [F] M008, M010, M011.
- **Supplier awards:** neither Bruker nor Rigaku appears in the award lists read: Intel SCQI 2011-2015 and 2020, Intel EPIC 2022, Micron 2025-2026 [F], TSMC 2021 [S] (C027-C035).

## Q4. Hybrid bonding: pre-bond Cu recess and roughness

**Bruker tools at chipmakers:**
- No saved document names a chipmaker (TSMC, Intel, Samsung, SK hynix, Micron, YMTC, Sony) that uses a Bruker AFM, AFP or WLI for pre-bond Cu recess or roughness [I] H081, C036.
- Bruker's own claims are unnamed [C]:
  - AN5001 covers 1-5 nm recess and calls AFM "indispensable" (H001-H005).
  - The 10-K says automated AFM is "used in the production of High Bandwidth Memory" (P039).
  - A hybrid-bonding package for InSight AFP was introduced at a webinar on 2024-12-04 (H007).

**Named research fabs using Bruker [F]:**
- **Fraunhofer IZM** awarded an in-line 300 mm AFM for pre-bond roughness and dishing (hybrid and direct bonding) to Bruker France, 2025-08 (C019, C020).
- **A*STAR IME** measured Cu dishing with a Bruker InSight CAP (Commun. Eng. 2026) (H010, H011).
- **ITRI/NYCU** used a Bruker Innova on 12-inch W2W wafers (H014); **NYCU** used a Dimension Icon (H015).

**Named chipmaker links to other vendors:**
- **Intel:** samples measured at NIST with an Oxford/Asylum Vero AFM [F] H012, H013. Intel also bought 6 Park NX-Hybrid WLI units, use not stated [S] H030.
- **SK hynix** released Infinitesima Metron3D in-line AFM for DRAM volume production [C] H040.
- **IBM Research** with Nova: Cu-recess scatterometry trained on AFM reference data [F] H018-H021.

**Competing tools:**

| Vendor | Tool | Hybrid-bonding claim | Adoption evidence | Tag | Ids |
|---|---|---|---|---|---|
| Park Systems | NX-Wafer, NX-Hybrid WLI, FX | "No practical solution other than AFM" | Intel 6 NX-Hybrid WLI [S]; Taiwan "T company" AFMs [S]; 2-year imec project [C] | [S]/[C] | H030-H038 |
| KLA | no tool tied to Cu recess in saved documents | FY25: >$925M advanced-packaging process-control revenue; hybrid bonding not mentioned | NOT DISCLOSED | [C] | H063 |
| Nova | Prism (spectral interferometry + OCD), VTS-ML | Inline Cu recess with "reduce[d] reliance on reference data" | IBM Research co-authored SPIE 2026 paper | [F]/[C] | H018-H021, H050-H052 |
| Onto Innovation | OCD for Cu recess; Dragonfly G5 + 3Di | OCD "strong correlation to AFM", suited to HVM | One HBM maker: "double-digit" G5 + 3Di commitments for HBM4 (inspection, not recess) | [C] | H053-H056 |
| Infinitesima, Nearfield, Camtek (Hawk) | in-line AFM, QUADRA, inspection | | SK hynix (Infinitesima) [C]; imec (Nearfield) [S]; >$50M Hawk orders, unnamed [C] | | H040-H042, H062 |

**Tool counts per line:** NOT DISCLOSED in anything read (H070). The only proxies are Intel's 6-unit Park purchase [S] and Onto's "double-digit" G5 order [C], and neither is a per-line ratio.

## Q5. Bruker's reaction to the Onto-Rigaku alliance (since 2026-04-20)

Two searches each found **nothing**: no partnership, acquisition, investment or fab product launch in X-ray or hybrid metrology, and no Bruker remark on Onto, Rigaku or X-ray competition [I] Q013, Q014, S notes. What was read:
- Q1, Q2 and Q3 FY2026 call transcripts, decks and releases.
- Q1, Q2 and Q3 FY2026 10-Qs.
- The four 8-Ks filed Aug-Nov 2026.
- The bruker.com sitemap: 28 news items in 2026, none relevant.

Closest items:
- **Q2-26 deck slide 8:** "AAFM, WLI, and X-ray metrology required" for HBM, CoWoS and AI logic [C] S067.
- **2026 acquisitions:** Tofwerk (Jan 6) and Mimetas (Aug 7), both in BSI BIOS, plus a minority stake in Atinary. None is semiconductor X-ray [F] Q010-Q012.
- **Bruker's "hybrid analysis" (FCMN, Mar 2026)** is X-ray only: XRR + HRXRD fitted together on Sirius-XRD. There is no optical/X-ray data fusion of the Onto-Rigaku kind [F] Q001.
- **Bruker staff quoted in trade press after April 2026** on X-ray roadmaps: new X-ray sources for patterned targets, sub-angstrom specs, XRDI at ~20 wafers/hour [S] Q006-Q008.

---

# Module B (semiconductor business only)

## B1. Disputed-claims ledger

| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| (a) Semiconductor metrology bookings grew more than 30% in the first nine months of 2026 | User prompt. Closest source: CEO, Q3-26 call, 2026-11-04 (S045) | CEO: "year to date ... greater than 30% organic bookings growth in BSI semicon metrology markets" (S045). H1-26 deck: ">30% Organic Order Growth" (S037). Q2-26 semi orders >50% (S039). Q3 BSI orders "driven by strong growth in semi" (call) | The 9M figure appears only in a third-party transcript, and the sentence ends "in the quarter", so the period is unclear (S045). The Q3 deck and release give no figure (S051, S052). The 10-Qs give no semi bookings at all (G082). The Q3 BSI order book was up only low-single-digit (call) | For: [F] for H1 only (S037); [S] for 9M (S045). Against: [I] (ambiguity, G082) |
| (b) Bruker leads X-ray metrology in logic fabs and Rigaku leads in memory | User prompt. No source found in filings, releases, papers or trade press (R notes §3) | Samsung memory unit co-presented X-ray CD with Rigaku and Onto (R048). Kioxia putting Rigaku MF-3400 into 3D NAND production (C005). Rigaku's 9M FY2025 memory revenue rose to ¥3.6bn from ¥1.1bn while logic fell to ¥3.9bn from ¥5.5bn (R040, R041). Bruker cites "logic chip foundries" first among AI needs (Q3-26 call) and its 2016-17 releases cite logic/foundry customers (P009, R061) | Rigaku's FY2024 semi revenue was logic-heavy: logic/foundry 35% vs memory 10% (R042). Rigaku claims a "major foundry" and a "major logic manufacturer" (R032, R037). Bruker's 2026 orders strength is "memory and advanced packaging" (S051, R063). Fraunhofer's inline 300 mm XRR went to Rigaku (C016). Neither vendor, nor Yole as relayed by Rigaku, gives share by fab type | For: [F] R048, R040; [C] C005. Against: [F] R042, C016; [C] R063 |
| (c) AFM remains the reference method for pre-bond copper recess | User prompt. Bruker AN5001 (©2025): "making AFM indispensable" (H003). Adeia: "AFM is the standard method" (H065). Park (H031, H035) | IBM/Nova trained inline scatterometry on AFM reference (H018-H021). imec calibrated in-line SEM to AFM, RMSE 0.42/0.47 nm (H022). Research fabs use AFM for recess (H010-H017). Fraunhofer IZM bought an in-line AFM for pre-bond dishing (C019). Onto validates OCD against AFM (H054) | Onto: AFM's "low throughput and contamination risk limit its applicability in high-volume manufacturing" (H053). Nova: Prism "reduce[s] reliance on reference data" (H050, H051). Adeia: PSI ~1,000x faster than AFM (H066). No SEMI standard or imec position statement found | For: [F] H018-H022, C019. Against: [C] H053, H050 |
| (d) Semi metrology is a ~$300M business at ~30% EBIT margin | Analyst framing on the Q3-26 call. The CEO called it only "directionally correct" (S050) | JPM 2026 deck: TTM to Q3-25 >$300M revenue and >25% EBIT (S022, S023). H1-26: ~30% EBIT (S038). CFO at Jefferies: ~$300M (G060) | FY2025 revenue flat (S025) and Q3-26 revenue down double digits (S047), so LTM to Q3-26 may be below the TTM-Q3-25 level; LTM figure NOT DISCLOSED. EBIT basis undefined; no one-offs named | For: [F] S022, S038. Against: [F] S025; [S] S047 |
| (e) Bruker is #1 in inline AFM, XRD, µXRF and XRDI | Bruker brochure B5000 (2026) (P003) | Bruker's 10-Ks name only Rigaku and Park as relevant competitors (G041). Rigaku's IPO filing calls Park's #1 in industrial automated AFM a goal, not an achievement (M025) | Rigaku claims X-ray metrology leadership: 30% (2023), 38% (2024) (R011, R012, M001). Park claims #1 in AFM overall (M020) and says it overtook Bruker in revenue in 2022 (M023). MarketsandMarkets via KIRS: Park 21.7%, Bruker 15.8% (whole AFM market, 2024) (M014) | For: [C] P003, M025. Against: [C] R012, M020; [S] M014 |
| (f) The Q3-26 semi revenue drop is timing (pushouts), not demand | CFO, Q2-26 call (S041); CEO, Q3-26 call (S047) | ~$20M shift from Q3 to Q4 flagged in August (S041). H1-26 orders >30% (S037). Conversion "mostly in fiscal year 2027" (S046). Capacity to double by end-2026 (G066) | Only 25-38% of the earlier $40M Q4-25 pushout was recaptured in Q1-26 (G064, calc). FY2025 revenue flat (S025) with "Softness in X-Ray Semi" (S019). BSI NANO revenue only "consistent" in H1-26 despite semi growth (G033) | For: [F] S037; [S] S041. Against: [F] S019, S025, G033 |

## B2. Facts that weaken each reading

**The three facts that most weaken the optimistic reading:**
1. Bruker offers no X-ray CD (CD-SAXS) tool in 2026. Meanwhile Samsung's memory unit co-presented X-ray CD for deep V-NAND with Onto and Rigaku (2026-03-18) [F] R048, and Onto says the combined CD-SAXS + Ai Diffract offering was "selected by two key customers" [C] R004.
2. By Rigaku's account, citing Yole, Rigaku held 38% of semiconductor X-ray metrology in 2024, up from 26.9% in 2022 [C] R012, M001. Kioxia is putting Rigaku MF-3400 into 3D NAND mass production [C] C005. In Fraunhofer's 2025 300 mm X-ray tenders, the inline cleanroom tool went to Rigaku and Bruker won only the lab XRD [F] C016, C018.
3. Semi revenue was flat in FY2025, with "Softness in X-Ray Semi" [F] S025, S019. Q3-26 semi revenue fell double digits on pushouts [S] S047. The 10-Qs show BSI NANO revenue only "remained consistent" in H1-26 [F] G033.

**The three facts that most weaken the pessimistic reading:**
1. H1-26 (Jan-Jun 2026): semi metrology orders up >30% and revenue up >15%, both organic, at ~30% EBIT margin [F] S037, S038.
2. One semiconductor manufacturer ordered 27 Bruker optical metrology systems for 2025 [F] S017. Fraunhofer IZM bought a Bruker in-line AFM for hybrid-bonding pre-bond metrology [F] C019, C020.
3. Rigaku's own IPO filing says customers who run competitors' installed tools are hard to win, because of tool-of-record lock-in [C] M005. The CFO says new fabs copy existing tools of record [S] G068. Together these protect an incumbent's installed base.

## B3. Dated catalysts, next 12 months (Dec 2026 - Nov 2027)

| Date | Event | Why it matters | Source / tag |
|---|---|---|---|
| Mid-Feb 2027 (not yet announced) | Bruker Q4 FY2026 results and FY2027 outlook | Whether Q3's ~$20M semi shift lands in Q4; any semi figure for FY2026 bookings or revenue | Precedent: Q4-25 results on 2026-02-12 [F] S024. Date is [I] |
| Late Feb 2027 (expected) | Bruker 10-K FY2026 | Annual goodwill test (Oct 1); any named semi reporting unit; NANO division merger details | [I] from the FY2025 10-K filed 2026-02-27 |
| End of 2026 | Semi capacity "at least double" (CFO target) | Delivery capacity for FY2027 conversion | [S] G066 |
| 2027 (mostly) | Conversion of 2026 semi orders to revenue, "mostly in fiscal year 2027 and some in fiscal year 2028" | Tests claims (a) and (f) | [S] S046 |
| 2026-12 (SEMICON Japan) / 2027-02-21..25 (SPIE Advanced Lithography + Patterning, San Jose) | Possible X-ray CD or hybrid-metrology papers and launches by Bruker, Rigaku and Onto | Q5 watch item; Bruker had SPIE AL 2026 X-ray CD leads | SPIE dates: NOT RETRIEVED (spie.org bot page); search lead only |
| Feb-Mar 2027 | Rigaku FY2026 results and annual securities report | New Yole share figure for 2025; whether MF-3400 sales pass the >JPY 6bn FY2026 forecast | [C] C006; Rigaku FY ends Dec 31 [F] R047 |
| 2027-03-30 .. 04-01 | SEMICON West, Phoenix (moves to spring) | Main North American launch venue | [F] SEMI release |
| ~June 2027 | IEEE ECTC 2027 | Hybrid-bonding metrology papers that would test claim (c) | Date NOT RETRIEVED (ectc.net 403) |
| Group-level items (debt maturities, lock-ups) | Not applicable at business-unit level | | Out of scope |
| Export controls | No dated deadline found. CEO: China restrictions on very high-performance semi equipment "in place for 2-3 years" | | [S] G052; deadline NOT DISCLOSED |

## B4. Gap log
See `gaps.md`.

## B5. Handoff row
See `handoff.md`.

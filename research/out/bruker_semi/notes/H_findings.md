# H — Hybrid-bonding pre-bond metrology: who uses Bruker AFM/AFP, competing tools, "AFM is the reference"

Scope: Cu-Cu / Cu-SiO2 / Cu-SiCN hybrid bonding (W2W, D2W), HBM4/4E, SoIC, 3D NAND CMOS bonding. Research date 2026-11-21.
Evidence rows: `research/out/bruker_semi/parts/H.csv` (H001-H081, 58 rows). `quote_check.py`: 54 FOUND, 4 rows with no quote ([I] / NOT DISCLOSED rows). No rows NOT FOUND.
Sources: `research/sources/bruker_semi/` (Europe PMC XML full texts were converted to tag-free text in `_text/` so quotes can be checked).

## (a) Chipmaker and research-fab usage evidence

| User | Tool vendor + model | Measurement | Source | Tag |
|---|---|---|---|---|
| A*STAR IME (Singapore research fab), W2W Cu/SiO2 | **Bruker InSight CAP** (automated AFM) | Post-CMP Cu dishing (7 ± 3.4 nm baseline; ~1.4 ± 0.5 nm with passivation), roughness | Cheemalamarri et al., Commun. Eng. 2026 (H010, H011) | [F] |
| NYCU + ITRI (Taiwan), 12-inch W2W Cu/SiO2 | **Bruker Innova** AFM | Cu (nt-Cu via) roughness Rq | Ong et al., Materials 2022 (H014) | [F] |
| NYCU (Taiwan) | **Bruker Dimension Icon** | Pre-bond Cu roughness | Lu et al., Materials 2024 (H015) | [F] |
| Intel (samples, Intel APTM co-authors) measured at NIST | **Oxford Instruments / Asylum Research Vero** (not Bruker) | Topography and nanomechanics of HB-ready Cu pads | Alderete et al., ACS Appl. Nano Mater. 2025 (H012, H013) | [F] |
| KAIST (Korea), Cu/polymer HB | **Park Systems NX10** | Roughness, dishing | Adv. Sci. 2025 (H016) | [F] |
| imec, 300 mm Cu-SiCN W2W | AFM, vendor NOT DISCLOSED | Statistical Cu step height (recess/protrusion) | Inoue et al., IEEE EDL 2021 (H017) | [F] |
| IBM Research Albany (+ Nova) | AFM as reference, vendor NOT DISCLOSED; Nova VTS-ML scatterometry for inline use | Cu recess, 15 training wafers x 5 dies, ~4 nm range; blind test R2 ~0.8 | Timoney et al., SPIE 2026 (H018-H021) | [F] |
| imec (ESTC 2024, via review) | In-line SEM (directional BSE) calibrated to AFM reference | Cu pad height, RMSE 0.42 / 0.47 nm | Micromachines 2026 review (H022); original paper NOT RETRIEVED | [F] (as reported in review) |
| 3D NAND Xtacking (YMTC's scheme) | Pattern-centric inline AFM, vendor not named | VIA dishing | Micromachines 2026 review (H024); JoMM 2019 original NOT RETRIEVED | [F] (as reported in review) |
| Sandia (DBI R&D) | AFM, vendor NOT DISCLOSED | SiO2 roughness, Cu recess | OSTI 1640140 slides (H025) | [F] |
| SK hynix | **Infinitesima Metron3D** in-line AFM released for volume production (DRAM; the HBM link is only in press) | "3D process control" | Infinitesima release via Quality Magazine (H040); Bits&Chips (H041) | [C] / [S] |
| Intel | **Park NX-Hybrid WLI**, 6 units in one purchase (use not specified) | not stated | greened.kr, Park official (H030) | [S] |
| "Taiwan T company" (unnamed) | Park, several AFMs for advanced packaging | not stated | ddaily.co.kr CEO interview (H034) | [S] |
| Unnamed chipmakers | Park test tools supplied, talks under way | hybrid bonding | technews.tw, Park EVP (H033) | [S] |

What this shows: in the documents saved, Bruker AFMs appear in research-fab and university methods sections (A*STAR IME InSight CAP, ITRI/NYCU Innova, Dimension Icon). No saved document names a chipmaker (TSMC, Samsung, SK hynix, Micron, YMTC, Sony, Intel) that uses Bruker AFM, AFP or WLI for pre-bond Cu recess or roughness [I] (H081). The only chipmaker-linked AFM methods section found uses an Asylum Vero (Intel samples at NIST). For Park and Infinitesima, the chipmaker links come from press relays or vendor releases.

## (b) Competing tools

| Vendor | Tool | Claimed hybrid-bonding use | Adoption evidence | Tag |
|---|---|---|---|---|
| Bruker | InSight 300 AFM, InSight AFP (hybrid-bonding package, LAS, ERO) | Cu pad recess (1-5 nm), roughness, defects, mm-scale topography, bevel ERO >45 WPH | No named customer. AN5001 reports a 25 nm to 15 nm topography reduction at an unnamed fab. Webinar dated 2024-12-04 (H001-H007) | [C] |
| Park Systems | NX-Wafer, NX-Hybrid WLI (AFM + WLI/PSI), FX large-sample, NX-TSH | "No practical solution other than AFM" for HB. HBM4 specs being tuned with customers | Intel 6x NX-Hybrid WLI [S]. "T company" AFMs [S]. imec 2-year JDP (2026-06-10) [C] (H030-H038) | [S]/[C] |
| Infinitesima | Metron3D (RPM, 10-100x AFM throughput claim) | In-line 3D process control | SK hynix released it for volume production, per Infinitesima (H040) | [C] |
| Nearfield Instruments | QUADRA | Cu pad and dielectric roughness, erosion, dishing, ERO | Tool being deployed at imec under a multi-year project (H042) | [S] |
| Nova | Prism (spectral interferometry + OCD), VTS-ML; WMC (bow/warp); edge metrology | Post-CMP Cu recess/dishing inline, with less need for reference data | IBM Research co-authored SPIE 2026 paper. Micron co-developed the edge-CMP paper (H018-H021, H050-H052) | [F]/[C] |
| Onto Innovation | OCD for Cu recess; Dragonfly G5 + 3Di; EchoScan (voids) | OCD gives "strong correlation to AFM" and suits HVM. G5 illumination targets CMP and hybrid-bonding defects | HBM maker made double-digit G5/3Di commitments for HBM4 2D inspection, displacing the incumbent tool of record (H053-H056, H061) | [C] |
| KLA | Advanced-packaging portfolio (no saved doc names a hybrid-bond recess tool) | FY25 ARS: AP process control >$925M. Hybrid bonding not mentioned | NOT DISCLOSED (H063). SemiEngineering lists KLA among WLI/PSI suppliers [S] (H058) | [C]/[S] |
| Camtek | Hawk (not Eagle G5) | Inspection and 3D measurement for HBM, chiplet, hybrid bonding | >$50M initial Hawk orders, customers unnamed (2024-11-29) (H062) | [C] |
| Zygo | WLI/PSI | Cu recess (journalist listing) | none found (H058) | [S] |
| Adeia (IP licensor) | Calibrated PSI method | ~1,000x AFM throughput for metal recess | ECTC 2024 paper NOT RETRIEVED (H065-H067) | [C]/[S] |
| Rigaku | X-ray metrology | "Compatible with" hybrid bonding. No recess claim | none (H064) | [C] |
| Samsung + PSI | CDI (X-ray coherent diffraction) simulations | Cu pad recess estimation | Simulation only (H068) | [S] |

## (c) Tool counts per line

NOT DISCLOSED (read: Bruker AN5001, InSight 300 page, webinar AF324; Onto Dragonfly G5 release 2026-03-16; Camtek Hawk release 2024-11-29; Infinitesima release 2025-07-08; greened.kr 2025-12-22; ddaily 2025-04-14; SemiEngineering 2026-11-10; KLA FY25 ARS). No source states AFMs per HBM or hybrid-bonding line, or tools per 10k wafer starts. Two proxies were found, and neither is a per-line ratio:
- Intel bought 6 Park NX-Hybrid WLI units in one purchase. This is [S], relayed from a Park official, and the use is not stated (H030).
- One HBM maker made "double-digit" Dragonfly G5 commitments for 2D inspection, plus a similar number of 3Di. This is [C], and these are inspection and bump-metrology tools, not recess metrology (H055).

## (d) "AFM remains the reference method for pre-bond copper recess"

| Side | Who, when | Evidence | Tag |
|---|---|---|---|
| For | Bruker (S. Hand, P. De Wolf), AN5001 ©2025 | "making AFM indispensable" for 1-5 nm recess verification (H003) | [C] |
| For | IBM Research + Nova, SPIE 2026 | AFM chosen as the high-resolution reference used to train inline VTS-ML. Blind-test correlation is reported against AFM (H018-H021) | [F] |
| For | imec (Altintas et al., ESTC 2024), via Micromachines 2026 review | In-line SEM height index calibrated to AFM reference measurements (H022) | [F] (as reported in review) |
| For | Onto Innovation case-study page; Onto staff in SemiEngineering 2026-11-10 | OCD validated by "strong correlation to AFM". Cu pad topography "typically characterized using AFM" (H054, H057, H059) | [C]/[S] |
| For | Adeia authors, 3D InCites 2024-05-21; Adeia blog 2024-07-08 | "AFM is the standard method to measure Cu recess" (H065, H067) | [S]/[C] |
| For | Park Systems (CEO 2025-04; official 2025-12) | Says non-AFM tools cannot measure Cu pad height variation (H031, H035) | [S] |
| For | Research fabs and universities (A*STAR IME, imec, ITRI/NYCU, Sandia, KAIST) | Methods sections use AFM for recess, dishing and roughness (H010-H017, H025) | [F] |
| Against (inline/HVM role) | Onto case-study page | AFM's "low throughput and contamination risk limit its applicability in high-volume manufacturing". OCD is positioned for HVM (H053) | [C] |
| Against | Nova blog 2025-08-03 | Prism SI+OCD for Cu recess "reduce[s] reliance on reference data" (H050, H051) | [C] |
| Against | Adeia 2024 | PSI is ~1,000x faster than AFM. An 80x80 µm AFM image takes ~5 min (H066, H067) | [S]/[C] |
| Against | SemiEngineering 2026-11-10 (Onto's M. Wu) | WLI/PSI and OCD are also used to measure recess (H057, H058) | [S] |
| Nuance | Bruker AN5001 itself | Local AFM showed recess in spec while mm-scale topography was out of spec. Bruker pushes AFP (profilometry) rather than AFM alone (H004) | [C] |

[I] (H080, confidence Medium): the claim holds for AFM as the reference and calibration method. Every optical or SEM recess method found (IBM/Nova VTS-ML, imec SEM-BSE, Onto OCD, Adeia PSI) is validated against AFM. The claim is contested for inline HVM monitoring, where vendors of optical tools position OCD, VTS, PSI or SEM as the production tool and AFM as the sampled reference. No SEMI standard or imec position statement on this was found. NOT RETRIEVED: imec-publications.be (connection reset), IEEE Xplore originals.

## (e) Gaps, NOT DISCLOSED / NOT RETRIEVED, premise errors

NOT DISCLOSED
- AFM vendor/model in: IBM/Nova SPIE 2026 paper; imec IEEE EDL 2021 (Inoue et al.); Sandia OSTI 1640140 (each read in full).
- Bruker customer names, hybrid-bonding orders and launch press release (read: AN5001, InSight 300 page, webinar AF324 page; web search found no release).
- KLA hybrid-bonding metrology product or revenue (read: KLA FY25 ARS; "hybrid" appears only on p33, about remote work).
- Customer names for Park hybrid-bonding work (greened.kr: Park declined to name them). Camtek Hawk customers. The HBM maker in Onto's G5 release.
- Tool counts per line (see c).

NOT RETRIEVED
- imec-publications.be records for Altintas et al. and Chew et al. (ESTC 2024): connection reset by peer.
- DOAJ record for YMTC Xtacking AFM paper (JoMM 2019): 403. SPIE 10962 original: paywalled, not attempted.
- semi.org KLA SEMI 2021 deck (Donzella): 403. semicontaiwan.org Nova 2026 PDF: 403.
- KLA Kronos 1190 release PDF and Zeta-6xx datasheet: server returned HTML, not PDF. KLA advanced-packaging page: JS-rendered, no text.
- businesswire Onto 2025-01-14 release (EchoScan/3Di): connection failed (http 000). investors.ontoinnovation.com not attempted (known 403).
- ECS JSS acec9b (IOP): 403. NIST PMC page (pmc.ncbi): browser check, so the Europe PMC full text was used instead.
- researcher.ibm.com "AFM assisted hybrid bonding interface optimization": 404.
- Meritz research PDF (2026-04-01): connection failed.
- Adeia ECTC 2023/2024 papers; Niazi et al. ECTC 2023 (OCD for pad recess): IEEE paywall, not retrieved.
- Lasertec: not researched (time). Consensus search unavailable (free monthly quota exhausted). Firecrawl search credits exhausted mid-session.

Premise errors and corrections
- "Camtek Eagle G5 for hybrid bonding": Camtek positions **Hawk**, not Eagle G5, for hybrid bonding. The saved Eagle G5 launch release (2024-09-24) does not mention hybrid bonding.
- "Nova Elipson for Cu recess": the saved Nova material names **Prism** (spectral interferometry + OCD) and VTS-ML for Cu recess. Elipson does not appear in it.
- "Onto Dragonfly 3Di for Cu recess": 3Di is presented as bump/3D metrology for HBM. Onto's Cu-recess claim is **OCD**. The G5 hybrid-bonding claim is about defect inspection.
- "KLA Candela/Zeta for hybrid-bond recess": no saved KLA document ties Candela or Zeta to hybrid-bond Cu recess. SemiEngineering only lists KLA among WLI/PSI suppliers [S].
- Park "NX-Hybrid WLI" means AFM + white-light interferometer hybrid. The name does not refer to hybrid bonding, and its 2021 launch release does not mention hybrid bonding.
- The SemiEngineering-hosted blog "Process Control For Hybrid Bonding..." (2026-10-08) is by **Onto** (Yong Gao), not KLA. The file was renamed to `2026-10-08_onto-semiengineering_...`.
- Infinitesima at SK hynix: the company release says DRAM volume production. The HBM-packaging framing appears only in Bits&Chips [S].
- File dates: eight auto-dated files were renamed to their publication dates and the manifest was updated (note "renamed by H agent").

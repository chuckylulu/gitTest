# Dossier: what chipmakers say they use to inspect and measure HBM stacks and hybrid-bonded interfaces

Run: 21 November 2026. Period covered: 1 January 2025 to 21 November 2026. Companies: SK hynix, Samsung Electronics, Micron, TSMC, Intel, ASE (incl. SPIL), Amkor. Modules A and B of the rules do not apply (user instruction).
Fiscal year-end: not applicable. No financial figures are used; every item is a technical statement dated by calendar month, so `period_fiscal` is `n/a` throughout.
Evidence: `evidence.csv` ({{N_ROWS}} rows: {{TAG_COUNTS}}). Every claim below carries one tag and the evidence ids that support it. Gap log: `gaps.md`. Method and access log: `run_log.md`. Scripts: `calc/`.

How to read the tags here: [F] = read in a saved primary document (for conference papers almost always the **abstract only**, because ieeexplore.ieee.org, spiedigitallibrary.org and dl.asminternational.org refuse scripted access); [C] = the company's own untestable claim; [S] = press or trade site; [I] = my inference, with inputs in `evidence.csv`.

## 0. Premise check: corrections to the prompt

1. **The rules block.** On this branch `research/CLAUDE.md` held only a TODO placeholder. The filled-in rules (with Modules A and B and the tag scheme) were on branch `ccr-2b9561fc-mqqdg4` and were copied over unchanged, with the tools. `prior/` is empty, so the premise check covers the prompt only. [I] MAIN-002
2. **"TSMC advanced-packaging metrology keynote at SEMICON Taiwan, September 2026."** It happened, but as the keynote of one forum, not a show keynote. The forum is the Semiconductor Advanced Inspection and Metrology Forum, on 4 September 2026 (slot from search snippets only). The speaker is Zhihua Zou of TSMC per a DIGITIMES photo caption [S] XR-014. The title, "Challenges and Opportunities for Metrology and Inspection of Advanced Packaging", comes from link text on a press page [S] XR-016. **The published abstract is NOT RETRIEVED**: semicontaiwan.org refuses scripts, and no copy was found elsewhere. Section 2.2 keeps abstract, snippet leads and press paraphrase apart. [I] XR-037
3. **"Hybrid-bonded HBM" as a current product.** Neither memory maker says its HBM is hybrid-bonded today. SK hynix's own August 2026 tech note says die-to-wafer hybrid bonding for HBM is "progressing toward commercialization" [F] TALK-014. Samsung's HBM page says it is "preparing to adopt" hybrid copper bonding [C] TALK-034. Inspection statements about hybrid-bonded HBM are therefore development statements. Production statements about hybrid bonding exist only for wafer-to-wafer V-NAND (Samsung, Section 1) and outside memory.
4. **TSMC SoIC and Intel Foveros Direct.** Intel's 100% bond-overlay paper describes chip-to-wafer hybrid-bonding metrology "at Intel" but does not name Foveros Direct [F] PAPL-059. No in-period TSMC document read names an SoIC inspection or sampling method. TSMC's SoIC-CS paper shows only daisy-chain results [F] PAPL-010.
5. **Award events.**
   - TSMC's 2025 Excellent Performance Awards were presented on 25 Nov 2025, not in December [S] AW-001. The 2026 awards have already been given, on 17 Nov 2026 [S] AW-011.
   - Samsung's semiconductor award event is the "DS 상생협력 Day". "Best Partner Award" is SK hynix's term [F] AW-033, AW-040.
   - SPIL has no separate supplier award. ASE Holdings runs one ceremony for ASE, SPIL and USI [S] AW-055.
6. **X-ray dose.** No chipmaker document in the period gives a dose limit or failure dose for HBM. The only chipmaker dose numbers are Intel's, for on-package DRAM (not HBM). They come from an October 2024 SMTA paper that SMT007 Magazine republished in April 2025; that republication is the only reason the item falls in the period [F] XR-001 to XR-003, XR-027.
7. **Venues.**
   - ECTC's own site, SEMICON forum pages (semi.org, semicontaiwan.org, semiconkorea.org) and SPIE paper pages refuse scripted access. Papers were therefore found through Crossref volume listings, which carry affiliations for IEEE and ASM records, and Semantic Scholar abstracts.
   - SPIE records carry no affiliations. A SPIE paper is attributed to a company only where its abstract names the company; otherwise the attribution is [I].
   - IITC 2026 and IPFA 2026 are not yet in Crossref. The IITC 2026 programme was read directly and has no in-scope paper by the seven [F] MAIN-004.
8. **Company names.** "HANA Micron", a Korean OSAT, is not Micron Technology; five papers were dropped from the inventory for this reason. Samsung Electro-Mechanics and Samsung Display are separate companies and are excluded. [I] MAIN-003

## Bottom line

- **What the seven name for HBM and bonded stacks is mostly electrical test and acoustic microscopy, and mostly on test vehicles.** In conference abstracts and full texts from 2025-26, the methods named most often for HBM stacks, TSVs, micro-bumps and bonded interfaces are:
  - electrical test: daisy chains, interface resistance and leakage;
  - scanning acoustic microscopy (C-SAM / SAT / cSAM): SK hynix HBM4 test vehicle; Micron wafer-to-wafer bonding; Intel chip-to-wafer hybrid bonding; Amkor 2.5D test vehicle.
  The status words are "test vehicle", "feasible", "demonstrated" or "examined". [I] SYN rows, Section 5
- **Production wording for an HBM-line inspection or measurement step appears only three times:**
  - Samsung pre-screens buffer-die micro-bump interface resistance "in mass production" [F] PAPM-049.
  - SK hynix's optimised TSV-film process, with its IR inspection and FIB cross-section checks, was "successfully applied in mass production" [F] PAPM-222.
  - SK hynix's in-line optical chip-warpage method for HBM is a "commercialized solution currently in use" [C] PAPM-201.
- **The non-electrical methods for bonded interfaces stay in development, with two exceptions:**
  - Intel's near-infrared post-bond overlay mapping is on a test vehicle [F] PAPL-046.
  - Intel's 100% chip-to-wafer overlay metrology is in development with a roadmap [F] PAPL-059.
  - SK hynix measured post-bond die shift and tilt by IR in a "production-grade MI setup" on actual HBM wafers [F] PAPM-216.
  - Samsung ran in-line AFM on production wafers for V-NAND (not HBM) hybrid bonding [F] SMP-016.
- **No chipmaker states X-ray or laser-acoustic use in production for HBM or hybrid bonds.**
  - X-ray appears as failure-analysis practice (ASE 3D X-ray microscopy [F] PAPL-107; Intel CT and synchrotron work [F] PAPL-067, PAPL-082), as "examined" (Samsung [F] TALK-020), in a patent application (Samsung [F] XR-012) and as a stated concern about memory damage (Intel [F] XR-001; TSMC per press [S] XR-013).
  - Laser-acoustic use at Samsung is reported only by trade press citing industry sources [S] TALK-024.
  - XRF, XRD and CD-SAXS are not named by any of the seven in an in-scope document read. [I] SYN rows
- **X-ray dose: no HBM number from any chipmaker.**
  - Intel exposed on-package DRAM to 350 rad, which it calls three times the DRAM maker's limit, with no functional errors; it warns long-term reliability "may be reduced" [F] XR-002, XR-003.
  - TSMC's 2026 forum keynote reportedly listed "DRAM/HBM damage concern by X-ray" [S] XR-015. Its abstract is NOT RETRIEVED.
- **Sampling intensity.** Direct evidence of more measurements per stack or wafer:
  - Intel's move from "reduced sampling plans" to "100% chiplet inspection" for chip-to-wafer bond overlay [F] SMP-030, SMP-031;
  - Samsung's added mass-production micro-bump pre-screen [F] PAPM-049;
  - Samsung's "massive metrology" for V-NAND hybrid bonding [F] SMP-016.
  Memory makers present virtual metrology as adding coverage to every wafer on top of sparse physical sampling. None says it removed physical measurements [I] SMP-042. No company gives an HBM test-time or insertion count [I] SMP-041.
- **Awards rarely mark HBM or hybrid-bonding inspection.** On the award lists read in full, inspection, metrology and test vendors are about 1 winner in 10 [I] AW-058. No award category read names an HBM or hybrid-bonding product. The one award tied to HBM inspection is Onto Innovation's reported SK hynix 2026 Best Partner Award, which is NOT RETRIEVED (gaps.md).
- **Tool vendors named by the chipmakers themselves:**
  - Hitachi High-Tech IS4100 (Samsung DRAM HVM line) [F] PAPM-225;
  - Nearfield (co-author of Samsung's in-line AFM paper) [F] SMP-016;
  - EV Group (co-author of Intel's 100% overlay paper) [F] PAPL-061;
  - Applied Materials (co-author of Intel's hybrid-bonding CMP paper) [F] PAPL-038;
  - Tokyo Electron (co-author of SK hynix's bond-wave paper) [F] PAPM-144;
  - Gauss Labs (SK hynix virtual metrology) [F] TALK-004;
  - NexSensor and Cobis Technology (SK hynix tool co-development) [F] TALK-009, TALK-012;
  - Thermo Fisher and Hamamatsu (failure-analysis tools) [F] PAPM-095, PAPM-081;
  - PVA TePla (ASE SAM) [F] SMP-037;
  - Comet (Intel CT) [F] XR-023;
  - Akrometrix (reference only) [F] PAPM-204.
  KLA, Onto, Camtek, Nova, Lasertec and Advantest appear as award winners, not in technical texts.

## 1. Evidence table: one row per paper or talk

What is in the table: {{N_DOCS}} documents ({{N_DOCS_INSCOPE}} touch one of the six named process steps). They come from:
- the PAPM, PAPL and TALK module tables;
- eight method-bearing papers found by the X-ray and sampling modules (`calc/section1_extra_rows.csv`).

The table is generated by `calc/build_tables.py`; `calc/section1_table.csv` is the machine-readable copy. Within each company, rows on the six named steps come first.

How to read it:
- Status and limits are the authors' own words, or NOT DISCLOSED with the file read. For IEEE and ASM papers "read" means the abstract (Semantic Scholar or Crossref record), because the full text is NOT RETRIEVED.
- "Tool vendor" is filled only where the document names the tool maker or a co-author is from a tool vendor.
- Every row is tagged. A row tagged [S] is press-only, and a row tagged [I] is attributed to the chipmaker by inference (SPIE records without affiliations).

{{SECTION1_TABLE}}

## 2. X-ray dose and radiation damage

### 2.1 Every chipmaker statement found (in period first; out-of-period context labelled)

| Chipmaker | Document, date | Exact wording | Dose / numbers | Failure mode | Method | Tag, evidence |
|---|---|---|---|---|---|---|
| Intel (all six authors Intel) | SMT007 Magazine, Apr 2025, p48 (republication of SMTA International, Oct 2024) | "The DRAM damage due to irradiation poses a significant challenge to the inspections of BGAs with on-package DRAM" | none in the sentence | damage to on-package DRAM (not HBM) | post-SMT 2D/3D X-ray | [F] XR-001 |
| Intel | same, p54 | "Even after total exposure of 350 rads, MemTest86 gave no errors on the DRAM." | 350 rad (3.5 Gy) total, in 50-rad steps; DOE 120-160 kV, 14.5-20 W, 55-315 s, no filter or Al/Zn/Cu 1.6-4.8 mm; TLD dosimeters | no functional errors | 2D manual X-ray (MXI); 3D automated (AXI) dose also measured | [F] XR-002, XR-005 |
| Intel | same, p54 | "even after overexposure to three times the limit provided by DRAM manufacturer, no infant mortality failures were observed." | "three times the limit"; the limit value and the DRAM maker are not stated (NOT DISCLOSED) | none observed; long-term reliability "may be reduced" | 2D MXI | [F] XR-003 |
| Intel | same, p48 | "the increase in reverse junction leakage is the most probable cause for tref degradation" | none | retention (static refresh time, tref) loss via junction leakage, from the literature the authors cite | n/a | [F] XR-004 |
| Intel (inference) | from XR-003 | - | read literally, the maker's limit is about 117 rad (350 / 3) | - | - | [I] XR-035, Low |
| Micron (co-author with Univ. Padova) | IEEE Trans. Nucl. Sci., Aug 2025, abstract | "Experimental results show that the alpha soft error rate is not significantly affected by previous X-ray irradiation, at least for small doses" | doses "well above those commonly used for printed circuit board inspections"; no values in the abstract | Vt shifts and bit errors in 3D NAND (not DRAM/HBM) | lab X-ray irradiation, then alpha exposure | [F] XR-007, XR-008, XR-009 |
| Micron (adjacent: field radiation, not X-ray inspection) | IRPS, Mar 2026, abstract | "The threshold for total ionizing dose damage from terrestrial usecases is measured and shown to be inconsequential." | value not in the abstract | TID from terrestrial radiation | neutron/alpha tests | [F] XR-010 |
| Samsung | US 2026/0126403 A1 (filed Oct 2025, published May 2026) | "damage and defects that may occur in the object to be inspected due to the X-ray beam can be reduced" | none | unspecified; HBM micro-bump bonding structures named as the target | in-line X-ray laminography / CT with a low-pass filter | [F] XR-011, XR-012 |
| TSMC (press account) | DIGITIMES, 4 Sep 2026 (paywalled teaser and caption) | "TSMC is calling for future HBM and DRAM designs to become more compatible with X-ray inspection" | none visible | "radiation exposure to sensitive memory devices" | X-ray inspection (type not stated) | [S] XR-013, XR-014 |
| TSMC (press about the abstract) | WindowsForum, 5 Sep 2026 | the abstract "explicitly lists 'DRAM/HBM damage concern by X-ray'" | no doses (per the same article) | "DRAM/HBM damage" | not stated | [S] XR-015, XR-018 |
| SK hynix, Amkor | - | no in-period statement found | - | - | - | [I] XR-038 |
| ASE | ICEP-IAAC, Apr 2025, abstract | 3D X-ray used in fan-out failure analysis; no dose or damage wording | n/a | n/a | 3D X-ray | [F] XR-024 |
| OUT OF PERIOD: Intel | SMTA International abstract, Oct 2024 | "the limits to which these DRAMs can be exposed are not clear or readily available" | - | DRAM degradation | post-PCB X-ray | [F] XR-027 |
| OUT OF PERIOD: Samsung | US 10,984,853 B2 (granted 2021) | "the damage of semiconductor memory devices by X-ray is increasing. However, quantifying the X-ray dosage is difficult." | - | Vt-shift leakage, refresh degradation | on-chip BJT dose detector | [F] XR-028 |
| OUT OF PERIOD: Samsung | US 11,217,495 B2 (granted 2022) | "cause various failures, such as degradation of refresh characteristics or a charge loss in the semiconductor chip" | soft X-ray about 0.1-12 keV filtered out; 12-120 keV for imaging | refresh degradation, charge loss | X-ray inspection with an absorption filter | [F] XR-029 |
| OUT OF PERIOD: Intel | US 11,506,709 B2 (granted 2022) | "the radiation used in commercial x-ray equipment may alter the electrical conditions of memory die at gate level, which may potentially induce irreversible damage." | - | gate-level damage; DRAM, SRAM and HBM named | interconnect X-ray inspection with a titanium filter | [F] XR-030 |

Reading of the table:
- **Dose numbers.** The only chipmaker dose numbers in the period are Intel's, for on-package DRAM [I] XR-038.
- **HBM-specific statements.** The only HBM-specific statements are a Samsung patent application with no numbers [F] XR-012 and a TSMC talk known through the press [S] XR-013.
- **"Production constraint."** No document uses that phrase. Intel calls the damage "a significant challenge to the inspections" [F] XR-001.
- **Context from non-chipmakers (not chipmaker statements).**
  - Hanyang University and Radiate (IEEE TNS, Nov 2026) measured DDR4 retention failures after a 130 kV PCB X-ray machine [F] XR-025.
  - An MDPI paper (19 Nov 2026, Hanyang/Radiate/Cisco) gives about 0.46 mGy(Si)/s during PCB 3D CT [F] XR-026. At that rate Intel's 350 rad would take roughly two hours of beam-on time [I] XR-036, Low: the dose quantities differ.
  - Trade press calls dose control "a top-line concern for memory chips" [S] XR-020.

### 2.2 The TSMC SEMICON Taiwan 2026 metrology keynote

**(a) Published abstract (TSMC's own words): NOT RETRIEVED.** The abstract is published only at https://www.semicontaiwan.org/en/node/18506, and semicontaiwan.org returns HTTP 403 / a Cloudflare challenge to scripts. No copy was found on a host that accepts scripts. Nothing from the abstract is quoted here. Pages for the user to save by hand:
- https://www.semicontaiwan.org/en/node/18506 (abstract)
- https://semicontaiwan.org/en/Metrology_2026 (forum agenda)
- https://www.semicontaiwan.org/en/node/17406 (speaker bio)

**(b) What search snippets suggest (leads only, not evidence).**
- The keynote is "Dr. Zhihua Zou, Director, TSMC", "Challenges and Opportunities for Metrology and Inspection of Advanced Packaging".
- It ran on Friday 4 September 2026, 09:45-10:25, as the keynote of the Semiconductor Advanced Inspection and Metrology Forum (chair: I-Shih Tseng, Chroma ATE).
- The bio snippet says Zou directs TSMC's Advanced Packaging Metrology Engineering division (InFO, CoWoS, SoIC metrology). It says he joined TSMC in 2023 after about 18 years at Intel in assembly and test development and about two years as principal engineer on hybrid bonding.
- A snippet repeats that the abstract lists "DRAM/HBM damage concern by X-ray". No snippet shows a dose number.

**(c) Press paraphrase. Every item is [S]; none is TSMC's own wording.**
- DIGITIMES, 4 Sep 2026: TSMC "is calling for future HBM and DRAM designs to become more compatible with X-ray inspection", citing buried defects and "radiation exposure to sensitive memory devices" [S] XR-013. The photo caption names "TSMC's Zhihua Zou" [S] XR-014.
- WindowsForum, 5 Sep 2026: the public abstract "explicitly lists 'DRAM/HBM damage concern by X-ray'" [S] XR-015. The article says the abstract names collaboration with foundry customers, HBM vendors and equipment vendors, and "design for metrology", as opportunities [S] XR-017. It also says no public material gives doses or failure rates [S] XR-018.
- An investor blog (7 Sep 2026) attributes the talk to TSMC's quality-and-reliability team at a closing session. It says TSMC named SK hynix, Samsung and Micron and asked for X-ray markers in HBM dies. No other saved source supports this, and it conflicts with the caption and the slot [S] XR-019.

**Other TSMC talks.**
- At the 3DICAMA launch on 9 September 2025, TSMC VP Jun He put HBM consumption at about 10 million stacks a quarter, so a 1% yield loss is costly [S] XR-034. He called "immediate detection" (第一時間偵測) a baseline requirement [S] TALK-044.
- No TSMC metrology or inspection talk was found at SEMICON Taiwan 2025 [I] MAIN-001.

## 3. Sampling intensity: more or fewer inspection and metrology steps

### 3.1 HBM (memory makers, OSAT context)

- **SK hynix: test insertions are visible, but there are no counts.**
  - Press reports an in-house HBM4 package-level (system-level) tester that passed internal qualification in January 2026, moving a post-integration test to the memory maker [S] SMP-009, SMP-010.
  - SK hynix's Hot Chips 2026 slides show a KGSD (known-good stacked die) wafer test before system-level packaging [S] SMP-011.
- **Samsung: one item added.**
  - Samsung adds a mass-production pre-screen of buffer-die micro-bump interface resistance, calling it "an essential quality monitoring item for buffer die" [F] SMP-014, PAPM-049.
  - Samsung's EDS test group names "the rising test cost of high-density HBM and DRAM products" [F] SMP-015.
  - A 2026 Samsung interview describes a new non-destructive red-light monitoring solution against HBM stacking damage, with no sampling numbers [F] SMP-013.
- **SK hynix warpage: from destructive sampling to all chips.** SK hynix replaced destructive warpage sampling (a sample "far too small") with in-line measurement of all chips on a wafer, at about 7-10 minutes for 600 chips [F] PAPM-206, PAPM-208.
- **Amkor: more insertions, by its own offer and its executive's words.**
  - Amkor offers "in-situ test between key assembly steps and final test (SLT and ATE) for 2.5D & 3D" [F] SMP-038.
  - Its test VP says intermediate HBM testing "is becoming increasingly critical" [S] SMP-039.
  - An unattributed figure of 3 to 12 test insertions for a 12-high stack appears in trade press [S] SMP-040.
- **Micron.** Its in-period earnings remarks read give only test capacity (a Taiwan DRAM test facility) [F] SMP-028. They contain no HBM test-time or insertion statement (NOT DISCLOSED, gaps.md).
- **Overall direction.** The direction for HBM is more test items, more insertions and higher test cost. No chipmaker publishes a count or a test time [I] SMP-041.

### 3.2 Hybrid-bonded logic

- **Intel (with EV Group, ECTC 2026): reduced sampling to 100%.** Today's chip-to-wafer bond-overlay metrology uses "reduced sampling plans" [F] SMP-030. Intel aims "to achieve high overlay metrology throughput with 100% chiplet inspection" [F] SMP-031. This is the only chipmaker statement in the period on sampling intensity for hybrid-bonded logic [I] SMP-043.
- **TSMC.** Its packaging unit ranks outlier dies from inline data by ML, with a 9x gain over baseline. The adaptive, targeted test stage is "envisioned" [F] SMP-035. Nothing names SoIC.
- **Intel test time.** On a multi-die client CPU, scan DFT "significantly reduced" test time [F] SMP-032. The abstract does not say the part is hybrid-bonded.

### 3.3 Virtual metrology and AI that replace or supplement physical measurement

- **SK hynix.**
  - AI virtual metrology provides "quality inspections for every wafer" [F] SMP-001 and screens "across all wafers without increasing the total production time" [F] SMP-002.
  - Panoptes VM has run in production lines since 2022 [F] TALK-004.
  - GRACE overlay VM has run in production since 2025 [F] SMP-007.
  - Both are presented as covering the "low sampling rates" and "sampling blind spots" of physical metrology [F] SMP-005, SMP-008.
- **Micron.**
  - AI defect classification replaced manual classification [F] SMP-022.
  - A cloud VM in an HVM memory fab aims "to improve sampling efficiency" and met production release criteria [F] SMP-025.
- **Samsung.**
  - AI super-resolution cuts SEM image time by up to 75% [F] SMP-017.
  - In DRAM development, measurements cover "only about 4% of the products", and ML imputation fills in the rest [F] PAPM-099.
- **Pattern.** VM and AI are presented as adding coverage and speed. No chipmaker gives a percentage cut in physical measurements, or a reduced sampling rate, for HBM [I] SMP-042. The quantified AI time savings apply to imaging or failure analysis (Samsung -75%; ASE SAM scan time, unquantified [F] SMP-037), not to HBM production inspection counts [I] SMP-044.

### 3.4 Direction table

{{SMP_DIRECTION_TABLE}}

## 4. Supplier awards 2025-2026: inspection, metrology and test vendors named

{{AWARDS_TABLE}}

Notes:
- Award categories describe production support, technology development or business performance. None names an HBM or hybrid-bonding inspection product [I] AW-058.
- KLA is on every full TSMC and Intel list read; Advantest is on TSMC 2025, TSMC 2026 and ASE 2025 [I] AW-058.
- No inspection, metrology or test winner was found on Micron's full 2025 and 2026 lists [F] AW-042, AW-043. Hanmi (a TC-bonder maker) won "Assembly & Test Capital Equipment" both years.
- **SK hynix.** Its own pages give counts only: 14 winners in 2025 and 11 in 2026, unnamed [F] AW-032, AW-034.
- **Onto Innovation at SK hynix.** The release saying Onto received a 2026 Best Partner Award "for Hidden Defect Prevention in High Bandwidth Memory Production" is NOT RETRIEVED. investors.ontoinnovation.com refuses scripts and the Business Wire copy failed; the URL is in gaps.md.
- **Out-of-period context.** FormFactor reported an SK hynix Best Partner Award in November 2024 for HBM probe cards [F] AW-036.
- **TSMC design-ecosystem award.** Teradyne says it won TSMC's OIP Partner of the Year 2025 for "3DFabric Testing" [F] AW-019. This is a design-ecosystem award, separate from the supplier awards.

## 5. Method by company: production, pilot or none ([I] rows only)

Each cell is an [I] row (SYN-001 to SYN-070 in `evidence.csv`), produced by `calc/method_matrix.py` from the evidence rows it cites.

How the cells are assigned:
- **PROD** = the company's own words say production, mass production, HVM, "currently in use" or in-line monitoring in a fab.
- **PILOT** = validated on production wafers or lines, or demonstrated in products, without a deployment statement.
- **lab** = test vehicle, feasibility, development, failure analysis, or "examined".
- **-** = no statement found in the documents read.
- Press-only ([S]) and vendor-only items never set a cell; they are named in the basis notes.
- The label in brackets says what a PROD or PILOT cell rests on:
  - HBM = HBM stack, TSV or micro-bump line;
  - HB = hybrid or wafer bonding outside HBM;
  - FE = memory front end, fab-wide;
  - offer = a service offering.
  - "[C]" means the status is the company's own untestable claim.

{{MATRIX}}

Reading of the matrix:
- **Production and HBM together.** Only three cells pair production with HBM: SK hynix infrared and e-beam (TSV-film inspection) and Samsung electrical test (micro-bump resistance pre-screen). SK hynix optical joins them on a company claim. [I] SYN-002, SYN-008, SYN-019, SYN-001
- **Production elsewhere.** Every other PROD rests on memory front-end, fab-wide practice or a service offer. [I] SYN rows
- **TSMC, Intel, ASE and Amkor.** Apart from Amkor's test offer, nothing goes beyond lab in their own words. TSMC's own hosts could not be read at all (gaps.md), so its row reflects missing access as much as absence of use. [I] MAIN-006
- **Laser-acoustic and X-ray scatterometry / XRF / XRD are empty for all seven.** Laser-acoustic use is reported only by press (Samsung), and X-ray scatterometry appears only in vendor-led SPIE papers without chipmaker affiliation. [I] SYN rows

## 6. Limits of this dossier

- **Abstracts, not full papers.** Conference evidence is abstract-level. Full texts sit behind ieeexplore.ieee.org, spiedigitallibrary.org and dl.asminternational.org, all of which refuse scripts. The exceptions are four open-access JSTS papers (SK hynix x3, Samsung x1) and the Intel SMT007 article, which were read in full. A method missing from an abstract may still be in the paper. [I] MAIN-005
- **TSMC, Intel, ASE and Amkor primary sites were not readable.** TSMC (all hosts), Intel (www and newsroom), ASE (all hosts), Amkor IR, Micron IR, SEMI/SEMICON and ECTC refuse scripts. The user can save the pages listed in gaps.md by hand. [I] MAIN-006
- **Venue coverage.** The paper inventory covers the venues in `calc/venues.tsv`; 85 of 3,378 records lack affiliations and are invisible to the scan. [I] MAIN-007
- **What "none found" means.** It means none in the documents read, not that a company does not use the method. [I] MAIN-008

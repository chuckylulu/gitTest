# Dossier: what chipmakers say they use to inspect and measure HBM stacks and hybrid-bonded interfaces

Run: 21 November 2026. Period covered: 1 January 2025 to 21 November 2026. Companies: SK hynix, Samsung Electronics, Micron, TSMC, Intel, ASE (incl. SPIL), Amkor. Modules A and B of the rules do not apply (user instruction).
Fiscal year-end: not applicable. No financial figures are used; every item is a technical statement dated by calendar month, so `period_fiscal` is `n/a` throughout.
Evidence: `evidence.csv` ({{N_ROWS}} rows: {{TAG_COUNTS}}). Every claim below carries one tag and the evidence ids that support it. Gap log: `gaps.md`. Method and access log: `run_log.md`. Scripts: `calc/`.

How to read the tags here: [F] = read in a saved primary document (for conference papers almost always the **abstract only**, because ieeexplore.ieee.org, spiedigitallibrary.org and dl.asminternational.org refuse scripted access); [C] = the company's own untestable claim; [S] = press or trade site; [I] = my inference, with inputs in `evidence.csv`.

## 0. Premise check: corrections to the prompt

1. **The rules block.** On this branch `research/CLAUDE.md` held only a TODO placeholder. The filled-in rules (with Modules A and B and the tag scheme) were on branch `ccr-2b9561fc-mqqdg4` and were copied over unchanged, with the tools. `prior/` is empty, so the premise check covers the prompt only. [I] MAIN-002
2. **"TSMC advanced-packaging metrology keynote at SEMICON Taiwan, September 2026."** It happened, but as the keynote of one forum, not a show keynote. The forum is the Semiconductor Advanced Inspection and Metrology Forum, on 4 September 2026 (slot from search snippets only). The speaker is Zhihua Zou of TSMC per a DIGITIMES photo caption [S] XR-014. The title, "Challenges and Opportunities for Metrology and Inspection of Advanced Packaging", comes from link text on a press page [S] XR-016. **The published abstract is NOT RETRIEVED**: semicontaiwan.org refuses scripts, and no copy was found elsewhere. Section 2.2 keeps abstract, snippet leads and press paraphrase apart. [I] XR-037
3. **"Hybrid-bonded HBM" as a current product.** None of the three memory makers says, in a document read, that its HBM is hybrid-bonded today [I] TALK-014, TALK-021, TALK-034.
   - A guest tech note by Prof. Seunghwan Joo (Inha University), hosted on SK hynix's newsroom in August 2026, says die-to-wafer hybrid bonding for HBM is "progressing toward commercialization". That is not SK hynix's own statement [S] TALK-014.
   - Samsung's undated HBM3E product-page FAQ says it is "preparing to adopt" hybrid copper bonding [C] TALK-034.
   - Micron's VLSI 2025 workshop talk is an "outlook" for chip-to-wafer hybrid-bonded memory stacking [F] TALK-021.
   Inspection statements about hybrid-bonded HBM are therefore development statements. No in-period document read gives a production statement for a hybrid-bonding inspection or measurement step. The closest is in-line AFM "performed on production wafers in the fab" for V-NAND wafer-to-wafer hybrid bonding, in a Nearfield-led paper with Samsung co-authors, which Section 5 rates pilot [F] SMP-016.
4. **TSMC SoIC and Intel Foveros Direct.**
   - Intel's 100% bond-overlay paper describes chip-to-wafer hybrid-bonding metrology "at Intel" but does not name Foveros Direct [F] PAPL-059.
   - TSMC's SoIC-CS abstract reports, as its only test of the bonded stack, that "high integration yield on daisy chains has also been successfully demonstrated" [F] PAPL-010.
   - Apart from that daisy-chain electrical test, no in-period TSMC document read names a method or a sampling plan for inspecting or measuring SoIC bonds [I] SYN-039, MAIN-006.
5. **Award events.**
   - TSMC's 2025 Excellent Performance Awards were presented on 25 Nov 2025, not in December [S] AW-001. The 2026 awards have already been given, on 17 Nov 2026 [S] AW-011.
   - Samsung's semiconductor award event is the "DS 상생협력 Day" [F] AW-040.
   - SK hynix's own Korean newsroom calls its event "파트너스데이" (Partners Day) and the winners "우수 협력사" [F] AW-032, AW-034. "Best Partner Award" is the English name used in vendors' releases, e.g. ULVAC's [F] AW-033.
   - No separate SPIL supplier award was found. SPIL took part, with ASE and USI, in ASE Technology Holding's ceremony [S] AW-055.
6. **X-ray dose.** No chipmaker document in the period gives a dose limit or failure dose for HBM. The only chipmaker dose numbers are Intel's, for on-package DRAM (not HBM). They come from an October 2024 SMTA paper that SMT007 Magazine republished in April 2025; that republication is the only reason the item falls in the period [F] XR-001 to XR-003, XR-027.
7. **Venues.**
   - ECTC's own site, SEMICON forum pages (semi.org, semicontaiwan.org, semiconkorea.org) and SPIE paper pages refuse scripted access. Papers were therefore found through Crossref volume listings, which carry affiliations for IEEE and ASM records, and Semantic Scholar abstracts.
   - SPIE proceedings records in Crossref carry no affiliations; SPIE journal records, such as J. Micro/Nanopatterning, do. A SPIE proceedings paper is attributed to a company only where its abstract or the company's own release names the company as an author.
   - Where an abstract names only the company's devices, or says "in collaboration with" it, authorship is unknown and the paper may be vendor material, so the attribution is [I] (e.g. PAPM-166, PAPM-171).
   - IITC 2026 and IPFA 2026 are not yet in Crossref. The IITC 2026 programme was read directly. No title by the seven names inspection or measurement of HBM stacks or hybrid bonds; Micron's invited talk "Advanced Memory Stacking: Thermal, Process and Reliability Challenges" is known by title only [F] MAIN-004.
8. **Company names.** "HANA Micron", a Korean OSAT, is not Micron Technology; five papers were dropped from the inventory for this reason [I] MAIN-003. Samsung Electro-Mechanics and Samsung Display are separate companies, and their papers are excluded [I] MAIN-009.

## Bottom line

- **The methods named most often for HBM and bonded stacks are electrical test and electron-beam imaging, mostly on test vehicles or in failure analysis.** {{METHOD_COUNTS}} Examples:
  - electrical test: daisy chains, interface resistance and leakage [F] PAPM-136, PAPM-052, PAPL-033;
  - e-beam:
    - SK hynix FIB cross-section of TSV film [F] PAPM-221;
    - Samsung TEM of pre-bond SiCN [F] PAPM-058;
    - Intel FIB-SEM on chip-to-wafer hybrid-bond Kelvin structures [F] PAPL-036;
    - ASE SEM/TEM/EDS of bonded interfaces [F] PAPL-108, PAPL-115;
  - scanning acoustic microscopy (C-SAM / SAT / cSAM):
    - SK hynix HBM4 test vehicle [F] PAPM-136;
    - Micron wafer-to-wafer bonding [F] PAPM-016;
    - Intel chip-to-wafer hybrid bonding [F] PAPL-035;
    - Amkor 2.5D test vehicle [F] TALK-051.
  The status words are "test vehicle", "feasible", "demonstrated" or "examined" [I] SYN-003, SYN-009, SYN-023, SYN-043, SYN-048, SYN-049, SYN-058, SYN-059, SYN-063.
- **Production wording near HBM-line inspection or measurement comes only from SK hynix, and only as its own untestable claims:**
  - SK hynix says its in-line chip-warpage method for HBM was "implemented into measurement equipment and developed into a commercialized solution currently in use", after transfer "to measurement equipment suppliers". The paper does not say where it is in use [C] PAPM-201, PAPM-202.
  - SK hynix says its optimised TSV-liner (TEOS SiO2) deposition recipe was "successfully applied in mass production" [C] PAPM-222. The paper used CVD-film IR inspection and FIB cross-sections to qualify that recipe change and does not describe them as routine production inspection steps [F] PAPM-219, PAPM-221.
- **Samsung's HBM micro-bump test is a proposal, not a statement of use.** Samsung proposes "a practical but very effective method for pre-screening of these interface failures in mass production" (buffer-die pad-to-micro-bump resistance). The abstract does not say it has been adopted [F] PAPM-049.
- **Non-electrical methods for bonded interfaces stay in development:**
  - Intel's near-infrared post-bond overlay mapping is on a test vehicle [F] PAPL-046.
  - Intel's 100% chip-to-wafer overlay metrology is in development with a roadmap [F] PAPL-059.
- **Two items come closer to production, both short of a deployment statement:**
  - SK hynix validated IR measurement of post-bond die shift and tilt in micro-bump-stacked HBM (not hybrid bonds) "using actual HBM device wafers in a production-grade MI setup" [F] PAPM-212, PAPM-213, PAPM-216.
  - A Nearfield-led paper with ten Samsung co-authors reports in-line AFM "performed on production wafers in the fab" (six wafers) for V-NAND (not HBM) hybrid bonding [F] SMP-016.
- **No chipmaker states X-ray or laser-acoustic use in production for HBM or hybrid bonds.** X-ray appears in five roles:
  - failure analysis: ASE 3D X-ray microscopy [F] PAPL-107; Intel CT de-warping with Comet, on FCPGA packages [F] XR-023;
  - process-research verification: Intel 3D X-ray CT of TCB micro-bump joints [F] PAPL-067;
  - post-silicon debug: X-ray-assisted device alteration on a mock stacked die (Intel, synchrotron) [F] PAPL-082;
  - "examined": Samsung [F] TALK-020;
  - a patent application: Samsung [F] XR-012.
  X-ray is also a stated concern about memory damage (Intel [F] XR-001; TSMC per press [S] XR-013).
  - Only trade press citing industry sources says Samsung has begun introducing laser-ultrasound (photoacoustic) hybrid-bonding inspection tools, reportedly "undergoing validation on mass production lines" [S] TALK-024, TALK-025.
  - XRF, XRD and CD-SAXS are not named by any of the seven in an in-scope document read [I] SYN-006, SYN-016, SYN-026, SYN-036, SYN-046, SYN-056, SYN-066.
- **X-ray dose: no HBM number from any chipmaker.**
  - Intel exposed on-package DRAM to a total of 350 rad in 50-rad steps with no MemTest86 errors [F] XR-002. It says the results show no infant-mortality failures "even after overexposure to three times the limit provided by DRAM manufacturer", and that long-term reliability "may be reduced" [F] XR-003.
  - Reading 350 rad as that "three times" (a limit of about 117 rad) is my inference [I] XR-035, Low.
  - TSMC's 2026 forum keynote reportedly listed "DRAM/HBM damage concern by X-ray" [S] XR-015. Its abstract is NOT RETRIEVED.
- **Sampling intensity.** Statements pointing to more measurements per stack or wafer, all development or proposals:
  - Intel (with EV Group) says current chip-to-wafer bond-overlay tools use "reduced sampling plans", and presents an on-the-move method for "100% chiplet inspection" as development on its roadmap [F] SMP-030, SMP-031;
  - Samsung's proposed micro-bump pre-screen for mass production [F] PAPM-049;
  - the call for "massive metrology" for V-NAND hybrid bonding, in a Nearfield-led paper with Samsung co-authors [F] SMP-016.
  Virtual metrology:
  - SK hynix presents VM as giving "quality inspections for every wafer" [C] SMP-001 and as covering the "low sampling rates" and "sampling blind spots" of physical metrology [F] SMP-005, SMP-008.
  - Micron cites VM "to improve sampling efficiency" without a number [F] SMP-025; that could include fewer physical measurements.
  - No company discloses a percentage cut in physical measurements [I] SMP-042.
  No company gives an HBM test time or a change in the number of HBM test insertions; the only insertion figures are press reports [I] SMP-041.
- **Awards rarely mark HBM or hybrid-bonding inspection.**
  - On the award lists read in full, inspection, metrology and test vendors are about 1 winner in 10 [I] AW-058.
  - No award category read names HBM or hybrid bonding. The nearest is Teradyne's TSMC OIP Partner of the Year 2025 for "3DFabric Testing", a design-ecosystem award [F] AW-019.
  - A search lead says Onto Innovation received an SK hynix 2026 Best Partner Award "for Hidden Defect Prevention in High Bandwidth Memory Production". The release is NOT RETRIEVED: investors.ontoinnovation.com refuses scripts and the Business Wire copy gave a stream error. The award is unverified (gaps.md).
- **Tool vendors named in, or co-authoring, the chipmakers' documents:**
  - Hitachi High-Tech IS4100 (Samsung DRAM HVM line; named in an SKKU degree-programme paper whose first author is a Samsung engineer) [F] PAPM-223, PAPM-225;
  - Nearfield Instruments (leads the in-line AFM paper, 13 of 23 authors, with ten Samsung co-authors) [F] SMP-016;
  - EV Group (co-author of Intel's 100% overlay paper) [F] PAPL-061;
  - Applied Materials (co-author of Intel's hybrid-bonding CMP paper; the cSAM and FIB-SEM makers are not named) [F] PAPL-038;
  - Tokyo Electron (co-author of a Yokohama National University-led bond-wave paper with four SK hynix co-authors) [F] PAPM-143, PAPM-144;
  - Gauss Labs, whose Panoptes VM SK hynix says it has used in production since 2022 [C] TALK-004;
  - NexSensor and Cobis Technology (SK hynix tool co-development) [F] TALK-009, TALK-012;
  - Thermo Fisher (iFAST platform named in a Samsung-majority ISTFA 2026 FA paper; co-author of a joint Micron FIB paper) [F] PAPM-090, PAPM-034;
  - Hamamatsu Photonics (co-author affiliation on a Samsung FA paper; no tool named in the abstract) [F] PAPM-081;
  - PVA TePla (co-author of ASE's AI-SAM paper) [F] SMP-037;
  - Comet (co-author of an Intel X-ray CT de-warping paper on FCPGA packages; not in the Section 1 table) [F] XR-023;
  - Akrometrix (reference only) [F] PAPM-204.
  Other vendors:
  - ASML is named (multi-beam e-beam inspection; virtual computing platform) in two SPIE abstracts on Micron devices whose authors are not recorded [F] PAPM-172, PAPM-174.
  - KLA, Camtek, Nova, Lasertec and Advantest appear only as award winners.
  - Onto Innovation appears as an award winner and, in press only, as Samsung's hybrid-bonding inspection JDP vendor [S] TALK-024.

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
- **Dose numbers.** The only chipmaker dose numbers in the period are Intel's, for on-package DRAM [F] XR-002, XR-005. Micron's co-authored study and Samsung's patent application give no dose values [F] XR-009, XR-011. Nothing came from SK hynix, ASE or Amkor [I] XR-038.
- **HBM-specific statements.** The only HBM-specific statements are a Samsung patent application with no dose numbers [F] XR-011, XR-012 and a TSMC talk known through the press [S] XR-013, XR-015.
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
- WindowsForum, 5 Sep 2026: the public abstract "explicitly lists 'DRAM/HBM damage concern by X-ray'" [S] XR-015. The article says the abstract names collaboration with foundry customers, HBM vendors and equipment vendors, and "design for metrology", as opportunities [S] XR-017. It also says that, in the material it reviewed, nothing identifies doses, tool types or failure rates [S] XR-018.
- An investor blog (7 Sep 2026) attributes the talk to TSMC's advanced-packaging quality-and-reliability team at the closing session [S] XR-019.
  - The same blog says TSMC named SK hynix, Samsung and Micron and called for "Design for Inspection" (DFI) in HBM dies. The X-ray markers it describes are the blogger's own gloss (no evidence row for these statements).
  - No other saved source corroborates the team, session or naming claims. The DIGITIMES caption names only "TSMC's Zhihua Zou" [S] XR-014.

**Other TSMC talks.**
- At the 3DICAMA launch on 9 September 2025, TSMC VP Jun He put HBM consumption at about 10 million stacks a quarter, so a 1% yield loss is costly [S] XR-034. He called "immediate detection" (第一時間偵測) a baseline requirement [S] TALK-044.
- No TSMC metrology or inspection talk was found at SEMICON Taiwan 2025 [I] MAIN-001.

## 3. Sampling intensity: more or fewer inspection and metrology steps

### 3.1 HBM (memory makers, OSAT context)

- **SK hynix: test insertions are visible, but there is no count change or test time.**
  - Press reports an in-house HBM4 package-level (system-level) tester that passed internal qualification in January 2026. It adds system-level test capability on the memory side, for compatibility checks and re-testing failed units; the article does not describe it as a per-unit production step [S] SMP-009, SMP-010.
  - SK hynix's Hot Chips 2026 slides show a KGSD (known-good stacked die) wafer test before system-level packaging. It is shown as part of the flow, not as newly added [S] SMP-011.
- **Samsung: one item proposed.**
  - Samsung proposes a mass-production pre-screen of buffer-die micro-bump interface resistance and says "it can be an essential quality monitoring item for buffer die". Adoption is not stated [F] SMP-014, PAPM-049.
  - Samsung's EDS test group names "the rising test cost of high-density HBM and DRAM products" [F] SMP-015.
  - A 2026 Samsung interview describes a new non-destructive red-light monitoring solution against HBM stacking damage, with no sampling numbers [F] SMP-013.
- **SK hynix warpage: from destructive sampling to all chips (method; deployment is a company claim).** SK hynix presents an in-line method that measures all chips on a wafer, at about 7-10 minutes for 600 chips, in place of destructive sampling whose sample is "far too small" [F] PAPM-206, PAPM-208. That the method is "currently in use" is SK hynix's own claim, and the paper does not say where [C] PAPM-201.
- **Amkor: intermediate insertions offered, and called increasingly critical by its executive.**
  - Amkor's test page offers distributed test, including "in-situ test between key assembly steps and final test (SLT and ATE) for 2.5D & 3D". HBM is named only as market context. The date of this text is not stated (page first published 2017, modified June 2026), so it may predate the period [C] SMP-038.
  - Its test VP says intermediate HBM testing "is becoming increasingly critical" [S] SMP-039.
  - An unattributed figure of 3 to 12 test insertions for a 12-high stack appears in trade press [S] SMP-040.
- **Micron.** Its in-period earnings remarks read give only test capacity (a Taiwan DRAM test facility) [F] SMP-028. They contain no HBM test-time or insertion statement (NOT DISCLOSED, gaps.md).
- **Overall direction.** Samsung papers, an Amkor web page, and trade-press reports on SK hynix and Amkor point to more test items and insertions and higher test cost. The SK hynix SiP-test item is press only. No chipmaker publishes a change in insertion count or a test time [I] SMP-041. The only insertion figures are press reports:
  - two wafer-level test steps in SK hynix's Hot Chips flow [S] SMP-011;
  - an unattributed 3-12 per 12-high stack [S] SMP-040.

### 3.2 Hybrid-bonded logic

- **Intel (with EV Group, ECTC 2026): reduced sampling to 100%.** The abstract says current chip-to-wafer bond-overlay measurement systems, inherited from lithography and wafer-to-wafer tools, use "reduced sampling plans" [F] SMP-030. It presents on-the-move imaging "to achieve high overlay metrology throughput with 100% chiplet inspection" as development and roadmap at Intel; HVM use is not stated [F] SMP-031. This is the main in-period chipmaker statement on sampling intensity for hybrid-bonded logic [I] SMP-043.
- **TSMC.** An IRPS 2026 paper from TSMC's packaging unit reports that, in experiments, ML ranking of inline data identified outlier dies 9-fold better than a baseline (metric not defined). The adaptive, targeted test stage is "envisioned" [F] SMP-035. Nothing names SoIC or says the ranking is in production use.
- **Intel test time.** On a multi-die client CPU, scan DFT "significantly reduced" test time [F] SMP-032. The abstract does not say the part is hybrid-bonded.

### 3.3 Virtual metrology and AI that replace or supplement physical measurement

- **SK hynix.**
  - SK hynix says its AI virtual metrology enables "quality inspections for every wafer" [C] SMP-001. It says the system screens "across all wafers without increasing the total production time" [C] SMP-002.
  - SK hynix says Panoptes VM has run in its production lines since 2022 [C] TALK-004.
  - SK hynix says it has applied GRACE, an explainability framework for overlay VM, in its production environment since 2025 [C] SMP-007.
  - Both are presented as covering the "low sampling rates" and "sampling blind spots" of physical metrology [F] SMP-005, SMP-008.
- **Micron.**
  - Micron says that with AI defect classification, technicians and engineers "no longer need to classify wafer defects manually" [C] SMP-022.
  - A cloud VM in an HVM memory fab aims "to improve sampling efficiency" and met production release criteria [F] SMP-025.
- **Samsung.**
  - AI super-resolution cuts SEM image time by up to 75% [F] SMP-017.
  - In DRAM development, measurements cover "only about 4% of the products", and ML imputation fills the missing values [F] PAPM-099, PAPM-100.
- **Pattern.** VM and AI are presented as adding coverage and speed. Micron's "sampling efficiency" could include fewer physical measurements, but no chipmaker gives a percentage cut in physical measurements, or a reduced sampling rate, for HBM [I] SMP-042. The AI time savings stated apply to image acquisition or failure analysis, not to HBM production inspection counts [I] SMP-044:
  - Samsung SEM, up to 75% [F] SMP-017;
  - ASE SAM scan time, unquantified [F] SMP-037;
  - SK hynix defect-analysis time, unquantified [C] SMP-004.

### 3.4 Direction table

{{SMP_DIRECTION_TABLE}}

## 4. Supplier awards 2025-2026: inspection, metrology and test vendors named

{{AWARDS_TABLE}}

Notes:
- Award categories describe production support, technology development or business performance. None names HBM or hybrid-bonding inspection; the nearest is TSMC's OIP "3DFabric Testing" award to Teradyne, a design-ecosystem award [F] AW-019. This reading of the categories is mine, over the award rows in the table above [I] AW-058.
- KLA is on every full TSMC and Intel list read (TSMC 2025 and 2026, Intel 2025) [S] AW-004, AW-014, AW-023. Advantest is on TSMC 2025, TSMC 2026 and ASE 2025 [S] AW-003, AW-013, AW-050.
- Micron's full 2025 and 2026 lists name no award category for inspection or metrology [F] AW-042, AW-043. Hanmi (a TC-bonder maker) won "Assembly & Test Capital Equipment" both years. By my classification, none of Micron's winners is an inspection, metrology or test vendor [I] AW-058.
- **SK hynix.** Its own pages give counts only: 14 winners in 2025 and 11 in 2026, unnamed [F] AW-032, AW-034.
- **Onto Innovation at SK hynix.** The release saying Onto received a 2026 Best Partner Award "for Hidden Defect Prevention in High Bandwidth Memory Production" is NOT RETRIEVED. investors.ontoinnovation.com refuses scripts and the Business Wire copy failed; the URL is in gaps.md.
- **Out-of-period context.** FormFactor reported an SK hynix Best Partner Award in November 2024 for HBM probe cards [S] AW-036.
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
- **Production and HBM together.** Only three cells pair production with HBM, all at SK hynix and all on its own untestable claims: infrared and e-beam (TSV-film inspection, PAPM-222 [C]) and optical (in-line chip warpage, PAPM-201 [C]). [I] SYN-001, SYN-002, SYN-008
- **Samsung electrical test.** It reaches pilot: a pre-screen proposed for mass production, and HBM validation and demonstration statements. [I] SYN-019
- **Production elsewhere.** Every other PROD rests on memory front-end, fab-wide practice (some of it the company's own claim) or a service offer. [I] SYN-010, SYN-011, SYN-021, SYN-028, SYN-069
- **TSMC, Intel, ASE and Amkor.** Apart from Amkor's test offer, nothing goes beyond lab in their own words. TSMC's own hosts could not be read at all (gaps.md), so its row reflects missing access as much as absence of use. [I] MAIN-006
- **Laser-acoustic and X-ray scatterometry / XRF / XRD are empty for all seven.** Laser-acoustic use is reported only by press (Samsung), and X-ray scatterometry appears only in vendor-led SPIE papers without chipmaker affiliation. [I] SYN-004, SYN-006, SYN-014, SYN-016

## 6. Limits of this dossier

- **Abstracts, not full papers.** Conference evidence is abstract-level. Full texts sit behind ieeexplore.ieee.org, spiedigitallibrary.org and dl.asminternational.org, all of which refuse scripts. A method missing from an abstract may still be in the paper. [I] MAIN-005
  The exceptions, read in full:
  - four open-access JSTS papers: three SK hynix, and one SKKU degree-programme paper with a Samsung first author;
  - the Amkor IMAPS 2025 paper;
  - the Intel SMT007 article;
  - the full-text items added in the gap-fill round (Section 7).
- **TSMC, Intel and ASE primary sites, and Amkor's and Micron's IR sites, were not readable.** TSMC (all hosts), Intel (www and newsroom), ASE (all hosts), Amkor IR, Micron IR, SEMI/SEMICON and ECTC refuse scripts. Amkor's test, event and blog pages and Micron's blog and supplier page were read. The user can save the pages listed in gaps.md by hand. [I] MAIN-006
- **Venue coverage.** The paper inventory covers the venues in `calc/venues.tsv`; 85 of 3,378 records lack affiliations and are invisible to the scan. [I] MAIN-007
- **What "none found" means.** It means none in the documents read, not that a company does not use the method. [I] MAIN-008

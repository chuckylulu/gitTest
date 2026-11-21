# Nordson Corporation (NDSN) — Test & Inspection, Advanced Technology Solutions (ATS) segment

Compiled 2026-11-21. Fiscal year ends 31 October. USD. Raw dated facts; no opinions, prices or multiples. "NOT DISCLOSED (checked: …)" = searched and absent. "(computed)" = arithmetic by the compiler from reported figures. Speaker labels: NORDSON / CUSTOMER / COMPETITOR / INDEPENDENT / SECONDARY. `[idx]` = wording taken only from a search-engine summary of a nordson.com page that returned HTTP 403; re-check against the live page.

**Rules applied.** `research/CLAUDE.md` still contains the placeholder "TODO: paste the rules block here", and `research/prior/` is empty. The rules applied are the "Global Chat Rules" used in the user's recent AI Studio prompts: raw dated primary facts, no adjectives or valuation, one URL per document, explicit absence markers. Module A items A1/A3/A5 and Module B are not defined in any file found. The scope used here is an assumption (the user stated no preference): **A1 = revenue and segment mix, A3 = profitability, A5 = cash and capital; Module B = claims ledger (claim | evidence for | evidence against | verdict | what would settle it) plus one handoff row.** Re-run sections 6–7 once the real rules block is pasted.

Supporting files: `notes/q1_q2_acoustic.md`, `notes/q3_xray.md`, `notes/q4_optical.md`, `notes/q5_financials.md` (full tables, every URL); `verification.md` (adversarial re-check of the load-bearing facts and the claims-ledger adjudication).

---

## 0. FY2026 fourth-quarter results: NOT PUBLISHED (as of 2026-11-21)

| Item | Fact | Source |
|---|---|---|
| Q4 / FY2026 release date | "release fourth quarter and fiscal year 2026 earnings on December 15, 2026, after the close of the market"; webcast "Wednesday, December 16, 2026", 8:30 AM ET | NORDSON IR release, 6 Nov 2026 |
| Latest results published | Q3 FY2026 (quarter ended 31 Jul 2026): 8-K Item 2.02 filed 19 Aug 2026; 10-Q filed 20 Aug 2026 | EDGAR submissions list, read 2026-11-21 |
| Filings after Q3 | 8-K 23 Oct 2026 (Items 7.01/8.01/9.01): Contrinex Holding SA acquired by Nordson London Limited on 23 Oct 2026; enterprise value ~USD 168M; "approximately $50 million in annual revenue"; "complements Nordson's test and inspection portfolio"; "will be integrated into Nordson's Advanced Technology Solutions segment". Afterwards only Forms 4 / 4/A (to 4 Nov 2026). | 8-K 23 Oct 2026 and Ex. 99.1 |

---

## 1. Acoustic (former Sonoscan): SpinSAM and other acoustic microscopes

| Product | Launch | Transducer frequency | Smallest void | Wafers per hour (settings) | Couplant handling | Edge exclusion | Status at customers | Applications named | Source |
|---|---|---|---|---|---|---|---|---|---|
| **SpinSAM** (300 mm, 4 spin-scan stages, EFEM) | Release 10 Jun 2024: "will be unveiled in a video presentation for the first time" at SEMICON West 2024 (9–11 Jul 2024, San Francisco). First booth showing SEMICON Taiwan, 4–6 Sep 2024. 2024 Best of West finalist (8 Jul 2024); 2024 Global Technology Award (release 30 Oct 2024). | NOT DISCLOSED as a number. Nordson: "widest frequency range ever achieved in a production environment" (distributor copy). General Nordson AMI range "15 megahertz up to about 300 megahertz" (podcast, not SpinSAM-specific). | NOT DISCLOSED (checked: releases Jun 2024–Sep 2026, Semiconductor Digest 9 Jan 2025, podcast 17 Apr 2025, distributor page, FY2025 Annual Report) | "up to 4 (300mm) wafers simultaneously at 41 wafers per hour"; "at 100 micron resolution about 41 wafers per hour ... eight times faster than our previous machine" (AW300); full-wafer scan "less than six minutes". Finest pixel "about 10 micron"; **WPH at 10 µm: NOT DISCLOSED**. Variable resolution: "lower resolution scan in the center ... maximize the resolution towards the edge". | "four matched waterfall transducers"; "Waterfall transducer provides non-immersion scanning which minimizes risks of contamination and false bond indications"; "limits the exposure to water versus some competitors that are using water bath or immersion scanning"; deionized water. Drying step: NOT DISCLOSED. | NOT DISCLOSED in mm. "edge scanning that targets defect prone areas"; "a ring around the outside of the wafer". | NOT DISCLOSED (no named or described customer, order, shipment, qualification or evaluation; checked: releases, FY2025 ARS, Q1–Q3 FY2026 calls, podcast, Korean press, SEC full-text search) | "bonded wafers, Chip-on-Wafer, stacked wafers, MEMS, and over-molded wafers"; HBM added once ("MEMs HBM wafers", 7 Aug 2025). **Hybrid bonding: not named. CoWoS: not named for SpinSAM** (named for the XM8000 X-ray tool). | NORDSON: Semiconductor Digest 10 Jun 2024; 3D InCites 1 Nov 2024; Semiconductor Digest 9 Jan 2025; 3D InCites podcast (B. Schackmuth) 17 Apr 2025; 3D InCites 7 Aug 2025; htt group distributor page; Nordson FY2025 ARS (SEC, 16 Jan 2026) |
| **SpinSAM Lite** | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | [idx] "spin scan up to 2 wafers simultaneously"; "100 μm scan (from wafer load to wafer load) takes less than six minutes" | [idx] matched transducers | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NORDSON [idx] product page |
| **AW300** (predecessor; 2 transducers, raster scan) | Jul 2012 (Sonoscan) | NOT DISCLOSED for AW300; AW-series page [idx] "500 MHz bandwidth pulser/receiver" | AW-series [idx]: delamination "as thin as 200Å"; sister AW200: "inter-wafer voids as small as 5-µm in diameter"; AW322 200 (Jun 2014): "down to 5 microns", "frequencies up to 230 MHz" | Not stated; SpinSAM stated as 8× faster at 100 µm | AW200: "Waterfall transducer"; "After imaging, the wafer pair is automatically dried" | NOT DISCLOSED | NOT DISCLOSED | Individual 300 mm wafers "before bonding" (crack screening); direct-bonded SOI; 3D IC, chip-on-wafer | Sonoscan releases via MySemiconDaily 9–11 Jul 2012; Silicon Semiconductor 29 Jun 2014 |
| **FACTS2 DF2400** (trays/carriers, not wafers) | Shipping announced Jan 2014 | NOT DISCLOSED | NOT DISCLOSED | "2x to 7x faster throughput than previous systems" (no units/h) | "non-immersion technology"; "dedicated drying areas" | n/a | NOT DISCLOSED | JEDEC trays, flip chips, lead-frame strips, IGBT modules | Microwave Journal 15 Jan 2014 |
| **Gen7 C-SAM** (lab) | 15 Aug 2018 | D9650 sibling [idx] "5 MHz to 230 MHz" | NOT DISCLOSED | n/a (lab); "50% higher screening throughput" vs prior | Waterplume option | n/a | Positioned for "laboratory analysis, failure investigation" (Sep 2026) | Lab / FA | Circuits Assembly 15 Aug 2018; I-Connect007 21 Sep 2026 |
| **SonoFlex** (back-end packages, small panels) | "worldwide debut" SEMICON West 13–15 Oct 2026 (Moscone, booth 5844); also SEMICON Europa 10–13 Nov 2026; [idx] 2026 Best of West award (15 Oct 2026) | NOT DISCLOSED | NOT DISCLOSED | "scanning speeds up to twice as fast as conventional solutions"; multi-system configs "increasing throughput by up to eight times" (no units/h) | NOT DISCLOSED | n/a | NOT DISCLOSED | "back-end advanced semiconductor manufacturing"; small panels | I-Connect007 21 Sep and 16 Oct 2026 |

- Business-level statement (all acoustic, not SpinSAM-specific): "our AMI business ... we are coming off of two really strong years of growth" (CEO, Q1 FY2026 call, 19 Feb 2026); "you typically use acoustic for memory and you use more x-ray for ... logic chips" (CEO, 11 Dec 2025).
- No Nordson product named "Gen8" was found. SpinSAM is the only Nordson SEC-filed product name match (FY2025 ARS, CEO letter: "high throughput and superior sensitivity ... scans multiple wafers simultaneously").

---

## 2. Head-to-head: Nordson vs PVA TePla vs Hitachi (automated wafer-level acoustic)

| Item | Nordson (SpinSAM) | PVA TePla (SAM Auto Wafer / Autowafer 300) | Hitachi Power Solutions (WAFER LINE; FineSAT) | Source |
|---|---|---|---|---|
| Coupling | Waterfall (non-immersion), 4 transducers | Autowafer 300 flyer (Mar 2026): "Non-immersion waterfall design"; "spin dryer"; "dual arm robot for wet and dry"; optional "Nearly dry process with DLIC technology"; C2W talk: water "only applied locally on the carrier side ... chips side remains dry" | WAFER LINE: coupling NOT DISCLOSED; FineSAT7 is a water-tank lab tool ("Larger water tank ... 300 mm") | flyer PDF; IEEE.tv 17 Jan 2025; Hitachi 29 Aug 2022 |
| Wafers in parallel | 4 (SpinSAM), 2 (Lite [idx]) | "Scanning up to 2 wafers simultaneously" (Autowafer 300); "four dual array transducers ... up to 400 MHz" (SAM Auto Wafer page) | NOT DISCLOSED; array probe 25/50/75 MHz (FineSAT Hybrid) | vendor pages |
| Resolution / void claim | ~10 µm pixel finest; void NOT DISCLOSED | "Minimum Resolution 0.5 µm/pixel" (flyer); CMD 2 Sep 2025: SAM "Resolution: 5–15 µm"; hybrid-bond talk: "push ... to the 5µm limit", UHF tonebursts "down to 1µm" for thinned chips | Patent award 14 Jun 2023: automatic detection of defects "直径10µm程度" (~10 µm diameter) at wafer bond interface | PVA flyer/CMD/IEEE.tv; Hitachi 14 Jun 2023 |
| WPH | 41 at 100 µm | NOT DISCLOSED | NOT DISCLOSED | — |
| Production / qualification status | NOT DISCLOSED | Edison (SECONDARY, 26 Mar 2026): qualified at "a Taiwanese foundry, a US IDM/foundry and a Korean memory player, with a system shipped for HVM"; H1 2026 Metrology order intake €97.7M (H1 2025: €53.3M); capacity "fully utilized through mid-2027" (PVA, 6 Aug 2026) | WAFER LINE: "continuous operations on several customers' mass-production lines" (unnamed; page ©2016) | Edison; PVA H1 2026 release; Hitachi product page |
| Published comparison naming the three vendors | NOT FOUND (checked: NIST/SEMI bond-void round robin 2016, ISTFA, SPIE/imec abstracts, SemiEngineering 2025, PVA CMD deck, Edison notes, Korean press). NIST round robin (tools anonymized): acoustic minimum sensitivities "range from 1 µm to 25 µm"; "key trade-off ... between speed of measurement and resolution". | same | same | NIST pub. 1 May 2016 |
| Shared customers | No vendor names a fab. Maeil Business (SECONDARY, 21 May 2025): Korean HBM C-SAM had relied on "Sonix and Sonoscan of the US and Hitachi of Japan" (customer unnamed). | Customers unnamed | Customers unnamed | Maeil 21 May 2025 |
| Pricing indications | NOT DISCLOSED | Per-tool price NOT DISCLOSED; order values given without unit counts (not divisible). CMD: SAM market $327M (2024) / $333M (2025), PVA share 22% (company estimate). | FineSAT7 (lab): "28.5 million yen ～" before tax (from 1 Oct 2022). WAFER LINE price NOT DISCLOSED. | Hitachi 29 Aug 2022; PVA CMD 2 Sep 2025 |
| Dry alternative (context) | — | — | — | Onto EchoScan (14 Jan 2025): "1µm voids in atmosphere"; incumbents "limited to ≥10µm ... require water immersion". The Elec (31 Mar 2026, SECONDARY): Onto in JDP with Samsung, laser-ultrasound equipment supplied to production lines. |

---

## 3. X-ray (former Dage / Matrix): automated wafer X-ray metrology and inspection

| Product | Launch | Source / resolution | Smallest void / feature | Wafers per hour (settings) | Handling | Edge exclusion | Status at customers | Applications named | Stated dose to memory / measures | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| **XM8000** (wafer X-ray metrology) | "introduced to the market on 6/24/2013"; launch release 17 Jan 2014 (SEMI European 3D TSV Summit, Grenoble) | Sealed-transmissive tube above wafer, detector below; kV NOT DISCLOSED | "The number and size of every void on every bump"; "every void in every TSV" (no µm figure) | NOT DISCLOSED; relative only: "20x faster than the Diamond" (Jan 2014), "30X faster than traditional X-ray" (Oct 2017) | Wafers up to 300 mm; "fully compliant with the front-end fab environment" | NOT DISCLOSED | Order from "a major customer in the semiconductor industry" (Nov 2014); "a number of tools have been sold" (Mar 2015); Korea clean-room demo facility (Jun 2016). No named customer. | TSVs, wafer bumps, 2.5D/3D IC, MEMS; overlay | "radiation safe defect detection" (Oct 2017); no number | Nordson IR 17 Jan 2014; 3D InCites 24 Jan 2014; Electronic Specifier Nov 2014; iConnect007 12 Oct 2017 |
| **XM8000 Pro series** (XM8000-5, -7 Pro, -7P Pro) | Launch date NOT DISCLOSED; shown as "XM8000Pro" at SEMICON West 2026 (13–15 Oct 2026) | [idx] NT100M LaB6 tube "10 times brighter"; [idx] 6.5 MP detector, 50 µm pixels; 2025 releases: "powered by the QuadraNT tube and detector"; kV NOT DISCLOSED | [idx] "100nm defect recognition"; "sub micron level 3D reconstruction"; smallest void in µm NOT DISCLOSED | NOT DISCLOSED; [idx] XM8000-5 "the fastest X-ray metrology system on the market" (no number); 2D/2.5D/3D modes trade throughput vs depth (blog 15 Jul 2026, no numbers) | [idx] projection angles up to 45°; -7P with EFEM supports panels to 510 × 515 mm; FOUP count NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED (checked: releases 2014–2026, FY2025 10-K, Q1–Q3 FY2026 calls, trade press, Korean/Chinese searches) | "CoWoS, TSVs, 2.5 and 3D IC packaging and wafer bumps" (Oct 2025); [idx] image caption "HBM Shield In Situ". Hybrid bonding: not named. | [idx] "IC-Safe Technology ... allows products to be safely inspected in-line without risk of radiation damage"; "IC-Safe shields completely eliminate radiation exposure to all other device samples not under test" (selective sampling). Dose per image/site/wafer: NOT DISCLOSED. | [idx] nordson.com XM8000 Pro page; Nordson productronica 2025 release PDF (Oct 2025); iConnect007 21 Sep 2026 |
| **Quadra W8** (lab-based automated wafer X-ray) | Trade press 9 Oct 2018 | Aspire 6.7 MP detector | "defects as small as 0.1µm" (conditions not stated) | NOT DISCLOSED | Dual-port EFEM, from FOUP, SECS/GEM, SEMI S2/S8 | NOT DISCLOSED | NOT DISCLOSED | Bumps, TSV, MEMS, 2.5D/3D WLP | NOT DISCLOSED | Circuits Assembly 9 Oct 2018 |
| Quadra 7 Pro (manual; context) | 2023 award | Directory: 30–160 kV, 20 W | n/a | n/a | Manual | n/a | n/a | HBM micro-bump arrays (Nordson article, SemiEngineering 9 Jun 2026) | Quadra tools (Nordson Dage, 27 Mar 2019): "Low dose mode"; "dose calculation tool"; zinc filter tray "can reduce overall X-ray dose by up to 80%" | Dataweek 27 Mar 2019 |
| AXI X# / XS + Dynamic Planar CT (board/tray inline; not a wafer handler) | DPCT "next-generation" (Oct 2025) | NOT DISCLOSED | [idx] flip-chip bumps "down to 40 micron" | "up to 2× faster image acquisition than classical Planar CT" | Boards/trays | n/a | NOT DISCLOSED | Flip-chip micro-bumps | DPCT "crucially reducing sample radiation dose" (no number); [idx] "low dose radiation filters" | productronica 2025 release PDF |

Dose evidence (memory):

| Study | Figure | Speaker | Date |
|---|---|---|---|
| Bernard (Dage) & Blish (AMD), EPTC 2005 | Random total-dose thresholds: Flash 50–150 Gy(Si); DRAM 150–500 Gy(Si). 100–150 µm zinc filter reduces silicon dose "by a factor ~ 100 X". | NORDSON co-authored | 2005 |
| Data I/O + Nordson DAGE, IPC APEX 2024 | Managed NAND failed after "an estimated 20,000 RADS" (= 200 Gy); recommended "Tube voltage: 60KV", "Tube power: 2 Watts", "Distance to target: 12.4 millimeters", "Filtering (Zinc): 150 Micron is a must" | NORDSON co-authored | 2024 |
| Sharma et al., IMAPS 2016 | NAND first byte errors at "75-150 Gy"; NOR "250-450 Gy"; normal 2D inspection "~ 15-20 Gy" | INDEPENDENT | Oct 2016 |
| NXP AN13412 | "A total dose << 1 Gy (including rework / re-inspection) is recommended." | INDEPENDENT (device maker) | 8 Oct 2021 |
| UAH, IEEE IMW 2023 | 3D TLC NAND bit errors after TID 10 krad(Si) (Co-60 gamma, not X-ray) | INDEPENDENT | May 2023 |
| HBM / hybrid-bonded DRAM wafer X-ray damage threshold | NOT FOUND (checked: SemiEngineering 2024–2026, Nordson HBM article 2026, NXP, IMAPS, IMW, patents) | — | — |

- Nordson business statements on X-ray: FY2025 10-K: ATS growth "partially offset by weakness in x-ray inspection systems"; Q1 FY2026 call: "Our X-ray systems ... are starting to inflect"; "the semi side of X-ray is doing really well and the auto is flattish".
- Competing 300 mm wafer X-ray tool announced in the same period: ZEISS NLX (3D laminography, "X-Guard dose control"), press release 12 Oct 2026 (COMPETITOR).

---

## 4. Optical (former CyberOptics): sensors and wafer bump inspection; overlap with Camtek, Onto, KLA

| Product | Launch | Key specification (vendor) | Status at customers | Applications named | Source |
|---|---|---|---|---|---|
| **WX3000** (2D/3D wafer bump inspection & metrology; NanoResolution MRS sensor) | Release 8 Jul 2020 (virtual SEMICON West 20–23 Jul 2020) | "100% 3D and 2D inspection and metrology simultaneously ... more than 25 wafers per hour"; features "down to 25 microns"; "in excess of 75 million 3D data points per second"; 12"/8" and 8"/6" versions. Product-page table (snippet only): ≥25 WPH 300 mm 3D+2D, ≥55 WPH 200 mm; 3D accuracy 0.2 µm; repeatability 0.3 µm @3σ; bump height range 25–250 µm. | First PO from "a large integrated device manufacturer", delivery scheduled Q1 2022 (27 Oct 2021). Later orders/customers: NOT DISCLOSED (checked: CyberOptics releases to Q2 2022, DEFM14A, Nordson 10-K FY2022–FY2025, releases, calls). No WX-series tool in Nordson SEMICON West 2025/2026 lists. | Wafer bumps, solder balls, gold bumps, Cu pillars, microbumps, interposers. HBM / hybrid bonding / CoWoS / fan-out: NOT DISCLOSED. | CyberOptics 10-K FY2021 (11 Mar 2022); Q3 2021 release; launch release reprints |
| **3D MRS / NanoResolution sensors** (sold to OEMs) | NanoResolution: SEMICON West Jul 2019 (Best of West 2019) | Nine MRS models; 3 µm-pixel NanoResolution sensor | KLA: 2015 "mutually exclusive agreement to supply 3D sensor subsystems" for "KLA-Tencor BEOL package inspection systems"; KLA = 10% of CyberOptics 2018 revenue; still named FY2019 10-K. Three unnamed OEMs ordered NanoResolution (FY2019 10-K). Post-Nov 2022 OEM sales/customers: NOT DISCLOSED. | Semiconductor component package inspection | CyberOptics 10-K FY2018, FY2019, FY2021; Silicon Semiconductor 20 Jan 2015 |
| **SQ3000+ / SQ7000+** (AOI/SPI/CMM) | SQ3000+ Oct 2021; SQ7000+ Feb 2025 (APEX 2025) | SQ3000+ features "down to 50 microns"; SQ7000+ "5-micron MRS sensor" | SQ7000+: unnamed "global GPU leader" (Nordson case study 30 Sep 2025, snippet) | "advanced packaging, socket metrology, and memory" (SQ7000+) | Nordson SEMICON West 2025 release |
| **WaferSense / ReticleSense** (wireless in-tool sensors: leveling, gapping, teaching, vibration, particles) | Since 2000s; ATS2 (2023), AGS2 and ACS (2025) | — | "Most of the world's largest manufacturers of semiconductors and semiconductor equipment purchase our WaferSense products" (CyberOptics, 2022); named customers NOT DISCLOSED | Front-end fab tool set-up and diagnostics | CyberOptics 10-K FY2021; Nordson releases 2023, 2025 |

CyberOptics revenue by product line (USD thousands; last disclosures before the acquisition):

| Line | 2019 | 2020 | 2021 | H1 2022 |
|---|---|---|---|---|
| High-precision 3D/2D sensors | 12,579 | 17,522 | 25,941 | 14,887 |
| Inspection & metrology systems (SQ3000, WX3000) | 32,713 | 37,547 | 42,958 | 22,759 |
| Semiconductor sensors (WaferSense) | 13,971 | 15,048 | 23,875 | 14,169 |
| **Total** | 59,263 | 70,117 | 92,774 | 51,815 |

Shares of 2021 revenue: 3D MRS sensors 19%, SQ3000 24%, WaferSense 26% (computed from table: 25.7%). WX3000 revenue NOT DISCLOSED. Deal: $54.00/share; "approximately $100 million in annual revenue"; aggregate price $377,843k net of $40,890k cash; closed 3 Nov 2022. Management forecast in DEFM14A: revenue $106.9M (2022), $123.0M (2023), $142.0M (2024).

Overlap:

| Task | Nordson / ex-CyberOptics | Camtek | Onto Innovation | KLA | Published head-to-head / shared customer |
|---|---|---|---|---|---|
| 3D bump height / coplanarity, 2D bump-level defects | WX3000: features ≥25 µm, >25 WPH (300 mm) | Eagle-AP "bumps down to 2µm"; Hawk (Feb 2025) "150 nanometer defects", "500 million micro bumps" | Dragonfly G3 + 3Di (14 Jan 2025) for HBM bump control, "below 5µm in HVM"; Dragonfly G5 (16 Mar 2026) "150nm" | Kronos 1190; CIRCL-AP | NOT DISCLOSED |
| Hybrid-bond pad / surface optical inspection | No ex-CyberOptics product (Nordson's bonded-wafer offer is acoustic and X-ray) | Hawk: "Chiplets, HBM and Hybrid Bonding" | Dragonfly G5 for "CMP and hybrid bonding" | NOT DISCLOSED in fetched text | n/a |
| 3D sensor inside third-party package inspection tools | MRS sensors (OEM) | NOT DISCLOSED | NOT DISCLOSED | KLA was a sensor customer (2015–FY2019); later status NOT DISCLOSED | Supplier relationship, not competition |
| Who names whom | CyberOptics (2022) named Camtek, Unity SC, Utechzone, Onto | Camtek names Onto and, for limited applications, KLA; not Nordson | Onto names KLA and Camtek; not Nordson | KLA names Lasertec, Onto (fetched portion); not Nordson | — |

Competitor HBM wins in the same task (COMPETITOR): Camtek — Hawk orders ~$45M from a tier-1 IDM (10 Feb 2026) and >$105M from a tier-1 OSAT and an HBM maker (2 Jun 2026). Onto — >$240M volume purchase agreement with an HBM maker for Dragonfly 2D inspection and 3D bump metrology (19 Feb 2026); Dragonfly G5 "displacing the previously established tool of record" at an HBM maker (16 Mar 2026). KLA — calendar 2025 advanced-packaging systems revenue "$950 million" (call 29 Jan 2026, SECONDARY transcript).

---

## 5. Size and momentum

### 5a. Every Nordson disclosure on Test & Inspection since the CyberOptics acquisition

T&I revenue in dollars: **NOT DISCLOSED** for any period. T&I margin: **NOT DISCLOSED**. (Checked: 10-K FY2023–FY2025; 10-Q Q1–Q3 FY2026; every earnings 8-K Q4 FY2022–Q3 FY2026; 16 call transcripts Dec 2022–Aug 2026; investor decks Aug 2024, May 2025, Aug 2026.)

| Date | Source | Disclosure (verbatim) |
|---|---|---|
| 8 Aug 2022 | Deal release | CyberOptics "generates approximately $100 million in annual revenue" |
| 15 Dec 2022 | Q4 FY2022 call (CFO J. Kelley) | "double digit growth in both the test and inspection and electronics dispense product lines" |
| FY2023 (releases) | Q1–Q4 FY2023 8-Ks | Acquisition (CyberOptics) contribution to ATS sales growth: Q1 +13.5%, Q2 +12.3%, Q3 +10.7%, Q4 +15.0%; FY2023 +12.9% (ATS organic −9.2%) |
| 21 Feb 2023 | Q1 FY2023 call | Organic growth "driven by the Test and Inspection acoustic product line"; "weakness in optical Test and Inspection product lines relating to the memory end market" |
| 22 Aug 2023 | Q3 FY2023 call (CEO) | "high-single-digit growth in the test and inspection business" |
| 20 Dec 2023 | FY2023 10-K (goodwill test, 1 Aug 2023) | Reporting unit "Advanced Technology Solutions Segment - Test & Inspection": goodwill $371,425k; fair value exceeds carrying value by 168% |
| 14 Dec 2023 | Q4 FY2023 call | CyberOptics "contributed 15%, the highest quarterly sales to date under Nordson ownership" |
| 21 May 2024 | Q2 FY2024 call (CEO) | "our X-ray business, which experienced double-digit growth in fiscal 2023"; "The acoustic test and inspection part of the business is also growing ... on some new memory applications" |
| 18 Dec 2024 | FY2024 10-K (goodwill test, 1 Aug 2024) | "ATS - Test & Inspection": goodwill $375,707k; headroom 173%. From FY2025 the reporting units equal the three segments. |
| 20 Feb 2025 | Q1 FY2025 call (CFO D. Hopgood) | "double-digit declines in electronics processing and x-ray product lines" |
| 29 May 2025 | Q2 FY2025 call (CFO) | "electronics dispense, optical, and x-ray inspection systems, all growing double-digits" |
| 29 May 2025 | Q2 FY2025 call (CEO); May 2025 deck | "50% of our business would be semiconductor high-power computing" (ATS), vs "20% to 30%" four to five years earlier; deck: Semiconductors "50% of ATS Sales" |
| 10–17 Dec 2025 | Q4 FY2025 release; FY2025 10-K | "fewer deliveries of test and inspection systems, particularly x-ray systems"; FY2025: "partially offset by weakness in x-ray inspection systems" |
| 11 Dec 2025 / 19 Feb 2026 | Calls (CEO) | Semiconductor applications "approximately 50% of ATS revenue"; automotive "about 15%" (11 Dec 2025) |
| 21 May 2026 | Q2 FY2026 call (CEO) | "over 50% of this business is in semiconductor now" |
| 19–20 Aug 2026 | Q3 FY2026 release; Aug 2026 deck | ATS organic +30.9% "driven by strong growth in electronics dispense and test and inspection product lines"; deck: ATS = Semiconductors 50%, General Electronics 25%, Automotive Electronics 10%, Industrial 15%; ATS geography Asia 67% |
| 23 Oct 2026 | Contrinex 8-K | ~$50M revenue sensor business "complements Nordson's test and inspection portfolio" |

### 5b. ATS segment (USD thousands)

| Period | Sales | YoY | Organic | Acquisitions | EBITDA (margin) | Basis |
|---|---|---|---|---|---|---|
| FY2022 | 562,859 | +18.8% | +22.4% | — | 142,033 (25%) | original |
| FY2023 | 577,270 | +2.6% | −9.2% | +12.9% | 131,151 (23%) | original |
| FY2024 | 510,220 | −11.6% | −11.4% | — | 113,559 (22%) | original |
| FY2024 recast (MCS moved from IPS to ATS, effective 1 Nov 2024) | 595,557 | −11.3% | −11.2% | — | 129,181 (21.7%) | recast |
| FY2025 | 624,510 | +4.9% | +4.1% | — | 146,589 (23.5%) | recast |
| Q1 FY2026 | 149,417 | +23.1% | +20.7% | — | 32,600 (22%) | recast |
| Q2 FY2026 | 177,531 | +10.1% | +8.5% | — | 48,327 (27%) | recast |
| Q3 FY2026 | 219,880 | +28.4% | +30.9% | — | 65,695 (30%) | recast |
| 9M FY2026 | 546,828 | +20.5% | +20.1% | — | 146,622 (27%) | recast |
| LTM to 31 Jul 2026 (computed: Q4 FY2025 + 9M FY2026) | 717,433 | — | — | — | 189,378 (26.4%) | recast |

From FY2025 the segment profit measure is EBITDA; segment operating profit is no longer disclosed. 9M FY2026 organic growth by segment: IPS +3.8%, MFS +7.1%, ATS +20.1%.

### 5c. HBM and advanced-packaging remarks, last six earnings calls

"HBM" / "high bandwidth": **0 mentions in all six calls** (TickerTrends full transcripts, cross-checked on Equibles; also absent from the FY2025 10-K, Aug 2024 / May 2025 / Aug 2026 decks and FY2026 releases).

| Call date | Speaker | Quote | HBM named |
|---|---|---|---|
| 29 May 2025 (Q2 FY2025) | S. Nagarajan, CEO | "this incredible investment that is going on for computing power, be it for AI, be it for cloud computing ... at the heart of all of that investment is really complex new generation computer chips and semiconductors"; "we are at very early stages of the GPUs that are getting built ... a new generation of in-process sensors called WaferSense. And that is a product category that is growing very nicely for us." | No |
| 21 Aug 2025 (Q3 FY2025) | CEO; D. Hopgood, CFO | "our products deliver leading productivity and quality in complex advanced packaging applications of semiconductors used for AI, cloud computing and more. Our applications are largely at the back end of the semiconductor packaging process"; CFO: "partially offset by weakness in X-ray Inspection system sales" | No |
| 11 Dec 2025 (Q4 FY2025) | CEO; CFO | "complex advanced packaging applications of semiconductors used for AI, cloud computing"; "composite structures ... where you have both logic as well as memory ... you typically use acoustic for memory and you use more x-ray for ... logic chips"; new test technologies "probably not in '26, probably in '27"; CFO: "near-term weakness in x-ray systems" | No (memory referenced) |
| 19 Feb 2026 (Q1 FY2026) | CEO | "our X-ray systems that ensure the quality of semiconductor packaging are starting to inflect"; "ATS core competency is in the advanced packaging process of semiconductor manufacturing"; "These complex chips are now both combined logic and memory on the same stack ... yield rates are everything here" | No (memory referenced) |
| 21 May 2026 (Q2 FY2026) | CEO | "our test and inspection systems that ensure the quality of semiconductor packaging are also inflected"; "panel-level packaging. It's very, very early stage"; "the last 3 quarters, our dispense business is far more robust than our test and inspection business" | No |
| 20 Aug 2026 (Q3 FY2026) | CEO | "Clearly, the dispense business is typically ahead of the curve in terms of growth cycle ... a good inflection point both for our X-ray and optical businesses. If you remember, these technologies are critical in ensuring semiconductor packaging." | No (no AI mention) |

---

## 6. Module A (group level; scope assumed — see header)

### A1. Revenue and segment mix (USD millions)

| Period | Group sales | YoY | Organic | IPS | MFS | ATS | ATS share |
|---|---|---|---|---|---|---|---|
| FY2023 | 2,628.6 | +1.5% (computed) | −1.4% | 1,391.0 | 660.3 | 577.3 | 22.0% |
| FY2024 | 2,689.9 | +2.3% | −2.5% (10-K; release "3%") | 1,484.2 (recast 1,398.9) | 695.5 | 510.2 (recast 595.6) | 22.1% (recast) |
| FY2025 | 2,791.7 | +3.8% (computed) | release: "a 3% decrease in organic volume"; acquisitions net +6% | 1,331.8 | 835.4 | 624.5 | 22.4% |
| Q1 FY2026 | 669.5 | +8.8% (computed) | +6.5% | 326.9 | 193.2 | 149.4 | 22.3% |
| Q2 FY2026 | 740.8 | +8.5% (computed) | +6.6% | 350.5 | 212.9 | 177.5 | 24.0% |
| Q3 FY2026 | 817.7 | +10.3% (computed) | +11.7% | 367.2 | 230.5 | 219.9 | 26.9% |
| 9M FY2026 | 2,228.0 | +9.2% (computed) | +8.4% | 1,044.6 | 636.6 | 546.8 | 24.5% |
| LTM to 31 Jul 2026 (computed) | 2,979.8 | — | — | — | — | 717.4 | 24.1% |
| FY2026 guidance (19 Aug 2026) | 3,035–3,075 | "9% to 10%" | — | — | — | — | — |

Mix (FY2025): geography Americas 43.2%, Europe 25.9%, Asia Pacific 30.9%; end markets (Aug 2026 deck, "directional") Electronics 27%, Medical 25%, Consumer non-durable 23%, Industrial 13%, other 12%; systems 60% / parts & consumables 40%. Group revenues reconcile to XBRL (RevenueFromContractWithCustomerExcludingAssessedTax).

### A3. Profitability

| Period | GAAP operating profit (margin) | EBITDA non-GAAP (margin) | GAAP diluted EPS | Adjusted EPS | Segment EBITDA margins IPS / MFS / ATS |
|---|---|---|---|---|---|
| FY2023 | 672.8 (25.6%) | 819.0 (31%) | 8.46 | 9.85 (revised definition) | 36% / 37% / 23% (orig.) |
| FY2024 | 674.0 (25.1%) | 849.2 (32%) | 8.11 | 9.73 | 37.2% / 36.9% / 21.7% (recast) |
| FY2025 | 711.7 (25.5%) | 899.5 (32%) | 8.51 | 10.24 | 37.1% / 37.3% / 23.5% |
| Q3 FY2026 | 223.1 (27.3%) | 262.5 (32%) | 2.73 | 3.25 | 35% / 38% / 30% |
| 9M FY2026 | 586.7 (26.3%) | 700.7 (31%) | 7.20 | 8.48 | 35% / 37% / 27% |
| FY2026 guidance | — | — | — | $11.80–12.00 (from $10.80–11.50 on 10 Dec 2025; raised 18 Feb, 20 May, 19 Aug 2026) | — |

### A5. Cash and capital (USD millions)

| Item | FY2023 | FY2024 | FY2025 | 9M FY2026 |
|---|---|---|---|---|
| Operating cash flow | 641.3 | 556.2 | 719.2 | 570.5 |
| Capex | 34.6 | 64.4 | 58.1 | 40.3 |
| Free cash flow (computed OCF − capex) | 606.7 | 491.8 | 661.1 | 530.2 |
| Share repurchases (cash) | 89.7 | 33.3 | 306.4 | 158.8 |
| Dividends paid | 150.4 | 161.4 | 179.1 | 137.4 |
| Net debt / leverage at period end (NORDSON) | $1.6B / 2.0x | $2.1B / 2.5x | ~$1.9B / 2.1x | ~$1.6B / 1.7x (31 Jul 2026) |

Capital events: CyberOptics (closed 3 Nov 2022; $377.8M net); ARAG (closed 24 Aug 2023; ~€957M); Atrion (closed 21 Aug 2024; $790.0M net); $850M bonds (Sep 2023); $600M 4.5% notes (Sep 2024); medical contract-manufacturing divestiture (2 Sep 2025; "roughly $30 million in net proceeds"); $1.2B revolver to 30 Jan 2031 (30 Jan 2026); CapstanAG (16 Mar 2026); $1.2B commercial paper program (2 Jun 2026); quarterly dividend +15% to $0.94 (27 Aug 2026); Contrinex (23 Oct 2026; EV ~$168M). Target leverage "2 times to 2.5 times" (29 May 2025). Goodwill $3,315.8M at 31 Jul 2026 (XBRL). Backlog +35% YoY entering Q4 FY2026.

---

## 7. Module B — claims ledger and handoff row

LEDGER_PLACEHOLDER

---

## 8. Access limits that affect this file

- nordson.com, investors.nordson.com, businesswire.com and semi.org returned HTTP 403 to automated fetches; Nordson text was read from verbatim mirrors (3D InCites, Semiconductor Digest, I-Connect007, semiconductorpackagingnews.com PDFs, Nasdaq.com release copies, Nordson IR CDN PDFs). `[idx]` rows depend on search-engine summaries.
- www.sec.gov documents were read through a fetch tool that summarises and truncates long quotes; data.sec.gov XBRL and submissions JSON were read directly. The contact email in `research/CLAUDE.md` was not sent to any service.
- Firecrawl and Exa were out of credits during the main research pass; the Wayback Machine was unreachable.

## 9. Key sources (one URL per document; full lists in `notes/`)

- Nordson FY2025 10-K: https://www.sec.gov/Archives/edgar/data/72331/000007233125000144/ndsn-20251031.htm
- Nordson FY2025 Annual Report to Shareholders (SpinSAM in CEO letter): https://www.sec.gov/Archives/edgar/data/72331/000119312526014673/d69179dars.pdf
- Nordson Q3 FY2026 release (8-K Ex. 99.1, 19 Aug 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000052/ndsn-q320268kxex991.htm
- Nordson Q3 FY2026 10-Q: https://www.sec.gov/Archives/edgar/data/72331/000007233126000054/ndsn-20260731.htm
- Nordson 8-K 23 Oct 2026 (Contrinex): https://www.sec.gov/Archives/edgar/data/72331/000007233126000063/ndsn-20261023.htm
- Nordson Q4/FY2026 earnings-date release (6 Nov 2026): https://investors.nordson.com/news/news-details/2026/Nordson-Corporation-Announces-Earnings-Release-and-Webcast-for-Fourth-Quarter-and-Fiscal-Year-2026/default.aspx
- Nordson investor presentation 20 Aug 2026: https://s202.q4cdn.com/528247721/files/doc_financials/2026/q3/FY26-Nordson-Investor-Presentation-8-20-26.pdf
- XBRL companyfacts: https://data.sec.gov/api/xbrl/companyfacts/CIK0000072331.json
- Call transcripts (TickerTrends): https://tickertrends.io/transcripts/NDSN/Q3-earnings-transcript-2026 (and Q2-2026, Q1-2026, Q4-2025, Q3-2025, Q2-2025 at the same path pattern)
- SpinSAM launch preview (Semiconductor Digest, 10 Jun 2024): https://semiconductor-digest.com/?p=27025
- SpinSAM technical article (Semiconductor Digest, 9 Jan 2025): https://semiconductor-digest.com/?p=29607
- 3D InCites podcast with B. Schackmuth (17 Apr 2025): https://www.buzzsprout.com/1731672/episodes/16985846
- Nordson SEMICON Taiwan 2025 release (HBM named): https://www.3dincites.com/?p=113701
- Nordson productronica/SEMICON Europa 2025 release PDF: https://www.semiconductorpackagingnews.com/uploads/2/Nordson_Productronica_25_Final.pdf
- SonoFlex launch (I-Connect007, 21 Sep 2026): https://iconnect007.com/article/151665/nordson-test-inspection-to-unveil-sonoflex-acoustic-inspection-system-at-semicon-west-2026/151662/smt
- XM8000 launch (Nordson IR, 17 Jan 2014): https://investors.nordson.com/news/news-details/2014/Nordson-DAGE-Launches-the-XM8000-Wafer-X-ray-Metrology-Platform/default.aspx
- XM8000 Pro product page: https://www.nordson.com/en/products/test-and-inspection-products/axm-xm8000-pro
- Bernard & Blish, EPTC 2005: https://smtnet.com/library/files/upload/Minimising-radiation-doses.pdf
- Data I/O + Nordson DAGE, IPC APEX 2024: https://www.electronics.org/system/files/technical_resource/E41%26S24_01%20-%20Dave%20Rohona.pdf
- IMAPS 2016 NOR/NAND X-ray study: https://imapsource.org/article/56080-effects-of-x-ray-exposure-on-nor-and-nand-flash-memories-during-high-resolution-2d-and-3d-x-ray-inspection.pdf
- NXP AN13412: https://www.nxp.com/docs/en/application-note/AN13412.pdf
- CyberOptics 10-K FY2021: https://www.sec.gov/Archives/edgar/data/768411/000089710122000230/cybe-20211231.htm
- CyberOptics DEFM14A: https://www.sec.gov/Archives/edgar/data/768411/000110465922102995/tm2225036-4_defm14a.htm
- PVA TePla Autowafer 300 flyer: https://www.pvatepla.com/fileadmin/sitepackage/pdf/flyer/PVA_Autowafer_300.pdf
- PVA TePla Capital Markets Day deck (2 Sep 2025): https://www.pvatepla.com/fileadmin/sitepackage/pdf/Pr%C3%A4sentationen/PVA-TePla-CMD-2025-online.pdf
- PVA TePla H1 2026 release: https://www.pvatepla.com/fileadmin/sitepackage/pdf/investor_relations/presse/2026/PR_PVA_TePla_Results_H1_2026.pdf
- Hitachi FineSAT7 release (29 Aug 2022): https://www.hitachi.com/en/press/articles/2022/08/0829/
- NIST bond-void round robin: https://www.nist.gov/publications/round-robin-experiment-support-bond-void-measurement-standards
- Onto EchoScan release mirror (14 Jan 2025): https://www.3dincites.com/?p=105827
- The Elec on Samsung hybrid-bond inspection (31 Mar 2026): https://www.thelec.net/news/articleView.html?idxno=6232
- Maeil Business on Korean HBM C-SAM (21 May 2025): https://www.mk.co.kr/news/business/11323116
- Camtek 20-F FY2024: https://www.sec.gov/Archives/edgar/data/1109138/000117891325000945/zk2532834.htm
- Onto Dragonfly G5 launch: https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Launches-Dragonfly-G5-Inspection-System-2026.pdf
- KLA 10-K FY2026: https://www.sec.gov/Archives/edgar/data/319201/000031920126000027/klac-20260630.htm

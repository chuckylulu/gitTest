# Nordson Corporation (NDSN) — Test & Inspection, Advanced Technology Solutions (ATS) segment

Compiled 2026-11-21. Fiscal year ends 31 October. USD. Raw dated facts; no opinions, prices or multiples. "NOT DISCLOSED (checked: …)" = searched and absent. "(computed)" = arithmetic by the compiler from reported figures. Speaker labels: NORDSON / CUSTOMER / COMPETITOR / INDEPENDENT / SECONDARY. `[idx]` = wording taken only from a search-engine summary of a nordson.com page that returned HTTP 403; re-check against the live page.

**Rules applied.** `research/CLAUDE.md` still contains the placeholder "TODO: paste the rules block here", and `research/prior/` is empty. The rules applied are the "Global Chat Rules" used in the user's recent AI Studio prompts: raw dated primary facts, no adjectives or valuation, one URL per document, explicit absence markers. Module A items A1/A3/A5 and Module B are not defined in any file found. The scope used here is an assumption (the user stated no preference): **A1 = revenue and segment mix, A3 = profitability, A5 = cash and capital; Module B = claims ledger (claim | evidence for | evidence against | verdict | what would settle it) plus one handoff row.** Re-run sections 6–7 once the real rules block is pasted.

Supporting files: `notes/q1_q2_acoustic.md`, `notes/q3_xray.md`, `notes/q4_optical.md`, `notes/q5_financials.md` hold the first-pass tables and every URL. `verification.md` holds the adversarial re-check: 37 load-bearing facts re-read against sources, 26 CONFIRMED and 11 CORRECTED, 0 refuted. The corrections are applied in this file, not in the notes. It also holds the claims-ledger adjudication and the gap-fill results.

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
| **SpinSAM** (300 mm, 4 spin-scan stages, EFEM) | Nordson release dated "June 2024" (mirrors 10 Jun 2024): "will be unveiled in a video presentation for the first time" at SEMICON West 2024 (9–11 Jul 2024, Moscone, booth 1233). Listed for the SEMICON Taiwan 2024 booth (4–6 Sep 2024). 2024 Best of West finalist (8 Jul 2024); 2024 Global Technology Award (release 30 Oct 2024). | NOT DISCLOSED for SpinSAM. Nordson: "widest frequency range ever achieved in a production environment". Nordson acoustic product manager, product not named (SemiEngineering, 10 Nov 2026): "We can go up to our 165 MHz transducer, which gets you down to a resolution of 12 microns ... if you had a 5-micron defect, we could detect it, but not measure it accurately." General range "15 megahertz up to about 300 megahertz" (podcast). | NOT DISCLOSED as a SpinSAM void spec. Podcast (17 Apr 2025): "we can see down to that 10 micron defect size" (stated apart from the 41 WPH figure). General AMI (10 Nov 2026): lateral "5 µm to 10 µm", gap "at least 0.1 µm thick". | "up to 4 (300mm) wafers simultaneously at 41 wafers per hour"; "at 100 micron resolution about 41 wafers per hour, which is, I think, eight times faster than our previous machine" (AW300); full-wafer scan "less than 6 minutes". Finest pixel "about 10 micron"; **WPH at 10 µm or 50 µm: NOT DISCLOSED**. Each scanner runs at its own resolution (examples 100 µm, 50 µm); with one scanner removed "throughput can still run smoothly at 75%"; "lower resolution scan in the center ... maximize the resolution towards the edge". Roadmap "about two times that throughput" (Apr 2025); 41 WPH still stated 21 Sep 2026. | "4 matched waterfall transducers"; "Waterfall transducer provides non-immersion scanning which minimizes risks of contamination and false bond indications"; "limits the exposure to water versus some competitors that are using water bath or immersion scanning"; waterfall "standard on production systems"; deionized water. Drying step: NOT DISCLOSED. | NOT DISCLOSED in mm. Perimeter scan region, e.g. "the last 10 millimeters at the wafer's edge" (scan band, not an exclusion); "edge scanning that targets defect prone areas". | CEO, Q1 FY2025 call (20 Feb 2025): "If you think about SpinSam, a new addition, it is not contributing to growth yet, but it positions us really well to continue to grow" (Equibles; TickerTrends renders "SpinSAM and new emission"). Investor Day 3 Oct 2024 process slide labels acoustic at die stacking "LAB". Named customers, orders, qualifications: NOT DISCLOSED (checked: releases 2024–2026, FY2024/FY2025 ARS, 16 calls, podcast, Korean press, SEC full-text search). | "bonded wafers, Chip-on-Wafer, stacked wafers, MEMS, and over-molded wafers"; HBM once ("MEMs HBM wafers", Aug 2025); podcast: "stacked die ... eight stack or 16 stack ... So that's the memory application". **Hybrid bonding: not named. CoWoS: not named for SpinSAM** (named for the XM8000). | NORDSON: release PDF Jun 2024; 3D InCites 1 Nov 2024; Semiconductor Digest 9 Jan 2025 and print Nov/Dec 2024 pp. 22–24; podcast (B. Schackmuth) 17 Apr 2025; 3D InCites 7 Aug 2025; Q1 FY2025 call; Investor Day deck 3 Oct 2024; SemiEngineering 10 Nov 2026; Nordson FY2025 ARS |
| **SpinSAM Lite** | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | [idx] "spin scan up to 2 wafers simultaneously"; "100 μm scan (from wafer load to wafer load) takes less than six minutes" | [idx] matched transducers | NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED | NORDSON [idx] product page |
| **AW300** (predecessor; 2 transducers, raster scan) | Shown at SEMICON West 14–16 Jul 2009 (Sonoscan; "Twin transducers scan two wafer pairs simultaneously"); re-promoted Jul 2012 | NOT DISCLOSED; sell sheet (2009): "500 MHz bandwidth pulser/receiver" | AW300 sell sheet (2009): "can detect voids smaller than 5 microns in diameter between two wafers"; AW200: "inter-wafer voids as small as 5-µm"; AW322 200 (Jun 2014, 200 mm MEMS): "down to 5 microns", "frequencies up to 230 MHz" | Not stated; SpinSAM stated as 8× faster at 100 µm | AW200: "Waterfall transducer"; "After imaging, the wafer pair is automatically dried" | NOT DISCLOSED | NOT DISCLOSED | Bonded wafer pairs up to 300 mm; individual wafers "before bonding" (crack screening); direct-bonded SOI; 3D IC, chip-on-wafer | SST SEMICON West booth guide 15 Jul 2009; MySemiconDaily 9–11 Jul 2012; Silicon Semiconductor 29 Jun 2014 |
| **FACTS2 DF2400** (trays/carriers, not wafers) | Shipping announced Jan 2014 | NOT DISCLOSED | NOT DISCLOSED | "2x to 7x faster throughput than previous systems" (no units/h) | "non-immersion technology"; "dedicated drying areas" | n/a | NOT DISCLOSED | JEDEC trays, flip chips, lead-frame strips, IGBT modules | Microwave Journal 15 Jan 2014 |
| **Gen7 C-SAM** (lab) | 15 Aug 2018 | D9650 sibling [idx] "5 MHz to 230 MHz" | NOT DISCLOSED | n/a (lab); "50% higher screening throughput" vs prior | Waterplume option | n/a | Positioned for "laboratory analysis, failure investigation" (Sep 2026) | Lab / FA | Circuits Assembly 15 Aug 2018; I-Connect007 21 Sep 2026 |
| **SonoFlex** (back-end packages, small panels) | "worldwide debut" SEMICON West 13–15 Oct 2026 (Moscone, booth 5844); also SEMICON Europa 10–13 Nov 2026; [idx] 2026 Best of West award (15 Oct 2026) | NOT DISCLOSED | NOT DISCLOSED | "scanning speeds up to twice as fast as conventional solutions"; multi-system configs "increasing throughput by up to eight times" (no units/h) | NOT DISCLOSED | n/a | NOT DISCLOSED | "back-end advanced semiconductor manufacturing"; small panels | I-Connect007 21 Sep and 16 Oct 2026 |

- Business-level statements (not SpinSAM-specific): "we also have our AMI business, which is our acoustic emission business. There, we are coming off of 2 really strong years of growth" (CEO, Q1 FY2026 call, 19 Feb 2026). In the same answer the CEO described AMI as "acoustic emission-based inspection techniques and optical techniques", so the statement may cover acoustic plus optical. "You typically use acoustic for memory and you use more x-ray for ... logic chips" (CEO, 11 Dec 2025). Investor Day (3 Oct 2024): Acoustic Micro Imaging sits in the "Optical Systems & Metrology" division with WaferSense and optical inspection (28% of ATS sales; period not stated).
- No Nordson product named "Gen8" was found. SpinSAM is the only Nordson SEC-filed product name match (FY2025 ARS, CEO letter: "high throughput and superior sensitivity ... scans multiple wafers simultaneously").

---

## 2. Head-to-head: Nordson vs PVA TePla vs Hitachi (automated wafer-level acoustic)

| Item | Nordson (SpinSAM) | PVA TePla (SAM Auto Wafer / Autowafer 300) | Hitachi Power Solutions (WAFER LINE; FineSAT) | Source |
|---|---|---|---|---|
| Coupling | Waterfall (non-immersion), 4 transducers | Autowafer 300 flyer (Mar 2026): "Non-immersion waterfall design"; "spin dryer"; "dual arm robot for wet and dry"; optional "Nearly dry process with DLIC technology"; C2W talk: water "only applied locally on the carrier side ... chips side remains dry" | WAFER LINE: coupling NOT DISCLOSED; FineSAT7 is a water-tank lab tool ("Larger water tank ... 300 mm") | flyer PDF; IEEE.tv 17 Jan 2025; Hitachi 29 Aug 2022 |
| Wafers in parallel | 4 (SpinSAM), 2 (Lite [idx]) | "Scanning up to 2 wafers simultaneously" (Autowafer 300); "four dual array transducers ... up to 400 MHz" (SAM Auto Wafer page) | NOT DISCLOSED; array probe 25/50/75 MHz (FineSAT Hybrid) | vendor pages |
| Resolution / void claim | ~10 µm pixel finest; void NOT DISCLOSED | "Minimum Resolution 0.5 µm/pixel" (flyer); CMD 2 Sep 2025: SAM "Resolution: 5–15 µm"; hybrid-bond talk: "push ... to the 5µm limit", UHF tonebursts "down to 1µm" for thinned chips | Patent award 14 Jun 2023: automatic detection of defects "直径10µm程度" (~10 µm diameter) at wafer bond interface | PVA flyer/CMD/IEEE.tv; Hitachi 14 Jun 2023 |
| WPH | 41 at 100 µm | NOT DISCLOSED | NOT DISCLOSED | — |
| Vendor-stated comparison | NORDSON (Semiconductor Digest print, Nov/Dec 2024): "41 wafers per hour, which is a throughput of around four to five times that achievable via competitive offerings" (competitors and settings not named) | CMD 2 Sep 2025: SAM "Best balance of resolution, depth, and speed"; "unmatched price-performance ratio" (no numbers) | NOT FOUND | as cited |
| Production / qualification status | CEO 20 Feb 2025: SpinSAM "not contributing to growth yet"; later status NOT DISCLOSED | Edison (SECONDARY, 26 Mar 2026): qualified at "a Taiwanese foundry, a US IDM/foundry and a Korean memory player, with a system shipped for HVM". PVA FY2025 deck (19 Mar 2026): "First metrology orders for HBM; will be shipped in 2027". Metrology order intake €97.7M H1 2026 (H1 2025: €53.3M); €148.4M 9M 2026 (+76%); "The dominant share of order intake now comes from high-volume manufacturers in the logic and memory sectors for fully automated ultrasonic systems" (5 Nov 2026) | WAFER LINE: "continuous operations on several customers' mass-production lines" (unnamed; page ©2016). Hitachi Review (Apr 2024): SATs mainly used at the packaging stage for fault analysis and screening; FineSAT 7 image of a 5-µm artificial defect inside bonded wafers. | Nordson Q1 FY2025 call; Edison; PVA FY2025 deck, H1 2026 report, Q3 2026 statement; Hitachi page and Review |
| Published comparison naming the three vendors | NOT FOUND (checked: NIST/SEMI bond-void round robin 2016, ISTFA, SPIE/imec abstracts, SemiEngineering 2025–2026, PVA CMD deck and reports, Edison notes, Korean press). NIST round robin (tools anonymized): minimum sensitivities "range from 1 µm to 25 µm"; "key trade-off ... between speed of measurement and resolution". | same | same | NIST pub. 1 May 2016 |
| Shared customers | No vendor names a fab. Maeil Business (SECONDARY, 21 May 2025): Korean HBM C-SAM had relied on "Sonix and Sonoscan of the US and Hitachi of Japan" (customer unnamed). | Customers unnamed | Customers unnamed | Maeil 21 May 2025 |
| Pricing indications | NOT DISCLOSED | Per-tool price NOT DISCLOSED; order values given without unit counts (not divisible). CMD: SAM market $327M (2024) / $333M (2025), PVA share 22% (company estimate). | FineSAT7 (lab): "28.5 million yen ～" before tax (from 1 Oct 2022). WAFER LINE price NOT DISCLOSED. | Hitachi 29 Aug 2022; PVA CMD 2 Sep 2025 |
| Dry alternative (context) | — | — | — | Onto EchoScan release (14 Jan 2025): "detect 1µm voids in atmosphere at the same speed as incumbent technologies limited to ~10µm"; "Current technologies are limited to ≥10µm void size sensitivity and require water immersion" (the release names "current technologies", not acoustic, and does not describe the method). Onto SPIE abstract (24 Feb 2026): picosecond laser acoustics, "coupling-free", "voids as small as 1 µm". The Elec (31 Mar 2026, SECONDARY): Onto in a JDP with Samsung; laser-ultrasound equipment "already supplied ... for use in production lines". |

---

## 3. X-ray (former Dage / Matrix): automated wafer X-ray metrology and inspection

| Product | Launch | Source / resolution | Smallest void / feature | Wafers per hour (settings) | Handling | Edge exclusion | Status at customers | Applications named | Stated dose to memory / measures | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| **XM8000** (wafer X-ray metrology) | Nordson IR release 17 Jan 2014 (timed to SEMI European 3D TSV Summit, Grenoble, 20–22 Jan 2014); a 3D InCites award page gives "introduced to the market on 6/24/2013". 2017 Global Technology Award (metrology), 14 Nov 2017. | Sealed-transmissive tube above wafer, detector below; kV NOT DISCLOSED. Investor Day 2024: detector "2 Mpixel", resolution "0.2µ/pixel", accuracy "3µ" | Release: measures "voiding and fill levels, overlay, critical dimensions"; no µm void figure. SECONDARY (3D InCites, 24 Jan 2014, author's rendering of P. Moyse, Nordson DAGE): "The number and size of every void on every bump". | NOT DISCLOSED. Release: "measures the invisible – fast". SECONDARY (3D InCites 24 Jan 2014): "20x faster than the Diamond"; Oct 2017: "30X faster than traditional X-ray" | SECONDARY (3D InCites): "handling wafers up to 300mm"; "fully compliant with the front-end fab environment" | NOT DISCLOSED | Order from "a major customer in the semiconductor industry" (Nov 2014); "a number of tools have been sold" (Mar 2015); Korea clean-room demo facility (Jun 2016). No named customer. | TSVs, wafer bumps, 2.5D/3D IC, MEMS; overlay | "radiation safe defect detection" (Oct 2017); Investor Day 2024: "X-ray dose monitoring: No" | Nordson IR 17 Jan 2014; 3D InCites 24 Jan 2014; Electronic Specifier Nov 2014; iConnect007 12 Oct 2017; Nordson IR 27 Nov 2017 |
| **XM8000 Pro series** (XM8000-5, -7 Pro, -7P Pro) | First dated presentation: "New XM8000 Pro", Nordson Investor Day, 3 Oct 2024 (slide 60). Name "XM8000Pro" first in a Nordson show release for SEMICON West 2026 (13–15 Oct 2026); 2025 releases say "XM8000 Automated X-Ray Metrology (AXM)". | Investor Day 2024 vs XM8000: detector "6.5 Mpixel" vs 2; resolution "0.13µ/pixel" vs 0.2; accuracy "2µ" vs 3µ; [idx] NT100M LaB6 tube "10 times brighter"; 2025 releases: "powered by the QuadraNT tube and detector"; kV NOT DISCLOSED | [idx] "100nm defect recognition"; "sub micron level 3D reconstruction"; smallest void in µm NOT DISCLOSED | NOT DISCLOSED as WPH. Investor Day 2024: speed "2x" vs XM8000 "1x". Sep 2026 release: "production-speed throughput" (no number). | [idx] projection angles up to 45°; -7P with EFEM supports panels to 510 × 515 mm; FOUP count NOT DISCLOSED | NOT DISCLOSED | NOT DISCLOSED (checked: releases 2014–2026, Investor Day 2024, FY2024/FY2025 ARS, 10-Ks, 16 calls, trade press). Not in the list of systems at Nordson's Phoenix Center of Excellence (24 Aug 2026). | "CoWoS, TSVs, 2.5 and 3D IC packaging and wafer bumps" (Oct 2025); Wafer-Level and Panel-Level Packaging (Sep 2026); [idx] image caption "HBM Shield In Situ" (undefined). Hybrid bonding: not named. | Investor Day 2024: "X-ray dose monitoring: Yes". [idx] "IC-Safe Technology ... allows products to be safely inspected in-line without risk of radiation damage"; "IC-Safe shields completely eliminate radiation exposure to all other device samples not under test". Dose per image/site/wafer, IC-Safe filter material: NOT DISCLOSED. | Investor Day deck 3 Oct 2024 slide 60; [idx] nordson.com XM8000 Pro page; Nordson productronica 2025 release PDF; iConnect007 21 Sep 2026 |
| **Quadra W8** (lab-based automated wafer X-ray) | Trade press 9 Oct 2018 | Aspire 6.7 MP detector | "defects as small as 0.1µm" (conditions not stated) | NOT DISCLOSED | Dual-port EFEM, from FOUP, SECS/GEM, SEMI S2/S8 | NOT DISCLOSED | NOT DISCLOSED | Bumps, TSV, MEMS, 2.5D/3D WLP | NOT DISCLOSED | Circuits Assembly 9 Oct 2018 |
| Quadra 7 Pro (manual; context) | 2023 award | Directory: 30–160 kV, 20 W | n/a | n/a | Manual | n/a | n/a | HBM micro-bump arrays (Nordson article, SemiEngineering 9 Jun 2026) | Quadra tools (Nordson Dage, 27 Mar 2019): "Low dose mode"; "dose calculation tool"; zinc filter tray "can reduce overall X-ray dose by up to 80%" | Dataweek 27 Mar 2019 |
| AXI X# / XS + Dynamic Planar CT (board/tray inline; not a wafer handler) | DPCT "next-generation" (Oct 2025) | NOT DISCLOSED | [idx] flip-chip bumps "down to 40 micron" | "up to 2× faster image acquisition than classical Planar CT" | Boards/trays | n/a | NOT DISCLOSED | Flip-chip micro-bumps | DPCT "crucially reducing sample radiation dose" (no number); [idx] "low dose radiation filters" | productronica 2025 release PDF |

Dose evidence (memory):

| Study | Figure | Speaker | Date |
|---|---|---|---|
| Bernard (Dage Precision Industries) & Blish (AMD), SMTA International Sep 2003 (also IEMT 2003; EPTC 2005 pp. 697–704) | Table citing a JPL/NASA document: random total-dose thresholds Flash 5,000–15,000 rad(Si) = 50–150 Gy(Si); DRAM 15,000–50,000 rad(Si) = 150–500 Gy(Si). "a compromise of ~ 100 – 150 µm thickness of zinc as the filter is proposed. This will reduce the dose to the susceptible silicon by a factor ~ 100 X" | NORDSON (predecessor) co-authored | 2003 |
| Rohona (Data I/O) & Bastin (Nordson DAGE), IPC APEX EXPO 2018 | Managed NAND (15/20 nm, automotive) "exposed to an estimated 20,000 RADS" (= 200 Gy) failed verification; recommended "Tube voltage: 60KV", "Tube power: 2 Watts", "Distance to target: 12.4 millimeters is typical", "Filtering (Zinc): 150 Micron is a must" | NORDSON co-authored | 2018 |
| Microchip AN4153 Rev. G (SmartFusion2/IGLOO2 flash FPGAs) | "Set a limit of 15 rads using a zinc filter tray"; test system named: Nordson DAGE Quadra 7 | CUSTOMER (device maker) | Nov 2023 |
| Nordson, "Overview Of Radiation Dose During X-ray Inspection Of Electronics" | Covers "typical dose tolerance limits" and dose-reduction methods; full paper behind a nordson.com form (HTTP 403); figures NOT READ | NORDSON | 9 Dec 2025 |
| Sharma et al., IMAPS 2016 | NAND first byte errors at "75-150 Gy"; NOR "250-450 Gy"; normal 2D inspection "~ 15-20 Gy" | INDEPENDENT | Oct 2016 |
| NXP AN13412 | "A total dose << 1 Gy (including rework / re-inspection) is recommended." | INDEPENDENT (device maker) | 8 Oct 2021 |
| UAH, IEEE IMW 2023 | 3D TLC NAND bit errors after TID 10 krad(Si) (Co-60 gamma, not X-ray) | INDEPENDENT | May 2023 |
| HBM / hybrid-bonded DRAM wafer X-ray damage threshold | NOT FOUND (checked: SemiEngineering 2024–2026, Nordson HBM article 2026, NXP, IMAPS, IMW, patents) | — | — |

- Nordson business statements on X-ray: FY2025 10-K: ATS growth "partially offset by weakness in x-ray inspection systems"; Q1 FY2026 call: "Our X-ray systems ... are starting to inflect"; "the semi side of X-ray is doing really well and the auto is flattish".
- Competing 300 mm wafer X-ray tool announced in the same period: ZEISS NLX, press release 12 Oct 2026 ("designed for 300-millimeter wafers and supports both the development of new processes and high-volume production"); "3D X-ray laminography" and "X‑Guard dose control for sensitive areas" appear on the undated product page, not in the release (COMPETITOR).
- Investor Day 2024 (slide 59): X-Ray & Test Systems division (automated X-ray metrology, automated X-ray inspection, manual X-ray) = 35% of ATS sales (period not stated). Slide 62: "X-Ray & Test Division Sales Growth 5% EBITDA Margin Expansion 1500 bps" for 2019 to TTM Q3 FY2024 (whether 5% is a CAGR is not stated).

---

## 4. Optical (former CyberOptics): sensors and wafer bump inspection; overlap with Camtek, Onto, KLA

| Product | Launch | Key specification (vendor) | Status at customers | Applications named | Source |
|---|---|---|---|---|---|
| **WX3000** (2D/3D wafer bump inspection & metrology; NanoResolution MRS sensor) | Release 8 Jul 2020 (virtual SEMICON West 20–23 Jul 2020) | "100% 3D and 2D inspection and metrology simultaneously ... more than 25 wafers per hour"; features "down to 25 microns"; "in excess of 75 million 3D data points per second"; 12"/8" and 8"/6" versions. Product-page table (snippet only): ≥25 WPH 300 mm 3D+2D, ≥55 WPH 200 mm; 3D accuracy 0.2 µm; repeatability 0.3 µm @3σ; bump height range 25–250 µm. | First PO from "a large integrated device manufacturer" (27 Oct 2021), "one of the top 10 in the world", which "looked at competitive systems really chose WX because of its speed"; PO value "more than $0.5 million and less than $1 million" (CyberOptics CEO, 17 Feb 2022). Second user: a Chinese OSAT via a Chinese system integrator buying sensor and software only. IDM system delayed by lockdowns (28 Apr 2022); "one order for the finished WX system ... to fulfill ... this quarter" (Q3 2022, call 27 Jul 2022). Later status: NOT DISCLOSED (checked: Nordson 10-K FY2022–FY2025, releases, 16 calls; WX3000 not named on any Nordson call). No WX-series tool in Nordson SEMICON West 2025/2026 lists. Nordson CEO at the deal (23 Aug 2022): CyberOptics' wafer-level business mostly sells "the MRS sensor, to their customers who build the broader system". | Wafer bumps, solder balls, gold bumps, Cu pillars, microbumps, interposers. HBM / hybrid bonding / CoWoS / fan-out: NOT DISCLOSED. | CyberOptics 10-K FY2021 (11 Mar 2022); CyberOptics releases and calls Q3 2021–Q2 2022 (TickerTrends); Nordson Q3 FY2022 call |
| **3D MRS / NanoResolution sensors** (sold to OEMs) | NanoResolution: SEMICON West Jul 2019 (Best of West 2019) | Nine MRS models; 3 µm-pixel NanoResolution sensor | KLA: 2015 "mutually exclusive agreement to supply 3D sensor subsystems" for "KLA-Tencor BEOL package inspection systems"; KLA = 10% of CyberOptics 2018 revenue; still named FY2019 10-K. Three unnamed OEMs ordered NanoResolution (FY2019 10-K). Post-Nov 2022 OEM sales/customers: NOT DISCLOSED. | Semiconductor component package inspection | CyberOptics 10-K FY2018, FY2019, FY2021; Silicon Semiconductor 20 Jan 2015 |
| **SQ3000+ / SQ7000+** (AOI/SPI/CMM) | SQ3000+ Oct 2021. SQ7000+: earliest reachable mention is Nordson's IPC APEX 2025 pre-show release (show 18–20 Mar 2025), which does not call it new | SQ3000+ features "down to 50 microns"; SQ7000+ "an even higher resolution" MRS sensor; "5-micron MRS sensor" only on the product page [idx] | SQ7000+: unnamed "global GPU leader" (Nordson case study 30 Sep 2025, snippet) | "advanced packaging, advanced SMT, socket metrology, memory, mini/microLED" (APEX 2025) | Nordson APEX 2025 release (reprint 4 Mar 2025); SEMICON West 2025 release |
| **WaferSense / ReticleSense** (wireless in-tool sensors: leveling, gapping, teaching, vibration, particles) | Since 2000s; ATS2 (2023), AGS2 and ACS (2025) | — | "Most of the world's largest manufacturers of semiconductors and semiconductor equipment purchase our WaferSense products" (CyberOptics, 2022); named customers NOT DISCLOSED | Front-end fab tool set-up and diagnostics | CyberOptics 10-K FY2021; Nordson releases 2023, 2025 |

CyberOptics revenue by product line (USD thousands; last disclosures before the acquisition):

| Line | 2019 | 2020 | 2021 | H1 2022 |
|---|---|---|---|---|
| High-precision 3D/2D sensors | 12,579 | 17,522 | 25,941 | 14,887 |
| Inspection & metrology systems (SQ3000, WX3000) | 32,713 | 37,547 | 42,958 | 22,759 |
| Semiconductor sensors (WaferSense) | 13,971 | 15,048 | 23,875 | 14,169 |
| **Total** | 59,263 | 70,117 | 92,774 | 51,815 |

Shares of 2021 revenue: 3D MRS sensors 19%, SQ3000 24%, WaferSense 26% (computed from table: 25.7%). WX3000 revenue NOT DISCLOSED. NanoResolution sensor price: "$100,000 to $120,000 price point range" (CyberOptics CEO, 18 Feb 2021). Deal: $54.00/share; "approximately $100 million in annual revenue"; aggregate price $377,843k net of $40,890k cash; closed 3 Nov 2022; goodwill $279,630k preliminary (FY2023 10-Qs) and $285,330k final ("As of October 31, 2023, the purchase price allocation is final", FY2023 10-K). Management forecast in DEFM14A: revenue $106.9M (2022), $123.0M (2023), $142.0M (2024). Investor Day 2024: Optical Systems & Metrology division (WaferSense, optical inspection and metrology, Acoustic Micro Imaging) = 28% of ATS sales (period not stated).

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
| 3 Oct 2024 | Investor Day deck (slides 54, 56, 59, 60, 62, 78) | **Only division split found.** ATS divisions "% OF SALES" (period not stated): Electronics Processing Solutions (EPS) 37%; **X-Ray & Test Systems (XRT) 35%** (automated X-ray metrology, automated X-ray inspection, manual X-ray); **Optical Systems & Metrology (OSM) 28%** (WaferSense, optical inspection and metrology, Acoustic Micro Imaging). XRT + OSM = 63% (computed). "X-Ray & Test Division Sales Growth 5% EBITDA Margin Expansion 1500 bps" (2019 to TTM Q3 FY2024). ATS TTM Q3 FY2024 revenue $503M, EBITDA 21% (12% in FY2019). Semiconductors "50% of ATS Sales" (earliest dated instance). Process-flow slide labels acoustic at die stacking "LAB". Dollar revenue of XRT or OSM: NOT DISCLOSED. |
| 18 Dec 2024 | FY2024 10-K (goodwill test, 1 Aug 2024) | "ATS - Test & Inspection": goodwill $375,707k; headroom 173%. ATS FY2024 organic −11.4% "driven by lower demand in electronics dispense product lines as well as test and inspection product lines". From FY2025 the reporting units equal the three segments. |
| 20 Feb 2025 | Q1 FY2025 call (CFO D. Hopgood; CEO) | "double-digit declines in electronics processing and x-ray product lines"; CEO: "If you think about SpinSam, a new addition, it is not contributing to growth yet, but it positions us really well to continue to grow" |
| 29 May 2025 | Q2 FY2025 call (CFO) | "electronics dispense, optical, and x-ray inspection systems, all growing double-digits" |
| 29 May 2025 | Q2 FY2025 call (CEO); May 2025 deck | "50% of our business would be semiconductor high-power computing" (ATS), vs "20% to 30%" four to five years earlier; deck: Semiconductors "50% of ATS Sales" |
| 10–17 Dec 2025 | Q4 FY2025 release; FY2025 10-K | "fewer deliveries of test and inspection systems, particularly x-ray systems"; FY2025: "partially offset by weakness in x-ray inspection systems" |
| 11 Dec 2025 / 19 Feb 2026 | Calls (CEO) | Semiconductor applications "approximately 50% of ATS revenue"; automotive "about 15%" (11 Dec 2025) |
| 21 May 2026 | Q2 FY2026 call (CEO); Q2 FY2026 10-Q | "In terms of number of applications, if you think about this business, over 50% of this business is in semiconductor now" (framed by number of applications, not revenue). 10-Q: Q2 ATS organic +8.5% "driven by ongoing growth in electronics dispense systems"; T&I not named. |
| 19–20 Aug 2026 | Q3 FY2026 release and 10-Q; Aug 2026 deck | ATS organic +30.9% (Q3) and +20.1% (9M) "driven by strong growth in electronics dispense and test and inspection product lines" / "exceptional growth in electronics dispense and test and inspection product lines"; deck: ATS = Semiconductors 50%, General Electronics 25%, Automotive Electronics 10%, Industrial 15%; ATS geography Asia 67% |
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

"HBM" / "high bandwidth" / "CoWoS" / "hybrid": **0 mentions in all six calls** on five transcript hosts (TickerTrends, Equibles, AlphaStreet, fool.com where available, Longbridge). Also absent from the FY2025 10-K and the 2024–2026 investor decks and FY2026 releases. Every quote below was matched on at least two hosts other than TickerTrends; the wording variants are listed in `verification.md` §3c (G4). Call dates are confirmed from the release texts.

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

Each claim was argued by an independent FOR advocate and AGAINST advocate. A judge then spot-checked the key sources and ruled. Full reasoning, rejected points and every source are in `verification.md` §2. Verdict scale: SUPPORTED / PARTLY SUPPORTED / UNPROVEN / CONTRADICTED.

### 7a. Claims ledger

| # | Claim | Evidence for | Evidence against | Verdict (confidence) | What would settle it |
|---|---|---|---|---|---|
| B1 | SpinSAM reaches production throughput without losing sensitivity to the smallest voids customers specify. | NORDSON: 41 WPH "at 100 micron resolution" (podcast 17 Apr 2025; releases Jun 2024–Sep 2026); "we can see down to that 10 micron defect size" (same podcast, stated apart from the WPH figure). COMPETITOR (Onto, 14 Jan 2025): incumbents at production speed "limited to ~10µm", so ~10 µm is the production-class level. | No source gives WPH and minimum void at the same settings; WPH at 10 µm or 50 µm NOT DISCLOSED. Nordson's own method trades resolution for speed (low resolution in the centre, high at the edge). INDEPENDENT (IEEE EPS summary of ECTC 2025 hybrid-bonding session): CSAM "has a resolution limit of approximately 10 µm, often insufficient for detecting voids in contemporary hybrid-bonded devices ... need for post-bonding metrology to detect sub-micron size voiding". COMPETITOR (PVA TePla, Jan 2025): leading edge requires "below 10µm ... may decrease even below 5µm". SECONDARY (TechSearch citing KLA): hybrid-bond interface defects "Sub-micron". INDEPENDENT (NIST): speed vs resolution trade-off. CEO, 20 Feb 2025: SpinSAM "not contributing to growth yet"; no customer, qualification or production use disclosed; "two times" throughput roadmap (Apr 2025) unpublished by Sep 2026. No fab-published void specification found. | **UNPROVEN** (medium); evidence leans against for hybrid-bond void sizes | WPH and minimum detected void from the same recipe (frequency, pixel, centre/edge mode) on a programmed-void reference wafer; a Nordson datasheet with WPH at ≤10 µm and MHz; a fab or OSAT void threshold for the step SpinSAM serves; a disclosed SpinSAM qualification or production release |
| B2 | Wet acoustic inspection is acceptable for hybrid-bonded wafers. | SAM is used on hybrid-bonded wafers. CUSTOMER (Samsung, SPIE 2025): SAM void maps of hybrid Cu-bonded 3D NAND "after annealing". CUSTOMER (STMicroelectronics, Dec 2020): "Standard bonding defect control is done in-line using SAM" (XY resolution 20 µm). INDEPENDENT (imec, ECTC 2024): SAM on D2W hybrid-bonded stacks after each transfer. INDEPENDENT (CEA-Leti, 2017): post-bake acoustic scans of 300 mm W2W hybrid stacks. CUSTOMER via SECONDARY: Intel C-SAM maps after 175/200 °C anneal (ECTC 2026); TSMC SoIC flow uses CSAM (IEDM 2024). COMPETITOR (PVA TePla): "the state of the art for inline metrology on hybrid bonded wafers". Vendors limit water exposure: waterfall (Nordson, PVA), carrier-side-only water for C2W (PVA), gas jet at the wafer edge (Hitachi patent). | None of the fab sources names the couplant, and only Samsung states the anneal state. NORDSON (9 Jan 2025): with immersion "any crack or other defect in the surface could lead to water entering the sample"; unannealed bonded pairs: "separation will often occur". COMPETITOR (Hitachi US 12,422,409 B2, 2025): liquid "infiltrates into a bonded surface between the wafers due to a capillary phenomenon"; before metal bonding, water forms "an oxide film" on the metal. COMPETITOR (PVA): "c2w processes should avoid water on the chip side". COMPETITOR (Sonix patent, 2023): water ingress into bonded BSI/CMOS/MEMS wafers. COMPETITOR (Onto): "contamination, delamination, and corrosion". SECONDARY (The Elec, 31 Mar 2026): Samsung's leading hybrid-bond inspection supplier is Onto's coupling-free laser ultrasound. No fab statement qualifying, accepting or rejecting wet-coupled SAM for hybrid-bonded HBM or W2W/D2W production; no published ingress or corrosion data for any mitigation. | **PARTLY SUPPORTED** (medium): SAM is in use on hybrid-bonded wafers (mostly post-anneal); acceptability of wet coupling in production is not evidenced | A fab process-of-record or qualification naming the post-bond method, the couplant and the anneal state at inspection; split-lot data (bond strength, Cu oxidation, yield, moisture reliability) with and without wet SAM; vendor ingress data for waterfall, carrier-side or air-jet coupling |
| B3 | Test & Inspection grows faster than the rest of its segment because of HBM and advanced packaging. | NORDSON: FY2023 T&I grew while dispense fell ("partially offset by stronger demand in test and inspection product lines", FY2023 10-K; "high-single-digit growth", 22 Aug 2023). 21 May 2026: "there are cases last year, we were growing our test and inspection faster than we were growing our dispense business" (periods unspecified). Q3 FY2026: ATS +30.9% organic "driven by strong growth in electronics dispense and test and inspection product lines". 19 Feb 2026: complex logic-plus-memory stacks create "more opportunities for our test and inspection portfolio". Investor Day 2024: X-Ray & Test division "Sales Growth 5%" (2019–TTM Q3 FY2024) vs ATS 5-year CAGR 4%; not assessed by the judge, because the basis of the 5% is not stated and the period predates the HBM ramp. | NORDSON: "the last 3 quarters, our dispense business is far more robust than our test and inspection business" (21 May 2026); "the dispense business is typically ahead of the curve in terms of growth cycle, and that's what we saw" (20 Aug 2026). Q4 FY2025: dispense strength "more than offset by fewer deliveries of test and inspection systems, particularly x-ray systems". Q2 FY2026 10-Q credits ATS growth to dispense only. The FY2023 outperformance was attributed to lower cyclicality ("It's smaller in T&I"), alongside memory-related optical weakness. X-ray lag attributed to automotive exposure. HBM: 0 mentions on six calls. T&I revenue NOT DISCLOSED. | **CONTRADICTED** (medium) for Q4 FY2025–Q2 FY2026; Q3 FY2026 shows both lines growing with no split; no Nordson statement links T&I outperformance to HBM | Q4/FY2026 release and call (15–16 Dec 2026) or FY2026 10-K MD&A ranking T&I vs dispense; an explicit management attribution to HBM or advanced packaging; a named HBM customer, order or qualification for SpinSAM, XM8000 Pro or another T&I tool |

### 7b. Handoff row

Business-unit (Test & Inspection) cells are NOT DISCLOSED: Nordson reports only the ATS segment. The one exception is a one-off division % split at Investor Day 2024, noted in the "Business-unit split" cell.

| Company | Ticker | FY end | Data as of | Last reported | Next results | Business unit | BU revenue | BU growth | BU margin | BU semi share | Business-unit split (one-off) | Segment | Segment sales LTM to 31 Jul 2026 | Segment organic growth 9M FY2026 | Segment EBITDA margin 9M FY2026 | Segment semi share | Group sales LTM to 31 Jul 2026 | Group EBITDA margin 9M FY2026 | Net debt / leverage 31 Jul 2026 | FY2026 guidance | Wafer-level T&I tools | Customer status of those tools | HBM named, last 6 calls | B1 | B2 | B3 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Nordson Corporation | NDSN | 31 Oct | 2026-11-21 | Q3 FY2026 (8-K 19 Aug 2026) | 15 Dec 2026, after close (Q4/FY2026) | Test & Inspection (ATS) | NOT DISCLOSED | NOT DISCLOSED (qualitative statements only) | NOT DISCLOSED | NOT DISCLOSED (ATS-level only) | X-Ray & Test Systems 35% + Optical Systems & Metrology 28% of ATS sales, period not stated (Investor Day 3 Oct 2024) | Advanced Technology Solutions | $717.4M (computed) | +20.1% | 27% | ~50% of ATS sales | $2,979.8M (computed) | 31% | ~$1.6B / 1.7x | Sales $3,035–3,075M; adj. EPS $11.80–12.00 | SpinSAM (acoustic; 41 WPH at 100 µm); XM8000 / XM8000 Pro (X-ray; speed 2x, dose monitoring on Pro); WX3000 (optical, 2020; no later disclosure) | NOT DISCLOSED for all three (SpinSAM "not contributing to growth yet", 20 Feb 2025) | 0 | UNPROVEN | PARTLY SUPPORTED | CONTRADICTED |

---

## 8. Access limits that affect this file

- nordson.com, investors.nordson.com, businesswire.com and semi.org returned HTTP 403 to automated fetches; Nordson text was read from verbatim mirrors (3D InCites, Semiconductor Digest, I-Connect007, semiconductorpackagingnews.com PDFs, Nasdaq.com release copies, Nordson IR CDN PDFs). `[idx]` rows depend on search-engine summaries.
- www.sec.gov documents were read through a fetch tool that summarises and truncates long quotes; data.sec.gov XBRL and submissions JSON were read directly. The contact email in `research/CLAUDE.md` was not sent to any service.
- Firecrawl and Exa were out of credits during the main research pass; the Wayback Machine was unreachable.
- The session's web-search allowance ran out during the gap-fill pass. Korean, Taiwanese, Japanese and Chinese trade-press and procurement searches for SpinSAM, XM8000 Pro and WX3000 customers and prices were therefore NOT RUN (`verification.md` §3c lists them).
- Nordson papers behind lead forms were not downloaded: the radiation-dose overview (9 Dec 2025) and "Automated X-Ray Metrology ..." (6 May 2026).

## 9. Key sources (one URL per document; full lists in `notes/`)

- Nordson FY2025 10-K: https://www.sec.gov/Archives/edgar/data/72331/000007233125000144/ndsn-20251031.htm
- Nordson FY2025 Annual Report to Shareholders (SpinSAM in CEO letter): https://www.sec.gov/Archives/edgar/data/72331/000119312526014673/d69179dars.pdf
- Nordson Q3 FY2026 release (8-K Ex. 99.1, 19 Aug 2026): https://www.sec.gov/Archives/edgar/data/72331/000007233126000052/ndsn-q320268kxex991.htm
- Nordson Q3 FY2026 10-Q: https://www.sec.gov/Archives/edgar/data/72331/000007233126000054/ndsn-20260731.htm
- Nordson 8-K 23 Oct 2026 (Contrinex): https://www.sec.gov/Archives/edgar/data/72331/000007233126000063/ndsn-20261023.htm
- Nordson Q4/FY2026 earnings-date release (6 Nov 2026): https://investors.nordson.com/news/news-details/2026/Nordson-Corporation-Announces-Earnings-Release-and-Webcast-for-Fourth-Quarter-and-Fiscal-Year-2026/default.aspx
- Nordson investor presentation 20 Aug 2026: https://s202.q4cdn.com/528247721/files/doc_financials/2026/q3/FY26-Nordson-Investor-Presentation-8-20-26.pdf
- Nordson Investor Day deck, 3 Oct 2024 (ATS division split, XM8000 Pro slide): https://s202.q4cdn.com/528247721/files/doc_events/2024/Oct/03/ndsn-investor-day-presentation_final-10-3-24-v2.pdf
- Nordson Q1 FY2025 call (SpinSAM "not contributing to growth yet"): https://equibles.com/stocks/ndsn/calls/2025-q1
- SemiEngineering, "Shrinking Hybrid Bonding Pitches Push Inspection Limits" (Nordson 165 MHz quote, 10 Nov 2026): https://semiengineering.com/shrinking-hybrid-bonding-pitches-push-inspection-limits/
- Semiconductor Digest print issue Nov/Dec 2024 (SpinSAM article, pp. 22–24): https://magazine.semiconductordigest.com/html5/reader/production/default.aspx?pubname=&edid=b0792fcf-71f7-417a-bd63-f55f370c7eb3&pnum=24
- CyberOptics Q4 2021 call (WX3000 PO value): https://tickertrends.io/transcripts/CYBE/Q4-earnings-transcript-2021
- IEEE EPS, Summary of ECTC 2025 Special Session on Hybrid Bonding: https://eps.ieee.org/wp-content/uploads/2026/03/EM_Hybrid-Bonding_Apr26.pdf
- STMicroelectronics/IEMN, SAM vs picosecond acoustics on hybrid bonding (Forum Acusticum 2020): https://hal.science/hal-03240341/file/000878.pdf
- Samsung/Nova, metrology for 3D NAND hybrid bonding (SPIE 2025): https://novami.com/wp-content/uploads/2025/04/challenges-and-responses-of-metrology-technologies-for-the-new-wave-of-3d-nand-devices.pdf
- Hitachi Power Solutions US 12,422,409 B2 (liquid infiltration into bonded wafers): https://patents.google.com/patent/US12422409B2/en
- PVA TePla interim statement Q3 2026: https://www.pvatepla.com/fileadmin/sitepackage/pdf/investor_relations/berichte/2026/PVATePla_Interim_Statement_Q3_2026.pdf
- Microchip AN4153 (15 rad limit, Nordson DAGE Quadra 7): https://onlinedocs.microchip.com/oxy/GUID-2952C8AA-A592-489E-8058-3FD06065EDDB-en-US-7/GUID-0955C097-E167-4BE4-9BA8-7732119EFBF5.html
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
- Bernard & Blish, SMTA International 2003 (also EPTC 2005): https://smtnet.com/library/files/upload/Minimising-radiation-doses.pdf
- Rohona (Data I/O) & Bastin (Nordson DAGE), IPC APEX EXPO 2018: https://www.electronics.org/system/files/technical_resource/E41%26S24_01%20-%20Dave%20Rohona.pdf
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

# China's domestic suppliers of chip measurement, inspection and test equipment and software

Research date: 12 November 2026. DRAFT 1, written after an interruption. Sections marked [INCOMPLETE] are still being filled. Primary filings are the Q3 2026 and FY2025 reports downloaded from CNINFO (巨潮资讯). All "my calc" figures are my arithmetic on filed numbers. RMB 1亿 = RMB 100m.

## 0. Summary tables

### 0a. Companies by sub-segment (status in brackets; "claim" = company claim, unconfirmed)

| Sub-segment | Chinese suppliers (listing / Entity List status) |
|---|---|
| Optical patterned/unpatterned defect inspection (bright-field, dark-field) | Skyverse 中科飞测 (688361 STAR; EL Dec-2024): unpatterned and dark-field in volume; bright-field in volume at mature nodes, advanced node "in validation, some orders" (broker). Jingce 精测电子 via 上海精积微 (300567 ChiNext; unit 上海精测半导体 on EL): bright-field accepted on a 28nm line, repeat delivery to a 14nm line (claim). SiCarrier 新凯来 (private; EL): BFI 岳麓山, DFI 丹霞山, unpatterned 蓬莱山 (claims, no shipments confirmed). Yuwei 御微 (private; EL): wafer and mask defect inspection (claim). TZTEK 天准 / 矽行 / MueTec: [INCOMPLETE] |
| E-beam inspection, review, CD-SEM | Dongfang Jingyuan 东方晶源 (private, STAR IPO under review; EL): CD-SEM, EBI, DR-SEM, HV-SEM; China e-beam share 2.83% in 2025 (QYR, in its IPO reply). Jingce: e-beam tools on advanced-packaging lines (claim). Skyverse: CD-SEM prototype in customer sample validation. SiCarrier: multi-beam EBI 井冈山 in product handbook only (Oct 2026). |
| Optical dimension (OCD) and film metrology | Skyverse (film in volume; 2nd-gen OCD small batch); Jingce/上海精测 (film, OCD; earliest domestic film supplier); RSIC 睿励 (private; EL): film/OCD/defect [details INCOMPLETE]. |
| Overlay | Skyverse (3rd-gen in revenue, 4th-gen at customers for validation); SiCarrier 天门山 DBO/IBO (claim); Yuwei (claim). |
| X-ray metrology | SiCarrier 赤壁山 XPS/XRD/XRF (claim); Skyverse X-ray HAR etch structure metrology passed production-line validation at a leading domestic memory maker; Angstrom Excellence 埃芯 (private; not on EL): optical + X-ray, >100 tools shipped (claim). |
| X-ray inspection (packaging, PCB, batteries) | Unicomp 日联科技 (688531 STAR; not on EL), plus acquired SSTI. |
| Bonded-wafer / advanced-packaging / HBM inspection | Skyverse (3D AOI, 3D topography, HBM wafer flatness, TSV Cu-fill voids); Jingce (HBM topography, hybrid-bond surface roughness, post-TSV-etch HAR, TGV); Angstrom (hybrid bonding, TSV, bump); TZTEK [INCOMPLETE]. |
| Electrical test: ATE (SoC, analog, memory) | Changchuan 长川 (300604 ChiNext; not on EL): SoC D9000, memory via 长迈; Huafeng 华峰测控 (688200 STAR; EL Dec-2024): analog/mixed-signal STS8300, SoC STS8600 small batch; Jingzhida 精智达 (688627 STAR; not on EL): DRAM test, 18Gbps FT project. |
| Probe cards and probers | Maxone 强一股份 (688809 STAR; MEMS probe cards; Huawei's Hubble holds 4.80%); Semishare 矽电 (301629 ChiNext; probers; Hubble 3.00%); Changchuan (probers, handlers). |
| Yield software, electrical-parameter (WAT) test | Semitronix 广立微 (301095 ChiNext; not on EL): EDA + WAT testers + yield software; Skyverse: three yield-software series (revenue RMB 12.6m in 2025); Dongfang Jingyuan: computational lithography/yield software (software and services RMB 269m of its backlog). |
| Electron-microscope reference analysis labs | Wintech Nano 胜科纳米 (688757 STAR; not on EL): failure analysis / materials analysis labs. |

### 0b. Evidence table for the three largest by scale (selected by revenue and backlog, not a quality ranking)

| Test | Skyverse 中科飞测 (688361) | Jingce 精测电子 (300567) + 上海精测/精积微 | Changchuan 长川 (300604) |
|---|---|---|---|
| (a) Position | Broadest domestic optical process-control line (13 equipment series, 3 software series); KLA still has the largest share in China (its own FY2025 report). No outside evidence of tool-of-record at a named advanced node. Unpatterned and wafer-level-packaging inspection are its strongest lines (claims of "absolute lead" among domestic firms and "most of" domestic packaging share — unconfirmed). | Front-end metrology/inspection is >90% of semiconductor orders and revenue; film/OCD/e-beam/bright-field. Bright-field "accepted on a 28nm line, repeat delivery to 14nm" (claim). | Largest domestic tester maker by revenue; SoC (D9000) and memory test (长迈) plus probers/handlers. Testers are a test-of-record function at OSATs, but no outside share data found. |
| (b) Lead (outside evidence) | 2025 China metrology/inspection share 5.8% (unsourced article); KLA+AMAT+Hitachi ~79% of China (Guosheng Securities). Named customers (broker): SMIC, YMTC, JCET, Huatian. | 3.2% China share 2025 (same unsourced article). No named customers in filings seen. | No third-party share data found. Memory-test duopoly Advantest+Teradyne 99% globally in 2023 (unsourced article). |
| (c) Revenue model | One-off hardware: 2025 inspection RMB 1,364m, metrology 623m, software 12.6m (0.6%). | Hardware; group also has display and new-energy test. | Hardware (testers, probers, handlers). |
| (d) Financials (9M 2026, filed) | Revenue 1,614m (+34.3%); GM 48.4%; R&D 39.3% of revenue; net -95m; deducted -205m; OCF -346m; contract liabilities 1,430m (2.5x end-2025); inventory 4,289m; net cash ~1.0bn (my calc); top-5 customers 36.6% (2025); 9M government subsidies 98m. | Revenue 2,852m (+25.6%); GM 45.0%; R&D 24.1%; net 80m (-20%; ex-share-based pay 191m); OCF -1,126m; net debt ~3.9bn (my calc); semiconductor backlog 3.66bn (+105%). | Revenue 5,942m (+57.3%); GM 55.8%; R&D 15.8%; net attributable 1,765m (+104%); OCF +1,039m; net cash ~2.4bn (my calc); inventory 6,180m; other income (VAT refunds, grants) 334m. |
| (e) Resilience | Demand is policy-driven (Chinese fabs replacing KLA); EL listing since Dec 2024; imports "some core components" (risk factor). A return of foreign tools would hit its advanced-node pipeline most. | Same as Skyverse, plus leverage and negative OCF. | Not on EL; driven by AI and memory test demand in China. |
| Transitions said / done | (3) packaging/HBM: done, multiple tools at HBM/memory makers in validation or production; (4) software: 3 yield-software series deployed, YMS manages data from "hundreds" of tools (claim), deep-learning ADC; (1) and (2): no evidence found. | (3) done: HBM topography, hybrid-bond roughness, TGV delivered (claim). (1)(2)(4): no evidence. | (3) memory/HBM test growth; [INCOMPLETE] |
| Entry point (12 Nov 2026 close) | RMB 266.27; mkt cap RMB 93.7bn; P/E TTM negative; P/E on 2025 profit 1,598x; P/S TTM ~38x (my calc); STAR 50 member; Northbound holding 2.03%. | RMB 121.70; mkt cap RMB 34.0bn; P/E TTM 549x; P/S TTM ~8.7x (my calc); Northbound 1.55%. | RMB 195.38; mkt cap RMB 126.8bn; P/E TTM 56.8x; Northbound 3.38%. |

## Q1. What each company ships, nodes, customers, and results

### Takeaway
[INCOMPLETE — being expanded] Domestic process-control suppliers are growing 25-35% with heavy R&D, weak or negative cash flow and swelling inventories and contract liabilities. The test and probe-card makers are growing faster (45-65%) and are highly profitable. The detail is in the cited findings below.

### Cited Findings
(see 0b and draft list; full per-company detail to follow in draft 2)

## Q2. Domestic share and the gap to KLA, Hitachi, Applied Materials and ASML [INCOMPLETE]

## Q3. Export controls from the Chinese side [INCOMPLETE]

## Q4. Advanced packaging and HBM in China [INCOMPLETE]

## Q5. Entry point and investor access (kept separate from quality evidence) [INCOMPLETE]

## What could not be verified [INCOMPLETE]

## Sources [INCOMPLETE — full list in draft 2]

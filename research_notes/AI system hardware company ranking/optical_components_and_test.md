# Optical components and photonic test for AI data centres: segment map, business quality and path forward (research date 12 November 2026)

Conventions. Every figure carries (period covered; publication date). "Company claim, unconfirmed" = a company statement no outside party has confirmed. "Secondary" = trade press or analyst estimate. "Derived" = my arithmetic on cited figures. No share prices, valuation multiples, market caps or price targets are used (separate workstream). Scope boundary respected: switch makers, NVIDIA/Broadcom/Marvell CPO system programmes, connectors/fibre and processor-to-processor optical links are covered elsewhere and appear here only as demand drivers.

Tooling note (affects coverage): the shared WebSearch budget for this run ran out after about 14 searches, and the Exa and Firecrawl tools had no credits. Everything after that came from fetching specific pages directly: SEC EDGAR filings and XBRL pages, company IR pages, pages that earlier searches had surfaced, and cninfo filing PDFs (Innolight and Eoptolink 2025 annual and Q3 2026 reports). As a result, coverage of Japan, Taiwan, Korea, India, Europe and the test-equipment makers is much thinner than for the six key companies (see sections 1 Gaps and 7).

---

## 1. Segment map (worldwide)

### Takeaway
In 2026 the segment has five layers, and gross margin falls at each step from the bottom up. InP substrates and lasers earn the most: AXT 56%, Lumentum 53% non-GAAP. Then come the Chinese plug-in module leaders (Innolight about 47%, Eoptolink about 46%), the vertically integrated Coherent (about 41%), silicon-photonics foundry (Tower about 34%), the US module maker AAOI (about 29%) and the contract assembler Fabrinet (about 12%). Chinese firms dominate module assembly (Innolight #1 and Eoptolink #2 in 2025). US and Japanese firms dominate InP lasers and substrates. Silicon-photonics wafers come from Israel/US/Japan (Tower) and Taiwan (TSMC). Final assembly sits in Thailand (Fabrinet, plus the Chinese makers' offshore plants). The two biggest structural events of 2026 are both in this segment: NVIDIA's $2B equity investment in each of Lumentum and Coherent (Mar 2026), and the all-stock Marvell-Lumentum combination announced on 2 Nov 2026, expected to close in 1H 2028.

### Cited Findings

#### 1a. Map table (rows with a 2026 source; unsourced starting-list names are in Gaps)

| Company | Home / main footprint | Listing, ticker | Role in segment | Why it matters (dated, sourced) |
|---|---|---|---|---|
| Lumentum | US; sells into US, Mexico, Thailand, HK, China | Nasdaq: LITE | InP lasers (EML, CW / ultra-high-power (UHP) for CPO, pump, narrow-linewidth), Cloud Light transceivers, optical circuit switches (OCS) | KEY. Q1 FY27 (qtr to 26 Sep 2026; pub. 2 Nov 2026) revenue $1,262.6M (+136.5% y/y), non-GAAP GM 53.2% ([release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx)). NVIDIA bought $2.0B of Series A convertible preferred, Mar 2026 ([10-Q R74](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R74.htm)). Marvell all-stock combination announced 2 Nov 2026, close expected 1H CY2028 ([Marvell](https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity)); Lumentum owns Cloud Light ([TrendForce, 3 Nov 2026](https://www.trendforce.com/presscenter/news/20261103-13294.html)) |
| Coherent | US; 6-inch InP lines in Texas and Sweden | NYSE: COHR | Vertically integrated: InP lasers, VCSELs, SiPh, transceivers, PhotonLink CPO/NPO platform | KEY. Q1 FY27 (qtr to 30 Sep 2026; pub. 4 Nov 2026) revenue $2,370.3M; Datacenter & Communications $1,951.7M ([release](https://finviz.com/news/415844/coherent-corp-reports-first-quarter-fiscal-2027-results)). Second PhotonLink anchor customer: 5-year deal valued at about $20B, revenue from early CY2028 ([Futurum, 6 Nov 2026](https://futurumgroup.com/?p=97623)) |
| Zhongji Innolight | China (Yantai/Suzhou); offshore plants in Thailand and Mexico per secondary source | SZSE: 300308; HKEX H-shares since 30 Jul 2026 | #1 plug-in transceiver maker | KEY. Q3 2026 revenue RMB 27.769B (+171.8% y/y) ([ifeng/Leiduo, 29 Oct 2026](https://finance.ifeng.com/c/8xcyvWhXO0b)). #1 in datacom revenue and high-speed units "by a wide margin" ([Cignal AI 1Q26, Jun 2026](https://cignal.ai/2026/06/datacom-optical-component-revenue-doubles-to-7-7-billion-in-1q26/)). Primary: 2025 top-5 customers 75.98% of sales (largest 24.06%); overseas 90.58% of 2025 revenue ([2025 annual report, cninfo, 31 Mar 2026](http://static.cninfo.com.cn/finalpage/2026-03-31/1225056459.PDF)) |
| Eoptolink | China (Chengdu); Thailand plant per secondary source | SZSE: 300502 | #2 plug-in transceiver maker; LPO/LRO, NPO, CPO R&D | KEY. #2 in LightCounting's 2025 ranking, overtaking Coherent ([C114, 28 May 2026](https://m.c114.com.cn/w5472-1311209.html), search summary). Q3 2026 revenue RMB 10.94B, -13% q/q ([CITIC via Gelonghui, 2 Nov 2026](https://m.gelonghui.com/news/5342407)). Primary: 2025 top-5 customers 72.34% (largest 22.97%); overseas 96.16% of 2025 revenue ([2025 annual report, cninfo, 24 Apr 2026](http://static.cninfo.com.cn/finalpage/2026-04-24/1225172598.PDF)) |
| Fabrinet | Cayman-incorporated; plants in Chonburi, Pinehurst and Navanakorn (Thailand) plus Santa Clara (US) | NYSE: FN | Contract assembler: transceivers, DCI, OCS, multi-rail, NPO/CPO, telecom, auto/industrial lasers | KEY. FY26 (to 26 Jun 2026) revenue $4,641.1M; customers above 10%: Cisco 19.9%, NVIDIA 16.3%, Nokia 10.7%, Amazon 10.5% ([10-K R111](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/R111.htm)) |
| Tower Semiconductor | Israel; fabs in Israel, US, Japan, Italy | Nasdaq/TASE: TSEM | Merchant silicon-photonics and SiGe foundry | KEY. Q4 2026 SiPho run-rate above $1.1B annualised, about 5x 2025 ([6-K, 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm)) |
| Applied Optoelectronics | US (Sugar Land TX); Taipei; Ningbo, China | Nasdaq: AAOI | Transceivers (800G/1.6T), CATV | Q3 2026 revenue $269.9M, datacenter $155.6M; multi-year deal with a Tier-1 hyperscaler ([8-K, 5 Nov 2026](https://www.sec.gov/Archives/edgar/data/1158114/000168316826008351/aaoi_ex9901.htm)) |
| AXT | US HQ; all manufacturing at three sites in China | Nasdaq: AXTI | InP substrates (also GaAs, Ge) | Physical constraint plus export-permit risk. Q3 2026 revenue $73.4M (+162% y/y), GM 56.0% ([8-K, 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm)) |
| JX Advanced Metals | Japan (Isohara; new Hitachinaka site) | TSE (ticker not re-verified) | InP substrates | Up to JPY 120B over four years to raise InP substrate capacity about 7-10x; about JPY 150B including earlier tranches ([JX, 16 Jun 2026](https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html)) |
| Broadcom (in passing) | US | Nasdaq: AVGO | EML, CW lasers, VCSELs; DSPs; Davisson CPO | Offers EML and CW lasers ([TrendForce](https://www.trendforce.com/presscenter/news/20261103-13294.html)); showed Davisson CPO samples at ECOC 2026 ([Cignal, 28 Sep 2026](https://cignal.ai/2026/09/ecoc-2026-show-report/)); Sian2 DSP is the NVIDIA-chain standard (secondary, [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Marvell (in passing) | US | Nasdaq: MRVL | PAM4/coherent DSPs; acquirer of Lumentum | 2nm optical DSP demos at ECOC, 21 Sep 2026 ([Marvell IR list](https://investor.marvell.com/news-events/press-releases)) |
| Credo Technology (owner of DustPhotonics since 28 May 2026) | US/Cayman; DustPhotonics is Israeli | Nasdaq: CRDO | SerDes, DSP, AECs; SiPh PICs for transceivers (DustPhotonics); microLED optical interconnect (Hyperlume) | Acquired 100% of DustPhotonics Ltd on 28 May 2026 for total consideration of about $1.25B: $769.6M cash, $169.1M shares, $310.0M contingent earn-out (cash and shares), $2.5M replacement awards; goodwill $895.8M. Stated aim: a "vertically integrated connectivity stack" spanning SerDes, DSP, SiPh and system integration. Also bought Hyperlume (29 Sep 2025, $92.0M) and Comira (25 Feb 2026, $35.1M cash) ([Credo 10-Q, filed 2 Sep 2026: R12](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R12.htm); [R38](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R38.htm)). DustPhotonics is therefore no longer an independent Israeli private firm |
| Accelink | China (Wuhan) | SZSE: 002281 | Modules and in-house lasers | #4 in LightCounting 2025 list (secondary); described as the only domestic firm making 25G EMLs in-house ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| HGTech / Huagong (HG Genuine) | China (Wuhan) | SZSE: 000988 | Modules; in-house EML/SiPh chips | #7 (secondary); claims $25-30 saving per 400G unit from in-house chips (company claim via [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Hisense Broadband | China; plants in Thailand and New Jersey | private (Hisense group) | Modules, lasers | #6 (secondary) ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| CIG ("Cambridge Technology") | China; Malaysia plant | SSE: 603083 | Modules | #10 (secondary) ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Linktel | China; Malaysia plant | SZSE: 301205 | Modules | Offshore plant (secondary) ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Source Photonics | Chinese-owned | private | Modules, InP lasers | In the top 10; "acquired by Chinese capital" (secondary, [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Yuanjie Semiconductor | China (Xi'an) | SSE STAR: 688498 | CW/DFB laser chips | Named as a CW laser supplier ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)); tagged in Cignal's Oct 2026 note on the shift from EML to SiPh/CW ([Cignal](https://cignal.ai/2026/10/update-to-cignal-ais-datacom-optical-front-end-forecast/)) |
| Shijia Photons | China | SSE STAR: 688313 | CW lasers, PLC/AWG | CW laser supplier ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Zetta; Changguang Huaxin | China | private; SSE STAR 688048 | Domestic EMLs | 100G EML in mass production, 200G EML announced Nov 2025 (Zetta); 56G EML since 2023 (Changguang) ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)) |
| Mitsubishi Electric | Japan | TSE: 6503 | 100G+ EML lasers | One of about five 100G+ EML suppliers (secondary, [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)); no 2026 capacity data retrieved |
| Sumitomo Electric | Japan | TSE: 5802 | Lasers (mainly DFB/VCSEL per source), modules | About $400-500M of 2025 transceiver-related sales (LLM-attributed estimate, low confidence) ([ComSoc](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/)); EML role per [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of) |
| Furukawa Electric | Japan | TSE: 5801 | DFB lasers; optical chiplets | DFB laser-diode plant announced 17 Dec 2025; NEDO-backed mass-production technology for "optical chiplets" (20 Oct 2026) ([Furukawa release list](https://www.furukawaelectric.com/en/release/)) |
| Aixtron | Germany; new Penang site | XETRA: AIXA | MOCVD tools (G10-AsP) for InP/GaAs lasers and detectors | G10-AsP orders from Lumentum "for AI networks" (19 May 2026); Aeluma (12 Nov 2026); Penang facility (23 Jul 2026) ([Aixtron releases](https://www.aixtron.com/en/press/press-releases)) |
| NewPhotonics | Israel | private | SiPh with InP laser chiplets; NPO chiplet | Initial production at Tower using InP laser chiplets attached to SiPh wafers ([MarketBeat Tower call, 2 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/)) |
| Teradyne / Quantifi Photonics | US / New Zealand | Nasdaq: TER | PIC wafer and CPO test, transceiver test | Quantifi's site reads "A Teradyne Company" (2026) and lists "PICs and CPO Testing" ([Quantifi](https://www.quantifiphotonics.com/)) |
| ficonTEC (RoboTechnik) | Germany; parent in China | parent SZSE: 300757, with a new HK listing | Photonic assembly (ASSEMBLYLINE), die and wafer-level electro-optical test, double-sided wafer tester | Site: "RoboTechnik Hong Kong listing enables ficonTEC's next phase of growth"; CPO-test cooperation with HTSI in Taiwan ([ficonTEC](https://www.ficontec.com/)) |
| Aehr Test Systems | US | Nasdaq: AEHR | Wafer- and package-level burn-in | FY27 guide $150M, driven by AI processors; SiPh named only as an application area ([8-K, 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009385/aehr_ex991.htm)) |
| Aeluma | US | (listing not verified) | Photodetectors, lasers | Buying Aixtron G10-AsP capacity ([Aixtron](https://www.aixtron.com/en/press/press-releases)) |

#### 1b. Segment-wide evidence: plug-in module volumes, revenue, shares and prices
- **Market size, 2025.** Optical component revenue was nearly $25B in 2025 ([Cignal AI, Jan 2026](https://cignal.ai/2026/01/optical-component-revenue-reaches-nearly-25b-in-2025/)). Datacom optical components passed $19B in 2025 ([Cignal AI, Apr 2026](https://cignal.ai/2026/04/datacom-optical-component-revenue-surpasses-19b-in-2025/)).
- **1Q26** (pub. Jun 2026), all [Cignal AI](https://cignal.ai/2026/06/datacom-optical-component-revenue-doubles-to-7-7-billion-in-1q26/):
  - datacom optical component revenue was $7.7B, more than double y/y;
  - 400G+ module shipments rose 145% y/y, to about 20M modules in the quarter;
  - 800GbE is the majority, and 800G units should more than double in 2026;
  - 1.6TbE should exceed 10M units in 2026; the forecast was raised from more than 5M in Jan and about 10M in Apr;
  - nearly all 1.6T modules ship as SiPh DR designs;
  - datacom optics should reach about $30B by 2029.
- **2Q26** (pub. 24 Sep 2026): datacom and telecom revenue hit new highs, 800GbE led, 1.6TbE shipped in volume, and OCS revenue is rising as Google moves to outside vendors. Figures are paywalled ([Cignal AI](https://cignal.ai/2026/09/2q26-optical-component-report/)).
- **LightCounting** (Sep 2026 reports, via [IEEE ComSoc, 2 Oct 2026](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/)), secondary:
  - Ethernet is about 80% of transceiver sales;
  - Q2 2026 800G 2xDR4/2xFR4 units were up to 3x y/y;
  - Ethernet transceiver revenue doubled in 2024 and rose about 90% in 2025;
  - forecast: +120% in 2026, +76% in 2027, slowing to about 20% by 2031;
  - the base case is a soft landing with cloud capex +50% in 2027; a "bumpy-ride" scenario with a supply-chain correction in 2027-2030 is "plausible".
- **TrendForce estimate** (pub. 2 Nov 2026), secondary ([TrendForce](https://www.trendforce.com/presscenter/news/20261102-13291.html)):
  - pluggable optical transceivers reach $84.1B in 2027, +76% y/y, with revenue growth outpacing shipments;
  - 1.6T is about 56% of 2027 pluggable revenue;
  - 1.6T ASPs "continue to fall but remain more than twice those of 800G";
  - copper stays dominant inside GPU racks in 2027.
- **TrendForce via Photoncap** (secondary-of-secondary): 800G+ units go from 24M (2025) to about 63M (2026) ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
- **Supplier ranking and shares:**
  - LightCounting's 2025 top-10 list (reported 28 May 2026): Innolight #1; Eoptolink #2, overtaking Coherent ([C114](https://m.c114.com.cn/w5472-1311209.html), search summary only).
  - Seven of the top 10 are Chinese (secondary, cites the 2024 list) ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
  - "Industry sources": Innolight plus Eoptolink hold about 60% of NVIDIA's 800G volume. Unverified ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
- **Pricing:**
  - Lumentum credited Q4 FY26 margin gains partly to "higher pricing on certain products" (company statement, [MarketBeat, 11 Aug 2026](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)).
  - JX says InP substrate "price revisions are under discussion" with customers ([JX, 16 Jun 2026](https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html)).
  - 1.6T ASPs are falling (TrendForce, above).

#### 1c. Segment-wide evidence: lasers and InP
- **EML suppliers at 100G+.** Roughly five: Lumentum, Coherent, Mitsubishi, Broadcom and Sumitomo. Lumentum is described as most aggressive at 200G/lane. TrendForce reports NVIDIA pre-allocated EML capacity, pushing lead times past 2027. China's localisation rate for 25G+ optical chips is below 15%. All secondary ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
- **Lumentum EML** (company statements):
  - record EML revenue in Q4 FY26; 200G EMLs were more than 25% of EML revenue;
  - EML and CW demand growing through 2H CY26 into 2027 ([MarketBeat, 11 Aug 2026](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/));
  - earlier: an EML shortfall of 25-30% vs demand (Nov 2025) ([Statementdog](https://statementdog.com/analysis/LITE/earnings_calls/301563), secondary), a laser-chip supply gap of more than 30% of demand, and a target of 200G EMLs at half of EML volume by mid-2027 ([Finsee review](https://finsee.ai/earnings/lite/2027/q1/en/)).
  - Cignal's view: "Lumentum already sells all the lasers it can build" (opinion) ([Cignal, 3 Nov 2026](https://cignal.ai/2026/11/marvell-acquires-lumentum/)).
- **Shift from EML to SiPh plus CW.** Some module vendors are moving FR optics from EMLs to SiPh with CW lasers. Cignal now forecasts SiPh at 60% of the datacom optical front end in 2030, up from 55%, at the expense of EMLs ([Cignal AI, 15 Oct 2026](https://cignal.ai/2026/10/update-to-cignal-ais-datacom-optical-front-end-forecast/)).
- **CW lasers.** Suppliers named: Lumentum, Yuanjie, Shijia. Supply was then "comparatively comfortable" (secondary, older; [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
- **UHP lasers and external laser sources (ELS)** (company statements, [MarketBeat, 11 Aug 2026](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/); [Finsee](https://finsee.ai/earnings/lite/2027/q1/en/)):
  - Lumentum expects a UHP laser run-rate of about $50M in the Dec-2026 quarter;
  - high-volume UHP shipments for scale-up begin 2H CY2027;
  - first ELS module purchase order is for delivery by 2H CY2027.
- **Coherent PhotonLink lasers** (company claims, [Futurum](https://futurumgroup.com/?p=97623)): the platform is built around a 400 mW laser; internal InP output doubled y/y in Q1 FY27; 6-inch InP lines yield better than 3-inch.
- **InP substrates:**
  - JX: up to JPY 120B, capacity about 7-10x, because demand is growing "faster than previously expected"; customers made "substantial requests" ([JX](https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html)).
  - AXT: "surpassed its goal to double InP capacity"; 2026 InP revenue opportunity "more than quadrupled" (company claims); export permits appear only as a forward-looking risk ([AXT 8-K](https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm)).
  - AXT revenue: Q2 2025 $18.0M → Q2 2026 $47.6M ([10-Q](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm)) → Q3 2026 $73.4M ([8-K](https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm)).
  - AXT raised about $632.5M gross in an April 2026 share offering ([10-Q](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm)).
- **Laser epitaxy tools.** Lumentum ordered Aixtron G10-AsP MOCVD systems in May 2026 ([Aixtron](https://www.aixtron.com/en/press/press-releases)).
- **Equity and long-term agreements:**
  - NVIDIA, Mar 2026: $2B into each of Lumentum and Coherent, with non-exclusive multiyear partnerships, "multibillion-dollar" purchase commitments and "future capacity access rights for advanced laser components" ([Verdict, 3 Mar 2026](https://www.verdict.co.uk/nvidia-invests-lumentum-coherent/); [Evertiq, 4 Mar 2026](https://evertiq.com/design/2026-03-04-nvidia-to-invest-2-billion-in-lumentum-under-new-optics-partnership)).
  - Lumentum: second NPO/CPO win with purchase commitments above $5B (company claim, customer unnamed) ([release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx)).
  - Coherent: a $20B, 5-year PhotonLink agreement (company claim, customer unnamed) ([Credence Research](https://www.credenceresearch.com/news/coherent-photonlink-20-billion-five-year-agreement-ai-data-center)).
  - Eoptolink: prepayments RMB 1.32B (+RMB 1.31B YTD), as it is "pre-stocking to secure supply" ([CITIC via Gelonghui](https://m.gelonghui.com/news/5342407)).

#### 1d. Segment-wide evidence: silicon-photonics foundries
- **Tower** ([6-K](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm); [MarketBeat call](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/)):
  - Q3 2026 SiPho about $240M; Q4 run-rate above $1.1B annualised;
  - capacity 3x the Q3 shipment level by Q3 2027 (Japan 300mm Track-1, full production starts Q3 2027), supporting a start-rate run-rate "a bit above $2.8B";
  - capacity "substantially covered by signed agreements and contracts in advanced negotiation", with commitments into 2029;
  - customer advances: $249M current and $92M long-term (vs $26M and $2M at Dec 2025);
  - NPO prototyping with more than 10 top customers.
  - Risk factors cite GlobalFoundries patent-infringement claims and an Intel capacity-corridor dispute.
- **TSMC** in the CPO path: Cignal frames NVIDIA's CPO as a "TSMC/NVIDIA venture" that will either lift off or fail ([Cignal OFC 2026](https://cignal.ai/2026/03/ofc-2026-show-report/), opinion). Foundry concentration: SiPh foundry capacity sits mainly overseas, with GlobalFoundries, Tower and TSMC ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of), secondary).

#### 1e. Segment-wide evidence: photonic test and assembly
- **Quantifi Photonics (Teradyne):** offers "PICs and CPO Testing", transceiver test, SiPh assembly/packaging solutions and PXI/MATRIQ/EPIQ platforms; no customers named ([Quantifi](https://www.quantifiphotonics.com/)).
- **ficonTEC:** lists WAFER TESTLINE wafer-level electro-optical probing, a double-sided wafer tester, die-level TESTLINE and ASSEMBLYLINE/CUSTOMLINE for co-packaging, and a "strategic cooperation" with HTSI "to scale advanced CPO test solutions in Taiwan". Its installed-base claims conflict on the site (more than 2,500 vs more than 1,000 systems) ([ficonTEC](https://www.ficontec.com/)).
- **Aehr:** sees "production potential" across more than a dozen customers, including SiPh, but disclosed no photonics orders ([8-K](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009385/aehr_ex991.htm)).
- **Teradyne:** IR releases from Sep to Nov 2026 include Q3 results (27 Oct 2026) and a Titan HP burn-in platform for AI data-centre devices (6 Oct 2026); none is photonics-specific ([Teradyne IR](https://investors.teradyne.com/news-events/press-releases)).
- **Why test and tooling matter for CPO:** cost, reliability, availability and the tooling investment needed for volume are why NVIDIA needs a "supplier-push" approach (Cignal opinion, [OFC 2026](https://cignal.ai/2026/03/ofc-2026-show-report/)).

### Inferences
- Gross-margin ranking as a value-capture map (Q3 2026 / Sep-qtr data): InP substrate (AXT 56%) ≈ InP laser specialist (Lumentum 53% non-GAAP) > Chinese module leaders (about 46-47%) > vertical integrator (Coherent 41%, diluted by a shrinking Industrial segment) > SiPh foundry (Tower about 34%, still depreciating new tools) > US module maker (AAOI about 29%) > contract assembler (Fabrinet 12%). In 2026, the scarce, capital- and know-how-heavy layers (InP substrates and lasers) earn the highest margins. The Chinese module leaders also earn unusually high margins, which looks like a shortage-era premium.
- The binding physical constraints in 2026-27 are InP lasers and, behind them, InP substrates. NVIDIA buys capacity rights rather than modules from Lumentum and Coherent; JX is expanding substrates 7-10x; AXT doubled capacity. Module assembly, contract assembly and SiPh wafers are being expanded fast (sections 2-3), so they are less likely to bind by 2028.
- Regions: China dominates module assembly (and is building domestic EML/CW makers). The US and Japan dominate high-end InP lasers and substrates. Israel/US/Japan (Tower) and Taiwan (TSMC) dominate SiPh wafers. Thailand is the assembly hub for US-bound product.

### Gaps
- **Starting-list and other names with no 2026 source retrieved.** Roles below are background knowledge only, unsourced; verify before use:
  - Taiwan: LandMark Optoelectronics (InP epi), Browave and FOCI (passives / fibre-array units for CPO), IntelliEPI and VPEC (epi), WIN Semiconductors (compound foundry), Truelight (VCSEL), Chroma ATE and MPI (photonic test and probing).
  - China: TFC Optical (passives, optical-engine components), Luxshare and Foxconn Interconnect (modules), Dongshan Precision's reported 2025 purchase of Source Photonics.
  - Foundries: GlobalFoundries (Fotonix; reported AMF Singapore purchase), TSMC COUPE capacity, STMicroelectronics PIC100 with AWS, X-FAB.
  - Europe: Soitec (photonics-SOI), IQE (sale/strategic review outcome), Sivers Semiconductors (InP laser arrays), Scintil and SMART Photonics (private InP/hybrid foundries), Ligentec.
  - Israel and US: Teramount; Jabil (SiPh modules); MACOM, Semtech, MaxLinear (electronics); POET (Canada). DustPhotonics is now verified as part of Credo (see table).
  - Test makers: FormFactor (its IR page returned 403), Keysight, Advantest, Santec, Anritsu, VIAVI, EXFO (private), Yokogawa.
- **Korea (coverage very thin; no sources retrieved).** Background candidates only: OE Solutions (KOSDAQ; mostly telecom/5G transceivers), Woori Ro (laser diodes/photodiodes), Opticis, Lighttron. I found no Korean company with material AI-data-centre optical-component revenue; DART was not searched.
- **India (coverage very thin; no sources retrieved).** No Indian AI-data-centre laser, module or SiPh maker of scale was identified. HFCL and Sterlite (fibre/telecom) are outside scope. NSE/BSE were not searched.
- Third-party EML/CW/UHP laser market shares (LightCounting/Cignal/Omdia) were not obtained; reports are paywalled.
- 2025-2028 unit and revenue tables for 800G/1.6T by supplier were not obtained. 2028 volumes are missing entirely.

---

## 2. Evidence on tests (a)-(e) for the key companies

Key companies chosen: Lumentum, Coherent, Innolight, Eoptolink, Fabrinet, Tower Semiconductor. Short partial notes cover AXT/JX (substrates), AAOI and the test makers.

### Takeaway
Lumentum has the strongest combination: a scarce physical constraint (InP lasers, sold out), the highest margins, positive free cash flow despite heavy capex, and outside validation (NVIDIA $2B; acquisition by Marvell). Its weak points are extreme customer concentration (one customer was 37% of Sep-2026 quarter revenue) and deal and approval risk until 1H 2028. Tower is the cleanest balance sheet, with net cash of about $1.3B, customer prepayments and contracts to 2029. Innolight is the market-share leader with high margins and a huge HK IPO cash pile, but its core product is a bridge. Coherent has a strong position (6-inch InP, two PhotonLink anchors), but FY26 free cash flow was about -$1.0B and it has net debt of about $2.2B. Fabrinet is diversified (four 10%+ customers) with net cash but a 12% gross margin. Eoptolink shows the clearest late-cycle warning signs: revenue fell 13% q/q in Q3 2026 and inventory rose 141% YTD.

### Cited Findings

#### Lumentum (Nasdaq: LITE)
- **(a) Position, products.**
  - Revenue mix in Q1 FY27 (qtr to 26 Sep 2026): Components $754.2M (59.7%); Systems $508.4M (40.3%; cloud transceivers, OCS, industrial lasers) ([release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx); [Finsee](https://finsee.ai/earnings/lite/2027/q1/en/)).
  - Pump lasers and OCS were "the leading contributors" (company).
  - Q4 FY26 call, 11 Aug 2026 (company statements, [MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)):
    - record 800G shipments; 1.6T production shipments began;
    - OCS shipments doubled q/q, and Q1 FY27 was guided as the first quarter with more than $100M of OCS revenue (actual not disclosed);
    - pump lasers "effectively sold out";
    - record EML revenue, with 200G EMLs more than 25% of the total;
    - UHP lasers for scale-up CPO in high volume from 2H CY2027, ahead of 2028 customer deployments;
    - first ELS module purchase order for 2H CY2027 delivery; NPO late 2027-2028;
    - "no impact yet" from potential new Chinese InP capacity.
  - Cignal (opinion): Lumentum "sells all the lasers it can build" ([Cignal](https://cignal.ai/2026/11/marvell-acquires-lumentum/)).
- **(b) Lead.**
  - Outside validation: NVIDIA's $2.0B Series A convertible preferred purchase (2.9M shares, Mar 2026; the 10-Q page does not name the buyer, but it matches the NVIDIA deal) ([10-Q R74](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R74.htm)), with multibillion purchase commitments and capacity rights ([Verdict](https://www.verdict.co.uk/nvidia-invests-lumentum-coherent/)).
  - Marvell's decision to buy the company to fill an InP-laser gap (TrendForce opinion) ([TrendForce](https://www.trendforce.com/presscenter/news/20261103-13294.html)).
  - NVIDIA and Lumentum jointly announced scale-up CPO for 2028 at OFC 2026 ([Cignal](https://cignal.ai/2026/03/ofc-2026-show-report/)).
  - The >$5B second NPO/CPO win is a company claim, unconfirmed (customer unnamed).
  - No third-party EML share figure was obtained.
- **(c) Revenue model.**
  - Hardware sales. Recurring-like elements: the NVIDIA multiyear purchase commitments and the >$5B commitments (company claim).
  - Prior backlog above $400M as of Dec 2025 ([Finsee](https://finsee.ai/earnings/lite/2027/q1/en/)).
  - Purchase obligations to suppliers are $2,948.9M; supply agreements with single- or limited-source vendors typically last 1 year ([10-Q R80](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R80.htm)).
  - No service or consumables revenue.
- **(d) Financial strength.**
  - FY2026 (to ~27 Jun 2026) revenue about $3.0B ([Finsee](https://finsee.ai/earnings/lite/2027/q1/en/), secondary). Q4 FY26 revenue $1.01B (+109% y/y), non-GAAP GM 50.4%, non-GAAP op margin 36.6% ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)).
  - Q4 FY26 GAAP net loss of $7.2B came from a one-time non-cash $7.8B induced-conversion charge; converts were cut by $1.1B ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)).
  - Q1 FY27 ([release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx)):
    - revenue $1,262.6M (+136.5% y/y, +25.5% q/q);
    - GM 51.0% GAAP / 53.2% non-GAAP; op margin 28.5% / 42.3%;
    - GAAP net income $360.3M;
    - cash plus short-term investments about $1.98B; debt $1,360.3M current (converts) plus $39.3M → net cash about $0.58B (derived).
  - Q1 FY27 cash flow ([10-Q R6](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R6.htm)): OCF $267.7M; capex $229.8M (18% of revenue); FCF about $38M (derived); $493.3M paid on note conversions.
  - Q2 FY27 guide: $1.575-1.625B revenue, 45-46% non-GAAP op margin.
  - Return on capital: not computed (invested-capital data not retrieved).
  - Concentration ([10-Q R82](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R82.htm)): Customer A 37% and Customer B 11% of Q1 FY27 revenue (prior-year quarter: 22% and 21%). One customer is 33.4% of receivables. A single vendor is 14% of purchases.
  - Geography, ship-to, Q1 FY27 ([10-Q R83](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R83.htm)): US 23.6%, Mexico 18.3%, Thailand 18.0%, Hong Kong 14.8%, China 12.8%, Japan 3.1%, EMEA 3.8%. China plus Hong Kong = 27.6% (derived).
- **(e) Resilience, cycle, export.**
  - Inventories $807.7M at Q1 FY27 ([Finsee](https://finsee.ai/earnings/lite/2027/q1/en/)); inventory +$59M in Q4 FY26 ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)).
  - The Marvell deal needs US and China approval (TrendForce) and closes 1H CY2028 ([Marvell](https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity); [TrendForce](https://www.trendforce.com/presscenter/news/20261103-13294.html)).
  - TrendForce flags possible restriction of laser access to Chinese module makers as "central to China's review" (opinion).

#### Coherent (NYSE: COHR)
- **(a) Position, products.**
  - Datacenter & Communications was $5,274.6M of $7,118.2M FY26 revenue (74%); Industrial was $1,843.6M and fell 10.3% ([10-K R58](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R58.htm)).
  - Products: InP lasers and photodetectors, VCSELs, SiPh, 800G/1.6T transceivers (1.6T ramping at multiple customers), inter-data-centre links (more than $200M in Q1 FY27, nearly 4x y/y) and PhotonLink (ELS, fibre assemblies, optical modules for CPO/NPO/chip-to-chip). All company claims ([Futurum](https://futurumgroup.com/?p=97623); [Semiconductor Today, 22 Sep 2026](https://semiconductor-today.com/news_items/2026/sep/coherent-220926.shtml)).
  - Base: more than 300M InP lasers and more than 1B InP/GaAs photodiodes shipped; 6-inch InP in Sherman TX and Järfälla, Sweden (company).
- **(b) Lead.**
  - NVIDIA's $2B equity (FY26 cash flow shows $1,998.6M from common-share issuance) ([10-K R8](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R8.htm); [Verdict](https://www.verdict.co.uk/nvidia-invests-lumentum-coherent/)).
  - #3 in transceivers in 2025, implied by Eoptolink overtaking it ([C114](https://m.c114.com.cn/w5472-1311209.html)).
  - The second anchor and the $20B value are company claims, unconfirmed; one review notes "the contract is anchored by a laser rather than a finished transceiver" ([Credence](https://www.credenceresearch.com/news/coherent-photonlink-20-billion-five-year-agreement-ai-data-center)).
  - PhotonLink engagements: more than 10 CPO, more than 10 NPO, more than 5 chip-to-chip (company claim).
- **(c) Revenue model.** Hardware. Contract liabilities are only about $63M at FY26 end, so customer prepayments are minimal ([10-K R57](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R57.htm)). The NVIDIA purchase commitments and the 5-year PhotonLink agreement are the long-term elements.
- **(d) Financial strength.**
  - FY26 (to 30 Jun 2026): revenue $7,118.2M (+22.5%; pro forma higher after the A&D sale) ([10-K R58](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R58.htm)).
  - FY26 cash flow ([10-K R8](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R8.htm)): OCF $79.5M (FY25 $633.6M); capex $1,102.9M → FCF about -$1,023M (derived); $437.0M from business sales; new $1.25B Term A loan; $2.40B of debt repaid.
  - Q1 FY27 (to 30 Sep 2026) ([release](https://finviz.com/news/415844/coherent-corp-reports-first-quarter-fiscal-2027-results)):
    - revenue $2,370.3M (+49.9%; +56% pro forma); D&C +79% y/y;
    - GM 39.1% GAAP / 40.6% non-GAAP; op margin 15.9% GAAP / 23.2% non-GAAP;
    - OCF -$92.7M; capex $775.5M (33% of revenue) → FCF about -$868M (derived);
    - cash $1,552.9M plus short-term $200M; debt about $4,000.6M → net debt about $2.25B (derived).
  - Targets (company): first $3B quarter by end FY27; FY27 pro forma growth above 60%; $4B quarter in FY28; non-GAAP GM above 45% before end CY2028.
  - Concentration: major customer one 20% and customer two 12% of FY26 revenue (FY25: 12% and 10%), both unnamed ([10-K R103](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R103.htm)).
  - Geography, Q1 FY27 ([10-Q R73](https://www.sec.gov/Archives/edgar/data/820318/000082031826000023/R73.htm)): North America $1,593.9M (67.2%), China $305.1M (12.9%), Europe $269.7M (11.4%), Japan $88.3M (3.7%), rest of world $113.4M (4.8%) (shares derived).
- **(e) Resilience, cycle.** Negative OCF reflects capacity expansion and inventory build ([24/7 Wall St](https://247wallst.com/cards/coherent-q1-2027-earnings-cohr-01m6m6c8nses8fzp5jba8fverb), secondary).

#### Zhongji Innolight (SZSE: 300308; HKEX H-shares)
- **(a) Position, products.** 800G/1.6T plug-in modules. Q3 GM rose on 1.6T volume ([ComSoc](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/), secondary). SiPh mix was above 40% in 2025 (secondary, [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)). No verified 2026 CPO/NPO qualification was found.
- **(b) Lead.** #1 by datacom revenue and units "by a wide margin" ([Cignal 1Q26](https://cignal.ai/2026/06/datacom-optical-component-revenue-doubles-to-7-7-billion-in-1q26/)); #1 in LightCounting's 2025 list ([C114](https://m.c114.com.cn/w5472-1311209.html)); about 23.4% global share (secondary, [Faxiangongchang](https://faxiangongchang.com/en/reports/china-optical-module-2026), unverified).
- **(c) Revenue model.** Per-unit module sales to a few large customers. Optical transceiver modules were RMB 37.457B, 97.95% of 2025 revenue (+63.7%) ([2025 annual report](http://static.cninfo.com.cn/finalpage/2026-03-31/1225056459.PDF)). Contract liabilities are only RMB 11.3M at 30 Sep 2026, so there are effectively no customer prepayments ([Q3 2026 report, cninfo, 30 Oct 2026](http://static.cninfo.com.cn/finalpage/2026-10-30/1225643953.PDF)). No long-term-agreement data was found.
- **(d) Financial strength.**
  - Q3 2026 ([ifeng/Leiduo, 29 Oct 2026](https://finance.ifeng.com/c/8xcyvWhXO0b)): revenue RMB 27.769B (+171.8% y/y; about +25% q/q); attributable net profit RMB 8.587B (+173.7%), a net margin of about 30.9% (derived).
  - 9M 2026: revenue RMB 69.547B (+178%); net profit RMB 22.238B (+211.8%) (same source). Q3 GM about 46.6% (secondary, search summary of [ithome](https://www.ithome.com/1/019/718.htm)).
  - Q2 2026 revenue about $3.3B (+192% y/y) ([ComSoc](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/)).
  - HK IPO, 30 Jul 2026: about HK$60.9B including greenshoe (about US$7.8B, derived); 29 cornerstone investors with about US$3.45B (Temasek $300M, Hillhouse $300M, JPMorgan AM and BlackRock $250M each, Alibaba, Tencent and CPP $50M each) ([ifeng](https://finance.ifeng.com/c/8xcyvWhXO0b), secondary).
  - Q3 had an FX loss of about RMB 390M on HKD cash and a fair-value loss of about RMB 440M (same).
  - Overseas revenue was 86.8% of 2024 sales ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
  - PRIMARY, 2025 annual report (FY2025; pub. 31 Mar 2026) ([cninfo PDF](http://static.cninfo.com.cn/finalpage/2026-03-31/1225056459.PDF)):
    - 2025 revenue about RMB 38.24B (overseas RMB 34.637B + domestic RMB 3.603B);
    - overseas share 90.58% (2024: 86.81%); overseas gross margin 44.64%;
    - top-5 customers RMB 29.056B = 75.98% of sales: A 24.06%, B 18.26%, C 14.22%, D 11.34%, E 8.10%;
    - 8.10% of sales went to a related party, matching customer E; the related-party table shows RMB 3.097B of goods sold to an associate company (2024: RMB 3.7M);
    - top-5 suppliers 51.50% of purchases.
  - PRIMARY, Q3 2026 report (to 30 Sep 2026; pub. 30 Oct 2026) ([cninfo PDF](http://static.cninfo.com.cn/finalpage/2026-10-30/1225643953.PDF)):
    - 9M revenue RMB 69.547B; 9M cost of sales RMB 37.281B → 9M GM about 46.4% (derived); 9M R&D RMB 1.863B (2.7% of revenue);
    - 9M OCF RMB 8.008B; capex (cash for fixed, intangible and long-term assets) RMB 9.161B (9M 2025: RMB 1.615B) → 9M FCF about -RMB 1.15B (derived);
    - cash raised from investors RMB 54.54B (HK IPO);
    - 30 Sep 2026 balance sheet: cash RMB 53.53B plus trading financial assets RMB 2.28B; short-term borrowings RMB 0.34B, long-term RMB 0.49B → net cash about RMB 55B (derived);
    - inventory RMB 23.88B (+88.3% YTD, "material preparation for order delivery"); receivables RMB 17.31B (+176%); prepayments RMB 1.57B;
    - fixed assets RMB 12.46B (+76%); construction in progress RMB 5.50B (+286%);
    - equity attributable RMB 94.36B; total liabilities RMB 30.44B.
- **(e) Resilience.**
  - Offshore plants in Thailand (main North America base) and Mexico; US Section 301 tariff of 25% on Chinese-origin goods; a 2025 DOJ trade-fraud task force (secondary, [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
  - Controlling holder sold down from 17.99% to 16.53% ([ifeng](https://finance.ifeng.com/c/8xcyvWhXO0b)).

#### Eoptolink (SZSE: 300502)
- **(a) Position.** 800G/1.6T modules, with "layouts" in LPO/LRO, XPO, NPO and CPO; "continuing to add North American customers" ([CITIC via Gelonghui, 2 Nov 2026](https://m.gelonghui.com/news/5342407)).
- **(b) Lead.** #2 in LightCounting's 2025 list ([C114](https://m.c114.com.cn/w5472-1311209.html)).
- **(c) Revenue model.** Per-unit module sales. Prepayments to suppliers of RMB 1.32B secure supply (an outflow, not customer money).
- **(d) Financial strength** ([CITIC via Gelonghui](https://m.gelonghui.com/news/5342407); [Wallstreetcn](https://wallstreetcn.com/articles/3784769), search summary):
  - Q3 2026: revenue RMB 10.94B (+80.3% y/y, -12.98% q/q); net profit RMB 3.843B (+61.2% y/y, -19.1% q/q); GM 46.27%; finance expense RMB 797M from FX losses; effective tax rate 15.6% vs 10.3%.
  - 9M 2026: revenue RMB 31.85B (+93%); net profit RMB 11.372B (+79.7%); 9M OCF -68% y/y.
  - Inventory RMB 17.41B (+140.7% YTD); fixed assets RMB 5.01B (+49%); 9M cash capex RMB 1.81B.
  - PRIMARY, 2025 annual report (FY2025; pub. 24 Apr 2026) ([cninfo PDF](http://static.cninfo.com.cn/finalpage/2026-04-24/1225172598.PDF)):
    - 2025 revenue about RMB 24.84B (overseas RMB 23.888B + domestic RMB 0.954B; 2024 about RMB 8.65B → about +187%, derived);
    - overseas share 96.16% (2024: 78.70%); overseas gross margin 48.36%;
    - top-5 customers RMB 17.971B = 72.34%: #1 22.97%, #2 16.64%, #3 15.63%, #4 10.96%, #5 6.15%; no related-party sales;
    - top-5 suppliers 41.88%.
  - PRIMARY, Q3 2026 report (to 30 Sep 2026; pub. 30 Oct 2026) ([cninfo PDF](http://static.cninfo.com.cn/finalpage/2026-10-30/1225642947.PDF)):
    - 9M revenue RMB 31.850B; cost RMB 16.659B → GM 47.7% (derived); 9M R&D RMB 0.600B (1.9%);
    - 9M OCF RMB 1.464B (9M 2025: RMB 4.637B); capex RMB 1.806B → 9M FCF about -RMB 0.34B (derived);
    - cash RMB 6.58B (down from RMB 8.16B) plus trading assets RMB 0.27B; NO bank borrowings or bonds;
    - inventory RMB 17.41B (+140.7%); payables RMB 10.46B (+181%); contract liabilities RMB 0.305B (+236%, "advance receipts increased");
    - equity RMB 27.96B.
- **(e) Resilience.** Key-material constraints; electronic and optical chip shortages are cited as a delivery risk; there is a tariff risk (CITIC). Thailand plant ramping 1.6T (secondary, [Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).

#### Fabrinet (NYSE: FN)
- **(a) Position.** A process-agnostic precision optical assembler.
  - Q1 FY27 mix: data center $777M (53%; transceivers, DCI, HPC); communications infrastructure $444M; automotive/industrial/other $253M.
  - Merchant-transceiver and hyperscaler direct-transceiver programmes are ramping; capacity is being installed for OCS and multi-rail systems.
  - NPO revenue from 2H FY27; CPO "further out"; management calls pluggable, NPO and CPO "complementary".
  - Source: [MarketBeat, 2 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/).
- **(b) Lead.** Qualified at four 10%+ customers in FY26: Cisco, NVIDIA, Nokia, Amazon ([10-K R111](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/R111.htm)). The Amazon warrant arrangement continues: "customer warrant" of $2.455M in Q1 FY27 ([10-Q R42](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000041/R42.htm)).
- **(c) Revenue model.** Contract manufacturing, labour- and floor-space-based, with thin margins (non-GAAP GM 12.1%) ([release](https://finviz.com/news/413587/fabrinet-announces-first-quarter-fiscal-year-2027-financial-results)).
- **(d) Financial strength.**
  - FY26 revenue $4,641.1M (+35.7%, derived); data center 47.9%, comms infrastructure 33.3%, auto/industrial/other 18.8% ([10-K R57](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/R57.htm)).
  - Q1 FY27 ([release](https://finviz.com/news/413587/fabrinet-announces-first-quarter-fiscal-year-2027-financial-results)): revenue $1,474.5M (+51%); op margin 9.9% GAAP / 10.8% non-GAAP; OCF $21.3M; capex $158.7M (including a $77M Santa Clara campus); FCF -$137.4M; cash $755.7M; debt $74.7M (new) → net cash about $681M (derived). Q2 guide $1.60-1.65B.
  - Concentration FY26: Cisco 19.9%, NVIDIA 16.3% (FY25 27.6%, FY24 35.1%), Nokia 10.7%, Amazon 10.5%; four customers = 57.4% (derived) ([10-K R111](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/R111.htm)). Implied NVIDIA revenue at Fabrinet: about $1.01B FY24 → $0.94B FY25 → $0.76B FY26 (derived).
  - Revenue by bill-to location, FY26: Thailand $2,842M, US $965M, Singapore $255M, Malaysia $114M, China $88M ([10-K R56](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/R56.htm)).
- **(e) Resilience, capacity** ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/)):
  - revenue capacity about $10B by Jan 2027, up from $5.8B at end FY26;
  - Building 10 (Chonburi) adds about $3.5B; Building 11 (about 1.5M sq ft, about $3B) completes around end FY2028;
  - management is evaluating more sites.

#### Tower Semiconductor (Nasdaq/TASE: TSEM)
- **(a) Position.** Merchant SiPh foundry: about $240M of Q3 2026 revenue, about 46% of the total (derived). Serves pluggables now and NPO next (more than 10 top customers prototyping; "appreciable" NPO in 2H 2027). Heterogeneous integration: InP laser chiplets on SiPh in initial production for NewPhotonics; TFLN die-to-wafer planned for 400G/lane ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/)).
- **(b) Lead.** Customer cash committed in audited accounts: current deferred revenue and advances $249M plus long-term advances $92M at 30 Sep 2026 (vs $26M and $2M at Dec 2025); SiPh prepayments are tied to minimum capacity commitments; contracts are "being extended through 2029" ([6-K](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm)). No third-party foundry share data was found.
- **(c) Revenue model.** Wafer sales under multi-year capacity agreements with prepayments. This is the most contract-backed model among the key companies.
- **(d) Financial strength** ([6-K](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm)):
  - Q3 2026: revenue $526M (+33% y/y); GM about 34%; op margin about 24%; net profit $120M.
  - 9M 2026: OCF $872M (including a $305M net increase in advances); capex $534M; FCF $338M (company formula).
  - Cash plus deposits about $1,473M; debt $153M → net cash about $1.32B (derived).
  - Q4 guide $600M ±5%; 2026 about $2.0B vs $1.57B in 2025 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/)).
  - $920M SiPh/SiGe capex programme, about 65% paid, "self-funded"; incremental GM about 62% (long-term 55-58%).
  - Long-term model (no year): $3.6B revenue / $1.2B net profit at 85% utilisation.
  - Customer concentration: NOT FOUND.
- **(e) Resilience, export.** Fabs in Israel, US, Japan, Italy. Risk factors: GlobalFoundries patent claims, an Intel capacity-corridor dispute, a Fab 3 landlord dispute ([6-K](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm)).

#### Others (brief)
- **AXT:** a physical constraint (InP substrates), but all manufacturing is in China, with export permits flagged as a risk; GM 56% ([8-K](https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm)).
- **JX Advanced Metals:** the non-China InP substrate alternative, expanding 7-10x ([JX](https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html)).
- **AAOI:** lower margin (non-GAAP GM 28.7%); PP&E up from $376M to $1,044M in nine months; US expansion delayed by power and construction issues ([8-K](https://www.sec.gov/Archives/edgar/data/1158114/000168316826008351/aaoi_ex9901.htm)).
- **Aehr:** a burn-in "judge" for AI processors, but photonics is not yet material ([8-K](https://www.sec.gov/Archives/edgar/data/1040470/000165495426009385/aehr_ex991.htm)).

### Inferences

#### (a) Classification of main products

| Company | Product | BRIDGE / SUCCESSOR | Successor and date | Slips observed |
|---|---|---|---|---|
| Lumentum | EML lasers for pluggables | BRIDGE | CW/UHP lasers for SiPh and CPO (scale-out CPO from 2026; scale-up 2028) | None found. Nov 2025 talk of a "broader ramp 2H CY26" is consistent with about $50M UHP run-rate in Dec-2026 qtr |
| Lumentum | Cloud Light 800G/1.6T modules | BRIDGE | NPO (late 2027-28), CPO | n/a |
| Lumentum | UHP lasers / ELS modules | SUCCESSOR | Volume scale-up 2H CY2027 for 2028 deployments | None found |
| Lumentum | OCS | SUCCESSOR-type (new switching layer) | Shipping; in-tray OCS 2028 | n/a |
| Coherent | 800G/1.6T transceivers | BRIDGE | PhotonLink CPO/NPO | n/a |
| Coherent | InP lasers (6-inch) | Both | Same InP base feeds pluggables and PhotonLink | n/a |
| Coherent | PhotonLink | SUCCESSOR | Ramp Q4 CY2026; >$250M/qtr target before end CY2027; second anchor revenue early CY2028 | Too early to judge |
| Innolight / Eoptolink | Plug-in modules (incl. LPO) | BRIDGE | NPO/CPO; no verified product qualification | n/a |
| Fabrinet | Assembly services | Both (process-agnostic) | NPO revenue 2H FY27 (Jan-Jun 2027); CPO "further out" | CPO timing at Fabrinet is later than NVIDIA's 2026 start |
| Tower | SiPh wafers | Both | NPO 2H 2027; 300mm Track-1 Q3 2027 | None found |

#### "Judge" vs physical constraint
- None of the six owns a "judge" in the strict sense of a measurement or qualification gate. The test makers (Quantifi/Teradyne, ficonTEC, Aehr, FormFactor, Keysight) are the candidates, but evidence of production-qualified CPO test share was not found.
- Lumentum, Coherent, AXT/JX and Tower own physical constraints: InP laser fab capacity and know-how, InP substrates, SiPh process know-how and capacity.
- Innolight, Eoptolink and Fabrinet own scale and process know-how in assembly. That is real but more replicable, as shown by fast capacity adds at AAOI (PP&E nearly 3x) and Fabrinet (+72% capacity in about 7 months).

#### (e) Resilience to the three 2030 scenarios (judgement, based on the cited data)

| Company | Steady growth (55%) | Financing-led pause ~2028 (25%) | Acceleration (20%) |
|---|---|---|---|
| Lumentum | Strong: sold-out lasers, CPO/OCS ramps | Moderate: 37% customer, convert balance; merger closing 1H 2028 lands in the pause window; contracted commitments cushion | Strongest: binding laser constraint lets it raise prices |
| Coherent | Strong growth but cash-hungry | Weakest of the US names: net debt about $2.25B and FCF about -$0.9B/qtr; a slip in 2028 PhotonLink revenue would need new financing | Strong if 6-inch InP yields hold |
| Innolight | Strong | Moderate: bridge product, top-5 customers 76%, 91% overseas, pricing pressure, 9M capex RMB 9.2B; but net cash about RMB 55B is a very large cushion | Constrained by laser supply |
| Eoptolink | Moderate: already slowing q/q | Weakest: inventory RMB 17.4B, OCF falling | Constrained by chips |
| Fabrinet | Strong (capacity to $10B) | Moderate-strong: net cash, low capital intensity, variable labour cost, diversified customers | Strong (capacity lead) |
| Tower | Strong (capacity 3x by Q3 2027) | Strongest: prepayments, contracts to 2029, net cash about $1.3B; but fixed-cost fabs | Strong; capacity-limited |

#### Cycle position
Classic late-upcycle markers are present:
- record inventories: Eoptolink +141% YTD, Lumentum $808M;
- negative operating cash flow during heavy expansion (Coherent);
- capacity being doubled or tripled across the chain: Tower 3x, AXT 2x, JX 7-10x, Coherent InP 2x, Fabrinet to $10B, AAOI to 1M units/month;
- equity raised at the top: Innolight's HK IPO, AXT's US$632M offering.
- Cignal: "AI has not solved the classic semiconductor inventory cycle" ([Cignal ECOC](https://cignal.ai/2026/09/ecoc-2026-show-report/)), and LightCounting's "bumpy ride" 2027-2030 scenario.
Upstream lasers and substrates are still short (pricing up), while module makers show the first q/q decline (Eoptolink).

#### Export controls
- China plus Hong Kong is 27.6% of Lumentum's ship-to revenue, and Lumentum's sale to Marvell needs Chinese approval. China therefore holds leverage over the largest US laser maker until 1H 2028.
- AXT's China-only production makes its InP output dependent on Beijing's permits. JX and Sumitomo (Japan) are the hedge.
- Chinese module makers serve US demand from Thailand and Mexico under the 25% Section 301 regime.

### Gaps
- ROIC/ROE for all six: not computed (invested-capital and equity data not retrieved).
- Lumentum FY2026 audited full-year concentration and product split; Lumentum's actual Q1 FY27 OCS revenue.
- Innolight and Eoptolink customer IDENTITIES (annual reports anonymise them as A-E). The identity of Innolight's associate company, which bought RMB 3.1B in 2025, was not established. Country split beyond domestic vs overseas is not disclosed.
- Tower customer concentration and SiPh customer names; GlobalFoundries/TSMC/ST SiPh revenue for comparison.
- Coherent PhotonLink and NVIDIA purchase-commitment amounts; Coherent customer names.
- No 2026 financial data was retrieved for Mitsubishi Electric, Sumitomo Electric, Furukawa (optical) or TFC.

---

## 3. Path-forward evidence and suggested verdicts

### Takeaway
Every key company must get through transition (2), plug-in modules to CPO, and most through (1), copper to optics between processors. Transitions (3) hybrid bonding matters mainly for Tower vs TSMC. Transitions (4)-(6) are marginal for this segment. The best-funded successor plans are Lumentum (NVIDIA $2B, >$5B commitments, Marvell) and Tower (prepayments, self-funded capacity to 2027). Coherent's plan is strategically sound but cash-negative. The Chinese module makers have funded bridges (cash, capacity) but no verified successor qualification.

### Cited Findings

#### Demand-driver timing (context only; other researcher owns CPO systems)
- NVIDIA "pushed CPO to market" in spring 2026, choosing scale-out first because pluggables are its backup plan.
- NVIDIA and Lumentum concurrently announced scale-up CPO for 2028.
- Cisco: CPO is "inevitable but not imminent"; NVIDIA's approach is "supplier-push".
- Source: [Cignal OFC 2026](https://cignal.ai/2026/03/ofc-2026-show-report/).
- Broadcom Davisson CPO samples at ECOC (Sep 2026); "NPO dominated the conversations but lacked definitive detail" ([Cignal ECOC](https://cignal.ai/2026/09/ecoc-2026-show-report/)).
- Copper stays dominant inside GPU racks in 2027 ([TrendForce](https://www.trendforce.com/presscenter/news/20261102-13291.html)).

#### Lumentum: SAID vs DONE
- **SAID** (company):
  - UHP laser run-rate about $50M in Dec-2026 quarter;
  - high-volume scale-up UHP from 2H CY2027 for 2028 deployments;
  - NPO late 2027-2028;
  - OCS "could become a multi-billion-dollar annual revenue stream";
  - Sources: [release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx); [Finsee](https://finsee.ai/earnings/lite/2027/q1/en/); [MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/).
- **DONE:**
  - first ELS module purchase order received ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/));
  - second NPO/CPO win with >$5B commitments (company claim);
  - $2.0B NVIDIA preferred received ([10-Q R74](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R74.htm));
  - net PP&E up from $1,159.1M to $1,410.4M in one quarter; Greensboro NC facility in process qualification ([release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx));
  - Aixtron G10-AsP orders ([Aixtron](https://www.aixtron.com/en/press/press-releases));
  - agreed all-stock combination with Marvell, close 1H CY2028, with >$1B run-rate cost synergies targeted ([Marvell](https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity)).

#### Coherent: SAID vs DONE
- **SAID** (company): PhotonLink >$100M in the Mar-2027 quarter and >$250M/qtr before end CY2027; second anchor ($20B over 5 years) from early CY2028; non-GAAP GM >45% before end CY2028 ([Futurum](https://futurumgroup.com/?p=97623)).
- **DONE:**
  - PhotonLink launched at ECOC on 21 Sep 2026 ([Semiconductor Today](https://semiconductor-today.com/news_items/2026/sep/coherent-220926.shtml));
  - InP output 2x y/y;
  - FY26 capex $1.10B and Q1 FY27 capex $0.78B ([10-K R8](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R8.htm); [release](https://finviz.com/news/415844/coherent-corp-reports-first-quarter-fiscal-2027-results));
  - divested aerospace & defense ($391.1M proceeds in Q1 FY26) ([release](https://finviz.com/news/415844/coherent-corp-reports-first-quarter-fiscal-2027-results));
  - NVIDIA $2B received.

#### Innolight: SAID vs DONE
- **DONE:**
  - HK$60.9B raised (Jul 2026); 9M 2026 cash raised from investors RMB 54.54B ([Q3 report](http://static.cninfo.com.cn/finalpage/2026-10-30/1225643953.PDF));
  - 9M 2026 capex RMB 9.16B (vs RMB 1.61B); construction in progress up to RMB 5.50B (same source);
  - 1.6T volume driving GM ([ifeng](https://finance.ifeng.com/c/8xcyvWhXO0b); [ComSoc](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/)).
- **SAID:** no verified 2026 statement on CPO/NPO wins was retrieved.

#### Eoptolink: SAID vs DONE
- **SAID:** "layouts" in LPO/LRO, XPO, NPO and CPO.
- **DONE:** capacity build (fixed assets +49%); supply pre-stocking ([CITIC](https://m.gelonghui.com/news/5342407)).

#### Fabrinet: SAID vs DONE
- **SAID:** NPO revenue in 2H FY27; CPO further out; Building 11 by end FY2028.
- **DONE:** Building 10 partly producing; second Santa Clara campus bought ($77M); OCS and multi-rail capacity installed ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/)).

#### Tower: SAID vs DONE
- **SAID:** SiPh capacity 3x by Q3 2027; Track-2 Japan by 2029; NPO "appreciable" 2H 2027.
- **DONE:** all Track-1 tools ordered; $920M programme about 65% paid; customer advances of $341M on the balance sheet; NewPhotonics heterogeneous InP-on-SiPh in initial production ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/); [6-K](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm)).

### Inferences (suggested verdicts)
- **Lumentum: COHERENT.**
  - Transitions: (1) and (2) directly, as the laser source for scale-out and scale-up CPO, plus OCS.
  - Bridge (EML, modules) and successor (UHP/ELS, OCS) share the same InP fabs, so a slip in CPO moves volume back to EML/CW for pluggables rather than stranding capacity.
  - Funded through a 1-2 year slip: net cash about $0.6B, positive FCF, NVIDIA capital and commitments.
  - Timing plausible (2H 2027 volume for 2028).
  - What must go right: UHP reliability at scale; Marvell deal approval (US/China); reducing 37% single-customer exposure.
  - The main risk to the verdict is the Cignal-forecast EML-to-SiPh shift. It is partly self-hedged because Lumentum also sells CW lasers.
- **Tower: COHERENT.**
  - Transitions: (1), (2) and (3); heterogeneous die-to-wafer bonding is its answer to TSMC's integrated COUPE path.
  - Its SiPh wafers serve 1.6T pluggables today and NPO next, so a CPO slip extends pluggable demand it already serves.
  - Funded: self-funded plus prepayments; capacity contracted to 2029.
  - What must go right: NPO wins converting in 2H 2027, and avoiding the GlobalFoundries patent and Intel disputes. The open risk is that NVIDIA-style CPO concentrates at TSMC.
- **Fabrinet: COHERENT (low-margin version).**
  - Process-agnostic: it builds pluggables, OCS, NPO and later CPO, so either side of the transition uses it.
  - Funded with net cash.
  - Weakness: CPO volume for it is "further out", and NVIDIA's revenue share has been falling since FY24. CPO engine assembly may sit with TSMC/OSATs rather than with Fabrinet.
- **Coherent: PARTLY COHERENT.**
  - The strategy is right (vertical InP, 6-inch, PhotonLink, two anchors).
  - It is not self-funded through a slip: FCF was about -$1.0B in FY26 and about -$0.87B in Q1 FY27, with net debt about $2.25B. The $20B anchor contract only starts in 2028.
  - Timing plausible, but a 1-2 year CPO slip would likely force more debt or equity.
- **Innolight: PARTLY COHERENT.**
  - A dominant, well-funded bridge (IPO cash), and pluggables persist longer than roadmaps (1.6T at 56% of 2027 pluggable revenue per TrendForce; NPO is pluggable-adjacent).
  - No verified successor qualification. In CPO the optical engine moves into the switch package (TSMC/NVIDIA/Broadcom), reducing a module maker's role to assembly or ELS sub-assembly.
- **Eoptolink: PARTLY COHERENT, trending to NOT COHERENT.** It is the same bridge-only position as Innolight, with weaker cash conversion, inventory risk and q/q decline already visible.

### Gaps
- Verified CPO/NPO qualifications for Innolight, Eoptolink, AAOI, Accelink and other Chinese makers.
- Actual 2026 CPO switch unit volumes and which laser/ELS suppliers are in NVIDIA Quantum-X/Spectrum-X Photonics (other researcher).
- The status of TSMC's COUPE capacity ramp (15x claim) was not verified (see section 5).

---

## 4. Suggested ordering of key companies by quality alone

### Takeaway
Suggested ordering: 1 Lumentum; 2 Tower; 3 Innolight; 4 Coherent; 5 Fabrinet; 6 Eoptolink. Ties I cannot separate cleanly: Tower vs Innolight, and Coherent vs Fabrinet.

### Cited Findings (comparison, latest quarter)

| Metric | Lumentum (Sep-26 qtr) | Tower (Sep-26 qtr) | Innolight (Q3 26) | Coherent (Sep-26 qtr) | Fabrinet (Sep-26 qtr) | Eoptolink (Q3 26) |
|---|---|---|---|---|---|---|
| Revenue growth y/y | +136.5% | +33% | +171.8% | +49.9% | +51% | +80.3% (-13% q/q) |
| Gross margin | 53.2% non-GAAP | ~34% | ~46.6% (secondary) | 40.6% non-GAAP | 12.1% non-GAAP | 46.3% |
| Op / net margin | 42.3% non-GAAP op | ~24% op; 23% net | ~30.9% net | 23.2% non-GAAP op | 10.8% non-GAAP op | ~35% net |
| FCF (latest qtr) | ~+$38M | ~-$6M (9M +$338M) | 9M: about -RMB 1.15B (OCF 8.01B, capex 9.16B) | ~-$868M | -$137M | 9M: about -RMB 0.34B (OCF 1.46B, capex 1.81B) |
| Net cash (debt) | ~+$0.58B | ~+$1.32B | about +RMB 55B (30 Sep 2026) | ~-$2.25B | ~+$0.68B | about +RMB 6.8B, no borrowings |
| Largest customer / top-5 | 37% (qtr) | n/a | 24.1% / 76.0% (2025) | 20% (FY26) | 19.9% / four 10%+ = 57.4% (FY26) | 23.0% / 72.3% (2025) |
| Position | InP laser constraint | SiPh capacity constraint | Bridge scale leader | InP constraint + bridge | Assembly know-how | Bridge #2 |

Sources: as in section 2 ([Lumentum release](https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx); [Lumentum 10-Q R6/R82](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R82.htm); [Tower 6-K](https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm); [Innolight/ifeng](https://finance.ifeng.com/c/8xcyvWhXO0b); [Coherent release](https://finviz.com/news/415844/coherent-corp-reports-first-quarter-fiscal-2027-results); [Fabrinet release](https://finviz.com/news/413587/fabrinet-announces-first-quarter-fiscal-year-2027-financial-results); [Eoptolink/CITIC](https://m.gelonghui.com/news/5342407)).

### Inferences
1. **Lumentum.** It owns the scarcest physical constraint, has the best margins, positive FCF while expanding, and its successor plan is funded and validated by NVIDIA and Marvell. Deductions: 37% single-customer concentration, converts outstanding, and merger and China-approval risk to 1H 2028. Note for the ranking: from 1H 2028 it is expected to be part of Marvell.
2. **Tower.** It has the most contract-backed revenue model, net cash and positive 9M FCF. Its SiPh platform straddles bridge and successor. Lower growth and margins than Lumentum, and the risk that CPO value concentrates at TSMC.
3. **Innolight.** The share leader, with very high profitability and IPO-funded resilience. Ranked below the constraint-owners because its main product is a bridge. Its top-5 customers are 76% of 2025 sales (largest 24%; 8% to a related associate) and 91% of revenue is overseas, so it has China/US trade exposure. Its single-customer concentration is lower than Lumentum's 37%. Net cash of about RMB 55B after the HK IPO is the largest cushion among the six, but 9M 2026 FCF was negative, with capex up 5.7x. The Tower-Innolight tie cannot be separated on current evidence: Innolight wins on margins and growth, Tower on position and contract quality.
4. **Coherent.** Its position (6-inch InP, PhotonLink, two anchors) is close to Lumentum's, but its financial strength is the weakest of the US names: FCF about -$1.0B in FY26, net debt about $2.25B, GM about 41%.
5. **Fabrinet.** Clean balance sheet, diversified customers, and it benefits whichever technology wins. But a 12% GM and a replicable, labour-based model limit its quality. The Coherent-Fabrinet tie cannot be separated cleanly: Coherent has the better position, Fabrinet the better finances.
6. **Eoptolink.** A bridge-only position, the first sequential decline, a 141% inventory build and collapsing OCF.

### Gaps
- No ROIC comparison was possible.
- Innolight's and Eoptolink's customers are anonymised (A-E), so it is not known how much of their concentration is NVIDIA vs hyperscalers.
- Tower's concentration is unknown.

---

## 5. Check of each background prior

### Takeaway
- Prior 1: confirmed for "began shipping in 2026"; the 15x capacity figure is unverified.
- Prior 2: confirmed (2028 plan); no slip evidence yet.
- Prior 3: updated. Lasers are binding in 2026-27; whether optics bind in 2028-30 is now uncertain given the scale of capacity additions.
- Prior 4: partly confirmed. Pluggables keep growing strongly through 2027, and within pluggables the EML bridge component is already losing share to SiPh.

### Cited Findings
- **Prior 1: CPO switches began shipping in 2026; NVIDIA and its packaging partner plan a 15-fold rise in optical-engine capacity by mid-2027.**
  - NVIDIA "pushed CPO to market" in spring 2026 ([Cignal OFC 2026](https://cignal.ai/2026/03/ofc-2026-show-report/)).
  - Lumentum: the lead CPO customer's production plans are "on track" and its demand signal has strengthened (company, [MarketBeat, Aug 2026](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)); UHP laser run-rate about $50M in Dec-2026 quarter (company, [Finsee](https://finsee.ai/earnings/lite/2027/q1/en/)).
  - Coherent PhotonLink revenue ramp from Q4 CY2026 (company, [Semiconductor Today](https://semiconductor-today.com/news_items/2026/sep/coherent-220926.shtml)).
  - Broadcom Davisson CPO samples, Sep 2026 ([Cignal ECOC](https://cignal.ai/2026/09/ecoc-2026-show-report/)).
  - The 15x optical-engine capacity figure was not found in any source retrieved.
- **Prior 2: processor-to-processor optics planned for 2028, may slip to 2028-29; copper stretched to 2027-28.**
  - NVIDIA and Lumentum announced scale-up CPO for 2028 (OFC, Mar 2026) ([Cignal](https://cignal.ai/2026/03/ofc-2026-show-report/)).
  - Lumentum: high-volume scale-up UHP shipments 2H CY2027 "ahead of customer deployments in 2028" ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)).
  - Coherent's second anchor customer revenue starts early CY2028 ([Futurum](https://futurumgroup.com/?p=97623)).
  - Fabrinet: CPO "further out" ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/)).
  - Copper remains dominant inside GPU racks in 2027 ([TrendForce](https://www.trendforce.com/presscenter/news/20261102-13291.html)).
- **Prior 3: optical links a binding constraint on AI compute in 2028-2030.**
  - Evidence of current binding:
    - laser supply gap above 30% of demand (Lumentum, prior quarter; [Finsee](https://finsee.ai/earnings/lite/2027/q1/en/));
    - pump lasers sold out (Lumentum); "sells all the lasers it can build" (Cignal opinion);
    - NVIDIA buying capacity rights at Lumentum and Coherent ([Verdict](https://www.verdict.co.uk/nvidia-invests-lumentum-coherent/));
    - Eoptolink pre-stocking against chip shortages ([CITIC](https://m.gelonghui.com/news/5342407));
    - JX: demand growing "faster than previously expected" ([JX](https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html)).
  - Evidence of relief by 2028:
    - Tower 3x SiPh capacity by Q3 2027 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/));
    - Coherent InP output 2x y/y ([Futurum](https://futurumgroup.com/?p=97623)); AXT capacity 2x ([AXT](https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm));
    - JX 7-10x over four years;
    - Fabrinet $10B capacity by Jan 2027 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/));
    - AAOI >1M units/month by end 2027 ([AAOI](https://www.sec.gov/Archives/edgar/data/1158114/000168316826008351/aaoi_ex9901.htm));
    - LightCounting's "bumpy ride" correction scenario for 2027-2030 is "plausible" ([ComSoc](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/)).
- **Prior 4: bridging hardware loses share in 2028-2030; bridges last longer than roadmaps.**
  - Pluggables +76% in 2027 to $84.1B, with 1.6T at 56% of revenue ([TrendForce](https://www.trendforce.com/presscenter/news/20261102-13291.html)); Ethernet transceivers +76% in 2027 ([LightCounting via ComSoc](https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/)).
  - NVIDIA chose scale-out CPO first because pluggables are its fallback ([Cignal](https://cignal.ai/2026/03/ofc-2026-show-report/)).
  - Fabrinet calls pluggable, NPO and CPO complementary.
  - SiPh to 60% of the datacom front end by 2030, at EML's expense ([Cignal](https://cignal.ai/2026/10/update-to-cignal-ais-datacom-optical-front-end-forecast/)).

### Inferences
- **Prior 1: CONFIRMED** (shipping began in 2026, in early, supplier-pushed volume). The 15x capacity statement is UNVERIFIED here; the CPO/packaging researcher should check it.
- **Prior 2: CONFIRMED as the plan** (2028 scale-up optics, with lasers in volume from 2H 2027). No slip announced as of 12 Nov 2026. The best early slip indicators to watch are Lumentum's UHP run-rate and Coherent's PhotonLink >$100M Mar-2027 target.
- **Prior 3: UPDATED.**
  - The constraint is real today but is specifically InP lasers and substrates, not "optical links" generically.
  - Announced capacity growth across SiPh (3x), InP (2x now, 7-10x at JX) and assembly (Fabrinet +72%, AAOI 3x) makes a broad optical constraint in 2028-30 less certain.
  - What could still bind: high-power CW/UHP lasers for ELS, which have stringent reliability and are a new product class, and CPO test/assembly tooling.
  - An overshoot (oversupply) in 2028 is a plausible alternative.
- **Prior 4: PARTLY CONFIRMED, timing nuanced.**
  - No source quantifies pluggable share loss in 2028-30.
  - Current forecasts show pluggables growing strongly through 2027.
  - Inside pluggables, the first bridge component to lose share is the EML, to SiPh plus CW.
  - NPO, which is pluggable-like, is the near-term successor (2H 2027), which supports "bridges last longer".

### Gaps
- LightCounting/Cignal/Yole CPO port and revenue forecasts for 2028-2030 (paywalled).
- Pluggable share of optical-link revenue in 2028-2030.
- Evidence of any announced CPO slip at NVIDIA (the other researcher should check).

---

## 6. Open question: which successor ships in volume first, and who captures the value

### Takeaway
On the evidence, volume arrives in this order:
- SiPh-based pluggables (already the majority at 1.6T);
- NPO (2H 2027: Tower, Fabrinet, Lumentum);
- scale-out CPO switches (shipping from 2026 in early volume);
- scale-up processor-to-processor CPO (2028).

Value is currently captured most by InP laser and substrate owners, and the integrated giants are moving to own them rather than bypass them. NVIDIA invested $2B in each of the two US laser makers, and Marvell is buying Lumentum. Module specialists keep high margins while pluggables last, but have no verified CPO role.

### Cited Findings
- Nearly all 1.6T optics ship as SiPh DR ([Cignal](https://cignal.ai/2026/06/datacom-optical-component-revenue-doubles-to-7-7-billion-in-1q26/)); SiPh to 60% of the front end by 2030 ([Cignal](https://cignal.ai/2026/10/update-to-cignal-ais-datacom-optical-front-end-forecast/)).
- NPO dates: Tower "appreciable" NPO shipments 2H 2027 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/)); Fabrinet NPO revenue 2H FY27 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/)); Lumentum NPO late 2027-28 ([MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/)); ECOC: NPO "lacked definitive detail" ([Cignal](https://cignal.ai/2026/09/ecoc-2026-show-report/)).
- Integration moves:
  - Marvell-Lumentum, "end-to-end" with "co-designed, pre-validated optical solutions" ([Marvell](https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity));
  - Credo (SerDes/DSP/AEC vendor) bought DustPhotonics (SiPh PICs) on 28 May 2026 for about $1.25B total consideration, to build "a vertically integrated connectivity stack", after buying Hyperlume (microLED optical interconnect) in Sep 2025 ([Credo 10-Q R12](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R12.htm));
  - Cignal: the deal signals the value chain "compressing", and could mirror Broadcom's 20-year Ethernet position ([Cignal](https://cignal.ai/2026/11/marvell-acquires-lumentum/));
  - TrendForce: the deal fills Marvell's InP laser gap and challenges Broadcom ([TrendForce](https://www.trendforce.com/presscenter/news/20261103-13294.html));
  - CPO "moves some optical component value from pluggable transceivers into switching equipment" ([TrendForce](https://www.trendforce.com/presscenter/news/20261102-13291.html)).
- Laser-anchored contracts: Coherent's $20B agreement is "anchored by a laser rather than a finished transceiver" ([Credence](https://www.credenceresearch.com/news/coherent-photonlink-20-billion-five-year-agreement-ai-data-center)); NVIDIA bought capacity rights for "advanced laser components" ([Evertiq](https://evertiq.com/design/2026-03-04-nvidia-to-invest-2-billion-in-lumentum-under-new-optics-partnership)).
- Margins (section 1 Inferences): lasers 53% and substrates 56% vs modules about 46% vs assembly 12%.
- Opinion (secondary): excess profit ultimately stays in chip IP rather than assembly; CPO is a medium-to-long-term threat to module assembly ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).

### Inferences
- In CPO the laser is the one optical component that stays external and replaceable (ELS) and requires a new high-power InP product. That keeps laser specialists, or whoever owns them (Marvell-Lumentum), in the value chain, and probably at higher content per port than in an EML pluggable.
- The optical engine itself (PIC plus EIC, hybrid-bonded) migrates toward the switch-ASIC owner and its foundry (NVIDIA/TSMC, Broadcom, Marvell). That is the part module specialists lose.
- Module specialists (Innolight, Eoptolink) capture value as long as pluggables and NPO dominate, which is through 2027 at least, and longer on the server/NIC side. Their margin premium looks cyclical.
- Contract assemblers (Fabrinet) and merchant SiPh foundries (Tower) are hedged: they serve both sides. But CPO may route through TSMC and OSATs instead.

### Gaps
- No third-party estimate of value per port (pluggable vs CPO) by component class was obtained.
- TSMC COUPE pricing and capacity, and Broadcom's CPO supply chain (laser source, assembler), were not verified.

---

## 7. What could not be verified

### Takeaway
All seven "leads to verify" were checked. Four are confirmed with primary or strong secondary evidence (NVIDIA investments, Innolight HK listing, Tower expansion, Teradyne-Quantifi), two are partly confirmed (laser shortages; RoboTechnik-ficonTEC), and one is not re-verified (China's InP export licensing). The coordinator passed on two more leads from another researcher, and both are confirmed from primary filings: Marvell-Lumentum (Marvell release, 2 Nov 2026) and Credo-DustPhotonics (Credo 10-Q). The Credo figures are updated: closed 28 May 2026, about $1.25B total including a $310M contingent earn-out.

### Cited Findings (status of leads)
- **NVIDIA about $2B each in Lumentum and Coherent with multi-year supply commitments (Mar 2026): CONFIRMED.**
  - Announced 2-3 Mar 2026 ([Verdict](https://www.verdict.co.uk/nvidia-invests-lumentum-coherent/)).
  - Lumentum: 2.9M Series A convertible preferred for $2.0B net ([10-Q R74](https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R74.htm)).
  - Coherent: $1,998.6M share issuance in FY26 ([10-K R8](https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R8.htm)).
  - Commitment amounts are undisclosed ("multibillion").
- **EML and CW laser shortages through 2026: PARTLY CONFIRMED.**
  - EML and laser-chip shortages: confirmed by company statements (Lumentum) and broker commentary (Eoptolink, CITIC). See [MarketBeat](https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/), [Finsee](https://finsee.ai/earnings/lite/2027/q1/en/), [CITIC](https://m.gelonghui.com/news/5342407).
  - CW shortage: weaker evidence; one secondary source called CW supply comfortable ([Photoncap](https://photoncap.net/p/chinese-optical-modules-own-7-of)).
- **Innolight Hong Kong listing: CONFIRMED (secondary).** Listed 30 Jul 2026; about HK$60.9B raised ([ifeng/Leiduo](https://finance.ifeng.com/c/8xcyvWhXO0b)). The HKEX prospectus was not retrieved.
- **Tower expanding SiPh capacity: CONFIRMED.** $920M programme; 3x by Q3 2027 ([MarketBeat](https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/)).
- **China export licensing for InP in 2025: NOT RE-VERIFIED.** AXT's Q3 2026 release still lists "the receipt of export permits" as a risk ([AXT 8-K](https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm)). AXT's revenue trough at $18.0M in Q2 2025 and recovery to $73.4M in Q3 2026 ([10-Q](https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm)) is consistent with a 2025 permit disruption that has since eased (inference).
- **RoboTechnik completed its purchase of ficonTEC: PARTLY CONFIRMED.** ficonTEC's site presents RoboTechnik's Hong Kong listing as enabling "ficonTEC's next phase of growth", which implies ownership; the completion date was not found ([ficonTEC](https://www.ficontec.com/)).
- **Teradyne bought Quantifi Photonics: CONFIRMED.** "Quantifi Photonics Limited, A Teradyne Company" ([Quantifi](https://www.quantifiphotonics.com/)); deal date not found.
- **Marvell-Lumentum all-stock combination (lead from another researcher, 2 Nov 2026): CONFIRMED (primary).** Marvell release, 2 Nov 2026: 4.500 Marvell shares per Lumentum share; about 67%/33% pro forma ownership; close expected 1H CY2028; shareholder and regulatory approvals needed ([Marvell](https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity)). TrendForce says US and China approval is needed ([TrendForce](https://www.trendforce.com/presscenter/news/20261103-13294.html)). Lumentum has filed multiple Form 425 communications since 2 Nov 2026 ([SEC submissions](https://data.sec.gov/submissions/CIK0001633978.json)). Effect on notes: Lumentum is ranked as a standalone company today but is expected to become part of Marvell from 1H 2028.
- **Credo completed its purchase of DustPhotonics, about $750M cash plus stock, by 1 Aug 2026 (lead from another researcher): CONFIRMED, with updated figures (primary).**
  - Credo acquired 100% of DustPhotonics Ltd on 28 May 2026.
  - Total purchase consideration about $1.25B: $769.6M cash, $169.1M fair value of shares issued, $310.0M contingent earn-out ($10M liability plus $300M equity, payable in cash and shares), $2.5M replacement awards. Goodwill $895.8M.
  - Described as "a developer of Silicon Photonics Photonic Integrated Circuit technology for optical transceivers", acquired to build "a vertically integrated connectivity stack".
  - Sources: Credo 10-Q for the quarter ended about 1 Aug 2026, filed 2 Sep 2026 ([R12](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R12.htm); [R37](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R37.htm); [R38](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R38.htm)).
  - Effect on notes: DustPhotonics moves from "Israeli private firm" to a unit of Credo (Nasdaq: CRDO). That is another case of a DSP/SerDes silicon vendor integrating optics (alongside Marvell-Lumentum).

### Inferences
- The InP licensing question matters most for AXT, whose production is all in China, and for Chinese buyers. For Western laser makers, JX's 7-10x expansion and in-house growth (Coherent) are the mitigation.

### Gaps (not verified; would need follow-up searches)
- China MOFCOM's 2025 indium-item control list and whether InP is explicitly covered; current permit lead times.
- Status of China's suspension of the Dec-2024 gallium/germanium ban on exports to the US. Per background knowledge it was suspended until 27 Nov 2026, which is two weeks after this research date; renewal status is unverified and matters for GaAs VCSEL substrates.
- Any US restriction (entity list, FCC, procurement) specifically on Chinese optical modules.
- LPO adoption rates (LightCounting covers LPO/LRO, but figures are paywalled).
- 800G/1.6T qualification lists at Google, Meta, Microsoft, Amazon and Oracle (only Fabrinet's 10-K names NVIDIA, Amazon, Cisco and Nokia as 10%+ customers).
- Third-party shares for EML, CW, UHP and VCSEL lasers; SiPh foundry shares; photonic test-equipment shares and customers.
- Whether CPO test is a production bottleneck: no data. Cignal names tooling investment as a CPO hurdle (opinion).
- Dongshan Precision's acquisition of Source Photonics; IQE sale outcome; GlobalFoundries-AMF; ST PIC100 ramp; TSMC COUPE capacity (15x).
- Japanese (TDnet/EDINET), Taiwanese (MOPS), Korean (DART) and Indian (NSE/BSE) filings were not searched because the search budget was exhausted. Furukawa's H1 FY results (9 Nov 2026) are listed but were not read ([Furukawa](https://www.furukawaelectric.com/en/release/)).

---

## 8. Sources (URL; date published or period; type)

### Takeaway
Primary sources cover the six key companies well: SEC 10-K/10-Q/8-K/6-K XBRL pages, company releases and IR lists. Market-level data is secondary: Cignal AI public summaries, LightCounting via IEEE ComSoc, TrendForce press releases, Chinese brokerage and press. Region coverage outside the US, China and Israel is thin.

### Cited Findings
**Primary: company filings and releases**
- Lumentum Q1 FY27 release, 2 Nov 2026 (qtr to 26 Sep 2026): https://investor.lumentum.com/financial-news-releases/news-details/2026/Lumentum-Announces-First-Quarter-of-Fiscal-Year-2027-Financial-Results/default.aspx
- Lumentum 10-Q Q1 FY27 XBRL pages, filed 3 Nov 2026: https://www.sec.gov/Archives/edgar/data/1633978/000162828026069615/R6.htm ; .../R74.htm ; .../R80.htm ; .../R82.htm ; .../R83.htm (same directory)
- Lumentum SEC submissions index (filings list incl. 425s, Nov 2026): https://data.sec.gov/submissions/CIK0001633978.json
- Marvell-Lumentum combination release, 2 Nov 2026: https://investor.marvell.com/news-events/press-releases/detail/1040/marvell-and-lumentum-to-combine-creating-a-category-leader-in-ai-connectivity
- Marvell press release list (accessed 12 Nov 2026): https://investor.marvell.com/news-events/press-releases
- Coherent Q1 FY27 release, 4 Nov 2026 (qtr to 30 Sep 2026): https://finviz.com/news/415844/coherent-corp-reports-first-quarter-fiscal-2027-results
- Coherent 10-K FY26 XBRL pages, filed 14 Aug 2026: https://www.sec.gov/Archives/edgar/data/820318/000082031826000020/R8.htm ; .../R57.htm ; .../R58.htm ; .../R103.htm
- Coherent 10-Q Q1 FY27 geography page, filed 4 Nov 2026: https://www.sec.gov/Archives/edgar/data/820318/000082031826000023/R73.htm
- Fabrinet Q1 FY27 release, 2 Nov 2026 (qtr to 25 Sep 2026): https://finviz.com/news/413587/fabrinet-announces-first-quarter-fiscal-year-2027-financial-results
- Fabrinet 10-K FY26 XBRL pages, filed 18 Aug 2026: https://www.sec.gov/Archives/edgar/data/1408710/000140871026000028/R111.htm ; .../R56.htm ; .../R57.htm
- Fabrinet 10-Q Q1 FY27, filed 3 Nov 2026: https://www.sec.gov/Archives/edgar/data/1408710/000140871026000041/R42.htm
- Tower Semiconductor Q3 2026 6-K exhibit 99.1, 2 Nov 2026: https://www.sec.gov/Archives/edgar/data/0000928876/000117891326004949/exhibit_99-1.htm
- AXT Q3 2026 8-K exhibit, 29 Oct 2026: https://www.sec.gov/Archives/edgar/data/1051627/000143774926033941/ex_1013304.htm
- AXT 10-Q Q2 2026, filed 13 Aug 2026: https://www.sec.gov/Archives/edgar/data/1051627/000143774926027677/axti20260630_10q.htm
- Applied Optoelectronics Q3 2026 8-K exhibit 99.1, 5 Nov 2026: https://www.sec.gov/Archives/edgar/data/1158114/000168316826008351/aaoi_ex9901.htm
- Aehr Test Systems Q1 FY27 8-K exhibit 99.1, 2 Nov 2026: https://www.sec.gov/Archives/edgar/data/1040470/000165495426009385/aehr_ex991.htm
- JX Advanced Metals InP capacity release, 16 Jun 2026: https://www.jx-nmm.com/english/newsrelease/fy2026/20260616_02.html
- Aixtron press releases (items 19 May, 23 Jul, 12 Nov 2026; accessed 12 Nov 2026): https://www.aixtron.com/en/press/press-releases
- Furukawa Electric release list (accessed 12 Nov 2026): https://www.furukawaelectric.com/en/release/
- Teradyne press releases (accessed 12 Nov 2026): https://investors.teradyne.com/news-events/press-releases
- Quantifi Photonics homepage (2026): https://www.quantifiphotonics.com/
- ficonTEC homepage (accessed 12 Nov 2026): https://www.ficontec.com/
- Coherent PhotonLink launch (Semiconductor Today, 22 Sep 2026; based on company release): https://semiconductor-today.com/news_items/2026/sep/coherent-220926.shtml
- Innolight (Zhongji Innolight) 2025 annual report, cninfo, pub. 31 Mar 2026: http://static.cninfo.com.cn/finalpage/2026-03-31/1225056459.PDF
- Innolight Q3 2026 report, cninfo, pub. 30 Oct 2026: http://static.cninfo.com.cn/finalpage/2026-10-30/1225643953.PDF
- Eoptolink 2025 annual report, cninfo, pub. 24 Apr 2026: http://static.cninfo.com.cn/finalpage/2026-04-24/1225172598.PDF
- Eoptolink Q3 2026 report, cninfo, pub. 30 Oct 2026: http://static.cninfo.com.cn/finalpage/2026-10-30/1225642947.PDF
- Credo 10-Q (qtr ended about 1 Aug 2026), business-combination pages, filed 2 Sep 2026: https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/R12.htm ; .../R37.htm ; .../R38.htm

**Secondary: earnings-call summaries and reviews**
- MarketBeat, Lumentum Q4 FY26 call, 11 Aug 2026: https://www.marketbeat.com/instant-alerts/lumentum-q4-earnings-call-highlights-2026-08-11/
- Finsee, Lumentum Q1 FY27 review, Nov 2026: https://finsee.ai/earnings/lite/2027/q1/en/
- Statementdog, Lumentum Q1 FY26 call, Nov 2025: https://statementdog.com/analysis/LITE/earnings_calls/301563
- MarketBeat, Fabrinet Q1 FY27 call, 2 Nov 2026: https://www.marketbeat.com/instant-alerts/transcript-fabrinet-q1-earnings-call-highlights-2026-11-02/
- MarketBeat, Tower Q3 2026 call, 2 Nov 2026: https://www.marketbeat.com/instant-alerts/transcript-tower-semiconductor-q3-earnings-call-highlights-2026-11-02/
- Futurum, Coherent Q1 FY27, 6 Nov 2026: https://futurumgroup.com/?p=97623
- Credence Research, Coherent $20B PhotonLink agreement, Nov 2026: https://www.credenceresearch.com/news/coherent-photonlink-20-billion-five-year-agreement-ai-data-center
- 24/7 Wall St, Coherent Q1 2027 (search summary): https://247wallst.com/cards/coherent-q1-2027-earnings-cohr-01m6m6c8nses8fzp5jba8fverb
- Verdict, NVIDIA invests in Lumentum and Coherent, 3 Mar 2026: https://www.verdict.co.uk/nvidia-invests-lumentum-coherent/
- Evertiq, NVIDIA to invest $2B in Lumentum, 4 Mar 2026: https://evertiq.com/design/2026-03-04-nvidia-to-invest-2-billion-in-lumentum-under-new-optics-partnership

**Secondary: Chinese-language press and brokerage**
- ifeng / Leiduo, Innolight Q3 2026 and HK IPO, 29 Oct 2026: https://finance.ifeng.com/c/8xcyvWhXO0b
- ithome, Innolight Q3 2026 (search summary only): https://www.ithome.com/1/019/718.htm
- Gelonghui (CITIC Securities review of Eoptolink Q3 2026), 2 Nov 2026: https://m.gelonghui.com/news/5342407
- Wallstreetcn, Eoptolink Q3 2026 (search summary only; fetch failed): https://wallstreetcn.com/articles/3784769
- C114, LightCounting 2025 top-10 suppliers, 28 May 2026 (search summary only): https://m.c114.com.cn/w5472-1311209.html

**Secondary: analysts and market trackers**
- Cignal AI 1Q26 datacom components, Jun 2026: https://cignal.ai/2026/06/datacom-optical-component-revenue-doubles-to-7-7-billion-in-1q26/
- Cignal AI 2025 datacom, Apr 2026: https://cignal.ai/2026/04/datacom-optical-component-revenue-surpasses-19b-in-2025/
- Cignal AI 2025 total optical components, Jan 2026: https://cignal.ai/2026/01/optical-component-revenue-reaches-nearly-25b-in-2025/
- Cignal AI OFC 2026 show report, Mar 2026: https://cignal.ai/2026/03/ofc-2026-show-report/
- Cignal AI 2Q26 Optical Component Report summary, 24 Sep 2026: https://cignal.ai/2026/09/2q26-optical-component-report/
- Cignal AI ECOC 2026 show report, 28 Sep 2026: https://cignal.ai/2026/09/ecoc-2026-show-report/
- Cignal AI datacom optical front-end forecast update, 15 Oct 2026: https://cignal.ai/2026/10/update-to-cignal-ais-datacom-optical-front-end-forecast/
- Cignal AI "Marvell Acquires Lumentum", 3 Nov 2026: https://cignal.ai/2026/11/marvell-acquires-lumentum/
- Cignal AI 3Q26 vendor reports (paywalled), 6 Nov 2026: https://cignal.ai/2026/11/3q26-vendor-reports-and-key-takeaways/
- Cignal AI latest-posts archive (accessed 12 Nov 2026): https://cignal.ai/category/latest/
- IEEE ComSoc TechBlog citing LightCounting Sep 2026 reports, 2 Oct 2026: https://techblog.comsoc.org/2026/10/02/light-counting-optical-transceiver-sales-surge-ieee-802-3-and-itu-t-optical-transport-standards-explained-uec-addendum/
- TrendForce, AI networking and interconnect market, 2 Nov 2026: https://www.trendforce.com/presscenter/news/20261102-13291.html
- TrendForce, Marvell-Lumentum, 3 Nov 2026: https://www.trendforce.com/presscenter/news/20261103-13294.html
- Photoncap, "Chinese Optical Modules Own 7 of the Top 10 Seats..." (undated, about late 2025; opinion-heavy): https://photoncap.net/p/chinese-optical-modules-own-7-of
- Faxiangongchang, China optical module 2026 (search summary only; 23.4% share claim): https://faxiangongchang.com/en/reports/china-optical-module-2026

### Inferences
- Treat the Innolight/Eoptolink figures as secondary until checked against the cninfo filings. They are consistent across ifeng, CITIC and ComSoc.
- The $20B Coherent and >$5B Lumentum commitments are company claims with unnamed customers.

### Gaps
- Not obtained: LightCounting, Cignal, Omdia, Dell'Oro and Yole full reports (paywalled); OFC/ECOC papers; OIF/IEEE 802.3 material; DIGITIMES/The Elec/Nikkei articles (search budget exhausted); cninfo, HKEXnews, MOPS, TDnet, EDINET and DART primary filings.

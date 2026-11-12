# Power delivery inside the AI rack (worldwide) — research notes as of 12 November 2026

Scope: power shelves and supplies, 800 VDC and +/-400 VDC architectures, sidecar power racks and solid-state transformers (SSTs) where they enter the rack row, busbars, battery-backup units (BBUs) and capacitor/supercapacitor units, conversion down to the chip (including vertical power delivery, VPD), and the power semiconductors and passives behind them. Quality only — no share prices, multiples or market capitalisation are used. Vertiv is covered for its power business only.

Method note: research ran on 12 November 2026. The shared web-search budget for this turn was exhausted part-way through (tool notice), and the coordinator then confirmed that the Exa and Firecrawl search tools were also out of credits. After that point only direct page fetches were used:
- pages already surfaced by earlier searches;
- SEC EDGAR filings (MPS FY2025 10-K, ADI 10-Q for the quarter to 1 Aug 2026, Eaton 10-Q for Q3 2026);
- stockanalysis.com financial-statement and statistics pages. These aggregate company filings (S&P Global data). They were used only for revenue, margins, cash flow, returns and net cash, never for valuation, and are labelled "stockanalysis, accessed 12 Nov 2026".

Coverage of FSP, Flex financials, Huawei Digital Power, Kehua, Japanese and Korean passives and power-semiconductor makers, India, and third-party market-share data (Dell'Oro, Omdia) is therefore thin. Section (7) lists these gaps. Labels: "company claim, unconfirmed" = no outside party confirms; "secondary" = trade press or analyst; "search summary" = seen only in a search-result summary, page not opened.

## (1) Segment map

### Takeaway
The in-rack power chain is split four ways. Taiwanese power-supply specialists (Delta far ahead, Lite-On second) hold the rack itself: power supplies, shelves, BBU shelves and the first 800 VDC power racks. US and European integrated electrical groups (Eaton, Schneider, Vertiv, ABB, Siemens) hold the AC "bridge" infrastructure, and they and venture start-ups (Heron, DG Matrix, Amperesand) race on SSTs. Power-semiconductor makers (Infineon, MPS, TI, ST, ADI and others) hold conversion down to the chip, where vertical delivery is the next step. Backup energy is led by Panasonic for cells and by Taiwanese module makers for BBUs. Coverage is thin for India (no player found), for Korean and Japanese passives and capacitors, and for Chinese HVDC suppliers other than Megmeet and Innoscience.

### Cited Findings
NVIDIA's own 800 VDC partner list (technical blog, 13 Oct 2025, primary) is the main published qualification list:
- **Silicon providers:** AOS, Analog Devices, Efficient Power Conversion (EPC), Infineon, Innoscience, MPS, Navitas, onsemi, Power Integrations, Renesas, Richtek, ROHM, STMicroelectronics, Texas Instruments.
- **Power system components:** BizLink, Delta, Flex, Lead Wealth, LITEON, Megmeet.
- **Data-centre power systems:** ABB, Eaton, GE Vernova, Heron Power, Hitachi Energy, Mitsubishi Electric, Schneider Electric, Siemens, Vertiv.

Source: [NVIDIA blog](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/). A May 2026 secondary summary of NVIDIA's partner web page lists the same 29 names ([BiotechClin, 30 May 2026](https://biotechclin.substack.com/p/nvidias-official-800v-dc-architecture)). OCP says more than 80 ecosystem partners are developing 800 VDC infrastructure ([Converge Digest, 12 Aug 2026](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)).

Tickers below are from general reference and were not re-checked against exchange filings in this pass.

**A. Rack power systems (PSUs, power shelves, BBU shelves, 800 VDC power racks)**

| Company | Home | Listing / ticker | Role | Why it matters / why left out (dated, sourced) |
|---|---|---|---|---|
| Delta Electronics | Taiwan | TWSE 2308; listed subsidiary Delta Electronics (Thailand), SET: DELTA | AI-server PSUs and power shelves, BBUs, 800 VDC in-row power rack, MVAC-to-800 VDC SST, busbars, DC-DC modules | **KEY.** Estimated ~70% share of Blackwell AI-server PSUs ([KGI, 1 Jul 2025](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf), analyst estimate). At GTC (Mar 2026) it showed a 660 kW 800 VDC in-row power rack with 480 kW of BBUs, plus an SST ([Power Electronics News, 19 Mar 2026](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). AI and data-centre products are ~50% of revenue (Q3 2026 call, [BigGo, 29 Oct 2026](https://finance.biggo.com/news/44f1e3fc-db83-4b4e-85f5-474840dae41b)). |
| Lite-On Technology | Taiwan | TWSE 2301 | PSUs (8.5 kW ASIC PSU), 110 kW Vera Rubin shelf, AMD Helios 42-inch shelf, BBUs, 800 VDC power rack, DC-DC bricks | **KEY.** Clear number two in PSUs. The 800 VDC rack is in final validation in Q4 2026 with shipments from Q1 2027 (company, [Fugle call memo, 30 Oct 2026](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)). NVIDIA names LITEON as co-designer of the GB300 power shelf ([NVIDIA blog](https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/), search summary). |
| AcBel Polytech | Taiwan | TWSE 6282 | Server PSUs | Left out of the key set. Not on NVIDIA's 800 VDC list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)). FY2025 revenue NT$31.7bn (+0.1%), gross margin 25.8%, operating margin 2.3%. Twelve months to Sep 2026: revenue NT$38.1bn (+24.2%), operating margin 2.8% ([stockanalysis, accessed 12 Nov 2026](https://stockanalysis.com/quote/tpe/6282/financials/)). Growing again but thin-margin; AI share not verified. |
| Chicony Power | Taiwan | TWSE 6412 | PSUs and adapters, server power | Left out. Not on NVIDIA's list. FY2025 revenue NT$34.5bn (−7.3%), gross margin 16.9%, operating margin 6.5%. Twelve months to Sep 2026: revenue NT$31.5bn (−13.7%), operating margin 3.2% ([stockanalysis](https://stockanalysis.com/quote/tpe/6412/financials/)). No sign of an AI-power ramp. |
| FSP Group | Taiwan | TWSE 3015 | PSUs | Named only by low-quality market-report sites; not verified. |
| Flex | US / Singapore | Nasdaq FLEX | Power shelves (33 kW for Blackwell, Aug 2025), embedded power | On NVIDIA's list. KGI calls it an "emerging supplier with vertical integration" ([KGI, Jul 2025](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf); [Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)). No 2026 financials collected. |
| Advanced Energy | US | Nasdaq AEIS | Data-centre power supplies (server and rack PSUs) | Not on NVIDIA's list, yet a real AI-power grower. Q3 2026 revenue $696.4m (+50.3% YoY), gross margin 41.8%, operating margin 20.7%. Data Center Computing revenue $256.2m vs $171.6m a year earlier (+49%) ([stockanalysis quarterly, accessed 12 Nov 2026](https://stockanalysis.com/stocks/aeis/financials/?p=quarterly)). Customers and 800 VDC plans not verified. |
| Megmeet | China | SZSE 002851 | PSUs; 33/110 kW shelves; 15 kW supercapacitor shelf; 16.5 kW BBU shelf; 800 V / 570 kW HVDC side rack | The only mainland-Chinese firm on NVIDIA's power-system-components list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)). H1 2026 power revenue was RMB1.841bn (+60.9%) ([ifeng, 1 Sep 2026](https://finance.ifeng.com/c/8w4hMGJVOYE)). It showed an 800 VDC "power centre" and SST architecture at OCP 2026 ([Ted Yu, 3 Nov 2026](https://ytyuted.substack.com/p/ep69-ocp-2026-ai)). Its claim to be the first Chinese firm certified for NVIDIA 800 V is a company/press claim, unconfirmed. Group FY2025 revenue RMB9.40bn (+15.1%), gross margin 21.7%, operating margin 1.5%. Twelve months to Sep 2026: revenue RMB11.65bn (+28.6%), operating margin 1.8% ([stockanalysis](https://stockanalysis.com/quote/she/002851/financials/)). AI volume has not yet lifted group margins. |
| Kehua Data | China | SZSE 002335 | UPS, HVDC | Brokers name it as a UPS-to-HVDC player ([Sohu, May 2026](https://m.sohu.com/a/1028510124_122014422), search summary). No 2026 numbers or customer evidence collected. |
| Huawei Digital Power | China | Private (Huawei unit) | DC power, UPS, HVDC | Not on NVIDIA's list. Nothing collected (search budget). |
| Ourmate (Oulutong) / China Greatwall | China | SZSE 300870 / SZSE 000066 | Server PSUs | Named as Megmeet's domestic rivals; Ourmate has Mexico and Vietnam bases ([ifeng, 1 Sep 2026](https://finance.ifeng.com/c/8w4hMGJVOYE)). |
| BizLink | Taiwan | TWSE 3665 | Power whips, busbars, cables | On NVIDIA's list. KGI calls it a qualified power-whip and busbar supplier for GPU and ASIC servers ([KGI, Jul 2025](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)). |
| Lead Wealth | Not verified | Not verified | Power system components | On NVIDIA's list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)); home country and role not verified. |

**B. Integrated electrical groups (rack-row and sidecar power, UPS, busway, SST)**

| Company | Home | Listing / ticker | Role | Why it matters / why left out |
|---|---|---|---|---|
| Eaton | Ireland (US-run) | NYSE ETN | UPS, switchgear, busway, PDUs; 800 VDC reference architecture (Oct 2025); SST via Resilient Power (bought Aug 2025); Boyd Thermal (bought 12 Mar 2026) | **KEY.** Its 15 kV / 2 MW medium-voltage SST passed UL testing, and it has 10 SST pilots ([Q3 call, 3 Nov 2026](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html); [8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)). |
| Schneider Electric | France | Euronext Paris SU | UPS, switchgear, busway, PDUs, prefab modules, liquid cooling (Motivair) | **KEY.** On NVIDIA's list. Direct data-centre exposure ~26%. No 800 VDC product timing given on the Q3 2026 call ([Investing.com transcript, 16 Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)). |
| Vertiv | US | NYSE VRT | UPS, power distribution, busway; 800 VDC portfolio | **KEY (power only).** The 800 VDC portfolio slipped from a planned H2 2026 release ([PR, 13 Oct 2025](https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html)) to validation now, revenue in 2027 and deployment in 2028 ([Q3 call summary, 28 Oct 2026](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)). |
| ABB | Switzerland | SIX ABBN | DC power systems, MV gear | On NVIDIA's list; reported SST programme ([PEN, Mar 2026](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). Investor in DG Matrix ([Data Center Richness, 16 Jun 2026](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)). Contributor to OCP's native-LVDC white paper ([Ted Yu](https://ytyuted.substack.com/p/ep69-ocp-2026-ai)). |
| Siemens | Germany | Xetra SIE | DC power systems, MV gear | On NVIDIA's list; reported SST programme ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). No financial evidence collected. |
| Hitachi Energy | Switzerland / Japan | Parent Hitachi, TSE 6501 | MV equipment, SST | On NVIDIA's list; reported SST programme ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). |
| GE Vernova | US | NYSE GEV | Grid and MV | On NVIDIA's list; mostly facility-level, so out of scope. |
| Mitsubishi Electric | Japan | TSE 6503 | DC power systems, SiC modules | On NVIDIA's data-centre power systems list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)); nothing further collected. |
| Legrand | France | Euronext Paris LR | PDUs, busway | Not on NVIDIA's 800 VDC list. Named with Vertiv and Amphenol as a winner if Kyber slips and Oberon racks last longer ([Tide Research via KuCoin, 6 Jul 2026](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge), secondary). |
| LS Electric / Fuji Electric | Korea / Japan | KRX 010120 / TSE 6504 | Switchgear, busway, UPS, power semis | On the starting list; not on NVIDIA's list. No evidence collected. |

**C. Solid-state transformer developers**

| Company | Home | Listing | Role | Why it matters |
|---|---|---|---|---|
| Heron Power | US | Private | MV SST ("Heron Link") | On NVIDIA's list. $140m Series B (18 Feb 2026); plans a 40 GW/yr US factory; field demos mid-2026, partner installs early 2027 (company) ([GlobeNewswire](https://www.globenewswire.com/news-release/2026/02/18/3240170/0/en/Heron-Power-Raises-140-Million-to-Build-a-Next-Generation-Power-Grid-in-Series-B-Co-led-by-Andreessen-Horowitz-Breakthrough-Energy-Ventures.html); [TechCrunch](https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/)). Its claim of 50 GW of orders is a company claim, unconfirmed. |
| DG Matrix | US | Private | Multiport SST | Joined the MGX ecosystem (GTC, Mar 2026). $60m Series A (Feb 2026), with ABB and Mitsubishi Heavy Industries participating. The CTO's claim that NVIDIA will use its SST as the 800 V reference is unconfirmed ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/); [Data Center Richness](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)). |
| Amperesand | Singapore | Private | SST | $80m Series A (Nov 2025; Walden Catalyst, Temasek). Targets 30 MW of commercial deployments in 2026 (company target) ([Data Center Richness](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)). |
| Resilient Power Systems | US | Eaton subsidiary since Aug 2025 | MV SST | See Eaton ([Eaton 8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)). |
| SolarEdge / Enphase | Israel / US | Nasdaq SEDG / ENPH | SST offerings for AI data centres | "Recently launched" SST offerings ([Data Center Richness, 16 Jun 2026](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)). Specs, customers and shipments not verified. |

**D. Power semiconductors and modules (chip-level conversion, 800 V devices)**

| Company | Home | Listing | Role | Why it matters |
|---|---|---|---|---|
| Infineon | Germany | Xetra IFX | Si, SiC and GaN switches; controllers; power stages; intermediate bus converters (IBCs); PSU reference designs (3.3–30 kW) | **KEY.** AI power-supply revenue ~€1.7bn in FY2026 (to Sep 2026) ([Investing.com, 10 Nov 2026](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)). |
| Monolithic Power Systems | US | Nasdaq MPWR | GPU/ASIC multiphase controllers, power stages and modules; 800 V GaN and SiC | **KEY.** Enterprise Data revenue $506.7m in Q3 2026, +164.6% ([8-K, 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm)). |
| Vicor | US | Nasdaq VICR | Factorised power modules; VPD; patents enforced through the ITC | Near-key. 68.3% gross margin and a large royalty stream ([Q3 2026 results](https://www.nasdaq.com/press-release/vicor-corporation-reports-results-third-quarter-ended-september-30-2026-2026-10-20)). |
| Texas Instruments | US | Nasdaq TXN | 800 V-to-6 V GaN IBC (97.6% peak), 30 kW AC-DC PSU, 800 V hot-swap | On NVIDIA's list; showed this at GTC 2026 ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/); [TI PR, 16 Mar 2026](https://www.ti.com/en-us/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia)). |
| Analog Devices | US | Nasdaq ADI | Power management; now owns Empower (IVR/VPD) | On NVIDIA's list. Announced the Empower deal on 19 May 2026 ([ADI PR](https://www.analog.com/en/newsroom/press-releases/2026/5-19-2026-adi-to-acquire-empower-semiconductor.html)) and completed it on 7 Jul 2026 for ~$1.5bn ([ADI 10-Q for the quarter to 1 Aug 2026, filed 19 Aug 2026](https://www.sec.gov/Archives/edgar/data/6281/000000628126000073/adi-20260801.htm), primary). |
| STMicroelectronics | Switzerland / France / Italy | Euronext Paris and NYSE STM | Reference designs: 800 V-to-6 V (20 kW, 96.5%) and 800 V-to-12 V (6 kW, 97.5%) | On NVIDIA's list ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). |
| onsemi / Power Integrations / AOS / Renesas / ROHM / Richtek (MediaTek unit) | US / US / US / Japan / Japan / Taiwan | ON / POWI / AOSL / TSE 6723 / TSE 6963 / private | SiC, GaN, MOSFETs, power stages, controllers | All on NVIDIA's silicon list; nothing further collected (search budget). |
| Navitas | US | Nasdaq NVTS | GaN and SiC | On NVIDIA's list. Q3 2026 revenue $14.0m. Has an 800 V reference design with Microchip ([GlobeNewswire, 3 Nov 2026](https://www.globenewswire.com/news-release/2026/11/03/3394777/0/en/navitas-semiconductor-announces-third-quarter-2026-financial-results.html), search summary). |
| Innoscience | China | HKEX 2577 | GaN | The only mainland-Chinese name on NVIDIA's silicon list. H1 2026 revenue RMB833.6m ([HKEX interim report, 18 Sep 2026](https://www.hkexnews.hk/listedco/listconews/sehk/2026/0918/2026091800446_c.pdf); [Chongdiantou](https://www.chongdiantou.com/archives/1788406187582.html)). |
| EPC | US | Private | GaN; 800 V-to-12.5 V converter (6 kW, >97%) | On NVIDIA's list ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). |
| Empower Semiconductor | US | Acquired by ADI on 7 Jul 2026 for ~$1.5bn ([ADI 10-Q](https://www.sec.gov/Archives/edgar/data/6281/000000628126000073/adi-20260801.htm)) | Integrated voltage regulators (IVR) and VPD (Crescendo); embedded silicon capacitors | Series D of more than $140m (22 Sep 2025); collaboration with Marvell (Jun 2025). At APEC 2026 it showed 16 regulators delivering ~1,000 A at 0.75 V ([Empower press page](https://www.empowersemi.com/category/press-release/); [APEC PR](https://www.globenewswire.com/news-release/2026/03/10/3252703/0/en/Empower-Semiconductor-Showcases-Vertical-Power-Delivery-Innovations-at-APEC-2026.html)). |
| Wolfspeed | US | NYSE (post-2025 restructuring; ticker not re-verified) | SiC | Not on NVIDIA's Oct 2025 list. Named as under pressure after the Kyber-delay report ([KuCoin](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge)). |
| Microchip | US | Nasdaq MCHP | SiC | Partner on Navitas's 800 V reference design ([Navitas Q3](https://www.globenewswire.com/news-release/2026/11/03/3394777/0/en/navitas-semiconductor-announces-third-quarter-2026-financial-results.html)). |

**E. Backup energy: BBU cells and modules, capacitor banks and supercapacitors**

| Company | Home | Listing | Role | Evidence |
|---|---|---|---|---|
| Panasonic Energy | Japan | Parent Panasonic Holdings, TSE 6752 | Li-ion cells and BBUs for data centres | Analyst piece: data-centre BBU sales forecast to rise 82% to ¥585bn in FY3/27 and 45% to ¥850bn in FY3/28 (forecast, not results). Japan cell capacity ~6 GWh by CY27 ([cnyes mirror, 26 Jul 2026](https://aeo.idaeo.ai/ai/news-cnyes-com/en/news/2026-07-26-data-center-power-revolution-with-major), secondary). Company target: ~¥1tn of data-centre storage revenue by FY2028 ([certi.news](https://certi.news/en/article/14090), search summary). |
| AES-KY / Simplo / STL | Taiwan | TWSE 6781 / TPEx 6121 / ticker not verified | BBU modules | BBU demand from AI servers kept rising in June 2026, lifting revenue; all three adding capacity ([Digitimes, 6–7 Jul 2026](https://www.digitimes.com/news/a20260706PD241/ai-server-battery-demand-revenue.html), paywalled lead only). |
| Dynapack | Taiwan | TPEx 3211 | BBU modules | Named with AES-KY as gaining from CSP second-sourcing (the article renders 3211 as "Sunlord") ([cnyes mirror](https://aeo.idaeo.ai/ai/news-cnyes-com/en/news/2026-07-26-data-center-power-revolution-with-major)). |
| Samsung SDI / LG Energy Solution | Korea | KRX 006400 / 373220 | Cells | Not verified this pass. |
| Musashi Energy Solutions | Japan | Subsidiary of Musashi Seimitsu, TSE 7220 | Lithium-ion capacitors (hybrid supercapacitors) | Competitor YMIN's marketing says Musashi's CCP3300SC (3.8 V, 3,000 F) is the GB300 reference (search summary, unconfirmed). Capacity and demand figures come only from blogs ([YMIN](https://www.ymin.cn/news/millisecond-level-transient-power-gaps-in-ai-server-rack-bbus-why-is-a-hybrid-supercapacitor-lic-bbu-more-suitable/); [Moljuurtei](https://www.moljuurtei.com/blog/en/musashi-seimitsu-hsc-ai-power-buffer)). |
| Skeleton Technologies | Estonia / Germany | Private | Supercapacitors ("GrapheneGPU") | Claims a 44% energy cut and 40% performance gain: company claim, unconfirmed ([PEN, 19 Nov 2025](https://www.powerelectronicsnews.com/impact-of-ai-systems-on-passive-components/)). |
| LS Materials / Nippon Chemi-Con | Korea / Japan | KOSDAQ 417200 / TSE 6997 | Ultracapacitors; aluminium electrolytic capacitors | Not verified this pass. Futurum says GB300 shelves use electrolytic capacitors, not supercapacitors ([Futurum](https://futurumgroup.com/insights/is-nvidias-gb300-nvl72-power-shelf-the-answer-to-ais-grid-strain/), search summary). |

**F. Passives and interconnect**

| Company | Home | Listing | Evidence |
|---|---|---|---|
| Samsung Electro-Mechanics | Korea | KRX 009150 | Mass-producing 220 µF (1206) and 330 µF (1210) MLCCs for AI servers ([PEN, 19 Nov 2025](https://www.powerelectronicsnews.com/impact-of-ai-systems-on-passive-components/)). |
| Murata / TDK / Kyocera AVX | Japan | TSE 6981 / 6762 / 6971 | 100 V, 1210-size MLCCs (1–10 µF) for 48 V racks ([PEN](https://www.powerelectronicsnews.com/impact-of-ai-systems-on-passive-components/)). |
| Yageo-KEMET / Taiwan's capacitor makers / Taiyo Yuden | Taiwan / Japan | TWSE 2327 / TSE 6976 | Not verified this pass. |
| Amphenol | US | NYSE APH | Its Surelock quick-connect is named as an example in the Mt. Diablo spec ([OCP spec](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf)). Named as a beneficiary of the Kyber slip ([KuCoin](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge)). |

**G. India:** no Indian company appears on NVIDIA's 800 VDC list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)) or in any source collected. Schneider reports strong growth in India and has added liquid-cooling capacity there ([Schneider Q3 call](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)). Coverage of India is thin. NSE and BSE filings were not searched because the search budget ran out.

### Inferences
- NVIDIA's 2025 list is weighted to Taiwan (Delta, Lite-On, BizLink, Richtek), the US and Europe. China has Megmeet and Innoscience; Japan has ROHM, Renesas and Mitsubishi Electric; Korea and India have none. Korean suppliers' exposure comes through components such as MLCCs and cells, not qualified rack systems.
- Three groups on the starting list are not on NVIDIA's list: AcBel, Chicony Power and Advanced Energy.
  - Being off the list does not mean being out of AI power: Advanced Energy's Data Center Computing revenue grew ~49% YoY in Q3 2026.
  - AcBel's thin margins (~2–3% operating) and Chicony Power's falling revenue and margins suggest neither is capturing much of the upswing (inference from filings-derived data).

### Gaps
- No third-party shares (Dell'Oro, Omdia, TrendForce full reports) for BBUs, vertical power modules, or controllers and power stages. The only PSU share figure is KGI's July 2025 estimate.
- Home country and role of "Lead Wealth" not verified.
- FSP, Flex, Huawei Digital Power, Kehua, LS Electric, Fuji Electric, LS Materials, Nippon Chemi-Con, Samsung SDI and Yageo: no 2026 evidence collected.
- AcBel, Chicony Power, Advanced Energy and Megmeet: filings-derived financials only, with no customer or 800 VDC evidence.

## (2) Evidence on tests (a)–(e) for the key companies

### Takeaway
Seven key companies were assessed: Delta, Lite-On, Monolithic Power Systems (MPS), Infineon, Eaton, Schneider and Vertiv (power only), with Vicor as near-key. None owns a "judge" outright. The gates are NVIDIA's MGX reference and partner lists, the hyperscalers' OCP specs, and UL certification, and all of them are owned by customers or third parties. Moats rest on physical constraints: manufacturing scale and qualification slots (Delta, Lite-On), fab and process capacity (Infineon), product-development know-how at the chip (MPS), medium-voltage equipment capacity plus UL-certified SSTs (Eaton), and ITC-enforced patents (Vicor). Revenue is overwhelmingly one-off hardware. The exceptions are Vicor's royalties (~34% of Q3 2026 revenue), services at the electrical groups, and capacity-reservation deals at Infineon. On financial strength (twelve months to Sep 2026, filings-derived):

| Company | Strengths | Weaknesses |
|---|---|---|
| MPS | 55.7% gross margin, ROIC ~33%, net cash | — |
| Delta | ROIC ~35%, net cash ~NT$98bn, free cash flow NT$66bn | Mid-teens operating margins |
| Eaton | 25.3% segment margin, $3.8bn free cash flow | ~$20bn net debt; ROIC ~11% after Boyd |
| Schneider | ROIC ~14%, €6.2bn free cash flow | — |
| Infineon | — | Weakest on returns (ROIC 7.2%), net debt |
| Lite-On | High ROIC (~30%) | Negative trailing free cash flow during its inventory and capex build |

### Cited Findings

#### Delta Electronics (Taiwan, TWSE 2308)
**(a) Position**

| Product | Class | Successor and timing | Source |
|---|---|---|---|
| 54 V AC-DC PSUs and power shelves (33 kW on GB200/GB300; six 33 kW shelves of six 5.5 kW PSUs per GB300 rack, or four 72 kW shelves on MGX) | BRIDGE | 800 VDC in-row power racks. NVIDIA's stated start is 2027 with Kyber. | [KGI, 1 Jul 2025](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf) |
| 660 kW 800 VDC in-row power rack with 480 kW of BBUs | SUCCESSOR | Shown at GTC (Mar 2026); shipping status not verified | [PEN, 19 Mar 2026](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/) |
| MVAC-to-800 VDC SST | SUCCESSOR | Shown at Computex 2025 and GTC 2026; MGX integration not confirmed | [KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf); [PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/) |

- **Constraint held:** scale manufacturing and qualification. It is on NVIDIA's power-system-components list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)), and its board approved a new Penang (Malaysia) site sized like its Thailand operations, to be finished within five years ([BigGo, 29 Oct 2026](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).

**(b) Lead**
- KGI estimated ~70% of AI-server PSUs on the Blackwell platform ([KGI, 1 Jul 2025](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf), analyst estimate).
- TrendForce (Mar 2026) says Delta's first-mover advantage and capacity keep its share dominant ([TrendForce bulletin](https://www.trendforce.com/research/download/RP260326MW), search summary of a paywalled report).
- Supply-chain estimates of PSU content per rack: GB200 US$35–40k, GB300 US$60–70k, VR200 more than US$150k (MGX designs) ([KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)).

**(c) Revenue model:** hardware sales. No recurring or service revenue was disclosed in the sources collected.

**(d) Financial strength**
- **Q3 2026** (board approval 28 Oct 2026):
  - Revenue NT$197.059bn, +31% YoY and +8% QoQ.
  - Net income NT$23.495bn; EPS NT$9.04 ([Delta release via Gulf Oil & Gas](https://www.gulfoilandgas.com/webpro1/main/mainnews.asp?id=1149042)).
  - Gross margin 34.1%, down 1.5 pp QoQ, after a ~NT$3.9bn inventory write-down (1.7% of revenue). Operating margin 16.6% ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
- **First nine months of 2026:** revenue NT$539.7bn (+37%); gross margin 35.5% (34.1% a year earlier); net profit NT$69.19bn (+62%) ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
  - Correction: BigGo says nine-month revenue was "above full-year 2025". FY2025 revenue was NT$554.9bn, so it is nine-month *net profit* that exceeds FY2025 net income of NT$60.1bn ([stockanalysis, accessed 12 Nov 2026](https://stockanalysis.com/quote/tpe/2308/financials/)).
- **FY2025:** revenue NT$554.9bn (+31.8%; FY2024 NT$421.1bn, +5.0%); gross margin 34.3%; operating margin 15.2% (FY2024 11.3%); net income NT$60.1bn ([stockanalysis](https://stockanalysis.com/quote/tpe/2308/financials/)).
- **Twelve months to Sep 2026** ([stockanalysis statistics](https://stockanalysis.com/quote/tpe/2308/statistics/), aggregated from filings):
  - Revenue NT$701.3bn.
  - Operating cash flow NT$128.3bn; capex NT$61.9bn; free cash flow NT$66.5bn (9.5% of revenue).
  - ROIC 34.9%; ROE 28.5%.
  - Cash NT$213.2bn against debt NT$115.1bn: net cash ~NT$98.1bn.
  - Employees: 85,684.
- **Segments, Q3 2026:**
  - Power & Components: NT$105.93bn (+40%), profit NT$19.92bn.
  - Infrastructure: NT$65.88bn (+25%), profit NT$12.07bn.
  - Automation: NT$15.9bn.
  - Mobility: NT$9.07bn, at a loss ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
- **AI exposure:** AI and data-centre ~50% of revenue; AI power ~25%; liquid cooling ~13% ([BigGo](https://finance.biggo.com/news/44f1e3fc-db83-4b4e-85f5-474840dae41b)).
- **Thai listed subsidiary, Q3 2026:** sales THB75.8bn (+42.4%), gross margin 27.3% ([Thailand Business News](https://www.thailand-business-news.com/business/336934-delta-thailand-q3-sales-surge-42-4-on-ai-demand-profit-misses-estimates), search summary).
- **Not collected:** customer concentration (largest customer, top five) and revenue by country.

**(e) Resilience**
- Q3 came in "a bit less than our original expectations" because of component mismatches and data-centre build delays (CFO). Raw materials are up ~2% this year; price increases take effect partly in Q4 and partly in Q1 2027 ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
- Management named the constraints as materials, grid power, electricians and local politics, and expects hyperscaler capex to exceed $1tn in 2027 (company view) ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
- Mexico was considered for new capacity but not chosen ([BigGo](https://finance.biggo.com/news/44f1e3fc-db83-4b4e-85f5-474840dae41b)).
- **Cross-border legal exposure:**
  - ITC case 337-TA-1370 (final determination 13 Feb 2025) imposed a limited exclusion order on all respondents and cease-and-desist orders on Delta Electronics (Americas) and Quanta Computer USA ([Vicor PR](https://www.vicorpower.com/press-room/itc-bars-importation-of-power-modules), search summary).
  - A new Section 337 investigation into "vertical power delivery systems" names Delta, Hon Hai, Quanta, Luxshare and Foxconn Industrial Internet among 20 respondents (complaint 9 Sep 2026). Delta says its products are not currently affected ([Taipei Times, 12 Oct 2026](https://www.taipeitimes.com/News/biz/archives/2026/10/12/2003865784)).

#### Lite-On Technology (Taiwan, TWSE 2301)
**(a) Position.** All items are company statements ([Fugle, 30 Oct 2026](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).

| Product | Class | Status |
|---|---|---|
| 8.5 kW ASIC PSU | BRIDGE | In mass production |
| BBU | BRIDGE | In mass production; revenue expected +30% in 2027 |
| Vera Rubin 110 kW shelf and AMD Helios 42-inch shelf | BRIDGE | Volume ramp in Q4 2026 |
| 800 VDC power rack | SUCCESSOR | Final validation Q4 2026; shipments from Q1 2027, depending on customer builds and grid power |
| DC-DC power brick | SUCCESSOR, chip side | Sampled to a CSP; revenue from Q3 2027 |

- NVIDIA says it worked with LITEON on the GB300 shelf's energy-storage power smoothing, which cuts grid-facing peak power by up to 30% ([NVIDIA blog](https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/), search summary).

**(b) Lead:** on NVIDIA's list. KGI says Lite-On "claims to be a major supplier" to a US CSP with an aggressive ASIC timeline ([KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)). No reliable share figure found; market-report sites give 14–17%, low quality.

**(c) Revenue model:** hardware. It signs three-year supply contracts for long-lead components (supply side, not customer prepayments) ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).

**(d) Financial strength**
- **Q3 2026:**
  - Revenue NT$57.4bn (+28% YoY, +9% QoQ); gross margin 25.9%; operating margin 15.1%.
  - Net income NT$7.4bn (+60%); EPS NT$3.27.
- **First nine months of 2026:** revenue NT$153.5bn (+26%); gross margin 25.2%; operating margin 13.7%.
- **Cloud & IoT segment:** NT$33.8bn (+57%, 59% of revenue).
- **AI share:** above 30% of 2026 revenue, and 40–50% possible in 2027.
- **Return on invested capital:** 34% (company figure).
- **Capex:** 2026 raised to NT$19.7bn from NT$18bn (NT$13.1bn spent in the first nine months), and higher again in 2027.
- **Inventory:** +NT$11bn QoQ, described as strategic.
- **Financing:** NT$36bn sustainability-linked syndicated loan (Oct 2026).
- Sources: [Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30); [cnyes](https://news.cnyes.com/news/id/6641958); [CNA](https://www.cna.com.tw/news/afe/202610300203.aspx).
- **FY2025:** revenue NT$166.1bn (+21.1%, after −14.5% in 2023 and −7.6% in 2024); gross margin 22.9%; operating margin 10.1%; net income NT$15.1bn ([stockanalysis, accessed 12 Nov 2026](https://stockanalysis.com/quote/tpe/2301/financials/)).
- **Twelve months to Sep 2026** ([stockanalysis statistics](https://stockanalysis.com/quote/tpe/2301/statistics/)):
  - Operating cash flow NT$7.3bn; capex NT$15.1bn; free cash flow **−NT$7.8bn**, reflecting the inventory build and capex.
  - ROIC ~30.0%, against the company's 34%.
  - Net cash ~NT$26.2bn (cash NT$74.4bn, debt NT$48.2bn).
- **Not collected:** customer concentration.

**(e) Resilience**
- New capacity: a Vietnam plant (Quang Ninh, opening Nov 2026), Kaohsiung phase 2 (Dec 2026) and McKinney, Texas (Q2 2027). Overseas capacity doubles, which management says covers 3–5 years of demand.
- US grid-power shortages hurt Q1 2026 pulls.
- Management expects AI server power to grow ~70% in 2027 (company view) ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).

#### Monolithic Power Systems (US, Nasdaq MPWR)
**(a) Position**

| Product | Class | Successor and timing |
|---|---|---|
| Lateral multiphase controllers, power stages and modules for GPU and ASIC core rails | BRIDGE | Vertical delivery. CEO: "you run out of peripheral, you have to do vertical." No date given. |
| 800 V GaN (sampling began Q3 2026) and SiC designs | SUCCESSOR | Revenue "probably end of the '27 and 2028". CFO: "we've always kind of been late in '27". |

- Customers choose between GaN and SiC. The CEO says a GaN product needs about 50 million units shipped before it is proven.
- The constraint MPS holds is speed of product development (more than 6,000 products) within a fabless model. Capacity supports more than $6bn of annual revenue, with a path to $8bn by H2 2027 (company).
- Process know-how: its 10-K says that, unlike most fabless firms that use foundry-standard processes, MPS has "developed our own proprietary process and packaging technologies". Its largest test facilities are in Chengdu, China ([FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1280452/000143774926006113/mpwr20251231_10k.htm)).
- Sources: [Q3 call, 30 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/); [8-K](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm).

**(b) Lead:** reported Enterprise Data revenue rose 164.6% YoY. The CFO says "most of the industry has already moved to modules" ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)). No third-party share data for GPU controllers or power stages was found.

**(c) Revenue model:** chips and modules, one-off. No recurring element.

**(d) Financial strength.** All from the 8-K of 29 Oct 2026 ([8-K](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm)).
- **Q3 2026 revenue:** $1,202.4m (+63.1% YoY, +22.6% QoQ). By end market:
  - Enterprise Data $506.7m (42.1%).
  - Storage & Computing $192.2m.
  - Communications $187.4m (+134.7%).
  - Automotive $180.7m.
  - Industrial $71.4m.
  - Consumer $64.0m.
- **Margins:** gross margin 55.4% GAAP and 55.7% non-GAAP; operating margin 29.7% GAAP and 38.6% non-GAAP.
- **Profit:** GAAP net income $271.1m.
- **Cash flow and balance sheet:**
  - Operating cash flow $289.9m.
  - Cash plus short-term investments $1,091.2m, after a $453.4m buyback in Q3; no debt line.
  - Net property and equipment up from $627.7m (Dec 2025) to $821.6m.
  - Inventory $764.9m (130 days).
- **First nine months of 2026:** revenue $2,987.2m (+46%); non-GAAP operating margin 37.5%.
- **Q4 2026 guidance:** revenue $1,315–1,385m.
- **Enterprise Data outlook:** the CFO is "comfortable with a floor of 150%" YoY growth ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)).
- **FY2025 10-K** (filed 27 Feb 2026, primary) ([10-K](https://www.sec.gov/Archives/edgar/data/1280452/000143774926006113/mpwr20251231_10k.htm)):
  - Revenue $2,790.5m (+26.4% from $2,207.1m).
  - Channel concentration: 85% of sales go through distribution. The top three customers, all distributors, took 54% of revenue: 26%, 18% and 10% (61% in 2024 and 55% in 2023). Distributor A held 35% of receivables. End-customer concentration (for example NVIDIA or a hyperscaler) is not disclosed.
  - Revenue by region, FY2025, as reported (likely ship-to):

    | Region | Revenue | Share |
    |---|---|---|
    | China | $1,544.3m | 55% |
    | Taiwan | $550.1m | 20% |
    | South Korea | $252.7m | 9% |
    | Southeast Asia | $148.1m | 5% |
    | Europe | $113.5m | 4% |
    | US | $96.7m | 3.5% |
    | Japan | $84.4m | 3% |

  - 92% of revenue comes from customers in Asia.
- **Twelve months to Sep 2026** ([stockanalysis statistics, accessed 12 Nov 2026](https://stockanalysis.com/stocks/mpwr/statistics/)): free cash flow $609m (16.3% of revenue) after $264m of capex; ROIC 33.3%; net cash ~$1.07bn.

**(e) Resilience**
- End markets are diversified (Automotive 15%, Communications 16%).
- Balance sheet: net cash.
- China footprint: the CEO describes a 1 million sq ft building in China used to test 800 V supplies ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)). Export-control exposure not verified.

#### Infineon Technologies (Germany, Xetra IFX)
**(a) Position**
- **BRIDGE:** silicon MOSFETs, power stages and controllers for 54 V and 12 V rails.
- **SUCCESSOR:**
  - 800 V SiC and GaN PSU stages and 800 V IBCs. The 800 V-to-12 V IBC handles 6–10.8 kW at 98.2% peak efficiency ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). CoolGaN 800 V-to-50 V and 800 V-to-12 V reference designs came in Mar 2026, and Infineon joined NVIDIA's MGX ecosystem in May 2026 ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)).
  - 300 mm GaN power wafers, with commercial production from 2027 ([Investing.com, 10 Nov 2026](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)).
- **Physical constraint:** fab capacity. Infineon reports demand for data-centre power exceeding capacity ([TrendForce, 27 Aug 2026](https://www.trendforce.com/research/download/RP260827TB)).

**(b) Lead**
- FY2026 AI power revenue ~€1.7bn, more than double the prior year, and about 40% of the Power Systems segment ([Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)).
- It beat a target of more than €1.6bn set in Aug 2026 ([Power Semiconductors Weekly, 10 Nov 2026](https://www.powersemiconductorsweekly.com/2026/11/10/infineon-reports-12-revenue-growth-to-e16-35-billion-in-fy2026-forecasts-e20-billion-for-fy2027-on-strong-ai-data-center-demand/); search summary for the target).
- AI power content is $100–250/kW, averaging $175/kW (company) ([Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)).
- No third-party share data for AI power was found.

**(c) Revenue model:** chips. Multi-year capacity reservation agreements exceeding €10bn were cited (search summary of results coverage; not verified on a primary page). Those would act like prepaid or committed supply.

**(d) Financial strength**
- **FY2026 (to 30 Sep 2026; published 10 Nov 2026):**
  - Revenue €16.353bn (+12%; +15% at constant FX).
  - Segment result €3.223bn, a 19.7% margin.
  - Free cash flow €993m reported, €1.925bn adjusted.
  - ROCE 7.2% (FY25: 4.9%).
- **Q4 FY2026:** revenue €4.706bn; segment result margin 23.8%; adjusted gross margin 45.1%.
- **Segments, FY2026:**
  - Automotive €7.77bn (20.0% margin).
  - Power Systems €5.43bn (+31%; 23.5% margin vs 15.1%).
  - Edge Systems €3.15bn (12.5% margin).
- **FY2027 outlook:**
  - Revenue ~€20bn.
  - Data-centre power revenue approaching €4bn (~20% of revenue).
  - Capex €3.0–3.5bn; adjusted free cash flow ~€2.2bn.
  - Segment result margin in the mid-20s %.
- **Manufacturing:** 13 fab sites; outsourcing share heading to 50% by FY27.
- Sources: [Power Semiconductors Weekly](https://www.powersemiconductorsweekly.com/2026/11/10/infineon-reports-12-revenue-growth-to-e16-35-billion-in-fy2026-forecasts-e20-billion-for-fy2027-on-strong-ai-data-center-demand/); [Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954).
- **FY2026 on stockanalysis's definitions** (IFRS, unadjusted; [stockanalysis statistics, accessed 12 Nov 2026](https://stockanalysis.com/quote/etr/IFX/statistics/)):
  - Gross margin 40.4% (IFRS reported; Infineon's adjusted gross margin is higher); operating margin 13.5%.
  - Operating cash flow €4.16bn; capex €2.18bn; free cash flow €1.98bn.
  - ROIC 7.2%.
  - Cash €2.14bn against debt €7.33bn: net debt ~€5.2bn. This may exclude Infineon's short-term financial investments, which its own "gross cash" includes; not verified.
- **Not collected:** regional split.

**(e) Resilience:** automotive is still 48% of revenue, which diversifies away from AI but adds its own cycle. Returns on capital are low after the FY24–25 downturn (ROCE 7.2%). Capex rises to €3.0–3.5bn ([Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)). Exposure to gallium export controls was not verified.

#### Eaton (Ireland / US, NYSE ETN)
**(a) Position**
- **BRIDGE:** AC UPS, switchgear, busway and PDUs.
- **SUCCESSOR:**
  - 800 VDC reference architecture (Oct 2025) ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)). No product shipping date was given on the Q3 2026 call.
  - Medium-voltage SST from Resilient Power, bought 6 Aug 2025 for $86m: $55m cash plus ~$31m contingent on 2025–28 revenue and technology milestones ([Eaton 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm), primary). The small price means Eaton bought an early-stage technology, not a revenue stream. The 15 kV / 2 MW unit passed UL testing; there are 10 SST pilots, and Eaton expects "multiple 15-kilovolt projects to ship during the year" (company) ([Q3 call, 3 Nov 2026](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).
  - "Beam Rubin DSX" platform co-designed with NVIDIA (GTC 2026) ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)).
- **Physical constraint:** medium-voltage equipment capacity. 18 of 25 expansion projects are complete, and a larger three-phase transformer plant is due in H1 2027 ([call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).

**(b) Lead**
- The UL test is third-party evidence.
- Electrical Americas data-centre sales rose 54% in Q3 2026 ([call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).
- Electrical-sector data-centre orders more than doubled on a rolling 12-month basis (search summary of Zacks/Yahoo). No third-party share data was found.

**(c) Revenue model:** mainly hardware against a large backlog. Total electrical backlog is above $20bn (+46% YoY) ([call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)). Services were not quantified.

**(d) Financial strength**
- **FY2025 (8-K, 26 Feb 2026):**
  - Sales $27.4bn (+10%; organic +8%); segment margin 24.5%.
  - Operating cash flow $4.5bn; capex $919m; free cash flow $3.6bn ([8-K](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000002/etn12312025exhibit99.htm)).
- **Q3 2026 (8-K, 3 Nov 2026):** sales $8,947m (+28%; organic +19%; acquisitions +8%); segment margin 25.3%.

  | Segment | Sales | Growth | Margin | Backlog |
  |---|---|---|---|---|
  | Electrical Americas | $4,172m | +22% organic | 29.8% | +33% |
  | Electrical Global | $2,727m | +58% (Boyd adds 31 pts) | 21.1% | +121% |

  - Q3 cash flow: operating $1,310m; capex $275m; free cash flow $1,034m.
  - FY2026 guidance: organic growth 13–15%; segment margin 24.1–24.5%.
  - Balance sheet at 30 Sep 2026: total debt $20,106m against cash plus short-term investments of $818m. That is ~$19.3bn of net debt (my calculation, after the $9.55bn Boyd purchase on 12 Mar 2026).
  - Source: [8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm).
- **Twelve months to Sep 2026** ([stockanalysis statistics, accessed 12 Nov 2026](https://stockanalysis.com/stocks/etn/statistics/)): revenue $31.98bn; operating cash flow $4.91bn; capex $1.11bn; free cash flow $3.80bn; ROIC 11.0% (diluted by Boyd and Fibrebond goodwill); net debt ~$20.1bn.
- **Not collected:** data-centre share of group sales (the Q3 10-Q gives none), customer concentration and geography.

**(e) Resilience**
- Electrical book-to-bill is 1.2 on a rolling 12-month basis ([8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)).
- Management expects none of its end markets to decline in 2027, and price minus cost was positive ([call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).

#### Schneider Electric (France, Euronext Paris SU)
**(a) Position**
- **BRIDGE:** AC UPS, switchgear, busway, PDUs and prefab modules.
- **SUCCESSOR:** 800 VDC. It is on NVIDIA's list ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)) and showed "solutions for megawatt-scale data centers" at GTC 2026 ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)).
- On the Q3 2026 call, the CFO said only that its design-partner role with hyperscalers and colocation operators gives visibility into the 800 V shift. No product timing was given ([transcript, 16 Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).

**(b) Lead:** triple-digit growth in data-centre demand in Q3, the third such quarter of the last four, with "visibility into 2027 and 2028" ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)). No third-party share data was found.

**(c) Revenue model:** not quantified in this pass. Pricing actions were raised in January and again in April 2026 ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).

**(d) Financial strength**
- **Q3 2026:** revenue €11.46bn (+16.9% organic). Energy Management €9.6bn (+19% organic); Industrial Automation €1.8bn (+8%) ([Reuters via MarketScreener, 16 Oct 2026](https://www.marketscreener.com/news/schneider-electric-raises-2026-targets-again-on-booming-data-centre-demand-ce785cdad98cf322)).
- **FY2026 guidance:** organic growth 12–14%; adjusted EBITA margin about 19.7–19.9% ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).
- **Data-centre exposure:** data centres and networks were ~30% of exposure at end-2025, with direct data centres ~26% ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).
- **Twelve months to Sep 2026** ([stockanalysis statistics, accessed 12 Nov 2026](https://stockanalysis.com/quote/epa/SU/statistics/), derived from filings):
  - Revenue €42.0bn; operating margin 17.9%.
  - Operating cash flow €7.24bn; capex €1.05bn; free cash flow €6.19bn (14.7% of revenue).
  - ROIC 14.0%; net debt ~€16.3bn.
- **Not collected:** FY2025 annual report.

**(e) Resilience**
- Q3 organic growth by region: North America +20%, China & East Asia +26% (the same call also says 32%, which conflicts), Europe +9%.
- Pricing is expected to offset raw-material inflation and net tariffs in 2026.
- Liquid-cooling capacity was added in India, Italy and China ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).

#### Vertiv (US, NYSE VRT): power business only
**(a) Position**
- **BRIDGE:** UPS, switchgear and busway, rack PDUs.
- **SUCCESSOR:** an 800 VDC portfolio of centralised rectifiers, high-efficiency DC busways, rack-level DC-DC converters and energy storage.
  - Planned (13 Oct 2025): release in H2 2026 for the 2027 Rubin Ultra rollout ([PR](https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html)).
  - Now (Q3 call, 28 Oct 2026): "in validation", with revenue during 2027 and market deployment in 2028 ([Yahoo summary](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)). That is a slip of roughly 12–18 months on deployment.
- KGI says Vertiv, like Delta and Lite-On, showed an HVDC power rack for 0.8–1 MW at Computex 2025 ([KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)).

**(b) Lead:** on NVIDIA's list; a contributor to OCP's native-LVDC white paper ([Ted Yu](https://ytyuted.substack.com/p/ep69-ocp-2026-ai)). No power-specific share data was found.

**(c) Revenue model:** services and spares were $0.68–0.72bn of Q3 2026 group sales (~16%). The release gives two inconsistent figures, and the split is group-level, not power-only ([8-K](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026067707/q32026exhibit991vrt10282026.htm)).

**(d) Financial strength:** Vertiv discloses no power-versus-thermal split ([8-K](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026067707/q32026exhibit991vrt10282026.htm)). Group financials are covered in the cooling notes.

**(e) Resilience:** the reported Kyber slip is framed as positive for Vertiv, because older Oberon racks on today's AC-to-54 V infrastructure stay in service longer ([KuCoin/Tide, 6 Jul 2026](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge), secondary).

#### Near-key: Vicor (US, Nasdaq VICR)
- **(a) Position:**
  - VPD modules are SUCCESSOR products. The 2nd-generation VPD is in demo with OEMs and hyperscalers. Vicor claims 3x the current density of VRs and 10–15% less processor power loss (company claim, unconfirmed).
  - Bricks and NBMs are BRIDGE products.
  - The moat is a legal gate: ITC-enforced patents.
  - Source: [Q3 call](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190).
- **(b) Lead:** third-party adjudication. The ITC's final determination of 13 Feb 2025 found Vicor's patents valid and infringed ([Vicor](https://www.vicorpower.com/press-room/itc-bars-importation-of-power-modules), search summary). Vicor granted its first pure VPD licence to an unnamed "leading AI OEM" (company). No hyperscaler licence is confirmed.
- **(c) Revenue model:** Q3 2026 royalties were $66.6m of $197.1m revenue (~34%). The Q4 royalty floor is $43m, and the CFO now describes royalties as recurring. Legal costs run at ~20% of royalties ([call](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190)).
- **(d) Financial strength (Q3 2026):** revenue $197.1m (+78.5%); gross margin 68.3%; net income $63.3m; cash $513.1m; backlog $406m (+166%) ([results](https://www.nasdaq.com/press-release/vicor-corporation-reports-results-third-quarter-ended-september-30-2026-2026-10-20), search summary). Twelve months to Sep 2026: revenue $560.7m; gross margin 60.6%; operating margin 26.1%; ROIC 37.1%; free cash flow $50.8m after $45.2m of capex; net cash ~$506m ([stockanalysis, accessed 12 Nov 2026](https://stockanalysis.com/stocks/vicr/statistics/)).
- **(e) Resilience:**
  - Vicor says many customers are single-source with it. Fab 2 equipment starts in Q2 2027 ([call](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190)).
  - The new ITC case is typically 12–16 months ([Taipei Times](https://www.taipeitimes.com/News/biz/archives/2026/10/12/2003865784)).
  - An appeal on licence defences is at the Federal Circuit ([Fed Circuit Blog, 28 Oct 2026](https://fedcircuitblog.com/2026/10/28/argument-preview-vicor-corp-v-international-trade-commission/), search summary).

### Inferences
Each company's exposure under the three AI-spending scenarios to 2030 (inference):

| Company | Steady growth (~55%) | Financing-led pause around 2028 (~25%) | Faster acceleration (~20%) |
|---|---|---|---|
| Delta | Best placed of the rack makers: content per rack rises from ~$35k (GB200) to more than $150k (VR200) (KGI) | Most exposed, with ~50% of revenue AI-linked, hardware-only sales, inventory already building in Q3 2026, and no recurring revenue; net cash of ~NT$98bn cushions the balance sheet | Capacity and component supply bind first |
| Lite-On | Same pattern as Delta | Similar to Delta, with smaller scale and lower gross margin (~26% vs ~34–35%), but AI is only ~30% of revenue; negative trailing free cash flow is a weakness going into a pause | Same capacity limits |
| MPS | Grows fastest: content per GPU rises and VPD adds content | Net cash and a fabless model (no fab underutilisation) cushion it | Extra growth capped by foundry capacity (company says capacity supports >$6bn) |
| Infineon | Gains from AI power | Automotive (48%) and industrial cycles dominate the outcome | Gains from AI power |
| Eaton | Well placed | A >$20bn electrical backlog and book-to-bill of 1.2 cushion a pause, but ~$19bn of net debt is higher than before Boyd | Constrained by medium-voltage equipment capacity |
| Schneider | Same pattern as Eaton | Cushioned by backlog | Same capacity limits as Eaton |
| Vertiv (power) | The UPS bridge business does well while Oberon racks persist | Cushioned by backlog | Its UPS business is the one most threatened once native 800 VDC removes UPSs |

- **Cycle position (all names):** orders are at records (Eaton, Vertiv, Schneider), suppliers are building inventory (Delta, Lite-On, MPS at 130 days), and capex is rising (Lite-On, Infineon, Vicor). That is a mid-to-late upcycle with pricing power (Schneider, Delta raising prices).

### Gaps
- Delta: customer concentration (whether NVIDIA or any single CSP exceeds 10%) and revenue by country. MOPS filings and Delta's IR page could not be read (the IR URL returned 404).
- MPS: end-customer concentration. The 10-K discloses distributor concentration only.
- Infineon: regional split. Its "capacity reservation >€10bn" was not verified on a primary page; the press-release page is script-rendered and unreadable by the fetch tool.
- Schneider: FY2025 annual report (only trailing aggregates collected).
- Eaton: data-centre share of group sales.
- Vertiv: no power-only disclosure exists.
- Largest-customer and top-five shares are available only for MPS, and only at distributor level (top three = 54%).

## (3) Path forward: what each company must get through, said vs done, and suggested verdicts

### Takeaway
The test for this segment is transition 6: today's 54 V AC-fed racks to 600 kW and 1 MW racks on 800 VDC (or +/-400 VDC). Inside it sit two sub-transitions: lateral to vertical delivery at the chip, and silicon to GaN and SiC in the high-voltage stages. By November 2026, the bridge (54 V shelves, BBUs, energy-storage smoothing) ships in volume. Successors (800 VDC power racks, SSTs, 800 V-to-6/12 V converters, VPD) are at demo, sampling, validation or pilot stage, with first revenue now guided to 2027 and deployment to 2028. The architecture is also forking. Google, Meta and Microsoft finalised the +/-400 VDC Mt. Diablo 1.0 spec (8 Oct 2026). NVIDIA leads a two-wire native 800 V path, which SemiAnalysis reports has slipped to after 2028.

### Cited Findings
**Architecture timeline: specified versus shipped**
- **NVIDIA, May 2025:** announced an 800 VDC architecture "for 1 MW IT racks and beyond, beginning in 2027" ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/), secondary summary of the May 2025 announcement).
- **NVIDIA, 13 Oct 2025:** the blog names the partners listed in section 1. It says the transition "will occur in phases" and gives figures:
  - Hopper to Blackwell raised per-GPU TDP by 75% and rack density by 3.4x.
  - 800 VDC carries 157% more power than 415 VAC at the same wire gauge.
  - Kyber's single-stage 64:1 LLC converter is 26% smaller than multi-stage alternatives.
  - The blog does not restate 2027 and names no shipping products ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)).
  - Separately, NVIDIA says full-scale 800 VDC production coincides with Kyber in 2027 ([GPU Smith, 23 Jul 2026](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained), secondary).
- **NVIDIA, GTC Mar 2026 and Computex Jun 2026:** NVIDIA reaffirmed H2 2027 for Rubin Ultra and Kyber ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained), secondary). Partner reference designs moved from 800 V-to-50 V in 2025 to 800 V-to-12 V and 800 V-to-6 V ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)).
- **The Kyber rack redesign:** the GTC 2026 Kyber has 36 compute sleds against 72 in the 2025 prototype. One HPC analyst said it "appeared to have lost half its GPU density." A ~300 kW figure is unconfirmed ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained)).
- **Delay reports:**
  - Jefferies (22 Jun 2026): the Kyber backplane is "highly likely to be delayed until 2028."
  - SemiAnalysis (10 Jun 2026): native 800 VDC delayed until after 2028.
  - SemiAnalysis (6 Jul 2026): Kyber NVL144 delayed more than 12 months to 2028; NVL72x2 cancelled; Rubin Ultra likely to revert to the Oberon NVL72 form factor ([KuCoin/Tide](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge), secondary).
  - NVIDIA: "Our roadmap is intact" ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained); [Barchart/Yahoo, 8 Jul 2026](https://finance.yahoo.com/technology/ai/articles/nvidia-allegedly-delaying-kyber-rack-155030298.html)).
- **Vera Rubin NVL72:** in full production since June 2026, with shipments to eight cloud partners from autumn 2026 (CNBC via [GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained), secondary). Lite-On's 110 kW Vera Rubin shelf ramps in Q4 2026 ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)). Vera Rubin therefore still uses in-rack shelves (inference from these two).
- **OCP and the hyperscalers:**
  - The Mt. Diablo Disaggregated Power Rack Specification 1.0.0, by Microsoft, Meta and Google, took effect on 8 Oct 2026 and is marked "Final release". History: v0.5.0 on 5 May 2025; v0.5.2 released to OCP in May 2025; v0.7 in Feb 2026; v0.7.0 in Mar 2026 ([OCP spec PDF](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf)).
  - Its content: a sidecar power rack from 800 kW to 1 MW+. Average DC load is 800 kW–1.1 MW at 480 VAC, up to 1.1 MW at 415 VAC, and up to 718 kW at 400 VAC. Output is +/-400 VDC (410 V at no load) or "differential 800 Vdc". Peak loading is 175% of TDP for under 2 ms, 180% for under 0.5 ms and 150% for under 50 ms. The BBU option gives 45–90 s of hold-up at 100% load, and there is a capacitor-bank (CBU) option (same source).
  - Mt. Diablo 2.0 (native 800 V) is planned with no date. The SST spec is at v0.3 ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)).
  - At OCP 2026 (Oct 2026), the native-LVDC white paper reached v1.1.0 with 39 contributors including ABB and Vertiv. A board-level power workstream on direct 800 VDC or 48 VDC to the board formed in Q4 2026. NVIDIA leads the two-wire 800 V path; Google, Meta and Microsoft lead the three-wire +/-400 V path. SSTs are described as still in hyperscaler validation and early pilots ([Ted Yu, 3 Nov 2026](https://ytyuted.substack.com/p/ep69-ocp-2026-ai), secondary).
  - Microsoft (13 Oct 2026) contributed Mt. Diablo v0.7 and v1.0 (~100 kW to more than 1 MW) and is "advancing solid-state transformer-based architectures" for 800 VDC. It gives no deployment status ([Azure blog](https://azure.microsoft.com/en-us/blog/infrastructure-for-the-frontier-era-scaling-intelligence-through-open-industry-collaboration/)).
  - The first 800 VDC AI factory, built by Visionbay, is under construction and claims ~45% less copper (NVIDIA's Ian Buck at OCP 2026) ([TechArena, 15 Oct 2026](https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat)).
  - Google, Meta, Microsoft and NVIDIA published an OCP grid-resilience spec ([TechArena](https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat)).
- **Camps:** TrendForce (Mar 2026) splits HVDC into an OCP +/-400 V camp and an NVIDIA/AWS 800 V camp ([TrendForce](https://www.trendforce.com/research/download/RP260326MW), search summary).
- **AMD:** Lite-On's Helios 42-inch power shelf ramps in Q4 2026 ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)). AMD's own 800 VDC or +/-400 VDC plan was not found.
- **Chinese hyperscalers:** not found. Innoscience claims more than 100 800 V HVDC chip products designed in at more than 20 leading CSPs, some in mass production (company claim, unconfirmed). CMBI's view is that NVIDIA's delay affects only native single-ended 800 VDC, while hyperscaler ASIC-side +/-400 VDC proceeds on schedule ([Xueqiu summary of broker notes](https://xueqiu.com/9282597341/397179025), search summary).
- **Supply-chain timing statements (company):**
  - Lite-On: 800 VDC rack shipments from Q1 2027 ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).
  - Vertiv: validation now, revenue 2027, deployment 2028 ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)).
  - MPS: 800 V revenue at the end of 2027 and in 2028 ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)).
  - HVDC-compatible BBUs: certification in H1 2027, shipments in H2 2027, significant revenue in 2028 ([cnyes mirror](https://aeo.idaeo.ai/ai/news-cnyes-com/en/news/2026-07-26-data-center-power-revolution-with-major), analyst).
  - Heron: partner installs in early 2027 ([TechCrunch](https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/)).
  - Eaton: SST pilots, with 15 kV projects shipping in 2026 ([call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).
  - Megmeet: one broker said an 800 V power rack would sample in mid-2026 and that large-scale production in 2026 was unlikely ([Sohu](https://www.sohu.com/a/1080573199_122121789), search summary).

**Said vs done, per key company**
- **Delta.**
  - *Said:* grid-to-chip 800 VDC, including power racks, BBUs and an SST ([KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)).
  - *Done:* showed the 660 kW rack, 480 kW of BBUs and an SST at GTC 2026 ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)). It is on NVIDIA's list, and its board approved the Penang capacity ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
  - Shipments of 800 VDC racks not verified.
- **Lite-On.**
  - *Said:* 800 VDC rack shipments from Q1 2027; power-brick revenue from Q3 2027.
  - *Done:* 800 VDC rack in final validation; 8.5 kW PSU and BBU in mass production; capex raised to NT$19.7bn; acquired Epic (DC-DC) and took a strategic stake in a high-power transformer and inductor maker ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).
- **MPS.**
  - *Said:* vertical delivery is inevitable; 800 V revenue at the end of 2027 and in 2028.
  - *Done:* sampling 800 V GaN; SiC designs; modules shipping at scale (Enterprise Data $506.7m in Q3) ([8-K](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm)).
- **Infineon.**
  - *Said:* data-centre power revenue approaching €4bn in FY27; 300 mm GaN in 2027.
  - *Done:* €1.7bn of AI power revenue in FY26; 800 V IBC reference designs; joined MGX ([Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954); [Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)).
- **Eaton.**
  - *Said:* 800 VDC reference architecture (Oct 2025).
  - *Done:* bought Resilient Power (Aug 2025), Fibrebond ($1.43bn, Apr 2025) and Boyd ($9.55bn, Mar 2026). UL-tested 15 kV / 2 MW SST; 10 pilots ([8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm); [call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).
- **Schneider.**
  - *Said:* megawatt-scale solutions (GTC 2026).
  - *Done:* no dated 800 VDC product found. Capacity is being added in prefab and liquid cooling ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279)).
- **Vertiv (power).**
  - *Said:* 800 VDC portfolio in H2 2026.
  - *Done:* in validation; revenue 2027; deployment 2028. That is a slip ([PR](https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html); [Yahoo](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)).

### Inferences
Suggested verdicts (inference):

- **Delta: coherent.**
  - Must get through transition 6 (and transition 5 for cooling, covered elsewhere).
  - The bridge (54 V shelves, BBUs) is earning record profits that fund the successor. It shows successor hardware across the whole chain: 800 VDC racks, high-voltage BBUs and an SST.
  - Funding is internal (trailing free cash flow NT$66.5bn, net cash ~NT$98bn, ROIC ~35%; [stockanalysis](https://stockanalysis.com/quote/tpe/2308/statistics/)), so it can absorb a 1–2 year slip.
  - What must go right: native 800 VDC or +/-400 VDC sidecars reach volume in 2027–28; it keeps first-source status as the in-rack PSU moves into a sidecar, where integrated electrical groups also compete; and the VPD-focused ITC case does not touch its power-module business.
- **Lite-On: coherent.** It has a dated successor (Q1 2027 shipments), internal funding and rising capex. Its risks are being second source and running at lower gross margin.
- **MPS: coherent.** Funding is strong (net cash, ~38% non-GAAP operating margin). Management sets realistic timing (late-2027 to 2028 for 800 V) and does not depend on 800 V for growth. What must go right: winning VPD sockets against ADI-Empower, Vicor, Infineon and Delta-class module makers, and avoiding Vicor-style IP friction.
- **Infineon: coherent.** It covers every stage of the conversion chain (SiC and GaN at 800 V, silicon at low voltage) and has a fab roadmap (300 mm GaN from 2027) funded by €3.0–3.5bn of capex. It is funded through a slip, though at low ROCE (7.2%).
- **Eaton: coherent.** It bought the successor technology (SST) rather than promising it, has third-party UL certification, and is funded by ~$1bn of quarterly free cash flow. The risks are leverage after Boyd and the UPS bridge shrinking under native DC.
- **Vertiv (power): partly coherent.** It is funded, but its successor slipped about a year against its own October 2025 date. Its UPS franchise is the product most directly displaced by native 800 VDC, which offsets the gain if bridges last longer.
- **Schneider: partly coherent.** This reflects an evidence gap, not proof of weakness: no dated 800 VDC product or SST was found in this pass. The bridge business and financing are strong.

### Gaps
- No verified shipment of a production 800 VDC power rack to a paying customer by Nov 2026.
- No verified 800 VDC or SST product dates from Schneider, ABB or Siemens.
- AMD's and Chinese hyperscalers' DC architectures were not documented.
- Google's and Meta's +/-400 VDC deployment status (in production or not) was not documented. Mt. Diablo is a spec, not proof of deployment.

## (4) Suggested ordering of the key companies by quality alone

### Takeaway
Suggested order, judged on quality only:

| Rank | Company | Note |
|---|---|---|
| 1 = | MPS | Tie with Delta: cannot separate |
| 1 = | Delta | Tie with MPS |
| 3 = | Eaton | Tie with Schneider: cannot separate |
| 3 = | Schneider | Tie with Eaton |
| 5 = | Infineon | Tie with Lite-On |
| 5 = | Lite-On | Tie with Infineon |
| 7 | Vertiv (power) | |
| Near-key | Vicor | Would rank on margin and IP but is hard to place given litigation dependence and small scale |

### Cited Findings
Key metrics side by side. "Trailing" = twelve months to Sep 2026 on stockanalysis's filings-derived definitions, accessed 12 Nov 2026.

| Company | Margins (latest quarter) | Trailing ROIC | Trailing free cash flow | Net cash (debt) | Other | Sources |
|---|---|---|---|---|---|---|
| MPS | Q3 2026 non-GAAP gross 55.7%, operating 38.6%; revenue +63% YoY | 33.3% | 16.3% of revenue | ~$1.07bn net cash | Top three distributors 54% of FY2025 revenue; 92% of revenue from Asia | [8-K](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm); [stockanalysis](https://stockanalysis.com/stocks/mpwr/statistics/); [10-K](https://www.sec.gov/Archives/edgar/data/1280452/000143774926006113/mpwr20251231_10k.htm) |
| Delta | Q3 2026 operating 16.6%, gross 34.1%; nine-month revenue +37% | 34.9% (ROE 28.5%) | NT$66.5bn (9.5% of revenue) | ~NT$98bn net cash | ~70% Blackwell PSU share (KGI estimate) | [BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29); [KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf); [stockanalysis](https://stockanalysis.com/quote/tpe/2308/statistics/) |
| Eaton | Q3 2026 segment 25.3% | 11.0% | $3.80bn | ~$20.1bn net debt | Book-to-bill 1.2 | [8-K Q3](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm); [stockanalysis](https://stockanalysis.com/stocks/etn/statistics/) |
| Schneider | Adjusted EBITA ~19.7–19.9% (FY26 guidance) | 14.0% | €6.19bn (14.7% of revenue) | ~€16.3bn net debt | — | [transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279); [stockanalysis](https://stockanalysis.com/quote/epa/SU/statistics/) |
| Infineon | FY26 segment result 19.7% | 7.2% (ROCE 7.2%) | €1.98bn | ~€5.2bn net debt (stockanalysis definition) | — | [Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954); [stockanalysis](https://stockanalysis.com/quote/etr/IFX/statistics/) |
| Lite-On | Q3 2026 operating 15.1%, gross 25.9% | ~30% (company says 34%) | −NT$7.8bn | ~NT$26bn net cash | — | [Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30); [stockanalysis](https://stockanalysis.com/quote/tpe/2301/statistics/) |
| Vicor | Q3 2026 gross 68.3% | 37.1% | — | ~$506m net cash | Royalties ~34% of Q3 revenue | [call](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190); [stockanalysis](https://stockanalysis.com/stocks/vicr/statistics/) |

### Inferences
- **MPS and Delta tie at the top.** Both earn ~33–35% ROIC with net cash.
  - MPS has far higher margins, its own process know-how and the clearer chip-level successor (vertical power). Against that, it sells 54% through three distributors and bills 92% in Asia.
  - Delta has the larger, third-party-estimated lead (~70% of Blackwell PSUs), solid free cash flow and the full set of successor hardware. Against that, its margins are mid-teens, sales are hardware-only, ~50% of revenue is AI, and it faces ITC exposure.
  - The filings-derived data added late in the research moved Delta up from the Eaton tier.
- **Eaton and Schneider tie.** Eaton has the clearer successor path (UL-tested SST, 800 VDC architecture) and a larger backlog. Schneider has better cash conversion (free cash flow ~15% of revenue) and higher ROIC (~14% vs ~11%), but thin 800 VDC evidence. Both carry sizeable net debt.
- **Infineon and Lite-On tie.** Infineon has deep fab and process moats across Si, SiC and GaN, but low returns (ROIC 7.2%), net debt and auto cyclicality. Lite-On has high returns but is a number-two hardware maker with negative trailing free cash flow during its build-out.
- **Vertiv (power) is last.** Its bridge is strong, but its successor slipped and its UPS franchise is at risk. Group-level quality is assessed in the cooling notes.
- **Vicor** has ROIC ~37%, net cash and a ~61% gross margin. It would rank near the top on financials, but its moat depends on litigation and its scale is small (~$0.56bn of revenue).

### Gaps
- Returns and cash flow come from an aggregator (stockanalysis), not annual reports.
- Customer concentration is still missing for every company except MPS, and for MPS only at distributor level. A disclosure that one customer takes more than 30% of Delta's or Lite-On's revenue would lower their rank.

## (5) Check of the background priors

### Takeaway
- The Kyber-2028 prior is **confirmed and should be strengthened**. The prior should also note that the 600 kW figure may itself be cut.
- The processor-power prior is **confirmed**, on secondary data.
- The "rack power binds and bridges last longer" prior is **confirmed** by suppliers' own timing slips.
- The 1 MW-by-2030 prior has **no direct evidence either way**. It should stay at ~50% or edge lower, and the definition should be tightened (a 1 MW sidecar power rack versus a 1 MW IT rack).

### Cited Findings
**Prior 1: Kyber 600 kW ships in volume in 2028, not 2027 (65%)**
- Evidence for a delay:
  - Jefferies (22 Jun 2026) and SemiAnalysis (6 Jul 2026) reported a delay to 2028 ([KuCoin/Tide](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge)).
  - SemiAnalysis (10 Jun 2026) reported native 800 VDC delayed until after 2028 (same source).
  - Vertiv (28 Oct 2026) puts 800 VDC deployment in 2028 ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)).
  - MPS (30 Oct 2026) puts 800 V revenue at the end of 2027 and in 2028 ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)).
  - HVDC BBUs reach significant revenue in 2028 (analyst) ([cnyes mirror](https://aeo.idaeo.ai/ai/news-cnyes-com/en/news/2026-07-26-data-center-power-revolution-with-major)).
  - The GTC 2026 Kyber redesign halved the sleds (36 vs 72) ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained)).
- Evidence against:
  - NVIDIA: "Our roadmap is intact"; H2 2027 reaffirmed at GTC and Computex 2026 ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained)).
  - Lite-On ships 800 VDC racks from Q1 2027, contingent on customers ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).

**Prior 2: 1 MW racks in production use by end-2030 (50%)**
- Mt. Diablo 1.0 specifies 800 kW to 1.1 MW sidecar power racks ([OCP spec](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf)).
- NVIDIA says 800 VDC supports 1 MW racks "starting 2027" ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained)).
- Visionbay's 800 VDC factory "scales from 100 kW racks toward 1 MW" and is under construction ([TechArena](https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat)).
- No 1 MW IT rack was found in production.

**Prior 3: processors up to 2.3 kW, heading to 4 kW**
- Rubin is ~2.3 kW "Max-P", raised from 1.8 kW and reportedly NVIDIA-confirmed ([Tech-Insider, 16 Mar 2026](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/), secondary).
- Estimates for Rubin Ultra conflict: ~3.6 kW per package in independent tracking ([GPU Smith](https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained)) versus ~2.5 kW ([Tech-Insider](https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/)).
- An OCP 2026 thermal paper puts the single-phase cold-plate limit near 4,000 W per reticle-class die, with frontier package power doubling about every two years ([TechArena](https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat)).
- Rack TDP history: GB200 NVL72 120 kW → GB300 136 kW → Rubin 250 kW → Rubin Ultra 600 kW ([KGI, Jul 2025](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)).

**Prior 4: rack power is a binding constraint in 2028–30; successors slip; bridges last longer**
- Vertiv's 800 VDC slipped about a year ([PR](https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html); [Yahoo](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)).
- Rubin Ultra is reportedly reverting to Oberon NVL72 ([KuCoin/Tide](https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge)).
- Delta's Q3 shortfall came from data-centre build delays; it names grid power and electricians as constraints ([BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29)).
- US power shortages hurt Lite-On's Q1 pulls ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).
- Medium- and high-voltage transformer lead times are 18–36 months ([Data Center Richness](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)).

### Inferences
- **Prior 1:** the evidence leans further toward 2028 than the prior. Suggest ~70–75% that Kyber-class 800 VDC racks reach volume in 2028 or later. Also flag a material chance that the volume Kyber is specified below 600 kW (inference).
- **Prior 2:** unchanged at ~50%, with downside because native 800 VDC is reportedly after 2028. A 1 MW *power* rack (sidecar) is very likely before 2030; a 1 MW *IT* rack is the uncertain part.
- **Prior 3:** confirmed. The 4 kW trajectory has secondary support only; no NVIDIA datasheet TDP was found.
- **Prior 4:** confirmed. Bridges (54 V shelves, AC UPS, BBUs) gained at least a year.

### Gaps
- No NVIDIA primary statement on the Kyber date after July 2026 was found. The "roadmap intact" quote is reported secondhand.
- No NVIDIA datasheet TDP for Rubin or Rubin Ultra was found.
- No hyperscaler disclosure of 1 MW IT racks in production was found.

## (6) Open question: which successor ships first, and who captures the value

### Takeaway
Likely order of volume shipment (inference from dated supplier statements):

1. In-rack energy storage and 54 V-era "bridge-plus" upgrades (shipping now).
2. +/-400 VDC or 800 VDC sidecar and in-row power racks from 2027.
3. MV SSTs in pilots now, with early commercial lots in 2026–27 and volume after 2028.
4. Native 800 VDC to the board last (after 2028).

At the chip, VPD is commercially licensed (Vicor) and being consolidated (ADI–Empower) but is not yet in volume. On value, Taiwanese specialists take most of the in-rack hardware dollars, and chip-level specialists (MPS, Vicor, Infineon) take the highest margins. Integrated groups (Eaton above all) are best placed for the SST and grid side. Their AC-UPS bridge franchise is the asset most at risk from native DC.

### Cited Findings
- **Shipping now:**
  - GB300 shelves with energy storage that cuts grid-facing peak power by 30% ([NVIDIA blog](https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/), search summary).
  - BBUs in mass production (Lite-On) ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).
  - Taiwanese BBU makers' revenue rising ([Digitimes](https://www.digitimes.com/news/a20260706PD241/ai-server-battery-demand-revenue.html)).
- **2027 power racks:**
  - Lite-On from Q1 2027 ([Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30)).
  - Delta's 660 kW rack shown ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)).
  - Megmeet's 800 V / 570 kW side rack ([ifeng](https://finance.ifeng.com/c/8w4hMGJVOYE)).
  - Vertiv's revenue from 2027 ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)).
  - The Mt. Diablo 1.0 sidecar is final ([OCP](https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf)).
- **SSTs:**
  - Eaton: UL-tested 15 kV / 2 MW unit, 10 pilots ([call](https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html)).
  - Heron: demos mid-2026, installs early 2027 ([TechCrunch](https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/)).
  - Amperesand: 30 MW target for 2026 ([Data Center Richness](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)).
  - OCP SST spec only at v0.3 ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)).
  - "Still in hyperscaler validation and early pilots" ([Ted Yu](https://ytyuted.substack.com/p/ep69-ocp-2026-ai)).
  - Arista showed a 28.8 MW pod design with four 9.6 MW SSTs fed at 34.5 kV ([Ted Yu](https://ytyuted.substack.com/p/ep69-ocp-2026-ai)).
- **Native DC to the board:** the OCP board-level 800 VDC / 48 VDC workstream only formed in Q4 2026 ([Ted Yu](https://ytyuted.substack.com/p/ep69-ocp-2026-ai)).
- **Lateral versus vertical at the chip:**
  - MPS CEO: "you have to do vertical" ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)).
  - Vicor's first pure VPD licence; a lead customer's large 2nd-generation VPD order; the CEO says IVR timing is "still out" ([Vicor call](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190)).
  - ADI announced the Empower deal on 19 May 2026 and completed it on 7 Jul 2026 for ~$1.5bn ([ADI PR](https://www.analog.com/en/newsroom/press-releases/2026/5-19-2026-adi-to-acquire-empower-semiconductor.html); [ADI 10-Q](https://www.sec.gov/Archives/edgar/data/6281/000000628126000073/adi-20260801.htm), primary). A large analog incumbent now owns an integrated-voltage-regulator and VPD start-up. MPS declined to comment on the deal ([MPS call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)).
  - Empower demonstrated ~1,000 A at 0.75 V ([APEC PR](https://www.globenewswire.com/news-release/2026/03/10/3252703/0/en/Empower-Semiconductor-Showcases-Vertical-Power-Delivery-Innovations-at-APEC-2026.html)).
  - A new ITC investigation targets VPD systems ([Taipei Times](https://www.taipeitimes.com/News/biz/archives/2026/10/12/2003865784)).
- **Silicon versus GaN versus SiC:**
  - MPS lets customers choose GaN or SiC ([call](https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/)).
  - The 800 V-to-6/12 V GaN designs from TI, ST, Navitas, EPC and Infineon are reference designs ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)).
  - Infineon starts 300 mm GaN in 2027 ([Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)).
  - Navitas reportedly landed an order for 1 million GaN devices for an 800 V brick (call summary, company claim) ([Navitas](https://www.globenewswire.com/news-release/2026/11/03/3394777/0/en/navitas-semiconductor-announces-third-quarter-2026-financial-results.html)).
  - Innoscience: AI and data-centre chip shipments +183% (H1 2026) ([Chongdiantou](https://www.chongdiantou.com/archives/1788406187582.html)).
- **Value pools:**
  - PSU content per rack: GB200 US$35–40k → GB300 US$60–70k → VR200 more than US$150k ([KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)).
  - Infineon semiconductor content: $100–250/kW ([Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954)).
  - A KGI estimate says 800 VDC power racks lift system efficiency by 4–5 points to above 92% ([KGI](https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf)).
  - Vicor's CEO argues 800 V gives only a few points of system efficiency and that the point-of-load stage is the binding constraint ([Vicor call](https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190)).
  - DG Matrix's CTO claims NVIDIA's 800 V reference would eliminate UPSs (claim, unconfirmed) ([PEN](https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/)).
- **Margins by layer:**

  | Layer | Company | Margin | Source |
  |---|---|---|---|
  | Chip | MPS | 38.6% non-GAAP operating margin | [8-K](https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm) |
  | Chip | Vicor | 68.3% gross margin | [Q3 results](https://www.nasdaq.com/press-release/vicor-corporation-reports-results-third-quarter-ended-september-30-2026-2026-10-20) |
  | Chip | Infineon Power Systems | 23.5% segment margin | [Investing.com](https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954) |
  | Rack | Delta | 16.6% operating margin | [BigGo](https://finance.biggo.com/news/TW_2308.TW_2026-10-29) |
  | Rack | Lite-On | 15.1% operating margin | [Fugle](https://blog.fugle.tw/post/earnings-call-2301-2026-10-30) |
  | Integrated | Eaton Electrical Americas | 29.8% segment margin | [8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm) |

### Inferences
- The +/-400 VDC sidecar is likely the first successor in volume. Its spec is final, three hyperscalers wrote it, and CMBI says ASIC-side +/-400 VDC is on schedule. NVIDIA's native two-wire 800 VDC depends on Kyber timing.
- SSTs follow later. Eaton (UL-certified, with a manufacturing base) and Delta are better placed than start-ups to supply the first data-centre volumes. Start-ups have funding (Heron $140m, DG Matrix $60m, Amperesand $80m) but must win against incumbents' MV qualification and service networks.
- On value capture:
  - Specialists capture the in-rack and in-row hardware. Delta and Lite-On's sidecar and BBU products are direct successors of their shelves.
  - Chip specialists capture the highest-margin step, VPD.
  - Integrated groups capture SSTs, MV and services, but must cannibalise UPS revenue.
  - Net: specialists gain share of incremental dollars; integrated groups keep the facility side.
- The ITC VPD case is a wild card that could redirect chip-level value toward Vicor through royalties.

### Gaps
- No market sizing of sidecar versus in-rack shelves from Dell'Oro or Omdia.
- No volume data on SST shipments.
- No independent efficiency measurement of 800 VDC versus 54 V systems (only vendor and analyst figures).

## (7) What could not be verified

### Takeaway
Gaps come mainly from the web-search budget running out mid-task (tool notice) and from paywalls (TrendForce full reports, Digitimes, Benzinga transcripts, the KGI full report).

### Cited Findings
- The lead that "Vertiv said its 800 V portfolio would be available in H2 2026" is verified, as is the later slip ([PR](https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html); [Yahoo](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)).
- The leads on Eaton–Resilient Power and Eaton–Boyd are verified; Boyd closed 12 Mar 2026 for $9.55bn ([8-K](https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm)).
- The lead on Infineon's AI targets is verified ([Power Semiconductors Weekly](https://www.powersemiconductorsweekly.com/2026/11/10/infineon-reports-12-revenue-growth-to-e16-35-billion-in-fy2026-forecasts-e20-billion-for-fy2027-on-strong-ai-data-center-demand/)).
- The lead on Vicor's 2025 ITC exclusion order is verified: final determination 13 Feb 2025 ([Vicor](https://www.vicorpower.com/press-room/itc-bars-importation-of-power-modules), search summary).
- The lead on NVIDIA's May and October 2025 partners is verified for October ([NVIDIA](https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/)). The May 2025 tie to 2027 is seen only secondhand ([Converge Digest](https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/)).
- The lead on SolarEdge's SST programme is only partly verified: "launched" per one secondary source ([Data Center Richness](https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape)).

### Inferences
- The overall picture (timing slips, the +/-400 VDC versus 800 VDC fork, Delta's lead, MPS's margins) rests on several independent sources. Company-level concentration data is the weakest part.

### Gaps
- **Not collected:**
  - Annual-report detail for Delta, Lite-On and Schneider. Annual and trailing figures came from stockanalysis aggregates, not the reports.
  - Customer concentration (largest customer and top five) for every key company except MPS, which discloses distributors only.
  - Revenue by country for every key company except MPS.
- **Third-party market shares:** none collected for PSUs (beyond KGI's 2025 estimate), BBUs, vertical power modules, or controllers and power stages (Dell'Oro and Omdia not reached).
- **Companies without evidence** (AcBel, Chicony Power, Advanced Energy and Megmeet now have filings-derived financials only): FSP, Flex (financials), Huawei Digital Power, Kehua, Ourmate, Zhongheng, Mitsubishi Electric, Fuji Electric, TDK, Murata, ROHM, Renesas, LS Electric, LS Materials, Samsung Electro-Mechanics' financials, Samsung SDI, Simplo, Dynapack and AES-KY financials, Musashi, Nippon Chemi-Con, Skeleton (beyond company claims), Wolfspeed's status, onsemi, TI, ADI and ST AI-power revenue.
- **India:** no player identified; NSE and BSE not searched.
- **Policy:** gallium and germanium export controls, tariffs on power equipment, and production shares in Taiwan, Thailand, Mexico and China were not documented beyond the items above.
- **Deals:** ADI–Empower is now verified (closed 7 Jul 2026, ~$1.5bn, ADI 10-Q). Empower's revenue and customers at the time of acquisition were not found.
- **NVIDIA primary statements:** none after July 2026 on Kyber timing; no TDP datasheets.
- **Shipments:** Megmeet's reported "GB300 800 V HVDC power delivered H1 2026" is a broker claim. It may be mislabelled, since GB300 racks use 54 V shelves.
- **Fed Circuit:** the outcome of Vicor's appeal is unknown.

## (8) Sources

### Takeaway
Primary sources: OCP's Mt. Diablo 1.0 PDF, NVIDIA's technical blog, Microsoft's Azure blog, SEC 8-Ks for MPS, Eaton and Vertiv, the MPS FY2025 10-K, the ADI 10-Q and the Eaton Q3 2026 10-Q. Delta's release and HKEX's Innoscience interim report are also primary. Most other items are secondary (trade press, analyst notes, call summaries) and are labelled as such above.

### Cited Findings
**Primary**
- OCP, Mt. Diablo Disaggregated Power Rack Specification 1.0.0, effective 8 Oct 2026 — https://www.opencompute.org/wp-content/uploads/2026/10/OCP-Specification-Mt.-Diablo-Disaggregated-Power-Rack-Specification-v1.0.0.pdf
- NVIDIA technical blog, "Building the 800 VDC Ecosystem…", 13 Oct 2025 — https://developer.nvidia.com/blog/building-the-800-vdc-ecosystem-for-efficient-scalable-ai-factories/
- NVIDIA blog on GB300 power smoothing (search summary only) — https://developer.nvidia.com/blog/how-new-gb300-nvl72-features-provide-steady-power-for-ai/
- Microsoft Azure blog, 13 Oct 2026 — https://azure.microsoft.com/en-us/blog/infrastructure-for-the-frontier-era-scaling-intelligence-through-open-industry-collaboration/
- MPS 8-K Q3 2026, 29 Oct 2026 — https://www.sec.gov/Archives/edgar/data/0001280452/000162828026068202/mpwr-20260930xexx991.htm
- Eaton 8-K Q3 2026, 3 Nov 2026 — https://www.sec.gov/Archives/edgar/data/0001551182/000155118226000037/etn09302026exhibit99.htm
- Eaton 8-K FY2025, 26 Feb 2026 — https://www.sec.gov/Archives/edgar/data/1551182/000155118226000002/etn12312025exhibit99.htm
- Vertiv 8-K Q3 2026, 28 Oct 2026 — https://www.sec.gov/Archives/edgar/data/0001674101/000162828026067707/q32026exhibit991vrt10282026.htm
- Vertiv PR, 13 Oct 2025 — https://www.prnewswire.com/news-releases/from-vision-to-readiness-vertiv-collaborates-with-nvidia-to-advance-800-vdc-platform-designs-to-power-the-next-generation-of-ai-factories-302582190.html
- Delta Q3 2026 release (via Gulf Oil & Gas), 28 Oct 2026 — https://www.gulfoilandgas.com/webpro1/main/mainnews.asp?id=1149042
- Innoscience 2026 interim report (HKEX), 18 Sep 2026 — https://www.hkexnews.hk/listedco/listconews/sehk/2026/0918/2026091800446_c.pdf
- Heron Power PR, 18 Feb 2026 — https://www.globenewswire.com/news-release/2026/02/18/3240170/0/en/Heron-Power-Raises-140-Million-to-Build-a-Next-Generation-Power-Grid-in-Series-B-Co-led-by-Andreessen-Horowitz-Breakthrough-Energy-Ventures.html
- Empower press-release index (accessed 12 Nov 2026) — https://www.empowersemi.com/category/press-release/ ; APEC PR, 10 Mar 2026 — https://www.globenewswire.com/news-release/2026/03/10/3252703/0/en/Empower-Semiconductor-Showcases-Vertical-Power-Delivery-Innovations-at-APEC-2026.html
- ADI PR, 19 May 2026 (search result; page returned 503) — https://www.analog.com/en/newsroom/press-releases/2026/5-19-2026-adi-to-acquire-empower-semiconductor.html
- TI PR, 16 Mar 2026 (search result) — https://www.ti.com/en-us/about-ti/newsroom/news-releases/2026/2026-03-16-ti-unveils-complete-800-vdc-power-architecture-for-future-generation-ai-data-centers-with-nvidia
- Vicor ITC PR (search summary) — https://www.vicorpower.com/press-room/itc-bars-importation-of-power-modules ; Vicor Q3 2026 results, 20 Oct 2026 (search summary) — https://www.nasdaq.com/press-release/vicor-corporation-reports-results-third-quarter-ended-september-30-2026-2026-10-20
- Navitas Q3 2026 results, 3 Nov 2026 (search summary) — https://www.globenewswire.com/news-release/2026/11/03/3394777/0/en/navitas-semiconductor-announces-third-quarter-2026-financial-results.html

**Primary filings added after the search budget ran out (fetched directly from SEC EDGAR)**
- MPS FY2025 10-K, filed 27 Feb 2026 — https://www.sec.gov/Archives/edgar/data/1280452/000143774926006113/mpwr20251231_10k.htm
- ADI 10-Q for the quarter to 1 Aug 2026, filed 19 Aug 2026 (Empower closing, ~$1.5bn, 7 Jul 2026) — https://www.sec.gov/Archives/edgar/data/6281/000000628126000073/adi-20260801.htm
- Eaton 10-Q Q3 2026 (Resilient Power $86m; Boyd $9.55bn; Fibrebond $1.43bn) — https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm

**Filings-derived aggregates** (stockanalysis.com, S&P Global Market Intelligence data, accessed 12 Nov 2026). Only revenue, margins, cash flow, returns and net cash/debt were used:
- Delta — https://stockanalysis.com/quote/tpe/2308/financials/ ; https://stockanalysis.com/quote/tpe/2308/statistics/
- Lite-On — https://stockanalysis.com/quote/tpe/2301/financials/ ; https://stockanalysis.com/quote/tpe/2301/statistics/
- AcBel — https://stockanalysis.com/quote/tpe/6282/financials/
- Chicony Power — https://stockanalysis.com/quote/tpe/6412/financials/
- Megmeet — https://stockanalysis.com/quote/she/002851/financials/
- Advanced Energy — https://stockanalysis.com/stocks/aeis/financials/?p=quarterly
- Infineon — https://stockanalysis.com/quote/etr/IFX/statistics/
- Schneider — https://stockanalysis.com/quote/epa/SU/statistics/
- MPS — https://stockanalysis.com/stocks/mpwr/statistics/
- Eaton — https://stockanalysis.com/stocks/etn/statistics/
- Vicor — https://stockanalysis.com/stocks/vicr/statistics/

**Transcripts and call summaries (secondary transcriptions of primary calls)**
- MPS Q3 2026 call (Motley Fool), 30 Oct 2026 — https://www.fool.com/earnings/call-transcripts/2026/10/30/monolithic-power-systems-mpwr-q3-2026-earnings-call-transcript/
- Schneider Q3 2026 call (Investing.com), 16 Oct 2026 — https://www.investing.com/news/transcripts/earnings-call-transcript-schneider-electric-posts-record-q3-2026-revenue-93CH-4953279
- Vicor Q3 2026 call (Investing.com), Oct 2026 — https://www.investing.com/news/transcripts/earnings-call-transcript-vicor-tops-q3-2026-estimates-as-ai-demand-lifts-sales-93CH-4960190
- Eaton Q3 2026 call highlights (MarketBeat via Yahoo), 3 Nov 2026 — https://finance.yahoo.com/markets/stocks/articles/eaton-q3-earnings-call-highlights-051410047.html
- Vertiv Q3 2026 call summary (Yahoo), 28 Oct 2026 — https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html
- Delta Q3 2026 call (BigGo), 29 Oct 2026 — https://finance.biggo.com/news/TW_2308.TW_2026-10-29 and https://finance.biggo.com/news/44f1e3fc-db83-4b4e-85f5-474840dae41b
- Lite-On Q3 2026 call (Fugle AI summary), 30 Oct 2026 — https://blog.fugle.tw/post/earnings-call-2301-2026-10-30 ; cnyes — https://news.cnyes.com/news/id/6641958 ; CNA — https://www.cna.com.tw/news/afe/202610300203.aspx
- Infineon FY2026 slides (Investing.com), 10 Nov 2026 — https://in.investing.com/news/stock-market-news/infineon-fy26-slides-ai-boom-drives-record-results-20bn-fy27-target-93CH-5692954 ; Power Semiconductors Weekly, 10 Nov 2026 — https://www.powersemiconductorsweekly.com/2026/11/10/infineon-reports-12-revenue-growth-to-e16-35-billion-in-fy2026-forecasts-e20-billion-for-fy2027-on-strong-ai-data-center-demand/

**Trade press and analysts (secondary)**
- Power Electronics News, GTC 2026 800 VDC, 19 Mar 2026 — https://www.powerelectronicsnews.com/nvidia-gtc-2026-800-vdc-power-partnerships-from-grid-to-processor/
- Power Electronics News, passives, 19 Nov 2025 — https://www.powerelectronicsnews.com/impact-of-ai-systems-on-passive-components/
- Converge Digest, OCP 800 VDC, 12 Aug 2026 — https://convergedigest.com/ocp-800-vdc-standard-megawatt-ai-racks/
- TechArena, OCP Global Summit 2026, 15 Oct 2026 — https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat
- Ted Yu, EP69 OCP 2026 (Chinese), 3 Nov 2026 — https://ytyuted.substack.com/p/ep69-ocp-2026-ai
- KuCoin repost of Tide Research / TechFlow (SemiAnalysis and Jefferies), 6 Jul 2026 — https://www.kucoin.com/news/flash/nvidia-kyber-delayed-to-2028-supply-chain-winners-and-losers-emerge
- Barchart via Yahoo, 8 Jul 2026 — https://finance.yahoo.com/technology/ai/articles/nvidia-allegedly-delaying-kyber-rack-155030298.html
- GPU Smith Kyber explainer, 23 Jul 2026 (updated 14 Oct 2026) — https://gpusmith.com/articles/en/nvidia-kyber-rack-scale-system-explained
- Tech-Insider, Rubin analysis, 16 Mar 2026 (updated 25 Apr 2026) — https://tech-insider.org/nvidia-gtc-2026-rubin-gpu-analysis/
- KGI Securities, "Power supply sector: Powering the AI beast", 1 Jul 2025 — https://www.kgi.com.hk/en/-/media/files/kgishk/research-reports/tw-reports/power-supply-industry_01072025.pdf
- TrendForce AI Infra bulletins, Mar 2026 (search summary) and 27 Aug 2026 — https://www.trendforce.com/research/download/RP260326MW ; https://www.trendforce.com/research/download/RP260827TB
- Digitimes, BBU demand, 6–7 Jul 2026 — https://www.digitimes.com/news/a20260706PD241/ai-server-battery-demand-revenue.html
- cnyes analyst piece (mirror), Panasonic and BBUs, 26 Jul 2026 — https://aeo.idaeo.ai/ai/news-cnyes-com/en/news/2026-07-26-data-center-power-revolution-with-major
- certi.news, Panasonic Energy (search summary) — https://certi.news/en/article/14090
- Data Center Richness, SSTs, 16 Jun 2026 — https://datacenterrichness.substack.com/p/solid-state-transformers-could-reshape
- TechCrunch, Heron, 18 Feb 2026 — https://techcrunch.com/2026/02/18/heron-power-raises-140m-to-ramp-production-of-grid-altering-tech/
- Taipei Times, Vicor ITC probe, 12 Oct 2026 — https://www.taipeitimes.com/News/biz/archives/2026/10/12/2003865784
- Fed Circuit Blog, 28 Oct 2026 (search summary) — https://fedcircuitblog.com/2026/10/28/argument-preview-vicor-corp-v-international-trade-commission/
- BiotechClin, NVIDIA partner page, 30 May 2026 — https://biotechclin.substack.com/p/nvidias-official-800v-dc-architecture
- ifeng, Megmeet, 1 Sep 2026 — https://finance.ifeng.com/c/8w4hMGJVOYE
- Sohu / 10jqka, Megmeet investor Q&A, 24 Sep 2026 (search summary) — https://www.sohu.com/a/1080573199_122121789
- Sohu, A-share 800 V names, May 2026 (search summary) — https://m.sohu.com/a/1028510124_122014422
- Chongdiantou, Innoscience H1 2026 — https://www.chongdiantou.com/archives/1788406187582.html
- Xueqiu broker-note summary (search summary) — https://xueqiu.com/9282597341/397179025
- Reuters via MarketScreener, Schneider, 16 Oct 2026 — https://www.marketscreener.com/news/schneider-electric-raises-2026-targets-again-on-booming-data-centre-demand-ce785cdad98cf322
- Thailand Business News, Delta Thailand Q3 2026 (search summary) — https://www.thailand-business-news.com/business/336934-delta-thailand-q3-sales-surge-42-4-on-ai-demand-profit-misses-estimates
- Futurum, GB300 power shelf (search summary) — https://futurumgroup.com/insights/is-nvidias-gb300-nvl72-power-shelf-the-answer-to-ais-grid-strain/
- YMIN, LIC and BBU (competitor marketing; search summary) — https://www.ymin.cn/news/millisecond-level-transient-power-gaps-in-ai-server-rack-bbus-why-is-a-hybrid-supercapacitor-lic-bbu-more-suitable/ ; Moljuurtei, Musashi blog — https://www.moljuurtei.com/blog/en/musashi-seimitsu-hsc-ai-power-buffer

### Inferences
- Where secondary sources conflict (Rubin Ultra power 2.5 vs 3.6 kW; Schneider China +26% vs +32%; Vicor revenue categories), both figures are kept above rather than one being picked.

### Gaps
- Benzinga transcripts (Vertiv, Eaton) returned 403. The Globe and Mail copy returned 404. The 21jingji and FourWeekMBA pages (Chinese AI campus on 800 V DC) returned 503 and 403, so Chinese hyperscalers' 800 V deployment remains unverified.

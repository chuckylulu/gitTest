# Package substrates for AI processors — organic ABF, glass cores, glass interposers and upstream materials (research date 12 Nov 2026)

**Conventions.** PRIMARY = company results deck, regulated filing or official release. SECONDARY = trade press, analysts, aggregators, blogs (reliability noted where weak). "Company claim, unconfirmed" = no outside party confirmed it. Japanese fiscal years: Ibiden, Ajinomoto and Nittobo "FY2026" = Apr 2026–Mar 2027; AT&S "2026/27" = Apr 2026–Mar 2027. No share prices, valuation multiples, market caps or price targets are used. Figures marked "(my arithmetic)" are derived by me from the cited numbers.

**Method limitation.** The shared WebSearch budget for this run was exhausted after about 25 of my searches, and the coordinator later confirmed the Exa and Firecrawl budgets were also spent. The rest of the evidence came from direct fetches:
- pages already surfaced;
- companies' own IR documents: Ibiden tanshin, Q&A and capex notice; AT&S half-year report 2026/27 and annual financial report 2025/26; Ajinomoto Q2 deck; NVIDIA and SEMCO releases;
- third-party TTM statistics pages (stockanalysis.com), from which I took only quality metrics (margins, ROE/ROIC, net cash, FCF) and no valuation fields.

The gaps in section 7 partly reflect this; a follow-up pass could close them.

---

## (1) Segment map

### Takeaway
AI-grade organic substrate supply is concentrated in Ibiden (Japan), Unimicron (Taiwan) and Samsung Electro-Mechanics (Korea), with AT&S (Austria; plants in China and Malaysia) as the Western-owned challenger. All of them depend on two Japanese chokepoints: Ajinomoto build-up film (ABF) and Nittobo low-expansion T-glass cloth. Glass-core and glass-interposer programmes are crowded across Korea, the US, Japan, China and India, but none ships glass-core substrates in volume as of Nov 2026. China has credible mid-layer FC-BGA makers (Shennan Circuits, Fastprint), but I found no confirmed qualification on a leading AI accelerator. I found no Israeli player. India's only relevant project is 3D Glass Solutions' Odisha glass-substrate unit, with production targeted for 2030.

### A. Organic ABF / FC-BGA substrate makers
| Company | Home | Listing / ticker | Role | Why it matters (or why left out) |
|---|---|---|---|---|
| Ibiden | Japan | TSE 4062 | Leading AI GPU/ASIC/CPU ABF substrate maker; Ono plant (GPU), Gama plant (ASIC/CPU) | **KEY.** NVIDIA funds a 3x expansion of Ono ([NVIDIA, 21 Oct 2026](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx)); BofA estimates 70–80% share of GPU substrates (secondary) ([thebuildout.ai, 26 Mar 2026](https://thebuildout.ai/intel/229c44f2-da57-4f46-b5fa-e5d03702236c)) |
| Unimicron | Taiwan | TWSE 3037 | Largest Taiwanese ABF maker; substrates ~68% of Q3 2026 revenue | **KEY.** NVIDIA capacity-reservation agreement for its "KF" expansion ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx)) |
| Samsung Electro-Mechanics (SEMCO) | Korea | KRX 009150 | FC-BGA for server CPUs, AI accelerators and network switches; new NVIDIA supplier; glass-core JV | **KEY.** Only large player on both the organic and the glass sides ([SEMCO, 21 Oct 2026](https://m.samsungsem.com/global/newsroom/news/view.do?id=10614)) |
| AT&S | Austria | Vienna (ATS) | High-end IC substrates in Chongqing (China), Kulim (Malaysia) and Leoben (Austria) | **KEY.** Kulim expansion anchored by AMD and financed by customer commitments ([ad hoc, 13 Jun 2026](https://www.finanzwire.com/press-release/ats-austria-technologie-systemtechnik-ag-etr-aus-eqs-adhoc-ats-austria-technologie-systemtechnik-ag-ats-expands-ai-substrate-capacity-in-kulim-and-increases-outlook-for-202627-JHz5CRE5qDV)) |
| Shinko Electric Industries | Japan | Private (JIC-led SPC JICC-04; tender closed 18 Mar 2025) | Major FC-BGA maker | Brief. Planned stakes: JIC 80%, DNP 15%, Mitsui Chemicals 5%. No current financials are public ([DNP, 19 Mar 2025](https://www.global.dnp/en/news/detail/2025/03/0319_20176512/); [DIGITIMES, 21 Mar 2025](https://apps.digitimes.com/news/a20250321PD206.html?chid=12)) |
| Nan Ya PCB | Taiwan | TWSE 8046 | ABF/BT; Taiwan (Shulin, Jinxing) and Kunshan (China) | Brief. Conservative expansion of 5–10% a year; wins with US server-CPU and networking customers ([CTEE, 6 Nov 2026](https://www.ctee.com.tw/news/20261106700224-430502)) |
| Kinsus | Taiwan | TWSE 3189 | ABF (46.7% of Q3 revenue) and BT (38.3%) | Brief ([storm.mg](https://www.storm.mg/article/11165649)) |
| Zhen Ding Technology | Taiwan | TWSE 4958 | PCB major entering ABF | Brief. Named as one of Taiwan's "four ABF makers" ([Wantrich, 28 Oct 2026](https://wantrich.chinatimes.com/news/20261028900159-420101)); no ABF-specific data retrieved (gap). Group TTM: revenue NT$210.65bn, operating margin 9.9%, FCF −NT$43.0bn on NT$65.8bn capex (section 2.9) |
| LG Innotek | Korea | KRX 011070 | FC-BGA for PC processors; AI-accelerator FC-BGA targeted for 2027; glass pilot | Brief. Package solutions are only 7.6% of sales ([Korea Herald, 27 Oct 2026](https://www.koreaherald.com/article/10916657)) |
| Daeduck Electronics | Korea | KRX 353200 | FC-BGA and memory substrates | Brief. Third-party TTM: revenue KRW 1.35tn, operating margin 13.0%, ROIC 18.4%, net cash KRW 217bn (section 2.9). FC-BGA share of sales and AI customers not retrieved |
| Kyocera | Japan | TSE 6971 | Organic FC-BGA packages | Left out: no 2026 data retrieved (Japanese-language IR not reached) |
| Toppan Holdings | Japan | TSE 7911 | FC-BGA (Niigata; new Singapore plant); glass-core pilot line being commissioned | Brief, but notable. First overseas FC-BGA plant (Advanced Substrate Technologies, Singapore) opened 29 Sep 2026, backed by Singapore's EDB and **Broadcom**; operations from Dec 2026; large, high-layer FC-BGA for generative AI and network switches; FC-BGA capacity target ≥2.5x the FY2022 level by end FY2027 ([Toppan, 30 Sep 2026](https://www.holdings.toppan.com/en/news/2026/09/newsrelease260930_1.html); [IRZ, 4 Sep 2026](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)) |
| Dai Nippon Printing (DNP) | Japan | TSE 7912 | Glass-core pilot line started Dec 2025; 15% of the Shinko SPC | Brief ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)) |
| Shennan Circuits | China | SZSE 002916 | Leading Chinese FC-BGA maker (≤26 layers in volume, company claim) | Brief ([Sina, 23 Oct 2026](https://finance.sina.com.cn/stock/aigc/agcbld/2026-10-23/doc-iniwcnvh5019323.shtml)) |
| Shenzhen Fastprint | China | SZSE 002436 | FC-BGA (≤20 layers in volume); Zhuhai and Guangzhou | Brief; Q3 2026 data is a gap ([Eastmoney, Apr 2026](https://caifuhao.eastmoney.com/news/20260414014428571468720)) |
| Other mainland makers (e.g., Zhuhai ACCESS) | China | various / private | Embedded and FC substrates | Coverage thin: Chinese-language sources not searched before the budget ran out |

### B. Glass-core and glass-interposer developers and new entrants
| Company | Home | Listing / ticker | Role | Why it matters |
|---|---|---|---|---|
| Absolics (SKC subsidiary; Applied Materials reported minority holder, not re-verified) | US plant (Covington, GA); Korean parent | Parent SKC: KRX 011790; Absolics private | First dedicated glass-core plant (phase 1: 12,000 m² a year) | **KEY (as SKC).** Closest to volume, with repeated slips ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)) |
| Intel | US | Nasdaq INTC | Started the glass-core programme (2023); EMIB-on-glass demo Jan 2026; TGV memorandum with Lens Jul 2026 | Brief. Reportedly moving toward licensing, with its own deployment around 2030 (Tom's Hardware via [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)) |
| GlaSSEM JV (SEMCO 66.2% / Dongwoo Fine-Chem 33.8%, a unit of Sumitomo Chemical, TSE 4005) | Korea | Private JV | Glass-core supply for SEMCO | Covered under SEMCO ([Korea Herald, 2 Jul 2026](https://www.koreaherald.com/article/10796508)) |
| BOE | China | SZSE 000725 | Display maker with an RMB 993m panel-level glass-core pilot line | Brief. Display makers are entering ([XenoSpectrum, 29 Jul 2026](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/)) |
| TCL CSOT (TCL Technology SZSE 000100), Tianma (SZSE 000050) | China | listed | Early TGV R&D | Brief ([TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)) |
| Samsung Display (part of Samsung Electronics, KRX 005930) | Korea | listed parent | Reported dedicated TGV-interposer R&D team | Brief ([TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)) |
| Innolux | Taiwan | TWSE 3481 | Glass-based fan-out panel-level packaging with TGV (1H 2025 materials) | Brief ([XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/)) |
| JNTC | Korea | KOSDAQ 204270 | Semi-finished glass panels (10,000 a month, 2025); Vietnam line planned for 2027 | Brief ([MIT Technology Review, 13 Mar 2026](https://www.technologyreview.com/2026/03/13/1134230/future-ai-chips-could-be-built-on-glass/)) |
| Lens Technology | China | SZSE 300433 | TGV pilot lines; one-year Intel memorandum | Brief ([XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/)) |
| Crystal-Optech | China | SZSE 002273 | TGV optical-interconnect substrates for CPO; domestic supplier for Corning's Glass Bridge | Brief ([TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)) |
| WG Tech (via TGV Circuits) | China | SSE 603773 | Wuhan glass-based TGV multilayer line (100,000 m² a year planned) | Brief (same source) |
| 3D Glass Solutions (3DGS) | US; Indian unit Heterogenous Integration Packaging Solutions Pvt Ltd | Private | Embedded glass-substrate ATMP in Odisha, ₹1,943 crore (~US$233m) | India's only relevant player; production 2030 ([Business Standard, 19 Apr 2026](https://www.business-standard.com/industry/news/india-s-1st-advanced-3d-glass-chip-packaging-unit-to-come-up-in-bhubaneswar-126041900360_1.html)) |
| TSMC (CoPoS panel interposer) | Taiwan | TWSE 2330 | Panel-level interposer, 310×310 mm | Scope boundary: keeps interposer value in the foundry; glass "under review" ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)) |

### C. Glass makers
| Company | Home | Listing / ticker | Role | Why it matters |
|---|---|---|---|---|
| Corning | US | NYSE GLW | Glass carriers (515×510 and 600×600 mm); Glass Bridge for CPO; 3-year MoU with BOE (May 2026) | Raw-glass oligopoly member ([XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/); [DIGITIMES, 1 Oct 2026](https://www.digitimes.com/news/a20261001PD230/ai-chip-tsmc-corning-tgv-agc.html)) |
| AGC | Japan | TSE 5201 | Glass panels for packaging and interposers, 510×515 mm | Same oligopoly ([DIGITIMES](https://www.digitimes.com/news/a20261001PD230/ai-chip-tsmc-corning-tgv-agc.html)) |
| Nippon Electric Glass | Japan | TSE 5214 | Core-substrate and TGV glass roadmap on 510×515 mm | Same; no 2026 customer or financial data retrieved |
| Schott | Germany | Private (Carl Zeiss Foundation) | Specialty glass and TGV | Same |

### D. Equipment for glass vias
| Company | Home | Listing / ticker | Role | Why it matters |
|---|---|---|---|---|
| LPKF | Germany | Xetra LPK | LIDE laser-induced deep etching | Brief. No series order by H1 2026 ([LPKF H1 2026](https://www.lpkf.com/fileadmin/mediafiles/Half-yearly_Financial_Report_2026.pdf)) |
| Philoptics | Korea | KOSDAQ 161580 | TGV equipment | Left out: no 2026 data retrieved |
| Hymson Laser / DR Laser | China | SSE STAR 688559 / SZSE 300776 | Ultrafast-laser and wet-etch TGV tools; DR Laser panel-level TGV tools shipping in volume with export orders | Brief ([TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)) |

### E. Upstream materials
| Company | Home | Listing / ticker | Role | Why it matters |
|---|---|---|---|---|
| Ajinomoto | Japan | TSE 2802 | ABF build-up film (~95% share, secondary estimate) | **KEY** constraint holder ([AtlasPCB](https://www.atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026/)) |
| Nitto Boseki (Nittobo) | Japan | TSE 3110 | T-glass cloth (~90% share), NER-glass (60–70%) (TrendForce estimates) | **KEY** constraint holder ([MPBxChange, 15 Oct 2026](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)) |
| Resonac | Japan | TSE 4004 | Substrate core laminates and prepreg | Brief. Raised all laminate and prepreg prices ~30% from Mar 2026 (same source) |
| Mitsubishi Gas Chemical | Japan | TSE 4182 | BT resin and laminates | Brief. Thai BT-materials capacity doubled (Nov 2025) (same source) |
| Nan Ya Plastics | Taiwan | TWSE 1303 | Specialty glass-fabric weaving | Possible second source: plans to weave 20% of Nittobo's specialty fabric volume by 2027 (same source) |
| Kingboard Holdings / Kingboard Laminates | Hong Kong | HKEX 0148 / 1888 | Low-CTE and quartz yarn kilns; specialty AI fabric from 1H 2027 | Possible second source (same source) |
| Mitsui Kinzoku | Japan | TSE 5706 | HVLP/VSP copper foil | Brief (same source) |
| Taiwan Glass (TWSE 1802), Grace Fabric (TWSE 1815), Asahi Kasei (TSE 3407), Sekisui Chemical (TSE 4204), China Jushi (SSE 600176) | various | listed | Potential low-CTE cloth or build-up-film alternatives | Left out: no 2026 evidence on qualification retrieved (China Jushi expansion is mostly thick cloth) |

### F. Scope boundary (only where it changes who captures substrate value)
- **CoWoP (chip-on-wafer-on-PCB)** would remove the ABF substrate and shift value to high-end PCB makers. I found no 2026 confirmation of adoption ([GlobalSMT](https://www.globalsmt.net/advanced-packaging/nvidias-cowop-pcb-architecture-targets-abf-substrates-but-faces-warpage-risk/)).
- **TSMC CoPoS** (panel interposer) still sits on an organic substrate, so it keeps interposer value in the foundry rather than removing the substrate maker.

### Regional coverage notes
- **Israel:** no relevant ABF or glass-substrate player surfaced in any search. A dedicated MAYA/TASE check was not possible after the search budget ran out.
- **India:** 3DGS Odisha is the only relevant project found. I identified no Indian ABF maker.
- **China:** good for Shennan Circuits; thin for Fastprint, Zhuhai ACCESS and Chinese ABF-film substitutes.
- **Korea:** thin for Daeduck and Philoptics.
- **Japan:** thin for Kyocera, DNP and Shinko, because Japanese-language IR pages were not reached. Toppan is partly covered from its English newsroom.

---

## (2) Evidence on tests (a)–(e)

### 2.0 Segment-level evidence: supply-demand, qualification, pricing and upstream materials

#### Takeaway
High-end ABF substrates are in their tightest market since 2021:
- Lead times are 48–56 weeks against a 12-week norm.
- Makers are sold out and utilisation is above 90%.
- NVIDIA is pre-funding suppliers.

The shortage is most credible through 2027. 2028 is the swing year, because most new capacity (Ibiden Ono 3x, Unimicron KF, SEMCO Sejong/Busan/Vietnam, AT&S Kulim) lands in 2028–29. Materials sellers currently have the strongest pricing power: reported ABF film +30%, laminates +30%, T-glass booked out. The tightest single chokepoint for 2026–27 is T-glass cloth, not ABF film.

#### Cited findings: supply and demand
- **Lead times:** TrendForce tracker: ABF substrates 48–56 weeks vs a 12-week equilibrium (~4–4.7x), classed as "severe shortage"; GPUs 20–30 weeks, no shortage ([BigGo citing TrendForce, 16 Sep 2026](https://finance.biggo.com/news/02cf5c8f-c58d-45f8-a7a3-8fe37716bc8f)).
- **NVIDIA's plan:** "NVIDIA plans to increase substrate capacity for its products by 2.5x over the next three years." Agreements:
  - IBIDEN: a "multibillion-dollar capacity reservation advance"; Ono to reach 3x current capacity, ramping from Q1 2028.
  - Samsung Electro-Mechanics: "joining NVIDIA's substrate supply chain", with new factories in Sejong and Busan.
  - Unimicron: a capacity reservation agreement for its KF expansion; capacity from Q2 2027, full by mid-2028.
  - NVIDIA says more agreements are "underway".
  - Source: PRIMARY ([NVIDIA, 21 Oct 2026](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx)).
- **NVIDIA purchase commitments:** total supply and capacity commitments were US$279bn at 26 Jul 2026, up from US$119bn a quarter earlier. Some agreements can be cancelled or rescheduled at a cost (NVIDIA 10-Q via [RCRTech, 23 Oct 2026](https://rcrtech.com/semiconductor-news/nvidia-supply-chain-capacity-commitments/)).
- **Ibiden's demand view** (company claim, unconfirmed), from its results deck ([Ibiden, 30 Oct 2026](https://www.ibiden.com/ir/items/en_kessannsetsumei2026Q2.pdf)):
  - SAP substrate demand index (CY26 = 100): CY27 135, CY28 170, CY29 210, CY30 350.
  - AI GPU/ASIC from CY26 to CY30: unit market ×1.8, production load ×3.0, SAP demand ×5.4.
  - Quote: "total SAP demand is expected to significantly exceed the industry's supply capacity."
- **Ibiden's management view** (Q&A, 30 Oct 2026; PRIMARY, company claim) ([Ibiden Q&A](https://www.ibiden.com/ir/items/en_QA_FY2026Q2.pdf)):
  - "In the high-end-AI-related market, there will be a change in the competitive landscape with the addition of a Korean manufacturer, bringing the total number of suppliers to three. However, even the combined capacity of our competitors will not be sufficient to meet overall demand."
  - In server CPUs, competitors are expanding, "including through acquisitions of existing plants", but combined capacity is "still insufficient".
  - Ibiden accepted a questioner's premise that the shortage persists "until around 2030": "there is currently no technology that can replace leading-edge IC package substrates. As a result, we believe demand will ultimately have to be constrained."
  - New substrate buildings take "at least four years from the investment decision", which bounds how fast supply can respond.
- **Shortage duration:** BofA expects the ABF shortage to last through 2028 (secondary) ([thebuildout.ai, 26 Mar 2026](https://thebuildout.ai/intel/229c44f2-da57-4f46-b5fa-e5d03702236c)). Unimicron's chairman (TPCA Show, 20 Oct 2026) named T-glass cloth, CCL and ABF as the main material bottlenecks and said some critical materials could be about 20% short in 2027 ([MPBxChange](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)).
- **Size of the gap (low reliability):** one blog compilation puts the shortfall at ~10% in 2H 2026, ~21% in 2027 and >40% in 2028 ([gate.com](https://www.gate.com/blog/why-abf-substrates-have-become-a-bottleneck-in-the-ai-gpu-supply-chain-2028-shortage-analysis)). Methodology unknown.
- **Utilisation:**
  - Unimicron: ABF utilisation >90%; ABF was 52% of Q2 2026 revenue ([BigGo, Unimicron call 29 Jul 2026](https://finance.biggo.com/quote/3037.TW/earnings-call/TW_3037.TW_2026-07-29)).
  - Nan Ya PCB: Shulin and Jinxing near full; Kunshan ramping toward full in Q4 2026 ([CTEE, 6 Nov 2026](https://www.ctee.com.tw/news/20261106700224-430502)).
  - SEMCO: Q4 FC-BGA supply "tight" ([Investing.com transcript, 28 Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).

#### Cited findings: capacity landing 2027–2029
- **Ibiden** ([Ibiden deck, 30 Oct 2026](https://www.ibiden.com/ir/items/en_kessannsetsumei2026Q2.pdf)):
  - Ono Cell8 (AI GPU): JPY 280bn, operations from FY2027 (Apr 2027–Mar 2028).
  - Gama Cell6: JPY 220bn already announced plus ~JPY 151bn added. The capex notice of 29 Oct 2026 says the new money goes to "Gama Plant and other overseas plant", for CPU substrates, mass production from FY2029 ([notice](https://www.ibiden.com/ir/items/koteishisansyutoku2026Q2.pdf)). The Q&A says ramp-up is 2H FY2029, the investment is for EMIB (not EMIB-T), and it is outside the FY2030 targets ([Q&A](https://www.ibiden.com/ir/items/en_QA_FY2026Q2.pdf)).
  - Cell7 and Cell9 decisions due within FY2026.
  - EMIB-T mass production 2H FY2027 (Oct 2027–Mar 2028), "no significant change" to schedule.
- **Unimicron** ([vocus.cc](https://vocus.cc/article/6ae2b2b0fd8978000150ef3d)):
  - Guangfu Plant 1 Phase 3 from Q3 2026.
  - Guangfu Plant 2 Phase 1 from Q2 2027.
  - Yangmei Plant 2 for 2027–28 demand.
- **SEMCO:** KRW 6.8tn package-substrate investment (Sejong, Busan, Vietnam), production phased from 2027, meaningful revenue from 2028 ([Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).
- **AT&S:** Kulim 1 and 2 in capacity build through 2027/28, high-volume manufacturing in 2028/29; Chongqing high-volume manufacturing in 2027/28 ([Investing.com, 4 Aug 2026](https://www.investing.com/news/company-news/ats-q1-202627-slides-ai-demand-drives-40-revenue-surge-93CH-4834617)).
- **Toppan:** Singapore plant starts Dec 2026; FC-BGA capacity ≥2.5x the FY2022 level by end FY2027 ([Toppan](https://www.holdings.toppan.com/en/news/2026/09/newsrelease260930_1.html)).
- **Nan Ya PCB:** ABF capacity +5–10% a year over the next two years ([CTEE](https://www.ctee.com.tw/news/20261106700224-430502)).

#### Cited findings: qualification and shares
- **NVIDIA:** Ibiden, Unimicron and SEMCO are named by NVIDIA itself (PRIMARY, customer-confirmed) ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx)).
- **Broadcom:** Toppan's new Singapore FC-BGA plant (operations Dec 2026; large, high-layer substrates for generative AI and network switches) is "backed by" Singapore's EDB and Broadcom. This is a supplier-side primary statement implying Broadcom sourcing from Toppan ([Toppan, 30 Sep 2026](https://www.holdings.toppan.com/en/news/2026/09/newsrelease260930_1.html)). Broadcom's own confirmation was not found.
- **AMD:** named by AT&S in a regulated ad hoc announcement ([13 Jun 2026](https://www.finanzwire.com/press-release/ats-austria-technologie-systemtechnik-ag-etr-aus-eqs-adhoc-ats-austria-technologie-systemtechnik-ag-ats-expands-ai-substrate-capacity-in-kulim-and-increases-outlook-for-202627-JHz5CRE5qDV)). I did not find AMD's own confirmation.
- **Unnamed US customers:**
  - Nan Ya PCB: a major US chip company adopts its ABF for a next-generation server CPU from Q1 2027; a US networking customer is in mass production at Kunshan ([CTEE](https://www.ctee.com.tw/news/20261106700224-430502)).
  - SEMCO: long-term agreements with a "leading North American big tech" customer ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).
- **Glass:**
  - SEMCO glass qualification work with Broadcom "reported" ([vlsi.kr, 20 Oct 2026](https://www.vlsi.kr/en/glass-core-substrate-race-en/)).
  - Absolics qualification with AMD and AWS "reportedly", per industry press ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)). Both unconfirmed.
- **Shares:**
  - BofA: Ibiden 70–80% of GPU substrates (secondary).
  - Low-reliability blogs: Unimicron ~22% of global ABF, >70% of ASIC substrates, ~30% of NVIDIA AI substrate volume ([Encyclopedia of Stocks](https://encyclopediaofstocks.substack.com/p/abf-substrate-market-ai-driven-super)).
  - I found **no reliable public evidence** of supplier shares at Google, Amazon, Broadcom, Marvell or MediaTek. The only supplier link found for Broadcom is Toppan's Broadcom-backed Singapore plant (above).

#### Cited findings: pricing
- **Substrates:**
  - Counterpoint expected substrate makers to raise prices 3–5% a quarter in 1H 2026 ([MPBxChange](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)).
  - Unimicron's July call cited price increases behind Q3 margin gains ([BigGo](https://finance.biggo.com/quote/3037.TW/earnings-call/TW_3037.TW_2026-07-29)). Analysts expect further high-end ABF increases in Q4 2026–Q1 2027 ([vocus.cc](https://vocus.cc/article/6ae2b2b0fd8978000150ef3d)).
  - SEMCO is "in price talks" ([transcript](https://investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).
- **Inputs:**
  - Ajinomoto ABF film: up to +30% from Q3 2026 (secondary; not quantified in Ajinomoto's deck) ([AtlasPCB](https://www.atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026/)).
  - Resonac: all laminates and prepreg about +30% from Mar 2026 (Resonac notice, 16 Jan 2026, via [MPBxChange](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)).
  - Copper (LME): US$14,114/t average in Q3 2026, +44% YoY (World Bank, via MPBxChange).
  - Nittobo: T-glass price rises "largely completed"; no further hikes planned ([TrendForce, 6 Aug 2026](https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/)).

#### Cited findings: upstream constraints
- **T-glass cloth:**
  - Nittobo holds ~90% of T-glass and 60–70% of NER-glass. TrendForce sees no new capacity before mid-2027.
  - Nittobo's Fukushima building (~JPY 15bn) starts production Jan–Mar 2027.
  - Thin-cloth easing is expected 2H 2027–2028 ([MPBxChange](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)).
  - Nittobo targets 3x FY3/2026 capacity by FY3/2029 and 2x its Taiwan capacity (vs 2025) by Mar 2028 ([TrendForce, 6 Aug 2026](https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/)).
  - NVIDIA, Microsoft, Google and Amazon have booked most of Nittobo's premium cloth for 2026 (Nikkei, via TrendForce).
- **ABF film:** Ajinomoto says that "throughout the supply chain, too, including coating companies, we have secured a supply capacity capable of fully meeting current demand" (company claim, unconfirmed). Its new varnish plant starts mass production in FY2030 ([Ajinomoto Q2 deck, 9 Nov 2026](https://www.ajinomoto.co.jp/company/en/ir/event/presentation/main/011111116/teaserItems1/01/linkList/03/link/FY26Q2_Presentation_E_with%20Script.pdf)).
- **Laminates and resin:** MGC doubled Thai BT-materials capacity (Nov 2025). A Daeduck executive said epoxy-resin waits rose from 3 to 15 weeks ([MPBxChange](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)).

#### Inferences
- **The shortage holds through 2027.** Lead times, sold-out utilisation and customer pre-funding are all independent signals.
- **2028–29 is the risk window.** Most incremental capacity starts then: Ibiden Ono ramps Q1 2028, Unimicron KF is full by mid-2028, SEMCO's meaningful revenue starts 2028, AT&S Kulim reaches high-volume manufacturing in 2028/29, and Ibiden Gama follows in FY2029.
  - In the steady scenario, NVIDIA's 2.5x plan and Ibiden's demand index (+70% CY26→CY28) roughly absorb it.
  - In the 2028 financing-pause scenario, the industry would repeat 2022–23: capacity arriving into a demand air-pocket.
- **The binding chokepoint for 2026–27 is upstream:** T-glass cloth (single supplier, booked by hyperscalers) and thin glass cloth. ABF film is less tight: Ajinomoto claims sufficient capacity but is extracting price.
- **Margins are expanding even though substrate price rises (3–5% a quarter) trail input rises (≈30%).** Mix (more layers, larger bodies) and utilisation are doing most of the work.

#### Gaps
- Prismark and Yole share tables (paywalled, not retrieved).
- Google, Amazon, Marvell and MediaTek substrate suppliers. For Broadcom, only the Toppan link was found.
- A Morgan Stanley 2030 gap revision (15%→22%) appeared only in search summaries; the original was not traced.
- Inventory levels at makers.

### 2.1 Ibiden (TSE 4062) — key company

#### (a) Position
- **Constraint held:** a physical constraint — scarce SAP capacity and process know-how for the largest, highest-layer substrates. Its roadmap runs from CY26 (90×90 mm, 10-X-10) to CY28 (110×110 mm, 12-X-12) and CY30+ (>130×130 mm, 14-X-14) ([Ibiden deck](https://www.ibiden.com/ir/items/en_kessannsetsumei2026Q2.pdf)). It owns no "judge".
- **Main product:** ABF FC-BGA for AI GPUs, ASICs and CPUs = **BRIDGE**. Named successors are glass core and panel/CoWoP.
- **Successor due date:**
  - Glass core: mainstream "after 2030" per TrendForce ([7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)).
  - Intel's own glass deployment: around 2030 ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
- **Slips:** recorded for the successors. Absolics went from 2024 to 2027+. Intel went from "second half of this decade" to around 2030.
- **No glass item on Ibiden's own CY25–CY30+ roadmap slide.** The slide shows interposer, silicon bridge, "power enhancement" and optical-electrical conversion. One source says Ibiden is "investing in glass" with no dates ([vlsi.kr](https://www.vlsi.kr/en/glass-core-substrate-race-en/), unverified).
- **EMIB-T:** BofA says Ibiden will start EMIB-T substrate production by FY3/28 (secondary) ([thebuildout.ai](https://thebuildout.ai/intel/229c44f2-da57-4f46-b5fa-e5d03702236c)).

#### (b) Lead
- NVIDIA's public, customer-side confirmation of a multibillion-dollar capacity reservation advance (PRIMARY) ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx)).
- BofA: 70–80% GPU-substrate share (secondary).
- Electronics operating margin of ~29% in H1 FY2026 (my arithmetic: 50.0/172.5) vs Unimicron's company-level 20.0% in Q3 2026. That is consistent with a yield or pricing lead (inference).

#### (c) Revenue model
- Hardware components sold per unit. Volume scales with accelerator units × substrate area × layer count.
- Customer-funded capacity:
  - NVIDIA advance: amount undisclosed. Bunshun reported ~JPY 280bn; neither company confirmed. Ibiden's balance sheet shows advances received rising JPY 118.8bn in Apr–Sep 2026 to JPY 199.7bn (PRIMARY tanshin), which is the observable footprint of customer prepayments.
  - Ibiden's CEO reportedly said a "substantial portion" of a JPY 500bn three-year capex plan is funded by customer prepayments (secondary) ([RCRTech](https://rcrtech.com/semiconductor-news/nvidia-supply-chain-capacity-commitments/)).
- No service or labour-hour revenue.

#### (d) Financial strength
Source for results and forecasts: PRIMARY deck dated 30 Oct 2026 ([Ibiden](https://www.ibiden.com/ir/items/en_kessannsetsumei2026Q2.pdf)).

| Item | Figure |
|---|---|
| H1 FY2026 (Apr–Sep 2026) sales | JPY 262.5bn (+34% YoY) |
| H1 FY2026 operating profit | JPY 60.1bn (+85%), margin 22.9% |
| H1 FY2026 net profit | JPY 38.6bn (+75%) |
| H1 Electronics | Sales JPY 172.5bn (+52%); OP JPY 50.0bn (+97%) |
| H2 FY2026 forecast (my arithmetic, approximates Q3+Q4) | Sales JPY 302.5bn; OP JPY 72.9bn (24.1%) |
| FY2026 forecast (raised 29 Oct) | Sales JPY 565.0bn (+36%); OP JPY 133.0bn (+114%, 23.5%); NP JPY 89.0bn |
| FY2026 forecast, Electronics | Sales JPY 385.0bn (+58%); OP JPY 114.0bn (+152%) |
| FY2025 actual (Apr 2025–Mar 2026) | Sales JPY 416.2bn; OP JPY 62.0bn (14.9%); NP JPY 63.7bn, incl. JPY 34.5bn after-tax gains on policy-share sales |
| Mid-term targets (company claim) | FY2027 sales JPY 650bn, OP JPY 165bn (raised by JPY 15bn); FY2030 sales >JPY 1tn, OP >JPY 300bn (30% margin) |
| Capex | FY25 JPY 64.3bn → FY26 JPY 210bn → FY27 JPY 350bn → FY28 higher still |
| Depreciation | FY25 66.2 → FY26 81.0 → FY27 90.0 (JPY bn) |
| Electronics EBITDA margin | FY25 39.9% → FY26F 47.6% → FY27F 48.3% |

Points to note:
- **Capex vs cash generation** (my arithmetic):
  - FY2026: capex JPY 210bn ≈ forecast EBITDA (133 + 81 = 214), so free cash flow is roughly zero before prepayments.
  - FY2027: capex JPY 350bn vs EBITDA ≈ 255, so free cash flow is negative unless customers prepay.
- **Balance sheet at 30 Sep 2026** (PRIMARY tanshin, 29 Oct 2026) ([tanshin](https://www.ibiden.com/ir/library/statement/items/tannshinn2026Q2.pdf); [supplementary data](https://www.ibiden.com/ir/items/hosokushiryou2026Q2.pdf)):
  - Cash and deposits JPY 420.5bn (31 Mar 2026: 295.7bn).
  - Interest-bearing debt JPY 162.0bn (my sum: bonds 10.0 current + 35.0; convertible bonds 56.0; long-term loans 61.0), down from JPY 192.5bn. That gives **net cash of about JPY 258bn** (my arithmetic; about JPY 103bn at Mar 2026).
  - **Advances received JPY 199.7bn**, up JPY 118.8bn in six months from JPY 81.0bn. These are customer prepayments, consistent with the NVIDIA capacity-reservation advance.
  - H1 operating cash flow JPY 193.2bn, including the +JPY 118.8bn of advances; investing −JPY 48.9bn; financing −JPY 18.3bn.
  - Equity ratio 53.5% (57.3% at Mar 2026). H1 capex was only JPY 43.4bn against the JPY 210bn full-year plan, so spending is heavily back-loaded.
- **Returns history** ([Integrated Report 2025](https://www.ibiden.com/ir/items/IntegratedReport2025_en.pdf)):
  - FY2024 (Mar 2025): interest-bearing debt JPY 343.0bn; equity ratio 45.35%; ROE 6.84% (FY2022: 13.32%; target ≥10%); FCF −JPY 45.3bn (FY2023: +68.0bn). R&I single-A.
  - Third-party TTM to Sep 2026: ROE 14.1%, ROIC 15.7%, operating margin 17.8%, FCF +JPY 168bn (flattered by advances) ([stockanalysis.com, fetched 12 Nov 2026](https://stockanalysis.com/quote/tyo/4062/statistics/)).
  - Company targets: Electronics operating margin "approximately 35% in FY2030"; Gama additions at ">30%" margin ([Q&A](https://www.ibiden.com/ir/items/en_QA_FY2026Q2.pdf)).
- **Customer concentration:** not disclosed. NVIDIA dependence is implied by the GPU share and the NVIDIA-funded plant (inference).
- **Country exposure:** 71% of FY2024 sales were overseas — Asia 47.1%, North and Central America 12.8%, Europe 7.3%. Substrate output comes from Japan (Ogaki, Ono, Gama, Aoyanagi) plus the Philippines and Malaysia (Integrated Report 2025).

#### (e) Resilience
- **Steady growth (55%):** forecasts imply about 4x operating profit between FY2025 and FY2027.
- **Financing-led pause around 2028 (25%):** this is the main risk. Ono Cell8 ramps from Q1 2028 and Gama Cell6 from FY2029, so new depreciation lands in a downturn.
  - Ibiden has done this before: a 2007 facility and a 2021 Intel-oriented facility ran near-idle (RCRTech, secondary).
  - FY2024 ROE of 6.8% shows how quickly returns compress.
  - The NVIDIA advance and prepayments are the mitigant.
- **Acceleration (20%):** Ibiden is capacity-bound. Cell7 and Cell9 are options awaiting customer terms.
- **Cycle position:** peak tightness — sold out, 48–56-week lead times, capex tripling.
- **Cross-border:**
  - Production is mostly in Japan, with no China fab listed, so low exposure to China export controls.
  - Demand is exposed to US limits on NVIDIA's China sales.
  - Tariff impact was not quantified in sources (gap).

### 2.2 Unimicron (TWSE 3037) — key company

#### (a) Position
- **Constraint held:** a physical constraint (SAP capacity and know-how).
- **Main product:** ABF = **BRIDGE**. Glass: "investing, no dates" ([vlsi.kr](https://www.vlsi.kr/en/glass-core-substrate-race-en/), unverified).

#### (b) Lead
- NVIDIA capacity reservation (PRIMARY).
- ABF utilisation >90%.
- BofA notes "a high mix of long-term agreements" (secondary) ([thebuildout.ai](https://thebuildout.ai/intel/229c44f2-da57-4f46-b5fa-e5d03702236c)).
- Share estimates are low-reliability.

#### (c) Revenue model
- Per-unit hardware: substrates ~68% of Q3 revenue, HDI 22%, PCB 8%, FPC 2%.
- AI products >60% of 1H 2026 revenue, heading to ~70% in 2H (press) ([China Times, 28 Oct 2026](https://www.chinatimes.com/realtimenews/20261028001621-260410)).
- Capacity reservation with NVIDIA.

#### (d) Financial strength
Q3 2026 results were published 27–28 Oct 2026 ([vocus.cc](https://vocus.cc/article/6ae2b2b0fd8978000150ef3d); [cnyes](https://news.cnyes.com/news/id/6638686)).

| Item | Figure |
|---|---|
| Q3 2026 revenue | NT$52.65bn (record; +22.8% QoQ, +54.9% YoY) |
| Q3 gross margin | 28.8% (Q2 24.8%; Q3 2025 ~13.4%), held back by a one-off employee-compensation adjustment |
| Q3 operating profit | NT$10.53bn (20.0% margin) |
| Q3 net profit | NT$10.05bn; EPS NT$6.15, 6.32 or 6.36 depending on source (conflict) |
| 9M 2026 | Revenue NT$132.99bn; GM 24.48%; net profit NT$28.21bn |
| FY2025 operating profit | Only ~NT$6.67bn — a deep 2024–25 trough |
| 2026 capex | Raised to ~NT$53.7bn |
| Long-lead equipment commitments | Cumulative ~NT$82.5bn |
| Cash (end Q3 2026) | ~NT$160.4bn |
| 9M operating cash flow | ~NT$25.1bn, below net profit |
| 9M net financing inflow | ~NT$94.9bn — the expansion is partly financed |

- **Third-party TTM to Sep 2026** ([stockanalysis.com, fetched 12 Nov 2026](https://stockanalysis.com/quote/tpe/3037/statistics/)):
  - Total debt NT$50.0bn vs cash NT$159.7bn, so net cash ~NT$109.7bn.
  - Revenue NT$167.7bn; operating margin 13.3%; operating cash flow NT$29.1bn; capex NT$25.4bn; FCF NT$3.8bn.
  - ROE 23.6%, inflated by Q2 non-operating gains. The site's ROIC of 23.9% sits oddly against its ROCE of 7.3%, so treat site-computed returns with caution.
- Customer concentration not disclosed.
- Footprint: Taiwan ABF plants (Guangfu, Yangmei); selling Unimicron Japan to Meiko (intent stage).

#### (e) Resilience
- **Operating leverage is very high:** gross margin moved about +15 points in a year. The reverse in a pause would be severe; FY2025 operating profit was only ~NT$6.7bn.
- **Pause scenario:** a large committed equipment pipeline that is partly debt- or equity-funded. The NVIDIA reservation covers only the KF expansion.
- **Cross-border:** Taiwan concentration (geopolitical); tariffs not quantified (gap).

### 2.3 Samsung Electro-Mechanics (KRX 009150) — key company

#### (a) Position
- **Constraint held:** a physical constraint (capacity) plus embedded-passive integration. Company claim, unconfirmed: it is "the only supplier able to offer passive components and FC-BGA substrates with those components embedded" ([search summary of call coverage](https://finance.yahoo.com/markets/stocks/articles/samsung-electro-mechanics-co-ltd-170335707.html)).
- **ABF FC-BGA = BRIDGE.** Embedded and multi-core server-CPU substrates are already in mass production, with Q4 2026 supply doubling.
- **Glass core = SUCCESSOR.**
  - GlaSSEM JV full-scale operation 2H 2027 ([Korea Herald, 2 Jul 2026](https://www.koreaherald.com/article/10796508)).
  - Company target "full operation in 2028" (company claim) ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).
- **Silicon capacitors:** mass production 2027, backed by a KRW 1.5tn supply contract disclosed in May 2026.

#### (b) Lead
- **NVIDIA:** onboarding confirmed by NVIDIA (PRIMARY).
- **NVIDIA agreement:** a multi-year supply agreement covering compute-chipset and network-switch substrates, with deliveries from 2026 and double-digit annual volume growth. By 2028 NVIDIA will be "a significant portion" of SEMCO's package-substrate capacity ([SEMCO release, 21 Oct 2026](https://m.samsungsem.com/global/newsroom/news/view.do?id=10614)).
- **Glass:** glass moved into a dedicated business unit in Feb 2026. A Korean outlet rated SEMCO's glass maturity 40/100 ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)). Broadcom glass work is "reported" only.

#### (c) Revenue model
- Per-unit hardware.
- Long-term agreements: with a North American big-tech customer for FC-BGA, and in MLCCs (>50–60% of 2027 MLCC revenue). Co-investment with NVIDIA for dedicated ABF lines (amount undisclosed) ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).

#### (d) Financial strength
Q3 2026, published 28 Oct 2026 ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482); [Herald Business](https://biz.heraldcorp.com/article/10917700)).

| Item | Figure |
|---|---|
| Q3 2026 revenue | KRW 3,763.3bn (+30% YoY) |
| Q3 operating profit | KRW 691bn (18.4% margin, my arithmetic) |
| Q3 net profit | KRW 468.7bn |
| Package Solution revenue | KRW 938–939bn (+58% YoY from 593.2bn; ~25% of group); division profit not disclosed |
| MLCC (components) revenue | KRW 1,883bn (+36%) |
| Liabilities/equity | 63% |
| Debt/equity | 33% |
| 2026 capex | Above plan |
| Package-substrate investment | KRW 6.8tn (Sept 2026 disclosure) |
| Vietnam subsidiary investment | KRW 2.5tn approved (reported in call coverage; not opened directly) |

- **Third-party TTM** (possibly only to Jun 2026) ([stockanalysis.com](https://stockanalysis.com/quote/krx/009150/statistics/)): revenue KRW 12.46tn; operating margin 9.8%; net cash ~KRW 241bn; operating cash flow KRW 1.88tn; capex KRW 1.59tn; FCF KRW 286bn; ROE 10.6%; ROIC 9.8%. These are group-level returns; the substrate division's returns are not disclosed.
- Customer concentration is not disclosed and will rise toward NVIDIA by 2028 (PRIMARY).
- Footprint: Korea (Sejong, Busan) and Vietnam for substrates; Philippines for MLCC.

#### (e) Resilience
- **Diversification is the strongest buffer among the key substrate makers:** MLCC is about 50% of revenue (with >40% share of AI-server MLCC), optics about 25%.
- **Pause scenario:** the KRW 6.8tn programme lands 2027–28. Group cash flow carries it more easily than single-product peers.
- **Cross-border:** Vietnam and Korea production; US tariff and export-control exposure not quantified (gap).

### 2.4 AT&S (Vienna: ATS) — key company

#### (a) Position
- **Constraint held:** a physical constraint — capacity outside Taiwan and Japan (Kulim, Malaysia; Leoben, Austria), plus embedded-core technology ("EMB Core", MTH, MLC).
- **Main product:** ABF IC substrates = **BRIDGE**.
- **Glass core is R&D only.** The Q1 2026/27 material does not mention glass; its roadmap covers co-packaged optics and power PCBs ([Investing.com, 4 Aug 2026](https://www.investing.com/news/company-news/ats-q1-202627-slides-ai-demand-drives-40-revenue-surge-93CH-4834617)). The FY2025/26 annual report, however, says "the research focus was on glass-based substrate cores… the international supply chain for glass cores has not yet been established in the required quality, making additional development steps necessary. AT&S is working on closing this gap early" (PRIMARY) ([AT&S Annual Financial Report 2025/26](https://ats.net/en/download/annual-financial-report-2025-26/?wpdmdl=61790)). There is no product date.
- **Own cores:** Kulim will also get "a new production facility for precursors for IC substrates (cores)" ([AT&S H1 report 2026/27](https://ats.net/en/download/half-year-financial-report-2026-27/?wpdmdl=67668)).

#### (b) Lead
- Regulated ad hoc of 13 Jun 2026: agreements on key terms with "AMD and another leading technology company" ([finanzwire](https://www.finanzwire.com/press-release/ats-austria-technologie-systemtechnik-ag-etr-aus-eqs-adhoc-ats-austria-technologie-systemtechnik-ag-ats-expands-ai-substrate-capacity-in-kulim-and-increases-outlook-for-202627-JHz5CRE5qDV)).
- Microelectronics EBITDA margin 42.3% in Q1 2026/27.
- "All major customers now generate revenue in the three-digit million euro range" ([Investing.com](https://www.investing.com/news/company-news/ats-q1-202627-slides-ai-demand-drives-40-revenue-surge-93CH-4834617)).

#### (c) Revenue model
- Per-unit hardware.
- The Kulim expansion (EUR 1.5–2.0bn) was "fully supported and financed by long-term customer commitments, which remain subject to final negotiation and execution" (ad hoc, Jun 2026). By the H1 report: "All planned investments are supported and financed by long-term customer commitments."
- **Prepayments are visible on the balance sheet** (PRIMARY, 30 Sep 2026) ([H1 report](https://ats.net/en/download/half-year-financial-report-2026-27/?wpdmdl=67668)):
  - Contract liabilities EUR 1,205.9m in total (non-current 1,038.5m; current 167.4m), up from EUR 885.9m at Mar 2026.
  - Additions of EUR 421.0m and releases of EUR 106.9m in H1.
  - Receivables from customer prepayments EUR 211.0m.
- Receivables factoring is being reduced: EUR 74.6m vs 206.5m.

#### (d) Financial strength

| Period | Revenue | EBITDA | Other |
|---|---|---|---|
| Q1 2026/27 (Apr–Jun 2026) | EUR 549m (+40% cc) | EUR 165m (30.1%) | Microelectronics EUR 344m (+93% cc) |
| Q2 2026/27 (Jul–Sep 2026) | EUR 681.9m (+52.4% cc) | EUR 244.0m (35.8%) | EBIT EUR 153.0m; net result EUR 125.4m |
| H1 2026/27 | EUR 1,230.6m (+45.4%; cc +46%) | EUR 409.0m (33.2%) | EBIT EUR 226.4m; profit EUR 166.2m; ROCE 17.7% |

- **Cash flow (H1):** operating cash flow EUR 100.4m (vs 209.4m) as working capital and safety inventories rose. Operating FCF was −EUR 11.0m per the press article (the report itself says −EUR 10.6m), or about EUR 120m at the prior-year factoring level ([ad-hoc-news, 12 Nov 2026](https://www.ad-hoc-news.de/boerse/news/corporate-news/at-und-s-stock-record-quarter-lifts-earnings-as-full-year-outlook-holds/70496565)).
- **H1 2026/27 per the report itself** (PRIMARY, 5 Nov 2026) ([H1 report](https://ats.net/en/download/half-year-financial-report-2026-27/?wpdmdl=67668)):
  - EBIT EUR 226.4m (18.4%); profit EUR 166.2m; ROCE 17.7% (H1 2025/26: 0.3%).
  - Net capex −EUR 111.0m; FCF from operations −EUR 10.6m (prior year +125.1m).
  - Inventories rose from EUR 234.9m to 339.5m.
- **Balance sheet at 30 Sep 2026** (same report):
  - Net debt EUR 1,333.0m (31 Mar 2026: 1,332.1m). This includes the EUR 350m 2021/22 hybrid, reclassified to current liabilities before its 22 Oct 2026 redemption.
  - Net debt/EBITDA 2.0 years; net gearing 100.3% (126.7% at Mar 2026).
  - Equity ratio 23.9% (25.5% pro forma for the redemption).
  - Liquidity: cash EUR 826.8m, plus financial assets EUR 133.0m and unused credit lines EUR 91.4m.
  - Other financial commitments EUR 758.0m for Kulim, Chongqing and Leoben (EUR 234.4m at Mar 2026).
  - A new EUR 400m hybrid convertible was issued in June 2026.
  - The Q1 figure of EUR 954m net debt reported by Investing.com is not comparable and is superseded.
- **FY2026/27 guidance** (raised 13 Jun, confirmed 5 Nov): cc revenue +45–55%, EBITDA margin 32–37%, capex EUR 1.0–1.2bn.
- **FY2025/26 (Apr 2025–Mar 2026)** (PRIMARY annual financial report) ([AFR 2025/26](https://ats.net/en/download/annual-financial-report-2025-26/?wpdmdl=61790)):
  - Revenue EUR 1,790.8m (+12.7%; cc +20.5%).
  - EBITDA EUR 418.0m (prior year EUR 605.7m included a plant-sale gain).
  - 90.3% of revenue is invoiced in foreign currency, mainly USD.
- **Customer concentration** (AFR 2025/26): "76.5% of total revenue (previous year: 71.3%) is attributable to the five largest customers… where the range is between 3% and 31%". The largest customer is therefore ~31% of revenue.
- **Revenue by customer headquarters:**
  - FY2025/26: Americas EUR 1,453.6m (81%), Germany 158.9m, other Asia 94.3m, China 10.6m.
  - H1 2026/27: Americas EUR 1,014.9m of 1,230.6m (82.5%), Germany 89.8m, Japan 34.6m, China 33.1m.
- **Footprint:** PP&E at 30 Sep 2026 — China EUR 1,236.4m, Malaysia EUR 1,232.7m, Austria EUR 724.9m. Plants: Chongqing (China), Kulim (Malaysia), Leoben (Austria).
- **Third-party TTM to Sep 2026:** ROE 18.5%, ROIC 11.8% ([stockanalysis.com](https://stockanalysis.com/quote/vie/ATS/statistics/)).

#### (e) Resilience
- The thinnest balance sheet of the key substrate makers, with the most concentrated customer base: top five = 76.5% of revenue, largest ~31%, and 81–83% of revenue from Americas-headquartered customers.
- Kulim reaches high-volume manufacturing in 2028/29, exactly when the pause scenario would hit. Prepayments (EUR 1.2bn contract liabilities) cushion that risk; AT&S itself flags possible "significant impairment charges".
- Materials: "the global shortage of glass cloth is a critical factor for AT&S… Several supplier qualifications were carried out in the past eighteen months". Some chemicals and composites come from "individual suppliers specified by the customer" (AFR 2025/26).
- Guidance assumes "no significant deterioration in geopolitical conditions or in the tight supply of certain materials".
- China (Chongqing) production for US customers carries export-control and tariff exposure. Kulim diversifies this.

### 2.5 SKC / Absolics (SKC: KRX 011790) — key company (successor-side)

#### (a) Position
- **Main product:** glass-core substrate = **SUCCESSOR**. Not a judge, and not yet a constraint because it is not qualified.
- **Dates, history:** commercialisation June 2024 → mass production 2025 → "certification complete 2026" → filing says it is "difficult to predict a specific mass-production schedule at present" (SBS Biz citing SKC filing, [29 May 2026](https://v.daum.net/v/20260529115214214)).
- **Latest analyst view:** TrendForce (Jul 2026) puts volume in 2027, with final validation by year-end ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
- **Q3 2026 commentary:** embedded product in "reliability testing and yield improvement"; a non-embedded "Plan B" product (added May 2026) under development, with customer proof-of-concept talks. **No date given** ([fnnews, 28 Oct 2026](https://www.fnnews.com/news/202610281435277261)).

#### (b) Lead
- First dedicated glass-core plant: US$600m; phase 1 of 12,000 m² a year, about 2–3m H100-size packages (Georgia Tech estimate) ([MIT Technology Review](https://www.technologyreview.com/2026/03/13/1134230/future-ai-chips-could-be-built-on-glass/)).
- Mass-production samples came off the line in Q1 2026. Embedded samples were sent to Taiwan for package-level reliability evaluation (The Elec, 27 Jul 2026, via [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
- No named customer supply agreement ([Slicast, 9 Sep 2026](https://slicast.com/commentary/intel-2026-09-09) — low-reliability site; consistent with IRZ).

#### (c) Revenue model
- No material revenue yet; future per-unit sales.

#### (d) Financial strength
- **SKC Q3 2026:** revenue KRW 638.9bn (+26%); operating loss KRW 49.6bn; net loss KRW 128.5bn ([ZDNet Korea](https://zdnet.co.kr/view/?no=20261028133954); [fnnews](https://www.fnnews.com/news/202610281435277261)).
- **Segments:**
  - Semiconductor materials: revenue KRW 71.8bn, OP KRW 21.8bn.
  - Copper foil: operating loss KRW 54.4bn.
  - Chemicals: OP KRW 13.4bn.
- **Leverage:** debt ratio cut from 233% (end-2025) to 122% after a KRW 1.1671tn rights offering in 1H 2026.
- **Funding for Absolics:**
  - KRW 589.6bn of the rights offering is planned for Absolics.
  - Cumulative injections into Absolics were KRW 417.4bn by May 2026.
- **Subsidies and divestments:**
  - CHIPS: US$75m manufacturing award, of which US$40m received. The remaining US$35m is tied to a second factory SKC does not plan. A separate US$100m R&D grant went to the Georgia Tech partnership ([SBS Biz](https://v.daum.net/v/20260529115214214); [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
  - SKC has sold its chemicals, film and front-end materials units and says there are "no further business units left to sell".

#### (e) Resilience
- **Parent's financial capacity** (third-party TTM; Korean data may run only to Jun 2026 because the Q3 quarterly report is filed mid-November) ([stockanalysis.com, fetched 12 Nov 2026](https://stockanalysis.com/quote/krx/011790/statistics/)):
  - Net debt about KRW 2.23tn (cash 2.07tn vs debt 4.30tn).
  - TTM free cash flow about −KRW 960bn; TTM net loss about KRW 805bn; ROE −26.7%.
- **A 1–2 year slip:** fundable from the earmarked KRW 589.6bn (inference). There is little margin beyond that.
- **A longer slip:** would need new equity or debt, because the parent burns cash, carries net debt and says it has no assets left to sell.
- **Unresolved inconsistency:** SKC's Q3 2026 release still reports a chemicals segment (revenue KRW 317.3bn). The May 2026 "nothing left to sell" statement may refer to agreed but unclosed sales.
- **Pause scenario:** most damaging. Customers defer new substrate architectures.
- **Acceleration scenario:** helps only if >110 mm packages force glass early.
- **Cross-border:** a US plant is positive for US customers. CHIPS conditions have already cost US$35m.

### 2.6 Ajinomoto (TSE 2802) — key upstream constraint holder (ABF film)

#### (a) Position
- **Constraint held:** a material constraint and de facto standard. Share is ~95% by secondary estimate ([AtlasPCB](https://www.atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026/)).
- **Product classification: spans BRIDGE and SUCCESSOR.** Build-up film is still used on glass cores. BOE's glass line integrates "ABF build-up" (search summary of [TechTimes, 23 Sep 2026](https://www.techtimes.com/articles/327959/20260923/boe-completes-glass-core-substrate-qualification-ships-customers-chip-level-testing.htm); not opened).
- **No announced successor** to ABF itself.
- **Threats:** CoWoP, which removes the substrate, and alternative dielectrics.

#### (b) Lead
- Share estimates (secondary).
- Ajinomoto calls ABF the "de facto standard" (company claim).
- A ~58% business-profit margin (PRIMARY) is itself evidence of a lead.

#### (c) Revenue model
- Recurring consumable material. Usage scales with the number of CPUs, GPUs and ASICs × substrate size × layer count (company slide).
- No prepayment data found.

#### (d) Financial strength
Source: PRIMARY deck and segment forecast, 9 Nov 2026 ([deck](https://www.ajinomoto.co.jp/company/en/ir/event/presentation/main/011111116/teaserItems1/01/linkList/03/link/FY26Q2_Presentation_E_with%20Script.pdf); [segment forecast](https://www.ajinomoto.co.jp/company/en/ir/event/presentation/main/011111116/teaserItems1/01/linkList/02/link/FY26Q2_Forecast_E.pdf)).

| Item | Figure |
|---|---|
| Functional Materials (electronic materials and others), H1 FY2026 | Sales JPY 73.3bn (+63%); business profit JPY 42.9bn (+81%), ~58.5% margin |
| FY2026 forecast (Nov) | Sales JPY 133.0bn (+32%; Aug forecast 120.6); BP JPY 76.5bn (+40%; Aug 65.5) |
| FY2025 actual | Sales JPY 100.7bn; BP JPY 54.6bn |
| Implied H2 FY2026 | Sales JPY 59.6bn; BP JPY 33.5bn — below H1, unexplained (possible pull-forward ahead of the reported price change, or conservatism) |
| Share of group | ~7.5% of group sales (JPY 1,767bn) but ~36% of segment business profit before shared costs (my arithmetic) |
| Capex | New ABF-varnish factory at Gunma, ~JPY 21.5bn: completion FY2029, mass production FY2030 |
| Earlier investment | ~JPY 10bn factory that started in 2025 |
| Land | Kani City, Gifu, acquired for demand "from 2030" (7 May 2026) |

- Customer concentration not disclosed.
- **Group-level third-party TTM** (food-dominated, so not ABF-specific) ([stockanalysis.com](https://stockanalysis.com/quote/tyo/2802/statistics/)): ROE 20.6%; ROIC 11.7%; net debt ~JPY 342bn; FCF ~JPY 119bn.

#### (e) Resilience
- **Pause scenario:** low capital intensity and high margins buffer a downturn.
- **Acceleration scenario:** the next large capacity step arrives only in FY2030, so film supply could become binding.
- **Cross-border:** reports say China allocations were cut about 30% (unconfirmed) ([FT Mercati](https://www.ftmercati.com/en/ajinomoto-to-cut-abf-film-supply-to-china-by-30-amid-global-shortage-178875.html)). That raises the incentive for Chinese substitutes.
- **Other:** the Middle East situation may cost the group about JPY 25bn in FY2026 (company).

### 2.7 Nittobo (TSE 3110) — key upstream constraint holder (T-glass cloth)

#### (a) Position
- **Constraint held:** a material constraint. TrendForce estimates ~90% of T-glass and 60–70% of NER-glass ([MPBxChange](https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil)).
- **Product classification: BRIDGE.** Glass-cloth-reinforced cores would be displaced by glass cores, but those are a 2030+ event on independent estimates.
- T-glass also serves BT memory substrates and high-end PCBs.

#### (b) Lead
- Third-party share estimates (TrendForce).
- Hyperscaler and NVIDIA bookings (Nikkei, via [TrendForce, 6 Aug 2026](https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/)).

#### (c) Revenue model
- Consumable material. Customers pre-book capacity; no prepayment data.

#### (d) Financial strength
Source: TrendForce, 6 Aug 2026, reporting the 5 Aug forecast revision.

| Item | Figure |
|---|---|
| FY3/2027 forecast | Revenue JPY 141bn; OP JPY 30bn (~21%); NP JPY 20bn (−52% YoY; cause not captured) |
| Q1 (Apr–Jun 2026) | Revenue JPY 34.0bn (+21%); NP JPY 5.7bn (+84%) |
| Electronic materials target | Revenue JPY 77.8bn (+27%); OP JPY 28.0bn (+44%; ~36% margin) |
| Capacity commitment | JPY 80bn for semiconductor materials in Japan and Taiwan |

- **Third-party TTM** (period not stated) ([stockanalysis.com](https://stockanalysis.com/quote/tyo/3110/statistics/)):
  - Revenue JPY 129.3bn; operating margin 21.3%; ROIC 14.3%.
  - Net income JPY 47.6bn with a 52% pretax margin, so it contains a large one-off gain. That also explains the −52% FY net-profit forecast.
  - Net debt ~JPY 5.0bn; operating cash flow JPY 9.0bn vs capex JPY 25.9bn, so FCF −JPY 16.9bn: expansion currently exceeds internal cash generation.
- H1 results (Nov 2026) and customer concentration not retrieved (gap). Nittobo's IR pages load through a script feed that could not be read.

#### (e) Resilience
- Nittobo is showing price restraint: no further hikes.
- **Pause scenario:** capacity triples by FY3/2029 just as second sources ramp (Nan Ya Plastics 2027, Kingboard 2027), so 2029 oversupply risk.
- **Longer-term risk:** glass-core substitution.
- **Cross-border:** Japan and Taiwan production; energy costs (Middle East).

### 2.8 Other makers — brief evidence

**LG Innotek** — Q3 2026 ([Korea Herald, 27 Oct 2026](https://www.koreaherald.com/article/10916657)):
- Revenue KRW 6.37tn (+18.6%); OP KRW 94.8bn (−53.4%; 1.5% margin, hit by FX).
- Package Solution KRW 481.8bn (+10.1%; 7.6% of sales). Optics is ~85% of revenue (Apple-dependent).
- Its first large-area FC-BGA for AI accelerators was shown at the KPCA Show in Sep 2026, with mass production targeted for 2027 ([Herald Business](https://biz.heraldcorp.com/article/10867093)). It plans to enter AI and server substrates "in stages through 2028".
- KB Securities estimate: FC-BGA revenue KRW 140bn (2026E) → >KRW 2tn (2030E) (analyst estimate, Jun 2026) ([PRESS9](https://www.press9.kr/news/articleView.html?idxno=77447)).

**Nan Ya PCB** — Q3 2026 ([CTEE, 6 Nov 2026](https://www.ctee.com.tw/news/20261106700224-430502)):
- GM 29.31%; NP NT$3.298bn; EPS NT$5.10 (15-quarter high); 9M EPS NT$10.63.
- Kunshan (China) ABF plant serves a US networking customer.

**Kinsus** — Q3 2026 ([storm.mg](https://www.storm.mg/article/11165649); date not captured):
- Revenue NT$14.54bn; GM 33.9%; NP NT$2.388bn; EPS NT$4.60.

**Shennan Circuits** — 9M 2026 ([Sina, 23 Oct 2026](https://finance.sina.com.cn/stock/aigc/agcbld/2026-10-23/doc-iniwcnvh5019323.shtml)):
- Revenue RMB 25.77bn (+53.8%); attributable NP RMB 4.13bn (+77.5%); Q3 revenue RMB 10.48bn, NP RMB 1.88bn.
- Packaging substrates, 1H 2026: revenue RMB 3.667bn (+110.8%), GM 31.35%.
- FC-BGA ≤26 layers in volume, ≥30 layers sampling (company claim, Oct 2026 investor Q&A; a broker note says ≤22 layers — conflict) ([10jqka](http://stock.10jqka.com.cn/20261101/c681325519.shtml)).

**Shenzhen Fastprint:**
- Zhuhai FC-BGA capacity 2m units a month; Guangzhou planned 20m a month; ≤20 layers in volume.
- Claims to be the "only domestic ABF mass producer" (company-favourable post, Apr 2026) ([Eastmoney](https://caifuhao.eastmoney.com/news/20260414014428571468720)).

**LPKF** ([LPKF H1 2026 report](https://www.lpkf.com/fileadmin/mediafiles/Half-yearly_Financial_Report_2026.pdf)):
- H1 2026 revenue EUR 36.5m (−38.3%); Q2 EBIT −EUR 7.2m.
- Q2 LIDE order from "a leading specialty glass manufacturer" for advanced-packaging qualification.
- The company says it is "premature" to claim a glass breakthrough. 2026 guidance of EUR 105–120m excludes large semiconductor orders.

### 2.9 Cross-company returns and balance sheets (third-party TTM; quality metrics only)

**Source and caveats.** stockanalysis.com statistics pages, fetched 12 Nov 2026 (URL pattern `https://stockanalysis.com/quote/<exchange>/<ticker>/statistics/`).
- Figures are trailing twelve months to the latest filed quarter. Sep 2026 is confirmed where cash matches company filings (Ibiden, AT&S, Unimicron). Korean companies may be to Jun 2026.
- These are third-party computations, and ROIC definitions vary.
- Valuation fields on these pages were deliberately not used.

| Company | TTM revenue | TTM op. margin | ROE | ROIC | Net cash (+) / net debt (−) | TTM FCF |
|---|---|---|---|---|---|---|
| Ibiden | JPY 483.3bn | 17.8% | 14.1% | 15.7% | +JPY 250.9bn | +JPY 168.1bn (incl. customer advances) |
| Unimicron | NT$167.7bn | 13.3% | 23.6%* | 23.9%* (ROCE 7.3%) | +NT$109.7bn | +NT$3.8bn |
| Samsung Electro-Mechanics | KRW 12.46tn | 9.8% | 10.6% | 9.8% | +KRW 240.6bn | +KRW 285.6bn |
| AT&S | EUR 2.18bn | 14.0% | 18.5% | 11.8% | −EUR 1.36bn | +EUR 94.6m |
| SKC (Absolics parent) | KRW 2.08tn | −9.9% | −26.7% | −3.9% | −KRW 2.23tn | −KRW 959.9bn |
| Ajinomoto (whole group) | JPY 1.68tn | 10.8% | 20.6% | 11.7% | −JPY 342.1bn | +JPY 119.4bn |
| Nittobo | JPY 129.3bn | 21.3% | n/a | 14.3% | −JPY 5.0bn | −JPY 16.9bn |
| LG Innotek | KRW 24.04tn | 4.5% | 11.4% | 12.2% | −KRW 942.5bn | +KRW 225.5bn |
| Nan Ya PCB | NT$52.3bn | 18.2% | 16.6% | 17.7% | +NT$9.3bn | +NT$6.8bn |
| Kinsus | NT$48.95bn | 13.7% | 13.0% | 12.4% | +NT$5.1bn | +NT$1.8bn |
| Zhen Ding Technology | NT$210.65bn | 9.9% | 9.1% | 8.5% | +NT$9.3bn | −NT$43.0bn (capex NT$65.8bn) |
| Daeduck Electronics | KRW 1.35tn | 13.0% | 16.6% | 18.4% | +KRW 216.7bn | +KRW 70.8bn |

\*Unimicron's returns are inflated by Q2 2026 non-operating gains, and the ROIC/ROCE gap is internally inconsistent.

Per-company URLs:
- [Ibiden](https://stockanalysis.com/quote/tyo/4062/statistics/)
- [Unimicron](https://stockanalysis.com/quote/tpe/3037/statistics/)
- [SEMCO](https://stockanalysis.com/quote/krx/009150/statistics/)
- [AT&S](https://stockanalysis.com/quote/vie/ATS/statistics/)
- [SKC](https://stockanalysis.com/quote/krx/011790/statistics/)
- [Ajinomoto](https://stockanalysis.com/quote/tyo/2802/statistics/)
- [Nittobo](https://stockanalysis.com/quote/tyo/3110/statistics/)
- [LG Innotek](https://stockanalysis.com/quote/krx/011070/statistics/)
- [Nan Ya PCB](https://stockanalysis.com/quote/tpe/8046/statistics/)
- [Kinsus](https://stockanalysis.com/quote/tpe/3189/statistics/)
- [Zhen Ding](https://stockanalysis.com/quote/tpe/4958/statistics/)
- [Daeduck](https://stockanalysis.com/quote/krx/353200/statistics/)

Inferences:
- **TTM figures still include weak late-2025 quarters.** Current run-rates are much higher: Ibiden Electronics H1 operating margin 29%; Unimicron Q3 operating margin 20%; AT&S Q2 EBITDA margin 35.8%.
- **Balance-sheet ordering** for funding the 2027–29 capacity wave:
  1. Ibiden: ~JPY 250bn net cash plus JPY 200bn customer advances.
  2. Unimicron and SEMCO: net cash.
  3. Nan Ya PCB, Kinsus and Daeduck: small net cash.
  4. Nittobo: roughly neutral.
  5. AT&S: EUR 1.3bn net debt, offset by EUR 1.2bn of prepayments.
  6. SKC: KRW 2.2tn net debt and cash burn. This is the weakest position from which to fund a successor through slips.
- **Zhen Ding's heavy negative FCF** reflects capex for its ABF/HDI push. Its ABF economics cannot be separated.

---

## (3) Path-forward evidence and suggested verdicts

### Which transitions each key company must get through
| Company | (1) Copper→optical links | (2) CPO | (3) Hybrid bonding | (4) Si interposer→panel/glass | (5) Two-phase cooling | (6) 800 V DC / MW racks |
|---|---|---|---|---|---|---|
| Ibiden | Indirect: optical-electrical conversion on its roadmap | Yes: switch and optical-engine substrates | Indirect: bigger packages | **Core test** | Indirect (warpage) | Yes: "power enhancement", embedded parts |
| Unimicron | Indirect | Yes | Indirect | **Core test** | Indirect | Yes |
| SEMCO | Indirect | Yes: NVIDIA switch substrates | Indirect | **Core test (both sides)** | Indirect | Yes: embedded passives, silicon capacitors, 1 kV+ MLCC |
| AT&S | Indirect | Yes: CPO on its roadmap | Indirect | **Core test** | Indirect | Yes: EMB core, power PCBs |
| SKC/Absolics | — | Possible (glass optics) | — | **Entire thesis** | Glass helps warpage | — |
| Ajinomoto | — | — | — | Film survives glass cores; CoWoP is the threat | — | — |
| Nittobo | — | — | — | Glass cores displace cloth cores (2030+) | — | — |

### Glass-core / panel programme tracker (as of Nov 2026)
| Programme | Originally stated | Currently stated (date of statement) | Samples | Customers | Capital | Subsidies | Slips |
|---|---|---|---|---|---|---|---|
| Absolics (SKC) | Commercialisation June 2024 | 2027 per TrendForce (Jul 2026); "difficult to predict" (SKC filing, May 2026); no date (Oct 2026) | Mass-production samples Q1 2026; embedded samples in Taiwan reliability evaluation (Jul 2026) | AMD and AWS "reportedly"; no named agreement | US$600m plant; KRW 417.4bn injected plus KRW 589.6bn earmarked | CHIPS US$75m manufacturing (US$40m received) plus US$100m R&D | ≥3 (2024 → 2025 → 2026 → 2027+) |
| Intel | "Second half of this decade" (Sep 2023) | Own deployment ~2030; shift toward licensing (Tom's Hardware, Aug 2026, via IRZ) | 78×77 mm, 10-2-10 EMIB glass core shown Jan 2026 ([TrendForce](https://www.trendforce.com/news/2026/01/26/news-intel-reportedly-presents-first-thick-core-glass-substrate-with-emib-targeting-ai-data-centers/)) | None | Lens TGV memorandum (24 Jul 2026), no purchase commitment | Not verified | Yes |
| SEMCO / GlaSSEM | Not verified this session | JV full-scale operation 2H 2027 (2 Jul 2026); "full operation 2028" (28 Oct 2026) | Sejong pilot line | Broadcom "reported" | JV KRW 480bn; SEMCO KRW 319.1bn for 66.2% | None found | None documented yet |
| LG Innotek | 2027–28 | 2027–28 ([vlsi.kr, Oct 2026](https://www.vlsi.kr/en/glass-core-substrate-race-en/)) | Gumi pilot | None | Not disclosed | — | — |
| BOE | Mass production "after 2026" (TrendForce, Oct 2025) | No mass-production date; yield not at mass-production level (BOE, 2026) | 9-2-9, 20-layer samples (2025); chip-level testing (Sep 2026) | Chinese customers at PoC/trial stage | RMB 390m + RMB 993m | — | Open-ended |
| DNP / Toppan | — | DNP pilot line started Dec 2025; Toppan commissioning a pilot line | — | — | — | — | — |
| 3DGS (India) | — | Production 2030 | — | — | ₹1,943 crore | ISM approval (2025) | — |
| TSMC CoPoS (panel, not glass) | — | Pilot line under construction (Apr 2026); trial 2027; mass production 2H/late 2028; glass "under review" | — | Not named | — | — | — |
| Independent views | — | SEMI: first glass-substrate production ~2028. TrendForce: mainstream after 2030 (Aug 2026); TSMC glass after 2030 | — | — | — | — | — |

Tracker sources: [SBS Biz](https://v.daum.net/v/20260529115214214); [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/); [XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/); [TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/); [Korea Herald](https://www.koreaherald.com/article/10796508); [Business Standard](https://www.business-standard.com/industry/news/india-s-1st-advanced-3d-glass-chip-packaging-unit-to-come-up-in-bhubaneswar-126041900360_1.html).

- **Is any glass-core product shipping in volume?** No. No commercial glass-core product had shipped as of Sep–Oct 2026 ([IRZ, 4 Sep 2026](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/); [vlsi.kr, 20 Oct 2026](https://www.vlsi.kr/en/glass-core-substrate-race-en/)). SKC gave no date in its Q3 2026 release.
- **Who is closest?** Absolics, as the only dedicated plant with mass-production samples in package-level reliability evaluation, then SEMCO (pilot line plus funded glass-core JV). This ranking is my inference.
- **Where glass ships first:** carriers and optics. Corning glass carriers ship today; Crystal-Optech TGV CPO substrates were sampling in 2H 2026; WG Tech is delivering small-batch 1.6T CPO carrier samples ([TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)).

### 3.1 Ibiden — suggested verdict: **COHERENT**
- **Said:** capacity in step with AI demand. Roadmap to 130 mm, 14-X-14 by CY30+ (organic). Optical-electrical conversion moving to die-to-die by CY30+.
- **Done:**
  - Ono mass production started in FY2025. Confirmed by a commemorative dividend "for the start of mass production at the Ono Plant", which verifies the lead.
  - Ono Cell8 (JPY 280bn) and Gama Cell6 (JPY 370bn total) committed.
  - FY2026 capex JPY 210bn.
  - NVIDIA-funded expansion (PRIMARY).
- **Funded?** Yes:
  - operating cash flow (Electronics EBITDA margin ~48%);
  - JPY 199.7bn of customer advances on the balance sheet at Sep 2026;
  - about JPY 258bn net cash (my arithmetic from the tanshin);
  - single-A rating.
- **Ibiden's stated view:** "no technology that can replace leading-edge IC package substrates" (Q&A, 30 Oct 2026; company claim).
- **Credible successor?** Its "bridge" is what customers are funding through ~2030. It has no dated glass-core programme. In the 30 Oct 2026 Q&A an analyst referred to future "products using glass" in Ibiden's mix; Ibiden did not contradict this but gave no detail. Its concrete successor steps are organic: EMIB-T mass production 2H FY2027, multi-core and embedded-component substrates. The lack of a dated glass plan is a risk only if glass arrives before 2030, against the weight of evidence.
- **Timing plausible?** Yes for organic capacity: Cell8 from FY2027, ramp Q1 2028.
- **What must go right:**
  - AI accelerator demand holds through FY2029.
  - Yields on 110 mm+ bodies.
  - No repeat of underused fabs.
  - NVIDIA does not shift to CoWoP or panel formats that bypass its substrates.

### 3.2 Unimicron — suggested verdict: **COHERENT** (weaker than Ibiden)
- **Said:** ABF expansion through 2030; land bought for post-2030 capacity.
- **Done:**
  - NVIDIA KF reservation.
  - 2026 capex ~NT$53.7bn; NT$82.5bn long-lead equipment commitments.
  - Unimicron Japan divestment started.
- **Funded?** Yes, but partly by external financing (NT$94.9bn in 9M).
- **Glass:** no dated plan.
- **What must go right:** prices keep rising so gross margin reaches 30%+, and AI demand absorbs Guangfu 2 and Yangmei 2 in 2027–28.

### 3.3 Samsung Electro-Mechanics — suggested verdict: **COHERENT** (organic); glass timing optimistic
- **Said:** glass "full operation 2028"; embedded substrates for AI accelerators and switches in 2027.
- **Done:**
  - GlaSSEM JV signed and funded (KRW 319.1bn for 66.2%; share purchase scheduled 1 Sep 2026).
  - Sejong pilot line.
  - NVIDIA multi-year agreement.
  - KRW 6.8tn substrate capex.
  - KRW 1.5tn silicon-capacitor contract.
  - Embedded server-CPU substrates in mass production.
- **Funded through a 1–2-year glass slip?** Yes. Glass is small relative to quarterly operating profit of KRW 691bn.
- **Timing:** 2H 2027 / 2028 for glass is ahead of independent views (2030+). Expect slips without impairing the group.
- **What must go right:** NVIDIA qualification at scale on Sejong/Busan lines, and glass reliability to win a first customer.

### 3.4 AT&S — suggested verdict: **PARTLY COHERENT**
- **Said:** Kulim high-volume manufacturing 2028/29; CPO and power roadmap.
- **Done:**
  - AMD plus one other customer agreement (key terms only).
  - Strong margin turnaround (Q2 EBITDA margin 35.8%).
  - Refinanced the hybrid.
- **Funded?** Largely by customers: EUR 1.2bn of contract liabilities (prepayments) at Sep 2026, and "all planned investments are supported and financed by long-term customer commitments" (H1 report). Leverage is high: net debt EUR 1.33bn, equity ratio 23.9%, H1 FCF from operations −EUR 10.6m. AT&S itself warns that the "high level of investment… could result in significant impairment charges".
- **Successor work:** glass-core R&D only. AT&S itself says the glass-core supply chain is not yet at the required quality (AFR 2025/26). No product date. It is building its own core-precursor plant at Kulim.
- **Timing risk:** high-volume manufacturing in 2028/29 coincides with the pause scenario.
- **What must go right:** customer commitments get executed, AMD's roadmap volumes hold, and materials stay available.

### 3.5 SKC / Absolics — suggested verdict: **PARTLY COHERENT** (funded near term; timing not credible)
- **Said:** successive dates from 2024 to 2027; now "difficult to predict".
- **Done:**
  - Plant built.
  - Samples shipped; Taiwan reliability evaluation.
  - KRW 1.17tn equity raised.
  - Other businesses sold.
  - Non-embedded fallback product added.
- **Funded?** A 1–2-year slip, probably yes from the KRW 589.6bn earmark. Beyond that, no: no assets left to sell and the parent is loss-making.
- **What must go right:** pass the package-level reliability tests (results possibly by end-2026), sign a named customer by 2027, and control glass cracking and via metallisation yields.
- **Downgrade trigger:** no customer contract by mid-2027 would argue for "not coherent".

### 3.6 Ajinomoto — suggested verdict: **COHERENT**
- **Said:** de facto standard; supply chain can meet current demand.
- **Done:**
  - 2025 factory (~JPY 10bn).
  - Gunma varnish plant (~JPY 21.5bn, FY2030).
  - Kani land for demand from 2030.
  - Segment profit +81% in H1.
- **Robustness:** ABF film is transition-robust to glass cores; the threat is CoWoP or substrate-less schemes, which have no 2026 adoption evidence.
- **What must go right:** capacity timing (FY2030) must not lag an acceleration scenario, and China substitution must stay slow.

### 3.7 Nittobo — suggested verdict: **COHERENT to FY3/2029; partly coherent beyond**
- **Said:** 3x capacity by FY3/2029; Taiwan 2x by Mar 2028.
- **Done:** JPY 80bn committed; Fukushima building (~JPY 15bn) starting Q1 2027; price increases completed.
- **Funded?** Yes.
- **Unaddressed:** no identified successor product for a glass-core world; second sources (Nan Ya Plastics, Kingboard) ramp in 2027.

---

## (4) Suggested ordering of key companies by quality alone

| Rank | Company | Why |
|---|---|---|
| 1 (tie) | **Ajinomoto (ABF business)** | Material chokepoint; ~58% business-profit margin (H1 FY2026); low capital intensity; survives the glass-core transition. Caveat: ABF is ~7.5% of a food-led group, so group-level exposure is diluted. |
| 1 (tie) | **Ibiden** | Customer-confirmed lead at NVIDIA (Ibiden says high-end AI has only three suppliers); ~29% Electronics operating margin. Customer-funded expansion visible on its balance sheet: JPY 199.7bn advances received, ~JPY 258bn net cash at Sep 2026. Single-A. Weaknesses: capital intensity (capex ≥ EBITDA FY2026–27), cyclicality (FY2024 ROE 6.8%), likely high customer concentration (undisclosed). **Cannot separate from Ajinomoto**: the two sit on different layers of the same constraint. |
| 3 (tie) | **Nittobo** | Tightest 2026–27 chokepoint and pricing power. But smaller, with second sources arriving in 2027 and a long-run glass-core substitution risk. |
| 3 (tie) | **Samsung Electro-Mechanics** | NVIDIA entry (customer-confirmed); broad diversification (MLCC ~50% of revenue, >40% share of AI-server MLCC); sound balance sheet (small net cash, debt/equity ~0.3); funded glass option. Division margins not disclosed; group ROIC ~10% TTM. **Cannot separate cleanly from Nittobo.** |
| 5 | **Unimicron** | Scale and NVIDIA reservation; lower margins than Ibiden; partly financed expansion; deep 2024–25 trough (FY2025 OP ~NT$6.7bn). Close to SEMCO on the substrate business alone. |
| 6 | **AT&S** | Real turnaround (H1 ROCE 17.7%, Q2 EBITDA margin 35.8%), an AMD anchor and EUR 1.2bn of customer prepayments. But leveraged (net debt EUR 1.33bn, equity ratio 23.9%), highly concentrated (largest customer ~31%, top five 76.5%), H1 FCF slightly negative, and glass only at R&D stage. |
| 7 | **SKC / Absolics** | Pre-revenue successor bet with ≥3 slips; parent loss-making; depends on the reliability-test outcome. |

Not ranked (not key; brief evidence only): Nan Ya PCB, Kinsus, LG Innotek, Shennan Circuits, Fastprint, LPKF, the glass makers.

---

## (5) Check of background priors

**Prior 1 — "Glass-core substrates are targeted for 2027–28 by several makers."**
- **Verdict:** CONFIRMED as stated targets; CONTRADICTED as a volume expectation.
- **Current company targets:**
  - SEMCO/GlaSSEM: full-scale operation 2H 2027 ([2 Jul 2026](https://www.koreaherald.com/article/10796508)); "full operation 2028" ([28 Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).
  - LG Innotek: 2027–28 ([20 Oct 2026](https://www.vlsi.kr/en/glass-core-substrate-race-en/)).
  - Absolics: 2027 per TrendForce (Jul 2026), but SKC itself says it cannot predict (May 2026) and gave no date (28 Oct 2026).
  - SEMI: initial glass-substrate production ~2028.
- **Independent views (Nov 2026):**
  - TrendForce: TGV glass enters mainstream packaging "after 2030" ([7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)); commercial glass-core production not before 2030 (17 Jun 2026, via [XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/)).
  - Intel's own deployment ~2030 (Aug 2026, via [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
  - Nothing ships in volume as of Nov 2026.
- **Change to the prior:** use **2030+ for meaningful volume**. Treat 2027–28 as pilot or first-customer dates that are likely to slip.

**Prior 2 — "Panel-sized packaging is in pilot in 2026 with volume expected in 2028–29."**
- **Verdict:** CONFIRMED.
- TSMC CoPoS pilot line under construction (1Q26 call, Apr 2026). TrendForce: 2026 equipment/material verification, 2027 trial production, late-2028 mass production on 310×310 mm panels (17 Jun 2026) ([XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/); [IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
- BOE's glass-panel pilot is running but not in mass production.
- **Nuance:** panel interposers (organic or glass carrier) arrive before glass cores. CoPoS still sits on an ABF substrate, so it does not remove the substrate maker.

**Prior 3 — "Packaging, including substrates, is a binding constraint in 2028–30; successor dates slip; bridge products last longer."**
- **Verdict:** UPDATED.
- **Slips:** CONFIRMED (Absolics ≥3 slips; Intel from "late decade" to ~2030).
- **Bridge longevity:** SUPPORTED. Ibiden's CY30+ roadmap is organic; NVIDIA is funding organic capacity to 2028+.
- **"Binding in 2028–30":** only partly supported.
  - On the supplier side, Ibiden (30 Oct 2026) accepted that the shortage lasts "until around 2030". It said no technology can replace leading-edge substrates, so "demand will ultimately have to be constrained", and that new buildings take ≥4 years. This is a self-interested company claim, but it is consistent with NVIDIA pre-funding capacity.
  - 2026–27 is clearly binding: ABF lead times 48–56 weeks (TrendForce, Sep 2026); BofA sees shortage through 2028; Unimicron's chairman sees ~20% material shortages in 2027.
  - But NVIDIA targets 2.5x substrate capacity within three years (Oct 2026), and Ibiden, Unimicron, SEMCO and AT&S capacity lands 2028–29. By 2029–30, substrates may stop being binding in the steady and pause scenarios. They stay binding mainly in the acceleration scenario.
- **Where the binding constraint actually sits in 2026–27:** upstream T-glass and thin glass cloth (no new Nittobo capacity before mid-2027; 3x only by FY3/2029) more than ABF film. Ajinomoto claims it can meet current demand (company claim).

---

## (6) Open question: which successor ships in volume first, and who captures the value

### Takeaway
The likely order of volume arrival is:
1. Incremental organic successors — embedded and multi-core ABF substrates, already in mass production at SEMCO.
2. Panel-level interposers — TSMC CoPoS, 2H/late 2028.
3. Glass in optics and carriers — sampling in 2026.
4. Glass-core substrates for AI accelerators — company claims 2027–28, independent views 2030+.

Value capture is splitting rather than migrating wholesale. Foundries keep the interposer layer. Substrate specialists keep the substrate layer through ~2030, funded by customers. In glass, raw-panel margin goes to a four-maker glass oligopoly, while via processing is contested by substrate makers, display makers and glass processors.

### Cited findings
- SEMCO's embedded/multi-core server-CPU substrates are in mass production, with Q4 2026 supply doubling and AI-accelerator and switch versions in 2027 ([transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482)).
- CoPoS (foundry-controlled): mass production late/2H 2028; glass "under review"; TrendForce puts TSMC glass after 2030 ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/)).
- Corning, AGC, NEG and Schott have all centred core-substrate and TGV roadmaps on 510×515 mm panels ([DIGITIMES, 1 Oct 2026](https://www.digitimes.com/news/a20261001PD230/ai-chip-tsmc-corning-tgv-agc.html)). Raw low-CTE glass supply is concentrated in these four, and new melting tanks take a long time ([Exponential Industry](https://exponentialindustry.com/blog/2026-08-13-glass-core-substrates-ai-chip-packaging/)).
- Substrate makers are vertically securing glass: SEMCO formed GlaSSEM with a Sumitomo Chemical unit "to secure a stable supply of glass cores" ([Korea Herald](https://www.koreaherald.com/article/10796508)).
- Display makers are building complete glass-core lines. BOE integrates TGV drilling, copper filling and build-up in one pilot line, and signed a 3-year MoU with Corning ([XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/)).
- The integrated giant that started glass (Intel) is reportedly moving toward licensing and demo vehicles, and partnering with a Chinese glass processor (Lens) ([IRZ](https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/); [XenoSpectrum](https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/)).
- Glass reaches optics first: Corning Glass Bridge for CPO; Crystal-Optech and WG Tech CPO samples in 2026 ([TrendForce, 7 Aug 2026](https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/)).
- CoWoP, the one scheme that would remove the substrate and shift value to PCB makers, faces line/space (<10/10 µm needed vs 20–30 µm in PCB mSAP) and warpage hurdles. No 2026 adoption was found ([GlobalSMT](https://www.globalsmt.net/advanced-packaging/nvidias-cowop-pcb-architecture-targets-abf-substrates-but-faces-warpage-risk/)).
- Customers are funding the specialists' organic capacity: NVIDIA (Ibiden, Unimicron, SEMCO); AMD and another company (AT&S) ([NVIDIA](https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx); [AT&S](https://www.finanzwire.com/press-release/ats-austria-technologie-systemtechnik-ag-etr-aus-eqs-adhoc-ats-austria-technologie-systemtechnik-ag-ats-expands-ai-substrate-capacity-in-kulim-and-increases-outlook-for-202627-JHz5CRE5qDV)).

### Inferences
- **Through 2030, substrate specialists capture the value of the bridge.** Customer pre-funding signals that buyers see no near-term substitute.
- **In a glass world:**
  - Build-up film (Ajinomoto) keeps its share of value, because glass replaces the core, not the build-up layers.
  - Glass-cloth makers (Nittobo) lose the core.
  - The four glass makers gain a materials margin.
  - The TGV/core processing step is the contested layer. Specialists that integrate it (SEMCO via GlaSSEM; Absolics) keep value. Those that don't would buy cores from glass or display players and keep build-up and assembly value. Ibiden and Unimicron have no dated glass plans found. AT&S has glass-core R&D and says the glass-core supply chain "has not yet been established in the required quality".
- **Integrated giants:**
  - TSMC captures panel-interposer value.
  - Intel appears to be monetising glass IP rather than capturing manufacturing value.
  - The Samsung group could integrate (SEMCO substrates plus a reported Samsung Display TGV team), but no customer evidence was found.
- **Evidence on relative economics (glass-panel margins vs substrate margins) is absent,** so this split is a judgement, not a measurement.

### Gaps
- No published cost or margin data on glass cores vs organic cores.
- No customer qualification data for any glass maker's panels in production substrates.

---

## (7) What I could not verify
- **Customer concentration:** now available for AT&S (top five 76.5%, largest ~31%, FY2025/26). For Ibiden, Unimicron, SEMCO, Nan Ya PCB and Kinsus it was not retrieved:
  - Ibiden's securities-report page loads by script;
  - the TWSE document server returned a stub;
  - DART needs an API key;
  - Unimicron's site failed TLS verification (I did not bypass it).
- **Shares and qualification:** reliable supplier shares at Google, Amazon, Broadcom, Marvell and MediaTek. Prismark and Yole tables were not retrieved.
- **Ajinomoto's 30% ABF price increase:** secondary only; not quantified in Ajinomoto's 9 Nov 2026 deck. Same for the reported ~30% cut to China allocations.
- **NVIDIA's advance to Ibiden:** the ~JPY 280bn figure is Bunshun's report, unconfirmed by either party. The "JPY 500bn three-year capex funded substantially by prepayments" quote is secondary (RCRTech).
- **Intel's licensing shift and ~2030 deployment:** Tom's Hardware (27 Aug 2026) via IRZ; the original was not opened. Low-quality sites claim Clearwater Forest ships on glass in volume; this was not accepted.
- **Absolics:** AMD and AWS qualification (industry press only); Applied Materials' current stake; CHIPS disbursement status after May 2026; The Elec's 27 Jul 2026 Taiwan reliability item (via IRZ only).
- **SEMCO:** the KRW 2.5tn Vietnam approval (call-coverage summary, not opened); the Broadcom glass qualification ("reported"); the "only supplier" embedded claim (company claim).
- **Nittobo:** H1 FY3/2027 results (Nov 2026), balance sheet and the cause of the −52% net-profit forecast. Nittobo IR pages did not render.
- **Net debt and returns:** now covered by primary filings for Ibiden and AT&S and by third-party TTM pages for the rest (section 2.9). Limits: site-computed ROIC definitions vary (Unimicron's 23.9% ROIC vs 7.3% ROCE is inconsistent), Korean TTM may lag a quarter, and no company-reported ROIC was found except AT&S's ROCE (17.7% for H1).
- **Missing companies:** Zhen Ding ABF progress; Kyocera, Toppan, DNP, Shinko and Daeduck 2026 substrate financials; Fastprint Q3 2026; Philoptics; Corning, AGC, NEG and Schott glass-core revenue or customers; Sekisui and Chinese build-up-film substitutes. The "Lotus Holdings RMB 103m" ABF-substitute item was seen as a headline only ([BigGo](https://finance.biggo.com/news/72147843-2346-4bf7-ad32-2d8c56ae3ca9)).
- **Policy exposure:** 2026 tariff and export-control specifics affecting substrate trade flows (e.g., US semiconductor tariffs, Malaysia/Vietnam reciprocal tariffs).
- **Regions:** Israel — no player surfaced and no dedicated MAYA check was run. India — the claimed Intel–Odisha–3DGS MoU (May 2026) comes from one weak source ([Anantam IAS](https://anantamias.com/current-affairs/india-3d-semiconductor-packaging-odisha-2026/)).
- **Shortage magnitudes:** the gap estimates (10%/21%/>40%; Morgan Stanley 15→22%) are secondary or untraced.
- **Data conflicts:**
  - Unimicron Q3 EPS: NT$6.15, 6.32 or 6.36 depending on source.
  - Shennan FC-BGA layers: ≤26 vs ≤22.
  - Ibiden Gama Cell6 product: "AI ASIC" on the slide vs "server CPU" in The Elec. Partly resolved: the primary capex notice (29 Oct 2026) says the ~JPY 151bn addition is for CPU substrates at Gama "and other overseas plant", and the Q&A says it is for EMIB. EMIB serves both Intel CPUs and foundry-customer ASICs, so both labels can be true.
- **Search budget:** further searching was blocked when the WebSearch budget ran out; a follow-up session could close most of the gaps above.

---

## (8) Sources (with dates)

### Primary — companies and official releases
- Ibiden, Financial Results of 1H FY2026 (deck dated 30 Oct 2026; forecasts as of 29 Oct 2026) — https://www.ibiden.com/ir/items/en_kessannsetsumei2026Q2.pdf
- Ibiden, Consolidated financial results (tanshin) for Q2 FY2026, with balance sheet and cash flow (29 Oct 2026) — https://www.ibiden.com/ir/library/statement/items/tannshinn2026Q2.pdf
- Ibiden, Outline of Consolidated Financial Results, Q2 (29 Oct 2026) — https://www.ibiden.com/ir/items/hosokushiryou2026Q2.pdf
- Ibiden, Key Q&A from the 2Q financial presentation (30 Oct 2026) — https://www.ibiden.com/ir/items/en_QA_FY2026Q2.pdf
- Ibiden, Notice regarding capital investment for high-performance IC package substrates (29 Oct 2026) — https://www.ibiden.com/ir/items/koteishisansyutoku2026Q2.pdf
- AT&S, Half-Year Financial Report 2026/27 (5 Nov 2026) — https://ats.net/en/download/half-year-financial-report-2026-27/?wpdmdl=67668
- AT&S, Annual Financial Report 2025/26 (FY ended 31 Mar 2026) — https://ats.net/en/download/annual-financial-report-2025-26/?wpdmdl=61790
- Ibiden, Integrated Report 2025 (FY2024 data) — https://www.ibiden.com/ir/items/IntegratedReport2025_en.pdf
- NVIDIA, "NVIDIA and Supply Chain Partners Expand Capacity…" (GTC Berlin, 21 Oct 2026) — https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-and-Supply-Chain-Partners-Expand-Capacity-to-Accelerate-AI-Infrastructure-Buildout/default.aspx
- Samsung Electro-Mechanics, NVIDIA ABF supply release (21 Oct 2026) — https://m.samsungsem.com/global/newsroom/news/view.do?id=10614
- Samsung Electro-Mechanics, MOU with Sumitomo Chemical Group (Nov 2025) — https://samsungsem.com/global/newsroom/news/view.do?id=9850
- Ajinomoto, FY2026 Q2 presentation with script (9 Nov 2026) — https://www.ajinomoto.co.jp/company/en/ir/event/presentation/main/011111116/teaserItems1/01/linkList/03/link/FY26Q2_Presentation_E_with%20Script.pdf
- Ajinomoto, FY2026 Revised Forecast by Segment (9 Nov 2026) — https://www.ajinomoto.co.jp/company/en/ir/event/presentation/main/011111116/teaserItems1/01/linkList/02/link/FY26Q2_Forecast_E.pdf
- AT&S ad hoc (13 Jun 2026), via finanzwire — https://www.finanzwire.com/press-release/ats-austria-technologie-systemtechnik-ag-etr-aus-eqs-adhoc-ats-austria-technologie-systemtechnik-ag-ats-expands-ai-substrate-capacity-in-kulim-and-increases-outlook-for-202627-JHz5CRE5qDV
- LPKF Half-yearly Financial Report 2026 — https://www.lpkf.com/fileadmin/mediafiles/Half-yearly_Financial_Report_2026.pdf
- TOPPAN, "TOPPAN Establishes FC-BGA Substrate Production Site in Singapore" (30 Sep 2026) — https://www.holdings.toppan.com/en/news/2026/09/newsrelease260930_1.html
- DNP, completion of investment in the Shinko SPC (19 Mar 2025) — https://www.global.dnp/en/news/detail/2025/03/0319_20176512/
- Press Information Bureau (India), Odisha 3D glass packaging unit (Apr 2026) — https://www.pib.gov.in/PressReleasePage.aspx?PRID=2253276&reg=3&lang=2

### Secondary — results coverage and transcripts
- Investing.com, SEMCO Q3 2026 call transcript (28 Oct 2026) — https://www.investing.com/news/transcripts/earnings-call-transcript-samsung-electromechanics-posts-record-q3-2026-profit-93CH-4977482
- Herald Business, SEMCO Q3 2026 (28 Oct 2026) — https://biz.heraldcorp.com/article/10917700
- Investing.com, AT&S Q1 2026/27 slides (4 Aug 2026) — https://www.investing.com/news/company-news/ats-q1-202627-slides-ai-demand-drives-40-revenue-surge-93CH-4834617
- ad-hoc-news.de, AT&S H1 2026/27 (12 Nov 2026; results 5 Nov 2026) — https://www.ad-hoc-news.de/boerse/news/corporate-news/at-und-s-stock-record-quarter-lifts-earnings-as-full-year-outlook-holds/70496565
- China Times, Unimicron Q3 2026 (28 Oct 2026) — https://www.chinatimes.com/realtimenews/20261028001621-260410
- cnyes, Unimicron Q3 2026 (Oct 2026) — https://news.cnyes.com/news/id/6638686
- vocus.cc, Unimicron Q3 2026 analysis (late Oct 2026) — https://vocus.cc/article/6ae2b2b0fd8978000150ef3d
- Wantrich / China Times, Unimicron broker report (28 Oct 2026) — https://wantrich.chinatimes.com/news/20261028900159-420101
- BigGo, Unimicron 29 Jul 2026 call — https://finance.biggo.com/quote/3037.TW/earnings-call/TW_3037.TW_2026-07-29
- CTEE, Nan Ya PCB Q3 2026 (6 Nov 2026) — https://www.ctee.com.tw/news/20261106700224-430502
- storm.mg, Kinsus/ABF (date not captured) — https://www.storm.mg/article/11165649
- Korea Herald, LG Innotek Q3 2026 (27 Oct 2026) — https://www.koreaherald.com/article/10916657
- Herald Business, LG Innotek FC-BGA at KPCA Show (Sep 2026) — https://biz.heraldcorp.com/article/10867093
- PRESS9, KB Securities on LG Innotek (Jun 2026) — https://www.press9.kr/news/articleView.html?idxno=77447
- fnnews, SKC Q3 2026 (28 Oct 2026) — https://www.fnnews.com/news/202610281435277261
- ZDNet Korea, SKC Q3 2026 (28 Oct 2026) — https://zdnet.co.kr/view/?no=20261028133954
- SBS Biz via Daum, SKC glass "Plan B" (29 May 2026) — https://v.daum.net/v/20260529115214214
- Sina Finance, Shennan Circuits 9M 2026 (23 Oct 2026) — https://finance.sina.com.cn/stock/aigc/agcbld/2026-10-23/doc-iniwcnvh5019323.shtml
- 10jqka, Shennan FC-BGA layers (1 Nov 2026) — http://stock.10jqka.com.cn/20261101/c681325519.shtml
- Eastmoney Caifuhao, Fastprint (Apr 2026) — https://caifuhao.eastmoney.com/news/20260414014428571468720
- The Elec, Ibiden Gama investment (30 Oct 2026) — https://www.thelec.net/news/articleView.html?idxno=15090
- Korea Herald, GlaSSEM JV (2 Jul 2026) — https://www.koreaherald.com/article/10796508
- RCRTech, NVIDIA capacity commitments (23 Oct 2026) — https://rcrtech.com/semiconductor-news/nvidia-supply-chain-capacity-commitments/

### Third-party financial statistics (quality fields only; fetched 12 Nov 2026)
- stockanalysis.com statistics pages, TTM — Ibiden https://stockanalysis.com/quote/tyo/4062/statistics/ ; Unimicron https://stockanalysis.com/quote/tpe/3037/statistics/ ; SEMCO https://stockanalysis.com/quote/krx/009150/statistics/ ; AT&S https://stockanalysis.com/quote/vie/ATS/statistics/ ; SKC https://stockanalysis.com/quote/krx/011790/statistics/ ; Ajinomoto https://stockanalysis.com/quote/tyo/2802/statistics/ ; Nittobo https://stockanalysis.com/quote/tyo/3110/statistics/ ; LG Innotek https://stockanalysis.com/quote/krx/011070/statistics/ ; Nan Ya PCB https://stockanalysis.com/quote/tpe/8046/statistics/ ; Kinsus https://stockanalysis.com/quote/tpe/3189/statistics/ ; Zhen Ding https://stockanalysis.com/quote/tpe/4958/statistics/ ; Daeduck https://stockanalysis.com/quote/krx/353200/statistics/

### Secondary — market, materials and glass
- TrendForce, Nittobo forecast and T-glass (6 Aug 2026) — https://www.trendforce.com/news/2026/08/06/news-nittobo-raises-fy2027-net-profit-forecast-by-jpy-3b-no-further-t-glass-price-hikes-planned/
- TrendForce, 18 Chinese glass-core players (7 Aug 2026) — https://www.trendforce.com/news/2026/08/07/news-18-chinese-enterprises-accelerate-positions-in-glass-core-substrate-market/
- TrendForce, Intel thick-core glass with EMIB (26 Jan 2026) — https://www.trendforce.com/news/2026/01/26/news-intel-reportedly-presents-first-thick-core-glass-substrate-with-emib-targeting-ai-data-centers/
- BigGo, TrendForce lead times (16 Sep 2026) — https://finance.biggo.com/news/02cf5c8f-c58d-45f8-a7a3-8fe37716bc8f
- thebuildout.ai, BofA on the ABF shortage (26 Mar 2026) — https://thebuildout.ai/intel/229c44f2-da57-4f46-b5fa-e5d03702236c
- MPBxChange, PCB material shortage 2026 (15 Oct 2026, updated 1 Nov 2026) — https://www.mpbxchange.com/research/pcb-material-shortage-2026-glass-cloth-copper-foil
- AtlasPCB, Ajinomoto ABF price increase (2026) — https://www.atlaspcb.com/news/news-ajinomoto-abf-substrate-price-increase-2026/
- FT Mercati, Ajinomoto China allocation (2026; unconfirmed) — https://www.ftmercati.com/en/ajinomoto-to-cut-abf-film-supply-to-china-by-30-amid-global-shortage-178875.html
- gate.com blog, ABF shortfall compilation (2026; low reliability) — https://www.gate.com/blog/why-abf-substrates-have-become-a-bottleneck-in-the-ai-gpu-supply-chain-2028-shortage-analysis
- Encyclopedia of Stocks (Substack), ABF shares (2026; low reliability) — https://encyclopediaofstocks.substack.com/p/abf-substrate-market-ai-driven-super
- DIGITIMES, four glass makers on 510×515 mm (1 Oct 2026) — https://www.digitimes.com/news/a20261001PD230/ai-chip-tsmc-corning-tgv-agc.html
- XenoSpectrum, Intel–Lens / BOE / CoPoS (29 Jul 2026) — https://xenospectrum.com/en/intel-lens-boe-glass-substrate-copos-tgv/
- IRZ, "Three years after Intel's promise…" (4 Sep 2026) — https://irz.fr/en/articles/verre-remplace-pas-encore-organique-en/
- MIT Technology Review, "Future AI chips could be built on glass" (13 Mar 2026) — https://www.technologyreview.com/2026/03/13/1134230/future-ai-chips-could-be-built-on-glass/
- vlsi.kr, glass-core race (20 Oct 2026, updated 1 Nov 2026) — https://www.vlsi.kr/en/glass-core-substrate-race-en/
- Slicast, Intel glass (9 Sep 2026; low reliability) — https://slicast.com/commentary/intel-2026-09-09
- TechTimes, BOE glass-core qualification (23 Sep 2026; seen via search summary) — https://www.techtimes.com/articles/327959/20260923/boe-completes-glass-core-substrate-qualification-ships-customers-chip-level-testing.htm
- Exponential Industry, glass-core guide (13 Aug 2026) — https://exponentialindustry.com/blog/2026-08-13-glass-core-substrates-ai-chip-packaging/
- GlobalSMT, CoWoP (2025) — https://www.globalsmt.net/advanced-packaging/nvidias-cowop-pcb-architecture-targets-abf-substrates-but-faces-warpage-risk/
- Business Standard, 3DGS Odisha (19 Apr 2026) — https://www.business-standard.com/industry/news/india-s-1st-advanced-3d-glass-chip-packaging-unit-to-come-up-in-bhubaneswar-126041900360_1.html
- DIGITIMES, Shinko delisting (21 Mar 2025) — https://apps.digitimes.com/news/a20250321PD206.html?chid=12
- Anantam IAS, Intel–Odisha MoU claim (2026; weak, unverified) — https://anantamias.com/current-affairs/india-3d-semiconductor-packaging-odisha-2026/

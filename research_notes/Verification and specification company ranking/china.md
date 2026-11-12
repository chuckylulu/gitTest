# China (mainland and Hong Kong): chip verification, sign-off tools and related fields

Research date: 12 November 2026; position as of that date. Final notes (this continuation pass completed earlier partial notes; every earlier fact, tag and URL is kept below, and no earlier fact was found to be wrong).

Tag key: [PRIMARY] filing or official document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] company statement not confirmed outside; [SECONDARY] press or analyst only; [UNVERIFIED] could not verify; [CALC] my own arithmetic on cited figures.

Source limits (read first):
- Most figures come from company filings downloaded directly from cninfo (巨潮资讯), the SSE STAR Market IPO database and HKEX lists. The filings are Chinese-language only; I read them by text extraction and keyword search, so tables were read selectively, not cover to cover.
- Search access failed part-way through: Exa and Firecrawl returned out-of-credit errors, and the shared WebSearch budget ran out after about eight searches. After that I used only direct fetches of known primary pages (cninfo, SSE, HKEX, eCFR, company websites, Tencent's public quote service) and URLs already found. Private companies, Chinese countermeasures, software proof in China and AI-native start-ups are therefore thinly covered; see Gaps.
- Facts resting only on Chinese-language sources: all cninfo filings, the SSE database, 科创板日报 / 财闻 / 界面 items, and UniVista's website. English-language sources: HKEX, eCFR, law-firm alerts, Investing.com, Tom's Hardware, TrendForce, Design & Reuse, S2C's website, Hugging Face, and the sibling notes on Synopsys, Cadence and Japan/Korea/Taiwan.

## 1. Map: who matters in China, by sub-segment

### Takeaway
Three listed EDA vendors lead China's field: Empyrean (the largest; analog, custom and flat-panel design, now adding digital sign-off; on the US Entity List and state-controlled), Primarius (device modelling and circuit simulation, now buying physical IP) and Semitronix (yield, DFM and test hardware). Around them sit private verification specialists (UniVista, X-Epic, S2C) and point-tool start-ups that Empyrean is buying stakes in. No Chinese firm shows a foundry-certified digital sign-off tool at an advanced node. Verification labour sits mainly in design-service houses (VeriSilicon, Brite).

### Cited Findings
**Market context**
- China EDA market 2024: about RMB 13.59bn, five-year CAGR 6.55% (中商产业研究院, cited in Semitronix's 2025 annual report, published 23 Apr 2026). [SECONDARY via PRIMARY] https://static.cninfo.com.cn/finalpage/2026-04-23/1225153967.PDF
- TrendForce 2024 global shares: Synopsys 32%, Cadence 29%, Siemens 13%; EE Times China says the three hold ">80%" in China (Design & Reuse, 5 Jan 2026). [SECONDARY] https://www.design-reuse.com/news/202529890-five-year-old-chinese-eda-firm-univista-sets-sights-on-ipo-led-by-ex-synopsys-and-cadence-team
- SemiAnalysis estimates (21 May 2026): PrimeTime holds over 90% of timing sign-off and Calibre over 85% of physical verification, both globally; emulation is a market of more than $1.5bn. [SECONDARY, cross-referenced from synopsys.md] https://newsletter.semianalysis.com/p/eda-market-primer
- Empyrean states its EDA market share is "first among domestic EDA firms". [COMPANY CLAIM] https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF

**Sub-segment 1: sign-off and formal verification tools**
- Empyrean 华大九天 (301269.SZ): analog/custom full flow (ALPS simulator), flat-panel full flow, and in 2025 four digital verification and sign-off tools: Hima Sim (simulation), Hima Time (static timing sign-off), Hima EMIR (power-integrity sign-off) and Argus SoC (physical-verification sign-off). It claims coverage of "80% of the main digital design tools" and HimaFormal Lint, a formal-based lint tool that supports military standard GJB-9765. [PRIMARY for what the company states; capability = COMPANY CLAIM] 2025 annual report (published 28 Apr 2026) https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF
- Primarius 概伦电子 (688206.SH): device modelling and verification tools that it says TSMC, Samsung, UMC, GlobalFoundries and SMIC use, and circuit simulation that it says Samsung, SK hynix and Micron use. [COMPANY CLAIM] https://static.cninfo.com.cn/finalpage/2026-04-16/1225108676.PDF . TSMC's EDA Alliance member list (as of 23 Sep 2026) includes Primarius; TSMC's certification grids (A14, A16, N2P, N3C and 3DFabric, as of 1 Oct 2026) list only Cadence, Synopsys and Siemens EDA. [PRIMARY: TSMC, cross-referenced from japan_korea_taiwan.md] https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- Semitronix 广立微 (301095.SZ): test-chip design, DFM sign-off, yield analytics (DATAEXP), DFT/ATPG (Quantest), wafer-level electrical (WAT) testers. [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-04-23/1225153967.PDF
- X-Times 芯行纪: digital implementation, including AmazeSys (described as "the first fully self-developed domestic digital place-and-route tool"), AmazeFP, the ML optimisers AmazeME-FP and AmazeME-Place, AmazeECO and AmazeDRCLite. Empyrean bought 6.90% for RMB 149.04m on 30 Sep 2026 "to quickly fill" its place-and-route gap, and says domestic place-and-route "still lags the international level". Empyrean already held 7.13% of another place-and-route developer, 亿方联创, bought in 2023. [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-08/1225597712.PDF
- Easy-Logic 奇捷科技: logic-optimisation (ECO) EDA used by "nearly 100" digital design firms [COMPANY CLAIM]; R&D centres in Shenzhen, Shanghai, Beijing and Hong Kong. 2025 revenue RMB 32.25m (2024: 27.42m); net loss RMB 19.39m (2024: 5.91m). On 30 Oct 2026 Empyrean's board approved buying up to 51% for up to RMB 220m; the agreement covers 50.3762% for RMB 218.83m, taking Empyrean to 73.87%. [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-11-02/1225650496.PDF
- Phlexing 行芯, Arcas 阿卡思, 国微芯, Giga Design Automation 鸿芯微纳, EnnoCAD 英诺达 and LEDA 立芯: I could retrieve no 2025-26 data. The SSE STAR IPO database shows no application from any of them (queried 12 Nov 2026). [PRIMARY database; otherwise UNVERIFIED] https://kcb.sse.com.cn/

**Sub-segment 2: emulation and prototyping hardware**
- UniVista 合见工软 (website fetched 12 Nov 2026): simulator UVS+, debugger UVD+, VPS verification management; emulation UVHS, UVHS-2 and UVHP; prototyping UV APS and PD-AS; virtual prototyping V-Builder; DFT Tespert (BSCAN, MBIST, SCAN, ATPG, DIAG, YIELD, IJTAG); 3DIC Designer; NodeClosure; AI platform UDA; Archer PCB; interface IP (PCIe Gen5, UCIe, HBM3/E, LPDDR5, DDR5, Ethernet, RDMA, UEC MAC). No formal-verification or verification-IP product is listed. News items: free trial of key EDA tools (3 Jun 2025), "Agent" strategy launch (1 Sep 2026), Quectel deploying Archer (6 Nov 2026). [COMPANY CLAIM] https://www.univista-isg.com/
- S2C 思尔芯 (website fetched 12 Nov 2026): Prodigy FPGA prototyping (S8 on AMD Versal Premium, S7 on Virtex UltraScale+, Stratix 10); claims "over 700 customers and more than 4,000 systems installed" and 90+ Prototype Ready IP; named cases BOSC (XiangShan RISC-V) and Artosyn. [COMPANY CLAIM] https://www.s2cinc.com/ . S2C's legal name in the SSE database is 上海国微思尔芯技术股份有限公司 [PRIMARY]; the name suggests a link to the 国微 group, but that is my inference from the name and was not checked.
- X-Epic 芯华章: its website is script-rendered and returned nothing; no STAR application found. Corigine 芯启源 and HyperSilicon 亚科鸿禹: no data retrieved; no STAR application found. [Gap]

**Sub-segment 3: verification components sold as IP**
- I found no Chinese verification-IP specialist. UniVista sells interface design IP, S2C sells prototyping daughter cards, and Primarius's acquisitions are physical design IP, not verification IP. [PRIMARY/COMPANY CLAIM as cited above]

**Sub-segment 4: AI-native chip-verification entrants**
- Moonshot AI's Kimi K3 (16 Jul 2026). According to Investing.com (17 Jul 2026), citing Moonshot's blog, K3 produced a 4 mm², 100 MHz design on 45nm with the open Nangate cell library, from "RTL to tape-out simulation", using "exclusively open-source tools" that were not named. No fabrication, foundry or sign-off was reported. Bloomberg Intelligence saw "no immediate threat" to Cadence and Synopsys revenue. [SECONDARY] https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775
- Incumbents' AI products: Empyrean's LLM agent PyAether Aether Coder (2025 annual report); UniVista's UDA and its Agent strategy (Sep 2026); S2C's AI-assisted RISC-V verification (26 Oct 2026). [COMPANY CLAIM] URLs as above.
- iEDA (open source, MulanPSL-2.0 licence): "open-source EDA infrastructure and tools from netlist to GDS", 11 tools, claims "4 times tape-out" without detail; 561 stars and 4,865 commits (fetched 12 Nov 2026). The repository page does not name the developing institution. [COMPANY CLAIM / PRIMARY repository] https://github.com/OSCC-Project/iEDA
- I verified no venture-funded Chinese AI-native verification start-up. [Gap]

**Sub-segment 7: verification services (labour)**
- VeriSilicon 芯原 (688521.SH): order backlog RMB 18.569bn at end-Sep 2026 (+265.90% on end-2025), over RMB 15bn of it mass-production services and more than 81% data-processing work, mainly AI ASICs; new orders from 1 Jan to 30 Oct 2026 RMB 17.174bn, more than 83% AI-compute. [PRIMARY] Q3 report (published 31 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-31/1225649712.PDF
- Brite 灿芯 (688691.SH): backlog RMB 903m at 30 Sep 2026 (design RMB 392m, mass production RMB 511m). [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-30/1225639403.PDF
- Empyrean's and Primarius's own service lines are covered in section 3.

**Deals, state money, IPO pipeline**
- Empyrean–Xpeedic 芯和: framework agreement of 28 Mar 2025 with 35 counterparties to buy 100% for shares plus cash, a related-party major restructuring (Empyrean's shares were suspended from 17 Mar 2025). Terminated 9 Jul 2025 because the parties "did not agree core terms". [PRIMARY] https://static.cninfo.com.cn/finalpage/2025-07-09/1224119966.PDF . On 13 Oct 2026 Empyrean also terminated a related-party investment in the 合肥中湾聚芯 fund (title only read). [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-13/1225604132.PDF
- Primarius bought 100% of 锐成芯微 (physical IP) for RMB 1.90bn and 45.64% of 纳能微 (interface IP) for RMB 274m, paid in shares plus cash. Equity transfers completed in July 2026 and were announced 14 Aug 2026; both are now wholly owned. Primarius says the two work with "30+ foundries" and hold "1,000+ physical IP" sets. [COMPANY CLAIM] https://www.caiwennews.com/article/1552968.shtml . Supporting-fundraising shares were registered on 3 Sep 2026, taking total shares from 435,177,853 to 531,014,050. [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-31/1225648713.PDF . Jiemian says 锐成芯微 failed two IPO attempts, its 2024 profit fell sharply and the earn-out is loose. [SECONDARY, opinion] https://m.jiemian.com/article/13434279.html
- State ownership of Empyrean at 30 Sep 2026: China Electronics Co (中国电子有限公司) 21.03%; 九创汇新 14.85%; 中电金投 13.72%; National IC Fund (Big Fund I) 6.97%; 上海建元 4.98%; HKSCC 1.55%. [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-30/1225641220.PDF . After the December 2024 Entity Listing, Empyrean's board handed control to China Electronics Corp, which took 6 of 11 seats. [SECONDARY] https://www.tomshardware.com/tech-industry/empyrean-technology-gives-control-to-cec-after-u-s-blacklisting-chinas-top-developer-of-chip-design-systems-hands-reins-to-state-owned-firm
- IPO pipeline:
  - UniVista filed for IPO tutoring on 26 Dec 2025 (EE Times China via Design & Reuse). [SECONDARY] URL above.
  - Xpeedic completed A-share IPO tutoring registration with CITIC Securities (科创板日报, 10 Feb 2025). Its investors include SMIC's 中芯聚源 (from 2015), SAIC's 尚颀资本 and Shanghai Urban Construction; its last round was in Oct 2022. [SECONDARY] https://www.cls.cn/detail/1938403
  - S2C's STAR application (filed 24 Aug 2021; planned raise field "10", i.e. RMB 1.0bn) shows status code 8 with a last update on 28 Jul 2022. The same code appears for 锐成芯微's 2022 application, which press reports describe as failed, while listed Primarius and Brite show code 5 with registration effective. I read code 8 as "terminated". [PRIMARY database; reading = my inference] https://kcb.sse.com.cn/

### Inferences
- Scale [CALC, at an assumed RMB 7.1–7.3 per US$, illustrative]: Synopsys's FY2025 China revenue ($814.3m) plus Cadence's ($680.0m) is about 8 times Empyrean's total 2025 revenue (RMB 1,325m, about $182–187m).
- Domestic share [CALC, rough]: Empyrean's 2024 revenue was about 9% of the RMB 13.59bn market; the three listed vendors' EDA-related revenue together was about 13% at most (this figure includes services and hardware).
- The map is very thin in formal verification, verification IP, specification and software proof. China has no visible owner of a specification that others must pass.
- Consolidation is led by state-anchored Empyrean through minority stakes and small buyouts, and by Primarius through a large IP purchase.

### Gaps
- X-Epic, Phlexing, Arcas, 国微芯, Giga Design Automation, Corigine, HyperSilicon, EnnoCAD and LEDA: products, revenue, latest funding round and valuation could not be retrieved (search budget exhausted). Their sub-segment placement is not verified in this pass.
- No Hong Kong IPO filings for Chinese EDA firms were checked (HKEXnews was not searched).

## 2. Software proof and specification tools in China

### Takeaway
China's visible machine-checked proof work comes from AI labs that publish open models for mathematics (DeepSeek, Moonshot with Numina, ByteDance). I found no evidence that anyone sells machine-checked proof for software as a product, and no notable Chinese requirements or specification tool vendor. Coverage is thin because the search budget ran out.

### Cited Findings
- DeepSeek-Prover-V2-671B, a formal theorem-proving model, is on Hugging Face (updated 30 Apr 2025; 31.3K downloads; DeepSeek-V3 architecture). [PRIMARY: model card overview; proof language not read] https://hf.co/deepseek-ai/DeepSeek-Prover-V2-671B
- Kimina-Prover-72B is published by Project Numina (fine-tuned from Qwen2.5-72B; MIT licence; updated 10 Jul 2025). The "Kimina" name and a "Moonshot-Math" demo space suggest Moonshot's Kimi team is involved, but the card overview does not confirm it. [PRIMARY: model card; Moonshot link UNVERIFIED] https://hf.co/project-numina/Kimina-Prover-72B
- Empyrean's HimaFormal Lint supports GJB-9765, a military standard, which suggests defence buyers for formal-style checks. [COMPANY CLAIM] https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF

### Inferences
- These provers are free research releases that prove mathematics, not software; any revenue sits inside each lab's model business. That fits transition (7), model makers offering verification themselves, more than (6), a paid market for verified software.

### Gaps
- Not verified: ByteDance Seed-Prover (repository not reachable from this session); Huawei's formally verified kernel work and its certifications; Ant Group; CertiK's China and Hong Kong operations; university spin-offs; Chinese requirements-tool vendors.

## 3. Business quality, tests a–e (independent of share price)

### Takeaway
Empyrean and Primarius own real but narrow verdicts: analog, custom and flat-panel sign-off inside China for Empyrean, and device models in foundry PDKs worldwide for Primarius. Both make core operating losses, depend on subsidies and fair-value gains for reported profit, and saw labour-style service revenue grow faster than licences in 2025-26. Semitronix is profitable but hardware-heavy and highly concentrated. The private verification firms cannot be scored on public data.

### Cited Findings
#### Empyrean (301269.SZ)
- **Latest results.** 2025 annual report (published 28 Apr 2026) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF :
  - Revenue RMB 1,324.98m (+8.40%; 2024: 1,222.35m; 2023: 1,010.40m).
  - Net profit attributable RMB 60.98m (-44.30%); after non-recurring items RMB -9.80m.
  - Operating cash flow RMB 560.65m.
  - Revenue mix: EDA software sales RMB 1,074.51m (81.10%, -1.63%); technical services RMB 201.28m (15.19%, +74.93%, gross margin 44.64%); hardware, agency and other RMB 49.18m (3.71%).
  - Domestic 90.09%, overseas 9.91%.
  - Top-5 customers 30.58% of sales (largest 18.68%); related-party share of top-5 sales 0.00%.
  - R&D RMB 859.18m (64.84% of revenue), none capitalised.
  - Other income RMB 149.65m; share-based payment RMB 145.13m.
  - Staff 1,460, of whom 1,077 in R&D.
- **2026 interim** (published 29 Aug 2026) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-08-29/1225525615.PDF :
  - H1 revenue RMB 566.46m (+12.95%): EDA software RMB 434.39m (+4.89%); technical services RMB 103.47m (+53.88%, gross margin 46.37%).
  - Completed adaptation to Hygon's DCU accelerators.
  - Says domestic analog, memory, RF and panel EDA "can fully support 14nm and below". [COMPANY CLAIM]
- **Q3 2026** (published 30 Oct 2026, unaudited) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-30/1225641220.PDF :
  - Q3 revenue RMB 393.67m (+29.82% y/y); 9M revenue RMB 960.13m (+19.30%).
  - 9M net profit attributable RMB 26.93m (+197.28%); after non-recurring items RMB -30.95m.
  - 9M operating cash flow RMB -111.77m (prior year +184.61m).
  - 9M R&D expense RMB 629.94m; 9M other income (mostly subsidies and VAT refunds) RMB 128.35m.
  - Balance sheet at 30 Sep 2026: cash RMB 757.7m; trading financial assets RMB 551.7m; short-term borrowings RMB 250.1m; goodwill RMB 45.7m; total assets RMB 6,253.9m; equity RMB 5,384.7m.
  - Q3 cost of sales +40.17%, "mainly because technical-service revenue rose".
- **a. Position.**
  - Foundry certifications: ALPS circuit simulator at 8nm/5nm/4nm, Patron transistor-level power integrity at 14nm, Argus DRC/LVS at 28nm. The foundries are not named. [COMPANY CLAIM]
  - Its own PDKs cover more than 70% of domestic foundry process nodes. [COMPANY CLAIM] 2025 annual report URL above.
  - Digital sign-off tools launched only in 2025; the plan is still to "strive to complete the digital full flow". [PRIMARY]
  - Its risk factor says lower urgency for domestic substitution "may affect" the business, so the company itself ties its position to policy. [PRIMARY]
- **b. Lead.**
  - Outside evidence is limited to the US Entity Listing on 2 Dec 2024 (one of 140 entities; covers subsidiaries, per TrendForce) [SECONDARY] https://www.trendforce.com/news/?p=26942 , and to scale, as Empyrean is the largest domestic vendor by revenue [PRIMARY figures].
  - No TSMC certification [PRIMARY: TSMC grids]; no published third-party benchmark found.
- **c. Revenue model.** 81% of revenue is software, but services grew 75% in 2025 and 54% in H1 2026 and reached 18.3% of H1 revenue [CALC]. Licence term and recognition split not read. [Gap]
- **d. Financial strength** [CALC from primary figures]:
  - Core business loss-making in 2025 and in 9M 2026.
  - Other income was 2.45 times net profit in 2025 and 4.8 times in 9M 2026.
  - Trailing return on equity about 1.5%.
  - Net cash plus liquid investments about RMB 1.06bn.
  - Customer concentration moderate; 90% domestic; anchored by state shareholders (above).
  - Accounting is conservative: R&D at 65.6% of 9M 2026 revenue, all expensed.
- **e. Resilience.** See sections 4 and 5. The 2025 annual report does not name the Entity List (keyword search of the full text); it carries only a generic "international trade friction" risk citing 9.91% overseas revenue. [PRIMARY]

#### Primarius (688206.SH)
- **2025 annual report** (published 16 Apr 2026) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-04-16/1225108676.PDF :
  - Revenue RMB 483.67m (+15.41%).
  - Net profit attributable RMB 34.24m (2024: -95.97m); after non-recurring items RMB -59.57m.
  - Operating cash flow RMB +137.76m (2024: -46.52m).
  - Main-business revenue RMB 476.34m:
    - EDA licences RMB 313.94m (65.91%): design EDA RMB 190.98m (+29.78%), manufacturing EDA RMB 122.96m (+11.71%).
    - Device characterisation test systems (hardware) RMB 77.01m (16.17%, -34.41%, gross margin 71.55%).
    - Technical development services RMB 85.39m (17.93%, +100.97%, gross margin 57.51%).
  - Domestic 76.24% (gross margin 85.00%); overseas RMB 113.19m (gross margin 96.71%; US, Korea, Taiwan, Europe, Japan).
  - Top-5 customers 35.81% (largest 10.45%), related parties 0%.
  - R&D RMB 326.39m (67.48% of revenue), of which RMB 18.73m (5.74%) capitalised; R&D staff 73.19% of headcount.
  - Government subsidies in non-recurring items RMB 43.90m; fair-value gains RMB 51.77m.
  - Admits its product breadth "clearly lags" Synopsys, Cadence and Siemens EDA.
- **2026 interim** (published 27 Aug 2026) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-08-27/1225514208.PDF :
  - H1 revenue RMB 240.39m (+10.05%): EDA licences RMB 160.41m (+8.07%; design RMB 95.10m +15.51%, manufacturing RMB 65.32m); test systems RMB 30.46m (+31.12%); technical development RMB 49.36m (+6.41%).
  - Domestic share 80.10% of main-business revenue.
  - Net profit attributable RMB -6.73m; after non-recurring items RMB -20.06m; operating cash flow RMB -50.71m.
  - R&D RMB 134.48m (55.94%, -7.49%).
  - New strategy: "EDA tools + semiconductor IP" dual engine.
- **Q3 2026** (published 31 Oct 2026, unaudited) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-31/1225648713.PDF :
  - Q3 revenue RMB 177.38m (+84.45%, with the acquired IP firms now consolidated); 9M revenue RMB 417.77m (+32.79%).
  - 9M net profit attributable RMB 0.66m; after non-recurring items RMB -24.90m; operating cash flow RMB -52.29m.
  - Goodwill RMB 1,226.4m (from RMB 162.2m); total assets RMB 4,973.2m.
- **a. Position.** Device models feed the foundry PDKs that every simulator uses, which makes this the most judge-like position among Chinese vendors. TSMC lists Primarius as an EDA Alliance member [PRIMARY: TSMC]. The named customers at global foundries and memory makers are a company claim.
- **b. Lead.** TSMC membership; overseas revenue of 24% at a 96.7% gross margin is consistent with sales to global foundries (inference). No share data found.
- **c. Revenue model.** About two-thirds licences, about one-sixth one-off hardware, about one-sixth services; services doubled in 2025. The IP businesses add licence and royalty income (split not yet disclosed).
- **d. Financial strength** [CALC]:
  - Core losses in 2025 and 9M 2026.
  - Subsidies equalled 128% of 2025 net profit.
  - Goodwill is now 24.7% of total assets.
  - Share count up 22.0% from the acquisition shares.
- **e. Resilience.** I found no mention of the Entity List or export controls in the 2025 or 2026 interim reports (keyword search). Overseas sales of 24% are exposed if US pressure reaches its foreign customers.

#### Semitronix (301095.SZ)
- **2025 annual report** (published 23 Apr 2026) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-04-23/1225153967.PDF :
  - Revenue RMB 734.98m (+34.40%).
  - Net profit attributable RMB 88.69m (+10.49%); after non-recurring items RMB 43.64m (-25.30%).
  - Operating cash flow RMB -121.78m.
  - Software development and licensing RMB 278.10m (37.84%, +75.13%, gross margin 69.95%); test equipment and accessories RMB 453.32m (61.68%, +17.30%, gross margin 50.42%); test services RMB 3.56m.
  - Domestic 97.00%.
  - Top-5 customers 72.37%, related parties 0%.
  - R&D RMB 302.77m (41.19% of revenue); R&D staff 672 (81.36%).
  - Government subsidies in other income RMB 52.47m.
  - First overseas sale of its big-data software in 2025; customers named include Samsung, SK hynix and "a leading domestic foundry". [COMPANY CLAIM]
- **Q3 2026** (published 28 Oct 2026) [PRIMARY] https://static.cninfo.com.cn/finalpage/2026-10-28/1225630347.PDF :
  - Q3 revenue RMB 241.22m (+32.71%); 9M RMB 582.29m (+36.14%).
  - 9M net profit attributable RMB 71.52m (+93.22%); after non-recurring items RMB 21.51m.
  - 9M operating cash flow RMB +102.02m.
  - Cash RMB 840.7m; goodwill RMB 285.8m; short-term borrowings RMB 134.1m; 9M other income RMB 40.74m.
- [CALC] Subsidies equalled 59% of 2025 net profit; other income equalled 57% of 9M 2026 net profit.
- **Tests in brief.** (a) Its verdict concerns process yield rather than design correctness. (c) 62% of revenue is hardware. (d) Very high customer concentration. (e) Tied to China's fab-capital-spending cycle.

#### UniVista, X-Epic, S2C (data-limited)
- UniVista: product list as in section 1. Funding: 36Kr lists an undisclosed A++ round (Nov 2025) and 2021 rounds; a separate 36Kr report describes a Pre-A round of more than RMB 1.1bn backed by SAIC's 尚颀资本, IDG and 国科投资 (undated). [SECONDARY] https://pitchhub.36kr.com/project/1958566457955330 . No financial statements found.
- S2C: 700+ customers claimed; one-off prototyping hardware model; STAR IPO terminated in 2022 (my reading of the SSE code).
- X-Epic: nothing retrievable.

#### VeriSilicon and Brite (verification as labour inside design services)
- VeriSilicon 9M 2026 [PRIMARY] (URL in section 1):
  - Revenue RMB 3,180.81m (+41.08%; Q3 RMB 1,317.27m, +2.85%).
  - Net profit attributable RMB -869.25m; adjusted RMB -572.04m.
  - Operating cash flow RMB +1,126.56m; R&D RMB 1,407.36m.
  - Domestic 72.35%; system makers, internet and cloud customers about 30%.
  - Guides adjusted EBITDA positive in H2 2026 and adjusted net profit positive in 2027. [COMPANY CLAIM]
- Brite 9M 2026 [PRIMARY] (URL in section 1):
  - Revenue RMB 626.87m (+33.92%).
  - Net profit attributable RMB -109.06m; operating cash flow RMB -61.52m.
  - R&D RMB 113.29m (18.07% of revenue, -15.12%).

### Inferences
- Provisional scoring (my judgment, H = strong, M = moderate, L = weak):

  | Company | a. Position | b. Lead | c. Revenue model | d. Financial strength | e. Resilience |
  |---|---|---|---|---|---|
  | Empyrean | M in China | L–M | M, drifting toward services | L–M | M (policy-supported, Entity-Listed) |
  | Primarius | M–H in a narrow niche | M | M | L (goodwill, losses) | M |
  | Semitronix | L–M for this ranking | M in China | L–M (hardware) | M | M (cyclical) |

- At all three, reported profit depends on subsidies, VAT refunds or investment gains; the underlying businesses run at a loss or break even.

### Gaps
- Licence term structure (time-based versus perpetual) and deferred revenue for all three.
- Identity of Empyrean's largest customer (18.68% of sales).
- The foundries behind Empyrean's 4nm, 5nm and 8nm certifications.
- Independent China market-share data by tool category.
- Private companies' financials.

## 4. Export controls: what happened, how demand responded, judge or gap

### Takeaway
The US cut off EDA licensing to China only briefly (May to July 2025), and the 50% Affiliates Rule has been suspended twice, now until 10 Jan 2027. Synopsys's China revenue fell 22% (excluding Ansys) in FY2025, while Cadence's China share was 16% in Q3 2026 against 13% for FY2025. Chinese vendors kept growing at 19–36% in 2026. The evidence says most of the Chinese vendors' position is a gap created and protected by policy, not a verdict others must pass. The exceptions are Primarius's global device-model niche and Empyrean's flat-panel and analog franchise.

### Cited Findings
- Empyrean was added to the Entity List on 2 Dec 2024, one of 140 Chinese entities. [SECONDARY] Tom's Hardware and TrendForce URLs above. The BIS list file could not be read (a bot-check page was returned).
- From Cadence's FY2025 10-K [PRIMARY, cross-referenced from cadence.md] https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf :
  - BIS imposed a licence requirement for EDA sales to China on 23 May 2025 and rescinded it on 2 Jul 2025.
  - The Affiliates Rule took effect 29 Sep 2025 and was suspended on 11 Nov 2025.
  - Cadence pleaded guilty to conspiracy to violate export controls (violations 2015–2021 on $45.3m of sales; $140.6m paid in Q3 2025).
- The Affiliates Rule suspension was extended to 10 Jan 2027 by a rule published 9 Nov 2026, effective on publication. It is tied to the "Busan agreement" and to the trade truce extended in late September 2026. Absent further action, the rule's licence requirements take effect on 10 Jan 2027. China has criticised the rule. [SECONDARY: law-firm summaries] Skadden, 11 Nov 2026 https://www.skadden.com/insights/publications/2026/11/bis-extends-suspension-of-affiliates-rule ; Nixon Peabody, 6 Nov 2026 https://www.nixonpeabody.com/insights/alerts/2026/11/06/bis-formally-suspends-the-affiliates-rule-until-january-10-2027 ; Baker McKenzie https://sanctionsnews.bakermckenzie.com/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027/ . Law-firm alerts warn that the rule and China's rare-earth controls could both take effect in January 2027 without a permanent deal. [SECONDARY]
- Big three in China:
  - Synopsys FY2025 China revenue $814.3m (12%) versus $989.5m (16%) in FY2024; down 22% excluding Ansys. Its 10-K mentions BIS administrative subpoenas about transactions with certain Chinese entities. [PRIMARY, via synopsys.md] https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf ; https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm
  - Cadence China $680.0m (13%) in FY2025, 16% of revenue in Q3 2026. [PRIMARY, via cadence.md] https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm
- Domestic response:
  - UniVista offered free trials of key EDA tools on 3 Jun 2025, during the cut-off. [COMPANY CLAIM]
  - Primarius's domestic main-business revenue rose 19.38% in 2025 and 16.22% in H1 2026. [PRIMARY]
  - Empyrean's 9M 2026 revenue rose 19.30% (Q3 +29.82%), but its EDA software grew only 4.89% in H1 2026. [PRIMARY]

### Inferences
- The six-week cut-off showed that US vendors can be switched off, which is the strongest policy argument for domestic tools. It was reversed quickly, however, and Cadence's China share reached 16% by Q3 2026, so Chinese customers still buy the big three's sign-off tools where they can.
- If the 10 Jan 2027 deadline passes without another suspension, entities at least 50% owned by Entity-Listed parties would be caught. Empyrean's majority-owned subsidiaries, and Easy-Logic once Empyrean owns 73.87% of it (Easy-Logic has a Hong Kong R&D centre), would then need US licences for items subject to US export rules. This is my reading of the rule's mechanics, not legal advice and not verified.
- Easing that let Synopsys and Cadence in fully would hit Empyrean's digital tools hardest, because they are new and uncertified. It would hit Primarius's modelling niche least, because that niche already competes globally.

### Gaps
- Chinese countermeasures (MOFCOM investigations, unreliable-entity actions, any rule requiring domestic EDA): not verified in this pass.
- US rules on advanced-node EDA (for example GAAFET-related controls) as they stand in 2026: not verified.
- Effects on prices: no data found.

## 5. Path forward: transitions, said versus done, funding and provisional verdicts

### Takeaway
The listed Chinese vendors are funded, through state shareholders, cash and share issuance, and they are executing deals. Their main transitions are (5) foundry certification without TSMC or Samsung design kits, (1) moving from labour to tools, and (4) open-source and AI substitution. On (1) the evidence points the wrong way, and on (5) there is no outside evidence of progress at advanced nodes.

### Cited Findings
- **Empyrean, said versus done.**
  - Done: launched four digital verification and sign-off tools in 2025; spent RMB 859m on R&D in 2025, all expensed; bought minority stakes in place-and-route developers (X-Times 6.90% for RMB 149.04m, 30 Sep 2026; 亿方联创 7.13% in 2023); is buying a majority of Easy-Logic for RMB 218.83m (approved 30 Oct 2026); completed Hygon DCU adaptation. [PRIMARY]
  - Failed: the Xpeedic acquisition (terminated 9 Jul 2025). [PRIMARY]
  - Said: "80%" digital coverage; "strive to complete" the digital full flow; 4nm simulator certification. [COMPANY CLAIM]
  - Funding: cash plus trading assets of RMB 1.31bn and equity of RMB 5.38bn; operating cash flow negative in 9M 2026. [PRIMARY]
- **Primarius, said versus done.**
  - Done: RMB 2.174bn of IP acquisitions completed July–August 2026; R&D cut 7.49% in H1 2026. [PRIMARY]
  - Said: "EDA tools + semiconductor IP" synergy; 30+ foundries for the IP. [COMPANY CLAIM]
- **Semitronix.** Software revenue +75% in 2025 [PRIMARY]; first overseas big-data software sale [COMPANY CLAIM].
- **Open source and AI.**
  - Kimi K3: open-source tools at 45nm, not fabricated. [SECONDARY]
  - iEDA: open source, with four tape-outs claimed. [COMPANY CLAIM]
  - On 17 Jul 2026, the day after the K3 announcement, Chinese names fell: Empyrean -8.2%, Primarius -11.4% (-9.6% on 20 Jul), Semitronix -11.4% (-11.9% on 20 Jul), VeriSilicon -4.9%, Brite -16.4%. [SECONDARY: Tencent daily prices] All five were already falling on 13–16 July, so the cause is not established.

### Inferences (provisional judgments, mine)
- **Empyrean: partly coherent.**
  - Its analog, flat-panel and domestic-PDK base is real and funded, and it is plausibly the default domestic sign-off supplier for mature-node Chinese designs within 3–5 years.
  - Full digital sign-off at advanced nodes depends on Chinese foundries' advanced nodes and on its partners (X-Times, Easy-Logic), with no outside qualification yet.
  - Transition (1) is going backwards, as services grow faster than licences.
  - What must go right: accredited digital sign-off at SMIC or Huawei-ecosystem nodes, adopted by leading Chinese AI chip makers, and controls staying in place.
- **Primarius: partly coherent.**
  - The device-modelling niche passes transition (5) better than any Chinese peer, as TSMC lists it as an alliance member.
  - The IP pivot moves it away from verification, adds RMB 1.2bn of goodwill and leaves the earn-out quality questioned.
  - Its timing depends on integrating 锐成芯微.
- **Semitronix: coherent within yield and DFM**, but marginal to this ranking. Hardware cyclicality is the key risk.
- **UniVista: cannot be judged (low confidence, leaning partly coherent).** It has the broadest domestic verification portfolio and an Agent strategy, and has started the IPO process, but no financials are available.
- **X-Epic and S2C: not assessable.** S2C's one-off hardware model and its terminated IPO weigh against it.
- **VeriSilicon and Brite** are labour and design services. VeriSilicon's AI-ASIC backlog shows demand flowing to services, not tools.

### Gaps
- R&D programmes and capital committed to formal verification (transition 3) at any Chinese firm.
- Any usage-based pricing (transition 2).
- Pricing and adoption of AI agents.
- Technical report on Kimi K3 (due 27 Jul 2026, not read).

## 6. Entry point and investor access (separate from the quality evidence)

### Takeaway
On trailing sales, Empyrean (about 33x) and Primarius (about 30x) are priced at two to three times the big three's multiples, though below their own end-2023 and end-2024 levels. Semitronix (about 12.7x) is in line with the big three. All five listed names are buyable northbound through Stock Connect. US persons may buy listed shares under the outbound-investment rule, but not private rounds in Chinese EDA developers.

### Cited Findings
- **Prices on 12 Nov 2026** (Tencent quote service; P/E figures reconciled to filed profits) [SECONDARY: market-data vendor] https://qt.gtimg.cn/q=sz301269,sh688206,sz301095,sh688521,sh688691 :
  - Empyrean RMB 89.92; market cap RMB 49.27bn; trailing P/E 624.7x; P/E on FY2025 807.8x; P/B 9.15.
  - Primarius RMB 32.91; total cap RMB 17.48bn (free float RMB 14.37bn); P/B 4.28; trailing P/E negative.
  - Semitronix RMB 56.35; total cap RMB 11.29bn (float RMB 9.83bn); trailing P/E 91.6x; P/E on FY2025 127.3x; P/B 3.55.
  - VeriSilicon RMB 116.43; cap RMB 61.23bn; P/B 22.2.
  - Brite RMB 55.42; total cap RMB 6.65bn (float RMB 4.04bn).
- **Price history** (monthly, since listing) https://web.ifzq.gtimg.cn/appstock/app/fqkline/get?param=sz301269,month,2019-01-01,2026-11-12,120,qfq :
  - Empyrean: high 154.70 (Nov 2024); low 67.46 (Jul 2022, listing month); year-end closes 89.47 (2022), 105.40 (2023), 120.80 (2024), 106.18 (2025).
  - Primarius: high 56.05 (Dec 2021); low 12.04 (Feb 2024).
  - Semitronix: high 160.72 (Aug 2022); low 33.90 (Sep 2024).
  - VeriSilicon: high 375.67 (Jun 2026); October 2026 close 98.19.
  - Brite: high 168.58 (Jan 2026).
- **Multiples against own history** [CALC; year-end shares approximated]:
  - Empyrean trailing revenue (12 months to 30 Sep 2026) RMB 1,480m. P/S about 33.3x now (EV/S 32.6x), against about 56.9x at end-2023, 53.9x at end-2024 and 43.7x at end-2025.
  - Primarius trailing revenue RMB 587m, understated because the IP firms are consolidated only from Jul–Aug 2026. P/S about 29.8x, against about 28.8x, 19.6x and 31.3x at end-2023, 2024 and 2025.
  - Semitronix trailing revenue RMB 890m. P/S about 12.7x (EV/S about 11.9x), against about 31.0x, 18.9x and 19.5x at end-2023, 2024 and 2025.
- **Peers** (StockAnalysis, 12 Nov 2026) [SECONDARY, via sibling notes]: Synopsys EV/sales 10.17x, trailing P/E 81.94x, forward 26.26x https://stockanalysis.com/stocks/snps/statistics/ ; Cadence EV/sales 14.94x, trailing P/E 65.47x, forward 34.94x https://stockanalysis.com/stocks/cdns/statistics/ ; Cadence's 10-year median P/S is 13.3x https://companiesmarketcap.com/cadence-design-systems/ps-ratio/
- **Growth the price assumes** [CALC, illustrative, at a constant share price]:
  - Empyrean's enterprise value of RMB 48.2bn needs revenue of RMB 3.24bn (2.2 times trailing) to trade at Cadence's 14.9x, or RMB 4.73bn (3.2 times) to trade at Synopsys's 10.2x. That is about 4.3–6.4 years at 20% annual growth, or 5.6–8.3 years at 15%.
  - Primarius needs revenue 2.0–2.9 times trailing. Semitronix already trades below Cadence's multiple and needs 1.24 times trailing revenue to reach Synopsys's.
  - Caveat: the Chinese figures are P/S or simple EV/S, while the US figures are EV/sales.
- **Lock-ups, deals and capital actions.**
  - Restricted share of total cap [CALC]: Primarius about 18% (restricted holders include 向建军 with 25.13m shares and the 国投创业 fund with 24.41m); Brite about 39%; Semitronix about 13%. Expiry dates not read. [PRIMARY holder tables; lock-up terms = Gap]
  - Empyrean–Easy-Logic purchase pending.
  - Semitronix's controlling holder proposed a buyback on 5 Nov 2026 https://static.cninfo.com.cn/finalpage/2026-11-05/1225657737.PDF ; his share-reduction plan had ended on 14 Sep 2026 https://static.cninfo.com.cn/finalpage/2026-09-14/1225563863.PDF .
  - VeriSilicon completed a buyback (31 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-31/1225649735.PDF and announced a senior-manager share-reduction plan (24 Sep 2026) https://static.cninfo.com.cn/finalpage/2026-09-24/1225578972.PDF . [PRIMARY titles, cninfo]
- **Access.**
  - HKEX's China Connect lists "eligible for both buy and sell", updated 12 Nov 2026, include Empyrean (301269), Semitronix (301095), Primarius (688206), VeriSilicon (688521) and Brite (688691). [PRIMARY] https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities?sc_lang=en
  - Stock Connect nominee holdings (HKSCC) at 30 Sep 2026: Empyrean 8.50m shares (1.55%); Semitronix 5.29m; VeriSilicon 10.37m (1.97%); Brite 1.60m (1.33%); HKSCC is not in Primarius's top 10. Primarius's top holders are founder 刘志宏 (foreign natural person) 13.19%, KLProTech H.K. 11.38% and 共青城明伦 4.82%. [PRIMARY] Q3 reports cited above.
  - The holder tables list only RMB ordinary (A) shares; I found no Hong Kong listing.
- **US persons.**
  - 31 CFR 850.224(a) prohibits transactions with a covered foreign person that "Develops or produces any electronic design automation software for the design of integrated circuits or advanced packaging". [PRIMARY] https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII/part-850
  - 31 CFR 850.501(a)(1)(i) excepts investment "In any publicly traded security" on an exchange or over the counter in any jurisdiction, unless it gives rights "beyond standard minority shareholder protections". [PRIMARY] Same URL.
  - BIS Entity List records set a licence requirement "for all items subject to the EAR", typically with a presumption of denial; they concern exports, not securities. [PRIMARY, partial read] https://www.bis.gov/media/documents/entity-list-faqs-11.10.2025.pdf
- **Private valuations.**
  - Easy-Logic implied about RMB 434m for 100%, about 13.5x 2025 sales [CALC from the Empyrean filing].
  - X-Times implied about RMB 2.16bn for 100% [CALC].
  - UniVista, X-Epic, S2C and others: no valuation found.

### Inferences
- The A-share EDA multiples look like a premium for domestic substitution rather than a reflection of profits. All three EDA names are priced on sales, as profits are close to zero.
- Foreign holders are present but small (1–2% through Stock Connect).
- For US persons, buying listed shares appears to be allowed, while private rounds in Chinese EDA developers appear to be prohibited. Whether CEC or Empyrean sits on OFAC's NS-CMIC list or the DoD 1260H list, either of which would add restrictions, is unchecked.

### Gaps
- Index changes; ETF holdings; QFII limits; NS-CMIC and 1260H status; lock-up expiry dates; whether any of these firms plans an H-share listing.

## 7. Synthesis: global relevance, what could not be verified, contradictions, sources

### Takeaway
Provisionally, no Chinese company belongs among the 8 to 15 that matter most globally for owning the verdict on correctness. If the ranking wants the strongest non-Western contender, Empyrean is the candidate on scale and state backing, and Primarius on the most genuinely judge-like global niche, device models in foundry PDKs. Both fail the financial-strength test.

### Cited Findings
- Evidence for this view is cited in sections 1 to 6: TSMC certification grids carry only the big three; there are core losses and subsidy-dependent profits; services are growing faster than licences; the policy-dependence risk is stated in Empyrean's own filing; and the big three's China revenue has persisted.

### Inferences
- **Global top 8–15 (provisional, mine).**
  - Empyrean: a borderline wildcard whose verdict ownership is real only inside China and is protected by policy.
  - Primarius: a niche mention.
  - Semitronix, UniVista, X-Epic, S2C, VeriSilicon and Brite: no.
- **Where the evidence contradicts "tools that own a verdict keep their position while labour loses it".**
  1. In China, labour is gaining share. Services grew 75% (2025) and 54% (H1 2026) at Empyrean and 101% (2025) at Primarius, while licences grew 5–8% in H1 2026.
  2. The fastest-growing money is in design services. VeriSilicon's backlog rose 266% in nine months on AI ASICs, while the tool vendors grew 19–36%.
  3. Chinese tools' "verdicts" rest on policy rather than foundry certification. The 17 Jul 2026 sell-off hit the Chinese tool names as hard as or harder than Synopsys and Cadence (about 8–9.5%), so the market treats them as more open to open-source and AI substitution (correlation only).
- **Evidence that supports the thesis.** The big three's China revenue persisted through controls (Cadence at 16% of revenue in Q3 2026 against 13% in FY2025; Synopsys still $814m in FY2025). The only Chinese niche with outside confirmation (Primarius's device models) is a verdict-style position.

### Gaps (could not verify)
- Private-company funding, valuations and revenue (X-Epic, UniVista, S2C, Phlexing, Arcas, 国微芯, Giga Design Automation, Corigine, HyperSilicon, EnnoCAD, LEDA).
- Which foundries certified Empyrean's tools.
- Chinese countermeasures and 2026 rules on advanced-node EDA.
- Huawei, Ant Group, ByteDance Seed-Prover and CertiK proof work.
- Requirements-tool vendors.
- NS-CMIC and 1260H status; lock-up dates; Kimi K3 technical details.
- Most items rest only on Chinese-language filings; the private-company items are thin.

### Sources with dates
- cninfo filings:
  - Empyrean: 2025 annual report (28 Apr 2026) https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF ; 2026 interim report (29 Aug 2026) https://static.cninfo.com.cn/finalpage/2026-08-29/1225525615.PDF ; Q3 report (30 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-30/1225641220.PDF ; Easy-Logic deal (2 Nov 2026) https://static.cninfo.com.cn/finalpage/2026-11-02/1225650496.PDF ; X-Times stake (8 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-08/1225597712.PDF ; Xpeedic termination (9 Jul 2025) https://static.cninfo.com.cn/finalpage/2025-07-09/1224119966.PDF ; fund-investment termination (13 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-13/1225604132.PDF
  - Primarius: 2025 annual report (16 Apr 2026) https://static.cninfo.com.cn/finalpage/2026-04-16/1225108676.PDF ; 2026 interim report (27 Aug 2026) https://static.cninfo.com.cn/finalpage/2026-08-27/1225514208.PDF ; Q3 report (31 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-31/1225648713.PDF
  - Semitronix: 2025 annual report (23 Apr 2026) https://static.cninfo.com.cn/finalpage/2026-04-23/1225153967.PDF ; Q3 report (28 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-28/1225630347.PDF ; buyback proposal (5 Nov 2026) https://static.cninfo.com.cn/finalpage/2026-11-05/1225657737.PDF
  - VeriSilicon: Q3 report (31 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-31/1225649712.PDF
  - Brite: Q3 report (30 Oct 2026) https://static.cninfo.com.cn/finalpage/2026-10-30/1225639403.PDF
- Exchanges and regulators: SSE STAR IPO database (queried 12 Nov 2026) https://kcb.sse.com.cn/ ; HKEX eligible-securities lists (updated 12 Nov 2026) https://www.hkex.com.hk/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities?sc_lang=en ; eCFR 31 CFR 850 (fetched 12 Nov 2026) https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII/part-850 ; BIS Entity List file https://www.bis.gov/media/documents/entity-list-faqs-11.10.2025.pdf ; TSMC EDA Alliance (as of 23 Sep and 1 Oct 2026) https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance
- US company filings (via sibling notes): Cadence FY2025 10-K https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf ; Cadence Q3 2026 CFO commentary (26 Oct 2026) https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cfocommentary10262026ex9902.htm ; Synopsys Q4 FY2025 supplement (10 Dec 2025) https://s201.q4cdn.com/778493406/files/doc_earnings/2025/q4/supplemental-info/Synopsys-Q4-FY2025-Financial-Supplement.pdf ; Synopsys FY2025 10-K https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm
- Law-firm alerts: Skadden (11 Nov 2026) https://www.skadden.com/insights/publications/2026/11/bis-extends-suspension-of-affiliates-rule ; Nixon Peabody (6 Nov 2026) https://www.nixonpeabody.com/insights/alerts/2026/11/06/bis-formally-suspends-the-affiliates-rule-until-january-10-2027 ; Baker McKenzie (Nov 2026) https://sanctionsnews.bakermckenzie.com/bis-extends-suspension-of-the-affiliates-rule-through-january-10-2027/
- Press: Investing.com (17 Jul 2026) https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775 ; Design & Reuse (5 Jan 2026) https://www.design-reuse.com/news/202529890-five-year-old-chinese-eda-firm-univista-sets-sights-on-ipo-led-by-ex-synopsys-and-cadence-team ; 科创板日报 (10 Feb 2025) https://www.cls.cn/detail/1938403 ; 财闻 (14 Aug 2026) https://www.caiwennews.com/article/1552968.shtml ; 界面 (undated, 2026) https://m.jiemian.com/article/13434279.html ; Tom's Hardware (Dec 2024) https://www.tomshardware.com/tech-industry/empyrean-technology-gives-control-to-cec-after-u-s-blacklisting-chinas-top-developer-of-chip-design-systems-hands-reins-to-state-owned-firm ; TrendForce (Dec 2024) https://www.trendforce.com/news/?p=26942 ; 36Kr project page (fetched 12 Nov 2026) https://pitchhub.36kr.com/project/1958566457955330
- Analyst and market data: SemiAnalysis (21 May 2026) https://newsletter.semianalysis.com/p/eda-market-primer ; StockAnalysis (12 Nov 2026) https://stockanalysis.com/stocks/snps/statistics/ and https://stockanalysis.com/stocks/cdns/statistics/ ; companiesmarketcap (12 Nov 2026) https://companiesmarketcap.com/cadence-design-systems/ps-ratio/ ; Tencent quote and price-history service (12 Nov 2026) https://qt.gtimg.cn/q=sz301269
- Company websites and repositories: UniVista (12 Nov 2026) https://www.univista-isg.com/ ; S2C (12 Nov 2026) https://www.s2cinc.com/ ; iEDA https://github.com/OSCC-Project/iEDA ; Hugging Face https://hf.co/deepseek-ai/DeepSeek-Prover-V2-671B and https://hf.co/project-numina/Kimina-Prover-72B

# Physical-simulation software in mainland China, as of 12 November 2026

**Summary for the report writer.** No Chinese vendor belongs in the global top tier. The largest, Empyrean (华大九天, 301269.SZ, controlled by state-owned CEC), had 2025 revenue of RMB1.325bn (~US$185m at ~7.1/USD, my conversion). That is about 3% of Synopsys's FY2025 revenue and smaller than Synopsys's China sales alone (US$707m in the nine months to July 2026). The best Chinese candidates are chip-design simulation vendors: Empyrean (analog/full-custom flows, FPD, physical verification), Primarius (概伦电子, 688206.SH; device modelling and SPICE, with a real global foundry footprint: 24% of revenue abroad) and Semitronix (广立微, 301095.SZ; yield software, but 62% of revenue is test hardware). General CAE is small, project-heavy and defence-dependent. Suochen (索辰科技, 688507.SH) earned only RMB198m from engineering-simulation software in 2025, down 13%. Its customers are "mainly military units and research institutes" and its receivables are 1.7x revenue. BIS added Suochen to the US Entity List on 16 Sep 2025 (90 FR 44499); I found no company disclosure of this. ZWSOFT's CAE line was RMB12m (1.3% of revenue).

Positions rest mainly on import substitution, state customers and subsidies. Empyrean's 2025 government support (~RMB150m including VAT refunds) was 2.5x its net profit, and it was entity-listed in Dec 2024. Sign-off evidence is almost entirely company claims: Empyrean says its ALPS simulator holds 8/5/4nm foundry certifications and its Argus DRC is the "standard" check at a leading domestic fab (foundries not named). The only regulator-verified acceptance found is older: China's nuclear regulator approved its first domestic safety-analysis code (CGN's PCM) in March 2021, after 37 months of review.

Two Chinese strengths are confirmed by outsiders. AISI/DP Technology's DPA-4.1 leads the Matbench Discovery leaderboard (Oct 2026). A Chinese CPU-only machine (LineShine, NSC Shenzhen) tops the June 2026 TOP500. CMA's AI weather models are operationally deployed, though not independently verified.

The July 2026 "AI designed a chip" episode was Moonshot AI's Kimi K3 blog. It describes a 48-hour autonomous run with unnamed open-source EDA tools on the Nangate 45nm library. The result was simulation only, with no tape-out and no released collateral. Synopsys and Cadence fell about 9% on 17 Jul; Chinese EDA/CAE stocks fell 12-22% over 16-20 Jul.

US controls bind unevenly. The May-July 2025 EDA licence requirement was rescinded, and the 50% Affiliates Rule is suspended to 10 Jan 2027. Sugon is on OFAC's NS-CMIC list, so US persons cannot buy its shares. All the Shanghai and Shenzhen names here are Stock Connect-eligible, but Beijing-listed Paratera is not. Coverage of private firms (IBE/Simdroid, PERA, Tongyuan, TenFong, Intesim, Xpeedic, UniVista, DJEL, DP Technology) and of defence customers is thin. The shared web-search budget ran out mid-task, so later evidence comes from primary filings, exchange and US-government data files.

## Q1. Map of the field: who matters, ownership and size

### Takeaway
Chinese physical simulation splits into a listed chip-design trio (Empyrean, Primarius, Semitronix), a small, loss-prone general-CAE group (Suochen, ZWSOFT's CAE line, Hollywave, private firms), state AI-for-science and weather efforts, and HPC hardware/compute (Sugon, Paratera, national supercomputing centres). All are small next to the foreign vendors' China revenue.

### Cited Findings
**Market size**
- China CAE software market RMB6.05bn (2025), forecast RMB13.12bn by 2030 (16.7% CAGR). Electronic thermal simulation was RMB364m in 2025 and is the fastest-growing niche, where domestic vendors made "单点突破" (single-point breakthroughs). No vendor shares are given — [IDC blog, 10 Aug 2026](https://www.idc.com/resource-center/blog/电子散热领跑、物理ai启航-中国cae市场的双重增/)
- Older third-party estimates (secondary, 2022 data): domestic CAE share 16.2% (7.0% in 2016); Ansys 17%, Siemens 15%, Dassault 8% of China CAE — [智研咨询 via search summary](https://www.chyxx.com/industry/1225266.html)
- "目前国产 EDA 市场只有三家上市公司" (only three listed domestic EDA firms). Domestic tools are "基本可用" (basically usable) at 28nm and above, with gaps at 7/5/3nm — [半导体产业纵横 via 36Kr, 27 Mar 2026](https://www.36kr.com/p/3741032844410885)
- TrendForce estimate (secondary): China EDA self-sufficiency >10% by 2024; global shares Synopsys 31%, Cadence 30%, Siemens 13% — [TrendForce via search summary](https://www.trendforce.com/news/?p=64035)

**Chip-design simulation (EDA)**
- **Empyrean 华大九天 (301269.SZ).**
  - 2025: revenue RMB1,325m (+8.4%). EDA software RMB1,074.5m (81.1%, −1.6%); technical services RMB201.3m (+74.9%); overseas RMB131.3m (9.9%, +127%).
  - 1,460 staff (1,077 in R&D).
  - No controlling shareholder; the actual controller is CEC (中国电子信息产业集团), which nominates directors — [2025 annual report, 28 Apr 2026](https://pdf.dfcfw.com/pdf/H2_AN202604271821642344_1.pdf)
  - CEC took control in Dec 2024 — [announcement, 10 Dec 2024](https://pdf.dfcfw.com/pdf/H2_AN202412091641230534_1.pdf)
- **Primarius 概伦电子 (688206.SH).**
  - 2025: revenue RMB484m. Domestic RMB363m and overseas RMB113m (24% of main revenue, 96.7% gross margin).
  - Split: design-class EDA RMB191m (+29.8%), manufacturing-class EDA RMB123m (+11.7%). 608 staff — [2025 annual report, 16 Apr 2026](https://pdf.dfcfw.com/pdf/H2_AN202604151821246387_1.pdf)
  - Says 9 of the top-10 foundries (incl. TSMC, Samsung, SMIC) use its tools (company claim via trade press, unconfirmed) — [36Kr, 27 Mar 2026](https://www.36kr.com/p/3741032844410885)
- **Semitronix 广立微 (301095.SZ).**
  - 2025: revenue RMB735m (+34.4%). Software development and licensing RMB278m (37.8%, +75%); test equipment RMB453m (61.7%).
  - Domestic 97%. 826 staff.
  - Bought LUCEDA NV (Belgium, silicon-photonics EDA) — [2025 annual report, 23 Apr 2026](https://pdf.dfcfw.com/pdf/H2_AN202604221821463282_1.pdf)
- **Private EDA pipeline.**
  - Xpeedic 芯和 (EM/package/SI simulation) completed IPO tutoring 24 Dec 2025 (CITIC) after Empyrean dropped its bid for it (below).
  - UniVista 合见工软 filed for tutoring 26 Dec 2025.
  - Xpeedic's products are reported in the Huawei, ZTE and JCET supply chains (unconfirmed) — [36Kr](https://www.36kr.com/p/3741032844410885)
- **Empyrean bolt-ons.**
  - Xpeedic plan (shares and cash, 35 counterparties; CEC to fund matching capital) — [plan, 31 Mar 2025](https://pdf.dfcfw.com/pdf/H2_AN202503301649146069_1.pdf); terminated — [9 Jul 2025](https://pdf.dfcfw.com/pdf/H2_AN202507091705879178_1.pdf)
  - 6.90% of 芯行纪 (digital place-and-route) for RMB149m — [8 Oct 2026](https://pdf.dfcfw.com/pdf/H2_AN202610081830214892_1.pdf)
  - Control of 奇捷科技 (logic optimisation; 2025 revenue RMB32.3m, loss RMB19.4m): 50.38% for RMB219m (~RMB435m for 100%, my calculation) — [2 Nov 2026](https://pdf.dfcfw.com/pdf/H2_AN202611011831294436_1.pdf); [NBD, 2 Nov 2026](https://www.nbd.com.cn/articles/2026-11-02/4634901.html)
  - Minority links to emulation/prototyping firms 亚科鸿禹/思尔芯 (S2C) — [13 Oct 2026](https://pdf.dfcfw.com/pdf/H2_AN202610131830416498_1.pdf)

**Chip-manufacturing simulation**
- Merchant computational lithography is ~US$1.27bn (2024), with the top three >80%. Dongfang Jingyuan (DJEL, private) and Yuwei Optics are the only Chinese names listed — [QYResearch, 17 Oct 2025](https://www.gii.co.jp/report/qyr1862413-computational-lithography-software-global-market.html)
- DJEL has been on the Entity List since 89 FR 96836 (5 Dec 2024) — [eCFR 15 CFR 744 Supp. 4, version of 9 Nov 2026](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744)

**General CAE**
- **Suochen 索辰科技 (688507.SH).**
  - 2025: revenue RMB466m. Engineering-simulation software RMB197.9m (86% gross margin, −13.4%); simulation product development RMB86.5m (−36.9%); production-control and industrial-automation lines added via the Likong acquisition. 802 staff.
  - Its IPO project builds 260 "DEMX" underwater-noise testers a year — [2025 annual report, 28 Apr 2026](https://pdf.dfcfw.com/pdf/H2_AN202604271821616055_1.pdf)
  - Bought 60% of 力控科技 (SCADA) for RMB192m, closed 4 Dec 2025; goodwill ~RMB169m; Likong's debt ratio was 94% — [Stockstar, 4 Mar 2026](https://stock.stockstar.com/SS2026030400020711.shtml)
- **ZWSOFT 中望软件 (688083.SH).** 2025 revenue RMB893m: CAE RMB11.8m (1.3%, +21%), 3D CAD RMB259m. Overseas 30.7% (+35%), domestic −9.7%. 1,779 staff — [2025 annual report, 23 Apr 2026](https://pdf.dfcfw.com/pdf/H2_AN202604221821444496_1.pdf)
- **Hollywave 霍莱沃 (688682.SH; antenna/EM measurement and simulation).** 2025 revenue RMB303m and net loss RMB23m. Gross margin ~25-31% points to a hardware-heavy mix — [Eastmoney F10 data](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_F10_FINANCE_MAINFINADATA&columns=ALL&filter=(SECUCODE=%22688682.SH%22))
- **Physical-AI platforms.** IDC names Suochen's "天工·开物" and 云道 (IBE)'s "Sim-PI" — [IDC, 10 Aug 2026](https://www.idc.com/resource-center/blog/电子散热领跑、物理ai启航-中国cae市场的双重增/)
- **State codes.** The PHengLEI developer CARDC (China Aerodynamics R&D Center) has been on the Entity List since 1999 (64 FR 28910) — [eCFR](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744)

**Materials and AI-for-science**
- DP Technology 深势科技 (private): Series C >RMB800m (24 Dec 2025; investors incl. Beijing AI fund, Lenovo Capital). Bohrium claims >3m users (company claim) — [PEdaily](https://news.pedaily.cn/202512/559044.shtml)
- DPA-4.1-Max (AISI Beijing/IAPCM, DP Technology co-developer) ranks #1 on Matbench Discovery (CPS 0.913, added 31 Oct 2026) — [Matbench Discovery, fetched 12 Nov 2026](https://matbench-discovery.materialsproject.org/); [DPA4 blog, 22 May 2026](https://blogs.deepmodeling.com/DPA4_05_22_2026/)

**Weather**
- CMA's Fengqing (global), Fenglei (nowcasting) and Fengshun cover 0-60 days. Upgrades plus the "Fengyuan" base model (with Shanghai AI Lab) were released 19 Dec 2025 — [Xinhua](https://www.news.cn/tech/20251219/99223b9d028a46faa3dda987a5f607b9/c.html); [Xinhua, 28 Apr 2026](https://www.news.cn/politics/20260428/8921ca234e624d50b08162a797a385a0/c.html)
- Huawei Pangu-Weather weights are CC BY-NC-SA ("commercial use... forbidden") — [GitHub](https://github.com/198808xc/Pangu-Weather). ECMWF stopped running Pangu in real time — [ECMWF, 11 May 2026](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)

**HPC and cloud**
- **Sugon 中科曙光 (603019.SH).** 2025 revenue RMB14.96bn and net profit RMB2.18bn; 9M 2026 revenue RMB12.24bn (+38.8%) and net RMB1.72bn (+78.5%) — [Eastmoney F10](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_F10_FINANCE_MAINFINADATA&columns=ALL&filter=(SECUCODE=%22603019.SH%22))
  - Its share-swap merger with Hygon was terminated on 10 Dec 2025 — [announcement](https://pdf.dfcfw.com/pdf/H2_AN202512091797127221_1.pdf)
- **Paratera 并行科技 (920493.BJ, ex-839493).** 2025 revenue RMB1.11bn: compute services RMB1,021m (22% gross margin), software RMB23.8m — [2025 annual report, 3 Apr 2026](https://pdf.dfcfw.com/pdf/H2_AN202604031821017462_1.pdf)
- **TOP500.** LineShine at NSC Shenzhen is #1 on the June 2026 TOP500 (2.198 EF Rmax). It runs 304-core LX2 CPUs with no accelerator, LingQi interconnect and Kylin OS, and is the first China-based #1 since 2017 — [TOP500](https://www.top500.org/lists/top500/2026/06/). NSC Shenzhen has been entity-listed since 86 FR 18438 (9 Apr 2021) — [eCFR](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744)

### Inferences
- The Chinese listed EDA software pool is roughly RMB2.1bn (Empyrean RMB1.33bn, Primarius RMB0.48bn, Semitronix software RMB0.28bn, 2025). Synopsys plus Cadence China revenue was ~US$1.3-1.4bn, so domestic vendors hold well under a quarter of China EDA (my calculation; Siemens, Keysight and Ansys excluded).
- In CAE, Suochen's simulation software is ~3% of IDC's China CAE market. No Chinese general-CAE vendor is near global scale.
- Primarius is the most "global" Chinese simulation vendor (foundry device-modelling footprint). Empyrean is the broadest domestic flow owner.

### Gaps
- No vendor-level China CAE or EDA shares from IDC or CCID for 2025 (IDC's CHC52293825 report is paywalled).
- Private firms (IBE/Simdroid, PERA Global 安世亚太, Tongyuan MWORKS 同元软控, TenFong 十沣, Intesim 英特仿真, Hongzhiwei 鸿之微, DJEL, Fastone 速石, Beilong 北龙超云): revenue, ownership and IPO status are unverified; search failed or ran out.
- The National Numerical Windtunnel/PHengLEI's 2025-26 status, FuXi (Fudan) and FengWu (Shanghai AI Lab) status and licences, and Huawei/Baidu/ByteDance AI-for-physics products are not verified.

## Q2. Framework applied to the strongest candidates (quality evidence only)

### Takeaway
Five candidates are scored: Empyrean, Primarius, Semitronix, Suochen and DP Technology. None owns a globally accepted judge. Primarius comes closest, through device modelling used at foreign foundries (company claim). Empyrean owns domestic judges by policy, not by contest. All depend on subsidies and import substitution. Agents, open-source EDA and AI are being said more than done.

### Cited Findings
**Empyrean**
- **(a) Position.**
  - Claims ALPS circuit simulation certified at 8/5/4nm, Patron (transistor-level power integrity) at 14nm and Argus DRC/LVS at 28nm. Argus is "国内头部晶圆厂流片流程中的标准 DRC 检查工具... 累计支撑数千款芯片成功签核流片" (standard DRC tool in a leading domestic fab's tape-out flow; thousands of chips signed off).
  - PDKs cover >70% of domestic foundry nodes. "Only" domestic analog full flow; >90% of domestic flat-panel firms use it.
  - Eight tools hold ISO 26262 TCL3 / IEC 61508 T2 (certifier not named). All company claims, unconfirmed; foundries not named — [2025 annual report](https://pdf.dfcfw.com/pdf/H2_AN202604271821642344_1.pdf); [H1 2026 report, 29 Aug 2026](https://pdf.dfcfw.com/pdf/H2_AN202608280006757902_1.pdf)
  - Gaps: digital sign-off tools (Hima Time STA, Hima EMIR, Argus SoC) only launched in 2025. Digital place-and-route and logic optimisation are being bought in (芯行纪, 奇捷). Broker: digital tool iteration "或有延长" (may lengthen) because domestic process iteration is slow — [Shenwan Hongyuan via Gelonghui, 30 Oct 2026](https://m.gelonghui.com/news/5340715)
- **(b) Lead.** The only outside evidence is market position inside China (three listed domestic EDA firms; foreign share dominant). I found no independent benchmark or named-foundry certification.
- **(c) Revenue model.**
  - Licence sales are 81% of revenue, with zero R&D capitalisation. Top-5 customers 30.6%.
  - Growth is shifting to services: H1 2026 EDA software +4.9% versus services +53.9% — [H1 2026 report](https://pdf.dfcfw.com/pdf/H2_AN202608280006757902_1.pdf)
  - Receivables RMB564m at end-2025 (43% of revenue). Top-5 suppliers 44.5%, of which 27.2% related-party (CEC group) — [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604271821642344_1.pdf)
- **(d) Financial strength.**
  - 2025: net RMB61m; recurring-basis net −RMB9.8m. R&D RMB859m (64.8% of revenue). Operating cash flow RMB561m.
  - Government support RMB149.6m, from non-recurring grants RMB61.5m + VAT refunds RMB51.5m + EDA project grants RMB36.1m + RMB0.6m (my sum).
  - CEC passes state capital-budget funds via an entrusted loan — [11 Dec 2025](https://pdf.dfcfw.com/pdf/H2_AN202512101797748407_1.pdf)
- **(e) Resilience.** Entity-listed since 5 Dec 2024 (89 FR 96836) — [eCFR](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744)

**Primarius**
- **(a/b) Position and lead.** Device modelling plus SPICE at foreign foundries (company claim via trade press). Its own assessment: substitution is effective in mature process, analog, device modelling and manufacturing EDA, while "高端数字流程、先进工艺支持、全流程工具贯通" (high-end digital, advanced-node support, full flow) remain "持续攻坚" (still being fought for) — [2025 annual report](https://pdf.dfcfw.com/pdf/H2_AN202604151821246387_1.pdf)
- **(c) Revenue model.**
  - 9M 2026: EDA licensing RMB232.6m (55.7%), IP licensing 14.5%, technical development 14.1%, characterisation hardware 9.3%, chip customisation 6.5% — [Stockstar, 9 Nov 2026](https://wap.stockstar.com/detail/RB2026110900023327)
  - Top-5 customers 35.8% (2025).
- **(d) Financial strength.**
  - 2025 net RMB34m; recurring-basis −RMB60m.
  - 9M 2026: revenue RMB418m (+32.8%), net RMB0.66m, recurring-basis −RMB24.9m — [Stockstar](https://wap.stockstar.com/detail/RB2026110900023327)
  - Acquired 100% of 锐成芯微 and the 45.64% of 纳能微 it did not already hold (~RMB2.17bn): SSE committee June 2026, CSRC registration 24 Jun 2026, transfer Aug 2026. The deal adds 67.5m shares plus RMB1.05bn of matching funds at RMB38.92 — [CSRC approval](https://pdf.dfcfw.com/pdf/H2_AN202606261824897980_1.pdf); [36Kr](https://www.36kr.com/p/3741032844410885)
- **(e) Resilience.** Not on the Entity List by name as of 9 Nov 2026 (my check of eCFR). Overseas revenue exposes it to US/allied foundry policy.

**Semitronix**
- **(a) Position.** Yield, test-chip and DFT software tied to its own WAT testers. "Agentic DFT" launched with a claimed >40% R&D-efficiency gain (company claim) — [CICC via Gelonghui, 3 Nov 2026](https://m.gelonghui.com/news/5343544)
- **(c) Revenue model.** Hardware 62% of revenue; top-5 customers 72.4%; receivables RMB642m (+75%) on revenue +34% (2025) — [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604221821463282_1.pdf)
- **(d) Financial strength.** 9M 2026: revenue RMB582m (+36%), net RMB71.5m, recurring-basis RMB21.5m, operating cash flow +RMB102m. Q3 gross margin 61.6% (−3.6pt) — [CICC](https://m.gelonghui.com/news/5343544)

**Suochen**
- **(a) Position.** Claims "全流程自主可控... 核心模块不依赖于第三方供应商" (fully self-controlled; core modules independent of third parties). Says research institutes increasingly "重视国内供应商的发掘" (prioritise finding domestic suppliers), i.e. substitution (company claim) — [2025 annual report](https://pdf.dfcfw.com/pdf/H2_AN202604271821616055_1.pdf)
- **(c) Revenue model.**
  - "下游客户主要集中于军工领域" / "主要为军工单位及科研院所" (customers mainly military units and research institutes). Top-5 customers 19.3%.
  - Receivables RMB795m (+31%) against revenue RMB466m.
  - About 77-78% of annual revenue lands in Q4, in both 2024 and 2025 (my calculation from quarterly data) — [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604271821616055_1.pdf); [Eastmoney F10](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_F10_FINANCE_MAINFINADATA&columns=ALL&filter=(SECUCODE=%22688507.SH%22))
- **(d) Financial strength.** 9M 2026: revenue RMB173m (+62.9%, consolidation-driven), net loss RMB95.2m; Q3 revenue RMB99.8m (+105%) — [10jqka, 29 Oct 2026](https://stock.10jqka.com.cn/20261029/c681247088.shtml)
- **(e) Resilience.** Entity List: "Shanghai Suochen Information Technology Co., Ltd., a.k.a. DEMX; DEMXS; Suochen Technology" at its registered address, presumption of denial, with the §734.9(e)(2) foreign-direct-product footnote, 90 FR 44499 (16 Sep 2025) — [eCFR](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744). The 2025 annual report text has no reference to it (my search of the PDF text).

**DP Technology (private)**
- **(a/b) Position and lead.** Independent leaderboard lead (DPA-4.1, above). DPA4 trains on one RTX 5090 in ~1 day (company/AISI claim) — [DPA4 blog](https://blogs.deepmodeling.com/DPA4_05_22_2026/)
- **(c) Revenue model.** Platform users plus enterprise R&D (CATL, BYD, PetroChina cited as clients); revenue undisclosed — [PEdaily](https://news.pedaily.cn/202512/559044.shtml)

**Transitions: said versus done**
- **(1) Seat licences to pricing by use or result.**
  - Said: none of the five.
  - Done: Paratera's compute is usage-priced, but it is resold hardware at 20-22% gross margin — [Paratera annual report](https://pdf.dfcfw.com/pdf/H2_AN202604031821017462_1.pdf)
- **(2) CPUs to GPUs and domestic accelerators.**
  - Done (company claim): Empyrean ported ALPS GT/Liberal GT to Hygon DCU — [H1 2026](https://pdf.dfcfw.com/pdf/H2_AN202608280006757902_1.pdf)
  - Said: Suochen's engines "支持 GPU" (support GPU) — [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604271821616055_1.pdf)
  - China's flagship HPC is CPU-only (LineShine).
- **(3) Agent-driven tools via APIs.**
  - Said or launched: Empyrean "PyAether 智能体" (coding assistant for its Python API), with AI agents to "灵活调度各类 EDA 工具" (orchestrate EDA tools).
  - Semitronix Agentic DFT and SemiMind LLM platform; UniVista UDA 2.0 — [H1 2026](https://pdf.dfcfw.com/pdf/H2_AN202608280006757902_1.pdf); [36Kr](https://www.36kr.com/p/3741032844410885)
  - No usage, pricing or customer metrics disclosed.
- **(4) Open-source codes improved by AI.** Kimi K3 demo (Q6). No Chinese vendor discloses open-source-based products.
- **(5) Learned models inside certified solvers.** Fengqing operational at CMA (state, not a vendor). No EDA/CAE vendor shows a learned model inside a signed-off flow.
- **(6) Regulator and customer sign-off rules.** See Q4. Domestic sign-off is mostly self-asserted.

### Inferences
- **Steady AI growth (~55%).** Domestic AI-chip design starts (Huawei, Hygon and others) and import substitution keep Empyrean and Primarius at 15-30% growth. Margins stay thin because R&D is ~50-65% of revenue.
- **Financing pause around 2028 (~25%).** State funding (CEC, subsidies) cushions Empyrean. Paratera (debt ratio 78.9%, AI compute 2/3 of revenue) and Semitronix's hardware line are most exposed.
- **Faster acceleration (~20%).** Agentic, open-source flows threaten seat-based licensing, but Chinese demand is policy-shielded. The bigger risk is foreign vendors' agentic tools re-widening the technology gap.
- Export-control exposure is highest for Suochen (defence plus entity-listed, with the FDP footnote) and lowest for Primarius/Semitronix. A new US EDA licence requirement would help domestic vendors in China but hit Primarius's foreign foundry business if China retaliated. (All inferences.)

### Gaps
- Defence and SOE revenue shares are not quantified by any company. Named foundry customers and certification letters are not disclosed. No independent benchmark of Chinese solvers against Ansys/Synopsys was found.

## Q3. Financials of the leading listed names (2025 annual; Q3/9M 2026)

### Takeaway
Revenue is growing at most names, but recurring-basis profits are negative or thin everywhere except Sugon. Subsidies and VAT refunds are material, and receivables are high at Suochen and Semitronix.

### Cited Findings
Data: Eastmoney F10 main indicators (from filings; notice dates 2026-04 for FY2025, 2026-10-27 to 31 for Q3) — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_F10_FINANCE_MAINFINADATA&columns=ALL&filter=(SECUCODE=%22301269.SZ%22)); cross-checked with the reports and media cited in Q2. RMB m; GM = gross margin.

| Company | FY2025 rev (yoy) | FY2025 net / recurring | 9M 2026 rev (yoy) | 9M 2026 net / recurring | 9M GM | 9M R&D/rev | 9M op. cash flow |
|---|---|---|---|---|---|---|---|
| Empyrean | 1,325 (+8.4%) | 61 / −10 | 960 (+19.3%); Q3 394 (+29.8%) | 27 / −31 | 88.9% | 65.6% | −112 |
| Primarius | 484 (+15.4%) | 34 / −60 | 418 (+32.8%); Q3 177 (+84%) | 0.7 / −25 | 80.9% | 53.5% | −52 |
| Semitronix | 735 (+34.4%) | 89 / 44 | 582 (+36.1%); Q3 241 (+32.7%) | 72 / 22 | 60.9% | 45.7% | +102 |
| Suochen | 466 (+23.0%) | 32 / 27 | 173 (+62.9%); Q3 100 (+105%) | −95 / −98 | 61.5% | 72.7% | −28 |
| ZWSOFT | 893 (+0.6%) | 21 / −116 | 580 (+7.8%) | −6 / −109 | 96.5% | 51.5% | +19 |
| Hollywave | 303 (+12.7%) | −23 / −30 | 183 (−14.9%) | 11 / 1 | 30.9% | 19.3% | −25 |
| Paratera | 1,110 (+69.6%) | 12 / 0 | 1,547 (+110.8%) | 79 / 63 | 20.4% | 3.1% | +337 |
| Sugon | 14,964 (+13.8%) | 2,176 / 1,838 | 12,239 (+38.8%) | 1,725 / 1,553 | 27.3% | 11.5% | +266 |

- **Subsidies.**
  - Empyrean 9M 2026: non-recurring items RMB57.9m, incl. grants RMB53.0m (net only RMB26.9m) — [NBD](https://www.nbd.com.cn/articles/2026-11-02/4634901.html)
  - ZWSOFT 9M 2026 grants RMB86m and 2025 VAT refunds RMB45.4m — [10jqka](https://news.10jqka.com.cn/20261027/c681139313.shtml); [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604221821444496_1.pdf)
  - Semitronix 2025 grants RMB28.9m; Suochen 2025 grants RMB7.8m plus other income RMB14.4m.
- **Receivables (end-2025).** Empyrean RMB564m; Primarius RMB185m; Semitronix RMB642m; Suochen RMB795m; ZWSOFT RMB99m; Paratera RMB246m (+170%) — annual reports cited in Q1/Q2.
- **Customer concentration (top-5, 2025).** Empyrean 30.6%; Primarius 35.8%; Semitronix 72.4%; Suochen 19.3%; ZWSOFT 15.6% — same reports.
- **Paratera.**
  - 9M 2026: compute services RMB1,469m (95%), AI compute ("智算") RMB1,049m (+144%); debt ratio 78.9% — [Caiwen, 29 Oct 2026](https://www.caiwennews.com/article/1675896.shtml)
  - Private placement accepted by the BSE 29 Sep 2026; its reply to the exchange's questions is due by 9 Dec 2026 — [filing](https://pdf.dfcfw.com/pdf/H2_AN202609291830004754_1.pdf); [11 Nov 2026](https://pdf.dfcfw.com/pdf/H2_AN202611111831631671_1.pdf)
- **Other 2025-26 actions.**
  - Suochen's controlling shareholder pledged no sales for 6 months — [4 Nov 2026](https://pdf.dfcfw.com/pdf/H2_AN202611031831372633_1.pdf)
  - "Big Fund" plans to cut its Empyrean stake by up to 1% (Sep 2026) — [NBD](https://www.nbd.com.cn/articles/2026-11-02/4634901.html)
  - Sugon filed a convertible bond prospectus (13 Jul 2026), per the exchange filing list.

### Inferences
- Recurring profitability is negative at four of the eight names. Subsidy dependence is structural, not cyclical.

### Gaps
- Hollywave's segment split and Sugon's software revenue were not extracted. Q3 2026 receivables are only partly available.

## Q4. Sign-off status in China and who certifies

### Takeaway
Domestic EDA sign-off is self-reported and node-limited (28nm-class for digital; analog/SPICE claims to 4nm). Nuclear has a formal regulator review that approved one domestic code by 2021. No virtual-testing acceptance was found in C-NCAP. Aerospace still relies on foreign tools.

### Cited Findings
- **EDA.**
  - Empyrean certification claims (Q2) name no foundry.
  - Trade press: domestic tools are "基本可用" at ≥28nm. A private firm, 行芯科技, claims STA validation on advanced-node projects (unconfirmed) — [36Kr](https://www.36kr.com/p/3741032844410885)
- **Nuclear.**
  - The NNSA's technical arm (Nuclear and Radiation Safety Center) reports that NNSA "did not approve any software before 2018." CGN's PCM (PINE+COCO) was "the first safety analysis computer code that passed the assessment of NNSA" (conclusions approved March 2021; review took 37 months).
  - 25 codes had been submitted by Oct 2021, including CNNC/NPIC's NESTOR and SPIC's COSINE.
  - The method follows US NRC RG 1.203; the minimum review is 18 months; applications come from Chinese firms only. WCOBRA/TRAC was approved for AP1000 (dated, 2021) — [Frontiers in Energy Research, 24 Dec 2021](https://www.frontiersin.org/journals/energy-research/articles/10.3389/fenrg.2021.785494/full)
  - NESTOR (68 codes for Hualong One) was launched in Dec 2015 — [China Daily](https://subsites.chinadaily.com.cn/cnnc/2015-12/21/c_1022874.htm)
- **Automotive.**
  - CATARC released the C-NCAP 2027 protocol on 20 Apr 2026, focused on EV electrical safety and intelligent driving; the management rules start 1 Jul 2027. I found no virtual-testing acceptance clause — [IT之家, 21 Apr 2026](https://www.ithome.com/0/941/401.htm) (via search summary)
  - Empyrean's ISO 26262 tool qualifications are company-claimed (Q2).
- **Aerospace.** Dassault's Q3 2026 Asia growth (+12%) was "led by China, with strength in aerospace (including COMAC)" — [Investing.com transcript, Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-dassault-systemes-beats-q3-2026-estimates-shares-fall-93CH-4978361)
- **Weather.** CMA (the regulator-operator) deploys Fengqing operationally (People's Daily, 6 Dec 2025, via search summary). A performance evaluation appears in 《气象》 2026(5), DOI 10.7519/j.issn.1000-0526.2026.030501 (not read) — [People's Daily](https://paper.people.com.cn/rmrb/pc/content/202512/06/content_30118755.html)

### Inferences
- Who certifies:
  - Nuclear: NNSA, via the Nuclear and Radiation Safety Center.
  - Automotive ratings: CATARC (C-NCAP).
  - Civil aircraft: CAAC (no domestic-CAE acceptance evidence found).
  - Chips: the foundries (SMIC, Hua Hong), which keep their certifications private.
- The policy "judge" in China is often the state customer itself (defence institutes, CMA), which favours domestic tools regardless of contest results.

### Gaps
- NNSA approvals after 2021 and CAAC/COMAC use of domestic CAE could not be verified (search exhausted). SMIC's EDA certification list and Huawei's EDA sign-off status are also unverified; Huawei's 2023 "14nm-and-above tools" claim was not re-checked.

## Q5. Policy and restrictions

### Takeaway
US EDA licensing was imposed and rescinded in 2025. Entity listings, not licence rules, are the live constraint (Empyrean, DJEL, Suochen, Sugon, Hygon, NSCs). Foreign vendors' China shares are falling at Synopsys but rising at Cadence and Dassault.

### Cited Findings
- **US EDA rules, 2025.** BIS required licences for EDA exports to China from late May 2025 (industry told 23 May) — [TechCrunch, 30 May 2025](https://techcrunch.com/2025/05/30/us-imposes-new-rules-to-curb-semiconductor-design-software-sales-to-china). The requirement was rescinded in early July 2025 after a rare-earths deal — [Business Standard, 3 Jul 2025](https://www.business-standard.com/world-news/us-rolls-back-chip-software-export-curbs-china-siemens-synopsys-cadence-resume-ops-125070300801_1.html)
- **Affiliates (50%) Rule.** Suspended again to 10 Jan 2027, announced ~5 Nov 2026 (FR doc 2026-22793), aligned with the US-China (Busan) arrangement — [Reed Smith, 6 Nov 2026](https://www.reedsmith.com/our-insights/blogs/trade-compliance-resource-hub/5272/bis-further-suspends-affiliates-rule-until-january-2027/); [Thompson Hine](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/)
  - China's rare-earth controls could apply globally from Jan 2027 if no deal is reached — [Reed Smith](https://www.reedsmith.com/our-insights/blogs/trade-compliance-resource-hub/5272/bis-further-suspends-affiliates-rule-until-january-2027/)
- **Entity List (eCFR, 9 Nov 2026).**
  - Empyrean and DJEL: 5 Dec 2024. Suochen: 16 Sep 2025. Sugon: 24 Jun 2019. Hygon: 2019 (FDP footnote added 2022). NSC Changsha/Guangzhou 2015; NSC Jinan/Shenzhen Apr 2021. CARDC 1999.
  - Not listed by name: Primarius, Semitronix, ZWSOFT, Hollywave, Paratera, Xpeedic, UniVista, Moonshot — [eCFR](https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-744/appendix-Supplement%20No.%204%20to%20Part%20744)
  - BIS reportedly avoided new China listings from late 2025 — [Malay Mail/Reuters, 18 Jun 2026](https://www.malaymail.com/news/world/2026/06/18/deepseek-cxmt-among-chinese-firms-awaiting-us-entity-list-action-as-washington-weighs-trade-risks/224127)
  - The DoD 1260H list was updated 8 Jun 2026, with a wider scope — [secrss](https://www.secrss.com/articles/91107)
- **China's levers.**
  - SAMR approved Synopsys-Ansys (14 Jul 2025) with ~10-year behavioural conditions: honour contracts, no bundling, keep interoperability for Chinese customers — [Schnitger, 14 Jul 2025](https://schnitgercorp.com/2025/07/14/china-finally-grants-approval-for-synopsysansys/)
  - MOFCOM/MOST draft export-control catalogue revision covering large AI models (16 Oct 2026; comments to 15 Nov) — [Yicai, 22 Oct 2026](https://www.yicai.com/news/103405081.html) (per the AI-labs strand; ministry page not opened).
- **Foreign vendors in China.**
  - Synopsys China revenue: US$255.5m of US$2,476.8m in Q3 FY2026 (10.3%, vs 14.2% a year earlier); 9M FY2026 9.9% (12.1%) — [10-Q, quarter to 31 Jul 2026](https://www.sec.gov/Archives/edgar/data/0000883241/000088324126000025/snps-20260731.htm)
  - Synopsys FY2025 China revenue fell 22% excluding Ansys; BIS administrative subpoenas over certain Chinese entities — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm)
  - Cadence China: 13% of FY2025 revenue (US$680m, +19%) — [CFO commentary, 17 Feb 2026](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000013/cfocommentary02172026ex9902.htm); 16% in Q3 2026 — [Q3 release, 26 Oct 2026](https://www.sec.gov/Archives/edgar/data/0000813672/000081367226000116/cdns10262026ex9901.htm)
  - Dassault: China double-digit growth in Q3 2026 (above). Siemens China local-for-local revenue +25% in FY2026 (call, per Siemens strand).
- **Company views of the domestic market.**
  - ZWSOFT: 2025 demand hurt by property-investment decline and "制造业企业经营困难" (manufacturers' difficulties), with policy support the offsetting factor — [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604221821444496_1.pdf)
  - Primarius: domestic EDA moving "由单点突破、局部可用... 迈向多点商用、规模替代" (from point breakthroughs to scaled substitution) — [annual report](https://pdf.dfcfw.com/pdf/H2_AN202604151821246387_1.pdf)

### Inferences
- Policy and controls create demand for domestic vendors, but the Synopsys decline coincides with Cadence growth. That suggests share moved partly between US vendors, not only to Chinese ones.

### Gaps
- Specific 2025-26 MIIT/State Council industrial-software funding documents, SASAC substitution deadlines and Big Fund III allocations to EDA/CAE are not verified (search exhausted). The reason BIS gave for Suochen's listing was not retrieved (the FR API blocked this IP).

## Q6. AI and open source in China

### Takeaway
The July 2026 episode is Moonshot AI's Kimi K3 blog: a self-reported, simulation-only demo on an academic 45nm library. It moved markets but proves no sign-off capability. AI weather is the most operational Chinese AI-for-physics use.

### Cited Findings
- **Kimi K3 blog (dated 16-17 Jul 2026).** "As an early proof of concept, Kimi K3 designed a chip to serve a nano model built on its own architecture. In a single 48-hour autonomous run, K3 built, optimized, and verified the chip using open-source EDA tools" on Nangate 45nm.
  - Results: 4 mm², 100 MHz timing closure, 1.46M standard cells, 0.277 MB SRAM, INT4 MAC array, >8,700 tokens/s "in simulation".
  - Tools are not named; no tape-out is mentioned. Weights were due "by July 27, 2026" — [Kimi blog](https://www.kimi.com/blog/kimi-k3); [IT之家, 17 Jul 2026](https://www.ithome.com/0/977/961.htm)
  - Company claim, unconfirmed: the design collateral was not public as of later reporting (LinkedIn post via search summary). Yosys/OpenROAD are named only by third parties.
- **Market reaction.**
  - Cadence closed −9.47% on 17 Jul 2026 and Synopsys fell ~9% — [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026); [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/cadence-synopsys-slide-kimi-k3-162824133.html)
  - Chinese closes, 16 Jul → 20 Jul 2026: Empyrean 106.21→93.72 (−11.8%), Primarius 43.42→34.75 (−20.0%), Semitronix 87.57→68.35 (−21.9%), Suochen 184.08→147.50 (−19.9%), ZWSOFT −7.6%. Paratera rose (Eastmoney daily data, my calculation; causation not established).
- **GPUs and agents.** See Q2 transitions (Hygon DCU port; PyAether agent; Agentic DFT; UDA 2.0). An industry insider says AI-EDA needs a "大管家" (scheduler) across many models, and expects faster gains in digital design than in physics simulation — [36Kr](https://www.36kr.com/p/3741032844410885)
- **Compute supply.** NVIDIA says it is "effectively foreclosed" from China's data-centre compute market — [NVIDIA 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm). This pushes Chinese solvers toward domestic accelerators (inference).
- **AI weather.** CMA operational models (Q1/Q4). ECMWF dropped Pangu, partly as first-generation models "are increasingly out of date" — [ECMWF](https://www.ecmwf.int/en/about/media-centre/aifs-blog/2026/farewell-external-ai-models)

### Inferences
- The K3 demo threatens the "seat for routine digital flow" layer, not analog/SPICE, physical-verification or foundry judges. That is where Chinese vendors are strongest and where policy protects them.

### Gaps
- No independent reproduction of K3's chip, nor the exact toolchain. GPU or Ascend versions of Suochen/PHengLEI solvers and their benchmarks are not verified.

## Q7. Entry-point data (valuation and access; separate judgment)

### Takeaway
Multiples are extreme on earnings and high on sales, even after 2026 falls. All Shanghai/Shenzhen names are Northbound-eligible. Sugon is barred to US persons (NS-CMIC). Paratera (BSE) has no Stock Connect route.

### Cited Findings
- **Closing data, 12 Nov 2026** (TTM multiples) — [Eastmoney valuation table](https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPT_VALUEANALYSIS_DET&columns=ALL&filter=(SECURITY_CODE=%22301269%22)); Sugon/Hygon from the [Tencent quote](https://qt.gtimg.cn/q=sh603019,sh688041). Price RMB / market value / PE / PS / PB:
  - Empyrean 89.92 / RMB49.3bn / 625x / 33.3x / 9.1x
  - Primarius 32.91 / 17.5bn / n.m. (loss) / 29.8x / 4.3x
  - Semitronix 56.35 / 11.3bn / 91.6x / 12.7x / 3.6x
  - Suochen 181.99 (−9.7% on the day) / 16.2bn / 1,322x / 30.5x / 6.0x
  - ZWSOFT 49.45 / 8.4bn / 152x / 9.0x / 3.3x
  - Hollywave 29.53 / 3.0bn / n.m. / 11.1x / 5.0x
  - Paratera 87.80 / 5.3bn / 64x / 2.8x / 9.0x
  - Sugon 80.02 / ~117bn / ~40x and ~6.4x PS (my TTM calculation)
  - Hygon 202.37 / ~470bn
- **Ranges since listing (daily TTM).**
  - Empyrean PS 31.9x (30 Oct 2026, low) to 113.5x (Aug 2022), median 52.1x; positive PE 167x to >4,000x, median 346x.
  - Primarius PS 14.9x (Sep 2024) to 105.6x (Dec 2021), median 33.7x.
  - Semitronix PS 11.3x (3 Nov 2026, low) to 145x (Aug 2022), median 24.6x; PE 64x to 481x, median 129x.
  - Suochen PS 10.2x (Aug 2024) to 56.2x (26 Jun 2026), median 21.3x.
  - ZWSOFT PS 7.9x (Jul 2026, low) to 78.5x (2021), median 16.1x.
  - Paratera PS 2.5x (3 Nov 2026) to 26.9x (Feb 2025).
- **2026 price history (31 Dec 2025 → 12 Nov 2026).** Empyrean −15.4%; Primarius −5.5% (high 53.00, 9 Jul); Semitronix −21.4% (30 Jun close 118.05); Suochen +81.5% (peak 294.12, 26 Jun); ZWSOFT −27.4% (unadjusted series); Hollywave −44.2%; Paratera −33.8%. All fell sharply in July 2026 (Q6).
- **Stock Connect.** The HKEX Northbound buy-and-sell lists updated 12 Nov 2026 include Empyrean and Semitronix (SZSE) and Primarius, Suochen, ZWSOFT, Hollywave, Sugon and Hygon (SSE); Paratera is absent — [HKEX SSE list](https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities_xls/SSE_Securities.xls); [HKEX SZSE list](https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities_xls/SZSE_Securities.xls)
- **US-person restriction.** OFAC non-SDN list: "DAWNING INFORMATION INDUSTRY CO., LTD", program CMIC-EO13959, ticker 603019 CN, ISIN CNE100001TW7, listed 16 Dec 2021, effective 14 Feb 2022. No entry for Empyrean, Suochen, Hygon or the others — [OFAC consolidated non-SDN CSV, downloaded 12 Nov 2026](https://sanctionslistservice.ofac.treas.gov/api/PublicationPreview/exports/CONS_PRIM.CSV)
- **Upcoming events.** Paratera's inquiry reply (by 9 Dec 2026); Suochen's no-sale pledge (to ~May 2027); Empyrean's 奇捷 deal closing; the Affiliates Rule and Busan deadline (10 Jan 2027); FY2026 annual reports (Apr 2027).

### Inferences
- Entity listing does not bar portfolio investment, but it raises counterparty, index and compliance risk; NS-CMIC does bar US persons (Sugon). Private names (DP Technology, Xpeedic, UniVista, IBE, DJEL) have no public route; US outbound-investment rules may also restrict private stakes (not re-verified).

### Gaps
- QFII/RQFII access rules for BSE, ETF holdings of these names, Hong Kong listings or plans (DP Technology's reported HK plan is unconfirmed), and forward consensus multiples were not verified.

## Could not verify; dated source list

### Could not verify
- Any third-party confirmation of Empyrean's or Primarius's foundry certifications, or the foundries' names.
- 2025-26 NNSA approvals of domestic codes; CAAC/COMAC use of domestic CAE; C-NCAP virtual-testing clauses.
- Revenue and IPO status of IBE/Simdroid, PERA, Tongyuan, TenFong, Intesim, Hongzhiwei, DJEL, Xpeedic (post-tutoring), UniVista and X-Epic.
- Defence or SOE revenue shares. BIS's stated reason for Suochen's listing, and whether Suochen disclosed it.
- FuXi and FengWu operational use and licences. Independent CMA verification. GPU/Ascend solver benchmarks. A Kimi K3 reproduction.
- Chinese industrial-software policy documents and funding amounts for 2025-26.

### Sources (publication dates; all accessed 12 Nov 2026)
- **Company filings via Eastmoney/cninfo PDFs.**
  - Empyrean: annual report 28 Apr 2026, H1 report 29 Aug 2026, plus announcements of 3 Dec 2024, 10 Dec 2024, 31 Mar 2025, 9 Jul 2025, 11 Dec 2025, 8 Oct 2026, 13 Oct 2026 and 2 Nov 2026.
  - Primarius: annual report 16 Apr 2026; CSRC approval 24 Jun 2026.
  - Semitronix: annual report 23 Apr 2026. Suochen: annual report 28 Apr 2026; announcement 4 Nov 2026. ZWSOFT: annual report 23 Apr 2026.
  - Paratera: annual report 3 Apr 2026; filings 29 Sep and 11 Nov 2026. Sugon: 10 Dec 2025.
- **Data.** Eastmoney F10 and valuation APIs (12 Nov 2026); Tencent quotes (12 Nov 2026); HKEX eligible lists (12 Nov 2026); eCFR Part 744 (9 Nov 2026 version); OFAC CONS_PRIM (12 Nov 2026); TOP500 (Jun 2026); Matbench Discovery (12 Nov 2026).
- **US filings.** Synopsys 10-Q (Q3 FY2026) and 10-K (FY2025); Cadence (17 Feb and 26 Oct 2026); NVIDIA 10-K (FY2026).
- **Press and analysis.** IDC 10 Aug 2026; 36Kr 27 Mar 2026; NBD 2 Nov 2026; Gelonghui 30 Oct and 3 Nov 2026; Stockstar 9 Nov 2026 and 4 Mar 2026; 10jqka 27 and 29 Oct 2026; Caiwen 29 Oct 2026; Kimi blog 16-17 Jul 2026; IT之家 17 Jul 2026 and 21 Apr 2026; TIKR/Yahoo Jul 2026; ECMWF 11 May 2026; Xinhua 19 Dec 2025 and 28 Apr 2026; People's Daily 6 Dec 2025; PEdaily 24 Dec 2025; DPA4 blog 22 May 2026; Frontiers 24 Dec 2021 (old); China Daily Dec 2015 (old); Reed Smith 6 Nov 2026; Thompson Hine Nov 2026; TechCrunch 30 May 2025; Business Standard 3 Jul 2025; Schnitger 14 Jul 2025; Malay Mail 18 Jun 2026; Yicai 22 Oct 2026; QYResearch 17 Oct 2025; Investing.com (Dassault Q3 2026).

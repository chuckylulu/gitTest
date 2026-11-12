# Advanced packaging and chip stacking for AI processors at foundries and OSATs (2.5D/3D: CoWoS, SoIC, EMIB, Foveros, I-Cube, X-Cube, fan-out, panel-level) — research notes as of 12 November 2026

Status: COMPLETE for this pass (12 Nov 2026).

Research limits (read first): partway through, the shared WebSearch budget ran out and the Firecrawl account had no credits left. After that point, evidence came only from fetching URLs already found and from primary transcripts and filings, which I downloaded and parsed locally (TSMC 4Q25 and 2Q26 call transcripts; Intel's 2025 Annual Report). I did not search Korean-, Japanese- or Chinese-language sources (DART, TDnet/EDINET, cninfo), so coverage of Korean and Chinese mid-tier houses is thin (see §7).

Conventions: "primary" means a company filing or transcript; "secondary" means trade press or an analyst. "Company claim, unconfirmed" means I found no outside confirmation. "(calc.)" marks my own arithmetic on cited figures. No share-price or valuation data is used, by instruction.

---

## (1) Segment map

### Takeaway
At the high end of AI-processor packaging (2.5D silicon-interposer/bridge packages and 3D hybrid bonding), money and capacity are concentrated in integrated manufacturers, led by TSMC. Yole puts six integrated firms (Intel, TSMC, YMTC, SK hynix, Samsung, Micron) at ~97% of 2025 "high-end performance packaging" revenue. Outsourced assembly-and-test houses (OSATs), led by ASE and then Amkor, handle the back-end steps (on-substrate assembly, test), overflow and full-process alternatives, and are now growing faster than they have for years. China runs a parallel, domestically-directed chain (JCET, Tongfu, Huatian, SJ Semiconductor). Japan, Singapore, India and Europe have pilot-stage or non-AI entrants only. I found no AI-processor packaging house in Israel.

### Segment map table
Tickers are the standard exchange identifiers and were not re-verified this session unless a cited URL shows them.

| Company | Home | Listing / ticker | Role in AI packaging | Why it matters, or why left out |
|---|---|---|---|---|
| TSMC | Taiwan | TWSE 2330; NYSE TSM | Foundry with captive advanced packaging: CoWoS-S/-L, InFO, SoIC hybrid bonding, SoW, CoPoS panel pilot, COUPE optics | KEY. Makes the large majority of CoWoS output. Advanced packaging "slightly over 10%" of 2025 revenue, guided to "low-teens %" in 2026 ([TSMC 4Q25 call, 15 Jan 2026](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf)) |
| ASE Technology Holding (ASE, SPIL, USI) | Taiwan | TWSE 3711; NYSE ASX | Largest OSAT: on-substrate (oS) back-end for CoWoS, full-process 2.5D, fan-out, test, CPO assembly, EMS | KEY. 44.6% of 2024 top-10 OSAT revenue ([TrendForce via Lapedus, 13 May 2025](https://marklapedus.substack.com/p/ase-amkor-top-osat-rankings-but-china)). LEAP (its advanced packaging and test line) >US$4bn in 2026 ([ASE 3Q26 call](https://www.investing.com/news/transcripts/earnings-call-transcript-ase-technology-beats-q3-2026-estimates-on-margin-surge-93CH-4982306)) |
| Amkor Technology | USA (ops mainly Korea, SE Asia, Japan) | NASDAQ AMKR | #2 OSAT: high-density fan-out (HDFO), 2.5D, test; first large US OSAT campus (Arizona) | KEY. 15.2% of 2024 top-10 OSAT revenue (TrendForce, same source). Advance payments from "a dozen customers" ([Amkor 3Q26 call](https://www.fool.com/earnings/call-transcripts/2026/10/26/amkor-amkr-q3-2026-earnings-call-transcript/)) |
| Intel (Intel Foundry) | USA | NASDAQ INTC | Integrated manufacturer: EMIB, EMIB-T, Foveros (-B/-R/-S/Direct), packaging-only foundry service | KEY. The main non-TSMC alternative to CoWoS. "Significant external customer traction" (company claim, unconfirmed) ([Intel 3Q26 call summary](https://finance.yahoo.com/markets/stocks/articles/intel-corp-intc-q3-2026-051348065.html)) |
| Samsung Electronics (foundry and advanced packaging) | Korea | KRX 005930 | Integrated manufacturer: I-Cube (2.5D), X-Cube (3D), SAINT design platform, panel-level, HBM plus logic turnkey | KEY on scale, but evidence is thin. Foundry gains in 3Q26 came from "HBM base-die and advanced-node sales" ([Lapedus, Nov 2026](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)) |
| JCET Group (owns STATS ChipPAC) | China | SSE 600584 | China's largest OSAT; XDFOI chiplet/fan-out; glass and panel pilot lines | KEY for China. 3Q26 computing revenue +54% YoY (Lapedus, same source) |
| SJ Semiconductor (盛合晶微) | China | SSE STAR Market (code not verified) | 2.5D silicon-interposer and 3D wafer-level packaging specialist (SMIC–JCET JV, founded 2014) | Brief. Listed 21 Apr 2026; ~RMB4.8–5bn raised for 3D multi-chip integration ([TrendForce, 23 Apr 2026](https://www.trendforce.com/news/2026/04/23/news-china-osat-sj-semiconductor-reportedly-raises-rmb-5b-in-ipo-largest-a-share-offering-of-2026-so-far/)) |
| Tongfu Microelectronics (TFME) | China | SZSE 002156 | OSAT; AMD's core assembly/test partner (TF-AMD Penang and Suzhou) | Brief. 8% of 2024 top-10 OSAT revenue (TrendForce). AMD reportedly holds 15% of the TF-AMD JVs ([Quartr 3Q25](https://quartr.com/events/tongfu-microelectronics-co-ltd-002156-q3-2025_FgfqXMee)). 3Q26 figures not found |
| Tianshui Huatian (HT-Tech) | China | SZSE 002185 | OSAT investing in high-end AI/HPC packaging | Brief. 2024 revenue US$2.01bn (+26%, fastest in top 10) (TrendForce). No 2026 data found |
| WiseRoad / UTAC | China / Singapore | Private | OSAT, mainly mainstream | Left out: 2024 revenue US$1.56bn; parent reportedly considering a sale of UTAC; no AI 2.5D evidence (TrendForce) |
| Powertech Technology (PTI) | Taiwan | TWSE 6239 | Memory OSAT; panel-level fan-out | Brief. 5.5% of 2024 top-10, "transition phase in advanced packaging" (TrendForce). 2026 AI evidence not verified (search budget exhausted) |
| KYEC (King Yuan Electronics) | Taiwan | TWSE 2449 | Test house; CoWoS and AI-GPU test | Brief, but a "judge" (a test gate). TrendForce notes "AI server, HPC and CoWoS testing demand growing". 2024 revenue US$0.91bn |
| ChipMOS | Taiwan | TWSE 8150; NASDAQ IMOS | Display-driver and memory OSAT | Left out: no AI 2.5D/3D role (TrendForce 2024: US$0.71bn) |
| UMC | Taiwan | TWSE 2303; NYSE UMC | Foundry; interposers and advanced-packaging engagement | Brief. 3Q26: "advanced packaging and silicon photonics" engagement strong, some capacity being converted ([Lapedus](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)). Interposer volumes not verified |
| GlobalFoundries | USA | NASDAQ GFS | Foundry; first US source of silicon interposers for TSMC CoWoS | Brief. 5-year, ~US$2bn TSMC interposer deal; volume from 1H28 at Malta, NY ([GF 3Q26 6-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/0001709048/000170904826000259/globalfoundries3q2026earni.htm)) |
| Hana Micron | Korea | KOSDAQ 067310 | Memory-focused OSAT (Korea, Vietnam) | Brief. 2024 revenue US$0.92bn (+23.7%) on memory customers (TrendForce). No AI 2.5D evidence found |
| Nepes; SFA Semicon | Korea | KOSDAQ 033640; 036540 | Fan-out/panel-level (Nepes); memory OSAT (SFA) | Not verified this session. No 2026 sources retrieved (search budget exhausted; Korean-language press not searched) |
| Rapidus (Rapidus Chiplet Solutions) | Japan | Private, government-backed | 2.5D/3D and 600 mm panel RDL-interposer pilot at Chitose | Brief. RCS opened 11 Apr 2026 ([PR Newswire](https://www.prnewswire.com/news-releases/rapidus-opens-analysis-center-and-rapidus-chiplet-solutions-302739433.html)). Pilot stage |
| Resonac (JOINT2/JOINT3 consortia) | Japan | TSE 4004 | Materials maker leading a panel-level organic-interposer consortium | Brief. JOINT3 reportedly had 28 members by May 2026 (single blog source, unconfirmed) ([DataM blog](https://www.datamintelligence.com/blogs/top-companies-in-advanced-packaging-japan)). Materials are covered by other researchers |
| Silicon Box | Singapore (plant in Italy) | Private | Panel-level chiplet integration and panel-level test | Brief. Novara, Italy plant (up to €3.2bn) granted "Open EU Foundry" status 16 Mar 2026; full capacity 2033 ([European Commission](https://digital-strategy.ec.europa.eu/en/news/open-eu-foundry-status-granted-innovative-chiplet-facility)) |
| Tata Electronics | India | Private (Tata group) | OSAT at Jagiroad, Assam | Brief. Pilot production from ~early Oct 2026; not 2.5D AI ([EFY](https://www.electronicsforyou.biz/industry-buzz/tata-electronics-starts-pilot-runs-at-assam-semiconductor-plant/)) |
| CG Semi (CG Power–Renesas–Stars JV); Kaynes Semicon | India | Parents listed on NSE/BSE (tickers not verified) | Mainstream OSATs at Sanand | Left out for AI. CG Semi G1 in commercial production 4 Jul 2026; Kaynes in production 31 Mar 2026 (power modules) ([semiconductor.cv](https://semiconductor.cv/blog/india-semiconductor-fabs-2026)) |
| Micron Sanand (India ATMP) | India / USA | NASDAQ MU | Memory assembly and test | Out of scope (memory makers' own stacking). Not verified this session |
| Tower Semiconductor | Israel | NASDAQ/TASE TSEM | Specialty foundry (silicon photonics, SiGe) | Left out: not a packaging house. 3Q26 revenue US$526m (+33%) on SiPho (Lapedus). Relevant to the optics researchers |
| Intel Fab 28 (Kiryat Gat) | Israel (Intel site) | — | Front-end wafer fab (Intel 10/7nm) | Left out: not packaging. Shut after an accident around 14 Oct 2026, ~US$300m revenue hit each in 4Q26 and 1Q27 (Intel call summary) |

### Inferences
- **Europe:** the only AI-relevant advanced-packaging project I found is Silicon Box's Novara plant, which is pre-production (full capacity 2033). European AI-relevant players otherwise sit in substrates (AT&S) and equipment (Besi), which other researchers cover. I found nothing to show any European OSAT doing 2.5D/3D AI packaging at volume.
- **Israel:** no AI-processor packaging house. Israel's relevance is front-end (Intel Fab 28), specialty foundry (Tower) and inspection/metrology equipment (covered elsewhere).
- **India:** all entrants are mainstream OSAT or memory ATMP. None does 2.5D/3D AI packaging.

### Gaps
- No TrendForce 2025 OSAT ranking found; the latest verified ranking covers 2024.
- Korea (Nepes, SFA Semicon, LB Semicon, Hana Micron 2026 data) and mid-tier China (Huatian, Tongfu 2026) are thin because Korean- and Chinese-language sources were not searched.
- The tickers for SJ Semiconductor and the Indian parents were not verified.

---

## (2) Evidence on tests (a)–(e) for key companies

Key companies: TSMC, ASE, Amkor, Intel (packaging), Samsung (packaging), JCET. SJ Semiconductor gets a brief entry as China's 2.5D specialist.

### 2.1 TSMC

**(a) Position: owns a physical constraint (capacity plus process know-how). Does not merely fill a gap.**
- The CEO says the constraint is real and binding. "Our packaging capacity is so tight that now it limits my customers' growth" ([2Q26 call, 16 Jul 2026, primary](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf)). "The gap between demand and supply are still quite big" and "a little bit shortage on the back end" ([3Q26 call, 15 Oct 2026, secondary transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695)).
- Testers are also short: "the tester in shortage, so we have to put more CapEx in the tester" (2Q26 call). The test "judge" is becoming a bottleneck in its own right. Test time per AI chip is reportedly ~4x Hopper for Blackwell and ~7x for Rubin (secondary) ([vlsi.kr, 27 Oct 2026](https://www.vlsi.kr/en/cowos-price-hike-mb-en/)).
- Product classification (2026 symposium roadmap via [fiisual, 2 Jun 2026](https://fiisual.com/blog/post/2026/2026-tsmc-technology-forum-highlights-ai-semiconductor-blueprint) and [SemiEngineering, 27 Apr 2026](https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/)):
  - **CoWoS-L, 5.5 reticles:** BRIDGE. In production with ">98% yield in 2026" (company claim, unconfirmed).
  - **CoWoS-L successors on the same wafer-based platform:** 14 reticles with 20 HBM stacks in 2028; beyond 14 reticles with 24 HBM in 2029.
  - **SoW-X (wafer-scale):** 40 reticles, 64 HBM stacks plus 16 compute dies, in 2029.
  - **CoPoS (panel, 310x310 mm first):** SUCCESSOR to the wafer interposer. Pilot line tools from Feb 2026, completion ~Jun 2026, volume 2028–29 (secondary: Commercial Times/CNA via [TrendForce, 13 Apr 2026](https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/); dual-track tool evaluation per [TrendForce, 16 Jun 2026](https://www.trendforce.com/news/2026/06/16/news-tsmc-reportedly-runs-dual-track-evaluation-on-copos-pilot-line-sparking-global-vs-local-vendor-competition/)).
  - **SoIC hybrid bonding:** SUCCESSOR to micro-bumps, already shipping. 9 µm pitch in mass production; 6 µm N2-on-N2 in 2028; 4.5 µm A14 in 2029.
  - **COUPE co-packaged optics:** SUCCESSOR. First 200G micro-ring modulator in mass production in 2026 (company roadmap claim, unconfirmed).
  - **Glass/new substrate pilot line:** "takes about another one year to be mature" (Wei, 16 Jul 2026), i.e., about mid-2027.
- Slips recorded:
  - A16 (front-end) now shown for 2027, previously advertised for late 2026 (SemiEngineering, 27 Apr 2026).
  - The 2025 roadmap's "9.5-reticle CoWoS in 2027" did not appear in the 2026 write-ups I found. In Oct 2026 Wei said "we are working on the 9X reticle size and moving into the 14X." That 2027 date is unconfirmed, not shown to have slipped.

**(b) Lead: strong outside evidence.**
- Yole: TSMC is one of six integrated firms holding ~97% of 2025 high-end performance packaging revenue ([Electronics Weekly, 25 Sep 2026](https://www.electronicsweekly.com/news/business/advanced-packaging-to-be-a-51bn-market-by-2031-2026-09/)). The scope is inferred from the article's context: it does not restate the scope next to the 97% figure. The list includes memory makers' 3D NAND hybrid bonding, so it is not a pure 2.5D share.
- Morgan Stanley (analyst): NVIDIA booked ~800–850k CoWoS wafers for 2026, ~60% of TSMC output ([clusterbid](https://clusterbid.com/blog/gpu-supply-chain-2026-tsmc-cowos-nvidia-allocation-lead-times)). Silicon Analysts: NVIDIA, Broadcom and AMD together take ≥85% ([TechTimes, 28 Jul 2026](https://www.techtimes.com/articles/321754/20260728/ai-supply-crisis-moves-upstream-advanced-packaging-becomes-binding-constraint.htm)).
- AMD is "a key SoIC customer" (TrendForce, 13 Apr 2026).
- On the competitor alternative, Wei said it offers "a very competitive solution", but that TSMC is the only one producing 5x-reticle packaging at scale (company claim, unconfirmed; 3Q26 call).
- Bloomberg Intelligence forecasts TSMC holding >40% of advanced packaging, with OSATs doubling to 16% by 2033 (forecast) ([Bloomberg Intelligence press release](https://www.bloomberg.com/company/press/advanced-semiconductor-packaging-market-could-reach-80-billion-by-2033-as-ai-chips-spread-to-consumer-devices-according-to-bloomberg-intelligence/)).

**(c) Revenue model.**
- Hardware (wafers and packaging services) priced per wafer or package. It recurs through multi-year capacity planning with customers rather than contract annuities: "it takes more than five years to develop the technology and product, prepare the capacity" (2Q26 call).
- No labour-hour or per-seat exposure.
- Pricing power: CoWoS price increases of 10–20% are reportedly "being prepared" across TSMC and OSATs (Commercial Times via [vlsi.kr, 27 Oct 2026](https://www.vlsi.kr/en/cowos-price-hike-mb-en/), secondary).
- Packaging revenue: ~8% (2024), "slightly over 10%" (2025), "low-teens %" (2026 guide). That is ≈US$12bn+ in 2025 and ≈US$20bn+ in 2026 if 2026 revenue grows ~40% (calc.). TrendForce (13 Apr 2026) instead says ~8% in 2025 and >10% in 2026. That conflicts with TSMC's corrected transcript, which I treat as authoritative; TrendForce looks a year behind.
- Prepayments or long-term agreements for packaging: none found.

**(d) Financial strength (primary).**
- **FY2025** (published 15 Jan 2026):
  - Revenue US$122bn (+35.9% in US$); NT$3.8tn (+31.6%).
  - Gross margin 59.9%; operating margin 50.8%; ROE 35.4%.
  - Operating cash flow NT$2.3tn; capex NT$1.3tn = US$40.9bn (~33.5% of revenue, calc.); free cash flow NT$1tn (+15.2%); dividends NT$467bn.
  - AI accelerators were "high-teens percent" of revenue.
- **3Q26** (published 15 Oct 2026; [6-K release](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm) and [presentation](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26presentatione.htm)):
  - Revenue US$46.72bn (+41.2% YoY in US$; NT$1,494.24bn, +50.9%).
  - Gross margin 66.4%; operating margin 58.7%; net margin 51.1%.
  - Operating cash flow NT$919.77bn; capex NT$443.21bn; free cash flow NT$476.56bn.
  - Cash and marketable securities NT$4,016.98bn against long-term interest-bearing debt NT$818.38bn, i.e., net cash ≈NT$3.2tn (calc., netting long-term interest-bearing debt only).
  - Annualised ROE 45.5%; inventory days 82 (74 a year earlier).
- **Guidance:** 4Q26 revenue US$52.3–54.3bn, gross margin 65–67%. FY2026 growth "slightly above 40%" (Jul 2026). 2026 capex US$60–64bn, raised from US$52–56bn; 10–20% of it goes to "advanced packaging, testing, mask making and others".
- **Concentration:** customer and geography shares were not retrieved (see §7). By analyst estimate NVIDIA alone takes ~60% of CoWoS wafers.
- **Manufacturing footprint:** advanced packaging is essentially all in Taiwan today; "13 leading-edge and advanced packaging fabs in Taiwan" are under construction (Jul 2026).
- **Arizona:** first advanced packaging fab in permitting (Jan 2026), plus an extra US$100bn for logic and "advanced packaging fabs" (Jul 2026). First Arizona packaging volume is due in 2028 per CNA (via TrendForce, 13 Apr 2026), but the facility is due in 2029 per [The Register, 8 Oct 2026](https://www.theregister.com/systems/2026/10/08/tsmc-taps-globalfoundries-to-bolster-us-silicon-interposer-production-in-2b-deal/5302061). The two sources conflict.

**(e) Resilience.**
- **Steady growth (prior ~55%):** capacity-limited upside. Goldman (analyst) has CoWoS at 1.275m wafers in 2026, 2.73m in 2027 (+114%) and 3.48m in 2028 (+27%) ([TrendForce, 16 Oct 2026](https://www.trendforce.com/news/2026/10/16/news-after-tsmcs-3q26-earnings-key-brokerage-takeaways-as-2028-capex-forecasts-reach-us105b/)).
- **Financing-led pause around 2028 (prior ~25%):** the most resilient in the segment. It holds net cash, generates positive free cash flow while spending record capex, and makes a 58.7% operating margin. The main exposure is fixed-cost build-up: depreciation rose "high-teens %" in 2026 (Jan 2026 guide), and broker capex forecasts are US$83–90bn for 2027 and US$92–105bn for 2028 (analyst estimates, same TrendForce source).
- **Acceleration (prior ~20%):** constrained by tools ("tool price inflation is real", CFO, 3Q26) and by equipment delivery times, which lengthened from 3–6 to 6–8 months (vlsi.kr).
- **Cycle position:** peak tightness. Demand is above supply, prices are rising, tool lead times are lengthening, and inventory days are up from 74 to 82 (calc. from the presentation).
- **Cross-border exposure:**
  - Taiwan concentration of packaging.
  - US 25% duty on certain advanced chips made abroad that transit the US (proclaimed Jan 2026) ([WSGR](https://www.wsgr.com/en/insights/a-mixed-bag-of-chips-significant-new-import-and-export-changes-for-advanced-semiconductors.html)).
  - BIS case-by-case licensing for H200-class chips to China (from 15 Jan 2026) ([Morgan Lewis](https://www.morganlewis.com/pubs/2026/01/bis-revises-export-review-policy-for-advanced-ai-chips-destined-for-china-and-macau)).
  - Overseas-fab gross-margin dilution of 2–3%, widening to 3–4% (2Q26 call).

### 2.2 ASE Technology Holding (including SPIL)

**(a) Position: physical constraint (cleanroom space and capacity, oS and test know-how), plus a test "judge".**
- "The biggest bottleneck today is really still the space"; 22 building projects are under way in Taiwan; test capacity waits on facilities, and wafer sort is prioritised over final test (3Q26 call, 29 Oct 2026, secondary transcript [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-ase-technology-beats-q3-2026-estimates-on-margin-surge-93CH-4982306)). Testing was NT$23.7bn (18.8%) of ATM revenue in 2Q26 ([ASE 2Q26 6-K, 30 Jul 2026, primary](https://www.sec.gov/Archives/edgar/data/0001122411/000095010326011353/dp250875_6k.htm)).
- Product classification:
  - **On-substrate (oS) assembly for CoWoS:** BRIDGE, tied to TSMC's wafer-based CoWoS. Whether CoPoS keeps an outsourced oS step is unknown. A TSMC subsidiary is reportedly entering oS, a competitive risk (analyst question on the 3Q26 call; ASE called it "sensitive").
  - **Full-process 2.5D:** BRIDGE-type alternative capacity. ~US$300m in 2026, ">US$1bn" in 2027 (company claim, unconfirmed).
  - **CPO assembly:** SUCCESSOR. "We already started mass production in Q4," with >US$0.5bn in 2027 (company claim, unconfirmed).
  - **Test:** a durable "judge".
- ASE's own panel-level line was not verified this session.

**(b) Lead: good outside evidence of share, weaker evidence at the leading edge.**
- TrendForce: 44.6% of 2024 top-10 OSAT revenue (US$18.54bn).
- Silicon Analysts: NVIDIA's supplementary CoWoS capacity sits at Amkor and ASE (via TechTimes, Jul 2026).
- Management calls ASE "the dominant player in this field" for oS (company claim, unconfirmed). Note that Yole's 2025 high-end top six excludes OSATs.

**(c) Revenue model.**
- Per-unit packaging and test service fees: recurring with volumes, not contracted annuities.
- Customer "trade financing" helps fund capex (3Q26 call; amounts undisclosed).
- EMS (USI) is low-margin pass-through: 3Q26 gross margin 8.3%, operating margin 3.3%.
- No labour-hour or per-seat pricing disclosed.

**(d) Financial strength.**
- **FY2025** (primary, from the 2Q26 6-K): revenue NT$645.4bn; gross profit NT$114.2bn (17.7%, calc.); operating income NT$50.8bn (7.9%, calc.); net income NT$40.7bn. 2025 capex ≈US$3.4bn (sum of quarterly chart, calc.).
- **2Q26** (primary): revenue NT$191.06bn (+27% YoY); gross margin 21.0%; operating margin 11.1%; ATM revenue NT$125.07bn.
  - ATM mix: communications 41%, computing 30%, auto/consumer/other 29%.
  - Cash NT$91.3bn; interest-bearing debt NT$306.2bn; net debt/equity 0.47.
- **3Q26** (released 29 Oct 2026; secondary summaries [BigGo](https://finance.biggo.com/news/TW_3711.TW_2026-10-29), [Lapedus](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)):
  - Revenue NT$244.16bn (+44.8% YoY); gross margin 22.1%; operating margin 13.6%; net income NT$27.0bn.
  - ATM NT$151.49bn (+51%), with gross margin 30.6% and operating margin 20.0%. ATM is 62% of revenue and 91% of operating profit. Management: gross margin "surpassed our historical structural margin ceiling".
  - Interest-bearing debt NT$406.5bn; net debt/equity 66% (expected to peak).
  - Annualised ROE ≈25% (calc., rough: 4 × NT$27.0bn against NT$419bn equity at Jun 2026).
- **Capex and cash:** 2026 capex US$11.5bn, raised from US$10.5bn (half facilities, half equipment; 60% of equipment is LEAP). 2027 capex "even larger". Free cash flow negative in 2026 and 2027 (company).
- **Concentration:** customer and geography shares were not retrieved (20-F not accessed).

**(e) Resilience.**
- **Steady growth:** strong. LEAP doubles in 2027, and pricing is "very pricing-friendly" (CFO).
- **Pause around 2028:** the most exposed of the leaders. Capex is roughly 3.4x the 2025 level and ~40%+ of 2026 revenue (calc.: 2026 revenue ≈NT$870bn ≈US$27bn using 4Q guide +6–8%). Debt rose ~NT$100bn in 3Q26 (secondary), and free cash flow is negative for two years. A pause would leave high fixed costs and leverage, partly offset by customer trade financing.
- **Acceleration:** gains overflow and pricing, but is space-limited.
- **Cycle:** at or near full utilisation; prices rising.
- **Cross-border:** Taiwan-centred build-out, with all 22 projects in Taiwan. No US plant was mentioned on the call. Tariff and export-control impact was not discussed on the call and was not verified.

### 2.3 Amkor Technology

**(a) Position: physical constraint (Korean HDFO/2.5D capacity; the first large US OSAT campus). Not a judge, although test is integrated "turnkey".**
- **2.5D programs:** BRIDGE. Two new programs (networking, data centre) online in 4Q26.
- **HDFO:** BRIDGE/alternative. Flagship CPU program scaling, plus a second "hyperscaler" CPU program ramping 3Q26.
- **Fan-out bridge:** SUCCESSOR-type. "On track for a late 2027 start into 2028."
- **Arizona (Peoria):** ~US$12bn over two phases. Phase 1 construction done by end-2027; packages "early 2028"; the customer ramps late 2028 (all 3Q26 call, 26 Oct 2026, [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/26/amkor-amkr-q3-2026-earnings-call-transcript/); [Lapedus](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)).
- I found no evidence of Amkor hybrid-bonding or panel-level programs for AI.

**(b) Lead.**
- TrendForce: #2 OSAT, 15.2% of 2024 top-10 revenue.
- TSMC contracted Amkor for CoWoS-compatible packaging in the US (The Register, 8 Oct 2026).
- New Gwangju (Korea) buildings support HDFO ramps "including the recent announcement with NVIDIA" (3Q26 call).
- Silicon Analysts names Amkor as supplementary NVIDIA capacity.

**(c) Revenue model.**
- Per-unit service fees. Packaging is 88% of sales and test 12% (3Q26).
- Advance-payment arrangements with "a dozen customers" since 2025, "tied to future capacity requirements", with "several more" under discussion. Amounts are undisclosed; an analyst cited ~US$3bn, which is not a management figure.

**(d) Financial strength (primary 8-Ks).**
- **FY2025:** net sales US$6.71bn (+6%); gross margin 14.0%; operating margin 7.0%; net income US$374m.
  - Operating cash flow US$1.10bn; capex US$905m; free cash flow US$308m.
  - Cash plus short-term investments US$1.99bn; debt US$1.45bn.
  - Mix: communications 46%, computing 20%; advanced products 83%; top-10 customers 72% ([8-K](https://www.sec.gov/Archives/edgar/data/1047127/000104712726000007/amkr123125erex-991.htm)).
- **3Q26** (26 Oct 2026; [8-K](https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000049/amkr9302026erex-991.htm)):
  - Net sales US$1,991m (+0.2% YoY, +4.9% QoQ); gross margin 18.3% (14.3% a year earlier); operating margin 11.3%; net income US$191m.
  - Computing 26% of sales (19% a year earlier); communications 37% (51%); top-10 customers 66%.
  - Year to date: operating cash flow US$868m against capex payments US$1,237m, so free cash flow ≈–US$369m (calc.).
  - Cash plus short-term investments US$2.4bn; debt ~US$2.47bn, i.e., net debt ≈US$0.1bn (calc.).
- **Guidance:** 2026 capex ~US$2.5bn (≈33% of 2026 sales, calc.). 4Q26 revenue US$1.9–2.0bn, gross margin 18–19%. Computing growth >30% in 2026 and "similar to even higher" in 2027 (company).
- **Concentration:** the largest single customer was not retrieved (10-K not accessed).
- **Footprint:** Korea (footprint +~40% vs 2025 after the 2028 expansions), Vietnam (SiP), Japan (Kumamoto), Arizona; other sites not verified.

**(e) Resilience.**
- **Pause around 2028:** moderate exposure. Arizona spending peaks in 2028–29, when Phase 2 construction overlaps Phase 1 equipment installation (company). Prepayments may mean "no incremental debt" through 2028 (CFO), but margins are thin, with an operating margin of ~11%.
- **Steady or accelerating growth:** gains from US-made packaging demand and NVIDIA overflow.
- **Cycle:** computing at record levels; communications falling.
- **Cross-border:** a US company, which is positive for US-sourcing rules and CHIPS support (award amount not verified this session). Most capacity is in Korea and Asia. Tariffs were not discussed on the call.

### 2.4 Intel (Intel Foundry advanced packaging)

**(a) Position: a credible alternative technology plus US-based capacity. The binding constraint is substrates, not Intel's know-how.**
- **EMIB:** in high-volume manufacturing since 2017. BRIDGE relative to large CoWoS.
- **EMIB-T:** SUCCESSOR candidate to silicon interposers for large packages. "Introduced EMIB-T in 2025, with adoption expected to scale beginning in 2026" (company claim) ([Intel 2025 Annual Report, SEC](https://www.sec.gov/Archives/edgar/data/50863/000005086326000060/intc014890-arsa.pdf)).
- **Foveros-B and Foveros-R:** "targeted for high-volume manufacturing in 2027".
- **Foveros Direct (hybrid bonding):** "announced in 2025"; HVM date not found.
- **Constraint:** CFO Zinsner said "the first half will remain constrained on Intel 3 wafers and substrates", with added substrate capacity arriving in the back half ([3Q26 call summary, 29 Oct 2026](https://finance.yahoo.com/markets/stocks/articles/intel-corp-intc-q3-2026-051348065.html)). Intel cited "an industry-wide shortage of advanced organic substrates for our EMIB packaging" and said it is adding advanced-packaging capacity "to support strong customer ramps... next year in New Mexico and Malaysia" (3Q26 call, quoted in a search summary of the [Benzinga transcript](https://www.benzinga.com/news/26/10/62725076/intel-q3-2026-earnings-call-transcript); the full page returned 403, so the speaker is not identified). Risk factors cite "industry-wide substrate and memory shortages" ([10-Q, quarter to 26 Sep 2026](https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000191/intc-20260926.htm)).

**(b) Lead: outside evidence of interest, not yet of volume.**
- SemiAnalysis reported that Google's 9th-gen TPU would use EMIB-T, with volume ~2027 (secondary; timeline disputed) ([Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-packaging-gains-traction-as-chip-designers-look-to-skirt-tsmcs-cowos-constraints-googles-reported-decision-for-9th-gen-tpus-highlights-intels-attractive-alternative)).
- MediaTek, at Goldman Sachs Taiwan Day (reported 2 Jun 2026), was quoted saying a next-gen program "is adopting only EMIB-T, tape-out 4Q26, mass production 4Q27". MediaTek then denied the report via Nikkei. It added Intel to its supplier list on 29 May 2026 ([Wccftech](https://wccftech.com/mediatek-says-its-next-gen-program-will-only-use-intels-emib-t-for-packaging/)).
- KeyBanc (analyst): Amazon and Google are potential EMIB customers; Qualcomm AI300 is under evaluation (~1m units ≈US$2–3bn of packaging revenue); substrate yields of ~50–60% at Ibiden and 20–30% at Unimicron could cap a Google ramp at ~5–6m units ([Wccftech](https://wccftech.com/keybanc-says-intel-has-won-contracts-from-broadcom-google-apple-amd-microsoft-and-nvidia-while-amazon-anthropic-and-spacexs-terafab-continue-to-evaluate-its-14a-and-18a-p-processes/); [Lapedus](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)).
- The strongest outside signal is TSMC's own CEO. In Oct 2026, answering an analyst question that named EMIB-T, he called "our competitor" solution "very competitive", without naming Intel. In Jul 2026, on EMIB-T, he said "the technology looks good, according to the newspaper, and we hope they will be successful".
- Against this, no customer has publicly confirmed an EMIB-T volume award. External foundry and assembly/test revenue was only US$411m in 3Q26, "primarily due to a non-recurring customer program", and US$878m over 9M26 (10-Q).

**(c) Revenue model.**
- Packaging-only foundry service priced per unit.
- US$1.2bn of "customer deposits received to secure product supply in future periods" (10-Q; not packaging-specific).

**(d) Financial strength (primary).**
- **FY2025** (Intel 2025 Annual Report):
  - Revenue US$52.853bn (–0.5% vs US$53.101bn, calc.); gross margin 34.8%; operating loss US$2.214bn.
  - Intel Foundry revenue US$17.826bn, operating loss US$10.318bn. Intel Products operating income US$12.739bn.
  - Operating cash flow US$9.7bn. Adjusted free cash flow was negative, but the chart text was garbled, so the figure is not reliable.
  - Three largest customers 43% (19%/12%/12%).
  - Revenue by geography: US 29.8%, China 24.0%, Singapore 18.0%, Taiwan 14.5%, other 13.6% (calc. from US$15.757bn / US$12.694bn / US$9.535bn / US$7.672bn / US$7.195bn).
- **3Q26** ([8-K](https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000188/q326earningsrelease.htm)):
  - Revenue US$16.5bn (+21%); non-GAAP gross margin 44.1%.
  - Intel Foundry revenue US$6.7bn (+58%), operating loss US$1.85bn (9M26 loss US$6.4bn).
  - Operating cash flow US$5.08bn; gross capex US$4.22bn; adjusted free cash flow US$1.64bn.
  - Cash plus short-term investments ≈US$54bn against debt ≈US$50bn (calc.).
- **Guidance:** 4Q26 revenue US$15–16bn, non-GAAP gross margin 38.0% (including the Fab 28 hit). 2026 gross capex ~US$20bn; 2027 "up strongly"; 2027 "likely an investment year without positive free cash flow".
- **Funding events:** NVIDIA US$5.0bn equity (closed 26 Dec 2025); SoftBank US$2.0bn; an Aug 2026 offering of ~US$22.6bn net. The US Commerce Department holds an escrowed-share arrangement, and its warrants become exercisable if Intel owns less than 51% of the foundry (10-Q).

**(e) Resilience.**
- **Pause around 2028:** weak to moderate. Foundry losses are large, and 2027 free cash flow is guided negative, though liquidity is now ample after equity raises.
- **Steady or accelerating growth:** Intel is the main beneficiary of CoWoS overflow, if substrates allow.
- **Cycle:** substrate-constrained until 2H27.
- **Cross-border:** a US packaging footprint (New Mexico) is an advantage under US-sourcing pressure. China was 24% of 2025 revenue, an export-control exposure for the products business. Malaysia packaging is an Asian leg.

### 2.5 Samsung Electronics (packaging)

**(a) Position:** a turnkey HBM-plus-logic-plus-packaging offering.
- I-Cube (2.5D silicon interposer) is a BRIDGE.
- X-Cube 3D: micro-bump in 2024 and bump-less (hybrid) "planned for 2026" per a 2023 article; status in 2026 not confirmed ([3D InCites, Apr 2023](https://www.3dincites.com/2023/04/iftle-553-samsung-foundry-update-amkor-globalfoundries-venture/)).
- A 2026 report says Samsung will make Onyang its core HBM advanced-packaging base (secondary, 11 Nov 2026; page blocked, headline only) ([Sammy Fans](https://www.sammyfans.com/2026/11/11/samsung-boss-vows-ai-semiconductor-pivot-with-new-hbm-advanced-packaging-hub/)).

**(b) Lead:** weak outside evidence. One analysis judges Samsung's packaging maturity about one generation behind TSMC (secondary, in the search summary). No named AI-processor 2.5D customer was confirmed this session.

**(d) Financials (secondary, [Lapedus](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)):**
- 3Q26 revenue KRW195.3tn (+127% YoY); operating profit KRW107.4tn.
- DS (semiconductor) revenue KRW147.1tn, operating profit KRW106.5tn.
- 2026 capex ~KRW84.4tn, of which DS KRW76.8tn.
- Foundry improved on "HBM base-die and advanced-node sales".
- Packaging revenue is not disclosed. The figures are memory-driven, so group strength does not show packaging quality.

**(e)** A strong group balance sheet (not verified this session). A financing-led pause would hit memory first. Korea's technology-protection rules were not verified.

### 2.6 JCET Group

**(a)/(b):**
- China's largest OSAT; #3 globally with 12% of 2024 top-10 revenue (+19.3%) (TrendForce).
- XDFOI fan-out chiplet platform: BRIDGE, an alternative to the silicon interposer.
- Glass-substrate and panel-level work "now moving to pilot lines" (SUCCESSOR, pilot), and XDFOI capabilities for CPO ([Lapedus](https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded)).

**(d) 3Q26** (22 Oct 2026, secondary): record revenue RMB11.43bn (+13.5% YoY); net profit RMB770m (+60%). Computing was 30.9% of 9M26 revenue, up 54% YoY. 2026 capex raised from RMB9.98bn to RMB17.31bn. FY2025 figures were not retrieved.

**(e) Cross-border:** demand is domestic and policy-driven under US controls, which keep Chinese designers away from TSMC CoWoS. The degree of US restriction on JCET itself was not verified.

### 2.7 SJ Semiconductor (brief)
- Founded 2014 as an SMIC–JCET alliance and backed by China's Big Fund.
- Its 2.5D and 3D businesses are in "scaled mass production". Chiplet multi-chip packaging rose from 5.3% of revenue (2022) to >56% (mid-2025).
- **Customer concentration:** top five >90% of revenue; largest customer >70% (prospectus via Investor China/SCMP, [TrendForce, 27 Feb 2026](https://www.trendforce.com/news/2026/02/27/news-sj-semiconductor-reportedly-wins-ipo-nod-as-china-leans-on-advanced-packaging-for-chip-self-reliance/)).
- Listed on the STAR Market 21 Apr 2026 ([Maples](https://maples.com/knowledge/sj-semiconductors-star-market-listing-a-new-milestone-for-cayman-red-chip-companies-in-chinas-a-share-market)).
- Revenue and profit were not retrieved. The lead on its listing is confirmed.

### 2.8 Which AI designers are qualified where (dated; confirmation level noted)

| Designer | Packaging supplier(s) | Evidence level |
|---|---|---|
| NVIDIA | TSMC CoWoS-L (~60% of 2026 CoWoS wafers); back-end overflow at Amkor and ASE; Amkor Korea HDFO buildings tied to the "recent announcement with NVIDIA"; reported CoPoS launch partner | Analyst (Morgan Stanley, Silicon Analysts); Amkor call (primary); CoPoS: secondary ([TechPowerUp](https://www.techpowerup.com/337960/tsmc-prepares-copos-next-gen-310-x-310-mm-packages)) |
| AMD | TSMC CoWoS and SoIC ("key SoIC customer"); Tongfu/TF-AMD for assembly and test | TrendForce Apr 2026; Quartr/TrendForce (secondary) |
| Broadcom | TSMC CoWoS (with NVIDIA and AMD ≥85% of capacity); reported interest in Intel packaging | Silicon Analysts (secondary); Intel interest: low-quality secondary ([Sammy Fans, 1 Sep 2026](https://www.sammyfans.com/2026/09/01/intel-attracts-mediatek-broadcom-and-meta-for-ai-chip-packaging-amid-tsmc-shortage/)) |
| Google (TPU) | TSMC CoWoS today; 9th-gen TPU reported on Intel EMIB-T (~2027) | SemiAnalysis via Tom's Hardware; unconfirmed by Google |
| MediaTek (Google partner) | Dual sourcing, TSMC CoWoS and Intel EMIB (29 May 2026); EMIB-T-only claim later denied | Wccftech/Nikkei (secondary) |
| Amazon | Potential EMIB customer; an unnamed "hyperscaler" HDFO CPU program at Amkor | KeyBanc (analyst); Amkor call (unnamed) |
| Qualcomm | AI300 ASIC evaluating EMIB-T | KeyBanc (analyst), unconfirmed |
| Meta, Microsoft, OpenAI | Not verified this session | Gap |
| Chinese designers (Huawei, Cambricon, etc.) | Domestic: SJ Semiconductor (2.5D; customers unnamed, largest >70%), JCET, Tongfu | Customer names not verified |

---

## (3) Path forward and suggested verdicts

Transitions in play for packagers: (3) solder bump to hybrid bonding; (4) silicon interposer to panel/glass; (2) and (1) co-packaged optics and optical links, through CPO assembly. Transitions (5) cooling and (6) 800 V power touch packaging only indirectly, through warpage, thermal and power-delivery design (EMIB-T's "improved power delivery"). I did not find packaging-house-specific evidence for (5) and (6).

### TSMC — suggested verdict: COHERENT
- **Must pass:** (4) CoWoS to CoPoS/SoW-X; (3) SoIC pitch scaling; (2)/(1) COUPE CPO.
- **Said:** 14x-reticle CoWoS in 2028; SoW-X and 4.5 µm SoIC in 2029; COUPE 200G in 2026; glass/new substrate pilot "another one year to be mature" (Jul 2026).
- **Done:**
  - 5.5x CoWoS in production (yield claim unconfirmed).
  - SoIC 9 µm in mass production (AMD).
  - CoPoS pilot line installed (secondary).
  - GF interposer second source signed (primary, GF 6-K).
  - Capex raised to US$60–64bn; 13 Taiwan fabs and Arizona packaging fabs committed.
- **Funded:** yes, from internal cash flow (3Q26 free cash flow NT$476.56bn). A 1–2 year CoPoS slip is covered, because the bridge (CoWoS-L, up to 14x reticles) is TSMC's own and is still being extended.
- **Timing:** plausible for CoWoS-L and SoIC; panel 2028–29 is the risk, given warpage.
- **What must go right:** panel warpage and yield, tool supply, Arizona execution and dilution, and holding substrate and HBM supply alignment.

### ASE — suggested verdict: PARTLY COHERENT (strong execution, stretched funding, platform dependence)
- **Must pass:** (4) the shift of value from wafer CoWoS (where its oS role is a BRIDGE) to panel. TSMC's CoPoS pilot is in-house, and a TSMC subsidiary is entering oS. It must also pass (2) CPO assembly.
- **Said:** LEAP >US$4bn (2026), doubling in 2027; full-process >US$1bn in 2027; CPO >US$0.5bn in 2027.
- **Done:** CPO mass production 4Q26 (company claim); full-process yields at mass-production level (claim); 2026 capex of US$11.5bn with 22 building projects; capacity running full.
- **Funded:** through debt and customer trade financing, with negative free cash flow in 2026–27 and net debt/equity at ~0.66 (secondary). A 1–2 year slip in a successor (panel, CPO volume) would land on a leveraged balance sheet.
- **Credible successor:** CPO and full-process 2.5D, yes. Its own panel offering was not verified.
- **What must go right:** TSMC keeps outsourcing back-end steps through the CoPoS era; AI demand avoids a 2028 financing pause; pricing holds.

### Amkor — suggested verdict: PARTLY COHERENT
- **Must pass:** (4), and (3) to a lesser degree.
- **Said:** fan-out bridge from late 2027 into 2028; Arizona packages in early 2028; computing growth >30% in 2027.
- **Done:** HDFO and 2.5D programs ramping; NVIDIA-linked Korea build-out; Arizona Phase 1 construction on schedule; a dozen customer prepayment agreements.
- **Funded:** largely, by prepayments plus cash. Management sees possibly no new debt through 2028.
- **Successor gap:** no evidence on hybrid bonding or panel. Its successor story is fan-out bridges plus US location, which is credible but leaves it a bridge-heavy specialist.
- **Timing:** Arizona's customer ramp is late 2028, an exposure if a 2028 pause hits.
- **What must go right:** US-sourcing demand, NVIDIA and hyperscaler program continuity, and margin expansion beyond 18–19%.

### Intel (packaging) — suggested verdict: PARTLY COHERENT
- **Must pass:** (4), where EMIB-T is the organic-bridge alternative that sidesteps silicon interposers, and (3) Foveros Direct.
- **Said:** EMIB-T adoption scales from 2026; Foveros-B/R in HVM 2027; customers "potentially ready to announce in the next two quarters" (Oct 2026); glass work with Lens Technology (8-K).
- **Done:** EMIB in HVM since 2017; EMIB-T launched 2025; capacity adds in New Mexico and Malaysia; US$1.2bn of customer deposits (not packaging-specific).
- **Not done:** no customer-confirmed EMIB-T volume award. External foundry revenue is small (US$411m in 3Q26, non-recurring) and substrates are short.
- **Funded:** at group level after equity raises (~US$54bn cash plus short-term investments), but the foundry loses ~US$2bn a quarter and 2027 free cash flow is guided negative. A 1–2 year slip is fundable but would deepen dependence on outside capital.
- **Timing:** Google and MediaTek-type volume in 2027 is plausible only if substrate yields improve.
- **What must go right:** named customer wins converting to volume in 2027, substrate supply (Ibiden, Unimicron), and the broader Intel Foundry turnaround.

### Samsung (packaging) — suggested verdict: PARTLY COHERENT at best (insufficient evidence)
- **Said (older):** bump-less X-Cube in 2026. **Said (2026, secondary):** an Onyang HBM packaging hub.
- **Done:** HBM4 base-die foundry sales (Lapedus).
- No 2026 evidence of AI-processor 2.5D customer wins, and panel status not verified.
- **Funded:** yes, by memory profits.
- **What must go right:** converting HBM leadership into turnkey logic-plus-HBM packaging wins.

### JCET — suggested verdict: PARTLY COHERENT
- **Said:** glass and panel moving to pilot; XDFOI for CPO.
- **Done:** capex raised to RMB17.31bn; computing +54%.
- **Funded:** yes.
- **Ceiling:** export controls cap access to leading-edge foreign AI designers and tools (not verified in detail). Its domestic AI demand depends on Chinese front-end capacity.

---

## (4) Suggested ordering by quality alone

1. **TSMC.** It owns the binding constraint, has the highest margins in the segment (3Q26 operating margin 58.7%), holds net cash, funds capex from internal cash, and owns both bridge and successor (CoWoS-L, then CoPoS/SoW-X; SoIC; COUPE).
2. **ASE Technology Holding.** It leads the specialists by a wide margin (≈45% of top-10 OSAT revenue), has ATM gross margin above its historical ceiling and real CPO and full-process traction. It ranks below TSMC because of debt-funded capex, negative free cash flow through 2027 and dependence on TSMC's outsourcing choices.
3. **Amkor and Intel (packaging), a tie I cannot separate cleanly.**
   - Amkor: profitable, prepayment-funded, US capacity, but bridge-heavy, thin margins, and no named hybrid-bonding or panel path.
   - Intel: a differentiated successor-type technology (EMIB-T) and US capacity, but no customer-confirmed volume, substrate-constrained, and inside a loss-making foundry.
   - If a tiebreak is forced, Amkor edges ahead on proven commercial evidence today, and Intel on optionality.
4. **JCET and Samsung (packaging), a tie, low confidence.** Samsung has scale and HBM but weak evidence of a packaging lead. JCET has share and growth but an export-control ceiling.
5. **SJ Semiconductor.** Insufficient financial data, and extreme concentration (largest customer >70%).

---

## (5) Background priors check

1. **"TSMC's advanced-packaging capacity has grown >80% a year since 2022; lead times 52–78 weeks." Status: CONFIRMED as company claim and analyst estimate. Growth is UPDATED to decelerate after 2027.**
   - TSMC's 2026 symposium put CoWoS plus SoIC capacity CAGR at >80% for 2022–2027 (company claim, via [fiisual, 2 Jun 2026](https://fiisual.com/blog/post/2026/2026-tsmc-technology-forum-highlights-ai-semiconductor-blueprint)).
   - ~35k wafers/month in late 2024 to ~130k projected at end-2026 (≈93%/yr, calc.) ([TechTimes, 28 Jul 2026](https://www.techtimes.com/articles/321754/20260728/ai-supply-crisis-moves-upstream-advanced-packaging-becomes-binding-constraint.htm)).
   - Goldman (analyst, 16 Oct 2026): +114% in 2027, then only +27% in 2028.
   - Lead times of 52–78 weeks come from trade estimates ([Silicon Analysts, Q1 2026](https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026)), and TSMC does not publish lead times. Silicon Analysts also notes TSMC has not said "sold out" on earnings calls. TechTimes, however, quotes Wei at the June 2026 shareholder meeting saying CoWoS is "extremely tight and sold out through 2026". The two sources conflict.
   - Equipment delivery stretched from 3–6 to 6–8 months (Oct 2026, secondary).
2. **"A larger package able to hold 12+ memory stacks is due in 2027." Status: UPDATED / not re-confirmed.**
   - The 2026 roadmap's dated anchors are 5.5 reticles (in production 2026), 14 reticles with 20 HBM (2028), more than 14 reticles with 24 HBM (2029) and SoW-X with 64 HBM (2029).
   - Wei (15 Oct 2026): "working on the 9X reticle size and moving into the 14X."
   - I found no 2026 source re-stating a 2027 date for the ~9x/12-HBM step. It is not contradicted, but the verified next anchor is 2028.
3. **"Panel-sized packaging in pilot in 2026, volume 2028–29." Status: CONFIRMED.**
   - TSMC CoPoS pilot: tools from Feb 2026, line ~Jun 2026, volume 2028–29 (secondary, Commercial Times/CNA). Some commentators say 2029–30 (low-grade source).
   - Yole: CoPoS and CoWoP expected 2028–29 (25 Sep 2026).
   - Others: Rapidus 600 mm panel prototypes (2026), JCET panel pilot lines (3Q26), Silicon Box Novara at full capacity only in 2033.
4. **"Packaging is a binding constraint 2028–2030; successor dates slip; silicon-interposer bridges last longer than roadmaps say." Status: CONFIRMED for 2026–27 (primary); PARTLY SUPPORTED for 2028–30.**
   - For 2026–27:
     - TSMC: capacity "limits my customers' growth" (Jul 2026) and demand "still far above our capability" (Oct 2026); Wei could not say whether 2027 will be tighter.
     - ASE: 2027 demand "way higher than what we'll be able to deliver".
     - Intel: substrates constrained into 1H27.
     - AT&S CEO: "It's no longer chip fabrication. It's packaging" (Nikkei via TechTimes, Jul 2026).
   - Bridges lasting longer:
     - The GF–TSMC 5-year interposer deal ramping from 1H28 implies silicon interposers through ~2032–33 (inference).
     - The CoWoS roadmap extends to 14x in 2028 and beyond in 2029, alongside CoPoS.
   - Slips: A16 moved from late 2026 to 2027.
   - Counter-signal: Goldman's +114% capacity in 2027 could loosen 2028 if demand undershoots (inference).
5. **"70% that at least one of A16-class, panel packaging, or processor-to-processor optics misses volume in 2028 (NVIDIA's 2028 generation)." Status: NOT CONTRADICTED; the weights shift.**
   - A16 already slipped to 2027, so 2028 volume remains plausible.
   - Panel volume is "2028–29", with some saying 2029–30, which makes panel the likeliest miss.
   - Optics packaging is arriving on or ahead of time: ASE CPO in mass production from 4Q26 with >US$0.5bn in 2027 (company claim); COUPE 200G in 2026 (company claim). Scale-up optics between processors at volume in 2028 was not verified.
   - Inference: ≥70% remains defensible, driven mainly by panel.

---

## (6) Open question: which successor ships first, and who captures value

### Takeaway
Order of volume arrival:
1. **Hybrid bonding** is already in volume, at TSMC SoIC 9 µm.
2. **CPO assembly** starts in low volume in 4Q26 and ramps in 2027 (ASE, TSMC COUPE).
3. **Organic-bridge alternatives to silicon interposers** (EMIB-T, fan-out bridges) arrive in 2027–28.
4. **Panel** (CoPoS, CoWoP) arrives in 2028–29.
5. **Glass** comes later: TSMC's pilot is ~mid-2027 maturity; glass-core detail is with other researchers.

Value is captured mainly by integrated giants (TSMC above all) in the front-end-like steps: hybrid bonding, interposer and panel fabrication. Specialists capture back-end, test, CPO assembly and overflow, at cyclically elevated margins.

### Cited findings
- SoIC 9 µm "already in mass production"; 6 µm in 2028; 4.5 µm in 2029 (fiisual, Jun 2026). AMD is a key SoIC customer (TrendForce, Apr 2026).
- ASE CPO mass production started 4Q26, >US$0.5bn in 2027 (company claim; 3Q26 call). TSMC COUPE 200G in 2026 (company claim).
- EMIB-T adoption "expected to scale beginning in 2026" (Intel claim); reported customer volume ~2027 (secondary). Amkor fan-out bridge from late 2027 into 2028 (company).
- CoPoS and CoWoP expected 2028–29 (Yole via Electronics Weekly, 25 Sep 2026). CoPoS pilot is in-house at TSMC (TrendForce).
- Value capture:
  - Yole: six integrated firms took ~97% of 2025 high-end performance packaging revenue, with no OSAT among them.
  - Bloomberg Intelligence: TSMC >40%; OSATs could double to 16% by 2033 (forecast).
  - TSMC advanced packaging rising to "low-teens %" of a company with a 66% gross margin.
  - ASE ATM gross margin 30.6%, "surpassed our historical structural margin ceiling".
  - Amkor gross margin 18.3%.
  - A TSMC subsidiary entering oS (ASE call).
  - Wei: "The frontend wafer business and the backend business are two different things... If they are the same, then you can expect ASE become the frontend competitor also" (Jul 2026).
- Yole: mold-interposer (CoWoS-L type) is the largest and fastest-growing 2.5D segment (28.1% CAGR 2025–31), and die-to-wafer hybrid bonding grows at ~65% CAGR.

### Inferences
- **Integrated players gain:** as interconnect moves toward hybrid bonding and panel interposers, the value-dense steps look more like wafer fabrication, which favours integrated players (TSMC, Intel, Samsung).
- **Specialists gain:** OSAT gains are concentrated in steps TSMC chooses to outsource (oS, test, CPO assembly), and in shortage-driven overflow.
- **Pause risk for specialists:** if a 2028 financing pause eases the shortage, specialists' elevated margins are the more exposed.
- **Intel EMIB-T:** the one route by which a non-TSMC player could take high-end 2.5D share before panel arrives. It is constrained by substrates rather than by technology.

### Gaps
- No third-party share data specific to 2.5D CoWoS-class units by supplier, and no figure for the share of TSMC CoWoS back-end outsourced to ASE/SPIL and Amkor.

---

## (7) What I could not verify

- **TSMC:** 2025 customer concentration (largest customer and top-5 shares) and revenue by geography; 2025 annual report and 20-F not accessed.
- **ASE:** customer concentration and geography (20-F). The 3Q26 debt and net-debt/equity figures come from a secondary summary, not the 6-K.
- **Amkor:** largest single customer share (10-K). Its CHIPS award amount was not re-verified.
- **Intel:** FY2025 adjusted free cash flow (annual report chart text garbled); Foveros Direct HVM date; any named EMIB-T customer confirmed by the customer.
- **Samsung:** packaging revenue, I-Cube/X-Cube customers, panel-level status; the 3Q26 primary release (fetch timed out); the Onyang article (403).
- **Others:** Powertech, Nepes, SFA Semicon, Hana Micron, Huatian and Tongfu 2026 results; JCET FY2025; SJ Semiconductor revenue and profit.
- **TrendForce 2025 OSAT ranking:** not found.
- **Capacity and lead times:** the share of CoWoS outsourced to OSATs; lead times beyond trade estimates; whether TSMC said "sold out" (conflicting sources).
- **TSMC Arizona packaging volume date:** 2028 (CNA via TrendForce) versus 2029 (The Register).
- **2027 9.5x/12-HBM CoWoS date:** not re-confirmed in 2026 sources.
- **Policy:** Taiwan's N-2 overseas-technology rule, Korea's national-core-technology rules and any Section 232 tariff specific to packaging were not verified. Subsidy amounts were not verified for Japan (Rapidus), China (beyond Big Fund backing of SJ Semiconductor) and India (beyond ISM approval facts). US items verified: GF's US$955m CHIPS reallocation including interposers, and the US–Japan Malta initiative (GF 6-K).
- **Membership and status:** JOINT3 membership (single blog source); Silicon Box Singapore customers and Novara construction status; Micron Sanand.
- **Europe and Israel:** "no relevant player" is based on limited searching; Amkor Portugal was not checked.
- **Local-language searches:** not performed (budget exhausted), so the Korea, Japan and China mid-tier picture is incomplete.

---

## (8) Sources (period covered / publication date)

Primary:
- TSMC 4Q25 earnings call transcript (FY2025; 15 Jan 2026): https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-01/51d09df96cd89ac19d65af39032b038dc2896a24/TSMC%204Q25%20Transcript.pdf
- TSMC 2Q26 earnings call transcript (16 Jul 2026): https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-08/3e494f0c14dd0890f897aa044415e21d93486cc4/TSMC%202Q26%20Transcript.pdf
- TSMC 3Q26 release, Form 6-K (15 Oct 2026): https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26e_withguidancexfinal.htm
- TSMC 3Q26 presentation, Form 6-K (15 Oct 2026): https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000726/a3q26presentatione.htm
- ASE 2Q26 Form 6-K with FY2025 figures (30 Jul 2026): https://www.sec.gov/Archives/edgar/data/0001122411/000095010326011353/dp250875_6k.htm
- Amkor FY2025 results 8-K (early 2026): https://www.sec.gov/Archives/edgar/data/1047127/000104712726000007/amkr123125erex-991.htm
- Amkor 3Q26 results 8-K (26 Oct 2026): https://www.sec.gov/Archives/edgar/data/0001047127/000104712726000049/amkr9302026erex-991.htm
- Intel 2025 Annual Report (FY2025; filed 2026): https://www.sec.gov/Archives/edgar/data/50863/000005086326000060/intc014890-arsa.pdf
- Intel 3Q26 earnings release 8-K (quarter to 26 Sep 2026; late Oct 2026): https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000188/q326earningsrelease.htm
- Intel 10-Q (quarter to 26 Sep 2026): https://www.sec.gov/Archives/edgar/data/0000050863/000005086326000191/intc-20260926.htm
- GlobalFoundries 3Q26 6-K (4 Nov 2026): https://www.sec.gov/Archives/edgar/data/0001709048/000170904826000259/globalfoundries3q2026earni.htm
- Rapidus RCS press release (11 Apr 2026): https://www.prnewswire.com/news-releases/rapidus-opens-analysis-center-and-rapidus-chiplet-solutions-302739433.html
- European Commission, Open EU Foundry status for Silicon Box (16 Mar 2026): https://digital-strategy.ec.europa.eu/en/news/open-eu-foundry-status-granted-innovative-chiplet-facility

Transcripts and call summaries (secondary transcription of primary events):
- TSMC 3Q26 call, Investing.com (15 Oct 2026): https://www.investing.com/news/transcripts/earnings-call-transcript-tsmc-beats-q3-2026-estimates-as-stock-slips-93CH-4950695
- ASE 3Q26 call, Investing.com (29 Oct 2026): https://www.investing.com/news/transcripts/earnings-call-transcript-ase-technology-beats-q3-2026-estimates-on-margin-surge-93CH-4982306
- ASE 3Q26 summary, BigGo (29 Oct 2026): https://finance.biggo.com/news/TW_3711.TW_2026-10-29
- Amkor 3Q26 call, Motley Fool (26 Oct 2026): https://www.fool.com/earnings/call-transcripts/2026/10/26/amkor-amkr-q3-2026-earnings-call-transcript/
- Intel 3Q26 call summary, GuruFocus/Yahoo (29 Oct 2026): https://finance.yahoo.com/markets/stocks/articles/intel-corp-intc-q3-2026-051348065.html

Trade press and analysts (secondary):
- Lapedus, "Q3 '26 Foundry/OSAT Earnings: Hit or Miss?" (early Nov 2026): https://marklapedus.substack.com/p/q3-26-foundryosat-earnings-hit-or-ded
- Lapedus/TrendForce 2024 OSAT ranking (13 May 2025): https://marklapedus.substack.com/p/ase-amkor-top-osat-rankings-but-china ; TrendForce press release: https://www.trendforce.com/presscenter/news/20250513-12577.html
- TrendForce, brokerage takeaways after TSMC 3Q26 (16 Oct 2026): https://www.trendforce.com/news/2026/10/16/news-after-tsmcs-3q26-earnings-key-brokerage-takeaways-as-2028-capex-forecasts-reach-us105b/
- TrendForce, CoPoS pilot line (13 Apr 2026): https://www.trendforce.com/news/2026/04/13/news-tsmc-advances-panel-level-packaging-copos-pilot-line-reportedly-set-for-june-completion-2028-29-ramp-eyed/
- TrendForce, CoPoS dual-track evaluation (16 Jun 2026): https://www.trendforce.com/news/2026/06/16/news-tsmc-reportedly-runs-dual-track-evaluation-on-copos-pilot-line-sparking-global-vs-local-vendor-competition/
- TrendForce, SJ Semiconductor IPO approval (27 Feb 2026): https://www.trendforce.com/news/2026/02/27/news-sj-semiconductor-reportedly-wins-ipo-nod-as-china-leans-on-advanced-packaging-for-chip-self-reliance/
- TrendForce, SJ Semiconductor IPO raise (23 Apr 2026): https://www.trendforce.com/news/2026/04/23/news-china-osat-sj-semiconductor-reportedly-raises-rmb-5b-in-ipo-largest-a-share-offering-of-2026-so-far/
- Maples Group, SJ Semiconductor STAR listing (2026): https://maples.com/knowledge/sj-semiconductors-star-market-listing-a-new-milestone-for-cayman-red-chip-companies-in-chinas-a-share-market
- SemiEngineering, TSMC Symposium 2026 by the numbers (27 Apr 2026): https://semiengineering.com/tsmc-tech-symposium-2026-by-the-numbers/
- fiisual, 2026 TSMC symposium highlights (2 Jun 2026): https://fiisual.com/blog/post/2026/2026-tsmc-technology-forum-highlights-ai-semiconductor-blueprint
- Power Electronics News, TSMC roadmap (2026): https://www.powerelectronicsnews.com/tsmc-paves-the-way-to-one-trillion-transistor-devices/
- Electronics Weekly / Yole, advanced packaging to US$51bn by 2031 (25 Sep 2026): https://www.electronicsweekly.com/news/business/advanced-packaging-to-be-a-51bn-market-by-2031-2026-09/
- Bloomberg Intelligence press release (advanced packaging to 2033): https://www.bloomberg.com/company/press/advanced-semiconductor-packaging-market-could-reach-80-billion-by-2033-as-ai-chips-spread-to-consumer-devices-according-to-bloomberg-intelligence/
- The Register, TSMC–GF interposer deal (8 Oct 2026): https://www.theregister.com/systems/2026/10/08/tsmc-taps-globalfoundries-to-bolster-us-silicon-interposer-production-in-2b-deal/5302061
- Tom's Hardware, GF interposers for CoWoS (Oct 2026): https://www.tomshardware.com/tech-industry/semiconductors/globalfoundries-to-produce-silicon-interposers-for-tsmcs-cowos-in-the-us-five-year-agreement-valued-at-usd2-billion
- DIGITIMES, TSMC–GF interposer deal (14 Oct 2026; paywalled, headline only): https://www.digitimes.com/news/a20261013PD248/tsmc-globalfoundries-packaging-capacity-silicon.html
- vlsi.kr, CoWoS price rises up to 20% (27 Oct 2026, updated 1 Nov 2026): https://www.vlsi.kr/en/cowos-price-hike-mb-en/
- TechTimes, packaging the binding constraint (28 Jul 2026): https://www.techtimes.com/articles/321754/20260728/ai-supply-crisis-moves-upstream-advanced-packaging-becomes-binding-constraint.htm
- Silicon Analysts, foundry allocation status (Q1 2026): https://siliconanalysts.com/analysis/foundry-allocation-status-q1-2026
- Clusterbid, GPU supply chain 2026 (2026): https://clusterbid.com/blog/gpu-supply-chain-2026-tsmc-cowos-nvidia-allocation-lead-times
- Tom's Hardware, EMIB gains traction / Google 9th-gen TPU (mid-2026): https://www.tomshardware.com/tech-industry/semiconductors/intels-emib-packaging-gains-traction-as-chip-designers-look-to-skirt-tsmcs-cowos-constraints-googles-reported-decision-for-9th-gen-tpus-highlights-intels-attractive-alternative
- Wccftech, MediaTek EMIB-T report and denial (2 Jun 2026): https://wccftech.com/mediatek-says-its-next-gen-program-will-only-use-intels-emib-t-for-packaging/
- Wccftech, KeyBanc on Intel contracts (2026): https://wccftech.com/keybanc-says-intel-has-won-contracts-from-broadcom-google-apple-amd-microsoft-and-nvidia-while-amazon-anthropic-and-spacexs-terafab-continue-to-evaluate-its-14a-and-18a-p-processes/
- Sammy Fans, Intel attracts MediaTek, Broadcom, Meta (1 Sep 2026; low quality): https://www.sammyfans.com/2026/09/01/intel-attracts-mediatek-broadcom-and-meta-for-ai-chip-packaging-amid-tsmc-shortage/
- Sammy Fans, Samsung Onyang HBM packaging hub (11 Nov 2026; headline only): https://www.sammyfans.com/2026/11/11/samsung-boss-vows-ai-semiconductor-pivot-with-new-hbm-advanced-packaging-hub/
- 3D InCites, Samsung X-Cube timeline (Apr 2023; dated): https://www.3dincites.com/2023/04/iftle-553-samsung-foundry-update-amkor-globalfoundries-venture/
- 3D InCites, Rapidus 600 mm RDL panels (Feb 2026): https://www.3dincites.com/2026/02/rapidus-to-produce-600mm-x-600mm-large-format-rdl-panels-at-imaps-dpc/
- DataM Intelligence blog, Japan advanced packaging / JOINT3 (2026; single source): https://www.datamintelligence.com/blogs/top-companies-in-advanced-packaging-japan
- TechPowerUp, CoPoS 310x310 mm and NVIDIA launch partner (2025): https://www.techpowerup.com/337960/tsmc-prepares-copos-next-gen-310-x-310-mm-packages
- Quartr, Tongfu 3Q25 (Oct 2025): https://quartr.com/events/tongfu-microelectronics-co-ltd-002156-q3-2025_FgfqXMee
- DIGITIMES Tongfu tag page (Sep 2026 headline): https://www.digitimes.com/tag/tfme/00112075.html
- Electronics For You, Tata Assam pilot (Oct 2026): https://www.electronicsforyou.biz/industry-buzz/tata-electronics-starts-pilot-runs-at-assam-semiconductor-plant/
- semiconductor.cv, India fabs and OSATs 2026–28 (2026): https://semiconductor.cv/blog/india-semiconductor-fabs-2026
- Evertiq, TrendForce 2024 OSAT ranking (23 May 2025): https://evertiq.com/news/2025-05-23-chinese-firms-gain-ground-in-2024-top-10-osat-ranking
- Morgan Lewis, BIS revised review policy for AI chips to China (Jan 2026): https://www.morganlewis.com/pubs/2026/01/bis-revises-export-review-policy-for-advanced-ai-chips-destined-for-china-and-macau
- Wilson Sonsini, import and export changes for advanced semiconductors (Jan 2026): https://www.wsgr.com/en/insights/a-mixed-bag-of-chips-significant-new-import-and-export-changes-for-advanced-semiconductors.html

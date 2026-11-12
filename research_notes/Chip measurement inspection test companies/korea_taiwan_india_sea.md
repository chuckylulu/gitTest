# Chip measurement, inspection and reference analysis: South Korea, Taiwan, India, Southeast Asia

**Research date: 12 November 2026.** Scope excludes electrical testers, probe cards, sockets and test handlers (covered elsewhere). KRW figures use 억원 (100 million won) as Korean filings do; NT$ figures from Taiwan exchange feeds are in NT$ thousand unless stated otherwise. Citations are reference-style links, so each `[label]` resolves to a URL with its date in §12. Labels used in the text:
- **"Company claim, unconfirmed"**: stated by the company, or by press repeating it, with no outside confirmation found.
- **"Background, not verified"**: from prior knowledge, not re-checked in this session.

Coverage is deepest for Park Systems, which rests on primary Korean filings. It is moderate for other Korean names (DART-based press plus FnGuide data) and for Taiwan (official exchange data feeds plus Chinese-language press summaries). It is thin for India and Southeast Asia (secondary press). Interim save made after an API interruption; this is the full rewrite.

## 1. Summary tables

### Takeaway
Park Systems is the only company in these regions with primary-filing evidence of a global #1 position, in AFM, with roughly 22-24% of a US$540-590M market by company-cited third-party estimates. It is a small (KRW 206bn revenue in 2025), high-gross-margin, ~93% hardware business moving from front-end AFM into advanced-packaging metrology. Its tool-of-record status at TSMC, Samsung, SK hynix, Micron and Intel is not confirmed by any chipmaker. Elsewhere:
- **Korea**: the other inspection vendors are smaller and cyclical (Nextin, Auros in losses in 2025-26).
- **Taiwan**: the analysis labs hold the outsourced slice of TEM/FIB reference data, and V5 Technologies is a reportedly TSMC-qualified AOI plus AI-classification vendor.
- **India**: no indigenous metrology or inspection supplier of global significance.
- **Southeast Asia**: ViTrox, Pentamaster and MI Technovation serve board-level and back-end inspection rather than wafer metrology.

### Cited Findings

**Table A. Suppliers by region and sub-segment**

| Region | Sub-segment | Company (listing) | Key dated evidence |
|---|---|---|---|
| Korea | AFM nano-metrology (CMP, roughness, sidewall, mask repair, packaging Cu-pad/RDL) + optical (ellipsometry, holography, WLI) | Park Systems (140860 KOSDAQ) | 2025 rev 2,056억, OPM 20.5% [PIR] |
| Korea | Optical patterned-wafer defect inspection (dark-field), IR bond-void, HBM, packaging | Nextin (348210 KOSDAQ) | 2025 OP −12억; China 85-87% of 2024 rev [A348210][NX0618] |
| Korea | Overlay and thin-film metrology | Auros Technology (322310 KOSDAQ) | 2025 rev 521억, OP −84억 [AU0211] |
| Korea | 3D SPI/AOI (boards) and 3D packaging inspection | Koh Young (098460 KOSDAQ) | Q3'26 OP 194억 (+312%) [KY1103a] |
| Korea | Package/FC-BGA substrate inspection | Intekplus (064290 KOSDAQ) | 2025 OP −37억 [A064290] |
| Korea | ABF substrate AOI and repair | Gigavis (420770 KOSDAQ) | 775억 of orders in 6 days, Oct 2026 [GV1028] |
| Korea | X-ray (HBM in-line, NDT) | SEC/쎄크 (081180 KOSDAQ) | Micron HBM tool order 58억 [SEC1110] |
| Korea | 3D inspection incl. memory modules | Pemtron (168360 KOSDAQ) | Micron Malaysia order 50억 [NVN168360] |
| Korea | Reliability/analysis services | QRT (405100 KOSDAQ) | 2025 rev 689억 [A405100] |
| Korea | Virtual-metrology software | Gauss Labs (private; SK hynix investor and customer) | Panoptes VM in SK hynix fabs since 2022 [GL-SKH] |
| Taiwan | Analysis labs (TEM/FIB material and failure analysis = reference data) | MA-tek 閎康 (3587 TPEx), iST 宜特 (3289 TPEx), MSScorps 汎銓 (6830 TWSE) | Jan-Oct 2026 rev +17.0%, −6.2%, +26.7% [TPEX-REV][TWSE-REV] |
| Taiwan | Wafer/advanced-packaging AOI + AI defect classification | V5 Technologies 倍利科 (7822 TWSE, listed 30 Mar 2026) | Reportedly TSMC-qualified; Jan-Oct rev +69.7% [V5-SD][TWSE-REV] |
| Taiwan | PCB/substrate/board AOI, AXI, panel and packaging AOI | Machvision 牧德 (3563), TRI 德律 (3030), Utechzone 由田 (3455), GPM 均豪 (5443), Favite 晶彩科 (3535) | Oct 2026 rev YoY: +96%, +72%, −18%, +126%, +73% [TWSE-REV][TPEX-REV] |
| Taiwan | Packaging process equipment with some inspection (not core metrology) | E&R 鈦昇 (8027), All Ring 萬潤 (6187), Scientech 辛耘 (3583) | Oct 2026 rev YoY +109%, +218%, +26% |
| India | Metrology start-up | Makr Microsystems (private, Bengaluru) | Rs 10.2 crore seed, Sep 2026 [MAKR] |
| India | Test/product-engineering hours | Tessolve (private) | FY26 rev ₹1,526 crore [TESS] |
| India | Assembly and test projects (ISM) | Micron Sanand, Kaynes, CG Semi, Tata Assam | Mostly running or in trial in 2026 [ISM-TV][ISM-CT] |
| SE Asia | Board-level and machine-vision inspection | ViTrox (Bursa) | 3Q26 rev RM485.1M, NP RM118.6M [VT1106] |
| SE Asia | Back-end automation/test and inspection | Pentamaster (Bursa) | 3Q26 NP RM20.4M [PM1106] |
| SE Asia | Wafer-level vision inspection/sorting + materials | MI Technovation (Bursa) | 3Q26 core NP RM69M [MI1102] |
| SE Asia | AI defect classification software | SixSense (private, Singapore) | Tong Hsing deal, Feb-Mar 2026 [SX-TH] |

**Table B. Park Systems: quality tests (a)-(e)**

| Test | Evidence |
|---|---|
| (a) Position | Direct tip-surface physical measurement. NX-Wafer does wafer inspection/analysis, automated defect review and post-CMP roughness "in front- and back-end"; NX-3DM measures sidewall/CD without cross-sectioning (company claim, unconfirmed) [PH1]. CEO: hybrid-bond Cu-pad height deformation is nm-scale, "only AFM can measure it"; AFM is slow (company claim) [DD25]. No chipmaker confirms tool-of-record status. Industrial units produced: 58 (2024), 75 (2025), 43 (H1'26); export ASP ≈ KRW 2.2bn [PH1]. |
| (b) Lead | Share of the AFM market: 21.7% in 2024 vs Bruker 15.8% and Oxford 14.3% (MarketsandMarkets-based, cited by the company) [PDK]. 23.8% of 2025 AFM revenue and 340 systems, #1 by units (QY Research, via company release) [MH1104]. "8 of top-10 chipmakers" are customers (company claim, unconfirmed) [FN0601]. Intel "a main customer"; mass-production supply of NX-TSH under discussion with the largest foundry (company statements) [ZD0529]. Third imec JDP, Apr 2026 [PH1]. |
| (c) Revenue model | 2025: industrial 71%, research 22%, service 7% [PVU]; H1'26: 65/28/7 [PDK]. No software or subscription line. Parent-only consumables plus service is 2.0% of 2025 revenue [PH1]. Probe maker acquired Apr 2026. |
| (d) Financials | 2025: revenue 2,056억 (+17.5%), GPM 66.4%, OP 422억 (20.5%), NI 345억. H1'26: revenue 924억 (−10%), GPM 68.6%, OP 63억 (6.8%) [PIR][PDK]. Net cash ≈ 438억 at 30 Jun 2026 [PH1]. ROE 16.7% (2025) [A140860]. FCF (parent) 96억 in 2025 vs 268억 in 2024 [PDK]. Top customer 8% of H1'26 revenue [PH1]. Exports 92% [PH1]. Greater China ≈ 41% of 2025 revenue (broker) [SH0728]. |
| (e) Resilience | Orders in Q2'26 were a record 784억; backlog 1,125억 at 30 Jun 2026 vs 693억 a year earlier [PDK]. Utilisation 96-98% [PH1]. Industrial AFM technology is Korean National Core Technology no. 2010-11 [PH1]. KRW strength is a stated H2'26 headwind [MZ0915]. |

**Table C. Park Systems: six transitions (SAID vs DONE)**

| Transition | Said | Done |
|---|---|---|
| 1 Imaging → inference with uncertainty | Nothing found | Hybrid WLI pairs fast optics with AFM [PH1]; no uncertainty-reporting product |
| 2 AI-built recipes | FX40 uses "AI and robotics" to auto-recognise and mount probes and automate set-up [PH1] | Research tools only; no industrial AI-recipe product found |
| 3 Bonded stacks / packaging | Expects 2.5D mass-production orders in 2026 [ZD0529]; roadmap names hybrid bonding [PVU] | Hybrid WLI orders and shipments; NX-TSH300 Overlay (RDL) developed; Cu-pad metrology in R&D plan; imec JDP on wafer bonding and CMP [PH1]; Lyncée DHM aimed at packaging [PLY] |
| 4 Hardware → software/data | Nothing found | Service ~7%; probe consumables via Rocky Mountain Nanotechnology (Apr 2026) [FN0506] |
| 5 On-premises AI | Nothing found | Nothing found |
| 6 Fewer tools per wafer after 2030 | Nothing found | Nothing found |

**Table D. Park Systems: entry-point data (checked 12 Nov 2026)**

| Item | Value |
|---|---|
| Price / market cap | ~KRW 210,000 (prior close; intraday 206,000-218,000) / KRW 1.4705tn [NV140860] |
| 52-week range | 182,400-351,500 [NV140860] |
| PER trailing / forward | 63.35x (TTM EPS 3,315) / 31.53x (2026E EPS 6,661) [NV140860] |
| PBR / dividend yield | 4.29x / 0.24% [NV140860] |
| Own history | Year-end PER 49.2x (2023), 34.5x (2024), 42.4x (2025) [A140860]; company's 2023-25 average PER 41.8x, PBR 7.5x [PVU] |
| Consensus | 2026E revenue 2,463억, OP 503억; Q3'26E revenue 680억, OP 181억 [A140860][Q140860] |
| Latest guidance | Qualitative: full year "can meet broker expectations" (CEO, 29 May 2026) [FN0601] |
| Next event | Q3 2026 quarterly report; not published as of 12 Nov 2026 (due ~14 Nov) |

### Inferences
- Park's share figures all come from research the company commissions or cites. Treat "#1 in AFM" as likely but company-sourced.
- No company in these regions shows evidence of owning a wafer-release "judge" at a leading chipmaker. Park comes closest in a physical-constraint niche (nm-scale topography that optics cannot resolve).

### Gaps
- No independent AFM share data; no share for automated in-line AFM versus Bruker's industrial AFM line.

## 2. Park Systems: quality tests (a)-(e), detail

### Takeaway
Park's strengths on the record: 64-68% gross margins, ~20% operating margins in 2021-25, low customer concentration, net cash and a rising backlog. Its weaknesses: ~93% one-off hardware, heavy Greater-China exposure, slow FCF conversion in 2025, an H1 2026 earnings collapse, and leading-customer wins that rest on company statements.

### Cited Findings
**(a) Position**
- Product set [PH1]:
  - NX-Wafer: inspection, automated defect review, post-CMP roughness.
  - NX-3DM: sidewall, overhang, CD.
  - NX-Hybrid WLI: AFM + white-light interferometry for QA/process control incl. advanced packaging; "orders and shipments under way".
  - NX-Mask: photomask particle removal/repair, delivered to chipmakers and mask makers.
  - NX-TSH: large and heavy samples; displays, now packaging.
  - NX-HDM/PTR: hard disks.
  - Optical: Accurion ellipsometers; Lyncée holographic microscopes.
- Filing claims 0.01 nm vertical resolution and no sample preparation, and says SEM cannot accurately measure FinFET/GAA 3D shapes, so AFM is "becoming essential" (company claim, unconfirmed) [PH1].
- SK Securities: with D2W hybrid bonding, Cu-dishing tolerance moves from sub-µm to nm; AFM demand is "structural, not cyclical" (broker view) [SK0930].

**(b) Lead**
- IR deck chart sourced to "QYResearch, 2026" shows segment values 31.2%, 23.4%, 17.6%, 11.3%, 7.2%, 5.1% and 4.3% for Park, Bruker, Oxford, Horiba, NT-MDT, Nanosurf and others [PDK]. My most plausible reading: others 31.2%, Park 23.4%, Bruker 17.6%, Oxford 11.3%. The press-release figure is 23.8% [MH1104].
- QY Research: AFM market US$586.9M in 2025, US$1.01bn by 2032 (11.23% CAGR); industrial AFM 15.72% CAGR [MH1104].
- MarketsandMarkets (in filing): AFM market US$541.8M (2025) → US$762.2M (2030); industrial US$241.8M → US$347.7M (7.5% CAGR); research US$299.9M → US$414.5M [PH1].
- Unsourced "20.6%" figure repeated by press [FN0816].
- Park became #1 in 2022 (company claim) [DD25]. CEO: the gap with #2 Bruker widens every year, and "Chinese firms cannot catch up" (company claim, unconfirmed) [MH0602].
- Customer evidence:
  - "Trades with 8 of the top 10 semiconductor companies" (company claim, unnamed) [FN0601].
  - Intel "one of Park's main customers" in advanced packaging (EMIB) (company statement via ZDNet; not confirmed by Intel) [ZD0529].
  - Executive VP Lee Dong-chun: new packaging metrology is "below 2 µm, beyond existing optical tools" (company claim) [ZD0529].
  - A Taiwanese "T company" ordered multiple AFMs for 2.5D/AI-HPC analysis (company claim) [DD25].
- Broker channel checks (estimates, not confirmations) [MZ0915]:
  - H1'26 orders were led by mainland China and Taiwan; H2 orders come from the US, Korea and Japan.
  - Hybrid WLI sales to a North American customer and TSH sales to a foundry's packaging lines are expected from H2'26 into 2027.
- SK Securities: order growth centred on Greater China, with high-value new tools entering the backlog; US orders for new tools expected in H2 [SK0930].
- Third imec JDP (April 2026) covers advanced packaging, wafer bonding and related CMP; Park joined imec's 3D Systems Integration IIAP (company disclosure) [PH1][PDK].

**(c) Revenue model**
- Orders by year (industrial/research/service, 억원) [PDK]:
  - 2021: 920 (622/262/36)
  - 2022: 1,472 (870/554/48)
  - 2023: 1,531 (1,067/380/84)
  - 2024: 1,844 (1,277/448/119)
  - 2025: 2,080 (1,491/462/~127, service implied)
- Backlog at end-2025 was 636억 (industrial 78%) [PVU].
- Service covers installation, maintenance, upgrades and application support [PVU]. Parent-only consumables and service: 34억 in 2025, 18억 in H1'26 [PH1].
- Production is hand assembly by skilled staff (38 people in H1'26) [PH1][DS0602].

**(d) Financial strength (K-IFRS consolidated, 억원)**
- Revenue / gross profit / OP by year [PDK][PIR]:
  - 2021: 853 / 552 / 176
  - 2022: 1,245 / 815 / 326
  - 2023: 1,448 / 924 / 276
  - 2024: 1,751 / 1,142 / 385
  - 2025: 2,056 / 1,365 / 422
- Net income: 428 (2024), 345 (2025).
- Quarterly revenue / OP: Q2'25 523/120; Q3'25 456/86; Q4'25 568/84; Q1'26 394/21; Q2'26 530/42 [PDK]. H1'26 SG&A rose 29% (R&D, labour, sales commissions) [PDK]; press also cites HQ-move costs and incentives [SK0930].
- R&D: 197억 = 9.5% of 2025 revenue (consolidated chart); parent R&D 141억 = 18.5% of H1'26 parent revenue; 130 R&D staff [PDK][PH1].
- Balance sheet at 30 Jun 2026: equity 3,403억, debt ratio 39.3% (55.4% at end-2025). Deposits 1,265억 vs borrowings 827억, i.e. net cash ≈ 438억 (≈13억 at end-2025) [PH1].
- KRW 100bn perpetual bond with warrants (hybrid equity), issued 8 Jun 2026: 30 years, 0% coupon, no investor put; buyers Kiwoom Securities and NV Mezzanine Growth Equity PEF [PH1]. Use of funds: 200억 R&D, 400억 M&A, 400억 capacity [DS0602]. Warrant exercise price: could not verify.
- FCF (parent): 2022 170억, 2023 171억, 2024 268억, 2025 96억. DPS 500 KRW [PDK]. KIS commercial credit rating BBB- (20 Apr 2026) [PH1].
- Concentration: top two customers were 8% and 3% of H1'26 revenue (13% and 11% in H1'25), unnamed [PH1].
- Geography: exports 92% (H1'26) [PH1]. Greater China 41% of 2025 revenue (SK Securities; the source may mean China + Taiwan) [SH0728]. The Beijing office books no sales [PH1].
- Ownership: CEO Park Sang-il 32.3% (2,258,871 of 7,002,469 shares); National Pension Service 2.9% [PH1]. Foreign holding 37.86% on 12 Nov 2026 [NV140860].
- Capacity utilisation, industrial / research: 2024 90.6% / 91.3%; 2025 96.2% / 97.4%; H1'26 97.7% / 99.0% [PH1].
- Idle space supports ~KRW 300bn of revenue, enough to 2027 (broker) [MZ0915]. New Gwacheon HQ (27,000 m²) completed April 2026 [FN0601].

**(e) Resilience**
- Quarterly orders: 323 → 409 → 558 → 629 → 784억 (Q2'25-Q2'26).
- Backlog over the same quarters: 693 → 645 → 636 → 871 → 1,125억. It was 1,023억 on 14 Aug 2026 at the then-current FX rate [PDK][PH1].

### Inferences
- **ROIC (my estimate, 2025): about 16%.** NOPAT ≈ 422억 × (1 − 16.4% tax) ≈ 353억, over invested capital ≈ equity 2,251 + debt 752 − cash 766 ≈ 2,238억. Goodwill and the new HQ are included.
- **Weak 2025 FCF:** FCF (96억) was well below OP, likely because of HQ construction; non-current assets rose from 832억 to 1,533억 in 2025. FCF is parent-basis and OP consolidated, so the comparison is approximate.
- **Industrial AFM share (rough):** consolidated industrial revenue ≈ 71% × 2,056억 ≈ KRW 146bn, ≈ US$100M at an assumed KRW 1,400-1,450/US$ (rate not sourced). That implies roughly 40% of MarketsandMarkets' 2025 industrial AFM segment. Definitions differ, so treat this as an order of magnitude.
- **Consensus dependency:** the 2026 consensus OP of 503억 needs H2 OP of ~440억 against 63억 in H1, so backlog conversion is the swing factor.
- **Scenarios to 2030:**
  - Steady growth: the backlog and capacity support brokers' ~+20-22% for 2027.
  - Financing-led pause around 2028: the ~70% industrial hardware share is exposed; research AFM (22-28%) gives only partial ballast; service is too small to cushion.
  - Faster acceleration: utilisation near 97% is the constraint, and the 400억 capex is the response.
  - Cycle position: early upswing in orders, but revenue lagged in H1 2026.

### Gaps
- Mainland-China-only revenue share.
- Whether US or Korean export rules restrict AFM sales to Chinese fabs.
- Named tool-of-record confirmations.

## 3. Park Systems: path through the six transitions, detail

### Takeaway
Park's concrete actions cluster on transition 3 (packaging) and on adding optical techniques by acquisition. It has done nothing visible on uncertainty-quantified inference, data or software revenue, on-premises AI, or a post-2030 fall in tools per wafer.

### Cited Findings
- **SAID:**
  - The company aims to become a "comprehensive metrology solutions company" [PH1].
  - Roadmap: "FX Project — the next standard in in-line AFM (higher throughput and detectability)", an "Interferom Project (Hybrid WLI platform)", and hybrid bonding [PVU].
  - Industrial tools will migrate from the NX to the FX line [ET0712].
- **DONE, products:**
  - NX-TSH300 Overlay for RDL developed.
  - NX-Wafer Plus (bevel) commercialised.
  - FX300 sliding stage for Cu-pad flatness.
  - "Cu pad inspection/metrology" and next-generation packaging metrology are in the R&D plan [PH1].
  - Research tools: NX1 launched 30 Apr 2026 [PDK]; FX40 IR launched 2 Jun 2026 [NVN140860].
- **DONE, M&A:**
  - Accurion: 100% acquired 4 Oct 2022 [PH1].
  - Lyncée Tec: announced 6 Jan 2025, with a plan for a fully automated DHM for advanced packaging [PLY]. The H1 report dates the deal March 2025 and the value-up plan says 2024 (inconsistent).
  - Rocky Mountain Nanotechnology (solid Pt/Pt-Ir probes; ~10 nm tips): acquired April 2026 for in-house parts and next-generation nanoprobing [FN0506][PH1].
  - CEO: 5 targets under review (Korea, US, Germany, France), ~2 to be disclosed in 2026, metrology tools or components only (company statement) [FN0601].

### Inferences
- **T1:** Park sells the direct measurement, not the inference. Its best defence is to become the non-destructive reference that calibrates fast optical tools, which Hybrid WLI points toward.
- **T4/T5:** Park has no data business, so it captures nothing if reference data stays with chipmakers.
- **T6:** a fall in tools per wafer would hit unit sales unless AFM's reference role proves the hardest measurement to replace by inference.

### Gaps
- Industrial AI or recipe automation.
- Data products.
- Status of the "two more acquisitions in 2026".

## 4. Park Systems: entry-point data, detail (separate from quality)

### Takeaway
On 12 Nov 2026 the shares were ~40% below their 52-week high at 31.5x consensus 2026 EPS, below the company's own 2023-25 average PER of 41.8x. Trailing PER was 63x because H1 2026 earnings fell 75%. The Q3 2026 report (due ~14 Nov) is the next catalyst.

### Cited Findings
- **SK Securities (30 Sep 2026)** [SK0930]:
  - Target raised from 350,000 to 390,000.
  - Q3'26E revenue 700억 / OP 190억; Q4'26E 850억 / 250억.
  - 2026E 2,480억 / 500억; 2027E 3,020억 / 780억 (OPM 26).
  - Valuation basis: 2027E EPS 9,522 × 41x.
  - The stock sat near the bottom of its 5-year 12-month-forward PER band.
- **Meritz (15 Sep 2026):** target cut from 350,000 to 330,000; Q3'26E 678억/185억; 2026E 2,471억/527억; 2027E 3,035억/684억 [MZ0915].
- **DB Securities:** 2026E 2,501억 / 581억 [FN0601].
- On 4 Nov 2026 press still cited SK's Q3 forecast, i.e. results had not yet been released [MH1104].
- KOSPI fell 6% intraday on 19 Aug 2026 (headline) [NVN140860]; market-wide volatility is relevant to timing.

### Inferences
- EV ≈ KRW 1.43tn (market cap less ~438억 net cash, treating the perpetual as equity). That is ~5.8x 2026E sales and ~7.3x TTM sales (1,948억 to June 2026). My calculation.
- Near-term events: Q3 report (~14 Nov 2026); M&A disclosures; FY2026 results (Feb 2027).

### Gaps
- Full 5-year valuation band data.
- Warrant dilution terms.

## 5. Korea: other inspection and metrology suppliers

### Takeaway
The other Korean inspection vendors split sharply in 2025-26. Nextin and Auros lost money as Chinese localisation orders faded. Packaging and substrate inspection (Koh Young, Gigavis, Intekplus, SEC) rebounded on AI-server, ABF-substrate and HBM demand. None has confirmed tool-of-record status for critical-layer metrology at Samsung or SK hynix. The nearest evidence is Nextin's repeat SK hynix wafer-inspection contracts and Gauss Labs' SK hynix-deployed virtual metrology.

### Cited Findings
- **Nextin (348210)**
  - Revenue / OP: 2023 879/362억 (41% OPM); 2024 1,137/470억; 2025 669/−12억; Q2'26 208/−8; 2026E 712/3 [A348210][Q348210].
  - H1'26 [NX1018]:
    - Revenue 288억 (−28.5%), operating loss 63억.
    - Products 188억 (−41%); services 98억 (+18%, 34% of sales); GPM ~48%.
    - HBM tool KROKY 59억 vs 200억.
    - China ~64억 vs 115억.
    - R&D 21.7% of sales; H1 orders 210억; backlog 90억.
    - ASPER shipped to its Wuxi entity Sep 2026; certification of the Wuxi plant pending.
  - SK hynix contracts: 107억 (Mar 2026) [NX0326] and 254.4억 (6 Oct 2026, to 25 Nov 2027, 38% of 2025 revenue; the company links it to the Yongin Y1 fab) [NX1014]. Shinhan (25 Aug 2026): China orders delayed, target cut (headline) [NX0825].
  - China was 85-87% of 2024 revenue. KROKY was "adopted by an HBM maker" (company claim). Nextin US is in San Jose; X-ray JV Nexray with Axiomatique [NX0618].
  - IRIS-III (IR detection of non-metal voids in W2W/C2W bonding) launched Feb 2026 [NX0210]. ASPER (warpage-tolerant packaging inspection; 50 nm defects claimed; AI algorithm) launched Dec 2025 [NX1217].
  - Price 25,800; market cap 2,703억; PBR 1.78x; 52-week range 20,050-110,000; consensus PER 172x [P348210].
- **Auros Technology (322310)**
  - 2024 revenue 614억 / OP 61억; 2025 521억 (−15.1%) / −84억 / NI −64억 [AU0211].
  - Q1'26 68/−68억; Q2'26 114/−23억; debt ratio 105% at Q2'26 [Q322310].
  - Price 9,640; market cap 903억; PBR 1.60x; 52-week range 7,250-52,000. Naver shows TTM EPS −862 "as of 2026.09", which implies Q3'26 has been filed (implied Q3 EPS ≈ +25 KRW, my arithmetic) [P322310]. A web search found no Q3 release [ES322310].
  - KRW 1bn treasury-share trust (10 Nov 2026) [AU1110].
  - Overlay and IR-overlay products and customers: background, not verified.
- **Koh Young (098460)**
  - 2025 revenue 2,326억, OP 173억 (7.5%); Q2'26 888/146억 (record); 2026E 3,674/609억 [A098460][Q098460].
  - Q3'26: OP 194억 (+312%) and first quarterly revenue above 1,000억 (headlines, 3 Nov 2026) [KY1103a][KY1103b].
  - Orders and investment: new order in China's AI-server chain [KY1021]; SOCAMM2 inspection order from a domestic memory maker [KY0930]; 294억 capex [KY0806].
  - Korea Investment & Securities target 44,000 KRW [KY1012].
  - Price 24,200; market cap KRW 1.65tn; PER 34.8x trailing / 34.6x forward [P098460].
  - Share of revenue from semiconductors vs boards: could not verify.
- **Intekplus (064290)**
  - 2025 revenue 898억, OP −37억; Q2'26 90/−51억; 2026E 1,071/83억; debt ratio 183% [A064290][Q064290].
  - Contracts: 140억 [IK0626]; 218억 [IK0702a]; 85억 with a Taiwanese firm [IK0702b]; 61억 [IK0909].
  - Price 47,600 (52-week low 10,960); market cap 6,195억; PBR 14x [P064290].
- **Gigavis (420770)**
  - Revenue / OP: 2023 914/350억; 2024 261/−18; 2025 524/121; 2026E 973/314 [A420770].
  - 775억 of orders in six days incl. 306억 to a Chinese substrate maker [GV1028].
  - Market cap 9,469억; forward PER 33x [P420770].
- **SEC (081180)**
  - 58억 HBM inspection order from Micron (9.8% of 2025 revenue) [SEC1110]; first advanced mass-production-line order [SEC1019].
  - 2025 revenue 592억, OP −31억; market cap 411억 [A081180].
- **Pemtron (168360):** 50억 Micron Malaysia order (23 Jun 2026 headline) [NVN168360]; Q1'26 revenue +53% on AI data-centre demand [PT0518]; 2025 OP 32억 [A168360].
- **QRT (405100):** 2025 revenue 689억, OP 48억; 2026E 850/122억 [A405100].
- **Gauss Labs (private)**
  - Panoptes VM in SK hynix mass production. Two joint papers at SPIE Advanced Lithography + Patterning 2026 (tool-to-tool matching; "GRACE" explainable overlay VM) use data from SK hynix fabs [GL-SKH].
  - Earlier deployments: thin film (Dec 2022) and etch (Aug 2024); SK hynix reported ~29% lower process variability when VM was combined with APC (from search-result summaries of SK hynix/Asia Economy coverage, not opened) [GL-AE].
  - Funding: seed, US$55M total, SK hynix investor (CB Insights) [GL-CBI]. No 2026 round or non-SK customers found.

### Inferences
- Nextin's China share fell from ~85% of revenue (2024) to ~22% in H1'26 (64/288억, my arithmetic). Its 40% margins depended on Chinese localisation demand that is now fading or being localised.
- Gauss Labs is the regional example of transition 5: virtual-metrology AI developed on, and kept with, the chipmaker's own data. The chipmaker is also the investor.

### Gaps
- Not researched in this session: SEMES metrology tools, ATI, NanoScope Systems, Oros.
- Auros IR overlay status.
- Mainland-China share for Koh Young and Intekplus.

## 6. Taiwan: equipment makers, analysis laboratories, TSMC in-house evidence

### Takeaway
Taiwan's growth vehicles in this field in 2026 are:
- **V5 Technologies (倍利科):** high-magnification AOI plus a multi-vendor AI defect-classification layer, reportedly qualified at TSMC.
- **Analysis labs (MA-tek, MSScorps, iST):** they sell TEM/FIB material and failure analysis, the outsourced share of reference data, driven by 2 nm GAA, chiplets and silicon photonics.

Board and substrate AOI makers (Machvision, TRI, GPM) are booming on AI servers, but are not wafer metrology. Cheng Mei Instrument, named in the brief, did not appear in TWSE/TPEx listed monthly-revenue data. TSMC builds its defect-inspection AI on NVIDIA tools in-house.

### Cited Findings
- **Monthly revenue, October 2026** (NT$ thousand; month YoY; Jan-Oct and YoY) [TWSE-REV][TPEX-REV]:
  - MA-tek 338,226 (+10.2%); 3,383,431 (+17.0%)
  - iST 360,503 (−8.4%); 3,757,748 (−6.2%)
  - MSScorps 254,801 (+48.5%); 2,228,073 (+26.7%)
  - V5 Technologies 316,939 (+32.6%); 2,622,995 (+69.7%)
  - Machvision 403,332 (+95.6%); 3,408,003 (+24.6%)
  - TRI 926,468 (+71.9%); 9,213,217 (+33.0%)
  - Utechzone 151,483 (−18.0%); 1,221,908 (−14.5%)
  - GPM 716,168 (+126.0%); 5,007,838 (+33.7%)
  - Favite 74,553 (+72.8%); 830,399 (+222.6%)
  - E&R 257,512 (+109.2%); 1,832,617 (+51.3%)
  - All Ring 978,004 (+217.7%); 8,067,739 (+68.6%)
  - Scientech 1,101,175 (+25.5%); 10,298,835 (+9.2%)
- **Prices and valuation** (close; P/E; P/B; yield). TWSE names are as of 11 Nov 2026 and TPEx names as of 12 Nov 2026 [TWSE-PX][TWSE-PE][TPEX-PX][TPEX-PE]:
  - MA-tek NT$188.0; 22.8x; 2.15x; 2.24%
  - iST NT$115.0; 25.2x; 2.10x; 3.88%
  - MSScorps NT$470; 1,880x (near-zero TTM EPS); 7.53x
  - V5 NT$644; 31.2x; 4.65x
  - Machvision NT$623; 33.4x; 6.85x
  - TRI NT$233.5; 16.9x; 5.19x
  - Utechzone NT$184; 78.6x
  - GPM NT$86.2; 27.5x; P/B 0.78x (as published; looks anomalous)
  - Favite NT$75.2; 33.9x
  - E&R NT$143.5; 478x
  - All Ring NT$950; 40.6x
  - Scientech NT$505; 31.0x
- **V5 Technologies (倍利科)**, all from Chinese-press search summaries; underlying articles not opened [V5-SD][V5-CT][V5-UDN][V5-BN]:
  - Products: AOI and metrology for wafer and advanced-packaging steps (plating, RDL, coating, bonding). V5300 PRO AOI at 100-150x vs 1-10x for conventional AOI, measuring micro-bumps, RDL and CD.
  - Software: the V5 ADC AI platform integrates 12 AOI brands, at >10 chipmaker customers and on >800 tools (company claim).
  - TSMC: reportedly "passed TSMC and other major customers' qualification, gradually replacing incumbent suppliers" (media; not confirmed by TSMC). Chairman 林坤禧 is reported to be an ex-TSMC senior VP.
  - 2025: revenue NT$2.075bn (+188%), net income NT$580M, EPS 14.04.
  - Pipeline: CoPoS and CPO inspection tools in customer qualification, due to finish Q4 2026, volume 2027 at the earliest.
  - IPO at NT$780 on 30 Mar 2026; first-day close NT$1,695.
- **Analysis labs**
  - All three set 2025 revenue records. 2 nm GAA and chiplets push foundries and designers toward outside MA/FA labs; ASIC programmes refresh every 1-2 years (analyst view) [TN0119].
  - MA-tek: TEM/FIB for CSP AI-chip verification; labs in Nagoya, Hokkaido and Kumamoto (1st and 2nd) [TN0119]. Q2'26 gross margin 33.85% (seven-quarter high); a one-off tax charge of NT$233M cut Q2 EPS to 0.80 (third-party analysis) [UA-LAB].
  - iST: 2 nm ALD new-material verification and silicon-photonics/CPO verification platforms; heavy upfront capex, revenue contribution from 2026 [TN0119].
  - MSScorps: silicon-photonics test and optical-loss localisation (patents in Taiwan and Japan). The chairman expects 2026 revenue, gross margin and profit above 2025 (company claim) [TN0119].
- **TSMC in-house:** TSMC uses NVIDIA Metropolis/TAO for vision-AI defect inspection, plus AI in computational lithography and process control, and "FabTwin" on Omniverse. Date June 2026 per search summary [NV-TSMC]. No source found on whether TSMC metrology data may leave its fabs.
- **Business lines below are background, not verified:**
  - Machvision, TRI, Utechzone, Favite: PCB/substrate/board/panel AOI (TRI also sells electrical ICT).
  - GPM: automation and AOI in TSMC's CoWoS supply chain.
  - E&R: laser/plasma packaging equipment.
  - Scientech: wet process and bonding.
  - Which of these inspect at wafer or advanced-packaging level at TSMC or ASE: could not verify.

### Inferences
- MA-tek and MSScorps growth (+17% and +27% YTD) is evidence that more reference analysis is being outsourced as 2 nm/GAA arrives. They sell hours on TEM/FIB tools and staff time: the labour-based model the thesis rates as weaker, but holding the reference data.
- V5's multi-vendor ADC layer, if confirmed, is the clearest regional example of software and data sitting above other vendors' hardware (transition 4), run on the chipmaker's premises (transition 5).

### Gaps
- Cheng Mei Instrument (政美應用) listing and financials.
- 2025 full-year margins for the labs.
- TSMC/ASE customer confirmation for any Taiwanese inspection vendor.
- TSMC data-residency policy.

## 7. India

### Takeaway
Nothing of global significance exists in Indian measurement or inspection tools. The only indigenous metrology effort found is Makr Microsystems, a seed-stage start-up. India's role is engineering-services hours (Tessolve) and newly running assembly-and-test plants that will buy foreign inspection tools.

### Cited Findings
- **Makr Microsystems (Bengaluru):** Rs 10.2 crore seed led by Bluehill VC with Artha Venture Fund (early Sep 2026). It works on "nanoscale 3D subsurface metrology" for hidden structures and defects; the team has AFM and MEMS backgrounds. No products or customers disclosed [MAKR][MAKR2].
- **Applied Instruments venture:** described as "India's first Make in India semiconductor equipment company" with defect-inspection offerings, formed with Singapore-based Applied Instruments. Indigenous content unverified [TV-AI].
- **Tessolve (private):** FY26 revenue ₹1,526 crore (FY25 ₹1,157 crore); target ₹2,000 crore for FY27; ≥25% of revenue from AI/data-centre work; no IPO planned (single outlet) [TESS].
- **India Semiconductor Mission:**
  - Phase 2 ("Semicon 2.0") approved by Cabinet in July 2026 at ~Rs 1.25-1.28 lakh crore; figures vary by source [ISM-EMS][ISM-TV].
  - Micron Sanand: assembly-and-test in commercial production from ~Feb 2026 (one source).
  - Kaynes Semicon Sanand OSAT: inaugurated 31 Mar 2026.
  - CG Semi: commercial production reported 4 Jul 2026, though other sources differ.
  - Tata Assam: in trial production, with output targeted by 31 Mar 2027.
  - All are assembly, test and packaging, not fabs; the sources are secondary and inconsistent [ISM-TV][ISM-CT].
- **Park Systems** has run an Indian sales subsidiary since Sep 2021 [PH1].

### Inferences
- India is a customer market for imported inspection and test tools and a supplier of engineering hours. Both sit at the weak end of the thesis.

### Gaps
- Not researched: KLA, Applied Materials, Lam and Advantest India R&D centres; Tata Elxsi, L&T Technology Services, MosChip and Soliton test-related revenue.

## 8. Southeast Asia

### Takeaway
Malaysia's listed inspection names are in a strong AI-driven upswing, but they serve board-level, machine-vision and back-end markets rather than wafer metrology. Singapore's SixSense is a small AI-classification software vendor whose pitch assumes fab data stays with the chipmaker.

### Cited Findings
- **ViTrox**
  - 3Q26 revenue RM485.1M (RM228.6M a year earlier); net profit RM118.58M (RM34.72M); best quarter since its 2005 listing [VT1106][VT1105].
  - Growth came from Automated Board Inspection and Machine Vision System on AI-infrastructure and networking demand, helped by tax incentives [VT1106].
  - 9M26 net profit RM254.8M (RM87.0M). Q3 revenue beat the RM360-402M guidance cited by BIMB [VT-EDGE].
  - Share price RM10.60 (5 Nov 2026); market cap ~RM20bn (search summary) [VT-EDGE].
- **Pentamaster:** 3Q26 net profit RM20.44M (RM17.07M); revenue RM224.05M per The Star vs RM130.24M per The Edge (conflict); order book RM500M; double-digit FY2026 revenue growth expected [PM1106].
- **MI Technovation:** 3Q26 core net profit RM69M (+114% YoY); 9M RM151M (Apex Research); materials unit Mi Material Holding listed on SGX on 28 Oct 2026 [MI1102].
- **SixSense (private)**
  - Collaboration with Tong Hsing Electronic on AI defect classification, announced Feb-Mar 2026 [SX-TH].
  - Company claims: >100M chips analysed; engineers fine-tune models on their own fab data and deploy in under two days; 2026 roadmap toward real-time in-machine classification (company claims) [SX-TH][SX-SGI].

### Inferences
- ViTrox's quarterly net margin rose from ~15% to ~24% (my arithmetic). Annualised 9M earnings (~RM340M) put it at roughly 59x a RM20bn market cap (rough, my arithmetic).
- None of these companies has evidence of front-end wafer metrology or tool-of-record status.

### Gaps
- ViTrox's semiconductor (vs board) mix and China share.
- MI Technovation product detail.
- SixSense funding after 2025.

## 9. Investor access

### Takeaway
Korean KOSDAQ names are directly accessible; Park Systems has 37.86% foreign holding. Korea has eased registration and omnibus rules, but MSCI did not watch-list it for developed-market status in June 2026. Taiwanese, Indian and Malaysian access runs through local registration regimes. None of the companies covered here has a depositary receipt, as far as I could find (not verified).

### Cited Findings
- **Korea, rules:** the government says it abolished foreign investor registration, moved to LEIs, broadened omnibus accounts, expanded English disclosure and resumed short selling [KR-MSCI]. It also issued an integrated-account guideline [KR-OMNI] and published an FX roadmap including 24-hour FX trading from July 2026 [KR-ROAD].
- **Korea, MSCI:** the 23 Jun 2026 review left Korea off the developed-market watch list, citing offshore won convertibility, omnibus use and pre-funding of settlement [KR-MSCI].
- **Korea, holdings:** foreign ownership on 12 Nov 2026 was Park 37.86%, Koh Young 31.92%, Nextin 15.28%, Auros 7.11% [P140860][P098460][P348210][P322310]. Nextin is in the KOSDAQ Global Segment [NX0618].
- **Taiwan, India, Malaysia (background, not verified):**
  - Taiwan: foreign investors register as FINI through a local agent/custodian.
  - India: Foreign Portfolio Investor registration with SEBI; the relevant Indian firms (Tessolve, Makr) are private anyway.
  - Bursa Malaysia: open to foreign investors through brokers and custodians.
  - Single-country ETFs (Korea, Taiwan, Malaysia, India) are large-cap weighted. Whether Park Systems or the Taiwanese small caps are held: could not verify.

### Gaps
- Exact current FINI and FPI procedures.
- ETF constituent lists.
- KOSDAQ foreign-ownership limits for designated National Core Technology companies (none found).

## 10. Does any company from these regions belong among the 8-15 most important globally?

### Takeaway
On the evidence collected, probably not on scale or confirmed tool-of-record status. The strongest case is Park Systems as the niche leader in a physical-constraint measurement (nm-scale topography, including hybrid-bond Cu pads) relevant to stacked chips. A secondary case is Taiwan's analysis labs as holders of outsourced reference data. This is evidence for the writer to judge, not a ranking.

### Cited Findings
- **Park Systems:** #1 in AFM with ~22-24% share (company-cited) [PDK][MH1104]. Its 2025 revenue of KRW 205.6bn [PIR] is small next to KLA's ~US$13bn as cited by Park's CEO [FN0601 (via fnnews 1 Jun 2026)]. No chipmaker confirms it as tool of record.
- **V5 Technologies:** reportedly TSMC-qualified; 2025 revenue NT$2.1bn [V5-SD].
- **Analysis labs:** MA-tek + iST + MSScorps Jan-Oct 2026 revenue ≈ NT$9.4bn combined (my sum) [TPEX-REV][TWSE-REV].

### Inferences
- If the global list values "owning a physical constraint plus reference role" over scale, Park is a candidate for the tail of a 15-company list. Otherwise these regions contribute niche suppliers and labour-based reference labs, not global judges.

### Gaps
- Independent share and qualification data that would settle Park's status.

## 11. What I could not verify
- Park Systems: Q3 2026 results (not out on 12 Nov 2026); independent AFM and in-line AFM shares versus Bruker; named tool-of-record wins at TSMC, Samsung, SK hynix, Micron or Intel; mainland-China share; warrant exercise terms; acquisitions after June 2026; any export-control limits on China sales.
- Nextin Q3 2026; Auros Q3 2026 figures and IR-overlay products; Koh Young semiconductor mix; SEMES, ATI, NanoScope Systems, Oros.
- Gauss Labs post-2024 funding and non-SK customers.
- Taiwan: Cheng Mei Instrument listing and financials; which AOI vendors serve TSMC or ASE at wafer or packaging level (V5 claims rest on media only); lab margins for 2025; TSMC data-residency rules.
- India: R&D centres of KLA, Applied Materials, Lam and Advantest; listed engineering-services firms' test revenue; exact ISM plant start dates (sources conflict).
- Southeast Asia: ViTrox segment and China mix; Pentamaster revenue (sources conflict).
- Investor access: current FINI/FPI procedures; ETF holdings; whether any covered company has a depositary receipt.

## 12. Sources (reference definitions: label, URL, title with date; accessed 12 Nov 2026 unless stated)

[PIR]: https://www.parksystems.com/kr/investors/fiancial-statements "Park Systems IR financial statements page (FY2022-H1 2026), accessed 12 Nov 2026"
[PDK]: https://www.parksystems.com/content/dam/parksystems/investor/pdf/2026_2Q_%ED%8C%8C%ED%81%AC%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%8A%A4%20IR%20%EC%9E%90%EB%A3%8C_260814(%EA%B5%AD%EB%AC%B8).pdf "Park Systems company intro + 2Q26 earnings IR deck (Korean), 14 Aug 2026"
[PH1]: https://www.parksystems.com/content/dam/parksystems/investor/pdf/-%ED%8C%8C%ED%81%AC%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%8A%A4-%EB%B0%98%EA%B8%B0%EB%B3%B4%EA%B3%A0%EC%84%9C(2026.08.14).pdf "Park Systems half-year report (반기보고서, DART copy), filed 14 Aug 2026"
[PVU]: https://www.parksystems.com/content/dam/parksystems/investor/pdf/%ED%8C%8C%ED%81%AC%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%8A%A4_2026%20%EA%B8%B0%EC%97%85%EA%B0%80%EC%B9%98%EC%A0%9C%EA%B3%A0%EA%B3%84%ED%9A%8D.pdf "Park Systems 2026 corporate value-up plan, May 2026"
[PLY]: https://www.parksystems.com/en/news-events/news/news-details.pr250106009 "Park Systems release: acquisition of Lyncée Tec SA, 6 Jan 2025"
[DD25]: https://www.ddaily.co.kr/page/view/2025041413510565105 "Digital Daily interview with CEO Park Sang-il, 14 Apr 2025"
[FN0601]: https://n.news.naver.com/mnews/article/014/0005529223 "FN News, 1 Jun 2026 (investor day of 29 May 2026); also https://www.fnnews.com/news/202606010841427685"
[FN0506]: https://n.news.naver.com/mnews/article/014/0005517677 "FN News, 6 May 2026 (Rocky Mountain Nanotechnology acquisition)"
[FN0816]: https://n.news.naver.com/mnews/article/014/0005562207 "FN News, 16 Aug 2026 (Q2 2026, 20.6% share claim)"
[ZD0529]: https://n.news.naver.com/mnews/article/092/0002424716 "ZDNet Korea, 29 May 2026 (packaging, NX-TSH, Intel)"
[MH0602]: https://n.news.naver.com/mnews/article/021/0002795199 "Munhwa Ilbo, 2 Jun 2026 (CEO on China, Bruker, M&A)"
[MH1104]: https://n.news.naver.com/mnews/article/021/0002830337 "Munhwa Ilbo, 4 Nov 2026 (QY Research 2025 share 23.8%)"
[DS0602]: https://dealsite.co.kr/articles/162519 "Dealsite, 2 Jun 2026 (utilisation 96%, BW use of funds)"
[ET0712]: https://n.news.naver.com/mnews/article/030/0003446789 "ET News, 12 Jul 2026 (WLI, FX line)"
[SK0930]: https://n.news.naver.com/mnews/article/018/0006377371 "Edaily on SK Securities note, 30 Sep 2026"
[MZ0915]: https://n.news.naver.com/mnews/article/018/0006369420 "Edaily on Meritz Securities note, 15 Sep 2026"
[SH0728]: https://stockhub.kr/news/news_080f11887650 "stockhub summary of SK Securities 2Q26 preview, 28 Jul 2026"
[NV140860]: https://m.stock.naver.com/api/stock/140860/integration "Naver Finance quote and valuation, Park Systems, 12 Nov 2026"
[P140860]: https://m.stock.naver.com/api/stock/140860/integration "same as NV140860"
[A140860]: https://m.stock.naver.com/api/stock/140860/finance/annual "Naver/FnGuide annual financials and consensus, 12 Nov 2026"
[Q140860]: https://m.stock.naver.com/api/stock/140860/finance/quarter "Naver/FnGuide quarterly financials and consensus, 12 Nov 2026"
[NVN140860]: https://m.stock.naver.com/api/news/stock/140860?pageSize=20&page=1 "Naver news headline list, Park Systems, 12 Nov 2026"
[P348210]: https://m.stock.naver.com/api/stock/348210/integration "Naver quote, Nextin, 12 Nov 2026"
[A348210]: https://m.stock.naver.com/api/stock/348210/finance/annual "Naver/FnGuide annual, Nextin"
[Q348210]: https://m.stock.naver.com/api/stock/348210/finance/quarter "Naver/FnGuide quarterly, Nextin"
[P322310]: https://m.stock.naver.com/api/stock/322310/integration "Naver quote, Auros, 12 Nov 2026"
[Q322310]: https://m.stock.naver.com/api/stock/322310/finance/quarter "Naver/FnGuide quarterly, Auros"
[ES322310]: https://etfshopping.com/stock/322310/earnings "Auros earnings calendar page (search result), Nov 2026"
[P098460]: https://m.stock.naver.com/api/stock/098460/integration "Naver quote, Koh Young, 12 Nov 2026"
[A098460]: https://m.stock.naver.com/api/stock/098460/finance/annual "Naver/FnGuide annual, Koh Young"
[Q098460]: https://m.stock.naver.com/api/stock/098460/finance/quarter "Naver/FnGuide quarterly, Koh Young"
[P064290]: https://m.stock.naver.com/api/stock/064290/integration "Naver quote, Intekplus, 12 Nov 2026"
[A064290]: https://m.stock.naver.com/api/stock/064290/finance/annual "Naver/FnGuide annual, Intekplus"
[Q064290]: https://m.stock.naver.com/api/stock/064290/finance/quarter "Naver/FnGuide quarterly, Intekplus"
[P420770]: https://m.stock.naver.com/api/stock/420770/integration "Naver quote, Gigavis, 12 Nov 2026"
[A420770]: https://m.stock.naver.com/api/stock/420770/finance/annual "Naver/FnGuide annual, Gigavis"
[A081180]: https://m.stock.naver.com/api/stock/081180/finance/annual "Naver/FnGuide annual, SEC"
[A168360]: https://m.stock.naver.com/api/stock/168360/finance/annual "Naver/FnGuide annual, Pemtron"
[A405100]: https://m.stock.naver.com/api/stock/405100/finance/annual "Naver/FnGuide annual, QRT"
[NVN168360]: https://m.stock.naver.com/api/news/stock/168360?pageSize=20&page=1 "Naver headline list, Pemtron (Micron Malaysia order, 23 Jun 2026)"
[NX1018]: https://n.news.naver.com/mnews/article/421/0009233867 "News1, 18 Oct 2026 (Nextin H1 2026 from DART)"
[NX1014]: https://n.news.naver.com/mnews/article/421/0009225900 "News1, 14 Oct 2026 (Nextin–SK hynix 254.4억)"
[NX0618]: https://n.news.naver.com/mnews/article/030/0003438768 "ET News, 18 Jun 2026 (Nextin US push, China 85-87% in 2024)"
[NX0210]: https://n.news.naver.com/mnews/article/092/0002410075 "ZDNet Korea, 10 Feb 2026 (IRIS-III)"
[NX1217]: https://n.news.naver.com/mnews/article/030/0003381687 "ET News, 17 Dec 2025 (ASPER)"
[NX0326]: https://n.news.naver.com/mnews/article/293/0000081622 "Bloter, 26 Mar 2026 (Nextin–SK hynix 107억; headline)"
[NX0825]: https://n.news.naver.com/mnews/article/008/0005404124 "Money Today, 25 Aug 2026 (Shinhan: China orders delayed; headline)"
[AU0211]: https://n.news.naver.com/mnews/article/018/0006217481 "Edaily, 11 Feb 2026 (Auros FY2025)"
[AU1110]: https://n.news.naver.com/mnews/article/003/0014313306 "Newsis, 10 Nov 2026 (Auros buyback trust; headline)"
[KY1103a]: https://n.news.naver.com/mnews/article/001/0016419112 "Yonhap, 3 Nov 2026 (Koh Young Q3 OP 194억; headline)"
[KY1103b]: https://n.news.naver.com/mnews/article/003/0014298690 "Newsis, 3 Nov 2026 (Koh Young first 1,000억 quarter; headline)"
[KY1021]: https://n.news.naver.com/mnews/article/366/0001199401 "Chosun Biz, 21 Oct 2026 (China AI-server order; headline)"
[KY0930]: https://n.news.naver.com/mnews/article/030/0003471121 "ET News, 30 Sep 2026 (SOCAMM2 order; headline)"
[KY0806]: https://n.news.naver.com/mnews/article/018/0006346288 "Edaily, 6 Aug 2026 (294억 capex; headline)"
[KY1012]: https://n.news.naver.com/mnews/article/366/0001197274 "Chosun Biz, 12 Oct 2026 (KIS target 44,000; headline)"
[IK0626]: https://n.news.naver.com/mnews/article/018/0006315757 "Edaily, 26 Jun 2026 (Intekplus 140억; headline)"
[IK0702a]: https://n.news.naver.com/mnews/article/018/0006320979 "Edaily, 2 Jul 2026 (Intekplus 218억; headline)"
[IK0702b]: https://n.news.naver.com/mnews/article/018/0006321002 "Edaily, 2 Jul 2026 (Intekplus 85억, Taiwan; headline)"
[IK0909]: https://n.news.naver.com/mnews/article/018/0006366296 "Edaily, 9 Sep 2026 (Intekplus 61억; headline)"
[GV1028]: https://n.news.naver.com/mnews/article/015/0005347603 "Hankyung, 28 Oct 2026 (Gigavis 775억 in six days; headline)"
[SEC1110]: https://n.news.naver.com/mnews/article/018/0006407102 "Edaily, 10 Nov 2026 (SEC–Micron HBM 58억; headline)"
[SEC1019]: https://n.news.naver.com/mnews/article/366/0001198746 "Chosun Biz, 19 Oct 2026 (SEC first advanced-line order; headline)"
[PT0518]: https://n.news.naver.com/mnews/article/092/0002423073 "ZDNet Korea, 18 May 2026 (Pemtron Q1; headline)"
[GL-SKH]: https://news.skhynix.com/en/sk-hynix-and-gauss-labs-present-ai-based-semiconductor-virtual-metrology-research-at-spie-al-2026/ "SK hynix newsroom: SPIE AL 2026 papers with Gauss Labs, 2026"
[GL-AE]: https://www.asiae.co.kr/en/article/2024022910322485771 "Asia Economy, 29 Feb 2024 (SK hynix–Gauss Labs AI metrology; via search summary)"
[GL-CBI]: https://www.cbinsights.com/company/gauss-labs "CB Insights profile, Gauss Labs (accessed via search, Nov 2026)"
[TWSE-REV]: https://openapi.twse.com.tw/v1/opendata/t187ap05_L "TWSE OpenAPI listed-company monthly revenue, Oct 2026 data, output 11 Nov 2026"
[TPEX-REV]: https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O "TPEx OpenAPI OTC monthly revenue, Oct 2026 data, output 12 Nov 2026"
[TWSE-PE]: https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL "TWSE P/E, dividend yield, P/B, 11 Nov 2026"
[TPEX-PE]: https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis "TPEx P/E, yield, P/B, 12 Nov 2026"
[TWSE-PX]: https://openapi.twse.com.tw/v1/exchangeReport/STOCK_DAY_ALL "TWSE daily closing prices, 11 Nov 2026"
[TPEX-PX]: https://www.tpex.org.tw/openapi/v1/tpex_mainboard_daily_close_quotes "TPEx daily closing prices, 12 Nov 2026"
[TN0119]: https://technews.tw/?p=1499698 "TechNews (MoneyDJ reprint), 19 Jan 2026: analysis labs on 2nm and silicon photonics"
[UA-LAB]: https://uanalyze.com.tw/articles/8379856736 "uAnalyze: MA-tek / iST / MSScorps comparison, 2026 (via search summary)"
[V5-SD]: https://statementdog.com/news/16813 "StatementDog: 倍利科 CoPoS/CPO inspection, 2026 (via search summary)"
[V5-CT]: https://www.ctee.com.tw/news/20260406700011-430501 "Commercial Times, 6 Apr 2026: 倍利科 (via search summary)"
[V5-UDN]: https://udn.com/news/story/7241/9656703 "UDN: 倍利科 chairman 林坤禧, 2026 (via search summary)"
[V5-BN]: https://www.bnext.com.tw/article/90475/v5-technologies-listed "Business Next: V5 Technologies listing, 2026 (via search summary)"
[NV-TSMC]: https://nvidianews.nvidia.com/news/nvidia-and-tsmc-bring-ai-into-fabs-to-advance-semiconductor-design-and-manufacturing "NVIDIA newsroom: NVIDIA and TSMC bring AI into fabs (June 2026 per search summary)"
[MAKR]: https://www.electronicsforyou.biz/industry-buzz/bluehill-backs-makr-in-rs-102-million-semiconductor-metrology-deal/ "Electronics For You, Sep 2026: Makr Microsystems seed round"
[MAKR2]: https://www.startupresearcher.com/news/makr-microsystems-raises-rs-10-2-crore-seed-funding-round "Startup Researcher: Makr Microsystems seed, Sep 2026"
[TV-AI]: https://techovedas.com/indias-first-make-in-india-semiconductor-equipment-company-launched/ "techovedas: 'India's first Make in India semiconductor equipment company' (date not checked)"
[ISM-TV]: https://techovedas.com/india-is-finally-making-chips-why-4-four-commercial-fabs-in-2026-change-everything/ "techovedas: Indian assembly-and-test plants in 2026"
[ISM-CT]: https://www.communicationstoday.co.in/indias-first-chip-shipments-are-real-not-fabs/ "Communications Today: India's first chip shipments, ~Nov 2026"
[ISM-EMS]: https://www.emsnow.com/?p=55356 "EMSNow: India approves second phase of ISM, 2026"
[TESS]: https://www.bisinfotech.com/tessolve-pursues-us-and-india-acquisitions-to-drive-500m-revenue-goal-and-ai-chip-expansion/ "BIS Infotech: Tessolve FY26 revenue and targets, 2026"
[VT1106]: https://www.thestar.com.my/business/business-news/2026/11/06/vitroxs-3q26-profit-more-than-triples "The Star, 6 Nov 2026: ViTrox 3Q26"
[VT1105]: https://www.thestar.com.my/business/business-news/2026/11/05/vitrox039s-3q-net-profit-leaps-to-rm11858mil "The Star, 5 Nov 2026: ViTrox 3Q26 net profit"
[VT-EDGE]: https://theedgemalaysia.com/node/824707 "The Edge Malaysia, 6 Nov 2026: ViTrox (via search summary)"
[PM1106]: https://www.thestar.com.my/business/business-news/2026/11/06/pentamasters-3q-profit-up-to-rm2044mil "The Star, 6 Nov 2026: Pentamaster 3Q26"
[MI1102]: https://www.thestar.com.my/business/business-news/2026/11/02/mi-technovations-strong-quarter-fuels-optimism "The Star, 2 Nov 2026: MI Technovation 3Q26"
[SX-TH]: https://www.streetinsider.com/PRNewswire/Tong+Hsing+Electronic+Partners+with+SixSense+on+AI+Solutions/26054270.html "PR Newswire via StreetInsider: Tong Hsing partners with SixSense, Feb/Mar 2026"
[SX-SGI]: https://sginnovate.com/blog/delivering-smarter-more-efficient-defect-classification-advanced-manufacturing "SGInnovate blog on SixSense (date not checked)"
[KR-MSCI]: https://view.asiae.co.kr/en/article/2026062407374289583 "Asia Economy, 24 Jun 2026: Korea fails again to join MSCI DM watch list"
[KR-ROAD]: https://view.asiae.co.kr/en/article/2026010819293113851 "Asia Economy, 8 Jan 2026: roadmap for DM index inclusion (FX hours etc.)"
[KR-OMNI]: https://www.asiae.co.kr/en/article/2025120408024651696 "Asia Economy, 4 Dec 2025: integrated (omnibus) accounts for foreign investors"

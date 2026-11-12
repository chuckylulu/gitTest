# Japanese listed instrument makers relevant to self-tuning instruments: financial notes (as of 12 November 2026)

Notes for the "self-tuning instruments: quality and entry" report. Part 1 holds the quality facts (tests c, d, e). Part 3 holds the valuation and entry facts and is kept separate. Each figure links to its source; the full source list with dates is in Part 5. "My calc", "my estimate" and "inference" mark my own arithmetic or judgement.

## Read-me: scope, conventions and limits

- **Companies.** In depth: JEOL (6951), Hitachi (6501; Hitachi High-Tech's measurement and analysis business), Shimadzu (7701), Rigaku Holdings (268A), Horiba (6856), Anritsu (6754), Lasertec (6920). Comparison rows: Advantest (6857), Hamamatsu Photonics (6965), JTEC (3446), Yokogawa Electric (6841), Tokyo Seimitsu (7729).
- **Fiscal years.** Each company's own convention is used.
  - FY3/27 means April 2026 to March 2027 for JEOL, Hitachi, Shimadzu and Anritsu. Hitachi and Anritsu call this "FY2026".
  - FY6/27 means July 2026 to June 2027 (Lasertec).
  - FY12/26 means calendar 2026 (Horiba, Rigaku).
- **Forecast labels.** "Co. forecast" means guidance in the company's 決算短信. "Consensus" means the StockAnalysis/S&P Global figure.
- **Prices.** All prices are TSE closes on 12 Nov 2026 (15:30 JST), retrieved 12 Nov 2026.
  - The two price sources count market capitalisation differently. Yahoo!ファイナンス uses shares issued, including treasury shares. StockAnalysis uses shares outstanding.
  - I use Yahoo for PER on the company forecast and StockAnalysis for EV-based metrics.
- **Results available on 12 Nov 2026.** JEOL's 1H FY3/27 results and Horiba's Q3 FY12/26 results are scheduled for 13 Nov 2026, the day after this note ([Y-6951], [Y-6856]).
  - For these two companies, the latest reported periods are therefore JEOL Q1 (April to June 2026) and Horiba 1H (January to June 2026).
  - All other requested periods were read from primary filings.
- **Tool limits in this session.**
  - The shared WebSearch budget ran out early in the session.
  - The Firecrawl and Exa tools had no credits. Two Firecrawl scrape calls and one Exa fetch call were attempted at the start; all three were rejected for lack of credits, and no data from them is used. On the coordinator's later instruction, no Firecrawl or other search service was used after that.
  - Kabutan, irbank and minkabu returned HTTP 403.
  - As a result, I fetched known URLs directly: TDnet PDFs through Yahoo!ファイナンス's disclosure mirror (the same filing files), StockAnalysis pages, and Yahoo!ファイナンス price pages.
  - Some items remain unverified; they are listed in Part 4.

---

## Part 1. Quality facts (tests c, d, e)

### 1.0 Common cycle context, November 2026

**The early-November sell-off**
- On 6 Nov 2026 the Nikkei 225 fell 3,643.13 points (-5.96%) to 57,434.77, its fifth straight daily fall. Matsui Securities called it "史上3番目の下落幅" (the third-largest point drop on record) [MAT-1106].
- Matsui gave these reasons [MAT-1106]:
  - The Democratic sweep in the 3 Nov US midterm elections raised fears of tighter AI and data-centre regulation.
  - The Philadelphia Semiconductor Index (SOX) fell 12% and the Nasdaq 5% in the previous US session.
  - Investors were concerned about curbs on data-centre construction.
- On 5 Nov the Nikkei had fallen 1.79% to 61,077.90 (search snippet of [MAT-1105]).

**Drawdowns from 2026 highs to the 12 Nov close** (my calc from Yahoo's 年初来高値)

| Company | Fall from 2026 high |
|---|---|
| Rigaku | -60% |
| Anritsu | -51% |
| Lasertec | -38% |
| Tokyo Seimitsu | -38% |
| Yokogawa | -33% |
| Horiba | -32% |
| Hamamatsu | -29% |
| Advantest | -29% |
| JEOL | -28% |
| Hitachi | -18% |
| Shimadzu | -2% |

The 2026 low came on 6 Nov 2026 for Anritsu, Rigaku, Hitachi, Yokogawa, Tokyo Seimitsu and JTEC (Yahoo pages).

**Company demand commentary (late October to November 2026) still describes strong AI-related demand**
- Lasertec: device makers "have further expanded their capital investment plans… the outlook for orders in FY2027 has exceeded previous expectations" [LT-Q1].
- Rigaku: AI semiconductor demand "has recently broadened to logic, DRAM, flash, and advanced packaging" [RG-3Q].
- Hitachi: Connective Industries orders +26%, "driven by semiconductor manufacturing, measurement and inspection equipment" [HI-OUT].
- Anritsu: "The build-out and speeding-up of data centers for generative AI is accelerating" [AN-1H].
- Shimadzu: the "semiconductor-related market continued to be buoyant" [SH-1H].
- Horiba: semiconductor growth "driven by demand for advanced semiconductors for AI and data centers" [HO-1H].

**Yen**
- USD/JPY bid was 159.658 on Yahoo!ファイナンス (retrieved 12 Nov 2026; no timestamp shown) [Y-FX].
- Company assumptions:

| Company | US$ assumption | € assumption | Note | Source |
|---|---|---|---|---|
| Hitachi | ¥160 (2H) | ¥185 | | [HI-OUT] |
| Horiba | ¥155 (full year) | ¥180 | 1H actual average ¥158.29/US$ | [HO-1H] |
| Anritsu | ¥150 | ¥175 | | [AN-1H] |
| JEOL (medium-term plan) | ¥145 | ¥157 | | [JE-MTP] |

- Inference: at about ¥160, the yen is weaker than most of these assumptions, which supports translated earnings.

**Academic and government budgets**
- Rigaku: "The decline in revenue from the academia sector due to the impact of Trump policies since last year has persisted longer than expected." Its 1-3Q academia/government revenue was ¥9.0bn, against ¥11.5bn a year earlier [RG-3Q p.19].
- Shimadzu: 1H liquid-chromatograph sales rose for "the government sector and university markets" in North America and Other Asia, and mass-spectrometer sales rose in Europe [SH-1H].
- Budget figures for Japan, the US and China could not be verified.

**Export controls and tariffs**
- None of the filings I read quantified an export-control or tariff effect in 2026.
- 2026 METI and US BIS decisions could not be verified (see Part 4).

---

### 1.1 JEOL (6951): electron microscopes, NMR and mass spectrometers; electron-beam lithography (mask writers); clinical analysers

**Takeaway.**
- Earnings swing with the high-margin semiconductor equipment business. Industrial Equipment was 27% of FY3/26 sales and 60% of segment profit, and 34% of its sales went to China.
- FY3/26 sales fell 8.8%. Q1 FY3/27 sales fell 39% with an operating loss.
- FY3/27 guidance still calls for operating profit up 1.9%, with the year weighted to 2H.
- The balance sheet is solid (equity ratio 62%). However, free cash flow was about zero in FY3/26 because of heavy capex and a ¥12.8bn buyback.
- 1H results are due 13 Nov 2026.

**Latest results and guidance**
- **Q1 FY3/27 (April to June 2026; reported 14 Aug 2026).**
  - Sales ¥24,465m (-39.1%).
  - Operating loss ¥1,961m, against an operating profit of ¥5,792m a year earlier.
  - Net loss ¥1,710m.
  - Equity ratio 62.3% (59.9% at 31 Mar 2026).
  - Full-year forecast unchanged.
  - Sources: Yahoo!ファイナンス summary of the 決算短信 [Y-6951] and a search snippet of the JPX filing. The primary Q1 PDF [JE-Q1] was not opened, so these figures are secondary.
- **FY3/26 (April 2025 to March 2026; 決算短信 of 15 May 2026)** [JE-FY26]:
  - Sales ¥179,353m (-8.8%).
  - Operating profit ¥26,017m (-26.7%); operating margin 14.5%, down from 18.0%.
  - Ordinary profit ¥28,610m.
  - Net profit ¥22,097m (+18.2%). FY3/25 net profit had been depressed by a ¥12,381m valuation loss on investment securities.
  - EPS ¥432.58; ROE 15.7%.
- **FY3/27 guidance (15 May 2026; unchanged at Q1)** [JE-FY26]:
  - 1H: sales ¥63,000m (-23.2%); operating profit ¥6,000m (-49.7%).
  - Full year: sales ¥164,000m (-8.6%); operating profit ¥26,500m (+1.9%, margin 16.2%); net profit ¥21,300m (-3.6%); EPS ¥432.64.
  - Dividend ¥132 (¥66 + ¥66).
  - My calc: the guidance implies 2H sales of ¥101.0bn and 2H operating profit of ¥20.5bn (20.3% margin).
- **Segments, FY3/26 (FY3/25 in brackets)** [JE-FY26 pp.12-13]:

| Segment | Products | Sales | Segment profit (margin) |
|---|---|---|---|
| Scientific & Metrology Instruments | electron microscopes, NMR, mass spectrometers | ¥116,295m (¥124,793m) | ¥13,069m, 11.2% (¥15,017m, 12.0%) |
| Industrial Equipment | e-beam lithography, e-beam metal 3D printing, high-frequency power supplies | ¥48,131m (¥56,483m) | ¥19,363m, 40.2% (¥26,316m, 46.6%) |
| Medical Equipment | clinical chemistry analysers | ¥14,926m (¥15,418m) | ¥64m (¥662m) |
| Corporate | | | -¥6,479m |

- Management comments for 1H on semiconductors, China, budgets, tariffs and FX will only come with the 13 Nov results.

**Test c: revenue model**
- The documents I read give no split of service, consumables or software revenue, so their share could not be verified.
- The medium-term plan's "YOKOGUSHI 2.0" has a second axis, "Applications/services": "increasing value through the acquisition of diversified data through the integration of hardware and software… development of applications responsible for the analysis of such data" [JE-MTP].
- Inference: revenue is still mostly one-off hardware, and mask-writer shipments are lumpy (Q1 FY3/27 sales -39%).

**Test d: financial strength**
- **Five-year trend (StockAnalysis/S&P; fiscal years ending March)** [SA-F-6951] [SAR-6951]:

| FY | Revenue | Gross margin | Operating margin | ROE | ROIC | FCF (S&P definition) |
|---|---|---|---|---|---|---|
| FY3/22 | ¥138.4bn | 40.0% | 10.2% | 17.9% | 16.3% | ¥21.4bn |
| FY3/23 | ¥162.7bn | 44.7% | 14.9% | 19.0% | 26.2% | -¥2.7bn |
| FY3/24 | ¥174.3bn | 45.5% | 15.8% | 19.1% | 21.4% | ¥12.1bn |
| FY3/25 | ¥196.7bn | 47.0% | 18.1% | 14.3% | 24.3% | ¥20.1bn |
| FY3/26 | ¥179.4bn | 46.3% | 14.5% | 15.7% | 16.1% | ¥2.5bn |
| TTM to Jun 2026 | ¥163.7bn (-18.4%) | | 11.2% | | | |

- **FY3/26 cash flow** [JE-FY26]:
  - Operating cash flow ¥16,000m (FY3/25: ¥23,104m).
  - Capex: property, plant and equipment ¥13,489m plus intangibles ¥1,606m. Free cash flow is about ¥0.9bn on my calc (¥2.5bn on StockAnalysis's definition).
  - Buyback ¥12,770m: treasury shares rose from 393,904 to 2,831,561, out of 51,532,800 issued.
  - Dividends ¥5,908m.
  - Borrowing: net short-term +¥14,000m; new long-term ¥8,000m.
- **Balance sheet** [JE-FY26] [SA-6951]:
  - At 31 Mar 2026: total assets ¥242.0bn; net assets ¥144.9bn; cash and deposits ¥38.9bn.
  - StockAnalysis TTM: net cash ¥17.96bn; debt ¥14.28bn.
- **Shareholder returns and R&D.**
  - Payout ratio 30.5% in FY3/26 [JE-FY26]. The medium-term plan guideline is 30% [JE-MTP].
  - R&D as a share of sales could not be verified.
- **Concentration by region, FY3/26** [JE-FY26]:
  - Japan ¥58,788m (32.8%); Americas ¥27,636m (15.4%); China ¥35,609m (19.9%; FY3/25 22.8%); other ¥57,319m (32.0%).
  - China's share by segment: Industrial Equipment ¥16,470m (34.2%); Scientific ¥18,496m (15.9%, down from ¥24,646m).
  - Customer concentration is not disclosed in the documents I read.

**Test e: cycle, scenarios, export controls**
- **Cycle position (inference).**
  - Industrial Equipment sales fell 14.8% in FY3/26, and segment profit fell 26%.
  - The 39% group sales fall in Q1 FY3/27 points to a trough in mask-writer shipments.
  - The guidance assumes a strong 2H.
  - Scientific Instruments sales fell 6.8% in FY3/26, including -25% in China [JE-FY26].
- **Dependence on AI-related capex (inference).** Mask writers serve leading-edge photomask production, and Industrial Equipment supplies 60% of segment profit. Profit is therefore highly geared to leading-edge semiconductor investment.
- **Scenario exposure (inference).**
  - Steady growth: supportive.
  - Financing-led pause around 2028: Industrial Equipment profit at risk; segment profit already fell 26% in FY3/26.
  - Faster acceleration: upside, limited by capacity. FY3/26 additions to property, plant and intangibles were ¥20.2bn.
- **Export controls (inference).** 34% of Industrial Equipment sales go to China, so the business is exposed to any tightening of Japanese or US controls on lithography-related tools. No change in 2026 was verified.

**Theme exposure**
- My calc from [JE-FY26]:

| Segment | Share of FY3/26 sales | Share of segment profit |
|---|---|---|
| Scientific & Metrology Instruments | 64.8% | 40.2% |
| Industrial Equipment | 26.8% | 59.6% |
| Medical Equipment | 8.3% | 0.2% |

- Inference: the theme mainly touches the Scientific segment, plus part of the e-beam systems.
- Once the medical business passes to Sysmex [JE-SYS], JEOL becomes a two-segment company. On FY3/26 figures (my calc), Scientific & Metrology would be about 71% of sales and Industrial Equipment about 29%. This raises theme purity.

**Medium-term plan and governance**
- **"Evolving Growth 2.0 – A New Horizon"** (announced 15 May 2025; covers FY2025 to FY2029, i.e., FY3/26 to FY3/30) [JE-MTP]:
  - FY2029 targets: net sales ¥225.0bn; operating profit ¥45.0bn (20.0% margin); net profit ¥33.8bn; ROE ≥15%; ROIC ≥15%. FX assumptions ¥145/US$ and ¥157/€.
  - Priority fields: semiconductor and life science.
  - Strategic R&D and M&A.
  - Payout guideline 30%; "for the time being, place greater emphasis on strategic investment for growth".
  - My calc: from the FY3/27 guidance, the FY2029 target needs sales +37% and operating profit +70% within three years.
- **Events.**
  - ¥12.8bn buyback in FY3/26 [JE-FY26].
  - FY3/26 year-end dividend raised from ¥53 to ¥79 (15 May 2026) [JE-FY26].
  - **Sale of the medical business to Sysmex.** On 2 Sep 2025 the board resolved to move the medical-equipment business (automated clinical chemistry analysers) into a new wholly owned subsidiary by simplified absorption-type company split, and then to "transfer to SYSMEX CORPORATION… all shares of the New Company" [JE-SYS]. The statutory pre- and post-split disclosures followed on 12 May 2026 [JE-TDnet]. The price, the closing date of the share transfer and the earnings effect could not be verified, because pages 3 onward of the notice were not read.
  - **Self-tender buying out Nikon (an unwinding cross-shareholding)** [JE-TOB]:
    - In late October 2025 Nikon, JEOL's second-largest shareholder (2,300,000 shares, 4.49%), said it intended to sell all of its shares "to enhance its own asset efficiency and strengthen its financial position", while keeping the business alliance that dates from 14 Feb 2014. Under that alliance JEOL had issued 8,000,000 new shares to Nikon at ¥368.
    - JEOL announced a tender offer for its own shares on 2 Feb 2026 and reported the result and completion on 5 Mar 2026 [JE-TDnet].
    - The tender price was not read. My calc: FY3/26 treasury-share purchases of ¥12,770m over a rise of about 2.44m treasury shares imply an average of about ¥5,240 a share.
  - I found no activist investor, but my search was limited.

**Gaps.** 1H results (13 Nov); share of service revenue; R&D ratio; price and closing date of the medical sale to Sysmex; the Nikon tender price; mask-writer orders and backlog; customer concentration.

---

### 1.2 Hitachi (6501): Hitachi High-Tech's Measurement & Analysis Systems

**Takeaway.**
- The theme sits in "Measurement & Analysis Systems" (M&AS), in the Industrial Solutions business unit of the Connective Industries (CI) segment.
- M&AS FY2026 forecast: revenue ¥900bn (+10%), adjusted EBITA ¥124bn (13.8%). That is only about 7.5-8% of group revenue and EBITA.
- The group is financially very strong (1H free cash flow ¥677bn; ¥814bn of shareholder returns planned for FY2026). It is a low-purity way to own the theme.

**Latest results and guidance**
- **1H FY2026 (April to September 2026; reported 28 Oct 2026; IFRS)** [HI-1H] [HI-OUT]:
  - Revenue ¥5,614.0bn (+17%; +10% normalised).
  - Adjusted operating income ¥643.3bn (+27%); EBIT ¥627.5bn.
  - Net profit ¥416.6bn (-12%). The prior year included a ¥91.7bn gain on the sale of the air-conditioning joint venture.
  - EPS ¥93.20. Gross margin 30.1% (my calc).
  - Q2 alone: revenue ¥2,904.4bn (+15%); adjusted EBITA ¥376.1bn (12.9%).
- **Segments, 1H** [HI-1H] [HI-OUT]:

| Segment | Revenue | Adjusted EBITA |
|---|---|---|
| Digital Systems & Services (DSS) | ¥1,533.2bn | ¥211.5bn |
| Energy | ¥1,872.4bn | ¥274.9bn |
| Mobility | ¥693.0bn | ¥55.9bn |
| Connective Industries (CI) | ¥1,586.6bn (+11%) | ¥178.4bn (11.2%, +40bp) |

  - CI orders ¥1,945.8bn (+26%), "driven by semiconductor manufacturing, measurement and inspection equipment".
- **Measurement & Analysis Systems** [HI-OUT p.26]:
  - Q2 FY2026: revenue ¥223.8bn (+6%); adjusted EBITA ¥34.1bn (15.2%, -140bp). The margin fell on "increase in strategic investments in Measurement & Analysis Systems".
  - FY2026 forecast: revenue ¥900.0bn (+10%; unchanged); adjusted EBITA ¥124.0bn (13.8%, +130bp; +¥2.0bn against the previous forecast).
  - Industrial Solutions business unit: FY2026 forecast ¥1,564.0bn and ¥209.3bn.
- **FY2026 guidance, raised 28 Oct** [HI-OUT]:
  - Revenue ¥12,000bn (+13%; previous ¥11,700bn).
  - Adjusted EBITA ¥1,560bn (13.0%; previous ¥1,520bn).
  - Net profit ¥920bn (previous ¥900bn); EPS ¥206.41; core free cash flow ¥920bn; ROIC 13.5%.
  - CI: revenue ¥3,300bn (+7%); adjusted EBITA ¥390bn (11.8%).
  - Management: "Continue monitoring the impact of geopolitical risks and higher interest rates on orders and customer demand."
  - CI full-year revenue driver: "Higher sales of semiconductor manufacturing, measurement and inspection equipment backed by AI-related demand" [HI-OUT p.5].
- **Revenue by market, 1H:** Japan 33%; North America 17%; Europe 22%; Asia 20%; other 8% [HI-1H].

**Test c: revenue model**
- The split of M&AS revenue into service and consumables versus systems is not disclosed in the documents I read.
- CI full-year profit driver: "Expansion of the service business including Lumada business" [HI-OUT p.5].

**Test d: financial strength (group)**
- **Margins and returns** [SA-6501] [SAR-6501] [HI-OUT]:
  - TTM: gross margin 30.2%; operating margin 11.7%; ROE 12.3%; ROIC 14.95%.
  - The company's own FY2026 ROIC forecast is 13.5%.
  - Five-year ROE (FY3/22 to FY3/26): 13.7%, 13.2%, 11.2%, 11.1%, 13.3%. ROIC: 9.3%, 12.0%, 9.9%, 10.9%, 14.4%.
- **Cash and balance sheet** [HI-1H]:
  - 1H operating cash flow ¥798.9bn; free cash flow ¥677.3bn.
  - Cash ¥1,511.0bn. Gross debt about ¥1,028.9bn (short-term ¥50.9bn, current portion of long-term ¥424.7bn, long-term ¥553.4bn), so net cash is about ¥482bn (my calc). StockAnalysis shows ¥938.6bn because it includes short-term investments.
  - Equity ratio about 43% (my calc).
- **Shareholder returns.**
  - FY2026: dividends ¥264bn plus buybacks ¥550bn, for a total of ¥814bn [HI-OUT].
  - The buyback covers up to 160m shares, was approved on 27 Apr 2026, and was 52% complete at the end of 1H.
  - Interim dividend raised from ¥28 to ¥32.
  - 1H buybacks ¥290.4bn [HI-1H].
- R&D: not captured.

**Test e: cycle, scenarios, FX**
- **Cycle.** CI orders rose 26%. M&AS full-year growth is guided at +10% on AI-related demand, although the Q2 M&AS margin fell 140bp [HI-OUT].
- **Scenario exposure (inference).** M&AS is cyclical with semiconductor investment, but it is under 10% of the group. Hitachi's larger AI exposure comes through Hitachi Energy and DSS, which lie outside the theme.
- **FX.** 2H assumption ¥160/US$. Each ¥1 move changes revenue by ¥8.0bn and adjusted EBITA by ¥1.1bn (US dollar) [HI-OUT].
- **China.** Not separately disclosed (Asia is 20% of revenue). The full-year profit outlook cites "weaker demand for new elevator and escalator installations (China)" [HI-OUT p.26].

**Theme exposure**
- M&AS is 7.5% of FY2026 forecast revenue and 7.9% of forecast adjusted EBITA (my calc).
- The split between electron microscopes, CD-SEM/defect review and clinical analysers could not be verified.

**Medium-term plan and governance**
- The numeric targets of the medium-term plan (Inspire 2027) are not in the documents read and could not be verified.
- Events:
  - ATM business deconsolidated on 1 Oct 2026.
  - Home-appliance business "scheduled to be deconsolidated within FY2026" [HI-OUT pp.23,26].
  - Industry SI moved from CI to DSS from 1 Apr 2026 [HI-1H].
  - Hitachi Energy Investor Day materials published 2 Nov 2026 [HI-TDnet].
  - Board Incentive Plan Trust introduced (28 Oct 2026) [HI-TDnet].
  - Buyback progress notices on 2 Oct and 4 Nov 2026 [HI-TDnet].

---

### 1.3 Shimadzu (7701)

**Takeaway.**
- Shimadzu is a steady, diversified analytical-instrument business: Analytical & Measuring Instruments (A&MI) is 63% of sales, with growing management emphasis on recurring revenue.
- 1H FY3/27 sales rose 10% and operating profit 18%, and guidance was raised.
- The ¥112bn cash purchase of Tescan (Czech electron-microscope and FIB-SEM maker) adds direct theme exposure. It also took net cash to about zero.
- ROIC has trended down from about 20% to about 12%.

**Latest results and guidance**
- **1H FY3/27 (April to September 2026; reported 6 Nov 2026)** [SH-1H]:
  - Net sales ¥281,984m (+10.0%).
  - Operating profit ¥37,359m (+18.3%; margin 13.2%).
  - Ordinary profit ¥38,729m (+23.5%); net profit ¥28,264m (+19.6%); EPS ¥97.82.
  - Operating profit before goodwill amortisation ¥38,103m (+18.0%).
- **Segments, 1H** (profit before goodwill amortisation; prior year restated to the new measure) [SH-1H p.14]:

| Segment | Sales | Segment profit (margin) |
|---|---|---|
| Analytical & Measuring Instruments | ¥177,089m (+5.3%) | ¥24,575m (+2.3%; 13.9%) |
| Medical Systems | ¥35,670m (+6.1%) | ¥2,964m (+119.2%) |
| Industrial Machinery | ¥44,709m (+35.8%) | ¥8,461m (+81.8%; 18.9%) |
| Aircraft Equipment | ¥21,579m | ¥4,399m |
| Other | ¥2,935m | ¥496m |
| Adjustments | | -¥2,793m |

- **FY3/27 guidance, raised 6 Nov (previous guidance 6 Aug)** [SH-1H]:
  - Sales ¥630,000m (+12.4%).
  - Operating profit ¥84,000m (+14.0%); ordinary profit ¥85,000m.
  - Net profit ¥61,000m (+0.8%); EPS ¥211.21.
  - Operating profit before goodwill amortisation ¥89,000m (+18.4%).
  - Dividend ¥72 (¥28 interim + ¥44 year-end), against ¥69 for FY3/26.
- **Management comments** [SH-1H]:
  - "semiconductor-related market continued to be buoyant, and in North America and China, investment related to the research, development, and production of biopharmaceuticals was also active"
  - "sluggishness of the Chinese economy"
  - A&MI: "delays in capital investment due to worsening conditions in the Middle East"
  - Industrial Machinery (turbomolecular pumps for semiconductor equipment): growth "driven by the expanding demand for semiconductor devices led by the growth of generative AI and data center markets"

**Test c: revenue model**
- Shimadzu defines its core businesses as liquid chromatograph, mass spectrometer and gas chromatograph systems "and recurring business" [SH-1H].
- In 1H it was "strengthening our lineup of reagents and consumables and expanding our service business".
- A&MI segment profit rose "due to the expansion of our recurring business".
- Industrial Machinery is expanding service bases "to grow our recurring business".
- The numeric share of recurring revenue is not in the 決算短信 and could not be verified.

**Test d: financial strength**
- **Five-year trend (StockAnalysis/S&P; fiscal years ending March)** [SA-F-7701] [SAR-7701]:

| FY | Revenue | Gross margin | Operating margin | Net profit | FCF | ROE | ROIC |
|---|---|---|---|---|---|---|---|
| FY3/22 | ¥428.2bn | 41.7% | 14.9% | ¥47.3bn | ¥53.2bn | 13.2% | 19.6% |
| FY3/23 | ¥482.2bn | 41.7% | 14.2% | ¥52.0bn | ¥31.5bn | 12.9% | 19.7% |
| FY3/24 | ¥511.9bn | 43.1% | 14.2% | ¥57.0bn | ¥14.6bn | 12.5% | 17.6% |
| FY3/25 | ¥539.0bn | 43.5% | 13.3% | ¥53.8bn | ¥36.9bn | 10.9% | 15.1% |
| FY3/26 | ¥560.7bn | 44.6% | 13.1% | ¥60.5bn | ¥39.7bn | 11.4% | 13.9% |
| TTM | ¥586.4bn | 45.3% | 13.6% | | | | 11.7% |

- **1H FY3/27 cash flow** [SH-1H]:
  - Operating cash flow ¥38.0bn; capex ¥17.3bn. Free cash flow before M&A is about ¥20.7bn (my calc).
  - Outflow for purchase of subsidiaries ¥112.3bn.
  - Short-term borrowing +¥110.0bn; long-term repayments ¥29.3bn.
  - Cash ¥128.6bn, down from ¥160.8bn.
- **Balance sheet.**
  - StockAnalysis: debt ¥120.8bn; net cash ¥15.4bn [SA-7701].
  - Equity ratio fell from 76.6% to 66.8% [SH-1H].
- **Shareholder returns and R&D.**
  - Payout ratio about 31-34% [SAR-7701].
  - R&D could not be verified.
- **Concentration** (my calc from [SH-1H] p.15):
  - 1H group sales: Japan 39.7%; Americas 15.6%; Europe 10.2%; China 16.9%; other Asia 14.4%; other 3.2%.
  - A&MI China sales ¥33.8bn, 19.1% of the segment.

**Test e: cycle, scenarios, export controls**
- **Cycle.**
  - A&MI grew only 5.3%: Japan +0.2%, China +1.8%.
  - Industrial Machinery grew 35.8%, with Other Asia up 106.6% (Taiwan and Korea) [SH-1H].
  - Sensitivity to semiconductor capex is therefore concentrated in Industrial Machinery: 15.9% of sales and 22.2% of segment profit (my calc).
- **Scenario exposure (inference).**
  - Low to medium overall. Pharmaceutical, clinical and government demand for chromatographs and mass spectrometers is less tied to AI capex.
  - A pause around 2028 would mainly hit the turbomolecular-pump profits.
- **China.** 16.9% of sales.

**Theme exposure**
- A&MI (chromatographs, mass spectrometers, spectrophotometers, testing machines, and now Tescan electron microscopes) was 62.8% of 1H sales (my calc).
- **Tescan's size** (Czech GAAP) [SH-TES]:

| Fiscal year (December) | Net sales | EBITDA | Adjusted operating profit (before goodwill amortisation) |
|---|---|---|---|
| FY12/23 | CZK 3,316m | CZK 285m | CZK 146m |
| FY12/24 | CZK 4,026m (≈¥30.6bn at the notice's rate of ¥7.6/CZK, my calc) | CZK 627m (≈¥4.8bn) | CZK 475m (≈¥3.6bn) |

- Products: SEM, FIB-SEM, TEM and Micro-CT; "more than 4,000 units sold across 80 countries".
- On FY12/24 figures, Tescan adds roughly 5% to Shimadzu's sales base (my calc).

**Medium-term plan and governance**
- **Medium-term plan.**
  - The 1H report refers to core businesses "emphasized in the Medium-Term Management Plan" [SH-1H].
  - The Tescan notice of 25 Dec 2025 calls the "FY2023–2025 Medium-Term Management Plan" "ongoing". Its stated aim is to "transform into a total solution provider that delivers the 'data' its customers require", with M&A as an inorganic growth lever [SH-TES].
  - The name, period and numeric targets of any successor plan from FY3/27 could not be verified.
- **IFRS.** On 26 Feb 2026 Shimadzu gave notice of "Voluntary Adoption of International Financial Reporting Standards (IFRS)" [SH-TDnet]. The timing was not read.
- **Tescan deal.**
  - On 25 Dec 2025 Shimadzu agreed "with Carlyle" to buy all shares of Glass HoldCo s.r.o., which indirectly owns Tescan Group a.s. [SH-TES].
  - The seller was CETP V Glass 2 S.A.S. (Luxembourg), owned 71.41% by CETP V Glass 1 S.a.r.l., 17.57% by Glass Founders a.s. and 6.70% by Orsay Group.
  - The two companies had a business alliance since July 2024 and a joint "SUPERSCAN" SEM brand since February 2025.
  - The headline price is on a page I did not read.
  - Glass HoldCo, Tescan and 16 other companies were consolidated from 1H FY3/27. The verified figures are a cash outflow of ¥112.3bn net, goodwill up ¥127.2bn (provisional) and A&MI segment assets up ¥164.3bn [SH-1H pp.12,14-16].
  - My calc: the ¥112.3bn outflow is about 23x Tescan's FY12/24 EBITDA (≈¥4.8bn). This is a rough multiple that ignores Tescan's net debt and FX.
- I found no activist investor or tender offer, but my search was limited.

---

### 1.4 Rigaku Holdings (268A)

**Takeaway.**
- Rigaku is an X-ray analytical and semiconductor-metrology company in transition.
- Semiconductor Process Control (SPC) is the growth engine: a ">¥30bn business… growing by 30% annually", with 1-3Q orders +117%, expected to provide more than half of FY12/26 operating profit.
- Weak academic demand and special charges cut 1-3Q operating profit by 37%.
- Full-year guidance is unchanged but needs a record Q4.
- Carlyle's former vehicle, Atom Investment, has exited (0.29% left), and Onto Innovation holds 27%.

**Latest results and guidance**
- **Q3 FY12/26 (July to September 2026; reported 11 Nov 2026)** [RG-3Q]:
  - Revenue ¥21.1bn (+12.7%); gross profit ¥12.4bn (+27.4%; gross margin +6.8 points).
  - Operating profit ¥1.5bn (7.4%); profit ¥0.8bn; EBITDA ¥3.7bn.
  - Orders +66%.
  - Special charges of ¥1.36bn: a ¥0.6bn US allowance for doubtful accounts and a ¥0.75bn impairment at MILabs (EMEA).
- **1-3Q (January to September 2026)** [RG-3Q]:
  - Revenue ¥60.6bn (+2.0%); gross profit ¥34.0bn (+5.0%).
  - Operating profit ¥4.1bn (-37.0%); margin 6.8%, down from 11.0%.
  - Profit before tax ¥3.3bn; profit ¥2.4bn (-42.0%); EPS ¥10.95; EBITDA ¥9.1bn (15.1%).
  - Orders +39%; pipeline +21%.
- **By category, 1-3Q** [RG-3Q p.19]:

| Category | Revenue | Operating profit (margin) | Notes |
|---|---|---|---|
| Multipurpose Analytical Instruments | ¥23.7bn (-10.3%) | ¥0.8bn (3.7%) | academia/government ¥9.0bn, from ¥11.5bn |
| Semiconductor Process Control | ¥18.3bn (+21.4%) | ¥2.7bn (15.1%) | orders +117% |
| Components & Services | ¥18.6bn (+4.0%) | ¥1.7bn (9.3%) | services ¥9.0bn (+15%); components ¥9.5bn |

- **By category, Q3** [RG-3Q]:
  - Multipurpose: ¥8.6bn (+4.4%); margin 9.7%; orders +39%.
  - Semiconductor Process Control: ¥5.5bn (+29.4%); margin 14.0%; orders +189%.
  - Components & Services: ¥6.9bn (+12.4%); margin 1.5%; services +20%.
- **FY12/26 guidance (unchanged)** [RG-3Q p.13]:
  - Revenue ¥101.0bn (+7.2%); operating profit ¥19.4bn (+16.1%; 19.3%).
  - Profit ¥12.5bn; EPS ¥55.27; EBITDA ¥25.3bn.
  - FX sensitivity: each ¥1 against the US dollar moves revenue by ¥0.2bn and operating profit by ¥0.04bn.
  - "Revenue: We continue to expect upside." The operating-profit target is to be reached "excluding special factors".
  - Q4 revenue "image" ¥40.3bn [RG-3Q p.17].
  - My calc: implied Q4 operating profit is about ¥15.3bn (37.9% margin). In Q4 FY12/25 it was about ¥10.2bn on ¥34.6bn of revenue (about 29.5%).
- **Outlook comments** [RG-3Q pp.13-15]:
  - Full-year orders up about 30%; SPC orders up 70%.
  - End-December 2026 backlog up more than 30%.
  - SPC "set to account for >50% of FY12/26 operating profit".
  - "customer EUV inventory should be depleted during next year" (components).
  - "Revenue from industry customers to expand to >60% of the total in FY12/26."

**Test c: revenue model**
- Services were ¥9.0bn, 14.9% of 1-3Q revenue (my calc). Components & Services together were 30.7%.
- Services are growing 15-20% "thanks to an expanding installed base overseas, price hikes" [RG-3Q].

**Test d: financial strength**
- **History (StockAnalysis/S&P; fiscal years ending December)** [SA-F-268A] [SAR-268A]:

| FY | Revenue | Operating margin | Gross margin | FCF | ROE | ROIC |
|---|---|---|---|---|---|---|
| FY12/23 | ¥79.9bn | 19.1% | 58.4% | n/a | 18.4% | 10.8% |
| FY12/24 | ¥90.7bn | 20.6% | 61.0% | ¥8.7bn | 18.5% | 12.7% |
| FY12/25 | ¥94.2bn | 18.4% | 56.1% | ¥3.6bn | 13.4% | 10.2% |
| TTM | ¥95.4bn | | | ¥5.6bn | | |

- **Leverage** [SA-268A] [SAR-268A]:
  - Debt ¥66.9bn; cash ¥27.3bn; net debt ¥39.7bn.
  - Debt/equity 0.77 now (1.23 in 2021).
  - Caution: the StockAnalysis statistics page shows TTM revenue of ¥93.0bn, which looks stale against ¥95.4bn on its financials page.
- **Dividend.** ¥19 per share forecast for FY12/26; payout 46% on TTM earnings [SA-268A].
- **R&D.** R&D cost 0.7 points of 1-3Q margin and other SG&A 3.9 points [RG-3Q p.9]. The R&D ratio itself could not be verified.
- **Concentration (Q3; approximate readings from the chart)** [RG-3Q p.18]:
  - China about ¥2.8bn of ¥21.1bn (about 13%).
  - The Americas is the largest region for SPC (¥2.3bn of ¥5.5bn).
  - "China: Tax-exemption procedures were delayed, shifting revenue into 4Q."

**Test e: cycle, scenarios, export controls**
- **Cycle.** Rigaku describes SPC as in a "full-scale growth stage", driven by memory (DRAM/HBM), advanced logic and a recovery at North American IDMs. The academic business is still declining because of US policy [RG-3Q].
- **Scenario exposure (inference).** Medium to high. SPC (about 30% of 1-3Q revenue and expected to be more than half of FY operating profit) is geared to AI memory and logic capex. Multipurpose instruments and Components & Services provide ballast.
- **Export controls.** China is about 13% of Q3 revenue. Whether any export controls apply to its X-ray metrology tools could not be verified.

**Theme exposure**
- Share of 1-3Q revenue (my calc):
  - Multipurpose Analytical Instruments (X-ray diffractometers, XRF, CT, crystallography; classic expert-tuned instruments): 39%.
  - Semiconductor Process Control: 30%.
  - Components & Services: 31%.

**Medium-term plan and governance**
- **Ownership chain:**
  - 21 Apr 2026: capital and business alliance with Onto Innovation announced.
  - 22 May 2026: Atom Investment, L.P. (Cayman; the pre-IPO owner) launched a secondary offering of 29,580,300 shares, plus over-allotment. Price set 1 Jun; settled 8 Jun 2026 [RG-0522] [RG-0812].
  - 10 Aug 2026: 61,123,436 shares (27.00%) transferred from Atom to Onto. Atom was left with 0.29% [RG-0812].
  - 1 Oct 2026: Onto moved the stake to Onto Innovation Japan (26.99%) [RG-0930].
- **The relationship.** "Joint development of hybrid metrology solutions in the semiconductor process control domain" [RG-0930]. Development of a CD-SAXS-OCD hybrid engine "commenced with Onto", aiming at memory mass-production lines in 1Q FY12/27 [RG-3Q p.11].
- **Stale register data.** Yahoo still lists アトム・インベストメント at 27.27% (June 2026 register) [Y-268A]. The notices above supersede this.
- **Alliance terms (notice of 21 Apr 2026)** [RG-0421]:
  - Atom held 95,140,800 shares before the deal and transferred 61,123,436 of them (27.0%).
  - Onto agreed:
    - to "maintain the Company's managerial autonomy and independence as a publicly listed company";
    - not to sell during a "Transfer Restriction Period" (lock-up);
    - not to buy more shares or make an acquisition proposal during that period without Rigaku's consent (standstill).
  - After the restriction period, the two sides will hold good-faith consultations on capital policy if either requests them.
  - Onto has a pre-emptive right to keep its stake if Rigaku issues new shares.
  - Onto can nominate one non-executive director, Michael Plisinski (Onto CEO), while it holds at least 50% of the transferred shares.
  - Aims: joint hybrid metrology for AI, advanced logic, memory and packaging; cross-selling to Onto's customers; possible manufacturing in Asia; "strengthen the ability to build software- and AI-driven solutions"; a new market with an estimated SAM of "at least USD300 million by 2030".
  - Rigaku describes its process-control business as having "robust revenue growth of approximately 20% on an annual basis".
  - Inference: the standstill plus "consultations… regarding the Company's capital policy" after the lock-up leave a possible further transaction open. This is speculation, not a disclosed plan.
- **Could not verify:** the price Onto paid (not stated on pages 1-3 of the notice); the length of the lock-up; whether Atom Investment is a Carlyle vehicle (Carlyle is named as the seller of Tescan to Shimadzu [SH-TES], but Atom's sponsor is not named in Rigaku's notices); medium-term plan targets.

---

### 1.5 Horiba (6856)

**Takeaway.**
- In profit terms Horiba has become a semiconductor-component company. Materials & Semiconductor (mass-flow controllers plus scientific instruments) was 56% of 1H sales and about 99% of operating profit, at a 30% margin.
- 2026 operating profit is guided up 32%, and the MLMAP2028 targets were raised (operating profit ¥90bn, ROE 14%).
- Shareholder returns are rising: payout ratio 40% from 2027, and ¥790 per share for 2026 including a special and a commemorative dividend.
- Q3 results are due 13 Nov 2026.

**Latest results and guidance**
- **1H FY12/26 (January to June 2026; reported 7 Aug 2026; revised 12 Aug 2026)** [HO-1H]:
  - Sales ¥179,853m (+20.8%).
  - Operating profit ¥30,488m (+39.3%; 17.0%); ordinary profit ¥31,419m.
  - Net profit ¥21,806m (+37.5%); EPS ¥519.15.
  - Q2 alone: sales ¥95,323m; operating profit ¥18,007m (18.9%) [HO-1H p.15].
- **Segments, 1H** [HO-1H]:

| Segment | Sales | Operating profit (margin) |
|---|---|---|
| Energy & Environment | ¥58,383m (+7.5%) | ¥1,079m |
| Bio & Healthcare | ¥21,513m (+14.1%) | -¥767m |
| Materials & Semiconductor | ¥99,956m (+31.9%) | ¥30,176m (+33.9%; 30.2%) |

  - In Q2, Materials & Semiconductor operating profit was ¥18,743m on sales of ¥55,794m (33.6%) [HO-1H p.15].
- **FY12/26 guidance, raised 7 Aug** [HO-1H p.13]:
  - Sales ¥382,000m (+14.7%); operating profit ¥70,000m (+32.0%; 18.3%).
  - Net profit ¥50,000m (+34.8%); EPS ¥1,189.87.
  - By segment:

| Segment | Sales | Operating profit |
|---|---|---|
| Materials & Semiconductor | ¥205,000m (+31.0%) | ¥61,500m (30.0%) |
| Energy & Environment | ¥134,000m | ¥9,000m |
| Bio & Healthcare | ¥43,000m | -¥500m |

  - FX assumptions ¥155/US$ and ¥180/€.
  - Implied 2H operating profit ¥39.5bn (19.5%) [HO-1H p.15].
- **Dividend FY12/26** [HO-1H]:
  - ¥790 per share, against ¥450 for FY12/25.
  - Made up of ¥150 interim and ¥640 year-end. The year-end amount is ¥210 ordinary, ¥190 special and ¥240 commemorative, the last "to mark the milestone of the Company's market capitalization exceeding 1 trillion yen".
- Q3 (January to September) results are due 13 Nov 2026 [Y-6856].

**Test c: revenue model**
- The share of service and consumables revenue is not disclosed in the documents read.
- MLMAP2028 refers to combining "core technologies, production capacity, customer network, and service/maintenance capabilities" [HO-MLMAP].

**Test d: financial strength**
- **Five-year trend (StockAnalysis/S&P; fiscal years ending December)** [SA-F-6856] [SAR-6856]:

| FY | Revenue | Gross margin | Operating margin | FCF | ROE | ROIC |
|---|---|---|---|---|---|---|
| FY12/21 | ¥224.3bn | 41.6% | 14.3% | ¥23.1bn | 11.1% | 15.8% |
| FY12/22 | ¥270.1bn | 43.2% | 17.0% | ¥22.3bn | 15.3% | 21.0% |
| FY12/23 | ¥290.6bn | 43.8% | 16.3% | ¥7.8bn | 15.4% | 18.9% |
| FY12/24 | ¥317.4bn | 43.1% | 15.2% | ¥22.2bn | 11.2% | 15.1% |
| FY12/25 | ¥333.1bn | 43.9% | 15.9% | ¥29.1bn | 11.2% | 16.0% |
| TTM | ¥364.0bn | 44.1% | 16.9% | | 12.7% | 17.4% |

- **R&D and capex** [HO-1H p.14] (percentages my calc):
  - R&D: ¥24,688m in FY12/25 (7.4% of sales); ¥13,441m in 1H FY12/26 (7.5%); ¥27,500m forecast for FY12/26 (7.2%).
  - Capex: ¥9,773m in 1H; ¥20,000m forecast for the year. Depreciation forecast ¥15,500m.
- **Balance sheet.** Equity ratio 67.1% at 30 Jun 2026. Net cash ¥108.1bn (debt ¥62.9bn) [HO-1H] [SA-6856].
- **Concentration, 1H by destination** [HO-1H p.14]:
  - Japan ¥44,237m (24.6%); Asia ¥80,758m (44.9%); Americas ¥22,456m (12.5%); Europe ¥32,400m (18.0%).
  - Materials & Semiconductor sales in Asia were ¥65,564m (+35.0%), 65.6% of the segment.
  - China is not split out.

**Test e: cycle, scenarios, export controls**
- **Cycle** [HO-1H]:
  - Materials & Semiconductor growth was "mainly due to an increase in sales to semiconductor production equipment manufacturers in Asia, driven by demand for advanced semiconductors for AI and data centers".
  - Energy & Environment: Europe -7.3%, with a slowdown in hydrogen-related markets. Automotive testing was steady in Japan and Asia on hybrid-vehicle development.
- **Scenario exposure (inference).** High profit gearing to semiconductor-equipment demand: about 99% of 1H operating profit came from Materials & Semiconductor. MFC capacity is being expanded "up to three times" at Fukuchiyama [HO-MLMAP], which raises operating leverage in both directions.

**Theme exposure**
- Scientific instruments (spectroscopy) sit inside Materials & Semiconductor alongside mass-flow controllers. The split between them is not disclosed.
- Automotive test (Energy & Environment) is about 32% of 1H sales; medical (Bio & Healthcare) about 12% (my calc).

**Medium-term plan and governance**
- **MLMAP2028 update, 7 Aug 2026** [HO-MLMAP]:
  - 2028 group targets raised: sales ¥460bn (initial ¥450bn); operating profit ¥90bn (¥80bn); net profit ¥62bn (¥55bn); ROE 14% (≥12%).
  - 2028 targets by field:

| Field | Sales (initial plan) | Operating profit (initial plan) |
|---|---|---|
| Materials & Semiconductors | ¥262bn (¥235bn) | ¥77bn (¥58.5bn) |
| Energy & Environment | ¥146bn (¥158bn) | ¥12.5bn (¥15.8bn) |
| Bio & Healthcare | ¥52bn (¥57bn) | ¥0.5bn (¥5.7bn) |

  - Structural reform of mechatronics (automotive test systems) overseas, hydrogen, and hematology.
  - Payout ratio raised from 30% to 40% from 2027; special dividends and buybacks "flexibly"; commemorative dividend of about ¥10bn.
  - Total shareholder return for 2024-2028 planned at ¥105.0bn, ¥37.0bn above the initial plan.
  - Considering a move to a Company with Audit & Supervisory Committee, with a majority of non-executive directors; subject to the AGM in March 2027.
- **Trading unit.** Horiba published its "Position and Policy regarding Reduction of Minimum Stock Trading Unit" on 27 Mar 2026 [HO-TDnet]. The content was not read.

---

### 1.6 Anritsu (6754)

**Takeaway.**
- Data-centre and optical test drove 1H orders up 60% and operating profit up 90%. Network Infrastructure is 55% of Test & Measurement (T&M) revenue, about 34% of group revenue.
- FY guidance was raised above the GLP2026 plan targets.
- Net cash is about ¥44-48bn, and the payout ratio is about 50%.
- Environmental Measurement (EV and battery test) is loss-making after a goodwill impairment.

**Latest results and guidance**
- **1H FY3/27 ("FY2026", April to September 2026; reported 29 Oct 2026; IFRS)** [AN-1H]:
  - Orders ¥87.8bn (+60%); revenue ¥69.3bn (+34%).
  - Operating profit ¥9.6bn (+90%; 13.9%).
  - Profit before tax ¥9.5bn; profit ¥6.6bn (+72%).
- **Segments, 1H** [AN-1H]:

| Segment | Revenue | Operating profit |
|---|---|---|
| Test & Measurement (T&M) | ¥42.1bn (+36%) | ¥8.7bn (+120%) |
| Products Quality Assurance (PQA; food and pharma inspection) | ¥17.0bn (+17%) | ¥2.2bn |
| Environmental Measurement | ¥7.0bn (+137%) | -¥1.3bn (includes ¥1.3bn impairment) |
| Others | ¥3.3bn | ¥1.1bn |

  - Q2 operating margins: T&M 24.4%; PQA 15.2%.
- **Orders by quarter:** Q1 ¥49.1bn; Q2 ¥38.8bn (Q2 FY3/26: ¥29.9bn) [AN-1H].
- **Guidance, raised 29 Oct** [AN-1H]:

| | Revised forecast | Previous forecast | FY3/26 actual |
|---|---|---|---|
| Revenue | ¥145.0bn (+23%) | ¥140.0bn | ¥117.5bn |
| Operating profit | ¥22.0bn (+48%) | ¥20.0bn | ¥14.8bn |
| Profit | ¥16.0bn | ¥15.0bn | ¥11.7bn |
| T&M (revenue / operating profit) | ¥90.0bn / ¥20.0bn | | |
| PQA | ¥34.0bn / ¥4.2bn | | |
| Environmental Measurement | ¥14.5bn / -¥1.2bn | ¥16.0bn / +¥1.0bn | |

  - FX assumptions ¥150/US$ and ¥175/€.
  - Dividend raised from ¥50 to ¥63 (¥25 interim + ¥38 year-end).
- **Management comments** [AN-1H]:
  - T&M: "Demand is strong, mainly related to data centers."
  - "Investments in the 5G development market are sluggish."
  - Aerospace and national-security demand continuing in North America and Japan; PCIe R&D demand strong.
  - PQA: X-ray inspection demand strong in the North American meat market.
  - Environmental Measurement: "Demand for test solutions for EV/battery is in an adjustment phase."
- **Share reaction.** The stock fell 11.7% from ¥3,120 (29 Oct close) to ¥2,754.5 on 30 Oct, after the results [YH-6754-d]. The reason was not verified.

**Test c: revenue model**
- The split of service and software revenue is not disclosed in the documents read.
- Inference: revenue is mostly instruments (T&M) and inspection equipment (PQA).

**Test d: financial strength**
- **Five-year trend (StockAnalysis/S&P; fiscal years ending March)** [SA-F-6754] [SAR-6754]:

| FY | Revenue | Gross margin | Operating margin | FCF | ROE | ROIC |
|---|---|---|---|---|---|---|
| FY3/22 | ¥105.4bn | 52.6% | 16.0% | ¥13.1bn | 11.5% | 17.8% |
| FY3/23 | ¥110.9bn | 48.7% | 10.6% | ¥2.0bn | 8.0% | 10.8% |
| FY3/24 | ¥110.0bn | 47.0% | 8.6% | ¥13.9bn | 6.3% | 8.6% |
| FY3/25 | ¥113.0bn | 48.7% | 10.6% | ¥18.6bn | 7.4% | 10.8% |
| FY3/26 | ¥117.5bn | 51.1% | 12.2% | ¥13.8bn | 9.1% | 12.5% |
| TTM | ¥135.1bn | 53.5% | 14.3% | | 11.1% | 15.9% |

- **1H cash.** Operating cash flow ¥8.8bn; free cash flow ¥6.5bn; cash ¥51.3bn; interest-bearing debt ¥7.0bn [AN-1H]. StockAnalysis shows net cash of ¥47.8bn [SA-6754].
- **Shareholder returns.** Payout ratio 50.4% (FY3/27 forecast). A chart shows ¥5.0bn buybacks in three periods. The total return ratio under GLP2023 was 87.5% [AN-1H p.13].
- **Concentration** [AN-1H]:
  - T&M revenue by region, 1H: Japan 11%; Asia & Others 48%; Americas 25%; EMEA 16%.
  - Group revenue in Q2: Japan ¥9.8bn; Americas ¥8.6bn; EMEA ¥4.4bn; Asia & Others ¥13.9bn.
  - China is not split out.
- R&D could not be verified.

**Test e: cycle, scenarios**
- **Cycle.**
  - Network Infrastructure rose from 39% of T&M revenue (FY3/26) to 55% (1H FY3/27) [AN-1H].
  - Production of 1.6TE optical transceivers is "expected to gain full steam in the second half of 2026" [AN-FY25 p.16].
  - Mobile (5G) R&D spending is sluggish.
  - Anritsu's roadmap shows 6G investment (Release 20) from about 2028 [AN-1H p.15].
- **Scenario exposure (inference).** High exposure to AI data-centre capex through optical and PCIe test. A partial offset could come from a 6G R&D cycle starting around 2028-29 (company roadmap), and from PQA and aerospace/national-security demand.

**Theme exposure**
- T&M (electronic test equipment) was 61% of 1H revenue [AN-1H].
- At CEATEC 2026 Anritsu showed an "AI-enabled vector network analyzer that derives optimal measurement methods" [AN-1H p.18].

**Medium-term plan and governance**
- **GLP2026 (FY2024 to FY2026; FY2026 = FY3/27)** [AN-FY25 p.15]:

| Target | Original plan | Revised plan (April 2026) |
|---|---|---|
| Group revenue | ¥140.0bn | ¥140.0bn |
| Group operating profit | ¥20.0bn (14%) | ¥20.0bn (14%) |
| Group profit | ¥15.0bn | ¥15.0bn |
| ROE | 12% | 12% |
| T&M (revenue / operating profit) | ¥90bn / ¥15bn (17%) | ¥85bn / ¥16.5bn (19%) |
| PQA | ¥30bn / ¥3.6bn | ¥33bn / ¥4.0bn |
| Environmental Measurement | ¥13bn / ¥1.4bn | ¥16bn / ¥1.0bn |

  - The October 2026 guidance (¥145bn revenue, ¥22bn operating profit) exceeds the group targets.
- **FY2030 revenue targets:** industrial measurement ¥50bn; pharmaceutical (healthcare) ¥10bn. Anritsu signed a sales agreement with TTi (UK) in April 2026 [AN-FY25 p.18].
- **Acquisition.** Anritsu completed an additional purchase of shares in an equity-method affiliate, making it a consolidated subsidiary, on 28 Oct 2026 (first announced 31 Mar 2026) [AN-TDnet]. The company's name could not be verified. Inference: the 137% rise in Environmental Measurement revenue fits a consolidation.
- **Next plan (inference).** GLP2026 ends with FY3/27, so a new plan would be expected around the FY3/27 results.

---

### 1.7 Lasertec (6920)

**Takeaway.**
- Lasertec has the strongest financial profile of the group: operating margin 46%, ROE 34%, ROIC 54%, no debt and ¥110.8bn of cash.
- It has a single segment and is fully geared to leading-edge semiconductor capex (EUV mask and blank inspection).
- Q1 FY6/27 sales fell 25.5%, but forward indicators turned up sharply:
  - Customer advances rose by ¥42.8bn in the quarter.
  - Production at sales prices rose 120%.
  - Management says the FY2027 order outlook "exceeded previous expectations".
- Services are now 40% of quarterly sales.

**Latest results and guidance**
- **Q1 FY6/27 (July to September 2026; reported 30 Oct 2026)** [LT-Q1]:
  - Sales ¥40,369m (-25.5%).
  - Gross profit ¥24,035m (59.5%).
  - Operating profit ¥15,769m (-41.0%; 39.1%).
  - Ordinary profit ¥14,711m, after a foreign-exchange loss of ¥1,260m.
  - Net profit ¥10,734m (-43.7%); EPS ¥119.72.
- **By category** [LT-Q1]: semiconductor-related products ¥23,849m (-42.9%); other products ¥508m; services ¥16,011m (+31.2%).
- **By customer location, Q1** [LT-Q1 p.9]:

| Location | Q1 FY6/27 | Q1 FY6/26 |
|---|---|---|
| USA | ¥14,354m (35.6%) | ¥22,005m |
| Taiwan | ¥9,304m (23.0%) | ¥6,059m |
| Korea | ¥6,933m (17.2%) | ¥14,463m |
| Asia (other) | ¥6,015m (14.9%) | |
| Europe | ¥2,020m (5.0%) | |
| Japan | ¥1,741m (4.3%) | |

- **Production at sales prices, Q1:** semiconductor-related ¥72,326m (+120.2%); total ¥89,527m (+95.5%) [LT-Q1 p.10].
- **Balance sheet at 30 Sep 2026** [LT-Q1]:
  - Work in process ¥138,050m (+¥15.6bn in the quarter).
  - Advances received ¥87,075m (from ¥44,284m).
  - Cash ¥110,768m; equity ratio 65.4%.
  - Q1 operating cash flow ¥39,102m.
- **FY6/27 guidance (unchanged since 6 Aug 2026)** [LT-Q1] [LT-FY26]:
  - Sales ¥290,000m (+25.8%).
  - Operating profit ¥125,000m (+18.8%; 43.1%).
  - Net profit ¥90,000m (+16.2%).
  - EPS ¥1,003.27 on the Q1 share count (¥1,004.12 in August).
  - Dividend ¥351 per share.
- **Management comment** [LT-Q1]: demand for CPUs, GPUs and HBM "has remained high due to robust investment in AI data centers, and device manufacturers have further expanded their capital investment plans… the outlook for orders in FY2027 has exceeded previous expectations".
- **FY6/26 (July 2025 to June 2026; reported 6 Aug 2026)** [LT-FY26]:
  - Sales ¥230,485m (-8.3%).
  - Operating profit ¥105,259m (-14.3%; 45.7%).
  - Net profit ¥77,485m (-8.5%); ROE 33.9%.
  - Operating cash flow ¥48,540m.
  - Dividend ¥329 per share (payout ratio 38.1%).
- **Orders and backlog.** A secondary site, seen only through a search snippet, gives FY6/26 orders of ¥237.5bn and a backlog of ¥322.9bn [GD-LT]. This is not verified in primary filings; the 決算短信 no longer shows orders.
- **Discarded figure.** A search-snippet claim of FY6/26 sales of ¥308.1bn is wrong. The primary filing shows ¥230.5bn, which StockAnalysis's TTM figure of ¥216.7bn corroborates.

**Test c: revenue model**
- Services were ¥16,011m, 39.7% of Q1 FY6/27 sales (22.5% a year earlier) [LT-Q1 p.9] (my %).
- Revenue recognised over time was ¥12,097m (30.0%).
- The services share for a full year could not be verified.

**Test d: financial strength**
- **Five-year trend (StockAnalysis/S&P; fiscal years ending June)** [SA-F-6920] [SAR-6920]:

| FY | Revenue | Gross margin | Operating margin | FCF | ROE | ROIC |
|---|---|---|---|---|---|---|
| FY6/22 | ¥90.4bn | 52.9% | 36.0% | -¥4.2bn | 38.9% | 55.6% |
| FY6/23 | ¥152.8bn | 55.0% | 40.8% | ¥21.8bn | 50.8% | 62.9% |
| FY6/24 | ¥213.5bn | 50.3% | 38.1% | ¥30.3bn | 45.4% | 59.4% |
| FY6/25 | ¥251.5bn | 59.0% | 48.9% | ¥75.8bn | 46.9% | 73.5% |
| FY6/26 | ¥230.5bn | 59.2% | 45.7% | ¥47.0bn | 33.9% | 54.2% |
| TTM | | | | ¥80.0bn | | |

- **Balance sheet.** No interest-bearing debt; cash ¥110.8bn [LT-Q1] [SA-6920].
- **Shareholder returns and R&D.**
  - Payout ratio about 35% planned for FY6/27 [LT-FY26].
  - R&D could not be verified.
- **Concentration.**
  - The top three customer locations made up 76% of Q1 sales (see table above).
  - The names of major customers are in the 有価証券報告書, which was not read.

**Test e: cycle, scenarios, export controls**
- **Cycle (inference from [LT-Q1]).** Product sales were at a trough in Q1 FY6/27, but advances, work in process and production all show an upturn in orders.
- **Scenario exposure (inference).**
  - Highest in the group.
  - A financing-led pause around 2028 would hit orders in 2027-28.
  - The large service base (40% of Q1 sales) cushions a downturn.
  - Acceleration offers upside limited by capacity.
- **Export controls.** "Asia (other)", which includes China but is not split, was 14.9% of Q1 sales.

**Theme exposure.** 100%: a single segment of inspection and measurement systems [LT-Q1 p.8].

**Medium-term plan and governance**
- No numeric medium-term plan was found. An IR page titled "経営戦略" exists but was not read.
- Disclosures [LT-TDnet]:
  - "Our Views and Policy on Lowering the Minimum Investment Unit" (25 Sep 2026).
  - Organisational changes (25 Sep 2026).
  - New MATRICS X712 mask-defect inspection product (31 Mar 2026).

---

### 1.8 Cross-company quality snapshot (test d)

| Metric | JEOL | Hitachi (group) | Shimadzu | Rigaku | Horiba | Anritsu | Lasertec |
|---|---|---|---|---|---|---|---|
| Operating margin, latest FY | 14.5% (FY3/26) | adj. EBITA 13.0% (FY3/27E) | 13.1% (FY3/26) | 18.4% (FY12/25) | 15.9% (FY12/25) | 12.2% (FY3/26) | 45.7% (FY6/26) |
| Gross margin, TTM (SA) | 46.3% (FY) | 30.2% | 45.3% | 57.1% | 44.1% | 53.5% | 58.9% |
| ROE, latest FY | 15.7% | 13.3% | 11.4% | 13.4% | 11.2% | 9.1% | 33.9% |
| ROIC, latest FY (SA) | 16.1% | 14.4% | 13.9% | 10.2% | 16.0% | 12.5% | 54.2% |
| Net cash (+) / net debt (−) | +¥18.0bn | +¥482bn (my calc) | +¥15.4bn | −¥39.7bn | +¥108.1bn | +¥47.8bn | +¥110.8bn |
| Equity ratio | 62.3% (Jun 26) | ~43% | 66.8% | n/v | 67.1% | n/v | 65.4% |
| FCF, latest | ~¥0.9bn (FY3/26) | ¥677bn (1H) | ~¥20.7bn pre-M&A (1H) | ¥5.6bn (TTM) | ¥30.8bn (TTM) | ¥6.5bn (1H) | ¥80.0bn (TTM) |
| China share of sales | 19.9% | n/d (Asia 20%) | 16.9% | ~13% (Q3, approx.) | n/d (Asia 44.9%) | n/d | n/d ("Asia other" 14.9%) |
| R&D / sales | n/v | n/v | n/v | n/v | 7.4% (FY12/25) | n/v | n/v |

Key: n/v = could not verify; n/d = not disclosed. Sources are as in sections 1.1-1.7.

### 1.9 Exposure to the three AI-spending scenarios to 2030 (my inference)

The scenarios are those given in the brief: steady growth (~55%), a financing-led pause around 2028 (~25%), and faster acceleration (~20%). The basis column gives the main reason for each rating.

| Company | Basis (verified shares) | Steady growth | Pause around 2028 | Acceleration |
|---|---|---|---|---|
| Lasertec | 100% semiconductor inspection; services 40% of Q1 sales | positive | strongly negative (orders and margins) | strongly positive, capacity-limited |
| Horiba | Materials & Semiconductor ≈99% of 1H operating profit | positive | strongly negative for profit | positive |
| JEOL | Industrial Equipment ≈60% of segment profit; 34% of it sold to China | positive | negative | positive |
| Rigaku | Semiconductor Process Control ≈30% of revenue, >50% of FY operating profit | positive | negative | strongly positive |
| Anritsu | Network Infrastructure ≈34% of group revenue | positive | negative, partly offset by the 6G cycle from ~2028 | positive |
| Shimadzu | Industrial Machinery 16% of sales, 22% of segment profit | mildly positive | mildly negative | mildly positive |
| Hitachi (Measurement & Analysis Systems) | <10% of group | positive at segment level, small at group level | negative at segment level, small at group level | positive at segment level |

---

## Part 2. Comparison rows (compact)

Prices are 12 Nov 2026 closes. P/E is shown as trailing / consensus forward (StockAnalysis), followed by Yahoo's PER on the company forecast.

| Company | Price; mkt cap | P/E | P/B | EV/EBITDA | Yield | ROE; op. margin | Net cash | 52-wk change; 2026 high/low | Latest results (Yahoo summary of 決算短信) |
|---|---|---|---|---|---|---|---|---|---|
| Advantest (6857) | ¥29,985 (-4.63% on day); ¥21.65tn | 38.06 / 24.45; co. 29.24 | 19.58 | 29.59 | 0.33% | 65.4%; 49.8% | ¥294.5bn | +50.9%; ¥41,990 (7 Oct) / ¥19,720 (31 Mar) | 1H FY3/27 (28 Oct): revenue ¥845.2bn (+60.5%); OP ¥456.8bn (+96.5%); net ¥368.0bn (+116.8%) [SA-6857] [Y-6857] |
| Hamamatsu Photonics (6965) | ¥2,205 (-6.47%); ¥635.5bn | 32.46 / 31.41; co. 28.88 | 1.97 | 12.45 | 1.72% (SA) / 1.81% (Yahoo) | 6.2%; 11.2% | ¥14.9bn | +32.8%; ¥3,100 (25 May) / ¥1,620 (6 Feb) | FY9/26 (10 Nov): sales ¥243.3bn (+14.8%); OP ¥27.18bn (+68.2%); FY9/27 EPS forecast ¥76.34, DPS ¥40 [SA-6965] [Y-6965] |
| JTEC (3446) | ¥1,168 (-9.74%); ¥6.91bn | 118.8 / 88.6; co. 114.96 | 2.42 | 28.51 | none | 2.1%; 3.7% | ¥0.1bn | -20.9%; ¥2,514 (17 Feb) / ¥1,089 (6 Nov) | Results 12 Nov 2026 (period not stated on page): sales ¥158m (-32.1%); operating loss ¥215.3m; "customer acceptance delays" in optics [SA-3446] [Y-3446] |
| Yokogawa Electric (6841) | ¥4,245 (+1.14%); ¥1.06tn | 20.74 / 15.42; co. 17.65 | 2.08 | 8.57 | 2.17% (DPS ¥92) | 10.9%; 12.8% | ¥166.3bn | -7.5%; ¥6,317 (27 Feb) / ¥3,705 (6 Nov) | 1H FY3/27 (4 Nov): sales ¥298.2bn (+5.8%); OP ¥35.73bn (-8.4%); net ¥23.06bn (-21.5%) [SA-6841] [Y-6841] |
| Tokyo Seimitsu (7729) | ¥13,290 (-1.52%); ¥539.4bn | 17.72 / 14.69; co. 16.86 | 2.70 | 10.88 | 2.38% (DPS ¥316) | 16.1%; 21.6% | ¥57.4bn | +23.4%; ¥21,310 (1 Jul) / ¥9,922 (6 Nov) | 1H FY3/27 (4 Nov): sales ¥92.39bn (+19.9%); OP ¥20.34bn (+38.2%); net ¥15.48bn (+61.1%) [SA-7729] [Y-7729] |

Notes on the comparison rows:
- Yahoo's AI commentary attributes Advantest's 12 Nov fall to "reports about an Nvidia CEO departure" [Y-6857]. This is not verified, and the commentary is machine-generated.
- JTEC's fiscal-year basis is unclear: Yahoo shows its forecasts under "2027/03".

---

## Part 3. Valuation and entry point (kept separate from quality)

### 3.0 Method notes
- Prices are 12 Nov 2026 TSE closes.
- PER on the company forecast comes from Yahoo!ファイナンス [Y-xxxx].
- Trailing P/E, consensus forward P/E, P/B, EV, EV/EBITDA and net cash come from StockAnalysis statistics pages [SA-xxxx], with data from S&P Global.
- History uses five fiscal-year-end points from StockAnalysis ratios pages [SAR-xxxx]. The "median" is the median of those five year-end values, not a daily median.
- Ten-year ranges were not available; the free view shows five years.
- StockAnalysis does not say which fiscal year its "forward P/E" uses. The EPS it implies is 5-48% above company guidance (table 3.5), which suggests a next-fiscal-year or next-twelve-months basis.

### 3.1 Snapshot, 12 Nov 2026

| Company | Price | Mkt cap (SA; Yahoo incl. treasury) | EV (SA) | P/E trailing (SA) | PER co. forecast (Yahoo; FY) | P/E consensus fwd (SA) | P/B | EV/EBITDA (SA) | Div. yield |
|---|---|---|---|---|---|---|---|---|---|
| JEOL | ¥6,680 | ¥325.4bn; ¥344.2bn | ¥307.4bn | 21.45 | 15.27 (FY3/27) | 13.58 | 2.36 (SA) / 2.31 (Yahoo) | 12.94 | 1.98% |
| Hitachi | ¥4,981 | ¥22.34tn; ¥22.59tn | ¥21.60tn | 30.02 | 24.20 (FY3/27) | 19.84 | 3.33 / 3.39 | 11.71 | 1.12% (SA) |
| Shimadzu | ¥4,594 | ¥1.33tn; ¥1.36tn | ¥1.31tn | 20.38 | 21.76 (FY3/27) | 20.71 | 2.28 / 2.29 | 13.00 | 1.57% |
| Rigaku | ¥1,348 | ¥305.3bn; ¥305.5bn | ¥345.5bn | 33.39 | 24.41 (FY12/26) | 19.91 | 3.60 / 3.51 | 18.35 (SA, possibly stale TTM); ~16.8 (my calc with TTM EBITDA ~¥20.6bn) | 1.41% |
| Horiba | ¥20,385 | ¥856.6bn; ¥860.9bn | ¥748.6bn | 19.99 | 17.12 (FY12/26) | 14.76 | 2.35 | 9.77 | 3.88% (Yahoo, incl. special and commemorative ¥790); 2.70% (SA, trailing); ordinary only ~1.77% (my calc, (¥150+¥210)/price) |
| Anritsu | ¥2,396.5 | ¥306.8bn; ¥325.6bn | ¥259.0bn | 21.27 | 19.17 (FY3/27) | 16.59 | 2.37 / 2.28 | 10.51 | 2.63% |
| Lasertec | ¥36,380 | ¥3.26tn; ¥3.43tn | ¥3.15tn | 47.20 | 36.24 (FY6/27) | 24.56 | 13.63 | 31.98 | 0.96% |

Rigaku TTM EBITDA (my calc): ¥9.1bn for 1-3Q FY12/26 plus ¥11.5bn for Q4 FY12/25 (¥21.8bn for FY12/25 minus ¥10.3bn for 1-3Q FY12/25) gives ¥20.6bn [RG-3Q].

### 3.2 Against each company's own five-year history (fiscal-year-end values from [SAR-xxxx])

| Company (FY ends) | P/E range; median | Current P/E (TTM / co. fwd) | P/B range; median | Current P/B | EV/EBITDA range; median | Current EV/EBITDA |
|---|---|---|---|---|---|---|
| JEOL (Mar 22-26) | 12.16-28.54; 12.65 | 21.45 / 15.27 | 1.71-4.08; 2.13 | 2.36 | 5.16-18.11; 8.04 | 12.94 |
| Hitachi (Mar 22-26) | 10.22-25.71; 21.84 | 30.02 / 24.20 | 1.11-2.97; 2.20 | 3.33 | 6.39-11.81; 10.83 | 11.71 |
| Shimadzu (Mar 22-26) | 17.62-26.39; 21.86 | 20.38 / 21.76 | 1.89-3.27; 2.53 | 2.28 | 9.91-13.97; 12.21 | 13.00 |
| Rigaku (Dec 24-25 only) | 15.22, 24.25 | 33.39 / 24.41 | 2.53, 3.13 | 3.60 | 10.41, 14.08 | 18.35 |
| Horiba (Dec 21-25) | 7.10-18.07; 11.57 | 19.99 / 17.12 | 1.00-1.92; 1.40 | 2.35 | 3.08-8.66; 5.55 | 9.77 |
| Anritsu (Mar 22-26) | 16.38-30.01; 18.96 | 21.27 / 19.17 | 1.30-2.64; 1.41 | 2.37 | 7.06-15.29; 7.46 | 10.51 |
| Lasertec (Jun 22-26) | 20.68-58.61; 55.10 | 47.20 / 36.24 | 8.34-21.51; 18.05 | 13.63 | 13.31-39.81; 37.46 | 31.98 |

Reading (my inference):
- **Above own median on all three measures:** Horiba, Anritsu, JEOL (on EV/EBITDA and P/B; P/E is above on the company forecast) and Hitachi.
- **About at median:** Shimadzu.
- **Below own median on all three:** Lasertec. Its five-year history includes the 2022-24 EUV boom multiples.
- Ten-year ranges: could not verify.

### 3.3 Closest global peers (StockAnalysis statistics; US prices are 11 Nov 2026 closes, Oxford Instruments and Japanese peers 12 Nov)

| Peer | Price; mkt cap | P/E trailing / fwd | P/B | EV/EBITDA | Yield | Op. margin | ROIC | 3-yr EPS growth forecast |
|---|---|---|---|---|---|---|---|---|
| Thermo Fisher (TMO) | $717.71; $265.9bn | 37.83 / 26.65 | 4.86 | 24.83 | 0.26% | 19.1% | 9.0% | 10.4% [SA-TMO] |
| Agilent (A) | $176.95; $49.9bn | 34.89 / 26.93 | 6.78 | 25.13 | 0.58% | 24.5% | 16.9% | 10.2% [SA-A] |
| Bruker (BRKR) | $62.41; $9.53bn | n/a (loss) / 26.52 | 4.17 | 20.24 | 0.32% | 9.2% | 8.0% | 15.8% [SA-BRKR] |
| Oxford Instruments (OXIG, London) | 2,626p; £1.43bn | 26.85 / 21.75 | 4.42 | 14.81 | 0.90% | 17.3% | 20.5% | 14.6% [SA-OXIG] |
| KLA (KLAC) | $161.01; $209.8bn | 40.36 / 25.91 | 32.17 | 32.07 | 0.57% | 42.6% | 69.1% | 30.8% [SA-KLAC] |
| Onto Innovation (ONTO) | $215.06; $10.56bn | 70.63 / 17.93 | 5.33 | 27.34 | none | 22.7% | 12.7% | 46.2% [SA-ONTO] |
| Keysight (KEYS) | $305.64; $52.0bn | 41.98 / 22.61 | 7.92 | 30.74 | none | 19.8% | 17.6% | 30.2% [SA-KEYS] |
| Advantest (Japan) | ¥29,985; ¥21.65tn | 38.06 / 24.45 | 19.58 | 29.59 | 0.33% | 49.8% | 65.4% | 48.3% [SA-6857] |
| Tokyo Seimitsu (Japan) | ¥13,290; ¥539.4bn | 17.72 / 14.69 | 2.70 | 10.88 | 2.38% | 21.6% | 27.1% | 23.5% [SA-7729] |
| Hamamatsu (Japan) | ¥2,205; ¥635.5bn | 32.46 / 31.41 | 1.97 | 12.45 | 1.72% | 11.2% | 5.6% | 12.6% [SA-6965] |
| Yokogawa (Japan) | ¥4,245; ¥1.06tn | 20.74 / 15.42 | 2.08 | 8.57 | 2.17% | 12.8% | 23.0% | 12.4% [SA-6841] |

Notes:
- KLA's $161 share price implies a split since 2025. I did not verify one, and the market cap of $209.8bn is consistent.

Reading (my inference):
- **Analytical makers.** The median forward P/E of TMO, A, BRKR and OXIG is about 26.6, and their median EV/EBITDA about 22.5 (my calc). JEOL (13.6 / 12.9), Shimadzu (20.7 / 13.0), Horiba (14.8 / 9.8) and Anritsu (16.6 / 10.5) trade at roughly 20-50% lower forward P/E and 40-60% lower EV/EBITDA. Their margins are also lower: operating margins of 12-17%, against 19-25% at Thermo Fisher and Agilent.
- **Metrology.** Lasertec (EV/EBITDA 32.0) is in line with KLA (32.1) on EV/EBITDA. Rigaku (fwd P/E 19.9; EV/EBITDA 16.8-18.4) is close to Onto on P/E (17.9) and cheaper on EV/EBITDA (27.3).
- **Electronic test.** Anritsu's EV/EBITDA (10.5) is about a third of Keysight's (30.7).

### 3.4 Share-price performance (price only, no dividends)

Method: reference prices are monthly closes from Yahoo!ファイナンス history pages [YH-xxxx]. YTD is measured against the December 2025 close; "about 3 years" against the November 2023 close; "about 5 years" against the November 2021 close (Hitachi's split-adjusted close). The 1-year figure is StockAnalysis's 52-week change. The 2026 high/low is Yahoo's 年初来高値/安値 (calendar year to date, not trailing 52 weeks).

| Company | 12 Nov 2026 | YTD | 1 yr | ~3 yr | ~5 yr | 2026 high (date) | 2026 low (date) |
|---|---|---|---|---|---|---|---|
| JEOL | ¥6,680 | +32.8% (from ¥5,031) | +29.9% | +14.0% (from ¥5,862) | -29.5% (from ¥9,470) | ¥9,255 (14 Aug) | ¥5,000 (5 Jan) |
| Hitachi | ¥4,981 | +1.6% (from ¥4,902) | -2.7% | +142.2% (adj. ¥2,057) | +272.4% (adj. ¥1,337.6) | ¥6,039 (10 Feb) | ¥4,301 (6 Nov) |
| Shimadzu | ¥4,594 | +10.2% (from ¥4,168) | +7.8% | +19.8% (from ¥3,835) | -4.5% (from ¥4,810) | ¥4,709 (11 Nov) | ¥3,388 (13 May) |
| Rigaku | ¥1,348 | +9.9% (from ¥1,227) | +39.6% | n/a (listed Oct 2024) | n/a | ¥3,400 (3 Jun) | ¥1,085 (6 Nov) |
| Horiba | ¥20,385 | +27.7% (from ¥15,960) | +50.6% | +104.7% (from ¥9,957) | +202.0% (from ¥6,750) | ¥30,100 (19 Jun) | ¥16,180 (5 Jan) |
| Anritsu | ¥2,396.5 | +6.8% (from ¥2,244.5) | +6.8% | +86.7% (from ¥1,283.5) | +35.8% (from ¥1,765) | ¥4,855 (3 Jun) | ¥2,060 (6 Nov) |
| Lasertec | ¥36,380 | +22.7% (from ¥29,645) | +26.2% | +10.1% (from ¥33,040) | +22.3% (from ¥29,745) | ¥58,580 (19 Jun) | ¥28,660 (5 Feb) |

- **True 52-week lows may be lower** than the 2026 lows for Lasertec (monthly lows of ¥25,590 in November 2025 and ¥27,515 in December 2025) and Rigaku (¥886 and ¥935) [YH-6920-m] [YH-268A-m]. The exact dates of those lows were not verified.
- **Recent daily moves (Yahoo daily history):**

| Company | Recent closes |
|---|---|
| JEOL | ¥6,700 (4 Nov) → ¥6,106 (6 Nov) → ¥6,680 (12 Nov) |
| Hitachi | ¥5,620 (28 Oct) → ¥5,071 (29 Oct, the day after results) → ¥4,542 (6 Nov) → ¥4,981 |
| Lasertec | ¥41,340 (29 Oct) → ¥37,700 (30 Oct, results day) → ¥32,040 (6 Nov) → ¥36,380 |
| Horiba | ¥20,885 (4 Nov) → ¥18,025 (6 Nov) → ¥20,385 |
| Shimadzu | ¥4,393 (5 Nov) → ¥4,170 (6 Nov, results day) → ¥4,594 |

### 3.5 Consensus expectations (StockAnalysis/S&P)

| Company | Implied consensus EPS (price ÷ fwd P/E) vs co. forecast | Revenue / EPS growth forecast, 3 yr (annual) | Analyst target; count; rating |
|---|---|---|---|
| JEOL | ¥492 vs ¥433 (+14%) | n/v | ¥8,720; 5; Buy [SA-6951] |
| Hitachi | ¥251 vs ¥206 (+22%) | 9.4% / 20.6% | ¥6,544; 16; Buy |
| Shimadzu | ¥222 vs ¥211 (+5%) | 7.7% / 7.5% | ¥5,193; 12; Buy |
| Rigaku | ¥67.7 vs ¥55.3 (+22%) | 11.3% / 20.6% | ¥2,140; 5; Hold |
| Horiba | ¥1,381 vs ¥1,190 (+16%) | 12.2% / 24.4% | ¥29,000; 7 |
| Anritsu | ¥144.5 vs ¥125.0 (+16%) | 14.6% / 27.4% | ¥3,763; 9; Buy |
| Lasertec | ¥1,481 vs ¥1,003 (+48%) | 27.6% / 29.9% | ¥49,269; 17; Buy |

- Year-by-year consensus revenue and profit for the next two fiscal years could not be verified; only the three-year growth rates and forward P/E above were available.

### 3.6 What the price implies (my own estimates; arithmetic shown)

**(a) Steady-state "value-driver" check.**
- Formula: forward P/E = (1 − g/ROE) / (r − g). Solving for growth gives g = (P/E × r − 1) / (P/E − 1/ROE).
- Inputs: P/E is the PER on the company forecast. ROE is as shown in the table. r is my assumed yen cost of equity, 8%, with ±1-point sensitivity.

| Company | P/E (co. fcst) | ROE used | Implied perpetual growth at r = 7% / 8% / 9% |
|---|---|---|---|
| JEOL | 15.44 (¥6,680 / ¥432.64) | 15.7% (FY3/26) | 0.9% / 2.6% / 4.3% |
| Horiba | 17.13 | 13% (TTM 12.7%; plan 14%) | 2.1% / 3.9% / 5.7% |
| Anritsu | 19.17 | 12% (GLP2026 target) | 3.2% / 4.9% / 6.7% |
| Shimadzu | 21.75 | 12% | 3.9% / 5.5% / 7.1% |
| Hitachi | 24.13 | 13% | 4.2% / 5.7% / 7.1% |
| Lasertec | 36.26 | 33.9% (FY6/26) | 4.6% / 5.7% / 6.8% |
| Rigaku | 24.39 | 12% | 4.4% / 5.9% / 7.4% |

Worked example (JEOL at r = 8%): (15.44 × 0.08 − 1) / (15.44 − 1/0.157) = 0.2352 / 9.071 = 2.6%.

**(b) Exit-multiple check.**
- Question: what EPS growth is needed so that, five years after the forecast year, the stock trades at its five-year median P/E while earning an 8% total return?
- Required price growth is (8% − dividend yield) a year.
- Required EPS in year 5 = price × (1.08 − yield)^5 ÷ exit P/E.
- Required EPS growth = (required EPS ÷ forecast EPS)^(1/5) − 1.

| Company | Required EPS in yr 5 | Exit P/E | Required EPS growth (annual) | Cross-check |
|---|---|---|---|---|
| JEOL | ¥707 (¥6,680 × 1.0602^5 = ¥8,948, ÷ 12.65) | 12.65 (median) | 10.3% | Plan FY3/30 net profit ¥33.8bn ≈ EPS ¥694 at 48.7m shares (my calc). The price roughly discounts delivery of the plan, about two years late. |
| Shimadzu | ¥287 | 21.86 (median) | 6.3% | Consensus 3-yr EPS growth 7.5% |
| Hitachi | ¥318 | 21.84 (median) | 9.0% | Consensus 3-yr EPS growth 20.6% |
| Horiba | ¥2,384 at 11.57x / ¥1,838 at 15x | 11.57 (median) / 15 | 14.9% / 9.1% | MLMAP2028 net profit ¥62bn ≈ EPS ¥1,475 (42.02m shares), 11.3% a year from 2026 to 2028 |
| Anritsu | ¥164 | 18.96 (median) | 5.6% | Consensus 3-yr EPS growth 27.4%, which includes the FY3/27 jump |
| Lasertec | ¥2,045 at 25x / ¥1,704 at 30x | 25-30 (≈KLA; the median of 55 is not used) | 15.3% / 11.2% | Consensus 3-yr EPS growth 29.9% |
| Rigaku | ¥92.7 | 20 (no five-year history) | 10.9% | Consensus 3-yr EPS growth 20.6% |

**(c) Margins the price assumes (inference).**
- **Lasertec.** The price assumes operating margins of about 43-46% (FY6/27 guidance 43.1%) and 11-15% EPS growth, i.e., near-peak margins sustained.
- **Horiba.** The price at about 17x 2026 EPS assumes Materials & Semiconductor margins of about 30% hold, and that MLMAP2028 (19.6% group margin) is delivered.
- **JEOL.** The price assumes the operating margin rises from 16% (FY3/27E) toward the plan's 20%.
- **Anritsu.** The price at about 19x needs only about 6% EPS growth, i.e., FY3/27's roughly 15% margin being held.
- **Shimadzu.** The price at about 22x assumes margins of 13-14% hold, with growth of about 6% a year.
- **Hitachi (theme value).** At 15-20x adjusted EBITA, Measurement & Analysis Systems would be worth ¥1.9-2.5tn, or 8.6-11.5% of Hitachi's EV of ¥21.6tn.

### 3.7 Access for a foreign investor

- **Listing and trading unit.** All seven trade on the TSE Prime market in units of 100 shares (Yahoo pages).
- **Minimum lot at the 12 Nov close** (my calc):

| Company | Cost of 100 shares |
|---|---|
| Lasertec | ¥3,638,000 |
| Horiba | ¥2,038,500 |
| JEOL | ¥668,000 |
| Hitachi | ¥498,100 |
| Shimadzu | ¥459,400 |
| Anritsu | ¥239,650 |
| Rigaku | ¥134,800 |

- **Smaller trading units.** Lasertec (25 Sep 2026) [LT-TDnet] and Horiba (27 Mar 2026) [HO-TDnet] have published policies on lowering the minimum investment unit. Neither was read, and no split was verified.
- **Over-the-counter and ADR lines** (seen only in search-result URLs and not verified as active):
  - Shimadzu: OTC SHMZF; Frankfurt HDZ (stockanalysis.com/quote/otc/SHMZF/; /quote/fra/HDZ).
  - Rigaku: OTC "RGAK.F" (simplywall.st URL).
  - Lasertec: ADR with ISIN US51809L1098 (parqet.com URL).
  - JEOL, Hitachi, Horiba and Anritsu: could not verify.
- **Foreign-ownership limits.** None appear in the documents read. Whether any of these companies is in a designated sector under Japan's FEFTA prior-notification rules could not be verified; this should be checked against the Ministry of Finance's published list.

### 3.8 Near-term events (to about May 2027)

**Confirmed dates**
- 13 Nov 2026: JEOL 1H FY3/27 results; Horiba Q3 FY12/26 results ("次回決算発表予定日" on [Y-6951] and [Y-6856]).
- March 2027 AGM: Horiba vote on moving to a Company with Audit & Supervisory Committee [HO-MLMAP].

**In progress**
- Hitachi buyback of ¥550bn, 52% complete at end-1H, runs through FY3/27 [HI-OUT].
- Hitachi home-appliance deconsolidation "within FY2026" [HI-OUT].
- Rigaku and Onto hybrid metrology engine targeted at memory lines in 1Q FY12/27 [RG-3Q].

**Inferred from prior-year timing; not announced**
- Late January to mid-February 2027:
  - Q3 FY3/27 results for Hitachi, Anritsu, Shimadzu and JEOL.
  - Lasertec Q2 FY6/27 (the prior-year Q2 came on 30 Jan 2026 [LT-TDnet]).
  - Horiba FY12/26 results (prior year: 12 Feb 2026 [HO-TDnet]).
  - Rigaku FY12/26 results and FY12/27 guidance (prior-year date not verified).
- Late April to mid-May 2027: FY3/27 results for Anritsu (prior year 27 Apr), Shimadzu (12 May) and JEOL (15 May). Anritsu's GLP2026 ends, so its next plan is likely then (inference).

**Not verified**
- Scheduled METI or US BIS export-control decisions.
- US tariff decisions.
- Any investor days other than Hitachi Energy's (2 Nov 2026).

### 3.9 Provisional reads on entry (PROVISIONAL; analysis, not a recommendation)

| Company | Provisional read | Reasons | Conditions that would improve the entry |
|---|---|---|---|
| JEOL | **Fair** | 15.3x the company FY3/27 forecast is above its five-year median of 12.7x, and EV/EBITDA of 12.9x is above its median of 8.0x, while earnings are near a cyclical low (Q1 loss; forecast weighted to 2H). The exit-multiple check needs about 10% EPS growth a year, roughly the plan path. The stock is at a deep discount to US analytical peers. | 1H results (13 Nov) and 2H evidence that mask-writer shipments recover and the ¥26.5bn operating-profit forecast holds. A price near ¥5,500 (12.7x the forecast, my calc). Closing and proceeds of the medical-business sale to Sysmex (which raises theme purity), and cash use (free cash flow about zero in FY3/26; ¥12.8bn spent buying back Nikon's stake). |
| Hitachi (as a theme vehicle) | **Fair for the group; low theme purity** | 24.2x the company forecast against a five-year median of 21.8x (the median is lifted by the 2024-26 re-rating). Strong free cash flow and ¥814bn of shareholder returns. Measurement & Analysis Systems is less than about 10% of value. | A pullback toward about 20x the forecast (≈¥4,100), or any structural move or separate disclosure for Hitachi High-Tech (none announced). |
| Shimadzu | **Fair** | 21.8x the company forecast equals its five-year median, and the stock is near its 2026 high. The price implies about 5.5% perpetual growth at r = 8%. ROIC is trending down, and net cash is about zero after Tescan. | About 19x the forecast or below (≈¥4,000), or evidence that Tescan and recurring revenue lift margins and ROIC. Next data: Q3, early February 2027 (inferred). |
| Rigaku | **Stretched** | 24.4x the FY12/26 forecast relies on a record Q4 (about ¥15.3bn operating profit); trailing P/E is 33x. Net debt is ¥39.7bn and free cash flow is thin. Order momentum is strong (+39%; semiconductor +117%), and Onto's 27% stake is strategic. | FY12/26 results (about February 2027) confirming Q4 delivery, with FY12/27 guidance consistent with more than 30% semiconductor growth. Or a price at or below about 18x consensus EPS (≈¥1,220, my calc). |
| Horiba | **Fair** (stretched against its own history, fair against peers) | 17.1x the forecast against a five-year median of 11.6x; EV/EBITDA 9.8x against 5.6x. The earnings mix has shifted structurally toward 30%-margin semiconductor work. The MLMAP2028 EPS of about ¥1,475 puts the stock at 13.8x 2028 earnings. About 99% of operating profit comes from Materials & Semiconductor, which is a cycle risk. | Q3 (13 Nov) confirming Materials & Semiconductor momentum, or a price near 14x the forecast (≈¥16,700, close to the 2026 low of ¥16,180). |
| Anritsu | **Attractive** (relative to peers and earnings momentum; on its own history only fair) | 19.2x the company forecast is about its median of 19.0x. Consensus forward P/E is 16.6x and EV/EBITDA 10.5x, against Keysight's 22.6x and 30.7x. The stock is 51% below its June high. TTM free-cash-flow yield is about 4.6% (¥14.2bn ÷ ¥306.8bn, my calc), net cash about 15% of market cap, and the dividend yield 2.6%. Orders rose 60% and guidance was raised. The exit-multiple check needs only about 5.6% EPS growth a year. | Continued data-centre order momentum in Q3 (late January 2027). The risk is that FY3/27 proves a peak in data-centre test demand, as in a pause around 2028. |
| Lasertec | **Fair** | 36.2x the company forecast (24.6x consensus) is below its own five-year medians (P/E 55, EV/EBITDA 37.5) and in line with KLA on EV/EBITDA. Leading indicators are strong (advances +¥42.8bn; production +120%). The price needs 11-15% EPS growth a year at near-peak margins, and the business depends entirely on AI-related capex. | A pullback toward the 2026 low (¥28,660 ≈ 28.6x the forecast), or Q2 (late January 2027) confirming orders and advances. Signs of financing stress in AI capex would argue for waiting. |

---

## Part 4. What I could not verify (and what I tried)

**Tool constraints**
- The WebSearch budget ran out partway through the session, and the Firecrawl and Exa tools had no credits.
- Kabutan, irbank and minkabu returned HTTP 403.
- So I worked only from directly fetched URLs: TDnet PDFs through the Yahoo mirror, StockAnalysis and Yahoo!ファイナンス.

**Results not yet published on 12 Nov 2026**
- JEOL 1H FY3/27 and Horiba Q3 FY12/26 results are due 13 Nov 2026.
- JEOL's Q1 figures come from Yahoo's summary and a search snippet; the primary Q1 PDF [JE-Q1] was not opened.

**Revenue model (test c)**
- No numeric share of service, consumables or software revenue was found for:
  - JEOL
  - Shimadzu (it describes a "recurring business" but gives no ratio in the 決算短信)
  - Horiba
  - Anritsu
  - Hitachi's Measurement & Analysis Systems
  - Lasertec on a full-year basis
- I checked each company's 決算短信 and presentation pages that I read. Annual reports and integrated reports were not read.

**Financial strength (test d)**
- R&D as a share of sales for JEOL, Hitachi, Shimadzu, Rigaku, Anritsu and Lasertec: StockAnalysis shows no R&D line for these companies, and the 決算短信 pages I read did not include it. Horiba's ratio was verified.
- Equity ratios for Rigaku and Anritsu.
- Customer concentration, i.e., named customers above 10% of sales (normally in 有価証券報告書; not read).
- China share for Hitachi, Horiba, Anritsu and Lasertec (reported only within "Asia").

**Company-specific items**
- **Hitachi:** targets of the Inspire 2027 plan; the split of Measurement & Analysis Systems between electron microscopes, CD-SEM and clinical analysers.
- **Shimadzu:**
  - the successor to the FY2023-2025 medium-term plan (name and numeric targets);
  - the headline Tescan purchase price (page 4 of [SH-TES] not read). The verified figures are a ¥112.3bn net cash outflow, ¥127.2bn goodwill and Tescan's FY12/24 sales of CZK 4,026m;
  - the year Shimadzu starts reporting under IFRS.
- **JEOL:**
  - the price, closing date and earnings effect of the medical-business sale to Sysmex. The buyer is verified [JE-SYS];
  - the Nikon tender price (later pages of [JE-TOB] not read);
  - mask-writer orders and backlog.
- **Rigaku:** the price Onto paid Atom Investment; the length of the lock-up; whether Atom is a Carlyle vehicle (not named in Rigaku's notices).
- **Anritsu:** the name of the newly consolidated subsidiary (28 Oct 2026).
- **Lasertec:** FY6/26 orders (¥237.5bn) and backlog (¥322.9bn) come only from a secondary site seen via a search snippet [GD-LT]; Lasertec's presentation PDFs were not reachable from its IR page as fetched.

**Valuation**
- Ten-year ranges and medians of P/E, P/B and EV/EBITDA (StockAnalysis's free view shows five fiscal years; Kabutan and irbank blocked).
- Daily-based five-year medians (I used fiscal-year-end values).
- Consensus revenue and profit for each of the next two fiscal years. Only three-year growth rates and forward P/E were available, and the fiscal-year basis of forward P/E is not stated.

**Policy**
- 2026 decisions on Japanese export controls (METI) and US rules (BIS), and US tariff decisions affecting these companies.
- Academic and government budget figures for Japan, the US and China.

**Investor access**
- Over-the-counter tickers for JEOL, Hitachi, Horiba and Anritsu.
- Whether any company is in a designated sector under FEFTA.
- The content of Lasertec's and Horiba's policies on the trading unit.

**Corporate events**
- Activist positions and cross-shareholding sales for all seven companies (search budget exhausted). None appeared in the filings read.

**Market context**
- The cause of the June-October 2026 sector de-rating (only the 5-6 November sell-off is sourced).
- The cause of Anritsu's -11.7% move on 30 Oct.

---

## Part 5. Sources (all retrieved 12 Nov 2026 unless noted; publication dates in brackets)

**Company filings (TDnet, read through the Yahoo!ファイナンス disclosure mirror)**
- [LT-Q1]: Lasertec, Consolidated Financial Results for Q1 ended 30 Sep 2026 (English) [30 Oct 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261030/20261030561656.pdf
- [LT-FY26]: Lasertec, Consolidated Financial Results for year ended 30 Jun 2026 (English summary) [6 Aug 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260806/20260806512261.pdf
- [AN-1H]: Anritsu, Financial Results for 2Q of FY ending 31 Mar 2027 (briefing presentation) [29 Oct 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261029/20261029559469.pdf
- [AN-FY25]: Anritsu, Financial Results for FY ended 31 Mar 2026 (briefing presentation) [27 Apr 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260427/20260427511745.pdf
- [SH-1H]: Shimadzu, Consolidated Financial Results for six months ended 30 Sep 2026 (English) [6 Nov 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261106/20261106567538.pdf
- [RG-3Q]: Rigaku, 3Q FY12/26 Earnings Presentation [11 Nov 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261111/20261111573406.pdf
- [RG-0522]: Rigaku, Notification Regarding Secondary Offering of Shares and Change in Principal Shareholder [22 May 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260522/20260522544958.pdf
- [RG-0812]: Rigaku, (Progress of Disclosure) Notification Regarding Changes in the Largest and Principal Shareholder [12 Aug 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260812/20260810517357.pdf
- [RG-0930]: Rigaku, Notification Regarding Changes in the Largest and Principal Shareholder [30 Sep 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260930/20260930542508.pdf
- [JE-FY26]: JEOL, Consolidated Financial Results for FY ended 31 Mar 2026 (English summary) [15 May 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260515/20260514534944.pdf
- [JE-Q1] (not opened): JEOL, Q1 FY3/27 summary [14 Aug 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260814/20260814520312.pdf
- [JE-MTP]: JEOL, Formulation of Medium-Term Management Plan "Evolving Growth 2.0 - A New Horizon -" [15 May 2025]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20250515/20250515554480.pdf
- [HO-1H]: Horiba, Summary of Consolidated Financial Statements for six months ended 30 Jun 2026 (updated) [12 Aug 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260812/20260812517719.pdf
- [HO-MLMAP]: Horiba, HORIBA Updates Mid-Long Term Management Plan (MLMAP2028) [7 Aug 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514627.pdf
- [HI-1H]: Hitachi, Consolidated Financial Results for Q2 ended 30 Sep 2026 [28 Oct 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261028/20261028557961.pdf
- [HI-OUT]: Hitachi, Outline of Consolidated Financial Results for Q2 ended 30 Sep 2026 [28 Oct 2026]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261028/20261028557964.pdf

**Disclosure lists (Yahoo!ファイナンス)**
- [LT-TDnet]: https://finance.yahoo.co.jp/quote/6920.T/disclosure
- [AN-TDnet]: https://finance.yahoo.co.jp/quote/6754.T/disclosure
- [SH-TDnet]: https://finance.yahoo.co.jp/quote/7701.T/disclosure
- [RG-TDnet]: https://finance.yahoo.co.jp/quote/268A.T/disclosure
- [JE-TDnet]: https://finance.yahoo.co.jp/quote/6951.T/disclosure (page 2: https://finance.yahoo.co.jp/quote/6951.T/disclosure?page=2)
- [HO-TDnet]: https://finance.yahoo.co.jp/quote/6856.T/disclosure
- [HI-TDnet]: https://finance.yahoo.co.jp/quote/6501.T/disclosure

**Price and market data (12 Nov 2026)**
- Yahoo!ファイナンス quote pages:
  - [Y-6951]: https://finance.yahoo.co.jp/quote/6951.T
  - [Y-6501]: https://finance.yahoo.co.jp/quote/6501.T
  - [Y-7701]: https://finance.yahoo.co.jp/quote/7701.T
  - [Y-268A]: https://finance.yahoo.co.jp/quote/268A.T
  - [Y-6856]: https://finance.yahoo.co.jp/quote/6856.T
  - [Y-6754]: https://finance.yahoo.co.jp/quote/6754.T
  - [Y-6920]: https://finance.yahoo.co.jp/quote/6920.T
  - [Y-6857]: https://finance.yahoo.co.jp/quote/6857.T
  - [Y-6965]: https://finance.yahoo.co.jp/quote/6965.T
  - [Y-3446]: https://finance.yahoo.co.jp/quote/3446.T
  - [Y-6841]: https://finance.yahoo.co.jp/quote/6841.T
  - [Y-7729]: https://finance.yahoo.co.jp/quote/7729.T
  - [Y-FX]: https://finance.yahoo.co.jp/quote/USDJPY=FX
- Yahoo!ファイナンス price history [YH-xxxx]: https://finance.yahoo.co.jp/quote/{code}.T/history?from=YYYYMM01&to=YYYYMMDD&timeFrame=m
  - Month windows used: 2021/11, 2023/11 and 2025/12 for 6951, 7701, 6920, 6754, 6856 and 6501.
  - [YH-268A-m]: monthly, 2024/10-2026/11.
  - [YH-6920-m]: monthly, 2021/11-2026/11.
  - [YH-6754-d] and other daily pages: https://finance.yahoo.co.jp/quote/{code}.T/history
- StockAnalysis statistics pages [SA-xxxx]: https://stockanalysis.com/quote/tyo/{6951|7701|6920|6754|6856|268A|6501|6857|6965|3446|6841|7729}/statistics/
- StockAnalysis ratios pages [SAR-xxxx]: https://stockanalysis.com/quote/tyo/{code}/financials/ratios/
- StockAnalysis financials pages [SA-F-xxxx]: https://stockanalysis.com/quote/tyo/{code}/financials/
- Peers (StockAnalysis statistics):
  - [SA-TMO]: https://stockanalysis.com/stocks/tmo/statistics/
  - [SA-A]: https://stockanalysis.com/stocks/a/statistics/
  - [SA-BRKR]: https://stockanalysis.com/stocks/brkr/statistics/
  - [SA-KLAC]: https://stockanalysis.com/stocks/klac/statistics/
  - [SA-KEYS]: https://stockanalysis.com/stocks/keys/statistics/
  - [SA-ONTO]: https://stockanalysis.com/stocks/onto/statistics/
  - [SA-OXIG]: https://stockanalysis.com/quote/lon/OXIG/statistics/

**Market news**
- [MAT-1106]: Matsui Securities, 日経平均 大引け, 5日続落 (6 Nov 2026): https://finance.matsui.co.jp/news/635738/index
- [MAT-1105]: Matsui Securities, 日経平均 大引け, 4日続落 (5 Nov 2026), seen via search snippet only: https://finance.matsui.co.jp/news/634949/index

**Secondary, seen only through search snippets (not opened; not relied on except where flagged)**
- [GD-LT]: gyokaidigest, Lasertec FY2026 report: https://www.gyokaidigest.com/companies/lasertec/report/2026-FY
- JPX filing archive, JEOL FY3/26 決算短信 (Japanese): https://www2.jpx.co.jp/disc/69510/140120260514534200.pdf
- OTC and ADR references: https://stockanalysis.com/quote/otc/SHMZF/ ; https://stockanalysis.com/quote/fra/HDZ/financials ; https://simplywall.st/stocks/us/tech/otc-rgak.f/rigaku-holdings/past ; https://app.parqet.com/en/assets/lasertec-US51809L1098

[LT-Q1]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261030/20261030561656.pdf
[LT-FY26]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260806/20260806512261.pdf
[AN-1H]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261029/20261029559469.pdf
[AN-FY25]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260427/20260427511745.pdf
[SH-1H]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261106/20261106567538.pdf
[RG-3Q]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261111/20261111573406.pdf
[RG-0522]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260522/20260522544958.pdf
[RG-0812]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260812/20260810517357.pdf
[RG-0930]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260930/20260930542508.pdf
[JE-FY26]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260515/20260514534944.pdf
[JE-Q1]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260814/20260814520312.pdf
[JE-MTP]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20250515/20250515554480.pdf
[HO-1H]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260812/20260812517719.pdf
[HO-MLMAP]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20260807/20260807514627.pdf
[HI-1H]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261028/20261028557961.pdf
[HI-OUT]: https://finance-frontend-pc-dist.west.edge.storage-yahoo.jp/disclosure/20261028/20261028557964.pdf
[LT-TDnet]: https://finance.yahoo.co.jp/quote/6920.T/disclosure
[AN-TDnet]: https://finance.yahoo.co.jp/quote/6754.T/disclosure
[SH-TDnet]: https://finance.yahoo.co.jp/quote/7701.T/disclosure
[RG-TDnet]: https://finance.yahoo.co.jp/quote/268A.T/disclosure
[JE-TDnet]: https://finance.yahoo.co.jp/quote/6951.T/disclosure
[HO-TDnet]: https://finance.yahoo.co.jp/quote/6856.T/disclosure
[HI-TDnet]: https://finance.yahoo.co.jp/quote/6501.T/disclosure
[Y-6951]: https://finance.yahoo.co.jp/quote/6951.T
[Y-6501]: https://finance.yahoo.co.jp/quote/6501.T
[Y-7701]: https://finance.yahoo.co.jp/quote/7701.T
[Y-268A]: https://finance.yahoo.co.jp/quote/268A.T
[Y-6856]: https://finance.yahoo.co.jp/quote/6856.T
[Y-6754]: https://finance.yahoo.co.jp/quote/6754.T
[Y-6920]: https://finance.yahoo.co.jp/quote/6920.T
[Y-6857]: https://finance.yahoo.co.jp/quote/6857.T
[Y-6965]: https://finance.yahoo.co.jp/quote/6965.T
[Y-3446]: https://finance.yahoo.co.jp/quote/3446.T
[Y-6841]: https://finance.yahoo.co.jp/quote/6841.T
[Y-7729]: https://finance.yahoo.co.jp/quote/7729.T
[Y-FX]: https://finance.yahoo.co.jp/quote/USDJPY=FX
[YH-6754-d]: https://finance.yahoo.co.jp/quote/6754.T/history
[YH-6920-m]: https://finance.yahoo.co.jp/quote/6920.T/history?from=20211101&to=20261112&timeFrame=m
[YH-268A-m]: https://finance.yahoo.co.jp/quote/268A.T/history?from=20241001&to=20261112&timeFrame=m
[SA-6951]: https://stockanalysis.com/quote/tyo/6951/statistics/
[SA-7701]: https://stockanalysis.com/quote/tyo/7701/statistics/
[SA-6920]: https://stockanalysis.com/quote/tyo/6920/statistics/
[SA-6754]: https://stockanalysis.com/quote/tyo/6754/statistics/
[SA-6856]: https://stockanalysis.com/quote/tyo/6856/statistics/
[SA-268A]: https://stockanalysis.com/quote/tyo/268A/statistics/
[SA-6501]: https://stockanalysis.com/quote/tyo/6501/statistics/
[SA-6857]: https://stockanalysis.com/quote/tyo/6857/statistics/
[SA-6965]: https://stockanalysis.com/quote/tyo/6965/statistics/
[SA-3446]: https://stockanalysis.com/quote/tyo/3446/statistics/
[SA-6841]: https://stockanalysis.com/quote/tyo/6841/statistics/
[SA-7729]: https://stockanalysis.com/quote/tyo/7729/statistics/
[SAR-6951]: https://stockanalysis.com/quote/tyo/6951/financials/ratios/
[SAR-7701]: https://stockanalysis.com/quote/tyo/7701/financials/ratios/
[SAR-6920]: https://stockanalysis.com/quote/tyo/6920/financials/ratios/
[SAR-6754]: https://stockanalysis.com/quote/tyo/6754/financials/ratios/
[SAR-6856]: https://stockanalysis.com/quote/tyo/6856/financials/ratios/
[SAR-268A]: https://stockanalysis.com/quote/tyo/268A/financials/ratios/
[SAR-6501]: https://stockanalysis.com/quote/tyo/6501/financials/ratios/
[SA-F-6951]: https://stockanalysis.com/quote/tyo/6951/financials/
[SA-F-7701]: https://stockanalysis.com/quote/tyo/7701/financials/
[SA-F-6920]: https://stockanalysis.com/quote/tyo/6920/financials/
[SA-F-6754]: https://stockanalysis.com/quote/tyo/6754/financials/
[SA-F-6856]: https://stockanalysis.com/quote/tyo/6856/financials/
[SA-F-268A]: https://stockanalysis.com/quote/tyo/268A/financials/
[SA-TMO]: https://stockanalysis.com/stocks/tmo/statistics/
[SA-A]: https://stockanalysis.com/stocks/a/statistics/
[SA-BRKR]: https://stockanalysis.com/stocks/brkr/statistics/
[SA-KLAC]: https://stockanalysis.com/stocks/klac/statistics/
[SA-KEYS]: https://stockanalysis.com/stocks/keys/statistics/
[SA-ONTO]: https://stockanalysis.com/stocks/onto/statistics/
[SA-OXIG]: https://stockanalysis.com/quote/lon/OXIG/statistics/
[MAT-1106]: https://finance.matsui.co.jp/news/635738/index
[MAT-1105]: https://finance.matsui.co.jp/news/634949/index
[GD-LT]: https://www.gyokaidigest.com/companies/lasertec/report/2026-FY

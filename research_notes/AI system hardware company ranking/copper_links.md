# Copper interconnect for AI clusters (cables and assemblies, AECs, backplane/midplane/board connectors, retimers/redrivers/cable DSPs) — research notes as of 12 November 2026

Conventions. Every figure carries the period it covers and its publication date. "Company claim, unconfirmed" = no outside party confirmed it. "Secondary" = trade press, self-media or analyst. "Derived" = my arithmetic on cited figures. No share prices, valuation multiples, market capitalisation or price targets are used (separate workstream); deal terms are given only where they bear on cash, debt or strategy.

Research constraint (read first). The shared WebSearch budget (200 calls per turn across all parallel agents) was exhausted part-way through this session. Following the tool's instruction, I did no further searching through any engine; the rest of the work used only URLs already found plus local text extraction of Credo's 10-K PDF. As a result, Japan, Korea, India, FIT Hon Teng, Lotes, Molex, Samtec, Rosenberger, Huber+Suhner, Semtech, MACOM, Montage, Parade, Point2 and IEEE 802.3 are covered only from background knowledge (pre-2026, flagged "not re-verified") or not at all. A follow-up session could close these gaps.

## 1. Segment map — companies worldwide, role, and why each matters or was left out

### Takeaway
The segment has three layers: (i) connector/cable houses that own high-speed copper and increasingly fibre (Amphenol, TE, Molex, Luxshare, FIT, Samtec); (ii) cable assemblers and wire/twinax makers (Bizlink, Woer/Lettin, Japanese twinax specialists); (iii) signal-conditioning silicon (Credo, Astera Labs, Marvell, Broadcom, MaxLinear, Montage, Parade). If a board midplane replaces the cable backplane (NVIDIA Kyber), value shifts towards high-layer PCB and laminate/material makers (Victory Giant, WUS, Shengyi, EMC, Feilihua). Evidence from H2 2026 was found for US, Taiwan (Bizlink) and mainland China. Japan, Korea and India are thin; see constraint above.

### Cited Findings
Legend for the "Evidence" column: V = verified in H2 2026 sources this session (source given); S = secondary/self-media only; B = background knowledge, not re-verified this session.

| Company | Home | Listing / ticker | Role in segment | Why it matters / why left out | Evidence |
|---|---|---|---|---|---|
| Amphenol | US | NYSE: APH | High-speed connectors, cable backplanes/cartridges, flyover cables, power, and fibre since buying CommScope CCS (closed 9 Jan 2026) | Largest and most profitable connector house in AI racks; AI ~3/4 of IT datacom (Q3 2026) | V — [8-K 28 Oct 2026](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926119421/aph-ex99d1.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/) |
| TE Connectivity | Ireland (Galway) | NYSE: TEL | Backplane, mid-board, flyover, front I/O, power connectivity (DDN sub-segment); CPO fibre attach (RAM Photonics) | Second broad house; AI exposure small (DDN FY2026 $975M of $19.9B sales) but doubling | V — [8-K 28 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/) |
| Molex | US | Private (Koch Industries) | Connectors, backplane, cable assemblies; named among overseas leaders in Chinese supply-chain commentary | Major private competitor; no H2 2026 financial data | S — [EET China](https://www.eet-china.com/mp/a300961.html) (search snippet; page did not load); B for Koch ownership |
| Samtec | US | Private | Flyover / co-packaged copper cable systems, high-speed connectors | Important technical player; no data found | B |
| Credo | US (Cayman holdco) | Nasdaq: CRDO | AEC system vendor (ZeroFlap), Ethernet/PCIe retimers, optical DSPs, ZF optical transceivers, SiPh PICs (DustPhotonics), micro-LED cables (Hyperlume) | Holds ~88–99% of AECs (third-party/competitor estimates); key specialist | V — [10-K FY2026](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf); [Q1 FY27 8-K](https://www.sec.gov/Archives/edgar/data/0001807794/000162828026059795/credoq12027ex-991.htm) |
| Astera Labs | US | Nasdaq: ALAB | Aries PCIe/CXL retimers, Taurus AEC modules, Scorpio P/X fabric switches, Leo CXL; optical drivers/TIAs (sampling) | Retimer leader moving to switching; key specialist | V — [Q3 2026 8-K](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm) |
| Marvell | US | Nasdaq: MRVL (B) | Alaska A PAM4 AEC DSPs sold to cable makers (1.6T, 8x200G); retimers; agreed 2 Nov 2026 to buy Lumentum (all-stock, close H1 2028) | Main merchant AEC-DSP rival to Credo; becoming an integrated electro-optical giant | V — [Light Reading](https://lightreading.com/ai-machine-learning/marvell-strikes-115b-deal-for-lumentum); [Lumentum 8-K ex99.2](https://www.sec.gov/Archives/edgar/data/0001633978/000119312526442758/d163169dex992.htm); S — [InsideDeepTech 9 Sep 2026](https://www.insidedeeptech.com/active-electrical-cables-aec-ai-data-centers-full-guide/) |
| Broadcom | US | Nasdaq: AVGO (B) | Retimers, SerDes IP, AEC DSPs | In passing; no H2 2026 copper-specific data found | B |
| MaxLinear | US | Nasdaq: MXL | Rushmore 1.6T PAM4 DSP for AECs sold to cable makers | New entrant targeting 20–30% of 1.6T AEC; first design win ships H1 2027 | S — [Stocktwits on Q3 2026 call, 22 Oct 2026](https://stocktwits.com/news-articles/markets/equity/crdo-stock-hits-6-month-low-after-max-linear-targets-credo-dominated-cable-market/cZxyk1CRBxY) |
| Semtech | US | Nasdaq: SMTC (B) | CopperEdge linear redrivers for active copper cables (ACC) | ACC alternative to AEC; not verified | B |
| MACOM | US | Nasdaq: MTSI (B) | Linear equalisers/redrivers for ACC | Same; not verified | B |
| Point2 Technology | US/Canada | Private | e-Tube radio-frequency plastic waveguide cables | Possible copper successor; not verified | B |
| Alphawave (acquired by Qualcomm) | UK | Formerly LSE: AWE; now part of Qualcomm (B) | SerDes IP, connectivity chiplets | Lead "Qualcomm bought Alphawave" not verified this session | B |
| Parade Technologies | Taiwan | 4966 (B) | PCIe retimers | Retimer rival; no data | B |
| Montage Technology | China | SSE STAR: 688008 (B) | PCIe retimers, memory interface chips | China's retimer champion; no data | B |
| Luxshare Precision | China | SZSE: 002475 (B) | 224G DAC/ACC, cable backplanes, NPC/CPC, optical modules, liquid cooling, power | Largest Chinese assembler; claimed No.2 copper source to NVIDIA | S — [10jqka 30 Oct 2026](http://stock.10jqka.com.cn/20261030/c681263349.shtml); [ifeng 4 Nov 2026](https://finance.ifeng.com/c/8xmRAHlvGpt) |
| Woer Nuclear Material (Lettin, 乐庭智联) | China | SZSE: 002130 | High-speed twinax communication cable (224G in volume; 448G trial) | Leading Chinese raw-cable supplier; Huizhou and Vietnam capacity | S — [broker report May 2026](https://pdf.dfcfw.com/pdf/H3_AP202605081822068042_1.pdf); [Gelonghui](https://m.gelonghui.com/live/2594403) (both via search snippets, not opened) |
| Zhaolong Interconnect (兆龙互连) | China | SZSE: 300913 (B) | High-speed cable; developing backplane connectors | Named as domestic backplane developer | S — [EET China snippet](https://www.eet-china.com/mp/a300961.html) |
| Huafeng Technology (华丰科技) | China | SSE STAR: 688629 (B) | Backplane connectors (domestic AI servers) | Named as domestic backplane developer | S — same |
| Kingsignal (金信诺) | China | SZSE: 300252 (B) | High-speed cable | Not verified | B |
| Shenyu (神宇股份), Xinya Electronic (新亚电子) | China | SZSE: 300563 / SSE (B) | Fine coax/twinax wire; Xinya claimed as Amphenol wire partner | Broker claim of RMB 4B+ Amphenol orders from 2026 is unverified | S — [CLS](https://www.cls.cn/detail/1828472); [Zhihu](https://zhuanlan.zhihu.com/p/2079096896665272736) (snippets) |
| AVIC Jonhon (中航光电), Shenglan (胜蓝股份) | China | SZSE: 002179 / 300843 | High-speed backplane connectors; claimed NVLink connector supplier | Self-media claims only | S — [Eastmoney self-media 28 Aug 2026](https://caifuhao.eastmoney.com/news/20260828173839122825400) |
| Foxconn Interconnect Technology (FIT Hon Teng) | Taiwan/HK | HKEX: 6088 (B) | Connectors, cables, CPO-related products | Important Foxconn-captive supplier; H1 2026 interim not retrieved | B |
| Bizlink | Taiwan (KY) | TWSE: 3665 | Contract manufacturer of Credo's AECs; own 800G AECs; power products; busbars (Interplex Datacom, consolidated 23 Sep 2026) | Key assembler; only long-term supply partner in Credo's 10-K | V — [Credo 10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf); S — [cnyes 5 Oct 2026](https://news.cnyes.com/news/id/6621868) |
| Lotes (嘉澤) | Taiwan | TWSE: 3533 (B) | CPU/GPU sockets, high-speed connectors | Not verified | B |
| Sumitomo Electric | Japan | TSE: 5802 (B) | Wire, twinax, optical | Not verified | B |
| Proterial (ex-Hitachi Metals) | Japan | Private (B) | High-speed twinax cable | Not verified | B |
| Junkosha | Japan | Private (B) | Fluoropolymer twinax for DAC/AEC | Not verified | B |
| Hirose, JAE, Yamaichi, I-PEX | Japan | TSE: 6806 / 6807 / 6941 / 6640 (B) | Board connectors; Yamaichi test sockets | Not verified; Japanese coverage thin | B |
| Rosenberger | Germany | Private (B) | RF/high-speed connectors, fibre | Not verified | B |
| Huber+Suhner | Switzerland | SIX: HUBN (B) | Fibre and RF connectivity | Not verified | B |
| Valens Semiconductor | Israel | NYSE: VLN (B) | MIPI A-PHY / HDBaseT chips | Left out: automotive/industrial, not AI cluster links | B |
| DustPhotonics | Israel | Acquired by Credo (2026) | Silicon photonics PICs, 400G–1.6T | Gives Credo an optical successor | V — [Investing.com](https://www.investing.com/news/company-news/credo-to-acquire-dustphotonics-for-750m-to-expand-optical-tech-93CH-4611185) |
| Victory Giant (胜宏科技), WUS (沪电股份), Shennan Circuits (深南电路) | China | SZSE: 300476 / 002463 / 002916 | High-layer PCBs; self-media claims Victory Giant is a core Rubin orthogonal-backplane supplier | Midplane beneficiaries if Kyber ships | S — [Eastmoney self-media](https://caifuhao.eastmoney.com/news/20260828173839122825400) |
| Shengyi Technology (生益科技), Feilihua (菲利华), Longyang (隆扬电子) | China | SSE: 600183 / SZSE: 300395 / 301389 | M9 CCL (claimed NVIDIA-certified); quartz glass fabric (claims to be one of two global mass producers); HVLP5 copper foil | Scarce materials for the midplane | S — same |
| Elite Material (EMC), Unimicron, TTM, Doosan, ISU Petasys | Taiwan / Taiwan / US / Korea / Korea | TWSE: 2383 / 3037; Nasdaq: TTMI; KRX: 000150 / 007660 (B) | CCL (EMC, Doosan); high-layer PCB (TTM, Unimicron, ISU Petasys) | Midplane/board beneficiaries; not verified | B |
| Broadex (博创科技), 3M | China / US | SZSE: 300548 (B) / NYSE: MMM (B) | AEC integrators shown in Marvell's OFC 2025 AEC demos | Minor | S — [InsideDeepTech](https://www.insidedeeptech.com/active-electrical-cables-aec-ai-data-centers-full-guide/) |
| Volex | UK | LSE: VLX (B) | Data-centre cable assemblies | Not verified | B |
| Korea (cables/retimers) | — | — | No Korean AEC, high-speed cable or retimer maker found; Korean presence appears to be boards and laminates (ISU Petasys, Doosan) | Coverage thin (DART not searched) | B |
| India | — | — | No Indian player found in AI copper interconnect | Coverage thin (NSE/BSE not searched) | — |

### Inferences
- Signal-conditioning silicon is concentrated in US fabless firms (Credo, Astera, Marvell, Broadcom, MaxLinear). Raw twinax and assembly capacity is concentrated in China and Taiwan (Woer, Luxshare, Bizlink), plus Japanese twinax specialists (not verified). Connector IP is held by US houses (Amphenol, TE, Molex, Samtec).
- A board midplane (Kyber) would move value from cable assembly (Amphenol cartridges, Luxshare) towards PCB, laminate and materials (Victory Giant, WUS, EMC, Shengyi, Feilihua quartz cloth) and towards the midplane connector (reportedly Amphenol). This is why the PCB/laminate makers belong on the map.

### Gaps
- No H2 2026 data on Molex, Samtec, FIT Hon Teng, Lotes, any Japanese maker, Rosenberger, Huber+Suhner, Semtech, MACOM, Montage, Parade, Point2 or Valens (search budget exhausted).
- Korea and India are effectively uncovered. DART, NSE and BSE were not searched.
- The Chinese listings and claimed roles rest mainly on self-media and broker summaries.

## 2. Evidence on tests (a)–(e) for the key companies (Amphenol, TE, Credo, Astera Labs, Luxshare, Bizlink)

### Takeaway
All six sell one-off hardware on purchase orders. None owns a "judge"; the qualification gate belongs to NVIDIA and the hyperscalers. Positions rest on know-how (SerDes and DSP design for Credo and Astera; connector signal integrity for Amphenol and TE) and on qualified manufacturing capacity (Amphenol, Luxshare, Bizlink). Amphenol combines the strongest evidence of commercial lead (IT datacom +77% organic, record orders) with diversification and owned fibre assets. Credo and Astera have the best unit economics (68–72% gross margins, net cash), but extreme customer concentration: top customer 49–53%. TE is financially strong but small in AI. Luxshare is large but low-margin, with negative nine-month operating cash flow. Bizlink is a profitable assembler tied to a bridge product.

### Cited Findings

#### Amphenol (APH) — Q3 2026 (quarter to 30 Sep 2026; published 28 Oct 2026)
- (d) Sales $10,229.7M: +65% reported, +37% organic, +28% from acquisitions. GAAP operating margin 29.5%; adjusted 29.7% (Q3 2025: 27.5%). Communications Solutions sales $6,583.0M (+99%, +51% organic), segment operating margin 33.1%. Orders $12.2B, book-to-bill 1.19. Operating cash flow $2,078.5M, capex $457.2M, free cash flow $1,622.7M. Nine-month 2026: sales $26,607.9M (+60%, +34% organic), FCF $3,659.4M (13.8% of sales, derived), capex $1,104.3M (4.2% of sales, derived), acquisitions net of cash $11,055.8M. FY2026 guidance: $36.9–37.1B (~+60%); Q4 guidance $10.3–10.5B — [Amphenol 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926119421/aph-ex99d1.htm)
- (d) Balance sheet, 30 Sep 2026: total debt $17,870.8M (31 Dec 2025: $15,502.0M); cash and short-term investments $5,301.4M; net debt $12.6B; net leverage 1.1x (CFO); $3.0B revolver undrawn; no commercial paper. CommScope CCS closed 9 Jan 2026, partly financed by two $1,534.1M delayed-draw term loans (the 364-day loan has been repaid; the 3-year loan is due 9 Jan 2029 at ~4.67%). Interest expense $212.3M in Q3 2026 vs $80.7M a year earlier. Inventories $5,264.5M vs $3,424.9M at 31 Dec 2025 — [Amphenol 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926120646/aph-20260930x10q.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/)
- (a)/(b) IT datacom grew 100% in USD and 77% organically (+30% quarter on quarter). AI is "approximately 3-quarters" of IT datacom (CEO). IT datacom will "more than double" in FY2026. "More interconnect means more copper high speed interconnect." The CEO declined to discuss specific customers or architectures — [call transcript](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/). Secondary summaries give IT datacom as ~48% of Q3 sales, and one cites +117% USD growth (this conflicts with the transcript's 100%) — [BigGo Finance](https://finance.biggo.com/news/US_APH_2026-10-28)
- (a) CommScope CCS: FY2026 sales now expected at $5.1B (earlier $4.6B). CCS IT-datacom sales to "more than double", reaching ~half of CCS sales (vs ~1/3 a year earlier). CCS is "further penetrating the IT Datacom market with their advanced optical interconnect solutions" and has secured glass supply. CCS operating margin is "low 20s" (CFO). Pending: Dexgreen (fibre FTTH, ~$90M of sales) and AdvancedPCB (~$270M). Empire Electronics closed Sep 2026. The four deals together cost ~$1.6B — [8-K](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926119421/aph-ex99d1.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/)
- (b) Outside evidence of NVIDIA share is secondary only and conflicting. A Chinese expert interview calls Amphenol the exclusive supplier of the GB200 copper solution. Another article estimates ~70% of GB200 in-rack scale-up copper. One article speculates that Amphenol's Paladin connectors are used in the Rubin/Kyber midplane — [EET China](https://www.eet-china.com/mp/a300961.html); [Zhihu](https://zhuanlan.zhihu.com/p/2079096896665272736); [Jdon](https://www.jdon.com/83082-Kyber-Amphenol-Paladin-HD2-NVLink.html) (search snippets; the pages failed to load)
- (c) Revenue is one-off hardware. Customers are "opening up their order aperture"; "longer dated orders" are normal (CEO) — [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/)
- (e) Inventory days, DSO and DPO are "within our normal ranges". Q3 was not pulled in. Q2 margins benefited from tariff recoveries. Nine-month discrete tax items of $389M include unfavourable determinations by Chinese tax authorities — [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/)

#### TE Connectivity (TEL) — FY2026 (year to 25 Sep 2026; published 28 Oct 2026)
- (d) Sales $19,885M: +15.2% reported, +11.9% organic. Q4 $5,312M (+12%; +13% organic). Orders $22.2B (+27%); Q4 orders $6.1B (+29%). Adjusted operating margin 22.0% (GAAP 20.1%). Operating cash flow $4,525M, capex $1,122M (5.6% of sales, derived), FCF $3,412M (100% of adjusted net income). Cash $1,697M against ~$5,639M debt, so net debt ~$3.9B (derived). Q1 FY27 guidance ~$5.35B (+15%); FY2027 "double-digit" growth — [TE 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm)
- (a) Digital Data Networks (DDN) FY2026 $975M (+44.2%; +43.5% organic), about 4.9% of TE sales (derived); Q4 $242M (+34%). DDN orders rose ~70% in FY2026. DDN is expected to add more than $1B of revenue in FY2027, "the vast majority of that from AI", weighted to the second half. About 30% of DDN is power connectivity; the rest is backplane, mid-board, flyover cables and front I/O. "The copper addressable market growing over 100%". "Future architectures will require both copper and fiber" (CEO) — [8-K](https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/)
- (a) Optics: RAM Photonics addresses CPO fibre-attach density, in engineering validation with some customers. TE committed ~$1.6B to bolt-on deals "to broaden the optics and power filtering portfolios" (Astrodyne TDI pending) — same sources
- (b) No third-party share data found. Orders are "driven by our strong position with our hyperscale customers" (company claim, unconfirmed)
- (e) Q4 sales were reduced by $87M of IEEPA tariff refunds passed back to customers; a further ~$50M is expected in Q1 FY27. Resin, metal and freight inflation is being offset by price, with some backlog repriced — [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/)

#### Credo (CRDO) — FY2026 (year to 2 May 2026; 10-K filed ~June 2026) and Q1 FY27 (quarter to 1 Aug 2026; published 1 Sep 2026)
- (d) FY2026 revenue $1,335.1M (FY2025 $436.8M; ~+206%). Gross profit $908.3M (~68.0% margin). GAAP operating income $445.0M (33.3%). Net income $472.3M. Operating cash flow $464.3M, capex $57.3M, FCF ~$407M (derived; ~30% of revenue) — [Credo 10-K FY2026](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf)
- (d) Q1 FY27 revenue $479.0M (+9.6% QoQ; +114.7% YoY). Gross margin 64.5% GAAP / 68.0% non-GAAP. Operating margin 25.2% GAAP / 48.2% non-GAAP. Cash and short-term investments $764.3M, down from $1,443.3M, mainly from the DustPhotonics outlay ($679M decline). Goodwill rose from $92.8M to $986.4M. Inventory $313.1M (+$62.2M QoQ). No borrowings. Q2 FY27 guidance $525–535M; FY2027 growth guided at ">85%" (implying >$2.47B, derived) — [Credo 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001807794/000162828026059795/credoq12027ex-991.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/)
- (d) Customer concentration:
  - FY2026, contracting parties: A 49% (FY25 67%), B 32%; top 10 ~90%.
  - FY2026, end-customer basis: D 33% (FY25 63%), B 32%, E 19% — three end customers ~84%.
  - Q1 FY27: 33%, 28%, 13% and 10% (top four 84%) — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf); [call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/)
- (d) Geography FY2026 by shipment destination: US $768.1M (~58%; North America was 15% in FY25), Hong Kong $378.2M (28%), mainland China $80.9M (~6%), Taiwan $22.7M (~2%), rest of world $85.2M (~6%) — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf)
- (a) Supply chain: TSMC is the sole wafer foundry; Amkor and ASE package; KYEC and Sigurd test; BizLink manufactures Credo's AECs. The BizLink agreement is Credo's only long-term supply contract — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf)
- (b) AEC share: ~88% per a 650 Group analyst (CNBC, 17 Oct 2025) — [CNBC](https://www.cnbc.com/2025/10/17/500-purple-cables-put-credo-in-middle-of-the-ai-boom.html). MaxLinear's CEO estimated 93–99% (22 Oct 2026; a competitor's estimate) — [Stocktwits](https://stocktwits.com/news-articles/markets/equity/crdo-stock-hits-6-month-low-after-max-linear-targets-credo-dominated-cable-market/cZxyk1CRBxY). Amazon held a customer warrant that vested on up to $201.0M of purchases; it was fully vested and exercised by 2 May 2026 — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf). "Deep relationships with 5 hyperscalers"; Microsoft was the first AEC customer (company claim, unconfirmed) — [call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/)
- (c) "Substantially all" product sales are on purchase orders without long-term commitments — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf)
- (e) Tariff assumptions rest on "the current tariff regime, which remains fluid" (CFO). The 10-K cites Taiwan and PRC tensions and Hong Kong sanctions risk (28% of FY26 revenue was generated in Hong Kong) — [call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/); [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf)

#### Astera Labs (ALAB) — Q3 2026 (quarter to 30 Sep 2026; published 3 Nov 2026)
- (d) Revenue $584.9M (+49% QoQ; +154% YoY); nine-month 2026 $1,285.7M (+121%, derived). Gross margin 72.3% GAAP / 72.4% non-GAAP. Operating margin 30.6% GAAP / 44.7% non-GAAP. Nine-month operating cash flow $341.5M, capex $73.4M, FCF ~$268M (derived; ~21% of revenue). Cash and securities $1,378M; no debt. Q4 2026 guidance $730–750M, ~72% gross margin — [Astera 8-K ex99.1](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm)
- (d) Direct-customer concentration (Q3 26 / Q3 25 / 9M 26): A 53% / 23% / 40%; B 14% / 24% / 18%; C 10% / 10% / 14%; D <10% / 27% / 11%. Customer A was 58% of receivables. FY2025 10-K, end-customer basis: one end customer >70%, top three ~86%. Revenue by billing address, Q3 2026: Singapore $310.2M (53%), China $146.7M (25%), Taiwan $87.0M (15%), US $6.0M (1%), other $35.0M (6%) — [10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm)
- (c) A customer warrant over ~3.26M shares was issued in Feb 2026 (holder not named in the 10-Q). Contra-revenue was $18.1M in Q3 2026 and $30.4M over nine months — [10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm). Secondary reporting identifies the holder as Amazon (unconfirmed by the filing) — [FourWeekMBA](https://fourweekmba.com/ai-amazon-warrant-cut-asteras-q3-sales-18m-9-6x-a-year-ago/)
- (a) Product mix: Scorpio fabric switches became the largest product family in Q3 2026, with X-Series ahead of P-Series and combined annualised revenue >$1B. Taurus 800G AEC is "qualified and shipping in volume to our lead customer". Aries growth comes from PCIe Gen6; Aries 7 (PCIe 7) was announced. Leo 2 volume is due mid-2027 (all company claims) — [8-K](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm); [call](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810)
- (b) No third-party retimer share data found
- (e) Inventory was $200.9M at 30 Sep 2026 vs $59.0M at 31 Dec 2025 (WIP $160.7M). Purchase commitments $163.6M. Risk factors cite China trade restrictions, export controls and US–China tariffs (not quantified). "Wafer capacity, grid power, and memory supply remain tightly constrained" (CEO) — [10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm); [call](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810)

#### Luxshare Precision (002475.SZ) — 9M 2026 (to 30 Sep 2026; report published 29 Oct 2026; secondary press citing the report)
- (d) Nine-month revenue RMB 285.01B (+29.01%). Attributable net income RMB 13.06B (+13.36%; net margin ~4.6%, derived); recurring net income RMB 10.37B (+8.72%). Q3 revenue RMB 110.51B (+14.62%); Q3 net income RMB 5.21B (+6.98% YoY; +24.65% QoQ). Nine-month R&D RMB 10.55B. Nine-month operating cash flow −RMB 6.43B. FY2026 net income guided at RMB 19.09–19.92B (+15–20%) — [10jqka](http://stock.10jqka.com.cn/20261030/c681263349.shtml); [Jiemian](https://www.jiemian.com/article/15265992.html); [Sina](https://finance.sina.com.cn/roll/2026-10-30/doc-iniwxqym8566902.shtml)
- (a) Communications and data-centre revenue was RMB 16.61B in H1 2026 (+49.66%), ~9.5% of H1 revenue (derived). Company claims, unconfirmed:
  - 224G DAC/ACC in volume, "about one quarter ahead of peers".
  - Cable backplanes in production with North American and domestic customers.
  - 448G channel bandwidth ">110 GHz vs ~90 GHz" for the best peer.
  - CPC (co-packaged copper) in validation, volume H2 2027.
  - 800G optical modules in mass delivery since H1 2026; 1.6T entering batch production.
  - Liquid cooling and power supplies in mass production.
  - A reported MOU with Marvell for DSPs.
  — [ifeng, 4 Nov 2026](https://finance.ifeng.com/c/8xmRAHlvGpt); [Sina](https://finance.sina.com.cn/roll/2026-10-30/doc-iniwxqym8566902.shtml)
- (b) Self-media claims ~60% of GB200 copper modules ("supply-chain information", unverified) — [Zhihu snippet](https://zhuanlan.zhihu.com/p/2079096896665272736)

#### Bizlink (3665.TW)
- (d) Q2 2026 (published 21 Aug 2026): revenue NT$23.28B (+37% YoY; +12% QoQ), gross margin 30.73%, operating margin 17.2%, net income NT$2.98B (net margin ~12.8%, derived), EPS NT$15.28. HPC was 42% of revenue, growing +67% YoY — [BigGo call summary](https://finance.biggo.com/news/TW_3665.TW_2026-08-21)
- (d) Q3 2026 revenue NT$27.854B (record; +19.6% QoQ; +51.3% YoY); nine-month NT$71.965B (+39.9%). Interplex Datacom (AI server and cabinet busbars; capacity in China, Vietnam, Thailand and Malaysia) consolidated from 23 Sep 2026; price undisclosed — [cnyes, 5 Oct 2026](https://news.cnyes.com/news/id/6621868)
- (a)/(b) Named in Credo's 10-K as Credo's AEC manufacturer and only long-term supply partner — [Credo 10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf). Its 800G AEC growth is reportedly driven by xAI and AWS Trainium 3 (secondary) — [cnyes/Yahoo TW summary](https://tw.stock.yahoo.com/news/%E8%B2%BF%E8%81%AF9%E6%9C%88%E7%87%9F%E6%94%B6%E5%9B%9E%E5%8D%87-q3%E5%AF%AB%E5%96%AE%E5%AD%A3%E6%96%B0%E9%AB%98%E5%AD%A3%E5%A2%9E%E8%BF%912%E6%88%90-112407089.html) (search snippet)
- (e) Management "will not add capacity simply because demand is strong" and may decline low-return business (company) — [BigGo](https://finance.biggo.com/news/TW_3665.TW_2026-08-21)

#### Others, briefly
- MaxLinear: Q3 2026 revenue $218.1M (+72% YoY); infrastructure +210% (secondary). Its Rushmore 1.6T AEC DSP design win ships H1 2027 — [Stocktwits](https://stocktwits.com/news-articles/markets/equity/crdo-stock-hits-6-month-low-after-max-linear-targets-credo-dominated-cable-market/cZxyk1CRBxY)
- Marvell: Alaska A 1.6T (8x200G) AEC DSP has been generally available since OFC 2025, with up to 7 m at 800G and >3 m at 1.6T in-rack. Ecosystem partners include Amphenol, TE, Luxshare-Tech, Broadex and 3M (secondary) — [InsideDeepTech, 9 Sep 2026](https://www.insidedeeptech.com/active-electrical-cables-aec-ai-data-centers-full-guide/)
- Woer/Lettin: FY2025 communications cable revenue RMB 2.551B (+49.83%), of which high-speed cable RMB 1.017B (+237.99%) (company investor Q&A, via search snippet) — [broker PDF](https://pdf.dfcfw.com/pdf/H3_AP202605081822068042_1.pdf); [Gelonghui](https://m.gelonghui.com/live/2594403)

### Inferences
- (a) Judge or constraint. No key company owns a judge; NVIDIA and the hyperscalers own the qualification gate. Credo's and Astera's positions are SerDes/DSP know-how plus incumbency on qualified platforms. Amphenol's and TE's are signal-integrity design and qualified high-volume manufacturing. Luxshare's and Bizlink's are capacity and cost. The genuinely scarce physical inputs in the midplane path are materials and high-layer PCB capacity (M9 CCL, quartz cloth, HVLP copper foil), which sit with laminate and PCB makers, not cable makers.
- (b) Lead. The strongest outside evidence is for Credo's AEC dominance (third-party and competitor estimates, plus filings that show Amazon, Microsoft and others as buyers) and for Amphenol's AI scale. Amphenol's implied AI-related sales were ~36% of Q3 sales, ~$3.7B in that quarter (derived: 0.75 × 48% × $10.23B, using a secondary 48% figure). TE's DDN was $975M for all of FY2026. Amphenol's IT datacom grew +77% organic in Q3 against DDN's +34% organic in TE's fiscal Q4, suggesting Amphenol is outgrowing TE in AI.
- (c) Revenue model. All six are effectively 100% one-off hardware. Customer warrants (Credo–Amazon from 2022; Astera's Feb 2026 warrant) tie volume to equity incentives but are not recurring revenue.
- (d) Concentration. Credo (top three end customers ~84%) and Astera (Customer A 53% in Q3) carry the highest single-customer risk in this report. Astera's rising concentration (23% to 53% year on year) shows a single platform ramp; inference: probably Scorpio X for one hyperscaler's custom accelerator, unconfirmed.
- (e) Cycle position. This looks like late expansion: book-to-bill above 1 (Amphenol 1.19; TE ~1.15, derived), rising inventories (Astera 3.4x since Dec 2025; Credo +$62M QoQ; Amphenol +54% including acquisitions), "longer dated orders", and backlog repricing. These are classic precursors of a digestion phase if customers' capex pauses. There is no direct evidence of double ordering.
- (e) Scenarios. These assessments are inference only.
  - Steady growth (~55%): all six grow. Copper content still rises through 2027–28 (TE: copper addressable market +100%; Rubin Ultra Kyber is all copper; AMD Helios is all copper).
  - Financing-led pause around 2028 (~25%): this coincides with the planned optical step (Feynman 2028). The concentrated, bridge-heavy names would be hit hardest: Credo (AEC), Astera (retimers, though Scorpio switching is media-agnostic) and Bizlink (AEC assembly). Amphenol and TE are cushioned by diversified end markets and strong FCF (TE $3.4B in FY2026; Amphenol $3.66B in the first nine months of 2026). Luxshare is cushioned by its scale but has thin margins and negative OCF. A pause could also delay the optical transition and extend copper's life.
  - Faster acceleration (~20%): optical scale-up arrives earlier. That favours firms already shipping optical products: Credo (FY27 optical revenue >$600M guided), Amphenol (CCS fibre) and Luxshare (800G/1.6T modules). It hurts pure copper suppliers (Woer, Bizlink AEC), although copper volumes also rise in the near term.
- (e) Export controls and geography. Astera bills 25% of revenue to China and 53% to Singapore. Credo ships 28% to Hong Kong. These are probably ODM and contract-manufacturer build locations for US hyperscalers (inference) and expose both to China trade measures. Credo depends wholly on TSMC. Luxshare, as a Chinese supplier to US platforms, is exposed to US restrictions (no source found).

### Gaps
- ROIC was not found for any company; cannot be computed reliably from the fetched data.
- Amphenol's and TE's largest-customer shares and geographic splits were not in the fetched excerpts. TE's FY2026 10-K was not retrieved (likely filed mid-November 2026).
- Luxshare's Q3 segment data and Bizlink's Q3 margins/EPS (Q3 report likely published ~mid-November 2026) were not retrieved.
- Lead times and pricing per cable were not disclosed by any company.
- No third-party retimer market share was found.

## 3. Path-forward evidence and suggested verdicts (transitions: 1 copper→optical; 2 pluggable→CPO; 3 hybrid bonding; 4 panel/glass; 5 two-phase cooling; 6 800 V DC / 1 MW racks)

### Takeaway
The firms best equipped for transition 1 are those that already ship on both sides of the bridge. Amphenol (copper connectors that survive a midplane, plus CommScope fibre and 800 V power) and Credo (AECs plus optical DSPs, ZF transceivers, DustPhotonics PICs and micro-LED cables) are funded and shipping. Astera's optical successor is still sampling; its Scorpio switches reduce its dependence on copper links. TE's optical steps are early and small. Luxshare claims a full copper/optical/thermal/power stack, mostly unconfirmed. Bizlink is a bridge-product assembler with small optical and power add-ons.

### Cited Findings
- Product classification (successor due dates from NVIDIA, as relayed in secondary sources). NVIDIA's GTC 2026 table, as relayed by a secondary source:
  - Rubin Ultra, Kyber NVL144: copper.
  - Rubin Ultra, Oberon NVL576: copper plus optical (CPO, two-level NVLink fabric).
  - Feynman, Kyber NVL1152: copper plus optical.
  - The Kyber cable cartridge is replaced by a passive midplane plus rear NVLink switch trays.
  — [Klockwood GTC 2026 recap, 23 Mar 2026](https://blog.glennklockwood.com/2026/03/gtc-2026-recap.html). Counterpoint (2 Apr 2026): Vera Rubin keeps an all-copper rack; scale-up moves to native CPO at Feynman (2028) — [Counterpoint](https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap)
- Slip record. SemiAnalysis (~5 Jul 2026) reported:
  - The Kyber NVL144 midplane PCB will slip more than 12 months, from 2027 to 2028.
  - NVL72x2 has been cancelled.
  - NVL576 CPO may be delayed or limited to small volumes.
  - The 4-die Rubin Ultra has been cancelled.
  NVIDIA (6 Jul 2026) said its roadmap is "intact" — [BigGo, 7 Jul 2026](https://finance.biggo.com/news/f253b550-28cf-463e-914f-d0e54c74ce15)
- Amphenol. SAID: more copper high-speed interconnect; optics significant in IT datacom; customers moving to "800 volt and beyond". DONE: CommScope CCS closed 9 Jan 2026, with its IT-datacom sales more than doubling in 2026 and glass supply secured; Dexgreen (fibre, pending); Empire, AdvancedPCB and Humanetics (~$1.6B including Dexgreen). FUNDED: 9M 2026 FCF $3.66B; net leverage 1.1x — [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/); [8-K](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926119421/aph-ex99d1.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926120646/aph-20260930x10q.htm). The Trexon acquisition (lead) is not mentioned in the Q3 2026 filings and was not verified.
- TE. SAID: both copper and fibre will be needed; power is "architecture-agnostic"; customers are experimenting with 800 V DC and liquid cooling. DONE: RAM Photonics (CPO fibre attach, engineering validation); ~$1.6B committed to optics and power-filtering bolt-ons (Astrodyne TDI pending); FY2026 acquisition cash only $212M. FUNDED: FCF $3.4B — [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/); [8-K](https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm)
- Credo. SAID: "connectivity from millimeters to kilometers ... optics and copper"; AEC growth will be slower than optics. DONE:
  - Hyperlume (micro-LED chip-to-chip optical) acquired 29 Sep 2025 for $92.0M (confirms lead).
  - DustPhotonics agreed 13 Apr 2026 for ~$750M cash plus ~0.92M shares and up to ~3.21M contingent shares; closed in Q1 FY27; first SiPh PIC revenue recognised.
  - ZF optics in production; record optical DSP revenue at 50G and 100G per lane; first 1.6T DSP revenue due later in FY27.
  - FY27 optical revenue guided >$600M.
  - ALC (micro-LED cables, up to 30 m) initial revenue targeted for FY28; NPO design wins to ramp in FY28.
  - 1.6T AEC (up to 6.5 m) contributes from late FY27.
  FUNDED: FY26 FCF ~$407M; $764M cash; no debt — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf); [call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/); [Investing.com](https://www.investing.com/news/company-news/credo-to-acquire-dustphotonics-for-750m-to-expand-optical-tech-93CH-4611185)
- Astera. SAID: some copper links move to optics in the next generation, raising content per link; scale-up optics is a ~$40B market by 2030 (company estimate); NPO revenue in H2 2027 (hundreds of dollars per accelerator); CPO volumes "mostly in the 2028, 2029 timeframe". DONE:
  - Smart optical drivers and TIAs for PCIe Gen7 NPO/LPO introduced at OCP; sampling Q4 2026.
  - Scorpio X switch is the largest product family.
  - Two 2026 asset acquisitions: $74.0M (9 Feb 2026, unnamed data-centre acceleration company) and one immaterial (29 May 2026).
  The aiXscale Photonics acquisition (lead) is not named in the 10-Q and was not verified. FUNDED: $1.38B cash; no debt; positive FCF — [call](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810); [10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm)
- Luxshare. SAID: CPC and XPO volume H2 2027; 448G modelling. DONE (company claims): 224G DAC/ACC and cable backplanes in production; 800G optical mass delivery; 1.6T batch production; liquid cooling (transition 5-adjacent) and power (transition 6) in mass production; "Xuanyuan 3.0" rack combining HVDC, liquid cooling and interconnect. FUNDING CAVEAT: nine-month operating cash flow −RMB 6.43B — [ifeng](https://finance.ifeng.com/c/8xmRAHlvGpt); [10jqka](http://stock.10jqka.com.cn/20261030/c681263349.shtml)
- Bizlink. DONE: Interplex Datacom busbars (power, transition 6), consolidated 23 Sep 2026; an "XFS acquisition adds optical connectivity" (company, per call summary; details not verified). It is Credo's AEC contract manufacturer — [cnyes](https://news.cnyes.com/news/id/6621868); [BigGo](https://finance.biggo.com/news/TW_3665.TW_2026-08-21); [Credo 10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf)

### Inferences
Verdicts are suggested, with the main reason for each.
- Amphenol — COHERENT. It must get through transitions 1, 2 and 6. It owns successor-side assets that are already shipping (CCS fibre, ~half of a $5.1B business in IT datacom in 2026) and power. Its high-speed connectors persist into midplane designs (reportedly Amphenol connectors; unverified). It is funded with ~$3.7B of nine-month FCF. Watch: the cable-cartridge revenue that a Kyber midplane removes, and acquisition leverage ($17.9B gross debt).
- Credo — COHERENT, with high execution and concentration risk. It must get through transitions 1 and 2. The bridge (AEC) has credible successors that are already shipping (optical DSPs, ZF optics, SiPh PICs) plus a funded long-shot (ALC, FY28). A 1–2 year optical slip extends AEC life, which Credo dominates, so a slip mostly helps. The risk is a simultaneous capex pause plus loss of share at 1.6T (MaxLinear, Marvell).
- Astera Labs — PARTLY COHERENT, trending to coherent. It must get through transition 1 (and 2 for its NPO/CPO parts). Its optical successor is only sampling (revenue H2 2027). Its Scorpio switching franchise is less exposed to the copper-to-optics switch than its retimers are. It is funded: net cash $1.38B with no debt.
- TE — PARTLY COHERENT. It must get through transitions 1, 2 and 6. Its optics moves are small and early (engineering validation); the AI business is ~5% of sales; balance sheet and FCF are strong. What must go right: converting the >$1B DDN growth guidance and winning share in CPO fibre attach.
- Luxshare — PARTLY COHERENT. It claims a stack across transitions 1, 2, 5 and 6, but the volume evidence is company-claimed. Margins are thin (~4.6% net) and nine-month OCF is negative, which constrains funding through a slip relative to its scale.
- Bizlink — PARTLY COHERENT. Its core AI product (AEC assembly) is a bridge. Its successor-side moves are power busbars (good for 800 V) and a small optical step. It is funded by profitable operations, with high exposure to a few AEC programmes (Credo, xAI, AWS; secondary).

### Gaps
- Funding and timing details for Luxshare's CPC/XPO and for Bizlink's XFS deal.
- Whether Amphenol supplies the Kyber midplane connectors (only speculation found).
- TE's RAM Photonics terms.
- Astera's aiXscale deal.
- Amphenol's Trexon deal.

## 4. Suggested ordering of key companies by quality alone

### Takeaway
1. Amphenol.
2=. Astera Labs and Credo (tie; cannot be separated on current evidence).
4. TE Connectivity.
5=. Bizlink and Luxshare (near-tie).

### Cited Findings
- Amphenol: adjusted operating margin 29.7%; organic growth 37% across a diversified base; IT datacom +77% organic; 9M FCF $3.66B; net leverage 1.1x; fibre and power successor assets already shipping — [8-K](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926119421/aph-ex99d1.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/)
- Astera: gross margin 72.3%, non-GAAP operating margin 44.7%, no debt; Customer A 53% of Q3 revenue; retimer bridge, but Scorpio switches now lead — [8-K](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm)
- Credo: FY26 gross margin ~68%, GAAP operating margin 33.3%, FCF ~30% of revenue, no debt; AEC share 88–99% (third-party/competitor); three end customers ~84%; optical successors shipping — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf); [CNBC](https://www.cnbc.com/2025/10/17/500-purple-cables-put-credo-in-middle-of-the-ai-boom.html)
- TE: adjusted operating margin 22.0%, FCF $3.4B, diversified; AI-exposed DDN only $975M (FY26) — [8-K](https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm)
- Bizlink: Q2 2026 gross margin 30.7%, operating margin 17.2% — [BigGo](https://finance.biggo.com/news/TW_3665.TW_2026-08-21). Luxshare: 9M net margin ~4.6% (derived), OCF −RMB 6.43B — [10jqka](http://stock.10jqka.com.cn/20261030/c681263349.shtml)

### Inferences
- Amphenol ranks first because it combines evidence of lead, diversification, owned successor assets and funding.
- Astera and Credo are tied. Both have exceptional economics and owned know-how, offset by extreme concentration and bridge exposure. Astera's mix is shifting to media-agnostic switching; Credo has stronger outside-confirmed share and already ships optical successors.
- TE ranks below the specialists on AI-specific position. A ranking that weights resilience more heavily could put TE above Credo and Astera.
- Bizlink versus Luxshare: Bizlink has better margins and a confirmed role, but is narrower and bridge-heavy. Luxshare is broader and larger, but margins are thin, cash flow negative and claims unconfirmed.

### Gaps
- ROIC was not available to separate the tied pairs.
- Retimer share data (Astera) is missing.
- Bizlink's Q3 profitability is not yet reported.

## 5. Check of background priors

### Takeaway
Prior 1 is CONFIRMED with updates. Copper scale-up holds through Rubin Ultra (2027). NVIDIA's first optical scale-up is planned in the Rubin Ultra generation for multi-rack NVL576 (2027, possibly small volume), mainstream at Feynman (2028). Suppliers place CPO volumes in 2028–29. Copper inside the rack persists even at Feynman. Prior 2 is PARTLY CONFIRMED and UPDATED. The reported Kyber slip, which NVIDIA denies, supports "bridges last longer". But absolute copper content is still growing fast into FY2027, and NVIDIA keeps copper inside Feynman racks, so copper's decline in 2028–30 is likely to be a loss of share within the rack, not a disappearance.

### Cited Findings
- Prior 1 ("copper stretched to 2027–28; optical between processors 2028, may slip to 2028–29").
  - NVIDIA's GTC 2026 table: Rubin Ultra Kyber NVL144 = copper; Rubin Ultra Oberon NVL576 = copper + optical; Feynman Kyber NVL1152 = copper + optical — [Klockwood, 23 Mar 2026](https://blog.glennklockwood.com/2026/03/gtc-2026-recap.html). Feynman (2028) brings native CPO scale-up — [Counterpoint, 2 Apr 2026](https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap).
  - Astera expects CPO volumes "mostly in the 2028, 2029 timeframe" and NPO revenue in H2 2027 (3 Nov 2026) — [call](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810). Credo expects NPO ramps and ALC revenue in FY28, i.e. May 2027 to April 2028 (Sep 2026) — [call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/). Luxshare expects CPC/XPO volume in H2 2027 — [ifeng](https://finance.ifeng.com/c/8xmRAHlvGpt).
  - Vera Rubin (all-copper Oberon NVL72) entered full production in May 2026, with first deployments in Sep 2026 (NVIDIA newsroom and blog, as cited) — [Wikipedia, last edited 17 Oct 2026](https://en.wikipedia.org/wiki/Rubin_(microarchitecture)).
  - AMD Helios (all-copper rear cartridges, UALink over Ethernet) began shipping at the end of Q3 2026, ramping into 2027 — [Fierce Network](https://www.fierce-network.com/cloud/amds-helios-bets-ai-networking-open-ethernet); [itdaily](https://itdaily.com/blogs/datacenter/amd-helios-analysis)
- Prior 2 ("bridging hardware loses share 2028–30; successors slip, bridges last longer").
  - SemiAnalysis reported Kyber's midplane slipping to 2028 and NVL576 CPO possibly limited; NVIDIA denied any delay (Jul 2026) — [BigGo](https://finance.biggo.com/news/f253b550-28cf-463e-914f-d0e54c74ce15).
  - Kyber is now "half as dense as originally announced", with 36 compute sleds instead of 72 — a scope-down — [Klockwood](https://blog.glennklockwood.com/2026/03/gtc-2026-recap.html).
  - Copper is still growing: TE says the copper addressable market is growing >100% and expects DDN to add >$1B in FY27 — [TE call](https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/). Amphenol expects IT datacom to more than double in FY2026 — [Amphenol call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/).
  - Credo itself expects AEC growth to be slower than optics going forward — [Credo call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/).

### Inferences
- Update to prior 1: the first optical scale-up product is nominally 2027 (Rubin Ultra NVL576 on Oberon), not 2028. Its reported fragility and the suppliers' 2028–29 CPO volume view keep the prior's centre of gravity right.
- Update to prior 2: there are two successor paths to copper cables, and they slip separately.
  - The board midplane (Kyber) replaces cable assemblies but is still copper.
  - Optical scale-up replaces copper links.
  A midplane slip prolongs cable cartridges (good for cable assemblers). An optical slip prolongs all copper (good for Credo, Amphenol and TE).

### Gaps
- No independent forecast of copper versus optical attach rates for 2028–30 was found (650 Group and LightCounting numbers for 2026 were not accessible).
- NVIDIA's own confirmation of Kyber timing beyond "roadmap intact" was not found.

## 6. Open question: which successor ships in volume first; specialists or integrated giants

### Takeaway
On current evidence, the first successors in volume are copper-on-copper upgrades and short-reach linear optics in 2027: 1.6T AECs, co-packaged copper (CPC) and NPO/LPO at the NIC. Board midplanes follow in 2027–28 (Kyber, if not delayed). Laser-based CPO scale-up comes in 2028–29, and micro-LED cables in FY28 and later. Specialists are capturing the highest-margin growth now. Integrated giants are consolidating optics: Marvell–Lumentum; Amphenol–CommScope; Credo's own vertical integration with DustPhotonics. Inference: value in the optical era will accrue to firms owning silicon plus photonics (DSPs, drivers, PICs, lasers) and to switch owners (NVIDIA CPO), with connector houses keeping fibre connectivity.

### Cited Findings
- Timing:
  - 1.6T AEC: Credo from late FY27 — [Credo call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/); MaxLinear's first design win ships H1 2027 — [Stocktwits](https://stocktwits.com/news-articles/markets/equity/crdo-stock-hits-6-month-low-after-max-linear-targets-credo-dominated-cable-market/cZxyk1CRBxY).
  - CPC: Luxshare H2 2027 — [ifeng](https://finance.ifeng.com/c/8xmRAHlvGpt).
  - NPO: Astera H2 2027 — [Astera call](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810).
  - LPO at the NIC on Vera Rubin — [Counterpoint](https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap).
  - CPO scale-up: Feynman 2028 — [Counterpoint](https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap); volume 2028–29 — [Astera call](https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810).
  - ALC: FY28 — [Credo call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/).
- Reach physics. Passive DAC reaches ~2–3 m at 800G (112G per lane) and ~1 m at 1.6T. AECs reach 4–7 m at 800G and >3 m in-rack at 1.6T (Marvell); Credo claims up to 6.5 m — [InsideDeepTech](https://www.insidedeeptech.com/active-electrical-cables-aec-ai-data-centers-full-guide/); [Credo call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/).
- OIF's LR reach was 1 m at 224G; at 448G it is TBD, with the target "beyond one meter of passive reach". Projects: CEI-448G-VSR and CEI-448G-LR started Feb 2026; framework published 6 Nov 2025; multi-vendor 448G demos at ECOC, 21–23 Sep 2026 — [OIF framework](https://www.oiforum.com/wp-content/uploads/OIF-FD-CEI-448G-01.0.pdf); [OIF current work](https://www.oiforum.com/technical-work/current-work/); [Converge Digest, 26 Aug 2026](https://convergedigest.com/oif-448g-800zr-cmis-ai-interoperability-ecoc-2026/).
- OIF President Nathan Tracy (TE): ≥1 m at 448G "may be achievable" but is "not a slam dunk". PAM4 at 448G needs ~112 GHz of channel bandwidth against ~100 GHz test channels; PAM6/PAM8 trade bandwidth for DSP and FEC complexity (Dec 2025) — [Gazettabyte](https://gazettabyte.com/448g-doing-what-has-been-done-before-may-no-longer-be-enough/).
- Consolidation:
  - Marvell–Lumentum, all-stock, announced 2 Nov 2026, close H1 2028 — [Light Reading](https://lightreading.com/ai-machine-learning/marvell-strikes-115b-deal-for-lumentum).
  - Amphenol–CommScope CCS closed 9 Jan 2026 — [10-Q](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926120646/aph-20260930x10q.htm).
  - Credo–DustPhotonics closed in Q1 FY27 — [Credo call](https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/).
- Growth comparison:
  - Q3 2026: Astera +154% YoY — [8-K](https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm); Amphenol IT datacom +77% organic — [call](https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/).
  - Q1 FY27: Credo +114.7% YoY — [8-K](https://www.sec.gov/Archives/edgar/data/0001807794/000162828026059795/credoq12027ex-991.htm).
  - FY2026: TE DDN +43.5% organic — [8-K](https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm).

### Inferences
- At 448G, passive copper shrinks to ~1 m or less, so copper increasingly needs active parts (retimers, AECs) or co-packaged copper. That lengthens the specialists' bridge even as optics becomes more competitive on cost per bit. Hypothesis: specialists win the 2027–28 window, and integrated electro-optical firms (Marvell–Lumentum, Credo with DustPhotonics, NVIDIA's own CPO) win 2028–30.
- Broad connector houses keep value where links stay copper (inside racks, midplanes, power) and through fibre connectivity (Amphenol CCS). Their risk is the cable-assembly content that midplanes and CPO remove.

### Gaps
- No 2026 third-party (LightCounting, Dell'Oro, 650 Group) quantification of AEC versus optics share was found.
- IEEE 802.3 positions on 400G per lane were not found.
- OCP Global Summit 2026 (Oct 2026) copper announcements are known only from company remarks.

## 7. What could not be verified

### Takeaway
The main unverified items are listed below. Several leads were confirmed: Hyperlume; CommScope CCS; Kyber passive midplane in NVIDIA's plan. Three were not verified this session: Trexon, aiXscale, Qualcomm–Alphawave.

### Cited Findings
- Confirmed leads:
  - Kyber passive midplane replacing the cable cartridge — [Klockwood](https://blog.glennklockwood.com/2026/03/gtc-2026-recap.html).
  - Amphenol–CommScope CCS (closed 9 Jan 2026) — [10-Q](https://www.sec.gov/Archives/edgar/data/0000820313/000110465926120646/aph-20260930x10q.htm).
  - Credo–Hyperlume (29 Sep 2025, $92.0M) — [10-K](https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf).
- New, not in the leads:
  - Credo–DustPhotonics (2026) — [Investing.com](https://www.investing.com/news/company-news/credo-to-acquire-dustphotonics-for-750m-to-expand-optical-tech-93CH-4611185).
  - Marvell–Lumentum (2 Nov 2026) — [Light Reading](https://lightreading.com/ai-machine-learning/marvell-strikes-115b-deal-for-lumentum).
  - Bizlink–Interplex Datacom (Sep 2026) — [cnyes](https://news.cnyes.com/news/id/6621868).
  - TE's RAM Photonics and Astrodyne TDI — [TE call](https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/).

### Inferences
- The concentration of evidence on US-listed firms reflects which sources were reachable before the search budget ran out, not where the industry sits.

### Gaps
- Leads not verified:
  - Amphenol–Trexon (not in the Q3 2026 filings).
  - Astera–aiXscale Photonics (not named in the Q3 2026 10-Q; the 2026 deals are unnamed).
  - Qualcomm–Alphawave (not searched).
- Market data not found:
  - NVIDIA supplier shares for cable backplanes and overpass cables (only conflicting Chinese secondary claims: Amphenol ~70% or "exclusive"; Luxshare ~60%).
  - Retimer shares (Astera, Broadcom, Marvell, Montage, Parade).
  - Copper content per rack in dollars. The copper cable count for NVL72 (~5,000+) is from earlier NVIDIA material not re-fetched; a Chinese snippet quotes 5,184. SemiAnalysis estimates a cable-based Kyber would need >20,000 cables — [Macrostream](https://www.macrostream.ai/articles/6a4af3b43c80f748cb632c76).
- Hyperscaler custom racks: AWS Trainium 3 AEC use is from secondary Bizlink reporting only; Google, Meta and Microsoft racks were not researched.
- Company coverage:
  - Japan (Sumitomo, Proterial, Junkosha, Hirose, JAE, Yamaichi, I-PEX), Korea and India: not researched (budget). TDnet, EDINET, DART, NSE and BSE were not accessed.
  - FIT Hon Teng (HKEXnews), Lotes and Bizlink Q3 profit (MOPS), Woer/Zhaolong/Kingsignal/Huafeng Q3 reports (cninfo): not retrieved.
  - Molex, Samtec and Rosenberger (private): no data.
- Standards: IEEE 802.3 400G-per-lane status and the OCP 2026 copper roadmap were not found.
- Amphenol customer and geographic concentration and ROIC for all companies: not found.

## 8. Sources (URL; date of publication; type)

### Takeaway
Primary sources dominate for the US-listed firms (SEC 8-K, 10-Q, 10-K, call transcripts). Chinese and Taiwanese evidence is secondary (financial press and self-media citing company reports).

### Cited Findings
- Amphenol Q3 2026 press release (8-K ex99.1), 28 Oct 2026, primary — https://www.sec.gov/Archives/edgar/data/0000820313/000110465926119421/aph-ex99d1.htm
- Amphenol 10-Q, quarter to 30 Sep 2026, filed ~29 Oct 2026, primary — https://www.sec.gov/Archives/edgar/data/0000820313/000110465926120646/aph-20260930x10q.htm
- Amphenol Q3 2026 call transcript, 28 Oct 2026, transcript (AI-assisted, may contain errors) — https://www.fool.com/earnings/call-transcripts/2026/10/28/amphenol-aph-q3-2026-earnings-call-transcript/
- BigGo Finance on the Amphenol Q3 2026 call, 28 Oct 2026, secondary — https://finance.biggo.com/news/US_APH_2026-10-28
- TE Connectivity Q4 FY2026 press release (8-K ex99.1), 28 Oct 2026, primary — https://www.sec.gov/Archives/edgar/data/0001385157/000110465926119326/tel-ex99d1.htm
- TE Q4 FY2026 call transcript, 28 Oct 2026, transcript — https://www.fool.com/earnings/call-transcripts/2026/10/28/te-connectivity-tel-q4-2026-earnings-call-transcript/
- Credo FY2026 Form 10-K (year to 2 May 2026), ~Jun 2026, primary — https://s205.q4cdn.com/511065572/files/doc_financials/2026/q4/a4179788-9dac-4cf3-9082-3e17792eb967.pdf
- Credo Q1 FY27 press release (8-K ex99.1), 1 Sep 2026, primary — https://www.sec.gov/Archives/edgar/data/0001807794/000162828026059795/credoq12027ex-991.htm
- Credo Q1 FY27 call transcript, ~1–8 Sep 2026, transcript — https://www.fool.com/earnings/call-transcripts/2026/09/08/credo-crdo-q1-2027-earnings-call-transcript/
- Credo–DustPhotonics deal, Apr 2026, secondary — https://www.investing.com/news/company-news/credo-to-acquire-dustphotonics-for-750m-to-expand-optical-tech-93CH-4611185 ; https://www.timesofisrael.com/us-based-credo-tech-snaps-up-israeli-maker-of-silicon-chips-for-up-to-1-3-billion/
- Credo customer concentration history (Q3 and Q4 FY26), 2026, secondary — https://www.metatrader.com/en/news/1742802-credos-diversification-push-can-it-cut-customer-concentration
- Astera Labs Q3 2026 press release (8-K ex99.1), 3 Nov 2026, primary — https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000044/q326exhibit991.htm
- Astera Labs 10-Q, quarter to 30 Sep 2026, Nov 2026, primary — https://www.sec.gov/Archives/edgar/data/0001736297/000173629726000045/alab-20260930.htm
- Astera Labs Q3 2026 call transcript, 3 Nov 2026, transcript — https://www.investing.com/news/transcripts/earnings-call-transcript-astera-labs-tops-q3-2026-estimates-on-record-revenue-93CH-4996810
- FourWeekMBA on the Astera warrant, Nov 2026, secondary — https://fourweekmba.com/ai-amazon-warrant-cut-asteras-q3-sales-18m-9-6x-a-year-ago/
- Luxshare Q3 2026 coverage, 30 Oct–4 Nov 2026, secondary — http://stock.10jqka.com.cn/20261030/c681263349.shtml ; https://www.jiemian.com/article/15265992.html ; https://finance.sina.com.cn/roll/2026-10-30/doc-iniwxqym8566902.shtml ; https://finance.ifeng.com/c/8xmRAHlvGpt
- Bizlink Q3 2026 revenue (cnyes), 5 Oct 2026, secondary — https://news.cnyes.com/news/id/6621868 ; Q2 2026 call summary (BigGo), 21 Aug 2026, secondary — https://finance.biggo.com/news/TW_3665.TW_2026-08-21
- MaxLinear Q3 2026 call coverage, 22–23 Oct 2026, secondary — https://stocktwits.com/news-articles/markets/equity/crdo-stock-hits-6-month-low-after-max-linear-targets-credo-dominated-cable-market/cZxyk1CRBxY
- CNBC on Credo and the 650 Group share estimate, 17 Oct 2025, secondary — https://www.cnbc.com/2025/10/17/500-purple-cables-put-credo-in-middle-of-the-ai-boom.html
- InsideDeepTech AEC guide, 9 Sep 2026, secondary — https://www.insidedeeptech.com/active-electrical-cables-aec-ai-data-centers-full-guide/
- Marvell–Lumentum: Light Reading, Nov 2026, secondary — https://lightreading.com/ai-machine-learning/marvell-strikes-115b-deal-for-lumentum ; Lumentum 8-K ex99.2, Nov 2026, primary — https://www.sec.gov/Archives/edgar/data/0001633978/000119312526442758/d163169dex992.htm
- Glenn Klockwood GTC 2026 recap, 23 Mar 2026, secondary (relays NVIDIA slides) — https://blog.glennklockwood.com/2026/03/gtc-2026-recap.html
- Counterpoint NVIDIA optics roadmap, 2 Apr 2026, secondary/analyst — https://counterpointresearch.com/en/insights/from-blackwell-to-feynman-analyzing-nvidias-optics-roadmap
- BigGo on the Kyber delay report and NVIDIA's denial, 7 Jul 2026, secondary — https://finance.biggo.com/news/f253b550-28cf-463e-914f-d0e54c74ce15 ; Macrostream (SemiAnalysis claims), Jul 2026, secondary — https://www.macrostream.ai/articles/6a4af3b43c80f748cb632c76
- Wikipedia, Rubin microarchitecture (last edited 17 Oct 2026; cites NVIDIA newsroom and blog), tertiary — https://en.wikipedia.org/wiki/Rubin_(microarchitecture)
- AMD Helios coverage, Q3–Q4 2026, secondary — https://www.fierce-network.com/cloud/amds-helios-bets-ai-networking-open-ethernet ; https://itdaily.com/blogs/datacenter/amd-helios-analysis
- OIF CEI-448G framework, 6 Nov 2025, primary standards body — https://www.oiforum.com/wp-content/uploads/OIF-FD-CEI-448G-01.0.pdf ; OIF current work page, 2026 — https://www.oiforum.com/technical-work/current-work/
- Converge Digest on OIF at ECOC 2026, 26 Aug 2026, secondary — https://convergedigest.com/oif-448g-800zr-cmis-ai-interoperability-ecoc-2026/
- Gazettabyte on 448G, 20 Dec 2025, secondary (OIF officers quoted) — https://gazettabyte.com/448g-doing-what-has-been-done-before-may-no-longer-be-enough/
- Eastmoney self-media on A-share Rubin suppliers, 28 Aug 2026, self-media — https://caifuhao.eastmoney.com/news/20260828173839122825400
- Chinese copper supply-chain claims (search snippets; pages blocked or unavailable), various 2025–2026 dates, self-media/broker — https://www.eet-china.com/mp/a300961.html ; https://zhuanlan.zhihu.com/p/2079096896665272736 ; https://www.jdon.com/83082-Kyber-Amphenol-Paladin-HD2-NVLink.html ; https://www.cls.cn/detail/1828472
- Woer (Lettin) broker report and Q&A (search snippets; not opened), May–Aug 2026, broker/company Q&A — https://pdf.dfcfw.com/pdf/H3_AP202605081822068042_1.pdf ; https://m.gelonghui.com/live/2594403

### Inferences
- Figures from the call transcripts should be cross-checked against the audio or filings where they are load-bearing; the Amphenol transcript is flagged as AI-assisted.

### Gaps
- MOPS, HKEXnews, cninfo full-text, TDnet/EDINET and DART filings were not accessed directly.

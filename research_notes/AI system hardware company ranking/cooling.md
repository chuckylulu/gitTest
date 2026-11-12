# Cooling for AI data-centre racks and chips (worldwide): research notes as of 12 November 2026

**Scope.** Cold plates and manifolds, coolant distribution units (CDUs), quick disconnects (QDs), two-phase direct-to-chip (DTC) and immersion cooling, coolants, thermal interface materials (TIMs), and in-chip or in-package cooling. Rack power (800 VDC, power shelves) is left to the power researcher.

**Conventions.**
- Each figure gives the period it covers and its publication date.
- "Company claim, unconfirmed" marks statements no outside party has confirmed.
- "(secondary)" marks trade press, blogs and analyst estimates.
- "(derived)" marks my own arithmetic on sourced figures.
- No share prices, valuation multiples, market capitalisation or price targets are used.

**Method note (read first).** Partway through, the shared WebSearch budget for this turn ran out, and both Exa and Firecrawl were out of credits.
- Before that point I used web search.
- After it, I only fetched pages already found or primary filings directly: SEC EDGAR 10-Q, 10-K and 8-K documents fetched with curl, and the OCP white paper PDF.
- In a second pass I used fixed-address data endpoints:
  - Taiwan exchange open data (TWSE/TPEx OpenAPI, built from MOPS filings; primary): October 2026 monthly revenue, and 9M 2026 income statements and balance sheets.
  - Eastmoney's financial-report API (secondary aggregator of company Q3 2026 reports): mainland China.
  - stockanalysis.com statistics pages (secondary aggregator): trailing-twelve-month (TTM) return on capital. Only return and margin fields were taken; all valuation fields were ignored.
- Coverage of Japan, Korea, India, European privates, TIM suppliers and QD makers is still thin (see section 7).
- Rows in the segment map marked "not re-verified" rest on prior knowledge and need checking.

---

## (1) Segment map

### Takeaway
- **Consolidation.** In the 12 months to November 2026 the segment consolidated into power and HVAC groups and one water-chemicals group:
  - Eaton closed Boyd Thermal for $9.55bn on 12 March 2026.
  - Ecolab closed CoolIT for $4.75bn on 2 July 2026.
  - Trane completed LiquidStack (March 2026) and bought Stellar Energy.
  - Johnson Controls (JCI) bought Alloy Enterprises.
  - Vertiv bought PurgeRite for $1.14bn, plus Strategic Thermal Labs and King Environmental Services.
- **Remaining independents.** Vertiv is the largest. The high-margin Taiwanese component makers are AVC and Auras. Envicool is the main mainland Chinese name. The two-phase start-ups (Accelsius, ZutaCore) remain small and dependent on outside capital.
- **Third-party share evidence.** Dell'Oro (January 2026) names Vertiv as leader, with CoolIT, nVent and Boyd strong and AAON fast-rising.

### Cited Findings: segment map table

Note: "Verified" means this session found a dated 2026 source for the row's key claim. "Not re-verified" means the role is from prior knowledge and must be checked.

| Company | Home | Listing / ticker | Role in segment | Why it matters / status (dated, sourced) | Verified |
|---|---|---|---|---|---|
| Vertiv | US | NYSE: VRT | Full thermal chain: chillers, CDUs, cold-plate design (via STL), fluid services, plus power | Dell'Oro (8 Jan 2026) names it liquid-cooling leader. Q3 2026 sales $4.31bn, +61% — [Dell'Oro PR](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html); [Vertiv Q3 PR](https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-Third-Quarter-2026-with-Net-Sales-Growth-of-61-Organic-Orders-Growth-over-100-and-Diluted-EPS-Growth-of-91-Adjusted-Diluted-EPS-Growth-of-78-Raises-Full-Year-2026-Guidance-Across-All-Key-Metrics/) | Y |
| Asia Vital Components (AVC, 奇鋐) | Taiwan | TWSE: 3017 | Cold plates (single- and double-sided), 3D vapour chambers, chassis; CDUs sampling in the US and Europe; consolidates Fositek (QDs and hinges) | Q3 2026 gross margin 33.86%, operating margin 28.53%. About 1M cold plates per month. Names NVIDIA and AMD as GPU customers — [vocus notes 10 Nov 2026](https://vocus.cc/article/6af3cc73fd89780001cc407d) | Y |
| Auras (雙鴻) | Taiwan | TPEx: 3324 | Cold plates, manifolds, CDUs | Q3 2026 gross margin 25.65%, down on new-product ramps. Expected to be on NVIDIA's "Group A" cold-plate supplier list (company expectation, Nov 2025) — [CTEE 11 Nov 2026](https://www.ctee.com.tw/news/20261111701940-430503); [udn 14 Nov 2025](https://money.udn.com/money/story/5612/9140567) | Y |
| Jentech (健策) | Taiwan | TWSE: 3653 (listed in TWSE open data) | Integrated heat spreaders and lids; candidate for micro-channel lids (MCL) | Highest margins in the segment. 9M 2026: revenue NT$22.07bn, gross margin 46.96%, operating margin 36.22%, net margin 30.04%. Oct 2026 revenue NT$3.07bn, +80.7% y/y; Jan–Oct +50.5% — [TWSE open data t187ap17](https://openapi.twse.com.tw/v1/opendata/t187ap17_L); [t187ap05](https://openapi.twse.com.tw/v1/opendata/t187ap05_L). Reported (secondary) as sampling MCL to NVIDIA with Auras and AVC — [Digitimes 12 Sep 2025](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000732415_G4K58U450ZCNXZ6RERD9C) | Y |
| Fositek (富世達) | Taiwan | TWSE: 6805; AVC subsidiary | QDs (UQD) and hinges | 9M 2026: revenue NT$12.43bn, gross margin 34.90%, operating margin 29.16%. Oct 2026 revenue +26.5% y/y; Jan–Oct +44.5%. QD vs hinge split not disclosed — [TWSE t187ap17](https://openapi.twse.com.tw/v1/opendata/t187ap17_L); [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d) | Y |
| Delta Electronics (cooling) | Taiwan | TWSE: 2308 | CDUs (2.5 MW-class on 800 VDC), fans, cold plates; Google "Deschutes" CDU | Group 9M 2026: revenue NT$539.67bn, gross margin 35.47%, operating margin 16.97%; Oct 2026 revenue +30.1% y/y — [TWSE t187ap17](https://openapi.twse.com.tw/v1/opendata/t187ap17_L). Showed a 2.5 MW CDU at OCP 2026; plans Deschutes CDU mass production in 1Q 2027 — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/). Cooling share of group revenue not found | Partial |
| Sunon (建準) | Taiwan | TWSE: 2421 | Fans; liquid-cooling modules | 9M 2026: revenue NT$16.58bn, gross margin 31.91%, operating margin 16.63%; Jan–Oct revenue +20.9% — [TWSE t187ap17](https://openapi.twse.com.tw/v1/opendata/t187ap17_L) | Y |
| Nidec Chaun-Choung (尼得科超眾) | Taiwan (Nidec subsidiary) | TWSE: 6230 | Heat pipes and vapour chambers; thermal modules | Laggard: Oct 2026 revenue −10.9% y/y; Jan–Oct +4.3% — [TWSE t187ap05](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) | Y |
| Forcecon (力致) | Taiwan | TWSE: 3483 | Thermal modules | Laggard: Oct 2026 revenue −31.2% y/y; Jan–Oct −12.5% — [TWSE t187ap05](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) | Y |
| Cooler Master | Taiwan | Private | Cold plates; 2.5 MW floor CDU; refrigerant cold-plate loops in development | OCP 2026 exhibits — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Y (products only) |
| Kaori (高力) | Taiwan | TWSE: 8996 | Brazed plate heat exchangers, CDUs, manifolds | Fastest grower among Taiwan names: Oct 2026 revenue NT$1.52bn, +125.2% y/y; Jan–Oct NT$10.99bn, +121.4% — [TWSE t187ap05](https://openapi.twse.com.tw/v1/opendata/t187ap05_L). Margins not in the open-data profitability set | Partial |
| LITEON | Taiwan | TWSE: 2301 (not re-verified) | Agreed to take ~25% of DCX (Poland) for ~$176M (3 Sep 2026) | (secondary) — [newmarketpitch Oct 2026](https://newmarketpitch.com/blogs/news/data-center-cooling-funding-news) | Partial |
| Wiwynn / MiTAC | Taiwan | TWSE: 6669 / 3706 (not re-verified) | Server makers (ODMs) qualifying two-phase | Wiwynn two-phase white papers; MiTAC showed ZutaCore two-phase in its servers at OCP 2026 — [Wiwynn](https://www.wiwynn.com/whitepapers/general-guidance-for-transitioning-from-single-phase-to-two-phase-liquid-cooling-solutions); [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Partial |
| CoolIT Systems | Canada | Inside Ecolab (NYSE: ECL) since 2 Jul 2026 | CDUs (3 MW CHx3000), cold plates | Closed for $4.75bn. Customers include NVIDIA and AMD (Reuters). About $550M sales expected over the next 12 months (Mar 2026) — [Ecolab 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/31462/000162828026068208/ecl-20260930.htm); [The Star/Reuters 20 Mar 2026](https://www.thestar.com.my/tech/tech-news/2026/03/20/ecolab-to-buy-coolit-for-475-billion-to-tap-into-ai-data-center-boom) | Y |
| Boyd Thermal | US | Inside Eaton (NYSE: ETN) since 12 Mar 2026 | Cold plates, CDUs, thermal components | $9.55bn net of cash. $1,058M sales and $257M segment profit from 12 Mar to 30 Sep 2026 — [Eaton 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm) | Y |
| Motivair | US | 75% owned by Schneider Electric (Euronext: SU) | CDUs (branded "HDU"), cold plates | 75% stake reportedly bought for $850M, completed Feb 2025 (secondary) — [wetheflywheel](https://wetheflywheel.com/en/guides/data-center-cooling-companies-2026/); [Dell'Oro 30 Sep 2025](https://www.delloro.com/market-at-the-boiling-point-is-the-cdu-space-becoming-saturated/). Share of Schneider revenue not found | Partial |
| nVent | UK/US | NYSE: NVT | CDUs, manifolds, enclosures, modular liquid-cooling platform | Dell'Oro names it a strong-share vendor. Q3 2026 sales $1.515bn, +44% — [Dell'Oro PR](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html); [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/nvent-electric-nvt-q3-2026-earnings-call-transcript/) | Y |
| AAON (BASX) | US | Nasdaq: AAON | Custom data-centre cooling, including liquid-cooling CDUs and air handlers for hyperscalers | Dell'Oro: "grown rapidly through deep hyperscaler partnerships". BASX products +218% in Q3 2026. Restating Q1 and Q2 2026, material weakness — [AAON 10-Q](https://www.sec.gov/Archives/edgar/data/824142/000082414226000088/aaon-20260930.htm); [AAON 8-K 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/824142/000082414226000083/aaon-20261109.htm) | Y |
| Modine (Airedale) | US | NYSE: MOD | Chillers, CRAH/CRAC units, fan walls, coolant distribution | Data Centers segment sales +95% y/y in Jul–Sep 2026. Pure-play climate company since 1 Oct 2026 (Performance Technologies merged into Gentherm) — [Modine 10-Q](https://www.sec.gov/Archives/edgar/data/67347/000110465926122523/mod-20260930x10q.htm); [8-K 1 Oct 2026](https://www.sec.gov/Archives/edgar/data/67347/000110465926112870/tm2626618d1_8k.htm) | Y |
| Trane Technologies | Ireland/US | NYSE: TT | Chillers; liquid distribution; LiquidStack (DTC and immersion) | LiquidStack fully acquired (Mar 2026). Stellar Energy bought 17 Feb 2026 ($553.4M) — [Trane 10-Q](https://www.sec.gov/Archives/edgar/data/1466258/000162828026068122/tt-20260930.htm); [Pulse 2, 4 Mar 2026](https://pulse2.com/trane-technologies-liquid-cooling-firm-liquidstack-acquired-to-expand-data-center-thermal-management-solutions) | Y |
| LiquidStack | US (Texas; Hong Kong operations) | Inside Trane | DTC CDUs; single- and two-phase immersion | Small deal: bundled in $353.4M of acquisitions — [Trane 10-Q](https://www.sec.gov/Archives/edgar/data/1466258/000162828026068122/tt-20260930.htm) | Y |
| Johnson Controls | Ireland/US | NYSE: JCI | Chillers, Silent-Aire CDUs; bought Alloy Enterprises (DLC components) | Alloy plus Nantum AI ~$291M, closed Apr–Jun 2026. Led Accelsius' $65M Series B (Jan 2026) — [JCI 10-Q Jun 2026](https://www.sec.gov/Archives/edgar/data/833444/000083344426000087/jci-20260630.htm); [Facilities Dive](https://www.facilitiesdive.com/news/accelsius-two-phase-data-center-cooling-technology-deployed-at-training-cen/828954/) | Y |
| Carrier | US | NYSE: CARR | Chillers; investor in ZutaCore | Carrier Ventures in ZutaCore's $100M Series C (2 Jun 2026) — [datacenterrichness](https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase). No data-centre figures found in the 10-Q | Partial |
| Flex (JetCool) | Singapore/US | Nasdaq: FLEX | JetCool micro-convective cold plates and CDUs | Cloud and Power Infrastructure unit (including liquid cooling) to be spun off as "Axiom", expected 1Q CY2027 — [Flex 10-Q Sep 2026](https://www.sec.gov/Archives/edgar/data/866374/000086637426000042/flex-20260925.htm) | Y |
| Accelsius | US (Austin) | Private; controlled by Innventure (Nasdaq: INV) | Two-phase DTC (NeuCool), in-rack and multi-rack CDUs | First binding contract worth >$15M (Apr 2026). Parent has going-concern language and a Nasdaq bid-price notice. Accelsius has hired Evercore to raise capital — [Innventure 10-Q](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000154/innv-20260630.htm); [Innventure PR 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000202/inv-pressreleasefundingstr.htm) | Y |
| ZutaCore | US HQ / Israel R&D | Private | Waterless two-phase direct-to-die | $100M Series C (2 Jun 2026), ~$200M raised in total. Backers: Mitsubishi Electric, Carrier, Samsung Ventures. 75+ deployments; names Equinix, SoftBank, University of Münster — [datacenterrichness](https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase) | Y (secondary) |
| Submer | Spain | Private | Single-phase immersion | $55.5M round in Oct 2024. MoU for a 1 GW site in Madhya Pradesh (Jul 2025) (secondary) — [newmarketpitch](https://newmarketpitch.com/blogs/news/data-center-cooling-funding-news) | Partial |
| Iceotope | UK | Private | Chassis-level precision immersion | $26M Series B (May 2026; Two Seas Capital, Barclays Climate Ventures) — [TAMradar](https://www.tamradar.com/funding-rounds/iceotope-series-b-26m) | Partial |
| GRC | US | Private | Single-phase immersion | No 2026 data (secondary mentions only) | N |
| DCX Liquid Cooling Systems | Poland | Private | CDUs, DTC, immersion | LITEON investing ~$176M for ~25% (Sep 2026) (secondary) — [newmarketpitch](https://newmarketpitch.com/blogs/news/data-center-cooling-funding-news) | Partial |
| Rittal | Germany | Private (Friedhelm Loh) | Racks; in-house CDU above 1 MW; 2 MW 800 VDC sidecar demonstrator with Bosch | OCP 2026 — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Y (products only) |
| Stulz | Germany | Private | Precision air conditioning, CDUs | Not re-verified | N |
| Munters | Sweden | Nasdaq Stockholm: MTRS | Data-centre air handling and liquid cooling | Shares fell after AWS's in-house IRHX unveiling (Jul 2025) — [Dell'Oro 14 Jul 2025](https://www.delloro.com/awss-new-liquid-cooling-solution-rattled-the-market-but-is-it-truly-disruptive/). No 2026 figures gathered | Partial |
| Alfa Laval | Sweden | Nasdaq Stockholm: ALFA (not re-verified) | Heat exchangers for CDUs | Not re-verified | N |
| Danfoss | Denmark | Private | QDs, valves, pumps | Not re-verified | N |
| Stäubli | Switzerland | Private | QDs | Partner on CoolIT cold plates for pluggable optics (OCP 2026) — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Partial |
| CPC (Dover) | US | NYSE: DOV | QDs (inside Pumps & Process Solutions); Dover also sells heat exchangers (SWEP) | Q3 2026 10-Q: "accelerating demand for heat exchangers used in data center cooling". CPC not quantified — [Dover 10-Q](https://www.sec.gov/Archives/edgar/data/29905/000002990526000033/dov-20260930.htm) | Partial |
| Parker Hannifin | US | NYSE: PH | QDs, fluid connectors | 10-Q has no data-centre cooling disclosure — [Parker 10-Q](https://www.sec.gov/Archives/edgar/data/76334/000007633426000172/ph-20260930.htm) | Partial |
| Corintis | Switzerland | Private | Microfluidic cold plates; in-chip channel prototypes | Microsoft partner; $25M Series A1 led by Applied Digital (2 Dec 2025, secondary) — [IEEE Spectrum 17 Nov 2025](https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis) | Y |
| Microsoft | US | Nasdaq: MSFT | In-chip microfluidics R&D; Mt Diablo sidecar specs | See section 2 (in-chip) — [IEEE Spectrum](https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis) | Y |
| TSMC / Intel / Samsung (in-package cooling) | TW / US / KR | TWSE: 2330 / Nasdaq: INTC / KRX: 005930 | Research on silicon-integrated micro-coolers | No 2026 production commitment found (search budget exhausted) | N |
| Frore Systems | US | Private | Solid-state active cooling; liquid cold plates | At OCP 2026 — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Partial |
| Jabil | US | NYSE: JBL | Micro-channel cold plates | At OCP 2026 — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Partial |
| xFusion | China | Private | Diamond-copper cold plates; 300 kW–1.2 MW power prototype | At OCP 2026 — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Partial |
| Envicool (英维克) | China | SZSE: 002837 | CDUs, cold plates, QDs, precision air conditioning; Deschutes CDU | 9M 2026 revenue +22.9%, net profit −7.6%. Deschutes design shown at its OCP 2026 booth — [Sina 26 Oct 2026](https://finance.sina.com.cn/stock/zqgd/2026-10-26/doc-iniwpwiq2476322.shtml); [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Y |
| Shenling (申菱) | China | SZSE: 301018 | Data-centre air conditioning and liquid cooling | 9M 2026: revenue RMB3.43bn (+36.9%), net profit RMB142M (−5.4%), gross margin 19.6%, weighted ROE 5.1% (9M, not annualised) — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22301018%22)) (secondary) | Y |
| Goaland (高澜) | China | SZSE: 300499 | Liquid-cooling systems | 9M 2026: revenue RMB0.77bn (+30.5%), net profit RMB61M (+76.8%), gross margin 29.6% — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22300499%22)) (secondary) | Y |
| Sugon Digital Creation (曙光数创) | China | BSE (code now 920808) | Immersion and cold-plate cooling for Sugon | Weak: 9M 2026 revenue RMB325.5M (+16.7%), net loss RMB119.2M, gross margin 8.5%, weighted ROE −17.0% — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_NAME_ABBR%3D%22%E6%9B%99%E5%85%89%E6%95%B0%E5%88%9B%22)) (secondary) | Y |
| Tongfei (同飞) | China | SZSE: 300990 | Industrial and data-centre liquid-cooling units | 9M 2026: revenue RMB2.71bn (+30.4%), net profit RMB208M (+15.4%), gross margin 21.0% — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22300990%22)) (secondary). Data-centre share not known | Y |
| FRD (飞荣达) | China | SZSE: 300602 | Thermal modules, cold plates, TIMs | 9M 2026: revenue RMB5.77bn (+25.1%), net profit RMB423M (+47.9%), gross margin 21.3% — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22300602%22)) (secondary) | Y |
| Zhongshi Technology (中石科技) | China | SZSE: 300684 | TIMs and thermal materials | 9M 2026: revenue RMB1.50bn (+15.4%), net profit RMB285M (+13.1%), gross margin 33.5% — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22300684%22)) (secondary) | Y |
| Yinlun (银轮) | China | SZSE: 002126 | Thermal management, including data-centre liquid cooling | 9M 2026: revenue RMB13.96bn (+26.2%), net profit RMB638M (−5.0%), gross margin 17.9%. Mostly automotive; data-centre share not known — [Eastmoney API](https://datacenter.eastmoney.com/securities/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22002126%22)) (secondary) | Y |
| Huawei Digital Power | China | Private (Huawei) | Liquid-cooled data-centre infrastructure | Not re-verified | N |
| Lenovo (Neptune) | China/HK | HKEX: 0992 (not re-verified) | Warm-water DTC in own servers | Not re-verified | N |
| Daikin (Chilldyne) | Japan | TSE: 6367 (not re-verified) | Chillers; Chilldyne negative-pressure DTC (reported 2025 deal) | Deal not re-verified | N |
| Nidec | Japan | TSE: 6594 (not re-verified) | CDUs (3.2 MW in-row prototype), pumps, fans | OCP 2026 — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Partial |
| Mitsubishi Heavy Industries | Japan | TSE: 7011 (not re-verified) | Chillers; data-centre cooling | Not re-verified | N |
| Mitsubishi Electric | Japan | TSE: 6503 (not re-verified) | ZutaCore investor | [datacenterrichness 2 Jun 2026](https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase) | Partial |
| LG Electronics | Korea | KRX: 066570 (not re-verified) | Chillers, CDUs | Not re-verified | N |
| Samsung Electronics (FläktGroup) | Korea | KRX: 005930 | FläktGroup air and liquid cooling (reported 2025 deal); Samsung Ventures in ZutaCore | FläktGroup deal noted by Dell'Oro (30 Sep 2025) — [Dell'Oro](https://www.delloro.com/market-at-the-boiling-point-is-the-cdu-space-becoming-saturated/); closing not re-verified | Partial |
| Chemours | US | NYSE: CC | Opteon refrigerants; Opteon two-phase immersion fluid planned with Navin | 10-Q shows no two-phase fluid revenue. Securities class action over Opteon demand statements — [Chemours 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1627223/000162722326000035/cc-20260930.htm) | Y |
| Navin Fluorine | India | NSE: NAVINFLUOR (not re-verified) | Contract maker of Chemours' two-phase fluid (Surat) | Agreement May 2025; production said to start in 2026 (unconfirmed) — [Chemours PR May 2025](https://www.chemours.com/en/news-media-center/all-news/press-releases/2025/chemours-and-navin-fluorine-announce-agreement-to-manufacture-new-liquid-cooling-product) | Partial |
| Solstice Advanced Materials (ex-Honeywell) | US | SOLS | Low-GWP refrigerants; ex-Honeywell electronic materials (TIMs, not re-verified) | Spun off 30 Oct 2025. Q3 2026 refrigerant growth "driven primarily by data center demand" — [Honeywell 10-Q](https://www.sec.gov/Archives/edgar/data/773840/000077384026000143/hon-20260930.htm); [Solstice 10-Q](https://www.sec.gov/Archives/edgar/data/2064953/000206495326000100/sols-20260930.htm) | Y |
| 3M | US | NYSE: MMM | Former Novec/Fluorinert two-phase fluid supplier | Exit from PFAS manufacturing completed by end-2025 — [3M 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/66740/000006674026000311/mmm-20260930.htm) | Y |
| Indium Corporation | US | Private | Indium and liquid-metal TIMs | Not re-verified | N |
| Henkel / Shin-Etsu / Dexerials / Dow | DE / JP / JP / US | XETRA: HEN3 / TSE: 4063 / TSE: 4980 / NYSE: DOW (not re-verified) | TIMs, gap fillers, silicone fluids | Dow 10-Q has no data-centre cooling disclosure; others not re-verified — [Dow 10-Q](https://www.sec.gov/Archives/edgar/data/1751788/000175178826000160/dow-20260930.htm) | N |
| KühlTherm | India | Private | Cold plates, CDUs, rear-door heat exchangers, immersion | $1.1M seed (16 Jul 2026) (secondary) — [newmarketpitch](https://newmarketpitch.com/blogs/news/data-center-cooling-funding-news) | Partial |
| Refroid | India | Private | Liquid cooling (named in assignment) | Not re-verified | N |
| Ecolab | US | NYSE: ECL | Owner of CoolIT; fluid treatment and monitoring (3D TRASAR) | CoolIT CDU integrated with Ecolab fluid monitoring (OCP 2026) — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/) | Y |
| Legrand | France | Euronext: LR (not re-verified) | Accelsius investor | [Facilities Dive 27 Aug 2026](https://www.facilitiesdive.com/news/accelsius-two-phase-data-center-cooling-technology-deployed-at-training-cen/828954/) | Partial |
| AWS (in-house) | US | Nasdaq: AMZN | In-house IRHX in-row heat exchanger (Jul 2025), likely built by vendors | Dell'Oro: "not a threat" to vendors — [Dell'Oro 14 Jul 2025](https://www.delloro.com/awss-new-liquid-cooling-solution-rattled-the-market-but-is-it-truly-disruptive/) | Y |

### Inferences
- **Two business models.**
  - Western integrators (Vertiv, Schneider-Motivair, Eaton-Boyd, Ecolab-CoolIT, Trane, JCI, nVent) sell systems, services and facility-side heat rejection.
  - Taiwanese component makers (AVC, Auras, Jentech, Fositek, Cooler Master, Delta) supply cold plates, lids and QDs into the server supply chain, where NVIDIA increasingly sets designs and runs procurement.
- **The two-phase layer is thin.** It consists of start-ups (Accelsius, ZutaCore), sub-units of large groups (LiquidStack in Trane) and ODMs running qualification work (Wiwynn, MiTAC).

### Gaps
- No 2026 figures were gathered for:
  - Kaori, Jentech, Delta's cooling share, Schneider-Motivair revenue, Munters, Alfa Laval, Stulz, Rittal;
  - mainland China beyond Envicool;
  - Japan (Daikin/Chilldyne, Nidec, MHI) and Korea (LG, Samsung/FläktGroup closing);
  - TIM suppliers, and QD makers' market shares.
- Cause: the shared search budget was exhausted, and Chinese, Japanese and Korean home-market filings (cninfo, EDINET/TDnet, DART) were not reachable without search.

---

## (2) Evidence on tests (a)–(e) for key companies

Key companies chosen: **Vertiv, AVC, Boyd (Eaton), CoolIT (Ecolab), nVent, Auras, Envicool**. Accelsius and ZutaCore (two-phase) are covered briefly as successor-side bellwethers.

### Takeaway
- **Vertiv** has the best evidence on breadth, financial strength and recurring revenue:
  - Q3 2026 adjusted operating margin 25.2%; net cash.
  - Deferred revenue $4.12bn, up from $1.81bn at end-2025.
  - Services and spares about 20% of FY2025 sales.
  - It stopped disclosing orders after Q3 2026.
- **AVC** has the strongest margins among the component makers (Q3 2026 operating margin 28.5%) and scale (about 1M cold plates per month). Its product is a bridge, and it carries rising inventory (160 days).
- **Boyd and CoolIT** now sit inside Eaton and Ecolab. Boyd earned a ~24% segment margin over its first ~6.5 months under Eaton.
- **Auras and Envicool** show margin pressure, and profit lagging revenue, during ramp-ups.

### Cited Findings

#### Vertiv (NYSE: VRT)

**(a) Position**
- Vertiv owns no chip-level "judge". Its strengths are physical capacity and system integration:
  - chiller capacity to double by end-2026;
  - a Johor (Malaysia) plant;
  - expansions in Slovakia and Ireland;
  - "long-term capacity agreements" with suppliers.
  - [Q3 2026 call, 28 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/)
- It bought Strategic Thermal Labs (cold-plate design and server-side validation) in April 2026, which brings it closer to a validation role — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- Product classes:
  - CDUs for single-phase loops: BRIDGE-to-neutral.
  - Chillers and heat rejection: successor-neutral.
  - Fluid services (PurgeRite, King Environmental Services): successor-neutral and recurring.

**(b) Lead**
- Dell'Oro (8 Jan 2026): "Vertiv leading the liquid cooling market" — [PR Newswire](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html)
- An 11.3% (2025) share attributed to Dell'Oro appears only on secondary sites; unverified — [Enki AI](https://enkiai.com/data-center/vertiv-liquid-cooling-microsoft/)
- Vendor-reported 30 MW DTC deployment at CapitaLand Mumbai for an unnamed hyperscaler (16 Oct 2026; company claim, unconfirmed; secondary) — [wetheflywheel](https://wetheflywheel.com/en/guides/data-center-cooling-companies-2026/)

**(c) Revenue model**
- FY2025 net sales $10,229.9M: products $8,207.0M, services and spares $2,022.9M.
  - Services share (derived): 19.8% in FY2025, 22.0% in FY2024, 23.2% in FY2023. The share is falling as product sales boom.
  - [10-K FY2025, filed 13 Feb 2026](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm)
- Services and spares +62% y/y in Q3 2026 (call summary) — [Yahoo summary](https://finance.yahoo.com/markets/stocks/articles/vertiv-holdings-co-q3-2026-005035648.html)
- Deferred revenue $4,120.5M at 30 Sep 2026 vs $1,814.7M at 31 Dec 2025. Customer prepayments more than doubled — [10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm)
- Acquisitions add fluid services, an attach and recurring stream:
  - PurgeRite, total consideration $1,138.3M, closed 4 Dec 2025 — [10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm)
  - King Environmental Services (fluid management and load testing), announced 24 Sep 2026 — [8-K](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026063311/exhibit991vrt-q320269242026.htm)
- Customers order 12–18 months ahead. Backlog counts only purchase orders, not capacity agreements — [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/)

**(d) Financial strength**
- Q3 2026 (quarter to 30 Sep, published 28 Oct 2026) — [Vertiv Q3 2026 PR](https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-Third-Quarter-2026-with-Net-Sales-Growth-of-61-Organic-Orders-Growth-over-100-and-Diluted-EPS-Growth-of-91-Adjusted-Diluted-EPS-Growth-of-78-Raises-Full-Year-2026-Guidance-Across-All-Key-Metrics/):
  - net sales $4,312.8M (+61.2%; organic +55.0%);
  - gross margin about 38.1% (derived from release);
  - GAAP operating profit $983.8M (22.8%); adjusted $1,086.9M (25.2%);
  - net income $764.5M;
  - operating cash flow $794.0M; capex $139.1M; adjusted FCF $652.2M;
  - cash $3,512.9M plus $198.8M short-term investments, against debt about $2,928.5M (net cash about $0.78bn, derived); liquidity $6.2bn.
- FY2026 guidance (28 Oct 2026), same source:
  - net sales $14.45–14.85bn (organic +37–39%);
  - adjusted operating margin 23.5–24.5%;
  - adjusted FCF $2.6–2.8bn;
  - capex about 4% of revenue.
- Organic orders more than doubled y/y in Q3 2026. Management is "not planning to share orders data going forward" — [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/)
- Last disclosed backlog: $15.0bn at Q4 2025, +109% y/y (per search summary of the Feb 2026 8-K) — [Vertiv 8-K 11 Feb 2026](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000006/exhibit991vrt02112026.htm)
- Geography:
  - Q3 2026: Americas $2,988.8M (adjusted operating margin 29.4%), APAC $779.3M (17.0%), EMEA $544.7M (28.0%) — [Q3 PR](https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-Third-Quarter-2026-with-Net-Sales-Growth-of-61-Organic-Orders-Growth-over-100-and-Diluted-EPS-Growth-of-91-Adjusted-Diluted-EPS-Growth-of-78-Raises-Full-Year-2026-Guidance-Across-All-Key-Metrics/)
  - FY2025: Americas $6,386.3M (62%), APAC $2,019.2M, EMEA $1,824.4M — [10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm)
- Footprint: about 300 offices and plants in 40+ countries; about 34,000 employees — same 10-K.
- Customer concentration: no percentages disclosed. The 10-K says large cloud/hyperscale, neocloud and colocation customers "comprise a material portion of our customer base" and have leverage that can produce "downward pricing pressures" — same 10-K.
- Working capital: 9M 2026 inventories rose by $1,814.9M and receivables by $1,276.1M, offset by +$2,312.9M deferred revenue — [10-Q](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm)
- Returns (TTM to Q3 2026, data date 12 Nov 2026) — [stockanalysis](https://stockanalysis.com/stocks/vrt/statistics/) (secondary):
  - ROIC 43.8%; ROE 46.6%; ROCE 29.3%;
  - FCF margin 24.0%; TTM revenue $13.12bn; TTM FCF $3.15bn;
  - total debt including leases $3.36bn; net cash $0.35bn.
- Total equity $5,502.0M at 30 Sep 2026 (vs $3,941.3M at 31 Dec 2025) — [10-Q](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm)

**(e) Resilience**
- Tariffs:
  - The US Supreme Court invalidated IEEPA tariffs in February 2026; customs refunds are being processed in phases (from April and June 2026) — [10-Q](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm)
  - Management expects positive price-cost in 2026 including tariffs — [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/)
- Pacing items cited are power availability, permitting, sentiment and skilled labour, "not slowing growth" — same call.
- The 10-K flags low-cost Chinese and Indian manufacturers as potential competitors — [10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm)

#### Asia Vital Components (AVC, TWSE: 3017)

**(a) Position**
- AVC's position is physical manufacturing capacity and process know-how (machining, brazing and plating of copper cold plates).
- Cold-plate capacity is about 1M units per month, to grow more than 50% in 2027, mainly in Vietnam (about 39 ha of land bought) — [cnyes 10 Nov 2026](https://news.cnyes.com/news/id/6656704)
- Diamond-copper has been tested but is not in server mass production because it is hard to machine — [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- Main product: double-sided cold plates, a BRIDGE. The planned successors are micro-channel cold plates and lids, then two-phase cold plates:
  - AVC says its two-phase work is "early-stage", samples "lead in thermal performance", and there is no confirmed adoption timeline (company claim, unconfirmed) — [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d)

**(b) Lead**
- Names NVIDIA and AMD as important GPU customers.
- "All ASIC customers" have adopted double-sided cold plates.
- CDUs have shipped to some mainland China customers and are sampling in Europe and the US.
- Customers "are adding suppliers to diversify risk"; AVC says it still leads technologically (company claim, unconfirmed).
- Source: [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- A report (secondary, rumour) says NVIDIA partnered with AVC on micro-channel cold plates — [fiisual 2026](https://fiisual.com/blog/post/2026/microchannel-cooling-technology)

**(c) Revenue model**
- Essentially one-off hardware per platform, priced as average selling price × units:
  - ASP "trending up"; double-sided plates carry higher ASPs;
  - value per unit up at least double digits each past generation;
  - copper, aluminium and iron costs passed through in quotes.
  - [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- No service revenue identified.

**(d) Financial strength**
- Q3 2026 (reported 10 Nov 2026) — [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d); [cnyes](https://news.cnyes.com/news/id/6656704):
  - revenue NT$59,089M (+20.29% q/q, +51.76% y/y);
  - gross margin 33.86% (3Q25: 26.12%); operating margin 28.53% (3Q25: 20.77%);
  - net profit NT$11,564M; EPS NT$29.32.
- 9M 2026, same sources:
  - revenue NT$157,248M (+71.17%); gross margin 32.18%; operating margin 26.93%; EPS NT$73.86.
- Mix, 9M 2026: thermal 65.05%, chassis 19.19%, systems and peripherals 7.86%, Fositek 7.90%. Q3 2026 server application 65% of revenue (+84% y/y).
- Capex: 9M 2026 NT$12,004M (+117%); FY2026 about NT$15bn; FY2027 NT$15–20bn.
- Balance sheet (30 Sep 2026):
  - cash NT$80,031M; no financing plan;
  - inventory NT$75,265M (+30% q/q), inventory days 160 (2Q26: 145);
  - receivables NT$14,749M (+55% q/q);
  - short-term borrowings NT$27,423M (+44% q/q);
  - FX loss NT$304M in Q3.
- Customer concentration and revenue by geography: not disclosed in the materials found.
- Exchange open data, 30 Sep 2026 balance sheet — [TWSE t187ap07](https://openapi.twse.com.tw/v1/opendata/t187ap07_L_ci); [t187ap06](https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci):
  - total assets NT$232.50bn; liabilities NT$157.21bn; total equity NT$75.29bn;
  - current assets NT$178.80bn vs current liabilities NT$141.76bn;
  - 9M net income NT$31.54bn, giving annualised ROE on period-end equity of about 56% (derived).
- Returns (TTM, data date 12 Nov 2026) — [stockanalysis](https://stockanalysis.com/quote/tpe/3017/statistics/) (secondary):
  - ROE 66.4%; ROCE 57.7%; ROIC 159.8% (inflated by low invested capital; read with caution);
  - FCF margin 19.3%; TTM FCF NT$39.47bn;
  - total debt NT$39.44bn vs cash NT$80.03bn (net cash NT$40.59bn).
- Monthly revenue: Oct 2026 NT$22.10bn (+34.4% y/y); Jan–Oct NT$179.35bn (+65.6%) — [TWSE t187ap05](https://openapi.twse.com.tw/v1/opendata/t187ap05_L)

**(e) Resilience**
- AVC "has not yet felt significant price pressure"; supply remains below demand.
- It acknowledged concerns about financing in the cloud-provider sector but does not expect customers to slow spending.
- Source: [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- Exposure to China via its China plant, which is getting new equipment in 2027 — [cnyes](https://news.cnyes.com/news/id/6656704)

#### Boyd Thermal (inside Eaton)

**(a)/(b)**
- Dell'Oro names Boyd among strong-share vendors (Jan 2026) and an "established" CDU name (Sep 2025) — [Dell'Oro PR](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html); [Dell'Oro CDU blog](https://www.delloro.com/market-at-the-boiling-point-is-the-cdu-space-becoming-saturated/)
- Main products: cold plates (BRIDGE) and CDUs.

**(d)**
- Acquired 12 Mar 2026 for $9.55bn net of cash; intangibles $7,142M (customer relationships, technology, backlog).
- Contributed sales of $1,058M and segment operating profit of $257M (about 24.3% margin, derived) from 12 Mar to 30 Sep 2026.
- That is about 4.2% of Eaton's 9M 2026 net sales of $24,929M (derived; part-period).
- Source: [Eaton 10-Q Q3 2026, filed 3 Nov 2026](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm)
- Over 6,000 employees; plants in North America, Asia and Europe — [Data Centre Review Mar 2026](https://datacentrereview.com/2026/03/eaton-completes-boyd-thermal-acquisition-as-it-bolsters-liquid-cooling-offering/)

#### CoolIT Systems (inside Ecolab)

**(a)/(b)**
- Dell'Oro names CoolIT a strong-share vendor (Jan 2026) — [Dell'Oro PR](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html)
- Customers include NVIDIA and AMD (Reuters) — [The Star/Reuters](https://www.thestar.com.my/tech/tech-news/2026/03/20/ecolab-to-buy-coolit-for-475-billion-to-tap-into-ai-data-center-boom)
- Previewed a 3 MW CHx3000 CDU integrated with Ecolab fluid monitoring — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

**(c)**
- Ecolab's thesis adds fluid chemistry and monitoring, a recurring element. A 3D TRASAR platform built on CoolIT is to launch at SC26 (secondary) — [wetheflywheel](https://wetheflywheel.com/en/guides/data-center-cooling-companies-2026/)

**(d)**
- Agreed 20 Mar 2026 at $4,750M; acquisition date 2 Jul 2026 — [Ecolab 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/31462/000162828026068208/ecl-20260930.htm):
  - goodwill $3,251.1M;
  - intangibles $1,755.7M (customer relationships $881.4M, technology $641.6M, trademarks $232.7M).
- About $550M of sales expected over the next 12 months (Mar 2026) — [The Star/Reuters](https://www.thestar.com.my/tech/tech-news/2026/03/20/ecolab-to-buy-coolit-for-475-billion-to-tap-into-ai-data-center-boom)
- That is roughly 3% of Ecolab's annualised sales (derived from Ecolab Q3 2026 sales of $4,694.8M).
- Year-to-date CoolIT sales grew >100% according to Ecolab (secondary) — [wetheflywheel](https://wetheflywheel.com/en/guides/data-center-cooling-companies-2026/)
- KKR had bought CoolIT for about $270M in 2023 (Reuters).

#### nVent (NYSE: NVT)

**(a)/(b)**
- Dell'Oro names nVent among strong-share vendors — [Dell'Oro PR](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html)
- Collaboration with AMD on Helios cooling (press release listed at OCP 2026) — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

**(c)**
- Hardware-led. No liquid-cooling service split disclosed.

**(d)** Q3 2026 (reported 30 Oct 2026) — [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/nvent-electric-nvt-q3-2026-earnings-call-transcript/):
- Sales $1.515bn (+44%). Systems Protection, which holds liquid and air cooling, $1.098bn (+53%; segment return on sales 23%).
- Adjusted operating income $335M (22.1%); FCF $268M.
- Backlog about $2.6bn; organic orders up low double digits.
- Total debt $2.2bn, cash >$1.1bn; target leverage 2–2.5x.
- 2026 tariffs about $105M.
- Liquid-cooling revenue not disclosed; "taking orders" for a new modular liquid-cooling platform.
- Systems Protection includes "cooling solutions, both liquid and air" — [nVent 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1720635/000162828026068596/nvt-20260930.htm)
- Returns (TTM, data date 12 Nov 2026) — [stockanalysis](https://stockanalysis.com/stocks/nvt/statistics/) (secondary):
  - ROIC 13.5%; ROE 17.4%; operating margin 17.7%; FCF margin 12.1%; net debt $1.22bn.
  - The much lower ROIC than Vertiv reflects acquisition goodwill.
- Total equity $4,112.5M at 30 Sep 2026 — [10-Q](https://www.sec.gov/Archives/edgar/data/1720635/000162828026068596/nvt-20260930.htm)

#### Auras (TPEx: 3324)

**(a)/(b)**
- Expected NVIDIA to lead Vera Rubin cold-plate design and procurement and to name 3–4 "Group A" suppliers by end-2025. Auras expected to be one (company expectation, unconfirmed).
- Says it has mastered MCL manufacturing that integrates lid and cold plate (company claim, unconfirmed).
- Source: [udn 14 Nov 2025](https://money.udn.com/money/story/5612/9140567)
- At OCP 2026, showed liquid cooling extended to memory, high-speed interfaces and power delivery — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

**(c)**
- Hardware. Liquid cooling was 24% of revenue in 2023, 34% in 2025, with a 55% target for 2026 (company, Mar 2026) — [Fugle notes](https://blog.fugle.tw/post/earnings-call-3324-1)

**(d)**
- Q3 2026 — [CTEE 11 Nov 2026](https://www.ctee.com.tw/news/20261111701940-430503):
  - revenue NT$9.787bn (+12.49% q/q, a record);
  - net profit NT$1.080bn; EPS NT$11.58; 9M EPS NT$34.59;
  - gross margin 25.65% (−2.77pp q/q); operating margin 13.92% (−2.06pp).
- The margin fall was attributed to several new liquid-cooling products in trial production at once and to a generation change. Q3 call due 18 Nov 2026.
- Capex plan NT$2–2.5bn over two years; evaluating Taiwan and Thailand lines (Nov 2025) — [udn](https://money.udn.com/money/story/5612/9140567)
- Management warned "NVIDIA-led procurement will pressure cold-plate margins" (Nov 2025) — same source.
- Exchange open data, 9M 2026 — [TPEx t187ap06](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap06_O_ci); [TPEx t187ap07](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap07_O_ci):
  - revenue NT$27.04bn; gross profit NT$7.52bn (27.8%); operating income NT$4.27bn (15.8%); net NT$3.39bn;
  - 30 Sep 2026 total equity NT$15.56bn; liabilities NT$22.63bn;
  - annualised ROE about 29% (derived).
- Oct 2026 revenue NT$3.37bn (+44.7% y/y); Jan–Oct +68.8% — [TPEx t187ap05](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O)
- Returns (TTM, 12 Nov 2026) — [stockanalysis](https://stockanalysis.com/quote/tpex/3324/statistics/) (secondary):
  - ROIC 23.2%; ROE 33.9%;
  - TTM FCF −NT$3.20bn (negative); net debt NT$5.31bn.

#### Envicool (SZSE: 002837)

**(d)** — [建投机械 note 26 Oct 2026](https://news.qq.com/rain/a/20261026A0BV6X00); [Sina 26 Oct 2026](https://finance.sina.com.cn/stock/zqgd/2026-10-26/doc-iniwpwiq2476322.shtml)
- 9M 2026: revenue RMB4.950bn (+22.94%); attributable net profit RMB369M (−7.62%).
- Q3 2026: revenue RMB1.933bn (+33.04%); net profit RMB184M (+0.25%); gross margin 27.83%; net margin 9.51%.
- Q3 R&D +39.4%; FX losses and higher interest also weighed.
- Balance sheet: contract liabilities RMB665M (+188% vs start of year); inventory RMB2.507bn (+155%), including goods shipped but not yet recognised.
- Profit lag attributed to delayed shipments and revenue recognition, and upfront investment in liquid cooling and overseas channels.

**(a)/(b)**
- Showed the Deschutes CDU design (spec v1.0) at OCP 2026 — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- No NVIDIA or hyperscaler qualification was verified in this session.

#### Two-phase start-ups (successor side)

**Accelsius**
- First "commercial" IR150 deployment at the EdgeConneX Global Training Center (27 Aug 2026) — [Facilities Dive](https://www.facilitiesdive.com/news/accelsius-two-phase-data-center-cooling-technology-deployed-at-training-cen/828954/)
- Binding contract worth >$15.0M, recognised by Innventure's board on 2 Apr 2026 — [Innventure 10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000154/innv-20260630.htm)
- Innventure consolidated revenue only $1.0M in Q2 and $2.4M in H1 2026, against an H1 net loss of $62.7M. Cash $41.5M at 30 Jun 2026; going-concern language — same 10-Q.
- Accelsius Class C units granted at $9.00 fair value in May 2026 vs a $12.175 Series A conversion price — same 10-Q.
- Nasdaq bid-price deficiency notice for Innventure, 23 Oct 2026 — [8-K](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000198/innv-20261023.htm)
- Strategic review announced 2 Nov 2026 — [PR](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000202/inv-pressreleasefundingstr.htm):
  - Innventure faces "near-term liquidity requirements";
  - most consolidated cash belongs to Accelsius;
  - Accelsius has engaged Evercore for "private capital formation";
  - Innventure will not use its ATM to fund Accelsius at current share prices.

**ZutaCore**
- $100M Series C (2 Jun 2026); ~$200M total; strategic backers Mitsubishi Electric, Carrier, Samsung Ventures; 75+ deployments; Equinix, SoftBank and University of Münster named — [datacenterrichness](https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase)
- Live two-phase demo on a running Blackwell GPU at OCP 2026 — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

### Inferences
- **Recurring revenue.** Vertiv's deferred-revenue jump and fluid-service acquisitions are the clearest evidence in the segment of revenue that is prepaid or recurring. AVC, Auras and Envicool are one-off hardware businesses.
- **Strength of two-phase players.** The two-phase specialists are the weakest balance sheets in the segment. ZutaCore is better funded; Accelsius' funding depends on a new private round.
- **Scenario resilience** (my inference, using the stated priors):
  - **Steady growth (55%).** Vertiv and AVC both keep growing. Vertiv is cushioned by prepayments and services; AVC's 2027 capacity build (+50%) is absorbed.
  - **Financing-led pause around 2028 (25%).**
    - AVC is most exposed: high fixed capex, 160 inventory days, rising short-term debt, no service tail.
    - Auras and Envicool are similarly exposed, with thinner margins.
    - Vertiv is better placed: net cash, ~20% services, broader non-AI base, though its 61% growth means a large air pocket is possible.
    - Accelsius might not survive a pause without new capital.
    - Boyd and CoolIT are shielded by parents with diversified cash flows.
  - **Faster acceleration (20%).** Capacity owners gain most (AVC, Vertiv). Two-phase timing could be pulled forward, helping ZutaCore and Accelsius only if they are funded.
- **Cycle position: late expansion.**
  - Order growth above 100% (Vertiv); inventories more than doubled (Vertiv); AVC inventory days rising.
  - Simultaneous capacity additions: Vertiv, AVC, nVent Blaine 2, Modine Data Centers +95%, AAON BASX +218%.
  - About 40 CDU vendors (Dell'Oro, Sep 2025).
  - Customers dual-sourcing (AVC).
  - Together these signal commoditisation risk in CDUs and standard cold plates once supply catches up.

### Gaps
- Return on invested capital (ROIC) could not be computed for any company: equity and invested-capital figures were not extracted.
- AVC's and Auras' largest-customer and top-five shares, and revenue by country, were not found. Taiwanese annual reports (MOPS) were not reachable.
- Vertiv gives no customer-concentration percentages.
- Schneider-Motivair and Delta cooling revenue, and its share of group revenue, were not found.

---

## (3) Path-forward evidence and suggested verdicts

### Takeaway
None of the key companies yet has a funded, shipping successor to the single-phase cold plate. The physics and economics evidence (OCP, October 2026) says single-phase will be stretched for years. That favours bridge-side companies, provided they extend into micro-channel parts, CDUs and services.

### Cited Findings
- **Transitions that matter here:** (5) cold plates to two-phase for all key companies, and (6) 600 kW and 1 MW racks for system vendors.
  - The 600 kW Kyber rack was reported in July 2026 to have slipped to 2028 (SemiAnalysis, disputed by NVIDIA) — [The Next Web 6 Jul 2026](https://thenextweb.com/news/nvidia-kyber-rack-delay-2028); [TechNews 7 Jul 2026](https://technews.tw/2026/07/07/semianalysis-kyber-postpone-nvdia-reject/)
- **Vertiv**
  - SAID: native 800 VDC revenue from 2027, broader deployment 2028 — [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/)
  - DONE:
    - Strategic Thermal Labs (cold-plate design and validation, Apr 2026) — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
    - PurgeRite ($1,138.3M) and King Environmental Services (fluid services) — [10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm); [8-K](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026063311/exhibit991vrt-q320269242026.htm)
    - ThermoKey agreement (Mar 2026); doubling chiller capacity — [Vertiv 8-K list via search](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026027297/exhibit991vrt-q220264272026.htm)
  - No Vertiv two-phase DTC product shipment was verified this session.
- **AVC**
  - SAID: two-phase "early-stage", no timeline; expects GPU and ASIC fully liquid-cooled by end-2027 — [vocus notes](https://vocus.cc/article/6af3cc73fd89780001cc407d)
  - DONE: +50% cold-plate capacity for 2027; land in Vietnam; NT$15–20bn 2027 capex — [cnyes](https://news.cnyes.com/news/id/6656704)
  - Micro-channel lids not mentioned in the Q3 2026 call notes — [vocus](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- **Micro-channel successor timing (secondary)**
  - Rubin flagship uses a micro-channel cold plate (MCCP) with a gold-plated lid. MCL is "not ready for volume production in the near term" — [TechNews 27 Jan 2026](https://technews.tw/2026/01/27/rubin-mccp-ai-gpu/)
  - Earlier (Sep 2025) reports had MCL decisions in 4Q 2025 for Rubin — [Digitimes](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000732415_G4K58U450ZCNXZ6RERD9C)
  - Volume was expected more likely on Rubin Ultra in 2027 — [CTEE 30 Sep 2025](https://www.ctee.com.tw/news/20250930700073-439901)
  - This is a recorded slip: from a Rubin 2H 2026 target to Rubin Ultra, which now arrives with Kyber in 2028 if the SemiAnalysis report holds.
- **Boyd (Eaton)**
  - DONE: $9.55bn acquisition integrated into Electrical Global; Eaton showed 800 VDC hardware at OCP — [Eaton 10-Q](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm); [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
  - Boyd's two-phase plans not found.
- **CoolIT (Ecolab)**
  - DONE: 3 MW CDU; Stäubli partnership on cold plates for pluggable optics; fluid-monitoring integration — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
  - Two-phase plans not found.
- **nVent**
  - DONE: modular liquid-cooling platform (taking orders); Blaine 1 ramping, Blaine 2 by mid-2027; 800 VDC rack to be shown at SC26 — [Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/nvent-electric-nvt-q3-2026-earnings-call-transcript/)
- **Auras**
  - SAID: MCL capability (claim) — [udn](https://money.udn.com/money/story/5612/9140567)
  - DONE: multiple new liquid products in trial production in Q3 2026, with a margin hit — [CTEE](https://www.ctee.com.tw/news/20261111701940-430503)
- **Envicool**
  - DONE: Deschutes CDU design shown — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
  - Contract liabilities up 188% — [建投机械](https://news.qq.com/rain/a/20261026A0BV6X00)
- **Accelsius**
  - DONE: binding contract worth >$15M; EdgeConneX deployment; multi-MW Austin test lab; 375 kW multi-rack unit teased — [Innventure 10-Q](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000154/innv-20260630.htm); [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
  - FUNDING: the parent's liquidity problems and the Evercore process mean it is not funded through a 1–2 year slip without a new round — [Innventure PR 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/2001557/000200155726000202/inv-pressreleasefundingstr.htm)
- **ZutaCore**
  - DONE: $100M Series C and a live Blackwell demo — [datacenterrichness](https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase); [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)

### Inferences: suggested verdicts
- **Vertiv — coherent.**
  - Its value sits in successor-neutral layers: facility heat rejection, CDUs, fluid services, validation.
  - It is funded (net cash, ~$2.7bn FCF guide), and its acquisitions match the stated plan.
  - What must go right: a two-phase-capable CDU or refrigerant distribution offer when needed (not evidenced), and price discipline as CDUs commoditise.
- **AVC — partly coherent.**
  - Excellent on scaling the bridge, which the evidence says will last longer than roadmaps.
  - Funded through a slip (NT$80bn cash).
  - The successor plan is thin: two-phase at sample stage, MCL status unverified, and rumoured NVIDIA MCCP work.
  - What must go right: winning MCCP/MCL qualification and holding share as customers add suppliers.
- **Boyd (Eaton) — partly coherent.** Strong margin and a funded parent. No visible successor programme in the sources found.
- **CoolIT (Ecolab) — partly coherent.** A funded parent, plus a recurring fluid angle. No two-phase evidence.
- **nVent — partly coherent.** Funded, with capacity being added, but there is no disclosure that lets anyone judge its liquid-cooling lead.
- **Auras — partly coherent.** Claimed MCL capability, but current execution shows margin stress, and NVIDIA-led procurement limits pricing.
- **Envicool — partly coherent / insufficient evidence.** Growth is real, but profit has declined, and its standing with US or hyperscaler customers is unverified.
- **Accelsius — not coherent on funding.** Its technology traction is real but early.
- **ZutaCore — partly coherent.** Funded for now, with strategic backers; production orders are unverified.

### Gaps
- Two-phase product status at Vertiv, Boyd, CoolIT, nVent and Delta was not found.
- NVIDIA's actual cold-plate supplier list for Vera Rubin (the "Group A" list) was not verified.

---

## (4) Suggested ordering by quality alone (not valuation)

### Takeaway
1. **Vertiv**
2. **AVC**
3. **Boyd (Eaton) = CoolIT (Ecolab)** — tie; cannot separate
4. **nVent**
5. **Auras = Envicool** — tie
6. Successor-side bellwethers, kept separate: ZutaCore ahead of Accelsius.

### Cited Findings
- **Vertiv: highest.** It has the best combination of things the evidence can confirm:
  - third-party leadership (Dell'Oro Jan 2026);
  - 25.2% adjusted operating margin and net cash (Q3 2026);
  - about 20% services;
  - $4.12bn in customer prepayments.
  - Sources: [Dell'Oro](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html); [Vertiv Q3 PR](https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-Third-Quarter-2026-with-Net-Sales-Growth-of-61-Organic-Orders-Growth-over-100-and-Diluted-EPS-Growth-of-91-Adjusted-Diluted-EPS-Growth-of-78-Raises-Full-Year-2026-Guidance-Across-All-Key-Metrics/); [10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm)
  - Weaknesses:
    - it stopped disclosing orders;
    - inventories more than doubled;
    - its 10-K concedes hyperscaler pricing leverage.
- **AVC: second.**
  - The best margins and scale among component makers; NVIDIA, AMD and ASIC customers named; no price pressure yet.
  - Pure hardware and bridge-exposed, with rising inventory days and short-term debt — [vocus](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- **Boyd and CoolIT: tied.** Both are named by Dell'Oro and both sit inside acquirers.
  - Boyd's segment margin is about 24% — [Eaton 10-Q](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm)
  - CoolIT has no standalone margin data — [Ecolab 10-Q](https://www.sec.gov/Archives/edgar/data/31462/000162828026068208/ecl-20260930.htm)
- **nVent: fifth.** Strong group metrics but undisclosed liquid metrics — [nVent Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/nvent-electric-nvt-q3-2026-earnings-call-transcript/)
- **Auras and Envicool: tied, sixth and seventh.**
  - Auras: operating margin 13.9% in Q3 2026, with ramp problems — [CTEE](https://www.ctee.com.tw/news/20261111701940-430503)
  - Envicool: net margin 9.5% and falling 9M profit — [建投机械](https://news.qq.com/rain/a/20261026A0BV6X00)

### Inferences
- If quality is weighted toward durability through a two-phase transition, Vertiv's lead over AVC widens. If it is weighted toward current returns, AVC's margins may equal Vertiv's.
- **AAON** is excluded from the key set. It is a fast grower (BASX +218%) but is restating two quarters and has disclosed a material weakness, which is a governance negative — [AAON 8-K 9 Nov 2026](https://www.sec.gov/Archives/edgar/data/824142/000082414226000083/aaon-20261109.htm)

### Gaps
- Without ROIC and concentration data, the AVC–Vertiv gap and the Boyd–CoolIT tie cannot be resolved.

---

## (5) Background priors check

### Takeaway
| Prior | Verdict |
|---|---|
| 1a. Chips up to 2.3 kW, heading to 4 kW | Confirmed (secondary) |
| 1b. Cold plates handle 100–150 kW per rack | Contradicted |
| 2. Two-phase held up by fluorinated-coolant restrictions | Updated |
| 3. In-chip channels unproven in production | Confirmed |
| 4. Power and cooling bind compute in 2028–2030 | Partly supported, with nuance |
| 5a. 600 kW rack in volume in 2028, not 2027 (65%) | Strengthened |
| 5b. 1 MW racks in production use by end-2030 (50%) | Weakened |
| 6. Bridges lose share in 2028–2030 but last longer than roadmaps say | First half contradicted, second half confirmed |

### Cited Findings
1. **Chip power: confirmed (secondary).**
   - Dual-die Rubin reported at 2,300 W, above an earlier 1,800 W estimate — [Digitimes 12 Sep 2025](https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000732415_G4K58U450ZCNXZ6RERD9C)
   - Per-GPU power "approaching 2,000 W" — [TechNews 27 Jan 2026](https://technews.tw/2026/01/27/rubin-mccp-ai-gpu/)
   - Rubin Ultra listed at 3,600 W in a roadmap table (secondary) — [Introl](https://introl.com/blog/nvidia-vera-rubin-gpu-600kw-racks-2027)
   - OCP: "reported figures for 2027-class parts already approach" the ~4,000 W single-phase wall — [OCP white paper v1.00, 12 Oct 2026](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
2. **"Cold plates handle about 100–150 kW a rack": contradicted.**
   - Single-phase liquid is being specified for VR200 NVL144 at about 230–250 kW per rack ("as reported") and for Kyber-class racks at about 600 kW — [OCP white paper, Table 10](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - NVIDIA's MGX 1.2 spec supports racks up to 250 kW — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
   - Single-phase DLC is "the vast majority" of liquid-cooled capacity — [Dell'Oro 8 Jan 2026](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html)
   - Single-phase cold plates "remain mainstream through 2030" (secondary) — [FUNDA 20 Oct 2026](https://fundaai.substack.com/p/researchpower-and-liquid-cooling)
   - The real limit is per-device heat flux, about 4,000 W per reticle-class die (~850 mm²), plus connector-count reliability. It is not rack kW — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - Other secondary estimates: GB300 NVL72 about 140–160 kW; Vera Rubin NVL72 about 190–230 kW; CPX about 370 kW — [DataGravity](https://www.datagravity.dev/p/600-kw-per-rack-the-ai-power-crisis)
3. **"Two-phase is held up by fluorinated-coolant restrictions": updated.**
   - For **immersion**, fluids are the main brake. OCP says fluid chemistry "has brought it to a halt", and 3M's PFAS exit questioned supply — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
     - 3M completed its exit from PFAS manufacturing by end-2025 — [3M 10-Q](https://www.sec.gov/Archives/edgar/data/66740/000006674026000311/mmm-20260930.htm)
   - For **two-phase DTC**, the bottlenecks are packaging, TIM and QDs/manifolds "rather than the coolant itself" (secondary) — [FUNDA](https://fundaai.substack.com/p/researchpower-and-liquid-cooling)
     - It is also an infrastructure change, not a drop-in, while single-phase keeps extending — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - **No binding EU ban yet.** Status of the EU universal PFAS restriction:
     - Risk Assessment Committee (RAC) final opinion 2 Mar 2026;
     - Socio-Economic Analysis Committee (SEAC) draft opinion 10 Mar 2026;
     - consultation 26 Mar–25 May 2026;
     - SEAC final opinion expected by end-2026;
     - then a Commission proposal and a REACH Committee vote, with no dates set.
     - Sources: [CMS 8 Apr 2026](https://cms.law/en/aut/legal-updates/support-for-eu-wide-pfas-restriction-with-targeted-derogations-what-happens-next); [Arnold & Porter Mar 2026](https://www.arnoldporter.com/en/perspectives/advisories/2026/03/echa-committees-advance-broad-pfas-restriction-under-reach)
   - **US federal:** the start of the TSCA 8(a)(7) PFAS reporting period was postponed again (April 2026). It now starts 60 days after a forthcoming revised rule takes effect, with a backstop of 31 Jan 2027 according to BCLP — [EPA](https://www.epa.gov/chemicals-under-tsca/update-reporting-deadline-tsca-pfas-reporting-rule); [BCLP](https://www.bclplaw.com/print/v2/content/1574597/tsca-pfas-reporting-delayed-yet-again.pdf)
   - **Fluid availability:** Chemours' two-phase fluid made by Navin was said to start in 2026, after slipping from a 2025 target. The Q3 2026 10-Q shows no such revenue — [Chemours PR May 2025](https://www.chemours.com/en/news-media-center/all-news/press-releases/2025/chemours-and-navin-fluorine-announce-agreement-to-manufacture-new-liquid-cooling-product); [Chemours 10-Q](https://www.sec.gov/Archives/edgar/data/1627223/000162722326000035/cc-20260930.htm)
   - Revised prior: two-phase DTC is held back mainly because single-phase keeps extending and by system integration. Regulatory uncertainty around PFAS fluids is a secondary drag on DTC and the main drag on immersion.
4. **"In-chip channels unproven in production": confirmed.**
   - OCP: microfluidics is "the least deployed". Chip suppliers "have not deemed it necessary yet"; co-designed in-stack cooling "remains a research frontier" — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - Corintis' current product is copper cold plates. Its in-chip line is a small prototype line, with no Maia production date — [IEEE Spectrum 17 Nov 2025](https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis)
   - MCL is not ready for volume — [TechNews Jan 2026](https://technews.tw/2026/01/27/rubin-mccp-ai-gpu/)
5. **"Rack power and cooling binding in 2028–2030": partly supported.**
   - OCP: cooling "now sets the pace at which compute can be deployed". The "whole-volume" liquid window opens at 250–300 kW racks in 2027–2029 — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - But today's cited pacing items are power availability, permitting and labour ("not slowing growth") — [Vertiv Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/)
   - Rack testing and the data hall are cited as the Vera Rubin bottleneck (secondary) — [FUNDA](https://fundaai.substack.com/p/researchpower-and-liquid-cooling)
   - The Kyber slip is a PCB midplane problem, not a cooling one — [TNW](https://thenextweb.com/news/nvidia-kyber-rack-delay-2028)
6. **600 kW rack: 65% prior for 2028 rather than 2027 — strengthened.**
   - SemiAnalysis (5 Jul 2026) reported Kyber slipped more than 12 months to 2028; NVIDIA says "Our roadmap is intact" — [TNW 6 Jul 2026](https://thenextweb.com/news/nvidia-kyber-rack-delay-2028); [TechNews 7 Jul 2026](https://technews.tw/2026/07/07/semianalysis-kyber-postpone-nvdia-reject/)
   - The OCP white paper already places the 600 kW Kyber-class rack in 2028 — [OCP Table 10](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - Inference: raise to roughly 75–85%.
7. **1 MW racks by end-2030: 50% prior — weakened.**
   - Dell'Oro: 1 MW racks will "arrive later and be rarer than earlier roadmaps implied". NVL576 is now eight 72-GPU racks linked by optics — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
   - Native 800 V rack expected in 2028; solid-state transformer (SST) volume beyond end-2028 (secondary) — [FUNDA](https://fundaai.substack.com/p/researchpower-and-liquid-cooling)
   - OCP carries 1,000 kW in 2030 only as an "announced direction" — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - Inference: cut to roughly 35–45%.
8. **Bridges lose share 2028–2030, last longer than roadmaps say: first half contradicted, second half confirmed.**
   - Cold plates are still gaining share against air: AVC expects all GPU and ASIC compute to be liquid-cooled by end-2027 — [vocus](https://vocus.cc/article/6af3cc73fd89780001cc407d)
   - Single-phase is expected to stay mainstream through 2030 (secondary) — [FUNDA](https://fundaai.substack.com/p/researchpower-and-liquid-cooling)
   - OCP calls the move "gradual, grudging … pulled by economics" — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
   - The successors are slipping:
     - MCL moved from Rubin 2H 2026 to "not near-term" — [TechNews](https://technews.tw/2026/01/27/rubin-mccp-ai-gpu/)
     - two-phase is still pilots and "early large-scale implementations" — [Dell'Oro Jan 2026](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html)

### Inferences
- Within cold plates, value should shift toward micro-channel and double-sided designs (higher ASPs) rather than toward two-phase before 2028.
- Two-phase share of liquid-cooled capacity by 2030 looks likely to be small (my judgement; no third-party share forecast found).

### Gaps
- No Omdia or TrendForce two-phase share forecast was obtained.
- Exact F-gas Regulation (EU) 2024/573 milestones and the SEAC draft's treatment of refrigerants and heat-transfer fluids were not retrieved (the ECHA PDF returned 403).

---

## (6) Open question: which successor ships in volume first, and who captures value

### Takeaway
- **Order of arrival, most likely first:**
  1. Single-phase micro-channel cold plates (MCCP) — shipping on Rubin per secondary reports.
  2. Two-phase DTC in niche or sidecar settings.
  3. Micro-channel lids.
  4. In-chip microfluidics last.
  - Two-phase immersion is stalled by fluids.
- **Value capture is splitting:**
  - Power and HVAC groups have bought the system layer.
  - NVIDIA increasingly controls cold-plate design and procurement.
  - Taiwanese component makers keep high margins on scale and process know-how.
  - Foundries show no production move yet.

### Cited Findings
- MCCP with a gold-plated lid on the Rubin flagship; MCL not near-term — [TechNews 27 Jan 2026](https://technews.tw/2026/01/27/rubin-mccp-ai-gpu/)
- At OCP 2026: Jabil micro-channel cold plates; xFusion diamond-copper plates; Cooler Master refrigerant loops "in development" — [Dell'Oro](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- Air-assisted liquid cooling (AALC) sidecars are "the most likely first commercial home for two-phase" (secondary) — [FUNDA](https://fundaai.substack.com/p/researchpower-and-liquid-cooling)
- OCP: "in-chip acquisition handing off to two-phase transport is one of the strongest combinations on the horizon"; two-phase cold plate is "the high-flux extension of the cold plate family" — [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
- **Acquirer deals (value moving to integrated groups):**
  - Eaton–Boyd $9.55bn — [Eaton 10-Q](https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm)
  - Ecolab–CoolIT $4.75bn — [Ecolab 10-Q](https://www.sec.gov/Archives/edgar/data/31462/000162828026068208/ecl-20260930.htm)
  - Trane–Stellar Energy $553.4M, plus LiquidStack — [Trane 10-Q](https://www.sec.gov/Archives/edgar/data/1466258/000162828026068122/tt-20260930.htm)
  - JCI–Alloy (~$291M with Nantum) — [JCI 10-Q](https://www.sec.gov/Archives/edgar/data/833444/000083344426000087/jci-20260630.htm)
  - Vertiv–PurgeRite $1.14bn — [Vertiv 10-K](https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm)
- **Strategic minority stakes:**
  - Carrier, Mitsubishi Electric and Samsung in ZutaCore — [datacenterrichness](https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase)
  - JCI and Legrand in Accelsius — [Facilities Dive](https://www.facilitiesdive.com/news/accelsius-two-phase-data-center-cooling-technology-deployed-at-training-cen/828954/)
  - LITEON in DCX (secondary) — [newmarketpitch](https://newmarketpitch.com/blogs/news/data-center-cooling-funding-news)
- **Chip-maker control:** "NVIDIA is expected to lead cold-plate design and procurement" for Vera Rubin, and this "will pressure cold-plate margins" — Auras, Nov 2025 — [udn](https://money.udn.com/money/story/5612/9140567)
  - Yet AVC's Q3 2026 operating margin was 28.5%, up 7.8pp y/y — [vocus](https://vocus.cc/article/6af3cc73fd89780001cc407d)
- **Hyperscaler in-house design:** AWS's IRHX is "not a threat", because vendors still build it — [Dell'Oro 14 Jul 2025](https://www.delloro.com/awss-new-liquid-cooling-solution-rattled-the-market-but-is-it-truly-disruptive/)
  - Google's Deschutes CDU spec is being built by Delta (mass production 1Q 2027) and shown by Envicool — [Dell'Oro 19 Oct 2026](https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/)
- **Market size:** about $3bn in 2025 (roughly doubled), about $7bn by 2029 — [Dell'Oro Jan 2026](https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html)
  - Fewer than 10 CDU vendors expected to take "the lion's share" by end of decade — [Dell'Oro Sep 2025](https://www.delloro.com/market-at-the-boiling-point-is-the-cdu-space-becoming-saturated/)
- **Refrigerant suppliers benefit through chillers, not two-phase:**
  - Solstice's refrigerant growth is "driven primarily by data center demand" — [Solstice 10-Q](https://www.sec.gov/Archives/edgar/data/2064953/000206495326000100/sols-20260930.htm)
  - Chemours' Opteon refrigerant sales fell to $287M in Q3 2026 from $368M — [Chemours 10-Q](https://www.sec.gov/Archives/edgar/data/1627223/000162722326000035/cc-20260930.htm)

### Inferences
- **Hyperscaler specs.** Open hyperscaler specifications (Deschutes, Mt Diablo) and NVIDIA-run procurement push CDUs and cold plates toward built-to-spec manufacturing. That favours scale players (AVC, Delta, Vertiv) over small specialists.
- **Where the moat lies.** If in-chip cooling eventually arrives, foundries and chip designers would capture the "judge" (the qualification gate). Until then, the moat is capacity, qualification and services.
- **Specialists vs integrated giants.** Integrated giants plus a few Taiwanese scale makers are capturing value. Independent specialists are being bought (CoolIT, Boyd, LiquidStack, Motivair) or capital-constrained (Accelsius).

### Gaps
- No Omdia CDU, cold-plate or QD share tables were obtained.
- NVIDIA's approved-vendor list was not verified.

---

## (7) What could not be verified
- **Search capacity.** Search budget exhaustion (WebSearch), plus out-of-credit Exa and Firecrawl, stopped work on:
  - Kaori, Jentech and Fositek standalone Q3 2026 results;
  - Delta's cooling revenue share;
  - Schneider/Motivair revenue;
  - Munters and Alfa Laval data-centre orders;
  - Rittal and Stulz.
- **Mainland China beyond Envicool** (Shenling, Goaland, Sugon Digital Creation, Huawei Digital Power, Lenovo Neptune): no 2026 data. Coverage is thin because cninfo and Chinese-language sources were not reachable without search.
- **Japan and Korea:**
  - Daikin–Chilldyne deal and Samsung–FläktGroup closing not re-verified;
  - Nidec CDU revenue, MHI and LG Electronics not covered;
  - EDINET, TDnet and DART not reached.
- **India:** Navin's Surat two-phase fluid plant status not confirmed; Refroid not verified.
- **Israel:** ZutaCore only (US HQ, Israeli R&D); MAYA filings not checked.
- **TIMs** (Indium, Henkel, Shin-Etsu, Dexerials, Dow, Solstice electronic materials): no 2026 evidence gathered.
- **QDs** (Stäubli, CPC, Parker, Danfoss, Fositek): no market shares. OCP gives only a reliability baseline:
  - 0.15% annualised failure rate per QD fitting;
  - six QDs and two cold plates per GB200-class tray.
  - [OCP](https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/)
- **TSMC, Intel and Samsung in-package cooling:** no 2026 status or production commitment found.
- **AMD Helios:** rack kW not officially disclosed. One secondary estimate is ">100 kW"; initial shipments end-Q3 2026 (secondary, unverified).
- **Vera Rubin NVL144:** official rack kW not confirmed by NVIDIA. At CES (5 Jan 2026), NVIDIA "isn't ready to say", and Ian Buck said power would not double — [The Register 5 Jan 2026](https://www.theregister.com/on-prem/2026/01/05/nvidia-unpacks-vera-rubin-rack-system-at-ces/2484391)
- **Other unverified figures:**
  - Vertiv's 11.3% share attributed to Dell'Oro (secondary only).
  - Exact closing dates in secondary sources: wetheflywheel gives LiquidStack 3 Mar 2026 vs Pulse 2's report of 4 Mar 2026.
- **ROIC and customer concentration** (largest and top five) for Vertiv, AVC, Auras and Envicool were not available in the sources reached.

---

## (8) Sources (URL — date)

**Primary filings**
- Vertiv Q3 2026 press release — 28 Oct 2026 — https://investors.vertiv.com/news/news-details/2026/Vertiv-Reports-Strong-Third-Quarter-2026-with-Net-Sales-Growth-of-61-Organic-Orders-Growth-over-100-and-Diluted-EPS-Growth-of-91-Adjusted-Diluted-EPS-Growth-of-78-Raises-Full-Year-2026-Guidance-Across-All-Key-Metrics/
- Vertiv 10-Q Q3 2026 — filed 28 Oct 2026 — https://www.sec.gov/Archives/edgar/data/1674101/000162828026067893/vrt-20260930.htm
- Vertiv 10-K FY2025 — filed 13 Feb 2026 — https://www.sec.gov/Archives/edgar/data/1674101/000167410126000008/vrt-20251231.htm
- Vertiv 8-K, King Environmental Services — 24 Sep 2026 — https://www.sec.gov/Archives/edgar/data/0001674101/000162828026063311/exhibit991vrt-q320269242026.htm
- Vertiv 8-K, Q4 2025 results — 11 Feb 2026 — https://www.sec.gov/Archives/edgar/data/1674101/000167410126000006/exhibit991vrt02112026.htm
- Eaton 10-Q Q3 2026 — filed 3 Nov 2026 — https://www.sec.gov/Archives/edgar/data/1551182/000155118226000040/etn-20260930.htm
- Ecolab 10-Q Q3 2026 — filed 29 Oct 2026 — https://www.sec.gov/Archives/edgar/data/31462/000162828026068208/ecl-20260930.htm
- Trane 10-Q Q3 2026 — filed 29 Oct 2026 — https://www.sec.gov/Archives/edgar/data/1466258/000162828026068122/tt-20260930.htm
- Johnson Controls 10-Q (quarter to 30 Jun 2026) — filed 29 Jul 2026 — https://www.sec.gov/Archives/edgar/data/833444/000083344426000087/jci-20260630.htm
- nVent 10-Q Q3 2026 — filed 30 Oct 2026 — https://www.sec.gov/Archives/edgar/data/1720635/000162828026068596/nvt-20260930.htm
- Flex 10-Q (quarter to 25 Sep 2026) — filed 30 Oct 2026 — https://www.sec.gov/Archives/edgar/data/866374/000086637426000042/flex-20260925.htm
- Flex 8-K — 14 Oct 2026 — https://www.sec.gov/Archives/edgar/data/866374/000119312526421058/d147467d8k.htm
- AAON 10-Q Q3 2026 — filed 9 Nov 2026 — https://www.sec.gov/Archives/edgar/data/824142/000082414226000088/aaon-20260930.htm
- AAON 8-K, Item 4.02 — 9 Nov 2026 — https://www.sec.gov/Archives/edgar/data/824142/000082414226000083/aaon-20261109.htm
- Modine 10-Q (quarter to 30 Sep 2026) — filed 4 Nov 2026 — https://www.sec.gov/Archives/edgar/data/67347/000110465926122523/mod-20260930x10q.htm
- Modine 8-K — 1 Oct 2026 — https://www.sec.gov/Archives/edgar/data/67347/000110465926112870/tm2626618d1_8k.htm
- Dover 10-Q Q3 2026 — filed 22 Oct 2026 — https://www.sec.gov/Archives/edgar/data/29905/000002990526000033/dov-20260930.htm
- Parker 10-Q — filed 5 Nov 2026 — https://www.sec.gov/Archives/edgar/data/76334/000007633426000172/ph-20260930.htm
- Chemours 10-Q Q3 2026 — filed 5 Nov 2026 — https://www.sec.gov/Archives/edgar/data/1627223/000162722326000035/cc-20260930.htm
- Honeywell 10-Q Q3 2026 — filed 22 Oct 2026 — https://www.sec.gov/Archives/edgar/data/773840/000077384026000143/hon-20260930.htm
- Solstice Advanced Materials 10-Q Q3 2026 — filed 4 Nov 2026 — https://www.sec.gov/Archives/edgar/data/2064953/000206495326000100/sols-20260930.htm
- 3M 10-Q Q3 2026 — filed 20 Oct 2026 — https://www.sec.gov/Archives/edgar/data/66740/000006674026000311/mmm-20260930.htm
- Dow 10-Q Q3 2026 — filed 23 Oct 2026 — https://www.sec.gov/Archives/edgar/data/1751788/000175178826000160/dow-20260930.htm
- Innventure 10-Q (quarter to 30 Jun 2026) — filed 13 Aug 2026 — https://www.sec.gov/Archives/edgar/data/2001557/000200155726000154/innv-20260630.htm
- Innventure 8-K (Nasdaq notice) — 23 Oct 2026 — https://www.sec.gov/Archives/edgar/data/2001557/000200155726000198/innv-20261023.htm
- Innventure strategic review press release — 2 Nov 2026 — https://www.sec.gov/Archives/edgar/data/2001557/000200155726000202/inv-pressreleasefundingstr.htm

**Standards bodies and regulators**
- OCP white paper "Thermal Boundaries in AI Infrastructure", v1.00 — 12 Oct 2026 — https://www.opencompute.org/documents/white-paper-thermal-boundaries-in-ai-infrastructure/
- ECHA, RAC opinion on PFAS — Mar 2026 — https://www.echa.europa.eu/-/echa-s-risk-assessment-committee-adopts-its-opinion-on-pfas-restriction-proposal
- EPA, TSCA PFAS reporting deadline update — Apr 2026 — https://www.epa.gov/chemicals-under-tsca/update-reporting-deadline-tsca-pfas-reporting-rule

**Earnings-call transcripts**
- Vertiv Q3 2026 — 28 Oct 2026 — https://www.fool.com/earnings/call-transcripts/2026/10/28/vertiv-vrt-q3-2026-earnings-call-transcript/
- nVent Q3 2026 — 30 Oct 2026 — https://www.fool.com/earnings/call-transcripts/2026/10/30/nvent-electric-nvt-q3-2026-earnings-call-transcript/

**Company results coverage (Taiwan, China)**
- AVC (cnyes) — 10 Nov 2026 — https://news.cnyes.com/news/id/6656704
- AVC (vocus notes) — Nov 2026 — https://vocus.cc/article/6af3cc73fd89780001cc407d
- AVC (vocus notes) — Nov 2026 — https://vocus.cc/article/6af48f7ffd89780001371ef8
- AVC (CTEE) — 11 Nov 2026 — https://www.ctee.com.tw/news/20261111700245-439901
- AVC (udn) — 10 Nov 2026 — https://udn.com/news/story/7240/9869791
- Auras (CTEE) — 11 Nov 2026 — https://www.ctee.com.tw/news/20261111701940-430503
- Auras (udn) — 14 Nov 2025 — https://money.udn.com/money/story/5612/9140567
- Auras (Fugle notes on 12 Mar 2026 call) — Mar 2026 — https://blog.fugle.tw/post/earnings-call-3324-1
- Envicool (Sina) — 26 Oct 2026 — https://finance.sina.com.cn/stock/zqgd/2026-10-26/doc-iniwpwiq2476322.shtml
- Envicool (建投机械 note via QQ) — 26 Oct 2026 — https://news.qq.com/rain/a/20261026A0BV6X00

**Analysts and trade press (secondary)**
- Dell'Oro, OCP 2026 recap — 19 Oct 2026 — https://www.delloro.com/inside-ocp-global-summit-2026-cold-plates-800-vdc-sidecars-and-a-buildout-at-full-steam/
- Dell'Oro, liquid cooling market press release — 8 Jan 2026 — https://www.prnewswire.com/news-releases/data-center-liquid-cooling-market-to-approach-7-billion-by-2029-as-ai-deployments-accelerate-according-to-delloro-group-302655848.html
- Dell'Oro, CDU saturation — 30 Sep 2025 — https://www.delloro.com/market-at-the-boiling-point-is-the-cdu-space-becoming-saturated/
- Dell'Oro, AWS IRHX — 14 Jul 2025 — https://www.delloro.com/awss-new-liquid-cooling-solution-rattled-the-market-but-is-it-truly-disruptive/
- FUNDA — 20 Oct 2026 — https://fundaai.substack.com/p/researchpower-and-liquid-cooling
- TechArena — Oct 2026 — https://techarena.ai/content/ocp-global-summit-2026-agents-800-volts-and-a-warning-on-heat
- The Next Web, Kyber delay — 6 Jul 2026 — https://thenextweb.com/news/nvidia-kyber-rack-delay-2028
- TechNews, Kyber delay — 7 Jul 2026 — https://technews.tw/2026/07/07/semianalysis-kyber-postpone-nvdia-reject/
- TechNews, Rubin MCCP — 27 Jan 2026 — https://technews.tw/2026/01/27/rubin-mccp-ai-gpu/
- Digitimes, micro-channel lid — 12 Sep 2025 — https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=0000732415_G4K58U450ZCNXZ6RERD9C
- CTEE, MLCP — 30 Sep 2025 — https://www.ctee.com.tw/news/20250930700073-439901
- The Register, Vera Rubin at CES — 5 Jan 2026 — https://www.theregister.com/on-prem/2026/01/05/nvidia-unpacks-vera-rubin-rack-system-at-ces/2484391
- DataGravity, rack power — 2026 — https://www.datagravity.dev/p/600-kw-per-rack-the-ai-power-crisis
- IEEE Spectrum, Corintis — 17 Nov 2025 — https://spectrum.ieee.org/microfluidics-cooling-ai-chips-corintis
- Facilities Dive, Accelsius — 27 Aug 2026 — https://www.facilitiesdive.com/news/accelsius-two-phase-data-center-cooling-technology-deployed-at-training-cen/828954/
- datacenterrichness, ZutaCore round — 2 Jun 2026 — https://datacenterrichness.substack.com/p/zutacore-raises-100m-for-two-phase
- The Star/Reuters, Ecolab–CoolIT — 20 Mar 2026 — https://www.thestar.com.my/tech/tech-news/2026/03/20/ecolab-to-buy-coolit-for-475-billion-to-tap-into-ai-data-center-boom
- Pulse 2, Trane–LiquidStack — 4 Mar 2026 — https://pulse2.com/trane-technologies-liquid-cooling-firm-liquidstack-acquired-to-expand-data-center-thermal-management-solutions
- Data Centre Review, Eaton–Boyd — Mar 2026 — https://datacentrereview.com/2026/03/eaton-completes-boyd-thermal-acquisition-as-it-bolsters-liquid-cooling-offering/
- CMS, PFAS restriction next steps — 8 Apr 2026 — https://cms.law/en/aut/legal-updates/support-for-eu-wide-pfas-restriction-with-targeted-derogations-what-happens-next
- Arnold & Porter, PFAS committees — Mar 2026 — https://www.arnoldporter.com/en/perspectives/advisories/2026/03/echa-committees-advance-broad-pfas-restriction-under-reach
- BCLP, TSCA PFAS delay — 2026 — https://www.bclplaw.com/print/v2/content/1574597/tsca-pfas-reporting-delayed-yet-again.pdf
- Chemours press release, Navin agreement — 6 May 2025 — https://www.chemours.com/en/news-media-center/all-news/press-releases/2025/chemours-and-navin-fluorine-announce-agreement-to-manufacture-new-liquid-cooling-product
- newmarketpitch, funding roundup — Oct 2026 — https://newmarketpitch.com/blogs/news/data-center-cooling-funding-news
- wetheflywheel, 2026 vendor guide — 2026 — https://wetheflywheel.com/en/guides/data-center-cooling-companies-2026/
- TAMradar, Iceotope — May 2026 — https://www.tamradar.com/funding-rounds/iceotope-series-b-26m
- Wiwynn white paper — https://www.wiwynn.com/whitepapers/general-guidance-for-transitioning-from-single-phase-to-two-phase-liquid-cooling-solutions

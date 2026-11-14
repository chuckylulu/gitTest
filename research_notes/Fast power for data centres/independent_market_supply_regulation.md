# Independent evidence on fast power for data centres: market, supply chain, customers and regulation (as of 14 November 2026)

Scope and conventions. This file collects evidence from sources that GE Vernova, Siemens Energy, Bloom Energy, Caterpillar (including Solar Turbines), Hitachi Energy, Schneider Electric and HD Hyundai Electric do not control. Each source is tagged **[independent]** or **[company]**. Qualifiers in the tag:
- **competitor**: a rival maker that is not one of the seven (Mitsubishi Heavy Industries, Wärtsilä, Doosan, Ansaldo).
- **govt data**: a government dataset that I downloaded and processed myself.
- **secondary**: an aggregator or blog that relays other people's data. Treat these with caution.

When an independent outlet repeats a figure that one of the seven companies reported, the bullet says "(company-reported)".

Research limits:
- The shared web-search budget for this session ran out partway through. After that I only fetched pages whose URLs had already turned up.
- `www.nrel.gov` is blocked by this session's network settings.
- Several pages returned HTTP 403, 402 or 405: IEA, IEEFA, DCD, Akin Gump, NGI and the PUCT rule PDF.
- The Census trade API now needs a key, so the HS 8504 import data could not be pulled.

Where a figure comes only from a search-result excerpt and not from the page itself, the bullet says so.

---

## 1. Data-centre power demand and grid-connection delays

### Takeaway
Every independent forecast names data centres as the largest driver of US load growth, but they disagree on how large it will be.
- US utilities' filings add up to about 90 GW of data-centre load by 2030. Grid Strategies thinks this overstates the likely figure by about 40%.
- BloombergNEF forecasts 106 GW of US data-centre demand by 2035.

Queues and "contracting pipelines" are far larger than what gets energised. ERCOT tracks about 474 GW of large-load requests, of which only about 205 GW qualified for its first batch study. Dominion has about 55 GW "in various stages of contracting", but only about 12 GW is under electric service agreements.

Developers have announced about 90 GW of their own behind-the-meter (BTM) power plants by mid-2026, and more than 100 GW by October 2026. Only about 2 GW was operating in mid-2026, and Cleanview expects 2.8–3.2 GW by the end of 2026.

### Cited Findings
**Global forecasts**
- IEA "Energy and AI" (published April 2025):
  - Data centres used about 415 TWh in 2024, roughly 1.5% of global electricity.
  - Base case for 2030 is about 945 TWh, just under 3% of global electricity.
  - US consumption rises by about 240 TWh (+130%) over 2024. The US and China account for nearly 80% of global growth.
  - For 2035 the base case is about 1,200 TWh, with a scenario range of 700–1,700 TWh.
  - Source: [IEA, Energy and AI – Executive summary (Apr 2025)](https://www.iea.org/reports/energy-and-ai/executive-summary) and [IEA, Energy demand from AI](https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai) [independent]. The IEA pages returned HTTP 403 in this session; the figures come from search-result excerpts of those pages.
- Secondary sites say an IEA 2026 update estimates 485 TWh in 2025, about 950 TWh in 2030, and 155 TWh in 2025 for AI-focused data centres. **Not verified on the IEA site.** Sources: [StatOrigin (2026)](https://statorigin.org/reports/data-centres-power-constraint-2026) and [MarlinFX (2026)](https://marlinfx.com/news/ai-data-centres-electricity-demand-iea-2026/) [independent; secondary].

**US forecasts**
- LBNL, "2024 United States Data Center Energy Usage Report" (December 2024): 176 TWh in 2023 (4.4% of US electricity), rising to 325–580 TWh in 2028 (6.7–12%). Source: [LBNL report (Dec 2024)](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf) [independent]. The link redirects to eScholarship, which returned an empty page in this session, so these widely reported figures were not re-read in-session.
- Grid Strategies, "Power Demand Forecasts Revised Up for Third Year Running, Led by Data Centers" (Wilson, Meyer, Zimmerman and Gramlich; November 2025). Source: [Grid Strategies (Nov 2025)](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf) [independent].
  - Utility five-year peak-growth forecasts total **166 GW** (3.7% a year), up more than six-fold from 24 GW three years earlier.
  - Electricity use is forecast to rise 32% by 2030.
  - About **90 GW (~55%)** of the growth is linked to data centres. Market analysts suggest "unlikely to require much more than 65 GW through 2030", so the data-centre portion is "likely overstated by roughly 25 GW", or about 40%.
  - Industrial load adds about 30 GW, and oil, gas and mining about 10 GW.
- BloombergNEF (reported 3 Dec 2025). Source: [Utility Dive, "U.S. data center power demand could reach 106 GW by 2035: BloombergNEF" (3 Dec 2025)](https://www.utilitydive.com/news/us-data-center-power-demand-could-reach-106-gw-by-2035-bloombergnef/806972/) [independent].
  - US data-centre demand "could reach 106 GW in 2035", 36% above BNEF's April 2025 forecast.
  - More than a quarter of 150 significant US projects announced in the previous year exceed 500 MW.
  - PJM alone could add 31 GW of data-centre load over five years, about 3 GW more than expected new generation.
- DOE (July 2025 report): 100 GW of new peak capacity is needed by 2030, of which 50 GW is attributable to data centres. Source: same Utility Dive article [independent].
- NERC, *Reliability Insights: Large Computational Load Risks Due to Voltage Sensitivity* (September 2026). Source: [NERC (Sep 2026)](https://www.nerc.com/globalassets/who-we-are/news/2026/09/reliability-insights_large-computational-load-risks-due-to-voltage-sensitivity.pdf) [independent].
  - NERC's 2025 Long-Term Reliability Assessment projects summer peak to rise by more than 224 GW over 10 years.
  - Computational loads "seek to interconnect very quickly (sometimes within one to two years)".
- Utility Dive, reporting on NERC: "Summer peak demand across the bulk power system is expected to rise 24% in the next 10 years", with data centres driving most of the increase. Source: [Utility Dive (5 May 2026)](https://www.utilitydive.com/news/nerc-issues-rare-level-3-alert-over-data-center-load-losses/819295/) [independent].
- Goldman Sachs, as cited by OilPrice:
  - US data-centre capacity additions of 8.5 GW realised in 2025, 13.6 GW scheduled for 2026 and 36.3 GW scheduled for 2027.
  - Data centres' share of US summer peak demand projected to rise from 4.1% to 8.5% by 2027.
  - Source: [OilPrice.com, "The Gas Turbine Shortage Just Became AI's Biggest Constraint" (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent; secondary relay of a bank forecast].

**Interconnection queues and contracting pipelines**
- **ERCOT** (Pablo Vegas to the Texas Senate Business & Commerce Committee, 29 July 2026). Source: [ERCOT, "ERCOT Update" (29 Jul 2026)](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf) [independent].
  - "ERCOT is tracking approximately 474 GW of Large Loads seeking interconnection, of which ~90% are data centers" (data as of June 2026).
  - About 205 GW is eligible for the first "Batch Zero" study, in three groups: base load (150 projects, ~65 GW), allocated load (127 projects, ~114 GW) and to-be-determined (49 projects, ~25 GW).
  - Not eligible: 315 projects (~274 GW) that had no qualifying study, and 47 projects (~20 GW) that submitted no dynamic model.
  - Generation queue at 30 June 2026: 1,949 active projects, 462,785 MW, of which 77.6 GW is gas.
- ERCOT Board of Directors, 1–2 June 2026 (Jeff Billo, VP Interconnection and Grid Analysis). Source: [ERCOT Board Item 8, "Interconnection and Grid Analysis Update" (Jun 2026)](https://www.ercot.com/files/docs/2026/05/24/8-Interconnection-and-Grid-Analysis-Update.pdf) [independent].
  - ERCOT is "tracking ~438 GW of Large Load Interconnection requests and ~452 GW of Generation Interconnection requests".
  - "The vast majority of requests do not have any studies submitted."
  - The one-at-a-time study process (PGRR115) ends on 10 July 2026, when ERCOT switches to batch studies.
  - The Q4 2026 Quarterly Stability Assessment includes "~4.0 GW of new Generation and ~3.9 GW of Large Load expected to energize in Q4 2026". That is about 3.9 GW actually energising in one quarter against about 438 GW requested.
  - Pin Oak Peaking Energy Center (459 MW gas, Freestone County) became the first Texas Energy Fund project approved for commercial operation.
- Ascend Analytics: in ERCOT, "198 GW of large load applied for interconnection in the first quarter of 2026 alone", and 86 GW of new requests were under review. Source: [Ascend Analytics (5 May 2026)](https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access) [independent]. The ERCOT figure is not sourced to an ERCOT primary document.
- An April 2026 report put ERCOT's large-load queue above 410 GW after Oncor submissions. Source: [RTO Insider (Apr 2026)](https://www.rtoinsider.com/129421-ercot-large-load-requests-soar-again/) [independent]. Search excerpt only; paywalled.
- **Dominion Energy Virginia** (Q3 2026 call, late October 2026). Source: [DCD (late Oct 2026)](https://www.datacenterdynamics.com/en/news/dominion-energy-reports-549gw-of-data-center-demand-in-various-stages-of-contracting/) [independent]; DCD returned 403, so these figures come from search excerpts of DCD, [Benzinga (Oct 2026)](https://www.benzinga.com/markets/earnings/26/10/62745619/dominions-contracted-data-center-capacity-climbs-to-nearly-55-gw-as-q3-beats) and [Investing.com (Q2 2026)](https://www.investing.com/news/company-news/dominion-q2-2026-slides-data-centers-surge-offshore-wind-81-done-93CH-4828982) [independent].
  - About **54.9 GW** of data-centre capacity "in various stages of contracting" as of September 2026, up about 6.3 GW (13%) since December 2025.
  - "more than 12GW" is under electric service agreements (ESAs).
  - Q2 2026 breakdown: 12 GW ESAs, 9.4 GW construction letters of authorisation, 32.4 GW in engineering. The total was 16.5 GW in July 2023.
  - Dominion's 2025 annual report says it has been "connecting an average of 15 data centers per year". Source: [Dominion 2025 ARS (SEC)](https://www.sec.gov/Archives/edgar/data/715957/000119312526115192/dei-ars-12312025.pdf) [independent – customer/utility]; search excerpt only.
- **Xcel Energy** (February 2026). Source: [POWER (5 Feb 2026)](https://www.powermag.com/xcel-energy-inks-dual-alliances-with-ge-vernova-nextera-to-support-6-gw-data-center-outlook-generation-expansion/) [independent].
  - More than 2 GW of data-centre ESAs signed, with targets of 3 GW by end-2026 and 6 GW contracted by end-2027.
  - Pipeline of about 4 GW "high-probability" plus more than 20 GW of prospects.
  - Data-centre sales are expected to ramp in 2029–2030.
- **NextEra** projects at least 15 GW of data-centre "hub" development by 2035, with an upside case of about 30 GW, and has identified more than 20 locations. Source: [Latitude Media (8 Dec 2025)](https://www.latitudemedia.com/news/nexteras-ai-bet-google-meta-and-more-gas/) [independent].
- **PJM**: the capacity shortfall "could reach 15 GW by 2030". Source: [Ascend Analytics (5 May 2026)](https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access) [independent].

**How many data centres are turning to on-site or bridge power**
- Cleanview, February 2026 snapshot, as reported by Power Engineering. Source: [Power Engineering (25 Feb 2026)](https://www.power-eng.com/onsite-power/trump-urges-tech-companies-to-build-their-own-power-plants-for-data-centers/) [independent].
  - 46 projects with 56 GW of planned BTM capacity, about 30% of planned US data-centre capacity in Cleanview's tracker. 90% were announced in 2025.
  - About 75% of the identified generating equipment (23 GW) is gas-fired.
  - Equipment commitments were confirmed at about two-thirds of projects, with suppliers including GE Vernova, Siemens, Caterpillar and Doosan.
  - Cleanview: "Speed to power is all that developers care about."
- Cleanview report, "Bypassing the Grid" (mid-2026; satellite images dated 13 May 2026). Source: [Cleanview report (mid-2026)](https://cleanview.co/reports/behind-the-meter-data-centers) [independent].
  - **59 data centres, about 90 GW** of BTM capacity, more than 25% of planned US data-centre capacity. 92% (about 82 GW) were announced since the start of 2025.
  - Status by share of capacity: **operating ~2.2% (about 2 GW)**, under construction 1.2%, permitted 36%, announced or early-stage 60%.
  - Five states hold 83% of proposed BTM capacity. Texas leads on announced capacity; Ohio leads on capacity under construction.
  - Forecast operating capacity: 2.8–3.2 GW by end-2026. By end-2027, about 13 GW if projects with signed tenants stay on schedule, or "as low as 5 GW" with delays.
- Cleanview newsletter (21 Oct 2026). Source: [Cleanview newsletter (21 Oct 2026)](https://newsletter.cleanview.co/p/data-center-developers-have-announced) [independent].
  - Headline: "more than 100 GW" announced. The body cites the June figure of about 90 GW and does not give an updated GW total.
  - A new daily-updated live tracker covers "more than 100 gas plants built to power data centers".
  - Since June, operating capacity has "nearly doubled" and capacity under construction has "roughly quadrupled".
- Wood Mackenzie, "US Data Center Pipeline: Q3 2025" (November 2025), as cited by Grid Strategies: just 9% of planned data centres include on-site generation, but those projects represent one-third of tracked capacity. Source: [Grid Strategies (Nov 2025)](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf) [independent].
- Grid Strategies: 16 GW-scale data centres totalling nearly 30 GW are scheduled online in 2026–2027. Nearly all have initial permits and about half are under construction. At least six plan on-site or co-located generation. Source: same report [independent].
- Global Energy Monitor, as relayed by Open Factory: 252 GW of US gas capacity was in development at the start of 2026, including 80.6 GW in Texas, of which about 40 GW is for data centres. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary].
- Open Factory's own model (base case) puts online BTM capacity at 3.0 GW by end-2026, 7.4 GW by end-2027 and 15.0 GW by end-2028 (range 10–22 GW for 2028). Source: same page [independent; secondary model].

**Government data: actual grid-connected gas build (my processing of EIA-860M, September 2026 file, downloaded 14 Nov 2026)**
Source for all bullets below: [EIA-860M September 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [independent; govt data].
- **Planned natural-gas generators: 71.1 GW in 495 generator rows.**
  - By plant type: combined-cycle parts 47.1 GW; simple-cycle combustion turbines 23.0 GW; internal-combustion (IC) engines 0.95 GW.
  - Under construction: 10.65 GW (8.71 GW up to half built, 1.94 GW more than half built). Built but not yet in service: 2.49 GW. Planned with approvals not yet started: 39.7 GW.
  - By planned online year: 2026 2.7 GW; 2027 10.7 GW; 2028 19.7 GW; 2029 15.7 GW; 2030 18.1 GW; 2031 2.3 GW.
  - By balancing authority: MISO 21.8 GW, ERCOT 17.4 GW, SPP 10.3 GW, PJM 7.2 GW.
- **Gas capacity actually entering service** (operating sheet, grid-connected): 2.44 GW in 2024, 5.26 GW in 2025 (simple-cycle 2.70 GW, IC engines 0.70 GW) and 3.72 GW in January–September 2026 (simple-cycle 2.45 GW, IC engines 0.30 GW).

### Inferences
- The ERCOT figures (about 474 GW requested, about 205 GW batch-eligible) and Dominion's (about 55 GW in contracting stages, about 12 GW under ESAs) show that most "demand" in queues is unfirm. This matches Grid Strategies' view that utility data-centre forecasts are inflated by about 40%.
- BTM generation is overwhelmingly announced, not built. About 2 GW was operating in mid-2026 against about 90 GW announced. The rapid jump in under-construction capacity after June 2026 (per Cleanview) suggests 2027 is the test year.
- EIA-860M shows only about 0.95 GW of planned grid-connected IC engines and almost no new fuel cells. The data-centre BTM fleet (engines, mobile turbines, fuel cells) is therefore largely invisible in federal generator statistics. That fits EIA-860's coverage of grid-connected plants. Independent trackers (Cleanview, Open Factory) are currently the main sources for the BTM fleet.

### Gaps
- Not retrieved after the search budget ran out:
  - EPRI's 2024 "Powering Intelligence" figures and any 2026 EPRI update.
  - Georgia Power, AEP and Oncor large-load pipelines and IRP figures.
  - PJM's January 2026 load forecast.
- I found no utility-by-utility statement of average **wait time in years** for a large-load connection. Dominion's throughput statement (about 15 data centres a year) is the closest.
- Not retrieved: BTM counts from Sightline Climate, S&P Global and Wood Mackenzie's 2026 updates.
- The IEA 2026 update figures are unverified.

---

## 2. Gas turbine market: orders, market shares, lead times, prices, slot reservations

### Takeaway
Independent and competitor data agree that 2025 orders were about double 2024 (about 58 GW).
- Global orders: about 96–110 GW, depending on source.
- US orders: about 40–51 GW.
- Wood Mackenzie puts manufacturing capacity at only 60–70 GW a year.

Large-frame delivery slots run out to 2028–2031, and buyers and analysts report waits of five years or more. Independent estimates put turbine prices at about three times 2019 levels. New combined-cycle projects are reported at about $2,000–2,800/kW installed.

Market-share data by manufacturer (McCoy, Dora, GlobalData) sit behind subscriptions and were not obtained. The only share figures found are company-reported.

### Cited Findings
**Order volumes (global and US)**
- McCoy Power Reports, via the Mitsubishi Heavy Industries "GTCC Business Briefing" (7 Oct 2025, "Courtesy McCoy Power Reports"). Source: [MHI GTCC Business Briefing (7 Oct 2025)](https://www.mhi.com/finance/library/business/pdf/2025_gtcc_summary.pdf) [independent; competitor citing McCoy].
  - Global gas-turbine order volume by year: 2019 40.3 GW; 2020 39.7; 2021 34.6; 2022 50.4; 2023 43.6; **2024 57.4 GW** ("highest since 2018"); **first half of 2025 41.7 GW**.
  - North America: 14.9 GW in all of 2024, already 18.6 GW in the first half of 2025.
  - Middle East and North Africa: 16.0 GW in 2024 and 12.0 GW in the first half of 2025. China: 6.8 GW in 2024, falling to 0.4 GW in the first half of 2025.
- EPRI (Bobby Noble, EPRI gas-turbine R&D), opinion piece in Utility Dive. Source: [Utility Dive, "5-year waits and rising costs: How demand is redefining the gas turbine market" (23 Mar 2026)](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/) [independent].
  - "worldwide orders reached 846 gas turbines totaling 100.3 GW" in 2025, against 399 units and 58.2 GW in 2024.
  - US 2025: "427 units, representing 43.1 GW".
  - 70% of 2025 units were under 100 MW. H- and J-class units were more than half of the megawatts but only 14% of units.
- S&P Global and McCoy, as reported by ESG News. Source: [ESG News (25 Aug 2026)](https://www.esgnews.earth/latest-news/global-gas-turbine-orders-exceed-100-gw/21572.html) [independent].
  - Global 2025 orders were above 100 GW, the "second-strongest year on record" after the early-2000s merchant boom.
  - **US heavy-duty orders were 51 GW in 2025**, against an average below 10 GW a year over the previous 20 years.
- Mitsubishi Power, citing McCoy: US heavy-duty demand rose from 6.1 GW in 2020 to "nearly 40 GW" in 2025. Mitsubishi estimates hyperscale data centres account for about 45% of that growth. Source: [Power Engineering (26 Oct 2026)](https://www.power-eng.com/gas/turbines/mitsubishi-power-gas-turbine-savannah-georgia/) [independent reporting of competitor estimate].
- MHI estimated global power-generation gas-turbine orders at **96 GW in 2025** and expects about 70 GW a year on average over the next five years, roughly double the level of five years earlier. Source: [POWER, "Ansaldo Returns to U.S. Gas Turbine Market as Equipment Crunch Widens Supplier Field" (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent; citing MHI Q1 FY2026 materials, 6 Aug 2026].
- Wood Mackenzie: global turbine orders reached 110 GW at end-2025 against 60–70 GW a year of manufacturing capacity, with orders expected to peak in 2026. Source: [Power Engineering, "Gas turbine prices climb 195% as supply crunch reshapes power development" (1 Apr 2026)](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/) [independent].
- Global orders in Q2 2026 "hit a record 38 GW", up 71% year on year, with the US accounting for half. The original data source is not named. Source: [OilPrice.com (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent; secondary].
- Ansaldo's 2025 report says "final sales" in the 60-Hz gas-turbine market exceeded 61 GW in 2025, the second-best result since 1980. Ansaldo's 2025 orders were €2.3bn, up 24%. Source: [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent; competitor data].
- **Conflict between sources:** 2025 global orders are given as 96 GW (MHI), 100.3 GW (EPRI), more than 100 GW (S&P/McCoy) and 110 GW (Wood Mackenzie). US 2025 orders are given as 43.1 GW (EPRI, all sizes), "nearly 40 GW" (Mitsubishi/McCoy, heavy-duty) and 51 GW (S&P/McCoy, heavy-duty). The sources do not reconcile their scopes.

**OEM backlogs and capacity (company- and competitor-reported, via independent press)**
- GE Vernova, Q2 2026 call (22 Jul 2026), company-reported. Source: [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent].
  - 116 GW under contract: 53 GW firm and 63 GW under slot-reservation agreements. About 80% is traditional power and 20% data centres, across about 100 customers.
  - "Sold out through 2030".
  - Annualised output rising to 20 GW, then 24 GW in 2028 and 30 GW in 2030.
- GE Vernova Q3 2026 (28 Oct 2026): backlog plus slot reservations of 122 GW, with a target of at least 130 GW by year-end. Source: [GE Vernova 8-K (28 Oct 2026)](https://www.sec.gov/Archives/edgar/data/0001996810/000199681026000162/gev3q2026form8-k10282026.pdf) [company]; search excerpt only.
- Siemens Energy, Q3 FY2026 (5 Aug 2026), company-reported. Source: [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent].
  - 15 GW of orders and 6 GW of shipments in the quarter. Firm backlog 69 GW plus 26 GW of reservations.
  - "42%" share of the market for turbines above 100 MW in the quarter.
  - Large-turbine capacity: about 35 units in FY2026, about 50 in FY2027 and more than 50 in FY2028.
- MHI (competitor):
  - Large-frame backlog of 80 units and 35 GW at 30 June 2026, against 53 units and 23 GW a year earlier. Q1 bookings deliver in 2028–2030; projects under discussion target 2030–2031. Source: [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent].
  - $490m expansion of its Savannah plant, "more than doubling its manufacturing footprint". Source: [Power Engineering (26 Oct 2026)](https://www.power-eng.com/gas/turbines/mitsubishi-power-gas-turbine-savannah-georgia/) [independent].
- GE Vernova's Greenville plant: 55 heavy-frame units a year (14 GW simple-cycle), rising to 70–80 units a year from the second half of 2026 and shipping about 20 GW a year from 2027, at a cost of $160m. Source: [Modern Power Systems (Drew Robb, 9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/) [independent].
- Tony Brough of Dora Partners estimated that at the start of 2025 about 60 GW of gas-turbine orders were undelivered, plus perhaps 30 GW of unreported reservations. He says the backlog "grew markedly" in 2025 and extends to units as small as 5 MW, with Solar Turbines enjoying an order boom. Source: same Modern Power Systems article [independent].

**Market shares**
- The only shares found are company-reported: Siemens Energy's 42% of the above-100 MW market in its Q3 FY2026 (see above).
- Barclays, citing McCoy, says GE Vernova holds "around a quarter of the global gas turbine market". This appeared only in a search-result excerpt, with no date or base. Source: [GE Vernova deep dive (Substack)](https://jimmysjournal.substack.com/p/ge-vernova-ge-deep-dive) [independent; secondary]. Unverified.

**Lead times and delivery slots (customer, analyst and competitor statements)**
- Google's Lucia Tian: "Slots for new gas turbines are now going out to 2030." Source: [Modern Power Systems (9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/) [independent – customer].
- NextEra CEO John Ketchum. Source: [Latitude Media (8 Dec 2025)](https://www.latitudemedia.com/news/nexteras-ai-bet-google-meta-and-more-gas/) [independent – customer].
  - Gas generation "won't be available at scale until 2030".
  - NextEra has "secured turbine slots for 4 GW of combined-cycle gas plants".
- Ketchum in 2025: "To get your hands on a gas turbine and to actually get it built across the market, you're really looking at 2030, or later". Source: [Renewable Energy World (2025)](https://www.renewableenergyworld.com/energy-business/policy-and-regulation/nextera-ceo-warns-against-scorning-renewable-generation-amidst-long-lead-times-for-gas-and-nuclear-development/) [independent]; search excerpt.
- Ketchum in January 2026: "I don't worry too much about it in terms of gas turbine availability though", because NextEra had secured 4 GW of GE Vernova slots. Source: search excerpt of the same coverage [independent]; unverified on a primary page.
- EPRI: large turbines take "more than five years from order to delivery". Smaller turbines take 18–36 months. A unit ordered today will "not begin operating until 2031". Source: [Utility Dive (23 Mar 2026)](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/) [independent].
- Wood Mackenzie: "six-year lead times and order books sold through 2027". Source: [Power Engineering (1 Apr 2026)](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/) [independent].
- New combined-cycle plants took about 3.5 years in 2023 and roughly five now, seven for some heavy-duty frames. Siemens Energy quotes "three years or more" (company-reported). GE Vernova is "taking reservations for 2031 delivery" (company-reported). Source: [OilPrice.com (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent].
- Utilities securing turbines:
  - Duke has up to 11 GE Vernova 7HA turbines in addition to eight already secured. NRG, GE Vernova and Kiewit plan four combined-cycle plants (5 GW) in ERCOT and PJM, online 2029–2032. Source: [Modern Power Systems (9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/) [independent].
  - Xcel reserved five GE Vernova F-class turbines as "a first step" and has 24 gas combustion turbines on order across its vendors. Source: [POWER (5 Feb 2026)](https://www.powermag.com/xcel-energy-inks-dual-alliances-with-ge-vernova-nextera-to-support-6-gw-data-center-outlook-generation-expansion/) [independent].
  - Williams CEO Chad Zamarin said Williams has "secured positions" with equipment suppliers to stay ahead "through the end of the decade". Source: [Power Engineering (6 Nov 2025)](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-demand-accelerates/) [independent – customer].
- An independent lead-time tracker (Open Factory "Lead-Time Monitor", August 2026; weeks shown as minimum/typical/maximum) gives:
  - Heavy-duty frame turbine: 130/156/208.
  - Aeroderivative or mobile fleet: 17/52/78.
  - Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary—methodology not audited].

**Prices and installed costs**
- Wood Mackenzie: gas-turbine prices are up 195%, "nearly tripling from 2019 levels", and projected to reach **$600/kW by end-2027** for the turbine alone. Turbines are 20–30% of combined-cycle project cost. Source: [Power Engineering (1 Apr 2026)](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/) [independent].
- EPRI: average gas-turbine prices rose from roughly $2,000/kW to $3,000/kW in six months, "a nearly 50% increase". The article does not define the cost basis. Source: [Utility Dive (23 Mar 2026)](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/) [independent].
- BloombergNEF: the average combined-cycle project cost $2,157/kW in 2025, up from under $1,500/kW in 2023. Source: [OilPrice.com (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent].
- GridLab, Energy Futures Group and Halcyon: combined-cycle plants due in 2026 and 2027 reported $1,116–1,427/kW. Recent projects cost about $2,000/kW, and 2030–31 projects "routinely report $2,000 per kW or more". Anna Sommer: "Gas capital costs have been increasing at a pace that outstrips inflation." Sources: [APPA Public Power (13 Sep 2025)](https://www.publicpower.org/periodical/article/new-report-finds-rising-cost-new-gas-plants-outpacing-planning-assumptions) [independent]; [OilPrice.com (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent].
- NextEra (Ketchum, April 2025 call): a new combined-cycle plant costs about $2,600–2,800/kW, up from about $2,400/kW before tariffs and about $800/kW in 2021. At CERAWeek (March 2025) he said "The cost of gas-fired generation has gone up three-fold." Source: [Utility Dive (2025)](https://www.utilitydive.com/news/nextera-energy-ceo-urges-energy-pragmatism-amid-rising-costs-demand/746207/) and [Gas Outlook (2025)](https://gasoutlook.com/analysis/costs-to-build-gas-plants-triple-says-ceo-of-nextera-energy/) [independent – customer]; search excerpts.
- IEEFA, "The Misguided Stampede to Build Gas Power Plants" (April 2026). Source: [IEEFA (Apr 2026)](https://ieefa.org/sites/default/files/2026-04/The%20Misguided%20Stampede%20To%20Build%20Gas%20Power%20Plants_April%202026.pdf) [independent]; page returned 403, search excerpt only.
  - The newest combined-cycle proposals cost "at least $2,500 per kilowatt", excluding financing and pipeline costs.
  - Major makers have "essentially sold out their combined-cycle capacity through 2030".
  - The same excerpt set cited Dominion and Santee Cooper's proposed 2,180 MW South Carolina plant at about $5bn ($2,293/kW); the attribution of that figure to IEEFA is not confirmed.
- Ascend Analytics: a combustion turbine at a high capacity factor "carries an LCOE above $120 per megawatt-hour". Source: [Ascend Analytics (5 May 2026)](https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access) [independent].

**Slot reservations, deposits, cancellations**
- OilPrice describes slot-reservation agreements as paid options that convert to firm orders if projects proceed; if they do not, the maker keeps the deposit. It also reports GE Vernova's Q2 2026 working-capital benefit from customer down payments as $6.4bn (company-reported). Source: [OilPrice.com (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent].
- GE Vernova, on its earnings call: slot-reservation pricing is "10 to 20 points higher" (company-reported). Source: [POWER (5 Feb 2026)](https://www.powermag.com/xcel-energy-inks-dual-alliances-with-ge-vernova-nextera-to-support-6-gw-data-center-outlook-generation-expansion/) [independent].
- A buyer's guide found no public fee percentages, deposit amounts or refund schedules for slot reservations. Source: [SecondWatt (26 Aug 2026)](https://secondwatt.com/resources/gas-turbine-orders-2025-backlog-lead-times-buyer-guide) [independent; secondary].

**New entrants and alternative suppliers**
- **Doosan Enerbility** (competitor):
  - Added an order for seven 380 MW-class turbines from an unnamed US firm. Deliveries start in May 2029, one unit a month. This brings its North American contracts to 12 units and its global total to 23. Source: [The Elec (9 Mar 2026)](https://www.thelec.net/news/articleView.html?idxno=5731) [independent].
  - xAI reportedly bought five 380 MW-class Doosan turbines, which Elon Musk confirmed. Source: [Asia Business Daily (6 Jan 2026)](https://view.asiae.co.kr/en/article/2026010616252732960) [independent]; search excerpt only.
- **Ansaldo Energia** returned to the US after more than 30 years with an order from Pacifico Energy (Texas) for eight AE64.3A turbines (78 MW each, about 624 MW), first deliveries 2027 (announced July 2026). Source: [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent].
- **Boom Supersonic / Baker Hughes**:
  - In December 2025 Crusoe was named launch customer for 29 "Superpower" 42 MW turbines (1.21 GW, more than $1.25bn). Baker Hughes is to supply 25 BRUSH generators. Source: [Power Engineering (25 Feb 2026)](https://www.power-eng.com/onsite-power/trump-urges-tech-companies-to-build-their-own-power-plants-for-data-centers/) [independent].
  - By September 2026 the order was "effectively on ice". Boom CEO Blake Scholl confirmed that Boom's "stationary power plants are no longer part of Crusoe's near-term plans". Source: [Crypto Briefing (25 Sep 2026)](https://cryptobriefing.com/crusoe-abandons-boom-supersonic-turbine-deal/) [independent; secondary].
- **ProEnergy**: Crusoe ordered 13 PE6000 aeroderivative packages (650 MW), announced 16 April 2026. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary]. Not verified against a primary source.

### Inferences
- Independent confirmations that large-frame slots run to about 2030–2031: Google, NextEra, EPRI, MHI's own delivery windows and the IEEFA excerpt. These broadly corroborate the OEMs' "sold out" messaging. Wood Mackenzie's "sold through 2027" (April 2026) gives a shorter horizon, probably reflecting firm orders only.
- The OEMs' combined firm-plus-reservation books (about 220–247 GW per POWER and OilPrice) are several times annual capacity (60–70 GW, Wood Mackenzie). Reservations are options that can lapse with a forfeited deposit, so headline backlogs overstate firm demand.
- The surge in small (under 100 MW) and aeroderivative units, 70% of 2025 units per EPRI, is consistent with data-centre developers buying whatever ships fastest ("speed to power", Cleanview).
- The EIA-860M figure for gas entering service (5.26 GW in 2025) is an order of magnitude below 2025 US orders (43–51 GW). This shows the multi-year gap between orders and operating capacity.

### Gaps
- No independent 2025–2026 share table by manufacturer from McCoy, GlobalData or Dora Partners; these are subscription data.
- Refurbished or used turbine prices and volumes: not found. Cleanview mentions refurbished industrial turbines in use but gives no figures.
- Slot-reservation fee levels and documented slot cancellations at GE Vernova, Siemens Energy or MHI: not found.
- Not retrieved: Lazard LCOE+ 2025 and 2026; EIA capital-cost assumptions; Baker Hughes NovaLT data-centre orders; Mitsubishi aeroderivative (FT8) orders; Entergy's and Duke's own lead-time statements.

---

## 3. Reciprocating engine and fuel-cell market data

### Takeaway
Reciprocating engines are a mainstream "fast power" option for BTM data-centre plants.
- Caterpillar (with Solar Turbines) has the largest share of BTM projects in Cleanview's tracker.
- Wärtsilä reports more than 3 GW of US data-centre engine sales.
- INNIO Jenbacher engines underpin VoltaGrid's deals.

Independent indicators say engine lead times are lengthening.

Among fuel cells, only Bloom has GW-scale data-centre deals in independent sources. Federal data cannot confirm deployed BTM fuel-cell volumes: EIA-860M lists only about 374 MW of grid-reported fuel cells nationally and almost no 2025–2026 additions.

### Cited Findings
**Reciprocating engines**
- Cleanview, mid-2026: "Caterpillar has the highest market share (33%) of projects we track", with more than 8.8 GW of permitted Caterpillar and Solar Turbines equipment. Bloom holds 14%. Source: [Cleanview report (mid-2026)](https://cleanview.co/reports/behind-the-meter-data-centers) [independent].
- **Wärtsilä** (competitor):
  - 282 MW order (15 × 50SG engines) for a US data centre developed by a major independent power producer, delivery 2028 and full operation 2029. Wärtsilä counts this as its seventh US data-centre order, taking US data-centre capacity sold above 3 GW. Source: [Wärtsilä press release (5 Oct 2026)](https://www.wartsila.com/media/news/05-10-2026-wartsila-to-supply-282-mw-onsite-power-solution-for-a-u-s-data-center-as-ai-growth-intensifies-demand-for-reliable-power-3797450) [independent; competitor].
  - Earlier 2026 orders: 429 MW (24 engines) in Q1 and 412 MW (34SG) in Q2. Source: [Wärtsilä announced orders](https://www.wartsila.com/investors/markets/announced-orders) [independent; competitor]; search excerpt.
  - January–September 2026 interim report: Q3 organic order intake up 41%, and engine lead times continue to lengthen. Source: [Wärtsilä Interim Report Jan–Sep 2026 (27 Oct 2026)](https://www.wartsila.com/media/news/27-10-2026-wartsila-s-interim-report-january-september-2026-3806530) [independent; competitor]; release summary via search excerpt.
- **INNIO Jenbacher and VoltaGrid**:
  - VoltaGrid will deploy 2.3 GW of Jenbacher-based modular generation for Oracle Cloud Infrastructure, with Energy Transfer supplying gas (announced October 2025). Source: [DCD (Oct 2025)](https://www.datacenterdynamics.com/en/news/voltagrid-to-supply-oracle-with-23gw-of-natural-gas-power-for-ai-data-centers/) [independent]; search excerpt.
  - Open Factory reports an INNIO order of 1.1 GW for more than 200 J624 engines (July 2026), a 1.25 GW INNIO–Rehlko framework (April 2026), a VoltaGrid order of 1.5 GW (300 Jenbacher units) and $5.0bn of VoltaGrid financing for a "4.3+ GW" plan. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary]. Not verified against primary sources.
- **Cummins**: plans to add 20 GW to reach 55 GW of high-horsepower output by 2030. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary].
- **Caterpillar** (company-reported, via a secondary source): large-engine backlog more than 3.5 times its January 2024 level, and a capacity target of 50 GW by 2030. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary]. Caterpillar's own disclosures are covered elsewhere.
- **Lead times** (Open Factory Lead-Time Monitor, August 2026): large reciprocating engines 78/104/130 weeks (minimum/typical/maximum). Source: same page [independent; secondary].
- EIA-860M (September 2026) lists only 0.95 GW of planned grid-connected natural-gas IC engines (66 rows). IC engines entering service on the grid were 0.70 GW in 2025 and 0.30 GW in January–September 2026. Source: [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [independent; govt data].

**Fuel cells**
- **AEP and Google, Wyoming**: a 702 MW Bloom solid-oxide fuel-cell plant near Cheyenne. Source: [Data Center Frontier (4 Nov 2026)](https://www.datacenterfrontier.com/energy/article/55413102/aep-google-advance-4-billion-fuel-cell-project-to-power-cheyenne-data-centers) [independent].
  - Cost about $4bn (about $5.7m per MW). AEP owns about 92% and Basalt the rest.
  - Google buys the full output under a 20-year PPA.
  - Construction is expected to start before end-2026, with full operation targeted for late 2028.
  - History: AEP and Bloom agreed in November 2024 on up to 1 GW (100 MW firm plus 900 MW of options). In January 2026 an AEP unregulated subsidiary committed about $2.65bn to buy "a substantial portion" of the option capacity.
- **Oracle and Bloom, "Project Jupiter"** (Doña Ana County, New Mexico): a 2.45 GW on-site plant that is "likely to miss its 2027 target after a pipeline was blocked". Source: [Cleanview report (mid-2026)](https://cleanview.co/reports/behind-the-meter-data-centers) [independent].
- **Supplier-side evidence of Bloom scaling**: LS Electric signed a 319bn won "distribution solution" contract with Bloom Energy in April 2026. Source: [Seoul Economic Daily (1 May 2026)](https://en.sedaily.com/finance/2026/05/01/korean-power-equipment-makers-clinch-record-orders-on-us) [independent].
- **NTT and Bloom**: NTT agreed to deploy 900 MW of Bloom fuel cells at its data centres, but the firm order size was not disclosed. Source: [StockTitan (2026)](https://www.stocktitan.net/articles/bloom-energy-ntt-900-mw-data-center-power-deal-2026) [independent; secondary]; search excerpt only.
- **Government data** (EIA-860M, September 2026). Source: [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [independent; govt data].
  - Operating fuel cells nationally: 373.8 MW in 187 generator rows. The entity named "Bloom Energy" accounts for 108.6 MW.
  - Fuel cells entering service: 14.0 MW in 2024, 8.0 MW in 2025 and 3.0 MW in January–September 2026.
  - Planned fuel cells: 0 MW.
- Lead times for solid-oxide fuel cells (Open Factory Lead-Time Monitor, August 2026): 8/40/78 weeks (minimum/typical/maximum). Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary].

**Standby and backup generators**
- Floodlight, via Open Factory: at least 38 Texas data centres have obtained minor air permits since 2024, covering more than 2,100 backup generators. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary].
- At Serverfarm's Covington, Georgia site, at least 36 of 37 planned diesel emergency generators were installed, according to the Southern Environmental Law Center (SELC) letter. Source: [Atlanta News First (2 Jul 2026)](https://www.atlantanewsfirst.com/2026/07/02/advocacy-groups-say-covington-data-center-power-plant-are-building-without-proper-permits/) [independent].

### Inferences
- In independent trackers, engines and Bloom fuel cells appear as the main non-turbine options for BTM plants that must be online before 2028. Lead-time indicators (Wärtsilä's "lengthening" comment; 78–130 weeks for large engines) suggest engines are no longer a short-lead item at GW scale.
- Bloom's data-centre deployments are mostly behind the meter and largely absent from EIA's generator inventory. Independent confirmation of installed MW therefore depends on customer disclosures (AEP, Oracle) and trackers (Cleanview), not federal statistics.

### Gaps
- Not found:
  - Rolls-Royce mtu data-centre order data.
  - Cummins primary statements.
  - FuelCell Energy and Doosan fuel-cell data-centre deployments, which are needed for the Bloom vs FuelCell vs Doosan comparison.
  - Independent standby-genset backlog and lead-time figures.
- Not found: independent measurements of Bloom installation time, from contract to commercial operation, at named sites.
- The Equinix–Bloom deployment status was not retrieved.
- NGI's article on engines (with a reported Chevron quote) returned HTTP 405 and could not be read.

---

## 4. Transformers, switchgear and HVDC supply: shortages, lead times, prices, imports, capacity additions

### Takeaway
Transformer supply remained tight in 2026.
- Wood Mackenzie (via secondary sources) estimates the US power-transformer shortfall fell from about 30% (2025) to about 15% (2026), yet GSU lead times reportedly rose above 160 weeks in Q1 2026.
- BLS price indices show transformer prices up about 88–96% since January 2020 and still rising about 6–7% year on year to October 2026. A further step-up came in July 2026.
- Switchgear prices are now rising faster than transformer prices: up 13.5% year on year.
- The US meets only about a fifth of power-transformer demand domestically.
- Korean exports of large transformers hit a record in 2025 (US about $738m), and Korean makers' backlogs stretch to 2031.

### Cited Findings
**Prices (government data; my calculations from BLS series via FRED, downloaded 14 Nov 2026; October 2026 values preliminary)**
- **Transformers and power regulators (WPU1174):** 235.9 in January 2020 to 442.392 in October 2026, **+87.5%**. Up **+5.6%** year on year (October 2025 was 419.045) and +11.6% on October 2024. Source: [FRED WPU1174](https://fred.stlouisfed.org/series/WPU1174) [independent; govt data].
- **Electric power and specialty transformer manufacturing (PCU335311335311):** 255.5 to 483.91, **+89.4%** since January 2020, and +5.6% year on year. Source: [FRED PCU335311335311](https://fred.stlouisfed.org/series/PCU335311335311) [independent; govt data].
- **Power and distribution transformers, except parts (WPU11740999):** 199.5 to 390.436, **+95.7%** since January 2020, and +6.9% year on year. Source: [FRED WPU11740999](https://fred.stlouisfed.org/series/WPU11740999) [independent; govt data].
- **July 2026 step-up:** month-on-month changes of +4.2% (WPU1174), +4.0% (PCU335311) and +4.6% (WPU11740999). Source: FRED series above [independent; govt data].
- **Switchgear and switchboard apparatus manufacturing (PCU335313335313):** 217.2 to 413.606, **+90.4%** since January 2020. Up **+13.5% year on year** (October 2025 was 364.494) and **+26.8%** over two years. Source: [FRED PCU335313335313](https://fred.stlouisfed.org/series/PCU335313335313) [independent; govt data].
- Wood Mackenzie (Q2 2025 survey, via secondary sources): unit prices up 77% for power transformers and 45% for GSUs since 2019. Source: search excerpts of [Wealthion](https://www.wealthion.com/learn/the-transformer-shortage-what-it-means-for-the-ai-buildout/) and [Industrial Sage](https://www.industrialsage.com/power-transformer-lead-times-us-grid-shortage/) [independent; secondary].
- IEA, via Korea Energy Insight: real cable costs nearly doubled since 2019, and power-transformer prices rose about 75%. Source: [Korea Energy Insight (5 Jun 2026)](https://www.energykor.com/p/korea-transformer-supercycle) [independent; secondary].

**Lead times and supply deficit**
- Wood Mackenzie Q2 2025 survey: power transformers about 128 weeks and GSUs about 144 weeks. In Q1 2026, GSU lead times passed 160 weeks, up from an average of 143 weeks in 2024 (Wood Mackenzie's Ben Boucher to Reuters, reportedly 9 July 2026). Sources: search excerpts of [Industrial Sage](https://www.industrialsage.com/power-transformer-lead-times-us-grid-shortage/) and [Explainx](https://explainx.ai/blog/transformer-lead-times-160-weeks-ai-data-centers-grid-equipment-shortage-2026) [independent; secondary]. The Reuters original was not retrieved.
- Wood Mackenzie's estimated US power-transformer shortfall fell from 30% (2025) to 15% (2026); the substation shortfall for 2026 is 8%. Source: search excerpts (same secondary sources) [independent; secondary]. Unverified against Wood Mackenzie.
- Wood Mackenzie: "demand for generator step up transformers increased by 274% between 2019 and 2025", and substation-transformer demand by 116%. PwC analysts put lead times for high-capacity units at up to four years. Source: [pv magazine USA (11 May 2026)](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) [independent].
- Korea Energy Insight: power transformers 128 weeks, GSUs 144 weeks, distribution transformers about 30 weeks. DC (HVDC) cable lead times exceed five years. Source: [Korea Energy Insight (5 Jun 2026)](https://www.energykor.com/p/korea-transformer-supercycle) [independent; secondary].
- DOE, as cited by TED Magazine: distribution transformers "now take more than 30 months to produce". Source: [TED Magazine (22 Aug 2025; updated 9 Jun 2026)](https://tedmag.com/trump-administration-increases-tariffs-on-certain-transformers/) [independent].
- Open Factory Lead-Time Monitor (August 2026; weeks, minimum/typical/maximum):
  - GSU transformer: 100/143/156.
  - Medium-voltage switchgear (15–38 kV): 44/60/104.
  - Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary].

**Import dependence**
- "only 20% of transformer demand is met by domestic supply", and the US lacks sufficient grain-oriented electrical steel (GOES) production. Source: [TED Magazine (22 Aug 2025)](https://tedmag.com/trump-administration-increases-tariffs-on-certain-transformers/) [independent].
- Korea Energy Insight says US domestic manufacturing meets about a fifth of power-transformer demand, and China holds close to 60% of global transformer capacity by industry estimates. Source: [Korea Energy Insight (5 Jun 2026)](https://www.energykor.com/p/korea-transformer-supercycle) [independent; secondary].
- Korea International Trade Association (KITA). Source: [AJU Press (21 Jan 2026)](https://www.ajupress.com/view/20260121151757742) [independent].
  - Korean exports of transformers rated 10,000 kVA or more reached **$1.3bn in 2025**, the highest since records began in 1977.
  - **The US took about $738m** (about 57%, my calculation). US shipments rose nearly seven-fold over three years.
  - Korean makers hold about 25% of the US transformer market.
- A Korean source says the US share of Korea's transformer exports rose from 32.3% in 2010 to 63.3% in 2024. Source: [Daum/Korean press](https://v.daum.net/v/1YhX5CphYQ) [independent]; search excerpt only.

**Korean makers' orders, backlogs and pricing (independent reporting)**
- Q1 2026 orders and backlogs. Source: [Seoul Economic Daily (1 May 2026)](https://en.sedaily.com/finance/2026/05/01/korean-power-equipment-makers-clinch-record-orders-on-us) [independent].
  - Hyosung Heavy Industries power equipment: 4.17 trillion won of orders; backlog 15.1 trillion won.
  - HD Hyundai Electric: $1.797bn of orders; backlog $7.888bn. Q1 orders were 42.6% of its $4.222bn annual target.
  - LS Electric: 627.1bn won of orders; backlog 5.64 trillion won.
  - Combined new orders exceeded 7 trillion won ($5.1bn), and combined backlog exceeded 32 trillion won.
  - Hyosung signed a 787.1bn won contract in February 2026 for 765 kV transformers and reactors with a US transmission operator.
  - A BNK Securities analyst said HD Hyundai Electric is "selectively taking orders", "leading to gradual price increases".
- Korean makers have contracts "stretching up to six years ahead", some booked through 2031. An industry official said: "Even with tariffs, clients are willing to pay more because products are in short supply." Source: [Transformer Magazine, via Chosun Biz (13 Nov 2025)](https://transformer-magazine.com/news/korean-power-equipment-makers-expand-amid-us-boom/) [independent].
- The three Korean makers' combined backlog was "roughly $20 billion (KRW 30 trillion)" by early 2026. Export prices rose while Korean domestic award prices stayed "comparatively contained". Factories prioritise earlier, larger, higher-margin export orders over Korean domestic projects. Source: [Korea Energy Insight (5 Jun 2026)](https://www.energykor.com/p/korea-transformer-supercycle) [independent; secondary].

**Capacity additions announced (as reported by independent outlets)**
- Hitachi Energy: more than $1bn of US investment, including a South Boston plant due online in 2028. Siemens: $421m for a transformer factory in Charlotte, North Carolina. Source: [pv magazine USA (11 May 2026)](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/) [independent; company plans as reported].
- HD Hyundai Electric: Alabama plant expansion to raise capacity by 30% by early 2026. Source: [AJU Press (21 Jan 2026)](https://www.ajupress.com/view/20260121151757742) [independent].
- HD Hyundai Electric: expansion of the Alabama plant to boost 765 kV transformer production by 2027. Source: [Transformer Magazine (13 Nov 2025)](https://transformer-magazine.com/news/korean-power-equipment-makers-expand-amid-us-boom/) [independent].
- HD Hyundai Electric: about $200m to raise extra-high-voltage capacity by 50%, with a second US plant scheduled to complete in April of the following year. Source: [HD Hyundai Electric release via Barchart](https://www.barchart.com/story/news/627111/hd-hyundai-electric-expands-u-s-production-subsidiary-solidifies-leadership-in-north-american-extra-high-voltage-power-transformer-market) [company]; search excerpt.
- Hyosung:
  - Will nearly double Memphis output to more than 250 units a year by 2027, and is building a $225m HVDC transformer plant in Changwon. Source: [AJU Press (21 Jan 2026)](https://www.ajupress.com/view/20260121151757742) [independent].
  - Is investing $157m to expand US transformer production (Reuters, December 2025, as cited). Source: [Korea Energy Insight (5 Jun 2026)](https://www.energykor.com/p/korea-transformer-supercycle) [independent; secondary].
- LS Electric: planned facilities in Texas and Utah. Source: [AJU Press (21 Jan 2026)](https://www.ajupress.com/view/20260121151757742) [independent].
- In-facility power equipment: LS Electric signed a 170bn won switchgear contract with AWS in April 2026. Source: [Seoul Economic Daily (1 May 2026)](https://en.sedaily.com/finance/2026/05/01/korean-power-equipment-makers-clinch-record-orders-on-us) [independent].
- Component bottleneck: bushings and on-load tap changers for high-voltage transformers depend on imports. Hyosung signed a 765 kV bushing contract with Trench Group in May 2026. Source: [Korea Energy Insight (5 Jun 2026)](https://www.energykor.com/p/korea-transformer-supercycle) [independent; secondary].

**Tariffs on transformers and GOES**
- Section 232 inclusions effective 18 August 2025: transformers containing non-US steel or aluminium face a 50% tariff on the value of that metal content. Dry-type and control transformers are affected. A NEMA-led coalition opposed applying Section 232 to transformers and grid components in April 2025. Source: [TED Magazine (22 Aug 2025; updated 9 Jun 2026)](https://tedmag.com/trump-administration-increases-tariffs-on-certain-transformers/) [independent].
- Proclamation 11021 (signed 2 April 2026, effective 6 April 2026) restructured the Section 232 steel, aluminium and copper tariffs to apply to full customs value. GOES is listed at 50% of full value. Source: [White House Annexes (Apr 2026)](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf) [independent – government]; search excerpt.
- A June 2026 proclamation modified the regime, with changes effective 8 June 2026 to 31 December 2027. Source: search excerpts of [GHY](https://www.ghy.com/trade-compliance/us-adjusts-section-232-tariffs-on-aluminum-steel-and-copper-full-customs-value-now-applies/) and [CTP](https://ctp-inc.com/articles/u-s-overhauls-section-232-tariffs-for-steel-aluminum-and-copper-products) [independent; secondary].
- One summary says a 15% "transitional rate" applies to metal-intensive grid components including transformers through 31 December 2027. A vendor blog instead claims a 25% Section 232 rate on finished transformers above 10,000 kVA with Korean and Indian exemptions. **These conflict and neither was verified against the Federal Register.** Sources: [DistroForge](https://distroforge.com/blog/section-232-tariff-grid-equipment-procurement-impact/) and [MegaGrid Supply](https://megagridsupply.com/insights/tariff-shock-transformers-2026) [independent; secondary].
- HD Hyundai Electric's tariff burden fell to $6.8m in Q3 2025 from $13.6m. Source: [Transformer Magazine (13 Nov 2025)](https://transformer-magazine.com/news/korean-power-equipment-makers-expand-amid-us-boom/) [independent; company figure].

### Inferences
- The BLS indices contradict any reading that transformer prices have plateaued. The indices rose again in July 2026 (+4–5% month on month), and switchgear inflation (+13.5% year on year) is now running ahead of transformers. That is relevant to in-facility and substation equipment suppliers.
- A falling Wood Mackenzie deficit estimate alongside rising GSU lead times is consistent with new capacity arriving in distribution and medium-voltage segments first, while large and GSU units remain constrained.
- US demand dominates Korea's export growth (about 57% of large-transformer exports in 2025), and Korean domestic projects lose slots to US orders. Sustained US pricing power for Korean makers, as reported by analysts, follows from this.

### Gaps
- Not retrievable in session:
  - NREL's February 2024 distribution-transformer study (www.nrel.gov is blocked by the session's network; it must be allowed in network settings).
  - The NIAC 2024 transformer report.
  - Wood Mackenzie's primary 2025 and 2026 deficit reports.
  - The Reuters July 2026 lead-time article.
- US Census and ITC HS 8504 imports by country: not retrieved, because the Census API now requires a key.
- Anti-dumping duty rates on large power transformers from Korea (Commerce administrative reviews 2025–2026): not found.
- Cleveland-Cliffs GOES capacity and output: not found.
- No independent tally of North American transformer capacity additions was found; the additions listed above are individual company plans.
- HVDC: no data retrieved on converter or cable slot availability, or on grid operators' framework agreements (for example TenneT or Amprion). The only items are Hyosung's HVDC transformer plant and the IEA statement that HVDC cable lead times exceed five years.
- Switchgear and UPS lead times from primary sources (manufacturer surveys, Wood Mackenzie): not found.

---

## 5. Data-centre on-site and bridge power deployments and the equipment each uses

### Takeaway
In independent sources, gas turbines (aeroderivative, industrial and frame), reciprocating engines and Bloom fuel cells are the equipment named for the large BTM projects.
- Caterpillar and Solar Turbines equipment appears at Abilene, Williams/Meta, Joule and Kilby.
- GE Vernova equipment appears at Abilene, Homer City and Kilby.
- Siemens Energy SGT-400s appear at Williams/Meta.
- Bloom appears at AEP/Google Wyoming and Oracle's Project Jupiter.
- Jenbacher engines appear with VoltaGrid.

Permitting and fuel supply, not equipment, are the visible constraints at several sites: xAI (both states), VoltaGrid in Georgia, Project Jupiter's gas pipeline, and Nebius in New Jersey.

### Cited Findings
| Project (operator; data-centre user) | Location | Size | Equipment / supplier (per independent sources) | Status and permits (date) | Sources |
|---|---|---|---|---|---|
| xAI Colossus 1 | Memphis, TN | Colossus 1 and 2 together have about 1,498 MW of operating gas-turbine capacity (Cleanview, mid-2026) | Mobile and aeroderivative gas turbines. **Makers not identified in sources read.** | Shelby County Health Department approved a 15-turbine permit after the SELC threatened suit. SELC flyovers found 35 turbines operating about four months after the early-2025 application. | [Scientific American (9 Sep 2026)](https://www.scientificamerican.com/article/spacexais-colossus-data-center-is-fueling-a-massive-backlash/) [independent]; [Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers) [independent] |
| xAI Colossus 2 power plant (MZX Tech, a SpaceX subsidiary) | Southaven, MS (serves Memphis) | Permit for 41 turbines, about 1,200 MW; about 1,775 MW installed by July 2026 | Turbine makers not named in sources read. Doosan reportedly sold xAI five 380 MW-class units (search excerpt). | MDEQ Permit Board approved the 41-turbine permit on **10 Mar 2026**. MDEQ counted 46 turbines (May), 60 (June) and 69 (July). A 30 Jul 2026 agreement lets 13 turbines run through year-end. The Permit Board denied the SELC-led appeal (reported 11 Nov 2026). NAACP Clean Air Act suit pending; DOJ moved to intervene for xAI. MDEQ treated unpermitted units as "temporary-mobile" (under one year). | [Mississippi Free Press (10 Mar 2026; upd. 22 Apr 2026)](https://www.mississippifreepress.org/mississippi-permit-board-grants-xais-request-for-41-southaven-gas-turbines-to-power-memphis-data-center/); [Sci Am (9 Sep 2026)](https://www.scientificamerican.com/article/spacexais-colossus-data-center-is-fueling-a-massive-backlash/); [Action News 5 (11 Nov 2026)](https://www.actionnews5.com/2026/11/11/state-rejects-appeal-over-spacexais-air-permit-southaven-facility/) [all independent] |
| Stargate Abilene (Crusoe; OpenAI/Oracle) | Abilene, TX | 360.5 MW permitted (TCEQ Reg. 177263); Grid Strategies says about 350 MW of BTM gas serves the first part of a campus of about 1.2 GW | **5 × Solar Turbines Titan 350 (38 MW) + 5 × GE LM2500 (34.1 MW)**. Crusoe ordered 10 GE LM2500XPRESS units (December 2024) plus 19 more (June 2025), about 35 MW each. | Registered 30 Aug 2024; modified 22 Jan 2025 (from 6+6 units to 5+5). Ten turbines reported built by July 2026. Phase one (about 200 MW) complete by February 2026 (MPS). Separate PSD permit 182126/PSDTX1688 (Longhorn Buildings 9–10) submitted 7 Nov 2025, draft noticed 5 Aug 2026, not issued. Press reports describe up to 49 turbines in total. | [Compute Atlas (upd. 16 Oct 2026)](https://www.compute-atlas.com/facilities/crusoe-abilene-onsite-generation-tx) [independent; secondary, cites TCEQ records]; [Modern Power Systems (9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/); [Grid Strategies (Nov 2025)](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf) [independent] |
| Williams "Socrates" North and South (Meta) | New Albany, OH | 400 MW (2 × 200 MW) | **Solar Turbines Titan 250 and PGM 130, Siemens Energy SGT-400, Caterpillar 3520 engines**. Two 24-inch gas pipelines. | Ohio Power Siting Board approved Socrates South on 9 Jun 2025. Service targeted for late 2026 under a 10-year PPA. Williams has committed $5.1bn in total, including a $3.1bn tranche for service by mid-2027 at about 20% pre-tax return. Cleanview: Meta plus EdgeConneX at New Albany total 736 MW under construction (mid-2026). | [Power Engineering (6 Nov 2025)](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-demand-accelerates/); [Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers) [independent] |
| Meta Hyperion: Entergy Louisiana plants | Richland Parish, LA | EIA-860M lists Richland Parish Power Station 1&2 at 1,560.6 MW and 3 and 4 at 780.3 MW each | **Turbine maker not identified in sources read.** | EIA status "P" (planned) as of September 2026 | [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [independent; govt data] |
| Oracle–VoltaGrid | Undisclosed sites | 2.3 GW (announced October 2025) | INNIO Jenbacher-based modular gensets; Energy Transfer gas; ABB | Separately, Texas filings reportedly show VoltaGrid approved for 210 Jenbacher units (700 MW) at a Shackelford County Stargate site (search excerpt). | [DCD (Oct 2025)](https://www.datacenterdynamics.com/en/news/voltagrid-to-supply-oracle-with-23gw-of-natural-gas-power-for-ai-data-centers/) [independent]; search excerpt |
| VoltaGrid / Serverfarm | Covington, GA | 90 MW | 33 × Jenbacher J620 (7 built by 19 Jun 2026) | No final permit (draft released). SELC letter of 25 Jun 2026 asked the Georgia Environmental Protection Division (EPD) to order construction to stop. EPD had not confirmed an investigation (2 Jul 2026). Serverfarm: "None of the generators have been operated nor will they be operated without a permit". | [SELC letter (25 Jun 2026)](https://www.selc.org/wp-content/uploads/2026/06/VoltaGrid-and-Serverfarm-Enforcement-Request.pdf); [Atlanta News First (2 Jul 2026)](https://www.atlantanewsfirst.com/2026/07/02/advocacy-groups-say-covington-data-center-power-plant-are-building-without-proper-permits/) [independent] |
| Oracle–Bloom, "Project Jupiter" (Stargate) | Doña Ana County, NM | 2.45 GW on-site | Bloom solid-oxide fuel cells | Gas pipeline blocked; "likely to miss its 2027 target" | [Cleanview (mid-2026)](https://cleanview.co/reports/behind-the-meter-data-centers) [independent] |
| AEP–Bloom for Google (Cheyenne Fuel Cell LLC) | Near Cheyenne, WY | 702 MW, about $4bn | Bloom solid-oxide fuel cells | Announced November 2026. Construction expected to start before end-2026; full operation targeted for late 2028; Google 20-year PPA. | [Data Center Frontier (4 Nov 2026)](https://www.datacenterfrontier.com/energy/article/55413102/aep-google-advance-4-billion-fuel-cell-project-to-power-cheyenne-data-centers) [independent] |
| AEP Ohio fuel cells (AWS, Cologix) | Ohio | Not confirmed (an aggregator cites 98 MW) | Bloom | Ohio regulators approved AEP installing and operating the fuel cells in June 2025 (search excerpt) | Search excerpts of [Enki AI](https://enkiai.com/fuel-cell/aep-bloom-energy-data-centers/) [independent; secondary] |
| Fermi America "Project Matador" | Amarillo area, TX | EIA-860M lists 11,679 MW of planned gas: combined-cycle parts 2027–2030 (5,472 + 1,560 + 300 MW turbines, 3,360 + 735 MW steam parts) plus 252 MW simple-cycle (2027) | Open Factory: seven leased GE TM2500 units landed; Siemens and GE frame units planned (secondary) | EIA status "T" (regulatory approvals received, not under construction), September 2026. Open Factory reports a TCEQ permit of about 6 GW dated 25 Feb 2026 (secondary). | [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [govt data]; [Open Factory](https://open-factory.com/articles/behind-meter-90gw/) [secondary] |
| Homer City Generating Station | Indiana County, PA | 4,396 MW in EIA (about 4.5 GW per Grid Strategies) | EIA lists seven combustion turbines of 360 MW each (four in 2028, three in 2029) with steam parts. GE Vernova supplies the turbines (Reuters, 2 Apr 2025, as cited by Grid Strategies). Open Factory says 7HA. | EIA status "P", September 2026 | [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [govt data]; [Grid Strategies (Nov 2025)](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf) [independent] |
| Joule Capital Partners campus | Utah | About 4 GW of on-site gas plus batteries (Caterpillar/Wheeler, per Caterpillar's 7 Aug 2025 announcement) | Caterpillar. Open Factory: 636 × Cat G3520K gensets; first phase ramps by early 2028 (secondary). | Not independently confirmed | [Grid Strategies (Nov 2025)](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf) [independent, citing company]; [Open Factory](https://open-factory.com/articles/behind-meter-90gw/) [secondary] |
| Pacifico Energy "GW Ranch" (Amazon-linked per Open Factory) | Pecos County, TX | TCEQ-permitted for up to 7.65 GW; 1.8 GW of batteries; up to 750 MWac of solar | **Ansaldo 8 × AE64.3A (about 624 MW)**, first deliveries 2027. Open Factory: 35 gas turbines, about 5 GW nominal (secondary). | First power targeted for Q1 2027; up to 1 GW in 2028; more than 5 GW by 2031 | [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent] |
| Pacifico "Fort Spunky" | Hood County, TX | 432 MW gas + 80 MW battery | Not stated | Air permits received; more than 450 MW to data-centre customers in 2028 | [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent] |
| Chevron / Engine No. 1 ("Project Kilby", per Open Factory) | Pecos County area, TX | 2,670 MW | Open Factory: 7 × GE Vernova 7HA.02 + 12 × Solar Titan 350; 20-year PPA signed 22 Jun 2026 ("Chevron/Microsoft") | **Unverified** against primary or independent news sources | [Open Factory](https://open-factory.com/articles/behind-meter-90gw/) [secondary] |
| NRG | ERCOT and PJM | 4 combined-cycle plants, 5 GW (2029–2032). EIA: NRG THW GT 377 MW entered service 2026; Greens Bayou 6, 447 MW simple-cycle, planned 2028. | GE Vernova (with Kiewit) | Under development | [Modern Power Systems (9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/); [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [independent] |
| Vantage (Virginia) | Virginia | 8 MW | Solar Turbines SMT-130 mobile turbines | Operating since September 2025 (secondary). A Vantage–VoltaGrid 1 GW deal was not retrieved. | [Open Factory](https://open-factory.com/articles/behind-meter-90gw/) [secondary] |
| Tallgrass "Cheyenne Power Hub" (phase one, for a large data centre; Open Factory links it to Crusoe's "Project Jade") | Cheyenne, WY | About 1,150 MW, more than $7bn | **2 × Mitsubishi M501JAC** | Turbines allocated (October 2026 report). Crusoe reportedly "stepped back" from a Wyoming campus (secondary, September 2026). | [Power Engineering (26 Oct 2026)](https://www.power-eng.com/gas/turbines/mitsubishi-power-gas-turbine-savannah-georgia/); [Crypto Briefing (25 Sep 2026)](https://cryptobriefing.com/crusoe-abandons-boom-supersonic-turbine-deal/) [independent] |
| Crusoe / Ensign wind co-location | Texas | 260 MW data centre + about 265.5 MW wind | Wind co-location | PUCT order of 24 Jul 2026: full site load must be able to curtail within 30 minutes in grid emergencies | [Verse (19 Aug 2026)](https://verse.inc/blog/texas-sb6-curtailment-rules-ercot-data-centers) [independent; secondary] |
| Nebius (Microsoft partner) | Vineland, NJ | 400 MW | On-site gas plant | Air-permit difficulties | [Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers) [independent] |
| Novva | West Jordan, UT | Not stated | Gas engines (four finished blocks, August 2026 imagery) | "one of the largest behind-the-meter projects operating" | [Cleanview newsletter (21 Oct 2026)](https://newsletter.cleanview.co/p/data-center-developers-have-announced) [independent] |
| Undisclosed IPP data centre | US | 282 MW | 15 × Wärtsilä 50SG | Delivery 2028, full operation 2029 | [Wärtsilä (5 Oct 2026)](https://www.wartsila.com/media/news/05-10-2026-wartsila-to-supply-282-mw-onsite-power-solution-for-a-u-s-data-center-as-ai-growth-intensifies-demand-for-reliable-power-3797450) [competitor] |
| Google / Intersect | Texas | Intersect USA "Quantum" and "Quantum II" BESS, 422.4 MW each (2026); Briggs Solar BESS 70.5 MW (2027) | Batteries (supplier not stated) | Listed in EIA-860M as planned. Google's acquisition of Intersect was not retrieved in session. | [EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx) [govt data] |

Additional deployment facts:
- Anthropic "has moved from a small buyer to one of the largest" in Cleanview's BTM tracker. No figures are given. Source: [Cleanview newsletter (21 Oct 2026)](https://newsletter.cleanview.co/p/data-center-developers-have-announced) [independent].
- Open Factory lists further projects that I did not verify independently. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary].
  - Stargate "Frontier" (Shackelford County): 2,580 MW, more than 670 reciprocating engines.
  - Monarch Compute Campus (Nscale/Microsoft): Caterpillar G3500-series engines.
  - Wärtsilä Ohio: 40 × 34SG, 412 MW. Wärtsilä Texas: 790 MW.
  - EdgeConneX New Albany: 336 MW.
  - Crusoe: 13 × ProEnergy PE6000.

### Inferences
- Caterpillar-group equipment (Solar Turbines plus Cat engines) recurs most often across independently documented BTM sites. That is consistent with Cleanview's 33% project share. Note that Solar Turbines is part of Caterpillar, so "Solar" units at Abilene, Williams/Meta and (reportedly) Kilby count towards Caterpillar.
- Many large announced campuses (Fermi, Homer City, Richland Parish, GW Ranch) still show planned or approval-stage status in EIA-860M or in independent reports as of September–November 2026. Most "fast" power actually operating comes from mobile and aeroderivative turbines and engine blocks, not frame units.

### Gaps
- Turbine makers for xAI's Memphis and Southaven fleets are not named in any source I read. Reports that Solaris Energy Infrastructure leases Solar Turbines units are not verified in-session.
- Not found:
  - Entergy's OEM for the Hyperion plants.
  - Fermi America's confirmed equipment contracts.
  - Equinix–Bloom status.
  - Google–Intersect deal terms.
  - Microsoft's own BTM projects.
  - Vantage–VoltaGrid 1 GW details.
  - Chevron/Engine No. 1 primary confirmation, including the customer.
- The Williams Socrates in-service status as of November 2026 is not confirmed.

---

## 6. Regulation and policy

### Takeaway
Federal regulators chose RTO-by-RTO "show cause" orders, not a national rule.
- On 18 June 2026 FERC issued Section 206 show-cause orders to six RTOs/ISOs. The DOE-initiated rulemaking (RM26-4) remains open.

Texas is implementing SB6:
- Batch studies for loads of 75 MW and above.
- Curtailment duties for co-located loads.
- A governor-directed pause on new data-centre approvals from 3 August 2026, pending an audit.

NERC escalated to a Level 3 alert (May 2026) after data-centre load-loss events, the largest nearly 4 GW in Virginia in July 2026. It is preparing registration of large loads by end-2026.

On-site generation faces state-level air-permit fights (xAI in Mississippi and Tennessee, VoltaGrid in Georgia). Tariffs (Section 232) raise costs for imported transformers and GOES.

### Cited Findings
**FERC and DOE**
- DOE (Secretary Chris Wright) directed FERC in October 2025 to consider large-load interconnection rules, using the Section 403 procedure, in docket RM26-4. Nearly 200 stakeholders commented. Source: [RMI, "Understanding FERC's Large Load Orders" (6 Jul 2026)](https://rmi.org/resources/understanding-fercs-large-load-orders/) [independent].
- From search excerpts of law-firm alerts: DOE's proposal targeted loads above 20 MW and asked for final action by 30 April 2026; a FERC order of 16 April 2026 said it would act by the end of June. Sources: [Akin Gump](https://www.akingump.com/en/insights/blogs/speaking-energy/doe-directs-ferc-to-initiate-large-load-interconnection-rulemaking) and [FERC Orders June 2026 summary](https://pranava0x0.github.io/FERC-Orders-June-2026/) [independent; secondary]. Not verified in the FERC record.
- **18 June 2026: FERC Section 206 show-cause orders** to PJM (EL26-67), SPP (EL26-68), NYISO (EL26-69), MISO (EL26-70), CAISO (EL26-71) and ISO-NE (EL26-72). Each must justify its tariff or file revisions. Source: [McGuireWoods (22 Jun 2026)](https://www.mcguirewoods.com/client-resources/alerts/2026/6/ferc-issues-section-206-show-cause-orders-directing-all-six-rtos-isos-to-justify-or-reform-large-load-integration-rules/) [independent].
  - Five reform categories: standardised applications and studies; cost-shift protections; co-location and BTM arrangements; new transmission services, including for flexible and co-located loads and loads with BTM generation; and studies of "electrically proximate" generation, meaning no more than two substations away.
  - Deadlines: 9 July (interventions), 20 July (resource-adequacy report), 3 August (requests for up to 90 days' abeyance), 17 August (show-cause filings), 16 September (comments).
  - RM26-4 was left open.
  - Concurrences by Chairman Swett and Commissioners LaCerte, Rosner, See and Chang.
- RMI adds: FERC suggested defining a large load as a new facility over 50 MW taking service above 69 kV. PJM was not ordered to reform co-location because it had already made a compliance filing in its co-location proceeding (EL25-49). SPP's earlier reforms for "high impact large loads" (HILL and HILLGA, ER26-247) were accepted. If abeyance is granted, filings move to 15 November and responses to 15 December 2026. Source: [RMI (6 Jul 2026)](https://rmi.org/resources/understanding-fercs-large-load-orders/) [independent].
- FERC's own page: [Commissioner Rosner's remarks on the large-load show-cause orders (18 Jun 2026)](https://www.ferc.gov/news-events/news/commissioner-rosners-remarks-large-load-show-cause-orders-e-7-e-12-june-18-2026) [independent – regulator]; not read in full.
- SPP: a HILLGA (expedited generator) study "completed in under 90 days". SPP's "CHILLS" filing offers "seven-year non-firm transmission service" as a bridge. Source: [Ascend Analytics (5 May 2026)](https://www.ascendanalytics.com/blog/large-load-interconnection-queues-data-center-grid-access) [independent].
- MISO filed large-load reliability tariff revisions on 28 Aug 2026 (ER26-3650). Source: search excerpt of [Infracompute regulatory tracker](https://www.infracompute.co.uk/tools/regulatory-tracker/us-ferc-large-load-interconnection) [independent; secondary]. Unverified.

**Texas (SB6, ERCOT, PUCT)**
- ERCOT: under SB6, a co-location arrangement letting ERCOT use the generator in emergencies applies only where the generation existed before 1 September 2025. Batch Zero milestones:
  - Study reviews under the old large-load process end on 10 July; utility packages due 24 July.
  - Classifications by 7 August; study begins no later than 2 September.
  - Financial security of $50,000/MW on reclassification.
  - Source: [ERCOT (29 Jul 2026)](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf) [independent].
- The PUCT approved Batch Zero on 18 June 2026 for loads of 75 MW and above. Source: [Sheppard Mullin](https://www.sheppard.com/insights/blogs/puct-approves-batch-zero-framework-that-will-provide-a-pathway-for-large-load-to-connect-to-the-grid-and-receive-electricity) [independent]; search excerpt.
- **3 August 2026: Governor Abbott** directed the PUCT and ERCOT to "pause new data center approvals until the agencies complete a project-by-project audit" of power and water use. ERCOT postponed the Batch Zero transmission planning study. No completion date had been announced as of 19 August. Sources: [Verse (19 Aug 2026)](https://verse.inc/blog/texas-sb6-curtailment-rules-ercot-data-centers) [independent; secondary, citing Houston Public Media]; corroborated by the headline of [Akin Gump, "Texas Pauses Data Center Interconnections Pending Statewide Audit"](https://www.akingump.com/en/insights/alerts/texas-pauses-data-center-interconnections-pending-statewide-audit) [independent]; the Akin page returned 403.
- The PUCT co-location curtailment rule (16 TAC §25.205, Project 58479) was adopted on 26 March 2026. A PUCT order of 24 July 2026 (Crusoe/Ensign) requires the full site load to be able to curtail within 30 minutes in emergencies. Source: [Verse (19 Aug 2026)](https://verse.inc/blog/texas-sb6-curtailment-rules-ercot-data-centers) [independent; secondary].
- Large-load interconnection standards (16 TAC §25.194, Project 58481): reportedly adopted 18 September 2026 and effective 8 October 2026, requiring disclosure of backup generation and curtailment protocols for loads of 75 MW and above interconnected after 31 December 2025. Sources: search excerpts of [NFM Consulting](https://nfmconsulting.com/knowledge/texas-sb6-large-load-ercot-data-center-compliance/) and [Gr1d](https://gr1d.us/insights/ercot-large-load-interconnection-texas) [independent; secondary]. The PUCT PDF returned HTTP 402 and could not be checked.

**NERC reliability**
- NERC Level 3 alert ("Essential Actions"), issued 4 May 2026. Source: [Utility Dive (5 May 2026)](https://www.utilitydive.com/news/nerc-issues-rare-level-3-alert-over-data-center-load-losses/819295/) [independent].
  - Transmission planners and operators, planning coordinators and balancing authorities must collect computational-load models and data, revise study thresholds, establish commissioning tests, and install dynamic fault recorders.
  - Acknowledgement was due 11 May and responses 3 August 2026.
- NERC (September 2026). Source: [NERC Reliability Insights (Sep 2026)](https://www.nerc.com/globalassets/who-we-are/news/2026/09/reliability-insights_large-computational-load-risks-due-to-voltage-sensitivity.pdf) [independent].
  - Load-loss events happen when, after normal fault-clearing voltage dips, data centres transfer load "to their backup power systems".
  - A fault on 18 April 2026 caused 500 MW of sustained data-centre load loss, against 1,500 MW in a similar July 2024 event. NERC attributes the improvement to changes in data-centre protection and ride-through settings.
  - "in July 2026, a nearly 4 GW customer-initiated load reduction occurred in Virgina", still under analysis.
  - FERC directed NERC to complete registry criteria and foundational Reliability Standards for large computational loads by end-2026.

**Air permitting of on-site generation**
- Mississippi: the MDEQ Permit Board approved xAI's 41-turbine Southaven permit (10 March 2026) and denied the appeal (reported 11 November 2026). MDEQ said earlier unpermitted units were "temporary-mobile". The NAACP Clean Air Act suit is pending, and DOJ sought to intervene for xAI. Sources: [Mississippi Free Press](https://www.mississippifreepress.org/mississippi-permit-board-grants-xais-request-for-41-southaven-gas-turbines-to-power-memphis-data-center/); [Action News 5 (11 Nov 2026)](https://www.actionnews5.com/2026/11/11/state-rejects-appeal-over-spacexais-air-permit-southaven-facility/); [Sci Am (9 Sep 2026)](https://www.scientificamerican.com/article/spacexais-colossus-data-center-is-fueling-a-massive-backlash/) [independent].
- Tennessee: Shelby County approved a 15-turbine permit for Colossus 1 after the SELC threatened suit. Source: [Sci Am (9 Sep 2026)](https://www.scientificamerican.com/article/spacexais-colossus-data-center-is-fueling-a-massive-backlash/) [independent].
- Georgia: the SELC asked the Georgia EPD (25 June 2026) to stop VoltaGrid and Serverfarm building before a permit was issued. Source: [SELC letter](https://www.selc.org/wp-content/uploads/2026/06/VoltaGrid-and-Serverfarm-Enforcement-Request.pdf); [Atlanta News First (2 Jul 2026)](https://www.atlantanewsfirst.com/2026/07/02/advocacy-groups-say-covington-data-center-power-plant-are-building-without-proper-permits/) [independent].
- Texas: the TCEQ issued a standard permit for Abilene's 10 turbines; a PSD permit for more is pending (draft 5 August 2026). Source: [Compute Atlas](https://www.compute-atlas.com/facilities/crusoe-abilene-onsite-generation-tx) [independent; secondary citing TCEQ]. The TCEQ also permitted GW Ranch for up to 7.65 GW. Source: [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/) [independent].

**Federal policy and trade**
- President Trump, State of the Union (24 February 2026), announced a "ratepayer protection pledge": "So I'm telling them they can build their own plant, they're going to produce their own electricity." There were no enforcement details. Source: [Power Engineering (25 Feb 2026)](https://www.power-eng.com/onsite-power/trump-urges-tech-companies-to-build-their-own-power-plants-for-data-centers/) [independent].
- Section 232 tariffs on transformers and GOES are covered in Section 4: 50% on steel and aluminium content from 18 August 2025, and the April 2026 Proclamation 11021 restructuring with GOES at 50%. Sources: [TED Magazine](https://tedmag.com/trump-administration-increases-tariffs-on-certain-transformers/); [White House Annexes (Apr 2026)](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf) [independent].
- DOE Section 202(c) emergency orders kept 8 plants in 7 states (5,349 MW) running. The Sierra Club estimates more than $235m in ratepayer costs for the first 13 orders. Source: [Open Factory (rev. 11 Oct 2026)](https://open-factory.com/articles/behind-meter-90gw/) [independent; secondary]. Unverified.

### Inferences
- The regulatory direction makes faster grid access conditional: non-firm or curtailable service, co-location rules, batch studies and NERC registration. Fast connection increasingly requires on-site generation, batteries or the ability to curtail. That supports demand for bridge and backup equipment, but adds permitting exposure.
- State air permitting has repeatedly lagged physical installation (xAI, VoltaGrid). This is a non-equipment bottleneck that equipment speed claims do not address.

### Gaps
- Not re-verified in session after the search budget ran out:
  - FERC's 1 November 2024 rejection of the Talen–Amazon Susquehanna amended interconnection agreement.
  - The text of FERC's December 2025 PJM co-location order (EL25-49).
  - RTO responses to the June 2026 orders, and any FERC action after August 2026.
- Not found:
  - EPA actions on permitting data-centre turbines and engines.
  - The fuel-cell provisions of the July 2025 "One Big Beautiful Bill Act" (Section 48E treatment).
  - Anti-dumping duties on Korean transformers.
  - EU grid-package and UK connection-reform measures for data centres.

---

## 7. Customer, utility and competitor statements that confirm or contradict the seven companies' claims

### Takeaway
Independent customers and analysts **broadly confirm** the OEMs' claims of sold-out large-frame capacity, rising prices and strong data-centre-driven demand. They also confirm Caterpillar's and Bloom's prominence in BTM projects. Several specific items are **contradicted or qualified**:
- Siemens Energy's market-size and lead-time framing.
- GE Vernova's "six months" aeroderivative timing, which is not like-for-like with order-to-delivery data.
- Speed claims for fuel cells at GW scale, against multi-year AEP and Oracle schedules.
- The scale of the BTM boom: about 90–100+ GW announced against about 2 GW operating.

No independent statements specific to Schneider Electric's or Hitachi Energy's data-centre claims were retrieved.

### Cited Findings
**GE Vernova**
- **Confirms "sold out through 2030" (GE Vernova Q2 2026 call, 22 Jul 2026, via [POWER](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/)):**
  - Google's Lucia Tian: "Slots for new gas turbines are now going out to 2030." [Modern Power Systems (9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/) [independent].
  - NextEra's Ketchum: gas "won't be available at scale until 2030". [Latitude (8 Dec 2025)](https://www.latitudemedia.com/news/nexteras-ai-bet-google-meta-and-more-gas/) [independent].
  - EPRI: an order placed today will "not begin operating until 2031". [Utility Dive (23 Mar 2026)](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/) [independent].
  - IEEFA: OEMs have "essentially sold out" combined-cycle capacity through 2030. [IEEFA (Apr 2026)](https://ieefa.org/resources/misguided-stampede-build-gas-power-plants) [independent; search excerpt].
- **Qualifies it:** Wood Mackenzie (April 2026) described order books as "sold through 2027" with six-year lead times. [Power Engineering (1 Apr 2026)](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/) [independent]. This is a shorter firm-order horizon, but consistent with long waits.
- **Confirms the slot-reservation model and that customers hold slots:**
  - NextEra secured slots for 4 GW. [Latitude (8 Dec 2025)](https://www.latitudemedia.com/news/nexteras-ai-bet-google-meta-and-more-gas/).
  - Xcel reserved five F-class turbines. [POWER (5 Feb 2026)](https://www.powermag.com/xcel-energy-inks-dual-alliances-with-ge-vernova-nextera-to-support-6-gw-data-center-outlook-generation-expansion/).
  - Duke has up to 11 7HAs plus eight secured. [Modern Power Systems (9 Feb 2026)](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/).
  - All [independent].
- **Context on reservation backlogs:** reservations are paid options and the deposit is kept if they do not convert. [OilPrice (22 Aug 2026)](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html) [independent]. Part of the 63 GW of reservations (July 2026) may therefore never become firm orders.
- **Claim vs. evidence on speed.**
  - GE Vernova (22 Jul 2026, via POWER): aeroderivatives take "about 6 months to commission".
  - Independent order-to-delivery data are longer: EPRI says smaller turbines take 18–36 months ([Utility Dive, 23 Mar 2026](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/)); Open Factory's monitor gives 17/52/78 weeks for aeroderivative or mobile fleets ([Open Factory](https://open-factory.com/articles/behind-meter-90gw/), secondary).
  - Customer case: Crusoe ordered LM2500XPRESS units in December 2024, and phase one (about 200 MW) at Abilene was complete by February 2026 ([MPS](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/)). That is roughly 14 months from first order to about 200 MW. Abilene's permitted fleet also included five Solar Titan 350s.
  - The metrics differ (commissioning after delivery vs. order-to-operation). Treat this as a qualification, not a direct contradiction.
- **Claim vs. evidence on data-centre share.**
  - GE Vernova (22 Jul 2026, via POWER): about 20% of gas backlog and reservations is with data centres.
  - Mitsubishi Power (competitor, October 2026) estimates hyperscale data centres account for about 45% of US heavy-duty demand growth, 2020–2025 ([Power Engineering, 26 Oct 2026](https://www.power-eng.com/gas/turbines/mitsubishi-power-gas-turbine-savannah-georgia/)).
  - These are different measures (direct data-centre contracts vs. growth attributable to data centres via utilities), so not a direct contradiction.
- **Confirms rising prices** (GE Vernova says reservation pricing is "10 to 20 points higher", via [POWER, 5 Feb 2026](https://www.powermag.com/xcel-energy-inks-dual-alliances-with-ge-vernova-nextera-to-support-6-gw-data-center-outlook-generation-expansion/)):
  - Wood Mackenzie: turbine prices up 195% vs 2019 ([Power Engineering, 1 Apr 2026](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/)).
  - EPRI: about $2,000 to $3,000/kW in six months ([Utility Dive, 23 Mar 2026](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/)).
  - All [independent].

**Siemens Energy**
- **Contradicted on market size.**
  - Claim: CEO Christian Bruch (5 Aug 2026) said the addressable gas-turbine market (above 10 MW) is **110–120 GW a year**, about half in the US. [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/).
  - Conflicting evidence: MHI (competitor, 6 Aug 2026) expects average demand of **about 70 GW a year** over the next five years. [POWER (1 Sep 2026)](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/).
  - Wood Mackenzie expects orders to **peak in 2026** and puts manufacturing capacity at 60–70 GW a year. [Power Engineering (1 Apr 2026)](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/).
  - All [independent].
- **Contradicted on lead time.**
  - Claim: Siemens Energy's CFO quoted lead times of "three years or more" (2026, via [OilPrice, 22 Aug 2026](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html)).
  - Conflicting evidence: EPRI says large turbines take "more than five years from order to delivery" ([Utility Dive, 23 Mar 2026](https://www.utilitydive.com/news/5-year-waits-and-rising-costs-how-demand-is-redefining-the-gas-turbine-mar/813385/)). Wood Mackenzie cites "six-year lead times" ([Power Engineering, 1 Apr 2026](https://www.power-eng.com/gas/turbines/gas-turbine-prices-climb-195-as-supply-crunch-reshapes-power-development/)). Combined-cycle plants take about five years, seven for some frames ([OilPrice](https://oilprice.com/Energy/Energy-General/The-Gas-Turbine-Shortage-Just-Became-AIs-Biggest-Constraint.amp.html)).
  - "Three years or more" is a lower bound, so this is a contradiction of the typical figure, not of the claim's literal wording.
- **Share claim unverified.** Claim: 42% of the above-100 MW market in Q3 FY2026 ([POWER](https://www.powermag.com/ansaldo-us-gas-turbine-market-equipment-crunch/)). No independent quarterly share data were found to confirm or refute it.
- **Confirms Siemens Energy equipment in data-centre BTM:** SGT-400 turbines at Williams' Socrates plants for Meta ([Power Engineering, 6 Nov 2025](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-demand-accelerates/)). Cleanview lists "Siemens" among confirmed suppliers ([Power Engineering, 25 Feb 2026](https://www.power-eng.com/onsite-power/trump-urges-tech-companies-to-build-their-own-power-plants-for-data-centers/)). Both [independent].

**Bloom Energy**
- **Confirms traction:**
  - Cleanview: Bloom has 14% of tracked BTM projects ([Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers)).
  - AEP and Google committed to 702 MW in Wyoming ([Data Center Frontier, 4 Nov 2026](https://www.datacenterfrontier.com/energy/article/55413102/aep-google-advance-4-billion-fuel-cell-project-to-power-cheyenne-data-centers)).
  - LS Electric's 319bn won supply contract with Bloom ([Seoul Economic Daily, 1 May 2026](https://en.sedaily.com/finance/2026/05/01/korean-power-equipment-makers-clinch-record-orders-on-us)).
  - All [independent].
- **Qualifies speed-to-power claims at scale.** Use Bloom's own wording from the company research. Evidence:
  - AEP's 702 MW project: construction to start before end-2026, full operation **late 2028**, about two years ([DCF](https://www.datacenterfrontier.com/energy/article/55413102/aep-google-advance-4-billion-fuel-cell-project-to-power-cheyenne-data-centers)).
  - Oracle's 2.45 GW Project Jupiter is "likely to miss its 2027 target" because its gas pipeline was blocked ([Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers)).
  - Typical solid-oxide fuel-cell lead time is 40 weeks, range 8–78 ([Open Factory](https://open-factory.com/articles/behind-meter-90gw/), secondary).
  - Fuel supply and permitting, not equipment delivery, set timelines in these cases.
- **Cannot be verified from government data:** EIA-860M shows only 8 MW of fuel cells entering grid service in 2025, 3 MW in January–September 2026, and 0 MW planned ([EIA-860M Sep 2026](https://www.eia.gov/electricity/data/eia860m/xls/september_generator2026.xlsx)) [govt data]. Installed BTM MW claims are not independently verifiable from federal statistics.

**Caterpillar (including Solar Turbines)**
- **Confirms market position:**
  - Cleanview: "Caterpillar has the highest market share (33%) of projects we track", with more than 8.8 GW of permitted Caterpillar and Solar equipment ([Cleanview](https://cleanview.co/reports/behind-the-meter-data-centers)).
  - Independently documented Caterpillar-group equipment: Solar Titan 350s at Abilene ([Compute Atlas](https://www.compute-atlas.com/facilities/crusoe-abilene-onsite-generation-tx), citing TCEQ); Solar Titan 250 and PGM 130 plus Cat 3520 engines at Williams/Meta ([Power Engineering, 6 Nov 2025](https://www.power-eng.com/gas/williams-pushes-deeper-into-power-generation-as-data-center-demand-accelerates/)).
  - Dora Partners' Tony Brough: Solar Turbines is "enjoying an order boom" ([MPS](https://www.modernpowersystems.com/data-centre-power/could-a-delivery-backlog-derail-a-gt-boom/)).
  - All [independent].
- **Qualifies engine-speed claims** (compare with Caterpillar's own statements in the company research):
  - Competitor Wärtsilä reports engine lead times "lengthening" (interim report, 27 Oct 2026) ([Wärtsilä](https://www.wartsila.com/media/news/27-10-2026-wartsila-s-interim-report-january-september-2026-3806530)) [competitor].
  - The independent monitor gives 78–130 weeks for large reciprocating engines (typical 104) ([Open Factory](https://open-factory.com/articles/behind-meter-90gw/), secondary).
- **Competitive pressure documented:** Wärtsilä has sold more than 3 GW of US data-centre engines ([Wärtsilä, 5 Oct 2026](https://www.wartsila.com/media/news/05-10-2026-wartsila-to-supply-282-mw-onsite-power-solution-for-a-u-s-data-center-as-ai-growth-intensifies-demand-for-reliable-power-3797450)). Jenbacher is behind VoltaGrid's 2.3 GW Oracle programme ([DCD](https://www.datacenterdynamics.com/en/news/voltagrid-to-supply-oracle-with-23gw-of-natural-gas-power-for-ai-data-centers/)).

**Hitachi Energy**
- **Confirms the investment claim as reported:** more than $1bn in US investment, including a South Boston plant online in 2028 ([pv magazine USA, 11 May 2026](https://pv-magazine-usa.com/2026/05/11/u-s-transformer-market-faces-severe-supply-constraints-as-lead-times-extend-to-four-years/)) [independent reporting of a company plan].
- **Evidence against any claim that the shortage is easing quickly:**
  - GSU lead times above 160 weeks in Q1 2026 (Wood Mackenzie via Reuters, secondary relay).
  - BLS transformer price indices up a further 5.6–6.9% year on year to October 2026, with a July 2026 step-up ([FRED WPU1174](https://fred.stlouisfed.org/series/WPU1174)) [govt data].
- **Evidence consistent with some easing:** Wood Mackenzie's estimated US power-transformer deficit fell from 30% (2025) to 15% (2026) (secondary relay; unverified).
- No HVDC-specific independent evidence on Hitachi Energy slots was retrieved.

**Schneider Electric**
- No independent statement specific to Schneider Electric's data-centre claims was retrieved.
- Relevant context for in-facility power:
  - The switchgear producer price index is up 13.5% year on year and 90.4% since January 2020 ([FRED PCU335313335313](https://fred.stlouisfed.org/series/PCU335313335313)) [govt data].
  - Competitor LS Electric won a 170bn won switchgear contract with AWS in April 2026 ([Seoul Economic Daily](https://en.sedaily.com/finance/2026/05/01/korean-power-equipment-makers-clinch-record-orders-on-us)).
  - NERC found that data-centre "backup power" transfer and protection settings drove grid load-loss events, including nearly 4 GW in Virginia in July 2026, and that changing ride-through settings reduced load loss from 1,500 MW (2024) to 500 MW (April 2026) ([NERC, Sep 2026](https://www.nerc.com/globalassets/who-we-are/news/2026/09/reliability-insights_large-computational-load-risks-due-to-voltage-sensitivity.pdf)). In-facility UPS and switchgear behaviour is now a reliability-regulation issue.

**HD Hyundai Electric**
- **Confirms record demand, long backlogs and pricing power:**
  - Q1 2026 orders of $1.797bn and a backlog of $7.888bn. A BNK analyst said it is "selectively taking orders", "leading to gradual price increases" ([Seoul Economic Daily, 1 May 2026](https://en.sedaily.com/finance/2026/05/01/korean-power-equipment-makers-clinch-record-orders-on-us)).
  - Korean makers' backlogs reach six years, some through 2031 ([Transformer Magazine, 13 Nov 2025](https://transformer-magazine.com/news/korean-power-equipment-makers-expand-amid-us-boom/)).
  - KITA data show record Korean large-transformer exports, with the US at about $738m in 2025 ([AJU Press, 21 Jan 2026](https://www.ajupress.com/view/20260121151757742)).
  - All [independent].
- **Context:** export prices rose while Korean domestic prices stayed contained ([Korea Energy Insight, 5 Jun 2026](https://www.energykor.com/p/korea-transformer-supercycle)). The tariff burden was $6.8m in Q3 2025 ([Transformer Magazine](https://transformer-magazine.com/news/korean-power-equipment-makers-expand-amid-us-boom/)).
- No independent figure contradicting HD Hyundai Electric's US share or capacity claims was found. A 25.7% US share in 2025 appears only in a Wikipedia citation of Korean press (search excerpt) and is unverified.

**Cross-cutting claims about the size of the "fast power" market**
- **Claim vs. evidence on the scale of BTM.**
  - Claim (multiple vendors and developers): a BTM build-out of about 90–100+ GW announced ([Cleanview, Oct 2026](https://newsletter.cleanview.co/p/data-center-developers-have-announced)).
  - Evidence: only about 2 GW (2.2%) was operating in mid-2026, and 60% existed only as announcements ([Cleanview report](https://cleanview.co/reports/behind-the-meter-data-centers)).
- **Claim vs. evidence on demand.**
  - Claim: utility forecasts of about 90 GW of data-centre load by 2030.
  - Evidence: Grid Strategies' market-analyst view of about 65 GW (overstated by about 40%) ([Grid Strategies, Nov 2025](https://gridstrategiesllc.com/wp-content/uploads/Grid-Strategies-National-Load-Growth-Report-2025.pdf)). In ERCOT, 474 GW requested against about 205 GW eligible for study ([ERCOT, 29 Jul 2026](https://www.ercot.com/files/docs/2026/07/29/ERCOT-Senate-July-29-Panel-1-Assessing-The-Grid.pdf)).
  - All [independent].
- **New-entrant claim vs. customer action.**
  - Claim: Boom Supersonic announced (December 2025) a $1.25bn, 1.21 GW launch order from Crusoe.
  - Evidence: by 25 September 2026, Boom's CEO confirmed that Boom's stationary plants "are no longer part of Crusoe's near-term plans" ([Crypto Briefing](https://cryptobriefing.com/crusoe-abandons-boom-supersonic-turbine-deal/)) [independent; secondary].

### Inferences
- The strongest independent corroboration is for the gas-turbine OEMs' scarcity and pricing claims. The weakest is for claims that depend on the BTM fleet's actual installed size or on deployment speed at GW scale. For those, independent evidence shows permitting and fuel supply constraints and very small operating capacity relative to announcements.
- Where the seven companies quote lead times or market sizes, independent figures tend to be less favourable for market size (MHI's 70 GW a year vs Siemens Energy's 110–120 GW a year) and longer for lead times (EPRI and Wood Mackenzie vs Siemens Energy's "three years or more").

### Gaps
- No independent statements were retrieved that address Schneider Electric's specific claims, for example on modular power, prefabricated systems or lead times.
- None were retrieved for Hitachi Energy's HVDC or transformer delivery claims.
- None were retrieved on Bloom's "within 90 days" or similar claims with site-level timing.
- Chevron's reported statement that "only one" announced BTM project "is at multi-gigawatt scale" (NGI, via Open Factory) could not be verified because the NGI page returned 405.

---

## 8. What could not be found or verified

### Takeaway
The main gaps are paywalled market data (McCoy, Dora and GlobalData shares; Wood Mackenzie primary reports) and several government sources that were unreachable (NREL blocked, Census API key, PUCT PDF paywalled, IEA 403). The web-search budget ran out mid-research, so policy items were not covered: OBBBA fuel-cell credits, anti-dumping duties, and EU and UK reforms. Several figures rest on secondary aggregators and are flagged as such.

### Cited Findings
- **Access failures in this session** (no data from these pages is used):
  - IEA Energy and AI pages returned HTTP 403 ([IEA](https://www.iea.org/reports/energy-and-ai/executive-summary)).
  - IEEFA page returned 403 ([IEEFA](https://ieefa.org/resources/misguided-stampede-build-gas-power-plants)).
  - DCD Dominion article returned 403 ([DCD](https://www.datacenterdynamics.com/en/news/dominion-energy-reports-549gw-of-data-center-demand-in-various-stages-of-contracting/)).
  - Akin Gump returned 403 ([Akin](https://www.akingump.com/en/insights/alerts/texas-pauses-data-center-interconnections-pending-statewide-audit)).
  - NGI returned 405 ([NGI](https://naturalgasintel.com/news/no-turbine-data-centers-find-faster-path-with-natural-gas-reciprocating-engines/)).
  - The PUCT Project 58481 adopted rule returned 402 ([PUCT](https://ftp.puc.texas.gov/public/puct-info/agency/rulesnlaws/subrules/electric/25.194/58481adt.pdf)).
  - The LBNL link redirected to an empty eScholarship page ([LBNL](https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report.pdf)).
  - The Nature article (2026) on AI data-centre demand needed authentication ([Nature](https://www.nature.com/articles/s44458-026-00152-5)).
  - www.nrel.gov does not resolve in this session's network and must be allowed in network settings.
  - The US Census trade API requires a key.
- **Conflicting secondary claims I found:**
  - Open Factory says Georgia EPD (2 July 2026) found VoltaGrid had installed 8 of 33 engines and "said construction must pause" ([Open Factory](https://open-factory.com/articles/behind-meter-90gw/)) [secondary].
  - Atlanta News First (2 July 2026) reports 7 of 33 engines, per the SELC's 19 June aerial images. It also reports that EPD had **not** confirmed an investigation and that no pause directive had been reported ([ANF](https://www.atlantanewsfirst.com/2026/07/02/advocacy-groups-say-covington-data-center-power-plant-are-building-without-proper-permits/)) [independent].
  - The Open Factory claim is therefore unverified or contradicted.
- **Section 232 transformer rate conflict:** a 15% "transitional" rate vs a 25% rate with Korean and Indian exemptions. Both appear only in secondary sources ([DistroForge](https://distroforge.com/blog/section-232-tariff-grid-equipment-procurement-impact/); [MegaGrid Supply](https://megagridsupply.com/insights/tariff-shock-transformers-2026)) and neither was verified in the Federal Register.
- **The 2025 global gas-turbine order total varies by source:** 96 GW (MHI), 100.3 GW (EPRI), more than 100 GW (S&P/McCoy) and 110 GW (Wood Mackenzie). US totals range from 40 to 51 GW. Sources as cited in Section 2.

### Inferences
- Because of these access limits, several "market-share" and "lead-time" comparisons rely on company-reported or secondary data. They are flagged in the notes and should not be presented as independently audited.

### Gaps
Searched for or required by the brief, but not found or not verified in this session:
1. **McCoy, GlobalData or Dora Partners** 2023–2026 order shares by OEM: GE Vernova, Siemens Energy, Mitsubishi, Ansaldo, Baker Hughes, Solar Turbines.
2. **Lazard LCOE+ (June 2025 and June 2026)** gas-peaker and combined-cycle cost ranges; **EIA** capital-cost assumptions for 2025–2026.
3. **Refurbished-turbine market** prices and volumes. Turbine **slot-reservation fee** levels and any documented **cancellations** at GE Vernova, Siemens Energy or MHI.
4. **Baker Hughes NovaLT** data-centre orders and **Mitsubishi aeroderivative** (FT8) orders. Primary confirmation of **ProEnergy**'s Crusoe order.
5. **Rolls-Royce mtu** and **Cummins** primary data-centre order figures. **FuelCell Energy** and **Doosan fuel cell** data-centre deployments. **Standby genset** backlog and lead times.
6. **Wood Mackenzie primary** transformer deficit reports (2025 and 2026); the **Reuters** July 2026 GSU lead-time story; the **NIAC June 2024** report; **NREL February 2024** distribution-transformer study (blocked host); **DOE** primary statements.
7. **Census or ITC HS 8504 import data by country**, including Korea's share of US imports.
8. **Anti-dumping duty** rates on Korean large power transformers. **Cleveland-Cliffs GOES** capacity. Any **independent tally** of transformer capacity additions. **HVDC** converter and cable slot availability, and TSO framework agreements (TenneT, Amprion, 50Hertz).
9. **Equipment suppliers** for:
   - xAI's Memphis and Southaven turbines.
   - Entergy's Hyperion plants.
   - Fermi America's frame units.
   - Equinix–Bloom.
   - Vantage–VoltaGrid (1 GW).
   - Microsoft's BTM projects.
   - Google–Intersect.
   Also not found: primary confirmation of Chevron / Engine No. 1 "Project Kilby".
10. **Regulation:**
    - FERC's 1 November 2024 Talen–Amazon rejection and the December 2025 PJM co-location order texts.
    - RTO responses to the June 2026 show-cause orders and FERC's subsequent action.
    - The final PUCT large-load rule text and date.
    - The status of Texas's 3 August 2026 pause.
    - EPA actions on data-centre generation permitting.
    - **OBBBA (July 2025) fuel-cell and other tax-credit changes.**
    - EU grid package and **UK connection reform** measures for data centres.
11. **Demand:**
    - IEA 2026 update figures on the IEA site.
    - EPRI 2024 and 2026 projections.
    - Georgia Power, AEP and Oncor large-load pipelines and IRP figures.
    - PJM's 2026 load forecast.
    - Average connection wait times in years by utility.
    - Sightline Climate and S&P Global BTM counts.
12. **Company-specific independent evidence** for Schneider Electric and Hitachi Energy, beyond the investment plans reported above.

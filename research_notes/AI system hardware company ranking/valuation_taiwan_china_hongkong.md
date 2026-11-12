# Entry-point evidence: system-level AI hardware companies listed in Taiwan, mainland China and Hong Kong (as of 12 November 2026)

Status: WORKING DRAFT v2, saved 12 Nov 2026 ~13:20 UTC. Sections marked PENDING are still being filled. Scope is valuation, cycle position, what the price assumes, dated events and investor access only. No ranking, no judgement of technology or business quality. Exploration notes, not personal financial advice; labels are not buy/sell instructions.

## Method, conventions and data limits
- Search tools were unavailable for this workstream (Firecrawl and Exa out of credits; the shared WebSearch budget was spent before any search ran). Everything below comes from direct fetches of known pages: Yahoo Finance chart/statistics/analysis pages; Yahoo Taiwan stock pages; TWSE and TPEx OpenAPI; Eastmoney F10 data endpoints; SEC EDGAR 6-K filings (TSMC, ASE); ASMPT investor-relations PDFs; Focus Taiwan (CNA) articles; HKEX Stock Connect lists and investor book; StockAnalysis statistics pages.
- Prices: closes of 12 Nov 2026 for Taiwan, Shenzhen, Shanghai and Hong Kong; 11 Nov 2026 close for US ADRs (US market had not opened at fetch time). FX on 12 Nov 2026 (Yahoo): USD/TWD 32.919, USD/CNY 6.6575, USD/HKD 7.8442. Source for all prices and returns: Yahoo Finance chart endpoint, fetched 12 Nov 2026 ([2330.TW example](https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?range=5y&interval=1d)).
- Returns are price returns: YTD from the 31 Dec 2025 close, 12 months from the 12 Nov 2025 close, "since Jan 2023" from the 30 Dec 2022 close. Drawdown is from the 52-week closing high.
- Market caps are computed as price x shares. Share counts come from MOPS share capital / NT$10 par (Taiwan, 30 Sep 2026), Eastmoney share-structure data (A shares), or Yahoo (TSMC, ASMPT). Yahoo's own market caps for several A-shares use stale share counts and are not used.
- Trailing P/E uses the last four reported quarters to Sep 2026, computed from reported quarterly EPS. TWSE's official daily P/E (BWIBBU) still used four quarters to Jun 2026 on 11 Nov because Q3 statements were still being filed, so it reads higher; both are shown.
- Consensus sources: Yahoo Finance analysis pages (TSMC, ASE; as of 12 Nov 2026); Eastmoney profit-forecast endpoint (A-shares; Chinese brokers, average of the last six months, as of 12 Nov 2026); StockAnalysis forward P/E (Delta; as of 12 Nov 2026). Eastmoney consensus for some names lags Q3 results (flagged where it does).
- Non-English sources: Eastmoney (Chinese), Yahoo Taiwan stock pages and MOPS/TWSE OpenAPI fields (Chinese). Hong Kong and Taiwan disclosures used here were in English (ASMPT, TSMC, ASE 6-K, Focus Taiwan).

## Market backdrop: dated sell-offs and events, Oct-Nov 2026
- 15 Oct 2026: Taiex -3.41% to 46,969.87 on Fed-hike fears after US September CPI of 3.7% (vs 3.6% expected); ASE fell 10% (limit down) to NT$673 — [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150013)
- 30 Oct 2026: Taiex -2.49% to 45,211.83 "amid growing concerns that massive AI investments would not deliver comparable returns" after Alphabet's disappointing sales and Amazon's soaring AI spending — [Focus Taiwan, 30 Oct 2026](https://focustaiwan.tw/business/202610300015)
- 5-6 Nov 2026: US midterms. Democrats won both chambers of Congress and governorships including Texas; dealers cited fears of restrictions on AI data-center development. Philadelphia Semiconductor Index fell 12.2% on 5 Nov (Yahoo ^SOX) and TSM ADR fell 10.8%. On 6 Nov the Taiex opened down a record 3,737.67 points, TSMC, Delta and ASE hit limit-down (NT$2,020, NT$1,020 and NT$515), and the index closed -4.51% at 39,701.64 — [Focus Taiwan, 6 Nov 2026](https://focustaiwan.tw/business/202611060006); [Focus Taiwan, 6 Nov 2026 close](https://focustaiwan.tw/business/202611060016)
- 6 Nov 2026: the National Financial Stabilization Fund (NT$500bn) authorised its 10th market intervention since 2000 — [Focus Taiwan, 6 Nov 2026](https://focustaiwan.tw/business/202611060020)
- 9-12 Nov 2026: Nvidia CEO controversy. Jensen Huang admitted an extramarital affair; media alleged the woman was a Chinese spy; Nvidia's board opened an investigation; three Republican lawmakers reportedly sought a closed-door meeting on whether high-end chips and servers reached China through third countries. On 12 Nov, Nvidia was down about 8% after hours on reports that the board was discussing whether to remove Huang. The Taiex fell 2.63% to 43,091.87, with TSMC -2.30% to NT$2,340 and ASE -5.02% to NT$586 — [Focus Taiwan, 9 Nov 2026](https://focustaiwan.tw/business/202611090013); [Focus Taiwan, 12 Nov 2026](https://focustaiwan.tw/business/202611120015)
- 10-11 Nov 2026: rebound (Taiex +2.52% and +3.62%) on a US rally, TSMC's October sales and its dividend increase — [Focus Taiwan, 11 Nov 2026](https://focustaiwan.tw/business/202611110018)
- MSCI November 2026 review (announced 11-12 Nov; effective after the close on 30 Nov 2026): Taiwan's weight in MSCI EM rises from 28.86% to 29.01%; Kinsus, Nan Ya PCB and Taiwan Union Technology join the MSCI Global Standard indexes (deferred from August because TWSE had flagged them as "disposition stocks"); TSMC's weight in MSCI Taiwan is cut 0.25 pp to 54.29% — [Focus Taiwan, 12 Nov 2026](https://focustaiwan.tw/business/202611120014)
- Index levels, 12 Nov 2026 (Yahoo): Taiex 43,091.87 (YTD +48.8%; -13.5% from the 6 Oct 2026 closing high of 49,822.55); SOX 10,564.11 on 11 Nov (YTD +49.1%; -27.8% from the 22 Jun 2026 high); Hang Seng 24,008.55 (YTD -6.3%).

## Tier 1 — TSMC (2330.TW; ADR TSM)

### 1. Price and performance
- TWD 2,340 close on 12 Nov 2026 (Yahoo; confirmed by [Focus Taiwan](https://focustaiwan.tw/business/202611120015)). ADR TSM: USD 413.35 close on 11 Nov 2026. 1 ADR = 5 shares; the ADR traded 13.7% above local parity on 11 Nov (local NT$2,395, FX 32.954; computed).
- Shares 25.93bn (Yahoo statistics). Market cap TWD 60.68tn = USD 1.843tn.
- EV ≈ TWD 57.5tn (USD 1.75tn) = market cap - total cash 4.02tn + total debt 0.818tn (Yahoo, quarter ended 30 Sep 2026; computed).
- 52-week range TWD 1,375 (24 Nov 2025) to 2,590 (6 Oct 2026, intraday). YTD +51.0%; 12 months +58.6%; since 30 Dec 2022 +421.7% (from NT$448.5). Closing high NT$2,585 on 6 Oct 2026; drawdown -9.5%. The 6 Nov 2026 close was NT$2,135 (intraday limit-down NT$2,020).

### 2. Valuation multiples (12 Nov 2026 price)
- Trailing P/E 23.8x on TTM EPS NT$98.27 (Q4'25 19.51 + Q1'26 22.08 + Q2'26 27.25 + Q3'26 29.43; [Yahoo TW EPS page](https://tw.stock.yahoo.com/quote/2330.TW/eps) and the Q3 release). TWSE's official P/E on 11 Nov was 27.76x (four quarters to Q2) — [TWSE OpenAPI BWIBBU_ALL](https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL)
- Forward P/E 21.2x on 2026E EPS NT$110.63 (35 analysts; range 98.4-113.4) and 15.6x on 2027E NT$149.53 (36; range 126.5-167.1). ADR: 23.6x 2026E (USD 17.50) and 17.7x 2027E (USD 23.39), including the ADR premium — [Yahoo analysis 2330.TW](https://finance.yahoo.com/quote/2330.TW/analysis/), [Yahoo analysis TSM](https://finance.yahoo.com/quote/TSM/analysis/), both 12 Nov 2026
- EV/EBITDA 15.9x (TTM EBITDA TWD 3.61tn); EV/sales 11.6x (TTM revenue TWD 4.94tn); P/B 8.6x (BVPS NT$271.60, 30 Sep 2026) — inputs from [Yahoo statistics](https://finance.yahoo.com/quote/2330.TW/key-statistics/)
- FCF yield ≈ 2.0% (Yahoo levered FCF TTM TWD 1.2tn; operating cash flow TTM TWD 3.13tn). Capex guidance for 2026 is US$60-64bn, unchanged — [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150018)
- Dividend yield: 1.24% on the last four declared quarterly dividends (NT$6+7+7+9 = 29); 1.54% on the new NT$9 quarterly run-rate (NT$36 a year). Q3 2026 dividend raised to NT$9.0 (board, 10 Nov 2026; ex-dividend 11 Mar 2027, payment 8 Apr 2027); Q2 2026 dividend of NT$7.0 goes ex on 10 Dec 2026 — [TSMC 6-K, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm); [Yahoo TW dividends](https://tw.stock.yahoo.com/quote/2330.TW/dividend)
- Own history (Yahoo quarter-end valuation measures, 2330.TW; quarter-ends 30 Sep 2025 / 31 Dec 2025 / 31 Mar 2026 / 30 Jun 2026 / 30 Sep 2026 / now): trailing P/E 23.4 / 25.6 / 26.6 / 32.7 / 29.0 / 24.6 (Yahoo, at the 11 Nov price); forward P/E 18.8 / 18.2 / 20.1 / 24.4 / 18.5 / 16.5; EV/EBITDA 13.6 / 15.4 / 16.5 / 20.9 / 19.0 / 16.3; P/B 7.4 / 8.0 / 8.4 / 10.6 / 10.0 / 8.9. 5- and 10-year ranges: PENDING (companiesmarketcap).
- Peers (Yahoo statistics, 11-12 Nov 2026; trailing P/E / forward P/E / EV/EBITDA / P/B): UMC 2303.TW 15.0 / 15.8 / 7.7 / 2.7; SMIC 0981.HK 46.5 / 27.1 / 15.4 / 2.1; Intel n/m / 37.0 / 180 (depressed EBITDA) / 2.7; Samsung Electronics 9.2 / n/m (Yahoo's 2.4x looks erroneous) / 5.0 / 2.5.

### 3. What the price assumes
- Consensus (Yahoo, 12 Nov 2026): EPS +67% in 2026 (66.25 to 110.63) and +35% in 2027 (to 149.53). The 2027 estimate rose 7.3% in 90 days (from 139.36); 27 upward and 2 downward revisions in 30 days.
- Company guidance: 2026 USD revenue growth about 44% (raised from "slightly more than 40%" in July); Q4 2026 revenue US$52.3-54.3bn (midpoint +58% YoY, +14% QoQ), gross margin 65-67%, operating margin 56.5-58.5% at NT$31.8 per US$. Capex 2026-28 to exceed the previous three years — [TSMC Q3 release (6-K exhibit)](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm); [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150018)
- Rough reverse reading (computed): at 15.6x 2027E, the price capitalises 2027 EPS at an earnings yield of 6.4%. To justify the price after 2027 at a terminal 15x, EPS needs to grow at roughly the cost of equity. Equivalently, holding 2027 EPS flat in 2028-30 would leave the stock at about 15.6x those years, below its recent forward range (18-24x). The multiple therefore does not require growth beyond 2027 at today's rate, but it does require 2027 to be delivered.
- Bridge vs successor: CoWoS (the bridge) is "customers' top choice" and TSMC will "ensure sufficient CoWoS capacity" (15 Oct call). The guidance and consensus as reported rest on current N2/N3 and CoWoS ramps; neither the 2026-27 numbers nor the multiple appear to need panel-level packaging (2028-29) or A16 to arrive on schedule. No source found here quantifying successor revenue in consensus (gap).

### 4. Cycle position
- Q3 2026 (15 Oct): revenue NT$1,494.24bn (+50.9% YoY, +17.6% QoQ), US$46.72bn (+41.2% YoY); gross margin 66.4%, operating margin 58.7%, net margin 51.1%; EPS NT$29.43 (+68.7% YoY). Wafer revenue mix: 2nm 8% (3% in Q2), 3nm 33%, 5nm 28%, 7nm 10%; 7nm and below 79% — [TSMC Q3 release](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm)
- Monthly revenue (TWD bn; YoY): Jun 442.68 (+67.9%); Jul 467.58 (+44.7%); Aug 514.81 (+53.3%); Sep 511.86 (+54.7%); Oct 586.89 (+59.7%, +14.7% MoM, a record); Jan-Oct 4,485.6 (+43.3%) — [TWSE OpenAPI t187ap05_L](https://openapi.twse.com.tw/v1/opendata/t187ap05_L); [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/2330.TW/revenue). October equals about 35% of the Q4 guidance midpoint converted at NT$31.8 (computed), so the quarter is tracking at or above guidance.
- Capacity and capital spending: capex US$60-64bn for 2026; board approved capital appropriations of about US$40.93bn on 10 Nov 2026 (advanced and specialty capacity, advanced packaging, fab construction, 2027 R&D capex) — [TSMC 6-K, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm)
- Margins against history: the Q3 gross margin of 66.4% and Q4 guide of 65-67% are the levels at hand. Previous peak and trough margins were not retrieved (PENDING; no remembered figures used).

### 5. Near-term events
- 30 Nov 2026 (after the close): MSCI rebalance; TSMC's weight in MSCI Taiwan cut to 54.29%.
- About 10 Dec 2026: November revenue (TSMC usually reports around the 10th; date not confirmed). 10 Dec 2026: ex-dividend NT$7.0.
- Mid-January 2027: Q4 2026 results and 2027 guidance (exact date not confirmed in sources accessed).
- 12 Nov 2026: NT$14.8bn green bonds listed — [Focus Taiwan, 4 Nov 2026](https://focustaiwan.tw/business/202611040008)
- 10 Nov 2026 board: up to US$500m for Anthropic shares at its IPO price, up to US$500m for OpenAI preferred stock, and up to US$500m for a strategic investment company — [TSMC 6-K](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm)
- Policy: the Nvidia board investigation and US congressional scrutiny of chip shipments to China; the new Democratic Congress (from January 2027) and possible AI data-center restrictions (see backdrop). TSMC is evaluating Texas production and cooperation with "Terafab" — [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150023)

### 6. Investor access
- TWSE 2330; NYSE ADR TSM (1:5). The ADR premium (13.7% on 11 Nov) is a cost of using the ADR route. Liquidity (20-day average traded value, computed from Yahoo volumes): 2330.TW about TWD 76bn (USD 2.3bn) a day; TSM ADR about USD 6.2bn a day.
- MSCI Taiwan weight 54.29% after the November review (Focus Taiwan). ETF weights: PENDING.
- Foreign-ownership rules for Taiwan listings were not checked against a primary source in this session (PENDING / unverified).

### 7. Suggested label: fair (as of 12 Nov 2026)
- Why: 15.6x 2027E is below TSMC's own 18-24x forward range at the last five quarter-ends; the cycle is still accelerating (October +59.7% YoY; Q4 guide +58% YoY); revisions are up. Against that, the stock is only 9.5% below its high while peers in AI hardware are 25-65% down, and policy and AI-capex sentiment risks are live.
- Better entry would be signalled by: (a) a price near NT$2,100 or lower (about 14x 2027E; the 6 Nov close was 2,135); (b) January 2027 guidance that holds 2027 growth near consensus (+35% EPS) with gross margin at or above 63%; (c) any sign that CoWoS lead times shorten or capex is trimmed without demand cuts; (d) a narrower ADR premium for ADR buyers.

## Tier 1 — ASE Technology Holding (3711.TW; ADR ASX)

### 1. Price and performance
- TWD 586 close on 12 Nov 2026 (-5.02% on the day; [Focus Taiwan](https://focustaiwan.tw/business/202611120015)). ADR ASX USD 37.82 (11 Nov); 1 ADS = 2 shares (the Q3 release shows EPS of NT$6.13 = US$0.384 per ADS); the ADR was 1.0% above parity on 11 Nov (computed).
- Shares 4.488bn (MOPS share capital NT$44.883bn, 30 Sep 2026). Market cap TWD 2.63tn = USD 79.9bn.
- Net debt TWD 306bn at 30 Sep 2026: short-term borrowings 70.4bn + bonds 42.2bn + long-term loans 276.6bn + current portion 5.1bn, less cash 88.4bn; net debt/equity 0.66 (0.47 at 30 Jun) — [ASE Q3 2026 6-K](https://www.sec.gov/Archives/edgar/data/1122411/000095010326016324/dp255760_6k.htm). EV ≈ TWD 2.94tn (USD 89bn), before non-controlling interests.
- 52-week range TWD 206 (19 Nov 2025) to 765 (12 Oct 2026). YTD +133.9%; 12 months +158.1%; since 30 Dec 2022 +524.1%. Closing high 762 (12 Oct 2026); drawdown -23.1%.

### 2. Valuation multiples
- Trailing P/E 33.4x (basic TTM EPS NT$17.56 = 3.39 + 3.24 + 4.80 + 6.13) or 34.9x on diluted (16.77). TWSE official on 11 Nov: 35.42x.
- Forward P/E 27.6x 2026E (NT$21.21; 14 analysts) and 17.4x 2027E (NT$33.67; 18 analysts; range 28.44-42.43). The 2027E rose from 28.72 to 33.67 in 30 days — [Yahoo analysis](https://finance.yahoo.com/quote/3711.TW/analysis/), 12 Nov 2026
- EV/EBITDA ≈ 15.5x (TTM EBITDA ≈ TWD 189bn, derived from Yahoo ASX EV/EBITDA 16.12 on EV US$92.55bn); EV/sales 3.7x (TTM revenue TWD 786.8bn); P/B 6.1x (BVPS NT$95.76).
- FCF yield negative, about -6% (Yahoo levered FCF TTM -TWD 166.85bn). Q3 operating cash flow NT$50.5bn against net PP&E payments of NT$125.9bn — ASE 6-K.
- Dividend yield 1.12% (FY2025 cash dividend NT$6.5848, ex-dividend 3 Jul 2026) — [Yahoo TW dividends](https://tw.stock.yahoo.com/quote/3711.TW/dividend)
- Own history (computed from quarter-end closes and basic TTM EPS): trailing P/E 20.1x (30 Sep 2025), 26.7x (31 Dec 2025), 30.2x (31 Mar 2026), 48.8x (30 Jun 2026), 40.0x (30 Sep 2026), 33.4x now. Yahoo's historical EV/EBITDA for 3711.TW: 8.0 / 11.5 / 13.0 / 25.5 / 21.2 at the same quarter-ends. 5- and 10-year ranges: PENDING.
- Peers (Yahoo, 11-12 Nov 2026; trailing P/E / forward P/E / EV/EBITDA / P/B): Amkor 13.9 / 13.3 / 6.9 / 1.8; Powertech 6239.TW 20.0 / n/a / 7.6 / 2.9; JCET and Tongfu in the Tier 2 table.

### 3. What the price assumes
- Consensus: EPS +139% in 2026 (8.89 to 21.21) and +59% in 2027 (to 33.67).
- Company guidance (29-30 Oct 2026): leading-edge advanced packaging and test (LEAP) revenue raised to US$4.0bn for 2026 (from US$3.7bn) and expected to double in 2027; 2026 capex raised to US$11.5bn (from US$10.5bn), 60% of new equipment for LEAP; Q4 consolidated revenue +6-8% QoQ; Q4 gross margin 23-24%, rising further in 2027 — [Focus Taiwan, 30 Oct 2026](https://focustaiwan.tw/business/202610300006). Q4 ATM revenue +11-13% QoQ, ATM gross margin +100-200 bp, EMS flat with about 2% operating margin, at NT$31.9 — [ASE 6-K investor presentation](https://www.sec.gov/Archives/edgar/data/1122411/000095010326016323/dp255782_6k.htm)
- Reading: 2027 consensus (+59%) is consistent with the company's LEAP doubling, so the multiple assumes guidance is met. It also prices ASE well above Amkor (17.4x vs 13.3x forward; EV/EBITDA about 15.5x vs 6.9x) while FCF is negative because of the capex step-up.
- Bridge vs successor: consensus rests on today's bridge (outsourced CoWoS-type and advanced test capacity working alongside TSMC). No evidence was found that fan-out panel or optical-engine packaging revenue is in 2026-27 numbers (gap).

### 4. Cycle position
- Q3 2026: revenue NT$244.16bn (+44.8% YoY, +27.8% QoQ, above the 21-22% guide); gross margin 22.1% (a record); operating margin 13.6%; net income NT$27.0bn; EPS NT$6.13 basic / 5.84 diluted. ATM revenue NT$151.5bn (+51.0% YoY), ATM gross margin 30.6% (27.3% in Q2), ATM operating margin 20.0%. EMS NT$93.5bn (+35.4% YoY) at 8.3% gross margin. Equipment capex US$2.10bn in the quarter — [ASE 6-K](https://www.sec.gov/Archives/edgar/data/1122411/000095010326016324/dp255760_6k.htm)
- Monthly revenue (TWD bn; YoY): Jun 65.78 (+32.9%); Jul 73.78 (+43.2%); Aug 82.25 (+45.7%); Sep 88.13 (+45.5%); Oct 88.62 (+47.1%, +0.6% MoM); Jan-Oct +32.2% — [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L); [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/3711.TW/revenue)
- Margins against history: Q3 gross margin of 22.1% is described by ASE as a new high; earlier-cycle peaks were not retrieved (PENDING).

### 5. Near-term events
- About 10 Dec 2026: November revenue. Late Jan or Feb 2027: Q4 results with 2027 capex and LEAP guidance (date not confirmed).
- 30 Nov 2026: MSCI rebalance (ASE weight change not reported).
- Same AI-capex and policy sentiment risks as TSMC (ASE fell 10% on 15 Oct and 5% on 12 Nov).

### 6. Investor access
- TWSE 3711; NYSE ADR ASX (1:2; near parity). Liquidity: 3711.TW about TWD 14.1bn (USD 0.43bn) a day; ASX about USD 0.42bn a day (20-day averages, computed).

### 7. Suggested label: stretched (borderline fair)
- Why: forward multiples sit above ASE's own trailing history (20-27x a year ago against 33x now) and well above Amkor, with negative FCF and rising net debt. The price leaves little room if 2027 LEAP doubling slips. Growth is real and guided, which is why this is borderline.
- Better entry would be signalled by: a price near NT$500 (about 15x 2027E; the 6 Nov limit-down was 515); evidence of LEAP 2027 orders (the Q4 call); capex intensity peaking with FCF turning positive; or an ATM gross margin above 31% sustained through Q1 2027.

## Tier 1 — Unimicron (3037.TW)

### 1. Price and performance
- TWD 792 close on 12 Nov 2026. Shares 1.644bn (MOPS share capital NT$16.439bn). Market cap TWD 1.30tn = USD 39.6bn. EV ≈ TWD 1.25tn (Yahoo implied net cash about TWD 0.05tn at 30 Sep 2026; approximate).
- 52-week range 157.5 (24 Nov 2025) to 1,420 (5 Oct 2026). YTD +260.0%; 12 months +376.5%; since 30 Dec 2022 +560.0%. Closing high 1,325 (5 Oct 2026); drawdown -40.2%.

### 2. Valuation multiples
- Trailing P/E 39.3x (TTM EPS 20.17 = 9M 2026 basic 17.85 from [TWSE OpenAPI t187ap06_L_ci](https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci) + Q4'25 2.32). TWSE official on 11 Nov: 44.72x. Caveat: 9M 2026 pre-tax profit of NT$35.04bn includes NT$15.10bn of non-operating income against NT$19.94bn of operating income, so trailing EPS is flattered (source of the gain not verified).
- Forward P/E: PENDING (no Yahoo consensus).
- P/B 7.3x (BVPS 108.24, 30 Sep 2026; it was about 2.6x a year ago on Yahoo data). Yahoo EV/EBITDA: 11.4x (30 Sep 2025), 15.2x (Dec 2025), 25.8x (Mar 2026), 51.2x (Jun 2026), 38.9x (Sep 2026), 22.5x now (Yahoo current, 11 Nov price).
- Dividend yield 0.25% (NT$1.98 for FY2025).
- Peers (Yahoo; trailing P/E / forward P/E / EV/EBITDA / P/B): Ibiden 4062.T 47.4 / n/a / 17.7 / 6.0; Samsung Electro-Mechanics 66.1 / 19.1 / 29.8 / 6.5; AT&S 82.3 / n/a / 12.7 / 5.7; Kinsus and Nan Ya PCB in the Tier 2 table.

### 3. What the price assumes: PENDING consensus. Reading so far: at about 39x trailing (inflated by non-operating gains), the price assumes ABF substrate tightness and pricing persist into 2027-28, before glass-core substrates (targeted 2027-28) could change the mix. No consensus source found yet to say whether glass core is in estimates.

### 4. Cycle position
- Monthly revenue (TWD bn; YoY): Jun 14.90 (+36.3%); Jul 16.25 (+43.7%); Aug 17.75 (+56.3%); Sep 18.65 (+64.7%); Oct 18.99 (+67.6%, +1.8% MoM); Jan-Oct +40.9%. Q3 revenue 52.65bn (+54.9% YoY, +22.8% QoQ; computed) — [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/3037.TW/revenue)
- Quarterly EPS: Q3'26 6.36, Q2'26 8.45 (non-operating gains), Q1'26 3.28, Q4'25 2.32, Q3'25 1.44. 9M 2026 gross margin 24.5%, operating margin 15.0% (computed from TWSE OpenAPI).
- Guidance and pricing commentary: PENDING.

### 5. Events: about 10 Dec 2026 November revenue; Q4 results in February 2027 (date not confirmed); 30 Nov MSCI rebalance (peers Kinsus and Nan Ya PCB join MSCI Standard).
### 6. Access: TWSE 3037 only (no ADR). Liquidity about TWD 21.5bn (USD 0.65bn) a day.
### 7. Suggested label: PENDING (provisionally stretched on trailing and book multiples).

## Tier 1 — Delta Electronics (2308.TW)

### 1. Price and performance
- TWD 1,240 close on 12 Nov 2026. Shares 2.598bn. Market cap TWD 3.22tn = USD 97.8bn; EV TWD 3.19tn (net cash 98.1bn = cash 213.2bn - debt 115.1bn) — [StockAnalysis statistics, 12 Nov 2026](https://stockanalysis.com/quote/tpe/2308/statistics/)
- 52-week range 886 (18 Dec 2025) to 2,585 (27 May 2026). YTD +28.8%; 12 months +28.2%; since 30 Dec 2022 +332.8%. Closing high 2,520 (27 May 2026); drawdown -50.8%. 6 Nov 2026: limit-down at NT$1,020 intraday, close 1,055.

### 2. Valuation multiples
- Trailing P/E 37.2x (TTM EPS 33.30 = 6.67 + 7.91 + 9.68 + 9.04). TWSE official on 11 Nov: 38.89x.
- Forward P/E 22.7x; EV/EBITDA 21.2x; EV/sales 4.55x; P/B 8.4x on StockAnalysis's basis (10.1x on parent BVPS of 122.50); P/FCF 48.5x; FCF yield 2.06%; dividend yield 0.94% (NT$11.60). Consensus: "Strong Buy" (22 analysts), average target NT$2,261, 3-year revenue growth forecast 39.1% and EPS growth 57.4% (as labelled on the page) — [StockAnalysis, 12 Nov 2026](https://stockanalysis.com/quote/tpe/2308/statistics/)
- Own history (Yahoo quarter-ends, 30 Sep 2025 / Dec 2025 / Mar 2026 / Jun 2026 / Sep 2026 / now): trailing P/E 50.9 / 50.2 / 59.8 / 72.1 / 60.3 / 38.4; forward P/E 36.2 / 30.3 / 40.8 / 51.1 / 30.6 / 22.9; EV/EBITDA 25.2 / 25.4 / 31.2 / 38.5 / 32.9 / 21.4 — [Yahoo statistics](https://finance.yahoo.com/quote/2308.TW/key-statistics/). Current multiples are the lowest of the six points. 5- and 10-year ranges: PENDING.
- Peers (Yahoo; trailing / forward / EV/EBITDA / P/B): Vertiv 36.3 / 19.9 / 25.8 / 13.6; Eaton 35.4 / 22.1 / 23.3 / 6.6; Schneider Electric 28.3 / 20.0 / 17.7 / 5.4; Lite-On (Tier 2).

### 3. What the price assumes
- At 22.7x forward, Delta trades in line with Eaton and Schneider and above Vertiv (19.9x), after its own forward multiple fell from 30-51x. The price assumes growth near consensus (the 3-year EPS growth figure is as labelled by StockAnalysis and may be a cumulative or annualised figure; not verified).
- Bridge vs successor: no source found here on how much 800V DC revenue is in consensus (gap). The move from 54V power shelves to 800V DC is a product transition inside Delta's own portfolio; the de-rating since May suggests the market is not paying ahead for it.

### 4. Cycle position
- Monthly revenue (TWD bn; YoY): Jun 65.60 (+55.4%); Jul 67.07 (+47.8%); Aug 64.59 (+35.0%); Sep 65.40 (+14.6%); Oct 74.67 (+30.1%, +14.2% MoM, the highest month in the series); Jan-Oct +36.3% — [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/2308.TW/revenue)
- Q3 2026 revenue 197.06bn (+31.1% YoY, +7.5% QoQ; computed); EPS 9.04 (+26.3% YoY but -6.6% QoQ). 9M 2026 gross margin 35.5%, operating margin 17.0% (TWSE OpenAPI). The Q3 earnings dip despite higher revenue is not explained in sources accessed (gap).
- Guidance and capacity commentary: PENDING.

### 5. Events: about 10 Dec 2026 November revenue; Q4 results and 2027 outlook in early 2027 (date not confirmed).
### 6. Access: TWSE 2308 only. Liquidity about TWD 19.8bn (USD 0.60bn) a day.
### 7. Suggested label: fair (provisional)
- Why: forward 22.7x is near large Western power peers and at the bottom of Delta's own five-quarter range, after a 51% drawdown. October revenue was a record, though growth slowed through Q3.
- Better entry would be signalled by: forward P/E below 20x (about NT$1,090, near the 6 Nov close of 1,055); Q4 margins recovering from the Q3 EPS dip; evidence of 800V DC or liquid-cooling orders in the Q4 call.

## Tier 1 — Asia Vital Components (3017.TW)

### 1. Price and performance
- TWD 2,775 close on 12 Nov 2026. Shares 406.8m (MOPS share capital NT$4.068bn). Market cap TWD 1.13tn = USD 34.3bn. EV ≈ TWD 1.10tn (Yahoo implied small net cash; approximate).
- 52-week range 1,205 (21 Nov 2025) to 3,700 (6 Oct 2026). YTD +83.8%; 12 months +84.4%; since 30 Dec 2022 +2,406%. Closing high 3,685 (6 Oct 2026); drawdown -24.7%.

### 2. Valuation multiples
- Trailing P/E 30.5x (TTM EPS 90.87 = 17.01 + 20.17 + 24.37 + 29.32). TWSE official on 11 Nov: 33.61x. P/B 16.3x (BVPS 170.53). Dividend yield 0.75% (NT$20.88). EV/sales 5.4x (TTM revenue NT$205.0bn).
- Forward P/E and EV/EBITDA: PENDING. Yahoo's EV/EBITDA (TTM to Jun 2026, stale) was 24.3x at the 11 Nov price; quarter-end history 16.3x (Jun 2025), 18.4x (Sep 2025), 22.8x (Dec 2025), 23.8x (Mar 2026), 24.4x (Jun 2026).
- Peers: Auras (Tier 2; TPEx trailing P/E 26.3x); Vertiv (above); Envicool and Jentech (Tier 2).

### 3. What the price assumes: PENDING consensus.

### 4. Cycle position
- Monthly revenue (TWD bn; YoY): Jun 17.62 (+66.1%); Jul 18.59 (+57.4%); Aug 19.48 (+54.3%); Sep 21.02 (+44.9%); Oct 22.10 (+34.4%, +5.2% MoM); Jan-Oct +65.6%. Q3 revenue 59.09bn (+51.8% YoY, +20.3% QoQ; computed). YoY growth is decelerating against stronger comparisons from late 2025 — [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/3017.TW/revenue)
- EPS Q3'26 29.32 (+114% YoY, +20% QoQ). 9M gross margin 32.2%, operating margin 26.9% (TWSE OpenAPI).

### 5-6. Events and access: November revenue about 10 Dec 2026; TWSE 3017 only; liquidity about TWD 8.7bn (USD 0.26bn) a day.
### 7. Suggested label: PENDING.

## Tier 1 — Zhongji Innolight (300308.SZ; H shares 3308.HK)

### 1. Price and performance
- A share CNY 508.90 close on 12 Nov 2026; H share HKD 649.50. The H share trades 8.3% above the A share (H/A 1.083 at CNY 0.8487 per HKD; computed).
- Shares: 1,177.9m in total = 1,115.2m A + 62.675m H. H shares first listed in Hong Kong on 30 Jul 2026 (54.5m shares; over-allotment raised this to 62.675m on 31 Aug 2026) — [Eastmoney share structure](https://emweb.securities.eastmoney.com/PC_HSF10/CapitalStockStructure/PageAjax?code=SZ300308) (Chinese)
- Market cap CNY 599.4bn (A price on all shares) = USD 90.0bn. EV ≈ CNY 550bn (USD 82.6bn) = market cap - cash 53.5bn - trading financial assets 2.3bn + debt 1.7bn + minority interests 5.0bn (30 Sep 2026 balance sheet; [Eastmoney](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/zcfzbAjaxNew?companyType=4&reportDateType=0&reportType=1&dates=2026-09-30&code=SZ300308)).
- 52-week range CNY 427.34 (6 Nov 2026) to 1,416.88 (22 Jun 2026). YTD -16.6%; 12 months +3.5%; since 30 Dec 2022 +1,783%. Closing high 1,382.33 (22 Jun 2026); drawdown -63.2%. H-share month-end closes: HKD 1,028 (Jul), 1,029 (Aug), 1,062 (Sep), 676 (Oct), 649.5 (12 Nov).

### 2. Valuation multiples
- Trailing P/E 23.1x (TTM net profit CNY 25.9bn = 9M 2026 22.24bn + Q4'25 3.67bn).
- Forward P/E 17.6x 2026E (net profit CNY 34.03bn; n=27) and 8.8x 2027E (68.10bn); 6.1x 2028E (98.62bn) — [Eastmoney profit forecast, 12 Nov 2026](https://emweb.securities.eastmoney.com/PC_HSF10/ProfitForecast/PageAjax?code=SZ300308) (Chinese)
- EV/sales 6.6x (TTM revenue CNY 82.8bn); EV/EBITDA ≈ 18x (estimate: TTM EBITDA ≈ CNY 31bn from net profit, a tax rate of about 13% and D&A of about CNY 1bn; not a reported figure); P/B 6.4x (BVPS CNY 80.11 after the H-share raise).
- FCF: 9M 2026 operating cash flow CNY 8.0bn less capex 9.2bn = about -1.2bn (inventory 23.9bn at 30 Sep). FCF yield about 0%.
- Own history (Yahoo quarter-ends; indicative only because Yahoo's share count is stale): trailing P/E 77.2 (Sep 2025), 79.7 (Dec 2025), 58.6 (Mar 2026), 94.6 (Jun 2026), 44.2 (Sep 2026); forward P/E 29.0 / 17.5 / 22.6 / 50.3 / 20.9.
- Peers (Yahoo; trailing / forward / EV/EBITDA): Coherent 44.4 / 23.6 / 28.7; Lumentum 143 / 27.5 / 117; Fabrinet 26.3 / n/a / 18.7; Eoptolink and TFC (below).

### 3. What the price assumes
- Consensus: net profit +215% in 2026 (10.80bn to 34.03bn) and +100% in 2027; revenue CNY 104.5bn (2026E) and 200.4bn (2027E). The latest broker notes (5-7 Nov 2026): Changjiang 2026E EPS 28.03 / 2027E 55.78; Guolian Minsheng 28.6 / 62.53; Huachuang 28.42 / 54.24; Industrial 29.48 / 51.15. Ratings in the last month: 18 institutions, 14 buy and 4 add (Eastmoney).
- Implied Q4 2026 profit in consensus: CNY 11.8bn vs Q3's 8.59bn (+37% QoQ; computed).
- Reverse reading: 8.8x 2027E means the market is discounting a large shortfall against consensus or a short earnings life. As a rough check, if 2027 profit were half of consensus (CNY 34bn, flat on 2026E), the stock would be on about 17.6x. The price is roughly consistent with profit plateauing at the 2026 level, not with the doubling in consensus.
- Bridge vs successor: consensus as published assumes plug-in modules (the bridge) keep growing through 2028 (CNY 98.6bn profit in 2028E). The multiple behaves as though the market assumes co-packaged optics, or a pluggable price and volume cycle, caps earnings sooner. No source accessed quantifies either.

### 4. Cycle position
- 9M 2026 (notice 30 Oct 2026): revenue CNY 69.55bn (+178%), net profit 22.24bn (+212%), gross margin 46.4%, net margin 34.6% — [Eastmoney indicators](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SZ300308)
- Quarterly (computed from cumulative figures): revenue Q1 19.50bn, Q2 22.28bn, Q3 27.77bn (+24.6% QoQ); net profit Q1 5.73bn, Q2 7.92bn, Q3 8.59bn (+8.5% QoQ). Gross margin is stable at about 46%, but net profit growth slowed relative to revenue in Q3.
- Working capital: inventory CNY 23.9bn, receivables 17.3bn (30 Sep 2026); 9M capex 9.2bn (2.8bn for all of 2025).

### 5. Events
- About 30 Jan 2027: six months after the 30 Jul 2026 H-share listing, when cornerstone lock-ups would typically end (lock-up terms not verified).
- Late Jan 2027: possible 2026 results preview (A-share rules); Q4 and annual results by April 2027 (dates not confirmed).
- Nvidia board investigation and US policy (backdrop); AI-capex sentiment (30 Oct).

### 6. Investor access
- A shares are on ChiNext; Northbound Stock Connect trading in ChiNext shares is limited to institutional professional investors. Innolight is on the Shenzhen Connect eligible list (12 Nov 2026) — [HKEX eligible SZSE list](https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities/SZSE_Securities.csv); [HKEX Investor Book, 6 Jul 2026](https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Getting-Started/Information-Booklet-and-FAQ/Information-Book-for-Investors/Investor_Book_En.pdf)
- Foreign ownership caps on A shares: 10% for a single foreign investor and 30% for all foreign investors combined; Northbound buying is suspended at 28% (HKEX Investor Book, section 3.20). ChiNext daily price limit ±20%.
- The H shares (3308.HK) give unrestricted Hong Kong access (5.3% of shares; at an 8% premium to the A share on 12 Nov). Liquidity: A share about CNY 22.3bn (USD 3.35bn) a day (20-day average).

### 7. Suggested label: attractive on consensus, low confidence (provisional)
- Why: 8.8x 2027E and about 23x trailing, after a 63% drawdown, while Q3 revenue still rose 25% QoQ and peers trade at 24-28x forward. Confidence is low because the market is plainly rejecting consensus and the reason (pricing, customer orders, co-packaged optics timing or AI-capex fears) could not be verified.
- Better entry would be signalled by: Q4 2026 profit near the implied CNY 11.8bn; 2027 1.6T volume or pricing commitments from major customers; stable gross margin near 46%; the H-share lock-up passing without heavy supply; or stabilisation in Eoptolink's sequential trend.

## Tier 1 — Eoptolink (300502.SZ)

### 1. Price and performance
- CNY 205.58 close on 12 Nov 2026. Shares 1,394.7m (after a 4-for-10 capitalisation issue on 11 Jun 2026; 140.0m restricted) — [Eastmoney share structure](https://emweb.securities.eastmoney.com/PC_HSF10/CapitalStockStructure/PageAjax?code=SZ300502). Market cap CNY 286.7bn = USD 43.1bn. EV ≈ CNY 280bn (cash 6.6bn plus 0.3bn trading assets; negligible debt; 30 Sep 2026).
- 52-week range 161.16 (6 Nov 2026) to 618.87 (1 Jul 2026). YTD -33.2%; 12 months -12.5%; since 30 Dec 2022 +2,275% (split-adjusted). Closing high 610.49 (25 Jun 2026); drawdown -66.3%.

### 2. Valuation multiples
- Trailing P/E 19.7x (TTM net profit CNY 14.57bn = 9M 11.37bn + Q4'25 3.20bn). Forward P/E 14.4x 2026E (CNY 19.90bn; n=18), 7.5x 2027E (38.46bn), 5.0x 2028E (56.95bn) — [Eastmoney profit forecast](https://emweb.securities.eastmoney.com/PC_HSF10/ProfitForecast/PageAjax?code=SZ300502). EV/EBITDA 15.4x (Yahoo TTM EBITDA CNY 18.22bn); EV/sales 7.0x (TTM revenue 40.19bn); P/B 10.3x (BVPS 20.05). FCF: 9M operating cash flow 1.46bn less capex 1.81bn = -0.34bn. Dividend yield about 0.5% (Yahoo forward).
- Own history (Yahoo, indicative): trailing P/E 61.4 (Sep 2025), 57.0 (Dec 2025), 58.6 (Mar 2026), 78.9 (Jun 2026), 41.4 (Sep 2026).

### 3. What the price assumes
- Consensus (6-month average) looks stale after Q3: it implies Q4 2026 profit of CNY 8.5bn against Q3's 3.84bn. The latest notes are lower — Changjiang (7 Nov) 2026E EPS 12.96 / 2027E 30.88; Huaxin (6 Nov) 13.82 / 23.86; Industrial (4 Nov) 13.51 / 25.91; Sinolink (1 Nov) 14.39 / 29.56. Even Changjiang's figure implies Q4 profit of about CNY 6.7bn (+75% QoQ; computed).
- At 7.5x 2027E, the price is not assuming the consensus doubling; it looks more consistent with flat-to-lower profit after 2026. Bridge vs successor: consensus rests entirely on plug-in modules (the bridge); nothing in sources accessed shows CPO revenue in estimates.

### 4. Cycle position (the clearest negative signal among Tier 1)
- 9M 2026 (notice 30 Oct 2026): revenue CNY 31.85bn (+93%), net profit 11.37bn (+80%), gross margin 47.7% — [Eastmoney indicators](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SZ300502)
- Computed quarters: revenue Q1 8.34bn, Q2 12.57bn, Q3 10.94bn (-13.0% QoQ; +80.5% YoY); net profit Q1 2.78bn, Q2 4.75bn, Q3 3.84bn (-19.2% QoQ; +60.7% YoY). This is the first sequential decline in the data. Inventory CNY 17.4bn (39% of total assets) at 30 Sep 2026.

### 5. Events: 2026 annual results by April 2027 (date not confirmed); restricted shares (140m) — release dates not verified; no H-share listing on record (Eastmoney shows none as of 12 Nov 2026).
### 6. Access: ChiNext, Shenzhen Connect eligible (institutional professional investors only Northbound); 10%/30% foreign caps; ±20% daily limit; liquidity about CNY 16.7bn (USD 2.5bn) a day.
### 7. Suggested label: cannot assess (provisional)
- Why: the low multiple (7.5-14x forward) sits against a sequential decline and a consensus that has not caught up with it. Until Q4 shows whether Q3 was a timing dip or a turn, the forward numbers are not a reliable base.
- Better entry would be signalled by: Q4 2026 revenue back above the Q2 level (CNY 12.6bn); inventory falling; consensus resetting to a level the company then beats.

## Tier 1 — ASMPT (0522.HK)

### 1. Price and performance
- HKD 101.20 close on 12 Nov 2026. Shares 419.39m. Market cap HKD 42.44bn = USD 5.41bn. EV ≈ HKD 40.5bn (net cash about HKD 1.9bn: cash 5.88bn, debt 3.97bn; Yahoo, 30 Sep 2026).
- 52-week range 68.90 (24 Nov 2025) to 244.40 (30 Jun 2026). YTD +30.2%; 12 months +27.6%; since 30 Dec 2022 +81.9%. Closing high 238.80 (30 Jun 2026); drawdown -57.6%.

### 2. Valuation multiples
- Trailing P/E 26.9x (Yahoo TTM EPS HK$3.76); on Q3 adjusted EPS annualised (HK$1.65 x 4) about 15.3x. Forward P/E about 16x (Yahoo 16.2x at the 11 Nov price). EV/EBITDA 15.3x (TTM EBITDA HK$2.64bn); EV/sales 2.25x (TTM revenue HK$17.98bn); P/B 2.45x (BVPS HK$41.26); dividend yield about 1.9% (Yahoo forward) — [Yahoo statistics](https://finance.yahoo.com/quote/0522.HK/key-statistics/)
- Own history: Yahoo forward P/E 20.3x at 30 Jun 2025 (only one historical point). 5- and 10-year ranges: PENDING (companiesmarketcap).
- Peers (Yahoo; trailing / forward / EV/EBITDA / P/B): BESI 41.5 / 22.9 / 31.7 / 18.0; Kulicke & Soffa 31.9 / 10.9 / 23.7 / 4.0; Hanmi Semiconductor 78.9 / 34.8 / 58.1 / 24.1; Disco 30.8 / 26.1 / 19.6 / 7.8.

### 3. What the price assumes
- Consensus figures were not retrieved (PENDING). The company said its Q4 guide is "above the market consensus".
- Bridge vs successor: TCB (the bridge) is carrying results — record chip-to-substrate orders from OSAT partners of a leading logic customer and repeat chip-to-wafer orders from a leading IDM. HBM-related TCB purchases are tied to HBM4 schedules, with "larger capability-driven investments ... pushed-out". Hybrid bonding (the successor) is at "sampling, evaluation and qualification" with leading logic and memory customers, with no volume orders disclosed. A forward P/E of about 16x, below BESI (the hybrid-bonding peer at 22.9x), suggests the price does not assume hybrid bonding arrives on schedule — [ASMPT Q3 2026 announcement](https://www.asmpt.com/site/assets/files/85973/q3_2026_en_announcement.pdf)

### 4. Cycle position (28 Oct 2026)
- Q3 bookings HK$8.85bn (US$1.13bn), +24.7% QoQ and +137.9% YoY; book-to-bill 1.69, the highest since Q1 2021. Revenue HK$5.25bn (US$669m), +6.3% QoQ and +48.7% YoY. Adjusted gross margin 42.9%; adjusted net profit HK$689.7m (+486% YoY); adjusted EPS HK$1.65 — [ASMPT Q3 2026 press release](https://www.asmpt.com/site/assets/files/85970/asmpt_2026_q3_press_release.pdf)
- SEMI segment: revenue HK$2.93bn (+68% YoY), bookings HK$4.42bn (+156% YoY), adjusted gross margin 46.6%. SMT segment: revenue HK$2.31bn (+30% YoY), record bookings HK$4.43bn including more than US$100m of bulk orders and pull-ins, adjusted gross margin 38.2%.
- Q4 2026 guide: revenue US$670-730m (midpoint +4.6% QoQ, +37.5% YoY). SEMI is expected flat because of longer lead times on advanced-packaging tools; Q4 bookings will be below Q3's record but significantly higher YoY; "AI demand is expected to drive sustained revenue growth in 2027". The NEXX disposal closed on 3 Jun 2026; Bassel Haddad is the new group CEO.

### 5. Events: Q4 2026 and full-year results around late February to early March 2027 (date not confirmed); HBM4 tool decisions at memory customers; hybrid-bonding qualification news.
### 6. Access: HKEX main board 0522 (no ADR). Liquidity is thin compared with the others: about HKD 473m (USD 60m) a day (20-day average). Southbound eligibility: PENDING.
### 7. Suggested label: attractive (provisional; pending own-history range)
- Why: about 16x forward and 2.25x EV/sales after a 58% drawdown, with record bookings and a 1.69 book-to-bill, below BESI, Disco and Hanmi on forward P/E. The risks are that bookings include one-off pull-ins and that HBM TCB demand has been pushed out.
- Better entry would be signalled by: Q4 bookings holding above about HK$6bn (book-to-bill above 1); a firm HBM4 TCB order or a hybrid-bonding volume order; or a price below about HK$90 (about 14x forward).

## Tier 2 — compact snapshots (12 Nov 2026 closes; YTD and 12-month price returns from Yahoo)
| Company | Price | Market cap | Forward P/E | EV/EBITDA | YTD / 12m | Cycle line |
|---|---|---|---|---|---|---|
| Luxshare 002475.SZ (H 2475.HK, listed 9 Jul 2026) | CNY 50.82 (H HKD 50.30, 16% below A) | CNY 393.5bn (USD 59.1bn) | 19.5x 2026E / 13.8x 2027E (Eastmoney, NP 20.19bn / 28.45bn) | 22.2x (Yahoo, 11 Nov; unverified basis) | -10.4% / -12.0% | 9M rev 285.0bn (+29%), NP 13.06bn (+13%); Q3 NP +7% YoY; gross margin 11.9%; 9M operating cash flow negative |
| Envicool 002837.SZ | CNY 40.98 | CNY 52.4bn (USD 7.9bn; 1,279m shares) | 50.9x 2026E on stale consensus; about 68x on Sinolink's 1 Nov EPS of 0.601 | 81.8x (Yahoo, stale) | -50.2% / -20.5% | 9M rev 4.95bn (+23%) but NP 0.37bn (-7.6%); gross margin 26.1% vs 27.3% a year earlier |
| Bizlink 3665.TW | TWD 1,515 | about TWD 296bn (USD 9.0bn; Yahoo-implied shares) | n/a | 18.1x (Yahoo, TTM to Jun) | -0.3% / +1.0% | Oct rev 11.85bn (+80% YoY, +27% MoM); Jan-Oct +44% |
| Auras 3324.TWO | TWD 1,170 | PENDING | n/a (TPEx trailing P/E 26.3x) | n/a | +15.8% / +15.3% | Oct rev 3.37bn (+45% YoY); Jan-Oct +69%; company cites liquid-cooling share gains |
| Accton 2345.TW | TWD 1,525 | about TWD 852bn (USD 25.9bn) | n/a (TWSE trailing 24.7x) | 18.3x (Yahoo, stale) | +28.7% / +55.1% | Oct rev 44.66bn (+91% YoY); Jan-Oct +66% |
| Elite Material 2383.TW | TWD 4,105 | TWD 1.47tn (USD 44.7bn) | n/a (trailing ≈44x on Yahoo TTM EPS 93.29) | ≈32x (Yahoo 35.3x at 4,500) | +149.5% / +205.2% | Oct rev 24.47bn (+203% YoY); 9M EPS 82.92; operating margin 27% |
| Lite-On 2301.TW | TWD 228 | TWD 519bn (USD 15.8bn) | n/a (TWSE trailing 24.4x) | 15.6x (Yahoo, stale) | +39.4% / +36.9% | Oct rev 20.07bn (+32% YoY); 9M EPS 8.08 |
| Kinsus 3189.TW | TWD 667 | TWD 351bn (USD 10.7bn) | n/a (TWSE trailing 79.9x) | 25.9x (Yahoo) | +319.5% / +407.2% | Oct rev 5.37bn (+49% YoY); 9M EPS 8.38; joins MSCI Standard after 30 Nov |
| Nan Ya PCB 8046.TW | TWD 972 | TWD 628bn (USD 19.1bn) | n/a (TWSE trailing 86.5x) | 39.6x (Yahoo, stale) | +303.3% / +241.7% | Oct rev 6.29bn (+70% YoY); 9M EPS 10.63; joins MSCI Standard after 30 Nov |
| Jentech 3653.TW | TWD 5,605 | TWD 825bn (USD 25.1bn) | n/a (TWSE trailing 140.5x at 6,225) | 96x (Yahoo, stale) | +104.2% / +147.5% | Oct rev 3.07bn (+81% YoY); 9M EPS 45.03 |
| JCET 600584.SS | CNY 54.45 | CNY 97.4bn (USD 14.6bn) | 43.5x 2026E / 33.7x 2027E (Eastmoney) | 42.4x (Yahoo; basis unclear) | +48.0% / +44.5% | 9M rev 30.95bn (+8%), NP 1.62bn (+70%); gross margin 16.0% |
| Tongfu 002156.SZ | CNY 48.36 | CNY 77.1bn (USD 11.6bn) | 33.6x 2026E on stale consensus (9M NP 3.06bn already above the 2.29bn 2026E) | 18.0x (Yahoo) | +28.3% / +24.5% | 9M rev 24.89bn (+24%), NP 3.06bn (+256%); placement shares listed 16 Sep 2026 |
| TFC Optical 300394.SZ | CNY 140.34 | CNY 153.1bn (USD 23.0bn) | 44.4x 2026E / 25.9x 2027E (Eastmoney) | 52.1x (Yahoo) | -3.2% / +19.8% | 9M rev 4.75bn (+21%), NP 2.08bn (+42%); Q3 rev +28% QoQ; gross margin 62.6% |
| FIT 6088.HK | HKD 2.80 | about HKD 18.7bn (USD 2.4bn) | ≈9.5x (Yahoo) | 6.2x (Yahoo) | -43.4% / -47.3% | PENDING |

Listing status of the two companies that were private or in the listing process:
- CXMT (ChangXin Memory): listed on the Shanghai STAR Market on 27 Jul 2026 as 长鑫科技 (688825.SS; subscription 16 Jul 2026; issue price CNY 8.66) — [Eastmoney IPO data](https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPTA_APP_IPOAPPLY&columns=SECURITY_CODE,SECURITY_NAME_ABBR,APPLY_DATE,LISTING_DATE,ISSUE_PRICE,TRADE_MARKET,MARKET_TYPE&sortColumns=APPLY_DATE&sortTypes=-1&pageSize=300&pageNumber=1) (Chinese). Close CNY 40.97 on 12 Nov 2026 (Yahoo); closing high 61.80 (17 Aug 2026), -33.7% from it. Not on the Northbound Stock Connect eligible list as of 12 Nov 2026; STAR shares are in any case limited to institutional professional investors Northbound.
- SJ Semiconductor (盛合晶微): listed on the STAR Market on 21 Apr 2026 (688820.SS; issue price CNY 19.68). Close CNY 89.32 on 12 Nov 2026; closing high 229.00 (26 May 2026), -61.0% from it. Not on the Northbound eligible list as of 12 Nov 2026.

## Peer comparison (summary; PENDING final table)

## What could not be verified (running list)
- 5- and 10-year valuation ranges and medians for all Tier 1 names (PENDING companiesmarketcap); previous-cycle peak and trough margins.
- Consensus for Unimicron, AVC and ASMPT (PENDING); Delta's consensus detail beyond StockAnalysis's summary.
- Delta, AVC and Unimicron Q3 call guidance, pricing and capacity commentary.
- Exact dates of Q4 results for all names; lock-up terms for the Innolight and Luxshare H shares; Taiwan foreign-ownership rules; ETF weights other than MSCI Taiwan.
- Company-specific reasons for the 60-66% drawdowns in Innolight and Eoptolink (only market-wide causes are sourced).

## Sources (fetched 12 Nov 2026 unless stated)
- PENDING full list; URLs are inline above.

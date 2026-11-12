# Entry-point evidence: system-level AI hardware companies listed in Taiwan, mainland China and Hong Kong (as of 12 November 2026)

Status: final notes, saved 12 Nov 2026 (~13:50 UTC). Scope is valuation, cycle position, what the price assumes, dated events and investor access only. No ranking, no judgement of technology or business quality. These are exploration notes, not personal financial advice; labels are not buy or sell instructions.

## Method, conventions and data limits
- No search engine was available for this workstream: Firecrawl and Exa were out of credits, and the shared WebSearch budget was spent before any search ran. Everything below comes from direct fetches of known pages: Yahoo Finance chart, statistics and analysis pages; Yahoo Taiwan stock pages; TWSE and TPEx OpenAPI; Eastmoney F10 data endpoints; SEC EDGAR 6-K filings (TSMC, ASE); ASMPT investor-relations PDFs; Focus Taiwan (CNA) articles found by stepping through article IDs; HKEX Stock Connect lists and investor book; StockAnalysis statistics pages; companiesmarketcap P/E-history pages.
- Prices are closes of 12 Nov 2026 for Taiwan, Shenzhen, Shanghai and Hong Kong, and the 11 Nov 2026 close for US ADRs (the US market had not opened at fetch time). FX on 12 Nov 2026 (Yahoo): USD/TWD 32.919, USD/CNY 6.6575, USD/HKD 7.8442. All prices and returns come from the Yahoo Finance chart endpoint, fetched 12 Nov 2026 ([example: 2330.TW](https://query1.finance.yahoo.com/v8/finance/chart/2330.TW?range=5y&interval=1d)).
- Returns are price returns: YTD from the 31 Dec 2025 close, 12 months from the 12 Nov 2025 close, "since Jan 2023" from the 30 Dec 2022 close. Drawdown is from the 52-week closing high.
- "Forward P/E (SA)" is StockAnalysis's forward P/E (12 Nov 2026). Back-solving shows it sits between the two fiscal years and is close to a next-twelve-months basis. For example, ASE: 586 / 19.16 = EPS of 30.6, between 2026E 21.21 and 2027E 33.67. Fiscal-year forward P/Es come from Yahoo (TSMC, ASE; 12 Nov 2026) and Eastmoney (A-shares; average of Chinese brokers over the last six months, as of 12 Nov 2026).
- Trailing P/E uses the last four reported quarters to Sep 2026, computed from reported quarterly EPS. TWSE's official daily P/E (BWIBBU) for 11 Nov still used four quarters to Jun 2026 because Q3 statements were still being filed, so it reads higher. Both are shown.
- Implied-growth readings use a transparent value-driver identity: P/E = (1 - g/ROE) / (r - g), with cost of equity r = 10% (9% as a sensitivity) and the ROE stated for each company. Solving for g gives the perpetual growth the multiple implies beyond the forecast year. This is rough by construction and depends on the inputs shown.
- Non-English sources: Eastmoney (Chinese), the Chinese-language fields of TWSE/TPEx OpenAPI, and Yahoo Taiwan. Data for mainland names is thinner in English: no English-language broker consensus was available for them, and Hong Kong consensus came only from StockAnalysis.

## Answers to the key questions (summary)

### What do current prices imply about growth and margins, against guidance and past peaks?
- Takeaway: the market splits sharply. Taiwanese names (TSMC, Delta, AVC, ASE, Unimicron) trade at 16-25x next-twelve-month earnings (SA), consistent with consensus being met plus 4-7% growth thereafter. China's optical-module makers trade at about 9x NTM and 7.5-9x 2027E, implying flat-to-falling earnings after 2026 against a consensus that doubles profit in 2027. ASMPT sits at about 17x NTM.
- Against their own history: ASE's trailing P/E (33x) is above every year-end in 2016-2025 (maximum 28.4x); Unimicron trades at about 25x forward against 5.6x at the 2022 earnings peak; Delta's forward multiple (22.7x) is the lowest of its last six quarter-ends; Innolight's trailing P/E (about 23x) is below its lowest year-end of 2016-2025 (24.4x in 2022). Sources and calculations are in each company section.

### Where is each company in its cycle?
- Takeaway: Taiwanese revenue was still accelerating or at records in October 2026 — TSMC +59.7% YoY, ASE +47.1%, Unimicron +67.6%, Delta +30.1% (a record month), AVC +34.4% (growth slowing) ([TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L)). ASMPT reported record bookings with a book-to-bill of 1.69. Innolight still grew Q3 revenue 25% QoQ, but Eoptolink's Q3 revenue fell 13% QoQ and its profit 19%, the clearest turn signal in the set. Share prices had already fallen 25-66% from mid-2026 highs for most names (TSMC -9.5%).

### Which dated events in the next three to six months could change the picture?
- Takeaway: MSCI rebalance effective after the close on 30 Nov 2026; Taiwan November revenue around 10 Dec; TSMC ex-dividend on 10 Dec (NT$7) and 11 Mar 2027 (NT$9); Q4 results from mid-January 2027 (TSMC) to late February or March (ASMPT, A-shares); Innolight's H shares reach six months after listing around 30 Jan 2027; the Nvidia board investigation and US congressional scrutiny; and US AI data-center policy under the new Congress from January 2027. Exact results dates were not confirmed.

### How can a foreign investor reach each company, and what are the frictions?
- Takeaway: Taiwan names trade directly on TWSE or TPEx; ADRs exist only for TSMC (1:5, 13.7% premium on 11 Nov) and ASE (1:2, near parity). TWSE data show ASE's foreign-ownership upper limit at 100%, with foreigners holding 75.5%. The A-shares are all on the Northbound Stock Connect list, but Innolight, Eoptolink and TFC are ChiNext stocks, which Northbound only institutional professional investors may trade. Single foreign holders are capped at 10% and all foreign holders at 30% (buying halts at 28%). Innolight (3308.HK) and Luxshare (2475.HK) now also have Hong Kong H shares. CXMT and SJ Semiconductor are STAR-listed and not yet Connect-eligible. ASMPT trades only in Hong Kong, at about USD 60m a day. Details are in each section.

## Market backdrop: dated sell-offs and events, Oct-Nov 2026
- 15 Oct 2026: Taiex -3.41% to 46,969.87 on Fed-hike fears after US September CPI of 3.7% (3.6% expected); ASE fell 10% (limit down) to NT$673 — [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150013)
- 21 Oct 2026: Taiex +1.28% after Supermicro raised its sales outlook — [Focus Taiwan, 21 Oct 2026](https://focustaiwan.tw/business/202610210012)
- 30 Oct 2026: Taiex -2.49% to 45,211.83 on concerns that "massive AI investments would not deliver comparable returns" after Alphabet's disappointing sales and Amazon's soaring AI spending — [Focus Taiwan, 30 Oct 2026](https://focustaiwan.tw/business/202610300015). Overnight in the US, Nasdaq fell 2.86%, the SOX 7.20% and the TSM ADR 5.95% — [Focus Taiwan, 31 Oct 2026](https://focustaiwan.tw/business/202610310008)
- 3 Nov 2026: Taiex -3.59% to 43,307.54 (seventh-steepest point fall) on AI-spending fears and high yields — [Focus Taiwan, 3 Nov 2026](https://focustaiwan.tw/business/202611030023)
- 5-6 Nov 2026 (US midterms): Democrats won both chambers of Congress and governorships including Texas. Dealers cited fears of restrictions on AI data-center development. The SOX fell 12.2% on 5 Nov and the TSM ADR 10.8% (Yahoo). On 6 Nov the Taiex opened down a record 3,737.67 points; TSMC (NT$2,020), Delta (NT$1,020) and ASE (NT$515) hit limit-down; the index closed -4.51% at 39,701.64 — [Focus Taiwan, 6 Nov 2026 (open)](https://focustaiwan.tw/business/202611060006); [Focus Taiwan, 6 Nov 2026 (close)](https://focustaiwan.tw/business/202611060016)
- 6 Nov 2026: the National Financial Stabilization Fund (NT$500bn) authorised its 10th market intervention since 2000 — [Focus Taiwan, 6 Nov 2026](https://focustaiwan.tw/business/202611060020). On 9 Nov the Taiex rose 4.94% to 41,661.70, its second-largest point gain — [Focus Taiwan, 9 Nov 2026](https://focustaiwan.tw/business/202611090017)
- 9-12 Nov 2026 (Nvidia CEO controversy): Jensen Huang admitted an extramarital affair; media alleged the woman was a Chinese spy; Nvidia's board opened an investigation; three Republican lawmakers reportedly sought a closed-door meeting on whether high-end chips and servers reached China through third countries — [Focus Taiwan, 9 Nov 2026](https://focustaiwan.tw/business/202611090013). On 12 Nov, Nvidia was down about 8% after hours on reports that the board was discussing whether to remove Huang. The Taiex fell 2.63% to 43,091.87, with TSMC -2.30% (NT$2,340) and ASE -5.02% (NT$586) — [Focus Taiwan, 12 Nov 2026](https://focustaiwan.tw/business/202611120015)
- Demand data: Taiwan's October 2026 exports hit a record US$96.76bn (+58.9% YoY; 36th straight month of growth) — [Focus Taiwan, 9 Nov 2026](https://focustaiwan.tw/business/202611090020)
- MSCI November 2026 review (announced 11-12 Nov; effective after the close on 30 Nov 2026): Taiwan's weight in MSCI EM rises from 28.86% to 29.01%; Kinsus, Nan Ya PCB and Taiwan Union Technology join the MSCI Global Standard indexes (deferred from August because TWSE had listed them as "disposition stocks" with trading restrictions); TSMC's weight in MSCI Taiwan is cut 0.25 pp to 54.29% — [Focus Taiwan, 12 Nov 2026](https://focustaiwan.tw/business/202611120014)
- Index levels, 12 Nov 2026 (Yahoo): Taiex 43,091.87 (YTD +48.8%; -13.5% from the 6 Oct 2026 closing high of 49,822.55); SOX 10,564.11 on 11 Nov (YTD +49.1%; -27.8% from the 22 Jun 2026 high); Hang Seng 24,008.55 (YTD -6.3%).

---

## Tier 1 — TSMC (2330.TW; ADR TSM)

### 1. Price and performance
- TWD 2,340 close on 12 Nov 2026 (Yahoo; confirmed by [Focus Taiwan](https://focustaiwan.tw/business/202611120015)). ADR TSM: USD 413.35 close on 11 Nov 2026. 1 ADR = 5 shares (the Q3 release gives EPS of NT$29.43 = US$4.60 per ADR). The ADR traded 13.7% above local parity on 11 Nov (local NT$2,395 at 32.954; computed).
- Market cap TWD 60.68tn (25.93bn shares) = USD 1.843tn. EV TWD 57.48tn (net cash TWD 3.20tn) — [StockAnalysis, 12 Nov 2026](https://stockanalysis.com/quote/tpe/2330/statistics/)
- 52-week range TWD 1,375 (24 Nov 2025) to 2,590 (6 Oct 2026, intraday). YTD +51.0%; 12 months +58.6%; since 30 Dec 2022 +421.7% (from NT$448.5). Closing high NT$2,585 (6 Oct 2026); drawdown -9.5%. The 6 Nov 2026 close was NT$2,135 (intraday limit-down NT$2,020).

### 2. Valuation multiples (12 Nov 2026)
| Measure | TSMC now | Own history | Notes and sources |
|---|---|---|---|
| Trailing P/E | 23.8x (TTM EPS 98.27 = 19.51 + 22.08 + 27.25 + 29.43); SA 24.0x; TWSE official 27.76x (TTM to Q2, 11 Nov) | Local basis: 23.8x at end-2024 (1,075 / 45.26), 23.4x at end-2025 (1,550 / 66.26). ADR basis (companiesmarketcap) year-ends 2016-25: 11.6, 14.8, 14.2, 23.5, 28.3, 27.2, 11.2, 19.3, 28.8, 28.3 — 10-yr range 11.2-28.8x, median 21.4x; 5-yr (2021-25) median 27.2x | [Yahoo TW EPS](https://tw.stock.yahoo.com/quote/2330.TW/eps); [companiesmarketcap](https://companiesmarketcap.com/tsmc/pe-ratio/) (ADR series includes the ADR premium) |
| Forward P/E | 21.2x 2026E (EPS 110.63; 35 analysts); 15.6x 2027E (149.53; 36 analysts; range 126.5-167.1); SA 16.4x | Yahoo quarter-end forward P/E: 18.8 (Sep 25), 18.2 (Dec 25), 20.1 (Mar 26), 24.4 (Jun 26), 18.5 (Sep 26) | [Yahoo analysis](https://finance.yahoo.com/quote/2330.TW/analysis/), [Yahoo statistics](https://finance.yahoo.com/quote/2330.TW/key-statistics/), 12 Nov 2026 |
| EV/EBITDA | 15.9x (TTM EBITDA TWD 3.61tn) | 13.6 / 15.4 / 16.5 / 20.9 / 19.0 at the same quarter-ends | SA; Yahoo |
| EV/sales | 11.6x (TTM revenue 4.94tn) | 9.5 / 10.6 / 11.4 / 14.7 / 13.9 | SA; Yahoo |
| P/B | 8.6x (BVPS 271.60) | 7.4 / 8.0 / 8.4 / 10.6 / 10.0 | SA; Yahoo |
| FCF yield | 2.44% (TTM FCF TWD 1.48tn) | n/a | SA |
| Dividend yield | 1.24% on the last four declared quarterly dividends (NT$6+7+7+9); 1.54% on the new NT$9 run-rate; SA 1.20% | 5-yr average 1.81% (Yahoo TW) | [TSMC 6-K, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm); [Yahoo TW dividends](https://tw.stock.yahoo.com/quote/2330.TW/dividend) |
- ADR multiples: 23.6x 2026E (USD 17.50) and 17.7x 2027E (USD 23.39), including the premium — [Yahoo analysis TSM](https://finance.yahoo.com/quote/TSM/analysis/)
- Peers (Yahoo statistics, 11-12 Nov 2026; trailing P/E / forward P/E / EV/EBITDA / P/B): UMC (2303.TW) 15.0 / 15.8 / 7.7 / 2.7; SMIC (0981.HK) 46.5 / 27.1 / 15.4 / 2.1; Intel n/m / 37.0 / 180 (depressed EBITDA) / 2.7; Samsung Electronics 9.2 / n/m (Yahoo's 2.4x looks erroneous) / 5.0 / 2.5 — [Yahoo statistics pages](https://finance.yahoo.com/quote/2303.TW/key-statistics/)

### 3. What the price assumes
- Consensus (Yahoo, 12 Nov 2026): EPS +67% in 2026 (66.25 to 110.63) and +35% in 2027 (to 149.53). The 2027E has risen 7.3% in 90 days (from 139.36); 27 up and 2 down revisions in 30 days. SA summary: 35 analysts, average target NT$3,389.80, "3-year" revenue and EPS growth forecasts of 36.7% and 42.4% (basis not stated).
- Company guidance: 2026 USD revenue growth of about 44% (raised from "slightly more than 40%" in July). Q4 2026: revenue US$52.3-54.3bn (midpoint +58% YoY, +14% QoQ), gross margin 65-67%, operating margin 56.5-58.5%, at NT$31.8 per US$. Capex 2026 US$60-64bn, unchanged; 2026-28 capex to exceed the previous three years — [TSMC Q3 release (6-K exhibit 99.1)](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm); [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150018)
- Implied growth (computed): 15.6x 2027E with ROE of 35% (Yahoo TTM ROE 41.85%, haircut) implies perpetual growth of about 4.4% after 2027 at r = 10% (3.2% at r = 9%). The price requires 2027 to be delivered but little acceleration after it.
- Bridge vs successor: management called CoWoS (the bridge) customers' "top choice" and will "ensure sufficient CoWoS capacity" (15 Oct call, Focus Taiwan). Guidance and consensus rest on N2/N3 ramps and CoWoS. Nothing here suggests the 2026-27 numbers or the multiple need panel-level packaging (2028-29) or A16 on schedule. No source quantified successor revenue in consensus (gap).

### 4. Cycle position
- Q3 2026 (15 Oct): revenue NT$1,494.24bn (+50.9% YoY, +17.6% QoQ), US$46.72bn (+41.2% YoY); gross margin 66.4%, operating margin 58.7%, net margin 51.1%; EPS NT$29.43 (+68.7% YoY). Wafer revenue: 2nm 8% (3% in Q2), 3nm 33%, 5nm 28%, 7nm 10%; 7nm and below 79% — [TSMC Q3 release](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm)
- Monthly revenue (TWD bn; YoY): Jun 442.68 (+67.9%); Jul 467.58 (+44.7%); Aug 514.81 (+53.3%); Sep 511.86 (+54.7%); Oct 586.89 (+59.7%, +14.7% MoM, a record); Jan-Oct 4,485.6 (+43.3%) — [TWSE OpenAPI t187ap05_L](https://openapi.twse.com.tw/v1/opendata/t187ap05_L); [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/2330.TW/revenue). October equals about 35% of the Q4 guidance midpoint at NT$31.8 (computed), so the quarter is tracking at or above guidance — [Focus Taiwan, 10 Nov 2026](https://focustaiwan.tw/business/202611100014)
- Capacity and capex: board approved capital appropriations of about US$40.93bn on 10 Nov 2026 (advanced and specialty capacity, advanced packaging, fab construction, 2027 R&D capex) — [TSMC 6-K, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm)
- Margins against history: Q3 gross margin of 66.4% and the 65-67% Q4 guide are the reference points. Previous-cycle peak and trough margins were not retrieved, and no remembered figures are used (gap).

### 5. Near-term events
- 30 Nov 2026 (after the close): MSCI rebalance cuts TSMC's MSCI Taiwan weight to 54.29% (Focus Taiwan, 12 Nov).
- About 10 Dec 2026: November revenue (October's was published by 10-11 Nov). 10 Dec 2026: ex-dividend NT$7.0 (Q2 2026).
- Mid-January 2027: Q4 2026 results and 2027 guidance (date not confirmed in sources accessed). 11 Mar 2027: ex-dividend NT$9.0 (Q3 2026), payment 8 Apr 2027.
- 12 Nov 2026: NT$14.8bn green bonds listed — [Focus Taiwan, 4 Nov 2026](https://focustaiwan.tw/business/202611040008)
- Board, 10 Nov 2026: up to US$500m for Anthropic shares at the IPO price, up to US$500m for OpenAI preferred stock, and up to US$500m to set up a strategic investment company (TSMC 6-K).
- Policy: the Nvidia board investigation and congressional scrutiny of chip shipments to China; the new Congress from January 2027 and possible AI data-center restrictions. TSMC is evaluating Texas production and cooperation with "Terafab" — [Focus Taiwan, 15 Oct 2026](https://focustaiwan.tw/business/202610150023)

### 6. Investor access
- TWSE 2330; NYSE ADR TSM (1:5). The 13.7% ADR premium is the cost of the ADR route. Liquidity (20-day average traded value, from Yahoo volumes): 2330.TW about TWD 76bn (USD 2.3bn) a day; TSM about USD 6.2bn a day.
- MSCI Taiwan weight 54.29% after the November review, the main driver of passive weights in Taiwan country funds. Weights in specific ETFs were not retrieved (iShares holdings files did not download).
- The foreign-ownership limit for TSMC was not retrieved per stock. TWSE's semiconductor category shows 41.67% of all sector shares held by foreign and mainland investors — [TWSE OpenAPI MI_QFIIS_cat](https://openapi.twse.com.tw/v1/fund/MI_QFIIS_cat)

### 7. Suggested label: fair (12 Nov 2026)
- Why: 15.6x 2027E and about 16x NTM are below TSMC's forward range at the last five quarter-ends (18-24x) and below its FY2021-25 year-end forward median (19.3x). Trailing P/E (23.8x local) equals the last two year-ends and the five-year median. EV/EBITDA (15.9x), EV/sales and P/B sit above their five-year ranges, partly offset by ROE of 41.9% (also above range). The cycle is still accelerating, with October +59.7% YoY, the Q4 guide +58% YoY and upward revisions. Against that, the stock is only 9.5% off its high while AI-hardware peers are 25-66% down, and policy and AI-capex sentiment risks are live.
- Entry would look better on: (a) a price near NT$2,100 or lower (about 14x 2027E; the 6 Nov close was 2,135); (b) January 2027 guidance holding 2027 near consensus (+35% EPS) with gross margin at or above 63%; (c) an ADR premium below 10% for ADR buyers; (d) clearer US data-center policy after the new Congress sits.

---

## Tier 1 — ASE Technology Holding (3711.TW; ADR ASX)

### 1. Price and performance
- TWD 586 close on 12 Nov 2026 (-5.02% on the day; [Focus Taiwan](https://focustaiwan.tw/business/202611120015)). ADR ASX USD 37.82 (11 Nov); 1 ADS = 2 shares (EPS NT$6.13 = US$0.384 per ADS in the Q3 release); 1.0% above parity on 11 Nov (computed).
- Shares: 4,488.1m issued (TWSE) or 4.42bn excluding treasury shares (SA and Yahoo). Market cap TWD 2.59-2.63tn = USD 78.7-79.9bn. Net debt TWD 288-306bn: debt 394.4bn (short-term 70.4bn, bonds 42.2bn, long-term 276.6bn, current portion 5.1bn) less cash 88.4bn at 30 Sep 2026; net debt/equity 0.66 (0.47 at 30 Jun) — [ASE Q3 2026 6-K](https://www.sec.gov/Archives/edgar/data/1122411/000095010326016324/dp255760_6k.htm). EV TWD 2.91tn (SA).
- 52-week range TWD 206 (19 Nov 2025) to 765 (12 Oct 2026). YTD +133.9%; 12 months +158.1%; since 30 Dec 2022 +524.1%. Closing high 762 (12 Oct 2026); drawdown -23.1%.

### 2. Valuation multiples
| Measure | ASE now | Own history | Sources |
|---|---|---|---|
| Trailing P/E | 33.4x basic (TTM 17.56 = 3.39 + 3.24 + 4.80 + 6.13); 34.9x diluted; SA 35.4x; TWSE 35.42x (11 Nov) | Year-ends 2016-25 (companiesmarketcap): 9.2, 11.7, 9.1, 28.4, 11.6, 6.9, 5.7, 18.6, 20.8, 26.6 — 10-yr range 5.7-28.4x, median 11.7x; 5-yr median 18.6x. Today's multiple is above the 10-year year-end maximum. Computed quarter-ends: 20.1x (Sep 25), 26.7x (Dec 25), 30.2x (Mar 26), 48.8x (Jun 26), 40.0x (Sep 26) | [companiesmarketcap](https://companiesmarketcap.com/ase-group/pe-ratio/) (pre-2018 figures are ASE Inc.) |
| Forward P/E | 27.6x 2026E (21.21; 14 analysts); 17.4x 2027E (33.67; 18 analysts; range 28.44-42.43); SA 19.2x | n/a | [Yahoo analysis](https://finance.yahoo.com/quote/3711.TW/analysis/) |
| EV/EBITDA | 17.0x (SA; TTM EBITDA 165.1bn) | Yahoo: 8.0 / 11.5 / 13.0 / 25.5 / 21.2 (Sep 25 to Sep 26) | [SA](https://stockanalysis.com/quote/tpe/3711/statistics/) |
| EV/sales | 3.7x (TTM revenue 786.8bn) | Yahoo: 1.4 / 2.1 / 2.5 / 4.9 / 4.7 | SA; Yahoo |
| P/B | 6.1x (BVPS 95.76; SA 5.7x) | Yahoo: 2.4 / 3.5 / 4.1 / 8.7 / 7.9 | MOPS via TWSE OpenAPI |
| FCF yield | -3.4% (TTM FCF -87.2bn) | n/a | SA |
| Dividend yield | 1.12% (FY2025 NT$6.5848; ex-dividend 3 Jul 2026) | 2023-25 cash yields at ex-date 7.2%, 3.1%, 3.6% (Yahoo TW) | [Yahoo TW dividends](https://tw.stock.yahoo.com/quote/3711.TW/dividend) |
- Peers (trailing / forward / EV/EBITDA / P/B): Amkor 13.9 / 13.3 / 6.9 / 1.8 (Yahoo); Powertech (6239.TW) 20.0 / n/a / 7.6 / 2.9 (Yahoo); JCET 43.9 / 28.7 (SA) / 15.1 / 3.2; Tongfu 21.6 / 40.1 (SA; inconsistent consensus) / 14.8 / 3.3.

### 3. What the price assumes
- Consensus (Yahoo): EPS +139% in 2026 (8.89 to 21.21) and +59% in 2027 (to 33.67). The 2027E rose from 28.72 to 33.67 in 30 days after Q3. SA: 18 analysts, average target NT$852.78.
- Company guidance (29-30 Oct 2026): LEAP (leading-edge advanced packaging and test) revenue for 2026 raised to US$4.0bn from US$3.7bn and expected to double in 2027; 2026 capex raised to US$11.5bn from US$10.5bn, with 60% of new equipment for LEAP; Q4 consolidated revenue +6-8% QoQ; Q4 gross margin 23-24%, rising further in 2027 — [Focus Taiwan, 30 Oct 2026](https://focustaiwan.tw/business/202610300006). Q4 ATM revenue +11-13% QoQ, ATM gross margin +100-200 bp, EMS flat at about 2% operating margin, at NT$31.9 — [ASE 6-K with presentation](https://www.sec.gov/Archives/edgar/data/1122411/000095010326016323/dp255782_6k.htm)
- Implied growth (computed): 17.4x 2027E with 2027 ROE of about 25% implies perpetual growth of about 5.5% after 2027 at r = 10%. 2027 consensus (+59%) matches the guided LEAP doubling, so the price assumes guidance is met and also holds a premium to Amkor (17.4x vs 13.3x forward; EV/EBITDA 17x vs 6.9x) while FCF is negative.
- Bridge vs successor: consensus rests on today's bridge (CoWoS-type outsourcing and advanced test alongside TSMC). No evidence was found that fan-out panel or optical-engine packaging revenue is in 2026-27 numbers (gap).

### 4. Cycle position
- Q3 2026: revenue NT$244.16bn (+44.8% YoY, +27.8% QoQ, against a 21-22% guide); gross margin 22.1% (a record); operating margin 13.6%; net income NT$27.0bn; EPS 6.13 basic / 5.84 diluted. ATM revenue NT$151.5bn (+51.0% YoY), gross margin 30.6% (27.3% in Q2), operating margin 20.0%. EMS NT$93.5bn (+35.4% YoY) at 8.3% gross margin. Equipment capex US$2.10bn in the quarter; operating cash flow NT$50.5bn against PP&E payments of NT$125.9bn — [ASE 6-K](https://www.sec.gov/Archives/edgar/data/1122411/000095010326016324/dp255760_6k.htm)
- Monthly revenue (TWD bn; YoY): Jun 65.78 (+32.9%); Jul 73.78 (+43.2%); Aug 82.25 (+45.7%); Sep 88.13 (+45.5%); Oct 88.62 (+47.1%, +0.6% MoM); Jan-Oct +32.2% — [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L); [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/3711.TW/revenue)
- Margins: ASE called the Q3 gross margin a new high. Earlier-cycle peaks were not retrieved.

### 5. Near-term events: November revenue around 10 Dec 2026; Q4 results and the 2027 capex/LEAP outlook in late January or February 2027 (date not confirmed); MSCI rebalance on 30 Nov; AI-capex and policy sentiment (ASE fell 10% on 15 Oct and 5% on 12 Nov).

### 6. Investor access: TWSE 3711; NYSE ADR ASX (1:2; near parity). TWSE foreign-investment upper limit is 100%; foreigners held 75.52% (3,389.4m of 4,488.1m shares) — [TWSE OpenAPI MI_QFIIS_sort_20](https://openapi.twse.com.tw/v1/fund/MI_QFIIS_sort_20). Liquidity: 3711.TW about TWD 14.1bn (USD 0.43bn) a day; ASX about USD 0.42bn a day.

### 7. Suggested label: stretched (borderline fair)
- Why: trailing P/E is above every year-end of the past decade. Forward multiples carry a large premium to Amkor while FCF is negative and net debt is rising. The price assumes the 2027 LEAP doubling is delivered. The growth is guided, which is why this is borderline.
- Entry would look better on: a price near NT$500 (about 15x 2027E; the 6 Nov intraday low was 515); LEAP 2027 order evidence on the Q4 call; capex intensity peaking with FCF turning positive; or an ATM gross margin above 31% sustained into Q1 2027.

---

## Tier 1 — Unimicron (3037.TW)

### 1. Price and performance
- TWD 792 close on 12 Nov 2026. Market cap TWD 1.30tn (1.64bn shares) = USD 39.5bn; EV TWD 1.20tn (net cash TWD 109.7bn) — [SA, 12 Nov 2026](https://stockanalysis.com/quote/tpe/3037/statistics/)
- 52-week range 157.5 (24 Nov 2025) to 1,420 (5 Oct 2026). YTD +260.0%; 12 months +376.5%; since 30 Dec 2022 +560.0%. Closing high 1,325 (5 Oct 2026); drawdown -40.2%.

### 2. Valuation multiples
| Measure | Unimicron now | Own history | Sources |
|---|---|---|---|
| Trailing P/E | 39.3x (TTM 20.17 = 9M 2026 basic 17.85 + Q4'25 2.32); SA 39.6x; TWSE 44.72x (11 Nov) | Year-ends 2017-25: 49.0, 17.4, 16.5, 21.0, 23.5, 5.6 (2022, the last earnings peak), 21.9, 41.8, 50.1 (2016 above 1,000x) — 10-yr median about 21.9x; 5-yr median 23.5x | [TWSE OpenAPI t187ap06_L_ci](https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci); [companiesmarketcap](https://companiesmarketcap.com/unimicron/pe-ratio/) |
| Forward P/E | 24.6x (SA; implied forward EPS about 32.2) | n/a | SA |
| EV/EBITDA | 31.7x (TTM EBITDA 41.7bn) | Yahoo: 11.4 (Sep 25), 15.2 (Dec 25), 25.8 (Mar 26), 51.2 (Jun 26), 38.9 (Sep 26) | SA; Yahoo |
| EV/sales | 8.0x (TTM revenue 167.7bn) | Yahoo: 2.0 / 2.8 / 5.4 / 12.1 / 12.7 | SA; Yahoo |
| P/B | 7.3x (BVPS 108.24); SA 7.9x | Yahoo: 2.6 (Sep 25), 3.7 (Dec 25) | TWSE OpenAPI |
| FCF yield | 0.26% (TTM FCF 3.76bn) | | SA |
| Dividend yield | 0.25% (NT$1.98) | | Yahoo TW |
- Earnings-quality caveat: 9M 2026 pre-tax profit of NT$35.04bn includes NT$15.10bn of non-operating income against NT$19.94bn of operating income (TWSE OpenAPI). Trailing EPS is flattered; the source of the gain was not verified.
- Peers (trailing / forward / EV/EBITDA / P/B): Ibiden (4062.T) 47.4 / n/a / 17.7 / 6.0; Samsung Electro-Mechanics 66.1 / 19.1 / 29.8 / 6.5; AT&S 82.3 / n/a / 12.7 / 5.7 (all Yahoo); Kinsus 67.7 / 23.7 / 24.2 and Nan Ya PCB 77.8 / 23.5 / 37.0 (SA).

### 3. What the price assumes
- SA consensus: 19 analysts ("Strong Buy"), average target NT$1,427.37, "3-year" revenue growth 44.1% and EPS growth 152.5% (basis not stated). The forward EPS of about 32 implies roughly +60% on TTM, before stripping out non-operating gains.
- Implied growth (computed): 24.6x forward with forward ROE of about 30% (32.2 / 108.2) implies perpetual growth of about 6.9% at r = 10%, the highest among the Taiwanese Tier 1.
- History check: at the last substrate earnings peak (end-2022) the market paid 5.6x trailing. Today it pays 39x trailing and about 25x forward, so it is pricing a longer or structurally different upcycle than 2021-22.
- Bridge vs successor: the multiple implies that organic ABF tightness (the bridge) persists through 2027-28, before glass-core substrates (targeted 2027-28) could change the mix. No source shows glass core in estimates.

### 4. Cycle position
- Monthly revenue (TWD bn; YoY): Jun 14.90 (+36.3%); Jul 16.25 (+43.7%); Aug 17.75 (+56.3%); Sep 18.65 (+64.7%); Oct 18.99 (+67.6%, +1.8% MoM); Jan-Oct +40.9%. Q3 revenue 52.65bn (+54.9% YoY, +22.8% QoQ; computed) — [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/3037.TW/revenue); [TWSE OpenAPI](https://openapi.twse.com.tw/v1/opendata/t187ap05_L)
- Quarterly EPS: Q3'26 6.36; Q2'26 8.45 (non-operating gains); Q1'26 3.28; Q4'25 2.32; Q3'25 1.44 — [Yahoo TW EPS](https://tw.stock.yahoo.com/quote/3037.TW/eps). 9M 2026 gross margin 24.5%, operating margin 15.0% (TTM 22.7% and 13.3%, SA).
- Guidance, ABF pricing and capacity commentary from the Q3 call: not found (gap).

### 5-6. Events and access: November revenue around 10 Dec 2026; Q4 results around February 2027 (date not confirmed); MSCI rebalance on 30 Nov adds peers Kinsus and Nan Ya PCB to MSCI Standard. TWSE 3037 only (no ADR); liquidity about TWD 21.5bn (USD 0.65bn) a day.

### 7. Suggested label: stretched
- Why: about 25x forward and 31.7x EV/EBITDA (against Ibiden at 17.7x), P/B up from 2.6x to about 7.3-7.9x in a year, trailing earnings inflated by non-operating income, and a price up 260% YTD despite a 40% drawdown. Revenue momentum is strong (October +67.6% YoY), so the label reflects price, not the cycle.
- Entry would look better on: forward P/E near 18x (about NT$580) or EV/EBITDA below 20x; evidence on the Q4 call of ABF price increases or sold-out 2027 capacity; operating income alone supporting the EPS run-rate.

---

## Tier 1 — Delta Electronics (2308.TW)

### 1. Price and performance
- TWD 1,240 close on 12 Nov 2026. Market cap TWD 3.22tn (2.60bn shares) = USD 97.8bn; EV TWD 3.19tn (net cash 98.1bn = cash 213.2bn - debt 115.1bn) — [SA, 12 Nov 2026](https://stockanalysis.com/quote/tpe/2308/statistics/)
- 52-week range 886 (18 Dec 2025) to 2,585 (27 May 2026). YTD +28.8%; 12 months +28.2%; since 30 Dec 2022 +332.8%. Closing high 2,520 (27 May 2026); drawdown -50.8%. 6 Nov 2026: intraday limit-down NT$1,020, close 1,055.

### 2. Valuation multiples
| Measure | Delta now | Own history | Sources |
|---|---|---|---|
| Trailing P/E | 37.2x (TTM 33.30 = 6.67 + 7.91 + 9.68 + 9.04); SA 37.3x; TWSE 38.89x | Year-ends 2016-25: 17.2, 16.4, 15.3, 14.9, 23.8, 24.4, 21.3, 23.5, 31.5, 41.5 — 10-yr range 14.9-41.5x, median 22.4x; 5-yr median 24.4x. Yahoo quarter-ends: 50.9 (Sep 25), 50.2 (Dec 25), 59.8 (Mar 26), 72.1 (Jun 26), 60.3 (Sep 26) | [companiesmarketcap](https://companiesmarketcap.com/delta-electronics/pe-ratio/); [Yahoo](https://finance.yahoo.com/quote/2308.TW/key-statistics/) |
| Forward P/E | 22.7x (SA; implied forward EPS 54.6) | Yahoo quarter-end forward: 36.2 / 30.3 / 40.8 / 51.1 / 30.6 | SA; Yahoo |
| EV/EBITDA | 21.2x (TTM EBITDA 149.7bn) | Yahoo: 25.2 / 25.4 / 31.2 / 38.5 / 32.9 | SA; Yahoo |
| EV/sales | 4.55x | Yahoo: 4.7 / 4.9 / 6.4 / 8.4 / 7.4 | SA |
| P/B | 8.4x (SA); 10.1x on parent BVPS 122.50 | Yahoo: 10.5 / 10.4 / 13.4 / 16.9 / 16.7 | SA |
| FCF yield | 2.06% (TTM FCF 66.5bn) | | SA |
| Dividend yield | 0.94% (NT$11.60, ex-dividend 17 Jun 2026) | | Yahoo TW |
- Peers (Yahoo; trailing / forward / EV/EBITDA / P/B): Vertiv 36.3 / 19.9 / 25.8 / 13.6; Eaton 35.4 / 22.1 / 23.3 / 6.6; Schneider Electric 28.3 / 20.0 / 17.7 / 5.4; Lite-On 23.5 / 16.5 / 17.1 (SA).

### 3. What the price assumes
- SA consensus: 22 analysts ("Strong Buy"), average target NT$2,261.32, "3-year" revenue growth 39.1% and EPS growth 57.4% (basis not stated).
- Implied growth (computed): 22.7x forward with ROE of about 29% (9M net income annualised on parent equity) implies perpetual growth of about 6.6% at r = 10%. That is a forward multiple in line with Eaton and Schneider and above Vertiv, after Delta's own forward multiple fell from 30-51x.
- Bridge vs successor: no source here quantifies 800V DC revenue in consensus (gap). The 54V-to-800V move is a transition inside Delta's own product line. The de-rating since May means the market is not paying ahead for the successor.

### 4. Cycle position
- Monthly revenue (TWD bn; YoY): Jun 65.60 (+55.4%); Jul 67.07 (+47.8%); Aug 64.59 (+35.0%); Sep 65.40 (+14.6%); Oct 74.67 (+30.1%, +14.2% MoM, the highest month in the series); Jan-Oct +36.3% — [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/2308.TW/revenue)
- Q3 2026 revenue 197.06bn (+31.1% YoY, +7.5% QoQ; computed); EPS 9.04 (+26.3% YoY but -6.6% QoQ). 9M gross margin 35.5%, operating margin 17.0% (TWSE OpenAPI). The Q3 EPS dip despite higher revenue is not explained in sources accessed (gap).
- Guidance, orders and capacity commentary from the Q3 call: not found (gap).

### 5-6. Events and access: November revenue around 10 Dec 2026; Q4 results and the 2027 outlook in early 2027 (date not confirmed). TWSE 2308 only; liquidity about TWD 19.8bn (USD 0.60bn) a day.

### 7. Suggested label: fair
- Why: 22.7x forward is near large Western power peers and the lowest of Delta's own recent quarter-ends, after a 51% drawdown; trailing 37x is above the 10-year median (22.4x) but below end-2025 (41.5x). October was a record month, though YoY growth slowed in Q3 and EPS dipped.
- Entry would look better on: forward P/E at or below 19-20x (about NT$1,040-1,090; the 6 Nov close was 1,055); a Q4 margin recovery from the Q3 EPS dip; evidence of 800V DC or liquid-cooling orders on the Q4 call.

---

## Tier 1 — Asia Vital Components (3017.TW)

### 1. Price and performance
- TWD 2,775 close on 12 Nov 2026. Market cap TWD 1.09tn on SA's 392.67m shares (1.13tn on MOPS share capital of 406.8m) = USD 33-34bn; EV TWD 1.06tn (net cash 40.6bn) — [SA, 12 Nov 2026](https://stockanalysis.com/quote/tpe/3017/statistics/)
- 52-week range 1,205 (21 Nov 2025) to 3,700 (6 Oct 2026). YTD +83.8%; 12 months +84.4%; since 30 Dec 2022 +2,406%. Closing high 3,685 (6 Oct 2026); drawdown -24.7%. 6 Nov 2026 close 2,310.

### 2. Valuation multiples
| Measure | AVC now | Own history | Sources |
|---|---|---|---|
| Trailing P/E | 30.5x (TTM 90.87 = 17.01 + 20.17 + 24.37 + 29.32); SA 31.0x; TWSE 33.61x | Computed year-ends: 29.3x end-2024 (623 / 21.25), 30.7x end-2025 (1,510 / 49.26). Longer history not retrieved | [Yahoo TW EPS](https://tw.stock.yahoo.com/quote/3017.TW/eps) |
| Forward P/E | 20.3x (SA; implied forward EPS about 137) | n/a | SA |
| EV/EBITDA | 19.0x (TTM EBITDA 56.1bn) | Yahoo (stale TTM): 16.3 (Jun 25), 18.4 (Sep 25), 22.8 (Dec 25), 23.8 (Mar 26), 24.4 (Jun 26) | SA; Yahoo |
| EV/sales | 5.25x (TTM revenue 205.0bn) | Yahoo: 3.5 / 4.0 / 5.1 / 5.5 / 5.8 | SA |
| P/B | 16.3x (BVPS 170.53); SA 14.7x | | TWSE OpenAPI |
| FCF yield | 3.56% (TTM FCF 39.5bn) | | SA |
| Dividend yield | 0.75% (NT$20.88, ex-dividend 19 Aug 2026) | | Yahoo TW |
- Peers: Auras (TPEx) 27.4 / 18.8 / 18.7 (SA); Vertiv 36.3 / 19.9 / 25.8 (Yahoo); Envicool 108.2 / 38.5 / 61.8 (SA); Jentech 102.5 / 40.8 / 98.6 (SA).

### 3. What the price assumes
- SA consensus: 17 analysts ("Strong Buy"), average target NT$4,180, "3-year" revenue growth 41.8% and EPS growth 63.0% (basis not stated).
- Implied growth (computed): 20.3x forward with ROE of about 55% implies perpetual growth of about 5.6% at r = 10%. Trailing P/E is unchanged from the last two year-ends (29-31x), so the market has not re-rated the stock up or down on the 2026 earnings jump.
- Bridge vs successor: the forward multiple looks set on cold-plate volumes (the bridge). Nothing found shows micro-channel lids or two-phase cooling revenue in estimates (gap).

### 4. Cycle position
- Monthly revenue (TWD bn; YoY): Jun 17.62 (+66.1%); Jul 18.59 (+57.4%); Aug 19.48 (+54.3%); Sep 21.02 (+44.9%); Oct 22.10 (+34.4%, +5.2% MoM, the highest month in the series); Jan-Oct +65.6%. Q3 revenue 59.09bn (+51.8% YoY, +20.3% QoQ; computed). YoY growth is decelerating against strong late-2025 comparisons while monthly levels keep rising — [Yahoo TW revenue](https://tw.stock.yahoo.com/quote/3017.TW/revenue)
- EPS Q3'26 29.32 (+114% YoY, +20% QoQ). 9M gross margin 32.2%, operating margin 26.9% (TWSE OpenAPI; TTM 30.8% and 25.5%, SA). Q3 call commentary was not found (gap).

### 5-6. Events and access: November revenue around 10 Dec 2026; Q4 results in early 2027 (date not confirmed). TWSE 3017 only; liquidity about TWD 8.7bn (USD 0.26bn) a day.

### 7. Suggested label: fair (borderline stretched)
- Why: 20.3x forward and 19x EV/EBITDA, below Vertiv's EV/EBITDA, with a 3.6% FCF yield and an unchanged trailing multiple versus the last two year-ends. Against that, trailing P/E, EV/EBITDA, EV/sales and P/B are at or above the top of AVC's FY2021-25 ranges. The cycle is still rising in levels but decelerating in growth rates.
- Entry would look better on: forward P/E at or below 17-18x (about NT$2,330-2,460; the 6 Nov close was 2,310); November and December revenue re-accelerating YoY; or disclosed wins for successor products.

---

## Tier 1 — Zhongji Innolight (300308.SZ; H shares 3308.HK)

### 1. Price and performance
- A share CNY 508.90 close on 12 Nov 2026; H share HKD 649.50 (H at an 8.3% premium to A; H/A 1.083 at CNY 0.8487 per HKD; computed).
- Shares 1,177.9m = 1,115.2m A + 62.675m H. H shares first listed on 30 Jul 2026 (54.5m; over-allotment raised this to 62.675m on 31 Aug 2026) — [Eastmoney share structure](https://emweb.securities.eastmoney.com/PC_HSF10/CapitalStockStructure/PageAjax?code=SZ300308) (Chinese)
- Market cap CNY 599-604bn = USD 90-91bn (my calculation 599.4bn; SA 603.6bn). EV CNY 550-555bn (net cash about 54bn at 30 Sep 2026; SA 554.6bn) — [Eastmoney balance sheet](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/zcfzbAjaxNew?companyType=4&reportDateType=0&reportType=1&dates=2026-09-30&code=SZ300308); [SA](https://stockanalysis.com/quote/she/300308/statistics/)
- 52-week range CNY 427.34 (6 Nov 2026) to 1,416.88 (22 Jun 2026). YTD -16.6%; 12 months +3.5%; since 30 Dec 2022 +1,783%. Closing high 1,382.33 (22 Jun 2026); drawdown -63.2%. H-share month-end closes: HKD 1,028 (Jul), 1,029 (Aug), 1,062 (Sep), 676 (Oct), 649.5 (12 Nov).

### 2. Valuation multiples
| Measure | Innolight now | Own history | Sources |
|---|---|---|---|
| Trailing P/E | 23.1x (TTM net profit 25.9bn = 9M 22.24bn + Q4'25 3.67bn); SA 22.1x | Year-ends 2016-25: 653, 161, 29.0, 98.4, 56.4, 49.5, 24.4, 56.0, 27.7, 64.5 — 5-yr range 24.4-64.5x, median 49.5x; 10-yr median 56.2x. Today is below the 10-year year-end low | [companiesmarketcap](https://companiesmarketcap.com/zhongji-innolight/pe-ratio/) |
| Forward P/E | 17.6x 2026E (NP 34.03bn; n=27); 8.8x 2027E (68.10bn); 6.1x 2028E (98.62bn); SA 9.1x | Yahoo quarter-end forward (indicative): 29.0 (Sep 25), 17.5 (Dec 25), 22.6 (Mar 26), 50.3 (Jun 26), 20.9 (Sep 26) | [Eastmoney profit forecast](https://emweb.securities.eastmoney.com/PC_HSF10/ProfitForecast/PageAjax?code=SZ300308) (Chinese) |
| EV/EBITDA | 16.1x (SA; TTM EBITDA 34.5bn) | | SA |
| EV/sales | 6.7x (TTM revenue 82.8bn) | | SA |
| P/B | 6.1-6.4x (BVPS 80.11 after the H-share raise) | | Eastmoney |
| FCF yield | 0.5% (SA TTM FCF 3.14bn); 9M 2026 operating cash flow 8.0bn less capex 9.2bn ≈ -1.2bn | | SA; [Eastmoney cash flow](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/xjllbAjaxNew?companyType=4&reportDateType=0&reportType=1&dates=2026-09-30%2C2025-12-31%2C2025-09-30&code=SZ300308) |
| Dividend yield | 0.47% (SA) | | SA |
- Peers (Yahoo; trailing / forward / EV/EBITDA): Coherent 44.4 / 23.6 / 28.7; Lumentum 143 / 27.5 / 117; Fabrinet 26.3 / n/a / 18.7; Eoptolink 19.7 / 9.6 / 16.1 (SA); TFC 58.2 / 28.9 / 47.7 (SA).

### 3. What the price assumes
- Consensus (Eastmoney, 12 Nov 2026): net profit +215% in 2026 (10.80bn to 34.03bn) and +100% in 2027; revenue CNY 104.5bn (2026E) and 200.4bn (2027E). Latest notes (5-7 Nov 2026): Changjiang 2026E EPS 28.03 / 2027E 55.78; Guolian Minsheng 28.6 / 62.53; Huachuang 28.42 / 54.24; Industrial 29.48 / 51.15. Ratings in the last month: 18 institutions, 14 buy and 4 add. SA: 19 analysts, average target CNY 1,215.12.
- Implied Q4 2026 profit in consensus: CNY 11.8bn against Q3's 8.59bn (+37% QoQ; computed).
- Implied growth (computed): 8.8x 2027E with ROE of about 50% (consensus 2027E ROE 53.7%) implies perpetual growth of about -1.8% after 2027 at r = 10%. On 2026E (17.6x) it implies about +4.9% after 2026. The price is consistent with profit plateauing near the 2026 level, not with the consensus doubling in 2027.
- Bridge vs successor: published consensus assumes plug-in modules (the bridge) keep growing through 2028 (CNY 98.6bn profit in 2028E). The multiple behaves as though the market assumes co-packaged optics, or a pluggable price and volume cycle, caps earnings sooner. No source accessed quantifies either.

### 4. Cycle position
- 9M 2026 (notice 30 Oct 2026): revenue CNY 69.55bn (+178%), net profit 22.24bn (+212%), gross margin 46.4%, net margin 34.6% — [Eastmoney indicators](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SZ300308)
- Computed quarters: revenue Q1 19.50bn, Q2 22.28bn, Q3 27.77bn (+24.6% QoQ); net profit Q1 5.73bn, Q2 7.92bn, Q3 8.59bn (+8.5% QoQ). Gross margin is stable at about 46%, but profit grew more slowly than revenue in Q3.
- Working capital and capex: inventory CNY 23.9bn and receivables 17.3bn (30 Sep 2026); 9M capex 9.2bn (2.8bn for all of 2025).

### 5. Events: around 30 Jan 2027, six months after the H-share listing, when cornerstone lock-ups would typically end (terms not verified); possible 2026 results preview in January and annual results by April 2027 (dates not confirmed); Nvidia board investigation and US policy; AI-capex sentiment (30 Oct, 3 Nov).

### 6. Investor access
- ChiNext A share. It is on the Northbound Shenzhen Connect list (HKEX, updated 12 Nov 2026), but ChiNext shares may be traded Northbound only by institutional professional investors — [HKEX eligible SZSE securities](https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities/SZSE_Securities.csv); [HKEX Information Book for Investors, 6 Jul 2026](https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Getting-Started/Information-Booklet-and-FAQ/Information-Book-for-Investors/Investor_Book_En.pdf)
- A-share foreign caps: 10% for a single foreign investor and 30% for all foreign investors (Connect, QFII and RQFII combined). Exchanges publish a notice at 24%; Northbound buying halts at 28% until holdings fall to 26%; excess above 30% is force-sold last-in-first-out (HKEX book, section 3.20). ChiNext daily price limit ±20%; Northbound daily quota RMB 52bn per link.
- The H shares (3308.HK) give unrestricted Hong Kong access (5.3% of shares, at an 8% premium on 12 Nov). Liquidity: A share about CNY 22.3bn (USD 3.35bn) a day (20-day average).

### 7. Suggested label: attractive on consensus, low confidence
- Why: 8.8x 2027E, about 9x NTM and 23x trailing, below the stock's own 10-year year-end range and the 24-28x forward of US peers, after a 63% drawdown, while Q3 revenue still rose 25% QoQ. Confidence is low because the market is plainly rejecting consensus, and the company-specific reason (pricing, customer orders, CPO timing, H-share supply) could not be verified.
- Entry would look better, or be confirmed, on: Q4 2026 profit near the implied CNY 11.8bn; 2027 1.6T volume or price commitments from major customers; gross margin holding near 46%; the H-share six-month mark passing without heavy supply; Eoptolink's sequential trend stabilising.

---

## Tier 1 — Eoptolink (300502.SZ)

### 1. Price and performance
- CNY 205.58 close on 12 Nov 2026. Shares 1,394.7m (after a 4-for-10 capitalisation issue on 11 Jun 2026; 140.0m restricted) — [Eastmoney share structure](https://emweb.securities.eastmoney.com/PC_HSF10/CapitalStockStructure/PageAjax?code=SZ300502). Market cap CNY 286.7bn = USD 43.1bn; EV CNY 280.2bn (net cash 6.8bn) — [SA](https://stockanalysis.com/quote/she/300502/statistics/)
- 52-week range 161.16 (6 Nov 2026) to 618.87 (1 Jul 2026). YTD -33.2%; 12 months -12.5%; since 30 Dec 2022 +2,275% (split-adjusted). Closing high 610.49 (25 Jun 2026); drawdown -66.3%.

### 2. Valuation multiples
- Trailing P/E 19.7x (TTM net profit 14.57bn = 9M 11.37bn + Q4'25 3.20bn; SA 19.67x). Forward P/E 14.4x 2026E (NP 19.90bn; n=18), 7.5x 2027E (38.46bn), 5.0x 2028E (56.95bn) — [Eastmoney profit forecast](https://emweb.securities.eastmoney.com/PC_HSF10/ProfitForecast/PageAjax?code=SZ300502). SA forward 9.6x.
- EV/EBITDA 16.1x (TTM EBITDA 18.2bn); EV/sales 7.3x (TTM revenue 40.2bn); P/B 10.3-10.7x (BVPS 20.05); FCF yield 0.8% (SA TTM FCF 2.31bn; 9M operating cash flow 1.46bn less capex 1.81bn = -0.34bn); dividend yield 0.35% (SA).
- Own history (Yahoo quarter-ends, indicative): trailing P/E 61.4 (Sep 25), 57.0 (Dec 25), 58.6 (Mar 26), 78.9 (Jun 26), 41.4 (Sep 26). companiesmarketcap had no page.
- Peers: as for Innolight.

### 3. What the price assumes
- The six-month-average consensus looks stale after Q3: it implies Q4 2026 profit of CNY 8.5bn against Q3's 3.84bn. Latest notes are lower: Changjiang (7 Nov) 2026E EPS 12.96 / 2027E 30.88; Huaxin (6 Nov) 13.82 / 23.86; Industrial (4 Nov) 13.51 / 25.91; Sinolink (1 Nov) 14.39 / 29.56. Even Changjiang's 2026 figure implies Q4 profit of about CNY 6.7bn (+75% QoQ; computed). SA: 9 analysts, average target CNY 582.52.
- Implied growth (computed): 7.5x 2027E with ROE of about 54% implies about -4.4% a year after 2027 at r = 10%. On 2026E (14.4x) it implies about +3.5% after 2026. The price is not assuming the consensus doubling.
- Bridge vs successor: consensus rests on plug-in modules. Nothing in sources accessed shows CPO revenue in estimates.

### 4. Cycle position (the clearest negative signal in the set)
- 9M 2026 (notice 30 Oct 2026): revenue CNY 31.85bn (+93%), net profit 11.37bn (+80%), gross margin 47.7% — [Eastmoney indicators](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SZ300502)
- Computed quarters: revenue Q1 8.34bn, Q2 12.57bn, Q3 10.94bn (-13.0% QoQ, +80.5% YoY); net profit Q1 2.78bn, Q2 4.75bn, Q3 3.84bn (-19.2% QoQ, +60.7% YoY). This is the first sequential decline in the data. Inventory CNY 17.4bn (39% of total assets) at 30 Sep 2026.

### 5. Events: annual results by April 2027 (date not confirmed); release dates for the 140m restricted shares not verified; no H-share listing on record (Eastmoney, 12 Nov 2026).
### 6. Access: ChiNext; on the Shenzhen Connect list (institutional professional investors only Northbound); 10%/30% foreign caps; ±20% daily limit; liquidity about CNY 16.7bn (USD 2.5bn) a day.
### 7. Suggested label: cannot assess
- Why: the low multiple (7.5-14x forward) sits against a sequential decline and a consensus that has not caught up with it. Until Q4 shows whether Q3 was a timing dip or a turn, forward numbers are not a reliable base.
- Entry would become assessable or look better on: Q4 2026 revenue back above Q2's CNY 12.6bn; inventory falling; consensus resetting to a level the company then beats.

---

## Tier 1 — ASMPT (0522.HK)

### 1. Price and performance
- HKD 101.20 close on 12 Nov 2026. Market cap HKD 42.44bn (419.4m shares) = USD 5.41bn; EV HKD 40.54bn (net cash 1.91bn) — [SA, 12 Nov 2026](https://stockanalysis.com/quote/hkg/0522/statistics/)
- 52-week range 68.90 (24 Nov 2025) to 244.40 (30 Jun 2026). YTD +30.2%; 12 months +27.6%; since 30 Dec 2022 +81.9%. Closing high 238.80 (30 Jun 2026); drawdown -57.6%.

### 2. Valuation multiples
| Measure | ASMPT now | Own history | Sources |
|---|---|---|---|
| Trailing P/E | 20.4x (SA) / 26.9x (Yahoo TTM EPS HK$3.76); about 15.3x on Q3 adjusted EPS annualised (1.65 x 4) | Year-ends (companiesmarketcap): 9.8 (2021), 8.3 (2022, earnings peak), 42.3 (2023), 89.8 (2024); 2025 not shown | [companiesmarketcap](https://companiesmarketcap.com/asm-pacific-technology/pe-ratio/) |
| Forward P/E | 17.1x (SA; implied forward EPS about HK$5.91); Yahoo 16.2x | Yahoo forward 20.3x at 30 Jun 2025 (only point) | SA; [Yahoo](https://finance.yahoo.com/quote/0522.HK/key-statistics/) |
| EV/EBITDA | 13.6x (SA; TTM EBITDA 2.64bn) | | SA |
| EV/sales | 2.26x (TTM revenue 17.98bn) | Yahoo: 1.78x at 30 Jun 2025 | SA; Yahoo |
| P/B | 2.45x (BVPS HK$41.26) | | SA |
| FCF yield | 1.6% (TTM FCF HK$0.68bn) | | SA |
| Dividend yield | 2.7% (SA trailing) / 1.9% (Yahoo forward) | | |
- Peers (Yahoo; trailing / forward / EV/EBITDA / P/B): BESI 41.5 / 22.9 / 31.7 / 18.0; Kulicke & Soffa 31.9 / 10.9 / 23.7 / 4.0; Hanmi Semiconductor 78.9 / 34.8 / 58.1 / 24.1; Disco 30.8 / 26.1 / 19.6 / 7.8. Peer forward median about 24.5x.

### 3. What the price assumes
- SA consensus: 19 analysts ("Buy"), average target HK$180.01, "3-year" revenue growth 24.0% and EPS growth 91.4% (basis not stated). ASMPT said its Q4 guide was "above the market consensus".
- Implied growth (computed): 17.1x forward with a low forward ROE of about 14% (5.91 / 41.26) implies about 7.0% perpetual growth at r = 10%. With a low ROE, growth needs reinvestment, so the multiple is less undemanding than the headline P/E suggests. On EV/sales (2.26x) and forward P/E, ASMPT is below hybrid-bonding peer BESI and below Disco and Hanmi.
- Bridge vs successor: TCB (the bridge) is carrying results — record chip-to-substrate orders "led by strong demand for larger compound-die TCB tools from OSAT partners of a leading advanced logic customer", and repeat chip-to-wafer orders from a leading IDM. In memory, purchases are tied to HBM4 schedules and "larger capability-driven investments have been pushed-out". Hybrid bonding (the successor) is at "sampling, evaluation and qualification" with leading logic and memory customers, with no volume orders disclosed. The discount to BESI suggests the price does not assume hybrid bonding on schedule — [ASMPT Q3 2026 results announcement](https://www.asmpt.com/site/assets/files/85973/q3_2026_en_announcement.pdf)

### 4. Cycle position (results of 28 Oct 2026)
- Q3 bookings HK$8.85bn (US$1.13bn), +24.7% QoQ and +137.9% YoY; book-to-bill 1.69, the highest since Q1 2021. Revenue HK$5.25bn (US$669m), +6.3% QoQ and +48.7% YoY. Adjusted gross margin 42.9%; net profit HK$533.2m; adjusted net profit HK$689.7m (+486% YoY); EPS HK$1.28 (adjusted HK$1.65) — [ASMPT Q3 2026 press release](https://www.asmpt.com/site/assets/files/85970/asmpt_2026_q3_press_release.pdf)
- SEMI: revenue HK$2.93bn (+68% YoY); bookings HK$4.42bn (+156% YoY, the highest since Q1 2021); adjusted gross margin 46.6%. SMT: revenue HK$2.31bn (+30% YoY); record bookings HK$4.43bn, including more than US$100m of bulk orders and pull-ins; adjusted gross margin 38.2%.
- Q4 2026 guide: revenue US$670-730m (midpoint +4.6% QoQ, +37.5% YoY). SEMI is expected flat because of longer lead times on advanced-packaging tools; Q4 bookings will be below Q3's record but significantly higher YoY; "AI demand is expected to drive sustained revenue growth in 2027". Other: the NEXX disposal closed on 3 Jun 2026; Bassel Haddad is the new group CEO; quarter-panel TCB has reached sample bonding with a leading logic customer.

### 5. Events: Q4 and full-year 2026 results around late February to early March 2027 (date not confirmed); HBM4 tool decisions at memory customers; hybrid-bonding qualification news; Q4 bookings against the HK$8.85bn record.
### 6. Access: HKEX main board 0522 (no ADR). Liquidity is thin relative to the rest of the set: about HKD 473m (USD 60m) a day (20-day average). Southbound eligibility was not checked.
### 7. Suggested label: fair (leaning attractive)
- Why: about 17x NTM, 2.3x EV/sales and 13.6x EV/EBITDA after a 58% drawdown, below the equipment-peer forward median (about 24.5x), with record bookings. Against that, the low ROE means the multiple still implies solid growth, part of the bookings are one-off SMT pull-ins, and HBM TCB demand has been pushed out.
- Entry would look better on: a price near HK$89 or lower (about 15x NTM EPS of 5.91); Q4 bookings holding above about HK$6bn (book-to-bill above 1); a firm HBM4 TCB order or a hybrid-bonding volume order.

---

## Own five-year valuation ranges, Tier 1 (fiscal year-ends FY2021-FY2025 against "current" at the 11 Nov 2026 close)
Source: StockAnalysis ratios pages, fetched 12 Nov 2026 ([TSMC example](https://stockanalysis.com/quote/tpe/2330/financials/ratios/); same pattern for tpe/3711, tpe/3037, tpe/2308, tpe/3017, she/300308, she/300502, hkg/0522). Each cell reads: now (FY21-25 low-high; median). Five year-end points understate intra-year extremes. Longer 10-year trailing P/E histories are in the company sections (companiesmarketcap).
| Company | Trailing P/E | Forward P/E | P/B | EV/sales | EV/EBITDA | FCF yield | Dividend yield |
|---|---|---|---|---|---|---|---|
| TSMC | 24.0 (11.7-26.9; 23.7) | 16.4 (11.9-23.5; 19.3) | 8.6 (4.0-7.5; 6.5) above range | 11.6 (4.9-10.1; 9.3) above | 15.9 (7.1-14.7; 13.5) above | 2.4% (1.7-4.5; 2.5) | 1.2% (1.4-2.5; 1.8) below |
| ASE | 35.4 (6.5-26.9; 18.3) above | 19.2 (8.1-20.8; 14.5) | 5.7 (1.3-2.9; 1.8) above | 3.7 (0.9-2.1; 1.3) above | 17.0 (4.3-11.4; 7.7) above | -3.4% (-2.1-10.4; 2.4) below | 1.1% (3.3-9.4; 5.2; FY25 n/a) below |
| Unimicron | 39.6 (6.0-50.4; 25.8) | 24.6 (5.8-28.5; 20.1) | 7.9 (1.9-5.2; 2.8) above | 8.0 (1.2-3.5; 2.5) above | 31.7 (3.3-16.1; 10.9) above | 0.3% (-7.4-16.4; 3.0) | 0.25% (0.9-6.7; 1.5) below |
| Delta | 37.3 (22.8-41.6; 26.7) | 22.7 (19.6-29.8; 23.7) below median | 8.4 (3.3-7.7; 3.8) above | 4.55 (2.0-4.5; 2.4) at top | 21.2 (13.0-22.6; 15.5) | 2.1% (0.7-5.3; 3.3) | 0.9% (1.2-3.4; 2.0) below |
| AVC | 31.0 (9.5-30.6; 24.3) at top | 20.3 (10.3-22.6; 19.8) | 14.7 (2.2-11.6; 5.0) above | 5.25 (0.7-4.1; 2.1) above | 19.0 (5.0-18.9; 13.5) at top | 3.6% (2.1-13.1; 5.2) | 0.8% (1.4-4.9; 2.1) below |
| Innolight | 22.1 (17.3-62.8; 38.7) | 9.1 (14.8-36.1; 27.3) below range | 6.1 (1.8-21.4; 6.0) | 6.7 (2.1-17.6; 5.7) | 16.1 (12.0-47.5; 29.7) below median | 0.5% (-0.1-7.8; 0.2) | 0.5% (0.2-0.7; 0.4) |
| Eoptolink | 19.7 (13.3-50.9; 30.0) | 9.6 (15.2-39.1; 26.5) below range | 10.7 (2.5-23.7; 6.4) | 7.3 (3.1-17.0; 9.3) | 16.1 (11.6-40.4; 24.7) below median | 0.8% (-1.0-3.9; 1.5) | 0.35% (0.2-0.5; 0.3) |
| ASMPT | 20.4 (8.8-90.4; 35.9) | 17.1 (13.0-30.6; 24.3) below median | 2.45 (1.5-2.3; 2.0) above | 2.26 (1.2-2.4; 2.1) | 13.6 (6.1-29.2; 19.3) below median | 1.6% (-0.5-10.8; 6.3) | 2.7% (0.6-5.8; 1.2) |
- Reading: on enterprise-value and book multiples, ASE, Unimicron and AVC sit above (or at the top of) their own five-year ranges; TSMC and Delta are above range on EV and book measures but at or below median on forward P/E; Innolight, Eoptolink and ASMPT are below their five-year medians on forward P/E and EV/EBITDA. ROE was also at or near five-year highs for most of the set (for example TSMC 41.9% now against 26.7-39.2%; AVC 66.4% against 26.3-49.9%; SA), which explains part of the book-multiple expansion.

## Tier 2 — compact snapshots (12 Nov 2026 closes; YTD and 12-month price returns from Yahoo; market cap, forward P/E and EV/EBITDA from StockAnalysis on 12 Nov 2026 unless stated)
| Company | Price | Market cap | Forward P/E (SA, ≈NTM) and fiscal-year consensus | EV/EBITDA | YTD / 12m | Cycle line |
|---|---|---|---|---|---|---|
| Luxshare 002475.SZ (H 2475.HK, listed 9 Jul 2026) | CNY 50.82; H HKD 50.30 (16% below A) | CNY 393.5bn on Eastmoney's 7,743m shares (SA 409.8bn) = USD 59-62bn | 15.1x; Eastmoney 19.5x 2026E / 13.8x 2027E | 17.4x | -10.4% / -12.0% | 9M rev 285.0bn (+29%), NP 13.06bn (+13%); Q3 NP +7% YoY; gross margin 11.9%; 9M operating cash flow negative ([Eastmoney](https://emweb.securities.eastmoney.com/PC_HSF10/NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=SZ002475)) |
| Envicool 002837.SZ | CNY 40.98 | CNY 52.4bn (USD 7.9bn) | 38.5x; Eastmoney 50.9x 2026E (stale; Sinolink 1 Nov EPS 0.601 → 68x) | 61.8x | -50.2% / -20.5% | 9M rev 4.95bn (+23%) but NP 0.37bn (-7.6%); gross margin 26.1% vs 27.3% a year earlier |
| Bizlink 3665.TW | TWD 1,515 | TWD 295.5bn (USD 9.0bn) | 15.6x | 17.2x | -0.3% / +1.0% | Oct rev 11.85bn (+80% YoY, +27% MoM); Jan-Oct +44% |
| Auras 3324.TWO | TWD 1,170 | TWD 108.9bn (USD 3.3bn) | 18.8x (TPEx trailing 26.3x) | 18.7x | +15.8% / +15.3% | Oct rev 3.37bn (+45% YoY); Jan-Oct +69%; company cites rising AI-server liquid-cooling share ([TPEx OpenAPI](https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O)) |
| Accton 2345.TW | TWD 1,525 | TWD 852.3bn (USD 25.9bn) | 14.7x | 18.3x | +28.7% / +55.1% | Oct rev 44.66bn (+91% YoY, +11% MoM); Jan-Oct +66% |
| Elite Material 2383.TW | TWD 4,105 | TWD 1.47tn (USD 44.7bn) | 18.4x | 34.1x | +149.5% / +205.2% | Oct rev 24.47bn (+203% YoY); 9M EPS 82.92; 9M operating margin 27% |
| Lite-On 2301.TW | TWD 228 | TWD 508.2bn (USD 15.4bn) | 16.5x | 17.1x | +39.4% / +36.9% | Oct rev 20.07bn (+32% YoY); 9M EPS 8.08 |
| Kinsus 3189.TW | TWD 667 | TWD 351.5bn (USD 10.7bn) | 23.7x | 24.2x | +319.5% / +407.2% | Oct rev 5.37bn (+49% YoY); 9M EPS 8.38; joins MSCI Standard after 30 Nov |
| Nan Ya PCB 8046.TW | TWD 972 | TWD 628.1bn (USD 19.1bn) | 23.5x | 37.0x | +303.3% / +241.7% | Oct rev 6.29bn (+70% YoY, +13% MoM); 9M EPS 10.63; joins MSCI Standard after 30 Nov |
| Jentech 3653.TW | TWD 5,605 | TWD 825.1bn (USD 25.1bn) | 40.8x | 98.6x | +104.2% / +147.5% | Oct rev 3.07bn (+81% YoY); 9M EPS 45.03 |
| JCET 600584.SS | CNY 54.45 | CNY 97.4bn (USD 14.6bn) | 28.7x; Eastmoney 43.5x 2026E / 33.7x 2027E | 15.1x | +48.0% / +44.5% | 9M rev 30.95bn (+8%), NP 1.62bn (+70%); gross margin 16.0% |
| Tongfu 002156.SZ | CNY 48.36 | CNY 77.1bn (USD 11.6bn) | 40.1x; Eastmoney 2026E stale (9M NP of 3.06bn already above the 2.29bn 2026E; consensus inconsistent) | 14.8x | +28.3% / +24.5% | 9M rev 24.89bn (+24%), NP 3.06bn (+256%); placement shares listed 16 Sep 2026 |
| TFC Optical 300394.SZ | CNY 140.34 | CNY 153.1bn (USD 23.0bn) | 28.9x; Eastmoney 44.4x 2026E / 25.9x 2027E | 47.7x | -3.2% / +19.8% | 9M rev 4.75bn (+21%), NP 2.08bn (+42%); Q3 rev +28% QoQ; gross margin 62.6% |
| FIT 6088.HK | HKD 2.80 | HKD 19.9bn (USD 2.5bn) | 10.9x (5 analysts) | 6.4x | -43.4% / -47.3% | Not retrieved; SA shows TTM revenue of 40.7bn and a 3-year forecast growth of 9.7% |
Sources: [SA statistics pages](https://stockanalysis.com/quote/tpe/2345/statistics/) (one per ticker, same URL pattern); [Eastmoney profit forecasts](https://emweb.securities.eastmoney.com/PC_HSF10/ProfitForecast/PageAjax?code=SZ002475); [TWSE OpenAPI revenue](https://openapi.twse.com.tw/v1/opendata/t187ap05_L) and [9M income statements](https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci); Yahoo chart data.

### Listing status of CXMT and SJ Semiconductor (as of 12 Nov 2026)
- CXMT (ChangXin Memory): listed on the Shanghai STAR Market on 27 Jul 2026 as 长鑫科技 (Yahoo name "CXMT Corporation"; 688825.SS; subscription 16 Jul 2026; issue price CNY 8.66) — [Eastmoney IPO data](https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPTA_APP_IPOAPPLY&columns=SECURITY_CODE,SECURITY_NAME_ABBR,APPLY_DATE,LISTING_DATE,ISSUE_PRICE,TRADE_MARKET,MARKET_TYPE&sortColumns=APPLY_DATE&sortTypes=-1&pageSize=300&pageNumber=1) (Chinese). First-day close CNY 49.00; closing high 61.80 (17 Aug 2026); 12 Nov close 40.97 (-33.7% from the high; 4.7x the issue price) — [Yahoo chart 688825.SS](https://query1.finance.yahoo.com/v8/finance/chart/688825.SS?range=1y&interval=1d). Not on the Northbound eligible lists of 12 Nov 2026; STAR shares are in any case limited to institutional professional investors Northbound.
- SJ Semiconductor (盛合晶微): listed on the STAR Market on 21 Apr 2026 (688820.SS; subscription 9 Apr 2026; issue price CNY 19.68). First-day close 76.65; closing high 229.00 (26 May 2026); 12 Nov close 89.32 (-61.0% from the high) — Eastmoney IPO data; [Yahoo chart 688820.SS](https://query1.finance.yahoo.com/v8/finance/chart/688820.SS?range=1y&interval=1d). Not on the Northbound eligible lists of 12 Nov 2026.
- Valuation multiples for both were not retrieved.

## Peer comparison across all names (12 Nov 2026; SA unless stated; "label" is the suggested entry label for Tier 1 only)
| Company | Mkt cap (USD bn) | Trailing P/E | Fwd P/E (SA ≈NTM) | EV/EBITDA | Drawdown from 52w closing high | YTD | Label |
|---|---|---|---|---|---|---|---|
| TSMC | 1,843 | 24.0 | 16.4 | 15.9 | -9.5% | +51.0% | fair |
| ASE | 79 | 35.4 | 19.2 | 17.0 | -23.1% | +133.9% | stretched (borderline) |
| Unimicron | 39.5 | 39.6 | 24.6 | 31.7 | -40.2% | +260.0% | stretched |
| Delta | 97.8 | 37.3 | 22.7 | 21.2 | -50.8% | +28.8% | fair |
| AVC | 33-34 | 31.0 | 20.3 | 19.0 | -24.7% | +83.8% | fair (borderline stretched) |
| Innolight | 90-91 | 22.1 | 9.1 | 16.1 | -63.2% | -16.6% | attractive (low confidence) |
| Eoptolink | 43.1 | 19.7 | 9.6 | 16.1 | -66.3% | -33.2% | cannot assess |
| ASMPT | 5.4 | 20.4 | 17.1 | 13.6 | -57.6% | +30.2% | fair (leaning attractive) |
| Luxshare | 59-62 | 21.0 | 15.1 | 17.4 | -36.6% | -10.4% | |
| Envicool | 7.9 | 108.2 | 38.5 | 61.8 | -56.0% | -50.2% | |
| Bizlink | 9.0 | 27.9 | 15.6 | 17.2 | -48.5% | -0.3% | |
| Auras | 3.3 | 27.4 | 18.8 | 18.7 | -31.6% | +15.8% | |
| Accton | 25.9 | 24.1 | 14.7 | 18.3 | -44.5% | +28.7% | |
| Elite Material | 44.7 | 44.0 | 18.4 | 34.1 | -35.4% | +149.5% | |
| Lite-On | 15.4 | 23.5 | 16.5 | 17.1 | -28.2% | +39.4% | |
| Kinsus | 10.7 | 67.7 | 23.7 | 24.2 | -39.4% | +319.5% | |
| Nan Ya PCB | 19.1 | 77.8 | 23.5 | 37.0 | -35.4% | +303.3% | |
| Jentech | 25.1 | 102.5 | 40.8 | 98.6 | -22.2% | +104.2% | |
| JCET | 14.6 | 43.9 | 28.7 | 15.1 | -48.9% | +48.0% | |
| Tongfu | 11.6 | 21.6 | 40.1 | 14.8 | -38.6% | +28.3% | |
| TFC | 23.0 | 58.2 | 28.9 | 47.7 | -60.5% | -3.2% | |
| FIT | 2.5 | 15.6 | 10.9 | 6.4 | -73.1% | -43.4% | |

Global peers (Yahoo statistics, 11-12 Nov 2026; trailing P/E / forward P/E (Yahoo basis) / EV/EBITDA): Amkor 13.9 / 13.3 / 6.9; Vertiv 36.3 / 19.9 / 25.8; Eaton 35.4 / 22.1 / 23.3; Schneider 28.3 / 20.0 / 17.7; Coherent 44.4 / 23.6 / 28.7; Lumentum 143 / 27.5 / 117; Fabrinet 26.3 / n/a / 18.7; BESI 41.5 / 22.9 / 31.7; Kulicke & Soffa 31.9 / 10.9 / 23.7; Hanmi 78.9 / 34.8 / 58.1; Disco 30.8 / 26.1 / 19.6; Ibiden 47.4 / n/a / 17.7; Samsung Electro-Mechanics 66.1 / 19.1 / 29.8; AT&S 82.3 / n/a / 12.7; UMC 15.0 / 15.8 / 7.7; SMIC 46.5 / 27.1 / 15.4 — e.g. [Yahoo VRT statistics](https://finance.yahoo.com/quote/VRT/key-statistics/). Yahoo "current" values are at the latest close available on 12 Nov (11 Nov for US and European listings).

## What could not be verified
- Company-specific causes of the 60-66% drawdowns in Innolight, Eoptolink and TFC, and of the Q3 sequential decline at Eoptolink. Only market-wide causes (AI-capex worries, US midterms, Nvidia controversy) are sourced.
- Q3 call guidance and commentary for Delta, AVC and Unimicron (orders, pricing, capacity, 800V DC, ABF pricing, glass core, two-phase cooling); the source of Unimicron's NT$15.1bn of 9M non-operating income; the reason for Delta's Q3 EPS dip.
- Previous-cycle peak and trough margins for all Tier 1 companies (no remembered figures used).
- Ten-year ranges for forward P/E, EV/EBITDA, P/B, FCF yield and dividend yield. Five-year (FY2021-25 year-end) ranges are tabulated from StockAnalysis, and ten-year trailing P/E year-end histories from companiesmarketcap exist for TSMC (ADR basis), ASE, Delta, Unimicron and Innolight (ASMPT's is incomplete; none for AVC or Eoptolink). Intra-year highs and lows of the multiples were not available.
- Exact dates for the next results (TSMC mid-January is customary, not confirmed); Nvidia's next earnings date; lock-up terms for the Innolight and Luxshare H shares and CXMT/SJ STAR placements; Eoptolink restricted-share release dates.
- ETF weights (iShares holdings files did not download); per-stock foreign-ownership limits for Taiwanese names other than ASE; Southbound eligibility of ASMPT and the H shares.
- StockAnalysis's "3-year growth" consensus fields and the exact basis of its forward P/E (likely NTM) are as labelled on the page and not independently verified.
- Data quality: Yahoo's A-share market caps use stale share counts (not used); Yahoo's historical quarter-end multiples for some Taiwanese names lag a quarter; Eastmoney's six-month-average consensus lags Q3 for Eoptolink, Envicool and Tongfu.

## Sources (all fetched 12 Nov 2026)
- Prices, returns, FX: Yahoo Finance chart endpoint, https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=5y&interval=1d (tickers as listed above, plus 3308.HK, 2475.HK, 688825.SS, 688820.SS, TWD=X, CNY=X, HKD=X, ^TWII, ^SOX, ^HSI)
- Yahoo statistics and analysis: https://finance.yahoo.com/quote/{ticker}/key-statistics/ and https://finance.yahoo.com/quote/{ticker}/analysis/ (2330.TW, TSM, 3711.TW, ASX and peers)
- Yahoo Taiwan revenue, EPS and dividend pages: https://tw.stock.yahoo.com/quote/{2330|3711|3037|2308|3017}.TW/{revenue|eps|dividend}
- TWSE OpenAPI: https://openapi.twse.com.tw/v1/exchangeReport/BWIBBU_ALL ; https://openapi.twse.com.tw/v1/opendata/t187ap05_L ; https://openapi.twse.com.tw/v1/opendata/t187ap06_L_ci ; https://openapi.twse.com.tw/v1/opendata/t187ap07_L_ci ; https://openapi.twse.com.tw/v1/fund/MI_QFIIS_sort_20 ; https://openapi.twse.com.tw/v1/fund/MI_QFIIS_cat
- TPEx OpenAPI: https://www.tpex.org.tw/openapi/v1/tpex_mainboard_peratio_analysis ; https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap05_O ; https://www.tpex.org.tw/openapi/v1/mopsfin_t187ap06_O_ci
- TSMC 6-Ks: Q3 release https://www.sec.gov/Archives/edgar/data/1046179/000104617926000726/a3q26e_withguidancexfinal.htm (15 Oct 2026); board resolutions https://www.sec.gov/Archives/edgar/data/1046179/000104617926000797/tsm-boardx202611xx.htm (10 Nov 2026); filing index via https://data.sec.gov/submissions/CIK0001046179.json
- ASE 6-Ks: https://www.sec.gov/Archives/edgar/data/1122411/000095010326016324/dp255760_6k.htm and https://www.sec.gov/Archives/edgar/data/1122411/000095010326016323/dp255782_6k.htm (29 Oct 2026)
- ASMPT Q3 2026 (28 Oct 2026): https://www.asmpt.com/site/assets/files/85970/asmpt_2026_q3_press_release.pdf ; https://www.asmpt.com/site/assets/files/85973/q3_2026_en_announcement.pdf ; https://www.asmpt.com/site/assets/files/85971/asmpt_q3_2026_investor_presentation.pdf
- Eastmoney F10 (Chinese): https://emweb.securities.eastmoney.com/PC_HSF10/ProfitForecast/PageAjax?code={SZ300308|SZ300502|SZ002475|SZ002837|SH600584|SZ002156|SZ300394} ; .../NewFinanceAnalysis/ZYZBAjaxNew?type=0&code=... ; .../CapitalStockStructure/PageAjax?code=... ; .../CompanySurvey/PageAjax?code=... ; balance sheet and cash flow endpoints as linked above; IPO data https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPTA_APP_IPOAPPLY...
- StockAnalysis statistics (12 Nov 2026): https://stockanalysis.com/quote/{tpe/2330|tpe/3711|tpe/3037|tpe/2308|tpe/3017|she/300308|she/300502|hkg/0522|tpe/2345|tpe/2383|tpe/3665|tpe/2301|tpe/3189|tpe/8046|tpe/3653|tpex/3324|hkg/6088|she/002837|she/002475|sha/600584|she/002156|she/300394}/statistics/
- companiesmarketcap P/E history: https://companiesmarketcap.com/{tsmc|ase-group|delta-electronics|unimicron|zhongji-innolight|asm-pacific-technology}/pe-ratio/
- HKEX: eligible lists https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Eligible-Stocks/View-All-Eligible-Securities/SZSE_Securities.csv and .../SSE_Securities.csv (updated 12 Nov 2026); Information Book for Investors (version 6 Jul 2026) https://www.hkex.com.hk/-/media/HKEX-Market/Mutual-Market/Stock-Connect/Getting-Started/Information-Booklet-and-FAQ/Information-Book-for-Investors/Investor_Book_En.pdf
- Focus Taiwan (CNA): https://focustaiwan.tw/business/202610150013 ; /202610150018 ; /202610150023 ; /202610210012 ; /202610300006 ; /202610300015 ; /202610310008 ; /202611030023 ; /202611040008 ; /202611060006 ; /202611060016 ; /202611060020 ; /202611090013 ; /202611090017 ; /202611090020 ; /202611100014 ; /202611110018 ; /202611120014 ; /202611120015

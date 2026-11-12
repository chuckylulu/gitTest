# Valuation, share-price history, what prices assume and the sector cycle: US- and European-listed companies in or next to chip and software verification/specification (as of 12 November 2026)

Research date: 12 November 2026 (all pages fetched on this date). STATUS: in progress; sections are filled progressively.
Price date used in all tables: close of Wednesday 11 November 2026 (the latest close on or before 12 November 2026 for every listing: US markets close 16:00 EST; Xetra, Euronext Paris and London AIM were still trading on 12 November when data were pulled at about 12:40 UTC).
FX (ECB euro reference rates, 11 November 2026) [PRIMARY]: EUR/USD 1.1127; EUR/GBP 0.83618, so GBP/USD = 1.3307 (cross computed by the researcher) — [ECB Data Portal, EXR D.USD.EUR.SP00.A and D.GBP.EUR.SP00.A](https://data-api.ecb.europa.eu/service/data/EXR/D.USD.EUR.SP00.A?startPeriod=2026-11-05&endPeriod=2026-11-12&format=csvdata)
Tags: [PRIMARY] filing, exchange or official data; [SECONDARY] aggregator, press or analyst report; [UNVERIFIED] could not be verified; [CALC] arithmetic by this researcher from the cited inputs (method stated).
This is analysis for exploration, not financial advice. No recommendations or price targets of the researcher's own are given; analysts' views are attributed and dated.

Main data sources (chosen for consistency):
- Valuation fields: StockAnalysis.com statistics, overview and forecast pages, all "Last updated: Nov 12, 2026" (EnSilica: Nov 11, 2026); financial data supplied to that site by S&P Global Market Intelligence [SECONDARY]. Pages: https://stockanalysis.com/stocks/{ticker}/statistics/ and https://stockanalysis.com/quote/{exchange}/{ticker}/statistics/
- Daily closing prices (YTD, 1-year, 52-week, event-day moves): Nasdaq.com historical-quote data for US listings (exchange data; [PRIMARY] for Nasdaq-listed SNPS, CDNS, AIP, ARM, PTC, SVCO; [SECONDARY] consolidated data for NYSE-listed KEYS and ULS), and Euronext Paris historical price downloads for DSY and ATE [PRIMARY]. URLs: https://www.nasdaq.com/market-activity/stocks/{ticker}/historical ; https://live.euronext.com/en/product/equities/FR0014003TT8-XPAR (DSY) and https://live.euronext.com/en/product/equities/FR0000071946-XPAR (ATE).
- Company results releases where cited.

## 1. Valuation table, all at the close of 11 November 2026

### Takeaway
On one consistent data source, the two EDA leaders trade at similar enterprise values (about $91-96bn) but very different multiples: Synopsys at about 10x EV/sales and 26x forward earnings, Cadence at about 15x EV/sales and 35x forward earnings; Arm is far above both (39x EV/sales, 79x forward P/E), while the European engineering-software and services names (Dassault 5x sales, 18x forward P/E; Alten 0.7x sales, 10x forward P/E) and Siemens (about 3x sales, 21-22x forward P/E) sit far lower. No company had to be dropped; EnSilica has no consensus estimates on the source used.

### Cited Findings

Table 1a. Price, size and price performance (close 11 Nov 2026)

| Company (ticker, exchange) | Close 11 Nov 2026 | Market cap, local | Market cap, USD | Enterprise value, local | 52-week high / low (intraday, date) | % below 52-week high (close vs intraday high) | YTD change (vs 31 Dec 2025 close) | 1-year change (vs 11 Nov 2025 close) |
|---|---|---|---|---|---|---|---|---|
| Synopsys (SNPS, Nasdaq) | $462.12 | $88.56bn | $88.56bn | $95.79bn | $539.48 (26 May 2026) / $362.55 (15 Sep 2026) | -14.3% | -1.6% (from $469.72) | +16.8% (from $395.60) |
| Cadence (CDNS, Nasdaq) | $329.26 | $90.34bn | $90.34bn | $91.61bn | $416.69 (2 Jun 2026) / $262.75 (3 Feb 2026) | -21.0% | +5.3% (from $312.58) | +3.4% (from $318.51) |
| Siemens AG (SIE, Xetra) | EUR 277.00 | EUR 212.7bn [CALC] | $236.7bn [CALC] | EUR 258.6bn [CALC] (includes Siemens Financial Services debt; see Table 1b) | EUR 291.70 / EUR 198.00 (dates n/a) | -5.0% [CALC] | n/a (no daily series obtained) | +14.83% (StockAnalysis "52-week price change", at 12 Nov intraday price) |
| Arteris (AIP, Nasdaq) | $20.32 | $1.01bn | $1.01bn | $0.916bn | $50.26 (30 Jun 2026) / $12.06 (21 Nov 2025) | -59.6% | +31.1% (from $15.50) | +31.0% (from $15.51) |
| Keysight (KEYS, NYSE) | $305.64 | $52.03bn | $52.03bn | $52.19bn | $389.93 (6 Oct 2026) / $167.23 (21 Nov 2025) | -21.6% | +50.4% (from $203.19) | +67.5% (from $182.46) |
| PTC (PTC, Nasdaq) | $196.14 | $21.28bn | $21.28bn | $22.85bn | $196.79 (10 Nov 2026) / $108.50 (12 Jun 2026) | -0.3% | +12.6% (from $174.21) | +10.2% (from $178.00) |
| Dassault Systemes (DSY, Euronext Paris) | EUR 25.34 | EUR 33.54bn [CALC] | $37.32bn [CALC] | EUR 32.50bn [CALC] | EUR 26.39 (9 Nov 2026) / EUR 15.82 (17 Feb 2026) | -4.0% | +6.3% (from EUR 23.84) | +5.9% (from EUR 23.93) |
| Arm Holdings (ARM, Nasdaq ADS) | $203.36 | $217.60bn | $217.60bn | $214.47bn | $452.70 (18 Jun 2026) / $100.02 (5 Feb 2026) | -55.1% | +86.0% (from $109.31) | +35.8% (from $149.74) |
| Silvaco (SVCO, Nasdaq) | $7.66 | $261.95m | $261.95m | $255.0m | $14.39 (1 Jul 2026) / $3.07 (9 Mar 2026) | -46.8% | +89.1% (from $4.05) | +57.6% (from $4.86) |
| Alten (ATE, Euronext Paris) | EUR 86.95 | EUR 2.94bn [CALC] | $3.27bn [CALC] | EUR 2.92bn [CALC] | EUR 92.00 (5 Nov 2026) / EUR 50.90 (30 Mar 2026) | -5.5% | +20.0% (from EUR 72.45) | +27.8% (from EUR 68.05) |
| EnSilica (ENSI, London AIM) | 66.00p | GBP 88.6m [CALC] | $117.9m [CALC] | GBP 87.9m [CALC] | 126.00p / 32.00p (dates n/a) | -47.6% [CALC] | n/a | +72.15% (StockAnalysis 52-week change) |
| UL Solutions (ULS, NYSE) | $81.58 | $16.47bn | $16.47bn | $16.39bn | $107.54 (6 May 2026) / $63.17 (17 Sep 2026) | -24.1% | +3.4% (from $78.86) | -7.0% (from $87.72) |

Sources and method for Table 1a:
- Closes, 52-week highs/lows (intraday), YTD and 1-year changes for SNPS, CDNS, AIP, KEYS, PTC, ARM, SVCO, ULS: computed [CALC] from daily data — [Nasdaq.com historical quotes, data through 11 Nov 2026](https://www.nasdaq.com/market-activity/stocks/snps/historical); DSY and ATE from [Euronext Paris historical prices (DSY)](https://live.euronext.com/en/product/equities/FR0014003TT8-XPAR) and [(ATE)](https://live.euronext.com/en/product/equities/FR0000071946-XPAR). The 52-week ranges match the ranges shown by StockAnalysis for every US listing checked (e.g. SNPS 362.55-539.48; CDNS 262.75-416.69; ARM 100.02-452.70) [SECONDARY] — [StockAnalysis SNPS overview](https://stockanalysis.com/stocks/snps/).
- Market caps and EVs for US listings: [StockAnalysis statistics pages, updated 12 Nov 2026](https://stockanalysis.com/stocks/snps/statistics/) [SECONDARY]; computed by that site at the 11 Nov close.
- European listings: StockAnalysis pages showed 12 Nov intraday prices (SIE EUR 283.30 at 12:46 CET, DSY EUR 25.33, ATE EUR 87.05, ENSI 66.10p); market caps and EVs were restated by the researcher to the 11 Nov close (StockAnalysis share counts: SIE 767.99m, DSY about 1.324bn, ATE 33.83m, ENSI 134.24m; EV restated by keeping StockAnalysis's EV-minus-market-cap bridge constant) and converted at ECB rates [CALC] — [StockAnalysis ETR:SIE](https://stockanalysis.com/quote/etr/SIE/statistics/), [EPA:DSY](https://stockanalysis.com/quote/epa/DSY/statistics/), [EPA:ATE](https://stockanalysis.com/quote/epa/ATE/statistics/), [AIM:ENSI](https://stockanalysis.com/quote/aim/ENSI/statistics/).
- 1-year change differs slightly from StockAnalysis's "52-week price change" (SNPS +15.31%, CDNS +0.10%, KEYS +66.55%, ARM +31.34%, PTC +10.51%, ULS -6.15%, AIP +36.01%, SVCO +51.98%) because the base date differs; both shown for transparency.
- Siemens close EUR 277.00 on 11 Nov 2026 also recorded in the sibling note siemens_eda.md (same figure).

Table 1b. Multiples and fundamentals (TTM unless stated; StockAnalysis/S&P Global data, 12 Nov 2026)

| Company | TTM revenue | EV/sales | EV/EBITDA | Trailing P/E (GAAP) | Forward P/E (non-GAAP, next 12 months) | FCF yield | Consensus revenue growth, next unreported fiscal year | GAAP operating margin (TTM) | Net cash / (net debt) |
|---|---|---|---|---|---|---|---|---|---|
| Synopsys | $9.42bn | 10.17x | 46.15x | 81.94x | 26.26x | 3.10% | FY10/2026: +37.8% ($9.72bn, includes Ansys); FY10/2027: +13.2% ($11.00bn) | 11.0% (non-GAAP Q3 FY26: 41.6%) | ($7.23bn) |
| Cadence | $6.13bn | 14.94x | 41.26x | 65.47x | 34.94x | 1.95% | FY12/2026: +21.0% ($6.41bn); FY12/2027: +14.4% ($7.33bn) | 29.9% | ($1.27bn) |
| Siemens AG | EUR 81.11bn (TTM to Jun 2026; FY09/2026 reported EUR 83.37bn) | 3.19x (SA, 12 Nov) | 18.61x (SA) | 27.99x (SA, 12 Nov intraday); 25.3x at 11 Nov close on FY26 basic EPS EUR 10.94 [CALC] | 21.96x (SA); 21.3x at 11 Nov close on FY27 consensus EPS EUR 13.02 [CALC] | 5.57% (SA); 5.7% on FY26 FCF EUR 12.10bn [CALC] | FY09/2027: +9.0% (EUR 90.66bn vs EUR 83.19bn FY26 consensus) | 12.4% (SA); Industrial Business margin 16.3% FY26 | SA: (EUR 38.99bn) incl. financial services; company "industrial net debt" EUR 4.78bn |
| Arteris | $92.98m | 9.85x | n/a (negative EBITDA) | n/a (loss) | 338.67x (not meaningful) | 0.21% | FY12/2026: +37.0% ($96.70m); FY12/2027: +21.0% ($117.03m) | -40.6% | $95.0m |
| Keysight | $6.58bn | 7.93x | 30.74x | 41.98x | 22.61x | 2.82% | FY10/2026: +32.4% ($7.12bn); FY10/2027: +15.4% ($8.21bn) | 19.8% | ($0.16bn) |
| PTC | $2.73bn | 8.36x | 21.90x | 21.96x | 21.74x | 4.10% | FY09/2027: +6.2% ($2.90bn); FY09/2028: +8.1% ($3.14bn) | 34.6% | ($1.56bn) |
| Dassault Systemes | EUR 6.30bn | 5.16x | 16.85x | 25.59x | 17.81x | 5.13% | FY12/2026: +3.4% (EUR 6.45bn); FY12/2027: +7.5% (EUR 6.93bn) | 25.5% (IFRS) | EUR 1.05bn |
| Arm Holdings | $5.46bn | 39.25x | 190.19x | 231.50x | 78.99x | 0.56% | FY03/2027: +24.0% ($6.10bn); FY03/2028: +37.3% ($8.38bn) | 17.0% | $3.12bn |
| Silvaco | $70.11m | 3.64x | n/a (negative EBITDA) | n/a (loss) | 32.83x | -10.24% | FY12/2026: +17.2% ($73.94m); FY12/2027: +9.2% ($80.75m) | -24.1% | $6.95m |
| Alten | EUR 4.12bn | 0.71x | 6.92x | 21.82x | 10.36x | 11.53% | FY12/2026: +3.5% (EUR 4.24bn); FY12/2027: +4.5% (EUR 4.43bn) | 7.8% | EUR 27.1m |
| EnSilica | GBP 27.81m | 3.16x | 22.94x | 53.74x | 45.21x | 6.48% | n/a (no consensus on source) | 10.5% | GBP 0.70m |
| UL Solutions | $3.19bn | 5.14x | 22.39x | 32.35x | 32.17x | 2.92% | FY12/2026: +7.2% ($3.27bn); FY12/2027: +9.3% ($3.58bn) | 19.0% | $82m |

Sources for Table 1b: [StockAnalysis statistics pages](https://stockanalysis.com/stocks/cdns/statistics/) and [forecast pages](https://stockanalysis.com/stocks/snps/forecast/) for each ticker, updated 12 Nov 2026 (EnSilica 11 Nov 2026); data from S&P Global Market Intelligence; forward P/E and EPS consensus "based on non-GAAP adjusted numbers" per the site [SECONDARY]. Siemens FY2026 figures (revenue EUR 83,372m, basic EPS EUR 10.94, EPS pre-PPA EUR 11.76, FCF all-in EUR 12,096m, EBITDA continuing operations EUR 15,326m, Industrial net debt EUR 4,782m) — [Siemens Earnings Release Q4 FY2026, 12 Nov 2026](https://assets.new.siemens.com/siemens/assets/api/uuid:11b1a70b-f540-45bb-824f-0b3fbb927e1b/dHQCOPR202611097494EN.pdf) [PRIMARY, figures as recorded in sibling note siemens_eda.md].

Notes and cross-checks against sibling notes:
- Synopsys: sibling note synopsys.md records the same StockAnalysis snapshot (price $462.12, market cap $88.56bn, EV $95.79bn, trailing P/E 81.94, forward P/E 26.26, EV/sales 10.17, EV/EBITDA 46.15, net debt $7.23bn); no difference.
- Cadence: sibling note cadence.md records price $329.26, market cap $90.34bn, EV $91.61bn, trailing P/E 65.47, forward P/E 34.94, EV/sales 14.94, EV/EBITDA 41.26, FCF yield 1.95%; no difference.
- Arteris, Arm, PTC, Dassault: sibling note specification_requirements_tools.md records the same StockAnalysis figures (Dassault at EUR 25.33, 12 Nov 12:50 CET); this note restates Dassault at the 11 Nov close EUR 25.34.
- Consensus vs company guidance: StockAnalysis/S&P consensus for Synopsys FY2027 revenue ($11.00bn) and EPS ($18.65) is below the company's own FY2027 guidance from its 30 Sep 2026 Investor Day (revenue $11.10-11.20bn; non-GAAP EPS $19.04-19.12) — [Synopsys Investor Day release, 30 Sep 2026](https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day) [PRIMARY]. Arteris consensus FY2026 revenue ($96.70m) is below company guidance of $98.5-99.5m given on 5 Nov 2026 — [Arteris Q3 2026 release, Form 8-K Ex. 99.1](https://www.sec.gov/Archives/edgar/data/0001667011/000162828026071063/exhibit991q3fy268-k.htm) [PRIMARY]. Either the aggregator consensus lags or some analysts sit below guidance; both figures are shown.
- PTC's price is bound by Schneider Electric's agreed $205-per-share cash offer (announced 5 Oct 2026; expected close Q3 2027); the stock rose 33.5% on 5 Oct 2026 [CALC from Nasdaq data] — [PTC/Schneider merger release, SEC exhibit](https://www.sec.gov/Archives/edgar/data/0000857005/000119312526413124/d174191dex991.htm) [PRIMARY]. PTC multiples therefore reflect the deal price, not a free market valuation.

### Inferences
- [CALC] Spread: Cadence's EV/sales premium over Synopsys (14.9x vs 10.2x) is wider than its forward P/E premium (34.9x vs 26.3x), consistent with Synopsys's lower GAAP margin and higher leverage after Ansys (net debt $7.2bn vs $1.3bn).
- Siemens's headline EV (EUR 258.6bn) includes Siemens Financial Services' financing debt; on Siemens's own "industrial net debt" (EUR 4.8bn), an industrial EV would be roughly EUR 218bn plus minority interests, so EV/sales on the industrial basis is nearer 2.6-2.7x [CALC; approximate, minorities not separately sourced].

### Gaps
- Siemens daily price series (YTD change; dates of the 52-week high and low) not obtained; StockAnalysis 52-week change used instead.
- EnSilica: no consensus estimates, no YTD change.
- Fiscal 2028 consensus is behind a paywall on StockAnalysis (see section 4 for other sources).

## 2. Multiples history: where today's multiples sit against each company's own past

### Takeaway
On five years of quarter-end data, Synopsys and Cadence both trade at or near the bottom of their own forward-P/E ranges (Synopsys 26.3x vs a 5-year median of 37.0x; Cadence 34.9x vs 43.8x, below every quarter-end in the window) and in the lower third of their EV/sales ranges; Dassault and PTC are also in the bottom quintile to quartile (PTC's price is now set by a cash bid); Arm sits mid-range of a short, very wide post-IPO range; Siemens and Keysight are at the top of theirs. A consistent 10-year series could not be obtained (two candidate sources refused access), so 10-year ranges are a gap.

### Cited Findings

Table 2. Five-year quarter-end multiples (20 fiscal quarter-ends, about Q4 2021 to Q3 2026, plus "current" at 11 Nov 2026 close; US$ and EUR as reported). Source: [StockAnalysis quarterly ratios pages](https://stockanalysis.com/stocks/snps/financials/ratios/?p=quarterly) for each ticker (S&P Global data; forward P/E is non-GAAP) [SECONDARY]; min, median, max and percentile rank computed by the researcher [CALC].

| Company, metric | Current (11 Nov 2026) | 5-yr min (quarter-end) | 5-yr median | 5-yr max (quarter-end) | Percentile of current within the 20 quarter-ends |
|---|---|---|---|---|---|
| Synopsys forward P/E | 26.26x | 24.49x (31 Jul 2026) | 37.00x | 45.34x (31 Oct 2021) | 5th (only one quarter-end lower) |
| Synopsys EV/sales | 10.17x | 8.64x (31 Oct 2022) | 12.21x | 17.67x (31 Jul 2025, Ansys debt in EV before Ansys revenue in TTM) | 15th |
| Synopsys trailing GAAP P/E | 81.94x | 32.81x (30 Apr 2025) | 57.41x | 119.56x (30 Apr 2026) | 95th (GAAP EPS depressed by Ansys amortisation and restructuring) |
| Synopsys EV/EBITDA | 46.15x | 32.89x (31 Oct 2022) | 48.87x | 83.31x (31 Jul 2025) | 40th |
| Cadence forward P/E | 34.94x | 35.09x (31 Mar 2026) | 43.77x | 54.88x (1 Jan 2022) | 0 (below every quarter-end) |
| Cadence EV/sales | 14.94x | 12.31x (31 Dec 2022) | 16.31x | 20.73x (31 Mar 2024) | 30th |
| Cadence trailing GAAP P/E | 65.47x | 51.91x (31 Dec 2022) | 71.30x | 90.22x (30 Sep 2025) | 25th |
| Cadence EV/EBITDA | 41.26x | 35.62x (Q2 2022, quarter ended early Jul 2022) | 47.87x | 62.63x (31 Mar 2024) | 25th |
| Arm forward P/E (13 quarter-ends since Sep 2023 IPO) | 78.99x | 54.91x (31 Mar 2025) | 78.15x | 162.42x (30 Jun 2026) | 54th |
| Arm EV/sales | 39.25x | 18.71x (30 Sep 2023) | 34.53x | 72.85x (30 Jun 2026) | 62nd |
| PTC forward P/E | 21.74x (deal-bound) | 14.78x (30 Jun 2026) | 26.93x | 36.37x (31 Mar 2024) | 25th |
| PTC EV/sales | 8.36x | 4.76x (30 Jun 2026) | 8.53x | 11.05x (31 Mar 2024) | 45th |
| Dassault forward P/E | 17.81x | 13.03x (31 Mar 2026) | 27.46x | 53.10x (31 Dec 2021) | 20th |
| Dassault EV/sales | 5.16x | 3.40x (30 Jun 2026) | 7.65x | 14.40x (31 Dec 2021) | 20th |
| Siemens trailing P/E | 27.92x (SA, 12 Nov) | 13.51x (30 Sep 2023) | 18.47x | 28.89x (31 Dec 2022) | 95th |
| Siemens forward P/E | 21.96x | 9.44x (30 Jun 2022) | 16.39x | 23.13x (30 Jun 2026) | 95th |
| Siemens EV/sales | 3.19x | 1.76x (30 Sep 2022) | 2.46x | 3.31x (30 Jun 2026) | 95th |
| Keysight forward P/E | 22.61x | 16.52x (31 Oct 2023) | 22.66x | 38.13x (30 Apr 2026) | 45th |
| Keysight EV/sales | 7.93x | 3.87x (31 Oct 2023) | 5.44x | 9.96x (30 Apr 2026) | 90th |

Supporting points:
- Annual fiscal-year-end forward P/E on the same source: Synopsys FY2021 45.34x, FY2022 31.66x, FY2023 38.14x, FY2024 36.44x, FY2025 35.09x; Cadence FY2021 54.88x, FY2022 37.24x, FY2023 48.22x, FY2024 44.38x, FY2025 40.58x; Siemens FY2021 20.08x, FY2022 9.45x, FY2023 12.26x, FY2024 16.66x, FY2025 20.11x — [StockAnalysis annual ratios](https://stockanalysis.com/stocks/cdns/financials/ratios/) [SECONDARY]. The free tier shows only five fiscal years, so it cannot supply a 10-year series.
- Third-party framing on the same theme: TIKR (page "last updated 18 Jul 2026") put Cadence at "NTM P/E of about 41 and NTM EV/EBITDA of about 30" at $330.11 and Synopsys "near 18x NTM EV/EBITDA" — [TIKR, Jul 2026](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026) [SECONDARY]. These NTM figures use a different earnings basis from Table 2 and are shown for comparison only.
- ts2.tech (17 Jul 2026) computed that at $382.98 Synopsys traded "near 25.9x" the midpoint of its then FY2026 adjusted EPS guidance ($14.72-14.80), versus 28.3x at the previous close — [ts2.tech, 17 Jul 2026](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/) [SECONDARY].
- Siemens P/E history: on the same source the 5-year trailing P/E median is 18.5x and the forward median 16.4x; the current 22x forward and 28x trailing (12 Nov intraday) are near the top of the range (Table 2). The FY2022 low (9.45x forward at 30 Sep 2022) coincides with the period of Siemens Energy-related losses [UNVERIFIED link; not checked in a filing].

### Inferences
- The de-rating of the two EDA leaders is mainly a multiple story, not an earnings story: both have raised guidance during 2026 (Synopsys FY2027 guide on 30 Sep 2026; Cadence FY2026 to about 21% growth on 26 Oct 2026), yet forward P/E is at or below the 5-year floor. This is consistent with the market discounting either slower long-run growth or higher perceived disruption risk (see sections 3 and 4).
- Siemens is the mirror image: its group multiples are at 5-year highs, so any "conglomerate discount" has narrowed rather than widened on these data (see section 4 for the debate).

### Gaps
- 10-year ranges and medians of forward P/E and EV/sales for Synopsys, Cadence, Arm (listed only since Sep 2023), PTC and Dassault: not obtained. Macrotrends and GuruFocus returned HTTP 403 on 12 Nov 2026, the StockAnalysis free tier stops at five fiscal years, and no search engine was available after the session's shared search budget was exhausted. Quarter-end sampling also understates intra-quarter extremes.

## 3. Drawdowns and price episodes (dates, causes, magnitudes)

### Takeaway
The EDA shares have had five distinct shocks since May 2025: the China EDA export-licence episode (about -10% in a day, reversed in July 2025), Synopsys's own results shock (-35.8% on 10 Sep 2025), the early-2026 software sell-off on AI-agent fears (Synopsys -15% and Cadence -11% from 27 Jan to 6 Feb 2026, with the worst day on 3 Feb 2026), the Kimi K3 open-tools chip demo (-7.9% and -9.5% on 17 Jul 2026), and the October to November 2026 AI-infrastructure sell-off, in which the chip index fell about 40% from its June peak while the EDA names fell much less. DeepMind's AlphaProof Code announcement (10 Nov 2026) moved both EDA shares only -1.5%.

### Cited Findings

Table 3. Episode-by-episode moves (closing prices; [CALC] from Nasdaq.com and Euronext daily data unless stated)

| Episode and date | Synopsys | Cadence | Benchmarks and peers | Cause as reported (source) |
|---|---|---|---|---|
| US EDA export licence requirement for China: 28 May 2025 | -9.6% (from $511.79 to $462.43); -11.1% over 28-29 May (to $454.99) | -10.7% (from $323.08 to $288.61); -11.9% over 28-29 May (to $284.50) | n/a | BIS imposed a licence requirement for EDA exports to China on 23 May 2025 and rescinded it on 2 Jul 2025 — [Cadence FY2025 Form 10-K, as recorded in cadence.md](https://s206.q4cdn.com/597110084/files/doc_downloads/2026/Mar/CDNS-FY-2025-Form-10-K.pdf) [PRIMARY] |
| Restriction lifted: 3 Jul 2025 | +4.9% (to $548.74) | +5.1% (to $326.81) | n/a | same source |
| Synopsys Q3 FY2025 results: 10 Sep 2025 | -35.8% (from $604.37 to $387.78) | -6.4% (to $338.53) | IGV +1.6% | Q3 FY2025 (released 9 Sep 2025): Design IP revenue $427.6m vs $463.1m a year earlier (about -7.7%); CEO: "our IP business underperformed expectations", "challenging geo-political backdrop"; CFO: "We are taking a more conservative view of Q4"; plan to "reallocate resources in our Design IP segment" — [Synopsys release, 9 Sep 2025](https://news.synopsys.com/2025-09-09-Synopsys-Posts-Financial-Results-for-Third-Quarter-Fiscal-Year-2025) [PRIMARY]. FY2025 10-K: "challenges with a major foundry customer negatively impacted our financial results for fiscal year 2025" — [Synopsys 10-K, as recorded in synopsys.md](https://www.sec.gov/Archives/edgar/data/883241/000088324125000028/snps-20251031.htm) [PRIMARY] |
| Early-2026 software sell-off ("SaaSpocalypse"): 29 Jan 2026 | -6.1% | -5.6% | IGV -4.9%; PTC -5.2%; Autodesk -4.7%; Dassault -4.3%; chip ETF SOXX +0.2% | Term "coined" by Jefferies traders; trigger: fear that "AI agents could make traditional software and per-seat pricing obsolete"; "For most of 2026, software stocks have been on the wrong side of the AI trade" — [MarketBeat, 10 Oct 2026](https://www.marketbeat.com/articles/schneider-just-paid-up-for-ptc-is-the-saaspocalypse-overdone/) [SECONDARY]. Specific trigger event on each date [UNVERIFIED] |
| Same: 3 Feb 2026 (worst EDA day of the episode) | -8.5% | -7.2% | IGV -4.6%; PTC -4.9%; Autodesk -5.8%; Alten -8.0%; SOXX -2.0% | as above |
| Same: 27 Jan to 6 Feb 2026, cumulative | -15.1% ($502.70 to $426.88) | -10.9% ($318.37 to $283.52) | IGV -15.7%; Autodesk -10.3%; Dassault -6.0%; PTC -5.4%; SOXX -0.7% | as above |
| Same, peak to trough early 2026 | -28.7% (12 Jan $533.42 to 27 Mar $380.47) | -18.8% (9 Jan $327.31 to 10 Apr $265.66) | IGV -29.7% (7 Jan to 10 Apr); Autodesk -26.2%; PTC -23.8%; Dassault -35.5% (9 Jan to 16 Feb) | as above; Dassault fell -20.8% on 11 Feb 2026 and -10.4% on 16 Feb 2026 (cause not verified; Dassault's 2026 growth objective stood at 3-5% until it was raised to 4-5% on 28 Oct 2026 — [Reuters, 28 Oct 2026](https://www.reuters.com/technology/dassault-systmes-raises-2026-growth-target-2026-10-28/) [SECONDARY]) |
| Synopsys Q2 FY2026 results: 28 May 2026 | -8.6% (the 52-week closing high, $534.56, was set two sessions earlier on 26 May) | -0.1% | IGV +2.8% | Q2 FY2026 released 27 May 2026 (Design IP $454m, -6% y/y) — see synopsys.md [PRIMARY]; reason for the reaction not separately sourced |
| Broad chip sell-off: 5 Jun 2026 | -6.0% | -8.6% | SOXX -10.4%; QQQ -4.8%; Arm -12.8% | cause [UNVERIFIED] (no search engine available) |
| Kimi K3 open-model chip demo: 17 Jul 2026 | -7.9% close ($417.03 to $384.27); intraday -8.17% at $382.98 | -9.5% close ($364.65 to $330.11); intraday -9.64% at $329.50 | IGV -1.0%; SOXX -1.6% (day); SMH -0.87% and QQQ -0.63% intraday per ts2.tech | Moonshot's Kimi K3 designed a chip in a 48-hour autonomous run with open-source EDA tools on the Nangate 45nm library, simulated only, 4 mm2, 100 MHz — [ts2.tech, 17 Jul 2026](https://ts2.tech/en/synopsys-nasdaqsnps-stock-sinks-as-kimi-chip-demo-tests-the-eda-moat/) [SECONDARY]; [Kimi blog, results "current as of July 16, 2026"](https://www.kimi.com/blog/kimi-k3) [PRIMARY, as recorded in cadence.md] |
| Kimi K3, following days (all vs the 16 Jul close) | -10.4% by 24 Jul ($373.47); -10.7% at the 30 Jul close ($372.33, post-event low); -6.7% at 27 Jul; +10.8% by 11 Nov | -10.5% by 24 Jul ($326.24, post-event low); -7.1% at 27 Jul; -9.7% by 11 Nov | SOXX -16.3% cumulative by 29 Jul (separate chip sell-off 28-29 Jul, cause [UNVERIFIED]) | Analysts: Bernstein's Robin Zhu said K3 showed Chinese labs could "keep pace with the US frontier" and that the immediate reaction "generally made sense" (ts2.tech, 17 Jul 2026, paraphrase plus quote); BNP Paribas told clients the reaction was overdone (TIKR, updated 18 Jul 2026, paraphrase) [SECONDARY]. Tech Fund (27 Jul 2026) said both shares were "down around 14%" since the news, a figure not reproduced by the closing data (-6.7% and -7.1% from 16 Jul to 27 Jul; at most about -10.5% at the late-July lows; about -12% from the 15 Jul close to 24 Jul) [SECONDARY; difference noted] |
| Synopsys Q3 FY2026 results: 27 Aug 2026 | +13.4% | +3.8% | IGV +7.7% | Q3 FY2026 released 26 Aug 2026 (synopsys.md) [PRIMARY] |
| Synopsys Investor Day: 1 Oct 2026 | +12.8% | +6.2% | IGV +1.6% | FY2027 guidance above consensus (revenue $11.1-11.2bn vs consensus $10.8bn; EPS $19.04-19.12 vs $17.69, per TheFly 30 Sep 2026), OpenAI and Amazon agreements — [Reuters, 1 Oct 2026](https://www.reuters.com/business/synopsys-shares-jump-robust-growth-outlook-openai-aws-deals-2026-10-01/) ; [TipRanks/TheFly, 30 Sep 2026](https://www.tipranks.com/news/the-fly/synopsys-sees-fy27-adjusted-eps-19-04-19-12-consensus-17-69-thefly-news) [SECONDARY] |
| Chip sell-off: 22 Oct 2026 | -6.4% | -5.0% | SOXX -6.8%; Keysight -8.7%; Arm -7.3%; Arteris -8.8% | cause [UNVERIFIED] |
| Cadence Q3 2026 results: 27 Oct 2026 | +4.4% | +6.5% (to $343.08) | SOXX +3.9% | Q3 revenue +22%, record backlog $8.2bn, FY2026 guide raised to about 21% growth (cadence.md, [PRIMARY]); price-target raises 27 Oct 2026: JPMorgan (Harlan Sur) $420 from $405, Needham (Charles Shi) $430 from $400, Baird $440 from $420, Rosenblatt $425 from $420 — [TipRanks/TheFly, 27 Oct 2026](https://www.tipranks.com/news/the-fly/cadence-design-price-target-raised-to-420-from-405-at-jpmorgan-thefly-news) [SECONDARY] |
| Chip sell-off: 30 Oct 2026 | -4.6% | -4.3% | SOXX -8.2%; QQQ -3.5%; Arm -10.0%; Keysight -6.9% | cause [UNVERIFIED]; came after Meta's 21 Oct results and during the late-October hyperscaler results season |
| Post-midterm AI sell-off: 5 Nov 2026 | -4.9% | -5.5% | SOXX -12.1%; QQQ -6.5%; Arm -13.1% (also its own royalty miss); Keysight -8.8%; IGV -4.4% | Democrats swept Congress on 3 Nov; on 5 Nov "major indexes had their worst day since April 2025" and the Magnificent Seven lost over $1 trillion, on "fears of a slowdown in the data center build-out" after candidates favouring data-centre regulation won in states such as Texas, and concern the AI trade may be past its peak — [CNBC, 6 Nov 2026](https://www.cnbc.com/2026/11/06/tech-executives-ai-data-center-selloff-midterms.html) [SECONDARY]. Arm: "weaker-than-expected smartphone-related royalty revenue" — [Invezz, 5 Nov 2026](https://invezz.com/news/2026/11/05/arm-stock-falls-12-as-weak-smartphone-royalties-offset-ai-data-centre-growth/) [SECONDARY] |
| Rebound 5 to 11 Nov 2026 | +5.0% | +5.7% | SOXX +17.8%; Arm +22.0%; Keysight +17.3%; IGV +3.3% | n/a |
| AlphaProof Code (Google DeepMind): 10 Nov 2026 | -1.5% (to $459.95); +0.5% on 11 Nov | -1.5% (to $331.64); -0.7% on 11 Nov | IGV -1.1%; SOXX -0.1% | AlphaProof Code announced 10 Nov 2026 (software verification of libsignal in Lean) — see model_makers_hyperscalers.md [PRIMARY]; no press attribution of EDA moves to it was found [UNVERIFIED] |

Longer swings (closing basis) [CALC]:
- Synopsys: -31.2% from 26 May 2026 ($534.56) to 15 Sep 2026 ($367.70, the 52-week closing low); -23.5% from 9 Sep 2025 ($604.37, the close before the results shock) to 11 Nov 2026.
- Cadence: -34.2% from 2 Jun 2026 ($416.39) to 15 Sep 2026 ($273.96).
- Chip ETF SOXX: -39.6% from 22 Jun 2026 ($218.34) to 5 Nov 2026 ($131.90); over the same dates Synopsys -5.2%, Cadence -19.9%, software ETF IGV +13.4%, Keysight -30.2%, Arm -59.1%, Arteris -64.2%.
- Arm: -62.1% from 18 Jun 2026 ($439.46) to 5 Nov 2026 ($166.72). Arteris: -67.2% from 30 Jun 2026 to 5 Nov 2026. Silvaco: -57.8% from 30 Jun 2026 to 4 Nov 2026.
- Other large single-day moves since May 2025: Synopsys -9.4% and Cadence -6.2% on 10 Oct 2025; Synopsys -6.6% on 4 Nov 2025; Cadence -7.6% on 1 Sep 2026; Arteris -24.0% on 6 Aug 2025 and -20.0% on 2 Jul 2026; PTC -12.4% on 11 Jun 2026 and +33.5% on 5 Oct 2026 (Schneider bid); Keysight +23.1% on 24 Feb 2026; UL Solutions -14.0% on 4 Aug 2026. Causes not verified unless stated elsewhere in these notes.

### Inferences
- EDA shares have behaved as software in software sell-offs (January to April 2026: Synopsys and Cadence fell broadly in line with IGV) and as semiconductors only partly in chip sell-offs (June to November 2026: Cadence fell about half as much as SOXX, Synopsys barely moved net). The specific "AI makes EDA obsolete" fear has so far produced one-day falls of 8-10% (17 Jul 2026) rather than a lasting re-rating relative to the chip sector.
- The 5 November 2026 episode is the first of these in which the stated cause is policy risk to data-centre construction rather than AI disruption of software; it hit chip and AI-infrastructure names hardest and EDA names moderately.

### Gaps
- Causes of the chip sell-offs on 5 Jun, 28-29 Jul, 22 Oct and 30 Oct 2026, and of the moves on 10 Oct 2025 and 1 Sep 2026: not verified (no search engine available after the shared search budget was exhausted; Firecrawl and Exa had no credits).
- The precise trigger of the 29 Jan and 3 Feb 2026 software sell-off days could not be sourced beyond MarketBeat's general description.
- No analyst note was found that attributes any EDA price move to AlphaProof Code.

## 4. What the price assumes (consensus, guidance, implied growth and the 2026 sell-side debate)

### Takeaway
At 11 Nov 2026 prices, consensus has Synopsys growing revenue about 13% and EPS about 23% in FY2027 (below its own guidance) and Cadence about 14% and 17% in FY2027; a simple reverse-DCF puts the free-cash-flow growth the market needs at roughly 12-15% a year for ten years for Synopsys and 18-20% for Cadence, against about 34-37% for Arm and only 4-6% for Dassault. The 2026 sell-side debate has centred on whether AI agents shrink seat counts; on the evidence of the calls, management and most covering analysts frame agents as extra paid consumption on top of subscriptions, while the market has periodically priced the opposite risk.

### Cited Findings

Table 4a. Consensus and company targets (StockAnalysis/S&P Global consensus, pages updated 12 Nov 2026 [SECONDARY]; company figures [PRIMARY] as cited)

| Company | Consensus revenue (growth) | Consensus non-GAAP EPS (growth) | Fiscal 2028 consensus | Company guidance or targets |
|---|---|---|---|---|
| Synopsys (FY ends Oct) | FY26 $9.72bn (+37.8%, Ansys full year); FY27 $11.00bn (+13.2%) | FY26 $15.14 (+17.3%); FY27 $18.65 (+23.2%) | n/a (paywalled) | FY26 guide $9.69-9.74bn, EPS $15.04-15.10 (26 Aug 2026); FY27 guide $11.10-11.20bn, EPS $19.04-19.12, FCF about $3.1bn; FY26-FY30 revenue CAGR about 15%, non-GAAP operating margin about 50% by FY30, EPS and FCF CAGR mid-20s% (30 Sep 2026) — [Investor Day release](https://news.synopsys.com/2026-09-30-Synopsys-Details-Growth-Strategy-and-Long-term-Financial-Model-at-2026-Investor-Day); pre-Investor-Day consensus was FY27 revenue $10.8bn and EPS $17.69 — [TheFly via TipRanks, 30 Sep 2026](https://www.tipranks.com/news/the-fly/synopsys-sees-fy27-adjusted-eps-19-04-19-12-consensus-17-69-thefly-news) [SECONDARY] |
| Cadence (FY ends Dec) | FY26 $6.41bn (+21.0%); FY27 $7.33bn (+14.4%) | FY26 $8.42 (+18.0%); FY27 $9.85 (+16.9%) | n/a (paywalled) | FY26 guide raised to $6.387-6.417bn and EPS $8.37-8.43 (26 Oct 2026, cadence.md) from an initial $5.9-6.0bn and $8.05-8.15 on 17 Feb 2026 (which excluded the pending Hexagon D&E deal) — [Motley Fool transcript, 17 Feb 2026](https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/) [SECONDARY transcript] |
| Arm (FY ends Mar) | FY27 $6.10bn (+24.0%); FY28 $8.38bn (+37.3%) | FY27 $2.27 (+28.1%); FY28 $3.07 (+35.6%) | FY29 n/a | Q2 FYE27 (4 Nov 2026): revenue $1.44bn (+27%), licence $773m (+50%), royalty $670m (specification_requirements_tools.md [PRIMARY]); StockAnalysis's call summary says supply commitments "lifted the FY2027-FY2028 revenue outlook to up to $2 billion" [SECONDARY; meaning unclear, not verified in the transcript] |
| PTC (FY ends Sep) | FY27 $2.90bn (+6.2%); FY28 $3.14bn (+8.1%) | FY27 $9.02 (+9.5%); FY28 $10.02 (+11.1%) | (FY28 shown) | Guidance suspended pending the Schneider deal; $205 cash offer vs $196.14 close = 4.5% gross spread [CALC]; close expected Q3 2027 — [SEC exhibit, 5 Oct 2026](https://www.sec.gov/Archives/edgar/data/0000857005/000119312526413124/d174191dex991.htm) [PRIMARY] |
| Dassault (FY ends Dec) | FY26 EUR 6.45bn (+3.4%); FY27 EUR 6.93bn (+7.5%, includes ArisGlobal) | FY26 EUR 1.35 (+3.3%); FY27 EUR 1.45 (+6.9%) | n/a | FY26 objective raised to 4-5% growth from 3-5% on 28 Oct 2026 — [Reuters, 28 Oct 2026](https://www.reuters.com/technology/dassault-systmes-raises-2026-growth-target-2026-10-28/) [SECONDARY]; analyst targets after Q3: Jefferies EUR 19 (Underperform, 28 Oct), Citi EUR 23.50 (Neutral) and JPMorgan EUR 23 (Neutral, 29 Oct) — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/dassault-systemes-price-target-raised-to-eur-19-from-eur-16-at-jefferies-thefly-news) [SECONDARY]; consensus "Hold", mean target EUR 24.88 (21 analysts) |
| Arteris (FY ends Dec) | FY26 $96.70m (+37.0%); FY27 $117.03m (+21.0%) | FY26 -$0.15 | n/a | FY26 revenue guide raised to $98.5-99.5m on 5 Nov 2026 (from $95-98m); after the "beat and raise", Oppenheimer cut its target to $30 from $40 (Outperform) and Jefferies (Kevin Garrigan) to $40 from $50 (Buy), 6 Nov 2026 — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/arteris-price-target-lowered-to-40-from-50-at-jefferies-thefly-news) [SECONDARY] |
| Siemens (FY ends Sep) | FY27 EUR 90.66bn (+9.0%) | FY27 EUR 13.02 | n/a | FY27 guidance (12 Nov 2026, excluding Healthineers): comparable revenue +9-11%, EPS pre-PPA EUR 10.20-10.80; Digital Industries margin 20-22% on +8-12% growth; mid-term comparable growth target raised to 7-11% from 6-9% — [MarketBeat call summary, 12 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-what-siemens-aktiengesellschaft-sie-said-on-its-q4-earnings-call-2026-11-12/) [SECONDARY]. The aggregator consensus EPS (EUR 13.02) and the guided ex-Healthineers EPS (EUR 10.20-10.80) are on different bases and should not be compared directly |
| Keysight (FY ends Oct) | FY26 $7.12bn (+32.4%); FY27 $8.21bn (+15.4%) | FY26 $11.47; FY27 $13.93 (+21.4%) | n/a | Q4 FY26 results due 19 Nov 2026; on 2 Nov 2026 the company said it was "not updating its previously provided outlook" and demand "remains strong" — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/keysight-technologies-says-end-markets-remains-strong-thefly-news) [SECONDARY] |
| Silvaco | FY26 $73.94m (+17.2%); FY27 $80.75m (+9.2%) | FY27 $0.20 | n/a | 4 Nov 2026: FY26 revenue growth about 17% and "similar mid-to-high teens revenue growth in 2027" — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/silvaco-sees-fy26-revenue-up-17-thefly-news) [SECONDARY]; consensus FY27 (+9.2%) sits well below that |
| UL Solutions | FY26 $3.27bn (+7.2%); FY27 $3.58bn (+9.3%) | FY26 $2.31; FY27 $2.65 | n/a | n/a |
| Alten | FY26 EUR 4.24bn (+3.5%); FY27 EUR 4.43bn (+4.5%) | FY26 EUR 8.04; FY27 EUR 8.75 | n/a | H1 2026: FY26 guidance raised to 1.7-1.9% organic growth and 9.2% operating margin (StockAnalysis transcript summary, 25 Sep 2026) [SECONDARY] |
| EnSilica | n/a | n/a | n/a | n/a (FY ends May; annual report published 13 Oct 2026 per StockAnalysis filings list) |

Table 4b. Growth implied by the price [CALC; illustrative arithmetic by the researcher, not a forecast]. Method: the constant 10-year free-cash-flow growth rate that, followed by 3% perpetual growth, makes the discounted cash flows equal today's EV, starting from TTM FCF (StockAnalysis); discount rates of 9% and 10% applied to all companies for comparability (StockAnalysis's own WACC estimates are 10.1% for Synopsys and Cadence, 6.9% for Dassault, 9.9% for Siemens). Also shown: the single-stage (Gordon) perpetual growth rate.

| Company | EV | TTM FCF | FCF/EV | Perpetual growth implied at 9% / 10% | 10-year FCF CAGR implied (then 3%) at 9% / 10% |
|---|---|---|---|---|---|
| Synopsys | $95.79bn | $2.75bn (FY27 guide about $3.1bn) | 2.9% | 6.0% / 6.9% | 12.3% / 14.6% |
| Cadence | $91.61bn | $1.76bn | 1.9% | 6.9% / 7.9% | 17.6% / 20.1% |
| Arm | $214.47bn | $1.21bn | 0.6% | 8.4% / 9.4% | 34.4% / 37.4% |
| Keysight | $52.19bn | $1.47bn | 2.8% | 6.0% / 7.0% | 12.5% / 14.9% |
| UL Solutions | $16.39bn | $0.48bn | 2.9% | 5.9% / 6.9% | 12.0% / 14.3% |
| Siemens (group EV) | EUR 258.6bn | EUR 12.10bn (FY26) | 4.7% | 4.1% / 5.1% | 5.9% / 8.0% |
| Dassault | EUR 32.5bn | EUR 1.72bn | 5.3% | 3.5% / 4.5% | 4.3% / 6.4% |
| EnSilica | GBP 87.9m | GBP 5.7m | 6.5% | 2.3% / 3.3% | 1.5% / 3.5% |
| Alten | EUR 2.92bn | EUR 0.34bn | 11.7% | negative | negative (-6.3% / -4.5%) |
| Arteris, Silvaco | n/m | FCF near zero or negative | n/m | n/m | n/m |

The 2026 sell-side debate on AI agents and seat-based licences (attributed, dated):
- Bear framing: "SaaSpocalypse", a term coined by Jefferies traders, for fears that "AI agents could make traditional software and per-seat pricing obsolete" — [MarketBeat, 10 Oct 2026](https://www.marketbeat.com/articles/schneider-just-paid-up-for-ptc-is-the-saaspocalypse-overdone/) [SECONDARY]. On the Kimi K3 demo, Bernstein's Robin Zhu said Chinese labs could "keep pace with the US frontier" and that the immediate reaction "generally made sense" (ts2.tech, 17 Jul 2026) [SECONDARY].
- The question put to Cadence on 17 Feb 2026: Vivek Arya (BofA) asked whether customers use AI or internal tools to reduce demand for EDA; CEO Anirudh Devgan: "we have seen absolutely no discussion with customers of reducing the usage"; to Jim Schneider (Goldman Sachs) on monetisation: "We will price it as like a virtual engineer or agent" and seat count is "a misnomer ... We are exploration limited"; CFO John Wall to Lee Simpson (Morgan Stanley): "we don't see AI forcing a wholesale change from subscriptions to consumption" and "we'll attach more usage-based pricing for incremental capacity and AI-driven optimization"; to Jay Vleeschhouwer (Griffin Securities) on contract length: "we are not seeing any change in the duration" — [Motley Fool transcript, 17 Feb 2026](https://www.fool.com/earnings/call-transcripts/2026/02/17/cadence-cdns-q4-2025-earnings-transcript/) [SECONDARY transcript of PRIMARY statements].
- Later Cadence statements (27 Apr and 26 Oct 2026): agentic products "priced as a subscription plus consumption model"; agentic AI "doesn't replace the core EDA engines. It calls them more often"; "greater customer usage should create greater value for Cadence" (quotes recorded in cadence.md from Motley Fool and Webull transcripts).
- Synopsys: "subscription plus consumption for the agents" (27 May 2026); pricing to include "subscription of our agents, subscription of our workflow as well as a consumption measure", and Ghazi "not worried at all" about end-to-end AI design bypassing Synopsys (26 Aug 2026); monetisation "through subscription and consumption-based models across tools, agents, and its platform", GPT-Synopsys revenue sharing with OpenAI and a licence-plus-royalty model with Amazon (30 Sep 2026) (all recorded in synopsys.md with primary links).
- Siemens CFO (12 Nov 2026): "we will introduce an agentic surcharge on really this underlying software subscription"; "other credit-based, user-based monetization will follow" (Investing.com transcript, recorded in siemens_eda.md) [SECONDARY].
- Bull sizing: Goldman Sachs (report cited by Tech Fund, 27 Jul 2026) put the agentic-AI opportunity for EDA at about $3.7bn a year by 2030, estimated a shortage of about 72,000 chip designers by 2030 and about 48,000 "agentic engineer-equivalents", modelled Cadence growth moving from about 13% to the mid-20s% and Synopsys to about 20%, with about +$2.30 and +$2.20 of EPS by 2030, and argued that consensus reflects a "pre-AI" industry — [Tech Fund, 27 Jul 2026](https://www.techinvestments.io/p/the-eda-crash-and-the-massive-ai) [SECONDARY; Goldman report not seen].
- Third-party valuation framing: TIKR's mid case for Cadence (July 2026) assumed about 10% annual revenue growth and net margin expanding toward the high 30s, giving about $600 by end-2030 (about 14% a year from $330.11) — [TIKR](https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026) [SECONDARY; model, not consensus].
- Analyst price targets (attributed, not endorsed): Synopsys mean $589.55 (25 analysts; low $475, median $600, high $700), with Morgan Stanley (Lee Simpson) $574 (20 Oct 2026), Needham (Charles Shi) $620 (12 Oct 2026), BofA (Vivek Arya) $600 and Deutsche Bank $640 (1 Oct 2026) — [StockAnalysis forecast, 12 Nov 2026](https://stockanalysis.com/stocks/snps/forecast/) [SECONDARY]; Cadence mean $411.76 (24 analysts; low $300, median $420, high $470) — StockAnalysis, recorded in cadence.md (9 Nov 2026) [SECONDARY].

Siemens and the conglomerate-discount question:
- Siemens's group multiples are at 5-year highs (Table 2: forward P/E and EV/sales at the 95th percentile of their own 5-year quarter-end ranges).
- Structural simplification under way: transfer of a 34.1% Siemens Healthineers stake to Siemens shareholders (one Healthineers share for every two Siemens shares), expected in late spring 2027, with Healthineers reported as discontinued from Q1 FY2027 — [MarketBeat call summary, 12 Nov 2026](https://www.marketbeat.com/instant-alerts/transcript-what-siemens-aktiengesellschaft-sie-said-on-its-q4-earnings-call-2026-11-12/) [SECONDARY]. Jefferies downgraded Siemens to Hold on 15 Oct 2026 (target EUR 300 from EUR 277) while raising Industrial EBITA estimates by 3-6% — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/siemens-downgraded-to-hold-from-buy-at-jefferies-thefly-news) [SECONDARY].
- No dated analyst estimate of the size of a conglomerate discount or a sum-of-the-parts value was found (see Gaps).

### Inferences
- For Synopsys, the market price embeds less than the company's own plan: about 12-15% FCF growth for a decade at 9-10% discount rates, versus guidance for FCF and EPS growth in the mid-20s% to FY2030. For Cadence, the requirement (about 18-20%) is closer to the consensus EPS path (about 17%) and to its 2026 growth, so it has less room for disappointment on this crude measure.
- Arm's price requires roughly 35% a year FCF growth for ten years; Dassault, Siemens and EnSilica require mid-single-digit growth; Alten's price implies declining FCF. These spreads, not business quality, define how much good news each entry price already carries.
- The consensus figures for Synopsys (FY27) and Silvaco (FY27) sit below the companies' own outlooks, which suggests either lagging estimates or analyst scepticism; either way the guidance is the more demanding benchmark for the December and February reports.

### Gaps
- Fiscal 2028 consensus for Synopsys, Cadence, Dassault and Arteris (and FY2029 for Arm) was not accessible (StockAnalysis paywall; no search engine available to find another source).
- No sell-side note that publishes an explicit "implied growth" figure for either EDA company was found; Table 4b is the researcher's arithmetic.
- No quantified estimate of a Siemens conglomerate discount was found.

## 5. Sector cycle as of November 2026, and scheduled events

### Takeaway
The chip cycle is at an extreme, memory-led high (WSTS spring forecast +90% for 2026; SIA September sales +146.8% year on year) and AI capital spending is still accelerating (Meta 2026 capex $135-145bn; Microsoft's quarterly additions to property and equipment roughly doubled), but share prices have started to discount a pause: the chip ETF fell about 40% from June to 5 November on data-centre policy and AI-trade-peak worries. EDA demand indicators remain firm (record Cadence backlog, Synopsys backlog near $11bn, Siemens EDA-led software growth), and the near-term calendar is dense: Synopsys on 8 Dec 2026, the 10 Jan 2027 US-China export-rule deadline, and Cadence's 2027 guidance in February 2027.

### Cited Findings
Semiconductor market and design-spend indicators:
- WSTS Spring 2026 forecast: 2026 market +90% to USD 1.51 trillion; memory about +250% to more than USD 800bn; logic +37%; 2027 +27% to about USD 1.9 trillion (memory +32%, logic +27%); Americas +112% in 2026 — [WSTS, Spring 2026 release](https://www.wsts.org/76/Recent-News-Release) [PRIMARY industry body; the next forecast is due in November per the site].
- SIA, 3 Nov 2026: Q3 2026 global sales $517.7bn, +24.1% on Q2; September 2026 $172.6bn, +146.8% year on year and +7.9% month on month — [SIA](https://www.semiconductors.org/global-semiconductor-sales-increase-24-1-from-q2-2026-to-q3-2026/) [PRIMARY industry body]. SIA, 5 Oct 2026: August $159.7bn, +144.3% year on year; year-to-date sales passed $1 trillion through August — [SIA](https://www.semiconductors.org/year-to-date-global-semiconductor-sales-top-1-trillion-through-august/) [PRIMARY].
- Early signs of strain in memory end-demand: TrendForce, 11 Nov 2026, "Mounting Finished-Goods Inventories Prompt Some PC OEMs to Adjust Memory Procurement Plans for 2027" (notebook shipments expected to decline from 3Q26); 6 Nov 2026 on "persistently high DRAM prices" — [TrendForce press centre](https://www.trendforce.com/presscenter/news/20261111-13303.html) [SECONDARY].
- Semiconductor R&D spending growth across the industry: no 2026 figure found (see Gaps). Design-tool demand proxies: Cadence 2026 revenue guided about +21%; Synopsys EDA growth 8.5% in Q3 FY2026; Siemens Digital Industries software revenue EUR 7.2bn in FY2026 (+13% comparable), "led by the EDA business" (siemens_eda.md, [PRIMARY]).

AI capital spending and financing:
- Meta (21 Oct 2026): Q3 capex $34.91bn; 2026 capex outlook $135-145bn ("narrowed from our prior outlook of $130-145 billion"); for 2027 it is "still developing our budget and capacity plans" and expects to keep "investing aggressively"; nine-month long-term debt issuance $24.91bn; $1.04bn distribution from a data-centre venture in Q3 — [Meta Q3 2026 release](https://investor.atmeta.com/investor-news/press-release-details/2026/Meta-Reports-Third-Quarter-2026-Results/default.aspx) [PRIMARY].
- Microsoft (28 Oct 2026): Q1 FY2027 additions to property and equipment $39.37bn vs $19.39bn a year earlier; Azure revenue +48%; capex guidance given only on the call (not obtained) — [Microsoft FY27 Q1 release](https://www.microsoft.com/en-us/investor/earnings/fy-2027-q1/press-release-webcast) [PRIMARY].
- TrendForce (3 Aug 2026): capex of nine large cloud providers about +90% to more than US$886.7bn in 2026 and about US$1.3tn in 2027; AI server shipments about +31% in 2026 — [TrendForce, 3 Aug 2026](https://www.trendforce.com/presscenter/news/20260803-13161.html) [SECONDARY, as recorded in market_structure_emulation_vip.md]. TrendForce (2 Nov 2026): AI networking and interconnect market US$279.8bn in 2027 — [TrendForce](https://www.trendforce.com/presscenter/news/20261102-13291.html) [SECONDARY].
- Signs of a possible pause: post-midterm sell-off on 5 Nov 2026 on "fears of a slowdown in the data center build-out" after candidates favouring data-centre regulation won; OpenAI's CFO said OpenAI would keep investing in data centres and "continue to raise capital"; Arm's CEO called the reaction "very, very short term thinking" — [CNBC, 6 Nov 2026](https://www.cnbc.com/2026/11/06/tech-executives-ai-data-center-selloff-midterms.html) [SECONDARY]. Siemens's CEO told CNBC on 12 Nov 2026 that data-centre expansion is "set to continue" (video headline only) — [CNBC, 12 Nov 2026](https://www.cnbc.com/video/2026/11/12/data-centre-expansion-set-to-continue-siemens-ceo.html) [SECONDARY]. A 9 Nov 2026 Invezz headline refers to "Arm Holdings, Intel, OpenAI woes" pulling SoftBank shares down 61% from their high (page refused access; content not verified) [UNVERIFIED].
- Hyperscaler 2027 capex guidance from Alphabet, Amazon and Oracle, and credit-market indicators (spreads on AI data-centre debt, private-credit terms): not obtained (see Gaps).

EDA backlog, China and policy:
- Synopsys backlog: $8.1bn (31 Oct 2024) to $11.4bn (31 Oct 2025, incl. $2.0bn non-cancellable FSA commitments), about $11bn (Q2 FY2026) and $10.9bn (Q3 FY2026) (synopsys.md; 10-K [PRIMARY], Q3 figure via TIKR [SECONDARY]).
- Cadence backlog: $7.8bn (end-2025) to a record $8.2bn (30 Sep 2026); next-12-month RPO $3.8bn to $4.2bn; about 64% of FY2026 revenue from beginning backlog (cadence.md [PRIMARY]).
- Siemens Digital Industries backlog EUR 11.0bn, of which EUR 7.3bn software (FY2026); "Fiscal 2027 is a strong renewal year for our EDA business, with the sales funnel again concentrated in Q4" (siemens_eda.md [PRIMARY]). Arteris RPO $135.5m (+29%) (specification_requirements_tools.md [PRIMARY]).
- China: Synopsys China revenue $814.3m (12%) in FY2025 vs $989.5m (16%) in FY2024; Cadence China 13% of FY2025 revenue and 16% in Q3 2026 (china.md, [PRIMARY]). Nikkei Asia (via TheFly, 12 Oct 2026) reported that Synopsys is exploring partnerships with Chinese AI labs on AI chip-design tools — [TipRanks/TheFly](https://www.tipranks.com/news/the-fly/synopsys-seeks-to-work-with-chinese-ai-labs-to-speed-up-chip-design-nikkei-says-thefly-news) [SECONDARY].
- Export controls: BIS extended the suspension of its Affiliates (50%) Rule, due to lapse on 9 Nov 2026, to 10 Jan 2027, alongside the extension of the US-China arrangement to 10 Jan 2027; law-firm alerts warn that the rule and China's rare-earth controls could both take effect in January 2027 absent a permanent deal (law-firm summaries recorded in cadence.md, synopsys.md and china.md, e.g. [Thompson Hine, Nov 2026](https://www.thompsonhinesmartrade.com/2026/11/bis-extends-affiliates-rule-until-january-2027/)) [SECONDARY].

Table 5. Scheduled events, 12 Nov 2026 to about 12 Feb 2027 (and just beyond)

| Date | Event | Source |
|---|---|---|
| 19 Nov 2026 | Keysight Q4 and FY2026 results | [Business Wire, 29 Oct 2026](https://www.businesswire.com/news/home/20261029502167/en/Keysight-Technologies-to-Report-Fourth-Quarter-and-Fiscal-Year-2026-Results-on-) [PRIMARY] |
| 8 Dec 2026 (after close) | Synopsys Q4 and FY2026 results; first update to FY2027 guidance ($11.10-11.20bn revenue, EPS $19.04-19.12) | [PR Newswire, 5 Nov 2026](https://www.prnewswire.com/news-releases/synopsys-announces-earnings-release-date-for-fourth-quarter-and-fiscal-year-2026-302931192.html) [PRIMARY] |
| By about early 2027 | Completion of Synopsys's $1bn accelerated share repurchase with JPMorgan (started 5 Oct 2026; end date not given in the headline) | [PR Newswire, 5 Oct 2026](https://www.prnewswire.com/news-releases/synopsys-initiates-1-billion-accelerated-share-repurchase) [PRIMARY; end date n/a] |
| 10 Jan 2027 | Expiry of the extended BIS Affiliates-rule suspension and of the extended US-China arrangement, unless renewed | law-firm summaries (section 5) [SECONDARY] |
| February 2027 (date not yet announced) | Cadence Q4 2026 results and 2027 guidance (the FY2025 report came on 17 Feb 2026) | cadence.md [PRIMARY for the 2026 date] |
| February 2027 (dates n/a) | Arm Q3 FYE27; Siemens Q1 FY2027 (first quarter with Healthineers as discontinued); Dassault FY2026 results; Arteris, Silvaco and UL Solutions Q4 2026 | not announced [UNVERIFIED dates] |
| 23 Feb 2027 | Alten FY2026 results | [StockAnalysis EPA:ATE overview](https://stockanalysis.com/quote/epa/ATE/) [SECONDARY] |
| Pending (no date) | Arm v. Qualcomm remedy ruling after the 13 Oct 2026 verdict | specification_requirements_tools.md [SECONDARY] |
| Late spring 2027 | Siemens Healthineers stake transfer to Siemens shareholders | MarketBeat, 12 Nov 2026 [SECONDARY] |
| Q3 2027 | Expected close of Schneider Electric's acquisition of PTC (vote and approvals pending) | SEC exhibit, 5 Oct 2026 [PRIMARY] |

### Inferences
- The cycle evidence points two ways. Semiconductor revenue (and so customers' ability to fund design and verification) is at a record, which historically supports EDA bookings with a lag; but the June-November share-price action, the post-midterm sell-off and early memory-inventory signals suggest markets are pricing a slowdown in AI-infrastructure spending in 2027. EDA revenue is mostly recurring and backlog-backed (Cadence about 64% of 2026 revenue from opening backlog), so a capex pause would likely show first in bookings, hardware-emulation orders and IP rather than in reported revenue.
- With Meta's 2027 budget not yet set and Microsoft's capex roughly doubling, the February 2027 reporting season (Cadence's 2027 guide, hyperscaler 2027 capex plans) is the main near-term test of the "pause" thesis.

### Gaps
- Industry-wide semiconductor R&D spending growth for 2026 (for example from SIA, TechInsights or company aggregates): not found.
- Alphabet, Amazon and Oracle 2027 capex guidance, Microsoft's call commentary, and credit-market indicators for AI data-centre financing (bond spreads, private-credit terms, any failed financings): not obtained because no search engine was available.
- Exact dates for Cadence's, Arm's, Siemens's and Dassault's February 2027 reports were not yet published or not found.

## 6. Data gaps, unverified items, and sources (dated)

### Takeaway
The cross-company table is complete for all 12 companies on one data source and one price date; the main gaps are 10-year multiple histories, fiscal 2028 consensus, the causes of several 2026 chip sell-off days, hyperscaler 2027 capex beyond Meta and Microsoft, and AI-financing credit signals. Research conditions: the session's shared WebSearch budget (200 calls, all agents) was already used up and Firecrawl and Exa had no credits, so all evidence after the first data pulls came from direct fetches of known pages and sibling notes.

### Cited Findings
Could not verify or find:
- 10-year ranges and medians of forward P/E and EV/sales (all companies); macrotrends and GuruFocus returned HTTP 403 on 12 Nov 2026.
- Fiscal 2028 consensus for Synopsys, Cadence, Dassault, Arteris; FY2029 for Arm.
- Siemens daily price series (YTD change and dates of the 52-week high and low); EnSilica YTD change and consensus.
- Causes of the moves on 10 Oct 2025, 5 Jun 2026, 28-29 Jul 2026, 1 Sep 2026, 22 Oct 2026 and 30 Oct 2026; the specific triggers of the 29 Jan and 3 Feb 2026 software sell-off days; Dassault's 11 and 16 Feb 2026 falls.
- Any analyst attribution of EDA share moves to AlphaProof Code (10 Nov 2026).
- Hyperscaler 2027 capex guidance other than Meta's "still developing" statement; credit-market signals for AI data-centre financing; industry semiconductor R&D growth.
- A quantified Siemens conglomerate discount or sum-of-the-parts estimate.
- The meaning of StockAnalysis's summary that Arm "lifted the FY2027-FY2028 revenue outlook to up to $2 billion".
- No company was dropped from the main table.

Sources (all accessed 12 Nov 2026; publication dates as shown):
- StockAnalysis.com statistics, overview, forecast and ratio pages for SNPS, CDNS, AIP, KEYS, PTC, ARM, SVCO, ULS, ETR:SIE, EPA:DSY, EPA:ATE, AIM:ENSI (updated 12 Nov 2026; EnSilica 11 Nov 2026; data from S&P Global Market Intelligence) [SECONDARY] — https://stockanalysis.com/
- Nasdaq.com historical quotes, daily data to 11 Nov 2026 (SNPS, CDNS, AIP, KEYS, PTC, ARM, SVCO, ULS, ADSK, IGV, SOXX, QQQ) — https://www.nasdaq.com/market-activity/stocks/snps/historical
- Euronext Paris historical prices for Dassault Systemes (FR0014003TT8) and Alten (FR0000071946), data to 11 Nov 2026 [PRIMARY] — https://live.euronext.com/
- ECB euro reference rates, 11 Nov 2026 [PRIMARY] — https://data-api.ecb.europa.eu/
- Synopsys Q3 FY2025 release, 9 Sep 2025 [PRIMARY]; Synopsys Investor Day release, 30 Sep 2026 [PRIMARY]; Synopsys Q4 date release, 5 Nov 2026 [PRIMARY] (URLs above).
- Meta Q3 2026 release, 21 Oct 2026 [PRIMARY]; Microsoft FY27 Q1 release, 28 Oct 2026 [PRIMARY]; SIA releases of 5 Oct and 3 Nov 2026 [PRIMARY]; WSTS Spring 2026 release [PRIMARY]; SEC exhibit on Schneider-PTC, 5 Oct 2026 [PRIMARY]; Arteris Q3 2026 release, 5 Nov 2026 [PRIMARY]; Siemens Q4 FY2026 earnings release, 12 Nov 2026 [PRIMARY] (URLs above).
- CNBC, 6 Nov 2026 and 12 Nov 2026; ts2.tech, 17 Jul 2026; TIKR, updated 18 Jul 2026; Tech Fund (techinvestments.io), 27 Jul 2026; MarketBeat, 10 Oct 2026 and 12 Nov 2026; Reuters, 1 Oct 2026 and 28 Oct 2026; Invezz, 5 Nov 2026; TheFly via TipRanks, 30 Sep to 6 Nov 2026; TrendForce, 3 Aug, 2 Nov and 11 Nov 2026; Motley Fool Cadence Q4 2025 transcript, 17 Feb 2026 [all SECONDARY] (URLs above).
- Sibling notes in this folder (synopsys.md, cadence.md, siemens_eda.md, specification_requirements_tools.md, china.md, market_structure_emulation_vip.md, model_makers_hyperscalers.md), read 12 Nov 2026, for primary figures cross-referenced above; no figure in this note conflicts with theirs except where shown (Dassault price date; Tech Fund's "around 14%").

### Inferences
- Because the price-based columns all use the 11 Nov 2026 close and one aggregator, cross-company comparisons in Tables 1-4 are internally consistent; absolute levels for Siemens (financial-services debt in EV; consensus EPS basis vs ex-Healthineers guidance) need the caveats noted.

### Gaps
- See the list above; a follow-up with a working search tool could close most of them (especially 10-year histories, fiscal 2028 consensus and the October 2026 hyperscaler capex calls).

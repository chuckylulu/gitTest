# Entry-point evidence: valuation, cycle position and investor access for US-listed AI system hardware (chips, optics, memory), as of 12 November 2026

Scope: valuation, cycle position, dated events and investor access only. These notes do not rank the companies and do not judge their technology or business quality; a separate workstream covers that. This is exploratory analysis, not personal financial advice. The labels (attractive, fair, stretched, cannot assess) describe the entry point as of the date checked. They are not buy or sell instructions.

Layout. The researcher format allows exactly three top-level sections, one per key question. The per-company Tier 1 sections (items 1 to 7) therefore sit under Key Question 1, in "Cited Findings". Key Question 2 holds the cross-company cycle table and the Tier 2 table. Key Question 3 holds the event calendar, the peer-comparison table, the access table, what could not be verified, and the source list.

Data conventions (apply throughout):
- Prices are 11 Nov 2026 closes, the last completed US session before the 12 Nov research date. Daily history comes from Nasdaq's historical-quote data and is split-adjusted. It agrees with StockAnalysis's "At close: Nov 11, 2026" quotes. Pre-market quotes for 12 Nov are time-stamped StockAnalysis indications. Example source: [Nasdaq historical data, NVDA](https://api.nasdaq.com/api/quote/NVDA/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12); [StockAnalysis NVDA statistics](https://stockanalysis.com/stocks/nvda/statistics/).
- Performance is price-only, not total return. Year-to-date is measured from the 31 Dec 2025 close, 12 months from the 11 Nov 2025 close, and "since January 2023" from the 30 Dec 2022 close. The 52-week range is on a closing basis, with the intraday range in brackets. Drawdown is measured from the 52-week closing high. All are computed from the Nasdaq history.
- Multiples come from StockAnalysis statistics pages read on 12 Nov 2026 at 11 Nov prices. "Trailing P/E" uses GAAP trailing-12-month EPS. StockAnalysis "Forward PE" is its own forward measure, and its period basis is not stated. To fix the basis, I also compute P/E from consensus EPS for the next two fiscal years.
- Consensus figures are S&P Global consensus as shown on StockAnalysis forecast pages, read 12 Nov 2026. StockAnalysis states that "EPS and Forward PE are based on non-GAAP adjusted numbers." Free access shows only the next two fiscal years, so a third year is not available.
- Own history uses two sources. StockAnalysis ratio pages give five fiscal-year-end values. Companiesmarketcap gives calendar-year-end values from roughly 2014 to 2025. EV/EBITDA has only five years of history; ten-year EV/EBITDA is not available.
- Reverse-DCF check, kept simple so it can be audited. Required EPS in year 5 = price × 1.10^5 ÷ exit P/E, with a 10% cost of equity and exit P/E of 15x or 20x. Implied growth = (required EPS ÷ FY2 consensus EPS)^(1 ÷ years from FY2 end to year 5) − 1. The check ignores dividends and buybacks. It is a reading of what the price needs, not a valuation.

## Key Question 1: What do current prices imply about growth and margins over the next two to three years, and how does that compare with guidance and with earlier cycle peaks?

### Takeaway
At 11 Nov 2026 closes, prices sit far below what consensus earnings would justify only where the market doubts that today's earnings will last. The clearest case is Micron. At about 4.6x FY2027 and 3.9x FY2028 consensus EPS, the price implies "normalized" EPS of roughly $68–81, against $176.50 FY2027 consensus. In other words the market prices the record 86–87% gross margins as transitory, much as it did at the 2017–18 peak. NVIDIA, at 18.6x FY2027 and 10.9x FY2028 consensus, needs almost no EPS growth after FY2028. Intel and Astera Labs, by contrast, need roughly 28–40% a year of EPS growth after FY2027 (Intel at 15–20x exit, Astera at 15–20x exit). Broadcom, Marvell, Lumentum, Coherent, Credo, Fabrinet and Amkor sit in between, needing roughly 3–27% a year depending on the exit multiple. Consensus for almost every name assumes the "successor" product arrives on schedule: Rubin, custom XPUs, co-packaged-optics lasers, optical DSPs and 14A foundry. The multiples on the optics and connectivity names are already below their own 2025–26 peaks.

### Cited Findings

#### Market backdrop (dated)
- Sector drawdown. The iShares Semiconductor ETF (SOXX) closed at 155.40 on 11 Nov 2026. That is +54.8% YTD and +58.0% over 12 months, but -28.8% from its 22 Jun 2026 closing high of 218.34. SMH was -24.2% from its 22 Jun high, QQQ -9.1% from its 6 Oct high, and SPY -2.5% from its 6 Oct high — [Nasdaq historical data, SOXX](https://api.nasdaq.com/api/quote/SOXX/historical?assetclass=etf&fromdate=2022-12-28&limit=9999&todate=2026-11-12); [Nasdaq historical data, SMH](https://api.nasdaq.com/api/quote/SMH/historical?assetclass=etf&fromdate=2022-12-28&limit=9999&todate=2026-11-12); [Nasdaq historical data, QQQ](https://api.nasdaq.com/api/quote/QQQ/historical?assetclass=etf&fromdate=2022-12-28&limit=9999&todate=2026-11-12); [Nasdaq historical data, SPY](https://api.nasdaq.com/api/quote/SPY/historical?assetclass=etf&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
- Midterm-election sell-off. On 4 Nov 2026, chip and data-center stocks fell after Democrats won both chambers of Congress and key governors' races "by pledging tougher tacks on data-center construction" — [MarketWatch, 4 Nov 2026](https://www.marketwatch.com/story/micron-and-other-chip-stocks-slip-as-election-results-strike-at-the-core-of-data-center-optimism-b55d19b3). On 5 Nov, "Wall Street is digesting the prospect of a slower AI buildout in the wake of the midterm election results" — [MarketWatch, 5 Nov 2026](https://www.marketwatch.com/story/micron-sandisk-and-other-ai-stocks-are-falling-hard-investors-dont-like-uncertainty-94d2a3b9). The WSJ called it "a historic selloff" — [WSJ, 11 Nov 2026](https://www.wsj.com/finance/stocks/investors-run-back-to-ai-stocks-less-than-a-week-after-a-historic-selloff-854483e8).
- Rebound. CoreWeave raised its 2026 revenue forecast to $13.0–13.3B with its Q3 results (10 Nov), and "Tech stocks roared back the next morning" — [StockAnalysis news, 11 Nov 2026](https://stockanalysis.com/stocks/mu/); [WSJ, 11 Nov 2026](https://www.wsj.com/finance/stocks/investors-run-back-to-ai-stocks-less-than-a-week-after-a-historic-selloff-854483e8)
- Breadth. "Nearly 40% of the S&P 500 is in a bear market" — [MarketWatch, 16 Oct 2026](https://www.marketwatch.com/story/nearly-40-of-the-s-p-500-is-in-a-bear-market-here-are-10-of-those-stocks-that-analysts-say-can-gain-up-to-81-93a51af6). Barron's (11 Nov 2026) wrote that semiconductor stocks "are trading in a pattern they traced in the late 1990s before the dot-com bubble burst" — [Barron's, 11 Nov 2026](https://www.barrons.com/articles/chip-stocks-dotcom-bubble-56f92d67)
- Supplier financing of customers, a cycle signal:
  - NVIDIA guarantees on OpenAI leases. On 17 Aug 2026 NVIDIA entered residual value guaranties for OpenAI-tenanted leases at the PORTS campus in Ohio (lessor: SB Energy). The aggregate obligation is "cumulatively capped at $105 billion" for about 4.25 GW, with optional credit support for about 3.8 GW more. Payments are conditional, ready-for-service milestones are "expected beginning in 2028", and OpenAI is to reimburse NVIDIA — [NVIDIA 8-K, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)
  - Marvell warrant to Google. Marvell issued Google a warrant for up to 58,970,907 shares at $206.58, mostly vesting one tranche per $500M of Custom revenue (240 tranches) — [Marvell 8-K, 19 Aug 2026](https://www.sec.gov/Archives/edgar/data/1835632/000119312526356217/d412696d8k.htm)
  - Headline-level reports: "Nvidia agreed to invest $3 billion in Meta" — [Investopedia, 27 Oct 2026](https://www.investopedia.com/5-things-to-know-before-the-stock-market-opens-on-tuesday-october-27-2026-12195919); "Broadcom Lined Up a $63B Deal for Anthropic" — [Investopedia, 27 Oct 2026](https://www.investopedia.com/market-update-broadcom-lined-up-a-usd63b-deal-for-anthropic-to-get-more-of-its-chips-the-stock-is-climbing-avgo-12196672)

#### NVIDIA (NVDA): Tier 1
1. **Price and performance**
   - Price: $173.73 close on 11 Nov 2026. After hours on 11 Nov it was -8.61% — [TipRanks, 12 Nov 2026](https://www.tipranks.com/news/why-amd-and-broadcom-stocks-gained-after-hours-while-nvidia-fell-over-8). Pre-market on 12 Nov (7:12 AM EST) it was $160.68, -7.51% — [StockAnalysis NVDA statistics](https://stockanalysis.com/stocks/nvda/statistics/)
   - Size: market cap $4.20T; EV $4.17T; net cash $23.6B — [StockAnalysis NVDA statistics](https://stockanalysis.com/stocks/nvda/statistics/)
   - 52-week closing range $165.17 (30 Mar 2026) to $239.24 (6 Oct 2026); intraday $164.27–$243.37 — [Nasdaq history NVDA](https://api.nasdaq.com/api/quote/NVDA/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD -6.8% (from $186.50); 12 months -10.1% (from $193.16); since 30 Dec 2022 +1,089% (from a split-adjusted $14.61). Drawdown from the 6 Oct high is -27.4%. Same source.
2. **Multiples**
   - Current — [StockAnalysis NVDA statistics](https://stockanalysis.com/stocks/nvda/statistics/):
     - Trailing GAAP P/E 21.97 (TTM EPS $7.91)
     - StockAnalysis forward P/E 14.33
     - EV/EBITDA 20.73; EV/sales 13.77
     - P/B 18.32
     - FCF yield 3.03% (TTM FCF $127.0B)
     - Dividend yield 0.58% ($1.00 a year)
   - On consensus — [StockAnalysis NVDA forecast](https://stockanalysis.com/stocks/nvda/forecast/):
     - P/E (adjusted) 18.6x FY2027 (EPS $9.32, FY ending Jan 2027) and 10.9x FY2028 ($15.93)
     - EV/sales 10.1x FY2027 and 6.0x FY2028
     - FY2027 consensus FCF yield 4.5% ($189.85B)
     - These are computed from the consensus figures.
   - Own history, fiscal year-ends Jan-2022 to Jan-2026 — [StockAnalysis NVDA ratios](https://stockanalysis.com/stocks/nvda/financials/ratios/):
     - Trailing P/E 58.55, 114.74, 50.65, 47.93, 37.98
     - Forward P/E 45.52, 52.57, 31.19, 36.24, 26.73
     - EV/EBITDA 50.25, 70.21, 43.51, 41.58, 33.85
     - P/B 21.46, 22.68, 35.08, 44.03, 28.99
     - Today's multiples are the lowest of the five-year set.
   - Own history, calendar year-ends 2016–2025 — [companiesmarketcap NVDA P/E](https://companiesmarketcap.com/nvidia/pe-ratio/); [P/S](https://companiesmarketcap.com/nvidia/ps-ratio/); [P/B](https://companiesmarketcap.com/nvidia/pb-ratio/):
     - Trailing P/E: min 17.1 (2018), median 59.2, max 89.0 (2021); 2024 missing from the series
     - P/S: median 17.4 (range 6.2–28.7), against 13.8 now
     - P/B: median 19.8 (range 8.59–49.9), against 18.3 now
   - Peers — StockAnalysis statistics: [AMD](https://stockanalysis.com/stocks/amd/statistics/), [AVGO](https://stockanalysis.com/stocks/avgo/statistics/), [TSMC (TPE:2330)](https://stockanalysis.com/quote/tpe/2330/statistics/), [MediaTek (TPE:2454)](https://stockanalysis.com/quote/tpe/2454/statistics/), [Hon Hai (TPE:2317)](https://stockanalysis.com/quote/tpe/2317/statistics/), [Quanta (TPE:2382)](https://stockanalysis.com/quote/tpe/2382/statistics/), [Foxconn Industrial Internet (SHA:601138)](https://stockanalysis.com/quote/sha/601138/statistics/):

     | Peer | Forward P/E | EV/EBITDA | P/B |
     |---|---|---|---|
     | AMD | 36.73 | 80.79 | 13.26 |
     | Broadcom | 19.84 | 32.21 | — |
     | TSMC (TPE:2330) | 16.42 | 15.88 | 8.62 |
     | MediaTek (TPE:2454) | 28.76 | 48.91 | — |
     | Hon Hai (TPE:2317), system assembly | 11.57 | 7.78 | — |
     | Quanta (TPE:2382), system assembly | 9.30 | 8.92 | — |
     | Foxconn Industrial Internet (SHA:601138), system assembly | 11.53 | 12.46 | — |

3. **What the price assumes**
   - Consensus, 54 analysts: FY2027 revenue $412.06B (+90.8%) with gross margin 73.78% and operating income $269.15B; FY2028 revenue $692.26B (+68.0%); EPS $9.32 and then $15.93 — [StockAnalysis NVDA forecast](https://stockanalysis.com/stocks/nvda/forecast/)
   - Company guidance for Q3 FY2027: revenue $108.0B ±2% and gross margin 74.0% ±50bp, with "not assuming any Data Center compute revenue from China" — [NVIDIA Q2 FY27 8-K, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/0001045810-26-000073.txt)
   - Computed: Q1 $81.6B plus Q2 $96.2B plus the Q3 guide of $108B means FY2027 consensus requires Q4 of about $126B, roughly +17% quarter on quarter.
   - Reverse-DCF: the price needs about $18.65 EPS in year 5 at a 15x exit (≈+4%/yr after FY2028), or $13.99 at a 20x exit (≈-3%/yr). Computed.
   - Bridge and successor: consensus assumes Rubin ramps on schedule. The August release says "Vera Rubin, now in full production". It also says Spectrum-6 switches "supporting pluggable and co-packaged optics" are arriving — [NVIDIA Q2 FY27 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/0001045810-26-000073.txt). The 10.9x FY2028 multiple does not capitalise growth beyond FY2028.
4. **Cycle position**
   - Q2 FY2027 (quarter ended 26 Jul 2026; reported 26 Aug 2026) — [NVIDIA Q2 FY27 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/0001045810-26-000073.txt):
     - Revenue $96.2B (+18% q/q, +106% y/y); Data Center $89.0B (+117% y/y)
     - GAAP and non-GAAP gross margin 75.0%; non-GAAP EPS $2.22, which now includes stock-based compensation
     - About $26.0B returned to shareholders; $99.0B of buyback authorisation left
   - Balance sheet — [NVIDIA Q2 FY27 8-K, financial statements](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/0001045810-26-000073.txt):
     - Inventories $31.6B at 26 Jul 2026, against $21.4B at 25 Jan 2026
     - Receivables $63.1B, against $38.5B
     - Q2 operating cash flow $24.1B
   - Gross-margin history (GAAP, fiscal years): 56.9% in FY2023 (trough), 75.0% in FY2025 (peak), 71.1% in FY2026. The current 75% sits at the prior peak — [SEC XBRL company facts, NVDA](https://data.sec.gov/api/xbrl/companyfacts/CIK0001045810.json)
   - Customer financing: the $105B-capped lease guaranties for OpenAI described in the market backdrop — [NVIDIA 8-K, 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)
5. **Near-term events**
   - Governance (press reports, not company disclosures):
     - WSJ reported that NVIDIA's board was preparing to remove CEO Jensen Huang. Barron's and TheFly cite this — [Barron's, 12 Nov 2026](https://www.barrons.com/articles/nvidia-stock-price-huang-affair-ceo-ouster-26c99dad); [TheFly via TipRanks, 12 Nov 2026](https://www.tipranks.com/news/the-fly/nvidia-downgraded-to-in-line-from-outperform-at-evercore-isi-thefly-news)
     - The board convened on the evening of 11 Nov after reports about the CEO's personal conduct — [CNBC, 12 Nov 2026](https://www.cnbc.com/2026/11/12/jensen-huang-nvidia-affair-ceo.html)
     - The FT says NVIDIA has no corporate succession plan — [TheFly via TipRanks, 12 Nov 2026](https://www.tipranks.com/news/the-fly/nvidia-ceo-huangs-future-uncertain-has-no-corporate-succession-plan-ft-says-thefly-news)
     - MarketWatch describes a "scandal engulfing Nvidia" centred on Singapore-based Megaspeed — [MarketWatch, 12 Nov 2026](https://www.marketwatch.com/story/heres-what-megaspeed-the-company-at-the-forefront-of-the-nvidia-scandal-is-now-saying-b73f8d0b)
     - The SEC submissions index showed no NVIDIA 8-K after 3 Sep 2026 when checked on 12 Nov — [SEC submissions, NVDA](https://data.sec.gov/submissions/CIK0001045810.json)
   - Broker actions on 12 Nov 2026 (all via TheFly/TipRanks unless noted):
     - Bernstein downgraded to Market Perform; target $200 from $400 — [link](https://www.tipranks.com/news/the-fly/bernstein-says-weve-had-enough-in-downgrade-of-nvidia-thefly-news)
     - Evercore ISI downgraded to In Line; target $186 from $465 — [link](https://www.tipranks.com/news/the-fly/nvidia-downgraded-to-in-line-from-outperform-at-evercore-isi-thefly-news)
     - William Blair downgraded to Market Perform — [link](https://www.tipranks.com/news/the-fly/nvidia-downgraded-to-market-perform-from-outperform-at-william-blair-thefly-news)
     - Oppenheimer downgraded to a hold-equivalent rating — [StockAnalysis NVDA forecast](https://stockanalysis.com/stocks/nvda/forecast/)
     - BofA kept Buy; target $280 from $350 — [link](https://www.tipranks.com/news/the-fly/nvidia-price-target-lowered-to-280-from-350-at-bofa-thefly-news)
     - Citi kept Buy; target $225 from $285 — [link](https://www.tipranks.com/news/the-fly/nvidia-price-target-lowered-to-225-from-285-at-citi-thefly-news)
     - Stifel kept Buy; target $205 from $315 — [link](https://www.tipranks.com/news/the-fly/nvidia-price-target-lowered-to-205-from-315-at-stifel-thefly-news)
     - The S&P Global average target of $311.51 predates these cuts — [StockAnalysis NVDA forecast](https://stockanalysis.com/stocks/nvda/forecast/)
   - Export controls: President Trump "authorized a crackdown on companies suspected of diverting Nvidia's advanced AI chips to China on November 5", per Axios, which also reports that Commerce Secretary Lutnick stalled the curbs — [TheFly via TipRanks, 12 Nov 2026](https://www.tipranks.com/news/the-fly/lutnick-stalled-trumps-nvidia-china-chip-curbs-axios-reports-thefly-news)
   - Earnings: Q3 FY2027 results on 17 Nov 2026 after the close (confirmed) — [StockAnalysis NVDA statistics](https://stockanalysis.com/stocks/nvda/statistics/)
6. **Access**
   - Listing: Nasdaq only; Delaware corporation — [SEC submissions, NVDA](https://data.sec.gov/submissions/CIK0001045810.json)
   - Liquidity: average daily value traded about $28.6B (20-day average volume of 164.8M shares × $173.73; computed from [StockAnalysis NVDA statistics](https://stockanalysis.com/stocks/nvda/statistics/))
   - Index membership: S&P 500 and Nasdaq-100 — [StockAnalysis S&P 500 list](https://stockanalysis.com/list/sp-500-stocks/); [Nasdaq-100 list](https://stockanalysis.com/list/nasdaq-100-stocks/)
   - ETF weights: SMH 18.92%, SOXX 7.11%, QQQ 7.10% — [StockAnalysis SMH holdings](https://stockanalysis.com/etf/smh/holdings/); [SOXX](https://stockanalysis.com/etf/soxx/holdings/); [QQQ](https://stockanalysis.com/etf/qqq/holdings/)
7. **Suggested label: cannot assess** (as of the 12 Nov 2026 pre-market).
   - Why: a binary governance event is unresolved, the stock is indicated about -7.5%, and results come on 17 Nov.
   - On multiples alone it would screen attractive: trailing P/E is at the bottom of its ten-year range, about 18.6x FY2027 and 10.9x FY2028 consensus, and the reverse-DCF needs about zero growth after FY2028.
   - Entry would look more attractive if:
     - the board's decision and any findings on the Megaspeed and export-diversion matters are disclosed and contained;
     - the 17 Nov print meets the $108B Q3 guide and the Q4 guide supports the roughly $126B Q4 that FY2027 consensus implies;
     - the scope of the 5 Nov export crackdown becomes clear;
     - the price falls to about $159 or below (10x FY2028) or $140 (15x FY2027), which would leave a margin even if consensus is cut.

#### Broadcom (AVGO): Tier 1
1. **Price and performance**
   - Price: $345.22 close on 11 Nov 2026 (+3.99% on the day). Pre-market on 12 Nov (7:23 AM) it was $348.00, +0.81% — [StockAnalysis AVGO statistics](https://stockanalysis.com/stocks/avgo/statistics/); [StockAnalysis AVGO](https://stockanalysis.com/stocks/avgo/)
   - Size: market cap $1.65T; EV $1.68T; total debt $59.4B — [StockAnalysis AVGO statistics](https://stockanalysis.com/stocks/avgo/statistics/)
   - 52-week closing range $291.53 (5 Nov 2026) to $481.57 (2 Jun 2026); intraday $289.77–$495.00 — [Nasdaq history AVGO](https://api.nasdaq.com/api/quote/AVGO/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD -0.3%; 12 months -1.9%; since 30 Dec 2022 +517%. Drawdown -28.3%. Same source.
2. **Multiples**
   - Current — [StockAnalysis AVGO statistics](https://stockanalysis.com/stocks/avgo/statistics/):
     - Trailing GAAP P/E 44.07 (TTM EPS $7.83)
     - StockAnalysis forward P/E 19.84
     - EV/EBITDA 32.21; EV/sales 18.89
     - P/B 16.53
     - FCF yield 2.39%
     - Dividend yield 0.75% ($0.65 a quarter)
   - On consensus (computed from [StockAnalysis AVGO forecast](https://stockanalysis.com/stocks/avgo/forecast/)):
     - P/E 29.6x FY2026 (EPS $11.67; the year ended about 1 Nov 2026) and 17.7x FY2027 ($19.47)
     - EV/sales 15.9x and 9.6x
     - FY2026 consensus FCF yield 3.0%
   - Own history, fiscal year-ends FY2021 to FY2025 — [StockAnalysis AVGO ratios](https://stockanalysis.com/stocks/avgo/financials/ratios/):
     - Trailing P/E 34.00, 17.07, 24.57, 133.83, 75.48
     - Forward P/E 17.43, 11.74, 18.77, 28.55, 44.02 (median 18.77)
     - EV/EBITDA 16.86, 11.47, 18.17, 32.90, 51.19 (median 18.17)
     - P/B 8.76, 8.43, 14.43, 11.66, 21.47
     - Dividend yield 2.81%, 3.69%, 2.28%, 1.29%, 0.66%
   - Own history, calendar year-ends 2016–2025 — [companiesmarketcap AVGO P/S](https://companiesmarketcap.com/broadcom/ps-ratio/); [P/B](https://companiesmarketcap.com/broadcom/pb-ratio/):
     - P/S median 6.02 (range 4.43–27.3), against 18.5 now
     - P/B median 8.88 (range 3.22–20.3), against 16.5 now
   - Peers — StockAnalysis statistics: [MRVL](https://stockanalysis.com/stocks/mrvl/statistics/), [MediaTek](https://stockanalysis.com/quote/tpe/2454/statistics/), [Alchip (TPE:3661)](https://stockanalysis.com/quote/tpe/3661/statistics/), [Global Unichip (TPE:3443)](https://stockanalysis.com/quote/tpe/3443/statistics/), [Socionext (TYO:6526)](https://stockanalysis.com/quote/tyo/6526/statistics/), [ANET](https://stockanalysis.com/stocks/anet/statistics/):

     | Peer | Forward P/E | EV/EBITDA |
     |---|---|---|
     | NVIDIA | 14.33 | 20.73 |
     | Marvell | 29.92 | 52.47 |
     | MediaTek (TPE:2454) | 28.76 | 48.91 |
     | Alchip (TPE:3661) | 18.20 | 27.60 |
     | Global Unichip (TPE:3443) | 63.58 | 145.77 |
     | Socionext (TYO:6526) | 18.96 | 10.33 |
     | Arista Networks | 34.76 | 44.14 |

3. **What the price assumes**
   - Consensus, 51 analysts: FY2026 revenue $105.99B (+65.9%), FY2027 $175.47B (+65.6%); EPS $11.67 and then $19.47 — [StockAnalysis AVGO forecast](https://stockanalysis.com/stocks/avgo/forecast/)
   - Q4 FY2026 guidance: revenue about $34.8B (+93% y/y); AI semiconductor revenue $21.7B (+236%); non-GAAP operating margin about 66% — [Broadcom Q3 FY26 8-K, 2 Sep 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000076/0001730168-26-000076.txt)
   - Reverse-DCF: the price needs $27.80 EPS in year 5 at 20x (≈+9%/yr after FY2027) or $37.07 at 15x (≈+17%/yr). Computed.
   - Bridge and successor: both consensus and the multiple assume the custom-accelerator (XPU) ramp carries on beyond FY2027, which means successor XPU generations and switch-package optics have to arrive on schedule. A headline-level report of a $63B Anthropic arrangement supports the backlog story — [Investopedia, 27 Oct 2026](https://www.investopedia.com/market-update-broadcom-lined-up-a-usd63b-deal-for-anthropic-to-get-more-of-its-chips-the-stock-is-climbing-avgo-12196672)
4. **Cycle position**
   - Q3 FY2026 (ended 2 Aug 2026; reported 2 Sep 2026) — [Broadcom Q3 FY26 8-K](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000076/0001730168-26-000076.txt):
     - Revenue $29.59B (+86% y/y): semiconductors $20.84B (+127%), AI semiconductors $16.7B (+221%), infrastructure software $8.75B (+29%)
     - Non-GAAP EPS $3.32; free cash flow $13.67B (46% of revenue); cash $24.0B
     - CEO: "Demand for our custom AI accelerators and networking continues to be very strong."
   - Gross-margin history (GAAP): 68.9% in FY2023 (peak), 67.8% in FY2025 — [SEC XBRL company facts, AVGO](https://data.sec.gov/api/xbrl/companyfacts/CIK0001730168.json). StockAnalysis shows a non-GAAP-style 75–77% — [StockAnalysis AVGO forecast](https://stockanalysis.com/stocks/avgo/forecast/)
   - Backlog was not in the release (see Gaps).
5. **Near-term events**
   - Earnings: Q4 FY2026 results on Wednesday 9 Dec 2026 — [PR Newswire, 9 Nov 2026](https://www.prnewswire.com/news-releases/broadcom-inc-to-announce-fourth-quarter-and-fiscal-year-2026-financial-results-on-wednesday-december-9-2026-302932749.html)
   - The 10 Sep 2026 S-4 is a debt exchange offer for $654M of 4.926% notes due 2037, not an acquisition — [Broadcom S-4](https://www.sec.gov/Archives/edgar/data/1730168/000119312526387881/d154803ds4.htm)
   - The 27 Oct 2026 8-K (Item 2.03, new direct financial obligation) was not read; its contents are not verified — [SEC submissions, AVGO](https://data.sec.gov/submissions/CIK0001730168.json)
   - Share moves: AVGO rose about 9–10% on 9 Nov — [TipRanks, 9 Nov 2026](https://www.tipranks.com/news/broadcom-stock-avgo-is-up-10-as-dip-buyers-rush-into-the-market). It gained on 12 Nov as investors looked to NVIDIA's rivals — [Barron's, 12 Nov 2026](https://www.barrons.com/articles/amd-stock-broadcom-nvidia-ai-chips-2b96c1f1)
6. **Access**
   - Listing: Nasdaq — [SEC submissions, AVGO](https://data.sec.gov/submissions/CIK0001730168.json)
   - Liquidity: average daily value traded about $9.0B (computed)
   - Index membership: S&P 500 and Nasdaq-100
   - ETF weights: SOXX 8.30%, SMH 5.90%, XSD 2.60%, QQQ 2.51% — [SOXX](https://stockanalysis.com/etf/soxx/holdings/); [SMH](https://stockanalysis.com/etf/smh/holdings/); [XSD](https://stockanalysis.com/etf/xsd/holdings/); [QQQ](https://stockanalysis.com/etf/qqq/holdings/)
7. **Suggested label: fair.**
   - Why: 17.7x FY2027 is below its five-year forward-P/E median (18.8x), but EV/EBITDA (32x against an 18x median) and P/S (18.5x against a 6.0x ten-year median) are far above history. The price also needs about 9–17%/yr EPS growth after a +66% FY2027.
   - Entry would look more attractive if:
     - the price is about $292 or below (15x FY2027, the 5 Nov low);
     - the 9 Dec print delivers at least $21.7B of AI semiconductor revenue and a Q1 FY2027 guide consistent with about $175B of FY2027 revenue;
     - a disclosed AI backlog covers a large share of FY2027.

#### Marvell (MRVL): Tier 1
1. **Price and performance**
   - Price: $168.80 close on 11 Nov 2026 (+9.33% on the day). Pre-market on 12 Nov (7:35 AM) it was $162.80, -3.55% — [StockAnalysis MRVL statistics](https://stockanalysis.com/stocks/mrvl/statistics/)
   - Size: market cap $148.20B; EV $149.56B — same source
   - 52-week closing range $73.73 (4 Feb 2026) to $316.43 (4 Jun 2026); intraday $70.69–$329.88 — [Nasdaq history MRVL](https://api.nasdaq.com/api/quote/MRVL/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD +98.6%; 12 months +89.0%; since 30 Dec 2022 +356%. Drawdown -46.7%. Same source.
   - The shares fell 12.72% on 2 Nov, the day the Lumentum deal was announced — [TipRanks, 3 Nov 2026](https://www.tipranks.com/news/marvell-stock-mrvl-why-wall-street-is-split-on-the-115b-lumentum-acquisition)
2. **Multiples**
   - Current — [StockAnalysis MRVL statistics](https://stockanalysis.com/stocks/mrvl/statistics/):
     - Trailing GAAP P/E 56.71
     - StockAnalysis forward P/E 29.92
     - EV/EBITDA 52.47; EV/sales 15.83
     - P/B 7.99
     - FCF yield 1.17%
     - Dividend yield 0.14%
   - On consensus (computed from [StockAnalysis MRVL forecast](https://stockanalysis.com/stocks/mrvl/forecast/)):
     - P/E 40.0x FY2027 (EPS $4.22; FY ending Jan 2027) and 23.0x FY2028 ($7.35)
     - EV/sales 12.4x and 7.6x
   - Own history, fiscal year-ends FY2022 to FY2026 — [StockAnalysis MRVL ratios](https://stockanalysis.com/stocks/mrvl/financials/ratios/):
     - Forward P/E 31.80, 23.54, 36.15, 43.66, 23.66 (median 31.8)
     - EV/EBITDA 50.74, 23.33, 64.59, 75.00, 26.24
     - P/B 3.56, 2.41, 3.94, 7.27, 4.68
   - Ten-year history was not available (no companiesmarketcap page found for MRVL).
   - Peers — [Montage Technology (SHA:688008)](https://stockanalysis.com/quote/sha/688008/statistics/); [CRDO](https://stockanalysis.com/stocks/crdo/statistics/); [ALAB](https://stockanalysis.com/stocks/alab/statistics/):

     | Peer | Forward P/E | EV/EBITDA |
     |---|---|---|
     | Broadcom | 19.84 | 32.21 |
     | Alchip (TPE:3661) | 18.20 | 27.60 |
     | Global Unichip (TPE:3443) | 63.58 | 145.77 |
     | MediaTek (TPE:2454) | 28.76 | 48.91 |
     | Montage Technology (SHA:688008) | 36.76 | 58.89 |
     | Credo | 19.39 | 47.57 |
     | Astera Labs | 33.57 | 94.58 |

3. **What the price assumes**
   - Consensus, 43 analysts: FY2027 revenue $12.07B (+47.3%), FY2028 $19.78B (+63.9%); EPS $4.22 and then $7.35 — [StockAnalysis MRVL forecast](https://stockanalysis.com/stocks/mrvl/forecast/)
   - Company guidance and commentary — [Marvell Q2 FY27 8-K, 27 Aug 2026](https://www.sec.gov/Archives/edgar/data/1835632/000183563226000022/0001835632-26-000022.txt); [Marvell 8-K, 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442714/0001193125-26-442714.txt):
     - Q3 FY2027 guide: revenue $3.150B; non-GAAP gross margin 57.5–58.5%; non-GAAP EPS $1.10 ±$0.05
     - On 2 Nov the revenue range was narrowed to ±2%, with preliminary revenue "consistent with previously provided guidance"
     - Management cited "a significant acceleration in our Custom business beginning in the second half of fiscal 2027" and raised its FY2027 and FY2028 outlook
   - Google warrant: up to 58.97M shares at $206.58, with one tranche per $500M of Custom revenue. Full vesting would imply about $120B of Google custom purchases through FY2033 (computed: 240 × $500M) — [Marvell 8-K, 19 Aug 2026](https://www.sec.gov/Archives/edgar/data/1835632/000119312526356217/d412696d8k.htm)
   - Reverse-DCF, standalone: about +18%/yr (20x) to +27%/yr (15x) EPS growth needed after FY2028.
   - Reverse-DCF, rough pro forma with Lumentum: FY2028 EPS of about $7.85 before synergies and about $8.51 with $1B of pre-tax synergies at a 15% tax rate, which puts the shares at about 19.8–21.5x. The price then needs about +13%/yr (20x) to +22%/yr (15x). Computed from consensus and the 4.5 exchange ratio; the mismatched fiscal years make this approximate.
   - Bridge and successor: the price and consensus assume the successors arrive on schedule. These are the custom XPUs, co-packaged optics and, after the deal, Lumentum's CPO lasers and optical circuit switches. The assignment says Celestial AI revenue is expected from 2H FY2028; I did not verify that in the filings read. The DSP bridge alone would not support the multiple.
4. **Cycle position**
   - Q2 FY2027 (ended 1 Aug 2026; reported 27 Aug) — [Marvell Q2 FY27 8-K](https://www.sec.gov/Archives/edgar/data/1835632/000183563226000022/0001835632-26-000022.txt):
     - Revenue $2.739B (+37% y/y; $39M above the guide midpoint); Data Center +46% y/y
     - Non-GAAP gross margin 58.9% (GAAP 53.1%); non-GAAP EPS $0.94
     - Operating cash flow $605.5M
     - "AI-related bookings remain exceptionally robust."
   - Gross-margin history (GAAP): 50.5% in FY2023, 41.3% in FY2025 (trough), 51.0% in FY2026 — [SEC XBRL company facts, MRVL](https://data.sec.gov/api/xbrl/companyfacts/CIK0001835632.json)
5. **Near-term events**
   - Earnings: Q3 FY2027 results on 1 Dec 2026 after the close (confirmed) — [StockAnalysis MRVL statistics](https://stockanalysis.com/stocks/mrvl/statistics/); [Business Wire, 6 Nov 2026](https://www.businesswire.com/news/home/20261106322575/en/Marvell-Technology-Inc.-Announces-Conference-Call-to-Review-Third-Quarter-of-Fiscal-Year-2027-Financial-Results/)
   - Lumentum merger: agreement dated 1 Nov 2026; 4.500 MRVL shares per LITE share, all stock — [Marvell 8-K Item 1.01](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442717/d352474d8k.htm)
     - Conditions: both shareholder votes, HSR clearance, "certain other required regulatory approvals", and an effective S-4
     - Outside Date: 1 Nov 2027, extendable to 1 Feb, 1 May and 1 Aug 2028
     - Termination fees: $5.8B payable by Marvell, $2.9B by Lumentum, and a $3.2B regulatory reverse fee payable by Marvell
     - Implied EV $115B (about $1,132 per LITE share, a 23.9% premium to the 28 Oct unaffected price)
     - Pro forma ownership 67% Marvell / 33% Lumentum; more than $1B of run-rate cost synergies; accretive in year one
     - Expected to close in "the first half of calendar year 2028" — [Marvell 8-K, 2 Nov 2026, Ex. 99.1/99.2](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442714/0001193125-26-442714.txt)
   - Holders of both companies criticised the terms ("It's a trash offer") — [MarketWatch, 2 Nov 2026](https://www.marketwatch.com/story/marvell-and-lumentum-shareholders-unite-in-panning-merger-deal-its-a-trash-offer-53a9f307)
   - Broker target cuts:
     - Cantor Fitzgerald $225 from $350 (Neutral), 3 Nov — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/marvell-price-target-lowered-to-225-from-350-at-cantor-fitzgerald-thefly-news)
     - B. Riley $275 from $365 on 3 Nov, then $250 on 9 Nov (Buy) — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/marvell-price-target-lowered-to-250-from-275-at-b-riley-thefly-news)
6. **Access**
   - Listing: Nasdaq; Delaware corporation — [SEC submissions, MRVL](https://data.sec.gov/submissions/CIK0001835632.json)
   - Liquidity: average daily value traded about $5.1B (computed)
   - Index membership: S&P 500 and Nasdaq-100
   - ETF weights: SMH 3.27%, SOXX 3.37% — [SMH](https://stockanalysis.com/etf/smh/holdings/); [SOXX](https://stockanalysis.com/etf/soxx/holdings/)
7. **Suggested label: fair** (with a deal overhang).
   - Why: the forward multiple is below its own five-year median (23x FY2028 against about 32x), but the reverse-DCF is demanding on a standalone basis. Merger arbitrage and dilution also weigh on the shares.
   - Entry would look more attractive if:
     - the S-4 shows pro forma financials and vote dates;
     - the 1 Dec print confirms the custom ramp;
     - the price is about $147 or below (20x FY2028 standalone; about 17x pro forma including synergies).

#### Micron (MU): Tier 1
1. **Price and performance**
   - Price: $811.30 close on 11 Nov 2026 (+11.89% on the day). Pre-market on 12 Nov (6:39 AM) it was $781.92, -3.62% — [StockAnalysis MU statistics](https://stockanalysis.com/stocks/mu/statistics/); [StockAnalysis MU](https://stockanalysis.com/stocks/mu/)
   - Size: market cap $917.92B; EV $849.65B; net cash $68.3B — [StockAnalysis MU statistics](https://stockanalysis.com/stocks/mu/statistics/)
   - 52-week closing range $201.37 (20 Nov 2025) to $1,213.56 (25 Jun 2026); intraday $192.59–$1,255.00 — [Nasdaq history MU](https://api.nasdaq.com/api/quote/MU/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD +184.3%; 12 months +236.5%; since 30 Dec 2022 +1,523%. Drawdown -33.1%. Same source.
   - MU and SanDisk fell "nearly 30% in a week" around the election — [Invezz, 9 Nov 2026](https://invezz.com/news/2026/11/09/micron-sandisk-stocks-crash-nearly-30-in-a-week-has-ai-selloff-gone-too-far/)
2. **Multiples**
   - Current — [StockAnalysis MU statistics](https://stockanalysis.com/stocks/mu/statistics/):
     - Trailing GAAP P/E 10.91 (TTM EPS $74.33)
     - StockAnalysis forward P/E 4.60
     - EV/EBITDA 7.81; EV/sales 6.38
     - P/B 6.63 (book value per share about $122)
     - FCF yield 6.42%
     - Dividend yield 0.07% ($0.15 a quarter)
   - On consensus (computed from [StockAnalysis MU forecast](https://stockanalysis.com/stocks/mu/forecast/) and [Micron Q4 FY26 8-K](https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/0000723125-26-000018.txt)):
     - P/E 4.6x FY2027 (EPS $176.50; FY ending Aug 2027) and 3.9x FY2028 ($207.76)
     - FQ1 FY2027 guided non-GAAP EPS of $38.15 annualises to $152.6, or 5.3x
     - EV/sales 3.1x FY2027
     - FY2027 consensus FCF yield 15.6% ($143.09B)
   - Own history, P/B (the key metric), calendar year-ends — [companiesmarketcap MU P/B](https://companiesmarketcap.com/micron-technology/pb-ratio/):

     | Year | P/B |
     |---|---|
     | 2014 | 3.01 |
     | 2016 | 1.83 |
     | 2017 | 2.03 |
     | 2018 | 1.02 |
     | 2019 | 1.64 |
     | 2020 | 2.10 |
     | 2021 | 2.27 |
     | 2022 | 1.11 |
     | 2023 | 2.20 |
     | 2024 | 2.11 |
     | 2025 | 6.04 |

     - Ten-year median (2016–25) 2.06; five-year median (2021–25) 2.20. Today's 6.63 is the highest in the 2002–2026 series.
     - StockAnalysis fiscal-year-end P/B: 1.27 (FY2022), 1.74, 2.35, 2.52, 7.82 (FY2026) — [StockAnalysis MU ratios](https://stockanalysis.com/stocks/mu/financials/ratios/)
   - Own history, other multiples:
     - Trailing P/E at calendar year-ends 2017 and 2018 (the last peak in earnings) was 5.91 and 2.42; the ten-year median of positive values is about 15 — [companiesmarketcap MU P/E](https://companiesmarketcap.com/micron-technology/pe-ratio/)
     - Fiscal-year-end EV/EBITDA: 3.52 (FY2022), 19.33, 12.19, 7.76, 9.72 — [StockAnalysis MU ratios](https://stockanalysis.com/stocks/mu/financials/ratios/)
   - Peers — [SK hynix (KRX:000660)](https://stockanalysis.com/quote/krx/000660/statistics/); [Samsung Electronics (KRX:005930)](https://stockanalysis.com/quote/krx/005930/statistics/); [Kioxia (TYO:285A)](https://stockanalysis.com/quote/tyo/285A/statistics/); [Nanya Technology (TPE:2408)](https://stockanalysis.com/quote/tpe/2408/statistics/); [SanDisk](https://stockanalysis.com/stocks/sndk/statistics/):

     | Peer | Trailing P/E | Forward P/E | EV/EBITDA | P/B | FCF yield |
     |---|---|---|---|---|---|
     | SK hynix (KRX:000660) | 4.80 | 2.52 | 3.77 | 2.96 | 13.6% |
     | Samsung Electronics (KRX:005930) | 6.41 | 2.92 | 3.49 | 2.17 | 15.2% |
     | Kioxia (TYO:285A) | 3.82 | 2.11 | 3.59 | 5.44 | 16.0% |
     | Nanya Technology (TPE:2408) | 7.44 | 3.30 | 5.09 | 3.41 | 12.2% |
     | SanDisk (SNDK) | 7.87 | 3.99 | 6.21 | 7.76 | 12.5% |

     Micron trades at a premium to every memory peer on forward P/E.
3. **What the price assumes**
   - Consensus, 49 analysts — [StockAnalysis MU forecast](https://stockanalysis.com/stocks/mu/forecast/):
     - FY2027 revenue $275.89B (+107%), gross margin 86.98%, operating income $230.30B, FCF $143.09B
     - FY2028 revenue $320.06B (+16%)
     - EPS $176.50 and then $207.76
   - Company guidance — [Micron Q4 FY26 8-K, 30 Sep 2026](https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/0000723125-26-000018.txt):
     - FQ1 FY2027: revenue $61.5B ±$1.5B; non-GAAP gross margin about 86.25%; non-GAAP EPS $38.15 ±$1.00
     - CEO: "we expect an even stronger fiscal 2027", and the "Strategic Customer Agreements provide added confidence in the durability of Micron's financial performance."
   - Reverse-DCF and normalized earnings (computed):
     - At a 10–12x mid-cycle multiple the price implies normalized EPS of about $68–81. That is 38–46% of FY2027 consensus and close to FY2026's actual $75.52.
     - At a 15x exit, the year-5 EPS needed is $87, so EPS could fall about 24% a year from FY2028 consensus and still justify today's price.
     - Cumulative FY2027–28 consensus EPS ($384) equals about 47% of the share price.
   - **The price does not assume peak-cycle margins persist.**
     - The multiple matches the 2017–18 peak (trailing P/E of 2.4–5.9x at those year-ends).
     - Against the prior being tested ("memory stays supply-limited through 2028, 70%"), the price looks consistent with a materially lower probability, or with a turn before 2028.
     - Consensus itself assumes record HBM and conventional-DRAM pricing holds through FY2028 (FY2028 revenue +16%). The multiple assumes it does not.
   - "First to turn in a spending pause": share-price behaviour supports this. MU and SanDisk fell about 30% in the week after the 3 Nov election "prospect of a slower AI buildout" without any fundamental turn — [MarketWatch, 5 Nov 2026](https://www.marketwatch.com/story/micron-sandisk-and-other-ai-stocks-are-falling-hard-investors-dont-like-uncertainty-94d2a3b9); [Invezz, 9 Nov 2026](https://invezz.com/news/2026/11/09/micron-sandisk-stocks-crash-nearly-30-in-a-week-has-ai-selloff-gone-too-far/). Fundamentals show no turn yet (the FQ1 guide is +13% q/q). Invezz also noted "Apple's warning about soaring memory-chip prices" (headline level).
4. **Cycle position**
   - FQ4 FY2026 (ended 3 Sep 2026; reported 30 Sep 2026) — [Micron Q4 FY26 8-K](https://www.sec.gov/Archives/edgar/data/723125/000072312526000018/0000723125-26-000018.txt):
     - Revenue $54.23B (FQ3 $41.46B; FQ4 FY2025 $11.32B)
     - Non-GAAP gross margin 87.0%; non-GAAP operating margin 82.3%; non-GAAP EPS $33.42
     - Operating cash flow $43.97B; net capex $10.77B; adjusted FCF $33.20B
     - Business units: Cloud Memory $16.28B (83% gross margin), Core Data Center $18.00B (90%), Mobile & Client $13.11B (90%), Automotive & Embedded $6.82B (84%)
   - FY2026 totals: revenue $133.19B; GAAP gross margin 80.7%; net capex $27.37B; cash $73.48B. Same source.
   - Inventory: $10.37B at 3 Sep 2026, against $8.57B (28 May 2026) and $8.36B (28 Aug 2025). Same source.
   - Gross-margin history (GAAP): 58.9% in FY2018 (prior peak), -9.1% in FY2023 (trough), 80.7% in FY2026. Guided FQ1 FY2027 is about 86%, far above any prior peak — [SEC XBRL company facts, MU](https://data.sec.gov/api/xbrl/companyfacts/CIK0000723125.json)
5. **Near-term events**
   - Earnings: FQ1 FY2027 results around 16 Dec 2026 (estimated, not confirmed) — [StockAnalysis MU statistics](https://stockanalysis.com/stocks/mu/statistics/)
   - The 5 Nov 8-K covers a director retirement and is immaterial — [Micron 8-K](https://www.sec.gov/Archives/edgar/data/723125/000110465926123389/tm2629062d1_8k.htm)
   - Policy risk to data-center construction after the midterms; see the market backdrop.
   - Broker views:
     - KeyBanc (John Vinh) sees about 140% upside — [Barron's, 10 Nov 2026](https://www.barrons.com/articles/micron-stock-price-soaring-70d54e25)
     - Goldman Sachs (James Schneider) sees about 70% upside — [TipRanks, 10 Nov 2026](https://www.tipranks.com/news/goldman-sachs-sees-70-upside-for-micron-stock-heres-why) — but "says its rivals could offer better value" — [Barron's, 11 Nov 2026](https://www.barrons.com/articles/micron-stock-price-memory-chips-ca71fbc4)
6. **Access**
   - Listing: Nasdaq; Delaware corporation — [SEC submissions, MU](https://data.sec.gov/submissions/CIK0000723125.json)
   - Liquidity: average daily value traded about $25.4B (computed)
   - Index membership: S&P 500 and Nasdaq-100
   - ETF weights: SOXX 6.99%, PSI 4.68%, SMH 4.22%, QQQ 3.77% — [SOXX](https://stockanalysis.com/etf/soxx/holdings/); [PSI](https://stockanalysis.com/etf/psi/holdings/); [SMH](https://stockanalysis.com/etf/smh/holdings/); [QQQ](https://stockanalysis.com/etf/qqq/holdings/)
7. **Suggested label: attractive** (conditional on the supply-limited prior). The record P/B is the risk flag.
   - Why: the price already discounts a downturn starting within about two years. If FY2027–28 consensus is met, cumulative EPS covers about half the price.
   - The downside case is a price-to-book fall towards prior-trough levels of about 1–2x, if margins mean-revert faster than consensus expects.
   - Entry would look more attractive if:
     - the 16 Dec print and the FQ2 guide hold gross margin at about 85% or more, with evidence of contracted 2027 pricing and volume;
     - there is no sign of 2027 industry capex accelerating (Samsung, SK hynix);
     - P/B falls to 5x or below (about $612) or the price to 4x FY2027 EPS or below (about $706).

#### Intel (INTC): Tier 1
1. **Price and performance**
   - Price: $62.50 close on 11 Nov 2026 (+7.52% on the day). Pre-market on 12 Nov (6:11 AM) it was $61.17, -2.13% — [StockAnalysis INTC statistics](https://stockanalysis.com/stocks/intc/statistics/)
   - Size: market cap $332.19B; EV $328.01B — same source
   - 52-week closing range $33.62 (20 Nov 2025) to $140.94 (22 Jun 2026); intraday $32.89–$142.35 — [Nasdaq history INTC](https://api.nasdaq.com/api/quote/INTC/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD +69.4%; 12 months +65.0%; since 30 Dec 2022 +136%. Drawdown -55.7%. Same source.
   - Intel fell 29% on 30 Oct and 45% in October, its worst month on record per FactSet — [CNBC, 2 Nov 2026](https://www.cnbc.com/2026/11/02/intel-foundry-faces-critical-test-after-stocks-45percent-plunge-in-october.html)
2. **Multiples**
   - Current — [StockAnalysis INTC statistics](https://stockanalysis.com/stocks/intc/statistics/):
     - Trailing GAAP P/E: not meaningful (TTM GAAP net income -$12.03B)
     - StockAnalysis forward P/E 44.91
     - EV/EBITDA 17.14; EV/sales 5.48
     - P/B 2.89; companiesmarketcap shows 3.22 on a different book date
     - FCF yield 1.13%
     - No dividend
   - On consensus (computed from [StockAnalysis INTC forecast](https://stockanalysis.com/stocks/intc/forecast/)): P/E 41.9x FY2026 (EPS $1.49) and 34.9x FY2027 ($1.79)
   - Own history, fiscal year-ends 2021 to 2025 — [StockAnalysis INTC ratios](https://stockanalysis.com/stocks/intc/financials/ratios/):
     - Forward P/E 14.22, 18.19, 29.09, 29.07, 85.44
     - EV/EBITDA 6.27, 7.37, 24.76, 11.84, 15.68
     - P/B 2.19, 1.06, 1.93, 0.83, 1.37
   - Own history, calendar year-ends 2016–25 — [companiesmarketcap INTC P/S](https://companiesmarketcap.com/intel/ps-ratio/); [P/B](https://companiesmarketcap.com/intel/pb-ratio/):
     - P/S median 2.94, maximum 3.91, against 5.55 now
     - P/B median 2.36, maximum 3.31, against 3.22 now
     - Both measures are at or above the top of the ten-year range.
   - Peers — [GFS](https://stockanalysis.com/stocks/gfs/statistics/); [UMC (TPE:2303)](https://stockanalysis.com/quote/tpe/2303/statistics/); [SMIC (HKG:0981)](https://stockanalysis.com/quote/hkg/0981/statistics/):

     | Peer | Forward P/E | EV/EBITDA | P/B |
     |---|---|---|---|
     | TSMC (TPE:2330) | 16.42 | 15.88 | 8.62 |
     | Samsung Electronics (KRX:005930) | 2.92 | 3.49 | 2.17 |
     | GlobalFoundries | 18.07 | 11.01 | 2.00 |
     | UMC (TPE:2303) | 15.79 | 8.03 | 2.69 |
     | SMIC (HKG:0981) | 34.74 | 17.13 | 2.13 |
     | AMD | 36.73 | 80.79 | 13.26 |

3. **What the price assumes**
   - Consensus, 49 analysts, rated "Hold": FY2026 revenue $61.74B (+16.8%), FY2027 $69.13B (+12.0%); EPS $1.49 and then $1.79; FY2026 gross margin 41.19% — [StockAnalysis INTC forecast](https://stockanalysis.com/stocks/intc/forecast/)
   - Q4 2026 guidance: revenue $15.0–16.0B; gross margin 37.1% GAAP / 38.0% non-GAAP; EPS $0.10 GAAP / $0.25 non-GAAP — [Intel Q3 2026 8-K, 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/50863/000005086326000188/0000050863-26-000188.txt)
   - Reverse-DCF: the price needs year-5 EPS of about $5.0 (20x) to $6.7 (15x), meaning +30% to +40% a year after FY2027.
   - Bridge and successor: the price assumes the successor arrives and scales. That means external foundry customers for 14A and 18A, and advanced packaging (EMIB, Foveros, glass). Today's bridge (supply-constrained Xeon, with PCs slowing) does not support the multiple.
     - Intel released the 14A 0.9 process design kit in October.
     - It cites a collaboration with Lens Technology on precision glass processing for advanced packaging.
     - Risk language refers to securing "demand commitments from potential significant external customers" — [Intel Q3 2026 8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086326000188/0000050863-26-000188.txt)
4. **Cycle position**
   - Q3 2026 (ended 26 Sep; reported 29 Oct) — [Intel Q3 2026 8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086326000188/0000050863-26-000188.txt):
     - Revenue $16.5B (+21%): Client Computing and Physical AI $8.1B (-5%); Data Center and AI $7.3B (+78%); Intel Foundry $6.7B (+58%)
     - Gross margin 43.0% GAAP / 44.1% non-GAAP; non-GAAP EPS $0.52; operating cash flow $5.1B
     - Intel "completed a $23B public equity offering"
     - The CEO's priority is to "unlock additional supply" for Xeon; risk factors cite substrate and memory shortages
     - CFO: "we see the PC slowdown continuing at least through the first half of next year."
   - Gross-margin history (GAAP): 63.7% in 2014 (peak); 32.7% in 2024 (trough); 34.8% in 2025 — [SEC XBRL company facts, INTC](https://data.sec.gov/api/xbrl/companyfacts/CIK0000050863.json)
   - Share count up 15.09% year on year — [StockAnalysis INTC statistics](https://stockanalysis.com/stocks/intc/statistics/)
   - Government stake: Barron's refers to "the Trump administration's 10% stake" — [Barron's, 5 Nov 2026](https://www.barrons.com/articles/intel-stock-chips-trump-stake-15bae5a5)
5. **Near-term events**
   - Earnings: Q4 2026 results, expected late January 2027 (date not confirmed).
   - 14A and 18A customer decisions: timing not verified.
   - Possible further issuance: an S-3ASR shelf has been on file since 10 Aug 2026 — [SEC submissions, INTC](https://data.sec.gov/submissions/CIK0000050863.json)
   - Law-firm "shareholder investigation" notices followed the Q4 guide — [PR Newswire, 2 Nov 2026](https://www.prnewswire.com/news-releases/intc-shareholder-investigation-suewallst-notifies-investors-of-potential-securities-claims-involving-intel-302926630.html)
6. **Access**
   - Listing: Nasdaq; Delaware corporation — [SEC submissions, INTC](https://data.sec.gov/submissions/CIK0000050863.json)
   - Liquidity: average daily value traded about $9.4B (computed)
   - Index membership: S&P 500 and Nasdaq-100
   - ETF weights: SOXX 6.00%, PSI 4.01%, SMH 2.97%, QQQ 1.42% — ETF holdings pages as above
7. **Suggested label: stretched.**
   - Why: even after the -56% drawdown, P/S and P/B sit at or above their ten-year maxima. The forward P/E is about 35x FY2027 for a turnaround whose successors are not yet confirmed.
   - Entry would look more attractive if:
     - named external foundry customers make 14A or 18A commitments with prepayments;
     - non-GAAP gross margin recovers above about 45%;
     - the price is closer to 2x book (about $43) or 25x FY2027 EPS (about $45).

#### Amkor (AMKR): Tier 1
1. **Price and performance**
   - Price: $38.10 close on 11 Nov 2026 (+10.53% on the day). Pre-market on 12 Nov it was $37.10, -2.62% — [StockAnalysis AMKR statistics](https://stockanalysis.com/stocks/amkr/statistics/)
   - Size: market cap $9.44B; EV $9.78B — same source
   - 52-week closing range $30.19 (20 Nov 2025) to $93.55 (22 Jun 2026); intraday $29.76–$96.68 — [Nasdaq history AMKR](https://api.nasdaq.com/api/quote/AMKR/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD -3.5%; 12 months +11.2%; since 30 Dec 2022 +59%. Drawdown -59.3%. Same source.
2. **Multiples**
   - Current — [StockAnalysis AMKR statistics](https://stockanalysis.com/stocks/amkr/statistics/):
     - Trailing P/E 15.38
     - StockAnalysis forward P/E 13.91
     - EV/EBITDA 6.92; EV/sales 1.31
     - P/B 1.97 (book value per share about $19.34)
     - FCF yield -1.65% (TTM FCF -$156M)
     - Dividend yield 0.88%
   - On consensus (computed from [StockAnalysis AMKR forecast](https://stockanalysis.com/stocks/amkr/forecast/)):
     - P/E 15.2x FY2026 (EPS $2.50) and 13.7x FY2027 ($2.78)
     - FY2026 consensus FCF is -$1.16B
   - Own history, fiscal year-ends 2021 to 2025 — [StockAnalysis AMKR ratios](https://stockanalysis.com/stocks/amkr/financials/ratios/):
     - Trailing P/E 9.43, 7.67, 22.73, 17.90, 26.10
     - EV/EBITDA 4.93, 4.22, 7.57, 6.06, 8.78
     - P/B 2.04, 1.59, 2.05, 1.52, 2.17
   - Own history, calendar year-ends 2016–25 — [companiesmarketcap AMKR P/E](https://companiesmarketcap.com/amkor-technology/pe-ratio/); [P/S](https://companiesmarketcap.com/amkor-technology/ps-ratio/); [P/B](https://companiesmarketcap.com/amkor-technology/pb-ratio/):
     - P/E median 12.85 (range 7.30–26.1)
     - P/S median 0.80, against 1.27 now
     - P/B median 1.58 (range 0.85–2.35), against 1.95 now
   - Peers — [ASE (TPE:3711)](https://stockanalysis.com/quote/tpe/3711/statistics/); [ASX ADR](https://stockanalysis.com/stocks/asx/statistics/); [Powertech (TPE:6239)](https://stockanalysis.com/quote/tpe/6239/statistics/); [JCET (SHA:600584)](https://stockanalysis.com/quote/sha/600584/statistics/); [Tongfu (SHE:002156)](https://stockanalysis.com/quote/she/002156/statistics/); [Hana Microelectronics (BKK:HANA)](https://stockanalysis.com/quote/bkk/HANA/statistics/):

     | Peer | Forward P/E | EV/EBITDA | P/B |
     |---|---|---|---|
     | ASE Technology (TPE:3711) | 19.16 | 17.02 | 5.70 |
     | ASE ADR (ASX) | 18.91 | 17.04 | 5.52 |
     | Powertech (TPE:6239) | 14.56 | 8.17 | 2.62 |
     | JCET (SHA:600584) | 28.66 | 15.07 | 3.03 |
     | Tongfu Microelectronics (SHE:002156) | 40.12 | 14.77 | 3.22 |
     | Hana Microelectronics (BKK:HANA) | 27.18 | 13.98 | 1.32 |

     Amkor's EV/EBITDA of 6.9x is the lowest in its OSAT peer set.
3. **What the price assumes**
   - Consensus, 11 analysts: FY2026 revenue $7.53B (+12.2%), FY2027 $8.59B (+14.1%); EPS $2.50 and then $2.78; FY2026 gross margin 17.08% — [StockAnalysis AMKR forecast](https://stockanalysis.com/stocks/amkr/forecast/)
   - Q4 2026 guidance: revenue $1.9–2.0B; gross margin 18.0–19.0%; EPS $0.65–0.75 — [Amkor Q3 2026 8-K, 26 Oct 2026](https://www.sec.gov/Archives/edgar/data/1047127/000104712726000049/0001047127-26-000049.txt). Consensus had been $0.78 — [TheFly via TipRanks, 26 Oct 2026](https://www.tipranks.com/news/the-fly/amkor-technology-sees-q4-eps-65c-75c-consensus-78c-thefly-news)
   - Reverse-DCF: +2.6%/yr (20x) to +10.4%/yr (15x) after FY2027. At the ten-year median of 12.9x it is about +15%/yr. Computed.
   - Bridge and successor: consensus (+14% FY2027) and the multiple assign little value to a large 2.5D or US-plant step-up. The successor is the Arizona campus, expanded to $12B with phase 2 — [Business Wire, 8 Sep 2026](https://www.businesswire.com/news/home/20260908126184/en/Amkor-Technology-Announces-Phase-2-of-Arizona-Advanced-Packaging-and-Test-Campus-Expands-Investment-to-12-Billion/). Amkor also announced additional Korea investments under its multi-year NVIDIA agreements — [TheFly via TipRanks, 21 Oct 2026](https://www.tipranks.com/news/the-fly/amkor-technology-nvidia-partner-for-ai-infrastructure-thefly-news)
4. **Cycle position**
   - Q3 2026 (ended 30 Sep; reported 26 Oct) — [Amkor Q3 2026 8-K](https://www.sec.gov/Archives/edgar/data/1047127/000104712726000049/0001047127-26-000049.txt):
     - Net sales $1.991B (flat y/y, +5% q/q)
     - Gross margin 18.3% (14.3% a year earlier); operating margin 11.3%; EPS $0.76; EBITDA $435M
     - Mix: computing 26% of sales (19% a year earlier); communications 37% (51%)
     - FY2026 capex "updated to approximately $2.5 billion" (about 33% of revenue, computed)
     - Cash $2.4B; debt $2.5B
   - Gross-margin history (GAAP): 20.0% in 2021 (peak); 14.0% in 2025 — [SEC XBRL company facts, AMKR](https://data.sec.gov/api/xbrl/companyfacts/CIK0001047127.json)
   - Broker target cuts, 27 Oct (TheFly via TipRanks):
     - Needham $55 from $90 (Buy) — [link](https://www.tipranks.com/news/the-fly/amkor-technology-price-target-lowered-to-55-from-90-at-needham-thefly-news)
     - Goldman Sachs $56 from $65 (Neutral) — [link](https://www.tipranks.com/news/the-fly/amkor-technology-price-target-lowered-to-56-from-65-at-goldman-sachs-thefly-news)
     - Morgan Stanley $63 from $70 (Equal Weight) — [link](https://www.tipranks.com/news/the-fly/amkor-technology-price-target-lowered-to-63-from-70-at-morgan-stanley-thefly-news)
5. **Near-term events**
   - Earnings: Q4 2026 results, expected late January or early February 2027 (not confirmed).
   - Arizona phase timing: not verified.
   - Financing: the 5 May 2026 8-K (Items 1.01, 2.03 and 3.02, suggesting a financing that involves equity-linked securities) was not read; its terms are not verified — [SEC submissions, AMKR](https://data.sec.gov/submissions/CIK0001047127.json)
6. **Access**
   - Listing: Nasdaq; Delaware corporation — [SEC submissions, AMKR](https://data.sec.gov/submissions/CIK0001047127.json)
   - Liquidity: average daily value traded about $0.24B (computed)
   - Index membership: not in the S&P 500 or Nasdaq-100 (StockAnalysis lists)
   - ETF weights: PSI 2.33% — [PSI](https://stockanalysis.com/etf/psi/holdings/)
   - Short interest 9.28% of float — [StockAnalysis AMKR statistics](https://stockanalysis.com/stocks/amkr/statistics/)
7. **Suggested label: fair.**
   - Why: P/E is near history and EV/EBITDA is mid-range and below peers. Against that, FCF is negative while the capex cycle runs, and Q4 guidance was below consensus.
   - Entry would look more attractive if:
     - capex peaks and FCF turns positive;
     - gross margin holds at 18–19% or better while computing's share rises;
     - the price is about $30–33 (the ten-year median P/B of 1.58x ≈ $30.6; 12x FY2027 ≈ $33.4).

#### Lumentum (LITE): Tier 1
1. **Price and performance**
   - Price: $648.06 close on 11 Nov 2026. Pre-market on 12 Nov (6:12 AM) it was $627.29, -3.20% — [StockAnalysis LITE statistics](https://stockanalysis.com/stocks/lite/statistics/)
   - Size: market cap $58.77B; EV $58.22B — same source
   - 52-week closing range $226.86 (13 Nov 2025) to $1,133.40 (6 Oct 2026); intraday $215.35–$1,143.00 — [Nasdaq history LITE](https://api.nasdaq.com/api/quote/LITE/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD +75.8%; 12 months +156.7%; since 30 Dec 2022 +1,142%. Drawdown -42.8%. Same source.
2. **Multiples**
   - Current — [StockAnalysis LITE statistics](https://stockanalysis.com/stocks/lite/statistics/):
     - Trailing P/E: not meaningful (TTM GAAP net income -$6.58B; the cause of the GAAP loss was not verified)
     - StockAnalysis forward P/E 22.18
     - EV/EBITDA 50.61; EV/sales 15.56
     - P/B 12.84
     - FCF yield 0.61%
     - No dividend
   - On consensus (computed from [StockAnalysis LITE forecast](https://stockanalysis.com/stocks/lite/forecast/)):
     - P/E 26.0x FY2027 (EPS $24.94; FY ending Jun 2027) and 16.1x FY2028 ($40.13)
     - EV/sales 8.7x and 5.5x
   - Own history, fiscal year-ends FY2022 to FY2026 — [StockAnalysis LITE ratios](https://stockanalysis.com/stocks/lite/financials/ratios/):
     - Forward P/E 11.78, 20.71, 54.57, 25.92, 51.57
     - EV/EBITDA 9.89, 23.80, n/a, 134.61, 79.56
     - P/B 2.86, 2.88, 3.60, 5.80, 13.69
   - Own history, calendar year-ends 2016–25 — [companiesmarketcap LITE P/S](https://companiesmarketcap.com/lumentum/ps-ratio/); [P/B](https://companiesmarketcap.com/lumentum/pb-ratio/):
     - P/S median 3.04, against 15.7 now
     - P/B median 3.62, against 12.7 now
   - Peers — [Zhongji Innolight (SHE:300308)](https://stockanalysis.com/quote/she/300308/statistics/); [Eoptolink (SHE:300502)](https://stockanalysis.com/quote/she/300502/statistics/); [Suzhou TFC Optical (SHE:300394)](https://stockanalysis.com/quote/she/300394/statistics/); [Accelink (SHE:002281)](https://stockanalysis.com/quote/she/002281/statistics/); [Sumitomo Electric (TYO:5802)](https://stockanalysis.com/quote/tyo/5802/statistics/); [Furukawa Electric (TYO:5801)](https://stockanalysis.com/quote/tyo/5801/statistics/); [Fujikura (TYO:5803)](https://stockanalysis.com/quote/tyo/5803/statistics/); [AAOI](https://stockanalysis.com/stocks/aaoi/statistics/):

     | Peer | Forward P/E | EV/EBITDA | P/B |
     |---|---|---|---|
     | Coherent | 20.00 | 29.35 | — |
     | Zhongji Innolight (SHE:300308) | 9.14 | 16.08 | 6.08 |
     | Eoptolink (SHE:300502) | 9.58 | 16.14 | 10.67 |
     | Suzhou TFC Optical (SHE:300394) | 28.85 | 47.67 | — |
     | Accelink (SHE:002281) | 34.87 | 35.85 | — |
     | Sumitomo Electric (TYO:5802) | 11.87 | 7.28 | — |
     | Furukawa Electric (TYO:5801) | 12.90 | 11.04 | — |
     | Fujikura (TYO:5803) | 13.86 | 12.66 | — |
     | Applied Optoelectronics | 18.30 | — | — |

3. **What the price assumes**
   - Consensus, 25 analysts: FY2027 revenue $6.66B (+121%) with gross margin 54.24%; FY2028 $10.53B (+58%); EPS $24.94 and then $40.13 — [StockAnalysis LITE forecast](https://stockanalysis.com/stocks/lite/forecast/)
   - Q2 FY2027 guidance: revenue $1.575–1.625B; non-GAAP operating margin 45–46%; non-GAAP EPS $5.90–6.20. Management says "we secured our second major NPO/CPO win, backed by purchase commitments exceeding $5 billion" and sees optical circuit switching becoming "a multi-billion-dollar annual revenue stream" — [Lumentum Q1 FY27 8-K, 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/1633978/000162828026068655/0001628280-26-068655.txt)
   - Reverse-DCF, standalone: +8%/yr (20x) to +18%/yr (15x) after FY2028.
   - Bridge and successor: consensus assumes the bridge (electro-absorption modulated lasers and cloud modules) and the successor (continuous-wave and ultra-high-power lasers for CPO/NPO, plus optical circuit switches) both ramp on schedule.
   - Deal linkage: the price now tracks 4.5 × MRVL less a deal spread. The implied deal value is 4.5 × $168.80 = $759.60, against $648.06, a 14.7% discount (17.2% gross spread). With about 19 months to the expected 1H 2028 close, that is roughly 10–11% a year. Computed from [Marvell 8-K](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442717/d352474d8k.htm) and the closes.
4. **Cycle position**
   - Q1 FY2027 (ended 26 Sep 2026; reported 2 Nov) — [Lumentum Q1 FY27 8-K](https://www.sec.gov/Archives/edgar/data/1633978/000162828026068655/0001628280-26-068655.txt):
     - Revenue $1,262.6M (+25.5% q/q, +136.5% y/y): Components $754.2M (+98.9% y/y); Systems $508.4M (+228.8% y/y)
     - Gross margin 51.0% GAAP / 53.2% non-GAAP; operating margin 28.5% GAAP / 42.3% non-GAAP; non-GAAP EPS $4.57
     - Cash $2.0B, down $758.8M on the quarter
   - Gross-margin history (GAAP): 46.0% in FY2022 (prior peak); 18.5% in FY2024 (trough); 41.7% in FY2026. The current 51% is above the prior peak — [SEC XBRL company facts, LITE](https://data.sec.gov/api/xbrl/companyfacts/CIK0001633978.json)
5. **Near-term events**
   - Merger milestones: S-4, both shareholder votes, HSR and other approvals (see Marvell).
   - Earnings: Q2 FY2027 results, expected early February 2027 (not confirmed).
   - Broker targets, all reflecting MRVL's price (TheFly via TipRanks):
     - UBS $686 from $960 (Neutral), 10 Nov — [link](https://www.tipranks.com/news/the-fly/lumentum-price-target-lowered-to-686-from-960-at-ubs-thefly-news)
     - Bernstein $635 from $900 on 9 Nov, then $700 on 10 Nov "to reflect Marvell's latest share price" — [link](https://www.tipranks.com/news/the-fly/lumentum-price-target-raised-to-700-from-635-at-bernstein-thefly-news)
6. **Access**
   - Listing: Nasdaq; Delaware corporation — [SEC submissions, LITE](https://data.sec.gov/submissions/CIK0001633978.json)
   - Liquidity: average daily value traded about $4.3B (computed)
   - Index membership: S&P 500 and Nasdaq-100. Lumentum would leave both at closing.
   - ETF weights: not in the top-25 lists of SMH, SOXX, PSI or QQQ checked.
   - Short interest 8.58% of float — [StockAnalysis LITE statistics](https://stockanalysis.com/stocks/lite/statistics/)
7. **Suggested label: cannot assess (standalone; the price is deal-linked).**
   - Standalone, the multiples are at the top of its own history (P/S 15.7x against a 3.0x ten-year median). The 16x FY2028 P/E looks moderate if consensus is met.
   - The entry today is effectively MRVL exposure at about a 15% discount to the deal terms, plus completion risk.
   - The picture would become clearer, or the entry more attractive, if:
     - the votes and regulatory path become clear, or the spread narrows;
     - the deal breaks: Lumentum would then revert to standalone ranges, and the termination fees ($2.9B, $5.8B and $3.2B) would apply.

#### Coherent (COHR): Tier 1
1. **Price and performance**
   - Price: $234.51 close on 11 Nov 2026. Pre-market on 12 Nov it was $227.00, -3.20% — [StockAnalysis COHR statistics](https://stockanalysis.com/stocks/cohr/statistics/)
   - Size: market cap $46.19B; EV $48.78B — same source
   - 52-week closing range $135.61 (20 Nov 2025) to $426.89 (2 Jun 2026); intraday $130.42–$440.00 — [Nasdaq history COHR](https://api.nasdaq.com/api/quote/COHR/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD +27.1%; 12 months +48.4%; since 30 Dec 2022 +568%. Drawdown -45.1%. Same source.
2. **Multiples**
   - Current — [StockAnalysis COHR statistics](https://stockanalysis.com/stocks/cohr/statistics/):
     - Trailing GAAP P/E 48.30
     - StockAnalysis forward P/E 20.00
     - EV/EBITDA 29.35; EV/sales 6.17
     - P/B 4.08
     - FCF yield -3.97% (TTM FCF -$1.83B)
     - No dividend
   - On consensus (computed from [StockAnalysis COHR forecast](https://stockanalysis.com/stocks/cohr/forecast/)): P/E 22.5x FY2027 (EPS $10.41) and 14.9x FY2028 ($15.79); EV/sales 4.4x and 3.1x
   - Own history, fiscal year-ends FY2022 to FY2026 — [StockAnalysis COHR ratios](https://stockanalysis.com/stocks/cohr/financials/ratios/):
     - Forward P/E 12.36, 25.14, 26.53, 21.26, 53.01
     - EV/EBITDA 10.66, 14.03, 25.15, 18.13, 55.16
     - P/B 1.24, 0.98, 1.39, 1.64, 6.87
   - Own history, calendar year-ends 2016–25 — [companiesmarketcap COHR P/S](https://companiesmarketcap.com/coherent/ps-ratio/); [P/B](https://companiesmarketcap.com/coherent/pb-ratio/):
     - P/S median 2.21 (maximum 6.60 in 2017), against 5.84 now
     - P/B median 1.92 (maximum 7.27), against 4.11 now
   - Peers: as for Lumentum. Lumentum itself trades at 22.18x forward and 50.61x EV/EBITDA.
3. **What the price assumes**
   - Consensus, 26 analysts: FY2027 revenue $11.21B (+57%) with gross margin 41.24%; FY2028 $15.62B (+39%); EPS $10.41 and then $15.79 — [StockAnalysis COHR forecast](https://stockanalysis.com/stocks/cohr/forecast/)
   - Q2 FY2027 guidance: revenue $2.55–2.75B; non-GAAP gross margin 40–42%; EPS $2.28–2.48 — [Coherent Q1 FY27 8-K, 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/820318/000119312526447200/0001193125-26-447200.txt). Management targets:
     - "We expect fiscal 2027 pro forma revenue growth to exceed 60%"
     - first $3B quarter by the end of FY2027 and first $4B quarter in FY2028
     - non-GAAP gross margin above 45% "before the end of calendar 2028"
   - Reverse-DCF: +5.4%/yr (20x) to +14.7%/yr (15x) after FY2028. Computed.
   - Bridge and successor: consensus assumes the transceiver bridge keeps growing and that the successor (continuous-wave and CPO lasers) arrives. The call summary mentions "a rapid PhotonLink ramp" — [StockAnalysis transcript summary, 4 Nov 2026](https://stockanalysis.com/stocks/cohr/). The roughly 15x FY2028 multiple does not assume a very long-lived bridge.
4. **Cycle position**
   - Q1 FY2027 (ended 30 Sep; reported 4 Nov) — [Coherent Q1 FY27 8-K](https://www.sec.gov/Archives/edgar/data/820318/000119312526447200/0001193125-26-447200.txt):
     - Revenue $2,370.3M (+49.9% y/y, +15.9% q/q; +56% pro forma)
     - Gross margin 39.1% GAAP / 40.6% non-GAAP; operating margin 15.9% GAAP / 23.2% non-GAAP
     - EPS $1.90 GAAP / $2.09 non-GAAP
     - TheFly's headline "Q1 EPS $1.90, consensus $1.97" appears to compare GAAP EPS with consensus — [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/coherent-reports-q1-eps-1-90-consensus-1-97-thefly-news)
   - Gross-margin history (GAAP): 40.0% in FY2017 (II-VI peak); 30.9% in FY2024 (trough); 37.5% in FY2026 — [SEC XBRL company facts, COHR](https://data.sec.gov/api/xbrl/companyfacts/CIK0000820318.json)
   - Negative TTM FCF of -$1.83B is consistent with heavy capacity build.
   - Share count: StockAnalysis shows shares +20.85% year on year. My calculation from the release implies about +6% in diluted shares (net income ÷ EPS). The discrepancy is unexplained.
   - Broker target changes, 5–6 Nov (TheFly via TipRanks):
     - BofA $240 from $400 (Neutral) — [link](https://www.tipranks.com/news/the-fly/coherent-price-target-lowered-to-240-from-400-at-bofa-thefly-news)
     - Craig-Hallum $310 from $480 (Buy)
     - B. Riley $228 from $262 (Neutral)
     - Stifel $450 from $420 (Buy)
     - Citi $440 from $420 (Buy)
5. **Near-term events**
   - Earnings: Q2 FY2027 results, expected early February 2027 (not confirmed).
   - Coherent was the best S&P 500 performer, with AMD, since the 5 Nov sell-off — [Barron's, 10 Nov 2026](https://www.barrons.com/articles/amd-stock-coherent-ai-selloff-e457aa02)
6. **Access**
   - Listing: NYSE; Pennsylvania corporation — [SEC submissions, COHR](https://data.sec.gov/submissions/CIK0000820318.json)
   - Liquidity: average daily value traded about $2.26B (computed)
   - Index membership: S&P 500
   - ETF weights: not in the top-25 lists checked.
7. **Suggested label: fair.**
   - Why: the FY2028 multiple of about 15x is undemanding if consensus holds. But P/S and P/B are well above their ten-year medians, FCF is negative, and the successor laser ramp is assumed.
   - Entry would look more attractive if:
     - FCF turns positive;
     - continuous-wave or CPO laser revenue becomes visible;
     - the price is about $187–189 (18x FY2027, 12x FY2028).

#### Credo (CRDO): Tier 1
1. **Price and performance**
   - Price: $141.41 close on 11 Nov 2026 (+8.94% on the day). Pre-market on 12 Nov (7:25 AM) it was $135.55, -4.14% — [StockAnalysis CRDO statistics](https://stockanalysis.com/stocks/crdo/statistics/)
   - Size: market cap $26.58B; EV $25.84B — same source
   - 52-week closing range $87.81 (30 Mar 2026) to $302.52 (22 Jun 2026); intraday $86.48–$308.67 — [Nasdaq history CRDO](https://api.nasdaq.com/api/quote/CRDO/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD -1.7%; 12 months -10.8%; since 30 Dec 2022 +962%. Drawdown -53.3%. Same source.
2. **Multiples**
   - Current — [StockAnalysis CRDO statistics](https://stockanalysis.com/stocks/crdo/statistics/):
     - Trailing P/E 49.94
     - StockAnalysis forward P/E 19.39
     - EV/EBITDA 47.57; EV/sales 16.24
     - P/B 9.73
     - FCF yield 1.65%
     - No dividend
   - On consensus (computed from [StockAnalysis CRDO forecast](https://stockanalysis.com/stocks/crdo/forecast/)):
     - P/E 22.4x FY2027 (EPS $6.31; FY ending Apr 2027) and 14.6x FY2028 ($9.71)
     - EV/sales 10.3x and 6.7x
     - FY2027 consensus FCF yield 3.1%
   - Own history, fiscal year-ends FY2022 to FY2026 — [StockAnalysis CRDO ratios](https://stockanalysis.com/stocks/crdo/financials/ratios/):
     - Forward P/E 112.65, 94.44, 75.42, 43.02, 38.69
     - P/B 4.78, 3.45, 5.61, 12.02, 16.48
   - Own history, calendar year-ends 2022–25 — [companiesmarketcap CRDO P/S](https://companiesmarketcap.com/credo-technology/ps-ratio/):
     - P/S median 19.95, against 16.7 now
     - P/B median 14.54, against 9.74 now
   - Peers:

     | Peer | Forward P/E | EV/EBITDA |
     |---|---|---|
     | Astera Labs | 33.57 | 94.58 |
     | Marvell | 29.92 | 52.47 |
     | Montage (SHA:688008) | 36.76 | 58.89 |
     | Alchip (TPE:3661) | 18.20 | 27.60 |
     | Semtech | 23.15 | 66.95 |
     | MACOM | 25.50 | 50.65 |

     - Montage's trailing P/E of 3.21 looks anomalous on StockAnalysis.
     - The Parade Technologies (TPE:4966) page returned 404 — [Montage](https://stockanalysis.com/quote/sha/688008/statistics/); [SMTC](https://stockanalysis.com/stocks/smtc/statistics/); [MTSI](https://stockanalysis.com/stocks/mtsi/statistics/)
3. **What the price assumes**
   - Consensus, 20 analysts: FY2027 revenue $2.50B (+87%), FY2028 $3.88B (+55%); EPS $6.31 and then $9.71; gross margin about 67.7% — [StockAnalysis CRDO forecast](https://stockanalysis.com/stocks/crdo/forecast/)
   - Q2 FY2027 guidance: revenue $525–535M; non-GAAP gross margin 67–69% — [Credo Q1 FY27 8-K, 1 Sep 2026](https://www.sec.gov/Archives/edgar/data/1807794/000162828026059795/0001628280-26-059795.txt)
   - The call summary says FY2027 guidance is for more than 85% revenue growth, with optical revenue "expected to exceed $600 million in fiscal 2027" — [StockAnalysis transcript summary](https://stockanalysis.com/stocks/crdo/)
   - Reverse-DCF: +4.7%/yr (20x) to +13.6%/yr (15x) after FY2028. Computed.
   - Bridge and successor: consensus assumes both pieces.
     - The active-electrical-cable bridge keeps growing: AEC unit growth drove more than 90% of the year-on-year revenue increase — [Credo 10-Q](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm)
     - The optical successor scales to about 24% of FY2027 revenue (computed: $600M of $2.5B).
     - The roughly 15x FY2028 multiple does not assume the bridge lasts beyond FY2028.
   - DustPhotonics acquisition — [Credo 10-Q, quarter ended 1 Aug 2026](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm):
     - Closed on 28 May 2026
     - "total purchase consideration of $1.3 billion"; the table totals $1,251.1M: cash $769.6M, shares $169.1M, replacement awards $2.5M, contingent consideration $310.0M
     - Goodwill $895.8M; intangibles $361.7M
4. **Cycle position**
   - Q1 FY2027 (ended 1 Aug 2026; reported 1 Sep) — [Credo Q1 FY27 8-K](https://www.sec.gov/Archives/edgar/data/1807794/000162828026059795/0001628280-26-059795.txt):
     - Revenue $479.0M (+9.6% q/q, +114.7% y/y)
     - Gross margin 64.5% GAAP / 68.0% non-GAAP; non-GAAP EPS $1.20
     - Cash $764.3M
   - Customer concentration — [Credo 10-Q](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm):
     - Contracting-party basis: Customer A 43%, Customer B 28%
     - End-customer basis: 33%, 28%, 13% and 10%
     - Receivables: Customer A is 57%
   - Commitments — same source:
     - Inventory $313.1M, up from $250.8M
     - Unconditional purchase obligations $222.2M
     - Capacity-reservation deposits $88.4M, with a further $102.4M due in FY2027
   - The non-GAAP gross margin of 68.0% is at the top of the FY2022–26 range of 57.7–68.0% — [StockAnalysis CRDO forecast](https://stockanalysis.com/stocks/crdo/forecast/)
   - The stock fell more than 9% after the September print — [Invezz, 2 Sep 2026](https://invezz.com/news/2026/09/02/credo-technology-stock-has-slipped-after-earnings-how-low-can-it-get/)
5. **Near-term events**
   - Earnings: Q2 FY2027 results on 1 Dec 2026 after the close (confirmed) — [Business Wire, 11 Nov 2026](https://www.businesswire.com/news/home/20261111758581/en/Credo-Schedules-Second-Quarter-Fiscal-Year-2027-Financial-Results-Conference-Call/); [StockAnalysis CRDO statistics](https://stockanalysis.com/stocks/crdo/statistics/)
   - Index membership: not in the S&P 500 or Nasdaq-100. Candidacy is not verified.
6. **Access**
   - Listing: Nasdaq; Cayman Islands holding company — [SEC submissions, CRDO](https://data.sec.gov/submissions/CIK0001807794.json)
   - Liquidity: average daily value traded about $1.24B (computed)
   - ETF weights: SOXX 1.40% — [SOXX](https://stockanalysis.com/etf/soxx/holdings/)
   - Short interest 5.66% — [StockAnalysis CRDO statistics](https://stockanalysis.com/stocks/crdo/statistics/)
7. **Suggested label: fair.**
   - Why: it is the lowest forward multiple in its connectivity peer group and below its own short history on P/S and P/B. Against that, two contracting parties make up 71% of revenue, and consensus needs both the copper bridge and the optical successor.
   - Entry would look more attractive if:
     - the 1 Dec print confirms the optical ramp is on track to exceed $600M in FY2027 and AEC growth is intact;
     - customer concentration falls;
     - the price is about $114–117 (18x FY2027, 12x FY2028).

#### Astera Labs (ALAB): Tier 1
1. **Price and performance**
   - Price: $230.91 close on 11 Nov 2026 (+6.81% on the day). Pre-market on 12 Nov it was $225.00, -2.56% — [StockAnalysis ALAB statistics](https://stockanalysis.com/stocks/alab/statistics/)
   - Size: market cap $40.36B; EV $39.03B — same source
   - 52-week closing range $100.27 (30 Mar 2026) to $483.02 (30 Jun 2026); intraday $97.89–$499.48 — [Nasdaq history ALAB](https://api.nasdaq.com/api/quote/ALAB/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD +38.8%; 12 months +37.8%; +272% since the first close in the data ($62.03 on 20 Mar 2024; the stock listed in 2024). Drawdown -52.2%. Same source.
2. **Multiples**
   - Current — [StockAnalysis ALAB statistics](https://stockanalysis.com/stocks/alab/statistics/):
     - Trailing P/E 91.13
     - StockAnalysis forward P/E 33.57
     - EV/EBITDA 94.58; EV/sales 25.08
     - P/B 20.18
     - FCF yield 0.85%
     - No dividend
   - On consensus (computed from [StockAnalysis ALAB forecast](https://stockanalysis.com/stocks/alab/forecast/)): P/E 52.7x FY2026 (EPS $4.38) and 32.5x FY2027 ($7.10); EV/sales 19.2x and 11.6x
   - Own history — [StockAnalysis ALAB ratios](https://stockanalysis.com/stocks/alab/financials/ratios/); [companiesmarketcap ALAB P/S](https://companiesmarketcap.com/astera-labs/ps-ratio/):
     - Fiscal year-end forward P/E 121.76 (2024) and 76.61 (2025)
     - EV/EBITDA 149.77 (2025)
     - Calendar year-end P/S 56.6 (2024) and 35.6 (2025), against 25.9 now
   - Peers: Credo (19.39x forward, 47.57x EV/EBITDA), Marvell (29.92, 52.47), Montage (36.76, 58.89), Broadcom (19.84, 32.21), Alchip (18.20, 27.60)
3. **What the price assumes**
   - Consensus, 25 analysts: FY2026 revenue $2.03B (+138%), FY2027 $3.36B (+66%); EPS $4.38 and then $7.10 — [StockAnalysis ALAB forecast](https://stockanalysis.com/stocks/alab/forecast/)
   - Q4 guidance: revenue $730–750M against $655.7M consensus; gross margin about 72%; EPS $1.62–1.66 against $1.42 — [TheFly via TipRanks, 3 Nov 2026](https://www.tipranks.com/news/the-fly/astera-labs-sees-q4-eps-1-62-1-66-consensus-1-42-thefly-news)
   - Computed: the Q4 guide midpoint annualises to $2.96B, so FY2027 consensus is only about 13% above the Q4 run-rate. Consensus may be conservative.
   - Reverse-DCF: +28%/yr (20x) to +38%/yr (15x) after FY2027. Computed.
   - Bridge and successor: the price assumes the successors keep compounding — Scorpio fabric switches (now the largest product family) and UALink and optical products. The retimer bridge alone would not support it — [GlobeNewswire, 3 Nov 2026](https://www.globenewswire.com/news-release/2026/11/03/3394769/0/en/astera-labs-reports-third-quarter-2026-financial-results.html)
4. **Cycle position**
   - Q3 2026 (reported 3 Nov) — [GlobeNewswire release](https://www.globenewswire.com/news-release/2026/11/03/3394769/0/en/astera-labs-reports-third-quarter-2026-financial-results.html); [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/astera-labs-reports-q3-eps-1-32-consensus-1-19-thefly-news):
     - Revenue $584.9M (+49% q/q, +154% y/y)
     - Non-GAAP gross margin 72.4%; non-GAAP EPS $1.32 against $1.19 consensus
   - The shares fell despite the beat — [Barron's, 4 Nov 2026](https://www.barrons.com/articles/astera-labs-stock-earnings-334d76c4)
   - Broker target changes on 4 Nov (TheFly via TipRanks):
     - RBC $400 from $500
     - TD Cowen $225 from $300 (Hold)
     - Susquehanna $258 from $310 (Neutral)
     - UBS $290 from $300 (Neutral)
     - Stifel $370 from $460
     - Jefferies $350 from $450
     - Morgan Stanley $389 from $382
     - Northland upgraded to Outperform ($315)
     - BMO initiated at Outperform ($375)
     - [Example: RBC](https://www.tipranks.com/news/the-fly/astera-labs-price-target-lowered-to-400-from-500-at-rbc-capital-thefly-news)
5. **Near-term events**
   - Earnings: Q4 results, expected around February 2027 (not confirmed).
   - Index membership: Nasdaq-100 member, not in the S&P 500 — [Nasdaq-100 list](https://stockanalysis.com/list/nasdaq-100-stocks/)
6. **Access**
   - Listing: Nasdaq; Delaware corporation — [SEC submissions, ALAB](https://data.sec.gov/submissions/CIK0001736297.json)
   - Liquidity: average daily value traded about $1.15B (computed)
   - ETF weights: SOXX 1.96%, SMH 0.86% — ETF holdings pages as above
7. **Suggested label: stretched.**
   - Why: it has the highest multiples in its peer group, and the reverse-DCF needs roughly 28–38%/yr EPS growth after FY2027.
   - Entry would look more attractive if:
     - the price is about $178 (25x FY2027) or EV is below about 9x FY2027 sales;
     - consensus moves up towards the Q4 run-rate, which would lower the forward multiple without any price change;
     - Scorpio and UALink revenue is shown to be diversified across customers.

#### Fabrinet (FN): Tier 1
1. **Price and performance**
   - Price: $369.01 close on 11 Nov 2026. Pre-market on 12 Nov it was $359.80, -2.50% — [StockAnalysis FN statistics](https://stockanalysis.com/stocks/fn/statistics/)
   - Size: market cap $13.18B; EV $12.50B — same source
   - 52-week closing range $292.97 (5 Nov 2026) to $746.47 (14 May 2026); intraday $286.07–$748.89 — [Nasdaq history FN](https://api.nasdaq.com/api/quote/FN/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)
   - Returns: YTD -18.9%; 12 months -17.9%; since 30 Dec 2022 +188%. Drawdown -50.6%. Same source.
2. **Multiples**
   - Current — [StockAnalysis FN statistics](https://stockanalysis.com/stocks/fn/statistics/):
     - Trailing P/E 27.86
     - StockAnalysis forward P/E 17.59
     - EV/EBITDA 21.19; EV/sales 2.43
     - P/B 5.26
     - FCF yield -1.45%
     - No dividend; aggregate buyback programme $637.3M
   - On consensus (computed from [StockAnalysis FN forecast](https://stockanalysis.com/stocks/fn/forecast/)): P/E 18.7x FY2027 (EPS $19.72) and 15.3x FY2028 ($24.11)
   - Own history, fiscal year-ends FY2022 to FY2026 — [StockAnalysis FN ratios](https://stockanalysis.com/stocks/fn/financials/ratios/):
     - Trailing P/E 15.28, 19.02, 29.87, 31.85, 39.75
     - Forward P/E 13.05, 17.25, 26.09, 26.57, 32.17 (median 26.1)
     - EV/EBITDA 10.60, 13.92, 24.75, 25.50, 33.66
   - Own history, calendar year-ends 2016–25 — [companiesmarketcap FN P/E](https://companiesmarketcap.com/fabrinet/pe-ratio/); [P/S](https://companiesmarketcap.com/fabrinet/ps-ratio/); [P/B](https://companiesmarketcap.com/fabrinet/pb-ratio/):
     - P/E median 21.6 (range 12.0–43.3)
     - P/S median 1.78, against 2.57 now
     - P/B median 3.08, against 5.37 now
   - Peers — [CLS](https://stockanalysis.com/stocks/cls/statistics/); [Jabil](https://stockanalysis.com/stocks/jbl/statistics/):

     | Peer | Forward P/E | EV/EBITDA |
     |---|---|---|
     | Celestica | 13.36 | 16.26 |
     | Jabil | 14.63 | 11.64 |
     | Hana Microelectronics (BKK:HANA) | 27.18 | 13.98 |
     | Hon Hai (TPE:2317) | 11.57 | 7.78 |
     | Foxconn Industrial Internet (SHA:601138) | 11.53 | 12.46 |
     | Quanta (TPE:2382) | 9.30 | 8.92 |
     | Zhongji Innolight (SHE:300308), module maker | 9.14 | 16.08 |

3. **What the price assumes**
   - Consensus, 9 analysts: FY2027 revenue $6.60B (+42%), FY2028 $8.07B (+22%); EPS $19.72 and then $24.11; gross margin about 12.3% — [StockAnalysis FN forecast](https://stockanalysis.com/stocks/fn/forecast/)
   - Q2 FY2027 guidance: revenue $1.60–1.65B; non-GAAP EPS $4.77–4.92 (consensus $4.43) — [Fabrinet Q1 FY27 8-K, 2 Nov 2026](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000034/0001408710-26-000034.txt); [TheFly via TipRanks](https://www.tipranks.com/news/the-fly/fabrinet-sees-q2-eps-4-77-4-92-consensus-4-43-thefly-news)
   - Reverse-DCF: +6.3%/yr (20x) to +15.7%/yr (15x) after FY2028. Computed.
   - Bridge and successor: consensus FY2028 growth slows to +22%, so it does not assume a large co-packaged optical-engine step-up. The multiple sits near its ten-year median P/E.
4. **Cycle position**
   - Q1 FY2027 (ended 25 Sep; reported 2 Nov) — [Fabrinet Q1 FY27 8-K](https://www.sec.gov/Archives/edgar/data/1408710/000140871026000034/0001408710-26-000034.txt):
     - Revenue $1,474.5M (+51%)
     - EPS $2.86 GAAP / $4.34 non-GAAP
     - Buyback authorisation raised by $103M to $637.3M
   - Gross margin has stayed in a 10.8–12.7% band since FY2012 (12.0% in FY2026) — [SEC XBRL company facts, FN](https://data.sec.gov/api/xbrl/companyfacts/CIK0001408710.json)
   - TTM FCF is negative, consistent with capacity build.
   - Customer concentration: the release cites only "our reliance on a small number of customers"; percentages were not verified.
   - Broker targets (TheFly via TipRanks):
     - JPMorgan $465 from $695 (Neutral) on 2 Nov, then $475 on 3 Nov
     - Barclays $496 from $739 (Overweight)
     - B. Riley $364 from $385 (Neutral)
     - [Barclays](https://www.tipranks.com/news/the-fly/fabrinet-price-target-lowered-to-496-from-739-at-barclays-thefly-news)
5. **Near-term events**
   - Earnings: Q2 FY2027 results, expected early February 2027 (not confirmed).
   - Programme transitions at large optical customers: not verified.
6. **Access**
   - Listing: NYSE; Cayman Islands company with operations in Thailand — [SEC submissions, FN](https://data.sec.gov/submissions/CIK0001408710.json)
   - Liquidity: average daily value traded about $0.45B (computed)
   - Index membership: not in the S&P 500
   - ETF weights: none in the top-25 lists checked.
   - Institutional ownership 99.5% — [StockAnalysis FN statistics](https://stockanalysis.com/stocks/fn/statistics/)
7. **Suggested label: fair.**
   - Why: the forward P/E is below its own five-year fiscal-year-end median (26x), but P/S and P/B are above their ten-year medians and FCF is negative.
   - Entry would look more attractive if:
     - FCF turns positive;
     - revenue from assembling co-packaged optical engines becomes visible;
     - the price is about $289–296 (12x FY2028, 15x FY2027, close to the 5 Nov low).

### Inferences
- The market has applied a "peak-cycle discount" unevenly. It is most extreme for memory: Micron and its Korean and Japanese peers trade at 2–5x forward earnings despite record guidance. It is moderate for NVIDIA, which needs about zero growth after FY2028. It is absent for Intel and Astera Labs, whose prices need roughly 28–40%/yr EPS growth after FY2027.
- In almost every case consensus assumes the successor product arrives on schedule. Today's multiples on the optics and connectivity names (Credo, Coherent, Fabrinet, Lumentum standalone) sit at 15–16x FY2028. That is consistent with partial doubt about successor timing, not with full belief in it.
- Several names price as cheaper on next-year multiples than on their own five-year fiscal-year-end medians: NVIDIA, Broadcom, Marvell, Fabrinet and Credo. On sales and book multiples, almost all remain above their ten-year medians, because margins are near record. Using P/B or P/S medians as "fair value" would assume those margins revert.
- For Micron, P/E and P/B give opposite messages. P/E (4.6x) looks like a peak-cycle trough multiple, while P/B (6.6x, a record) looks like a high multiple. The likely reconciliation is that the market expects a high but temporary return on equity. That makes P/B the better downside gauge if the cycle turns.

### Gaps
- Consensus for a third fiscal year was not available on free StockAnalysis pages. Consensus margins beyond the first fiscal year were also unavailable.
- Ten-year EV/EBITDA history was not available. Ten-year P/E medians mix negative values for Micron, Intel, Lumentum and Coherent, so I quote positive-only figures where noted.
- Marvell's ten-year history was not available (no companiesmarketcap page found).
- Broadcom's AI backlog and NVIDIA's purchase and supply commitments were not in the portions of the releases read; they appear in calls or 10-Qs that were not read.
- Customer concentration percentages for NVIDIA, Broadcom, Marvell, Lumentum, Coherent, Fabrinet and Astera Labs were not verified. Only Credo's were.
- The cause of Lumentum's large GAAP loss (TTM -$6.58B) and of Coherent's share-count change was not verified.
- The governance reports on NVIDIA are press reports; the board's decision was pending when checked.

## Key Question 2: Where is each company in its cycle (orders, pricing, capacity additions, inventory, customer concentration in the latest quarter)?

### Takeaway
Reported fundamentals are still in an up-cycle across the group. Every Tier 1 company except Amkor and Intel guided the next quarter up by double digits sequentially, and margins at NVIDIA, Micron, Lumentum and Credo are at or above prior peaks. Share prices, however, sit 27–59% below their mid-2026 highs. Late-cycle markers are visible:
- inventory build at NVIDIA (+48% in six months) and Micron (+24% year on year);
- suppliers financing customers: NVIDIA's $105B-capped OpenAI lease guarantees, Marvell's Google warrant, and reported Broadcom and NVIDIA deals with Anthropic and Meta;
- heavy capacity spending with negative FCF at Amkor, Coherent, Fabrinet and Celestica;
- high customer concentration: Credo's two largest customers are 71% of revenue.

The step-down in Intel's and Amkor's guidance is the main exception.

### Cited Findings

#### Cross-company cycle snapshot (latest reported quarter; sources as in the Key Question 1 company sections)

| Company | Latest quarter (reported) | Revenue, y/y | Next-quarter guide | Gross margin now vs history | Orders, backlog, inventory, capacity signals |
|---|---|---|---|---|---|
| NVIDIA | Q2 FY27 (26 Aug 2026) | $96.2B, +106% | $108B ±2% (+12% q/q) | 75.0%; ties the FY2025 peak; FY2023 trough 56.9% | Inventory $31.6B vs $21.4B in Jan 2026; receivables $63.1B; $105B-capped OpenAI lease guarantees ([8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm)) |
| Broadcom | Q3 FY26 (2 Sep 2026) | $29.6B, +86% | ~$34.8B (+18% q/q); AI $21.7B | GAAP 67.8% (FY2025) vs 68.9% FY2023 peak | AI semis +221%; backlog not verified; reported $63B Anthropic arrangement (headline) |
| Marvell | Q2 FY27 (27 Aug 2026) | $2.739B, +37% | $3.15B ±2% (+15% q/q) | Non-GAAP 58.9%; GAAP 53.1% vs FY2025 trough 41.3% | "AI-related bookings remain exceptionally robust"; Google custom deal and warrant |
| Micron | FQ4 FY26 (30 Sep 2026) | $54.2B, +379% | $61.5B ±$1.5B (+13% q/q) | ~87% non-GAAP; prior peak 58.9% (FY2018); trough -9.1% (FY2023) | Inventory $10.37B (+24% y/y); FY2026 net capex $27.4B; Strategic Customer Agreements |
| Intel | Q3 2026 (29 Oct 2026) | $16.5B, +21% | $15.0–16.0B (down q/q) | 44.1% non-GAAP; guide 38.0%; peak 63.7% (2014); trough 32.7% (2024) | Xeon supply-constrained; PC slowdown through 1H 2027; $23B equity raise |
| Amkor | Q3 2026 (26 Oct 2026) | $1.99B, flat | $1.9–2.0B (flat or down) | 18.3% vs 20.0% peak (2021) | FY2026 capex ~$2.5B; Arizona $12B; computing 26% of sales |
| Lumentum | Q1 FY27 (2 Nov 2026) | $1.263B, +137% | $1.575–1.625B (+27% q/q) | 51.0% GAAP, above the FY2022 peak of 46.0% | NPO/CPO win with >$5B of purchase commitments; cash down $759M on the quarter |
| Coherent | Q1 FY27 (4 Nov 2026) | $2.37B, +50% | $2.55–2.75B (+12% q/q) | 39.1% GAAP vs 40.0% FY2017 peak | TTM FCF -$1.83B (capacity build); FY2027 pro forma growth >60% |
| Credo | Q1 FY27 (1 Sep 2026) | $479M, +115% | $525–535M (+11% q/q) | 68.0% non-GAAP, top of range | Customers A and B 43% and 28%; inventory +25% q/q; capacity deposits $88M (+$102M) |
| Astera Labs | Q3 2026 (3 Nov 2026) | $585M, +154% | $730–750M (+26% q/q) | 72.4% non-GAAP (range 69–76%) | Scorpio now the largest product family |
| Fabrinet | Q1 FY27 (2 Nov 2026) | $1.474B, +51% | $1.60–1.65B (+10% q/q) | ~12% (band 10.8–12.7% since 2012) | TTM FCF negative; buyback raised |

Notes on the table:
- Micron's +379% is computed from $54.23B against $11.32B.
- Amkor's flat year-on-year revenue compares $1,991M with $1,987M.

#### Tier 2 compact snapshot (prices are 11 Nov 2026 closes)
Sources: StockAnalysis statistics pages ([AMAT](https://stockanalysis.com/stocks/amat/statistics/), [ANET](https://stockanalysis.com/stocks/anet/statistics/), [CSCO](https://stockanalysis.com/stocks/csco/statistics/), [CIEN](https://stockanalysis.com/stocks/cien/statistics/), [CLS](https://stockanalysis.com/stocks/cls/statistics/), [GFS](https://stockanalysis.com/stocks/gfs/statistics/), [ONTO](https://stockanalysis.com/stocks/onto/statistics/), [FORM](https://stockanalysis.com/stocks/form/statistics/), [KLIC](https://stockanalysis.com/stocks/klic/statistics/), [SMTC](https://stockanalysis.com/stocks/smtc/statistics/), [MTSI](https://stockanalysis.com/stocks/mtsi/statistics/), [AAOI](https://stockanalysis.com/stocks/aaoi/statistics/), [AEHR](https://stockanalysis.com/stocks/aehr/statistics/), [VICR](https://stockanalysis.com/stocks/vicr/statistics/), [NVTS](https://stockanalysis.com/stocks/nvts/statistics/)). Performance is from Nasdaq history (for example [AMAT](https://api.nasdaq.com/api/quote/AMAT/historical?assetclass=stocks&fromdate=2022-12-28&limit=9999&todate=2026-11-12)). Cycle lines come from the cited headlines and releases.

| Ticker | Price (11 Nov) | Mkt cap | Fwd P/E (SA) | EV/EBITDA (TTM) | YTD | 12m | Off 52w high | One-line cycle position (dated) |
|---|---|---|---|---|---|---|---|---|
| AMAT | $395.08 | $313.5B | 22.27 | 30.69 | +53.7% | +72.8% | -45.4% | Reports FQ4 FY26 on 12 Nov after the close; raised its BE Semiconductor stake to 20% ([Reuters, 27 Oct](https://www.reuters.com/business/shares-be-semiconductor-jump-over-9-after-applied-materials-raises-stake-20-2026-10-27/)) |
| ANET | $196.68 | $248.5B | 34.76 | 44.14 | +50.1% | +45.8% | -9.3% | Q3 revenue $3.66B (+58.5%); sees FY2027 revenue ~$18.5B vs $16.44B consensus ([TheFly, 3 Nov](https://www.tipranks.com/news/the-fly/arista-networks-sees-fy27-revenue-roughly-18-5b-consensus-16-44b-thefly-news)) |
| CSCO | $100.76 | $396.7B | 19.57 | 22.10 | +30.8% | +40.5% | -22.5% | Reports FQ1 FY27 on 12 Nov after the close ([SA](https://stockanalysis.com/stocks/csco/statistics/)) |
| CIEN | $296.04 | $42.0B | 28.44 | 41.37 | +26.6% | +42.7% | -52.8% | September quarter beat and guide lifted optical peers ([Barron's, 17 Sep](https://www.barrons.com/articles/ciena-stock-ai-earnings-guidance-0e17c876)); FQ4 due ~10 Dec (estimated) |
| CLS (NYSE and TSX) | $242.92 | $30.6B | 13.36 | 16.26 | -17.8% | -26.8% | -48.6% | Q3 revenue $5.83B (+83%); targets about $40B of 2027 revenue; capex and working capital to absorb cash ([Nasdaq, 29 Oct](https://www.nasdaq.com/articles/cls-raises-2026-outlook-ai-demand-powers-aggressive-2027-ramp)) |
| GFS | $42.85 | $23.9B | 18.07 | 11.01 | +22.7% | +23.1% | -52.4% | Q3 revenue $1.9B at a record gross margin; Q4 EPS guide 59c ±5c; ~$4B of 2027 net capex ([TheFly, 4 Nov](https://www.tipranks.com/news/the-fly/globalfoundries-reports-q3-eps-53c-consensus-51c-thefly-news)) |
| ONTO | $215.06 | $10.6B | 17.93 | 27.34 | +36.2% | +61.2% | -43.2% | Q3 revenue $409.7M; backlog >$1.3B; Q4 EPS guide $2.59–2.79 ([TheFly, 10 Nov](https://www.tipranks.com/news/the-fly/onto-innovation-sees-q4-eps-2-59-2-79-consensus-2-48-thefly-news)) |
| FORM | $95.78 | $7.5B | 23.66 | 28.35 | +71.7% | +84.5% | -40.1% | Q3 revenue $280.6M (~+40% y/y); capacity-constrained; Q4 EPS 95c ±9c ([TheFly, 28 Oct](https://www.tipranks.com/news/the-fly/formfactor-reports-q3-eps-1-04-consensus-86c-thefly-news)) |
| KLIC | $73.20 | $3.8B | 12.52 | 20.91 | +60.7% | +89.4% | -45.3% | FQ4 FY26 results due 18 Nov, call 19 Nov ([PR Newswire, 10 Nov](https://www.prnewswire.com/news-releases/kulicke--soffa-schedules-fourth-quarter-2026-conference-call-for-800-am-et-november-19th-2026-302933486.html)) |
| SMTC | $125.22 | $11.7B | 23.15 | 66.95 | +69.9% | +73.9% | -36.5% | Raised its Q3 FY27 EPS guide to $1.12–1.16 on 15 Oct; FY2030 revenue target $3.2B ([TheFly](https://www.tipranks.com/news/the-fly/semtech-raises-q3-eps-view-to-1-12-1-16-from-1-02-1-08-consensus-1-06-thefly-news)); reports 23 Nov |
| MTSI | $249.86 | $19.1B | 25.50 | 50.65 | +45.9% | +47.0% | -39.0% | FY2026 revenue >$1.3B with record backlog ([GlobeNewswire, 5 Nov](https://www.globenewswire.com/news-release/2026/11/05/3396302/19814/en/macom-reports-fiscal-fourth-quarter-and-fiscal-year-2026-financial-results.html)) |
| AAOI | $55.86 | $5.1B | 18.30 | n/a (negative) | +60.2% | +135.2% | -75.0% | Q3 revenue $269.9M (+127.5%); material shortages and facility delays; share count +44.9% y/y ([TheFly, 5 Nov](https://www.tipranks.com/news/the-fly/applied-optoelectronics-reports-q3-adjusted-eps-17c-consensus-14c-thefly-news)) |
| AEHR | $65.78 | $2.2B | 63.34 | n/a | +225.8% | +184.0% | -54.8% | FQ1 FY27 revenue $33M vs $27.5M consensus ([TheFly, 2 Nov](https://www.tipranks.com/news/the-fly/aehr-test-systems-reports-q1-eps-28c-consensus-13c-thefly-news)) |
| VICR | $168.10 | $7.8B | 30.77 | 43.60 | +53.4% | +81.6% | -55.7% | Q3 revenue $197.1M; raised guidance twice on licensing royalties ([TheFly, 20 Oct](https://www.tipranks.com/news/the-fly/vicor-reports-q3-eps-1-33-consensus-1-24-thefly-news)) |
| NVTS | $10.07 | $2.7B | n/a | n/a | +41.0% | +10.4% | -68.3% | Q3 revenue $14.0M (+33% q/q); Q4 guide $15.5–16.5M ([TheFly, 3 Nov](https://www.tipranks.com/news/the-fly/navitas-semiconductor-sees-q4-revenue-15-5m-16-5m-consensus-15-12m-thefly-news)) |

### Inferences
- Order and guidance data show no reported turn yet. The signals that typically come before a turn are present, though: inventory build, supplier financing of customers, capex-driven negative FCF, customer concentration, and a political shock to data-center construction. Share prices have de-rated ahead of any fundamental turn, which is common late in a cycle.
- Memory is the only sub-segment where margins are far above any previous peak: Micron at about 86–87% against 58.9% in FY2018. That supports the reading that its earnings are the most exposed to mean reversion. It also explains why its multiple is the lowest.
- Intel's and Amkor's guides point down or flat while AI-exposed peers guide up. Their cycle drivers (PCs, smartphones, CPU supply) differ from the AI-accelerator cycle. Intel's multiple does not reflect that difference, while Amkor's does.

### Gaps
- Broadcom's and NVIDIA's order backlogs, and NVIDIA's supply and purchase commitments, were not verified.
- Customer concentration for most companies, other than Credo, was not verified.
- Industry pricing data (DRAM, HBM and optical-module prices) came only from company margins and headlines; independent price indices were not read.
- The ALAB, ANET, ONTO, FORM and other Tier 2 quarterly figures rely on TheFly and company headlines in the StockAnalysis news feed, not on full releases.

## Key Question 3: Which dated events in the next three to six months could change the picture?

### Takeaway
The next six weeks are dense:
- the NVIDIA board and CEO decision, which was pending on 12 Nov;
- results from Applied Materials and Cisco (12 Nov), NVIDIA (17 Nov), Kulicke & Soffa (18 Nov), Semtech (23 Nov), Marvell and Credo (1 Dec), Broadcom (9 Dec), Ciena (~10 Dec, estimated) and Micron (~16 Dec, estimated);
- the December index reviews (dates not verified).

Policy events also overhang the group: the 5 Nov export-diversion crackdown and the Democratic Congress seated in January 2027. The Marvell–Lumentum process (S-4, votes and approvals, with an Outside Date of 1 Nov 2027 and expected close in 1H 2028) is the main corporate event. Dilution sources include Intel's $23B raise and shelf, the Marvell warrant to Google, and Credo's contingent DustPhotonics consideration.

### Cited Findings

#### Event calendar (next 3–6 months; "confirmed" means the company or StockAnalysis lists the date as confirmed)

| Date | Event | Companies affected | Source |
|---|---|---|---|
| 12 Nov 2026 (pending) | NVIDIA board decision on the CEO, per press reports; downgrades the same day | NVDA, plus supply chain (CoreWeave, Intel, Marvell, Lumentum and Coherent moved on it) | [Barron's, 12 Nov](https://www.barrons.com/articles/nvidia-stock-price-huang-affair-ceo-ouster-26c99dad); [Barron's, 12 Nov](https://www.barrons.com/articles/intel-stock-price-marvell-chips-nvidia-a79a4389) |
| 12 Nov 2026, after close | Applied Materials FQ4 FY26 results; Cisco FQ1 FY27 results (confirmed) | AMAT, CSCO; read-across to equipment and networking | [SA AMAT](https://stockanalysis.com/stocks/amat/statistics/); [SA CSCO](https://stockanalysis.com/stocks/csco/statistics/) |
| 17 Nov 2026, after close | NVIDIA Q3 FY27 results (confirmed; guide $108B ±2%) | All | [SA NVDA](https://stockanalysis.com/stocks/nvda/statistics/) |
| 18–19 Nov 2026 | Kulicke & Soffa FQ4 FY26 results (18 Nov) and call (19 Nov, 8:00 AM ET) | KLIC; packaging read-across | [PR Newswire](https://www.prnewswire.com/news-releases/kulicke--soffa-schedules-fourth-quarter-2026-conference-call-for-800-am-et-november-19th-2026-302933486.html) |
| 19 Nov 2026 | Alibaba results (China AI demand and NVIDIA supply read-through) | NVDA and China-exposed names | [TipRanks, 12 Nov](https://www.tipranks.com/news/why-is-alibaba-stock-baba-falling-in-premarket-ahead-of-november-19-earnings) |
| 23 Nov 2026 | Semtech Q3 FY27 results | SMTC | [SA SMTC](https://stockanalysis.com/stocks/smtc/statistics/) |
| 1 Dec 2026, after close | Marvell Q3 FY27 results (guide $3.15B ±2%); Credo Q2 FY27 results (guide $525–535M) | MRVL, LITE (deal-linked), CRDO | [Business Wire (MRVL)](https://www.businesswire.com/news/home/20261106322575/en/Marvell-Technology-Inc.-Announces-Conference-Call-to-Review-Third-Quarter-of-Fiscal-Year-2027-Financial-Results/); [Business Wire (CRDO)](https://www.businesswire.com/news/home/20261111758581/en/Credo-Schedules-Second-Quarter-Fiscal-Year-2027-Financial-Results-Conference-Call/) |
| 9 Dec 2026, after close | Broadcom Q4 FY26 results (guide ~$34.8B; AI $21.7B) | AVGO; custom-silicon read-across | [PR Newswire](https://www.prnewswire.com/news-releases/broadcom-inc-to-announce-fourth-quarter-and-fiscal-year-2026-financial-results-on-wednesday-december-9-2026-302932749.html) |
| ~10 Dec 2026 (estimated) | Ciena FQ4 FY26 results | CIEN; optical read-across | [SA CIEN](https://stockanalysis.com/stocks/cien/statistics/) |
| ~16 Dec 2026 (estimated) | Micron FQ1 FY27 results (guide $61.5B ±$1.5B; GM ~86%) | MU; memory peers | [SA MU](https://stockanalysis.com/stocks/mu/statistics/) |
| December 2026 (dates not verified) | S&P 500 quarterly rebalance and Nasdaq-100 annual reconstitution. Non-members in this group include CRDO, AMKR and FN (S&P 500 and Nasdaq-100) and ALAB (S&P 500 only); candidacy not verified | CRDO, ALAB, AMKR, FN | [SA S&P 500 list](https://stockanalysis.com/list/sp-500-stocks/); [SA Nasdaq-100 list](https://stockanalysis.com/list/nasdaq-100-stocks/) |
| Ongoing from 5 Nov 2026 | Presidential authorisation of a crackdown on diversion of NVIDIA chips to China; implementation reportedly stalled | NVDA; possibly AMD, AVGO and other exporters | [TheFly via TipRanks, 12 Nov](https://www.tipranks.com/news/the-fly/lutnick-stalled-trumps-nvidia-china-chip-curbs-axios-reports-thefly-news); [MarketWatch, 9 Nov](https://www.marketwatch.com/story/are-amd-and-broadcom-the-real-winners-of-the-nvidia-spy-scandal-d2343072) |
| 3 Jan 2027 (constitutional start of the new Congress; inference) | Democratic majorities seated after the 3 Nov 2026 midterms, which were run on "tougher tacks on data-center construction" | Data-center capex chain: MU, NVDA, AVGO, optics | [MarketWatch, 4 Nov](https://www.marketwatch.com/story/micron-and-other-chip-stocks-slip-as-election-results-strike-at-the-core-of-data-center-optimism-b55d19b3) |
| Late Jan to Feb 2027 (not confirmed) | Q4 and December-quarter results for INTC, AMKR, ALAB, LITE, COHR, FN, ANET, GFS and others | Various | Company patterns; not verified |
| 2027 (dates TBD) | Marvell–Lumentum S-4, both shareholder votes, HSR and other approvals; Outside Date 1 Nov 2027 (extendable to 1 Aug 2028); expected close 1H 2028 | MRVL, LITE | [Marvell 8-K](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442717/d352474d8k.htm); [Marvell 8-K Ex. 99](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442714/0001193125-26-442714.txt) |
| From 2028 (outside the window) | Ready-for-service milestones that trigger NVIDIA's OpenAI lease guarantees | NVDA | [NVIDIA 8-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000069/nvda-20260817.htm) |

Share issues, convertibles and dilution:
- Intel completed a $23B public equity offering and has an automatic shelf (S-3ASR) filed on 10 Aug 2026 — [Intel Q3 8-K](https://www.sec.gov/Archives/edgar/data/50863/000005086326000188/0000050863-26-000188.txt); [SEC submissions, INTC](https://data.sec.gov/submissions/CIK0000050863.json)
- Marvell's warrant to Google covers up to 58.97M shares (about 6.7% of the 878M shares outstanding, computed) at a $206.58 strike, vesting with Custom revenue — [Marvell 8-K](https://www.sec.gov/Archives/edgar/data/1835632/000119312526356217/d412696d8k.htm)
- The Marvell–Lumentum deal issues about 408M new MRVL shares (computed from 90.7M LITE shares × 4.5) — [Marvell 8-K](https://www.sec.gov/Archives/edgar/data/1835632/000119312526442717/d352474d8k.htm)
- Credo's DustPhotonics deal includes $310M of contingent consideration ($300M classified as equity) — [Credo 10-Q](https://www.sec.gov/Archives/edgar/data/1807794/000162828026060111/crdo-20260801.htm)
- Applied Optoelectronics' share count rose 44.89% year on year — [SA AAOI](https://stockanalysis.com/stocks/aaoi/statistics/)
- Amkor's May 2026 financing 8-K (Items 1.01, 2.03, 3.02) has terms that are not verified — [SEC submissions, AMKR](https://data.sec.gov/submissions/CIK0001047127.json)

#### Peer-comparison table: all names, with non-US peers (StockAnalysis statistics, read 12 Nov 2026)
US prices are 11 Nov closes. Asian prices were shown as "Delayed Price" on 12 Nov, which is likely the 12 Nov close; the exact timestamp was not captured. European prices were intraday. Non-US market caps are in local currency.

| Company (ticker) | Fwd P/E | EV/EBITDA | P/B | 52-week change |
|---|---|---|---|---|
| NVIDIA (NVDA) | 14.33 | 20.73 | 18.32 | -12.7% |
| Broadcom (AVGO) | 19.84 | 32.21 | 16.53 | -3.7% |
| Marvell (MRVL) | 29.92 | 52.47 | 7.99 | +81.1% |
| Micron (MU) | 4.60 | 7.81 | 6.63 | +220.3% |
| Intel (INTC) | 44.91 | 17.14 | 2.89 | +62.6% |
| Amkor (AMKR) | 13.91 | 6.92 | 1.97 | +8.2% |
| Lumentum (LITE) | 22.18 | 50.61 | 12.84 | +149.4% |
| Coherent (COHR) | 20.00 | 29.35 | 4.08 | +40.7% |
| Credo (CRDO) | 19.39 | 47.57 | 9.73 | -16.9% |
| Astera Labs (ALAB) | 33.57 | 94.58 | 20.18 | +32.9% |
| Fabrinet (FN) | 17.59 | 21.19 | 5.26 | -21.0% |
| AMD | 36.73 | 80.79 | 13.26 | +126.6% |
| SanDisk (SNDK) | 3.99 | 6.21 | 7.76 | +264.9% |
| Jabil (JBL) | 14.63 | 11.64 | 16.77 | +18.1% |
| TSMC ADR (TSM) | 19.76 | 15.40 | 8.34 | +40.0% |
| TSMC (TPE:2330) | 16.42 | 15.88 | 8.62 | +59.7% |
| SK hynix (KRX:000660) | 2.52 | 3.77 | 2.96 | +102.6% |
| Samsung Electronics (KRX:005930) | 2.92 | 3.49 | 2.17 | +101.0% |
| Kioxia (TYO:285A) | 2.11 | 3.59 | 5.44 | +111.4% |
| Nanya Technology (TPE:2408) | 3.30 | 5.09 | 3.41 | +130.7% |
| MediaTek (TPE:2454) | 28.76 | 48.91 | 12.98 | +210.5% |
| Alchip (TPE:3661) | 18.20 | 27.60 | 5.23 | +1.1% |
| Global Unichip (TPE:3443) | 63.58 | 145.77 | 71.60 | +311.5% |
| Socionext (TYO:6526) | 18.96 | 10.33 | 2.44 | -22.2% |
| Montage Technology (SHA:688008) | 36.76 | 58.89 | 8.83 | +28.1% |
| UMC (TPE:2303) | 15.79 | 8.03 | 2.69 | +123.2% |
| SMIC (HKG:0981) | 34.74 | 17.13 | 2.13 | -32.9% |
| ASE Technology (TPE:3711) | 19.16 | 17.02 | 5.70 | +157.0% |
| Powertech (TPE:6239) | 14.56 | 8.17 | 2.62 | +41.9% |
| JCET (SHA:600584) | 28.66 | 15.07 | 3.03 | +41.4% |
| Tongfu Microelectronics (SHE:002156) | 40.12 | 14.77 | 3.22 | +24.6% |
| Hana Microelectronics (BKK:HANA) | 27.18 | 13.98 | 1.32 | +130.8% |
| Zhongji Innolight (SHE:300308) | 9.14 | 16.08 | 6.08 | +8.7% |
| Eoptolink (SHE:300502) | 9.58 | 16.14 | 10.67 | -11.7% |
| Suzhou TFC Optical (SHE:300394) | 28.85 | 47.67 | 24.24 | +18.7% |
| Accelink (SHE:002281) | 34.87 | 35.85 | 5.58 | +75.5% |
| Sumitomo Electric (TYO:5802) | 11.87 | 7.28 | 1.64 | +6.1% |
| Furukawa Electric (TYO:5801) | 12.90 | 11.04 | 3.42 | +139.3% |
| Fujikura (TYO:5803) | 13.86 | 12.66 | 6.76 | -6.6% |
| Hon Hai (TPE:2317) | 11.57 | 7.78 | 1.58 | -2.6% |
| Quanta (TPE:2382) | 9.30 | 8.92 | 3.01 | -4.5% |
| Foxconn Industrial Internet (SHA:601138) | 11.53 | 12.46 | 4.58 | -36.3% |
| ASML (AMS:ASML) | 24.42 | 30.84 | 24.33 | +54.8% |
| Tokyo Electron (TYO:8035) | 20.88 | 22.49 | 9.73 | +36.1% |
| BE Semiconductor (AMS:BESI) | 26.75 | 33.85 | 19.50 | +15.4% |
| Advantest (TYO:6857) | 24.45 | 29.59 | 19.58 | +50.9% |
| Hanmi Semiconductor (KRX:042700) | 42.53 | 69.11 | 22.88 | +40.3% |

Sources for the table: StockAnalysis quote pages, for example [SK hynix](https://stockanalysis.com/quote/krx/000660/statistics/), [Kioxia](https://stockanalysis.com/quote/tyo/285A/statistics/), [Innolight](https://stockanalysis.com/quote/she/300308/statistics/), [ASE](https://stockanalysis.com/quote/tpe/3711/statistics/), [ASML](https://stockanalysis.com/quote/ams/ASML/statistics/), [Tokyo Electron](https://stockanalysis.com/quote/tyo/8035/statistics/), [BESI](https://stockanalysis.com/quote/ams/BESI/statistics/), [Advantest](https://stockanalysis.com/quote/tyo/6857/statistics/), [Hanmi](https://stockanalysis.com/quote/krx/042700/statistics/). US rows link to the same pages under /stocks/<ticker>/statistics/. 52-week changes are StockAnalysis's figures and can differ slightly from the Nasdaq-based 12-month returns elsewhere in these notes.

#### Investor access summary (foreign investor)
- **Listing venues.** NVDA, AVGO, MRVL, MU, INTC, AMKR, LITE, CRDO and ALAB list on Nasdaq; COHR and FN on NYSE — [SEC submissions files](https://data.sec.gov/submissions/CIK0001045810.json). In Tier 2, ANET, CIEN, CLS and ONTO list on NYSE and the rest on Nasdaq — [StockAnalysis pages](https://stockanalysis.com/stocks/anet/statistics/). Celestica is dual-listed on the NYSE and TSX — [GlobeNewswire, 30 Oct 2026](https://www.globenewswire.com/news-release/2026/10/30/3392160/0/en/celestica-announces-tsx-acceptance-of-normal-course-issuer-bid.html)
- **Domicile.** Credo and Fabrinet are Cayman Islands companies and Coherent is a Pennsylvania company. The other Tier 1 companies are Delaware corporations, though Broadcom's state of incorporation is blank in the SEC file — [SEC submissions](https://data.sec.gov/submissions/CIK0001807794.json)
- **Liquidity** (20-day average daily value traded, computed from StockAnalysis volume × price): NVDA ~$28.6B; MU ~$25.4B; INTC ~$9.4B; AVGO ~$9.0B; MRVL ~$5.1B; LITE ~$4.3B; COHR ~$2.3B; CRDO ~$1.2B; ALAB ~$1.2B; FN ~$0.45B; AMKR ~$0.24B.
- **ETF weights** (StockAnalysis holdings pages, top-25 lists, read 12 Nov 2026):

  | ETF | Holdings shown |
  |---|---|
  | SMH | NVDA 18.92%, AVGO 5.90%, MU 4.22%, AMAT 4.20%, MRVL 3.27%, INTC 2.97%, ALAB 0.86% |
  | SOXX | AVGO 8.30%, NVDA 7.11%, MU 6.99%, INTC 6.00%, AMAT 3.75%, MRVL 3.37%, ALAB 1.96%, CRDO 1.40%, MTSI 1.03% |
  | PSI | MU 4.68%, AMAT 4.68%, INTC 4.01%, SMTC 2.93%, MTSI 2.80%, KLIC 2.71%, FORM 2.61%, AMKR 2.33%, ONTO 2.23% |
  | XSD (equal weight) | AVGO 2.60%, NVTS 2.30% |
  | QQQ | NVDA 7.10%, MU 3.77%, AVGO 2.51%, CSCO 1.77%, INTC 1.42%, AMAT 1.34% |

  Sources: [SMH](https://stockanalysis.com/etf/smh/holdings/); [SOXX](https://stockanalysis.com/etf/soxx/holdings/); [PSI](https://stockanalysis.com/etf/psi/holdings/); [XSD](https://stockanalysis.com/etf/xsd/holdings/); [QQQ](https://stockanalysis.com/etf/qqq/holdings/)
- **Index membership.** S&P 500: AMAT, ANET, AVGO, CIEN, COHR, CSCO, INTC, LITE, MRVL, MU, NVDA. Nasdaq-100: ALAB, AMAT, AVGO, CSCO, INTC, LITE, MRVL, MU, NVDA — [SA S&P 500](https://stockanalysis.com/list/sp-500-stocks/); [SA Nasdaq-100](https://stockanalysis.com/list/nasdaq-100-stocks/)

### Inferences
- The two earnings dates most likely to reset the group are 17 Nov (NVIDIA, against the roughly $126B Q4 that consensus implies) and 9 Dec (Broadcom's FY2027 AI trajectory). Micron's ~16 Dec print tests the memory prior directly: whether gross margin holds near 86% and what 2027 pricing looks like.
- The NVIDIA governance event is unusual for this group. It is a company-specific shock to a stock whose price embeds the group's AI capex view. On 12 Nov rivals (AMD, Broadcom) rose while suppliers (Intel, Marvell, Lumentum, Coherent) fell. Any read-across therefore depends on whether investors see it as share shift or as risk to aggregate demand — [Barron's, 12 Nov 2026](https://www.barrons.com/articles/intel-stock-price-marvell-chips-nvidia-a79a4389)
- Lumentum should now be analysed as a deal-linked security. Its entry economics are MRVL beta plus a spread of about 15% (about 10–11% a year over ~19 months), less the risk of deal failure.
- For a foreign investor, every Tier 1 name is accessible through a primary US listing with deep liquidity, except Amkor and Fabrinet, which are thinner (below $0.5B a day). Broad semiconductor ETFs give meaningful exposure only to the large caps plus Astera Labs and Credo; the optics names (LITE, COHR, FN) are not in the top-25 lists of the main semiconductor ETFs checked.

### Gaps
- **December index dates and candidates.** The exact December 2026 S&P 500 and Nasdaq-100 review dates and candidates were not verified.
- **Q4 and December-quarter report dates.** Dates for INTC, AMKR, ALAB, LITE, COHR and FN were not verified.
- **Investor days and product events.** None were checked, for example NVIDIA GTC 2027 or OFC 2027 dates.
- **Secondary listings and UCITS ETFs.** Secondary or unofficial listings (Germany, Mexico SIC, Brazil BDRs, Canadian CDRs) and UCITS ETF equivalents of SMH and SOXX were not verified. The WebSearch budget was exhausted and the harness said not to work around it with other search services, so no third-party search engines were used. All data come from direct fetches of known URLs.
- **Unread filings.** These filings were seen in the SEC index but not read:
  - Broadcom's 27 Oct 2026 8-K (Item 2.03)
  - Amkor's 5 May 2026 8-K (Items 1.01, 2.03 and 3.02)
  - Fabrinet's 17 Aug 2026 8-K (Items 1.01, 2.03 and 5.02)
  - Marvell's 23 Oct 2026 8-K (Item 1.01) and 25 Sep 2026 8-K (Item 8.01)
  - Coherent's 31 Aug 2026 8-K (Items 5.02 and 8.01)
  - Astera Labs' 4 Nov 2026 8-K (Item 5.02)
- **News teasers.** NVIDIA governance, the Megaspeed matter, Anthropic and Meta deals, the Apple memory-price warning and broker actions come from headline and summary text in the StockAnalysis news feed. The full articles were not read; most are paywalled (WSJ, Barron's, FT).
- **Coordinator's leads.** Lead 1 (Marvell–Lumentum all-stock deal, close expected 1H 2028) is confirmed by Marvell's 8-Ks; the agreement is dated 1 Nov and was announced 2 Nov 2026. Lead 2 (Credo–DustPhotonics) is confirmed with corrections: it closed on 28 May 2026, before the 1 Aug quarter-end, for about $1.25–1.3B in total (about $770M cash, $169M stock and $310M contingent), not about $750M.

# The 2026 fall in chip-equipment, test and probe-card shares: causes, what prices assume, near-term events

Compiled 12 November 2026 (today). Scope: entry point and market pricing only. No business-quality judgments and no buy/sell calls. Builds on figures already established by other researchers (peak-to-low falls, FactSet 6 Nov, WFE outlooks, AI-financing signals, 10 Jan 2027 deadlines), which are not repeated here.

Labels:
- **[F]** = read in the fetched article.
- **[S]** = search snippet or headline only.
- **[Op: X]** = opinion of a named author or firm.
- **[calc]** = my arithmetic.

Sources are reference-style links; the dated list is at the end.

## Summary table

| Candidate cause | Evidence for | Evidence against | Verdict |
|---|---|---|---|
| **De-rating from peak multiples** (sector) | AMAT fwd P/E 49x on 30 Jun, 21x on 2 Nov; average target still $628 [F][tikr]. Analysts cut targets, not visible EPS: Evercore $700→$590, MS $563→$538, B. Riley $700→$475 [S][sa-amat] | No source shows estimates falling first | **Supported** |
| **Rates, inflation, oil** (market-wide) | Fed hiked 25bp in Sep. On 28 Oct it held 3.75-4.00% by 10-2, with Hammack and Cook voting to hike. 10-yr closed 5.03%; WTI >$100 (+78% YTD); FedWatch 78% for a Dec hike [F][sa-fed], 84.5% on 9 Nov [S][roic-cpi] | NDX +0.6% on Fed day. No article seen names rates as the cause of a chip-specific fall | **Partly supported** (backdrop to the de-rating) |
| **Fears that AI capex won't last or won't happen** (sector) | 28 Jul "...Selloff Over Spending Fears" [S][rss1]. 14 Sep slide after Anthropic CEO urged slowing AI capability gains; BIS cited "rising concerns about the future profitability of significant AI investments" [F][w247-sep]. Citi via Barron's, 23 Oct [S][pluang]. 5 Nov: fear AI spending "won't materialize next year" [S][hey] | TSMC raised 2026 outlook on 15 Oct [S][crn]. Lam/KLA see 2027 WFE >$200bn. No cancellations | **Partly supported** (fear, not reported cuts) |
| **AI-financing stress** | CoreWeave unsecured debt repriced on 14 Oct (CRWV -14.9% intraday, Nebius -9.7%) [S][roic14]. 15 Oct "AI financing shock...as debt costs bite" [S][roic15]. Hyperscaler bond pushback in Jul-Aug [S][fortune][ifre] | Article fetch blocked. The 11 Nov rebound came with CoreWeave's results | **Partly supported** (snippet-level) |
| **Midterms on 3 Nov: Democratic sweep → AI and data-centre regulation fears** (political) | 5 Nov rout of >$2tn [F][gpb]. AMAT -13.6% with no company news; XLK -8.0% [F][trefis]. Data-centre operators -15%+; MS expects tighter state data-centre rules [S][finimize][nbc] | Analysts doubt laws can stall construction [S][nbc]. Stocks rose on 4 Nov | **Supported** as trigger of the 5 Nov low |
| **China's home-grown chip tools / competition** (sector) | 28 Jul: Kospi -10.8%, SK Hynix -14.7%, Taiex -4.7% after The Information reported China mass-producing DUV tools [S][ap-jul]. 27 Jul: Nikkei -2,884 yen on "China's chip equipment push" [S][rss1]. 13 Oct: China fears hit Samsung/SK Hynix [S][rss1]. Lam 35% China revenue in Sep qtr [F][tikr] | No new US export rule found in the window | **Supported** for late July; **partly** for October |
| **Supply constraints at toolmakers** (company/sector) | Lam on 21 Oct: Dec-qtr guide "failed to impress"; some shipments slip into March; cleanroom limits on 2027. LRCX -8% after hours; AMAT -7.4% on 22 Oct [S][stw-lrcx][technews] | BofA: "supply constrained, not demand constrained" [S][stw-lrcx] | **Supported** for the 22 Oct leg |
| **Profit-taking / positioning** | 13 Oct: AMAT -7%, LRCX/KLAC -4% "as investors take profits" [S][w247-oct]. AMAT "+98% in 2026" by 18 Aug [S][rss1] | - | **Partly supported** |
| **Weak chip-designer results** | Qualcomm's weak guide after the 4 Nov close [F][tikr]; "weak results from two chip designers" [S][alpha] | AMD +7% on 4 Nov after "stellar" results [S][rss2] | **Partly supported** (5 Nov contributor) |
| **Hedge-fund deleveraging on 5 Nov** | "hedge funds reducing borrowing" [S][alpha] | Not in any fetched article | **Could not verify** |
| **Memory-price peak / memory costs** | 26 Jun: "Semiconductor stocks retreat over worries about memory costs" [S][rss1] | Micron FQ1 FY27 guide $61.5bn [S][aiw]; Teradyne record memory-test revenue [F][tikr] | **Partly supported** (June start only) |
| **Margin-peak fears** | None found | AMAT Q4 non-GAAP gross-margin guide ~50.4% [S][mb-amat] | **Could not verify** |
| **Export-control or tariff news** | Undated headline only ("China export risks resurface") | No dated rule found; deadlines are 10 Jan 2027 | **Could not verify** |
| **Credit event** | None (CoreWeave was a repricing, not a default) | - | **Not supported** |
| **Negative TSMC, hyperscaler or memory capex/order signals** | None found | TSMC 15 Oct: 2026-28 capex "significantly higher" [S][crn]; Micron guide strong | **Not supported** |

## 1. Causes: late June to mid-September, then 7 October to 5 November

### Takeaway
The fall came in two legs:
- **Leg 1:** AMAT went from $723.00 on 30 Jun to $429.71 on 14 Sep (-41% [calc]). Drivers: AI-spending and China-tool fears, plus profit-taking.
- **Rebound:** to about $521 by 7 Oct [calc from Trefis's -38.7%].
- **Leg 2:** AMAT fell to $319.25 on 5 Nov. This leg layered several shocks:
  - a hawkish Fed (10-yr above 5%);
  - mid-October AI-financing stress;
  - Lam's supply warning (21-22 Oct);
  - the midterm rout on 5 Nov.

No company reported order cuts. This was a de-rating, not a fall in estimates.

### Cited Findings
- **Late June:**
  - 23 Jun, AP: "AI stock slump raises the question if investors are just taking profits or getting very nervous" [S][ap-jun].
  - 26 Jun: memory-costs headline [S][rss1].
- **Mid-July (headlines) [S][rss1]:**
  - 15 Jul, CNBC: "SK Hynix shares plunge over 11%...tracking U.S. chip losses".
  - 17 Jul: European chip stocks fall after US peers.
  - 17 Jul: Tokyo Electron, Advantest and Kioxia "plunging" [S][invezz].
- **27-28 Jul, the China DUV report:** Kospi -10.8% to 6,023.66; Samsung -13.4%; SK Hynix -14.7%; Taiex -4.7%; TSMC -3% [S][ap-jul]. Same days: "AI Chip Stocks Tumble...Over Spending Fears" [S][rss1].
- **30 Jul:** AMAT +15.0%, its biggest daily gain in 12 months; the cause is not stated [F][trefis].
- **13-14 Aug:** AMAT FQ3 revenue a record $9.12bn (+25%). It guided FQ4 to $10.25bn ±$0.5bn, non-GAAP EPS $4.02 ±$0.20 and gross margin ~50.4% [S][mb-amat]. On 14 Aug the shares were down 6% premarket [S][w247-aug].
- **14 Sep [F][w247-sep], by D. Moadel:**
  - Moves: AMAT -6% to $429.71 (-22% in a month); LRCX -6% to $279.18; ASML ADR -5%; SOXX -5%.
  - Trigger: Anthropic CEO Dario Amodei wrote "We must slow the pace at which we improve the capabilities of AI models". The article says, without sourcing, that Altman and xAI's head agreed. Its link to fab spending is the article's own inference.
  - Same day, BIS: "rising concerns about the future profitability of significant AI investments".
  - [Op: Neil Wilson, Saxo] Analysts would be "scrabbling around to assess likely impact on earnings and valuations".
- **September:** the Fed hiked 25bp, unanimously [F][sa-fed].
- **9 Oct:** Kokusai, Lasertec and Fujikura each fell almost 10% [S][rtt9].
- **13 Oct:** AMAT -7%, LRCX/KLAC -4% on profit-taking [S][w247-oct]. Same day: Morningstar, "Samsung and SK Hynix Lead Chip Selloff as China Competition Fears Grow"; Reuters, "Chip selloff pulls European stocks back from one-week high" [S][rss1].
- **Mid-October:**
  - After hot September CPI, Citi moved to forecast a December hike; futures priced about 94% [S][iliv].
  - 14-15 Oct: CoreWeave debt repricing and the "AI financing shock" [S][roic14][roic15].
- **16 Oct:**
  - Tokyo: Advantest almost -10%, Tokyo Electron almost -7%, Screen -8%+, Nikkei about -3.8%, USD/JPY about 157 [S][rtt16].
  - US: MarketWatch, "Nearly 40% of the S&P 500 is in a bear market" [S][sa-amat].
- **21-22 Oct (Lam results):**
  - Record revenue, but the Dec-qtr guide of $8.6bn ±$0.4bn "failed to impress" [S][technews].
  - Shares fell about 8% after hours to ~$242, from $261.47.
  - CFO: supply constraints push some shipments into March.
  - BofA called Lam supply-constrained, not demand-constrained, and Cantor's C.J. Muse agreed [S][stw-lrcx].
  - AMAT fell about 7.4% on 22 Oct [S][pluang].
- **23-24 Oct [S][pluang]:** [Op: Citi via Barron's] Chip-equipment stocks may see sharper declines "amid AI spending concerns", and this "could be just the beginning". No targets or scenarios were seen.
- **Late October [F][tikr]:**
  - KLA: Dec-qtr guide $4.7bn, against $4.14bn in September.
  - Teradyne: Q3 revenue +70% with record memory test; Q4 guide roughly flat.
- **28 Oct, Fed meeting [F][sa-fed]:**
  - Held 10-2, with two votes for a hike.
  - The statement called the economy "strong".
  - Chair Warsh said inflation has been above target "for close to six years".
  - The 10-yr closed at 5.03%.

### Inferences
- **Summer leg:** AI-spending doubt, China's home-grown tools, and the 14 Sep "pacing" remark.
- **Autumn leg:** rates and AI-financing pressure on long-duration AI assets, then the political shock of 5 Nov.
- **Common to both:** peak multiples, crowded positioning, and no deterioration in reported orders.

### Gaps
- What drove the 14 and 19 Aug falls (24/7 Wall St, "What's Prompting the Selloff...", not read).
- What drove the rebound from late September to 7 October.

## 2. The low on 5-6 November and the rebound

### Takeaway
The low came on Thursday 5 Nov, two days after the midterms. The trigger was fear that a Democratic Congress and the new governors will regulate AI and restrict data centres, compounded by Qualcomm's guidance. There was no news from the equipment companies themselves.

The rebound in stages:
- 6 Nov: the chip index rose 4.6% [S][fool6].
- From 9 Nov: an AI-trade revival around CoreWeave's results (10 Nov, after the close).
- 11 Nov: Nvidia recovered.

By 11 Nov AMAT was at $395.08: +23.8% from the low and -45.4% from the peak [calc][F][sa-amat].

### Cited Findings
- **5 Nov, Trefis [F][trefis]:** Nasdaq Composite -5.5%, S&P 500 -4.4%, XLK -8.0%. AMAT -13.6% to $319.25 with no announcement, its biggest daily fall in 12 months. MCHP -13.9%, TXN -10.7%.
- **5 Nov, TIKR [F][tikr]:** intraday LRCX -14%, KLAC -12%, TER -14%. The selloff "began after Democrats' midterm wins"; Democrats "signaled plans to regulate AI".
- **5 Nov, GPB/NPR [F][gpb], by R. Nam:**
  - The selloff wiped out >$2tn and reversed Wednesday's broad rally.
  - Voters "revolted against AI data centers".
  - [Op: David Busch, Trajan Wealth] "fears that there could be far more regulations coming".
  - No mention of rates or deleveraging.
- **Conflict on 4 Nov:** TIKR says data-centre stocks fell first, on Wednesday 4 Nov; GPB says shares rose across the board that day.
- **5 Nov, snippets only:**
  - SOX -12.25% to 9,011.14, its second-worst day on record and worst since 16 Mar 2020 [S][alpha] (fetch returned 403).
  - NVDA -9.26% to $181.60; MU -17.46%; AMD -17.26% [S][hey].
  - Applied Digital, Cipher and IREN -15%+. 32 of 34 winning governor candidates favour tighter data-centre rules [S][nbc].
- **8-9 Nov [S][st-nvda]:** Nvidia's board opened an investigation into a report about CEO Jensen Huang's personal conduct. NVDA fell in overnight and Frankfurt trading while other chip stocks rose. Details conflict between sources.
- **10-12 Nov headlines [S][rss1][rss2]:**
  - "Wells Fargo Turns Less Bearish on AI Stocks After 38% Semiconductor Crash" (Coinpaper, 10 Nov).
  - "Nikkei surges nearly 3%...SoftBank jumps 14%" (10 Nov).
  - "Nvidia Rebounds as CoreWeave Earnings Reignite the AI Trade" (Motley Fool, 11 Nov).
  - "Nvidia Selloff Puts China Exposed US Chip Stocks Back In Focus" (Yahoo, 11 Nov).
  - "Samsung...gains as US chip rally lifts Seoul" (12 Nov).
- **12 Nov [F][sa-amat]:** AMAT $385 pre-market (-2.55%).

### Inferences
- The low was a capitulation-type day: a record-scale fall on political news while fundamentals were unchanged.
- The rebound came from AI-demand news flow and the unwinding of 5 Nov's move, not from any policy reversal.

### Gaps
- Causes of the 6 Nov bounce beyond mean reversion.
- Whether deleveraging ended.
- Contents of the Wells Fargo note and of Seeking Alpha's "A $57 Billion Storm May Hit Semiconductor Stocks This Week" (8 Nov).

## 3. What prices assume; are 2027 estimates being cut?

### Takeaway
No sell-side source found says prices assume a spending pause in 2027 or 2028. The best-documented reading is multiple compression:
- AMAT's forward P/E fell from 49x to about 21-22x, close to its five-year average.
- That is still well above the 8.2x it hit at the 2018 trough.
- Estimates held or rose; analysts cut price targets, not EPS.

The opposing view is Citi's: more downside to come "amid AI spending concerns" [S].

### Cited Findings
- **[Op: TIKR author, 5 Nov] [F][tikr]:**
  - AMAT forward P/E: 21x on 2 Nov, against 49x on 30 Jun and 8.2x in Oct 2018.
  - The price "doesn't assume a real downturn". The stock was "marked down for a slowdown no company has reported".
  - Normalized EPS is expected to nearly double from FY2025 to FY2027.
- **AMAT, 11-12 Nov [F][sa-amat]:**
  - Forward P/E 22.27. Average target $623.31 from 40 analysts ("Strong Buy").
  - Target cuts: Evercore (about mid-Oct); MS to Equal Weight (about 3 Nov), described as a "Lone Wolf...Hold Call"; B. Riley (about 10 Nov).
- **Lam and KLA, snippets with unclear dates:**
  - Zacks consensus implies LRCX FY27 EPS +61% and FY28 +22%; KLAC FY27 +44% and FY28 +21% [S][zacks].
  - Lam FY27 revenue estimates were lifted to about $34.8bn from $31.1bn [S][zacks].
  - Erste cut its Lam FY27 estimate on 15 Jul [S][mb-lrcx].
  - KLA raised guidance (revenue +6.7%, EPS +9.2%) and said 2027 growth will exceed 2026 [S][rallies-kla].
- **WFE forecasts (conflicting, undated) [S][ss]:**
  - BofA: $140bn / $171bn / $193bn for 2026 / 2027 / 2028.
  - Citi optimistic case: $145bn / $200bn / $250bn.
  - Both are below Lam and KLA's "mid-$150bn" for 2026, so probably older.
- **SEMI mid-year 2026 [S][semi]:**
  - Total equipment $165.9bn in 2026 (+23.2%); WFE $143.9bn.
  - **Test equipment +31.0% to $15.3bn.**
  - $229.5bn by 2028.
- **AMAT FQ4 bar [S][ss]:**
  - About $10.25bn revenue and ~$4.00 EPS.
  - Its quality hinges on gross margin and "evidence that the DRAM ramp continues into 2027".
  - A quoted consensus of $3.71 EPS on $9.55bn conflicts with this and looks stale.

### Inferences
- 2027 EPS is still forecast to rise steeply, and multiples are near five-year averages.
- So prices seem to discount some risk of a slowdown after 2027 and a higher discount rate (10-yr above 5%), but not a 2018-scale downturn.
- This is my interpretation, not a sourced sell-side statement.

### Gaps
- No time series of consensus FY27 EPS for AMAT, LRCX or KLAC was found.
- No sourced estimate of the WFE level implied for 2027 or 2028.
- No sourced view on implied margins.

## 4. Link to AI data-centre financing

### Takeaway
**Partly supported.**
- The October leg coincided with a repricing of AI-infrastructure credit (CoreWeave, 14-15 Oct) and with hyperscaler-debt worries.
- The 5 Nov low was framed as political and regulatory risk to data-centre construction, not as a financing problem.
- TSMC and memory demand signals stayed strong.

### Cited Findings
- **Evidence for:**
  - CoreWeave's unsecured debt repriced sharply on 14 Oct. Reports blamed "concerns about the sustainability of the financing structure", "not a sudden collapse in demand" [S][roic14].
  - 15 Oct: "anxiety over borrowing costs and the capital intensity" [S][roic15].
  - July-August: Nvidia issued $25bn of bonds and BofA said investors were pushing back. A Meta-linked data-centre bond drew lukewarm demand. Goldman expects AI issuers' credit curves to steepen further [S][fortune][ifre].
- **Evidence against:**
  - TSMC Q3 (15 Oct): revenue about $46.7bn (+41.2%); Q4 guide $52.3-54.3bn; 2026 growth about 44%; capex $60-64bn; 2026-28 capex "significantly higher"; no 2027 capex guide [S][crn][futurum].
  - Adair Turner: fears of an AI-driven financial crisis may be overblown [S][ifre2].
  - No data-centre cancellations or power delays were found in this session.

### Gaps
- The CoreWeave article returned 403, so its details are unverified.
- No direct evidence ties Meta's or Alphabet's equity raises to chip-equipment price moves.

## 5. Local factors outside the US

### Takeaway
The falls were mostly transmitted from the US. One regional shock stands out: the late-July China DUV report hit Korea, Japan and Taiwan. The yen at 157-162 per dollar would normally help Japanese exporters, so it does not explain their falls [inference]. Lithography and test names outside the US fell less: ASML -32%, Advantest -33%, Lasertec -44%, against -56% to -57% for the large US names (other researchers).

### Cited Findings
- **Korea:**
  - 28 Jul: Kospi -10.8%; Samsung -13.4%; SK Hynix -14.7% on the China DUV report [S][ap-jul].
  - 13 Oct: China competition fears [S][rss1].
- **Japan:** 9 Oct and 16 Oct falls (see section 1). The yen passed 160 in July, and closed at 162.38 on a day the Nikkei fell 4% [S][rtt16].
- **Taiwan:** 28 Jul Taiex -4.7% [S][ap-jul]. No Taiwan-specific cause found.
- **Europe:**
  - 13 Oct, Reuters: chip selloff hits European stocks [S][rss1].
  - About 27 Oct: AMAT to lift its BESI stake to about 20%; BESI +9% [S][sa-amat].
- **China:** the push for domestic tools is a sector risk for foreign toolmakers. Lam got 35% of Sep-qtr revenue from China [F][tikr]. No new Chinese policy step was found in the window.

### Gaps
- Korea, Taiwan and China moves on 5-6 Nov.
- Taiwan dollar and won effects.
- Local policy news.

## 6. Near-term event calendar (as of 12 Nov 2026)

| Date | Event | Notes |
|---|---|---|
| 12 Nov, after US close | AMAT FQ4 FY26 results and first guide for the 14-week FQ1 FY27 | Guide $10.25bn ±$0.5bn, EPS $4.02 ±$0.20. CFO expects sequential growth in FQ1 [S][mb-amat]. **Not out when checked** [sa-amat] |
| This week (exact date not verified) | US October CPI, the last print before the FOMC | Russell: "even a small CPI beat could seal" a December hike [S][roic-cpi] |
| 17 Nov (Tue, after close) | Nvidia FQ3 FY27 results; questions on the Huang report expected | [S][st-nvda] |
| 8-9 Dec | FOMC, with 84.5% odds of a 25bp hike (9 Nov) | [S][roic-cpi] |
| 10 Dec | US November CPI, after the FOMC | [S][roic-cpi] |
| ~10 Dec / ~10 Jan | TSMC monthly revenue for November / December | Customary timing; **not verified** |
| ~16 Dec (Wed, 16:30 ET), unconfirmed | Micron FQ1 FY27 results; guide $61.5bn ±$1.5bn, EPS $38.15 ±$1 | [S][days][aiw] |
| Mid-Dec (SEMICON Japan) | SEMI year-end equipment forecast (last year's came 16 Dec 2025) | 2026 date **not verified** [semi] |
| January 2027 | New Democratic Congress convenes: AI and data-centre regulation risk | [F][gpb] |
| 10 Jan 2027 | Affiliates-rule suspension, rare-earth suspension and tariff truce all expire | Other researchers |
| Mid-Jan 2027 (not verified) | TSMC Q4 results; first 2027 capex guide | No 2027 guide given on 15 Oct [S][futurum] |
| 19 Jan 2027 | Meta share sales begin (about $60bn) | Other researchers |
| Not verified | BoJ, ECB and BoK December meetings | - |

## 7. Chinese suppliers on the NS-CMIC and 1260H lists
Not checked; the budget was exhausted. Skyverse, Jingce, Changchuan, Huafeng, SiCarrier, Dongfang Jingyuan and RSIC remain **unverified**.

## Could not verify (consolidated)
- The SOX record-fall figure.
- Hedge-fund deleveraging.
- The second weak "chip designer".
- Details of Citi's 23 Oct note.
- The Wells Fargo 10 Nov note.
- The causes of the 14 and 19 Aug falls and of AMAT's +15% on 30 Jul.
- CoreWeave bond details.
- The Nvidia/Huang report.
- The trend in consensus FY27 EPS revisions.
- Margin-peak fears.
- Any dated export-control trigger.
- Causes specific to probe-card makers (FormFactor, Technoprobe, MJC); none were found beyond the sector moves.
- AMAT FQ4 results.
- Exact dates for CPI, TSMC, Micron, SEMI and other central banks.

## Dated sources
[tikr]: https://www.tikr.com/blog/applied-materials-sinks-12-lam-research-down-14-as-chip-stock-rout-deepens-after-midterms "TIKR, 5 Nov 2026 (fetched)"
[trefis]: https://www.trefis.com/stock/amat/articles/623353/why-did-applied-materials-stock-fall/2026-11-06 "Trefis, 6 Nov 2026 (fetched)"
[gpb]: https://www.gpb.org/news/2026/11/05/fears-about-ai-crackdown-after-midterms-sparks-2-trillion-rout-in-tech-stocks "GPB/NPR, 5 Nov 2026 (fetched)"
[sa-fed]: https://stockanalysis.com/news/fed-holds-rates-steady-oct-2026/ "stockanalysis, 28 Oct 2026 (fetched)"
[sa-amat]: https://stockanalysis.com/stocks/amat/ "stockanalysis AMAT page and feed, 12 Nov 2026 (fetched)"
[w247-sep]: https://247wallst.com/investing/2026/09/14/chip-equipment-stocks-slide-as-ai-pacing-call-reaches-fab-spending-applied-materials-and-lam-research-fall-6-asml-sinks-5/ "24/7 Wall St, 14 Sep 2026 (fetched)"
[w247-oct]: https://247wallst.com/investing/2026/10/13/semiconductor-equipment-stocks-slide-as-investors-take-profits-on-a-huge-year-applied-materials-sinks-7-lam-research-and-kla-drop-4/ "24/7 Wall St, 13 Oct 2026"
[w247-aug]: https://247wallst.com/investing/2026/08/14/applied-materials-is-down-6-premarket-will-it-drag-down-lam-research-kla-and-other-semi-equipment-stocks/ "24/7 Wall St, 14 Aug 2026"
[rss1]: https://news.google.com/rss/search?q=chip+equipment+stocks+selloff&hl=en-US&gl=US&ceid=US:en "Google News RSS, headlines 26 Jun-11 Nov 2026"
[rss2]: https://news.google.com/rss/search?q=semiconductor+stocks+November+2026&hl=en-US&gl=US&ceid=US:en "Google News RSS, headlines Oct-12 Nov 2026"
[alpha]: https://alpha-maven.com/news/hedge-fund/chip-stocks-just-had-their-second-worst-day-on-record "AlphaMaven, ~5-6 Nov 2026 (snippet; 403)"
[hey]: https://www.heygotrade.com/en/news/nvidia-nvda-stock-news-november-6-2026/ "heygotrade, 6 Nov 2026"
[nbc]: https://www.nbcnewyork.com/news/national-international/ai-data-centers-midterm-elections/6568865/ "NBC, ~5 Nov 2026"
[finimize]: https://finimize.com/content/democrats-midterm-win-spooks-ai-and-data-center-stocks "Finimize, ~5 Nov 2026"
[fool6]: https://fool.com/investing/2026/11/06/why-micron-stock-is-up-today "Motley Fool, 6 Nov 2026"
[st-nvda]: https://stocktwits.com/news-articles/markets/equity/amd-avgo-intc-mu-chip-stocks-inch-higher-as-investors-look-past-midterms-led-selloff-nvidia-controversy/cNGAD0CR9eR "Stocktwits, ~9 Nov 2026"
[ap-jun]: https://mynews13.com/fl/orlando/ap-top-news/2026/06/23/ai-stock-slump-raises-the-question-if-investors-are-just-taking-profits-or-getting-very-nervous "AP, 23 Jun 2026"
[ap-jul]: https://feeds.ajc.com/news/2026/07/asian-shares-slip-and-south-koreas-kospi-index-sinks-11-on-heavy-selling-of-chipmaking-stocks/ "AP via AJC, 28 Jul 2026"
[invezz]: https://invezz.com/news/2026/07/17/heres-why-tokyo-electron-advantest-and-kioxia-stocks-are-plunging-today/ "Invezz, 17 Jul 2026"
[mb-amat]: https://www.marketbeat.com/instant-alerts/applied-materials-q3-earnings-call-highlights-2026-08-13/ "MarketBeat, 13 Aug 2026"
[rtt9]: https://www.rttnews.com/3698294/japanese-market-sharply-lower.aspx "RTTNews, 9 Oct 2026"
[rtt16]: https://www.rttnews.com/3699078/japanese-market-sharply-lower.aspx "RTTNews, 16 Oct 2026"
[iliv]: https://investinglive.com/central-banks/icymi-citi-now-expects-a-december-fed-rate-hike-after-hotter-september-us-inflation/ "investinglive, mid-Oct 2026"
[roic14]: https://www.roic.ai/news/ai-infrastructure-stocks-tumble-as-coreweave-bond-yield-spike-ignites-financing-fears-10-14-2026 "roic.ai, 14 Oct 2026 (snippet; 403)"
[roic15]: https://www.roic.ai/news/ai-financing-shock-hits-tech-stocks-as-debt-costs-bite-10-15-2026 "roic.ai, 15 Oct 2026"
[roic-cpi]: https://www.roic.ai/news/even-a-small-cpi-beat-could-seal-december-fed-rate-hike-russell-investments-warns-11-09-2026 "roic.ai, 9 Nov 2026"
[stw-lrcx]: https://stocktwits.com/news-articles/markets/equity/lrcx-stock-sinks-as-analysts-trim-targets-see-supply-constraints-but-longer-term-bull-case-remains/cZxwBbwRBww "Stocktwits, ~22 Oct 2026"
[technews]: https://finance.technews.tw/2026/10/22/lam-research-forecast-fails-to-impress-shares-drop-nearly-7-after-hours/ "TechNews TW, 22 Oct 2026"
[pluang]: https://pluang.com/en/news-feed/masalah-saham-peralatan-chip-baru-mulai "Pluang relay of Barron's/Citi, ~23 Oct 2026"
[zacks]: https://www.zacks.com/stock/news/2994891/the-zacks-analyst-blog-highlights-applied-materials-lam-research-and-kla "Zacks, undated 2026"
[mb-lrcx]: https://www.marketbeat.com/instant-alerts/fy2027-eps-estimates-for-lam-research-decreased-by-analyst-2026-07-20/ "MarketBeat, 20 Jul 2026"
[rallies-kla]: https://rallies.ai/news/kla-sees-2027-growth-outpacing-2026-after-raising-revenue-and-eps-guidance "rallies.ai, undated"
[ss]: https://streetsignal.substack.com/p/amat-preview "StreetSignal AMAT preview, ~Nov 2026"
[semi]: https://semi.org/en/semi-press-release/global-semiconductor-equipment-sales-projected-to-reach-a-record-of-156-billion-dollars-in-2027-semi-reports "SEMI, 16 Dec 2025; mid-2026 update via search"
[fortune]: https://fortune.com/2026/07/17/ai-boom-debt-blitz-investor-demand-hyperscaler-bond-issuance/ "Fortune, 17 Jul 2026"
[ifre]: https://www.ifre.com/people-and-markets/2348522/ai-financing-boom-begins-to-show-cracks-as-investors-balk-at-debt-binge "IFRE, undated 2026"
[ifre2]: https://www.ifre.com/bonds/2463746/bond-market-begins-to-question-ai-boom-as-beignet-sequel-falls-flat "IFRE, undated 2026"
[crn]: https://www.crnasia.com/news/2026/components-and-peripherals/tsmc-third-quarter-revenue-tops-guidance-as-ceo-says-ai-dema "CRN Asia, ~15 Oct 2026"
[futurum]: https://futurumgroup.com/?p=96944 "Futurum, ~15 Oct 2026"
[days]: https://days.to/micron-earnings "days.to, accessed 12 Nov 2026"
[aiw]: https://aiweekly.co/alerts/micron-q4-revenue-jumps-379-to-542b-on-ai-memory-demand-guides-fiscal-2027-q1 "AI Weekly, ~30 Sep 2026"

Dated source list (same links, readable form):
- 23 Jun: AP.
- 13 Aug: MarketBeat.
- 14 Aug: 24/7 Wall St.
- 17 Jul: Fortune, Invezz.
- 28 Jul: AP/AJC.
- 14 Sep: 24/7 Wall St.
- 9 Oct: RTTNews.
- 13 Oct: 24/7 Wall St.
- 14-15 Oct: roic.ai; CRN Asia; Futurum.
- 16 Oct: RTTNews.
- 22 Oct: TechNews; Stocktwits.
- 23 Oct: Pluang/Barron's.
- 28 Oct: stockanalysis.
- 5 Nov: TIKR; GPB/NPR; NBC; Finimize; AlphaMaven.
- 6 Nov: Trefis; heygotrade; Motley Fool.
- 9 Nov: roic.ai; Stocktwits.
- 12 Nov: stockanalysis AMAT; Google News RSS (headlines 26 Jun-12 Nov).

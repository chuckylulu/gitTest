# Demand cycle, physical bottlenecks and trade-policy backdrop for leading-edge chip manufacturing (as of 14 November 2026)

**Purpose.** Test two earlier judgements: (a) leading-edge fabrication and lithography are constraints AI demand cannot remove; (b) roughly a one-in-four chance of a pause in AI spending around 2028.

**Tag key.** [FILING] filed or audited figure (also used for official government documents: Federal Register, proclamations, ministry notices); [COMPANY CLAIM] company statement no outside party has confirmed; [CONFIRMED] company statement confirmed by a named outside party; [ESTIMATE] third-party estimate, forecast or industry statistic; [PRESS] press report resting on unnamed sources or not traced to a primary document. "My calc" marks my arithmetic on cited figures.

**Method limits.** The shared web-search budget for this session ran out about a third of the way through; the rest came from direct fetches of known pages, SEC filings and XBRL data (data.sec.gov) and exchange price data. What I could not reach is listed in section 8. Quarterly figures are for July–September 2026 unless stated.

**Reading in one paragraph (mine; facts follow).** Suppliers and buyers both say supply, not demand, limits AI computing through 2027–28. By their own statements the tightest items are memory and powered data-centre space; EUV tools and leading-edge wafers join the list for 2027–28. All are being expanded with money on lags of two to four years, so "cannot remove" holds for about two years and weakens after that. The spending now runs at about 100% of the four largest buyers' operating cash flow, with about $370bn of bonds issued in 2026, and two mainstream forecasters already pencil in a stall or a fall for 2028 while two others still forecast growth. I put the chance of an outright fall in aggregate spending around 2028 at about 30% (range 20–40%), similar to or somewhat above one in four, and the chance of a growth stall that suppliers would feel at about one in two. Applied Materials, Lam and KLA shares are 48–50% below their June 2026 highs, with no fall in revenue yet.

## 1. AI capital spending: actuals, guidance, financing, returns, strain, forecasts

### Takeaway
The five largest US buyers spent about $412bn in 2025 and about $560bn in January–September 2026 (+100% year on year), an annualised rate of about $920bn in the latest quarter; all five say 2027 will be higher and none has given a number. Capital spending by the four largest rose from 65% of operating cash flow in 2025 to about 100% in January–September 2026, with the gap funded by record bond issuance, leases and customer prepayments.

### Cited Findings

**Table 1. Cash purchases of property and equipment, US$bn (excludes finance leases unless stated).** [FILING: SEC XBRL, 10-K/10-Q data; sums, growth rates and ratios are my calc]

| Company | Calendar 2025 | Jan–Sep 2026 (y/y) | Latest quarter | Capex ÷ operating cash flow | 2026 guidance [COMPANY CLAIM] | 2027 statement [COMPANY CLAIM] | Long-term debt, end-2024 → end-2025 → 30 Sep 2026 |
|---|---|---|---|---|---|---|---|
| Microsoft | 83.1 (FY to Jun 2025: 64.6; FY to Jun 2026: 115.9) | 106.1 (+99%) | 39.4; 45.2 incl. finance leases | 68%; 78% incl. leases | Calendar 2026 about 170 incl. finance leases (175 in July; cut for "3P capacity delays"); Oct–Dec above 50 | FY2027 capex to grow; no number | 45.0 → 40.3 → 35.5 |
| Alphabet | 91.5 | 132.0 (+107%) | 51.4 | 104% (9M); 121% (Q3) | 195–205 (raised in July from 180–190) | "increase significantly"; detail in January | 10.9 → 46.6 → 125.1 |
| Amazon | 131.8 | 175.7 (+90%) | 77.3 gross; 75.9 "cash capex" | 154% (9M) | about 220 | "meaningfully more" | 58.0 → 68.8 → 180.9 |
| Meta | 69.7 (72.2 incl. finance leases) | 83.1 (+72%) | 34.9 incl. finance leases | 86% (9M); above 100% (Q3) | 135–145 | budget not set; "upward pressure" | 28.8 → 58.7 → 80.9 |
| Oracle | 35.5 (Dec 2024–Nov 2025); FY to May 2026: 55.7 | 63.6 (Dec 2025–Aug 2026; +171%) | 28.5 (Jun–Aug) | 174% (FY to May 2026); 123% (Jun–Aug) | FY to May 2027: 90–95 gross, at most 70 net of prepayments | none | about 125 total debt [PRESS] |
| **Five** | **about 412** | **about 560 (+100%)** | **231 (about 920 annualised)** | four largest: 65% (2025) → 100% (Jan–Sep 2026) | about 810–835 (mixed year bases) | | |

Sources: SEC XBRL for [Microsoft](https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json), [Alphabet](https://data.sec.gov/api/xbrl/companyconcept/CIK0001652044/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json), [Amazon](https://data.sec.gov/api/xbrl/companyconcept/CIK0001018724/us-gaap/PaymentsToAcquireProductiveAssets.json), [Meta](https://data.sec.gov/api/xbrl/companyconcept/CIK0001326801/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json), [Oracle](https://data.sec.gov/api/xbrl/companyconcept/CIK0001341439/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json) (operating cash flow and debt from the same API, tags `NetCashProvidedByUsedInOperatingActivities`, `LongTermDebt` or `LongTermDebtNoncurrent`); guidance from the [Alphabet call, 28 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/), [Amazon call, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/), [Meta call highlights, 21 Oct 2026](https://www.marketbeat.com/instant-alerts/transcript-meta-platforms-q3-earnings-call-highlights-2026-10-21/), [Oracle call highlights, 10 Sep 2026](https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/?.tsrc=rss), [Microsoft Q1 FY2027 analysis](https://beancount.io/blog/2026/11/07/microsoft-fy2027-q1-earnings-analysis).

- Microsoft spent $45.2bn including finance leases, below the "over $50bn" guided in July, "as some third-party capacity deliveries we expected in Q1 were delayed"; about three-quarters went on short-lived assets; free cash flow fell 27% to $18.6bn; OpenAI supplied $10.0bn of the quarter's revenue (about 10.8%) and owed $7.2bn of receivables [COMPANY CLAIM, secondary write-up of the call and 10-Q] — [beancount.io](https://beancount.io/blog/2026/11/07/microsoft-fy2027-q1-earnings-analysis); cash figure $39.37bn [FILING] — [24/7 Wall St, 28 Oct 2026](https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb). In July it lengthened building lives from 15 to 25 years and restated calendar-2026 capex from $190bn to about $175bn [COMPANY CLAIM] — [CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/).
- Alphabet: free cash flow −$9.1bn in the quarter; purchase commitments $924bn plus $152bn of leases not yet started; it began "utilizing third-party compute capacity at the end of Q3" "given the supply constrained environment" [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/).
- Amazon: "We can fund this plan"; AWS "can grow north of 40% in each of 2027 and in 2028"; "There's only so many chips that provider can provide each year" [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/). Trailing twelve-month free cash flow was −$42.4bn [COMPANY CLAIM via press] — [Constellation Research, 29 Oct 2026](https://www.constellationr.com/insights/news/aws-q3-revenue-growth-surges-39-capex-stings-amazons-cash-flow).
- Meta's unconditional purchase obligations rose from $58.1bn (30 Sep 2025) to $355.7bn (30 Sep 2026) [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001326801/us-gaap/UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount.json).
- Oracle: remaining performance obligations $664bn; most new contracts came "through customer prepayments or bring-your-own-hardware deals"; a $20bn at-the-market share sale was completed in the quarter [COMPANY CLAIM] — [call highlights](https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/?.tsrc=rss).

**Other buyers.**
- CoreWeave: purchases of property and equipment $23.6bn in January–September 2026; debt $47.5bn and contracted backlog $132.3bn at 30 Sep 2026 [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001769628/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json).
- OpenAI raised $122bn at $852bn post-money in March 2026; its cumulative cash outflow to 2030 was reported at $665bn [PRESS] — [The Decoder, 27 Feb 2026](https://the-decoder.com/openais-up-to-110-billion-raise-lines-up-almost-exactly-with-the-111-billion-it-just-added-to-its-cash-burn-forecast/). A first close of about $11bn on 6 November 2026 compared with a reported target of $30bn or more [PRESS]; the finance chief confirmed the $1.25tn pre-money valuation and said the business grew 70% quarter on quarter, without a revenue figure [COMPANY CLAIM] — [24/7 Wall St, 7 Nov 2026](https://247wallst.com/investing/2026/11/07/openai-just-raised-11-billion-at-a-1-25-trillion-valuation).
- Anthropic (prospectus, as relayed by Reuters): about $518bn of compute and infrastructure obligations over a decade, about 80% non-cancellable — Google $111.1bn, Amazon $110bn, Microsoft $31.4bn, Broadcom equipment leases $161.2bn, capacity hosted by xAI/SpaceX up to $84.5bn through 2029 [PRESS] — [TechTarget, 29 Sep 2026](https://www.techtarget.com/it-infrastructure/news/366651336/Report-Anthropic-locks-in-518B-AI-infrastructure-commitments). An earlier report in this repository records nine-month 2026 revenue of $33.2bn (`reports/Automated security quality and entry points.md`).
- Nvidia: revenue $215.9bn in the year to January 2026 and $177.8bn in the next six months; long-term debt rose from $8.5bn to $33.4bn by 26 Jul 2026 [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001045810/us-gaap/LongTermDebt.json). It holds stakes in customers it supplies [PRESS] — [Trending Topics, 27 Aug 2026](https://www.trendingtopics.eu/nvidia-posts-another-blockbuster-quarter-but-debt-is-rising-in-ai-frenzy/).
- Sovereign programmes: the EU's call for up to seven AI "gigafactories" carries $11.5bn of public money and seeks at least $23bn of private money; bids closed on 12 November 2026 and winners are expected in early 2027 [PRESS] — [AI Business, 31 Jul 2026](https://aibusiness.com/data-centers/eu-pledges-11-5b-seven-ai-gigafactories).

**Financing.**
- US investment-grade bond sales reached a record $1.88tn in the year to 4 November (LSEG); Amazon, Alphabet, Meta, Microsoft and Oracle issued more than $370.7bn, about a fifth; Oracle's five-year credit default swap hit a record 325.45 basis points "last month" [ESTIMATE/PRESS] — [Finimize, undated; year inferred as 2026 from the filed debt figures above](https://finimize.com/content/big-techs-ai-bond-binge-pushed-us-issuance-to-a-record).
- Bond cover ratios fell from nearly 5 times in February to below 2 times in July 2026 (Apollo); the Bank for International Settlements warned in June that disappointing AI returns "could trigger a sudden financing pullback" [ESTIMATE] — [Reuters via Express Tribune, 17 Jul 2026](https://tribune.com.pk/story/2618784/among-ai-crowd-some-investors-position-for-slower-hyperscaler-spending-growth).
- Morgan Stanley (15 Oct 2026): hyperscalers and specialised clouds post their most negative free cash flow in 2027, with cash burn approaching $600bn; about $255bn of unsecured hyperscaler bonds had been issued by mid-October; they could add $400bn of debt in 2027 while keeping adequate coverage [ESTIMATE] — [Crypto Briefing, 18 Oct 2026](https://cryptobriefing.com/morgan-stanley-hyperscaler-cash-burn-2027/).
- Customers also fund suppliers: Micron holds $32bn of customer financial commitments, "mostly cash deposits", under 26 multi-year "take or pay" agreements [COMPANY CLAIM] — [Blocks & Files, 1 Oct 2026](https://www.blocksandfiles.com/flash/2026/10/01/memory-gold-rush-bonanza-makes-billions-for-micron/5300445).

**Revenue and returns.**
- Google Cloud: revenue $30.7bn (+103%), operating margin 36.2%, backlog $561bn, "tens of billions of dollars in AI revenues year-to-date" [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/). AWS: revenue $46.0bn (+39.3%), margin 38.7%, backlog $578bn [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/). Microsoft: remaining performance obligations $683bn at 30 Sep 2026 [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/us-gaap/RevenueRemainingPerformanceObligation.json); Azure +48% [COMPANY CLAIM] — [24/7 Wall St](https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb).
- Capital Economics calculates that external AI revenue must grow about tenfold by 2030 to justify the spending [ESTIMATE] — [Fortune, 8 Nov 2026](https://fortune.com/2026/11/08/stock-market-outlook-sp500-ai-capex-gdp-growth-productivity/).

**Signs of strain as of mid-November 2026.**
- After Democratic wins in the 3 November midterms raised fears of data-centre moratoriums, the Philadelphia Semiconductor Index fell 12.25% on 5 November, its second-largest one-day fall on record [CONFIRMED by exchange prices] — [24/7 Wall St, 6 Nov 2026](https://247wallst.com/investing/2026/11/06/chip-stocks-just-had-their-second-worst-day-on-record/).
- Morgan Stanley (8–9 November): 20% of US data-centre projects planned for 2028 (about 5 GW) may slip to 2029; US capacity additions −4% in 2028, then +38% in 2029; parts of the supply chain could see "a traditional downcycle in 2028" [ESTIMATE] — [investingLive, 9 Nov 2026](https://investinglive.com/stocks/morgan-stanley-says-buy-the-ai-dip-sees-3-4-trillion-in-hyperscaler-spending-through-2028/). UBS puts about 30% of expected 2028 US capacity additions at risk, 18 GW of the pipeline in Texas [ESTIMATE, bank note not seen] — [Finimize](https://finimize.com/content/ubs-flags-a-post-midterms-speed-bump-for-data-centers).
- Texas froze air permits for data centres from 21 September 2026; New York has a one-year moratorium; more than 300 local moratoriums or bans are in force, though only about 2.3 GW was "genuinely delayed" as of September [ESTIMATE] — SemiAnalysis, [1 Nov 2026](https://newsletter.semianalysis.com/p/the-datacenter-backlash-goes-bipartisan) and [15 Sep 2026](https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums).
- TSMC: "we are being prudent in our business planning going into 2027", citing consumer markets squeezed by "rising component prices" [COMPANY CLAIM] — [The Next Web, 17 Oct 2026](https://thenextweb.com/news/tsmc-q3-2026-record-profit-prudent-2027). Notebook shipments fell 15.8% quarter on quarter and PC makers are trimming 2027 memory orders as inventories build [ESTIMATE] — [TrendForce, 11 Nov 2026](https://www.trendforce.com/presscenter/news/20261111-13303.html).

**Published forecasts.**

| Source (date) | Scope | 2026 | 2027 | 2028 and after |
|---|---|---|---|---|
| Goldman Sachs (25 Sep 2026) [ESTIMATE] | five largest US buyers | about $800bn | $1.2tn (consensus $1.1tn) | 2028 given as $1.4tn in one report and $2tn in another; $7.6tn cumulative 2026–31 |
| Morgan Stanley (15 Oct; reaffirmed 8 Nov 2026) [ESTIMATE] | hyperscalers plus AI clouds | about $980bn | $1.58tn | $1.81tn, "some downside risk" |
| TrendForce (3 Aug 2026) [ESTIMATE] | nine largest cloud providers, five US and four Chinese | over $886.7bn (+90%) | about $1.3tn (+50%) | |
| UBS (Jul 2026) [ESTIMATE] | hyperscalers | $673bn (+76%) | +25% | +6% |
| Capital Economics (6 Nov 2026) [ESTIMATE] | AI investment | about $800bn | rising, more slowly | falls about 10% in 2028 |
| Jefferies (2026) [PRESS, note not seen] | large buyers | | may fall short of $1.04tn consensus | "may have peaked" |
| Apollo (6 Aug 2026) [ESTIMATE] | hyperscaler capex, % of US GDP | 1.4% in 2025 | 3.1% | about 3% a year 2027–29 |

Sources: Goldman via [PYMNTS](https://www.pymnts.com/?p=4233514) and [Crypto Briefing](https://cryptobriefing.com/goldman-sachs-ai-infrastructure-capex-2027/), which quotes it calling 2027 spending "a larger share of GDP than any technological investment cycle since the railroad build-out in the late 1800s"; Morgan Stanley via [Crypto Briefing](https://cryptobriefing.com/morgan-stanley-hyperscaler-cash-burn-2027/) and [investingLive](https://investinglive.com/stocks/morgan-stanley-says-buy-the-ai-dip-sees-3-4-trillion-in-hyperscaler-spending-through-2028/); [TrendForce](https://www.trendforce.com/presscenter/news/20260803-13161.html); [UBS via Reuters](https://tribune.com.pk/story/2618784/among-ai-crowd-some-investors-position-for-slower-hyperscaler-spending-growth); [Capital Economics via Fortune](https://fortune.com/2026/11/08/stock-market-outlook-sp500-ai-capex-gdp-growth-productivity/); [Jefferies via FourWeekMBA](https://fourweekmba.com/ai-jefferies-google-meta-peers-202b-capex-may-have-peaked/); [Apollo](https://www.apollo.com/wealth/insights-news/insights/daily-spark/the-ai-capex-boom-is-building-twice-as-fast-as-the-housing-boom).

### Inferences
- Demand evidence and financing evidence point in opposite directions. Cloud revenue is accelerating and backlogs total about $2.6tn across Microsoft, Alphabet, Amazon, Oracle and CoreWeave. But the backlogs overlap: a large part is the same commitments by two loss-making labs, whose ability to pay depends on capital markets. Microsoft alone took about 11% of its revenue from OpenAI.
- Self-funding has ended for three of the five: Alphabet, Amazon and Meta added about $213bn of long-term debt in nine months (my calc from Table 1). Microsoft is the exception.
- The first visible shortfall against guidance (Microsoft) came from late delivery of capacity, not weak demand. A deployment bottleneck defers chip purchases just as a financing pause would.

### Gaps
- xAI: no primary figures found. Sovereign programmes in the Gulf, Japan, Korea and India: only unsourced secondary figures found, so not cited.
- Microsoft's calendar-2026 figure and OpenAI revenue share come from a secondary write-up, and Oracle's total debt from one press report; both need the transcripts and 10-Qs.
- Off-balance-sheet financing totals for 2026 (joint ventures, private credit) were not obtained.

## 2. The probability of a pause around 2028

### Takeaway
The one-in-four figure was never derived: it entered the earlier work as a stated prior. Independent evidence supports a similar or somewhat higher number for an outright fall in spending around 2028, and about one in two for a growth stall. Confidence is low because every source defines "pause" differently.

### Cited Findings

**How the figure arose.**
- The research prompts state "a financing-led pause around 2028 (about 25%)" beside steady growth (about 55%) and faster acceleration (about 20%), under the instruction "Treat the probabilities below as priors" — `prompts/Company research prompts.md`, line 38. Both reports apply the weights without a calculation; one says "The scenario readings are the research team's judgements" — `reports/Automated security quality and entry points.md`, line 152. The supporting note lists credit indicators and 2027 guidance from Alphabet, Amazon and Oracle as "not obtained" — `research_notes/Verification and specification company ranking/sector_valuation_cycle.md`, section 5.

**Base rates.**

| Cycle | What happened | Source |
|---|---|---|
| Combined capex of Microsoft, Alphabet, Amazon and Meta, 2017–2025 | +30%, +60%, **+8% (2019)**, +34%, +34%, +20%, **−7% (2023)**, +55%, +65%: one fall and one stall in nine years, each after growth of 20–60% | [FILING, my calc] [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001018724/us-gaap/PaymentsToAcquireProductiveAssets.json) |
| Telecom and fibre, 1996–2002 | Telecom capex peaked at 1.2% of US GDP in 2000 after rising 0.4 points; hyperscaler capex is forecast at 3.1% in 2027 after rising 2.5 points in four years. By 2002, 2.7% of fibre was in use | [ESTIMATE] [Apollo](https://www.apollo.com/wealth/insights-news/insights/daily-spark/the-ai-capex-boom-is-building-twice-as-fast-as-the-housing-boom); [M. Alderson, citing the Wall Street Journal](https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/) |
| Chip-industry echo of 2000–02 | TSMC sales −24% and utilisation 106% → 51% (2001); ASML sales −41% (2001); Applied Materials −53% (FY2000–03); Micron −59% (FY2000–02) | [FILING] section 5 |
| Memory | Micron's revenue fell in 6 of the 16 fiscal years 2010–2025 | [FILING, my calc] [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000723125/us-gaap/Revenues.json) |
| Equipment | Applied Materials' revenue fell in 5 of the 18 fiscal years 2008–2025; Lam's in 3 of the 16 fiscal years 2010–2025 | [FILING, my calc] [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000006951/us-gaap/Revenues.json) |

**Stated odds, surveys and markets.**
- FutureSearch (15 Aug 2026): 15% for a "significant pullback in AI capex by December 31, 2027", meaning a year-on-year decline or a guidance cut above 10% attributed to moderating AI investment; it notes that "consensus expectations point toward a sharp deceleration in spending growth, not a decline" [ESTIMATE] — [FutureSearch](https://futuresearch.ai/app/p/a/ai-pullback-2027).
- Polymarket, "AI bubble burst by June 30, 2027": about 26.5% on 7 November 2026 after 31% on 5 November; it resolves Yes only if three of six listed market events fall within one 90-day window [PRESS, market page not seen] — [FourWeekMBA](https://fourweekmba.com/ai-polymarkets-ai-bubble-test-chip-etf-down-37-5-nvidia-22/).
- Bank of America fund manager survey, July 2026: 28% expected a hyperscaler to announce a capex cut in 2026; 48% named hyperscaler capex the most likely source of a systemic credit event; 45% named an AI bubble the top tail risk [ESTIMATE] — [Webull/Benzinga, 15 Jul 2026](https://www.webull.com/news/15231944027677696). October 2026: AI bubble named by 23%; 45% expect a bubble to form in 2027 and 42% do not [ESTIMATE] — [Crypto Briefing, 15 Oct 2026](https://cryptobriefing.com/bofa-survey-fund-managers-overweight-tech/).
- Base cases that already contain a 2028 stall: UBS +6%; Capital Economics −10%; Morgan Stanley US capacity additions −4% (section 1).

**Evidence against a pause.**
- All five large buyers guided 2027 higher in late October 2026 (Table 1). Nvidia guided growth of about 70% for the year to January 2028, described as a supply-constrained outlook, and its supply commitments more than doubled to $279bn, "primarily for memory procurement" [COMPANY CLAIM, single secondary source, paraphrase] — [SentiSense, 26 Aug 2026](https://app.sentisense.ai/stories/nvidia-beats-across-the-board-guides-108-billion-with-zero-china-revenue-assume-08262026).
- Supply contracts now run past 2028 (section 3): SK hynix is sold out "through 2029" and ASML reports interest in orders for 2029 and 2030 [COMPANY CLAIM] — [Kyunghyang Shinmun](https://www.khan.co.kr/en/article/202610281734027), [Unite.AI](https://www.unite.ai/asml-warns-2027-2028-chip-tool-output-will-fall-short-of-ai-demand).
- KLA: physical constraints mean "we're going to have a longer cycle in terms of the growth" [COMPANY CLAIM] — [KLA call, 28 Oct 2026](https://www.webull.com/news/15828153893520384).

### Inferences
**My reading (labelled as mine).** The answer depends on the definition, so I give three.

| Definition | My probability | Reasoning |
|---|---|---|
| Aggregate capex of the five largest buyers falls year on year in calendar 2028 | about 20–25% | Similar to the prior. Capital Economics has a 10% fall in its 2028 base case and UBS a near-stall (+6%), while Goldman and Morgan Stanley still forecast growth; contracts and backlogs cover 2027–28 |
| It falls in 2028 or 2029 (the sense of "around 2028") | about 30% (range 20–40%) | Somewhat above the prior. The past decade shows one fall and one stall in nine years, each after growth of 20–60%. The current run is +55%, +65%, about +100% and "up" again, at 100% of operating cash flow with debt funding the margin. Power and permitting add a second route to the same outcome |
| Growth below 10% in 2028 or 2029 (a stall suppliers would feel) | about 50% | UBS's base case for 2028 is +6%. A stall at this scale still means flat or lower orders for wafers, tools and memory |

- Since the prior was set, three things moved the odds up: the scale of external financing shown in the quarterly filings; the post-midterm permitting risk to 2028 US capacity; and OpenAI's smaller-than-sought round. Two moved them down: every buyer guided 2027 higher, and supply contracts lengthened to 2028–2030.
- The prior calls the pause "financing-led". On this evidence a pause is as likely to be led by power, permits and delivery delays, with financing as the amplifier. For chip, tool and materials makers the distinction matters little: orders slip either way.
- Confidence is low. No source measures the same event: FutureSearch's 15% covers a window ending in 2027, Polymarket's 26.5% covers share prices to mid-2027, and the strategists give paths without probabilities. A claim of precision finer than about ±10 points would overreach.

### Gaps
- No Kalshi or Metaculus market on AI capital spending was found, nor the November 2026 Bank of America survey.
- A sourced series for US telecom capital spending after 2000 was not obtained; chip-industry filings stand in as the measured echo of that bust.

## 3. What limits the supply of AI chips in 2026–2028

### Takeaway
By the suppliers' own statements, memory and powered data-centre space are the tightest items now; advanced packaging is easing; EUV output did not limit chip makers in 2026 but ASML says its 2027–28 supply will fall short of demand; TSMC says wafer demand exceeds supply and tools are tight. Every one of these is being expanded, on lags of one to four years.

### Cited Findings

**Table 3. Constraint by constraint.**

| Constraint | Dated evidence that it binds, or does not | Lead times and supplier view for 2027–28 |
|---|---|---|
| Leading-edge wafers (3nm, 2nm) | TSMC, 15 Oct 2026: "we still think the demand is higher than the supply, and we are working very hard to narrow the gap"; "the tool supply is tight"; "The tool price inflation is real". 3nm was 33% and 2nm 8% of wafer revenue [COMPANY CLAIM] | 2nm capacity to "more than double by 2027"; new Tainan 3nm fabs in H1 2027 and H1 2028; Arizona fab 2 in volume in Q3 2027; 2026–28 capex "even more significantly higher than the past three years" [COMPANY CLAIM]. 3nm from over 180,000 to 210,000 wafers a month and 2nm from 90,000 to 110,000 between end-2026 and mid-2027; wafer prices up 3–6% from January 2027 [PRESS] |
| Advanced packaging (CoWoS) | Gap about 20% in June 2026, seen at about 10% by end-2026; in October supply "remains tight" and a price rise of up to 20% was reported; final test takes about four times (Blackwell) to seven times (Rubin) as long as the previous generation [PRESS/ESTIMATE] | About 130,000 wafers a month at end-2026 to 260,000 at end-2028 [PRESS]; Goldman: 1.275m wafers in 2026, 2.73m in 2027, 3.48m in 2028 [ESTIMATE]; TrendForce expects the shortage to "begin moderating by 2027" [ESTIMATE]; equipment lead times six to eight months [PRESS] |
| HBM and DRAM | SK hynix, 28 Oct 2026: DRAM and HBM "effectively all sold out for the next three years, through 2029"; customers ask for more than twice the HBM available. Micron, Sept 2026: conditions "much tighter in fiscal 2027 and 2028 than they were in 2026"; "we do not have line of sight to when supply and demand will return to balance". Samsung, 29 Oct 2026: demand next year will "far exceed supply" [COMPANY CLAIM] | Clean-room space is the limit: Micron's Idaho 1 starts output mid-2027, Idaho 2 and a Japan fab late 2028; SK hynix: "more investment or more fabs does not necessarily mean more supply" because "clean rooms will be opened in phases"; achievable 2027 DRAM bit growth mid-20s% [COMPANY CLAIM]. SEMI: 300mm memory capacity 4.1m wafers a month in 2026 and 4.2m in 2027 [ESTIMATE] |
| EUV tools | July 2026: about 65 low-NA systems to ship in 2026; "the capacity is there to meet the demand, but the demand is still fluctuating". October 2026: planned supply for 2027 and 2028 "will not fully meet customer demand" [COMPANY CLAIM] | Capacity +30% in 2027 (about 85 systems; about +45% in wafer output from newer models); a further 30% (a "110 scenario") under study for 2028, plus ways to exceed it; 2027 "close to being fully covered with orders"; a Zeiss component caps one model; a new campus serves "beyond 2028" [COMPANY CLAIM] |
| Other tools and clean rooms | KLA, 28 Oct 2026: lead times "averaging right around 12 months" and lengthening; one customer is "desperate for more capacity and they can't take equipment because their clean room is delayed". Lam, 21 Oct 2026: "clean-room availability and supply constraints for certain components may limit" the industry in 2027 [COMPANY CLAIM] | SEMI: 300mm fab construction spending $47.5bn in 2026 (+23%) and $63.3bn in 2027 (+33%); 20 new fabs or lines start construction in 2026; 23 begin operating in 2027 [ESTIMATE] |
| Power, grid, turbines, transformers | Microsoft's capex shortfall came from late third-party capacity (section 1). Morgan Stanley: shortage of powered capacity above 30% through 2028 [ESTIMATE]. TSMC is sending teams to check US data-centre construction and power supply [PRESS] | GE Vernova: gas-turbine backlog plus slot reservations 116 GW at mid-2026 against output of 20 GW a year (24 GW in 2028, 30 GW in 2030); customer talks reach 2032 [COMPANY CLAIM]. Transformers three to five years, gas turbines more than five [ESTIMATE, one analyst]. SemiAnalysis: 38 GW of US capacity due in 2027 (22 GW under vertical construction); 62.2 GW modelled for 2028, mostly not started [ESTIMATE] |

Sources: TSMC — [call transcript, 15 Oct 2026](https://www.webull.com/news/15751044230423552), [capacity report, 14 Sep 2026](https://www.trendforce.com/news/2026-09-14/news-tsmc-reportedly-targets-22-2nm-16-3nm-capacity-boost-by-mid-2027-cowos-to-double-by-2028/); packaging — TrendForce [15 Jun 2026](https://www.trendforce.com/news/2026/06/15/news-tsmc-cowos-supply-demand-gap-reportedly-seen-narrowing-from-20-to-10-by-end-2026-as-capacity-expands) and [27 Oct 2026](https://trendforce.com/news/2026/10/27/news-tsmc-reportedly-eyes-20-cowos-price-hike-skips-equipment-price-renegotiations-amid-ai-demand-surge); memory — SK hynix via [Kyunghyang Shinmun](https://www.khan.co.kr/en/article/202610281734027) and a [call summary](https://finsee.ai/earnings/skhy/2026/q3/en/), [Micron](https://www.blocksandfiles.com/flash/2026/10/01/memory-gold-rush-bonanza-makes-billions-for-micron/5300445), [Samsung](https://lightreading.com/finance/memory-boom-carries-samsung-to-another-bumper-quarter), [SEMI, 29 Jun 2026](https://www.prnewswire.com/news-releases/semi-projects-300mm-memory-equipment-investment-to-surpass-50-billion-in-2026-302811354.html); EUV — ASML [call, 15 Jul 2026](https://www.fool.com/earnings/call-transcripts/2026/07/15/asml-asml-q2-2026-earnings-call-transcript/) and [results, 14 Oct 2026](https://investinglive.com/stocks/asml-says-2027-and-2028-supply-will-fall-short-of-demand-as-q3-sales-hit-a-record/); tools — [KLA call](https://www.webull.com/news/15828153893520384), [Lam call highlights](https://www.marketbeat.com/instant-alerts/transcript-lam-research-q1-earnings-call-highlights-2026-10-21/), [SEMI, 13 Oct 2026](https://www.prnewswire.com/news-releases/global-300mm-fab-equipment-spending-to-reach-227-billion-in-2029-as-buildout-accelerates-semi-projects-302906628.html); power — [GE Vernova, 23 Jul 2026](https://www.turbomachinerymag.com/view/ge-vernova-gas-turbine-backlog-hits-116-gw-as-power-orders-more-than-double), [analyst via TechTarget](https://www.techtarget.com/it-infrastructure/news/366651336/Report-Anthropic-locks-in-518B-AI-infrastructure-commitments), [SemiAnalysis](https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums), [Morgan Stanley](https://investinglive.com/stocks/morgan-stanley-says-buy-the-ai-dip-sees-3-4-trillion-in-hyperscaler-spending-through-2028/), [The Next Web](https://thenextweb.com/news/tsmc-q3-2026-record-profit-prudent-2027).

**Does ASML limit chip makers, or do chip makers limit ASML?**
- Through mid-2026, chip makers' plans set ASML's shipments. Chief executive Fouquet on 15 July 2026: "Short answer is, yes, the capacity is there to meet the demand, but the demand is still fluctuating"; the finance chief said ASML was building ahead of purchase orders and "We're not sharing order intakes" [COMPANY CLAIM] — [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/07/15/asml-asml-q2-2026-earnings-call-transcript/).
- By 14 October 2026 ASML said the direction reverses for 2027–28: "adding 30% more capacity in 2027 and another 30% in 2028 will not allow ASML to meet customer demand"; "A lot of order intake is now for 2028"; customers expect their own supply to fall short "at least until 2028" [COMPANY CLAIM] — [Unite.AI](https://www.unite.ai/asml-warns-2027-2028-chip-tool-output-will-fall-short-of-ai-demand). TSMC's "the tool supply is tight" the next day supports the direction, without numbers [CONFIRMED in direction by TSMC] — [TSMC call](https://www.webull.com/news/15751044230423552). With no published order intake, the claim cannot be checked against bookings.
- The pull is led by memory: ASML expected memory-related system sales to grow over 75% in 2026 against over 25% for advanced foundry [COMPANY CLAIM] — [Q2 call](https://www.fool.com/earnings/call-transcripts/2026/07/15/asml-asml-q2-2026-earnings-call-transcript/).
- The earlier work's figures (about 65 EUV tools a year, about 30% more in 2027) match ASML's statements.

### Inferences
**My reading (labelled as mine).**
- Ranking of tightness today, by what suppliers say and by price behaviour: memory first (sold out to 2029; Micron's gross margin is 87% and SK hynix's operating margin 80%); powered data-centre space second; leading-edge wafers and EUV third (TSMC raises wafer prices by 3–6%, not multiples, on a 66% gross margin); packaging fourth and easing. This fits the earlier work's own sequence ("memory, power connection and financing in 2026–2028") better than the claim that fabrication and lithography are the constraint.
- If AI demand doubled against current plans for 2027–28, memory and powered space would bind first: both are already short by a factor of 1.3 to 2. Wafers and EUV would bind next: TSMC's planned increases to mid-2027 are 16–22%, and ASML is already short at +30% a year.
- Could money remove each within two to three years? Packaging and test: yes, in 12–18 months. Leading-edge wafers: partly; shells under way deliver in 2027–28, a new fab takes longer, and 2027 EUV slots are sold. Memory: only from late 2028, when new clean rooms open. EUV: partly; ASML is studying more than +30% for 2028, but optics supply and the new campus point past 2028. Power: partly and at higher cost, through on-site generation; turbine slots run into the 2030s and grid connections are not for sale.
- So judgement (a) is half right. For about two years none of these can be bought away, which supports pricing power for TSMC, ASML and the memory makers. Beyond about three years every one is being expanded by money, and that expansion becomes excess if demand stalls. Second sources also exist at the margin: Samsung reports 2nm order wins and Intel says it has committed to its 14A process.

### Gaps
- The International Energy Agency's latest data-centre figures, US interconnection-queue statistics and primary transformer lead-time data could not be fetched. Evidence on construction labour is anecdotal.
- TSMC gives no utilisation or packaging capacity numbers; wafer-per-month figures are press reports from unnamed supply-chain sources. ASML's 2025 EUV unit count (44 in one secondary summary) was not verified.

## 4. Size of the equipment and chip markets

### Takeaway
SEMI forecasts wafer-fab-equipment spending of about $144bn in 2026 (+23%), about $175bn in 2027 and about $200bn in 2028; the equipment makers themselves say mid-$150bn in 2026 and above $200bn in 2027. SEMI raised its 2027 figure by about 30% in seven months. Growth is led by DRAM, and China's share of equipment billings fell from about 42% (2024) to 36.5% (2025).

### Cited Findings

**Table 4. SEMI equipment data, US$bn.** [ESTIMATE; "about" values are my calc from stated growth rates]

| | 2024 | 2025 | 2026F | 2027F | 2028F |
|---|---|---|---|---|---|
| Total equipment billings, actual | 117.1 | 135.1 (+15%) | | | |
| Total equipment, forecast of 14 Jul 2026 | | | 165.9 (+23.2%) | not stated | 229.5 |
| Total equipment, forecast of Dec 2025 | | 133 | 145 | 156 | |
| Wafer-fab equipment, Jul 2026 | 104 | 116.9 | 143.9 (+23.1%) | about 175 (+21.8%) | about 200 (+14.1%) |
| Wafer-fab equipment, Dec 2025 | 104 | 115.7 | about 126 (+9.0%) | 135.2 | |
| Foundry and logic, Jul 2026 | | about 65.6 | 78.0 (+18.9%) | about 92 (+18.1%) | 104.7 |
| DRAM, Jul 2026 | | about 27.9 | 38.8 (+39.0%) | about 49 (+27.4%) | 56.9 |
| NAND, Jul 2026 | | about 10.6 | 13.9 (+30.7%) | about 18 (+31.1%) | 20.8 |
| Test / assembly and packaging, Jul 2026 | | | 15.3 / 6.7 | | 20.8 / 8.6 |
| 300mm fab equipment (13 Oct 2026) | | about 114 | 149 (+31%) | double-digit growth | 227 in 2029 |

Sources: SEMI — [2025 billings, 7 Apr 2026](https://www.prnewswire.com/news-releases/semi-reports-global-semiconductor-equipment-billings-reached-135-billion-in-2025-up-15-year-on-year-302735003.html); [mid-year forecast, 14 Jul 2026](https://www.webull.com/news/15226022544172032); [year-end forecast, Dec 2025](https://evertiq.com/news/2025-12-17-semiconductor-equipment-sales-to-reach-a-156-billion-in-2027); [300mm outlook, 13 Oct 2026](https://www.prnewswire.com/news-releases/global-300mm-fab-equipment-spending-to-reach-227-billion-in-2029-as-buildout-accelerates-semi-projects-302906628.html).

- Quarterly billings were $40.53bn in April–June 2026 (+23% year on year), a second straight record [ESTIMATE] — [SEMI, 3 Sep 2026](https://www.prnewswire.com/news-releases/global-semiconductor-equipment-billings-increased-23-year-over-year-in-q2-2026-semi-reports-302869446.html).
- By region, 2025: China $49.3bn (36.5%; −0.5%), Taiwan $31.5bn (+90%), Korea $25.8bn (+26%), North America $10.9bn (−20%), Japan $9.5bn (+22%), Europe $2.9bn (−41%), rest of world $5.2bn; China's 2024 share works out at about 42% [ESTIMATE, shares my calc] — [SEMI, 7 Apr 2026](https://www.prnewswire.com/news-releases/semi-reports-global-semiconductor-equipment-billings-reached-135-billion-in-2025-up-15-year-on-year-302735003.html). SEMI expects China, Taiwan and Korea to stay the top three through 2028, with China first but its growth moderating in 2026 [ESTIMATE] — [mid-year forecast](https://www.webull.com/news/15226022544172032). Americas 300mm equipment spending: $18.1bn in 2026, $40.6bn in 2029 [ESTIMATE] — [300mm outlook](https://www.prnewswire.com/news-releases/global-300mm-fab-equipment-spending-to-reach-227-billion-in-2029-as-buildout-accelerates-semi-projects-302906628.html).
- Equipment makers' own view: Lam (21 Oct 2026) and KLA (28 Oct 2026) both put 2026 wafer-fab equipment in the "mid-$150 billion range" and 2027 above $200bn, led by DRAM, then leading-edge foundry and logic, then NAND; KLA calls its 2030 model of about $220bn "a very conservative one" [COMPANY CLAIM] — [Lam](https://www.marketbeat.com/instant-alerts/transcript-lam-research-q1-earnings-call-highlights-2026-10-21/), [KLA](https://www.webull.com/news/15828153893520384).
- China's share of vendor revenue: Lam 35% in the latest quarter (26% the quarter before; "significantly lower" next quarter); KLA guides 27–29% for October–December and "low 20s" for 2027; Applied Materials 28% in May–July 2026 against 35% a year earlier; ASML 14% of system sales in April–June and about 20% expected for 2026 [COMPANY CLAIM] — [Lam](https://www.marketbeat.com/instant-alerts/transcript-lam-research-q1-earnings-call-highlights-2026-10-21/), [KLA](https://www.webull.com/news/15828153893520384), [Applied analysis](https://sec-api.io/insights/applied-materials-amat-financial-analysis-q3-fy2026-china-revenue-share-export-control-settlement-wafer-equipment-peers-and-scenarios-to-fy2029), [ASML via TrendForce](https://www.trendforce.com/news/2026/08/25/news-u-s-may-push-near-total-asml-china-ban-on-duv-sales-and-servicing-amid-chinas-domestic-lithography-push/).
- Chip market: WSTS (2 Jun 2026) forecasts $1.51tn in 2026 (+89.9%), with memory at $803.9bn (+249.5% from $230.0bn), and about $1.9tn in 2027 (+27%; memory $1.06tn); its autumn forecast is due in December [ESTIMATE] — [WSTS](https://www.wsts.org/76/Recent-News-Release), [summary](https://anysilicon.com/news/global-semiconductor-market-surges-beyond-usd-1-5-trillion-in-2026-driven-by-extraordinary-memory-expansion/). Actual sales were $517.7bn in July–September 2026 (+24.1% on the quarter); September was up 146.8% year on year [ESTIMATE] — [SIA, 3 Nov 2026](https://www.semiconductors.org/global-semiconductor-sales-increase-24-1-from-q2-2026-to-q3-2026/).

**Table 5. Capital spending by chip maker.**

| Company | Latest actual | 2026 plan | Statement on 2027 | Source |
|---|---|---|---|---|
| TSMC | $13.8bn in Jul–Sep 2026 | $60–64bn (raised in July from $52–56bn) | 2026–28 "even more significantly higher than the past three years" | [COMPANY CLAIM] [CNA](https://focustaiwan.tw/business/202610150018), [Newsquawk](https://www.newsquawk.com/headlines/tsmc-tsm2330-tt-q3-guidance-usd-revenue-at-446-458bln-exp-426bln-gross-margin-66-67-exp-659-2026-capex-60-64bln-prev-saw-52-56bln) |
| Samsung Electronics | KRW 57tn in Jan–Sep 2026 (+77%) | about KRW 84.4tn (+60%) | AI-driven demand to "far exceed" industry supply | [COMPANY CLAIM] [Light Reading](https://lightreading.com/finance/memory-boom-carries-samsung-to-another-bumper-quarter) |
| SK hynix | KRW 12.7tn in Jul–Sep 2026 | KRW 48–50tn (plan set in July) | "increase significantly compared to 2026" | [COMPANY CLAIM, summary page] [Finsee](https://finsee.ai/earnings/skhy/2026/q3/en/) |
| Micron | net capex about $27.4bn in the year to 3 Sep 2026, on revenue of $133.2bn [FILING for revenue] | first half of FY2027 about $25bn | FY2027 capex raised "above prior plans", mostly construction | [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000723125/us-gaap/Revenues.json), [Blocks & Files](https://www.blocksandfiles.com/flash/2026/10/01/memory-gold-rush-bonanza-makes-billions-for-micron/5300445); capex figures per sibling note `samsung_skhynix_micron.md`, not re-verified |
| Intel | $14.6bn in 2025; $10.2bn in Jan–Sep 2026 (cash) [FILING] | gross about $20bn | "up strongly" | [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000050863/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json); plan per sibling note `intel_rapidus.md`, not re-verified |
| SMIC | $1.09bn in Jul–Sep 2026 | about flat on 2025's roughly $8.1bn | none found | per sibling note `china_smic_smee_naura_amec.md`, not re-verified |

### Inferences
- The forecasters are chasing the cycle: SEMI's 2027 wafer-fab-equipment figure went from $135bn to about $175bn in seven months, and the vendors are already above it. Revisions of that size happen both at genuine step changes and late in cycles; the data cannot tell which this is.
- Memory is the swing factor. DRAM and NAND are about 37% of 2026 equipment spending but supply most of the growth, and memory is 46% of Lam's and about 40% of KLA's systems revenue. Memory capex has been the most cyclical part of the market (section 5).
- China is a shrinking but still large share, about a quarter to a third of vendor revenue, so export controls stay material and the January 2027 truce date is live (section 6).

### Gaps
- TechInsights and Gartner forecasts were not obtained. SEMI's regional forecast figures and World Fab Forecast detail sit in images or behind a paywall. Tokyo Electron's market view (a $150–170bn a year range for 2026–27 on one aggregator page) could not be verified.
- SEMI's year-end forecast and the WSTS autumn forecast are both due in December 2026.

## 5. Past downturns, for calibration

### Takeaway
In the two deep downturns (2001–03 and 2008–09) equipment makers' revenue fell 37–58% and profits became losses. In the two shallow ones (2019 and 2023) revenue fell 0–15% and ASML grew, yet shares still fell 26–57%. Order backlog cushioned only when leading-edge demand held.

### Cited Findings

**Table 6. Revenue, peak to trough.** [FILING; percentages my calc]

| Company | 2000–03 | 2007–09 | 2018–20 | 2022–24 |
|---|---|---|---|---|
| Applied Materials (FY Oct) | $9.56bn → $4.48bn (FY2000–03): −53%; net income $2.06bn → −$0.15bn | $9.73bn → $5.01bn (FY2007–09): −49%; operating income $2.37bn → −$0.39bn | $16.70bn → $14.61bn: −13%; operating income −25% | no fall ($25.79bn → $26.52bn) |
| Lam Research (FY Jun) | $1.52bn → $0.76bn (FY2001–03): −50% | $2.57bn → $1.12bn (FY2007–09): −57%; net income $0.69bn → −$0.30bn | $11.08bn → $9.65bn: −13% | $17.43bn → $14.91bn (FY2023–24): −14% |
| KLA (FY Jun) | $2.10bn → $1.32bn (FY2001–03): −37% | $2.73bn → $1.52bn (FY2007–09): −44%; net income $0.53bn → −$0.52bn | rose | $10.50bn → $9.81bn: −7% |
| ASML | €2.67bn → €1.59bn (2000–01): −41%; net income €0.38bn → −€0.48bn | €3.77bn → €1.60bn (2007–09): −58% | rose 8% (2019) | rose 30% (2023) |
| TSMC | NT$166.2bn → NT$125.9bn (2001): −24%; net income −78%; utilisation 106% → 51%; capex NT$103.8bn → NT$37.9bn (2000–03) | not re-fetched | not re-fetched | not re-fetched |
| Micron (FY Aug/Sep) | $6.36bn → $2.59bn (FY2000–02): −59% | $5.84bn → $4.80bn (FY2008–09): −18%; operating losses of $1.6–1.7bn in both years | $30.39bn → $21.43bn (FY2018–20): −29%; operating income −80% | $30.76bn → $15.54bn (FY2023): −49%; operating income $9.70bn → −$5.75bn |

Sources: 10-K and 20-F filings — [Applied FY2003](https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm); Lam [FY2003](https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm), [FY2010](https://www.sec.gov/Archives/edgar/data/707549/000119312510194304/d10k.htm); KLA [FY2003](https://www.sec.gov/Archives/edgar/data/319201/000031920103000112/fy2003kla10k.htm), [FY2010](https://www.sec.gov/Archives/edgar/data/319201/000119312510179757/d10k.htm); Micron [FY2003](https://www.sec.gov/Archives/edgar/data/723125/000104746903033422/a2120427z10-k.htm), [FY2010](https://www.sec.gov/Archives/edgar/data/723125/000072312510000174/q4fy2010.htm); [ASML 2003](https://www.sec.gov/Archives/edgar/data/937966/000115697304000133/u47074e20vf.htm); [TSMC 2003](https://www.sec.gov/Archives/edgar/data/1046179/000119312504095792/d20f.htm); later years from SEC XBRL for [Applied](https://data.sec.gov/api/xbrl/companyconcept/CIK0000006951/us-gaap/Revenues.json), [Lam](https://data.sec.gov/api/xbrl/companyconcept/CIK0000707549/us-gaap/Revenues.json), [KLA](https://data.sec.gov/api/xbrl/companyconcept/CIK0000319201/us-gaap/Revenues.json), [ASML](https://data.sec.gov/api/xbrl/companyconcept/CIK0000937966/us-gaap/Revenues.json), [Micron](https://data.sec.gov/api/xbrl/companyconcept/CIK0000723125/us-gaap/Revenues.json).

**Table 7. Largest share-price fall in each episode, %.** [my calc from daily closes; [Yahoo Finance chart data](https://query1.finance.yahoo.com/v8/finance/chart/%5ESOX?period1=757382400&period2=1794700000&interval=1d), same endpoint per ticker]

| | 2000–02 | 2007–08 | 2018 | 2021–22 | 2026 high to November low | 13 Nov 2026 vs high; year to date |
|---|---|---|---|---|---|---|
| Philadelphia Semiconductor Index | −84 | −69 | −26 | −47 | −38 | −31; +43 |
| ASML (New York) | −90 | −66 | −34 | −57 | −32 | −25; +40 |
| Applied Materials | −82 | −65 | −53 | −55 | −56 | −49; +44 |
| Lam Research | −88 | −75 | −46 | −57 | −57 | −48; +32 |
| KLA | −73 | −76 | −34 | −41 | −57 | −50; +25 |
| Tokyo Electron | −80 | −75 | −49 | −49 | −48 | −40; +38 |
| TSMC (ADR) | −85 | −51 | −26 | −57 | −27 | −18; +31 |
| Micron | −93 | −88 | −54 | −50 | −46 | −36; +173 |
| SK hynix | not meaningful | −85 | −40 | −44 | −61 | −58; +87 |
| Samsung Electronics | −65 | −47 | −29 | −37 | −48 | −43; +72 |

Index dates: 10 Mar 2000 to 9 Oct 2002; 17 Jul 2007 to 20 Nov 2008; 12 Mar to 24 Dec 2018; 27 Dec 2021 to 14 Oct 2022; 22 Jun to 5 Nov 2026.

**Backlog as a cushion.**
- Applied Materials' backlog was $4.38bn at the end of fiscal 2000 (46% of that year's sales) and $2.73bn a year later; in fiscal 2003 "backlog adjustments ... totaled $553 million, which consisted of cancellations, currency and other adjustments" [FILING] — [10-K](https://www.sec.gov/Archives/edgar/data/6951/000089161804000093/f95058e10vk.htm).
- ASML's backlog fell from 365 systems (end-2000) to 118 (end-2001) and systems sold from 455 to 197 [FILING] — [20-F](https://www.sec.gov/Archives/edgar/data/937966/000115697304000133/u47074e20vf.htm). Lam: orders "are subject to cancellation by our customers with limited penalties" [FILING] — [10-K](https://www.sec.gov/Archives/edgar/data/707549/000089161803004913/f93126e10vk.htm).
- Today: Applied's backlog was $15.0bn at 26 Oct 2025 [FILING, via an [analysis](https://sec-api.io/insights/applied-materials-amat-financial-analysis-q3-fy2026-china-revenue-share-export-control-settlement-wafer-equipment-peers-and-scenarios-to-fy2029)]; SK hynix's long-term agreements fix volume within "a range agreed with customers, not fixed prices" [COMPANY CLAIM, summary page] — [Finsee](https://finsee.ai/earnings/skhy/2026/q3/en/); Micron's are "take or pay" [COMPANY CLAIM] — [Blocks & Files](https://www.blocksandfiles.com/flash/2026/10/01/memory-gold-rush-bonanza-makes-billions-for-micron/5300445).

### Inferences
- A shallow pause on the 2019 or 2023 pattern would mean equipment revenue down 10–15% and memory revenue down 30–50%. A deep one on the 2001 or 2009 pattern would mean equipment down 40–55% and losses.
- The shallow cases may understate the risk to ASML and TSMC. In 2019 and 2023 the leading edge was the stable part of demand; an AI-led pause would start at the leading edge.
- Equipment shares fell as far in 2026 as in 2022 (56–57% at the low), before any fall in revenue. A shallow pause is arguably priced; a deep one (falls of 65–90% in 2000–02 and 2007–08) is not.
- Memory contracts now protect volumes better than in past cycles, but not prices.

### Gaps
- SEMI's industry totals for 2001, 2009, 2019 and 2023, and the downturn-year results of TSMC (after 2001), Tokyo Electron, Samsung and SK hynix, were not re-fetched.

## 6. Policy and geopolitics as of November 2026

### Takeaway
The measures that matter most are narrow or suspended, and the dates cluster: the US–China truce, the US affiliates rule and China's rare-earth controls all run to 10 January 2027. The only US chip tariff in force covers a narrow class of AI chips and exempts US data centres; I found no proclamation of the broader "phase two" tariff.

### Cited Findings

**US tariffs and country terms.**
- Proclamation 11002, signed 14 January 2026 and effective 12:01 a.m. EST on 15 January: a 25% duty on "certain advanced computing chips" and derivative products, exempt when imported for US data centres, repairs, research, startups, non-data-centre consumer and civil industrial uses, the public sector, or other uses the Commerce Secretary approves. Chip-making equipment is not tariffed. The President "may consider imposing significant tariffs on imports of semiconductors" with "an accompanying tariff offset program". Commerce found the US "fully manufactures only approximately 10 percent of the chips it requires". Reports were due at 90 days and by 1 July 2026 [FILING] — [proclamation text](https://www.govinfo.gov/content/pkg/CDOC-119hdoc136/html/CDOC-119hdoc136.htm). A customs-compliance page updated 11 October 2026 still lists phase two as "pending" [PRESS] — [GingerControl](https://gingercontrol.com/blog/section-232-semiconductor-tariff).
- Taiwan: the Agreement on Reciprocal Trade, signed 12 February 2026, caps US tariffs at 15% and gives chips "most-favorable-treatment under Section 232"; Taiwan refused a US goal of moving 40% of chip output ("that's impossible"); the text went to the legislature for approval [PRESS, named officials] — [Taipei Times, 14 Feb 2026](https://www.taipeitimes.com/News/front/archives/2026/02/14/2003852298). Under the January terms, firms building US capacity may import up to 2.5 times planned capacity free of Section 232 duty during construction and 1.5 times their US capacity afterwards, with at least $250bn of investment and $250bn of credit guarantees pledged [FILING, Commerce fact sheet as relayed by a law firm] — [Thompson Hine, 16 Jan 2026](https://www.thompsonhinesmartrade.com/2026/01/u-s-and-taiwan-sign-agreement-on-trade-investment/).
- Korea: for chips and chip-making equipment, terms "no less favorable than terms that may be offered in a future agreement" of comparable trade volume (13 Nov 2025) [FILING] — [White House](https://www.whitehouse.gov/fact-sheets/2025/11/joint-fact-sheet-on-president-donald-j-trumps-meeting-with-president-lee-jae-myung/). EU: combined tariff on chips "does not exceed 15 percent"; the EU "intends to purchase at least $40 billion worth of U.S. AI chips" (21 Aug 2025) [FILING] — [White House](https://www.whitehouse.gov/briefings-statements/2025/08/joint-statement-on-a-united-states-european-union-framework-on-an-agreement-on-reciprocal-fair-and-balanced-trade/). Japan: the implementing order of 4 September 2025 does not mention semiconductors [FILING] — [White House](https://www.whitehouse.gov/presidential-actions/2025/09/implementing-the-united-states-japan-agreement/).
- CHIPS Act: the government took 9.9% of Intel at $20.47 a share, paid with $11.1bn of grants (August 2025); the manufacturing tax credit was raised by 10 points; in May 2026 nine quantum firms received $2bn of grants in return for equity stakes [PRESS, encyclopaedia summary] — [Wikipedia](https://en.wikipedia.org/wiki/CHIPS_and_Science_Act).

**US export controls.**
- AI chips to China: from 15 January 2026, case-by-case licence review for chips below 21,000 total processing performance and 6,500 GB/s memory bandwidth (Nvidia H200, AMD MI325X), subject to US third-party testing and supply certifications [FILING] — [BIS](https://bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china), [Covington](https://www.cov.com/-/media/files/corporate/publications/2026/04/us-commerce-department-revises-license-review-policy-for-exports-of-certain-advanced-computing-commodities-to-china-and-macau.pdf). Nvidia's August guidance still assumed no China data-centre revenue [COMPANY CLAIM] — [SentiSense](https://app.sentisense.ai/stories/nvidia-beats-across-the-board-guides-108-billion-with-zero-china-revenue-assume-08262026).
- Affiliates (50%) rule: issued 30 September 2025 (90 FR 47201), stayed 10 November 2025, and "further stayed until January 10, 2027" by a rule effective 9 November 2026 (91 FR 70789) [FILING] — [Federal Register](https://www.federalregister.gov/documents/2026/11/09/2026-22793/extension-of-the-suspension-of-expansion-of-end-user-controls-for-affiliates-of-certain-listed).
- MATCH Act: would give allies 150 days to match US controls, failing which the US could bar ASML from selling or servicing immersion DUV tools at SMIC, Huawei, Hua Hong, CXMT and YMTC. It rode on the defence bill, which failed to advance on 14 July 2026; the Dutch government rejects policy "dictated by unilateral US legislation" [PRESS] — [Bits&Chips, 21 Aug 2026](https://bits-chips.com/article/iran-war-deadlock-gave-asml-reprieve-from-us-china-crackdown/).

**US–China truce and China's measures.**
- The October 2025 Busan truce was extended by two months to 10 January 2027, announced on 23 September 2026 during Xi's state visit to Washington; the US Trade Representative said national-security export controls were "off the table"; no longer-term deal was reached [PRESS, named officials] — [China Briefing, 29 Sep 2026](https://www.china-briefing.com/news/xi-trump-meeting-washington-takeaways/).
- China's notices of 9 November 2026: the 24% additional tariff stays suspended (10% remains); export-control waivers for critical minerals, measures against 11 US firms on the unreliable-entity list and 16 on the export-control list, and special port fees are suspended to 10 January 2027; a third Xi–Trump meeting of the year was expected at the APEC summit in China the following week [PRESS] — [Reuters via TimesLIVE](https://www.timeslive.co.za/news/world/2026-11-09-china-extends-us-trade-truce-by-two-months/).
- Chinese actions in 2026: ten US entities, including MP Materials, added to the export-control list in June; procurement curbs on 46 US firms; a public reporting channel for mineral-export violations from 1 July [FILING, Chinese ministry notices as relayed by a law firm] — [Morgan Lewis](https://www.morganlewis.com/pubs/2026/07/recent-china-export-control-actions-signal-active-enforcement-for-rare-earths-and-strategic-minerals). A state-backed group targets about 5 home-made immersion DUV tools in 2026 and about 20 in 2027; China imported 95 DUV systems in 2025 [PRESS] — [TrendForce, 25 Aug 2026](https://www.trendforce.com/news/2026/08/25/news-u-s-may-push-near-total-asml-china-ban-on-duv-sales-and-servicing-amid-chinas-domestic-lithography-push/).

**Taiwan.**
- On 13–14 November 2026 Taiwan's defence ministry counted 10 PLA aircraft sorties (4 inside its air-defence zone), 8 navy vessels and 3 official ships [FILING] — [MND](https://www.mnd.gov.tw/en/News/PLAAct/88212). On 12 November a China Coast Guard ship declared a "law enforcement patrol" about 40 nautical miles south-east of Orchid Island [PRESS] — [CNA](https://focustaiwan.tw/politics/202611140008). Xi said unification "must and will be achieved" [PRESS] — [CNA](https://focustaiwan.tw/politics/202611120026).
- Electricity: the last reactor shut on 17 May 2025 and a restart referendum failed on 23 August 2025; Taipower applied to restart Maanshan on 27 March 2026, the regulator approved a preliminary plan on 24 September 2026, and the minister targets 2028 [PRESS, encyclopaedia summary] — [Wikipedia](https://en.wikipedia.org/wiki/Maanshan_Nuclear_Power_Plant). TSMC: "power supply situation is one of the consideration factors" in capacity planning [COMPANY CLAIM] — [call](https://www.webull.com/news/15751044230423552).
- Capital Economics: a fall in AI capital spending could cut Taiwan's real GDP growth next year by about 3 points and Korea's by about 1 [ESTIMATE] — [Fortune](https://fortune.com/2026/11/08/stock-market-outlook-sp500-ai-capex-gdp-growth-productivity/).

### Inferences
- Tariff exposure for leading-edge makers is low today because of the exemptions and the country caps. The open risk is phase two, which would reach chips, equipment and derivative products, with an offset favouring firms that build in the US.
- 10 January 2027 is the date to watch. A lapse would bring back the affiliates rule, which reaches Chinese buyers of tools and design software, and China's rare-earth regime, which reaches tool makers' inputs.
- Three leader-level meetings in 2026 argue against a near-term crisis, but they also make export controls a bargaining item in either direction. The Taiwan Strait evidence gathered here is too thin to move a prior.

### Gaps
- Not found: any phase-two tariff action after 1 July 2026; ratification of the Taiwan agreement; Dutch or Japanese control changes in 2026; counts of 2026 exercises around Taiwan, official invasion or blockade assessments, insurance or market-implied measures; Taiwan's reserve margin.

## 7. Sector pricing and positioning

### Takeaway
The Philadelphia Semiconductor Index peaked at 14,634.72 on 22 June 2026, fell 38% to 9,011.14 on 5 November and closed at 10,146.32 on 13 November: 31% below the high and 43% up on the year. Applied Materials, Lam and KLA are 48–50% below their highs, Tokyo Electron 40% and ASML 25%. Positioning was one-sided in July and still overweight in October.

### Cited Findings
- Index levels and per-stock moves: Table 7 [my calc from exchange closes]. The 5 November close was 12.25% down on the day, the largest fall since 16 March 2020 [CONFIRMED by exchange data] — [24/7 Wall St](https://247wallst.com/investing/2026/11/06/chip-stocks-just-had-their-second-worst-day-on-record/).
- Valuation: the iShares Semiconductor ETF showed a price/earnings ratio of 39.31 and price/book of 9.00 on 12 November 2026, with $41.2bn of assets [FILING, fund sponsor data] — [iShares](https://www.ishares.com/us/products/239705/ishares-semiconductor-etf).
- Positioning: in July 2026, 82% of fund managers called long semiconductors the most crowded trade and none reported being short; chip funds took a record $10bn of net inflows in January–May (Morningstar) [ESTIMATE] — [Reuters via Express Tribune](https://tribune.com.pk/story/2618784/among-ai-crowd-some-investors-position-for-slower-hyperscaler-spending-growth). In October, 45% still named semiconductors, the net technology overweight of 37% was the highest since August 2020, and cash was 3.9% [ESTIMATE] — [Crypto Briefing](https://cryptobriefing.com/bofa-survey-fund-managers-overweight-tech/). Nomura attributed the 5 November fall partly to hedge funds selling the year's winners [PRESS] — [24/7 Wall St](https://247wallst.com/investing/2026/11/06/chip-stocks-just-had-their-second-worst-day-on-record/).
- Dated tests ahead: Nvidia results on 17 November; SEMI and WSTS forecasts in December; the 10 January 2027 truce date; the large buyers' 2027 capex figures in late January and early February 2027.

### Inferences
- Prices have moved from euphoria to discounting a shallow pause in equipment and memory, while the index is held up by its largest members. A trailing multiple near 39 on earnings inflated by memory margins of 80% is not a cushion: cyclical multiples look lowest at peak earnings.

### Gaps
- Forward earnings multiples for the index and the equipment group against their own history, short interest and fund flows after May 2026 were not obtained. A sibling note (`market_data_snapshot.md`) is compiling per-company multiples.

## 8. What I could not verify, and figures on which sources conflict

### Takeaway
The filed figures (capex, cash flow, debt, revenue histories, the Federal Register stay) are solid. The weakest material is press-relayed: lab financials, bank forecasts seen only in summaries, capacity counts from unnamed supply-chain sources, and almost everything on Taiwan Strait risk. Where a filing and a press figure disagree I have used the filing. Where only press figures exist, treat magnitudes as indicative and directions as more reliable. A second pass with search access should close items 1, 3, 8, 9 and 10 of the first list before any conclusion leans on them.

### Could not verify
1. Whether a phase-two Section 232 action on chips or equipment was proclaimed after 1 July 2026; ratification and entry into force of the Taiwan–US agreement.
2. Reports that Chinese customs blocked H200 imports, that Samsung and SK hynix hold annual 2026 licences for their China fabs, and the detail of the February 2026 Supreme Court tariff ruling: seen in search summaries only.
3. Polymarket odds (secondary page blocked); the UBS, Goldman and Jefferies notes (press relays only); JPMorgan ($5.5tn through 2030) and Bank of America ($800bn in 2026, $1tn in 2027) forecasts (search summaries only).
4. OpenAI's revenue and burn in dollars; Anthropic's financials (prospectus not read).
5. Microsoft's October call details and Oracle's total debt (secondary write-ups).
6. Industry equipment totals in past downturns. From memory, not re-fetched: about −59% (2000–02), −63% (2007–09), −7% (2019), −1% (2023).
7. Tokyo Electron's market forecast; ASML's 2025 EUV unit count; wafer-per-month capacity figures for TSMC.
8. Dutch and Japanese export-control changes in 2026; the MATCH Act's status after July 2026.
9. Taiwan Strait exercise counts, official risk assessments, insurance or market measures; Taiwan's reserve margin.
10. International Energy Agency data, interconnection-queue statistics and transformer lead times from primary sources.
11. The iShares page shows 39.31 for both the price/earnings ratio and another field, so the figure may be a display error.

### Conflicting figures
1. Microsoft calendar-2026 capex: $190bn (before a July accounting change), $175bn (July), about $170bn (October).
2. Amazon's quarterly capex: $75.9bn "cash capex" (call) against $77.3bn purchases of property and equipment (filing). Meta 2025: $69.7bn (filing line) against $72.2bn including finance leases.
3. Anthropic's commitments: $417bn, $518bn or up to $800bn depending on the outlet; xAI/SpaceX capacity $84.5bn or $120.5bn; public filing dated 29 September or 26 October 2026.
4. OpenAI's November round: target $30bn at $1.4tn (press) or $1.5tn (investors), neither confirmed by the company. March round: $110bn at $730bn pre-money or $122bn at $852bn post-money.
5. Goldman's 2028 figure: $1.4tn or $2tn; 2027 growth 50% or 54%. Morgan Stanley's $600bn: one year's cash burn (2027) or a cumulative shortfall through 2028.
6. Wafer-fab equipment: SEMI $143.9bn (2026) and about $175bn (2027) against the vendors' mid-$150bn and above $200bn. SEMI's July release implies 2025 DRAM and NAND equipment of about $27.9bn and $10.6bn against $22.5bn and $14.0bn in its December 2025 release.
7. CoWoS capacity in 2026: about 106,000 wafers a month (Goldman, annual average), over 130,000 (Commercial Times), or 120,000–140,000 at TSMC plus 50,000–60,000 at subcontractors.
8. CoreWeave's 2026 capex guidance: $37–39bn or $31–35bn.
9. US data-centre capacity at risk from moratoriums: about 30% of 2028 additions (UBS), 20% of 2028 projects or about 5 GW (Morgan Stanley), 5.7–30 GW (SemiAnalysis), about 45% of planned capacity (Goldman, one secondary report).
10. ASML: EUV growth "over 45%" (sales) or "more than 50%" (units); China 14% of system sales (April–June), about 20% (full-year guide), 23% (July–September, per a sibling note).
11. The 5 November index fall: 12.25% at the close against "about 9%" and 8.27% in intraday reports.
12. SK hynix shareholder returns: KRW 60tn additional or about KRW 100tn in total. Micron fiscal-2026 capex: $27.4bn net or $30.7bn gross. Taiwan's pledges: "at least" $250bn each (Commerce, via a law firm) or "up to" $250bn of guarantees (Taipei Times).

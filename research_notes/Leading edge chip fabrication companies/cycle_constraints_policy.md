# Demand cycle, physical bottlenecks and trade-policy backdrop for leading-edge chip manufacturing (as of 14 November 2026)

**Purpose.** Test two earlier judgements: (a) leading-edge fabrication and lithography are constraints AI demand cannot remove; (b) roughly a one-in-four chance of a pause in AI spending around 2028.

**Tag key.** [FILING] filed or audited figure (also used for official government documents: Federal Register, proclamations, ministry notices); [COMPANY CLAIM] company statement no outside party has confirmed; [CONFIRMED] company statement confirmed by a named outside party; [ESTIMATE] third-party estimate, forecast or industry statistic; [PRESS] press report resting on unnamed sources or not traced to a primary document. "My calc" marks my arithmetic on cited figures.

**Method limits.** The shared web-search budget for this session ran out about a third of the way through. Everything after that came from direct fetches of known pages, SEC XBRL data (data.sec.gov), SEC filings and exchange price data. Topics I could not reach that way are listed in section 8. Quarter-end figures are for July–September 2026 unless stated.

**Reading in one paragraph (mine; facts follow).** Suppliers and buyers both say supply, not demand, limits AI computing through 2027–28, and the tightest items by their own statements are memory and powered data-centre space, with EUV tools and leading-edge wafers joining the list for 2027–28. All of these are being expanded with money on a two-to-four-year lag, so "cannot remove" holds for about two years and weakens after that. The spending behind this now runs at roughly 100% of the four largest buyers' operating cash flow and is funded at the margin by about $370bn of bonds in 2026; mainstream forecasters already pencil in a flat-to-down 2028. I read the chance of an outright fall in aggregate spending around 2028 as similar to or somewhat above one in four (about 30%, range 20–40%), and the chance of a growth stall that suppliers would feel as about one in two. Equipment shares have already fallen 48–57% from their June 2026 highs with no fall in revenue.

## 1. AI capital spending: actuals, guidance, financing, returns, strain, forecasts

### Takeaway
The five largest US buyers spent about $412bn in 2025 and about $560bn in January–September 2026 (+100% year on year), an annualised rate of about $920bn in the latest quarter; all five say 2027 will be higher and none has given a number. Capital spending by the four largest rose from 65% of operating cash flow in 2025 to about 100% in January–September 2026, with the gap funded by record bond issuance, leases and customer prepayments.

### Cited Findings

**Table 1. Cash purchases of property and equipment, US$bn (excludes finance leases unless stated).** [FILING: SEC XBRL, 10-K/10-Q data; sums, growth rates and ratios are my calc]

| Company | Calendar 2025 | Jan–Sep 2026 (y/y) | Latest quarter | Capex ÷ operating cash flow | 2026 guidance [COMPANY CLAIM] | 2027 statement [COMPANY CLAIM] | Long-term debt, end-2024 → end-2025 → 30 Sep 2026 |
|---|---|---|---|---|---|---|---|
| Microsoft | 83.1 (FY to Jun 2025: 64.6; FY to Jun 2026: 115.9) | 106.1 (+99%) | 39.4; 45.2 incl. finance leases | 68%; 78% incl. leases | Calendar 2026 about 170–175 incl. finance leases; Oct–Dec above 50 | Free cash flow positive through FY2027; no number | 45.0 → 40.3 → 35.5 |
| Alphabet | 91.5 | 132.0 (+107%) | 51.4 | 104% (9M); 121% (Q3) | 195–205 (raised in July from 180–190) | "increase significantly"; detail in January | 10.9 → 46.6 → 125.1 |
| Amazon | 131.8 | 175.7 (+90%) | 77.3 gross; 75.9 "cash capex" | 154% (9M) | about 220 | "meaningfully more" | 58.0 → 68.8 → 180.9 |
| Meta | 69.7 (72.2 incl. finance leases) | 83.1 (+72%) | 34.9 incl. finance leases | 86% (9M); above 100% (Q3) | 135–145 | budget not set; "upward pressure" | 28.8 → 58.7 → 80.9 |
| Oracle | 35.5 (Dec 2024–Nov 2025); FY to May 2026: 55.7 | 63.6 (Dec 2025–Aug 2026; +171%) | 28.5 (Jun–Aug) | 174% (FY to May 2026); 123% (Jun–Aug) | FY to May 2027: 90–95 gross, at most 70 net of prepayments | none | about 125 total debt [PRESS] |
| **Five** | **about 412** | **about 560 (+100%)** | **231 (about 920 annualised)** | four largest: 65% (2025) → 100% (Jan–Sep 2026) | about 810–840 (mixed year bases) | | |

Sources: SEC XBRL for [Microsoft](https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json), [Alphabet](https://data.sec.gov/api/xbrl/companyconcept/CIK0001652044/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json), [Amazon](https://data.sec.gov/api/xbrl/companyconcept/CIK0001018724/us-gaap/PaymentsToAcquireProductiveAssets.json), [Meta](https://data.sec.gov/api/xbrl/companyconcept/CIK0001326801/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json), [Oracle](https://data.sec.gov/api/xbrl/companyconcept/CIK0001341439/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json) (operating cash flow and debt from the same API, tags `NetCashProvidedByUsedInOperatingActivities`, `LongTermDebt`); guidance from the [Alphabet call, 28 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/), [Amazon call, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/), [Meta call highlights, 21 Oct 2026](https://www.marketbeat.com/instant-alerts/transcript-meta-platforms-q3-earnings-call-highlights-2026-10-21/), [Oracle call highlights, 10 Sep 2026](https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/?.tsrc=rss), [Microsoft coverage, 28–30 Oct 2026](https://www.pymnts.com/earnings/2026/microsoft-extends-data-center-lifespans-to-soften-ai-buildout-costs/).

- Microsoft spent $45.2bn including finance leases, below the "over $50bn" it guided in July, "as some third-party capacity deliveries we expected in Q1 were delayed"; about 75% went on short-lived assets; some supply "move[d] out into H2" [COMPANY CLAIM] — [PYMNTS](https://www.pymnts.com/earnings/2026/microsoft-extends-data-center-lifespans-to-soften-ai-buildout-costs/), [24/7 Wall St](https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb). From July 2026 it lengthened building lives from 15 to 25 years and restated calendar-2026 capex to about $175bn from $190bn [COMPANY CLAIM] — [CFO Dive](https://www.cfodive.com/news/microsoft-holds-line-ai-spending-plans/826648/).
- Alphabet: free cash flow −$9.1bn in the quarter; purchase commitments $924bn plus $152bn of leases not yet started; it began "utilizing third-party compute capacity at the end of Q3" "given the supply constrained environment" [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/).
- Amazon: "We can fund this plan"; AWS "can grow north of 40% in each of 2027 and in 2028"; "There's only so many chips that provider can provide each year" [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/). Trailing twelve-month free cash flow −$42.4bn [PRESS on a company figure] — [Constellation Research](https://www.constellationr.com/insights/news/aws-q3-revenue-growth-surges-39-capex-stings-amazons-cash-flow).
- Meta's unconditional purchase obligations rose from $58.1bn (30 Sep 2025) to $355.7bn (30 Sep 2026) [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001326801/us-gaap/UnrecordedUnconditionalPurchaseObligationBalanceSheetAmount.json).
- Oracle: remaining performance obligations $664bn; most new contracts came "through customer prepayments or bring-your-own-hardware deals" that "will not impact our CapEx or revenues until fiscal 28 or beyond"; a $20bn at-the-market share sale was completed in the quarter [COMPANY CLAIM] — [call highlights](https://www.marketbeat.com/instant-alerts/transcript-oracle-q1-earnings-call-highlights-2026-09-10/?.tsrc=rss).

**Other buyers.**
- CoreWeave: purchases of property and equipment $23.6bn in January–September 2026; debt $47.5bn and contracted backlog $132.3bn at 30 Sep 2026 [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001769628/us-gaap/PaymentsToAcquirePropertyPlantAndEquipment.json). Customer commitments: OpenAI about $22.4bn, Meta about $35bn [PRESS] — [investingLive, 10 Nov 2026](https://investinglive.com/stocks/coreweave-q3-beats-on-seven-key-metrics-lifts-full-year-revenue-and-run-rate-guidance/).
- OpenAI: $122bn raised at $852bn post-money (March 2026); cumulative cash outflow to 2030 put at $665bn [PRESS] — [The Decoder, 27 Feb 2026](https://the-decoder.com/openais-up-to-110-billion-raise-lines-up-almost-exactly-with-the-111-billion-it-just-added-to-its-cash-burn-forecast/). On 6 November 2026 a first close of about $11bn arrived against a press-reported target of $30bn or more [PRESS]; the $1.25tn pre-money valuation was confirmed by the CFO, who said the business grew 70% quarter on quarter and gave no revenue figure [COMPANY CLAIM] — [24/7 Wall St, 7 Nov 2026](https://247wallst.com/investing/2026/11/07/openai-just-raised-11-billion-at-a-1-25-trillion-valuation).
- Anthropic (prospectus, as relayed by Reuters): about $518bn of compute and infrastructure obligations over a decade — Google $111.1bn, Amazon $110bn, Microsoft $31.4bn, Broadcom equipment leases $161.2bn, xAI/SpaceX-hosted Nvidia capacity up to $84.5bn through 2029; about 80% non-cancellable [PRESS] — [TechTarget, 29 Sep 2026](https://www.techtarget.com/it-infrastructure/news/366651336/Report-Anthropic-locks-in-518B-AI-infrastructure-commitments). The earlier report in this repository records nine-month 2026 revenue of $33.2bn (see `reports/Automated security quality and entry points.md`).
- Nvidia: revenue $215.9bn in the year to January 2026 and $177.8bn in the following six months; long-term debt rose from $8.5bn to $33.4bn by 26 Jul 2026 [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001045810/us-gaap/LongTermDebt.json). It holds stakes in customers it supplies and cites about $366bn of multi-year infrastructure commitments [PRESS] — [Trending Topics, 27 Aug 2026](https://www.trendingtopics.eu/nvidia-posts-another-blockbuster-quarter-but-debt-is-rising-in-ai-frenzy/).
- Sovereign programmes: the EU opened bids for seven AI "gigafactories" on 30 July 2026 (about $11.4bn of public money; bids closed 12 November 2026) [PRESS] — [AP](https://abcnews.com/Technology/wireStory/eu-lays-114-billion-7-ai-gigafactories-aims-135218478).

**Financing.**
- US investment-grade bond sales reached a record $1.88tn in the year to 4 November (LSEG); Amazon, Alphabet, Meta, Microsoft and Oracle issued more than $370.7bn, about a fifth; Oracle's five-year credit default swap hit a record 325.45 basis points "last month" [ESTIMATE/PRESS] — [Finimize, undated; year inferred as 2026 from the filed debt figures above](https://finimize.com/content/big-techs-ai-bond-binge-pushed-us-issuance-to-a-record).
- Bond cover ratios fell from nearly 5 times in February to below 2 times in July 2026 (Apollo); the Bank for International Settlements warned in June that disappointing AI returns "could trigger a sudden financing pullback" [ESTIMATE] — [Reuters via Express Tribune, 17 Jul 2026](https://tribune.com.pk/story/2618784/among-ai-crowd-some-investors-position-for-slower-hyperscaler-spending-growth).
- Morgan Stanley expects hyperscalers and specialised clouds to burn close to $600bn of cash in 2027 [ESTIMATE] — [Crypto Briefing](https://cryptobriefing.com/morgan-stanley-hyperscaler-cash-burn-2027/). Goldman's forecast implies about $400bn of investment-grade issuance in 2027 [ESTIMATE] — [PYMNTS](https://www.pymnts.com/?p=4233514).

**Revenue and returns.**
- Google Cloud revenue $30.7bn (+103%), operating margin 36.2%, backlog $561bn; "tens of billions of dollars in AI revenues year-to-date" [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/). AWS revenue $46.0bn (+39.3%), margin 38.7%, backlog $578bn [COMPANY CLAIM] — [call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/). Microsoft's remaining performance obligations were $683bn at 30 Sep 2026 [FILING] — [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000789019/us-gaap/RevenueRemainingPerformanceObligation.json); Azure grew 48% [COMPANY CLAIM] — [24/7 Wall St](https://247wallst.com/cards/microsoft-q1-2027-earnings-msft-01m6223bcjxyqzvby9cw8yzzqb).
- Capital Economics calculates that external AI revenue must grow about tenfold by 2030 to justify the spending [ESTIMATE] — [Fortune, 8 Nov 2026](https://fortune.com/2026/11/08/stock-market-outlook-sp500-ai-capex-gdp-growth-productivity/).

**Signs of strain as of mid-November 2026.**
- After Democratic wins in the 3 November midterms raised fears of data-centre moratoriums, the Philadelphia Semiconductor Index fell 12.25% on 5 November, its second-largest one-day fall on record [CONFIRMED by exchange prices] — [24/7 Wall St, 6 Nov 2026](https://247wallst.com/investing/2026/11/06/chip-stocks-just-had-their-second-worst-day-on-record/).
- Morgan Stanley (8–9 November): 20% of US data-centre projects planned for 2028 (about 5 GW) may slip to 2029; US capacity additions −4% in 2028 then +38% in 2029; a shortage of powered capacity above 30% persists through 2028; parts of the supply chain could see "a traditional downcycle in 2028" [ESTIMATE] — [investingLive, 9 Nov 2026](https://investinglive.com/stocks/morgan-stanley-says-buy-the-ai-dip-sees-3-4-trillion-in-hyperscaler-spending-through-2028/). UBS puts about 30% of expected 2028 US capacity at risk [ESTIMATE, bank note not seen] — [Finimize](https://finimize.com/content/ubs-flags-a-post-midterms-speed-bump-for-data-centers).
- Texas froze air permits for data centres from 21 September 2026; New York has a one-year moratorium; more than 300 local moratoriums or bans are in force, though only about 2.3 GW was "genuinely delayed" as of September [ESTIMATE] — SemiAnalysis, [1 Nov 2026](https://newsletter.semianalysis.com/p/the-datacenter-backlash-goes-bipartisan) and [15 Sep 2026](https://newsletter.semianalysis.com/p/everyone-says-datacenter-moratoriums).
- TSMC: "we are being prudent in our business planning going into 2027", citing consumer markets squeezed by "rising component prices" [COMPANY CLAIM] — [The Next Web, 17 Oct 2026](https://thenextweb.com/news/tsmc-q3-2026-record-profit-prudent-2027). Notebook shipments fell 15.8% quarter on quarter and PC makers are trimming 2027 memory orders as inventories build [ESTIMATE] — [TrendForce, 11 Nov 2026](https://www.trendforce.com/presscenter/news/20261111-13303.html).

**Published forecasts.**

| Source (date) | Scope | 2026 | 2027 | 2028 and after |
|---|---|---|---|---|
| Goldman Sachs (Sep 2026) [ESTIMATE] | five largest US buyers | | $1.2tn (+54%); upside $1.4tn | $7.6tn cumulative 2026–31 |
| Morgan Stanley (8 Nov 2026) [ESTIMATE] | hyperscalers plus AI clouds | | $1.6tn | $1.8tn, "some downside risk" |
| UBS (Jul 2026) [ESTIMATE] | hyperscalers | $673bn (+76%) | +25% | +6% |
| Capital Economics (6 Nov 2026) [ESTIMATE] | AI investment | about $800bn | rising, more slowly | falls about 10% in 2028 |
| Jefferies (2026) [PRESS, note not seen] | large buyers | | may fall short of $1.04tn consensus | "may have peaked" |
| Apollo (6 Aug 2026) [ESTIMATE] | hyperscaler capex, % of US GDP | 1.4% in 2025 | 3.1% | about 3% a year 2027–29 |

Sources: [Goldman via PYMNTS](https://www.pymnts.com/?p=4233514); [Morgan Stanley via investingLive](https://investinglive.com/stocks/morgan-stanley-says-buy-the-ai-dip-sees-3-4-trillion-in-hyperscaler-spending-through-2028/); [UBS via Reuters](https://tribune.com.pk/story/2618784/among-ai-crowd-some-investors-position-for-slower-hyperscaler-spending-growth); [Capital Economics via Fortune](https://fortune.com/2026/11/08/stock-market-outlook-sp500-ai-capex-gdp-growth-productivity/); [Jefferies via FourWeekMBA](https://fourweekmba.com/ai-jefferies-google-meta-peers-202b-capex-may-have-peaked/); [Apollo](https://www.apollo.com/wealth/insights-news/insights/daily-spark/the-ai-capex-boom-is-building-twice-as-fast-as-the-housing-boom).

### Inferences
- Demand evidence and financing evidence point in opposite directions. Cloud revenue is accelerating and backlogs total about $2.6tn across Microsoft, Alphabet, Amazon, Oracle and CoreWeave, but those backlogs overlap: a large part is the same commitments by two loss-making labs (Anthropic's roughly $518bn; OpenAI's several hundred billion), whose ability to pay depends on capital markets.
- Self-funding has ended for three of the five: Alphabet, Amazon and Meta added about $213bn of long-term debt in nine months (my calc from Table 1). Microsoft is the exception.
- The first visible shortfall against guidance (Microsoft) was caused by late delivery of capacity, not by weak demand. A deployment bottleneck defers chip purchases just as a financing pause would.

### Gaps
- xAI: no primary figures found. Sovereign programmes in the Gulf, Japan, Korea and India: only unsourced secondary figures found, so not cited.
- Microsoft's exact calendar-2026 figure (sources give $170bn, $175bn and $190bn) and Oracle's total debt need the call transcript and 10-Q.
- Off-balance-sheet financing totals for 2026 (joint ventures, private credit) not obtained; the roughly $65bn figure found dates from 2025.

## 2. The probability of a pause around 2028

### Takeaway
The one-in-four figure was never derived: it entered the earlier work as a stated prior. Independent evidence supports a similar or somewhat higher number for an outright fall in spending around 2028, and about one in two for a growth stall; confidence is low because every source defines "pause" differently.

### Cited Findings

**How the figure arose.**
- The research prompts state: "Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%)", under "Treat the probabilities below as priors" — `prompts/Company research prompts.md`, line 38. Both reports apply the weights to companies without a calculation; the security report says "The scenario readings are the research team's judgements" — `reports/Automated security quality and entry points.md`, line 152. The supporting note lists credit-market indicators and 2027 guidance from Alphabet, Amazon and Oracle as "not obtained" — `research_notes/Verification and specification company ranking/sector_valuation_cycle.md`, section 5.

**Base rates.**

| Cycle | What happened | Source |
|---|---|---|
| Combined capex of Microsoft, Alphabet, Amazon, Meta, 2017–2025 | +30%, +60%, **+8% (2019)**, +34%, +34%, +20%, **−7% (2023)**, +55%, +65%. One fall and one stall in nine years; each followed a year of +20% to +60% | [FILING, my calc] [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0001018724/us-gaap/PaymentsToAcquireProductiveAssets.json) |
| Telecom and fibre, 1996–2002 | US telecom capex peaked at 1.2% of GDP in 2000 after rising 0.4 points; hyperscaler capex is forecast at 3.1% in 2027 after rising 2.5 points in four years. By 2002, 2.7% of fibre was lit | [ESTIMATE] [Apollo](https://www.apollo.com/wealth/insights-news/insights/daily-spark/the-ai-capex-boom-is-building-twice-as-fast-as-the-housing-boom); [M. Alderson, citing WSJ](https://martinalderson.com/posts/are-we-really-repeating-the-telecoms-crash-with-ai-datacenters/) |
| Chip-industry echo of 2000–02 | TSMC sales −24%, utilisation 106% → 51% (2001); ASML sales −41% (2001); Applied Materials −53% (FY2000–03); Micron −59% (FY2000–02) | [FILING] section 5 |
| Memory | Micron revenue fell in 6 of the 16 fiscal years 2010–2025 (FY2012, 2015, 2016, 2019, 2020, 2023) | [FILING, my calc] [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000723125/us-gaap/Revenues.json) |
| Equipment | Applied Materials revenue fell in 5 of 18 fiscal years 2008–2025; Lam in 4 of 16 (FY2010–2025) | [FILING, my calc] [SEC XBRL](https://data.sec.gov/api/xbrl/companyconcept/CIK0000006951/us-gaap/Revenues.json) |

**Stated odds, surveys and markets.**
- FutureSearch (15 Aug 2026): 15% for a "significant pullback in AI capex by December 31, 2027", defined as a year-on-year decline or a guidance cut above 10% attributed to moderating AI investment; reasons include multi-year supply agreements and the fact that "consensus expectations point toward a sharp deceleration in spending growth, not a decline" [ESTIMATE] — [FutureSearch](https://futuresearch.ai/app/p/a/ai-pullback-2027).
- Polymarket, "AI bubble burst by June 30, 2027": about 26.5% on 7 November 2026 after 31% on 5 November; resolves Yes only if three of six listed market events fall within one 90-day window [PRESS, market page not seen] — [FourWeekMBA](https://fourweekmba.com/ai-polymarkets-ai-bubble-test-chip-etf-down-37-5-nvidia-22/).
- Bank of America fund manager survey, July 2026: 28% expected a hyperscaler to announce a capex cut in 2026; 48% named hyperscaler capex the most likely source of a systemic credit event; 45% named an AI bubble the top tail risk; 82% called long semiconductors the most crowded trade [ESTIMATE] — [Webull/Benzinga, 15 Jul 2026](https://www.webull.com/news/15231944027677696). October 2026: AI bubble 23%; semiconductors most crowded 45%; net 37% overweight technology [PRESS] — [Crypto Briefing](https://cryptobriefing.com/bofa-survey-fund-managers-overweight-tech/).
- Base cases that already contain a 2028 stall: UBS +6%; Capital Economics −10%; Morgan Stanley US capacity additions −4% (Table in section 1).

**Evidence against a pause.**
- All five large buyers guided 2027 higher in late October 2026 (Table 1). Nvidia guided growth of about 70% for the year to January 2028 and called it supply-constrained [COMPANY CLAIM, single secondary source] — [SentiSense, 26 Aug 2026](https://app.sentisense.ai/stories/nvidia-beats-across-the-board-guides-108-billion-with-zero-china-revenue-assume-08262026).
- Supply contracts now run past 2028: SK hynix says DRAM and HBM are "effectively all sold out for the next three years, through 2029", with long-term agreements covering more than half of capacity for two years [COMPANY CLAIM] — [Kyunghyang Shinmun, 28 Oct 2026](https://www.khan.co.kr/en/article/202610281734027); ASML reports "strong interest to already place orders for 2029 and sometimes even 2030" [COMPANY CLAIM] — [Unite.AI, 14 Oct 2026](https://www.unite.ai/asml-warns-2027-2028-chip-tool-output-will-fall-short-of-ai-demand).
- KLA: physical constraints mean "we're going to have a longer cycle in terms of the growth" [COMPANY CLAIM] — [KLA call, 28 Oct 2026](https://www.webull.com/news/15828153893520384).

### Inferences
**My reading (labelled as mine).** The answer depends on the definition, so I give three.

| Definition | My probability | Reasoning |
|---|---|---|
| Aggregate capex of the five largest buyers falls year on year in calendar 2028 | about 20–25% | Similar to the prior. Two houses' base cases are flat to down in 2028; against that, contracts and backlogs cover 2027–28 |
| It falls in 2028 or 2029 (the sense of "around 2028") | about 30% (range 20–40%) | Somewhat above the prior. The past decade shows one fall and one stall in nine years, each after +20–60% growth; the current run is +55%, +65%, about +100% and "up" again, at 100% of operating cash flow and with debt funding the margin. Power and permitting add a second route to the same outcome |
| Growth below 10% in 2028 or 2029 (a stall suppliers would feel) | about 50% | UBS's base case is +6% for 2028; a stall at this scale still means flat or lower orders for wafers, tools and memory |

- Since the prior was set, three things moved the odds up: the size of external financing shown in the quarterly filings; the post-midterm permitting risk to 2028 US capacity; and OpenAI's smaller-than-sought round. Two moved them down: every buyer guided 2027 higher, and supply contracts lengthened to 2028–2030.
- The prior calls the pause "financing-led". The evidence suggests a pause, if it comes, is as likely to be led by power, permits and delivery delays, with financing as the amplifier. For chip, tool and materials makers the distinction matters little: orders slip either way.
- Confidence is low. No source measures the same event: FutureSearch's 15% covers an earlier window (to end-2027), Polymarket's 26.5% covers share prices to mid-2027, and the strategists give paths without probabilities. Anyone claiming precision finer than about ±10 points is overreaching.

### Gaps
- No Kalshi or Metaculus market on AI capital spending was found. The November 2026 Bank of America survey was not found.
- A sourced series for US telecom capital spending after 2000 was not obtained; I have used chip-industry filings as the measured echo of that bust.

# AI-native vulnerability discovery and repair, autonomous pentesting / security-validation vendors, and pentest and bug-bounty platforms (worldwide excluding Japan, South Korea, Taiwan, China): notes as of 2026-11-12

_Method note: the research date is 2026-11-12. I fetched primary pages where I could. The shared web-search budget ran out partway through the work. After that I only fetched URLs that earlier searches had already turned up, and ran no new searches. "(search snippet)" means the item comes from a search-result summary of the linked page, and I did not open that page myself. "[company claim, unconfirmed]" means no outside party confirms the claim. Theori is covered by another researcher, so only its AIxCC result appears here. I record business facts only and include no exploit technique details._

## 1. Ownership and funding: latest round, valuation, leads, M&A, IPO plans, current owner

### Takeaway
In 2026 a lot of capital went to autonomous finders. XBOW raised $120M at more than $1B in March and a $35M strategic extension in May. Horizon3.ai raised $250M at more than $2B in August. depthfirst raised $120M in under three months and RunSybil raised $40M. Cohere, a model maker, acquired AISLE, completing on 10 Nov 2026. I found no new 2025–26 primary rounds at HackerOne, Synack, Cobalt, YesWeHack or Intigriti. Bugcrowd bought Mayhem instead. NCC Group sold Escode, ended its sale review without a sale, and remains listed.

### Cited Findings
**XBOW (US, private)**
- **Series C:** $120M at a valuation of "over $1bn", announced 18–19 Mar 2026.
  - Leads: DFJ Growth and Northzone. New investors: Sofina and Alkeon. Existing investors: Altimeter, NFDG and Sequoia.
  - CEO is founder Oege de Moor. No revenue, ARR or customer count was disclosed. — [FinTech Global, 19 Mar 2026](https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/). The valuation was also reported by [Law360, 18 Mar 2026](https://www.law360.co.uk/articles/2454426) (search snippet).
- **Series C extension:** $35M on 7 May 2026 from strategic investors: Accenture Ventures, DNX Ventures, Liberty Global Tech Ventures, NVentures (NVIDIA), Samsung Ventures and SentinelOne S Ventures.
  - Samsung became a preferred reseller in South Korea.
  - XBOW had passed 250 employees. — [Pulse 2.0, 7 May 2026](https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/)
- **Total raised:** about $272M over five rounds: seed $20M, Series A $22M, Series B $75M, Series C $120M and the C extension $35M. The site records a $1B valuation but does not say whether it is pre- or post-money. — [Multiples.vc, accessed 12 Nov 2026](https://multiples.vc/private-comps/xbow)
  - Other trackers give $237M or count only the Series C (search snippet). The cumulative figure is not reconciled.
- **Series B:** $75M led by Apoorv Agrawal of Altimeter, with Sequoia and Nat Friedman. It took the total to $117M and the product became generally available. — [XBOW blog "Series B"](https://xbow.com/blog/series-b)
  - The page displays a date of 20 Mar 2026, but the round itself was announced in June 2025 alongside the HackerOne milestone. — [Slashdot/CSO, 5 Jul 2025](https://tech.slashdot.org/story/25/07/05/1847237) (search snippet)
- I found no IPO statement.

**Horizon3.ai (US, private; NodeZero)**
- **Series E:** $250M on 3 Aug 2026 at more than $2B, co-led by existing investors NightDragon and NEA. The prior valuation was $650M at the Series D "just over a year earlier".
  - New investors: Acrew, Blue Cloud Ventures, Demeter, EDBI (Singapore), PSG, SAIC and Sapphire.
  - Existing investors: Craft, Prosperity7, Qualcomm Ventures, Ridge and SignalFire.
  - Dave DeWalt and Morgan Kyauk of NightDragon join the board. The release says nothing about an IPO. — [Horizon3 press release, 3 Aug 2026](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/)
- **Total raised:** $428.5M — [Help Net Security, 3 Aug 2026](https://www.helpnetsecurity.com/2026/08/03/horizon3-ai-250-million-funding/) (search snippet)
- **Other investment:** Prosperity7 Ventures invested in Jan 2026 — [Business Wire, 13 Jan 2026](https://www.businesswire.com/news/home/20260113598188/en/Horizon3.ai-Secures-Investment-from-Prosperity7-Ventures-to-Protect-AI-Datacenters-and-Critical-Infrastructure) (search snippet). The $100M Series D was in June 2025 — [Bernama/Business Wire](https://mrem.bernama.com/viewsm.php?idm=51282) (search snippet).

**Pentera (Israel/US, private)**
- **Series D:** $60M on 12 Mar 2025, led by Evolution Equity Partners with Farallon. Insight and Blackstone did not take part.
  - Total raised is now $250M. The valuation was "not disclosed, estimated at over $1B", the same level as the 2022 Series C.
  - The CEO said the round was "clean", with no secondaries or special preferences. — [Calcalist/CTech, 12 Mar 2025](https://www.calcalistech.com/ctechnews/article/ryvxvby21x)
- **Round history:**

  | Date | Round | Amount | Notes |
  |---|---|---|---|
  | Jan 2018 | Seed | $5M | Awz |
  | Nov 2019 | A | $10M | |
  | Sep 2020 | B | $25M | Insight |
  | Jan 2022 | C | $150M | $1B post-money, K1 lead |
  | Mar 2025 | D | $60M | $1B |

  — [Multiples.vc](https://multiples.vc/private-comps/pentera)
- **Acquisitions and later moves:**
  - Two acquisitions in 2025: DevOcean, which became Pentera Resolve, and EVA Information Security, which became Pentera Offensive Security Services. Pentera says it is exploring M&A on the way to more than $200M ARR.
  - April 2026: listed on AWS Marketplace and appointed Hagit Ynon as CFO.
  - July 2026: partnership with Recorded Future. — [Pentera site](https://pentera.io/?p=762) (search snippet)
- I found no announced IPO plans — [TechStackIPO](https://www.techstackipo.com/company/pentera-security) (search snippet; the source marks its own data as pending verification).

**RunSybil (US, private)**
- **Funding:** $40M on 18 Mar 2026, led by Khosla Ventures, with S32, Anthropic's Anthology Fund, Menlo, Conviction and Elad Gil. Angels include Nikesh Arora and Jeff Dean. The valuation was not disclosed.
- **Founders:** the company was founded in 2023 by Ari Herbert-Voss and Vlad Ionescu.
  - Herbert-Voss was OpenAI's first security research hire, from 2019 to 2022.
  - Ionescu previously led Meta's offensive red teams. — [Fortune, 18 Mar 2026](https://fortune.com/2026/03/18/exclusive-ai-cybersecurity-startup-runsybil-founded-by-openais-first-security-hire-raises-40-million-led-by-khosla-ventures/)

**AISLE (Czech/US), now Cohere Cyber; owner is Cohere**
- **Origins and funding:** AISLE emerged from stealth in October 2025.
  - Angel investors named: Jeff Dean, Thomas Wolf, Olivier Pomel and Ian Goodfellow. No round amounts were given. — [Lupa.cz, 1 Jun 2026](https://www.lupa.cz/aktuality/cesky-aisle-je-podle-berkeley-nejlepsi-ai-v-hledani-zranitelnosti-predstihl-anthropic-google-i-microsoft/)
  - As of June 2026 the company had disclosed no funding or valuation — [The Next Web, Jun 2026](https://thenextweb.com/news/aisle-snapshot-on-prem-vulnerability-detection-regulated-enterprises) (search snippet).
- **Acquisition by Cohere:**
  - 15 Oct 2026: Cohere announced a letter of intent, "Cohere to acquire AISLE to advance cyber-resilient sovereign AI". — [Cohere blog](https://cohere.com/blog)
  - 10 Nov 2026: completion, announced as "Goodbye AISLE, Hello Cohere Cyber". AISLE "has been formally acquired by Cohere". No terms were disclosed. — [aisle.com, accessed 12 Nov 2026](https://aisle.com)

**ZeroPath (US, private; YC S24)**
- **Funding:**
  - $500K pre-seed in September 2024.
  - Seed led by SurgePoint Capital in January 2025. The amount was not disclosed; a co-founder's post cited "$7M", which is the most credible figure.
  - Aggregator figures of $20M and $25.5M are unverified.
  - ZeroPath was a finalist in the RSAC 2026 Innovation Sandbox, and the profile says the Sandbox SAFE came from Crosspoint. — [Zeltser RSAC 2026 profile, Mar 2026](https://zeltser.com/media/rsac-2026-sandbox/zeropath)
  - A "$12.5M Series A, Feb 2026" listing is unverified — [ToolRadar](https://toolradar.com/companies/zeropath-com) (search snippet).

**depthfirst (US, private)**
- **Series A:** $40M on 14 Jan 2026, led by Accel.
  - Founders: Qasim Mithani (ex-Databricks and Amazon), Daniele Perito (ex-Square) and Andrea Michi (ex-DeepMind). — [TechCrunch, 14 Jan 2026](https://techcrunch.com/2026/01/14/ai-security-firm-depthfirst-announces-40-million-series-a)
- **Series B:** $80M around 1 Apr 2026, led by Meritech, with Forerunner and The House Fund. That brings the total to $120M. The valuation was not disclosed. — [SecurityWeek, 1 Apr 2026](https://www.securityweek.com/depthfirst-raises-80-million-in-series-b-funding/)

**Cymulate (Israel, private)**
- Founded in 2016. Eyal Wachsman is CEO. The site shows investors only as unnamed logos and gives no round data. — [Cymulate About, accessed 12 Nov 2026](https://cymulate.com/about-us/)

**Picus Security (Turkey/US, private)**
- **Series B:** $27M in October 2021, led by Turkven, with Bek and Mastercard.
- **Series C:** $45M in September 2024, led by Riverwood, with Bek.
- **Total raised:** $80M. — [Picus About, accessed 12 Nov 2026](https://www.picussecurity.com/about-us)

**HackerOne (US, private)**
- The last disclosed round was a $49M Series E in January 2022, taking the total to about $160M.
- Kara Sprague became CEO in 2024, succeeding Mårten Mickos. — [The CyberSec Guru](https://thecybersecguru.com/analysis/what-happened-to-hackerone/), citing HackerOne. Sprague is confirmed as CEO as of 3 Nov 2026 — [Help Net Security, 3 Nov 2026](https://www.helpnetsecurity.com/?p=389850)

**Bugcrowd (US/Australia, private)**
- **Funding:** $102M of growth funding in February 2024, led by General Catalyst, with Rally and Costanoa — [Pulse 2.0](https://pulse2.com/bugcrowd-102-million-funding/) (search snippet). It then bought Informer — [BankInfoSecurity](https://www.bankinfosecurity.com/bugcrowd-buys-informer-to-enhance-attack-surface-management-a-25314?web_view=true) (search snippet).
- **Mayhem acquisition:** Bugcrowd acquired Mayhem Security on 4 Nov 2025; terms were not disclosed. — [Bugcrowd press release, 4 Nov 2025](https://www.bugcrowd.com/press-release/bugcrowd-acquires-mayhem-security/)
  - Mayhem was formerly ForAllSecure, a 2012 Carnegie Mellon spin-out that won DARPA's Cyber Grand Challenge in 2016.
  - Mayhem's CEO David Brumley became Bugcrowd's Chief AI and Science Officer (search snippet).
- **Valuation claim:** Bugcrowd said the deal "nearly doubled" its valuation, which had previously been reported at over $1B [company claim, unconfirmed] — [Business News Australia](https://www.businessnewsaustralia.com/articles/bugcrowd-unites-hacker-community-with-mayhem-security-acquisition.html) (search snippet; the page returned 403 when fetched).

**Synack (US, private)**
- The latest round is a Series D, with about $107.4M raised in total and 201–500 staff — [CB Insights](https://www.cbinsights.com/company/synack) (search snippet).
- I found no 2026 round or layoffs.

**Cobalt (US/Germany, private)**
- The last disclosed round is a $29M Series B led by Highland Europe — [Cobalt blog](https://www.cobalt.io/blog/q-and-a-with-cobalts-ceo-and-cso-about-securing-series-b-funding) (search snippet).
- Tony Spinelli joined the board in April 2026 (search snippet). I found no 2026 round or acquisition.

**YesWeHack (France, private)**
- **Series C:** €26M in June 2024, led by Wendel, with Adelie and Bpifrance. The company then had 110 staff. — [Presse-Citron](https://www.presse-citron.net/french-tech-qui-est-yeswehack-la-start-up-de-hackeurs-ethiques-qui-a-conquis-le-cac40/) (search snippet)
- **2025 events:** YesWeHack made its "first-ever acquisition" in 2025; the target is not named on the page. — [YesWeHack Report 2026 page, 5 Feb 2026](https://www.yeswehack.com/community/yeswehack-report-2026-trends-security)

**Intigriti (Belgium, private)**
- The latest round I found is a Series B of more than €21M in April 2022 — [Intigriti blog](https://www.intigriti.com/blog/news/intigriti-secures-more-than-21-million-series-b-funding) (search snippet). I found no 2026 round.

**Immunefi (Web3, private)**
- The Immunefi Foundation launched the IMU token on 22 Jan 2026. Anchorage Digital bought IMU in March 2026. — [KuCoin blog, promotional](https://www.kucoin.com/blog/en-immunefi-ecosystem-2026-q1-update)

**NCC Group plc (UK; LSE: NCC; FTSE 250 as of 11 Jun 2026)**
- **Escode sale:** sold to funds controlled by TDR Capital. The SPA was signed on 21 Jan 2026 and the sale completed on 29 May 2026.
  - Net cash proceeds were £262.8m before transaction costs and completion adjustments.
  - The release also cites gross proceeds of £309.1m on completion.
- **Earlier disposals:** Fox-IT DetACT (30 Apr 2024) and Fox-IT Crypto (28 Mar 2025). The three disposals together had an EV of c.£349m, about 9.8x adjusted EBITDA.
- **Strategic review:** concluded 11 Jun 2026. NCC will remain listed, it said it is "not in receipt of any approaches", and the offer period ended. — [NCC interim results RNS, 11 Jun 2026](https://www.investegate.co.uk/announcement/rns/ncc-group--ncc/unaudited-interim-results/9612591) (full text: [PDF](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf))
- **Escode enterprise value:** £275m — [AJ Bell, 11 Jun 2026](https://www.ajbell.co.uk/news/articles/ncc-decides-remain-london-listed-pure-play-cyber-security-firm); [Verdict](https://www.verdict.co.uk/ncc-group-sale-escode-tdr/) (search snippet)
- **October 2025:** NCC said it was considering offers for the whole company — [AJ Bell, 11 Dec 2025](https://www.ajbell.co.uk/news/articles/ncc-reports-decline-full-year-sales-one-offs-boost-profitability)
- **CEO change, 27 Oct 2026:** CFO Guy Ellis succeeded Mike Maddison "with immediate effect" — [Sharecast via Hargreaves Lansdown, 27 Oct 2026](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations)

### Inferences
- **Valuation steps:**
  - Horizon3's valuation roughly tripled in about 14 months, from $650M to more than $2B, while its stated ARR growth was 120%. That implies the ARR multiple expanded by roughly 1.4x. This is my arithmetic on company figures.
  - Pentera's valuation was flat at about $1B from January 2022 to March 2025, while ARR rose more than 300%. That implies the multiple compressed about 4x.
  - So investors in 2026 paid up for "AI-native" positioning (XBOW, Horizon3, depthfirst) over the earlier automation generation.
- **Who is buying whom:** in 2025–26 the main acquirers were a model maker (Cohere bought AISLE) and a crowd platform (Bugcrowd bought Mayhem, an autonomous CRS pioneer). This fits model makers moving down into security products and platforms buying automation they did not build.
- **Strategic money in XBOW:** the May 2026 investors in XBOW (Accenture, NVIDIA, Samsung, SentinelOne, Liberty Global) are distribution and compute partners. That is a channel advantage, but the round was likely priced with strategic terms.

### Gaps
- I found no post-money valuations for XBOW's Series B, RunSybil, depthfirst, ZeroPath, Picus, Cymulate, HackerOne (post-2022), Synack, Cobalt, YesWeHack or Intigriti.
- I could not verify Cymulate's last round in this session. The site lists none, and my searches ran out before I found coverage.
- I found nothing on Trail of Bits' ownership or outside funding. It appears independent and privately held, but I did not confirm this.
- I did not find the Cohere–AISLE price or structure.
- I did not open the Caplight and Forge Global secondary pages for XBOW, Pentera and ZeroPath, which appeared in searches, so I have no secondary marks.

## 2. Revenue or ARR and growth, named customers, pricing model, and share of labour or services revenue

### Takeaway
Few firms disclose dollar figures. Pentera reports more than $100M ARR as of January 2026, and Horizon3 reports +120% ARR growth (August 2026) with no base given; both are company claims. XBOW reports more than 100 customers and no ARR. NCC Group remains essentially all services: about 66% of Cyber revenue is project or hourly work and about 34% is managed services, now that the Escode escrow product line is sold. Pricing is mostly undisclosed subscription. The exception is ZeroPath's per-seat list price.

### Cited Findings
- **XBOW:**
  - ARR and revenue were not disclosed at the Series C — [FinTech Global, 19 Mar 2026](https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/)
  - More than 100 customers globally, including Moderna and Seznam, as of 7 May 2026 [company claim, unconfirmed] — [Pulse 2.0](https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/)
  - Pricing is not public; buyers "book a demo" — [XBOW blog](https://xbow.com/blog/series-b). The revenue model is listed as product sales — [Multiples.vc](https://multiples.vc/private-comps/xbow).
  - Bounty income was small. As of 4 Aug 2025 the largest XBOW bounty found on HackerOne was $3,000 (Hilton) — [God Access Substack, Aug 2025](https://godaccess.substack.com/p/behind-the-hype-is-xbow-ai-really-the-game-changer)
- **Horizon3.ai:**
  - ARR +120% year on year, reported 3 Aug 2026, with no dollar base [company claim, unconfirmed].
  - More than 7,000 organisations, including four Fortune 10 companies, and "310,000 tests safely executed in production" [company claim, unconfirmed].
  - Pricing and profitability were not disclosed. — [Horizon3 press release, 3 Aug 2026](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/)
  - A March 2026 release reported FY2026 ARR +102% [company claim, unconfirmed] — [Business Wire, 19 Mar 2026](https://www.businesswire.com/news/home/20260319233634/en/) (search snippet; the page returned 403)
- **Pentera:**
  - ARR passed $100M as of 7 Jan 2026, with 1,200+ enterprises in 60+ countries and the US team up more than 40%. No growth rate was given. [company claim, unconfirmed] — [TechIntelPro, 7 Jan 2026](https://techintelpro.com/news/cybersecurity/ai/pentera-hits-100m-arr-as-first-aev-centaur-company)
  - In March 2025 Pentera said ARR had grown more than 300% since January 2022. Customers had doubled to over 1,100 and the average deal had quadrupled to about $100K. Headcount was about 400 and the company was "approaching breakeven". It targets $200M of revenue and profitability within about 2.5 years. [company claim, unconfirmed] — [Calcalist/CTech, 12 Mar 2025](https://www.calcalistech.com/ctechnews/article/ryvxvby21x)
  - A services line (expert-led red teaming) came from the EVA acquisition. Its revenue share is not disclosed. — [TechIntelPro](https://techintelpro.com/news/cybersecurity/ai/pentera-hits-100m-arr-as-first-aev-centaur-company)
- **RunSybil:** named customers are Cursor, Turbopuffer, Notion, Baseten and Thinking Machines Lab. It also cites "several major financial institutions and Fortune 500 companies". Revenue, pricing and headcount were not disclosed. — [Fortune, 18 Mar 2026](https://fortune.com/2026/03/18/exclusive-ai-cybersecurity-startup-runsybil-founded-by-openais-first-security-hire-raises-40-million-led-by-khosla-ventures/)
- **AISLE / Cohere Cyber:**
  - Customer and partner logos include Bose, Ataccama, Livesport, Productboard, Apify, ENISA, Chromium and the Ethereum Foundation. OpenSSL and curl appear as case studies.
  - Deployment options are SaaS, private cloud, on-premises and air-gapped. Products include a one-time "Snapshot" audit. — [aisle.com](https://aisle.com)
  - Amazon confirmed and fixed issues AISLE found, but no commercial contract is described — [Lupa.cz](https://www.lupa.cz/aktuality/cesky-aisle-je-podle-berkeley-nejlepsi-ai-v-hledani-zranitelnosti-predstihl-anthropic-google-i-microsoft/)
- **ZeroPath:**
  - Claims "750+ companies" as of August 2025 [company claim, unconfirmed], and 200,000+ monthly scans by early 2026.
  - Named customers: Aptos Labs (case study), Exodus, Commenda and Aquanow.
  - List price: Team plan $1,000 a month plus $60 per developer; Enterprise is custom.
  - Revenue is estimated at about $5M by a third party, unverified.
  - It also sells penetration-testing services. — [Zeltser profile, Mar 2026](https://zeltser.com/media/rsac-2026-sandbox/zeropath)
- **depthfirst:** partners are AngelList, Lovable and Moveworks. ARR and pricing were not disclosed. — [TechCrunch, 14 Jan 2026](https://techcrunch.com/2026/01/14/ai-security-firm-depthfirst-announces-40-million-series-a)
- **Cymulate:** "1000+" customers in 50 countries [company claim, unconfirmed] — [Cymulate About](https://cymulate.com/about-us/)
- **Picus:** 500+ customers and 80 channel partners. Mastercard's "Cyber Front" platform is "powered by Picus". — [Picus About](https://www.picussecurity.com/about-us)
- **HackerOne:**
  - 2023 customer terms set a default 20% fee on bounty rewards. HackerOne later moved toward subscription pricing; the article gives no date.
  - In 2024 it said its pentest and AI red-teaming business grew 200% in 12 months [company claim, unconfirmed]. — [The CyberSec Guru](https://thecybersecguru.com/analysis/what-happened-to-hackerone/)
  - Researcher payouts were $89.1M for July 2025 to June 2026, across 92,194 valid reports — [HackerOne Security Research Report 2026](https://www.hackerone.com/report)
  - The prior year (July 2024 to June 2025) was $81M, up 13% — [HackerOne press release, Oct 2025](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy) (search snippet)
- **Bugcrowd:** no revenue figures. Products include Savant (Pathseeker, Vista), AI Pen Test and CrowdMatch, plus Mayhem's API, code, SBOM and RL-environment products. — [Bugcrowd press release, 4 Nov 2025](https://www.bugcrowd.com/press-release/bugcrowd-acquires-mayhem-security/)
- **Synack:**
  - Sara AI Pentesting reached general availability on 8 May 2026, sold through its PTaaS platform and the AWS, Microsoft and Google Cloud marketplaces. Pricing was not disclosed.
  - Synack claims "nearly 10 million hours" of testing and says Sara runs "a fraction of the cost" of a traditional pentest [company claim, unconfirmed]. — [IT Brief, 8 May 2026](https://itbrief.co.nz/story/synack-launches-sara-ai-pentesting-for-wider-coverage)
- **Cobalt:**
  - Claims "thousands" of customers [company claim, unconfirmed].
  - Its Cobalt Core network has about 500 vetted pentesters.
  - Autonomous Pentest reaches general availability in August 2026, with human pentesters reviewing plans and scope. Pricing is not stated. — [ChannelLife, 24 Jul 2026](https://channellife.news/story/cobalt-launches-autonomous-pentest-for-continuous-testing)
- **YesWeHack:** the European Commission made it its preferred bug-bounty provider in 2025. It is also a CVE Numbering Authority and sells an "Agentic Pentest" product. — [YesWeHack Report 2026 page, 5 Feb 2026](https://www.yeswehack.com/community/yeswehack-report-2026-trends-security)
- **Intigriti:** revenue appears only as third-party guesses of about $7.3M, which are unreliable — [Bitscale](https://bitscale.ai/directory/intigriti) (search snippet). Clients named in press are the European Commission, Brussels Airlines, Randstad and Kinepolis (search snippet).
- **Immunefi** (promotional source, self-reported):

  | Measure | Figure |
  |---|---|
  | Researcher payouts, Q4 2025 | $2.40M across 953 reports |
  | Researcher payouts, Q1 2026 | $7.87M across 1,104 reports (the same page also says $7.3M across 1,268) |
  | Share of Q1 2026 from one payout | 38% ($3M) |
  | All-time payouts | more than $134M by March 2026 |
  | Active programmes | 230 |
  | Registered researchers | 81,828 |

  — [KuCoin blog](https://www.kucoin.com/blog/en-immunefi-ecosystem-2026-q1-update)
- **NCC Group, H1 FY26 (six months to 31 Mar 2026):**
  - Cyber revenue was £118.4m, +5.9% at constant currency excluding Fox Crypto. Including Fox Crypto in the prior period it was −4.1% reported.
  - By capability:

    | Capability | Revenue | Growth (constant currency) | Share of Cyber |
    |---|---|---|---|
    | Technical Assurance Services (pen testing and assurance) | £45.0m | +0.2% | |
    | Consulting & Implementation | £26.1m | +19.7% | |
    | Managed Services | £40.0m | +4.7% | 33.8% |
    | Digital Forensics & Incident Response | £6.9m | +7.8% | |
    | Other | £0.4m | | |

  - By region: UK & APAC £73.9m (+12.5%), North America £25.0m (−8.1%), Europe £19.5m (+3.2%).
  - Consulting & Implementation plus Managed Services made up 55.8% of Cyber revenue, against 37.5% in the year to May 2023.
  - Utilisation across Technical Assurance and Consulting rose to 76.0% from 70.4% in FY25, helped by the Manila delivery centre. NCC has about 1,800 Cyber staff. — [NCC interims, 11 Jun 2026](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
- **NCC Group, FY26 (to 30 Sep 2026):** Cyber revenue of about £235m, +3.7% at constant currency — [Sharecast/HL, 27 Oct 2026](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations)

### Inferences
- **NCC revenue mix:** after the Escode sale (Escode was 21.7% of H1 FY26 group revenue), NCC has no product or escrow revenue. About 66% of Cyber revenue is project or hourly work (Technical Assurance 38%, Consulting 22%, DFIR 6%). About 34% is contracted managed services, which is still labour-delivered. Revenue per Cyber employee is roughly £130K (≈£235m ÷ ~1,800), which is my arithmetic.
- **Crowd platforms:** HackerOne, Bugcrowd, Synack and Cobalt all sell human-delivered PTaaS alongside new agentic products. None discloses the labour share. On the evidence, a large but unknown share of their revenue is still tied to human testing hours or crowd output.
- **Pricing models:** the AI-native firms price as subscriptions. Pentera's average deal was about $100K in March 2025. ZeroPath is the exception, pricing per developer seat, which exposes it to seat counts and to bundling by model makers.

### Gaps
- No credible dollar ARR figures for XBOW, Horizon3 (one search snippet cited an unverified "~$100M ARR in 2025" attributed to TechCrunch), RunSybil, depthfirst, AISLE, HackerOne, Bugcrowd, Synack, Cobalt, YesWeHack, Intigriti, Picus or Cymulate.
- No services share disclosed for any private platform.
- No pricing disclosed for XBOW, Horizon3, Synack Sara or Cobalt Autonomous Pentest.

## 3. Independent evidence of lead: leaderboards, credited CVEs, vendor-confirmed bounties, competitions, analysts, benchmarks

### Takeaway
The strongest outside-confirmed signals are these:
- DARPA AIxCC results (8 Aug 2025): Team Atlanta, Trail of Bits and Theori came first to third.
- Google's $250,000 Chrome full-chain reward to XBOW, approved 31 Aug 2026 and made public 13 Oct 2026. The work was human-steered and AI-heavy.
- XBOW's HackerOne #1 US ranking for Q2 2025, which leaned on VDPs; by 4 Aug 2025 it was 3rd.
- AISLE's credited OpenSSL CVEs, and first place on a Berkeley coverage map (June 2026).

Analyst recognition in this field is thin. It is mostly Gartner Peer Insights, Frost & Sullivan, GigaOm and G2 for the breach-and-attack-simulation and exposure-validation vendors.

### Cited Findings
- **XBOW on HackerOne (2025):**
  - As of 25 Jun 2025 XBOW was #1 in the US and #1 in the "VDP Institutions" category for April–June 2025, but 6th globally in the overall ranking that includes bounty programmes. A HackerOne co-founder said "AI doesn't learn to hack on its own. Hackers train it." — [Gigazine, 25 Jun 2025](https://www.gigazine.net/gsc_news/en/20250625-hackerone-xbow)
  - Bloomberg reported it as the first time a company's AI product topped HackerOne's US leaderboard by reputation — [Bloomberg, 24 Jun 2025](https://www.bloomberg.com/news/articles/2025-06-24/one-of-the-best-hackers-in-the-country-is-an-ai-bot) (search snippet)
- **XBOW's own submission record:** about 1,060 submissions. — [XBOW blog, 24 Jun 2025](https://xbow.com/blog/top-1-how-xbow-did-it/)
  - Outcomes: 130 resolved, 303 triaged, 125 pending, 33 new, 208 duplicates, 209 informative and 36 not applicable.
  - Severity over 90 days: 54 critical, 242 high, 524 medium and 65 low.
  - XBOW's security team reviewed findings before submission to comply with HackerOne's policy on automated tools.
- **Critics:**
  - The ranking came from the VDP leaderboard, not the bug-bounty leaderboard — [Utku Sen, 25 Jun 2025](https://utkusen.substack.com/p/does-xbow-ai-hacker-deserve-the-hype)
  - XBOW was 3rd in the US with 3,921 reputation points on 4 Aug 2025. The same author estimates about 37.5% accuracy and notes the largest bounty was $3,000. — [God Access Substack, Aug 2025](https://godaccess.substack.com/p/behind-the-hype-is-xbow-ai-really-the-game-changer)
  - XBOW's March 2026 Series C materials still say it "reached the top of the HackerOne leaderboard" [company claim; no current ranking verified] — [FinTech Global](https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/)
- **Google confirmation of XBOW's Chrome finding:** CyberInsider, 14 Oct 2026 — [CyberInsider](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/)
  - Google's public issue record shows an engineer reproduced the three-bug chain, and Google's reward panel approved $250,000 on 31 Aug 2026. All three bugs are fixed.
  - The campaign ran 2–7 Aug 2026 at about $40,000 of compute.
  - Humans chose targets, checked results and redirected the work, led by Brendan Dolan-Gavitt. XBOW published on 13 Oct 2026.
  - It was the first payout under Google's new 2026 Chrome rules — [CSO Online, 16 Oct 2026](https://www.csoonline.com/article/4236599/xbow-spent-40k-on-ai-and-cracked-google-chrome-wide-open-2.html)
  - Coverage called it the first full-chain award of 2026 and the second in the programme's history. "First to an autonomous platform" and "a billion users affected" are XBOW's framing. — [Let's Data Science](https://letsdatascience.com/news/google-awards-xbow-250000-for-chrome-exploit-chain-cf47fed1) (search snippet)
- **AISLE on OpenSSL:** 20 credited CVEs across three releases. — [AISLE blog, 24 Apr 2026](https://aisle.com/blog/aisle-discovers-20-openssl-zero-days-in-6-months) [company account; CVE credits are public but I did not check them one by one]
  - The releases were September 2025 (3), January 2026 (all 12) and 7 Apr 2026 (5 of 7).
  - Ten of the fixes were written by AISLE and accepted.
  - One CVE was independently reported by Anthropic (Alex Gaynor) 63 days after AISLE.
  - Curl maintainer Daniel Stenberg and Bruce Schneier are quoted crediting AISLE with 13 of 14 OpenSSL CVEs assigned in 2025 — [aisle.com](https://aisle.com)
  - The site also claims "650+" independently validated CVEs, plus 2026 credits in FFmpeg and Wireshark [company claim, unconfirmed].
- **Berkeley "Agentic Vulnerability Coverage Map" (June 2026):** AISLE ranked first, ahead of Anthropic, Google, Microsoft and XBOW. It led on breadth (73 CWE types, 20 of 25 MITRE Top 25) and on volume (205 CVEs). — [Lupa.cz, 1 Jun 2026](https://www.lupa.cz/aktuality/cesky-aisle-je-podle-berkeley-nejlepsi-ai-v-hledani-zranitelnosti-predstihl-anthropic-google-i-microsoft/) AISLE's site cites 514 against 267 for second place [company claim].
- **DARPA AIxCC final, announced 8 Aug 2025 at DEF CON 33:** — [DARPA, 8 Aug 2025](https://www.darpa.mil/news/2025/aixcc-results)
  - Placings:

    | Place | Team | Prize |
    |---|---|---|
    | 1 | Team Atlanta (Georgia Tech, Samsung Research, KAIST, POSTECH) | $4M |
    | 2 | Trail of Bits | $3M |
    | 3 | Theori | $1.5M |

  - The other finalists were all_you_need_is_a_fuzzing_brain, Shellphish, 42-beyond-bug and Lacrosse; the DARPA page gives no placings for them.
  - Systems found 54 of 63 synthetic vulnerabilities and patched 43. They also found 18 real zero-days and supplied 11 patches.
  - Cost was about $152 per task. Patches arrived in 45 minutes on average, across more than 54M lines of code.
  - All seven systems are to be released as open source. DARPA and ARPA-H added $1.4M in prizes for teams that integrate the systems into critical infrastructure software.
  - Anthropic, Google and OpenAI each donated $50K in LLM credits per team.
- **Analyst and peer recognition:**
  - Synack was a Leader and Fast Mover in GigaOm's 2025 PTaaS Radar (company-cited) — [Synack press release, 13 Apr 2026](https://www.bolsamania.com/nota-de-prensa_print/mercados/synack-launches-glasswing-readiness-assessment-to-close-the-ai-security-coverage-gap--22278365.html)
  - Picus: Gartner Peer Insights Customers' Choice in adversarial exposure validation, Frost Radar 2026 Innovation Leader, and #1 in G2's breach-and-attack-simulation report for four quarters — [Picus press releases](https://www.picussecurity.com/press-releases)
  - Cymulate: Gartner Peer Insights Customers' Choice, and it cites the 2026 Gartner Market Guide for Adversarial Exposure Validation — [Cymulate](https://cymulate.com/about-us/)
  - Pentera: Leader in the QKS SPARK Matrix 2025 for exposure management — [TechIntelPro](https://techintelpro.com/news/cybersecurity/ai/pentera-hits-100m-arr-as-first-aev-centaur-company)
  - ZeroPath: RSAC 2026 Innovation Sandbox finalist; the assessor scored it 29/40 — [Zeltser](https://zeltser.com/media/rsac-2026-sandbox/zeropath)
- **Horizon3:** "FedRAMP High authorized" and "four Fortune 10" customers [company claim; I did not check FedRAMP's marketplace] — [Horizon3 press release](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/)
- **HackerOne's 2025 report:** autonomous agents ("hackbots") had more than 560 validated reports, mostly in simpler bug classes — [HackerOne press release, Oct 2025](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy) (search snippet)
- **Model makers' results, for context:**
  - Anthropic's Claude Code Security team found more than 500 vulnerabilities in production open-source code using Opus 4.6 — [Anthropic, 20 Feb 2026](https://www.anthropic.com/news/claude-code-security)
  - Google's CodeMender upstreamed 72 security fixes over six months — [Google DeepMind, 6 Oct 2025](https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/)
  - OpenAI's Codex Security scanned 1.2M commits in 30 days and found about 800 critical issues (company-reported) — [The Hacker News, Mar 2026](https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html) (search snippet)
  - Glasswing reportedly scanned more than 1,000 open-source projects and flagged 23,019 potential issues, 6,202 of them priority or critical. Independent firms confirmed over 90% of a 1,752-finding sample, and fewer than 1% had been fixed — [ForkLog, 24 Jul 2026](https://forklog.com/en/the-end-of-bug-bounties/) (secondary source)

### Inferences
- **XBOW's two results:** the 2025 HackerOne ranking shows volume on lower-competition, mostly unpaid VDP programmes. The 2026 Chrome reward is a much stronger, vendor-confirmed signal of depth, but it was done with human direction on a public model. Neither shows a moat that model makers cannot match.
- **AISLE's evidence:** credited CVEs plus maintainer-accepted fixes are a "final" external judge. That matches the framework's strongest position, and it is probably why a model maker bought the company.
- **Exposure-validation vendors (Pentera, Horizon3, Cymulate, Picus):** their evidence is mostly peer reviews and customer counts, not independent effectiveness tests.

### Gaps
- XBOW's current (2026) HackerOne ranking: the leaderboard is dynamic and I could not retrieve it.
- AIxCC placings 4–7 and prize amounts.
- RSAC 2026 Innovation Sandbox winner.
- No Forrester, IDC or GigaOm rankings of autonomous pentesting vendors found.
- The underlying Berkeley study was not retrieved; only Czech press coverage of it.

## 4. Access to gated frontier models, and competition from model makers' own security products

### Takeaway
None of the companies in scope is named in Anthropic's Project Glasswing or OpenAI's Trusted Access for Cyber partner lists. The named gated access goes to large platform vendors (CrowdStrike, Palo Alto Networks, Cisco, Zscaler and others) and banks. Trail of Bits is the exception among testers: it works directly with OpenAI and uses GPT-5.5-Cyber. XBOW's headline Chrome result used a publicly available OpenAI model. Model makers now ship their own find-and-fix products: Anthropic's Claude Code Security (February 2026), OpenAI's Codex Security (March 2026) and Google's CodeMender (October 2025). One model maker, Cohere, bought a finder outright (AISLE).

### Cited Findings
- **Anthropic Project Glasswing:** — [Anthropic Glasswing page](https://www.anthropic.com/glasswing)
  - Launched 7 Apr 2026 with AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA and Palo Alto Networks, plus "over 40 additional organizations" that were not named.
  - Anthropic committed up to $100M of Mythos Preview credits and $4M of donations.
  - Mythos Preview will not be generally available. After the preview, the price is $25 per million input tokens and $125 per million output tokens.
  - On 6 Oct 2026 Anthropic set up a three-tier Cyber Verification Program covering Claude Opus 5.5, Sonnet 5.5 and Mythos 5.1. Glasswing members move to the "Specialized Access" tier.
  - The page does not name XBOW, Horizon3, Pentera, HackerOne, Bugcrowd, Synack, Trail of Bits, NCC, RunSybil, AISLE, depthfirst, ZeroPath or any pentest firm.
- **Glasswing expansion, 2 Jun 2026:** about 150 more organisations in more than 15 countries, about 200 in total. None of the new members were named, and ENISA was still negotiating use. — [Implicator, 2 Jun 2026](https://www.implicator.ai/anthropic-adds-150-new-project-glasswing-partners-in-more-than-15-countries/)
- **OpenAI Trusted Access for Cyber (TAC):** — [GovInfoSecurity](https://www.govinfosecurity.com/openai-courts-banks-in-trusted-access-for-cyber-partner-push-a-31447); [SecurityBrief UK](https://securitybrief.co.uk/story/openai-launches-trusted-access-for-cyber-with-major-names); [Help Net Security](https://www.helpnetsecurity.com/?p=366217) (search snippets)
  - Started as a pilot in February 2026 alongside GPT-5.3-Codex, with $10M of API credits.
  - Expanded on 14 Apr 2026 to thousands of vetted individuals and hundreds of teams. The top tiers get GPT-5.4-Cyber.
  - Initial partners were Bank of America, BlackRock, BNY, Citi, Goldman Sachs and Morgan Stanley.
  - Cisco, CrowdStrike, JPMorganChase and NVIDIA are in both TAC and Glasswing. iVerify, SpecterOps and Zscaler are in TAC only.
- **OpenAI Codex Security:** "Aardvark is now Codex Security", a research preview from 6 Mar 2026 for ChatGPT Enterprise, Business, Edu and Pro users, plus "Codex for OSS" for maintainers — [OpenAI Aardvark page](https://openai.com/index/introducing-aardvark) (search snippet). I found no evidence it had reached general availability by November 2026.
- **Anthropic Claude Code Security:** a limited research preview since 20 Feb 2026 for Enterprise and Team plans, with free expedited access for open-source maintainers. Pricing is not stated. — [Anthropic, 20 Feb 2026](https://www.anthropic.com/news/claude-code-security)
- **Google CodeMender:** a research agent since 6 Oct 2025 that patches vulnerabilities and rewrites code to remove whole classes of them. All patches are human-reviewed and it is not a product. — [Google DeepMind](https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/)
- **Trail of Bits:** "Patch the Planet" launched 22 Jun 2026 as a partnership with OpenAI and its "Daybreak" initiative, using GPT-5.5-Cyber and Codex. — [Trail of Bits blog, 22 Jun 2026](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/)
  - First-week output covered 19 projects, including cURL, Sigstore, PyPI, Go and RustCrypto. More than 30 projects have joined.
  - Output: 64 PRs, 51 issues and 37 patches merged.
  - Later posts cover Codex-based backporting (2 Nov 2026) and agent plugins for patching (21 Oct 2026) — [Trail of Bits blog index](https://blog.trailofbits.com/)
- **XBOW:** used OpenAI's GPT-5.6 Sol, described as publicly available. No special access arrangement was mentioned. OpenAI co-founder Greg Brockman publicly highlighted the result on 13 Oct 2026. — [CyberInsider](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/); [CSO Online](https://www.csoonline.com/article/4236599/xbow-spent-40k-on-ai-and-cracked-google-chrome-wide-open-2.html)
- **RunSybil:** Anthropic's Anthology Fund is an investor, and the models used are not disclosed. Fortune contrasts RunSybil's live-application testing with Claude Code Security's pre-deployment code analysis. Khosla says there is "currently little competition in this part of the offensive security market". — [Fortune](https://fortune.com/2026/03/18/exclusive-ai-cybersecurity-startup-runsybil-founded-by-openais-first-security-hire-raises-40-million-led-by-khosla-ventures/)
- **HackerOne:** AI partners include AWS Bedrock and Anthropic under zero data retention, per an April 2026 statement — [The CyberSec Guru](https://thecybersecguru.com/analysis/what-happened-to-hackerone/), citing a HackerOne blog post
- **depthfirst:** trains its own model, dfs-mini1, on an open-source base model; the first version targets smart contracts. Frontier models are not mentioned. — [SecurityWeek, 1 Apr 2026](https://www.securityweek.com/depthfirst-raises-80-million-in-series-b-funding/)
- **AISLE:** uses a "multi-model system" and claims "10x more cost-efficient vulnerability discovery than Mythos" [company claim, unconfirmed] — [aisle.com](https://aisle.com). Cohere's stated rationale for the acquisition is "cyber-resilient sovereign AI" — [Cohere blog](https://cohere.com/blog)
- **Positioning around Mythos without access:**
  - Synack's "Glasswing-Readiness Assessment" (13 Apr 2026) is built around Mythos-era risk, but does not say Synack has Glasswing access — [Synack press release](https://www.bolsamania.com/nota-de-prensa_print/mercados/synack-launches-glasswing-readiness-assessment-to-close-the-ai-security-coverage-gap--22278365.html)
  - Picus launched an "Autonomous Exposure Validation Platform for the post-Mythos era" in 2026 — [Picus press releases](https://www.picussecurity.com/press-releases)
- **AIxCC:** model makers supplied $50K of LLM credits to each finalist — [DARPA](https://www.darpa.mil/news/2025/aixcc-results)

### Inferences
- **Who gets gated access:** it is tied to scale and distribution (platform security vendors, hyperscalers, banks) and to direct partnerships (Trail of Bits with OpenAI). The venture-backed finders in scope rely on public or tier-accessible models.
  - That has not stopped top results so far: XBOW's Chrome result used a public model.
  - But the people who decide access are also competitors. Anthropic and OpenAI scan open source themselves (Glasswing, Codex for OSS) and sell code-security products. Finders whose value is "finding" in source code are the most exposed: ZeroPath, and depthfirst's code products.
- **Less exposed positions:** firms with an environment-specific judge are less exposed. Examples are Horizon3 and Pentera (exploitation inside customer networks, plus a FedRAMP High authorisation), RunSybil and XBOW (live-application testing), and platforms with a crowd and a compliance wrapper.
- **Unequal access across countries:** Glasswing grew to 15+ countries only after vetting, and ENISA was still negotiating in June 2026. Cohere's "sovereign" pitch and Samsung reselling XBOW in Korea suggest non-US buyers will look for non-US or locally integrated stacks. Israeli (Pentera, Cymulate) and Turkish (Picus) vendors could face unequal gated-model access. This is my inference; I found no direct evidence.

### Gaps
- No primary OpenAI TAC partner page: openai.com returned 403, so the partner list rests on press coverage.
- The 40+ unnamed Glasswing organisations and the ~150 June additions are unknown. Some in-scope firms could be among them.
- I don't know which models Horizon3, Pentera, Cymulate, Picus, Synack, Cobalt or Bugcrowd/Mayhem use.

## 5. Path forward: transitions (1)–(6), what each company has said versus done

### Takeaway
Transitions (1) billable hours → automation and (2) human triage → machine-speed find-and-fix are now concrete at every crowd platform:
- HackerOne launched Hai Triage and cut Internet Bug Bounty rewards.
- Bugcrowd bought Mayhem and added anti-spam controls.
- Synack launched Sara and Cobalt launched Autonomous Pentest.

The AI-native firms are adding remediation. Transition (4) is now the main strategic risk, with model makers both gating access and competing. Transition (6), verified software, shows up only in early form: Trail of Bits' agent-built formal models and Google's CodeMender rewriting code. NCC says AI "reinforces" the case for human assurance while it raises utilisation and sells its only product line.

### Cited Findings
- **XBOW:**
  - Said: it will use the funds for enterprise expansion, product and international growth — [FinTech Global](https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/)
  - Done: HackerOne #1 US (Q2 2025), the Chrome $250K (2026), 100+ customers, a Samsung reseller deal in South Korea and 250+ staff — [Pulse 2.0](https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/)
- **Horizon3.ai:**
  - Said: funds go to go-to-market, Singapore, Australia and EMEA, and "autonomous blue-team agents that remediate findings from NodeZero pentests". It cites DORA, NIS 2, NIST CSF 2.0 and HIPAA as compliance drivers.
  - Done: FedRAMP High and 7,000+ organisations [company claims]. — [Horizon3 press release](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/)
- **Pentera:** — [TechIntelPro](https://techintelpro.com/news/cybersecurity/ai/pentera-hits-100m-arr-as-first-aev-centaur-company); [Pentera site](https://pentera.io/?p=762) (search snippet); [Calcalist](https://www.calcalistech.com/ctechnews/article/ryvxvby21x)
  - Done: launched Resolve (AI-assisted remediation workflows, 100+ integrations), Offensive Security Services (human red team), AI web attack testing and ISO/IEC 42001 certification. Listed on AWS Marketplace (April 2026) and partnered with Recorded Future (July 2026).
  - Said: M&A to reach more than $200M ARR.
- **RunSybil:** said its continuous automated testing will replace scheduled, periodic pentests — [Fortune](https://fortune.com/2026/03/18/exclusive-ai-cybersecurity-startup-runsybil-founded-by-openais-first-security-hire-raises-40-million-led-by-khosla-ventures/)
- **AISLE:** done: credited CVEs, accepted fixes, autonomous remediation, on-premises and air-gapped deployment, then the sale to Cohere — [aisle.com](https://aisle.com); [AISLE blog](https://aisle.com/blog/aisle-discovers-20-openssl-zero-days-in-6-months)
- **depthfirst:** said it will train more security models in new domains and expand the research team; done: first in-house model — [SecurityWeek](https://www.securityweek.com/depthfirst-raises-80-million-in-series-b-funding/)
- **Trail of Bits:**
  - Said: "the expensive part of security work has moved". The advantage is "no longer in finding bugs, but everything after", meaning confirming, patching and coordinating disclosure. — [Trail of Bits, 22 Jun 2026](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/)
  - Done: open-sourced Buttercup (AIxCC 2nd), Patch the Planet with OpenAI, agent-built formal models in a zkVM audit (18 Sep 2026), patch and regression agent plugins (21 Oct 2026) and Codex backporting (2 Nov 2026) — [Trail of Bits blog index](https://blog.trailofbits.com/)
- **After AIxCC:** — [DARPA](https://www.darpa.mil/news/2025/aixcc-results); [Team Atlanta site](https://team-atlanta.github.io/); [Pulse 2.0](https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/)
  - DARPA required all finalist systems to be open-sourced.
  - Team Atlanta's site shows the win but no commercialisation, spin-off or Samsung deployment.
  - In May 2026 Samsung Ventures invested in XBOW and Samsung became XBOW's preferred reseller in South Korea.
- **Theori:** 3rd in AIxCC ($1.5M); company detail is out of scope — [DARPA](https://www.darpa.mil/news/2025/aixcc-results)
- **HackerOne:**
  - Done:
    - Hai Triage AI pre-screening launched in July 2025 — [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/)
    - Hai became a "multi-agent system for agentic security testing" — [The CyberSec Guru](https://thecybersecguru.com/analysis/what-happened-to-hackerone/)
    - New Community Member Terms took effect on 11 May 2026 (same source).
    - Internet Bug Bounty rewards were cut 76–89% and new submissions paused in May 2026 — [The Register, 21 May 2026](https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458)
  - Said: CEO Kara Sprague, 3 Nov 2026: "AI makes the crowd model stronger", but routine, pattern-based findings "will become harder to monetize". Humans keep the edge on business logic and chaining. — [Help Net Security, 3 Nov 2026](https://www.helpnetsecurity.com/?p=389850)
- **Bugcrowd:**
  - Said: automation layered into triage and signal detection (CEO Dave Gerry) (search snippet, [ChannelE2E](https://www.channele2e.com/news/bugcrowd-acquires-mayhem-security-to-advance-ai-augmented-offensive-testing))
  - Done:
    - Bought Mayhem in November 2025 — [Bugcrowd](https://www.bugcrowd.com/press-release/bugcrowd-acquires-mayhem-security/)
    - In March 2026 added identity verification, rate limiting, CAPTCHAs, a 30-day suspension after 10 consecutive rejections and permanent bans for automated spam — [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/)
- **Synack:** done: Sara AI Pentesting GA (8 May 2026), with human validation by the Synack Red Team, and the Glasswing-Readiness Assessment (13 Apr 2026) — [IT Brief](https://itbrief.co.nz/story/synack-launches-sara-ai-pentesting-for-wider-coverage); [Synack press release](https://www.bolsamania.com/nota-de-prensa_print/mercados/synack-launches-glasswing-readiness-assessment-to-close-the-ai-security-coverage-gap--22278365.html)
- **Cobalt:** — [Help Net Security](https://www.helpnetsecurity.com/2026/03/19/cobalt-continuous-pentesting-ai-capabilities/) (search snippet); [ChannelLife](https://channellife.news/story/cobalt-launches-autonomous-pentest-for-continuous-testing)
  - Done: AI continuous pentesting and MCP support (19 Mar 2026), and Autonomous Pentest GA in August 2026.
  - Said: human-led pentests remain better suited to compliance-driven and deeper work.
- **YesWeHack:** done: Agentic Pentest product, CNA status, EU Commission preferred provider and a first acquisition — [YesWeHack](https://www.yeswehack.com/community/yeswehack-report-2026-trends-security)
- **Immunefi:** said IMU pledges "power training data for Immunefi AI" (promotional) — [KuCoin](https://www.kucoin.com/blog/en-immunefi-ecosystem-2026-q1-update)
- **NCC Group:** — [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
  - Said: "While AI is expected to reshape aspects of cyber services, our view remains that it reinforces, rather than undermines, the need for independent, expert-led assurance". "Automation will continue to improve delivery efficiency in areas such as testing, analysis, and reporting".
  - Done:
    - Utilisation rose to 76% via the Manila delivery centre and AI.
    - Targets: about £25m of savings by FY28 against FY25, with £7m in FY26; mid-single-digit Cyber growth in FY27–28; mid-teens Cyber adjusted EBITDA margin by end-FY28.
    - Sold Escode.
    - "No current plans" for M&A.
  - Its principal risks include "technology changes render services obsolete" and reductions in its Technical Assurance business.
- **Regulation, transition (5):** the EU Cyber Resilience Act's mandatory vulnerability and incident reporting starts 11 Sep 2026. Actively exploited bugs must be reported within 24 hours, with penalties up to €15M or 2.5% of revenue. — [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/)
- **Verified software, transition (6):**
  - CodeMender "proactively rewrites existing code to remove entire vulnerability classes" — [Google DeepMind](https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/)
  - Trail of Bits used agents to build formal models during an audit — [Trail of Bits index](https://blog.trailofbits.com/)

### Inferences
- **(1) Billable hours → automation:** every human-crowd platform shipped an agentic product in 2026, but each keeps humans "in the loop" as the selling point. That protects price for now but caps margins.
  - NCC's North American Technical Assurance decline came from large tech clients, which are the most likely to automate in-house. That is the clearest early sign of transition (1) eating billable testing, though NCC does not say so.
- **(2) Triage → machine speed:** the bottleneck has moved from finding to fixing. Signs:
  - Glasswing's fewer than 1% fixed.
  - HackerOne's open valid reports up 131% (Section 6).
  - Trail of Bits' "everything after" framing.
  - Firms that close the loop (AISLE, Horizon3's planned blue-team agents, Pentera Resolve, CodeMender) are aimed at the right problem. Pure finders face falling value per finding.
- **(4) Gated models:** the risk is uneven.
  - XBOW and RunSybil test live systems and depend on frontier models without named access. Model makers' products currently target source code, not live environments, but the gap could close.
  - depthfirst's own-model approach and AISLE's sale to Cohere are two different hedges.
- **(6) Verified software:** no company in scope sells verified-by-construction software yet. It is a long-run threat to all "finders", and so far only Trail of Bits (formal methods) and Google have moved toward it.

### Gaps
- No company disclosed timing or budget for remediation agents (Horizon3's are "planned").
- No evidence of NCC deploying AI pentest tools at scale beyond utilisation claims.
- No 2025–26 statements found from Intigriti on AI policy or products.
- No commercial follow-up found for AIxCC finalists 4–7.

## 6. Pricing power: bounty payouts, pentest prices, budget shifts, programme closures and restrictions

### Takeaway
Bounty pricing is splitting into two tiers.
- Total crowd payouts are still rising: HackerOne paid $89.1M for July 2025–June 2026 and payouts rose 26% year on year in H1 2026.
- Top-end rewards are rising: Apple $2M, Google Titan M $1.5M, Microsoft $5M Zero Day Quest.
- Routine and open-source bounties are being cut or closed: curl (January 2026), Nextcloud (April 2026), HackerOne's Internet Bug Bounty cut 76–89% and paused (May 2026), Google's OSS VRP product reports paused (October 2026), and lower Chrome base rewards (May 2026).

I found no direct data on pentest day rates. The indirect evidence (flat Technical Assurance revenue at NCC, rapid ARR growth claims at automation vendors) points to budget shifting toward automation.

### Cited Findings
- **HackerOne totals:**
  - $89.1M paid for July 2025–June 2026 and 92,194 valid reports — [HackerOne report](https://www.hackerone.com/report)
  - Open valid reports up 131% from 2024 to 2026, with the critical open backlog up 123%.
  - 70% of security leaders say validated findings arrive faster than they can be fixed.
  - Valid AI-vulnerability reports up 222% in two years.
  - The previous year was $81M (+13%) — [HackerOne press release, Oct 2025](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy) (search snippet)
- **HackerOne CEO, 3 Nov 2026:** — [Help Net Security](https://www.helpnetsecurity.com/?p=389850)
  - Researcher payouts rose 26% year on year in H1 2026 and accelerated in Q3.
  - Programmes pay less for low-severity issues, duplicates and automatable findings.
  - Since January 2025, submissions are up 2.8x and valid reports 1.9x.
- **HackerOne March 2026 platform data:** 46,947 submissions (+76% year on year), about 25% valid, and critical or high at 32% of validated findings against a historical 26–28% — [The CyberSec Guru](https://thecybersecguru.com/analysis/what-happened-to-hackerone/)
- **Internet Bug Bounty cut:**

  | Severity | Old reward | New reward |
  |---|---|---|
  | Critical | $9,250 | $2,257 |
  | High | $4,429 | $1,009 |
  | Medium | $1,843 | $297 |
  | Low | $597 | $68 |

  - The new rates took effect on 18 May 2026 according to The Register, or 22 May according to LavX. The two sources conflict.
  - New submissions were paused. HackerOne said bounty levels "automatically adjust based on the contributions from active participating sponsors" and did not say whether AI reports were the cause. — [The Register, 21 May 2026](https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458); [LavX News, 21 May 2026](https://news.lavx.hu/article/hackerone-cuts-internet-bug-bounty-payouts-by-over-75-percent-amid-ai-driven-reporting-surge)
  - In the same piece, Daniel Stenberg said AI "slop" had given way to many good AI-assisted reports, and Linus Torvalds called the Linux security list "almost entirely unmanageable" because of duplicate AI-driven reports (The Register).
- **curl:** ended its bug bounty, run on HackerOne since 2019, at the end of January 2026, suspended from 1 Feb 2026, because of LLM-generated "AI slop". — [Hackaday, 26 Jan 2026](https://hackaday.com/2026/01/26/the-curl-project-drops-bug-bounties-due-to-ai-slop) The announcement was on 21 Jan 2026, and by mid-2025 about 20% of submissions were "AI slop" (search snippets, [The New Stack](https://thenewstack.io/drowning-in-ai-slop-reports-curl-ends-bug-bounties/)).
- **Nextcloud:** closed its bug bounty in April 2026, according to HackerOne's team updates page — [ForkLog, 24 Jul 2026](https://forklog.com/en/the-end-of-bug-bounties/)
- **Google OSS VRP:** paused new product-vulnerability submissions from 1 Oct 2026 until at least Q1 2027, citing floods of invalid and hallucinated reports. Patch Rewards and Cloud VRP remain open. — [Malwarebytes, Oct 2026](https://www.malwarebytes.com/blog/news/2026/10/google-pauses-open-source-bug-bounty-program-after-rise-in-ai-submissions); [BleepingComputer](https://bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge) (search snippets)
- **Intel:** reportedly launched an Intigriti programme with no bounties. Intel did not confirm that AI reports were the reason (search snippet in coverage of Google's pause; source article not retrieved).
- **Platform restrictions:** Bugcrowd's March 2026 controls and HackerOne's Hai Triage (July 2025) — [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/)
- **High-end rewards rising:** — [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/)
  - Microsoft Zero Day Quest: up to $5M in total (August 2025).
  - Apple: top reward raised from $1M to $2M (October 2025).
  - Google Titan M: from $1M to $1.5M (May 2026).
  - Google also cut base rewards for Chrome memory bugs to $500 and removed bonuses for simple read/write issues (May 2026).
- **Chrome full-chain:** Google paid its maximum of $250K to XBOW. The broker Crowdfense advertises up to $1.5M for comparable desktop Chrome chains (search snippet) — [CyberInsider](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/)
- **Immunefi:** Q1 2026 payouts of $7.87M against $2.40M in Q4 2025, with one $3M payout making up 38% of Q1 (promotional source) — [KuCoin](https://www.kucoin.com/blog/en-immunefi-ecosystem-2026-q1-update)
- **Pentest demand at NCC:** — [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
  - Technical Assurance revenue was flat (+0.2% at constant currency) in H1 FY26 year on year.
  - North America Cyber fell 11.3% at constant currency against H2 FY25, "driven by a reduction in Technical Assurance Services revenue from large technology clients".
  - NCC introduced "a more consistent approach to pricing and margin management".
  - Cyber gross margin rose 3.2 points to 38.4%.
- **Budget-shift indicators, all company claims:** — [Horizon3](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/); [Calcalist](https://www.calcalistech.com/ctechnews/article/ryvxvby21x); [IT Brief](https://itbrief.co.nz/story/synack-launches-sara-ai-pentesting-for-wider-coverage)
  - Horizon3 ARR +120%.
  - Pentera's average deal quadrupled to about $100K (March 2025).
  - Synack says Sara costs "a fraction" of a traditional pentest.
- **Vendor-sponsored surveys:**
  - 87% of organisations are planning, piloting or using agentic AI for pentesting (Synack/Omdia, March 2026) — [Synack/Omdia release](https://www.bolsamania.com/nota-de-prensa/mercados/95-of-enterprises-prioritize-pentesting-yet-only-32-of-attack-surfaces-are-tested-new-synack-and-omdia-research-finds--22105138.html) (search snippet)
  - 94% value humans in offensive security (Cobalt/Omdia) — [ChannelLife](https://channellife.news/story/cobalt-launches-autonomous-pentest-for-continuous-testing)
- **Trail of Bits:** the "expensive part" has moved from finding to confirming, patching and coordinating — [Trail of Bits](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/)

### Inferences
- **Value per finding:** it is falling for routine, automatable bugs and rising for deep chains and business-logic flaws. The crowd platforms' unit economics depend on the second group.
  - AI floods raise their triage costs, hence the AI triage and anti-spam controls.
  - Free or lightly funded open-source programmes are the first to close.
- **XBOW's Chrome economics:** a $250K reward against about $40K of compute is roughly 6x before human time. That shows elite findings can now be produced at a cost that undercuts human-only teams.
- **Day rates:** I have no direct evidence. NCC's flat Technical Assurance revenue at higher utilisation, combined with higher gross margin, suggests it is holding price for now by moving to "higher-value" work. Volume is the weak spot, especially with large tech clients.

### Gaps
- No published UK, EU or US pentest day-rate series for 2025–26, whether from CREST, a survey or a procurement framework.
- No data on the share of budget moving from human to automated testing beyond vendor surveys.
- Not verified:
  - The Dark Reading "Vulnpocalypse is repricing the bug bounty economy" piece (403).
  - A report that "HackerOne halted new submissions" (page unavailable). This is likely a conflation with the Internet Bug Bounty pause.
  - Intel's Intigriti programme details.

## 7. Financial strength: burn, profitability, layoffs; NCC Group detail

### Takeaway
Among the private firms, only Pentera has made a profitability claim ("approaching breakeven", March 2025). The others are funded on large raises:
- Horizon3: $428.5M in total.
- XBOW: about $272M, with 250+ staff.
- depthfirst: $120M.

The only crowd-platform layoffs I found are HackerOne's 12% in 2023.

NCC Group has become a smaller company with net cash:
- FY26 (to 30 Sep 2026): Cyber revenue about £235m (+3.7% at constant currency), Cyber adjusted EBITDA £16.3m (6.9% margin), year-end net cash about £53m. That is after £210m of buyback and tender returns.
- Statutory Cyber profitability is thin. Margins sit well below the FY28 target of mid-teens.

### Cited Findings
- **Pentera:** "approaching breakeven", about 400 employees, targeting $200M revenue and profitability within about 2.5 years [company claim, unconfirmed] (12 Mar 2025) — [Calcalist](https://www.calcalistech.com/ctechnews/article/ryvxvby21x)
- **Horizon3:** profitability not disclosed — [Horizon3 press release](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/). $428.5M raised in total — [Help Net Security](https://www.helpnetsecurity.com/2026/08/03/horizon3-ai-250-million-funding/) (search snippet)
- **XBOW:**
  - More than 250 employees (May 2026) — [Pulse 2.0](https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/)
  - About $272M raised — [Multiples.vc](https://multiples.vc/private-comps/xbow)
  - The Chrome campaign used about $40K of compute in six days — [CyberInsider](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/)
- **HackerOne:** cut about 12% of staff in August 2023 — [Axios, 4 Aug 2023](https://www.axios.com/2023/08/04/hackerone-layoffs-12-percent-workforce) (search snippet). I found no confirmed 2026 layoffs (search snippet).
- **Synack, Immunefi:** I found no layoffs or new rounds in 2026 (search snippets).
- **NCC Group, H1 FY26 (to 31 Mar 2026; published 11 Jun 2026):** — [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
  - Group revenue was £151.3m (+5.0% at constant currency excluding Fox Crypto; −3.5% reported).
  - Cyber gross margin was 38.4% and Escode's was 72.9%.
  - Group adjusted EBITDA was £23.5m (+27.7%). Cyber, including central costs, was £8.3m (7.0% margin, up from 3.2%) and Escode was £15.2m.
  - Group operating profit was £11.9m. The Cyber-plus-central operating line was a £1.2m loss.
  - Profit before tax was £10.7m, adjusted EPS 4.5p and basic EPS 2.6p. Cash conversion was 79.1%.
  - Net debt excluding leases was £10.2m at 31 March. Net cash was about £230m on 1 Jun 2026, after Escode.
  - Facilities were resized to £30m, to be refinanced within six months. The interim dividend was held at 1.50p, and the policy will be reset after the tender.
  - The £40m buyback (announced 21 Jan 2026) was completed on 17 Apr 2026, and a £170m tender plus £15m buyback was announced.
  - North American gross margin improved through "headcount reductions".
- **NCC Group, FY25 (to 30 Sep 2025; published 11 Dec 2025):** — [AJ Bell, 11 Dec 2025](https://www.ajbell.co.uk/news/articles/ncc-reports-decline-full-year-sales-one-offs-boost-profitability)
  - Revenue £305.4m (−7.2%) and adjusted EBITDA £43.7m (−12%), both including Escode.
  - Profit before tax £20.6m, helped by an £11.4m gain on Fox Crypto.
  - Net cash excluding leases £13.1m, against net debt of £45.3m a year earlier. Final dividend held at 3.15p.
  - Continuing-operations revenue was £238.9m — [MarketScreener](https://www.marketscreener.com/news/ncc-group-plc-reports-earnings-results-for-the-full-year-ended-september-30-2025-ce7d50dad08bf322) (search snippet; consistent with Escode being reported as discontinued)
  - NCC's financial year now ends on 30 September; it previously ended in May — [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
- **NCC Group, FY26 trading update (27 Oct 2026):** — [Sharecast/HL, 27 Oct 2026](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations)
  - Group revenue in line with expectations, and adjusted EBITDA ahead.
  - Cyber revenue about £235m and Cyber adjusted EBITDA £16.3m (6.9% margin).
  - Gross margin a record 38.4%, up 1.8 points.
  - Year-end net cash about £53m.
  - The £170m tender completed in August, and 35% of the £15m buyback was executed by year-end.
  - FY27 outlook unchanged; the cost programme is "on track".
- **NCC Group concentration:** North American exposure to large technology clients is expected to fall to about 23% in FY26. UK & APAC is 62% of H1 Cyber revenue. — [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)

### Inferences
- **NCC return on capital:** with about £16m of Cyber EBITDA and a negative statutory Cyber operating line in H1, return on capital in the remaining business is low. The equity story rests on the £25m cost plan and on whether hourly assurance revenue holds up.
  - The net cash of about £53m and the £30m facility give a buffer, not a war chest.
- **Private finders' burn:** likely heavy (staff plus model compute). The XBOW and RunSybil models need continuing access to expensive frontier inference. Horizon3's and Pentera's scale and Pentera's near-breakeven claim make them the sturdiest of the private group, if the claims are true.

### Gaps
- No audited financials for any private company.
- No burn figures.
- NCC's FY26 audited results, including the Escode gain, were not yet published as of 12 Nov 2026. The trading update gave no FY26 statutory figures.
- NCC's return on capital and free cash flow for FY26 are not yet disclosed.

## 8. Entry-point data: private marks, implied multiples, exposure routes; NCC Group and listed peers

### Takeaway
**NCC Group** at 156.8p (12 Nov 2026) has a market cap of about £236m.
- My estimate of EV is about £183m on FY26 net cash of about £53m. That gives roughly 0.8x FY26 Cyber revenue and about 11x FY26 Cyber adjusted EBITDA.
- If the FY28 margin target were met, the multiple would be roughly 5x.
- That is cheap on sales and not cheap on current EBITDA. My suggested label is **fair**, contingent on execution.

**Private AI-native firms:**
- Pentera: about 10x ARR at a stale 2025 mark.
- XBOW (more than $1B) and Horizon3 (more than $2B): the ARR multiple cannot be computed because ARR is not disclosed.
- Outside investors have only indirect access, through listed corporate investors where the stake is a small part of their value, or through the IMU token for Immunefi.

### Cited Findings
- **NCC price and multiples, 12 Nov 2026:** — [Stockanalysis NCC statistics](https://stockanalysis.com/quote/lon/NCC/statistics/)
  - Price 156.80p and market cap £235.87m on 150.43M shares.
  - Stockanalysis shows EV of £285.17m, built on stale net debt of £49.3m: £9.6m cash and £58.9m debt, which appears to be the 31 Mar 2026 balance sheet.
  - Trailing P/E 52.8x and forward P/E 24.7x. EV/Sales 1.21x on that stale EV. EV/FCF 7.7x.
  - Dividend yield 2.97%, which matches the FY25 4.65p of dividends; that payout is to be reset.
- **NCC price history:**
  - Year-end market caps were £723.3m (2021), £624.0m (2022), £402.7m (2023), £462.0m (2024) and £427.0m (2025). The current figure is £235.9m, down 47.5% in a year after the capital returns. — [Stockanalysis NCC market cap](https://stockanalysis.com/quote/lon/NCC/market-cap/)
  - Daily closes from 4 Sep to 12 Nov 2026 ranged from a low of 125.40p (9 Sep 2026) to a high of 174.40p (26 Oct 2026) — [Stockanalysis NCC history](https://stockanalysis.com/quote/lon/NCC/history/)
  - The shares were 139.00p on 11 Jun 2026, when the market cap was £392.9m; they were down 15% over 12 months — [AJ Bell](https://www.ajbell.co.uk/news/articles/ncc-decides-remain-london-listed-pure-play-cyber-security-firm)
  - They were 171p on 27 Oct 2026 after the trading update — [Sharecast/HL](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations)
- **Listed peers, 12 Nov 2026:**

  | Company | Market cap | EV | EV/Sales | EV/EBITDA | EV/FCF | P/E (trailing / forward) | Other |
  |---|---|---|---|---|---|---|---|
  | Rapid7 (US; products plus services) | $1.01B | $1.24B | 1.46x trailing | 17.5x | 8.9x | 71.2x / 7.8x | net debt $226M |
  | Wavestone (France; consulting) | €868m | €768m | 0.81x | 5.5x | 5.9x | 10.6x / 9.7x | net cash €101m, yield 1.41% |
  | TAC Infosec (India; NSE: TAC) | INR 8.29bn | INR 8.10bn | 14.5x | 27.3x | | 37.1x trailing | net cash INR 243m |

  — [Stockanalysis RPD](https://stockanalysis.com/stocks/rpd/statistics/); [Stockanalysis WAVE](https://stockanalysis.com/quote/epa/WAVE/statistics/); [Stockanalysis TAC](https://stockanalysis.com/quote/nse/TAC/statistics/)
- **NCC near-term references:**
  - Board targets: mid-single-digit Cyber growth in FY27 and FY28, about £25m of savings by FY28 and a mid-teens Cyber adjusted EBITDA margin by end-FY28 — [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
  - FY27 outlook unchanged as of 27 Oct 2026 — [Sharecast/HL](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations)
  - The FY25 results came out on 11 Dec 2025 — [AJ Bell](https://www.ajbell.co.uk/news/articles/ncc-reports-decline-full-year-sales-one-offs-boost-profitability)
- **Private marks:**
  - XBOW: more than $1B (March 2026) — [FinTech Global](https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/); Dealroom estimates $1–2.5B (search snippet) — [Dealroom](https://dealroom.co/companies/xbow/)
  - Horizon3: more than $2B (August 2026) — [Horizon3](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/)
  - Pentera: about $1B (March 2025), shown as 10.0x revenue on $100M — [Multiples.vc](https://multiples.vc/private-comps/pentera)
  - Bugcrowd: "nearly doubled" from more than $1B [company claim, unconfirmed] (search snippet)
  - Not disclosed: RunSybil, depthfirst, ZeroPath, HackerOne, Synack, Cobalt, YesWeHack, Intigriti, Picus and Cymulate.
- **Exposure routes through listed investors:**
  - XBOW: Sofina (Series C) — [FinTech Global](https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/); Accenture Ventures, NVentures (NVIDIA), Samsung Ventures, SentinelOne S Ventures and Liberty Global Tech Ventures — [Pulse 2.0](https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/)
  - Horizon3: Qualcomm Ventures, SAIC and Prosperity7 (existing), plus EDBI (Singapore) — [Horizon3](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/)
  - Pentera: Blackstone, Insight, Evolution, K1 and Farallon — [Multiples.vc](https://multiples.vc/private-comps/pentera)
  - YesWeHack: Wendel led the Series C (search snippet) — [Presse-Citron](https://www.presse-citron.net/french-tech-qui-est-yeswehack-la-start-up-de-hackeurs-ethiques-qui-a-conquis-le-cac40/)
  - Picus: Mastercard joined the Series B — [Picus](https://www.picussecurity.com/about-us)
  - RunSybil: Anthropic's Anthology Fund — [Fortune](https://fortune.com/2026/03/18/exclusive-ai-cybersecurity-startup-runsybil-founded-by-openais-first-security-hire-raises-40-million-led-by-khosla-ventures/)
  - Immunefi: the IMU token trades on Coinbase, KuCoin, Bybit and others. The page's own token valuation figures (market cap about $2.15M, FDV about $25M) look inconsistent and are unreliable. — [KuCoin](https://www.kucoin.com/blog/en-immunefi-ecosystem-2026-q1-update)
  - AISLE: no longer separately investable; it is inside Cohere, which is private — [aisle.com](https://aisle.com)
- **IPO plans:** none announced for XBOW, Horizon3 or Pentera in the sources reviewed. Pentera's April 2026 CFO hire is the only finance-build signal I saw — [Pentera site](https://pentera.io/?p=762) (search snippet).

### Inferences
- **NCC EV and multiples (my arithmetic):**
  - EV ≈ £235.9m market cap − about £53m FY26 net cash ≈ £183m, excluding leases and the rest of the £15m buyback.
  - EV/FY26 Cyber revenue ≈ 0.78x and EV/FY26 Cyber adjusted EBITDA ≈ 11.2x.
  - At FY28 targets, roughly £255–260m of revenue at a 14–16% margin gives about £36–41m of EBITDA, so EV/EBITDA ≈ 4.5–5x.
  - The price therefore implies heavy discounting of the margin plan, or an expectation that AI will erode hourly Technical Assurance volume.
- **NCC against peers:**
  - Against Wavestone (5.5x EV/EBITDA, about 10x P/E), NCC looks expensive on current earnings.
  - Against Rapid7 (1.46x EV/Sales), NCC looks cheap on sales.
  - Against its own history, the market cap is about a third of end-2021. Most of that gap reflects disposals and roughly £210m returned in 2026, so per-share comparisons need the share-count history.
  - Rough check: the market cap fell from £392.9m at 139p (about 283m shares, June 2026) to 150.4m shares by November. That implies the £170m tender bought about 128–132m shares at about 130p. I did not retrieve the tender circular, so this is approximate.
- **NCC entry conditions:**
  - Improves if: FY26 audited results (likely around December 2026, by analogy with 11 Dec 2025) confirm the £16.3m and net cash; the new CEO keeps the cost plan; Technical Assurance stabilises despite automation; or the price falls back toward the September 2026 low (~125p).
  - Worsens if: the dividend reset is deep, or North America keeps shrinking.
  - Bid interest is a wildcard. The board said in June 2026 that there were no approaches.
- **Private AI-native multiples:**
  - Pentera: about 10x on $100M ARR.
  - XBOW and Horizon3: multiples cannot be assessed. Horizon3's valuation tripled while ARR grew 2.2x, so its multiple expanded.
  - Outside access: retail or listed investors get only diluted exposure. Sofina and Wendel are the closest listed vehicles, and the stakes are small relative to their portfolios.

### Gaps
- No 5-year NCC P/E or EV/EBITDA history, and no consensus forward EV/EBITDA. The tools I could reach did not provide them.
- No secondary-market prices (Caplight or Forge pages exist but were not read).
- The size of listed investors' stakes is unknown.
- No Israeli listed pure-play testing firm identified. Indian listed peer TAC Infosec was not assessed for business quality, and neither was Wavestone's cyber share.

## 9. Per-company scorecard, companies considered and excluded, and dated source list

### Takeaway
The best positions belong to automation that proves exploitability or ships accepted fixes against an outside judge.
- **Leaders:** Horizon3 and Pentera (in-environment exploit validation, with FedRAMP High at Horizon3), XBOW (vendor-confirmed Chrome reward) and AISLE (now Cohere).
- **Weakest:** labour-heavy testers (NCC, Trail of Bits as a business model) and the crowd platforms, whose routine-finding economics AI is eroding.
- **Evidence of lead:** mostly company-reported, apart from AIxCC, the Google reward, OpenSSL credits and the Berkeley map.
- **Entry:** cannot be assessed for most private firms. NCC Group is "fair".

### Cited Findings
Dated source list (all accessed 12 Nov 2026; "(snippet)" = search-result summary only):
- **AIxCC and model makers:**
  - DARPA AIxCC results, 8 Aug 2025 — https://www.darpa.mil/news/2025/aixcc-results
  - Anthropic Project Glasswing, launched 7 Apr 2026 and updated 6 Oct 2026 — https://www.anthropic.com/glasswing
  - Implicator, Glasswing expansion, 2 Jun 2026 — https://www.implicator.ai/anthropic-adds-150-new-project-glasswing-partners-in-more-than-15-countries/
  - Anthropic, Claude Code Security, 20 Feb 2026 — https://www.anthropic.com/news/claude-code-security
  - OpenAI Aardvark / Codex Security, 6 Mar 2026 update (snippet) — https://openai.com/index/introducing-aardvark
  - The Hacker News on Codex Security, Mar 2026 (snippet) — https://thehackernews.com/2026/03/openai-codex-security-scanned-12.html
  - GovInfoSecurity on OpenAI TAC, 2026 (snippet) — https://www.govinfosecurity.com/openai-courts-banks-in-trusted-access-for-cyber-partner-push-a-31447
  - SecurityBrief UK on TAC (snippet) — https://securitybrief.co.uk/story/openai-launches-trusted-access-for-cyber-with-major-names
  - Help Net Security on GPT-5.4-Cyber, Apr 2026 (snippet) — https://www.helpnetsecurity.com/?p=366217
  - Google DeepMind CodeMender, 6 Oct 2025 — https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
  - Cohere blog, AISLE LOI post 15 Oct 2026 — https://cohere.com/blog
- **XBOW:**
  - FinTech Global, Series C, 19 Mar 2026 — https://fintech.global/2026/03/19/xbow-raises-120m-series-c-to-scale-autonomous-hacker/
  - Law360, 18 Mar 2026 (snippet) — https://www.law360.co.uk/articles/2454426
  - Pulse 2.0, Series C extension, 7 May 2026 — https://pulse2.com/xbow-35-million-added-to-series-c-to-expand-autonomous-offensive-security-platform/
  - Multiples.vc XBOW — https://multiples.vc/private-comps/xbow
  - XBOW blog, Series B (round June 2025) — https://xbow.com/blog/series-b
  - XBOW blog, "Top 1", 24 Jun 2025 — https://xbow.com/blog/top-1-how-xbow-did-it/
  - Gigazine, 25 Jun 2025 — https://www.gigazine.net/gsc_news/en/20250625-hackerone-xbow
  - Bloomberg, 24 Jun 2025 (snippet) — https://www.bloomberg.com/news/articles/2025-06-24/one-of-the-best-hackers-in-the-country-is-an-ai-bot
  - Utku Sen Substack, 25 Jun 2025 — https://utkusen.substack.com/p/does-xbow-ai-hacker-deserve-the-hype
  - God Access Substack, Aug 2025 — https://godaccess.substack.com/p/behind-the-hype-is-xbow-ai-really-the-game-changer
  - CyberInsider, 14 Oct 2026 — https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/
  - CSO Online, 16 Oct 2026 — https://www.csoonline.com/article/4236599/xbow-spent-40k-on-ai-and-cracked-google-chrome-wide-open-2.html
  - Let's Data Science (snippet) — https://letsdatascience.com/news/google-awards-xbow-250000-for-chrome-exploit-chain-cf47fed1
  - Dealroom (snippet) — https://dealroom.co/companies/xbow/
- **Horizon3:**
  - Horizon3 press release, 3 Aug 2026 — https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/
  - Help Net Security, 3 Aug 2026 (snippet) — https://www.helpnetsecurity.com/2026/08/03/horizon3-ai-250-million-funding/
  - Business Wire, 13 Jan 2026 (snippet) — https://www.businesswire.com/news/home/20260113598188/en/Horizon3.ai-Secures-Investment-from-Prosperity7-Ventures-to-Protect-AI-Datacenters-and-Critical-Infrastructure
  - Business Wire, 19 Mar 2026 (snippet) — https://www.businesswire.com/news/home/20260319233634/en/
  - Bernama, Series D, Jun 2025 (snippet) — https://mrem.bernama.com/viewsm.php?idm=51282
- **Pentera:**
  - Calcalist/CTech, 12 Mar 2025 — https://www.calcalistech.com/ctechnews/article/ryvxvby21x
  - TechIntelPro, 7 Jan 2026 — https://techintelpro.com/news/cybersecurity/ai/pentera-hits-100m-arr-as-first-aev-centaur-company
  - Multiples.vc Pentera — https://multiples.vc/private-comps/pentera
  - Pentera site (snippet) — https://pentera.io/?p=762
  - TechStackIPO (snippet) — https://www.techstackipo.com/company/pentera-security
- **Other AI-native firms:**
  - Fortune, RunSybil, 18 Mar 2026 — https://fortune.com/2026/03/18/exclusive-ai-cybersecurity-startup-runsybil-founded-by-openais-first-security-hire-raises-40-million-led-by-khosla-ventures/
  - aisle.com, "Goodbye AISLE, Hello Cohere Cyber", 10 Nov 2026 — https://aisle.com
  - AISLE blog, 24 Apr 2026 — https://aisle.com/blog/aisle-discovers-20-openssl-zero-days-in-6-months
  - Lupa.cz, 1 Jun 2026 — https://www.lupa.cz/aktuality/cesky-aisle-je-podle-berkeley-nejlepsi-ai-v-hledani-zranitelnosti-predstihl-anthropic-google-i-microsoft/
  - The Next Web, Jun 2026 (snippet) — https://thenextweb.com/news/aisle-snapshot-on-prem-vulnerability-detection-regulated-enterprises
  - Zeltser, ZeroPath, Mar 2026 — https://zeltser.com/media/rsac-2026-sandbox/zeropath
  - ToolRadar (snippet) — https://toolradar.com/companies/zeropath-com
  - TechCrunch, depthfirst, 14 Jan 2026 — https://techcrunch.com/2026/01/14/ai-security-firm-depthfirst-announces-40-million-series-a
  - SecurityWeek, depthfirst, 1 Apr 2026 — https://www.securityweek.com/depthfirst-raises-80-million-in-series-b-funding/
  - Trail of Bits, Patch the Planet, 22 Jun 2026 — https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
  - Trail of Bits blog index (posts to 2 Nov 2026) — https://blog.trailofbits.com/
  - Team Atlanta site — https://team-atlanta.github.io/
  - Cymulate About — https://cymulate.com/about-us/
  - Picus About — https://www.picussecurity.com/about-us
  - Picus press releases (2026) — https://www.picussecurity.com/press-releases
- **Platforms:**
  - HackerOne Security Research Report 2026 (Jul 2025–Jun 2026 data) — https://www.hackerone.com/report
  - HackerOne press release, Oct 2025 (snippet) — https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy
  - Help Net Security, HackerOne CEO, 3 Nov 2026 — https://www.helpnetsecurity.com/?p=389850
  - The Register, 21 May 2026 — https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458
  - LavX, 21 May 2026 — https://news.lavx.hu/article/hackerone-cuts-internet-bug-bounty-payouts-by-over-75-percent-amid-ai-driven-reporting-surge
  - The CyberSec Guru, 2026 — https://thecybersecguru.com/analysis/what-happened-to-hackerone/
  - Axios, 4 Aug 2023 (snippet) — https://www.axios.com/2023/08/04/hackerone-layoffs-12-percent-workforce
  - Bugcrowd press release, 4 Nov 2025 — https://www.bugcrowd.com/press-release/bugcrowd-acquires-mayhem-security/
  - Help Net Security, 4 Nov 2025 — https://www.helpnetsecurity.com/2025/11/04/bugcrowd-mayhem-security-acquisition/
  - Pulse 2.0, Bugcrowd $102M (snippet) — https://pulse2.com/bugcrowd-102-million-funding/
  - BankInfoSecurity, Informer (snippet) — https://www.bankinfosecurity.com/bugcrowd-buys-informer-to-enhance-attack-surface-management-a-25314?web_view=true
  - Business News Australia (snippet) — https://www.businessnewsaustralia.com/articles/bugcrowd-unites-hacker-community-with-mayhem-security-acquisition.html
  - ChannelE2E (snippet) — https://www.channele2e.com/news/bugcrowd-acquires-mayhem-security-to-advance-ai-augmented-offensive-testing
  - IT Brief, Synack Sara, 8 May 2026 — https://itbrief.co.nz/story/synack-launches-sara-ai-pentesting-for-wider-coverage
  - Synack Glasswing-Readiness press release, 13 Apr 2026 — https://www.bolsamania.com/nota-de-prensa_print/mercados/synack-launches-glasswing-readiness-assessment-to-close-the-ai-security-coverage-gap--22278365.html
  - Synack/Omdia, Mar 2026 (snippet) — https://www.bolsamania.com/nota-de-prensa/mercados/95-of-enterprises-prioritize-pentesting-yet-only-32-of-attack-surfaces-are-tested-new-synack-and-omdia-research-finds--22105138.html
  - CB Insights Synack (snippet) — https://www.cbinsights.com/company/synack
  - ChannelLife, Cobalt, 24 Jul 2026 — https://channellife.news/story/cobalt-launches-autonomous-pentest-for-continuous-testing
  - Help Net Security, Cobalt, 19 Mar 2026 (snippet) — https://www.helpnetsecurity.com/2026/03/19/cobalt-continuous-pentesting-ai-capabilities/
  - Cobalt Series B blog (snippet) — https://www.cobalt.io/blog/q-and-a-with-cobalts-ceo-and-cso-about-securing-series-b-funding
  - YesWeHack Report 2026 page, 5 Feb 2026 — https://www.yeswehack.com/community/yeswehack-report-2026-trends-security
  - Presse-Citron (snippet) — https://www.presse-citron.net/french-tech-qui-est-yeswehack-la-start-up-de-hackeurs-ethiques-qui-a-conquis-le-cac40/
  - Intigriti Series B (snippet) — https://www.intigriti.com/blog/news/intigriti-secures-more-than-21-million-series-b-funding
  - Bitscale Intigriti (snippet) — https://bitscale.ai/directory/intigriti
  - KuCoin, Immunefi Q1 2026 (promotional) — https://www.kucoin.com/blog/en-immunefi-ecosystem-2026-q1-update
- **Programme closures and pricing:**
  - ForkLog, 24 Jul 2026 — https://forklog.com/en/the-end-of-bug-bounties/
  - Hackaday, 26 Jan 2026 — https://hackaday.com/2026/01/26/the-curl-project-drops-bug-bounties-due-to-ai-slop
  - The New Stack (snippet) — https://thenewstack.io/drowning-in-ai-slop-reports-curl-ends-bug-bounties/
  - Malwarebytes, Oct 2026 (snippet) — https://www.malwarebytes.com/blog/news/2026/10/google-pauses-open-source-bug-bounty-program-after-rise-in-ai-submissions
  - BleepingComputer (snippet) — https://bleepingcomputer.com/news/google/google-halts-open-source-bug-bounty-program-amid-ai-spam-surge
- **NCC Group and peers:**
  - NCC interim results RNS, 11 Jun 2026 — https://www.investegate.co.uk/announcement/rns/ncc-group--ncc/unaudited-interim-results/9612591
  - NCC interims full PDF — https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf
  - AJ Bell, 11 Jun 2026 — https://www.ajbell.co.uk/news/articles/ncc-decides-remain-london-listed-pure-play-cyber-security-firm
  - AJ Bell, 11 Dec 2025 — https://www.ajbell.co.uk/news/articles/ncc-reports-decline-full-year-sales-one-offs-boost-profitability
  - Sharecast via HL, 27 Oct 2026 — https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations
  - Verdict (snippet) — https://www.verdict.co.uk/ncc-group-sale-escode-tdr/
  - MarketScreener (snippet) — https://www.marketscreener.com/news/ncc-group-plc-reports-earnings-results-for-the-full-year-ended-september-30-2025-ce7d50dad08bf322
  - Stockanalysis NCC statistics, market cap and history, 12 Nov 2026 — https://stockanalysis.com/quote/lon/NCC/statistics/ ; https://stockanalysis.com/quote/lon/NCC/market-cap/ ; https://stockanalysis.com/quote/lon/NCC/history/
  - Stockanalysis Rapid7, Wavestone and TAC Infosec, 12 Nov 2026 — https://stockanalysis.com/stocks/rpd/statistics/ ; https://stockanalysis.com/quote/epa/WAVE/statistics/ ; https://stockanalysis.com/quote/nse/TAC/statistics/

### Inferences
**Per-company scorecard.** This is my judgement on the cited evidence. Test (a) position, (b) lead from outside evidence only, (c) revenue model, (d) financial strength, (e) resilience across the three scenarios: steady growth ~55%, a financing-led pause ~2028 ~25%, faster acceleration ~20%.

**XBOW (US, private)**
- **(a) Position: strong but contestable.**
  - Autonomous live-application exploitation with built-in validators. A working exploit is a fast and final judge.
  - It is a finder, not a fixer.
  - It runs on public frontier models (GPT-5.6 Sol), with no named gated access.
- **(b) Lead: moderate to strong.**
  - Google's $250K Chrome reward (approved 31 Aug 2026).
  - HackerOne US #1 in Q2 2025, but VDP-heavy and 3rd by August 2025.
  - Behind AISLE on the Berkeley map. No analyst rankings.
- **(c) Revenue model:** subscription platform, no disclosed labour share; bounty income is immaterial.
- **(d) Financial strength:** unknown. About $272M raised and 250+ staff, burn undisclosed.
- **(e) Resilience:**
  - Steady scenario: it grows with strategic channels (Accenture, Samsung).
  - Pause: high-burn and valuation-reset risk.
  - Acceleration: model makers' agents could commoditise live-application testing.
  - Low export-control exposure as a US firm on US models.
- **Path: coherent.** Transitions (1), (2) and (4). Funded, with outside proof of capability. What must go right: it must keep a lead over model makers' own agents and add remediation.
- **Entry:** last mark more than $1B (March 2026), plus the $35M extension (May 2026). ARR undisclosed, so no multiple. No IPO plan. Exposure is via Sofina or strategic investors' parents. **Cannot assess.**

**Horizon3.ai (US, private)**
- **(a) Position: strong.**
  - In-production exploitation and verification across customer networks.
  - FedRAMP High is a regulatory constraint AI cannot remove [company claim].
  - Planned blue-team remediation agents.
- **(b) Lead: moderate.**
  - Customer scale (7,000+ organisations, four Fortune 10) and FedRAMP are company-stated.
  - Investor step-ups. No independent benchmark.
- **(c) Revenue model:** recurring subscription. ARR +120% (company claim).
- **(d) Financial strength:** well-funded ($428.5M raised). Profitability undisclosed.
- **(e) Resilience:**
  - Steady scenario: strong.
  - Pause: the August 2026 cash should bridge.
  - Acceleration: demand for validation grows, but agentic attackers and defenders raise the bar.
  - It is expanding into Singapore and Australia; export-control exposure is low.
- **Path: coherent.** Transitions (1), (2) and (5). Funded; the remediation agents are "said, not done".
- **Entry:** more than $2B (3 Aug 2026), with no ARR base. The valuation tripled in about 14 months. Exposure via Qualcomm, SAIC and Prosperity7. **Cannot assess.**

**Pentera (Israel/US, private)**
- **(a) Position: strong to medium.** In-environment exploit validation, plus remediation (Resolve). It added human services, which is a partial reversion to labour.
- **(b) Lead: moderate.**
  - First exposure-validation vendor past $100M ARR, by its own claim.
  - QKS SPARK Matrix Leader.
  - No independent effectiveness data.
- **(c) Revenue model:** recurring; average deal about $100K (March 2025). A services line was added, share undisclosed.
- **(d) Financial strength:** best evidence in the group, "approaching breakeven" in March 2025 [company claim].
- **(e) Resilience:**
  - Pause: resilient, since it is near breakeven.
  - Acceleration: risk of being leapfrogged by LLM-native attack depth.
  - Israeli headquarters adds geopolitical and export-regime exposure (my inference).
- **Path: coherent.** Transitions (1) and (2). M&A to $200M ARR is funded only modestly.
- **Entry:** about $1B (March 2025), about 10x ARR on $100M (January 2026). No IPO announced; a CFO was hired in April 2026. **Fair (stale mark, illiquid).**

**RunSybil (US, private)**
- **(a) Position: medium.** Black-box live-application testing with an exploit-proof judge. Dependent on frontier models, with no named programme; Anthropic's fund is an investor.
- **(b) Lead: weak.** Named AI-company customers only.
- **(c) Revenue model:** continuous subscription (my inference).
- **(d) Financial strength:** $40M raised (March 2026); early stage.
- **(e) Resilience:** fragile in a pause, and exposed to model makers in acceleration.
- **Path: partly coherent.** The thesis matches transition (1), but the evidence is thin.
- **Entry:** valuation undisclosed. **Cannot assess.**

**AISLE, now Cohere Cyber (owner Cohere)**
- **(a) Position: strong.** It finds and fixes against an outside judge: CVE credits and maintainer-accepted patches. It now sits inside a model maker, which removes the gated-model dependence (on Cohere's models).
- **(b) Lead: strong.** OpenSSL credits (20 CVEs, 10 fixes) and #1 on the Berkeley map (June 2026).
- **(c) Revenue model:** enterprise platform plus one-off Snapshot audits; mix unknown.
- **(d) Financial strength:** undisclosed; now Cohere's balance sheet.
- **(e) Resilience:** tied to Cohere's financing. "Sovereign" positioning helps where US-model access is unequal.
- **Path: coherent as a capability.** The independent path ended with the sale, which is itself a transition (4) signal.
- **Entry:** acquired 10 Nov 2026, terms undisclosed. **Cannot assess / not investable.**

**ZeroPath (US, private)**
- **(a) Position: weak to medium.** AI-native SAST with autofix, competing head-on with Claude Code Security and Codex Security. The judge (static findings plus patch review) is weaker than live exploitation.
- **(b) Lead: weak to moderate.** RSAC 2026 finalist and curl-maintainer endorsement; customer claims unverified.
- **(c) Revenue model:** per-developer seat pricing.
- **(d) Financial strength:** small; about $7M seed.
- **(e) Resilience:** low across all three scenarios.
- **Path: partly coherent.**
- **Entry: cannot assess.**

**depthfirst (US, private)**
- **(a) Position: medium.** Own models (dfs-mini1) reduce gated-model dependence. The judge is unclear (smart-contract focus).
- **(b) Lead: weak.** Partnerships only; no CVEs or benchmarks found.
- **(c) Revenue model:** platform (my inference).
- **(d) Financial strength:** $120M raised (January–April 2026).
- **(e) Resilience:** funded to ride out a pause. Own-model training could fall behind in acceleration.
- **Path: partly coherent.**
- **Entry:** valuation undisclosed. **Cannot assess.**

**Trail of Bits (US, private consultancy)**
- **(a) Position: weak business model, strong capability.** Billable audits, but with direct OpenAI access (GPT-5.5-Cyber). Formal-methods skill fits transition (6).
- **(b) Lead: strong.** AIxCC 2nd ($3M) and the OpenAI partnership.
- **(c) Revenue model:** mostly services (my inference; no disclosures).
- **(d) Financial strength:** unknown.
- **(e) Resilience:** labour model at risk in acceleration. Its "everything after finding" niche (triage, patching, coordination) is where demand is moving.
- **Path: partly coherent.** It open-sourced Buttercup, so it captures no product value; it adapts as an AI-amplified services firm.
- **Entry: not investable.**

**Cymulate (Israel, private)**
- **(a) Position: medium.** Breach-and-attack simulation / exposure validation (control validation) plus agentic "Cowork". It could be bundled away by platform vendors.
- **(b) Lead: weak to moderate.** Gartner Peer Insights and Frost; customer claim of 1000+.
- **(c) Revenue model:** subscription.
- **(d) Financial strength:** unknown.
- **(e) Resilience:** medium. Israeli exposure.
- **Path: partly coherent.**
- **Entry: cannot assess.**

**Picus Security (Turkey/US, private)**
- **(a) Position: medium.** Breach-and-attack-simulation pioneer with "post-Mythos" exposure validation. Mastercard OEM distribution is a modest moat.
- **(b) Lead: moderate.** Gartner Peer Insights Customers' Choice, Frost Radar Innovation Leader 2026 and G2 #1.
- **(c) Revenue model:** subscription.
- **(d) Financial strength:** $80M raised. Profitability unknown.
- **(e) Resilience:** medium. Possible unequal access to gated US models (my inference).
- **Path: partly coherent.**
- **Entry: cannot assess.**

**HackerOne (US, private)**
- **(a) Position: medium, eroding.** It owns the marketplace and the triage and reputation judge. AI floods raise triage costs, and routine findings are being devalued.
- **(b) Lead: moderate.** Largest payout pool found ($89.1M). No market-share data.
- **(c) Revenue model:** subscription plus PTaaS (human labour) plus legacy bounty fees.
- **(d) Financial strength:** unknown. Last raise in 2022; layoffs in 2023.
- **(e) Resilience:**
  - Steady scenario: slow erosion.
  - Pause: budget cuts.
  - Acceleration: severe compression outside business-logic and chained findings.
- **Path: partly coherent.** Hai Triage and agents are done, and the Internet Bug Bounty was cut, but the crowd remains the product.
- **Entry: cannot assess.**

**Bugcrowd (US/Australia, private)**
- **(a) Position: medium.** Crowd plus Mayhem's autonomous fuzzing (a strong, final judge for crashes).
- **(b) Lead: weak.** The valuation claim is company-sourced.
- **(c) Revenue model:** subscription, PTaaS (labour) and AI Pen Test.
- **(d) Financial strength:** $102M raised in 2024. Profitability unknown.
- **(e) Resilience:** medium.
- **Path: partly coherent.** The Mayhem acquisition is the most concrete automation move among the crowd platforms.
- **Entry:** "nearly doubled" from more than $1B is a company claim. **Cannot assess.**

**Synack (US, private)**
- **(a) Position: medium.** Vetted, cleared researcher network for government and defence (a constraint AI cannot remove quickly), plus Sara.
- **(b) Lead: weak to moderate.** GigaOm 2025 PTaaS Leader (company-cited).
- **(c) Revenue model:** labour-heavy PTaaS subscription.
- **(d) Financial strength:** about $107M raised. Unknown otherwise.
- **(e) Resilience:** medium, with government ballast.
- **Path: partly coherent.**
- **Entry: cannot assess.**

**Cobalt (US/Germany, private)**
- **(a) Position: weak to medium.** Human PTaaS (about 500 pentesters) plus Autonomous Pentest from August 2026, a late entry.
- **(b) Lead: weak.** Mostly G2 badges.
- **(c) Revenue model:** labour-heavy subscription.
- **(d) Financial strength:** small disclosed funding.
- **(e) Resilience:** low to medium.
- **Path: partly coherent.**
- **Entry: cannot assess.**

**YesWeHack (France, private)**
- **(a) Position: medium.** EU sovereignty, European Commission preferred provider and CNA status are constraints AI cannot remove.
- **(b) Lead: moderate.** EC procurement selection.
- **(c) Revenue model:** platform subscription and bounty-linked fees.
- **(d) Financial strength:** €26M raised in 2024.
- **(e) Resilience:** medium. Beneficiary of EU regulation (CRA).
- **Path: partly coherent.**
- **Entry:** exposure via Wendel is tiny. **Cannot assess.**

**Intigriti (Belgium, private)**
- **(a) Position:** medium to weak, as an EU crowd platform.
- **(b) Lead:** weak; data is thin.
- **(c) Revenue model:** platform.
- **(d) Financial strength:** €21M raised in 2022.
- **(e) Resilience:** low to medium.
- **Path: cannot judge** (no 2025–26 strategy data).
- **Entry: cannot assess.**

**Immunefi (Web3, private plus token)**
- **(a) Position: medium.** The on-chain exploit is a strong judge. AI smart-contract auditors (depthfirst's first model targets this) threaten it.
- **(b) Lead:** moderate. Payout scale is self-reported.
- **(c) Revenue model:** platform fees, lumpy.
- **(d) Financial strength:** unknown. Exposed to the crypto cycle.
- **(e) Resilience:** low in a pause.
- **Path: partly coherent.** Token plus "Immunefi AI".
- **Entry:** the IMU token is liquid but not equity, with unreliable valuation data. **Cannot assess.**

**NCC Group plc (UK, listed)**
- **(a) Position: weak.** Billable assurance hours, about 66% of Cyber revenue. Managed services are about 34%. No product line remains after Escode. Independence and regulatory assurance are its only partial "judge" role.
- **(b) Lead: weak to moderate.**
  - UK & APAC growth of 12.5% and a record 38.4% gross margin.
  - But North American Technical Assurance is shrinking with large tech clients.
  - No outside ranking.
- **(c) Revenue model:** labour-dominated.
- **(d) Financial strength:** moderate.
  - Net cash about £53m (FY26) and a £30m facility.
  - Cyber EBITDA margin about 7%, thin statutory profit.
  - About £210m returned in 2026.
- **(e) Resilience:**
  - Steady scenario: Technical Assurance volume pressure.
  - Pause: cost plan and regulation (DORA, NIS2, CRA) cushion it.
  - Acceleration: its weakest case, with hourly testing automated.
- **Path: partly coherent.** The cost plan is funded and plausible to FY28, but there is no automation product and it relies on human judgement staying scarce. A new CEO took over on 27 Oct 2026.
- **Entry:** 156.8p and £236m market cap (12 Nov 2026). My estimates: EV about £183m, about 0.8x EV/FY26 Cyber sales, about 11x EV/FY26 Cyber EBITDA, and about 5x on FY28 targets. Stockanalysis shows 24.7x forward P/E. Peers: Wavestone 5.5x and Rapid7 17.5x EV/EBITDA. **Fair.**

**Listed peers used for valuation only (quality not assessed):** Wavestone (France), TAC Infosec (India) and Rapid7 (US), with data as of 12 Nov 2026.

**Companies considered and excluded, with reasons:**
- **Theori (US/Korea):** deep-dive belongs to another researcher; only the AIxCC 3rd place is recorded.
- **Team Atlanta:** an academic and industry team, not a company, and no commercial vehicle was found. Its Samsung link appears only through Samsung's later XBOW investment and reseller deal.
- **Other AIxCC finalists (all_you_need_is_a_fuzzing_brain, Shellphish, 42-beyond-bug, Lacrosse):** no commercial follow-up found.
- **Mayhem Security:** now part of Bugcrowd and covered there.
- **Other AI-native names I expected to check but could not verify:** Tenzai, Novee, Terra Security (Israel), Hadrian (Netherlands), Ethiack (Portugal), Escape (France), Aikido (Belgium), Corgea and Almanax. The search budget ran out before they could be verified. They should not be read as absent from the market.
- **Model makers' products (Anthropic, OpenAI, Google, Cohere):** treated as competitors and gatekeepers, not scored.
- **Platform security vendors with gated access (CrowdStrike, Palo Alto Networks, Cisco, Zscaler, Wiz, Tenable):** outside this scope; noted as competitors.
- **AppSec incumbents (Snyk, Semgrep, Checkmarx, Endor Labs):** outside scope.
- **Other European listed or private testers:**
  - Orange Cyberdefense, Thales and Atos/Eviden are segments of larger groups.
  - Integrity360, Claranet and Bridewell are private.
  - WithSecure and Kudelski were not researched in this session.
- **Israeli listed testers:** none found.
- **Irregular (formerly Pattern Labs):** an AI model security evaluator rather than a vulnerability finder or fixer; not verified.

### Gaps
Cross-cutting gaps:
- XBOW's 2026 HackerOne rank.
- Dollar ARR for every private firm except Pentera.
- Services shares of revenue.
- Pentest day-rate data.
- The full TAC and Glasswing member lists.
- The Cohere–AISLE terms.
- NCC's FY26 audited results, 5-year multiple history and consensus estimates.
- Cymulate's funding.
- Secondary-market marks.
- The unverified AI-native challengers listed above.

Several summaries came from search snippets after primary pages returned 403. These include SecurityWeek (XBOW), Business Wire (Horizon3, March 2026), openai.com and Dark Reading, and they should be checked again before publication.

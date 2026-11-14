# Demand side of AI processors: buyers, contracts, vendor financing and cross-company claim contradictions (state of affairs as of 14 November 2026)

Notes on method and labels. Research date: 14 Nov 2026. The shared web-search budget ran out partway through. After that, findings come from fetching primary documents directly: SEC EDGAR filings (10-K, 10-Q, 8-K, S-1/A, 424B4), Federal Reserve, Bank of England and IMF pages, and company pages. Anything that could not be checked is listed in the last section. Provenance labels: **[CO]** = company-stated by the vendor or seller; **[BUY]** = buyer-stated; **[REG]** = regulator or government-stated; **[EST]** = analyst or industry estimate; **[PRESS-U]** = press report citing unnamed sources or non-public documents. "via press" means an on-record statement as relayed by a news outlet. "(calc)" marks arithmetic done for these notes. Filing dates are SEC filing dates. "As of" dates are balance-sheet or report dates.

Scheduled but **not yet happened** as of 14 Nov 2026:
- NVIDIA reports Q3 FY2027 results on 17 Nov 2026.
- Anthropic's IPO has not priced. The S-1/A was filed 10 Nov 2026 with a $70–$78 range.
- Alphabet and Meta will give 2027 capex guidance on their Q4 calls.
- The Senate (Sen. Tim Scott) has asked Jensen Huang to testify on 3 Dec 2026, per CNBC's live blog.

---

## 1. OpenAI: what it has committed, what is definitive versus LOI, what changed in 2026, and how commitments compare with revenue, losses and funding

### Takeaway
OpenAI's compute commitments fall into two groups:
- **Definitive contracts, as confirmed in counterparties' filings:** Microsoft Azure (+$250B), AWS ($38B + $100B), CoreWeave (≥$18.4B verified), Cerebras (750 MW committed) and NVIDIA-guaranteed 20-year Ohio leases.
- **Framework or LOI-type arrangements with no disclosed dollar value:** NVIDIA's 10 GW LOI and Broadcom's 10 GW. AMD's 6 GW is a definitive purchase agreement, but no milestone tranche had vested by 26 Sep 2026.

NVIDIA's "up to $100B" LOI was never converted into a definitive $100B agreement. NVIDIA instead invested $30B in OpenAI's 2026 round (Feb–Mar 2026). In Aug 2026 it guaranteed up to $105B of lease obligations for an OpenAI campus.

OpenAI's own investor framing of total compute spend has moved three times:
- about $1.4T for about 30 GW (Oct 2025);
- about $600B through 2030 (Feb 2026);
- about $856B for 2026–2030 (July 2026 presentation, per the FT).

Over the same period, 2026 revenue is reported at about $36B (FT) and OpenAI raised $122B.

### Cited Findings

**Headline commitment totals (OpenAI framing)**
- [BUY via press] On a 28 Oct 2025 livestream, Altman said OpenAI was committed to about 30 GW of compute at about $1.4T total cost. — [Reuters via StreetInsider, "Altman touts trillion-dollar AI vision as OpenAI restructures to chase scale," 29 Oct 2025](https://www.streetinsider.com/Reuters/Altman+touts+trillion-dollar+AI+vision+as+OpenAI+restructures+to+chase+scale/25515962.html); [PYMNTS, "OpenAI Aims to Add 1 Gigawatt of Compute Per Week," Oct 2025](https://www.pymnts.com/artificial-intelligence-2/2025/openai-aims-to-add-1-gigawatt-of-compute-per-week/)
  - Lead check: the user's lead says "Nov 2025, about $1.4T over about 8 years". The $1.4T and about 30 GW figures are confirmed. The coverage found dates them to 28–29 Oct 2025. A November 2025 statement with "eight years" wording was **not located** in this session.
- [PRESS-U] Feb 2026: OpenAI told investors it targets about $600B of total compute spend by 2030, down from Altman's $1.4T figure. It projects more than $280B of revenue in 2030. — [CNBC via Yahoo Finance, "OpenAI recalibrates growth path with $600 billion compute target," ~20–21 Feb 2026](https://finance.yahoo.com/news/openai-recalibrates-growth-path-600-233121761.html); [CNBC, "OpenAI announces $110 billion funding round…," 27 Feb 2026](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)
- [PRESS-U] A July 2026 OpenAI presentation, prepared for a computing deal, puts compute and infrastructure at about $856B for 2026–2030. The same presentation shows:
  - 2030 revenue of about $350B, against about $36B in 2026;
  - cumulative negative free cash flow of about $278B for 2026–2030, down from about $305B in a May projection;
  - per the FT, the $122B raised is "on track to be exhausted by 2028".
  - — [TNW, "OpenAI told investors in February its compute bill would be around $600bn. A July presentation puts it at $856bn," 19 Sep 2026 (citing FT; Bloomberg write-up 18 Sep 2026)](https://thenextweb.com/news/openai-856bn-compute-vs-600bn-reset-burn-improved)
- [PRESS-U, unverified] A single secondary outlet attributes a $750B compute capex projection to the WSJ. It could not be checked. — [BigGo Finance](https://finance.biggo.com/news/c50bdf51-e150-4bc0-b17f-fddd90b1212b)

**Microsoft (definitive)**
- [CO] 28 Oct 2025 restructuring:
  - OpenAI "has contracted to purchase an incremental $250B of Azure services".
  - Microsoft no longer has a right of first refusal to be OpenAI's compute provider.
  - Microsoft's stake was about 27% as-converted, valued at about $135B.
  - — [Microsoft blog, "The next chapter of the Microsoft–OpenAI partnership," 28 Oct 2025](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)
- [CO] As of 30 Sep 2026:
  - Microsoft holds an equity-method interest of about 24% as-converted.
  - In Q1 FY27 (quarter to 30 Sep 2026) it recorded **$10.0B of revenue from OpenAI** commercial arrangements, including revenue-sharing payments. That is about 10.8% of Microsoft's $92.3B total revenue (calc).
  - Accounts receivable from OpenAI were $7.2B.
  - Funding commitments to OpenAI total $13.0B, of which $12.0B is funded.
  - OpenAI-related net gains were $272M in the quarter, against $4.1B of net losses a year earlier.
  - — [SEC EDGAR: Microsoft Form 10-Q for quarter ended 30 Sep 2026, filed 28 Oct 2026](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm)
- [CO] Microsoft's commercial RPO is $677B (+73%). Microsoft does not disclose OpenAI's share. RPO's sequential decline was smaller than usual "due to the large Azure commitment this quarter" (customer unnamed). — [Motley Fool transcript, Microsoft Q1 FY27 call, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)

**AWS / Amazon (definitive)**
- [CO] Q1 2026: AWS and OpenAI expanded the "existing $38.0 billion multi-year commitment… by $100.0 billion over 8.0 years, which includes contractual obligations related to the performance of AWS chips." — [SEC EDGAR: Amazon Form 10-Q, Q3 2026, filed 30 Oct 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- [CO via press] OpenAI will use about 2 GW of Trainium capacity (Trainium3 and Trainium4; Trainium4 deliveries from 2027). AWS becomes the exclusive third-party cloud distributor for OpenAI Frontier. — [DCD, "OpenAI to use 2GW of Trainium on AWS, expand Amazon cloud contract by $100bn," Feb 2026](https://www.datacenterdynamics.com/en/news/openai-to-use-2gw-of-trainium-on-aws-expand-amazon-cloud-contract-by-100bn/); [CNBC, 27 Feb 2026](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)

**Oracle / Stargate (definitive agreement; dollar value not verified here)**
- [CO via press] March 2026, Oracle's statement: it has "completed leasing for an additional 4.5 GW of capacity to support its OpenAI commitments". It called reports of problems at Abilene "false and incorrect". Bloomberg's correction said Oracle and OpenAI "are not moving ahead with the planned expansion lease" of about 600 MW at Abilene, but that the 4.5 GW agreement "remains on track". Reported reasons were drawn-out financing talks and a shift in OpenAI's needs. — [Tom's Hardware via Yahoo Finance, "Oracle hits back at Stargate data center cancellation reports," 9 Mar 2026](https://finance.yahoo.com/news/oracle-hits-back-stargate-data-172802489.html)
- [CO] On 10 Sep 2026 Oracle said: "618 megawatts and 75% of total capacity have now been delivered to the customer" at Abilene. It described Shackelford as the next gigawatt-scale campus. — [Motley Fool transcript, Oracle Q1 FY27 call, 11 Sep 2026](https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/)
- [BUY/CO] Oracle does not name OpenAI in its filings. "No single customer accounted for 10% or more of our total revenues in fiscal 2026, 2025 or 2024." — [SEC EDGAR: Oracle Form 10-K FY2026, filed 22 Jun 2026](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm)

**CoreWeave (definitive)**
- [CO] OpenAI committed to pay up to about $11.9B through Oct 2030 (March 2025 MSA) and up to about $6.5B through 31 May 2031 (Sept 2025 order form). That is about $18.4B verified (calc). — [SEC EDGAR: CoreWeave Form 10-K FY2025, filed 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm); [CoreWeave 10-Q Q3 2026, filed 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm)

**NVIDIA (LOI never finalized as $100B; replaced by equity plus guarantee)**
- [CO] 22 Sep 2025 letter of intent:
  - "at least 10 gigawatts" of NVIDIA systems;
  - NVIDIA "intends to invest up to $100 billion… progressively as each gigawatt is deployed";
  - first GW in H2 2026 on Vera Rubin;
  - details to be finalized "in the coming weeks".
  - — [NVIDIA Newsroom, "OpenAI and NVIDIA Announce Strategic Partnership to Deploy 10 Gigawatts of NVIDIA Systems," 22 Sep 2025](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems)
- [CO via press] On 31 Jan 2026 Huang called a WSJ report "nonsense" and said NVIDIA's contribution to the current round "wouldn't approach $100 billion." On 1 Feb 2026 he said "It was never a commitment… we will invest one step at a time." On first-GW timing: "it's up to OpenAI".
  - [PRESS-U] The WSJ (30 Jan 2026) reported that Huang privately stressed the agreement was nonbinding and criticized OpenAI's business discipline.
  - — [Fortune, "Pledge to invest $100 billion in OpenAI was 'never a commitment,' says Nvidia's Huang," 2 Feb 2026](https://fortune.com/2026/02/02/jensen-huang-nvidia-ceo-on-openai-investment-never-a-commitment/)
- [CO] "We are finalizing an investment and partnership agreement with OpenAI. There is no assurance that we will enter into an investment and partnership agreement with OpenAI or that a transaction will be completed." — [SEC EDGAR: NVIDIA Form 10-K FY2026 (FY ended 25 Jan 2026), filed 25 Feb 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- [CO/BUY via press] 27 Feb 2026: NVIDIA put $30B into OpenAI's round. OpenAI "will use 3 GW of dedicated inference capacity and 2 GW of training capacity on Nvidia's Vera Rubin systems". Reuters noted it was unclear whether the $30B replaced the September LOI. — [CNBC, 27 Feb 2026](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)
- [CO] 17 Aug 2026, SB Energy PORTS-Pike campus in Pike County, Ohio:
  - initial 4.25 IT-GW; NVIDIA holds an option on another 3.75 IT-GW (8 IT-GW total);
  - 20-year leases to OpenAI;
  - NVIDIA is the exclusive compute provider and gives credit support for land, power and shell;
  - NVIDIA invests $1.5B in SB Energy;
  - capacity comes online in phases from 2028.
  - — [SEC EDGAR: NVIDIA 8-K exhibit (SB Energy/OpenAI/NVIDIA release), 17 Aug 2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000069/sbeoainvidia-portsrelease.htm)
- [CO] The NVIDIA guarantees:
  - are capped at $105B;
  - cover nine construction phases, the first expected in FY2029;
  - "terminate upon certain events, including OpenAI achieving a satisfactory credit rating";
  - OpenAI "has agreed to reimburse and indemnify us for certain losses".
  - — [SEC EDGAR: NVIDIA Form 10-Q, quarter ended 26 Jul 2026, filed 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [CO] NVIDIA estimates that "one AI research and deployment company contributed a meaningful amount of our revenue by purchasing cloud services from our customers". This is an indirect customer, not named. — [NVIDIA 10-Q Q2 FY27, filed 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)

**AMD (definitive purchase agreement, milestone-based)**
- [CO] Oct 2025 product purchase agreement:
  - 6 GW, with the first GW on MI450;
  - warrant for up to 160M AMD shares at $0.01;
  - vesting tied to purchase milestones and AMD share-price targets.
  - — [SEC EDGAR: AMD Form 10-K FY2025, filed 4 Feb 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000018/amd-20251227.htm)
- [CO] As of 26 Sep 2026, "no warrant shares had vested or become exercisable" for either warrant customer (OpenAI or Meta). — [SEC EDGAR: AMD Form 10-Q Q3 2026, filed 4 Nov 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- [CO] 3 Nov 2026: "Anthropic, Meta, Microsoft, OpenAI and Oracle Cloud Infrastructure are running models and workloads on the first AMD Helios rackscale solutions" powered by MI450. — [SEC EDGAR: AMD Q3 2026 earnings release (Ex. 99.1), 3 Nov 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm)

**Broadcom (framework; no dollar value disclosed)**
- [CO via press] 13 Oct 2025: 10 GW of custom accelerators, with racks deployed "starting late next year". Financial terms were not disclosed. — [CNBC, "Broadcom stock pops 9% on OpenAI custom chip deal…," 13 Oct 2025](https://www.cnbc.com/2025/10/13/openai-partners-with-broadcom-custom-ai-chips-alongside-nvidia-amd.html)
- [CO via press] 24 Jun 2026: "Jalapeño" inference chip unveiled.
  - Initial deployment is targeted by the end of 2026, with "small prototype development" late in 2026.
  - Hock Tan: "We will start seeing it really ramp up in '27 and really going full tilt in first half '28."
  - — [CNBC, "OpenAI unveils first chip as part of Broadcom deal…," 24 Jun 2026](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- [CO via press] Sept 2026 Broadcom call: it expects 1.3 GW of OpenAI deployment in 2027 and more than 5 GW in 2028. — [Yahoo Finance, "Broadcom Just Named Its Next AI Customer. It Isn't Google.," Sept 2026](https://finance.yahoo.com/technology/ai/articles/broadcom-just-named-next-ai-222044865.html)

**Cerebras (definitive; delivery shortfall)**
- [CO] Dec 2025 Master Relationship Agreement with OpenAI:
  - 750 MW that OpenAI is "contractually committed to purchase", deployed 2026–2028 in tranches;
  - option for another 1.25 GW by end-2030 (up to 2.0 GW total);
  - $1.0B "Working Capital Loan" funded by OpenAI in Jan 2026, at 6%, maturing by 2032;
  - warrant to OpenAI for up to 33,445,026 Class N shares at $0.00001;
  - 10,033,508 vested shares had been exercised by 30 Sep 2026.
  - — [SEC EDGAR: Cerebras Form 10-Q Q3 2026, filed 12 Nov 2026](https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm); [Cerebras 424B4 prospectus, 14 May 2026](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
- [PRESS-U] Deal value of "over $10 billion", per "people close to the company". — [CNBC, "Cerebras scores OpenAI deal worth over $10 billion ahead of AI chipmaker's IPO," 14 Jan 2026](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)
- [CO] Status at 30 Sep 2026:
  - OpenAI was 34% of Cerebras's Q3 2026 revenue.
  - Cerebras RPO was $26.1B, "a significant amount" attributable to OpenAI.
  - As of 30 Sep 2026, Cerebras had "delivered less capacity to OpenAI than the quantity contemplated by the MRA".
  - Service credits began accruing on 1 Oct 2026.
  - Delays "may continue through a portion of 2027".
  - Capacity terminable in 2026 is expected to be under 5% of committed capacity.
  - — [Cerebras 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm)

**Google Cloud**
- [BUY via press] OpenAI lists Google Cloud among its cloud partners, alongside Microsoft, Oracle, AWS and CoreWeave. No dollar figure was found. — [CoinDesk, "OpenAI raises a record $122 billion as revenue crosses $2 billion per month," 1 Apr 2026](https://www.coindesk.com/tech/2026/04/01/openai-raises-a-record-usd122-billion-at-as-revenue-crosses-usd2-billion-per-month)

**Revenue, losses and funding**
- [BUY via press] OpenAI's statements on 31 Mar 2026:
  - more than $2B of revenue per month, up from $1B per quarter at end-2024;
  - more than 900M weekly ChatGPT users and more than 50M subscribers;
  - enterprise is over 40% of revenue;
  - a revolving credit facility of about $4.7B, undrawn.
  - — [CoinDesk, 1 Apr 2026](https://www.coindesk.com/tech/2026/04/01/openai-raises-a-record-usd122-billion-at-as-revenue-crosses-usd2-billion-per-month)
- [BUY] The round closed 31 Mar 2026 with "$122 billion in committed capital at an $852B post-money valuation". — [OpenAI on X, 31 Mar 2026](https://x.com/OpenAI/status/2039085161971896807)
  - Announced 27 Feb 2026 at $110B: Amazon $50B, NVIDIA $30B, SoftBank $30B, at $730B pre-money. — [CNBC, 27 Feb 2026](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)
  - **Lead check: confirmed.**
- [CO] Amazon's $50B was fully funded by Q3 2026: $15.0B in Series C preferred (Q1 2026), $13.7B (Q2) and the remaining $21.3B (Q3). Amazon's equity investments in private companies, mainly Anthropic and OpenAI, had a $143.7B carrying value at 30 Sep 2026. — [Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- [PRESS-U] 2026 quarterly figures reported by the WSJ, seen only via a secondary tracker and not verified at source:
  - Q1 2026: revenue $5.7B, operating loss $9.3B;
  - Q2 2026: revenue $6.7B, operating loss $12.3B;
  - Q1 2026 cash burn $3.7B (The Information).
  - — [AI Funding Tracker, "Is OpenAI Losing Money? 2026…" (secondary)](https://aifundingtracker.com/is-openai-losing-money/)
- [PRESS-U, unverified] Secondary sites say OpenAI told investors its annualized revenue was "nearing $50 billion" at the end of September 2026. — [ValueAdd VC (secondary)](https://valueaddvc.com/blog/openai-revenue-2026-20b-arr-4b-month-path-to-profitability)
- [PRESS, conflicting] OpenAI confidentially submitted a draft S-1. Sources disagree on timing: submitted 22 May 2026 or announced 8 Jun 2026. Several outlets say OpenAI said it "may be a while". No public S-1 had been filed as of 14 Nov 2026. — [The Tech Portal, 9 Jun 2026](https://thetechportal.com/2026/06/09/openai-confidentially-files-for-ipo-through-draft-s-1-submission-to-us-sec/)

**Comparison (calc)**
- Dollar commitments verifiable in counterparties' filings:
  - Azure +$250B;
  - AWS $138B;
  - CoreWeave $18.4B.
  - Total: about **$406B**.
  - This excludes Oracle (value unverified), NVIDIA, AMD, Broadcom (no dollar terms), Cerebras (more than $10B, press) and the SB Energy leases (value undisclosed). The $406B equals about 11x OpenAI's reported 2026 revenue of about $36B (FT) and about 3.3x the $122B round.
- OpenAI's own July 2026 projection: cumulative negative free cash flow of about $278B for 2026–2030, more than twice the $122B raised (FT).

### Inferences
- Definitive (counterparty-filed) commitments: Microsoft, AWS, CoreWeave, Cerebras, Ohio/SB Energy leases, and the AMD purchase agreement (with milestone warrants).
- LOI or framework with no disclosed dollar obligation: NVIDIA's 10 GW and Broadcom's 10 GW. The NVIDIA 10 GW now appears to run partly through the Feb 2026 "3 GW inference + 2 GW training" commitment and the Ohio campus.
- Changed in 2026:
  - NVIDIA's $100B progressive investment became a $30B equity stake plus a $105B lease guarantee.
  - The Abilene expansion lease was dropped (Mar 2026).
  - The compute-spend target was reset from $1.4T to $600B, then rose to $856B in a later presentation.
  - Several delivery timelines slipped:
    - NVIDIA's first GW was "H2 2026"; the first Ohio phase is FY2029.
    - Broadcom's deployment moved from "late 2026" to a 2027 ramp.
    - Cerebras is short on delivery.
- OpenAI's revenue is growing quickly. Even so, its own projections imply that much of the 2026–2030 compute bill must be externally financed. This is consistent with vendors (NVIDIA, Amazon, AMD, Cerebras) supplying equity, loans or guarantees.

### Gaps
- OpenAI has no public audited financials; its draft S-1 is confidential.
- The Oracle–OpenAI contract value, widely reported as about $300B in 2025, was not verified.
- Google Cloud contract size is not available.
- The CoreWeave May 2025 tranche of about $4B (which would make about $22.4B total) was not verified in filings fetched.
- The WSJ quarterly 2026 figures and the "nearly $50B run-rate" were not verified at source.
- Whether NVIDIA's $30B formally superseded the LOI was not stated by either party in documents found.

---

## 2. Anthropic: commitments (Google TPUs, AWS/Rainier, Microsoft/NVIDIA, Broadcom, Fluidstack and others) versus revenue and funding

### Takeaway
Anthropic's public S-1/A (10 Nov 2026) is the most complete buyer-side disclosure available. Key figures:
- About **$900.9B** of aggregate committed spend (as of and after 30 Sep 2026), with **$70.7B due in the 12 months** after 30 Sep 2026.
- Against this: 9M-2026 GAAP revenue of $33.2B, a run-rate of about $81B at 31 Oct 2026, and $131.9B of cash plus short-term investments.
- A pending IPO, plus a $26.0B private placement bought largely by its chip and cloud vendors.

The buyer's disclosures confirm, and in several cases exceed, vendors' announced figures. Microsoft's $30B became $47.2–49.2B after amendments. Broadcom's $21B of disclosed orders (Dec 2025) compares with $161.2B of five-year TPU equipment-lease rents in Anthropic's filing; the scope differs. Several commitments are contingent or cancellable.

### Cited Findings

**Revenue, run-rate and losses**
- [BUY] GAAP revenue:
  - 2023: $41M
  - 2024: $386M
  - 2025: $4,585M
  - 9M 2025: $2,545M
  - 9M 2026: **$33,242M**
- [BUY] Operating loss:
  - 2025: $(8,060)M
  - 9M 2026: $(1,260)M
- [BUY] Net loss for 2025 was $(41,965)M, including $(34,308)M of fair-value changes on convertible instruments.
- [BUY] Compute and infrastructure expense for 9M 2026 was $18,808M.
- — [SEC EDGAR: Anthropic, PBC Form S-1/A (Amendment No. 2), filed 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
- [BUY via press] Q3 2026 revenue was about $17.0B. The 9M-2026 net loss of about $104B was mostly fair-value changes. — [CNBC, "Anthropic reports $17 billion in Q3 revenue, purchase commitments of $895.4 billion in revised S-1," 2 Nov 2026](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html)
- [BUY] Run-rate path (**lead check: steep growth confirmed**):
  - about $9B at end-2025, rising to above $30B by 6 Apr 2026 — [Anthropic, "Anthropic expands Google and Broadcom compute deal," 6 Apr 2026](https://anthropic.com/news/google-broadcom-partnership-compute)
  - $65B at end-July 2026, per what Anthropic told investors — [CNBC, 17 Aug 2026](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html)
  - "approximately $81 billion as of October 31, 2026, up $10 billion from September 30, 2026" — [S-1/A, 10 Nov 2026](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
- [BUY] Customers with more than $100K of trailing-twelve-month revenue grew from more than 950 (30 Sep 2025) to more than 11,900 (30 Sep 2026). — [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)

**Funding and IPO**
- [BUY] Series G-1 raised $23.45B (Jan–Feb 2026, $259.1364/share). Series H-1 raised $45.73B (May–Jun 2026, $589.0095/share). — [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
  - Press headline totals differ from the S-1 figures because they include other tranches: Series G $30B at $380B post-money; Series H $65B at $965B post-money (28 May 2026). — [CNBC, 28 May 2026](https://www.cnbc.com/2026/05/28/anthropic-open-ai-startup-value.html)
- [BUY] IPO terms:
  - 825M Class A shares at a $70–$78 range, Nasdaq ticker "ANT";
  - about $61.1B gross at the $74 midpoint before over-allotment (calc);
  - **concurrent $26.0B private placement**:

    | Buyer | Amount |
    |---|---|
    | Google | $10.0B |
    | NVIDIA | $10.0B |
    | AMD | $2.5B |
    | Broadcom | $1.0B |
    | Micron | $1.0B |
    | Microsoft | $1.0B |
    | TSMC | $0.5B |

  - — [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
- [BUY] As of 30 Sep 2026: $95.6B cash and equivalents, $36.3B short-term investments and $2.6B restricted cash. — [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)

**Aggregate commitments**
- [BUY] About $900.9B of committed spend "substantially all of which is related to compute and infrastructure":
  - $451.6B before 31 Dec 2030;
  - the remainder mostly 2031–2045;
  - $70.7B due in the 12 months after 30 Sep 2026.
- [BUY] Components outside the main table:
  - the table itself (30 Sep 2026) totals $320.0B, including $313.8B of purchase commitments;
  - leases executed but not commenced: $451.2B;
  - post-30 Sep commitments: $105.7B;
  - short-term commitments: $17.4B.
- — [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
- The 2 Nov S-1/A No. 1 figure was $895.4B. — [CNBC, 2 Nov 2026](https://www.cnbc.com/2026/11/02/anthropic-ant-s-1-quarter-financials.html)

**By counterparty (S-1/A, 10 Nov 2026, unless noted)**
- **Google TPUs**
  - [BUY] CSP hosting agreement signed Mar 2026 and amended May–Oct 2026: at least about **$121.3B** between Apr 2026 and Jul 2033, with a true-up if spend falls short. It is non-cancelable except for Google's uncured breach.
  - [BUY] Additional TPU compute for 2028–2031, estimated at **$125.0–150.0B**, is not included in the table.
  - [BUY] Earlier announcement (23 Oct 2025): "up to one million TPUs", "tens of billions of dollars", "well over a gigawatt of capacity online in 2026". — [Anthropic, "Expanding our use of Google Cloud TPUs and Services," 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- **Broadcom (TPU racks)**
  - [BUY] Five-year master equipment leases (finance leases) with rent of about **$161.2B** excluding interest, secured by the leased equipment and with cross-defaults. Broadcom assigned portions of these leases to a third party in Q2 2026 and to a newly formed special-purpose financing entity in Oct 2026.
  - [BUY] Broadcom's "Infrastructure Partner 2026 NPA" provides up to **$42.0B** of convertible notes to finance rent.
  - [CO via press] Broadcom said Anthropic placed $10B plus $11B of orders, $21B in total (Dec 2025 call). — [24/7 Wall St live coverage, 11 Dec 2025](https://247wallst.com/investing/2025/12/11/live-broadcom-avgo-q4-earnings-coverage/)
  - [CO via press] Broadcom expects 1 GW of Ironwood for Anthropic in 2026, about 5 GW of TPU v8i in 2027, and a "path to another 10 GW in 2028". It expects Anthropic to become its largest XPU customer in 2027. — [Yahoo Finance, Sept 2026](https://finance.yahoo.com/technology/ai/articles/broadcom-just-named-next-ai-222044865.html)
  - [CO via press] A Broadcom filing put the figure at about 3.5 GW for Anthropic from 2027. — [Data Center Knowledge, Apr 2026](https://www.datacenterknowledge.com/data-center-chips/anthropic-secures-multi-gigawatt-tpu-deal-with-google-broadcom)
- **Amazon / Trainium**
  - [BUY] Apr 2026 agreement: at least **$110.0B** between May 2026 and Apr 2036, with a true-up.
  - [CO] Amazon's description: "more than $100.0 billion over 10.0 years, which includes contractual obligations related to the performance of AWS chips." — [Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
  - [BUY] On 6 Apr 2026 Anthropic said Amazon remains its "primary cloud provider and training partner" on Project Rainier. — [Anthropic, 6 Apr 2026](https://anthropic.com/news/google-broadcom-partnership-compute)
- **Microsoft / NVIDIA**
  - [BUY] Nov 2025 agreement, amended Feb–Nov 2026: at least **$47.2B** and up to $49.2B between Nov 2026 and Jun 2033, "regardless of actual usage".
  - [PRESS] The Nov 2025 announcement was $30B of Azure, up to 1 GW on Grace Blackwell and Vera Rubin, with NVIDIA investing up to $10B and Microsoft up to $5B. — [Yahoo Finance, "Microsoft and Nvidia to Invest in Anthropic as Startup Commits $30 Billion to Azure," 18 Nov 2025](https://finance.yahoo.com/news/microsoft-nvidia-invest-anthropic-startup-113316065.html)
- **SpaceXAI (formerly xAI)**
  - [BUY] Agreements signed May–Oct 2026 for compute "powered by NVIDIA GPUs": up to **$120.5B** over terms into 2029, about $3.1B per month once all capacity is delivered (expected Dec 2026).
  - Either party may cancel on 90 days' notice once the initial non-cancelable periods end in Jan and Mar 2027.
- **AMD**
  - [BUY] July 2026 Hardware Supply Agreement for MI450 "Helios" racks, with an initial tranche in 2027. If the full initial capacity is procured, spend is expected to exceed **$20.0B**. There is an option for roughly the same amount again.
  - [BUY] AMD committed to buy up to **$5.0B** of Anthropic Class N stock, drawable on delivery milestones; the first milestone is expected in 2027.
- **Nscale**
  - [BUY] Aug 2026: up to about **$44.6B** of NVIDIA GPU compute into 2033. Nscale must "use best efforts to obtain qualifying financing for the NVIDIA GPUs and data center infrastructure".
- **Lambda**
  - [BUY] May, Jun and Aug 2026: about **$41.3B** into 2034.
  - The Aug 2026 agreement (about $34.9B) is "currently terminable by either party" because Lambda did not secure the facility lease by the deadline. No notice has been given, and Anthropic does not intend to terminate.
- **Fluidstack / own data centers**
  - [BUY] 12 Nov 2025: $50B of US infrastructure, with Fluidstack building sites in Texas and New York that come online through 2026. — [Anthropic, "Anthropic invests $50 billion in American AI infrastructure," 12 Nov 2025](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure)
  - [BUY] The S-1/A describes a colocation and services agreement with Fluidstack. It says "Our first data center facility became operational this year". To secure some data center projects, Anthropic has relied on "financing sources or partners who guarantee the lease obligations… expected to host such partner's chips".

**Vendor financing into Anthropic (S-1/A)**
- [BUY] Potential future financing capacity totals **$77.0B**:

  | Agreement | Capacity | Notes |
  |---|---|---|
  | Google 2026 NPA | $20.0B | Drops to $10.0B once Google's $10B IPO placement closes |
  | Amazon 2026 NPA | $15.0B | |
  | Broadcom Infrastructure Partner 2026 NPA | $42.0B | |

- [BUY] There is also $6.2B of outstanding Amazon notes.

### Inferences
- Buyer disclosures broadly **support** vendors' claims about Anthropic as a customer:
  - Google/Broadcom (TPU),
  - Amazon (Trainium),
  - Microsoft/NVIDIA (GPUs),
  - AMD (MI450).
  - In dollar terms, the buyer's commitments are larger than the vendors' announcements.
- A meaningful share of the commitment headline is contingent or cancellable:
  - SpaceXAI can be cancelled after early 2027;
  - Lambda's Aug 2026 deal is currently terminable;
  - Nscale's depends on financing;
  - AMD's has conditions;
  - the $125–150B of additional TPU spend for 2028–2031 is an estimate.
- Several vendors are also Anthropic's financiers and shareholders: Google, Amazon, Broadcom, AMD, NVIDIA, Microsoft, Micron and TSMC.
- At 30 Sep 2026, liquidity ($131.9B) covered about 1.9x the next-12-month obligations ($70.7B) (calc). Total commitments are about 11x the Oct-2026 run-rate (calc).

### Gaps
- Amazon's and Google's exact percentage ownership was not extracted.
- It was not established whether NVIDIA's and Microsoft's Nov 2025 "up to" investments were funded before the IPO placement.
- Which Fluidstack sites are live was not established.
- Amazon's 10-Q describes a facility "not to exceed $20.0 billion". Anthropic's S-1/A shows a $15.0B Amazon 2026 NPA, plus a 19.3M-share Series G-2 commitment of about $5B. These likely reconcile, but neither filing states it explicitly (see the contradictions log).

---

## 3. Other buyers: Meta, Microsoft, xAI/SpaceXAI, Oracle, CoreWeave and other neoclouds, sovereign buyers. Which chips and what commitments?

### Takeaway
Every large buyer is now multi-sourcing:
- Meta: AMD (binding 1 GW, up to 6 GW with warrants), NVIDIA via CoreWeave, and Google TPU software work.
- Microsoft: NVIDIA, AMD and its own Maia.
- Oracle: NVIDIA, AMD and Google TPU systems.

Neoclouds remain NVIDIA-centric: CoreWeave says its customers contractually specify NVIDIA, and SpaceXAI, Nscale and Lambda use NVIDIA GPUs. Off-balance-sheet obligations are very large:
- Meta: $454.5B non-cancelable commitments and $355.7B of leases not commenced.
- Microsoft: $364.6B of leases not commenced.
- Oracle: $288B of leases not commenced.

xAI, now inside SpaceX, has become a seller of NVIDIA compute to Anthropic.

### Cited Findings

**Meta**
- [CO] On 23 Feb 2026 AMD issued Meta a warrant for up to 160M shares at $0.01.
  - Meta "agreed to a binding commitment… to purchase… the initial one (1) gigawatt equivalent" of AMD Instinct GPUs.
  - Full vesting requires 6 GW of purchases.
  - Stock-price thresholds escalate to $600 for the final tranche.
  - The warrant is exercisable until 23 Feb 2031.
  - — [SEC EDGAR: AMD Form 8-K, 24 Feb 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000045/amd-20260223.htm)
- [CO] CoreWeave contracts with Meta:
  - Sept 2025: Meta committed up to about $14.2B through Dec 2031.
  - Mar 2026: Meta "initially committed to pay us up to approximately $21.0 billion", through 20 Dec 2032.
  - — [CoreWeave 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm); [CoreWeave 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm)
- [CO] Google (Thomas Kurian, 28 Oct 2026): "we recently worked closely with Meta to deliver TorchTPU." No TPU purchase by Meta is disclosed. — [Investing.com transcript, Alphabet Q3 2026 call, 28 Oct 2026](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037)
- [BUY] Meta's position as of 30 Sep 2026:
  - non-cancelable contractual commitments of **$454.52B**, "mostly… third-party cloud capacity arrangements and investments in servers and network infrastructure", with $45.85B due in 2026 and $121.41B in 2027;
  - leases not yet commenced of about **$355.73B** (2026–2036);
  - contingent obligations to buy up to $14.72B of cloud capacity over five years, reducible if the provider resells it;
  - maximum residual value guarantees of **$41.5B** to its data center Ventures (Louisiana lease from 2029, Texas from 2028).
  - — [SEC EDGAR: Meta Form 10-Q Q3 2026, filed 22 Oct 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)
- [PRESS-U] Mar 2026: Bloomberg reported Meta was evaluating Abilene space originally earmarked for OpenAI, with NVIDIA helping facilitate talks. — [Yahoo Finance, 9 Mar 2026](https://finance.yahoo.com/news/oracle-hits-back-stargate-data-172802489.html)

**Microsoft (as buyer)**
- [BUY] "We continue to scale our fleet with the latest innovations from NVIDIA and AMD alongside our own Maia systems." "Maia 300 will… deliver 40% more tokens per watt compared to the leading GPU-based systems." Microsoft has "docked our first NVIDIA Vera Rubin GPUs." "Some third-party capacity deliveries we expected in Q1 were delayed." — [Microsoft Q1 FY27 call transcript, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)
- [BUY] Leases not yet commenced were $364.6B at 30 Sep 2026, commencing FY2027–FY2034. — [Microsoft 10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm)
- [CO] Cerebras says it signed commercial agreements with Oracle and Microsoft "in the second half of 2026 for the sale of hardware". — [Cerebras 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm)

**xAI / SpaceXAI**
- [BUY] SpaceX completed its acquisition of xAI on 2 Feb 2026. — [SEC EDGAR: SpaceX Form 10-Q Q3 2026, filed 22 Oct 2026](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)
  - The SpaceX IPO prospectus (424B4) was filed 12 Jun 2026, per [EDGAR filing list](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001181412).
- [BUY] SpaceX's AI ("Super Intelligence") segment:
  - "nameplate compute" was **1.7 GW** at 30 Sep 2026, against 0.6 GW a year earlier;
  - in 2026 it "entered into revenue arrangements to provide cloud services to customers";
  - SpaceX's total backlog was $63.0B.
  - — [SpaceX 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)
- [BUY] Anthropic is a SpaceXAI customer for up to $120.5B of NVIDIA-GPU compute (see Section 2).
- [BUY] GPU financing at SpaceXAI:
  - Valor Equity Partners equipment leases for "SI infrastructure hardware", accounted for as a failed sale-leaseback, carried $12.9B of debt at 30 Sep 2026, against $4.5B at 31 Dec 2025.
  - Valor's CEO is a SpaceX director.
  - Earlier xAI debt: $3B of 12.5% senior secured notes and $2B of term loans (Jun 2025).
  - — [SpaceX 10-Q](https://www.sec.gov/Archives/edgar/data/1181412/000162828026066880/spcx-20260930.htm)

**Oracle (as buyer and operator)**
- [BUY/CO] Position as of 31 Aug 2026:
  - RPO of $664B (13% recognizable within 12 months), against $455B a year earlier;
  - $288B of additional lease commitments not yet commenced, mostly data centers, starting Q2 FY27–FY2029 with 15–19-year terms;
  - $11.4B of customer prepayments with a significant financing component in Q1 FY27;
  - $19.9B net raised through its at-the-market equity program;
  - $125.0B of senior notes and borrowings at par, with a fair value of $105.7B.
  - — [SEC EDGAR: Oracle Form 10-Q Q1 FY27, filed 11 Sep 2026](https://www.sec.gov/Archives/edgar/data/1341439/000119312526389274/orcl-20260831.htm)
- [BUY] Oracle on financing new contracts: "the vast majority of those new contracts were via prepay or bring your own hardware or a similar mechanic." On chips: "NVIDIA Vera systems are performing better than expected." — [Oracle Q1 FY27 call transcript, 11 Sep 2026](https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/)
- [CO] Oracle runs AMD MI450/Helios (AMD, 3 Nov 2026). Google has "partnerships to deliver TPU systems with both Crux AI and Oracle" (Kurian, 28 Oct 2026). — [AMD Q3 2026 release](https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm); [Alphabet Q3 call](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037)

**CoreWeave and other neoclouds**
- [BUY] "All of the GPUs used in our infrastructure today are NVIDIA GPUs… our current customers have contractually specified our use of NVIDIA GPUs."
- [BUY] RPO was **$132.3B** at 30 Sep 2026, against $60.7B at 31 Dec 2025.
- [BUY] Customer concentration:
  - Microsoft was about 67% of 2025 revenue;
  - the top two customers were about 30% and 24% of Q3 2026 revenue;
  - Jane Street committed about $6.0B (Apr 2026).
- [BUY] NVIDIA bought about 23M CoreWeave shares at $87.20 ($2.0B) in Jan 2026.
- — [CoreWeave 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm); [CoreWeave 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000104/crwv-20251231.htm)
- [CO] NVIDIA's Vera Rubin racks are running at CoreWeave, Google Cloud, Microsoft Azure, OCI and Nebius. — [SEC EDGAR: NVIDIA Q2 FY27 press release, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
- [BUY] Nscale and Lambda sell NVIDIA-GPU compute to Anthropic (about $44.6B and about $41.3B; see Section 2).

**Sovereign buyers**
- [CO] Cerebras customer concentration:
  - MBZUAI (Abu Dhabi) was 38% of Cerebras's Q3 2026 revenue (70% in Q3 2025).
  - G42 was 7% (14% in Q3 2025).
  - Cerebras issued G42 penny warrants in Dec 2025 (1,857,516 shares) and Apr 2026 (1,655,975 shares); both were exercised.
  - — [Cerebras 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm)
  - G42 had been 87% of Cerebras revenue in H1 2024. — [CNBC, 14 Jan 2026](https://www.cnbc.com/2026/01/14/cerebras-scores-openai-deal-worth-over-10-billion.html)
- [CO] NVIDIA:
  - Its "AI Clouds, Industrial & Enterprise" revenue was $40.3B in Q2 FY27, driven partly by "sovereign customers".
  - It announced Korea "sovereign AI" partnerships with SK Telecom, NAVER and Brookfield.
  - HUMAIN appears in the release only as a DRIVE robotaxi partner.
  - — [NVIDIA Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm); [NVIDIA CFO commentary Q2 FY27, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27cfocommentary.htm)

### Inferences
- Large buyers' filings support multi-vendor demand. Hyperscalers and Meta disclose GPU and ASIC mixes.
- Neocloud demand for NVIDIA is partly structural: customer contracts specify NVIDIA (CoreWeave).
- Much buyer demand is now expressed as long-dated leases and take-or-pay commitments, not capex.

### Gaps
- Meta's reported Feb 2026 multiyear NVIDIA deal and its MTIA status were not verified.
- Meta–Nebius and Meta–Google Cloud contract values were not verified.
- HUMAIN's NVIDIA, AMD and AWS commitments, the Stargate UAE/G42 1 GW status, and US export approvals to UAE and Saudi buyers were not verified; the search budget was exhausted.
- NVIDIA's reported investment in xAI's 2025 round was not verified.

---

## 4. Hyperscaler capex: 2024 actual, 2025 actual, 2026 guidance/latest; statements on custom chips vs NVIDIA GPUs

### Takeaway
On reported cash capex, the four US hyperscalers roughly doubled from 2024 to 2025 and are guiding to roughly another doubling in 2026.

2026 guidance or latest:
- Alphabet: $195–205B
- Amazon: about $220B
- Meta: $135–145B
- Microsoft: about $170B for calendar 2026

Oracle guides FY2027 (to May 2027) to $90–95B gross.

Every hyperscaler with its own chip (Google TPU, Amazon Trainium, Microsoft Maia) now publicly claims price-performance or efficiency advantages over "leading GPU-based systems" or "alternatives". All of them also continue to deploy NVIDIA, and some deploy AMD.

### Cited Findings

**Capex figures (cash "purchases of / additions to property and equipment" unless noted) [BUY]**

| Company | 2024 actual | 2025 actual | 2026 latest / guidance |
|---|---|---|---|
| Alphabet | $52.5B | $91.4B | 9M-2026 $132.0B; Q3 2026 $51.4B; FY2026 guidance **$195–205B**, held on 28 Oct 2026 (range set at Q2 2026; earlier ranges were lower) |
| Amazon | $83.0B | $131.8B | 9M-2026 $175.7B (Q3 $77.3B gross); 2026 cash capex **about $220B**; "meaningfully more in 2027" |
| Meta | $37.3B ($27.0B in 2023) | $69.7B; $72.22B including finance-lease principal | 9M-2026 $83.1B; Q3 2026 $34.91B including finance leases; 2026 guidance **$135–145B** (narrowed from $130–145B on 21 Oct 2026) |
| Microsoft (FY ends 30 Jun) | FY2024 $44.5B | FY2025 $64.6B | FY2026 $115.9B; Q1 FY27 $39.4B cash ($45.2B including finance leases); "for the calendar year, spend should be approximately $170 billion" |
| Oracle (FY ends 31 May) | FY2025 $21.2B | FY2026 $55.7B | Q1 FY27 $28.5B; FY2027 guidance **$90–95B**, with "not more than $70 billion in net cash CapEx" |

Sources:
- Alphabet: [Alphabet 10-K FY2025, filed 5 Feb 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm); [Alphabet 10-Q Q3 2026, filed 29 Oct 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm); [CNBC, "Alphabet sinks 10% as it holds 2026 capex unchanged…," 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)
- Amazon: [Amazon 10-K FY2025, filed 6 Feb 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000004/amzn-20251231.htm); [Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm); [Amazon Q3 2026 call, 30 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- Meta: [Meta 10-K FY2025, filed 29 Jan 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026003942/meta-20251231.htm); [Meta Q3 2026 release (Ex. 99.1), 21 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001326801/000162828026066700/meta-09302026xexhibit991.htm); [Meta 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1326801/000162828026066773/meta-20260930.htm)
- Microsoft: [Microsoft 10-K FY2026, filed 29 Jul 2026](https://www.sec.gov/Archives/edgar/data/789019/000119312526323660/msft-20260630.htm); [Microsoft 10-Q Q1 FY27](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm); [Microsoft call, 29 Oct 2026](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)
- Oracle: [Oracle 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1341439/000119312526277521/orcl-20260531.htm); [Oracle Q1 FY27 call, 11 Sep 2026](https://www.fool.com/earnings/call-transcripts/2026/09/11/oracle-orcl-q1-2027-earnings-call-transcript/); [CNBC, 10 Sep 2026](https://www.cnbc.com/2026/09/10/oracle-orcl-q1-earnings-report-2027.html)

**Other hyperscaler data points**
- [BUY] Alphabet's long-term debt was $125.1B at 30 Sep 2026, against $46.5B at 31 Dec 2025. Free cash flow was negative $9.1B in Q3 2026 (CNBC). Inventory, which "consists primarily of hardware related to TPU systems for sale to enterprise customers and consumer devices", was $13.3B, against $2.4B at 31 Dec 2025. — [Alphabet 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm); [CNBC, 28 Oct 2026](https://www.cnbc.com/2026/10/28/alphabet-googl-earnings-q3-2026.html)
- [CO] Backlogs at 30 Sep 2026:
  - Alphabet $567.7B, of which Google Cloud $560.8B;
  - AWS $578B;
  - Microsoft commercial RPO $677B.
  - — [Alphabet 10-Q](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm); [Amazon Q3 call](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/); [Microsoft 10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm)

**Statements on custom chips vs NVIDIA GPUs**
- [BUY/CO] **Google**, 28 Oct 2026:
  - "TPU 8t and 8i offer up to 2.7 times better training performance and 80% better inference price performance." The baseline is not stated in the transcript excerpt.
  - "Nearly 100 customers use TPUs today."
  - TPU system sales have begun: "some system sales recorded as revenue… more… through 2027."
  - Google also lists "the latest Nvidia GPUs" in its infrastructure.
  - — [Alphabet Q3 call transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037)
- [BUY/CO] **Amazon**, 30 Oct 2026:
  - "Trainium, with the meaningful advantage it has in price performance versus other alternatives…"
  - "revenue commitments for Graviton and Trainium have each increased more than 20x year-over-year."
  - "the majority and most of Bedrock today is being run on top of Trainium."
  - Amazon plans to offer Trainium outside AWS "late in 2027". NVIDIA is not named.
  - — [Amazon Q3 call transcript](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- [BUY/CO] **Microsoft**, 29 Oct 2026: Maia 300 delivers "40% more tokens per watt compared to the leading GPU-based systems". Microsoft also deploys NVIDIA (Vera Rubin) and AMD. — [Microsoft Q1 FY27 call](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)
- [BUY] **Anthropic**, S-1/A: "We can select chips based on the best price-performance and efficiency characteristics for each workload." It uses Trainium, TPUs, NVIDIA GPUs and AMD GPUs. — [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
- [CO] **NVIDIA**, 25 Nov 2025, on X:
  - "NVIDIA is a generation ahead of the industry — it's the only platform that runs every AI model and does it everywhere computing is done."
  - It offers "greater performance, versatility, and fungibility than ASICs."
  - The statement responded to The Information's report of Meta–Google TPU talks.
  - Google said demand was accelerating for both TPUs and NVIDIA GPUs.
  - — [CNBC, "Nvidia says its GPUs are a 'generation ahead' of Google's AI chips," 25 Nov 2025](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html)

### Inferences
- Sum of 2026 guidance for Alphabet, Amazon, Meta and calendar-2026 Microsoft: about $720–740B (calc; periods and definitions differ).
- The custom-chip claims are each benchmarked against different, often unnamed, baselines. They are not directly comparable with each other or with NVIDIA's claims.
- Buyer behaviour (multi-sourcing, Trainium and TPU external sales) is consistent with the custom-chip claims. Buyers' continued NVIDIA deployments are consistent with NVIDIA's.

### Gaps
- Microsoft's FY2026 capex including finance leases was not extracted; the cash figure is shown.
- Meta's and Alphabet's 2027 numbers are not yet guided.
- Independent benchmarks comparing TPU, Trainium, Maia and NVIDIA were not obtained.

---

## 5. Circular and vendor financing: NVIDIA, AMD, Broadcom, Google, Amazon (and Microsoft, Cerebras), GPU-backed debt, and regulator commentary

### Takeaway
Vendor-to-customer financing is now disclosed in vendors' own filings. NVIDIA's guarantees have a maximum gross exposure of $108.5B. NVIDIA also has $36B of six-year cloud-buyback commitments to "AI clouds". Its non-marketable equity investments rose to $47.9B. AMD has issued penny warrants for up to 320M shares to two customers. Broadcom offers an "AI XPV" financing platform with possible residual value guarantees and has a $42B note facility for Anthropic. Google's data-center backstops (credit derivatives) nearly tripled, from $16.9B to $48.0B notional. Amazon holds $143.7B of Anthropic and OpenAI equity.

The Federal Reserve's 13 Nov 2026 Financial Stability Report:
- explicitly describes a "circular financing" dynamic;
- estimates more than $1.1T of outstanding advanced-computing public debt;
- estimates more than $2T of undiscounted take-or-pay and residual-value-guarantee obligations.

### Cited Findings

**NVIDIA [CO]**
- From the [NVIDIA 10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm):
  - **Guarantees:** maximum gross exposure of $108.5B, made up of the $105B SB Energy/OpenAI cap plus $3.5B of land, power and shell guarantees for AI cloud partners' leases. Partners hold $712M in escrow.
  - **AI cloud agreements**, a "new business model" in Q2 FY27: AI clouds buy NVIDIA infrastructure, and NVIDIA commits to cloud service agreements, typically six years, totalling **$36B** at 26 Jul 2026. The AI clouds "can unilaterally stop providing to us and sell to third-party customers at more advantageous rates". NVIDIA may share revenue.
  - **Other commitments:**
    - cloud service agreements for R&D: $29B;
    - data center leases not commenced: $25B;
    - third-party data center leases not commenced: $20B;
    - equity investments: $25B "subject to certain contingencies";
    - supply and capacity: $279B (up from $119B the prior quarter).
  - **Investments:**
    - non-marketable securities of $51.2B at 26 Jul 2026, against $22.3B at 25 Jan 2026;
    - non-marketable equity carrying value of $47.9B;
    - net additions of $31.0B in H1 FY27;
    - $3.3B of equity-method investments in "infrastructure financiers".
- [CO] In Jan 2026 NVIDIA bought $2.0B of CoreWeave shares at $87.20. — [CoreWeave 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm)
- [CO] NVIDIA's FY2026 10-K, filed 25 Feb 2026:
  - It provided $3.5B of land, power and shell guarantees "to early-stage companies… in exchange for warrants".
  - "We have been asked to offer financing arrangements to support our customers'… buildout… We have not entered into any financing arrangements."
  - Multi-year cloud service commitments were $27B.
  - The non-exclusive Groq license cost $13.0B paid at closing plus $4B payable within a year.
  - — [NVIDIA 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
- [BUY] NVIDIA is buying $10.0B of Anthropic stock in the IPO private placement. — [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
- [PRESS-U] The Information reported that CFO Colette Kress opposed the $105B OpenAI guarantee; CNBC said it had not verified this. — [CNBC live blog, "Nvidia CEO Jensen Huang resigns: Live updates," 12 Nov 2026](https://cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
- [CO] On 12 Nov 2026 Huang resigned as CEO and director, effective immediately. Kress became interim CEO while remaining CFO, and Harvey C. Jones became the first Chair. No reason was given. The board said customer commitments and the roadmap "continue without interruption". — [NVIDIA Newsroom, "NVIDIA Announces CEO Transition," 12 Nov 2026](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)
  - Press coverage tied the resignation to reports about Huang's personal conduct; those reports are not detailed here. — [CNBC live blog, 12 Nov 2026](https://cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)
- [CO via press; article not read in full] Huang reportedly rejected the "circular financing" label for the Ohio guarantee, saying OpenAI will pay the lease. — [Data Center Knowledge, Aug 2026](https://www.datacenterknowledge.com/data-center-construction/nvidia-backs-openai-s-ohio-data-center-buildout-with-105b-guarantee)

**AMD [CO]**
- From the [AMD 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm):
  - Warrants were issued to two customers in Oct 2025 (OpenAI) and Feb 2026 (Meta), each for up to 160M shares at $0.01; 320M combined.
  - At 26 Sep 2026 no warrant shares had vested.
  - The warrant liability was $1.2B, and Q3 2026 included a $1.2B non-cash remeasurement charge.
  - Weighted-average fair value was $178.58 per share "as most market conditions had been met".
  - $4.5B of unrecognized grant-date fair value will be recorded as a reduction of revenue.
- [BUY] AMD has committed up to $5.0B of equity to Anthropic, tied to MI450 delivery milestones, and $2.5B in the IPO placement. — [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)

**Broadcom [CO]**
- From the [Broadcom 10-Q, quarter ended 2 Aug 2026, filed 10 Sep 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm):
  - The "AI XPV platform" with "sophisticated financial partners" is meant "to enable more than 20 gigawatts in compute capacity" of Broadcom XPUs "for the leading frontier AI labs through 2028". It "bridges the gap between the current cash flows of the leading frontier AI labs and significant upfront investments". Broadcom "may provide residual value guarantees".
  - Customers seek "to lease our custom AI accelerators… or requir[e] us to purchase and then lease to them full AI racks".
  - The top five end customers were about 55% of net revenue in the quarter.
- [BUY] Anthropic's leases with Broadcom ($161.2B rent) and the $42.0B Broadcom note facility. Broadcom assigned lease portions to a special-purpose financing entity in Oct 2026. — [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)

**Google / Alphabet [CO]**
- Data-center backstops, accounted for as credit derivatives: notional **$48.0B** at 30 Sep 2026, against $16.9B at 31 Dec 2025. Terms run up to 15 years, and Google may assume the leases on default.
- Energy financial guarantees: $16.2B, against $5.7B at 31 Dec 2025.
- Crux AI joint venture with Blackstone: Alphabet committed up to $10.0B of data-center and energy backstops.
- Equity derivatives: $21.1B, including "$20.0 billion of future capital funding commitments with a private company contingent upon… milestones through 2030". This matches the size of Anthropic's $20.0B Google 2026 NPA.
- — [Alphabet 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000084/goog-20260930.htm); [Alphabet 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1652044/000165204426000018/goog-20251231.htm)
- [BUY] Google is buying $10.0B of Anthropic stock in the IPO placement, which reduces the NPA from $20B to $10B. — [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)

**Amazon [CO]**
- Investments in Anthropic:
  - $8.0B of Anthropic convertible notes (2023–2025), with a fair value of $146.2B at 30 Sep 2026;
  - $5.0B of Series G (Q2 2026);
  - Anthropic nonvoting preferred carried at $92.5B;
  - a facility "not to exceed $20.0 billion", made available as compute delivery milestones are met;
  - upward fair-value adjustments of $62.8B in 9M-2026.
- Investment in OpenAI: $50.0B of Series C (2026).
- — [Amazon 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)

**Microsoft [CO]**
- About 24% of OpenAI. It received $10.0B of revenue from OpenAI in Q1 FY27. It is buying $1.0B in Anthropic's IPO placement. — [Microsoft 10-Q](https://www.sec.gov/Archives/edgar/data/789019/000119312526436133/msft-20260930.htm); [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)

**Cerebras [CO]**
- OpenAI lends Cerebras $1.0B and receives warrants. G42 received penny warrants. — [Cerebras 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm)

**GPU-backed and SPV debt [BUY]**
- **CoreWeave:**
  - recourse debt of $41.6B at 30 Sep 2026, against $20.7B at 31 Dec 2025;
  - plus the non-recourse DDTL 4.0 of $4.6B;
  - special-purpose subsidiaries' debt "secured by $22.2 billion of non-current assets, primarily… property and equipment";
  - Q3 interest expense up 173% year on year.
  - — [CoreWeave 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm)
- **SpaceXAI:** $12.9B of Valor GPU-lease debt (see Section 3).
- **Anthropic:** Broadcom equipment leases secured by the equipment.
- **Nscale:** GPU financing is a condition of its contract (see Section 2).

**Regulators and central banks [REG]**
- **Federal Reserve, Financial Stability Report, 13 Nov 2026**, Box 2.2 "Leverage in the Data Center Buildout":
  - "Advanced computing–related debt issuance rose to more than $680 billion by October 2026, about a fivefold increase from $130 billion in all of 2023."
  - Advanced computing's share of nonfinancial investment-grade issuance rose from under 6% (2023) to about 31% (2026).
  - Outstanding public advanced-computing debt is more than $1.1T (Oct 2026).
  - Not-yet-commenced leases of more than $1T (undiscounted) and take-or-pay contracts and residual value guarantees of more than $2T (undiscounted). This covers Amazon, Alphabet, Broadcom, Meta, Microsoft, Nvidia and Oracle.
  - "GPU makers often provide a guaranteed residual value of the GPU collateral… supplemented with equity investments… which create a 'circular financing' dynamic."
  - The largest US bank holding companies have close to $1T of exposure to these firms, special-purpose entities, private credit vehicles and utilities.
  - The survey found AI the top-cited risk, with "circular financing arrangements" named.
  - — [Federal Reserve, Financial Stability Report, November 2026 (PDF), 13 Nov 2026](https://www.federalreserve.gov/publications/files/financial-stability-report-20261113.pdf)
- **Federal Reserve FSR, May 2026:** respondents cited AI "equity valuations; that capital expenditures are increasingly funded by debt, creating leverage". — [Fed FSR, 8 May 2026](https://www.federalreserve.gov/publications/files/financial-stability-report-20260508.pdf)
- **Federal Reserve FSR, Nov 2025:** "a turn in the prevailing sentiment toward AI… could lead to a correction in risk assets." — [Fed FSR, 7 Nov 2025](https://www.federalreserve.gov/publications/files/financial-stability-report-20251107.pdf)
- **Bank of England FSR, July 2026:**
  - "AI-related companies' use of credit markets has accelerated rapidly" across "public markets, private credit, leveraged and structured finance".
  - "This pace of investment is unprecedented historically."
  - "Increasing complexity and opacity in debt structures used could increase risks to financial stability."
  - Valuations "have also become more stretched".
  - — [Bank of England, Financial Stability Report, 7 Jul 2026](https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026)
- **IMF GFSR, April 2026:** "stretched valuations and concentration — particularly in artificial intelligence related firms — raise downside risks." The Oct 2025 GFSR summary page refers only generally to "stretched asset valuations". — [IMF GFSR April 2026, 14 Apr 2026](https://www.imf.org/en/publications/gfsr/issues/2026/04/14/global-financial-stability-report-april-2026); [IMF GFSR Oct 2025](https://www.imf.org/en/publications/gfsr/issues/2025/10/14/global-financial-stability-report-october-2025)
- **Market reaction:** on 12 Nov 2026 NVIDIA closed down 4.3%, CoreWeave fell about 12% and Nebius about 17% after the CEO change. — [CNBC live blog, 12 Nov 2026](https://cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html)

### Inferences
- The "circular" pattern is now visible in primary filings. Vendors (NVIDIA, AMD, Broadcom, Google, Amazon, Microsoft) are simultaneously equity holders, lenders or guarantors, and suppliers to the same buyers (OpenAI, Anthropic, Meta, CoreWeave, AI clouds).
- Vendor revenue therefore partly depends on vendor-provided balance-sheet support. The Fed notes this shifts risk onto the large firms' off-balance-sheet obligations.
- NVIDIA said in its Feb 2026 10-K that it had "not entered into any financing arrangements". By Aug 2026 it carried $108.5B of guarantees and $36B of capacity-buyback commitments. Whether these fall within its definition of "financing arrangements" is not stated.

### Gaps
- No Moody's or S&P rating actions or commentary were retrieved; the search budget was exhausted. Oracle's filings note rating sensitivity but give no rating.
- The IMF's October 2026 GFSR was not listed on the IMF GFSR page when fetched on 14 Nov 2026.
- Academic commentary was not retrieved.
- NVIDIA's investment in xAI and its 2025 $6.3B CoreWeave capacity backstop were not verified in documents fetched.
- Google's specific 2025 TeraWulf/Cipher/Fluidstack backstops are not itemized in filings fetched; only aggregates are disclosed.

---

## 6. Export controls and the China market as tests of company claims

### Takeaway
The vendors' own 2026 filings show the US moved from banning to licensing China sales:
- H20 licences from Aug 2025;
- H200 "small amounts" from Feb 2026, with US inspection and an effective 25% tariff;
- AMD MI308 and later MI325 licences.

China's government then restricted purchases. NVIDIA says it is "effectively foreclosed" from China's data-center compute market, took a $0.4B H200 charge, and guides Q3 FY27 with no China data-center compute revenue. Even so, NVIDIA's geographic table shows China (including Hong Kong) revenue of $7.9B in Q2 FY27, by headquarters of direct customers. That table is not the same measure as data-center compute sold into China.

### Cited Findings
- [CO describing REG actions] NVIDIA timeline, from the [NVIDIA 10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm):
  - **April 2025:** a licence requirement for H20 led to a $4.5B charge in Q1 FY26.
  - **May 2025:** the US government announced it would rescind the AI Diffusion IFR; the replacement rule's "scope, timing, and requirements… remain uncertain" as of Aug 2026.
  - **Oct 2025:** the Senate passed the GAIN AI Act in the NDAA.
  - **From Aug 2025:** H20 licences were granted, but "such sales were restricted by the PRC government, and we were unable to sell our H20 inventory".
  - **From Feb 2026:** licences were granted "to ship small amounts of H200 products to specific China-based customers, but such sales were restricted by the PRC government". There was a $0.4B H200 charge in H1 FY27. Shipments are "less than 1% of Data Center revenue". Licences require inspection in the US, so each unit carries a 25% tariff that NVIDIA has been "unable to pass along".
- [CO] NVIDIA's own assessment:
  - "We were effectively foreclosed from competing in China's data center computing/compute market, and our effective foreclosure from the China market helped our competitors build larger developer and customer ecosystems to challenge us worldwide."
  - The Q3 FY27 outlook ($108.0B ±2%) "assumes no China Data Center compute revenue".
  - — [NVIDIA 10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm); [NVIDIA CFO commentary, 26 Aug 2026](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27cfocommentary.htm)
- [CO] NVIDIA revenue from China (including Hong Kong), by headquarters of the direct customer:
  - **$7.88B in Q2 FY27**, against $3.99B in Q2 FY26;
  - $12.43B in H1 FY27, against $13.64B in H1 FY26.
  - NVIDIA notes that "the end customer and shipping location may be different".
  - — [NVIDIA 10-Q Q2 FY27](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- [CO] AMD:
  - MI308 was restricted in April 2025, causing inventory charges in 2025. Licences were later granted, and shipping began at the end of fiscal 2025.
  - In H1 2026 the US government granted licences to ship MI325 to certain China-based customers, subject to US inspection and therefore a 25% tariff.
  - China sales "depend on customer demand, China's import control rules and our ability to obtain licenses".
  - — [AMD 10-Q Q3 2026](https://www.sec.gov/Archives/edgar/data/2488/000000248826000191/amd-20260926.htm)
- [CO] NVIDIA names Huawei as a competitor in GPUs and custom chips, CPUs and networking. — [NVIDIA 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)

### Inferences
- **What each side said vs what happened.** The US relaxed controls (licensing H20 and H200, with a revenue or tariff take), but sales did not follow because the Chinese government restricted purchases (NVIDIA's account). NVIDIA's claim that it is "foreclosed" is consistent with its sub-1% Hopper shipments to China and its guidance. It sits alongside a growing China-headquartered revenue line that likely reflects non-data-center products and/or China-headquartered customers buying for use elsewhere. This is not established in the filing.
- No buyer-side Chinese disclosure (ByteDance, Alibaba, Tencent and others) was obtained to test either side.

### Gaps
None of the following were obtained or verified; the search budget was exhausted:
- the text of the BIS/Federal Register H200 rule;
- the status of the Chip Security Act and of location-verification requirements;
- the final status of the GAIN AI Act;
- CAC, MOFCOM, SAMR or customs statements;
- official US estimates of Huawei Ascend output (the lead "≤200,000 AI chips in 2025", attributed from memory to Commerce testimony in June 2025, is **unverified**);
- Huawei's own capability claims (Atlas 950/960 SuperPoD);
- Jensen Huang's "95% to 0%" China-share remarks.

---

## 7. Do the buyers' own disclosures support the vendors' claims? Vendor-by-vendor check

### Takeaway
For NVIDIA, Broadcom, Google TPUs, Amazon Trainium, AMD and Cerebras, buyer filings generally **confirm** that the named customers exist and that the contracts are large. In several cases they show **larger** dollar commitments than vendors announced. Three qualifiers apply:
- part of the demand is supported by the vendors' own financing;
- several contracts are contingent or cancellable;
- delivery timelines have slipped.

No buyer disclosures were found for Huawei.

### Cited Findings
- **NVIDIA.** NVIDIA-GPU buyers' filings confirm large NVIDIA-based commitments:
  - Anthropic, with Microsoft $47.2–49.2B, SpaceXAI up to $120.5B, Nscale about $44.6B and Lambda about $41.3B;
  - CoreWeave, with $132.3B of RPO, all on NVIDIA GPUs;
  - Meta, via CoreWeave, about $35B across two order forms ($14.2B in Sep 2025 and $21.0B in Mar 2026; calc). Any overlap from the option exercise is not stated.
  - — [Anthropic S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm); [CoreWeave 10-Q](https://www.sec.gov/Archives/edgar/data/1769628/000176962826000465/crwv-20260930.htm)
  - [CO] Concentration and support: one direct customer was 16% of Q2 FY27 revenue. NVIDIA supports demand through its $36B AI-cloud buyback commitments and $108.5B of guarantees. — [NVIDIA 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
- **AMD.**
  - [BUY] Anthropic confirms an MI450 deal worth more than $20B.
  - [CO] Meta's binding 1 GW is in AMD's 8-K.
  - [CO] OpenAI and Meta tranches were not vested at 26 Sep 2026.
  - [CO] AMD's Q3 2026 Data Center revenue was a record $8.5B, up 97%, on the MI450 launch.
  - — [AMD Q3 2026 release](https://www.sec.gov/Archives/edgar/data/2488/000000248826000188/q32026991.htm)
- **Broadcom.**
  - [CO via press] Broadcom expects Anthropic to be its largest XPU customer in 2027. [BUY] Anthropic's $161.2B of leases supports this, but they are financed through Broadcom's $42B note facility and special-purpose assignments.
  - [CO via press] Broadcom expects 1.3 GW of OpenAI deployment in 2027, against the 10 GW announced. No OpenAI-side contract value is public.
  - [CO via press] Broadcom projected AI semiconductor revenue of about $58B in FY2026, $115B in FY2027 and $230B in FY2028 (company projections). — [Yahoo Finance, Sept 2026](https://finance.yahoo.com/technology/ai/articles/broadcom-just-named-next-ai-222044865.html)
- **Google TPU.**
  - [BUY] Anthropic's Google commitment of at least $121.3B, plus an estimated $125–150B, confirms Google's TPU demand claims.
  - [CO] Google says "nearly 100" TPU customers.
  - [CO] TPU-systems inventory rose to $13.3B.
  - [CO] No other named external TPU buyer's filing was found. Meta's involvement is "TorchTPU" software collaboration.
- **Amazon Trainium.**
  - [BUY] Anthropic commits at least $110B.
  - [CO] OpenAI's $100B expansion "includes contractual obligations related to the performance of AWS chips", with about 2 GW of Trainium (press).
  - Amazon does not disclose standalone Trainium revenue.
- **Cerebras.**
  - [CO] OpenAI was 34% of Q3 2026 revenue.
  - [CO] MBZUAI and G42 together were 45%.
  - [CO] A June 2026 AWS agreement and H2-2026 Oracle and Microsoft hardware agreements.
  - [CO] Cerebras is short on delivery to OpenAI.
  - — [Cerebras 10-Q](https://www.sec.gov/Archives/edgar/data/2021728/000162828026073494/cbrs-20260930.htm)
  - [CO] Cerebras IPO priced at $185 on 14 May 2026. — [Cerebras 424B4](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
- **Huawei.** No buyer disclosures were obtained.

### Inferences
- "Demand" claims are best tested against buyers' take-or-pay commitments and RPO. These are large and real, but increasingly long-dated: Anthropic's commitments run to 2045, Microsoft's leases to FY2034, Meta's to 2036.
- Some of these commitments are cancellable or financing-contingent, and some are underwritten by the vendors themselves.

### Gaps
- Huawei Ascend buyer disclosures were not obtained.
- OpenAI's own commitments schedule is not public.
- HUMAIN and Stargate UAE buyer-side data were not obtained.

---

## 8. (a) Log of cross-company claim contradictions and tensions (dated and sourced)

### Takeaway
The most substantive contradictions found are:
- NVIDIA's $100B "commitment" to OpenAI versus its later "never a commitment";
- NVIDIA's "generation ahead of ASICs" claim versus Google, Microsoft and Amazon claiming better price-performance or efficiency for their own chips;
- the drift in OpenAI's compute-spend figures;
- vendor deployment timelines versus later disclosures;
- Oracle versus Bloomberg/Reuters on Abilene;
- the funding of Amazon's "conditional" OpenAI tranche.

Several apparent conflicts are partly explained by differing definitions: run-rate vs GAAP revenue, HQ-based vs shipment-based China revenue, and vendor-announced GW vs buyer-disclosed dollars.

### Cited Findings
1. **NVIDIA–OpenAI $100B.**
   - [CO] 22 Sep 2025: NVIDIA "intends to invest up to $100 billion"; details to be finalized "in the coming weeks". — [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/openai-and-nvidia-announce-strategic-partnership-to-deploy-10gw-of-nvidia-systems)
   - [CO via press] 1 Feb 2026: Huang said "It was never a commitment." — [Fortune, 2 Feb 2026](https://fortune.com/2026/02/02/jensen-huang-nvidia-ceo-on-openai-investment-never-a-commitment/)
   - [CO] 25 Feb 2026: NVIDIA was still "finalizing", with "no assurance". — [NVIDIA 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm)
   - Outcome: a $30B equity investment (27 Feb 2026) and a $105B lease guarantee (Aug 2026).
   - **Lead check: the $100B LOI was not finalized as such (confirmed).**
2. **NVIDIA "generation ahead… greater performance, versatility, and fungibility than ASICs"** (25 Nov 2025, [CNBC](https://www.cnbc.com/2025/11/25/nvidia-says-its-gpus-are-a-generation-ahead-of-googles-ai-chips.html)) **versus:**
   - Google, 28 Oct 2026: TPU 8t/8i "up to 2.7 times better training performance and 80% better inference price performance". — [transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-alphabet-q3-2026-profit-miss-sparks-10-afterhours-drop-93CH-4981037)
   - Microsoft, 29 Oct 2026: Maia 300 "40% more tokens per watt compared to the leading GPU-based systems". — [transcript](https://www.fool.com/earnings/call-transcripts/2026/10/29/microsoft-msft-q1-2027-earnings-call-transcript/)
   - Amazon, 30 Oct 2026: Trainium's "meaningful advantage… in price performance versus other alternatives". — [transcript](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
   - Caveat: the baselines differ and are not stated, so the claims are not directly comparable.
3. **OpenAI compute spend.**
   - About $1.4T for about 30 GW (28 Oct 2025, Reuters/StreetInsider).
   - About $600B through 2030 (Feb 2026, CNBC, unnamed sources).
   - About $856B for 2026–2030 (July 2026 presentation, FT via TNW, 19 Sep 2026).
   - About $750B (an unverified WSJ attribution).
   - — sources in Section 1.
4. **NVIDIA financing posture.**
   - "We have not entered into any financing arrangements" (10-K, 25 Feb 2026).
   - Versus $105B of OpenAI lease guarantees (Aug 2026), $36B of AI-cloud buyback commitments and $3.5B of guarantees for warrants (10-Q, 26 Aug 2026).
   - The Fed (13 Nov 2026) describes GPU makers providing "guaranteed residual value of the GPU collateral" and a "circular financing" dynamic.
   - Huang reportedly rejected the "circular" label (DCK, Aug 2026; article not read in full).
   - The tension may be definitional.
5. **Amazon's "conditional" $35B to OpenAI.**
   - 27 Feb 2026: Amazon put in $15B initially, with $35B "in the coming months when certain conditions are met". — [CNBC](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)
   - Commentary claimed the conditions were tied to an IPO or AGI. — [SaaStr](https://www.saastr.com/openais-122b-vc-round-is-vendor-deals-contingent-capital-and-a-guaranteed-return-it-arguably-cant-afford/)
   - Versus Amazon's 10-Q: $13.7B (Q2) and $21.3B (Q3) invested, so the full $35B was funded by 30 Sep 2026, with no OpenAI IPO and no explanation of which condition was met. — [Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
6. **Oracle vs Bloomberg/Reuters on Abilene** (Mar 2026).
   - Reports: the Abilene expansion of about 600 MW was dropped because of financing and OpenAI's shifting needs.
   - Oracle: the reports are "false and incorrect", and the 4.5 GW is on track.
   - Bloomberg's correction: the expansion lease is not proceeding, but the 4.5 GW remains on track.
   - — [Yahoo/Tom's Hardware, 9 Mar 2026](https://finance.yahoo.com/news/oracle-hits-back-stargate-data-172802489.html)
7. **Timelines vs delivery.**
   - NVIDIA–OpenAI: first GW "H2 2026" (Sep 2025), against the first Ohio phase in FY2029 (NVIDIA 10-Q).
   - Broadcom–OpenAI: deploy "starting late next year" (Oct 2025), against "small prototype" late 2026 and a ramp in 2027 (Jun/Sep 2026).
   - AMD–OpenAI: first GW "H2 2026", against no warrant tranche vested at 26 Sep 2026. AMD nonetheless says OpenAI runs workloads on the first Helios racks (3 Nov 2026).
   - Cerebras–OpenAI: first 250 MW by end-2026 (press), against a delivery shortfall with service credits from 1 Oct 2026 and delays into 2027 (10-Q).
   - Microsoft, 29 Oct 2026: third-party capacity deliveries were "delayed" (supplier unnamed).
   - Lambda failed to secure a facility lease on time (Anthropic S-1/A).
   - — sources in Sections 1 and 2.
8. **Cerebras vs NVIDIA/Groq on speed.**
   - [CO] Cerebras says it is "up to 15 times faster than leading GPU-based solutions" and the "fastest inference platform on the market, as benchmarked by Artificial Analysis". — [Cerebras 424B4, 14 May 2026](https://www.sec.gov/Archives/edgar/data/2021728/000162828026035214/cerebras-424b4.htm)
   - [CO] Versus NVIDIA's licensing of Groq's LPU technology (about $17B; Dec 2025) and its announcement that "NVIDIA Groq 3 LPX, the interactive AI inference accelerator, is now in full production" (26 Aug 2026). — [NVIDIA 10-K](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000021/nvda-20260125.htm); [NVIDIA Q2 FY27 release](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000073/q2fy27pr.htm)
   - NVIDIA published no head-to-head speed figure in the documents found.
9. **NVIDIA "foreclosed from China" vs reported China revenue.**
   - [CO] NVIDIA says it is "effectively foreclosed" from China's data-center compute market, and its outlook assumes no China data-center compute revenue.
   - [CO] Yet its China (including Hong Kong) revenue by customer headquarters was $7.88B in Q2 FY27, against $3.99B a year earlier.
   - Not like-for-like: the geographic figure includes non-data-center products and is based on HQ location. — [NVIDIA 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
   - Huang's oral China-share claims were not retrieved.
10. **US policy vs Chinese policy on H20/H200.**
    - [CO describing REG] The US granted licences (H20 from Aug 2025; H200 "small amounts" from Feb 2026).
    - The PRC restricted the same purchases. — [NVIDIA 10-Q](https://www.sec.gov/Archives/edgar/data/1045810/000104581026000075/nvda-20260726.htm)
11. **Broadcom–Anthropic capacity figures differ by document.**
    - About 3.5 GW from 2027 (Broadcom filing, Apr 2026, per DCK).
    - About 5 GW of TPU v8i in 2027 plus a path to 10 GW in 2028 (Broadcom call, Sep 2026).
    - $161.2B of lease rents (Anthropic S-1/A).
    - Different units, dates and possibly scopes.
12. **Microsoft–Anthropic size.**
    - $30B of Azure (Nov 2025 press).
    - At least $47.2B, up to $49.2B, after amendments Feb–Nov 2026 (Anthropic S-1/A).
    - An upward revision, not a conflict.
13. **Amazon–Anthropic facility size.**
    - Amazon: "aggregate facility not to exceed $20.0 billion" plus $5.0B of Series G (Amazon 10-Q).
    - Anthropic: Amazon 2026 NPA principal of $15.0B plus 19.3M Series G-2 shares at $259.14, about $5.0B (S-1/A).
    - A $5B definitional difference not reconciled in either filing.
14. **Cerebras–OpenAI value.**
    - "Over $10B" (CNBC, unnamed sources, 14 Jan 2026).
    - Versus secondary reports of more than $20B.
    - Versus Cerebras RPO of $26.1B, "significant amount" OpenAI, including pass-through costs (10-Q).
15. **Anthropic run-rate vs GAAP revenue.**
    - Run-rate of about $9B at end-2025 (Anthropic) against 2025 GAAP revenue of $4.585B (S-1/A).
    - Run-rate of about $81B at 31 Oct 2026 against Q3 GAAP revenue of about $17.0B.
    - These are different measures. One aggregator mis-attributed Anthropic's H1-2026 operating loss ($693M) and net loss ($80.7B) to OpenAI. — [AI Funding Tracker](https://aifundingtracker.com/is-openai-losing-money/) vs [Dealroom summary of Anthropic draft S-1](https://dealroom.co/news/164610-anthropic-s-draft-s-1-reveals-16-3b-revenue-80-7b-loss-and-up-to-750b-co/)
16. **NVIDIA internal (press).**
    - [PRESS-U] The Information: Kress opposed the $105B OpenAI guarantee.
    - [CO] The board said commitments "continue without interruption".
    - — [CNBC live blog, 12 Nov 2026](https://cnbc.com/2026/11/12/nvidia-jensen-huang-ceo-live-updates.html); [NVIDIA Newsroom](https://nvidianews.nvidia.com/news/nvidia-announces-ceo-transition)

### Inferences
- The largest gaps lie between announcement-day framing and later filings: "up to $100B", "10 GW", "6 GW", "$1.4T", "starting H2 2026".
- Filings, by design, convert headline figures into committed or contingent amounts, often with longer timelines.
- Custom-chip vs GPU claims are not falsifiable from the documents found, because the baselines are not disclosed.

### Gaps
None of the following were found or verified:
- AMD vs NVIDIA performance-per-dollar claim pairs (for example MI355X vs B200, InferenceMAX);
- Huawei vs NVIDIA vs US government claims on Chinese capability;
- Groq's own speed claims vs Cerebras;
- any explicit claim by one chip vendor about another vendor's delays.

---

## 9. (b) What could not be found or verified (including the user's leads)

### Takeaway
Of the four user leads:
- **Confirmed:** the OpenAI $110B → $122B round, with Amazon, NVIDIA and SoftBank as large participants.
- **Confirmed:** Anthropic's steep run-rate growth.
- **Confirmed:** the NVIDIA $100B LOI was not finalized as a $100B agreement.
- **Partly confirmed:** Altman's $1.4T is confirmed, but it is dated 28 Oct 2025 and the "eight years" wording was not located.

Regulator, export-control and Huawei items were the main casualties of the exhausted search budget.

### Cited Findings
- **Lead 1, Altman about $1.4T.**
  - Confirmed as about $1.4T and about 30 GW, reported 28–29 Oct 2025. — [Reuters via StreetInsider](https://www.streetinsider.com/Reuters/Altman+touts+trillion-dollar+AI+vision+as+OpenAI+restructures+to+chase+scale/25515962.html)
  - A November 2025 statement with "about 8 years" wording was **not verified**.
  - CNBC (27 Feb 2026) refers to "Altman's earlier $1.4 trillion infrastructure figure". — [CNBC](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html)
- **Lead 2, OpenAI 2026 round of about $100B+.**
  - **Confirmed:** $110B announced 27 Feb 2026, then $122B closed 31 Mar 2026 at $852B post-money.
  - Amazon $50B (fully funded by Q3 2026), NVIDIA $30B, SoftBank $30B.
  - — [OpenAI on X](https://x.com/OpenAI/status/2039085161971896807); [CNBC](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html); [Amazon 10-Q](https://www.sec.gov/Archives/edgar/data/1018724/000101872426000040/amzn-20260930.htm)
- **Lead 3, Anthropic run-rate steep.**
  - **Confirmed:** about $9B (end-2025), more than $30B (Apr 2026), $65B (Jul 2026), about $81B (31 Oct 2026).
  - — [Anthropic](https://anthropic.com/news/google-broadcom-partnership-compute); [CNBC](https://www.cnbc.com/2026/08/17/anthropic-says-annualized-revenue-climbed-to-65-billion-in-july.html); [S-1/A](https://www.sec.gov/Archives/edgar/data/2130357/000162828026072484/anthropicpbc-sx1ax2.htm)
  - The early-2025 figure (about $1B, from memory) was not verified.
- **Lead 4, NVIDIA–OpenAI $100B LOI not finalized.**
  - **Confirmed** (Section 8, item 1).

### Inferences
- The fact base relies on primary filings for vendor and buyer commitments, and on company statements for the claims tested. Press-only or unnamed-source items are labelled.

### Gaps
Items not found or not verified, mostly because the web-search budget was exhausted mid-task:
- **Ratings:** Moody's and S&P actions and commentary on Oracle, CoreWeave, Meta SPVs, OpenAI and Anthropic.
- **IMF:** the October 2026 GFSR was not listed on the IMF GFSR page when fetched.
- **Academic:** academic papers on circular AI financing.
- **US export-control texts:**
  - BIS/Federal Register text for the H200 licensing rule (Jan 2026);
  - Chip Security Act / location-verification status;
  - final status of the GAIN AI Act;
  - text of the AI Diffusion replacement rule.
- **China:**
  - CAC, MOFCOM, SAMR and customs statements on NVIDIA H20 and H200 and on domestic-chip mandates;
  - Chinese buyers' disclosures (ByteDance, Alibaba, Tencent).
- **Huawei:**
  - official US estimates of Ascend output (the "≤200,000 in 2025" lead is unverified);
  - Huawei's 2025–2026 roadmap and capability claims, and responses by NVIDIA and the US government.
- **Jensen Huang China-share quotes:** the "95% to 0%" and "China will win" statements (2025) were not retrieved; NVIDIA filings were used instead.
- **AMD vs NVIDIA:** performance-per-dollar claims; any company claims about rivals' delays.
- **Sovereign buyers:** HUMAIN (NVIDIA, AMD and AWS commitments; xAI's 500 MW), Stargate UAE (G42/OpenAI/Oracle 1 GW; first 200 MW status), and US export licences for UAE and Saudi shipments.
- **Meta:** the Feb 2026 NVIDIA multiyear deal, the status of the Meta–Google TPU purchase, Meta–Nebius values, and Hyperion/Blue Owl SPV terms (Meta's 10-Q shows only aggregate residual value guarantees).
- **OpenAI:**
  - audited financials;
  - the Oracle contract value (reported about $300B in 2025);
  - the Google Cloud contract value;
  - the May 2025 CoreWeave $4B tranche;
  - the WSJ 2026 quarterly figures;
  - the "nearly $50B run-rate at end-Sep 2026" claim;
  - Stargate site-by-site status other than Abilene.
- **NVIDIA:**
  - xAI investment (2025);
  - the 2025 $6.3B CoreWeave capacity agreement;
  - the 2025 Lambda leaseback;
  - Q3 FY27 results (**not yet reported**; due 17 Nov 2026).
- **Google:** itemized 2025 neocloud backstops (TeraWulf, Cipher/Fluidstack); only aggregate credit-derivative notionals are disclosed.
- **Anthropic:** the IPO pricing date and final size (**not yet happened**); Amazon's and Google's ownership percentages.

# Broadcom: custom AI accelerators (XPU/ASIC) and AI networking, fact base as of 14 November 2026

Provenance tags used on every item:
- **[CO]** Broadcom said it (filing, press release, earnings call, or an executive quoted in the press).
- **[CUST: name]** A customer or counterparty said it. These sources sit outside Broadcom but are interested parties.
- **[IV: who]** Observed or checked by a named third party that is not a party to the deal.
- **[EST: who]** Analyst or industry estimate, recorded as a data point only.
- **[PRESS-UNNAMED: outlet]** Press report that cites unnamed sources.
- **[PRESS: outlet]** Press or secondary report whose sourcing is named or unclear.
- **[CALC]** My own arithmetic from the cited figures.
- **[SUMMARY-ONLY]** I saw this only in a search-result summary and did not open the page. Confidence is lower.

Research conditions: the shared web-search budget ran out partway through. After that I only fetched known URLs: SEC EDGAR filings, earnings-call transcripts, and pages already found. investors.broadcom.com, reuters.com, axios.com, blackstone.com, openai.com and dl.acm.org refused automated fetches (HTTP 403 or blocked). Most hard numbers below therefore come from SEC filings, which I downloaded and read directly, and from call transcripts. Broadcom's fiscal 2026 ended on **1 Nov 2026**. **Q4 FY2026 results have NOT been released as of 14 Nov 2026.** EDGAR shows no Item 2.02 8-K after 2 Sep 2026, and the latest 8-K is dated 27 Oct 2026 ([SEC EDGAR filing index for CIK 1730168, accessed 14 Nov 2026](https://data.sec.gov/submissions/CIK0001730168.json)). The prior-year Q4 was reported on 11 Dec 2025.

## 1. What Broadcom makes and at what stage: custom XPUs by customer, AI networking, packaging, 2nm

### Takeaway
As of Sept 2026 Broadcom says it has **six XPU customers**, four of them named: Google, Meta, Anthropic and OpenAI. Google TPUs (Ironwood/v7, and v8 production) and Anthropic's Ironwood racks are shipping in volume. Meta MTIA is shipping, with a new generation's production shipments expected in Q4 FY2026. OpenAI's first chip, "Jalapeño", was unveiled in Jun 2026 and is in early shipments, with volume in 2027. The two other customers are unnamed and were due to begin shipments in late 2026. Networking is Tomahawk 6 (shipping since about mid-2025), Tomahawk Ultra (deploying from late FY2026) and Tomahawk 7 (taped out by Sept 2026). In Q3 FY2026, XPUs were 73% of AI semiconductor revenue.

### Cited Findings
**Business definition and scale**
- (10-K for FY2025, filed 18 Dec 2025) Broadcom describes "Custom Silicon Solutions" as "advanced technology and intellectual property ('IP') platforms for customers to design and develop application specific integrated circuits ('ASICs')… such as our custom accelerators or XPUs, for hyperscalers, companies with AI frontier models and system integrators". The platforms integrate "embedded logic, high-bandwidth memory, serializer/deserializer technology, IP cores and processor cores using advanced packaging technologies". The semiconductor portfolio includes "switches, subsystems and, in some cases, racks." [CO] — [Broadcom Form 10-K FY2025, SEC, 18 Dec 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- (Q3 FY2026 call, 2 Sep 2026) Tan: "Our 6 XPU customers are accelerating the adoption of custom accelerators." He said four of the six are "financially secure" and fund themselves, while Anthropic and OpenAI receive financing support. [CO] — [Motley Fool transcript, Broadcom Q3 FY2026 call (posted 9 Sep 2026)](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); six customers confirmed by [Investing.com transcript, Q3 FY2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)
- (Q3 FY2026, quarter ended 2 Aug 2026) "XPU shipments for the third quarter were up over 3.5x year-on-year", representing **73% of AI revenue**. AI networking revenue was "up over 2.5x year-on-year". [CO] — [Motley Fool Q3 FY2026 transcript](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); [Investing.com Q3 FY2026 transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849). That implies roughly $12.2B of XPU revenue and roughly $4.5B of networking and other AI revenue out of $16.7B [CALC].

**Google TPU**
- (8-K, 6 Apr 2026) Broadcom and Google signed "a Long Term Agreement for Broadcom to develop and supply custom Tensor Processing Units ('TPUs') for Google's future generations of TPUs and a Supply Assurance Agreement for Broadcom to supply networking and other components to be used in Google's next-generation AI racks through up to 2031." [CO] — [Broadcom Form 8-K, 6 Apr 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm)
- (Q2 FY2026 call, 3 Jun 2026) Tan said it is "a long-term agreement to develop and supply multiple generations of TPUs". He also said Google may use "some diversity of sources." [CO] — [Motley Fool transcript, Q2 FY2026 (3 Jun 2026)](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- (Q3 FY2026 call, 2 Sep 2026) Ironwood (TPU v7) "shipped in high volume" and production shipments of TPU v8i began. Tan: "Broadcom is now shipping the TPU version 8i ahead of the MediaTek version v8t", and "we are planning to deliver multi-tens of billions of dollars of TPUs annually over the next several years." [CO] — [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); the v8i/v8t wording is also in [Investing.com Q3 FY2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849). This conflicts with the press mapping; see Section 9.
- (Google, 22 Apr 2026, Cloud Next) Google announced TPU 8t (training) and TPU 8i (inference/RL) for general availability "later this year", "designed in partnership with Google DeepMind". Google's post names **no** silicon partner. [CUST: Google] — [Google blog, "Our eighth generation TPUs: two chips for the agentic era"](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
- (Wccftech, 20 Apr 2026) Reports attribute TPU 8t "Sunfish" to Broadcom and TPU 8i "Zebrafish" to MediaTek. Wccftech cites unnamed "media and supply-chain reports" and an X post by Dan Nystedt. Google has not confirmed this. [PRESS: Wccftech] — [Wccftech, "Google Splits TPUv8 Strategy Into Two Chips…", 20 Apr 2026](https://wccftech.com/google-splits-tpuv8-strategy-two-chips-broadcom-training-mediatek-inference-duties/)

**Anthropic (TPU/Ironwood racks bought through Broadcom)**
- (Q4 FY2025 call, 11 Dec 2025) "we received a $10 billion order to sell the latest TPU Ironwood racks to Anthropic". "In this quarter Q4, we received an additional $11 billion order from this same customer for delivery in late 2026." This identifies Anthropic as the "fourth XPU customer" disclosed in Sept 2025. [CO] — [Motley Fool transcript, Q4 FY2025 (12 Dec 2025)](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
- (Anthropic, 23 Oct 2025) Anthropic will use "up to one million" Google TPUs, "tens of billions of dollars", "well over a gigawatt" online in 2026. The post does not mention Broadcom. [CUST: Anthropic/Google] — [Anthropic, "Expanding our use of Google Cloud TPUs and Services", 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)
- (8-K, 6 Apr 2026) "Anthropic, beginning in 2027, will access through Broadcom approximately 3.5 gigawatts… The consumption of such expanded AI compute capacity by Anthropic is dependent on Anthropic's continued commercial success." [CO] — [Broadcom 8-K, 6 Apr 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm). Anthropic's own post says "multiple gigawatts… starting in 2027" and gives no number [CUST: Anthropic] — [Anthropic, "Anthropic expands Google and Broadcom compute deal", 6 Apr 2026](https://www.anthropic.com/news/google-broadcom-partnership-compute)
- (Q3 FY2026 call, 2 Sep 2026) 1 GW of Ironwood is deploying in 2026, "5 GW of TPU v8i in 2027", and "an incremental 10 gigawatts" in 2028. "Anthropic is on track to become our largest XPU customer in 2027 and sustain that in 2028." [CO] — [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); [Investing.com Q3 FY2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)

**Meta MTIA**
- (Q1 FY2026 call, 4 Mar 2026) "contrary to recent analyst reports, Meta's custom accelerator MTIA roadmap is alive and well. We are shipping now." [CO] — [Motley Fool transcript, Q1 FY2026 (4 Mar 2026)](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript)
- (Meta, 14 Apr 2026) The agreement "includes a commitment that exceeds 1GW, which is the first phase of a sustained, multi-gigawatt rollout". Meta is "developing and deploying four new generations of MTIA chips within the next two years". "Broadcom will work with us across chip design, advanced packaging, and networking." [CUST: Meta] — [Meta Newsroom, "Meta Partners With Broadcom to Co-Develop Custom AI Silicon", 14 Apr 2026](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/)
- (CNBC, 14 Apr 2026) The partnership is extended through 2029. Broadcom says the MTIA chips will be "the first AI silicon built on a 2-nanometer process". Meta unveiled four new MTIA versions in Mar 2026. [CO via PRESS: CNBC] — [CNBC, "Meta commits to 1 gigawatt of custom chips with Broadcom…", 14 Apr 2026](https://www.cnbc.com/2026/04/14/meta-commits-to-one-gigawatt-of-custom-chips-with-broadcom-as-hock-tan-agrees-to-leave-board.html)
- (Q2 FY2026, 3 Jun 2026) "we expect to deploy 3 gigawatts through the end of 2028". The first 1 GW order "will start delivery in the second half of 2027." (Q3 FY2026, 2 Sep 2026) "we expect production shipments of their custom MTIA accelerator" in Q4 FY2026, and "3 generations of MTIA accelerators to Meta" through 2027. [CO] — [Motley Fool Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/); [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)

**OpenAI**
- (13 Oct 2025) OpenAI and Broadcom announced a collaboration on 10 GW of custom accelerators designed by OpenAI. Broadcom handles development, networking and system integration, using Ethernet. First deployments are planned for H2/late 2026 and full deployment "by 2029". The two had worked together for 18 months beforehand. Financial terms were not disclosed. [CO/CUST via PRESS: Maginative] — [Maginative, "OpenAI and Broadcom to co-design custom AI chips, deploy 10 GW by 2029", 13 Oct 2025](https://www.maginative.com/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029). (OpenAI's own page returned 403: [openai.com announcement URL](https://openai.com/index/openai-and-broadcom-announce-strategic-collaboration/).)
- (Q1 FY2026, 4 Mar 2026) "We also now have a sixth customer. We expect OpenAI to be deploying in volume their first generation XPU in 2027." [CO] — [Motley Fool Q1 FY2026](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript)
- (24 Jun 2026) Jalapeño was unveiled as an inference "Intelligence Processor" designed end to end in about nine months with help from OpenAI's models. A physical sample was delivered that day. Tan: "small prototype development" in late 2026, "really ramp up in '27 and really going full tilt in first half '28." [CO/CUST via PRESS: CNBC] — [CNBC, "OpenAI and Broadcom reveal Jalapeno…", 24 Jun 2026](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- (Q3 FY2026, 2 Sep 2026) "Jalapeno is on track for the planned deployment of 1.3 gigawatts in 2027". There is "line of sight" to more than 5 GW in 2028 across Jalapeño and its successor. The next-generation XPU is "approaching tape-out" and a third generation is in development. Shipments are said to be ongoing. [CO] — [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); [Investing.com Q3 FY2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)

**Customer #5, the "other two" customers, and reported customers**
- (11 Dec 2025) "we acquired a fifth XPU customer… through a $1 billion order placed for delivery in late 2026". Tan declined to name it: "he's a real customer". [CO] — [Motley Fool Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). Per Constellation's account of the call, two of Broadcom's other customers "prefer to control their own destiny by building their own XPUs" [CO via PRESS] — [Constellation Research, 12 Dec 2025](https://www.constellationr.com/insights/news/broadcom-ceo-comments-highlight-build-vs-buy-ai-debate)
- (3 Jun 2026) Of the "other two customers" (beyond Google, Anthropic, OpenAI and Meta): "we expect shipments to begin in late 2026 and accelerate into 2027". Purchase orders total "$6 billion". [CO] — [Motley Fool Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- (8-K, 6 Jul 2026) Broadcom and Apple will "expand their long-standing technology collaboration through 2031" with new multi-year agreements "for Broadcom to develop and supply a range of custom ASIC silicon products for use in multiple generations of Apple products." The filing does **not** say AI or server. [CO] — [Broadcom 8-K, 6 Jul 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526295589/d84378d8k.htm)
- (Dec 2024) The Information reported that Apple was developing an AI server chip, codenamed "Baltra", with Broadcom handling networking technology, for mass production by 2026. [PRESS-UNNAMED: The Information via BNN Bloomberg] — [BNN Bloomberg, 11 Dec 2024](https://bnnbloomberg.ca/business/technology/2024/12/11/apple-is-working-on-ai-chip-with-broadcom-information-reports). A later Bloomberg-based report said completion is expected by 2027 [SUMMARY-ONLY; PRESS-UNNAMED] — [Tom's Hardware](https://www.tomshardware.com/pc-components/cpus/apple-reportedly-readies-baltra-processors-for-ai-servers)
- (~6–8 Dec 2025) The Information reported that Microsoft was in talks to design future custom chips with Broadcom, which could shift business away from Marvell. Marvell stock fell 6% on 8 Dec 2025. No company commented. [PRESS-UNNAMED: The Information, via Investing.com/Yahoo] — [Yahoo Finance/Investing.com, "Marvell stock falls on Microsoft-Broadcom talks…", 8 Dec 2025](https://finance.yahoo.com/news/marvell-stock-falls-microsoft-broadcom-130457554.html); [The Information briefing (paywalled)](https://www.theinformation.com/briefings/microsoft-discusses-custom-chips-broadcom)
- xAI was only mentioned speculatively, as "next in line", by TweakTown. [SUMMARY-ONLY; PRESS] — [TweakTown](https://www.tweaktown.com/news/107627/broadcom-secures-dollars10-billion-asic-contract-with-apple-and-xai-next-in-line-for-new-ai-chips/index.html). I found no source for a SoftBank or Arm custom-chip deal with Broadcom.

**AI networking**
- (11 Dec 2025) "Our current order backlog for AI switches exceeds $10 billion", referring to the "102 terabit per second Tomahawk six". [CO] — [Motley Fool Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
- (3 Jun 2026) "we have been shipping the industry's only 100 terabit Ethernet switch, the Tomahawk 6, for over one year", and the next-generation 200-terabit switch would tape out "this quarter". (2 Sep 2026) "we just taped out Tomahawk 7, the industry's first 200 terabit per second Ethernet switch". Tomahawk 6 is available in 100G and 200G SerDes versions (Kawwas). Tomahawk Ultra (scale-up Ethernet) is "deployed starting actually this quarter and in FY '27" (Kawwas). [CO] — [Motley Fool Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/); [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
- On co-packaged optics: Tan on 4 Mar 2026: "Even as we are the lead in CPO, CPOs will come in its time. Not this year, maybe not next year." On 3 Jun 2026 Broadcom called CPO "the de facto standard in the industry to extend AI clusters across data centers." [CO] — [Motley Fool Q1 FY2026](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript); [Motley Fool Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- AI networking share of AI revenue: Q1 FY2026 "one third" (+60% YoY); Q2 FY2026 "almost 40%"; Q3 FY2026 about 27% (implied by XPU at 73%). Tan expects networking "closer to around 30%" over time. [CO; Q3 share is CALC] — [Motley Fool Q1](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript), [Q2](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/), [Q3](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
- OpenAI's Jalapeño platform uses Broadcom Tomahawk for networking. Celestica supplies board and rack-scale infrastructure. [CO/CUST disclosures via IV: ServeTheHome] — [ServeTheHome, 24 Jun 2026](https://www.servethehome.com/openai-jalapeno-intelligence-platform-shown-powered-by-broadcom/)

**Packaging and process**
- (The Register, 5 Sep 2025) 3.5D XDSiP's largest design supports two 3D compute stacks, two I/O dies and up to 12 HBM stacks on a 6,000 mm² package. The first such parts are expected to ship in 2026, which is The Register's statement. [PRESS: The Register, describing Broadcom material] — [The Register, "If Broadcom is helping OpenAI build AI chips…", 5 Sep 2025](https://www.theregister.com/2025/09/05/openai_broadcom_ai_chips/)
- (12 Dec 2024) Tan said the next-generation XPUs "in three nanometers… will be the first of its kind" in that node. [CO] — [Motley Fool Q4 FY2024 transcript, 12 Dec 2024](https://www.fool.com/earnings/call-transcripts/2024/12/12/broadcom-avgo-q4-2024-earnings-call-transcript/). (Apr 2026) Meta MTIA is to be the first AI silicon on 2nm [CO via CNBC](https://www.cnbc.com/2026/04/14/meta-commits-to-one-gigawatt-of-custom-chips-with-broadcom-as-hock-tan-agrees-to-leave-board.html). Jalapeño is on TSMC 3nm [IV/analysis: TechInsights, 3 Sep 2026](https://www.techinsights.com/blog/openai-jalapeno-inference-chip-architecture).

### Inferences
- The six customers are most likely Google, Meta, Anthropic, OpenAI, customer #5 and one more. Earlier press reports name ByteDance as an earlier Broadcom customer, but Broadcom did not name it in any 2025–26 material I read. The two unnamed customers are the "other two" with $6B of purchase orders, shipping from late 2026.
- Anthropic is counted as an XPU customer even though the chip is Google's TPU. Broadcom's "largest XPU customer in 2027" claim therefore concentrates exposure in one TPU design family across two buyers, Google and Anthropic.
- The Apple 8-K is consistent with Broadcom's long-running Apple component supply (wireless/RF). It does not confirm an Apple AI XPU.

### Gaps
- Broadcom's role in TPU v1 through v6 could not be verified in this session. Only v7 (Ironwood) and v8 are covered by Broadcom statements.
- ByteDance customer status, chip node and manufacturing status could not be checked. Reuters was blocked and searches were exhausted.
- I found no primary source for the launch dates of Tomahawk 6, Tomahawk Ultra, Jericho3-AI/Jericho4, Thor Ultra NIC or Tomahawk 6 "Davisson" CPO. Broadcom's newsroom returned 403. From memory and unverified: TH6 Jun 2025, Tomahawk Ultra Jul 2025, Jericho4 Aug 2025, Thor Ultra and TH6-Davisson CPO Oct 2025, 3.5D XDSiP Dec 2024.
- I could not establish whether any 3.5D XDSiP-based XPU or 2nm XPU is shipping in volume as of Nov 2026.
- I found no reliable source tying customer #5 to xAI, Apple, SoftBank/Arm or Microsoft.

## 2. Roadmap and milestones: management commitments, dated, and their status

### Takeaway
Broadcom met or beat its quarterly AI revenue guidance in each of the four quarters I checked (Q4 FY2025 to Q3 FY2026), and its 2027 outlook has risen from ">$100B" to "~$115B". Several dated commitments are still pending as of 14 Nov 2026: the late-2026 deliveries for Anthropic, customer #5 and the other two customers; Meta's Q4 production shipments; and the "start H2 2026" for OpenAI's 10 GW. Q4 FY2026 results, due around Dec 2026, are not out. Some disclosure framing changed: Broadcom stopped quoting a single "AI backlog" number after Dec 2025, and the Anthropic 2027 capacity figure moved from ~3.5 GW to ~5 GW.

### Cited Findings
- **Dec 2024, FY2027 SAM:** Tan put the XPU-plus-networking serviceable market at "$60 billion to $90 billion in fiscal 2027 alone" for "three hyper-scale customers", each planning "one million XPU clusters". He added: "this is not revenue". Two more hyperscalers were "in advanced development" but "not validated… as customers". [CO] — [Motley Fool Q4 FY2024, 12 Dec 2024](https://www.fool.com/earnings/call-transcripts/2024/12/12/broadcom-avgo-q4-2024-earnings-call-transcript/). **Status: pending.** FY2027 began about 2 Nov 2026. The Sep 2026 FY2027 AI revenue outlook is about $115B, but it covers six customers rather than three, so it is not directly comparable [CO] — [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/).
- **Sep 2025, "$10B+" order from a new customer:** Broadcom said it had "secured over $10 billion of orders of AI racks" from a prospect turned customer. [CO via PRESS: The Register, 5 Sep 2025](https://www.theregister.com/2025/09/05/openai_broadcom_ai_chips/). **Status: confirmed as Anthropic** (Ironwood racks) on 11 Dec 2025, with a further $11B order for delivery in late 2026 [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). Delivery is in progress: 1 GW of Ironwood is deploying in 2026 [CO, Sep 2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/). Completion by "late 2026" is pending.
- **Dec 2025, AI backlog:** ">$73 billion" (about $20B non-XPU, the rest XPU), out of $162B consolidated backlog, to be "delivered over the next eighteen months". Tan said: "do not take that $73 billion as… the revenue we ship". [CO] — [Motley Fool Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). Per Sherwood News, Tan called it a "minimum" for the next six quarters, against a consensus of about $69B [PRESS] — [Sherwood News, 11 Dec 2025](https://sherwood.news/markets/broadcom-q4-2025-earnings-report-guidance-asics-ai-boom-bubble/). **Status: pending (18 months runs to about mid-2027).** No updated AI backlog figure was given on the Q2 or Q3 FY2026 calls. AI semiconductor revenue recognized from Q1 to Q3 FY2026 was $35.9B [CALC from 8-Ks](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm). Q2 FY2026 AI bookings were ">$30 billion" [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/).
- **Oct 2025, OpenAI 10 GW, start H2 2026, complete by 2029:** see the Maginative source in Section 1. In Dec 2025 Tan reframed it as "an agreement to be aligned on developing 10 gigawatts for OpenAI over 27 to 29 time frame" [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). OpenAI's deal was not expected to add much in 2026 [PRESS: Sherwood](https://sherwood.news/markets/broadcom-q4-2025-earnings-report-guidance-asics-ai-boom-bubble/). **Status: partly pending.** Jalapeño was unveiled on 24 Jun 2026, with "small prototype" deployment in late 2026 and volume in 2027 (1.3 GW "contractual commitment", per [CO, 3 Jun 2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)). I found no independent confirmation of a production deployment by 14 Nov 2026.
- **FY2026 AI revenue:** In Dec 2025 there was no full-year guide ("rather not give you guys any guidance"). Jun 2026: "$56 billion". Sep 2026: "$58 billion". [CO] — [Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/), [Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/), [Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/). Q1–Q3 actuals plus the Q4 guide sum to 8.4 + 10.8 + 16.7 + 21.7 = $57.6B [CALC]. **Status: pending Q4 results (about Dec 2026).**
- **FY2027 AI revenue:** In Mar 2026, "line of sight to achieve AI revenue from chips, just chips, in excess of $100 billion in 2027" ([CO](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript)), reiterated in Jun 2026. In Sep 2026: "we have secured the supply to again double AI revenue to approximately $115 billion". FY2028: "line of sight… to again double to $230 billion". FY2028 EPS "on target to exceed $30". [CO] — [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/). **Status: pending.**
- **Quarterly AI guidance track record:** [CO, 8-K exhibits]
  - Q4 FY2025: guide $6.2B ([8-K, 4 Sep 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000094/avgo-08032025x8kxex99.htm)), actual $6.5B.
  - Q1 FY2026: guide $8.2B ([8-K, 11 Dec 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm)), actual $8.4B.
  - Q2 FY2026: guide $10.7B ([8-K, 4 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000011/avgo-02012026x8kxex99.htm)), actual $10.8B.
  - Q3 FY2026: guide $16.0B ([8-K, 3 Jun 2026](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000051/avgo-05032026x8kxex99.htm)), actual $16.7B ([8-K, 2 Sep 2026](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm)).
  - **Met or beaten each time.**
- **Tomahawk 7 tape-out** "this quarter" (said 3 Jun 2026): reported taped out on 2 Sep 2026. **Met (company-stated).** [CO] — [Q2](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/), [Q3](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
- **Meta MTIA:** production shipments expected in Q4 FY2026 (ended 1 Nov 2026), the first 1 GW order delivering from H2 2027, and 3 GW through 2028. **Pending.** [CO] (Section 1 sources)
- **Customer #5 ($1B, late 2026) and the "other two" customers (from late 2026):** **pending.** [CO] (Section 1 sources)
- **Anthropic 2027 capacity:** ~3.5 GW in the 8-K of 6 Apr 2026; ">3 GW" on 4 Mar 2026; "another 5 gigawatts… beginning in 2027" on 3 Jun 2026; "5 GW of TPU v8i in 2027" on 2 Sep 2026. **Pending, and the figure changed (see Section 9).** [CO]

### Inferences
- The near-term record (quarterly AI guidance met or beaten in all four quarters checked; Q3 FY2025's own guide was not checked) is strong and comes from Broadcom's own reported numbers in SEC 8-Ks. The long-dated items (FY2027 ~$115B, FY2028 $230B, OpenAI 10 GW, Anthropic 10 GW in 2028) are all still forecasts.
- FY2026 Q4 actuals are not yet public, so FY2026 totals ($58B AI, about $106B revenue implied: Q1–Q3 $71.1B plus the $34.8B guide [CALC]) cannot be confirmed yet.

### Gaps
- I did not retrieve the original Q3 FY2025 call transcript. The Motley Fool URL returned 404, so the Sep 2025 "$10B+" quote comes via The Register.
- I found no Broadcom statement after Dec 2025 that updates the "$73B" AI backlog on the same basis.

## 3. Financials: FY2025, FY2026 Q1–Q3, Q4 guidance, backlog/RPO, balance sheet, returns, concentration

### Takeaway
FY2025 revenue was $63.9B, with AI semiconductor revenue of $20.2B (+65%). In FY2026, quarterly revenue rose from $19.3B to $22.2B to $29.6B, and AI revenue from $8.4B to $10.8B to $16.7B. Consolidated non-GAAP gross margin fell from about 77% to 75%, with about 73% guided for Q4, which management attributes to XPU and memory mix. Semiconductor segment operating margin rose to 61%. Remaining performance obligations jumped from $45.0B to $179.2B after the Google long-term agreement. Broadcom also took on large contingent exposures: backstops with maximum potential liability of about $29B and about $43B, a customer convertible-note facility of up to $42B, and $126.8B of purchase commitments. Broadcom does not report XPU revenue separately; every split it has given is listed below.

### Cited Findings
**FY2025 (ended 2 Nov 2025; reported 11 Dec 2025)** — [8-K Ex.99.1, 11 Dec 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm) [CO]
- Revenue was $63,887M (+24%): semiconductor solutions $36,858M, infrastructure software $27,029M.
- GAAP net income $23,126M; non-GAAP net income $33,728M. EPS $4.77 GAAP / $6.82 non-GAAP.
- Adjusted EBITDA $43,004M; cash from operations $27,537M; free cash flow $26,914M.
- Cash at year end $16,178M. Debt about $65,136M (short-term $3,152M plus long-term $61,984M). GAAP interest expense $3,210M.
- Dividends $11,142M; buybacks $2,450M. The FY2026 quarterly dividend was raised 10% to $0.65 ($2.60 per year).
- FY2025 AI semiconductor revenue was **$20.2B, +65%**. [CO] — [Broadcom DEF 14A (Chairman's letter), 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085691/d49254ddef14a.htm); "$20 billion" on the [Q4 FY2025 call](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). Q4 FY2025 AI revenue was $6.5B (+74%), and total Q4 revenue was $18,015M (+28%).
- FY2025 semiconductor segment operating income was $21,232M (+27%), a margin of 57.6% [CALC]. Infrastructure software operating income was $20,765M. [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- FY2025 non-GAAP gross margin was $50,245M (78.6% [CALC]). [CO] — [8-K, 11 Dec 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000116/avgo-11022025x8kxex99.htm)
- FY2025 Q3 (ended 3 Aug 2025): revenue $15,952M; AI revenue $5.2B (+63%). [CO] — [8-K, 4 Sep 2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000094/avgo-08032025x8kxex99.htm)
- Debt detail (Dec 2025): "gross principal fixed rate debt of $67.1 billion" at about 4% average rate and 7.2 years average maturity (Spears). [CO] — [Motley Fool Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)

**Q1 FY2026 (ended 1 Feb 2026; reported 4 Mar 2026)** — [8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000011/avgo-02012026x8kxex99.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript) [CO]
- Revenue $19,311M (+29%). AI semiconductor revenue $8.4B (+106%). Semiconductor solutions $12,515M (+52%); software $6,796M (+1%).
- Gross margin: GAAP $13,157M (68.1% [CALC]); non-GAAP $14,868M (77.0%).
- Non-GAAP operating income $12,826M. GAAP net income $7,349M. EPS $1.50 GAAP / $2.05 non-GAAP.
- Adjusted EBITDA $13,128M (68%). Free cash flow $8,010M.
- Cash $14,174M. Debt $66,057M. Interest expense $801M (GAAP).
- Dividends $3,086M; buybacks $7,850M (about 23M shares). A new $10B repurchase authorization runs through 31 Dec 2026.
- XPU/networking split: "customer accelerator business grew 140%". AI networking grew 60% and was "one third of total AI revenue". The semiconductor segment had about 68% gross margin and **60% operating margin** (+260bp).
- Q2 guide: revenue ~$22.0B, AI $10.7B, gross margin "flat sequentially at 77%".

**Q2 FY2026 (ended 3 May 2026; reported 3 Jun 2026)** — [8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000051/avgo-05032026x8kxex99.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/) [CO]
- Revenue $22,187M (+48%). AI $10.8B (+143%). Semiconductor solutions $15,009M (+79%); software $7,178M (+9%).
- Gross margin: GAAP $15,415M (69.5% [CALC]); non-GAAP $17,109M (77.1%, "down 230 basis points year-on-year").
- Non-GAAP operating income $14,928M. GAAP net income $9,310M. EPS $1.91 / $2.44.
- Adjusted EBITDA $15,244M (69%). Free cash flow $10,262M.
- Cash $19,628M. Debt $64,907M. Interest expense $776M.
- Dividends $3,092M; buybacks $600M.
- Networking was "almost 40%" of AI revenue. The semiconductor segment had about 70% gross margin and **62% operating margin** (+460bp).
- Q3 guide: revenue ~$29.4B, AI $16.0B, consolidated gross margin "down to approximately 74%". Spears: "This decline in gross margin does not represent a structural change in semiconductor margin." TPUs carry lower margins; AI networking has "very rich margins".
- Market reaction headline: "Broadcom stock plunges on weak software sales, unchanged AI chip forecast for the year" [PRESS: CNBC, 3 Jun 2026](https://www.cnbc.com/2026/06/03/broadcom-avgo-earnings-report-q2-2026.html) (headline only).

**Q3 FY2026 (ended 2 Aug 2026; reported 2 Sep 2026; 10-Q filed 10 Sep 2026)** — [8-K Ex.99.1](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm); [10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [call](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/) [CO]
- Revenue $29,591M (+86%). AI semiconductor revenue $16.7B (+221% YoY, +54% QoQ), 56% of revenue. Semiconductor solutions $20,839M (+127%); software $8,752M (+29%).
- Gross margin: GAAP $20,456M (69.1% [CALC]); non-GAAP $22,191M (75.0%, down 210bp sequentially on AI mix).
- Operating income: GAAP $15,955M; non-GAAP $20,095M (67.9%). GAAP net income $13,088M. EPS $2.68 / $3.32.
- Cash from operations $14,197M; capex $532M; free cash flow $13,665M (46%).
- **Semiconductor solutions operating income $12,770M (+145%), a 61.3% margin** [CALC; the call says "61%… up 440 basis points"]. Software operating income $7,325M. Unallocated expenses were −$4,140M.
- XPUs were 73% of AI revenue. Non-AI semiconductor revenue was about $4.2B per a secondary summary [SUMMARY-ONLY: Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/broadcom-inc-avgo-q3-2026-110030403.html).
- Cash $23,975M. Debt $59,419M (short-term $2,252M plus long-term $57,167M; principal $61,079M). Broadcom repurchased $5,641M of notes in Q3, repaid or repurchased $10,541M year to date, and issued $4,500M. A further $1.5B was repaid after quarter end. Gross fixed-rate debt is $59.6B (CFO).
- Interest expense $778M GAAP ($2,355M year to date).
- Dividends $3,103M ($9,281M year to date, $1.95/share). No buybacks in Q3 ($8,450M year to date); $10.1B of authorization remains.
- **Q4 FY2026 guidance (quarter ended 1 Nov 2026; results NOT yet released as of 14 Nov 2026):**
  - Revenue ~$34.8B (+93%); semiconductors ~$26.1B; AI ~$21.7B (+236%); non-AI semiconductors ~$4.3B; software ~$8.7B.
  - Consolidated gross margin ~73% ("down from 78% a year ago", attributed to "the increasing mix of XPUs with their increasing memory content"). Operating margin ~66%. Capex ~$1.4B.
  - Tan: "stop focusing on gross margin."
  - [CO] — [8-K, 2 Sep 2026](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm); [Investing.com transcript](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)

**Margin-dilution statements over time** [CO]
- 11 Dec 2025: Q1 gross margin "down approximately 100 basis points sequentially". On systems: "We'll be passing through more components that are not ours"; gross margin dollars rise while the percentage falls; operating margin percentage "will come down a bit" (Spears). [Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
- 4 Mar 2026: Spears said "the impact relative to our overall mix is actually not going to be substantial at all." [Q1 FY2026](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript)
- 3 Jun 2026 and 2 Sep 2026: see above (74% guide, then 75% actual and 73% guide).
- 10-Q risk factor (Sep 2026): XPU and rack sales "will likely increase our operating margin but compress or lower future gross margin". [10-Q, 10 Sep 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)

**Backlog and remaining performance obligations (RPO, firmly committed only)** [CO]
- Nov 2, 2025: $33.3B, 35% within 12 months. [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- Feb 1, 2026: $45.0B, 33%. [10-Q Q1 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm)
- May 3, 2026: $164.6B, about 30%. This "include[s] obligations under a long-term contract for custom AI accelerators entered in the fiscal quarter ended May 3, 2026". [10-Q Q2 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm)
- Aug 2, 2026: **$179.2B**, about 25% within 12 months. [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
- The Dec 2025 "AI backlog >$73B" and "consolidated backlog $162B" are management order-backlog figures, not RPO. [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)

**Contingent and off-balance-sheet items (AI XPV platform)** [CO]
- In Jun 2026 Broadcom launched the "AI XPV platform", with "an initial tranche of $35 billion led by a financial partner to facilitate the deployment of more than 1 gigawatt of compute infrastructure for our customer". The financial partner takes on agreements to purchase AI racks based on Broadcom XPUs and the related leases with the customer.
- The **Backstop** covers 5-year leases. On default, Broadcom's liability is the difference between 85% of the outstanding lease amounts and the resale value of the racks. "maximum potential liability… approximately $29 billion". Fair value is not material and nothing has been paid.
- The platform targets more than 20 GW for frontier AI labs through 2028.
- "Our customer may… issue to us convertible promissory notes up to an aggregate principal amount of $42 billion". None had been issued as of 2 Aug 2026.
- Sources: [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [10-Q Q2 FY2026, subsequent event dated 8 Jun 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm)
- The Apollo release (9 Jun 2026) names Anthropic as the beneficiary of the first $35B tranche. Wells Fargo, BNP Paribas, Citi and UBS arranged the A1 tranche; Goldman Sachs, BofA and Morgan Stanley were placement agents for A2. Won Kim of Broadcom calls it "the first pillar of the XPV Platform". [CO/counterparty] — [Apollo press release, 9 Jun 2026](https://ir.apollo.com/news-events/press-releases/detail/629/apollo-leads-35-billion-capital-solution-for-broadcom-ai)
- DCD reported the sites as "Fluidstack-based" and starting mid-2026 [SUMMARY-ONLY: DCD](https://www.datacenterdynamics.com/en/news/broadcom-apollo-and-blackstone-launch-20gw-xpu-platform/). Axios cited PitchBook on off-balance-sheet concerns [SUMMARY-ONLY: Axios, 10 Jun 2026](https://www.axios.com/2026/06/10/apollo-anthropic-blackstone-broadcom).
- **26 Oct 2026, second backstop (8-K Item 2.03):** "financial partners [take] on a portion of certain agreements to purchase AI racks… and the related lease agreements with the Company's customer". Broadcom provides "residual value support to a newly formed special purpose vehicle". Liability is the difference between **72.5%** of outstanding lease amounts and the rack value. "maximum potential liability… approximately **$43 billion**." The customer is not named. [CO] — [Broadcom 8-K, filed 27 Oct 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm)
- **Purchase commitments** (unconditional, mostly inventory): $54M at 1 Feb 2026; **$128,110M** at 3 May 2026 (FY2027 $55,214M, FY2028 $72,870M); **$126,821M** at 2 Aug 2026 (FY2026 remainder $1,110M, FY2027 $52,674M, FY2028 $72,952M, FY2029 $85M). [CO] — [10-Q Q1](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm), [Q2](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm), [Q3](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)

**Debt actions** [CO]
- 6–13 Jan 2026: $4.5B of senior notes issued (4.300% due 2031, 4.600% 2033, 4.950% 2036, 5.700% 2056). [8-K, 13 Jan 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526011731/d104560d8k.htm)
- Jun 2026: cash tender offers launched 11 Jun, upsized and completed 17 Jun. [8-K, 11 Jun 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526266777/d152717d8k.htm); [8-K, 18 Jun 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526275077/d149683d8k.htm)

**Customer concentration (10-K and 10-Qs)** [CO]
- FY2025: one distributor was 32% of revenue (FY2024 28%); top five end customers about 40%; distributors 48%; shipments to China (including Hong Kong) 17% (FY2024 20%). [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- Q1 FY2026: one distributor 42%; top five about 50%. [10-Q Q1](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm)
- Q2 FY2026: one distributor 42%; top five about 45%. [10-Q Q2](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm)
- Q3 FY2026: one distributor **50%** (46% year to date); top five about **55%** (50% year to date); distributors 56% year to date. [10-Q Q3](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)

**Outside estimates (labelled)**
- Mizuho estimated Broadcom's Google-plus-Anthropic custom-silicon revenue at $21B for 2026 and $42B for 2027. [EST: Mizuho; SUMMARY-ONLY via tech-insider.org, a low-quality aggregator] — [tech-insider.org](https://tech-insider.org/google-tpu-8t-8i-broadcom-mediatek-nvidia-2026/)
- On 11 Dec 2025, BofA's Vivek Arya lowered his gross margin estimates for the next two fiscal years. [EST: BofA via Sherwood](https://sherwood.news/markets/broadcom-q4-2025-earnings-report-guidance-asics-ai-boom-bubble/)

### Inferences
- The step-up in RPO between Feb and May 2026 (+$119.6B [CALC]) coincides with the 6 Apr 2026 Google TPU long-term agreement. The 10-Q describes "a long-term contract for custom AI accelerators" entered that quarter. The 10-Q does not name the counterparty.
- The single distributor at 50% of Q3 revenue is very likely the channel for XPU and TPU shipments, but Broadcom does not name it, so this is unconfirmed.
- The maximum backstop exposures (~$29B plus ~$43B) together are about 1.2 times the ~$59.4B of reported debt at 2 Aug 2026 [CALC]. Both are contingent and not on the balance sheet.
- Purchase commitments of about $127B, mostly in FY2027–28, line up with management's claim to have "secured the supply" for FY2027.

### Gaps
- Broadcom gives no dollar XPU revenue, no per-customer revenue, and no gross margin for XPUs or racks. All splits above are percentages management gave on calls.
- I did not check the FY2025 Q4 XPU/networking split.
- Q4 FY2026 actuals and any FY2027 guidance will not be available until about Dec 2026.
- The customer behind the Oct 2026 $43B backstop and the $42B convertible notes is not named in the filings.

## 4. Customers and contracts: binding vs announced

### Takeaway
The binding items, as Broadcom describes them, are the Google TPU long-term agreement and supply assurance agreement (8-K, Apr 2026); Anthropic's $10B and $11B orders; customer #5's $1B order; $6B of POs from two other customers; OpenAI's "contractual commitment" of 1.3 GW for 2027; and the Apple long-term agreements (8-K, Jul 2026). The announced or framework items are OpenAI's 10 GW (a "term"-style alignment through 2029), Anthropic's ~3.5–5 GW from 2027 and 10 GW in 2028 (explicitly "dependent on Anthropic's continued commercial success"), and Meta's ">1 GW first phase" and "multi-gigawatt" rollout. Microsoft, xAI and SoftBank/Arm appear only in press reports or speculation.

### Cited Findings
- **Google:** a Long Term Agreement to "develop and supply" future TPU generations and a supply assurance agreement for networking and other rack components "through up to 2031". [CO, 8-K, binding agreements; financial terms undisclosed] — [8-K, 6 Apr 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm). RPO includes a long-term custom AI accelerator contract signed in Q2 FY2026 [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm).
- **Anthropic:**
  - Orders of $10B (Q3 FY2025) and $11B (Q4 FY2025, delivery late 2026) are firm orders per Broadcom. [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
  - The ~3.5 GW from 2027 is "dependent on Anthropic's continued commercial success" and "the parties are in discussions with certain operational and financial partners". [CO, 8-K](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm)
  - Anthropic says this is its "largest compute commitment to date", that run-rate revenue "surpassed $30 billion" (about $9B at end-2025), and that it also uses AWS Trainium and NVIDIA. [CUST](https://www.anthropic.com/news/google-broadcom-partnership-compute)
  - Financing goes through the XPV platform ($35B first tranche), with a Broadcom backstop (max ~$29B) and a facility for convertible notes of up to $42B. [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
  - Asked about the Anthropic deal on 3 Jun 2026, Tan said: "It was not backstopped in that sense." [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- **OpenAI:**
  - The 10 GW of Oct 2025 is described by Tan as "an agreement to be aligned on developing 10 gigawatts… over 27 to 29". [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
  - "We have a contractual commitment to deploy 1.3 gigawatts in 2027" (3 Jun 2026). [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
  - The Apollo release does not mention OpenAI. Other coverage named OpenAI among the platform's initial customers [SUMMARY-ONLY: DCD](https://www.datacenterdynamics.com/en/news/broadcom-apollo-and-blackstone-launch-20gw-xpu-platform/).
  - OpenAI also has deals with AWS (Trainium), AMD and Cerebras. [PRESS: CNBC, 24 Jun 2026](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html)
- **Meta:** "a commitment that exceeds 1GW" as "the first phase" [CUST](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/). The partnership is extended through 2029 [PRESS: CNBC](https://www.cnbc.com/2026/04/14/meta-commits-to-one-gigawatt-of-custom-chips-with-broadcom-as-hock-tan-agrees-to-leave-board.html). The first 1 GW order starts delivery in H2 2027 [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/). Meta also has up to 6 GW of AMD GPU commitments, "millions" of NVIDIA chips, and custom chips with Arm [PRESS: CNBC](https://www.cnbc.com/2026/04/14/meta-commits-to-one-gigawatt-of-custom-chips-with-broadcom-as-hock-tan-agrees-to-leave-board.html).
- **Customer #5:** a $1B order for delivery in late 2026 (firm order per Broadcom). [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
- **"Other two" customers:** POs totalling $6B, shipments from late 2026. [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- **Apple:** multi-year long-term agreements through 2031 for custom ASIC silicon "for use in multiple generations of Apple products". The filing does not specify AI. [CO, 8-K, 6 Jul 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526295589/d84378d8k.htm)
- **Microsoft:** reported talks only. [PRESS-UNNAMED: The Information, Dec 2025](https://finance.yahoo.com/news/marvell-stock-falls-microsoft-broadcom-130457554.html)
- **Unnamed customer behind the 26 Oct 2026 SPV:** Broadcom provides residual value support of up to about $43B. [CO](https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm)

### Inferences
- The gigawatt figures, which are the largest numbers in Broadcom's narrative, are mostly capacity plans conditioned on customers' growth and financing. The contractual items Broadcom has quantified in dollars are much smaller: $10B + $11B + $1B + $6B in orders, plus the RPO step-up.
- The 10-Q's "customer" in the Jun 2026 XPV backstop and convertible-note facility is most likely Anthropic, since the Apollo release names Anthropic for the first tranche. The filing itself does not name the customer.

### Gaps
- None of the contract values for Google, Meta or OpenAI are disclosed.
- No Anthropic or OpenAI filing confirms the backstop or convertible-note terms. Anthropic is private, and I found no OpenAI statement on them.
- ByteDance contract status could not be checked.

## 5. Capacity: TSMC wafers and CoWoS, HBM, substrates, lasers, rack integration

### Takeaway
Broadcom depends almost entirely on TSMC: about 95% of its contract-manufactured wafers in the first three quarters of FY2026. It says it has "fully secured" leading-edge wafers, HBM and substrates for 2026–2028, backed by about $127B of unconditional purchase commitments. Lasers (EML and CW) and data-centre "land, power and shell" are the constraints it now names. For HBM, Q4 margin dilution from XPUs' "increasing memory content" indicates Broadcom is buying memory into at least some XPU products. Celestica is one disclosed rack and board partner.

### Cited Findings
- "approximately 95% of the wafers manufactured by our CMs were produced by… TSMC. We believe our wafer requirements represent a meaningful portion of TSMC's total production capacity… TSMC has raised, and may in the future raise, their prices". "more than three-quarters of our manufacturing materials from five materials suppliers, some of which are single source". [CO] — [10-Q Q3 FY2026, 10 Sep 2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
- (4 Mar 2026) "constrained capacity in leading-edge wafers, in high bandwidth memory, and substrates", and "we have fully secured capacity of these components for 2026 through 2028… We have locked up substrates." [CO] — [Motley Fool Q1 FY2026](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript)
- (3 Jun 2026) Broadcom has secured supply, including "HBMs" and "DRAM". Power is a constraint. [CO] — [Motley Fool Q2 FY2026](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/)
- (2 Sep 2026) Tan: "demand for lasers, whether it's EML lasers, CW lasers, is far surpassing supply". Indium phosphide laser capacity is "more than tripling" (Kawwas). "We are going to start deploying our Singapore fab for substrates" from FY2027. Land, power and shell "dictates specific timing of when this capacity gets deployed". Q4 gross margin dilution comes from XPUs' "increasing memory content". [CO] — [Motley Fool Q3 FY2026](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); [Investing.com Q3 FY2026](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849)
- (11 Dec 2025) On 2nm and 3nm: "so far, we do not have that constraint", while adding 2nm and 3nm capacity at TSMC. Advanced packaging in Singapore is being "partially insourc[ed]". [CO] — [Motley Fool Q4 FY2025](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/)
- Purchase commitments: $126.8B as of 2 Aug 2026, almost all in FY2027–28. [CO] — [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
- Broadcom's own fabs: Fort Collins (FBAR filters) and Breinigsville, Pennsylvania (InP wafers for optics), plus Singapore. [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- Rack partners: Celestica supplies boards and rack-scale infrastructure for OpenAI Jalapeño. [CO/CUST disclosure via ServeTheHome, 24 Jun 2026](https://www.servethehome.com/openai-jalapeno-intelligence-platform-shown-powered-by-broadcom/)
- Competitor capacity: TheNextWeb reported that MediaTek asked TSMC for a sevenfold CoWoS increase for Google orders [SUMMARY-ONLY; PRESS](https://thenextweb.com/news/google-ironwood-tpu-inference-cloud-next). MediaTek's CEO: "TSMC is our most important partner, period" (30 Oct 2026) [CUST/competitor via PRESS: BigGo](https://finance.biggo.com/news/TW_2454.TW_2026-10-30).

### Inferences
- Broadcom's 95% TSMC dependence and its claim to be a "meaningful portion" of TSMC capacity make TSMC allocation and pricing the main external capacity variable. I found no TSMC statement about Broadcom (TSMC does not name customers).
- Gross margin dilution from "memory content" implies HBM pass-through on at least some XPU programmes, likely the rack-level TPU sales to Anthropic. Broadcom has not said which programmes. This is an inference.

### Gaps
- I found no CoWoS wafer allocation for Broadcom, from TSMC or from analysts such as Morgan Stanley or TrendForce. Search was exhausted.
- Who buys HBM per programme (Google directly versus Broadcom) is not disclosed.
- The rack integrator for Anthropic's Ironwood racks was not identified.

## 6. Ownership and key people

### Takeaway
Hock Tan (CEO since 2006) is locked in through fiscal 2030 by a performance award tied to AI revenue of $60–120B over any four consecutive quarters in FY2028–FY2030. Management's own FY2027–28 outlook exceeds that range. CFO Kirsten Spears retired on 12 Jun 2026 and was replaced by Amie Thuener, formerly Alphabet's chief accounting officer. Henry Samueli chairs the board and owns 1.8% of shares. Vanguard (9.9%) and BlackRock (7.3%) are the largest disclosed holders.

### Cited Findings
- **Tan PSU award** (granted 3 Sep 2025):
  - Target of 610,521 PSUs. Vesting depends on AI revenue targets over FY2028–FY2030 and on Tan's continued service through the end of FY2030.
  - "Applicable AI Revenue" is the highest four-consecutive-quarter total in the period. Payout is 0% at or below $60B, 100% at $90B, 200% at $105B and 300% at or above $120B, linear between levels.
  - AI Revenue includes custom AI accelerators, XPUs, ASICs and networking and connectivity.
  - Tan must hold shares from his 2023 PSU award until 3 Nov 2030 (31 Oct 2032 if he voluntarily resigns without good reason).
  - [CO] — [Broadcom 8-K, filed 9 Sep 2025](https://www.sec.gov/Archives/edgar/data/1730168/000119312525199281/d58273d8k.htm)
  - Press valued the award at about $205M at target and over $616M at maximum [PRESS; SUMMARY-ONLY](https://parameter.io/broadcom-avgo-stock-board-bets-big-on-ceo-with-616m-performance-award/).
- Tan has been President and CEO since March 2006. [CO, 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm) He left Meta's board after declining to stand for re-election (Apr 2026) and moved to an advisor role. [CUST: Meta](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/); [CNBC, 14 Apr 2026](https://www.cnbc.com/2026/04/14/meta-commits-to-one-gigawatt-of-custom-chips-with-broadcom-as-hock-tan-agrees-to-leave-board.html)
- **Charlie B. Kawwas, Ph.D.:** President, Semiconductor Solutions Group since July 2022 (COO Dec 2020–Jul 2022). Beneficially owns 814,716 shares. [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm); [DEF 14A, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085691/d49254ddef14a.htm)
- **CFO transition:**
  - Announced 2 Apr 2026: Amie Thuener, Alphabet VP, corporate controller and chief accounting officer since 2018, succeeds Kirsten Spears effective 12 Jun 2026. Spears had been CFO since late 2020 and stays as an advisor for nine months. [PRESS: The Star, 3 Apr 2026](https://www.thestar.com.my/tech/tech-news/2026/04/03/broadcom-taps-alphabet-executive-amie-thuener-as-next-cfo); [Broadcom release (URL from search; fetch blocked)](https://investors.broadcom.com/news-releases/news-release-details/broadcom-announces-planned-chief-financial-officer-transition)
  - EDGAR shows an Item 5.02 8-K on 2 Apr 2026. Spears signed the 11 Jun 2026 8-K as CFO; Thuener signed from 18 Jun 2026. [CO, EDGAR](https://www.sec.gov/Archives/edgar/data/1730168/000119312526275077/d149683d8k.htm)
- **Henry Samueli, Ph.D.:** Chairman; 85,559,569 shares (1.8%). **Hock Tan:** 908,474 shares (under 1%). Directors and officers as a group: 1.9%. Shares outstanding: 4,735,602,612 (24 Feb 2026). [CO] — [DEF 14A, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085691/d49254ddef14a.htm)
- **Major holders:** The Vanguard Group 468,544,898 shares (9.9%) and BlackRock 347,023,720 (7.3%). These are based on 13G/A filings from 4 Oct 2024 and 26 Jan 2024, so the holdings are dated. [CO, proxy] — [DEF 14A, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085691/d49254ddef14a.htm)
- **Other officers:** Mark D. Brazeal is Chief Legal and Corporate Affairs Officer [CO, 10-K](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm). Won Kim is Broadcom's "Head of Corporate Development and AI Infrastructure Partnerships" [CO via Apollo, 9 Jun 2026](https://ir.apollo.com/news-events/press-releases/detail/629/apollo-leads-35-billion-capital-solution-for-broadcom-ai).
- **Board:** Eddy Hartenstein (former Lead Independent Director) retired at the 2026 annual meeting, and the board shrank to eight. [CO, 8-K, 2 Mar 2026](https://www.sec.gov/Archives/edgar/data/1730168/000119312526085656/d305325d8k.htm)
- **Workforce:** about 33,000 employees, about 57% in R&D (2 Nov 2025). [CO, 10-K](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)

### Inferences
- Management's Sep 2026 outlook (~$115B AI in FY2027; "line of sight" to $230B in FY2028) is above the award's $120B maximum. If it holds, the maximum payout of 1,831,563 shares [CALC: 610,521 × 3] would be reached. In effect, the award's targets were set below management's current public outlook.
- The new CFO comes from the parent of Broadcom's largest XPU customer. I found no disclosure of related-party issues; this is noted only as a fact pattern.

### Gaps
- I could not verify the name of the head of the ASIC/custom silicon division in this session. Frank Ostojic (SVP & GM, ASIC Products Division) is from memory and unverified, because Broadcom's site returned 403.
- I did not retrieve 13F or 13G updates after 2024 for Vanguard and BlackRock.
- I did not retrieve the Apr 2026 Item 5.07 vote results (annual meeting).

## 7. Legal and regulatory matters

### Takeaway
Broadcom's filings describe no material accrued legal losses. They disclose regulatory inquiries in Korea, Japan and the EU into contracting practices, and FTC oversight. Since the Q1 FY2026 10-Q (Mar 2026), Broadcom has added risk language on customers being designated a "supply chain risk" and on "customer-owned tooling". The China SAMR VMware conditions, EU and US VMware complaints and lawsuits, ByteDance export-control issues, and any custom-silicon patent suits could **not** be verified in this session.

### Cited Findings
- Broadcom is subject to "the U.S. Federal Trade Commission. We have been, and may in the future be, involved or required to participate in regulatory investigations or inquiries from regulatory authorities in Korea, Japan and the European Union into certain of our contracting and business practices". [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm); unchanged in [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
- No material amounts are accrued for loss contingencies. Broadcom does not expect pending proceedings to have a material adverse effect. [CO] — [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
- The VMware securities class action (filed 31 Mar 2020, N.D. Cal.) settled, with court approval in March 2025. [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- Export control risk factor: if suppliers or customers "become subject to export restrictions or are designated a 'supply chain risk', we may be required to suspend purchasing from such suppliers or selling to such customers". This language is absent from the FY2025 10-K and first appears in the Q1 FY2026 10-Q (filed 11 Mar 2026). [CO; text comparison is CALC] — [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm); [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm); [10-Q Q1 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm)
- Contract terms: indemnification and liquidated damages in some contracts with "some of our largest customers, are potentially unlimited." [CO] — [10-Q Q3 FY2026](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm)
- China exposure: 17% of FY2025 revenue came from shipments to China (including Hong Kong), down from 20% in FY2024. [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
- Global minimum tax: Singapore's enactment, effective FY2026, is expected to have a "material impact" on results and cash flows. [CO] — [10-K FY2025](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)

### Inferences
- The new "supply chain risk" wording appeared in March 2026. The term matches language used in US government procurement. Because Broadcom's prospective largest XPU customer (Anthropic) is a frontier lab, I checked whether this wording relates to any US government designation of an AI customer. I could not verify any such designation (see Gaps).

### Gaps (unverified leads; none confirmed in this session)
- **China SAMR conditions** on the VMware approval (reported Nov 2023: interoperability and continued-supply commitments in China). I could not retrieve the source, and the 10-K and 10-Q do not mention SAMR.
- **EU and US VMware complaints and lawsuits** (from memory): the CISPE complaint and its 2025 appeal to the EU General Court; AT&T v. Broadcom/VMware (2024, reported settled); Tesco's UK claim (2025); Siemens' US suit (2025). None were verified, and Broadcom's filings do not name them.
- **ByteDance and export controls** (TSMC due-diligence rules; reported Broadcom–ByteDance chip): I could not retrieve this. Reuters blocked the fetch and searches were exhausted.
- **Patent or antitrust suits involving Broadcom custom silicon:** none found.
- **Any US government "supply chain risk" designation of an AI customer** (for example, reported Pentagon–Anthropic disputes in 2026): not verified.

## 8. Science and engineering: demonstrated, verified, unproven, limits

### Takeaway
Google and Meta have shown publicly that custom accelerators work in production at scale. Google's TPU v4 was published at ISCA 2023 with measured comparisons to the A100, and Ironwood and TPU 8 specifications are customer-stated. Meta's MTIA v2 was in production in 16 regions in 2024. These are the customers' own claims and papers; none names Broadcom, and none is an independent benchmark. Broadcom's networking and packaging claims (200G SerDes, Tomahawk 6/7, 3.5D, CPO) are company-stated, and I found no independent verification in this session. OpenAI's Jalapeño performance, the new customers' chips, rack-scale XPU economics and XPU-versus-GPU total cost of ownership remain unproven by independent data. The binding limits Broadcom itself names are supply (leading-edge wafers, HBM, substrates, lasers), deployment sites and power, and customers' freedom to dual-source (MediaTek is now shipping a TPU variant).

### Cited Findings
**Demonstrated (customer-published, outside Broadcom)**
- **TPU v4** (Jouppi et al., ISCA 2023): 4,096-chip supercomputer. Optical circuit switches are under 5% of system cost and under 3% of power. SparseCores give 5–7× on embedding models. 2.1× faster and 2.7× better performance per watt than TPU v3. **1.2–1.7× faster than NVIDIA A100 using 1.3–1.9× less power.** Deployed since 2020. [CUST: Google, peer-reviewed venue; not independent] — [arXiv:2304.01433, Apr 2023](https://arxiv.org/abs/2304.01433)
- **Ironwood (TPU v7):** 4,614 TFLOPs per chip, 192 GB HBM, 7.37 TB/s, 1.2 TBps ICI. Pods of 256 or 9,216 chips; the 9,216-chip pod delivers 42.5 EF at nearly 10 MW. 2× performance per watt versus Trillium. [CUST: Google] — [Google blog, 9 Apr 2025](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/)
- **TPU 8t:** 9,600-chip superpods, 121 EF, 2 PB HBM. **TPU 8i:** 288 GB HBM, 384 MB SRAM, 19.2 Tb/s ICI, 80% better performance per dollar than Ironwood. Both offer up to 2× performance per watt. [CUST: Google, 22 Apr 2026] — [Google blog](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/)
- **MTIA v2:** TSMC 5nm, 1.35 GHz, 90 W, 708 TOPS INT8 sparse (354 dense), 256 MB SRAM, 128 GB LPDDR5. 3× v1 on four models. Serving production models in 16 regions within nine months of first silicon. [CUST: Meta, 10 Apr 2024] — [Meta AI blog](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/)
- Google Cloud's Thomas Kurian cited "strong price-performance and efficiency" seen by Anthropic's teams on TPUs. [CUST] — [Anthropic, 23 Oct 2025](https://www.anthropic.com/news/expanding-our-use-of-google-cloud-tpus-and-services)

**Third-party observation of Broadcom-related silicon**
- **Jalapeño:** TechInsights, working from OpenAI's Hot Chips 2026 disclosures and patents, reports TSMC 3nm, a weight-stationary systolic array "in the same broad family as Google's TPU", per-core HBM slices, and the Gluon/Triton software stack. It notes benchmarks are **not independently verified** and calls software maturity a weak point. It did no teardown. [IV/analysis: TechInsights, 3 Sep 2026] — [TechInsights](https://www.techinsights.com/blog/openai-jalapeno-inference-chip-architecture)
- ServeTheHome read six HBM sites from the photos, hedged as "might be off". It ran no performance tests. [IV: ServeTheHome, 24 Jun 2026] — [STH](https://www.servethehome.com/openai-jalapeno-intelligence-platform-shown-powered-by-broadcom/)
- Tom's Hardware described Jalapeño as "a massive reticle-sized ASIC". [PRESS: Tom's Hardware headline, Jun 2026](https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle)
- A cost-efficiency claim of about 50% better than GPUs is attributed to Broadcom's CEO and is unverified. [SUMMARY-ONLY: RCR](https://rcrtech.com/semiconductor-news/openai-broadcom-jalapeno-inference-chip/)

**Broadcom engineering claims (company-stated; independent verification not found)**
- Tomahawk 6 (102.4 Tbps; 100G and 200G SerDes versions), Tomahawk 7 (200 Tbps) taped out, Tomahawk Ultra scale-up deployments, CPO leadership, and the 3.5D XDSiP design (6,000 mm² package, 12 HBM stacks). [CO] — sources in Section 1.

**Unproven as of 14 Nov 2026**
- OpenAI Jalapeño production performance and schedule. Only lab operation is claimed (running GPT-5.3-Codex-Spark) [CUST via STH](https://www.servethehome.com/openai-jalapeno-intelligence-platform-shown-powered-by-broadcom/). Volume is due in 2027 [CO](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/).
- The chips of customer #5 and the "other two" customers: no public specifications [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/).
- Rack-scale XPU systems financed through leases and backstops: no default or residual-value history exists. Backstop fair value is "not material" per Broadcom [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm).
- XPU-versus-GPU total cost of ownership: the only public numbers are from vendors or customers. Examples are Google's 80% performance-per-dollar gain against its own prior TPU (not against GPUs) and the TPU v4 versus A100 comparison from 2023. Meta states a goal of "the best mix of performance and total cost of ownership" without numbers [CUST](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/).

**Physical and engineering limits, with evidence**
- **Supply:** leading-edge wafers, HBM and substrates (Mar 2026); lasers (Sep 2026); 95% TSMC dependence; TSMC price increases. [CO] — Section 5 sources.
- **Deployment:** land, power and shell set deployment timing (Sep 2026) [CO](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/). An Ironwood 9,216-chip pod draws nearly 10 MW [CUST: Google](https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/).
- **Die size and packaging:** single-die limits push toward multi-die packages, such as the 6,000 mm² 3.5D XDSiP with up to 12 HBM stacks [PRESS: The Register](https://www.theregister.com/2025/09/05/openai_broadcom_ai_chips/). Jalapeño is described as reticle-sized [PRESS: Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/broadcom-and-openai-unveil-custom-built-jalapeno-inference-processor-openais-first-chip-is-a-massive-reticle-sized-asic-built-in-an-ultra-fast-nine-month-development-cycle).
- **Design-cycle time:** Jalapeño took about nine months to tape-out, which is OpenAI's claim and not independently verified [PRESS: CNBC](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html). MTIA v2 reached production in under nine months from first silicon [CUST: Meta](https://ai.meta.com/blog/next-generation-meta-training-inference-accelerator-AI-MTIA/).
- **Dependence on customers' architecture teams:** OpenAI designs the accelerator [PRESS: Maginative](https://www.maginative.com/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029). Google co-designs TPUs with DeepMind [CUST](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/). Meta "co-develops" with Broadcom across design, packaging and networking [CUST](https://about.fb.com/news/2026/04/meta-partners-with-broadcom-to-co-develop-custom-ai-silicon/).
- **Customer moves and dual-sourcing:**
  - MediaTek began AI-accelerator shipments in Sep 2026 and expects about $2.5B of revenue in Q4 2026. It targets the high end of its 2027 range (press puts that at about $16B, which is not in the quoted remarks) and "around 20% of the total AI accelerator ASIC market". It has a second customer with first revenue in 2028. [competitor statements via PRESS: BigGo, 30 Oct 2026](https://finance.biggo.com/news/TW_2454.TW_2026-10-30)
  - Broadcom itself refers to the "MediaTek version v8t" [CO](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/).
  - Benchmark's Cody Acree said Marvell lost AWS Trainium 3 and 4 to Alchip [EST/analyst view, 8 Dec 2025](https://finance.yahoo.com/news/marvell-stock-falls-microsoft-broadcom-130457554.html).
  - Broadcom's 10-Qs since Mar 2026 list "customers proceed with customer-owned tooling" as a risk [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm).

### Inferences
- **Does it stand on solid ground?**
  - The evidence is strongest that the XPU model works technically and commercially for Google's TPU line. Google's own papers and specifications support this, Anthropic has made multi-GW commitments, and Google signed a long-term agreement through about 2031.
  - It is moderately strong for Meta: MTIA is in production and the extended agreement is binding in part.
  - It is weakest for OpenAI and the unnamed customers, for which no independent performance or production data exist yet.
  - The rack-plus-financing model introduces credit and residual-value risk, with backstops of up to about $72B in total [CALC]. This has no track record yet.
  - Gross margin compression from memory pass-through is now visible in reported numbers.
- The main technical risk Broadcom's filings and calls name is supply (wafers, HBM, substrates, lasers), not design capability. The main commercial risk visible in third-party data is dual-sourcing: MediaTek on TPU, and customers' own design teams.

### Gaps
- No MLPerf results that include Broadcom-designed XPUs were retrieved. I did not check whether Google submitted Ironwood or TPU 8 to MLPerf.
- No independent verification of Broadcom's 200G SerDes, 3.5D XDSiP or CPO reliability was retrieved. A reported Meta CPO field-reliability study is unverified.
- I found no source for 2nm or 3nm yields and costs, or for SerDes power figures.
- I did not retrieve the Meta MTIA ISCA papers (2023, 2025); dl.acm.org returned 403. Hot Chips 2025 and 2026 TPU and Jalapeño materials were seen only via TechInsights.
- I found no independent XPU-versus-GPU total-cost-of-ownership study.

## 9. Cross-examination log: Broadcom's statements against customers, suppliers, competitors, analysts and press

### Takeaway
The main discrepancies are these: who the first "$10B" customer was; which TPU v8 variant Broadcom builds; Anthropic's 2027 gigawatt figure; the OpenAI start date; gross margin guidance ("not substantial", then about 4–5 points lower year on year); whether the business is "all chips" or includes racks; Tan's "no backstop" remark versus backstops filed days later; and customer-owned tooling being dismissed on calls while added as a risk factor in filings.

### Cited Findings
1. **Identity of the first $10B customer.** The FT (Sep 2025, unnamed sources) said it was OpenAI [PRESS-UNNAMED: FT via The Register, 5 Sep 2025](https://www.theregister.com/2025/09/05/openai_broadcom_ai_chips/). Broadcom (11 Dec 2025) said it was Anthropic, ordering Ironwood racks [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/).
2. **TPU v8 split.**
   - Press and supply-chain reports (Jan and Apr 2026): Broadcom builds the training part (8t "Sunfish"; SemiAnalysis calls it "v8AX") and MediaTek the inference part (8i "Zebrafish"). [PRESS: Wccftech, 20 Apr 2026](https://wccftech.com/google-splits-tpuv8-strategy-two-chips-broadcom-training-mediatek-inference-duties/); [SUMMARY-ONLY: SemiAnalysis post on X](https://x.com/SemiAnalysis_/status/2016209828188750028)
   - Broadcom (2 Sep 2026, two independent transcripts): "shipping the TPU version 8i ahead of the MediaTek version v8t", and Anthropic gets "5 GW of TPU v8i in 2027" [CO](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/); [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849).
   - Google does not name its partners [CUST](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/).
   - MediaTek does not name its customer [competitor via BigGo](https://finance.biggo.com/news/TW_2454.TW_2026-10-30).
   - **Unresolved.**
3. **Anthropic 2027 capacity.** ">3 GW" (4 Mar 2026); "approximately 3.5 gigawatts… through Broadcom" (8-K, 6 Apr 2026); "another 5 gigawatts" (3 Jun 2026); "5 GW of TPU v8i" (2 Sep 2026). Anthropic itself says only "multiple gigawatts". [CO](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm); [CUST](https://www.anthropic.com/news/google-broadcom-partnership-compute)
4. **OpenAI start date.** The Oct 2025 announcement said deployments start in H2 or late 2026 [PRESS: Maginative](https://www.maginative.com/openai-and-broadcom-to-co-design-custom-ai-chips-deploy-10-gw-by-2029). By Dec 2025 Broadcom said "over 27 to 29" [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). In Jun 2026 Tan said "small prototype" in late 2026, ramp in 2027, "full tilt" in H1 2028 [PRESS: CNBC](https://www.cnbc.com/2026/06/24/openai-and-broadcom-reveal-jalapeno-first-ai-chip-in-partnership.html). There is no announced "delay", but volume has moved to 2027. I found no third-party report of a Jalapeño delay.
5. **Gross margin.** Spears said "not going to be substantial at all" (4 Mar 2026). By Jun 2026 the guide was about 74% and "not… a structural change". The Q3 actual was 75%, and the Q4 guide of about 73% is about 5 points below the 78% of a year earlier, attributed to XPU memory content. [CO] — [Q1](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript), [Q2](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/), [Q3](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/). Analysts at Morgan Stanley (Joseph Moore) and BofA flagged rack and Anthropic margin dilution in Dec 2025 [PRESS: Sherwood](https://sherwood.news/markets/broadcom-q4-2025-earnings-report-guidance-asics-ai-boom-bubble/).
6. **"Chip business only" versus racks.** Tan (3 Jun 2026) said the business is "all a chip business only" [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/). Yet Broadcom sells "TPU Ironwood racks" to Anthropic [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/), and its 10-Q describes purchase and lease of "AI racks" with backstops [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000080/avgo-20260802.htm).
7. **Backstops.** Tan said "It was not backstopped in that sense" (3 Jun 2026) [CO](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/). Five days later (8 Jun 2026) Broadcom entered a backstop worth up to about $29B [CO, 10-Q](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000054/avgo-20260503.htm). On 2 Sep 2026 the CFO said any future guarantees would be "modest" [CO](https://www.investing.com/news/transcripts/earnings-call-transcript-broadcom-tops-q3-2026-estimates-as-ai-sales-surge-93CH-4886849). On 26 Oct 2026 Broadcom added a backstop with up to about $43B maximum potential liability [CO, 8-K](https://www.sec.gov/Archives/edgar/data/1730168/000119312526434271/d148323d8k.htm).
8. **Customer-owned tooling.** On calls: "overblown hypothesis… I do not think will happen" (11 Dec 2025) and "will not see competition in COT for many years" (4 Mar 2026) [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). In filings, the Q1 FY2026 10-Q (11 Mar 2026) and later 10-Qs add "customers proceed with customer-owned tooling" as a demand risk [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016826000016/avgo-20260201.htm). Externally, MediaTek began shipping AI accelerators in Sep 2026 [via BigGo](https://finance.biggo.com/news/TW_2454.TW_2026-10-30), and Broadcom names the "MediaTek version v8t".
9. **Backlog versus RPO.** The "AI backlog >$73B" (Dec 2025) compares with total RPO of $33.3B (2 Nov 2025). These are different measures, and RPO counts only firm non-cancellable amounts. [CO](https://www.sec.gov/Archives/edgar/data/1730168/000173016825000121/avgo-20251102.htm)
10. **Meta MTIA status.** "We are shipping now" (Mar 2026). Then "production shipments" expected in Q4 FY2026 (Sep 2026), and the first 1 GW order delivers from H2 2027 (Jun 2026). "Recent analyst reports" questioning MTIA were cited but not identified. [CO] — [Q1](https://www.fool.com/earnings/call-transcripts/2026/03/04/broadcom-avgo-q1-2026-earnings-call-transcript), [Q2](https://www.fool.com/earnings/call-transcripts/2026/06/03/broadcom-avgo-q2-2026-earnings-transcript/), [Q3](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/)
11. **Google long-term agreement end date.** The 8-K sentence places "through up to 2031" after the supply assurance (networking) clause, so it is ambiguous whether 2031 also applies to the TPU agreement [CO](https://www.sec.gov/Archives/edgar/data/1730168/000119312526144028/d87999d8k.htm). Press reports the TPU agreement runs to 2031 [SUMMARY-ONLY: DCD](https://www.datacenterdynamics.com/en/news/broadcom-to-develop-google-tpus-until-2031-anthropic-signs-deal-with-both-companies-for-35gw-of-tpus/).
12. **TPU 8 timing.** Social and press items said both v8 chips target TSMC 2nm in late 2027 [SUMMARY-ONLY: X post](https://x.com/mark_k/status/2046984786749624568). In contrast, Google said GA "later this year" (2026) [CUST](https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/eighth-generation-tpu-agentic-era/), and Broadcom (Sep 2026) and MediaTek (Sep 2026 first shipments) both describe 2026 shipments.
13. **Apple timing.** The Information (Dec 2024) said mass production in 2026 [PRESS-UNNAMED](https://bnnbloomberg.ca/business/technology/2024/12/11/apple-is-working-on-ai-chip-with-broadcom-information-reports). A Bloomberg-based report says completion by 2027 [SUMMARY-ONLY](https://www.tomshardware.com/pc-components/cpus/apple-reportedly-readies-baltra-processors-for-ai-servers). Broadcom's 8-K (Jul 2026) does not mention AI [CO](https://www.sec.gov/Archives/edgar/data/1730168/000119312526295589/d84378d8k.htm).
14. **Transcript error.** The Motley Fool Q3 FY2026 transcript labels the CFO "Amie O'Toole". The 8-K and the Investing.com transcript say Amie Thuener. [CO](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm)

### Inferences
- Most contradictions are framing changes in Broadcom's own disclosures (gigawatts, margins, backstops, racks) rather than outside parties disputing Broadcom's facts. Customers' own statements (Google, Meta, Anthropic) are consistent with Broadcom's customer list but give fewer specifics, and none confirms Broadcom's per-generation role.

### Gaps
- TSMC, NVIDIA and Marvell statements specifically about Broadcom were not retrieved. TSMC does not name customers. I did not retrieve NVIDIA's ASIC commentary or Marvell's earnings remarks.
- SemiAnalysis full reports and teardowns are paywalled or were not retrieved.

## 10. Closing lists: (a) contradictions found, and (b) items not found or not verified, including the four memory leads

### Takeaway
All four memory leads are confirmed or partly confirmed. Anthropic was customer #4 with a $10B order and a further $11B; customer #5 placed about $1B; the AI backlog was more than $73B; Google does dual-source TPU v8 with MediaTek, though the variant mapping is disputed; and Microsoft's talks with Broadcom were reported but are not confirmed as a deal. Many legal and regulatory items and product launch dates remain unverified.

### Cited Findings
**(a) Contradictions** (details and sources in Section 9):
1. $10B customer: FT said OpenAI; Broadcom said Anthropic.
2. TPU v8 variant mapping: press says Broadcom builds 8t and MediaTek 8i; Broadcom's call says Broadcom ships v8i and MediaTek v8t.
3. Anthropic 2027 capacity: >3 GW, then ~3.5 GW (8-K), then 5 GW (calls).
4. OpenAI: "start H2 2026" became prototype in late 2026 and volume in 2027–28.
5. Gross margin impact: "not substantial" became Q4 ~73% against 78% a year earlier.
6. "All a chip business only" versus rack sales and leases.
7. "Not backstopped" (3 Jun) versus the $29B backstop (8 Jun) and the $43B backstop (26 Oct 2026); "modest" guarantees versus $43B.
8. Customer-owned tooling dismissed on calls but added as a risk factor in 10-Qs from Mar 2026, while MediaTek is shipping.
9. AI backlog of $73B versus RPO of $33.3B (different measures).
10. Meta MTIA: "shipping now" (Mar 2026) versus production shipments expected in Q4 FY2026 and the first GW from H2 2027.
11. Ambiguous 2031 scope in the Google 8-K versus press reports.
12. Press "late 2027" TPU 8 timing versus 2026 shipments.
13. Apple Baltra timing (2026 versus 2027) and the Broadcom 8-K's silence on AI.
14. Transcript misnaming of the CFO.

**Status of the memory leads**
- "Anthropic was the $10B customer #4": **confirmed** [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/). Broadcom said the $10B order was for "TPU Ironwood racks".
- "Further $11B order disclosed Dec 2025": **confirmed**, for delivery in late 2026 [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/).
- "~$1B order from customer #5": **confirmed**, for delivery in late 2026 [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/).
- "AI backlog ~ $73B in Dec 2025": **confirmed** as ">$73 billion" over 18 months, out of a $162B consolidated backlog [CO](https://www.fool.com/earnings/call-transcripts/2025/12/12/broadcom-avgo-q4-2025-earnings-call-transcript/).
- "Google uses MediaTek for some TPU variants": **confirmed in substance.** Broadcom itself refers to the "MediaTek version v8t" [CO](https://www.fool.com/earnings/call-transcripts/2026/09/09/broadcom-avgo-q3-2026-earnings-call-transcript/), and MediaTek started shipments in Sep 2026 without naming the customer [via BigGo](https://finance.biggo.com/news/TW_2454.TW_2026-10-30). Which variant MediaTek builds is disputed.
- "Microsoft held talks about moving custom-chip work to Broadcom": **reported only** (The Information, Dec 2025, unnamed sources) [PRESS-UNNAMED](https://finance.yahoo.com/news/marvell-stock-falls-microsoft-broadcom-130457554.html). No deal was confirmed as of 14 Nov 2026, and Microsoft is not among Broadcom's four named XPU customers.

### Inferences
- These conclusions rest mainly on SEC filings and two independent transcript services. Where only one source exists, such as single-transcript quotes from the Q1 and Q2 calls, exact wording should be treated as transcription-dependent.

### Gaps
**(b) Not found or not verified in this session**
- Q4 FY2026 results: not released; expected around mid-Dec 2026 (inferred from the 11 Dec 2025 prior-year date).
- Exact product launch dates and specifications for Tomahawk 6, Tomahawk Ultra, Jericho3-AI/Jericho4, Thor Ultra and TH6-Davisson CPO, and 3.5D XDSiP shipment status.
- Broadcom's role in TPU v1 through v6.
- ByteDance status, chip and export-control constraints (TSMC foundry rules).
- China SAMR conditions on VMware; the EU (CISPE), US and UK VMware lawsuits and complaints; patent suits on custom silicon.
- Head of the ASIC division (Frank Ostojic is unverified).
- TSMC CoWoS allocation to Broadcom; HBM procurement responsibilities; the Anthropic rack integrator.
- MLPerf results; independent SerDes, CPO or 3.5D verification; 2nm yields and costs; SerDes power.
- Identity of the customer behind the Oct 2026 $43B SPV backstop and the $42B convertible-note facility.
- Reports of Google moving TPU work (The Information, 2025) and of OpenAI chip delays: the primary articles were not retrieved, and no delay report was found.
- xAI and SoftBank/Arm links to Broadcom: no credible source found.
- Up-to-date 13F or 13G holdings after 2024.

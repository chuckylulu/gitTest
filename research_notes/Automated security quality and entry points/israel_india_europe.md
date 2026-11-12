# Automated security in Israel, India and Europe: quality tests, path forward and entry points (research date 2026-11-12)

Conventions used below. "[company claim, unconfirmed]" = a statement only the company has made. "[search extract]" = taken from a search-engine summary of the page; the page itself was not opened in this session. "[sibling notes]" = a fact taken from the parallel research notes in `research_notes/AI capability advances last 30 days/` and `research_notes/AI lab views on AI progress/`, which cite the primary URL given; I did not re-open those pages. All market data are delayed quotes from StockAnalysis.com (S&P Global data), read on 2026-11-12. Session limits: the shared web-search budget ran out part-way through and Firecrawl credits were exhausted, so later facts come only from direct fetches of known pages (CTech/Calcalist tag pages, company and EU pages, StockAnalysis). Coverage of ESET, Sekoia, Detectify, Eviden/Atos, Airbus Protect, Thales's cyber segment, Tata Communications and the smaller Indian vendors is therefore thin (see the Gaps sections). Companies other researchers cover (Check Point, CyberArk/Palo Alto, Wiz/Google, Armis, Claroty, Pentera, Cymulate, Picus, Checkmarx, JFrog, Snyk, Aikido, GitGuardian, YesWeHack, Intigriti, NCC Group, ONEKEY, Cybellum, Zero Networks, Waterfall, Radiflow, Cylus, Certora, TrustInSoft, AbsInt, Cryspen) appear only as context.

## 1. Which companies from these regions, if any, belong among the 8–15 automated-security companies that matter most globally?

### Takeaway
None of the companies I covered clearly belongs in a global top 8–15 for automated vulnerability discovery and repair. None owns a strong "judge" for that work, and none is named in Anthropic's or Google's gated programmes. Cato Networks (Israel) is the strongest borderline case: $415M ARR growing 42% (July 2026), OpenAI Daybreak partner status, and a network-level "shielding" position. Cyera (Israel) is borderline on capital and momentum (valuation above $12B, $1.4B raised in 2026), but it shows no lead evidence or gated-model access. India has no candidate. In Europe, Darktrace and Sophos have Daybreak access and detection-and-response scale, but there is no outside evidence that either leads in machine-speed find-and-fix. The region's real top-tier contenders are mostly firms other researchers cover (Check Point, CyberArk inside Palo Alto, Wiz inside Google, Armis, Pentera, Checkmarx, Snyk).

### Cited Findings
**Gated US frontier-model programmes and named regional participants**
- Anthropic Project Glasswing: the initial cohort (early April 2026) included AWS, Apple, Broadcom, Google, Microsoft, Palo Alto Networks and CrowdStrike [search extract] — [ITPro](https://www.itpro.com/technology/artificial-intelligence/project-glasswing-anthropic-announces-big-tech-consortium-to-test-claude-mythos-ai-model-that-could-reshape-cybersecurity). Anthropic's expansion post (June 2, 2026) adds "approximately 150" organisations in "more than 15 countries" on top of a roughly 50-partner first cohort, but names none of them. Each must meet Anthropic's security requirements. The post also refers to the Cyber Verification Program and Claude Security — [Anthropic, 2026-06-02](https://www.anthropic.com/news/expanding-project-glasswing).
- Coverage of the Glasswing expansion says it includes "European nations for the first time". It also reports that a European Commission spokesperson welcomed possible future use by ENISA, with ENISA's terms still under negotiation [search extract; outlet not pinned down] — [Capacity](https://capacityglobal.com/news/anthropic-takes-project-glasswing-to-15-countries/); [BankInfoSecurity](https://www.bankinfosecurity.com/anthropic-expands-mythos-to-global-critical-infrastructure-a-31836). I found no source naming any Israeli, Indian or European company as a Glasswing partner.
- Anthropic's Claude Mythos 5.2 (Nov 9, 2026): its cyber capabilities are accessible through the Cyber Verification Program, and Claude Enterprise customers can access Claude Security [sibling notes] — [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2).
- OpenAI Daybreak: OpenAI announced the Daybreak Cyber Partner Program on June 22, 2026. Darktrace joined, to use OpenAI models "to help customers assess the business impact of cyber events". Check Point was "selected" to embed OpenAI models, with a "deliberate and gradual" rollout — [Channel Insider, 2026-06-23](https://www.channelinsider.com/ai/openai-daybreak-cyber-program-security-tools/).
- Cato Networks joined the Daybreak Cyber Partner Program (announced June 22, 2026), having been in OpenAI's Trusted Access for Cyber programme since May 1, 2026 [search extract of company release] — [Cato release via PR Newswire](https://www.prnewswire.com/il/news-releases/cato-advances-enterprise-defense-joining-the-openai-daybreak-cyber-partner-program-302805920.html); [Ynet](https://www.ynetnews.com/tech-and-digital/article/skhk2tpmgl).
- On Aug 11, 2026, Daybreak access was extended to "Accenture, IBM, CrowdStrike, Cisco, Sophos and Cloudflare". There are two tiers. Daybreak Blue gives frontier general models (GPT-5.6 Sol) for defensive work. Daybreak Red gives models for "vulnerability research, security testing, and exploit validation", including GPT-5.6-Cyber — [Engadget, 2026-08-11](https://engadget.com/2234335/openai-daybreak-model-less-likely-to-refuse-higher-risk-tasks).
- OpenAI's August post on Daybreak names "Accenture, IBM, Capgemini, Cognizant, EY" among security and services partners [search extract] — [OpenAI](https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands). OpenAI's partner page carries partner statements from Akamai, Cato Networks, Fortinet and Okta [search extract; page returned 403 when fetched] — [OpenAI Daybreak partners](https://openai.com/daybreak/partners-new/).
- GPT-6 Cyber (Nov 5, 2026) was first limited to selected approved customers in Daybreak Red [sibling notes] — [SiliconANGLE](https://siliconangle.com/2026/11/05/openai-launches-gpt-6-cyber-a-gpt-6-astra-model-built-to-keep-vulnerability-research-in-scope/).
- Google DeepMind's Fairwind Program (Sept 2, 2026) offers Gemini 3.8 Flash Cyber with CodeMender. Google says it works with "over 650 partners". The partners named in coverage are CrowdStrike, Datadog, Menlo Security, Palo Alto Networks and Snowflake. No Israeli, European or Indian organisation is named; Bitdefender and XM Cyber appear only as advertisers — [The Hacker News, 2026-09-02](https://thehackernews.com/2026/09/google-anthropic-and-openai-unveil.html). The Fairwind page restricts access to approved partners' internal cyber, incident-response and penetration-testing teams — [Google DeepMind](https://deepmind.google/fairwind-program/). Gemini 4 Carbon (Oct 28, 2026) went first to Fairwind participants, and its low-guardrail cyber version remained Fairwind-only after the Nov 10 public opening [sibling notes] — [Forbes](https://www.forbes.com/sites/janakirammsv/2026/10/30/google-limits-gemini-4-carbon-to-vetted-cyber-defenders/); [technology.org](https://www.technology.org/2026/11/11/gemini-4-carbon-available-developers-ai-ultra-pricing/).
- Indian IT firms: the search found no Daybreak, Glasswing or Fairwind participation by TCS, Infosys, Wipro or HCLTech. They have general AI partnerships instead: Infosys with Anthropic (February 2026) and OpenAI (April 2026); HCLTech with its own OpenAI agreement; TCS building data centres with OpenAI as anchor tenant for Stargate India; Wipro aligned with Microsoft — [Analytics India Magazine, 2026-05-07](https://analyticsindiamag.com/it-services/indian-its-biggest-ai-partners-are-its-newest-enterprise-threats); [TechCrunch, 2026-04-22](https://techcrunch.com/2026/04/22/openai-teams-up-with-infosys-to-bring-ai-tools-to-more-businesses/) [search extract].

**Scale markers of the regional candidates (details in sections 2–4)**
- Cato: $415M ARR, +42% year on year (July 27, 2026) [company figure] — [CTech](https://www.calcalistech.com/ctechnews/article/b1bqq6nrfg).
- Cyera: valuation above $12B; $1.4B raised in 2026 (to Sept 2026) — [CTech, 2026-10](https://www.calcalistech.com/ctechnews/article/8e72dv4yf).
- Island: $6.4B valuation (Sept 24, 2026); about $200M revenue [company claim, unconfirmed] — [CTech](https://www.calcalistech.com/ctechnews/article/bkonawz9fx); [CTech](https://www.calcalistech.com/ctechnews/article/s1114h6yfze).
- Axonius: over $200M ARR, +35% — [CTech, 2026-11-09](https://www.calcalistech.com/ctechnews/article/9upwifo24).
- Darktrace: ARR was $782.2M at the last public report before Thoma Bravo took it private in 2024 [search extract] — [Sharecast](https://sharecast.com/news/news-and-announcements/darktrace-reports-continued-strong-top-line-growth-ahead-of-thoma-bravo-takeover--17100755.html).
- Bitdefender: 2025 revenue $480M, +11% — [Financiarul, 2026-07-06](https://financiarul.ro/companii/bitdefender-a-avut-venituri-de-480-de-milioane-de-dolari-in-2025-si-amana-l/).
- Sophos: named a Leader in the 2026 IDC MarketScape for Worldwide Modern Endpoint Security for Enterprises (October 2026) — [Sophos press page](https://www.sophos.com/en-us/press).
- Securonix: described as a five-time Leader in the Gartner Magic Quadrant for SIEM (June 2025) — [SiliconANGLE, 2025-06-11](https://siliconangle.com/2025/06/11/securonix-acquires-threat-intelligence-startup-threatquotient/).

### Inferences
- **Gated-model access is the clearest separating test, and the regions split on it.** Israel has two names with confirmed early OpenAI access: Cato, and Check Point (covered elsewhere). Europe has three: Darktrace, Sophos, and Capgemini on the services side. India has none. None of these regions has a named participant in Anthropic's or Google's gated programmes; for Glasswing, that is because Anthropic names no expansion partners at all. Access looks unequal by country in practice, though not by stated rule. US platforms such as CrowdStrike and Palo Alto appear in all three programmes.
- **No regional company owns a strong "judge" for automated find-and-fix.** Cato's 45-minute CVE "time-to-protect" [company claim, unconfirmed] is a shielding capability, not a judge. Cyera's data classification and Axonius's asset inventory are measurements, but not ones that decide whether a fix is right. Yubico owns a hardware constraint that AI cannot remove (possession-based, phishing-resistant authentication). secunet appears to hold a regulator-recognised sovereign position in Germany (95% public sector; see section 4). Neither of those last two is automated vulnerability discovery.
- **Suggested tiering for a global list:**
  - Borderline include: Cato Networks. It has scale, growth, Daybreak access and a shielding product line, but no lead evidence was retrieved in this session.
  - Watch-list, not top 15: Cyera and Island (capital-rich AI-agent control layers, lead unverified); Upwind (runtime cloud, $50M ARR, small); Axonius (growth slowed to 35%); Darktrace and Sophos (large detection-and-response incumbents with Daybreak access, but no evidence of machine-speed fixing leadership, and Darktrace's growth reportedly slowing).
  - Exclude: XM Cyber (CrowdStrike bought its technology), Zafran (founder departure, Cisco talks at a "steep discount"), all Indian vendors, and the European listed small caps (F-Secure, Wallix, secunet, Yubico) as automated-security leaders.
- If the global list is built around automated discovery and repair, the Israeli representatives are more likely to be the already-covered names (Check Point, Pentera, Cymulate, Checkmarx, Snyk) or Israeli assets now inside US platforms (CyberArk in Palo Alto, Wiz in Google, Armis in ServiceNow) than any company in this file.

### Gaps
- Analyst rankings for Cato (SASE), Cyera (DSPM), Island (enterprise browser) and Darktrace (NDR) were not retrieved, because the search budget was exhausted, so the "lead" test is weak for every candidate.
- OpenAI's full Daybreak roster is published as a logo grid, and the page returned 403. Whether Cyera, Island, Upwind, Torq, Bitdefender, ESET, Thales, Atos/Eviden or any Indian firm is a member could not be confirmed either way.
- Anthropic does not name its approximately 150 Glasswing expansion partners or its Cyber Verification Program members, so absence from public lists is not evidence of absence.

## 2. Israel: company notes (ownership, funding and valuation, revenue, model, lead, frontier-model access, cross-border exposure) and the state of the ecosystem

### Takeaway
Israeli cyber is at a funding peak despite the war. YL Ventures counted $4.4B in 2025, a record, and Q3 2026 brought at least $2.425B, about 46% of global cyber funding. Exits were also large: Palo Alto–CyberArk closed on Feb 11, 2026 for $21.06B. Below that headline the field is splitting. Cato, Cyera, Island and Upwind are raising at rising valuations around securing AI agents. XM Cyber has been hollowed out (CrowdStrike bought its IP for about $586M; 250 of 300 Israeli staff were laid off), Zafran faces discounted takeover talk after its founder left, and Axonius is cutting R&D in an "AI-driven" re-engineering. None of the private companies gives outside investors access except through secondaries or fund stakes, and Cato's IPO still has no date.

### Cited Findings
#### Ecosystem
- YL Ventures' State of the Cyber Nation (2025): $4.4B across 130 rounds (record), against $689M in 2015. Global VCs outpaced Israeli VCs at every stage for the first time. There were 12 Israeli-on-Israeli acquisitions (acquirers include Check Point, Cato, Cyera, Pentera and Orca). Security-for-AI led seed funding with 12 companies. The 2025 mega-rounds were Cyera $540M, Armis $435M, Cato $359M, Island $250M and Dream Security $100M — [Ynet](https://www.ynetnews.com/business/article/rjggjusz11g) (article undated; full report scheduled for Jan 7, 2026).
- Other 2025 tallies differ because they measure different scopes. Cybertech put Israeli cyber fundraising at $8.27B and exits at $72.6B [search extract] — [Ynet](https://www.ynetnews.com/business/article/b1uoo5nlze). NightDragon counted 20 Israeli cyber exits worth $59B in the first eight months of 2025 [search extract] — [CTech](https://www.calcalistech.com/ctechnews/article/sk12dfuslx).
- Q3 2026: Israeli startups raised at least $2.425B across 26 disclosed rounds. Global cyber funding was $5.26B, the highest quarter since 2022 (Pinpoint Search Group via WSJ). About 20 of the 26 rounds went to companies securing AI agents, machine identities or AI-era infrastructure. The article warns that more than 20 startups chase overlapping problems and that some valuations "will be hard to justify" — [CTech, published 2026-10-09](https://www.calcalistech.com/ctechnews/article/8e72dv4yf).
- Palo Alto–CyberArk: announced at about $25B in July 2025 and closed on Feb 11, 2026. Total consideration was $21.061B, and the shares issued were worth about $36.6B at the Nov 10, 2026 close ($326.36 per PANW share). Palo Alto was reported in talks for Clutch Security ($500M) and Beacon — [CTech, 2026-11-11](https://www.calcalistech.com/ctechnews/article/hy11rj2wrgx).
- War: on Mar 31, 2026 CTech described Cato's hiring push as taking place "amid war", without naming the conflict — [CTech](https://www.calcalistech.com/ctechnews/article/syecewyszl). An Axonius HR interview (May 27, 2026) said people are "considering where they see their future and whether that's in Israel or abroad" — [CTech](https://www.calcalistech.com/ctechnews/article/c81815hkp).
- Regulation and enforcement: Sygnia's CEO said (June 21, 2026) that Israel has not built an enforcement environment for civilian companies comparable to the EU, Australia or parts of the US ("In Israel, this is not the situation yet"). He also said exploit development has fallen from "weeks or months" to hours, and that none of Israel's critical infrastructure has had a significant cyber outage — [CTech, 2026-06-21](https://www.calcalistech.com/ctechnews/article/syejhghzgx).

#### Cato Networks (SASE; private)
- Funding and valuation: $359M at more than $4.8B (June 30, 2025), with a third of the funding going to employees and the IPO "kept on ice" — [CTech](https://www.calcalistech.com/ctechnews/article/pmald8ywg). A Mar 31, 2026 CTech article calls it a "$409 million Series G" at above $4.8B — [CTech](https://www.calcalistech.com/ctechnews/article/syecewyszl). The $359M vs $409M discrepancy is unresolved; the extra $50M may be an extension. Total raised is about $1.1B. Employees sold another roughly $100M in shares on Sept 29, 2026 (the second employee secondary in about a year), with no implied valuation disclosed — [CTech tag page](https://www.calcalistech.com/tags/Cato_Networks); [CTech](https://www.calcalistech.com/ctechnews/article/2m3af3ns2).
- Revenue: a $350M run rate in 2025, +43% — [CTech, 2026-02-24](https://www.calcalistech.com/ctechnews/article/rjf7exsube). $415M ARR, +42% year on year, with growth accelerating in Q2 2026 [company figure]. Profitability is not disclosed. Headcount is about 1,800, roughly half in Israel. The chief strategy officer said "We have not stopped planning the IPO", with no timing given. CEO Shlomo Kramer denied reported CrowdStrike acquisition talks — [CTech, 2026-07-27](https://www.calcalistech.com/ctechnews/article/b1bqq6nrfg); [Globes](https://en.globes.co.il/en/article-1001550594).
- AI and automation: Cato acquired Aim Security (AI security) for $350M (Sept 3, 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/7pzhe3mrd). Cato says it launched an AI security offering in March 2026 and added AI-agent governance in Q2 [company claim, unconfirmed]. It says it cut its time to protect against newly disclosed CVEs to 45 minutes [company claim, unconfirmed] — [CTech, 2026-07-27](https://www.calcalistech.com/ctechnews/article/b1bqq6nrfg). At Black Hat (August 2026) it presented "Agentic Threat Prevention" [company claim, unconfirmed] — [CTech, 2026-08-04](https://www.calcalistech.com/ctechnews/article/rygsooy8fx).
- Frontier-model access: in OpenAI Trusted Access for Cyber since May 1, 2026 and a Daybreak Cyber Partner from June 22, 2026 (see section 1).
- Cross-border: opened a London AI-focused engineering hub (June 3, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/bkuhtb6xzl). Planned 140 hires in Israel "amid war" (Mar 31, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/syecewyszl).

#### Cyera (data security / AI-era data "trust layer"; private)
- $400M Series F at $9B (January 2026, led by Blackstone funds); total funding then above $1.7B — [Cyera press release](https://www.cyera.com/press-releases/cyera-raises-400m-to-meet-rapidly-growing-demand-for-ai-security-among-enterprises); [TechRepublic](https://www.techrepublic.com/article/news-cyera-january-2026-funding/).
- $600M Series G at $12B (June 2026), led by Evolution Equity Partners, with Cyberstarts, Temasek, Accel, AT&T Ventures, Blackstone, Coatue and Spark — [Cyera press release](https://www.cyera.com/press-releases/cyera-raises-600-million-at-12-billion-valuation-to-continue-building-the-trust-layer-for-the-ai-era); [Globes](https://en.globes.co.il/en/article-1001545507).
- September 2026: $400M from Goldman Sachs, bringing 2026 funding to $1.4B and the valuation above $12B — [CTech, 2026-10-09](https://www.calcalistech.com/ctechnews/article/8e72dv4yf).
- Cyera says it tripled ARR three years in a row but gives no figures [company claim, unconfirmed; search extract of press release]. Valuation path: $3B (late 2024), $6B (mid-2025), $9B (January 2026), $12B (June 2026) [search extract] — [Pulse 2.0](https://pulse2.com/cyera-raises-600-million-at-12-billion-valuation-in-rapid-ascent-to-top-of-data-security-market/amp/).
- No Daybreak, Glasswing or Fairwind participation found.

#### Island (enterprise browser to control layer for employees and AI agents; private)
- $250M at $4.8B (March 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/1pcuwcvaj); J.P. Morgan at $4.8B (July 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/1fbqnnbnh); an employee secondary of $250–300M at about $5B (Sept 16, 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/yt2l11c40); $400M at $6.4B (Sept 24, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/bkonawz9fx).
- Co-founder Dan Amiga reports about $200M revenue and roughly 100% annual growth (Sept 10, 2026) [company claim, unconfirmed] — [CTech](https://www.calcalistech.com/ctechnews/article/s1114h6yfze).

#### Upwind (runtime-first cloud security; private)
- $250M Series B at $1.5B (Jan 26, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/rkoe111h8be); Salesforce Ventures at $1.6B (Mar 24, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/sjxxkfgize); $300M at $3.8B led by Bessemer and TCV (Sept 2, 2026), expanded to $400M at the same valuation (Oct 28, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/rohkgwlwu).
- ARR above $50M, up from about $20M at end-2025 (reported by CTech, not independently verified) — [CTech, 2026-10-28](https://www.calcalistech.com/ctechnews/article/rohkgwlwu).
- Datadog was in talks to acquire it for $1B (July 22, 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/1146p9qyl). CTech's Oct 22, 2026 headline asks "Did Datadog really offer $4 billion" — [CTech](https://www.calcalistech.com/ctechnews/article/plg9r2pk0). Upwind acquired Aegis (AI-agent security, September 2026) and Nyx (April 2025) — [CTech tag page](https://www.calcalistech.com/tags/Upwind).
- At Black Hat 2026 it launched an AI Agent Context Scanner for system prompts, tools and MCP connectors [company claim, unconfirmed] — [CTech, 2026-08-04](https://www.calcalistech.com/ctechnews/article/rygsooy8fx).

#### Axonius (cyber asset visibility; private)
- $2.6B valuation (March 2022 round and March 2024 extension) — [CTech](https://www.calcalistech.com/ctechnews/article/hkfogi4tp). Acquired Cynerio (healthcare IoT) for $180M (July 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/hkek009mdle). Cisco was in advanced talks to buy it for $2B (Jan 4, 2026); no deal followed in the sources seen — [CTech](https://www.calcalistech.com/ctechnews/article/bjxge1de11l).
- Leadership: the CEO stepped back "as IPO nears" (February 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/r1so8odpwx). Joe Diamond became permanent CEO in May 2026. ARR passed $200M in Q1 FY2027, +35% year on year, with nearly 1,000 customers including more than 100 of the Fortune 1000. On Nov 9, 2026 the company cut 66 jobs (9% of 722), including 46 at the Israeli development centre (about 22% of 207 Israeli staff), to reshape engineering around "a new AI-driven way of working" — [CTech, 2026-11-09](https://www.calcalistech.com/ctechnews/article/9upwifo24).

#### Torq (AI SOC / autonomous security operations; private)
- $140M at $1.2B (Jan 11, 2026); Torq runs security operations with autonomous AI agents — [CTech](https://www.calcalistech.com/ctechnews/article/bkaxxwwhzx). Acquired Jit (AppSec automation, context graph, about 30 engineers) for an estimated $70M (May 19, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/h1rtehykml). In 2024 it targeted $100M ARR by end-2026 [company claim, unconfirmed] — [CTech, 2024-09-24](https://www.calcalistech.com/ctechnews/article/sjt008nlrr).

#### Zafran (exposure management / mitigation; private)
- $60M raise that doubled its valuation, choosing independence over takeover offers (Dec 2, 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/s1e1gw3zbl). American Express invested (Feb 25, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/tg4phxk5v). Cisco was in talks to buy it "at steep discount", with figures of $150–200M reported (July 20, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/by11gqei4zx). After its founder left, Cisco invested instead (July 22, 2026) — [CTech](https://www.calcalistech.com/ctechnews/article/a6lm0ykz3). Its Q3 2026 raise was undisclosed — [CTech](https://www.calcalistech.com/ctechnews/article/8e72dv4yf).

#### XM Cyber (attack-path / exposure management; owned by Germany's Schwarz Group)
- Schwarz Group bought it for $700M (November 2021) — [CTech](https://www.calcalistech.com/ctech/articles/0,7340,L-3923098,00.html). CrowdStrike acquired XM Cyber's source code and IP, including more than 45 patents, but not its revenue or customers. Terms were $145M in cash and shares at signing (July 2026) plus 2,118,022 CrowdStrike shares issued at closing (about $441M at $208), for an implied total of about $586M. XM Cyber continues as a standalone business serving existing customers under a licence. The deal includes a partnership around Schwarz Digits' STACKIT sovereign cloud. An estimated backlog of about $450M stays outside the sale — [CTech, 2026-10-13](https://www.calcalistech.com/ctechnews/article/sje00evoizx). About 250 of 300 Israeli employees were laid off — [CTech, 2026-10-13](https://www.calcalistech.com/ctechnews/article/0x146nqil).

#### Noma Security (AI-agent security; private)
- $100M raise (July 31, 2025); no later valuation, ARR or customer data found — [CTech](https://www.calcalistech.com/ctechnews/article/s19xaaudxl); [CTech tag page](https://www.calcalistech.com/tags/Noma_Security).

#### Sygnia (incident response and consulting; owned by Temasek since 2018)
- Temasek acquisition — [CTech, 2018](https://www.calcalistech.com/ctech/articles/0,7340,L-3747753,00.html). The CEO changed twice in six months (Avi Golan, March 2025; Guy Segal replaced him in September 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/sytn4z00nlg). It led the Bybit hack forensics (February 2025) — [CTech](https://www.calcalistech.com/ctechnews/article/bjt11ar25kl). No revenue data found.

### Inferences
**Cato Networks**
- Quality tests:
  - (a) Position: moderate-strong. It owns the network enforcement point where shielding of unpatchable or not-yet-patched assets can happen fast (the 45-minute CVE protection is a claim). It does not own a judge, and SASE competitors (Zscaler, Palo Alto, Netskope) can match.
  - (b) Lead: unverified this session. Gated OpenAI access is outside evidence of standing, but not of lead.
  - (c) Revenue model: subscription. ARR is the reported metric, and there is no labour model.
  - (d) Financial strength: about $1.1B raised and recurring secondaries suggest liquidity. Margins and free cash flow are undisclosed.
  - (e) Resilience: steady scenario good; pause scenario weakens the IPO window and private marks; acceleration helps if Daybreak access deepens. About half the staff are in Israel, a war and geopolitical exposure partly hedged by London.
- Path forward:
  - Transitions: (3) shielding is shipped in the platform; (2) machine-speed response is claimed; (4) dependence on gated models, done via TAC and Daybreak but not exclusive; (5) EU and UK regulation helps SASE demand.
  - Plan: funded. Timing is plausible for products and unclear for the IPO.
  - What must go right: proof that AI-generated protections are faithful, continued Daybreak access, and an IPO window.
  - Suggested verdict: partly coherent. The direction is shipped and funded, but the AI claims are unconfirmed and profitability is unknown.
- Entry point (private): last primary mark more than $4.8B (June 2025), about 11.6x the July 2026 ARR of $415M on that stale mark. Employee secondaries have run without a disclosed price, and there is no IPO date. Outside investors can get exposure only via secondary platforms or fund LP stakes. Suggested label: cannot assess.

**Cyera**
- Quality tests:
  - (a) Position: data-access control for AI agents, a measurement-type position. AI may raise its value (more agents touching data) rather than close it, but it is not a find-and-fix judge.
  - (b) Lead: no outside ranking retrieved. Capital raised is not evidence of lead.
  - (c) Revenue model: subscription (presumed; not disclosed).
  - (d) Financial strength: very large cash raises ($1.4B in 2026). Burn is unknown.
  - (e) Resilience: high sensitivity to a 2028 financing-led pause, given a valuation above $12B with undisclosed ARR.
- Path forward:
  - Transitions: (4) AI-agent data control; (5) privacy regulation (GDPR, India's DPDP) supports demand.
  - Said vs done: acquisitions done (an acquirer in YL's list). Nothing confirmed on gated-model access.
  - Suggested verdict: partly coherent.
- Entry point (private): ARR undisclosed, so no multiple can be computed. Investors are Blackstone, Goldman, Temasek and others; no IPO plan was found. Suggested label: cannot assess (and likely stretched if ARR is below about $400M; that threshold is my inference, not data).

**Island**
- Quality tests:
  - (a) Position: the browser as a control layer for employees and agents. It is useful, but browser makers (Google, Microsoft) and SASE vendors can close the gap.
  - (b) Lead: the revenue figure is a company claim.
  - (c) Revenue model: subscription.
  - (d) Financial strength: about $400M fresh cash.
  - (e) Resilience: pause-sensitive.
- Path forward: (3) and (4). Suggested verdict: partly coherent.
- Entry point: about 32x the claimed $200M revenue at $6.4B. Suggested label: stretched (private, no access).

**Upwind**
- Quality tests:
  - (a) Position: runtime evidence of exploitability is closer to a "judge" of which vulnerabilities matter than static scanners are. But cloud-native platforms (Wiz/Google, CrowdStrike, Palo Alto) compete directly.
  - (b) Lead: none confirmed.
  - (c) Revenue model: subscription.
  - (d) Financial strength: $400M fresh capital.
  - (e) Resilience: the most pause-sensitive name here (about 76x ARR).
- Path forward: (2) and (4). Suggested verdict: partly coherent.
- Entry point: $3.8B on more than $50M ARR. Suggested label: stretched. A Datadog bid, if real, would be the most likely route to outside exposure (via DDOG).

**Axonius**
- Quality tests:
  - (a) Position: an asset-inventory measurement layer. AI agents can increasingly assemble inventories from APIs, so the position is at risk.
  - (b) Lead: more than 100 Fortune 1000 customers (outside-reported).
  - (c) Revenue model: subscription.
  - (d) Financial strength: restructuring repeated (November 2025, February 2026, November 2026).
  - (e) Resilience: growth slowed to 35%; exit to a strategic buyer (Cisco talk) is the likely route.
- Path forward: transition (3) via Cynerio, done by acquisition; internal labour automation is happening (the AI-driven cuts). Suggested verdict: partly coherent.
- Entry point: about 10–13x ARR on the $2B Cisco talk or the $2.6B 2024 mark. Suggested label: fair, but there is no access.

**Torq**
- Quality tests:
  - (a) Position: autonomous SOC agents replace human triage, which is transition (2) itself. But model makers' own security agents and the SIEM incumbents compete.
  - (b) Lead: none confirmed.
  - (c) Revenue model: subscription.
  - (d) Financial strength: $140M raise.
- Path forward: the Jit acquisition extends it into code security, so (1), (2) and (6)-adjacent. Suggested verdict: coherent in direction, scale unverified.
- Entry point: $1.2B with ARR unknown. Suggested label: cannot assess.

**Zafran**
- Quality tests: (a) exposure prioritisation is a gap that frontier models and platforms are closing; (b) no lead; (d) founder departure plus discounted bid talk (about $150–200M) signal weakness.
- Suggested verdict: not coherent as an independent company.
- Entry point: cannot assess. Indirect exposure via Cisco's minority stake is immaterial to Cisco.

**XM Cyber**
- Its technology now belongs to CrowdStrike, and the standalone company is a licence-based servicing shell with most of its Israeli staff gone. Suggested verdict: not coherent as an independent company.
- Exposure: via CrowdStrike (NASDAQ: CRWD; covered elsewhere) or Schwarz Group (private).
- The STACKIT sovereign-cloud partnership is a notable sovereignty-procurement datapoint: Israeli-origin exposure-management technology is being distributed through a German sovereign cloud by a US platform.

**Noma Security**
- AI-agent security with thin data. Suggested verdict: cannot assess. Entry point: cannot assess.

**Sygnia**
- Quality tests: (a) incident response sold as expert hours is the weakest position under the framework (labour). (b) Its Bybit forensics shows reputation but is not a lead metric.
- Path forward: transition (1) is a threat. CEO churn (2025) suggests strategy unsettled. Suggested verdict: cannot assess.
- Entry point: Temasek-owned, no outside access.

**Ecosystem**
- Capital is plentiful (Israel took about 46% of Q3 2026 global cyber funding), but rounds cluster around AI-agent security with overlapping products, which raises dispersion risk in the 2028 pause scenario.
- The labour model is shifting inside Israeli R&D itself (Axonius's "AI-driven" cuts, XM Cyber's collapse after its IP sale), while Cato says it is still hiring.

### Gaps
- No access to TASE/MAYA filings, Globes Hebrew or IVC/Startup Nation Central 2026 data in this session. I did not verify 2026 H1 Israeli totals, the Wiz and Armis closing dates and prices (covered by others), or Cato's Gartner standing.
- Israel National Cyber Directorate: I found no source in this session on its current head, its powers, the status of the long-pending cyber bill, or reporting duties. The only source is a CEO's view that enforcement is weak.
- Israeli export controls on offensive tools (the Defense Export Control Law and the Defense Export Controls Agency's licensing, including the 2021 tightening of the country list): not verified in this session. Background only; needs a primary source.
- The war: CTech refers to hiring "amid war" (March 2026) without naming the conflict. I found no quantified effect on cyber companies, such as reservist absence, investor behaviour or lost contracts.
- Cato's profitability, Cyera's ARR, Noma's and Torq's 2026 metrics, and the reason for the $359M vs $409M Cato round discrepancy are all unknown.

## 3. India: company notes and the IT-services labour model

### Takeaway
India has no automated-security company of global top-15 calibre. Quick Heal, the only listed pure play, is shrinking: Q2 FY27 revenue was down 22% year on year as consumer antivirus fell 40%. It is pivoting to enterprise EDR/XDR and data protection for the DPDP Act, and it trades at about 2.5x EV/Sales with about ₹232 crore net cash. CloudSEK (about $200M valuation) and Securonix (Vista-backed SIEM; headquarters not verified this session) are the notable private names, and data on the rest is thin. The big IT-services firms have general OpenAI and Anthropic partnerships but no named place in gated cyber programmes. Their labour model is visibly pressured: the Nifty IT index was down 23% year to date as of May 2026, and the model makers are launching their own services arms.

### Cited Findings
#### Quick Heal Technologies (NSE: QUICKHEAL)
- Q2 FY27 (July–September 2026, results Oct 27–28, 2026): revenue about ₹64.9 crore, −22% year on year from ₹83.5 crore; PAT ₹5.8 crore against ₹7.9 crore. Aggregator figures, not checked against the NSE filing [search extract] — [Sahi](https://www.sahi.com/news/quick-heal-technologies-reports-q2-net-profit-of-5-8-crore-versus-7-9-crore-yoy); [Arthneeti](https://www.arthneeti.com/insights/quick-heal-tech-q2-fy27-earnings).
- Concall (Oct 28, 2026):
  - Revenue mix: enterprise revenue ₹35 crore (+18% quarter on quarter, −4% year on year); consumer ₹36 crore (−40% year on year). Management expects enterprise to exceed 80% of revenue within three years, as "an expectation rather than formal guidance".
  - Products: EPP, EDR, XDR and DLP for micro, small and medium businesses. Quick Heal is not in firewall or security service edge.
  - Customers: wins in defence, BFSI and a large IT-services company. It is engaging customers on DPDP compliance.
  - Profit: EBITDA ₹2.3 crore, after a Q1 EBITDA loss of ₹17.6 crore and a Q1 PAT loss of ₹5.3 crore.
  - Balance sheet: receivables ₹98 crore, against ₹176 crore a year earlier; enterprise order book above ₹57 crore.
  - Guidance: none formal — [Multibagg, 2026-11-05](https://www.multibagg.ai/market-pulse/articles/quick-heal-enterprise-revenue-shift-concall-cmw349fd6004c2gtatbrn4zla).
- Market data (Nov 12, 2026, 3:30 pm IST): ₹150.47.
  - Size: market cap ₹8.17B (about ₹817 crore); EV ₹5.85B; net cash ₹2.32B; total debt ₹297M.
  - Multiples: EV/Sales 2.54; EV/FCF 12.7; P/S 3.54; P/B 1.87; P/E not meaningful.
  - Trailing twelve months: revenue ₹2.30B (−16.7%); net income −₹128M; free cash flow ₹460M; operating margin −24.4%.
  - Ownership and price: insiders (promoters) 72.95%; 52-week range ₹125–337; −52% over 52 weeks — [StockAnalysis statistics](https://stockanalysis.com/quote/nse/QUICKHEAL/statistics/); [StockAnalysis quote](https://stockanalysis.com/quote/nse/QUICKHEAL/).

#### Subex (NSE: SUBEXLTD), owner of Sectrio (OT/IoT security)
- Market data (Nov 12, 2026): ₹16.77; market cap ₹9.31B; EV ₹7.98B; EV/Sales 2.63; EV/EBITDA 16.8; P/E 22.6; net cash ₹1.33B; free cash flow ₹622M; trailing revenue ₹3.09B; operating margin 12.2%; +23.7% over 52 weeks; insiders 0.01% — [StockAnalysis](https://stockanalysis.com/quote/nse/SUBEXLTD/statistics/).

#### CloudSEK (AI-led external threat intelligence; private)
- $19M round at about $118M valuation, about five times the prior round (May 2025) — [Outlook Business](https://www.outlookbusiness.com/corporate/cloudsek-sees-5-fold-jump-in-valuation-in-19-million-fundraise-round). $10M in January 2026, completing Series B2 (total about $39M; valuation close to $200M), described as the first US state-backed fund investment in an Indian-origin cyber firm [search extract] — [Angel One](https://www.angelone.in/news/unlisted-companies/cybersecurity-firm-cloudsek-raises-10-million-first-indian-origin-company-backed-by-a-us-state-fund). CB Insights labels the January 2026 deal a secondary — [CB Insights](https://www.cbinsights.com/company/cloudsek/financials). Exfinity reportedly exited at 13x [search extract] — [Whalesbook](https://www.whalesbook.com/news/English/startupsvc/Exfinity-Exits-CloudSEK-With-13x-Return-Amid-AI-Cybersecurity-Boom/69f3207808235f0c2a1e7e7f).

#### Securonix (SIEM; private; listed under India in the brief; headquarters and India headcount not verified)
- More than $1B growth investment, mostly from Vista Equity Partners (2022), with Volition and Eight Roads. Acquired ThreatQuotient (June 11, 2025), and was described then as a five-time Gartner MQ SIEM Leader — [SiliconANGLE](https://siliconangle.com/2025/06/11/securonix-acquires-threat-intelligence-startup-threatquotient/); [SecurityWeek](https://www.securityweek.com/securonix-acquires-threat-intelligence-firm-threatquotient/). A June 29, 2026 CEO change to Toby Weiss appears on a single aggregator [unconfirmed] — [Simplify](https://simplify.jobs/c/Securonix).

#### IT services (TCS, Infosys, Wipro, HCLTech) and AI
- India's IT services industry is about $280B. The Nifty IT index was down 23% year to date, and the sector lost about $70B in market value "within weeks of Claude Code's February release" (AIM's phrasing). Anthropic's enterprise services venture reportedly has about $1.5B committed (WSJ), and OpenAI's has $4B from TPG, Brookfield and Bain (Bloomberg). Anthropic's applied AI engineers will "work alongside client teams to redesign workflows". The article does not mention cybersecurity services — [Analytics India Magazine, 2026-05-07](https://analyticsindiamag.com/it-services/indian-its-biggest-ai-partners-are-its-newest-enterprise-threats).
- TCS, Infosys and HCLTech hit 52-week lows after OpenAI's deployment-company launch [search extract; date not confirmed] — [Free Press Journal](https://www.freepressjournal.in/amp/business/tcs-infosys-hcl-tech-hit-52-week-lows-it-stocks-sink-as-openais-new-ai-venture-sparks-industry-fears).
- Capgemini (France) and Cognizant (US-listed, India-heavy delivery) are named among OpenAI's Daybreak security and services partners. No Indian-headquartered IT major is named [search extract] — [OpenAI](https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands).

### Inferences
**Quick Heal**
- Quality tests:
  - (a) Position: weak. Consumer antivirus is a gap that operating systems and AI close, and its enterprise EDR/XDR has no judge and no gated-model access.
  - (b) Lead: none. Its customers are Indian SMB, government and BFSI.
  - (c) Revenue model: licences and subscriptions. Deferred revenue of ₹48 crore suggests a partly recurring base.
  - (d) Financial strength: net cash about 28% of market cap and positive free cash flow. The free cash flow appears driven by collecting receivables (₹176 crore down to ₹98 crore), not by operating profit (inference). Revenue is concentrated in India.
  - (e) Resilience: largely independent of the AI-capex cycle, but exposed to substitution in all three scenarios. DPDP enforcement from about May 2027 is a domestic tailwind.
- Path forward: transitions (2) and (5) apply. Said: an enterprise share above 80% and data-privacy revenue matching endpoint "very soon". Done: enterprise growth of 18% quarter on quarter, but −4% year on year. Funded from cash. Suggested verdict: partly coherent at best, because the pivot is too small to offset consumer decline so far.
- Entry point: EV/Sales about 2.5x with negative operating margins, near the 52-week low. The price implies continued shrinkage, with option value in DPDP-driven enterprise demand. Near-term event: Q3 FY27 results (about late January 2027, inferred from the usual cycle). Suggested label: fair (cheap on cash, value-trap risk).

**Subex**
- (a) Position: Sectrio addresses transition (3), shielding OT and IoT devices that cannot be patched. Subex's revenue is still mostly telecom analytics (inference; no segment split retrieved).
- Suggested verdict: cannot assess. Entry point: EV/EBITDA 16.8x. Suggested label: cannot assess (security share unknown).

**CloudSEK**
- Small (total funding about $39M) and AI-native in external threat intelligence. There is no evidence of gated-model access or of lead. Suggested verdict: cannot assess. Entry point: private, about $200M valuation. Suggested label: cannot assess.

**Securonix**
- (a) Position: SIEM, under pressure from AI-native SOC platforms and hyperscaler SIEMs.
- (b) Lead: Gartner Leader as of June 2025.
- (c) Revenue model: subscription.
- Suggested verdict: partly coherent. Entry point: Vista-owned, no access. Suggested label: cannot assess.

**IT-services cyber practices**
- Position: largely billable hours and per-seat managed services, the weakest position under the framework. They are not in the named gated cyber programmes, unlike Accenture, IBM, Capgemini and Cognizant.
- Path forward: transitions (1) and (2) are threats. Partnerships with OpenAI and Anthropic are "said"; the model makers' own services ventures compete directly.
- Suggested verdict: partly coherent at group level, not coherent for labour-priced cyber services if machine-speed find-and-fix commoditises testing and triage hours.
- The near-term benefit is regulatory compliance work (CERT-In, DPDP, sector rules) that still needs people.

### Gaps
- No data retrieved for Sequretek, Astra Security, Appknox, Cyble or K7 Computing. I could not establish funding, revenue or AI-model access for them; they are listed as considered but not assessed.
- No cyber-segment revenue or headcount was found for TCS, Infosys, Wipro, HCLTech or Tata Communications, and no 2026 market data for these companies was fetched.
- Sectrio's revenue share within Subex is unknown.
- Securonix's headquarters (believed US, Texas) and 2026 metrics were not verified.
- Quick Heal's NSE filing was not opened; figures come from aggregators.

## 4. Europe: company notes

### Takeaway
Europe's relevant names are mostly mid-sized, PE-owned or sovereign-procurement plays, not automated find-and-fix leaders. Darktrace (Thoma Bravo) and Sophos (Thoma Bravo, owner of Secureworks) have Daybreak access. Darktrace's growth is reportedly slowing after two CEO changes; Sophos was named an IDC endpoint Leader in October 2026. WithSecure was taken private by CVC and Risto Siilasmaa (delisted March 2026). Bitdefender ($480M revenue in 2025, cash-rich) deferred its IPO to about end-2028. The listed names split sharply:
- secunet (+19% revenue, 95% public sector) fell 14% on its Nov 12 Q3 statement.
- Yubico re-rated: Q3 sales +29%, bookings +88%, trading at about 44x forward P/E.
- F-Secure trades near its 52-week low after warning that a large Tier 1 partner will not renew from March 2027.
- Wallix is small and 81% recurring.

### Cited Findings
#### Darktrace (UK; private, Thoma Bravo)
- The Thoma Bravo take-private (about $5.3B) closed in October 2024 [search extract] — [SecurityWeek](https://www.securityweek.com/darktrace-to-be-taken-private-in-5-3-billion-sale-to-thoma-bravo/amp/). Its last public ARR figure was $782.2M, +22.7% [search extract] — [Sharecast](https://sharecast.com/news/news-and-announcements/darktrace-reports-continued-strong-top-line-growth-ahead-of-thoma-bravo-takeover--17100755.html).
- CEO Jill Popelka was replaced in January 2026 after 16 months, and Ed Jennings became CEO in March 2026. The Times (March 2026) said revenue growth was slowing. The company plans $200M of US investment in 2026 and is pursuing revenue above $1B [search extract; pages returned 429/403 when fetched] — [Business Weekly](https://www.businessweekly.co.uk/posts/us-owner-seeks-new-ceo-for-ai-cyber-security-company-darktrace); [WebProNews](https://www.webpronews.com/darktrace-targets-1b-revenue-after-5-3b-thoma-bravo-acquisition).
- It joined OpenAI's Daybreak Cyber Partner Program (June 2026) — [Channel Insider](https://www.channelinsider.com/ai/openai-daybreak-cyber-program-security-tools/).

#### Sophos (UK; private, Thoma Bravo; owns Secureworks per the brief)
- Daybreak access extended to Sophos (Aug 11, 2026) — [Engadget](https://engadget.com/2234335/openai-daybreak-model-less-likely-to-refuse-higher-risk-tasks).
- Named a Leader in the 2026 IDC MarketScape for Worldwide Modern Endpoint Security for Enterprises (October 2026). Launched "AI Defense" for shadow AI (October 2026). Says it serves "more than 600,000 customers" [company claim, unconfirmed] — [Sophos press page](https://www.sophos.com/en-us/press).

#### WithSecure (Finland; private since 2025–2026)
- A CVC Growth Funds and Risto Siilasmaa consortium (Diana BidCo Oy) made a recommended €1.70-per-share cash tender. Completion trades took place Nov 10, 2025 (one source says Nov 17), and the holding reached 93.8% after the subsequent offer period. After squeeze-out proceedings, WithSecure was delisted from Nasdaq Helsinki per a release of Mar 26, 2026 [search extract] — [Inderes release](https://www.inderes.fi/en/releases/inside-information-a-consortium-formed-by-cvc-and-risto-siilasmaa-announces-a-recommended-cash-tender-offer-of-eur-170-per-share-through-diana-bidco-oy-to-the-shareholders-of-withsecure-corporation); [MarketScreener](https://www.marketscreener.com/news/cvc-capital-partners-plc-and-risto-siilasmaa-completed-the-acquisition-of-93-8-withsecure-oyj-from-ce7e5bdad18bf121); [MFN notice](https://mfn.se/a/withsecure/withsecure-corporation-notice-pursuant-to-the-finnish-securities-market-act-chapter-9-section-10-1).

#### F-Secure (Nasdaq Helsinki: FSECURE)
- January–September 2026 (published Oct 28, 2026): revenue €116.6M (+6.0%; +8.1% currency-neutral); adjusted EBITA €36.2M (31.0%, against 34.8%). Q3: revenue €40.5M (+12.2%); adjusted EBITA €13.6M (33.6%).
- 2026 outlook: currency-neutral growth 8–11% (previously 7–12%); adjusted EBITA €46–50M (previously €44–50M).
- Partner risk: "one of our largest Tier 1 partners does not intend to extend its agreement, which runs until the end of March 2027" [search extract of release] — [Placera (release)](https://www.placera.se/pressmeddelanden/f-secure-f-secure-interim-report-1-january-30-september-2026-accelerated-growth-driven-by-embedded-security-20261028); [Inderes](https://www.inderes.fi/releases/f-secure-interim-report-1-january-30-september-2026-accelerated-growth-driven-by-embedded-security).
- On Mar 10, 2026 F-Secure raised its full-year 2026 revenue outlook (title only seen) — [Placera](https://www.placera.se/pressmeddelanden/f-secure-inside-information-profit-warning-f-secure-raises-its-full-year-2026-revenue-outlook-profitability-outlook-remains-unchanged-20260310).

#### Bitdefender (Romania; private)
- 2025: revenue $480M (+11%); operating profit $57M; cash $362.6M with no bank debt; 2,145 employees (1,709 in Romania).
- Ownership and IPO: the Talpeș family holds about 55%. The article gives a "theoretical" value above $4B based on listed peers' multiples (journalist estimate). The IPO is deferred from an estimated June 2026 to end-December 2028.
- 2025 acquisitions: Mesh Security (Ireland) and Bitshield assets (Malaysia), $31M combined. About $202M of revenue was billed in the US — [Financiarul, 2026-07-06](https://financiarul.ro/companii/bitdefender-a-avut-venituri-de-480-de-milioane-de-dolari-in-2025-si-amana-l/).

#### Yubico (Nasdaq Stockholm: YUBICO)
- Q3 2026 (published Nov 5, 2026): net sales SEK 708.0M (+29.3%; organic +28.3%); EBIT SEK 179.3M (25.3% margin, against 14.5%); bookings SEK 949.0M (+88.2%); diluted EPS SEK 1.69.
- Nine months: net sales SEK 1,731.2M (+3.7%; organic +9.0%; currency −5.3pp); EBIT SEK 272.7M (15.7%).
- New 2027–2031 targets: 15–20% average annual sales growth, with EBIT margin moving toward 20% by 2031. Capital Markets Day Nov 19, 2026 [search extract of release] — [MFN](https://mfn.se/a/yubico/interim-report-july-september-2026); [Inderes](https://www.inderes.se/en/releases/interim-report-july-september-2026-2).

#### secunet (Xetra: YSN; majority owner believed to be Giesecke+Devrient, not verified this session; StockAnalysis float data fit a ~75% strategic holding)
- Nine months to Sept 30, 2026 (statement signed Nov 11, published Nov 12, 2026):
  - Revenue: €339.8M (+19.3%); Q3 €135.2M (+19.5%).
  - Orders: order intake €392.5M (+25.0%), but Q3 order intake €105.1M (−31.2%); backlog €330.2M (+18.4% vs Dec 31, 2025); book-to-bill 1.2x.
  - Profit: EBITDA €38.8M (−1.0%); EBIT €22.9M (−7.8%), Q3 EBIT €14.3M (−19.2%); gross margin 20.6% (against 23.0%).
  - Cash: operating cash flow −€49.0M, attributed to an inventory build ahead of expected call-off orders; cash €5.6M (against €35.8M); 1,233 employees.
  - Segments and regions: Public Sector €322.2M (+29.2%; 94.8% of revenue), led by Defence & Space and by Homeland Security's border-control systems "across Europe". Business Sector €17.7M (−50.2%, on weak healthcare and industrial demand). Domestic sales 89.2% of revenue.
  - Guidance unchanged: revenue €460–500M (at the upper end), EBIT €53–58M, EBITDA €76–84M.
  - Strategy: 2026 and 2027 are "years of transformation" with restructuring costs. New segments from 2027 are "Sovereign Solutions" and "Defence & Security" — [secunet Q3 statement (PDF, German)](https://www.secunet.com/fileadmin/user_upload/02_Downloads/IR/Finanzpublikationen/2026/Q3/26_11_12_Q3_Bericht_de_v3.pdf).
- H1 2026: revenue €204.7M (+19.2%), EBIT €8.7M [search extract] — [goldesel](https://goldesel.de/aktien/news/secunet-steigert-h1-umsatz-um-19-auf-2047-mio-und-peilt-2026-am-oberen-ende-der-spanne). Preliminary FY2025 figures were published on Jan 29, 2026 [search extract] — [extraETF/dpa-AFX](https://extraetf.com/de/news/dpa-afx/roundup-secunet-steigert-umsatz-und-operativen-gewinn--1769684609-05573-1769684605806).

#### Wallix (Euronext Growth: ALLIX)
- H1 2026 (AMF filing July 16, 2026): revenue €20.6M (+14.2%); monthly recurring revenue €2.8M (+19.4%); ARR €33.1M at end-June; recurring revenue 81% of revenue (against 74%); operating loss −€1.2M (against −€2.96M); positive free cash flow; 2026 targets confirmed — [AMF filing](https://echanges.dila.gouv.fr/OPENDATA/AMF/ACT/2026/07/FCACT080594_20260716.pdf); [ABC Bourse](https://www.abcbourse.com/marches/wallix-ameliore-nettement-ses-resultats-au-premier-semestre-2026-et-affiche-un-f_703931) [search extract].

#### Thales (Euronext Paris: HO; owns Imperva)
- Group market data only, in section 6. Thales's investor page returned no content when fetched, so cyber-segment results were not retrieved.

### Inferences
**Darktrace**
- Quality tests:
  - (a) Position: autonomous detection and response at machine speed, a strong position in principle. But frontier-model security agents and hyperscaler SOCs encroach, and it owns no judge for fixes.
  - (b) Lead: none confirmed this session.
  - (c) Revenue model: subscription.
  - (d) Financial strength: PE-levered (leverage unknown).
  - (e) Resilience: slowing growth and CEO churn weaken it in the pause scenario.
- Path forward: (2), and (4) via Daybreak. Suggested verdict: partly coherent.
- Entry point: about 6.8x ARR at the 2024 take-private price. Private, so exposure is only via Thoma Bravo funds. Suggested label: cannot assess.

**Sophos**
- (a) Position: MDR at scale, part labour, increasingly automated. (b) Lead: IDC Leader (October 2026) is outside evidence.
- Path forward: (1) and (2), with (4) via Daybreak. Suggested verdict: partly coherent.
- Entry point: cannot assess (private).

**WithSecure**
- No post-delisting data. Suggested verdict: cannot assess. Entry point: no public access since March 2026.

**F-Secure**
- Quality tests:
  - (a) Position: consumer security embedded through operators (B2B2C), with no automated find-and-fix role.
  - (b) Lead: none.
  - (c) Revenue model: recurring via partners, but concentrated (the partner loss).
  - (d) Financial strength: adjusted EBITA margin about 31–34%; net debt €138M, about 3.5x EBITDA (my calculation from StockAnalysis figures).
  - (e) Resilience: largely uncorrelated with AI capex; partner concentration is the main risk.
- Path forward: suggested verdict partly coherent.
- Entry point: see section 6.

**Bitdefender**
- Quality tests:
  - (a) Position: endpoint/XDR and consumer, with no gated-model access found.
  - (c) Revenue model: subscription.
  - (d) Financial strength: strong (cash $363M, no debt, about 12% operating margin).
  - (e) Resilience: EU-vendor status may help with sovereignty-minded buyers (inference).
- Path forward: suggested verdict partly coherent.
- Entry point: about 8.3x revenue on the journalist's theoretical value. IPO end-2028. Suggested label: cannot assess.

**Yubico**
- Quality tests:
  - (a) Position: owns a constraint AI cannot remove, hardware-bound phishing-resistant authentication. That makes it a beneficiary of AI-driven phishing rather than a victim, though it is not automated security.
  - (b) Lead: bookings +88% is outside-visible demand but not a ranking.
  - (c) Revenue model: mainly hardware sales (one-off) with some subscription (split not retrieved).
  - (d) Financial strength: net cash SEK 1.21B; free cash flow SEK 393M; gross margin about 79%.
  - (e) Resilience: largely uncorrelated with AI capex.
- Path forward: (5), since regulation favours phishing-resistant MFA (inference). Suggested verdict: coherent as a niche.
- Entry point: see section 6.

**secunet**
- Quality tests:
  - (a) Position: a sovereign, regulator-recognised supplier to the German state (95% public sector), a "constraint" AI cannot remove (procurement sovereignty) rather than a judge. Gross margin of about 21% indicates hardware and integration content.
  - (b) Lead: concentration in German government is the moat and also the risk.
  - (c) Revenue model: project, hardware and services heavy (book-to-bill and "call-off" language).
  - (d) Financial strength: 9M operating cash flow −€49M, cash down to €5.6M, net debt €23M.
  - (e) Resilience: defence and sovereignty spending makes it countercyclical to AI capex; exposed to German budget timing.
- Path forward: transitions (5) and EU sovereignty procurement. Not (2) or (4): no gated-model link found. Suggested verdict: partly coherent, with transformation costs in 2026–27 and a need for Q4 2026 EBIT of €30–35M (my calculation: €53–58M guidance minus €22.9M nine-month EBIT) to meet guidance.
- Entry point: see section 6.

**Wallix**
- Quality tests: (a) privileged access management, with a sovereignty pitch (not verified). (c) Revenue model: recurring 81%. (d) Financial strength: about breakeven.
- Suggested verdict: partly coherent.

**Thales**
- Cyber is a minority of a €22.8B defence group. Suggested verdict: cannot assess for cyber.

### Gaps
- ESET (Slovakia), Sekoia (France), Detectify (Sweden), Eviden/Atos cyber and Airbus Protect: no data retrieved in this session after the search budget ran out. I could not verify ownership changes, funding or AI programmes.
- Thales's Digital Identity & Security and cyber-products (Imperva) figures for 2026 were not retrieved.
- Sophos's revenue and ARR, and the status of the Secureworks integration, were not retrieved.
- Darktrace's 2026 revenue and ARR were not found; the only data is the pre-takeover ARR plus press summaries.
- G+D's stake in secunet was not re-verified. StockAnalysis shows a float of 1.61M of 6.47M shares, consistent with about 75% held by a strategic owner.

## 5. Policy: India, Europe, Israel

### Takeaway
- EU: the Cyber Resilience Act's first hard obligation, reporting actively exploited vulnerabilities, has applied since Sept 11, 2026, and its main obligations follow on Dec 11, 2027. In January 2026 the Commission proposed both a revised Cybersecurity Act (a trusted ICT supply-chain framework against risky third-country suppliers, a common EU vulnerability-management service run by ENISA, and faster certification schemes) and NIS2 simplifications.
- India: the DPDP Rules (notified Nov 13, 2025) phase in over 18 months to about May 13, 2027. They add a 72-hour breach report to CERT-In's six-hour incident clock.
- Israel: on the evidence found, civilian cyber enforcement is weak. Export-control facts were not verified this session.

### Cited Findings
- **EU Cyber Resilience Act:** entered into force Dec 10, 2024. "As of 11 September 2026, manufacturers are required to report actively exploited vulnerabilities". Main obligations apply from Dec 11, 2027. The Commission published practical guidance on July 27, 2026. Page updated Sept 7, 2026 — [European Commission, CRA](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act).
- **NIS2:** the transposition deadline was Oct 17, 2024. On Jan 20, 2026 the Commission proposed targeted NIS2 amendments to "ease compliance for 28,700 companies, including 6,200 micro and small-sized enterprises" — [European Commission, NIS2](https://digital-strategy.ec.europa.eu/en/policies/nis2-directive).
- **Cybersecurity Act revision (proposed January 2026):**
  - ENISA tasks: early threat alerts, ransomware support with Europol and CSIRTs, a "common Union vulnerability management service", and the single entry point for incident reporting proposed in the Digital Omnibus.
  - Supply chain: a "harmonised, proportionate, risk-based trusted supply chain framework" to reduce risks from third-country suppliers.
  - Certification: schemes to be developed "within 12 months by default". Page updated June 22, 2026 — [European Commission, Cybersecurity Act](https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-act).
- **Certification schemes:** EUCC has applied since Feb 27, 2025. Candidate schemes for EUCS (cloud), EU5G, managed security services and EUDI wallets were requested from ENISA, and none is adopted per the page. The managed-security-services amendment to the Act was adopted Jan 15, 2025, enabling schemes for incident response, penetration testing, audits and consultancy. Page updated Sept 9, 2026 — [European Commission, certification framework](https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-certification-framework); [European Commission, Cybersecurity Act](https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-act).
- **Sovereignty-driven procurement, datapoints:**
  - The CrowdStrike–XM Cyber deal includes a partnership around Schwarz Digits' STACKIT sovereign cloud — [CTech, 2026-10-13](https://www.calcalistech.com/ctechnews/article/sje00evoizx).
  - secunet's growth comes from Defence & Space and from Homeland Security border-control systems "across Europe", and it will report a "Sovereign Solutions" segment from 2027 — [secunet Q3 statement](https://www.secunet.com/fileadmin/user_upload/02_Downloads/IR/Finanzpublikationen/2026/Q3/26_11_12_Q3_Bericht_de_v3.pdf).
  - Anthropic's Glasswing expansion reportedly includes European nations, and ENISA's terms are under negotiation [search extract] — [Capacity](https://capacityglobal.com/news/anthropic-takes-project-glasswing-to-15-countries/).
- **India, DPDP Rules 2025:** notified by MeitY on Nov 13, 2025 (press reports Nov 14). Phases are immediate, 12 months and 18 months. The 18-month phase (about May 13, 2027; one source says May 12) brings notice, security safeguards, breach reporting, retention, children's data, Significant Data Fiduciary obligations and international transfers. The SPDI Rules 2011 remain in force for 18 months [search extract] — [AZB & Partners](https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/); [Deccan Herald](https://www.deccanherald.com/amp/story/india%2Fcentre-notifies-dpdp-rules-implementation-planned-in-phases-spread-over-12-18-months-3798465); [YourStory](https://yourstory.com/2025/11/digital-personal-data-protection-dpdp-rules-2025-rollout-over-18-months).
- **India, two reporting clocks:** a DPDP breach needs an intimation "without delay" plus a detailed report within 72 hours, while CERT-In directions under the IT Act 2000 require reporting cyber incidents, including breaches, within six hours. Commentators describe this as a "dual clock" [search extract] — [Mondaq](https://www.mondaq.com/india/data-protection/1706890/a-closer-look-at-the-dpdp-rules-2025); [Legal500 (Saga Legal)](https://www.legal500.com/firms/237811-saga-legal/c-india/news-and-developments/the-privacy-timer-starts-now-analysing-the-dpdp-rules-and-its-18-month-countdown).
- **Israel, enforcement:** Sygnia's CEO (June 21, 2026) says Israel lacks EU-style enforcement for civilian companies, and that "the government, regulators and the Knesset" must set standards — [CTech](https://www.calcalistech.com/ctechnews/article/syejhghzgx).

### Inferences
- **CRA reporting (live since Sept 11, 2026) and the Dec 2027 main obligations create a dated, EU-wide demand pull for device makers' vulnerability handling.** This favours firms selling SBOM and firmware analysis and vulnerability management to manufacturers (ONEKEY and Cybellum, covered elsewhere) more than the firms in this file.
- **The CSA revision's "common Union vulnerability management service" under ENISA could become an EU-run "judge-adjacent" clearing point for vulnerabilities.** With ENISA negotiating Glasswing terms, the EU state, not a European vendor, may be the main European holder of gated-model access.
- **The trusted-supply-chain framework and the sovereign-cloud language favour EU-domiciled vendors in public procurement** (secunet, Thales, Wallix, Bitdefender, and Schwarz/STACKIT as distributor). They could disadvantage some non-EU vendors. Israeli vendors' EU access is not obviously restricted, and XM Cyber's technology now reaches the EU through STACKIT.
- **India's two clocks and the May 2027 DPDP deadline are a domestic tailwind** for Quick Heal's DLP and privacy products and for IT-services compliance work. The international-transfer rules arrive in the 18-month phase. This is localisation risk for foreign SaaS security vendors serving Indian data fiduciaries (inference; the details of transfer restrictions were not retrieved).

### Gaps
- The NIS2 transposition count and infringement status as of November 2026 are not known; the Commission's transposition page returned "not found". Germany's NIS2 implementation date was not verified.
- The status of the CSA revision in Parliament and Council, and the CRA harmonised standards and implementing acts, were not retrieved.
- India's Telecom Cyber Security Rules (2024, under the Telecommunications Act 2023) and any 2025 amendments were not retrieved. Neither were the CERT-In 2022 directions' log-retention and in-India log storage terms; the six-hour rule is cited only via commentary.
- Israel: the INCD's mandate and head, the cyber bill's status, and the defense-export regime for offensive cyber tools are unverified in this session.

## 6. Listed companies: latest results, valuation versus own history and peers, foreign-investor access

### Takeaway
On Nov 12, 2026 multiples spread widely:
- Yubico: about 48x EV/EBITDA and 44x forward P/E, after a large re-rating.
- secunet: 20.5x EV/EBITDA and 33x forward P/E, after a 14% one-day drop on Q3.
- Thales: 13.6x EV/EBITDA and 19x forward P/E.
- Subex: 16.8x EV/EBITDA.
- F-Secure: 9.6x EV/EBITDA and 9.7x forward P/E, near its 52-week low.
- Wallix: 3.0x EV/Sales, about 4.5x EV/ARR.
- Quick Heal: 2.5x EV/Sales, loss-making, net cash about 28% of market cap.

Five-year ranges and global peer multiples were not retrieved, so comparisons are to 52-week ranges and within this set only. Indian shares need an FPI or NRI route; that route was not verified this session.

### Cited Findings
Market data, Nov 12, 2026 (delayed; StockAnalysis/S&P Global):

| Company (ticker) | Price | Mkt cap | EV | EV/Sales | EV/EBITDA | EV/FCF | P/E TTM | Fwd P/E | Net cash (debt) | 52-wk range / change | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Quick Heal (NSE: QUICKHEAL) | ₹150.47 | ₹8.17B | ₹5.85B | 2.54 | n/a (loss) | 12.70 | n/a | n/a | ₹2.32B | ₹125–337 / −52.0% | [StockAnalysis](https://stockanalysis.com/quote/nse/QUICKHEAL/statistics/) |
| Subex (NSE: SUBEXLTD) | ₹16.77 | ₹9.31B | ₹7.98B | 2.63 | 16.80 | n/a | 22.61 | n/a | ₹1.33B | n/a / +23.7% | [StockAnalysis](https://stockanalysis.com/quote/nse/SUBEXLTD/statistics/) |
| secunet (XETRA: YSN) | €200.50 (−14.1% on day) | €1.30B | €1.32B | 3.12 | 20.53 | n/a (FCF −€1.2M) | 37.91 | 32.72 | (€22.8M) | €152.80–268.00 / +19.2% | [StockAnalysis](https://stockanalysis.com/quote/etr/YSN/statistics/) |
| Yubico (STO: YUBICO) | SEK 179.50 | SEK 15.51B | SEK 14.30B | 6.27 | 47.73 | 36.42 | 66.48 | 43.90 | SEK 1.21B | SEK 29.55–180.00 / +88.3% | [StockAnalysis](https://stockanalysis.com/quote/sto/YUBICO/statistics/) |
| F-Secure (HEL: FSECURE) | €1.384 | €241.9M | €379.6M | 2.50 | 9.55 | 18.44 | 16.72 | 9.74 | (€137.7M) | €1.340–2.335 / −18.3% | [StockAnalysis](https://stockanalysis.com/quote/hel/FSECURE/statistics/) |
| Wallix (EPA: ALLIX) | €23.15 | €155.1M | €150.6M | 3.00 | n/a | n/a | 118.43 | 36.13 | €4.5M | n/a / −4.8% | [StockAnalysis](https://stockanalysis.com/quote/epa/ALLIX/statistics/) |
| Thales (EPA: HO) | €229.50 | €47.15B | €47.68B | 2.10 | 13.63 | 11.96 | 31.61 | 19.18 | (€519M) | n/a / −4.6% | [StockAnalysis](https://stockanalysis.com/quote/epa/HO/statistics/) |

- Other ratios on the same pages:
  - secunet: ROIC 24.6%; EBITDA margin 13.8%; trailing revenue €491.8M.
  - Yubico: gross margin 78.7%; ROIC 26.8%; free cash flow SEK 392.7M.
  - F-Secure: EBITDA margin 25.2%; ROIC 10.6%; free cash flow €20.6M.
  - Wallix: trailing revenue €49.45M; free cash flow €2.88M.
  - Thales: trailing revenue €22.82B; free cash flow €4.00B; ROIC 22.8%.
  - Sources: same StockAnalysis links as the table.
- Recent results and events with dates: Quick Heal Q2 FY27 (Oct 27–28, 2026); F-Secure Q3 (Oct 28, 2026); Yubico Q3 (Nov 5, 2026; Capital Markets Day Nov 19, 2026); secunet 9M (Nov 12, 2026; guidance confirmed); Wallix H1 (July 16, 2026) — sources as cited in sections 3–4.
- WithSecure is no longer listed (delisted from Nasdaq Helsinki, March 2026) — [MFN](https://mfn.se/a/withsecure/withsecure-corporation-notice-pursuant-to-the-finnish-securities-market-act-chapter-9-section-10-1).
- CTech quotes PANW at $326.36 (Nov 10, 2026) and CRWD at $263 (mid-October 2026). These are prices only, not multiples — [CTech](https://www.calcalistech.com/ctechnews/article/hy11rj2wrgx); [CTech](https://www.calcalistech.com/ctechnews/article/sje00evoizx).

### Inferences
**secunet**
- What the price implies: EV €1.32B against the €55.5M EBIT guidance midpoint gives about 24x EV/EBIT. That prices continued mid-to-high-teens growth and post-transformation margin recovery.
- The 14% fall on Nov 12 coincides with Q3 order intake down 31%, Q3 EBIT down 19% and negative operating cash flow; the market reaction is my inference, as no commentary was read.
- Near-term events: Q4 delivery (Q4 EBIT of about €30–35M needed), preliminary FY2026 results (about late January 2027 by last year's pattern), and the 2027 resegmentation.
- Would improve the entry: evidence of cash conversion and of order intake recovering.
- Suggested label: fair.

**Yubico**
- What the price implies: about 48x EV/EBITDA and 36x EV/FCF require sustained 15–20% growth (its new target) plus margin expansion. Q3 bookings +88% support the near term.
- Data conflict: the 52-week low of SEK 29.55 against a +88% 52-week change suggests either a mid-year collapse and recovery or a data error; this needs checking.
- Near-term event: Capital Markets Day Nov 19, 2026.
- Suggested label: stretched.

**F-Secure**
- What the price implies: the multiples price in the Tier 1 partner loss (from end-March 2027) and leverage of about 3.5x EBITDA.
- Would improve the entry: clarity on the size of the lost partner's revenue.
- Suggested label: fair. Cheap on multiples, but with a known revenue hole.

**Wallix**
- What the price implies: EV about 4.5x ARR (my calculation, €150.6M / €33.1M) implies modest expectations against management's "hyper-growth" target.
- Data conflict: trailing revenue of €49.45M conflicts with H1 revenue of €20.6M, so the data needs checking.
- Suggested label: fair.

**Quick Heal**
- The price implies continued decline; net cash plus free cash flow limits downside, but the operating trend is negative. Suggested label: fair, with value-trap risk.

**Subex**
- Suggested label: cannot assess (security share unknown).

**Thales**
- Fair as a defence group (about 19x forward P/E). Cyber exposure cannot be separated. Suggested label: cannot assess for cyber.

**Peers**
- Within this set, Yubico trades about 5x F-Secure's EV/EBITDA. secunet's forward P/E sits about 1.7x Thales's.
- No global cyber-peer multiples (CRWD, PANW, FTNT, OKTA, CHKP) were retrieved this session for comparison.

### Gaps
- No five-year valuation ranges were retrieved for any listed name, and no global peer multiples. The "versus own ~5-year range" test cannot be answered from this session's data.
- Foreign-investor access to India, not verified here. Standard routes, as background to confirm: registration as a Foreign Portfolio Investor with SEBI through a Designated Depository Participant and custodian; NRI investment via a Portfolio Investment Scheme bank account; indirect exposure through India-focused funds or ETFs; or US-listed ADRs where they exist (Infosys and Wipro have NYSE ADRs; Quick Heal and Subex do not, to my knowledge). Promoter control of 72.95% at Quick Heal limits free float.
- European listings (Xetra, Nasdaq Stockholm and Helsinki, Euronext Paris and Growth) are generally open to non-residents via international brokers. Specific restrictions were not checked.
- Quick Heal's and Subex's figures were not reconciled to NSE/BSE filings or Screener.in.

## 7. Closing summary: per-company scorecard, exclusions, coverage limits and sources

### Takeaway
The scorecard below compresses sections 2–6. Facts are cited in those sections; the verdicts and labels are my suggested judgments. No company covered here clears the bar for a global top 8–15 in automated find-and-fix. Cato is the closest, and Cyera, Island, Upwind, Darktrace and Sophos form a watch-list.

### Cited Findings
#### Per-company scorecard (tests a–e; path-forward verdict; entry snapshot and suggested label)
Key facts behind each line are cited in sections 1–6. Scenario shorthand for test (e): S = steady growth (~55%), P = financing-led pause around 2028 (~25%), F = faster acceleration (~20%).

**Cato Networks (Israel, private)**
- a: network-level shielding point, no judge.
- b: Daybreak access; no ranking retrieved.
- c: subscription ARR $415M (July 2026).
- d: about $1.1B raised; margins undisclosed.
- e: S+ / P− (IPO window) / F+ if access deepens; Israel exposure.
- Path forward: partly coherent.
- Entry: more than $4.8B (June 2025) ≈ 11.6x ARR; no IPO date. Label: cannot assess.

**Cyera (Israel, private)**
- a: data-control measurement for AI agents.
- b: none confirmed.
- c: subscription, ARR undisclosed.
- d: $1.4B raised in 2026.
- e: S+ / P−− / F+.
- Path forward: partly coherent.
- Entry: valuation above $12B; ARR unknown. Label: cannot assess.

**Island (Israel, private)**
- a: browser/agent control layer, which big platforms can copy.
- b: revenue is a company claim.
- c: subscription.
- d: $400M raised (September 2026).
- e: S+ / P−− / F+.
- Path forward: partly coherent.
- Entry: $6.4B ≈ 32x claimed revenue. Label: stretched.

**Upwind (Israel, private)**
- a: runtime exploitability evidence.
- b: none.
- c: subscription; ARR more than $50M.
- d: $400M raised (October 2026).
- e: S+ / P−− / F+.
- Path forward: partly coherent.
- Entry: $3.8B ≈ 76x ARR. Label: stretched.

**Axonius (Israel, private)**
- a: asset inventory, at risk from AI.
- b: more than 100 Fortune 1000 customers.
- c: subscription; ARR more than $200M, +35%.
- d: repeated restructurings.
- e: S0 / P− / F−.
- Path forward: partly coherent.
- Entry: about 10–13x ARR (2024 mark / Cisco talk). Label: fair, no access.

**Torq (Israel, private)**
- a: autonomous SOC (replaces triage).
- b: none.
- c: subscription.
- d: $140M raised (January 2026).
- e: S+ / P− / F±.
- Path forward: coherent in direction.
- Entry: $1.2B. Label: cannot assess.

**Zafran (Israel, private)**
- a: prioritisation gap that AI is closing.
- b: none.
- c: subscription.
- d: founder departure, discounted takeover talk.
- e: weak in all scenarios.
- Path forward: not coherent independently.
- Entry: label cannot assess.

**XM Cyber (Israel/Germany, Schwarz-owned)**
- a: technology sold to CrowdStrike.
- b: n/a.
- c: licence-servicing.
- d: shrinking (250 of 300 Israeli staff cut).
- e: n/a.
- Path forward: not coherent.
- Entry: n/a (exposure via CRWD).

**Noma Security (Israel, private)**
- a: AI-agent security.
- b–d: no data.
- e: P−−.
- Path forward: cannot assess.
- Entry: label cannot assess.

**Sygnia (Israel, Temasek-owned)**
- a: billable incident-response hours (weakest position).
- b: reputation only.
- c: labour.
- d: unknown.
- e: exposed to transition 1.
- Path forward: cannot assess.
- Entry: n/a.

**Quick Heal (India, NSE)**
- a: weak (consumer antivirus decline; no judge).
- b: none.
- c: licence/subscription; consumer −40% year on year.
- d: net cash ₹232 crore; operating loss trailing twelve months.
- e: low AI-cycle correlation; substitution risk.
- Path forward: partly coherent at best.
- Entry: EV/Sales 2.5; −52% over 52 weeks. Label: fair (value-trap risk).

**Subex/Sectrio (India, NSE)**
- a: OT/IoT shielding, segment small or unknown.
- b: none.
- c: mixed.
- d: net cash ₹133 crore; FCF positive.
- e: n/a.
- Path forward: cannot assess.
- Entry: EV/EBITDA 16.8. Label: cannot assess.

**CloudSEK (India, private)**
- a: AI threat intelligence.
- b: none.
- c: subscription.
- d: about $39M raised.
- e: P−.
- Path forward: cannot assess.
- Entry: about $200M valuation. Label: cannot assess.

**Securonix (US/India, Vista-backed)**
- a: SIEM under AI-SOC pressure.
- b: Gartner MQ Leader (2025).
- c: subscription.
- d: PE-backed.
- e: S0 / P− / F−.
- Path forward: partly coherent.
- Entry: label cannot assess.

**Indian IT services (TCS, Infosys, Wipro, HCLTech)**
- a: labour hours and seats.
- b: no gated-cyber membership found.
- c: labour.
- d: strong balance sheets (not retrieved).
- e: F−− (AI substitution).
- Path forward: partly coherent / not coherent for cyber hours.
- Entry: not assessed.

**Darktrace (UK, Thoma Bravo)**
- a: autonomous detection and response.
- b: Daybreak partner; growth reportedly slowing.
- c: subscription.
- d: PE leverage unknown.
- e: S0 / P− / F±.
- Path forward: partly coherent.
- Entry: 2024 take-private ≈ 6.8x ARR. Label: cannot assess.

**Sophos (UK, Thoma Bravo)**
- a: MDR plus endpoint.
- b: IDC Leader (October 2026); Daybreak access.
- c: subscription plus services.
- d: unknown.
- e: S0 / P− / F±.
- Path forward: partly coherent.
- Entry: label cannot assess.

**WithSecure (Finland, CVC/Siilasmaa)**
- a–e: no post-deal data.
- Path forward: cannot assess.
- Entry: delisted March 2026.

**F-Secure (Finland, listed)**
- a: embedded consumer security, no judge.
- b: none.
- c: recurring via partners (concentrated).
- d: adjusted EBITA margin about 31%; net debt about 3.5x EBITDA.
- e: low AI correlation; partner-loss risk from March 2027.
- Path forward: partly coherent.
- Entry: EV/EBITDA 9.6; forward P/E 9.7. Label: fair.

**Bitdefender (Romania, private)**
- a: endpoint/XDR and consumer.
- b: none confirmed.
- c: subscription.
- d: cash $363M, no debt.
- e: steady.
- Path forward: partly coherent.
- Entry: about 8.3x revenue (theoretical); IPO end-2028. Label: cannot assess.

**Yubico (Sweden, listed)**
- a: owns a hardware constraint (phishing-resistant authentication).
- b: bookings +88% (Q3 2026).
- c: mostly hardware.
- d: net cash SEK 1.2B; FCF positive.
- e: low AI-cycle correlation.
- Path forward: coherent (niche).
- Entry: EV/EBITDA 48; forward P/E 44. Label: stretched.

**secunet (Germany, listed)**
- a: sovereign state supplier (constraint, not judge).
- b: 95% public sector.
- c: projects and hardware.
- d: 9M operating cash flow −€49M; ROIC 24.6%.
- e: countercyclical (defence).
- Path forward: partly coherent.
- Entry: EV/EBITDA 20.5; forward P/E 32.7; −14% on Nov 12. Label: fair.

**Wallix (France, listed)**
- a: privileged access management.
- b: none.
- c: 81% recurring; ARR €33.1M.
- d: around breakeven; small net cash.
- e: steady.
- Path forward: partly coherent.
- Entry: EV/Sales 3.0; EV/ARR about 4.5. Label: fair.

**Thales (France, listed)**
- a: sovereign crypto and Imperva (not separated).
- b: n/a.
- c: mixed.
- d: FCF €4.0B; net debt €0.5B.
- e: defence-driven.
- Path forward: cannot assess for cyber.
- Entry: EV/EBITDA 13.6; forward P/E 19.2. Label: cannot assess for cyber.

#### Companies considered and excluded (with reasons)
- XM Cyber: its technology now sits inside CrowdStrike, which is covered elsewhere — [CTech](https://www.calcalistech.com/ctechnews/article/sje00evoizx).
- WithSecure: delisted and private; no data — [MFN](https://mfn.se/a/withsecure/withsecure-corporation-notice-pursuant-to-the-finnish-securities-market-act-chapter-9-section-10-1).
- Zafran: weakened, with possible absorption by Cisco — [CTech](https://www.calcalistech.com/ctechnews/article/a6lm0ykz3).
- Sequretek, Astra Security, Appknox, Cyble, K7 Computing (India); ESET, Sekoia, Detectify, Eviden/Atos cyber, Airbus Protect (Europe); Tata Communications (India): considered but not assessed because no data could be retrieved after the search budget ran out. This is not a judgment on their merits.
- Kaspersky and Positive Technologies (Russia): outside the investable universe as sanctioned entities, per the brief. Their sanctions status (US prohibition on Kaspersky products; Positive Technologies' US sanctions listing) was not re-verified this session.
- Companies covered by other researchers (listed in the opening note): excluded from scoring here by design.

### Inferences
- Across the three regions, the companies with plausible "position" strength are those that own a constraint (Yubico's hardware, secunet's sovereign procurement) or a fast enforcement point (Cato). The capital-rich Israeli AI-agent security startups own neither a judge nor a constraint yet, and their entry points look stretched in a 2028 pause scenario.
- The labour-heavy models (Indian IT cyber services, Sygnia's incident response, parts of Sophos's MDR) are the most exposed to transitions (1) and (2), especially as OpenAI and Anthropic build their own services arms and gate their best cyber models to selected partners.

### Gaps
#### Coverage limits by region
- **Israel:** good coverage of private-company funding and valuations via CTech tag pages; no TASE/MAYA filings. No INCD, export-control or war-impact data. No analyst rankings. ARR is missing for Cyera, Torq and Noma.
- **India:** Quick Heal from aggregators and a concall summary only, with NSE filings unopened. No data on Sequretek, Astra, Appknox, Cyble, K7, Tata Communications or the cyber practices of the IT majors. Telecom security rules and the FPI route were not verified. Screener.in was not used.
- **Europe:** secunet from its primary PDF; F-Secure, Yubico and Wallix from release mirrors. Darktrace from search extracts only. Nothing on Sophos's financials, ESET, Sekoia, Detectify, Eviden/Atos, Airbus Protect or Thales's cyber segment. NIS2 transposition status is missing.
- **All regions:** no five-year valuation ranges; no global peer multiples. Full partner lists for the gated programmes were unavailable (OpenAI's page returned 403; Anthropic and Google publish no full lists). Firecrawl's Alexandria finance data could not be used (credits exhausted), and the shared web-search budget ran out mid-task.

#### Dated source list
- Anthropic, "Expanding Project Glasswing" (2026-06-02) — https://www.anthropic.com/news/expanding-project-glasswing
- Anthropic, Claude Fable/Mythos 5.2 announcement (2026-11-09) [sibling notes] — https://www.anthropic.com/claude-fable-and-mythos-5-2
- ITPro, Project Glasswing launch (April 2026) [search extract] — https://www.itpro.com/technology/artificial-intelligence/project-glasswing-anthropic-announces-big-tech-consortium-to-test-claude-mythos-ai-model-that-could-reshape-cybersecurity
- Capacity / BankInfoSecurity, Glasswing expansion coverage (June 2026) [search extract] — https://capacityglobal.com/news/anthropic-takes-project-glasswing-to-15-countries/ ; https://www.bankinfosecurity.com/anthropic-expands-mythos-to-global-critical-infrastructure-a-31836
- Channel Insider, OpenAI Daybreak partners (2026-06-23) — https://www.channelinsider.com/ai/openai-daybreak-cyber-program-security-tools/
- Cato release via PR Newswire / Ynet, Daybreak (2026-06-22) [search extract] — https://www.prnewswire.com/il/news-releases/cato-advances-enterprise-defense-joining-the-openai-daybreak-cyber-partner-program-302805920.html ; https://www.ynetnews.com/tech-and-digital/article/skhk2tpmgl
- Engadget, Daybreak tiers and expanded partners (2026-08-11) — https://engadget.com/2234335/openai-daybreak-model-less-likely-to-refuse-higher-risk-tasks
- OpenAI, "Putting frontier cyber models in more trusted hands" (August 2026) [search extract] — https://openai.com/index/putting-frontier-cyber-models-in-more-trusted-hands ; partner page (403) — https://openai.com/daybreak/partners-new/
- SiliconANGLE, GPT-6 Cyber (2026-11-05) [sibling notes] — https://siliconangle.com/2026/11/05/openai-launches-gpt-6-cyber-a-gpt-6-astra-model-built-to-keep-vulnerability-research-in-scope/
- The Hacker News, Google/Anthropic/OpenAI cyber releases (2026-09-02) — https://thehackernews.com/2026/09/google-anthropic-and-openai-unveil.html
- Google DeepMind, Fairwind Program page (read 2026-11-12) — https://deepmind.google/fairwind-program/
- Forbes (2026-10-30) and technology.org (2026-11-11) on Gemini 4 Carbon [sibling notes] — https://www.forbes.com/sites/janakirammsv/2026/10/30/google-limits-gemini-4-carbon-to-vetted-cyber-defenders/ ; https://www.technology.org/2026/11/11/gemini-4-carbon-available-developers-ai-ultra-pricing/
- CTech/Calcalist tag pages (read 2026-11-12): Cato, Upwind, Zafran, Torq, Axonius, Island, XM Cyber, Noma, Sygnia, cybersecurity — https://www.calcalistech.com/tags/Cato_Networks ; https://www.calcalistech.com/tags/Upwind ; https://www.calcalistech.com/tags/Zafran ; https://www.calcalistech.com/tags/Torq ; https://www.calcalistech.com/tags/Axonius ; https://www.calcalistech.com/tags/Island ; https://www.calcalistech.com/tags/XM_Cyber ; https://www.calcalistech.com/tags/Noma_Security ; https://www.calcalistech.com/tags/Sygnia
- CTech articles:
  - Cato ARR (2026-07-27) — https://www.calcalistech.com/ctechnews/article/b1bqq6nrfg
  - Cato hiring (2026-03-31) — https://www.calcalistech.com/ctechnews/article/syecewyszl
  - Q3 2026 Israeli cyber funding (2026-10-09) — https://www.calcalistech.com/ctechnews/article/8e72dv4yf
  - Upwind round (2026-10-28) — https://www.calcalistech.com/ctechnews/article/rohkgwlwu
  - Axonius cuts (2026-11-09) — https://www.calcalistech.com/ctechnews/article/9upwifo24
  - CrowdStrike–XM Cyber price (2026-10-13) — https://www.calcalistech.com/ctechnews/article/sje00evoizx
  - Palo Alto–CyberArk value (2026-11-11) — https://www.calcalistech.com/ctechnews/article/hy11rj2wrgx
  - Black Hat roundup (2026-08-04) — https://www.calcalistech.com/ctechnews/article/rygsooy8fx
  - Sygnia CEO on enforcement (2026-06-21) — https://www.calcalistech.com/ctechnews/article/syejhghzgx
- Globes, Cato ARR (July 2026) — https://en.globes.co.il/en/article-1001550594 ; Cyera $12B (June 2026) — https://en.globes.co.il/en/article-1001545507
- Cyera press releases (January 2026; June 2026) — https://www.cyera.com/press-releases/cyera-raises-400m-to-meet-rapidly-growing-demand-for-ai-security-among-enterprises ; https://www.cyera.com/press-releases/cyera-raises-600-million-at-12-billion-valuation-to-continue-building-the-trust-layer-for-the-ai-era
- Ynet, YL Ventures 2025 report (late 2025; undated) — https://www.ynetnews.com/business/article/rjggjusz11g
- Quick Heal: Sahi / Arthneeti (Oct 2026) [search extract] — https://www.sahi.com/news/quick-heal-technologies-reports-q2-net-profit-of-5-8-crore-versus-7-9-crore-yoy ; Multibagg concall (2026-11-05) — https://www.multibagg.ai/market-pulse/articles/quick-heal-enterprise-revenue-shift-concall-cmw349fd6004c2gtatbrn4zla
- CloudSEK: Outlook Business (May 2025); Angel One (January 2026) [search extract] — https://www.outlookbusiness.com/corporate/cloudsek-sees-5-fold-jump-in-valuation-in-19-million-fundraise-round ; https://www.angelone.in/news/unlisted-companies/cybersecurity-firm-cloudsek-raises-10-million-first-indian-origin-company-backed-by-a-us-state-fund
- Securonix: SiliconANGLE (2025-06-11) — https://siliconangle.com/2025/06/11/securonix-acquires-threat-intelligence-startup-threatquotient/
- Analytics India Magazine, Indian IT and AI labs (2026-05-07) — https://analyticsindiamag.com/it-services/indian-its-biggest-ai-partners-are-its-newest-enterprise-threats
- AZB & Partners, DPDP phased rollout (November 2025) [search extract] — https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/ ; Mondaq (November 2025) [search extract] — https://www.mondaq.com/india/data-protection/1706890/a-closer-look-at-the-dpdp-rules-2025
- European Commission pages:
  - CRA (updated 2026-09-07) — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
  - NIS2 (updated 2026-07-02) — https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
  - Cybersecurity Act (updated 2026-06-22) — https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-act
  - Certification framework (updated 2026-09-09) — https://digital-strategy.ec.europa.eu/en/policies/cybersecurity-certification-framework
- secunet, Zwischenmitteilung zum 30. September 2026 (2026-11-12) — https://www.secunet.com/fileadmin/user_upload/02_Downloads/IR/Finanzpublikationen/2026/Q3/26_11_12_Q3_Bericht_de_v3.pdf
- F-Secure Q3 2026 release (2026-10-28) [search extract] — https://www.placera.se/pressmeddelanden/f-secure-f-secure-interim-report-1-january-30-september-2026-accelerated-growth-driven-by-embedded-security-20261028
- Yubico Q3 2026 release (2026-11-05) [search extract] — https://mfn.se/a/yubico/interim-report-july-september-2026
- Wallix H1 2026, AMF filing (2026-07-16) — https://echanges.dila.gouv.fr/OPENDATA/AMF/ACT/2026/07/FCACT080594_20260716.pdf
- WithSecure tender and delisting (2025-11 to 2026-03) [search extract] — https://www.inderes.fi/en/releases/inside-information-a-consortium-formed-by-cvc-and-risto-siilasmaa-announces-a-recommended-cash-tender-offer-of-eur-170-per-share-through-diana-bidco-oy-to-the-shareholders-of-withsecure-corporation ; https://mfn.se/a/withsecure/withsecure-corporation-notice-pursuant-to-the-finnish-securities-market-act-chapter-9-section-10-1
- Financiarul, Bitdefender 2025 results and IPO deferral (2026-07-06) — https://financiarul.ro/companii/bitdefender-a-avut-venituri-de-480-de-milioane-de-dolari-in-2025-si-amana-l/
- Darktrace: Sharecast (2024) and Business Weekly / WebProNews (2026) [search extract] — https://sharecast.com/news/news-and-announcements/darktrace-reports-continued-strong-top-line-growth-ahead-of-thoma-bravo-takeover--17100755.html ; https://www.businessweekly.co.uk/posts/us-owner-seeks-new-ceo-for-ai-cyber-security-company-darktrace
- Sophos press page (read 2026-11-12) — https://www.sophos.com/en-us/press
- StockAnalysis quote/statistics pages (all read 2026-11-12) — https://stockanalysis.com/quote/nse/QUICKHEAL/statistics/ ; https://stockanalysis.com/quote/nse/SUBEXLTD/statistics/ ; https://stockanalysis.com/quote/etr/YSN/statistics/ ; https://stockanalysis.com/quote/sto/YUBICO/statistics/ ; https://stockanalysis.com/quote/hel/FSECURE/statistics/ ; https://stockanalysis.com/quote/epa/ALLIX/statistics/ ; https://stockanalysis.com/quote/epa/HO/statistics/

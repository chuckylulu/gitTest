# Three priors about the automated-security market, and whether defenders or attackers gain more from AI models: aggregate evidence as of 2026-11-12

*Method: primary data downloaded on 2026-11-12 (CISA KEV catalogue JSON, version 2026.11.10; NVD CVE API 2.0 counts by publication date, rejected records excluded), direct fetches of primary pages, seven WebSearch queries (WebSearch still worked; Firecrawl and Exa were not used), and consolidation of the nine notes files in this folder (file names in brackets). Every figure is dated. Company statements that no outside party has confirmed are tagged [company claim, unconfirmed]. Aggregate statistics, policy and business facts only.*

## 1. Offense–defense metrics: exploited flaws and CVE volumes 2022–2026, time-to-exploit, the Glasswing discovery-versus-repair gap, the open-weight lag and who has gated access

### Takeaway
Discovery has exploded but exploitation has not kept pace. NVD published 96,496 CVEs in 2026 up to 11 November, against 48,150 in all of 2025 (2.4x on a like-for-like basis), with the surge starting in Q2 2026. CISA's catalogue of exploited flaws grew only 36% (295 additions against 217 by 10 November), so the share of new CVEs known to be exploited fell to about 0.3%. Exploitation is faster, though: Mandiant's average time-to-exploit fell from 63 days (2018–19) to 5 days (2023) and an estimated −7 days (M-Trends 2026), meaning exploitation often comes before a patch.

Repair is the bottleneck. The two Glasswing figures in the notes describe the same disclosure pipeline at two dates:
- about 6%: 97 of 1,596 disclosed findings patched, data to 22 May 2026;
- 8.4%: 516 of 6,157 patched by 2 October 2026.

Between the two dates the unpatched backlog grew from about 1,500 to about 5,640. Open-weight models trail the frontier by about four to eight months on cyber tasks at roughly a hundredth of the cost. Gated access is concentrated in a few large US platforms.

### Cited Findings

#### CISA Known Exploited Vulnerabilities (KEV) catalogue (downloaded 2026-11-12; version 2026.11.10, released 2026-11-10, 1,779 entries; my counts by `dateAdded`)
| Year added | Additions (full year) | Additions 1 Jan–10 Nov | Additions whose CVE ID is from the same year | Memory-safety weakness share (of additions with a CWE tag)* | Distinct vendors |
|---|---|---|---|---|---|
| 2021 (catalogue launched Nov 2021) | 311 | — | — | — | — |
| 2022 | 555 | 543 | 91 (16%) | 32.7% (159 of 486) | 98 |
| 2023 | 187 | 161 | 121 (65%) | 27.9% (46 of 165) | 67 |
| 2024 | 186 | 154 | 116 (62%) | 17.4% (31 of 178) | 64 |
| 2025 | 245 | 217 | 151 (62%) | 21.8% (48 of 220) | 99 |
| 2026 (to 10 Nov) | 295 | 295 | 207 (70%) | 14.0% (40 of 286) | 111 |

*CWE-119/120–127/131/415/416/476/590/762/787/788/805/822–825/843. Source for the table and the items below: [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) (my calculations).
- Monthly additions in 2026: Jan 17, Feb 28, Mar 26, Apr 31, May 21, Jun 23, Jul 26, Aug 31, Sep 43, Oct 36, Nov (to the 10th) 13. In 2025 monthly additions ranged from 11 to 32 — [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)
- Vendors with the most 2026 additions: Microsoft 41, Cisco 21, Google 10, Apple 10, Linux 9, Fortinet 9, Ivanti 8 (2025: Microsoft 39, Apple 9, Cisco 8, Fortinet 8) — [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json)

#### CVE publications (NVD API 2.0, queried 2026-11-12, by NVD publication date, `noRejected`)
| Year | Q1 | Q2 | Q3 | Q4 | Total | YoY |
|---|---|---|---|---|---|---|
| 2022 | 6,016 | 6,346 | 6,483 | 6,228 | 25,073 | — |
| 2023 | 6,975 | 7,132 | 6,930 | 7,779 | 28,816 | +14.9% |
| 2024 | 8,681 | 11,698 | 8,523 | 11,051 | 39,953 | +38.6% |
| 2025 | 11,946 | 11,695 | 11,725 | 12,784 | 48,150 | +20.5% |
| 2026 | 15,152 | 20,688 | 36,953 | 23,703 (1 Oct–11 Nov) | 96,496 (to 11 Nov) | — |

- Like-for-like windows: 1 Jan–11 Nov, 40,951 (2025) vs 96,496 (2026), +136%. 1 Oct–11 Nov, 5,585 (2025) vs 23,703 (2026), 4.2x. Q3 2026 was 3.2x Q3 2025 — [NVD CVE API 2.0](https://services.nvd.nist.gov/rest/json/cves/2.0) (my queries)
- KEV additions as a share of NVD publications (my calculation): 2.2% (2022, inflated by back-filling older CVEs), 0.65% (2023), 0.47% (2024), 0.51% (2025), 0.31% (2026 to 10/11 Nov) — [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json); [NVD CVE API 2.0](https://services.nvd.nist.gov/rest/json/cves/2.0)

#### Exploitation timing and time-to-exploit
- **Mandiant (2024-10-15):** average time-to-exploit (TTE: time from patch or disclosure to exploitation; negative means exploited before a patch) was 63 days (2018–19), 44 (2020 to early 2021), 32 (2021–22) and 5 (2023). The 2023 figure excludes 15 outliers; it is 47 days with them. The 2023 sample was 138 exploited vulnerabilities, 70% of them zero-days — [Google Cloud / Mandiant, 2024-10-15](https://cloud.google.com/blog/topics/threat-intelligence/time-to-exploit-trends-2023)
- **M-Trends 2026 (2026-03-23; 2025 investigations, 500,000+ hours) [vendor report]:**
  - Mean TTE an estimated −7 days.
  - Exploitation was the top initial vector at 32% of intrusions, for the sixth straight year.
  - Global median dwell time 14 days (11 in 2024).
  - Hand-off from initial access to a second group: 22 seconds, against more than 8 hours in 2022.
  - Mandiant does not consider 2025 "the year where breaches were the direct result of AI".
  - Source: [Google Cloud, 2026-03-23](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)
  - A secondary post giving a 2025 mean of 44 days contradicts the −7 figure and was not confirmed in the primary source (search-result summary only) — [AlgeriaTech](https://algeriatech.news/?p=30026)
- **VulnCheck State of Exploitation 1H-2026 (2026-07-28; Patrick Garrity) [vendor data]:**
  - 495 CVEs first exploited in 1H-2026.
  - 23.43% were exploited on or before the CVE publication day, down from 28.93% in 2025.
  - Median time from CVE publication to KEV listing was 80 days, against 120 in 2025.
  - VulnCheck's own KEV-to-CVE ratio was 1.4%, down from a 2.7% peak in 2H-2023. KEVs rose about 10% over the prior six months while CVEs rose about 45%.
  - About 200 CVEs were exploited within 31 days in 1H-2026, against 194 "in 2025" and 196 "in 2024". The page does not make clear whether those comparison figures are full years or half-years.
  - About one-third of 1H-2026 KEVs were in content-management systems, and "the large majority" of edge-device makers had new KEVs.
  - Source: [VulnCheck, 2026-07-28](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026)
- **VulnCheck on AI-found flaws (same report):** 1,061 vulnerabilities were attributed to AI-assisted discovery. 14 of them (1.3%) were confirmed exploited in the wild, "roughly" the overall 1H-2026 rate and below historical rates. The Glasswing ledger held 23,019 reported findings, of which 126 had become published CVEs and one was confirmed exploited — [VulnCheck, 2026-07-28](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026)
- **CSA synthesis (data to 22 May 2026):**
  - Median time from disclosure to weaponised exploit fell from 771 days (2018) to "single-digit hours".
  - "28.3% of CVEs exploited within 24 hours". CSA's underlying sources were not checked. The figure resembles VulnCheck's 28.93% exploited on or before disclosure day in 2025, and probably refers to exploited CVEs, not all CVEs.
  - Source: [Cloud Security Alliance, released c. 2026-06-07](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity) [model_makers_gated_access.md]

#### Discovery versus repair: reconciling the Glasswing figures
| Data cut | Source | Discovered / disclosed | Patched | Patched share |
|---|---|---|---|---|
| ~22 May 2026 | [The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html) | >10,000 high/critical flagged by partners; 6,202 estimated high/critical in >1,000 OSS projects; 1,726 confirmed valid; 88 advisories | 97 patched upstream | 5.6% of confirmed valid |
| 22 May 2026 | [CSA, released c. 2026-06-07](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity) | 1,752 assessed by independent firms (90.6% valid, 62.4% high/critical); 1,596 disclosed to maintainers across 281 projects; 88 CVE/GHSA | 97 | 6.1% of disclosed |
| 28 Jul 2026 | [VulnCheck, 2026-07-28](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026) | 23,019 findings in the Glasswing ledger; 126 CVEs | n/a (1 exploited) | — |
| 9 Sep 2026 | Dark Reading citing Patrick Garrity, via [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary] | ~10% of discovered flaws disclosed | "under 1%" fixed | <1% of discovered |
| 2 Oct 2026 | Anthropic-reported, via [SIG, updated 2026-10-15](https://www.softwareimprovementgroup.com/blog/mythos-project-glasswing-security/) [company claim, unconfirmed] | 6,157 disclosed by Anthropic; ≥129,000 verified vulnerabilities found by partners Apr–Jul 2026 (from 33 partners' reports); 5,500 more from Anthropic's own OSS scanning through October; >33,000 critical/high; "<$50 of compute per vulnerability" | 516 | 8.4% of disclosed |

- **Reconciliation (my arithmetic on the figures above):**
  - Both figures measure patched ÷ disclosed to maintainers, at two dates.
  - From 22 May to 2 Oct 2026, disclosures rose 3.9x (1,596 → 6,157) and patches 5.3x (97 → 516). The patched share rose from 6.1% to 8.4%.
  - The unpatched backlog rose 3.8x, from 1,499 to 5,641.
  - Disclosures ran at about 245 a week in both periods. Patches rose from about 15 to about 22 a week. These rates assume disclosures began on 7 April 2026.
  - The "<1% fixed" figure uses all discovered findings as the denominator. The 129,000 partner figure is not comparable: partners' own code, with fixes not publicly tracked.
- **OpenAI's Linux-kernel scan (published c. 2026-11-04):** of 948 claimed flaws, 61 were patched (6.4%), 43 staging and 299 under discussion at scan end [company claim, unconfirmed] — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145) [model_makers_gated_access.md]
- **HackerOne, 2026 report:** open valid reports +131% from 2024 to 2026; critical open backlog +123%; 70% of security leaders say validated findings arrive faster than they can be fixed [company claim, unconfirmed] — [HackerOne report](https://www.hackerone.com/report) [ai_discovery_and_testing_platforms.md]
- **Other voices on the bottleneck:**
  - Trail of Bits (2026-06-22): the "expensive part" has moved from finding to confirming, patching and coordinating — [Trail of Bits](https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/)
  - Linus Torvalds called the Linux security list "almost entirely unmanageable" because of duplicate AI-driven reports — [The Register, 2026-05-21](https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458)
  - SecurityWeek (2026-06-09): discovery is "cheap and abundant", triage and remediation scarce — [SecurityWeek](https://www.securityweek.com/will-ai-kill-the-bug-bounty-industry/) [ai_discovery_and_testing_platforms.md]

#### Open-weight models against the frontier on cyber tasks (consolidated from [model_makers_gated_access.md])
- **DeepSeek V4 Pro (CAISI/NIST, 2026-05-01):** "lag behind the frontier by about 8 months". On CAISI's CTF-Archive-Diamond: GPT-5.5 71%, Opus 4.6 46%, DeepSeek V4 Pro 32% — [NIST CAISI](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
- **GLM-5.3 (CAISI, 2026-09-17):** "roughly four months behind U.S. frontier models in aggregate". SEC-Bench Pro 40.4% vs 90.2%; ExploitBench 61.1% vs 100%; ExploitGym 9.4% vs 44.4%; OSS-Fuzz 7.7% vs 23.2% — [CASRAI guide](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments) [secondary]
- **Kimi K3 (UK AISI + CAISI, 2026-07-23, updated 2026-08-28):** full automated compromise in 0 of 41 sampled vulnerabilities, against about 20 of 41 for the most capable models — [CASRAI guide](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments) [secondary]
- **CSA synthesis of UK AISI data (2026-07-31):**
  - The lag was four to seven months in mid-2026, down from six to ten in 2025.
  - DeepSeek V4-Pro cost about $0.28 per task against $12.50–15.17 for Opus 4.5/4.6.
  - Open-weight tests were "largely unimpeded by safeguards".
  - Caveat: the two largest 2026 jumps came from closed models.
  - Source: [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/)
- **Cost of an open-weight exploit (late Sep 2026):** Anthropic reported that GLM-5.3-Flash wrote a working exploit for an already-fixed browser flaw for $20.40 at API prices, plus 20 minutes of human attention [competitor claim, not independently verified] — [Notebookcheck, 2026-10-01](https://www.notebookcheck.net/GLM-5-3-China-s-open-AI-model-built-a-Chrome-exploit-for-20.1413141.0.html)
- **Attackers' model choice in practice:** operators of the criminal ARTEX campaigns mostly configured Chinese models (DeepSeek, Kimi), and switched to Chinese models when an Anthropic model's guardrails triggered [vendor research] — [Check Point Research, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/) [fortinet_checkpoint_exposure_mgmt.md]
- **Chinese domestic substitute:** 360's Tulongfeng ("China's version of Mythos"). Zhou Hongyi said domestic models still have "a 20%-30% gap in base capability"; Reuters could not verify 360's claims — [Insurance Journal (Reuters), 2026-06-26](https://www.insurancejournal.com/news/international/2026/06/26/875418.htm)

#### Who has gated access (consolidated from [model_makers_gated_access.md], Tables A–B)
- **Anthropic Project Glasswing → Cyber Verification Program (CVP):**
  - Launch partners (7 Apr 2026) included Palo Alto Networks, CrowdStrike, Cisco and Broadcom — [Anthropic](https://www.anthropic.com/glasswing)
  - Okta joined on 27 May 2026 — [BankInfoSecurity, 2026-09-18](https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191)
  - Trend Micro announced participation on 3–4 Jun 2026; Hitachi signed in June with access "expected to be granted later" — [Uravation](https://uravation.com/media/hitachi-trendmicro-claude-mythos-project-glasswing-japan-2026/)
  - Booz Allen is a Glasswing partner — [Unite.AI, Oct 2026](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/)
  - Rubrik was a named Mythos 5.2 tester (9 Nov 2026) — [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2)
  - HackerOne announced a Mythos integration on 21 Sep 2026 — [HackerOne](https://www.hackerone.com/press-release/hackerone-bring-anthropics-mythos-exposure-management-lifecycle-discovery-verified)
  - Samsung, SK Hynix, SK Telecom, NATO and ENISA were named in the 2 Jun 2026 expansion to about 15 "U.S.-friendly" countries — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- **OpenAI Trusted Access for Cyber → Daybreak:**
  - Partners (10–11 Aug 2026): Palo Alto Networks (Unit 42), CrowdStrike, Cisco, Sophos, Akamai, Fortinet, Cloudflare, NCC Group, SpecterOps, plus consultancies (Accenture, IBM, Capgemini, Cognizant, EY, KPMG, PwC) — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/)
  - GPT-6 Cyber (5 Nov 2026, rated "Critical" for cyber) users: Palo Alto Networks, Cisco, Calif, CodeRabbit — [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/). Dragos is an evaluation partner — [CyberScoop, 2026-11-05](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)
  - Check Point, Tenable, HackerOne, Elastic and Proofpoint appear only in a search extract of OpenAI's partners page [unconfirmed; page returned 403] — [OpenAI](https://openai.com/daybreak/partners/)
- **Google DeepMind Fairwind (blog 2026-09-02):** CrowdStrike, Palo Alto Networks, Wiz, Menlo Security, Datadog, Snowflake, Armadin and the Center for Internet Security; more than 650 partners in September 2026 — [DeepMind](https://deepmind.google/fairwind-program/); [Google blog](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)
- **Not found in any published list:** Zscaler, SentinelOne, Rapid7, Qualys, Snyk, Socket, Bugcrowd, Claroty, Armis/ServiceNow, Nozomi/Mitsubishi Electric, and Indian and Taiwanese vendors. Absence is not proof of exclusion. XBOW used public OpenAI models — [XBOW, 2026-10-13](https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users)
- **Country rules:**
  - Since 5 Sep 2025 Anthropic bars companies majority-controlled from China, Russia, Iran or North Korea — [The Decoder](https://the-decoder.com/anthropic-bans-companies-majority-controlled-by-china-russia-iran-and-north-korea-from-claude/)
  - From 12 to 30 Jun 2026 a US Commerce directive suspended all foreign-national access to Mythos 5 and Fable 5 — [Tech Policy Press, 2026-06-15](https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/); [CNBC, 2026-06-30](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)
  - The top CVP tier is reviewed "in collaboration with the US government" (6 Oct 2026) — [Unite.AI](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/)
  - Korean access was disputed on 17 Sep 2026 — [The Elec, 2026-09-18](https://www.thelec.net/news/articleView.html?idxno=14029)
  - Japan's cyber director said the June directive disrupted government vulnerability scanning and that Japan "should not rely on any one particular AI model" — [TechTimes, 2026-08-10](https://www.techtimes.com/articles/323705/20260810/japans-cyber-chief-confirms-us-ai-export-ban-hit-government-security-scanning.htm) [japan_korea_taiwan.md]
- **Gate leakage:** unauthorised users reached Mythos through a private Discord channel, reported 21 Apr 2026 — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- **Independent capability check:** UK AISI (2026-04-13) found Mythos Preview the first model to complete its 32-step range (3 of 10 attempts). The ranges had no active defenders, so "we cannot say for sure whether Mythos Preview would be able to attack well-defended systems" — [UK AISI](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)

### Inferences
- **The 2026 CVE surge coincides with the gated AI-discovery programmes** (Glasswing from 7 Apr; Daybreak from Aug; Fairwind from Sep 2026). Q2 2026 rose 77% year on year, Q3 215% and October–mid-November 324%. The data do not show how much is AI-driven: VulnCheck tags only 1,061 1H-2026 flaws as AI-found, against a surplus of about 55,000 CVEs year to date. "AI-driven" is a likely but unproven explanation.
- **Exploitation has grown far more slowly than disclosure.** KEV additions rose 36%, CVEs 136%. VulnCheck's share exploited on or before publication day fell, and AI-found bugs are exploited at the baseline rate. So far the AI discovery wave adds mainly to defenders' patch queues, not to observed exploitation. KEV is a lagging and detection-limited measure, so this is a statement about what has been seen, not what has happened.
- **Faster exploitation predates the gated models.** Mandiant's mean TTE had already reached 5 days in 2023, before the 2026 models. The 2026 data (VulnCheck's median time to KEV down from 120 to 80 days; 70% of 2026 KEV additions carrying 2026 CVE IDs, against 62% in 2025) are consistent with continued compression, and with KEV listing faster.
- **The repair gap is widening in absolute terms** (unpatched disclosed backlog ×3.8 in about four months) while improving slightly in percentage terms (6.1% → 8.4%). This is the strongest quantitative evidence that, in the short run, the same models raise attackers' supply of known-but-unfixed flaws faster than defenders can close them.
- **Gated access buys defenders months, not years.** The lag is four to eight months, and open-weight testing is "largely unimpeded by safeguards". The lead is concentrated in a handful of US platforms (Palo Alto Networks and CrowdStrike in all three programmes, Cisco in two) and depends on Washington for non-US holders.

### Gaps
- CVE.org's own metrics page was not used. NVD counts by NVD publication date can differ slightly from CVE.org's counts of published records. FIRST EPSS was not analysed.
- The −7-day M-Trends figure is not defined on the blog page, and the full report PDF was not opened. VulnCheck's comparison periods for the "within 31 days" counts are ambiguous.
- No source measures what share of the 2026 CVE surge comes from AI-assisted discovery, nor any net offence-versus-defence effect.
- CISA KEV is US-federal-centric and under-represents consumer IoT; VulnCheck's broader KEV lists many consumer router makers with 1H-2026 KEVs. No independent check of Anthropic's 129,000 / 6,157 / 516 counts was found; they reach these notes via SIG, a secondary source.

## 2. P1 — "a mass compromise of consumer or industrial devices is attributed to AI-built exploits by the end of 2027" (prior 60%)

### Takeaway
As of 2026-11-12, no government agency or major threat-intelligence team has attributed a mass compromise of consumer or industrial devices to AI-built exploits. The parts of the prior have each been seen separately:
- **Mass device compromises without AI:** BADBOX 2.0 ("millions" of infected consumer devices, FBI, June 2025) and state actors on end-of-life routers.
- **AI-written exploit code in consumer-IoT malware:** Unit 42's TuxBot v3 (15 Jul 2026) has exploit modules for previously known flaws, is about 70% functional, and comes with no infection count.
- **AI-run intrusions against organisations:**
  - Anthropic (Nov 2025): about 30 targets, "a small number" breached.
  - Amazon (Feb 2026): 600+ firewalls in 55+ countries, but no vulnerability was exploited.
  - Korean banks (Oct 2026): described as AI-linked, with no official attribution.

Mandiant says 2025 was not "the year where breaches were the direct result of AI". Verdict: partly supported. The precursors exist; the event as defined has not happened. Thirteen and a half months remain.

### Cited Findings

#### What has been attributed to AI (dated; aggregate facts only)
- **Anthropic (2025-11-13, edited 2025-11-14):**
  - Attributed "with high confidence" to a Chinese state-sponsored group a campaign in which AI did an estimated 80–90% of the work, with humans at 4–6 decision points.
  - Roughly 30 targets: large tech companies, financial institutions, chemical manufacturers and government agencies. It succeeded in "a small number of cases". No consumer or industrial devices are mentioned.
  - The model sometimes hallucinated credentials and results, which Anthropic says "remains an obstacle" to fully autonomous attacks [company claim, unconfirmed by outside parties].
  - Source: [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage)
- **Amazon Threat Intelligence (2026-02-20, CJ Moses):**
  - A Russian-speaking, financially motivated actor of low-to-medium skill, not linked to a state group, compromised over 600 FortiGate firewalls in more than 55 countries between 11 Jan and 18 Feb 2026.
  - It used at least two commercial generative-AI services across all phases.
  - "The campaign did not exploit any FortiGate software vulnerability"; access came from weak credential and configuration hygiene.
  - Amazon expects AI-augmented activity to keep growing in 2026, and says commercial AI can "lower the technical barrier to entry" [company threat-intelligence finding].
  - Source: [AWS Security Blog](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/)
  - CSA describes what appears to be the same case as an "AI-orchestrated campaign" that scanned 2,516 FortiGate targets in 106 countries and compromised more than 600 devices. Its country count conflicts with Amazon's 55+ — [CSA](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity)
- **Palo Alto Networks Unit 42, TuxBot v3 Evolution (2026-07-15; Davila, Navarrete, Santos):**
  - The developer "relied heavily on LLM-generated code". The evidence is artefacts: leftover model reasoning in comments, an identical safety disclaimer in about 60 files, and a hallucinated feature.
  - The exploit modules target previously disclosed CVEs dated 2007–2026; no zero-days are described.
  - About 70% of the framework is functional.
  - No count of infected devices, victims or attack size is given, and Unit 42 does not call it a mass compromise.
  - The operator is linked through shared infrastructure to the Keksec ecosystem (with Aisuru-related tooling).
  - Unit 42 calls a fully working version "a likely threat" [vendor threat-intelligence finding].
  - Sources: [Unit 42](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/); [Security Affairs, 2026-07-16](https://securityaffairs.com/195486/ai/tuxbot-v3-the-iot-botnet-built-with-ai-bugs-disclaimers-and-all.html)
  - An OECD AI Incidents Monitor entry dated 2026-07-15 is titled "AI-Assisted TuxBot v3 IoT Botnet Actively Exploits Devices for DDoS Attacks" (title from a search result; not opened) — [OECD.AI](https://oecd.ai/en/incidents/2026-07-15-98ee)
- **South Korean banks (October 2026):**
  - Shinhan said on 1 Oct 2026 that data on about 25,000 customers leaked; Hana and KB also reported leaks.
  - The hackers "reportedly used advanced artificial intelligence tools"; the source of that claim is not named.
  - The Financial Supervisory Service found suspect IP addresses in 12 countries. No official attribution to an actor or country was reported. President Lee called for a thorough investigation.
  - Source: [Korea JoongAng Daily, 2026-10-11](https://www.koreajoongangdaily.com/business/banks-boost-defenses-after-ailinked-hacks/12913975)
  - President Lee said AI appears to have been used (headline only; paywalled) — [Japan Times, 2026-10-06](https://www.japantimes.co.jp/business/2026/10/06/south-korea-bank-hacks/)
  - A report that CrowdStrike tied the attacks to a China-based actor using an open-source AI penetration-testing agent alongside Claude Code comes only from a low-reliability blog [unverified] — [Shattered.io](https://shattered.io/crowdstrike-artex-ai-agent-korea-bank-hack-2026/) [japan_korea_taiwan.md]
- **Check Point Research, ARTEX (2026-11-05; covering October 2026):**
  - Criminals repurposed an LLM-driven multi-agent penetration-testing platform.
  - 2,557 systems hosted or had hosted its panels, 1,608 of them live.
  - Victims were web, crypto and gaming domains, not devices.
  - Operators were largely hands-off and mostly used Chinese models [vendor research].
  - Source: [CPR](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/) [fortinet_checkpoint_exposure_mgmt.md]
- **Mandiant, M-Trends 2026 (2026-03-23):** edge-device and router compromises in 2025 are attributed to zero-days and in-memory malware, not AI. Mandiant does not consider 2025 "the year where breaches were the direct result of AI" — [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026)
- **VulnCheck (2026-07-28):** 14 of 1,061 AI-discovered vulnerabilities (1.3%) are confirmed exploited in the wild. This concerns AI-found flaws, not AI-built exploits — [VulnCheck](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026)
- **Warnings without attribution:**
  - Anthropic privately warned officials that large-scale attacks were significantly more likely in 2026 (Axios, via Fortune) — [Fortune, 2026-04-07](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/)
  - OpenAI (Nov 2026): a low-privileged account on an unpatched system "should be considered functionally equivalent to root access" for a well-resourced actor — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145) [model_makers_gated_access.md]
  - Finite State's "Vulnpocalypse" framing is vendor marketing, not attribution — [The IT Nerd, 2026-11-10](https://itnerd.blog/2026/11/10/finite-state-raises-27-million-to-help-device-makers-fight-the-vulnpocalypse-with-ai-powered-product-security/) [ot_iot_shielding_regulation.md]

#### Large device compromises without an AI attribution
- **BADBOX 2.0:** FBI PSA (2025-06-05) describes "millions of infected devices" (TV boxes, projectors, vehicle infotainment, picture frames), mostly made in China, with malware pre-installed or installed at setup — [FBI IC3](https://www.ic3.gov/PSA/2025/PSA250605) [ot_iot_shielding_regulation.md]
- **State actors on routers:** the FBI said in April 2026 that Russian military intelligence exploited a TP-Link router flaw, with most affected products end-of-life. State lawsuits also cite Microsoft's 2024 report of a China-based botnet made mostly of TP-Link routers — [The Hacker News, Oct 2026](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html) [ot_iot_shielding_regulation.md]
- **Mirai variant without AI:** an April 2026 variant tracked by Akamai spread through an old router flaw. Its code string suggests it was written without AI (search-result summary) — [Help Net Security, 2026-04-22](https://www.helpnetsecurity.com/2026/04/22/new-mirai-variants-target-routers-and-dvrs-via-old-flaws/)

#### Aggregate device-exploitation indicators (my counts; [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json))
- **Consumer, small-office and IoT device makers:** 19 KEV additions in 2025, against 6 in 2026 to 10 November. The match on D-Link, TP-Link, ASUS, Zyxel, DrayTek, GeoVision, Edimax, Digiever, Ubiquiti and Hikvision was checked by hand.
- **Industrial or OT vendors:** about one or two additions a year (2025: Sierra Wireless; 2026: Rockwell, plus a Siemens software product). There is no surge in CISA's catalogue. VulnCheck's broader catalogue shows "the large majority" of edge-device makers with new KEVs in 1H-2026 — [VulnCheck](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026)

### Inferences
- **How far the evidence is from the prior:**
  - The "AI-built exploit" element has appeared in consumer-IoT malware (TuxBot) and in an espionage campaign (Anthropic).
  - The "mass compromise of consumer or industrial devices" element happens routinely without AI (BADBOX 2.0; router botnets).
  - The conjunction has not been reported: a mass device compromise that a credible party attributes to AI-built exploits. The missing pieces are scale and public attribution, not capability.
- **Attribution friction cuts against 60%.** AI authorship has so far been detected through careless artefacts (disclaimers, reasoning comments, hallucinated features), which competent operators can remove. IoT botnets mostly reuse known exploits, which humans and LLMs write equally easily, so an AI-built exploit leaves little distinctive trace. Even if AI-written exploits power a large botnet before end-2027, a public attribution of the kind the prior requires may lag.
- **Evidence that keeps the prior plausible.** The Keksec/Aisuru-linked ecosystem already uses LLMs, and Unit 42 expects a working TuxBot version. Exploit-writing costs with open weights are reported at about $20 (claim). Amazon and Anthropic both expect AI-augmented attacks to grow in 2026.
- **Evidence that contradicts the prior's implied timing:**
  - M-Trends 2026 explicitly finds no AI-caused breaches in 2025.
  - The best-documented AI-augmented device campaign (Amazon) used no exploit.
  - AI-found flaws are exploited at the baseline rate (VulnCheck).
  - CISA's consumer-device KEV additions fell in 2026.
- On balance the evidence is consistent with the event being possible by end-2027, but it gives no support for treating it as more likely than not. The 60% prior looks generous: precursors are present, the event is absent, and attribution is hard.

### Gaps
- Sizes of the record IoT DDoS botnets of 2025–2026 (for example Aisuru and Kimwolf), and any AI link, were not verified. Nor were OT incidents in 2025–2026 (water utilities, European dams).
- No government advisory (CISA, FBI, NCSC, Japan's NCO, KISA) attributing device compromises to AI-built exploits was found. The search was not exhaustive because of the search budget.
- CrowdStrike's reported attribution of the Korean bank attacks is unverified. The Japan Times and American Banker articles were not opened.
- Unit 42 gives no infection counts for TuxBot. The OECD incident entry was not opened.

## 3. P2 — "rates for human penetration testing fall first; overall spending on finding and patching flaws shrinks only after 2030, if verified software removes whole classes of bugs" (prior 35%)

### Takeaway
The first leg is not visible in day rates. UK contractor pentest day rates rose in the six months to 12 Nov 2026: median £590 against £550 a year earlier (+7.3%), 90th percentile £775 against £675, with job ads up 10%. NCC Group's human assurance revenue is flat, not cut-price.

What is falling is the price of routine findings:
- low-end bounty rates are being cut (Internet Bug Bounty −76% to −89%, May 2026; the Chrome memory-bug base reward is now $500);
- several open-source bounties closed or paused in 2026;
- autonomous tests are sold at about $3,000 a year, against a UK human median of £1,000 a day.

Total payouts still rise (HackerOne +26% in H1 2026).

The second leg — no shrinkage before 2030 — fits every forecast (Gartner 10.8% CAGR 2025–30; IDC 12.5%) and the doubling of CVEs. A bug class is shrinking as a share of flaws: memory-safety bugs fell below 20% of Android vulnerabilities in 2025, and from 32.7% to 14.0% of KEV additions between 2022 and 2026. AI proofs became two to three orders of magnitude cheaper in one case. Yet total find-and-fix work is rising. Verdict: partly supported. The "rates fall first" leg is contradicted so far for day rates and supported only for bounty-priced routine work.

### Cited Findings

#### Human penetration-testing prices
- **UK contract day rates for penetration testing (ITJobsWatch, data to 2026-11-12).** These are what testers are paid, not what clients are billed — [ITJobsWatch](https://www.itjobswatch.co.uk/contracts/uk/penetration%20testing.do)

  | Six months to 12 Nov | 2026 | 2025 | 2024 |
  |---|---|---|---|
  | Daily rates quoted | 185 | 172 | 102 |
  | 10th percentile | £417 | £400 | £450 |
  | Median | £590 | £550 | £583 |
  | 90th percentile | £775 | £675 | £765 |
  | Contract job ads | 274 | 248 | 151 |
  | Rank among all skills (lower = more demand) | 441 | 347 | 395 |

- **UK public-sector billing rates (G-Cloud 14):**
  - Median £1,000 a day across 30 pentest rate cards (read 29 Aug–1 Sep 2026); central band £800–1,200; full spread £480–1,600; red team median £1,400; web/application £950.
  - US federal (GSA CALC+, 553 rates from 163 contractors): median ceiling $157.03 an hour, about $1,256 a day.
  - No year-on-year series is given.
  - The lowest published prices are "mostly autonomous or same-day AI-powered tests", e.g. about $2,999–3,000 a year for autonomous tiers. The publisher sells both autonomous and human tiers [vendor index; commercial interest].
  - Source: [Stingrai, 2026-06-05, re-read 2026-10-23](https://www.stingrai.io/blog/penetration-testing-price-index-2026)
- **Big Four bands:** published framework bands of £400–2,885 a day (KPMG) and £500–3,500 (PwC) (search-result summary; not opened) — [Stingrai cost per hour](https://www.stingrai.io/blog/penetration-testing-cost-per-hour-2026)
- **Survey spend:** Pentera's 2025 survey of 500 security executives found US enterprises spend an average of $187,000 a year on penetration testing (search-result summary; vendor survey) — [DeepStrike](https://deepstrike.io/blog/penetration-testing-statistics)
- **AI economics at the top end:** Google paid its $250,000 maximum for a full Chrome exploit chain built by XBOW in six days for about $40,000 of compute. Approved 31 Aug 2026; public 13 Oct 2026; human-steered — [CyberInsider](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/) [ai_discovery_and_testing_platforms.md]
- **Budget-shift claims by automation vendors:** Horizon3 ARR +120%; Pentera's average deal quadrupled to about $100,000 (March 2025); Synack says its Sara agent costs "a fraction" of a traditional pentest [company claims, unconfirmed] — [Horizon3](https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/); [Calcalist](https://www.calcalistech.com/ctechnews/article/ryvxvby21x); [IT Brief](https://itbrief.co.nz/story/synack-launches-sara-ai-pentesting-for-wider-coverage)
- **Vendor-sponsored surveys:** 87% of organisations plan, pilot or use agentic AI for pentesting (Synack/Omdia, March 2026); 94% value humans in offensive security (Cobalt/Omdia) — [Synack/Omdia](https://www.bolsamania.com/nota-de-prensa/mercados/95-of-enterprises-prioritize-pentesting-yet-only-32-of-attack-surfaces-are-tested-new-synack-and-omdia-research-finds--22105138.html); [ChannelLife](https://channellife.news/story/cobalt-launches-autonomous-pentest-for-continuous-testing) [ai_discovery_and_testing_platforms.md]

#### Bug-bounty payouts and programme closures (consolidated from [ai_discovery_and_testing_platforms.md])
- **HackerOne totals:**
  - $89.1M paid in July 2025–June 2026, across 92,194 valid reports; $81M the previous year (+13%) [company data] — [HackerOne report](https://www.hackerone.com/report); [HackerOne press release, Oct 2025](https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy)
  - CEO, 3 Nov 2026: payouts +26% year on year in H1 2026, accelerating in Q3. Submissions are up 2.8x and valid reports 1.9x since January 2025. Programmes pay less for low-severity issues, duplicates and automatable findings [company claim, unconfirmed] — [Help Net Security](https://www.helpnetsecurity.com/?p=389850)
  - March 2026: 46,947 submissions (+76%), about 25% valid; critical or high at 32% of validated findings, against a historical 26–28% — [The CyberSec Guru](https://thecybersecguru.com/analysis/what-happened-to-hackerone/)
- **Internet Bug Bounty (effective 18 or 22 May 2026; sources conflict):**
  - Critical $9,250 → $2,257; high $4,429 → $1,009; medium $1,843 → $297; low $597 → $68.
  - New submissions were paused.
  - Sources: [The Register, 2026-05-21](https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458); [LavX, 2026-05-21](https://news.lavx.hu/article/hackerone-cuts-internet-bug-bounty-payouts-by-over-75-percent-amid-ai-driven-reporting-surge)
- **Closures and pauses:**
  - curl ended its bounty at the end of January 2026, citing AI "slop" — [Hackaday, 2026-01-26](https://hackaday.com/2026/01/26/the-curl-project-drops-bug-bounties-due-to-ai-slop)
  - Nextcloud closed its bounty in April 2026 — [ForkLog, 2026-07-24](https://forklog.com/en/the-end-of-bug-bounties/)
  - Google's open-source VRP paused new product reports from 1 Oct 2026 until at least Q1 2027 — [Malwarebytes, Oct 2026](https://www.malwarebytes.com/blog/news/2026/10/google-pauses-open-source-bug-bounty-program-after-rise-in-ai-submissions)
  - Intel reportedly launched an Intigriti programme with no bounties (search snippet; unverified).
- **Two-tier pricing:**
  - Google cut Chrome memory-bug base rewards to $500 (May 2026).
  - Top rewards rose: Apple $2M (Oct 2025), Google Titan M $1.5M (May 2026), Microsoft Zero Day Quest up to $5M (Aug 2025).
  - Source: [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/)
- **AI-found duplicates:** half of one hunter's ten AI-found bugs were duplicates — [SecurityWeek, 2026-06-09](https://www.securityweek.com/will-ai-kill-the-bug-bounty-industry/)

#### Revenue trends at labour-heavy testers
- **NCC Group (UK), H1 FY26 (to 31 Mar 2026; published 11 Jun 2026):**
  - Technical Assurance revenue +0.2% at constant currency.
  - North America Cyber −11.3% at constant currency against H2 FY25, "driven by a reduction in Technical Assurance Services revenue from large technology clients".
  - "A more consistent approach to pricing and margin management".
  - Cyber gross margin up 3.2 points to 38.4%.
  - Source: [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf)
- **NCC Group, FY26 trading update (to 30 Sep 2026; published 27 Oct 2026):** Cyber revenue about £235m (+3.7% at constant currency); Cyber adjusted EBITDA £16.3m (6.9%); record 38.4% gross margin — [HL/Sharecast](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations) [ai_discovery_and_testing_platforms.md]
- **LAC (Japan):** delisted effective 25 Feb 2025 after KDDI's tender offer and cash-out. The last public results covered nine months to 31 Dec 2024 (published 13 Feb 2025), so no current public revenue trend exists — [LAC IR page, accessed 2026-11-12](https://www.lac.co.jp/english/ir/)
- **Indian IT services:**
  - No cyber-practice revenue disclosures were retrieved.
  - The Nifty IT index was −23% year to date, and the sector lost about $70B in market value "within weeks of Claude Code's February release" (AIM's phrasing) — [Analytics India Magazine, 2026-05-07](https://analyticsindiamag.com/it-services/indian-its-biggest-ai-partners-are-its-newest-enterprise-threats)
  - No Indian-headquartered IT major is named in a gated cyber programme. Capgemini and Cognizant are Daybreak partners — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/) [israel_india_europe.md]
- **Services lines at product vendors:** Rapid7 professional services −19% in Q3 2026, 3% of revenue — [Rapid7 8-K, 2026-11-04](https://www.sec.gov/Archives/edgar/data/0001560327/000156032726000049/q32026rapid78-kex991.htm) [fortinet_checkpoint_exposure_mgmt.md]

#### Is memory-safe or verified software shrinking a class of bugs?
- **Google, Android (2025-11-13, Jeff Vander Stoep):**
  - Memory-safety vulnerabilities fell "below 20% of total vulnerabilities for the first time" in 2025; the chart shows above 70% in 2019–2021.
  - Rust has about 0.2 vulnerabilities per million lines against close to 1,000 for C/C++.
  - New Rust code slightly exceeded new C++ in the first three quarters of 2025.
  - Google calls memory-safe languages "only one part" of the strategy; C and C++ "will persist".
  - Source: [Google blog](https://blog.google/security/rust-in-android-move-fast-fix-things/)
- **CISA KEV:** the memory-safety share of KEV additions with a CWE tag fell from 32.7% (2022) to 27.9% (2023), 17.4% (2024), 21.8% (2025) and 14.0% (2026 to 10 Nov) — [CISA KEV JSON](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) (my calculation)
- **Verification escapes:** "Verification Theatre" (IACR ePrint 2026/192, revised 2026-06-25) found 13 vulnerabilities that escaped formal verification in verified crypto libraries. Nine were in unverified code and four in specification or proof code. One caused real decryption failures in Signal's post-quantum ratchet — [IACR ePrint](https://eprint.iacr.org/2026/192) [code_supply_chain_verification.md]

#### Cost evidence for AI-generated proofs (from [code_supply_chain_verification.md])
- **CryptoProver (arXiv 2608.00965; v1 2026-08-02, v2 2026-10-16):** a new independent Verus proof of curve25519-dalek in 11.4 hours for $466.99 of API cost, against "a focused five-month, three-person effort" originally — [arXiv](https://arxiv.org/abs/2608.00965)
- **Products:** Certora AutoProver (July 2026) [company claim] — [ChainCatcher](https://www.chaincatcher.com/en/article/2243764); AWS Kiro requirements analysis pairing an LLM with an SMT solver (May 2026) — [GeekWire](https://www.geekwire.com/2026/aws-targets-ai-slop-with-new-spec-check-in-kiro-coding-tool-amid-scrutiny-of-agent-reliability/)
- **Signal Shot (2026-04-20):** no verified results yet — [de Moura blog](https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/)
- **Regulation:** the EU Cyber Resilience Act requires lifecycle vulnerability handling whatever the development method. Reporting applies from 2026-09-11 and main obligations from 2027-12-11 — [European Commission](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act)

#### Demand for finding and patching through 2030
- **Gartner (3Q26 forecast, report G00862059, via secondary):**
  - Growth of 10.4% (2028), 10.0% (2029) and 9.6% (2030) in constant currency; 2025–2030 CAGR 10.8%.
  - "AI-amplified security" reaches $204B by 2030 but "is not additive spending".
  - Source: [Software Strategies Blog, 2026-11-09](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/) [secondary; Gartner report links are subscription-only]
- **IDC:** $512.9B in 2030 with a five-year CAGR of 12.5% (IDC IT Security event page, undated, via the same blog) [secondary] — [Software Strategies Blog](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/)

### Inferences
- **Sequencing so far runs volume first, then price.** NCC's human assurance revenue is flat and its North American large-tech book fell, while UK contractor day rates rose. The routine end is being priced down through bounties and cheap autonomous products, not through day-rate cuts. That contradicts "rates for human penetration testing fall first" for day rates, as of November 2026.
- **The ITJobsWatch rank fell 94 places** even as absolute ads rose 10%. Pentesting's share of total contract demand is slipping, which may come before rate pressure. This is a watch item, not evidence of a fall.
- **"Shrinks only after 2030" is consistent with all available forecasts.** No forecaster projects a decline before 2030. The leg is not testable before then, but nothing contradicts it.
- **"If verified software removes whole classes of bugs":**
  - The memory-safety class is shrinking as a share in Android and in exploited flaws (KEV).
  - Proof costs fell sharply in one narrow, high-value component.
  - But total CVE volume doubled in 2026 and patch backlogs grew, and verified code still yields escapes. So far class removal changes the mix of find-and-fix work rather than shrinking it.
- **Implication for the 35% prior:** the conditional structure is plausible. The leading indicator the prior names (human rates falling first) has not appeared, so the evidence gives no reason to raise the prior and some reason to doubt the predicted order.

### Gaps
- No time series of client billing rates (CREST, a procurement framework, or a survey) for 2024–2026 in any country. ITJobsWatch measures contractor pay; Stingrai is a snapshot. US, EU and Japanese series were not found. Cyentia's 2026 State of Pentesting report was not read.
- No LAC financials after delisting, and no Indian IT services cyber-practice revenue.
- NCC's audited FY26 results were not yet published as of 2026-11-12. No pentest-only revenue lines were found for Big Four or Japanese integrators.
- No data on the total spend shifting from human to automated testing beyond vendor surveys.

## 4. P3 — "security demand holds in an AI-spending pause, because cheap models are enough for attackers"

### Takeaway
No AI-spending pause has happened, so P3 can only be tested indirectly. Forecasters expect security spending to grow 11–13% a year in 2026–27:
- Gartner (3Q26): $247.5B in 2026 (+13.6%) and $276.1B in 2027 (+11.6%);
- IDC: $310.42B in 2026 (+13.2%);
- Omdia: $315B in 2026 (+13%).

Buyer surveys are thinner. IANS found budgets up 5% on average in 2026 but with the median flat; 45% of CISOs had flat budgets and 10% cuts. Security spending slowed but kept growing in 2009 and in 2022–23.

Q3 2026 growth ranged from −30% (Qi An Xin) to +34% (Palo Alto Networks, boosted by acquisitions):
- US platforms +20% to +34%; exposure management −2.5% to +11%;
- Check Point −1%; Trend Micro +3% in constant currency; AhnLab +23%;
- Chinese median −4%; European +4% to +29%; India's Quick Heal −22%.

Cheap models do appear to be enough for opportunistic attackers: the ARTEX operators used DeepSeek and Kimi, and open weights trail the frontier by four to eight months at about a hundredth of the cost. That supports the mechanism. But China's 2023–25 contraction and flat median CISO budgets show demand does not hold everywhere, and part of 2026's growth is tied to the AI build-out. Verdict: partly supported.

### Cited Findings

#### Security-spending forecasts for 2026–2027
- **Gartner, 3Q26 forecast (report G00862059; published 24 Sep 2026 per a search summary, unverified):**
  - 2026 $247.5B (+13.6%; +12.7% constant currency), against $248.2B in 2Q26 and $244.2B in 4Q25. 2027 $276.1B (+11.6%; +11.2% constant currency).
  - 2026 segments: software $126.9B, services $93.5B, network security equipment $27.0B, consumer $9.0B. Managed security services $32.3B, of which MDR $11.5B.
  - US $119.5B (2026), $133.6B (2027) and $181.1B (2030); Europe $64.0B (2026).
  - Source: [Software Strategies Blog, 2026-11-09](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/) [secondary; Gartner's own release not retrieved]
- **Gartner, securing AI:** $2.835B (2026) → $4.783B (2027, +68.7%) → about $7.7B (2028) — [IT Brief UK, 2026-08-27](https://itbrief.co.uk/story/gartner-sees-securing-ai-market-hit-usd-4-8bn-in-2027). That is about 1.1% of Gartner's 2026 total and 1.7% of 2027 (my calculation).
- **IDC:**
  - $310.42B in 2026, +13.2% (Worldwide Security Spending Guide V2) — [IDC blog, 2026-10-28](https://www.idc.com/resource-center/blog/security-budgets-are-up-ceos-still-rank-it-their-top-tech-risk/) (primary)
  - Earlier: $308B for 2026 (press release of 2026-03-03, via the blog). 2027 $361.9B (+12.4%) and 2030 $512.9B from an undated IDC event page — [Software Strategies Blog](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/) [secondary]
  - IDC's scope includes hardware: 38 technology markets and 28 industries.
- **IDC buyer surveys:**
  - February 2026 CEO Survey (n=492): cybersecurity is the top-ranked anticipated technology risk, and 50% of CEOs name advanced cybersecurity a top-three investment area for the next 12–24 months.
  - March 2026 endpoint survey (n=846): more than 60% raised 2026 endpoint budgets.
  - Source: [IDC blog, 2026-10-28](https://www.idc.com/resource-center/blog/security-budgets-are-up-ceos-still-rank-it-their-top-tech-risk/)
- **Omdia:** $315B in 2026 (+13%), about one-third technology and two-thirds services (channel analysis, 2026-10-01); $311B in June 2026 [secondary] — [Software Strategies Blog](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/)
- **Canalys:** no figures were retrieved.
- **Forrester:**
  - 82% of technology decision-makers expect budget increases in 2027, after a "year of more cautious spending"; more than 2,600 decision-makers surveyed — [Forrester press release, 2026-07-15](https://www.forrester.com/press-newsroom/forresters-2027-budget-planning-guides/)
  - Security-specific shares (secondary, citing the Budget Planning Guide 2027 and IT Brief of 2026-07-17): 60% expect security budgets to rise at least 5% in 2027 (55% for 2026); 16% expect more than 10% (15%); 44% expect 5–10% (40%) — [Software Strategies Blog](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/)
- **Qi An Xin's chairman, citing IDC:** the US cybersecurity industry will exceed RMB 1 trillion in 2026, against about RMB 80bn in China; US security exceeds 15% of IT budgets against under 2% in China [company claim, unconfirmed] — [QAX IR record, 2026-11-02 call](https://data.eastmoney.com/notices/detail/688561/AN202611051831455238.html) [china_vendors.md]

#### 2026 CISO budget surveys
- **IANS Research and Artico Search, 2026 Security Budget Benchmark:**
  - Average budget growth 5% in 2026.
  - 45% reported no increase and 10% a decrease, so about 45% increased; the article's "only 45% saw budgets increase" is consistent with that.
  - 64% expect an increase in 2027.
  - 69% name AI for security their top priority for new budget.
  - 69% do not expect AI to reduce security headcount, and 81% expect AI to create demand for new roles.
  - Source: [TechTarget, 2026-09-16](https://www.techtarget.com/cybersecurity/news/366650512/Cyber-budgets-flatline-as-CISOs-shift-new-spending-to-AI)
  - From a search-result summary only: average 4% in 2025, the median flat for a second straight year, and 8% expecting a 2027 cut — [IANS blog](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/29/large-enterprise-cisos-face-budget-and-expectations-disconnect); [Infosecurity Magazine](https://www.infosecurity-magazine.com/news/ai-top-priority-new-spend-cyber/)
- **Absolute Security (1,001 CISOs, US and UK):** 60% say board pressure to adopt AI outpaces their ability to secure it; 83% are piloting or running agentic AI in security operations — [TechTarget, 2026-09-16](https://www.techtarget.com/cybersecurity/news/366650512/Cyber-budgets-flatline-as-CISOs-shift-new-spending-to-AI)
- **Breach-driven budget jumps in Korea:**
  - KB Kookmin plans a 2027 security budget above KRW 100bn, against KRW 86.1bn in 2026 (more than +16%) — [Korea JoongAng Daily, 2026-10-11](https://www.koreajoongangdaily.com/business/banks-boost-defenses-after-ailinked-hacks/12913975)
  - The three carriers spent KRW 367.5bn in 2025 (+22%) — [Korea Times, 2026-07-13](https://www.koreatimes.co.kr/business/tech-science/20260713/telecoms-step-up-cybersecurity-spending-after-breaches) [japan_korea_taiwan.md]

#### How security spending behaved in past slowdowns
- **2008–09:**
  - Gartner said the worldwide security software market grew "over 18%" in 2008 and "defied the economic gloom". Analyst Ruggero Contu said budget restrictions forced security leaders to prove value, which slowed sales cycles — [techpartner.news, 2009-06-23](https://www.techpartner.news/news/security-software-market-ignores-the-recession-148317)
  - The 2008 base conflicts: $11.3bn in that article, against $13.5bn (+18.6% from $11.3bn) in other coverage summarised by search — [internetnews (title only)](https://internetnews.com/security/security-software-revs-grew-19-in-2008)
  - For 2009, Gartner put security software revenue at $14.8bn, with growth slowing to about 7% (search-result summary; page returned 403, unverified) — [Deccan Herald](https://www.deccanherald.com/business/global-security-software-revenue-cross-2507213). Gartner's 2009 forecasts were about 8–9% (search-result summary).
- **2022–23:**
  - Gartner (2023-09-28) put 2023 security and risk management spending at about $188.1B and forecast $215B for 2024 (+14.3%), with security services about $90B (+11%). The primary page returned 403; figures are from a search summary of it and of secondary coverage — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2023-09-28-gartner-forecasts-global-security-and-risk-management-spending-to-grow-14-percent-in-2024); [ITnews](https://www.itnews.com.au/news/worldwide-spending-on-risk-management-to-hit-us215-bn-in-2024-gartner-600860)
  - Listed US vendors kept growing while their multiples fell (StockAnalysis annual data) — [us_platforms_panw_crwd_zs_s.md]; [StockAnalysis CRWD](https://stockanalysis.com/stocks/crwd/financials/ratios/):
    - CrowdStrike: revenue growth 66.0% (FY22), 54.4% (FY23), 36.3% (FY24). Market cap −39% from Jan 2022 to Jan 2023; EV/Sales 25.8x → 9.8x.
    - Zscaler: 62.1% → 48.2% → 34.1%.
    - Palo Alto Networks: 29.3% → 25.3% → 16.5%; market cap +54% from Jul 2022 to Jul 2023.
    - SentinelOne: 120.1% → 106.1% → 47.1%; market cap −64%.
- **China's 2023–25 downturn:**
  - Combined revenue of eight listed specialists fell from RMB 27.5bn (2023) to RMB 24.2bn (2025).
  - The group lost about RMB 1.5–1.9bn a year in 2024–25, and payrolls shrank by roughly a sixth.
  - Qi An Xin cites price competition and the first-year planning phase of the 15th Five-Year Plan.
  - Source: [Eastmoney filings data](https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22688561%22)) [china_vendors.md]

#### Q3 2026 growth across listed vendors worldwide (consolidated from the notes; year-on-year revenue unless stated)
| Region | Company (period; release date) | Growth | Note | Source |
|---|---|---|---|---|
| US | Palo Alto Networks (Q4 FY26 to 31 Jul; 2026-09-01) | +34% | includes CyberArk and Chronosphere; FY27 guide +23–24% | [SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000019/ex991q426earningsrelease.htm) |
| US | CrowdStrike (Q2 FY27 to 31 Jul; 2026-08-26) | +26% | ARR +25%; net new ARR +51% | [SEC](https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm) |
| US | Zscaler (Q4 FY26 to 31 Jul; 2026-09-03) | +25% | FY26 +20% excluding Red Canary; FY27 guide ~17% | [SEC](https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm) |
| US | SentinelOne (Q2 FY27 to 31 Jul; 2026-08-27) | +21% | ARR +22% | [Release PDF](https://s28.q4cdn.com/399982429/files/doc_financials/2027/q2/SentinelOne-Q2-27-Earnings-Press-Release.pdf) |
| US | Fortinet (Q3 to 30 Sep; 2026-10-28) | +20.5% | product +36.8%; billings +29%, of which price rises ~10 points [company claim, unconfirmed] | [SEC](https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000024/ftntq3-2026ex991.htm) |
| US | JFrog (Q3 to 30 Sep; 2026-11-05) | +31% | cloud +60% | [SEC](https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm) |
| US | GitLab (Q2 FY27 to 31 Jul; 2026-09-01) | +21% | | [Release PDF](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf) |
| US | Cisco security (Q4 FY26 to 25 Jul; 2026-08-12) | +14% (FY26 +2%) | 13% of Cisco revenue | [SEC](https://www.sec.gov/Archives/edgar/data/858877/000085887726000106/exhibit991pressrelease-q4f.htm) |
| US | Qualys (Q3; 2026-11-09) | +11% | | [SEC](https://www.sec.gov/Archives/edgar/data/0001107843/000110784326000043/qlys-20261109xex991.htm) |
| US | Tenable (Q3; 2026-10-28) | +9.5% | | [SEC](https://www.sec.gov/Archives/edgar/data/0001660280/000166028026000050/q32026financialresults-ear.htm) |
| US | Rapid7 (Q3; 2026-11-04) | −2.5% | ARR −2.2% | [SEC](https://www.sec.gov/Archives/edgar/data/0001560327/000156032726000049/q32026rapid78-kex991.htm) |
| Israel | Check Point (Q3; 2026-11-02) | −1.1% | products −19.1%; CEO: "revenues reached a trough" | [Results PDF](https://www.checkpoint.com/downloads/investor/check-point-software-third-quarter-2026-financial-results.pdf?v=1.2) |
| Japan | Trend Micro (Q3 to 30 Sep; 2026-11-12) | +9% reported, +3% constant currency | TrendAI ARR +8% | [Q3 deck](https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf) |
| Korea | AhnLab (Q3, preliminary; 2026-10-28) | +23.1% | 9M +14.0% | [MTN](https://news.mtn.co.kr/article/2026102810354690595) |
| China | Sangfor (Q3; 2026-10-29) | +31.4% | driven by server and component price rises in cloud | [Eastmoney](https://data.eastmoney.com/notices/detail/300454/AN202610281831103091.html) |
| China | Venustech (Q3; 2026-10-30) | +21.0% | China Mobile-driven | [Eastmoney](https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22002439%22)) |
| China | NSFOCUS (Q3; 2026-10-30) | +1.3% | | [china_vendors.md] |
| China | 360 Security (Q3; 2026-10-30) | −3.9% | | [china_vendors.md] |
| China | DBAPPSecurity (Q3; 2026-10-28) | −8.0% | | [china_vendors.md] |
| China | Topsec (Q3; 2026-10-29) | −18.9% | | [china_vendors.md] |
| China | Qi An Xin (Q3; 2026-10-31) | −29.8% | 9M −20.2% | [Eastmoney](https://data.eastmoney.com/notices/detail/688561/AN202610301831226150.html) |
| Europe | Yubico (Q3; 2026-11-05) | +29.3% (organic +28.3%) | | [MFN](https://mfn.se/a/yubico/interim-report-july-september-2026) |
| Europe | secunet (Q3; 2026-11-12) | +19.5% | Q3 order intake −31.2% | [secunet PDF](https://www.secunet.com/fileadmin/user_upload/02_Downloads/IR/Finanzpublikationen/2026/Q3/26_11_12_Q3_Bericht_de_v3.pdf) |
| Europe | F-Secure (Q3; 2026-10-28) | +12.2% | | [Placera](https://www.placera.se/pressmeddelanden/f-secure-f-secure-interim-report-1-january-30-september-2026-accelerated-growth-driven-by-embedded-security-20261028) |
| Europe | Wallix (H1 2026; 2026-07-16) | +14.2% | | [AMF](https://echanges.dila.gouv.fr/OPENDATA/AMF/ACT/2026/07/FCACT080594_20260716.pdf) |
| Europe | NCC Group Cyber (FY to 30 Sep; 2026-10-27) | +3.7% constant currency | services-heavy | [HL/Sharecast](https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations) |
| India | Quick Heal (Q2 FY27, Jul–Sep; 2026-10-27/28) | −22% | aggregator figures | [Sahi](https://www.sahi.com/news/quick-heal-technologies-reports-q2-net-profit-of-5-8-crore-versus-7-9-crore-yoy) |

The four large US platforms report July quarters; their October quarters are due 18 Nov to about 3 Dec 2026 — [us_platforms_panw_crwd_zs_s.md]. Sources for rows marked with a notes file are in that file.

#### Are cheap models enough for attackers?
- **ARTEX:** operators mostly used DeepSeek and Kimi, switching away from an Anthropic model when its guardrails triggered — [CPR, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/)
- **FortiGate campaign:** a low-to-medium-skill actor built with commercial generative AI a toolkit that "would normally require a much larger team" — [AWS, 2026-02-20](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/)
- **TuxBot:** a single developer built a multi-architecture botnet with LLM help — [Unit 42, 2026-07-15](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/)
- **Open-weight models:** four to eight months behind at about a hundredth of the cost per task, with safeguards largely ineffective — [CSA, 2026-07-31](https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/); [NIST CAISI, 2026-05-01](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
- **Counter-evidence: the hardest tasks still need frontier models:**
  - Kimi K3 achieved 0 of 41 full compromises, against about 20 of 41 for the best models; GLM-5.3 scored 9.4% against 44.4% on ExploitGym — [CASRAI](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments)
  - The state-sponsored campaign Anthropic disrupted used a frontier tool (Claude Code) — [Anthropic, 2025-11-13](https://www.anthropic.com/news/disrupting-AI-espionage)

#### AI-linked exposures inside security revenue (from the notes)
- **Palo Alto Networks:** the FY27 outlook includes a "nine-figure" benefit from a large LLM customer migrating to Chronosphere, assumed to run only through Q1 — [GuruFocus](https://www.gurufocus.com/news/9063501/palo-alto-networks-inc-panw-q4-2026-earnings-call-highlights-record-rpo-surpasses-20-billion-ngs-arr-soars-63) [us_platforms_panw_crwd_zs_s.md]
- **Memory-chip shortage from the AI build-out:**
  - Fortinet raised prices and its product gross margin fell from 67.7% to 64.4% — [Fortinet 10-Q](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000027/ftnt-20260930.htm)
  - Check Point lost about 1 point of gross margin in 2026 and expects similar in 2027 — [Motley Fool transcript, 2026-11-02](https://www.fool.com/earnings/call-transcripts/2026/11/02/check-point-chkp-q3-2026-earnings-call-transcript/)
  - Zscaler bought data-centre equipment ahead of memory price rises (Q4 capex 22% of revenue) — [ZS release](https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm)
  - Notes files: [fortinet_checkpoint_exposure_mgmt.md; us_platforms_panw_crwd_zs_s.md]
- **Fortinet's refresh cycle:** Jefferies says Q3 benefited from a pull-forward that could weigh around mid-2027 — [Investing.com, 2026-10-29](https://www.investing.com/news/stock-market-news/fortinet-earnings-analysis-questions-answered-and-next-catalysts-93CH-4984773)
- **The review framework's scenario B:** a financing-led AI pause around 2028, weighted at about 25%. By analogy with 2022–23, the notes expect security spending to decelerate but stay positive, with the largest de-rating on the richest multiples [us_platforms_panw_crwd_zs_s.md; fortinet_checkpoint_exposure_mgmt.md]
- **Market reaction:**
  - Security stocks sold off on model-maker security launches, then recovered. From 7 Apr to 18 Sep 2026: Okta +130.7%, Fortinet +102%, Zscaler +40%.
  - An 8–11% one-day fall around GPT-6 Cyber (5 Nov 2026) was attributed to a wider AI-trade unwind.
  - Source: [BankInfoSecurity, 2026-09-18](https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191) [model_makers_gated_access.md]

### Inferences
- **The mechanism is supported for opportunistic and criminal attacks.** Attackers already run on cheap or open models (ARTEX, the FortiGate campaign) and the capability lag is months. An AI-capex pause would not remove attacker capability, which supports continued defence demand.
- **The mechanism is weaker for the hardest attacks.** Frontier models still lead on long attack chains, so a pause that slows frontier progress would also slow the top end of offence.
- **Demand resilience has precedent, but it is not uniform:**
  - Security grew through 2009 (decelerating to single digits on secondary evidence) and through 2022–23.
  - China shows security demand can shrink when the main payer (government and state-owned firms) cuts.
  - IANS shows the median CISO budget flat for two years even as forecasters project 11–13% growth. Market growth is concentrated: price rises, large platforms, AI-linked projects.
- **An AI-specific pause would hit AI-linked lines first:** PANW's LLM-customer revenue, Zscaler's AI-linked upsells, and securing-AI products (about 1–2% of total spending per Gartner). It would also unwind the 2026 memory-price tailwind that lifted hardware revenue at Fortinet and Sangfor, while easing their component costs. The direct revenue at risk looks small relative to the total; the bigger risk is valuation multiples, as in 2022–23.
- **Contradiction with the prior's wording:** "security demand holds" is too strong as stated. The 2026 data already show dispersion from −30% to +34%, a flat median budget, and a services and legacy tail that is shrinking (Rapid7, Check Point products, Quick Heal) without any pause.

### Gaps
- Gartner's own 3Q26 press release and its exact date were not retrieved; all Gartner totals come from a secondary blog citing a report ID. Canalys figures were not found. IDC's 2027 and 2030 figures come from an undated event page via the same blog.
- The 2009 actual (about 7%, $14.8bn) is unverified (403). No 2001–02 or 2020 comparisons were gathered.
- The full IANS report (median, sample size) was not read. Wing VC and Evanta surveys were not found. Forrester's security-specific shares are secondary.
- No spending data split by AI-linked versus non-AI-linked demand. Taiwan's listed vendors and Israeli listed vendors other than Check Point are not in the growth table.

## 5. Consolidation: evidence register for the priors and the open question, verdict table, and dated sources

### Takeaway
None of the three priors is cleanly supported:
- **P1 (60%):** partly supported — precursors exist; no attributed mass device compromise.
- **P2 (35%):** partly supported — its second leg fits every forecast; its first leg, human rates falling first, is contradicted so far for day rates.
- **P3:** partly supported — the attacker-side mechanism holds for opportunistic attacks; resilience is uneven; no pause has occurred to test it.

On the open question, discovery has clearly outrun repair: patched shares are 6–8%, and the unpatched backlog grew 3.8x between late May and early October 2026. But exploitation has not yet surged with discovery: KEV additions +36% against CVEs +136%, and AI-found flaws are exploited at baseline rates. The net balance therefore cannot be measured. In the short run the evidence leans toward attackers gaining at least as much as defenders, unless repair is automated. Gated frontier access sits mainly with Palo Alto Networks and CrowdStrike (all three programmes) and Cisco (two), plus a thin, conditional non-US layer.

### Cited Findings

#### Evidence register (one line per item; direction relative to each prior)
| # | Item (date) | Bears on | Direction | Source | Notes file |
|---|---|---|---|---|---|
| 1 | NVD CVEs 96,496 in 2026 to 11 Nov vs 48,150 in 2025 | Open question; P2 | discovery ↑↑; find-and-patch work rising | [NVD API](https://services.nvd.nist.gov/rest/json/cves/2.0) | this file |
| 2 | KEV additions 295 vs 217 (to 10 Nov, +36%); KEV/CVE 0.31% | Open question; P1 | exploitation not scaling with discovery | [CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | this file |
| 3 | Mean TTE 63 → 5 → −7 days (2018–19 → 2023 → 2025) | Open question | faster exploitation, predates gated AI | [Mandiant 2024-10-15](https://cloud.google.com/blog/topics/threat-intelligence/time-to-exploit-trends-2023); [M-Trends 2026-03-23](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026) | this file |
| 4 | Exploited on or before publication day 28.93% (2025) → 23.43% (1H-2026); median time to KEV 120 → 80 days | Open question | mixed | [VulnCheck 2026-07-28](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026) | this file |
| 5 | AI-found flaws: 14 of 1,061 exploited (1.3%); Glasswing 1 of 126 CVEs exploited | P1; open question | against an AI-driven exploitation surge | [VulnCheck](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026) | this file |
| 6 | Glasswing patched share 6.1% (22 May) → 8.4% (2 Oct); backlog 1,499 → 5,641 | Open question | repair is the bottleneck | [CSA](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity); [SIG](https://www.softwareimprovementgroup.com/blog/mythos-project-glasswing-security/) | model_makers; fortinet_checkpoint |
| 7 | OpenAI kernel scan: 61 of 948 patched (c. 4 Nov 2026) [company claim] | Open question | repair bottleneck | [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145) | model_makers |
| 8 | Open-weight lag 4–8 months, ~1/100 cost; hardest tasks still trail (0/41 vs ~20/41) | P3; open question | cheap models suffice for narrow tasks, not the hardest | [CSA 2026-07-31](https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/); [CAISI](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro); [CASRAI](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments) | model_makers |
| 9 | ARTEX operators used DeepSeek/Kimi (2026-11-05) | P3 | for | [CPR](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/) | fortinet_checkpoint |
| 10 | Anthropic AI-orchestrated espionage, ~30 targets, few breached (2025-11-13) | P1 | precursor (organisations, not devices) | [Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage) | ot_iot |
| 11 | Amazon: 600+ FortiGates, 55+ countries, AI-augmented, no exploit (2026-02-20) | P1; P3 | precursor; against "AI-built exploits"; for cheap-model sufficiency | [AWS](https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/) | this file |
| 12 | Unit 42 TuxBot v3: LLM-written IoT botnet with exploit modules for known CVEs, ~70% functional, no infection count (2026-07-15) | P1 | closest precursor | [Unit 42](https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/) | this file |
| 13 | Korean bank hacks "reportedly" AI-linked; no official attribution (Oct 2026) | P1; P3 | not devices; budgets up | [JoongAng Daily](https://www.koreajoongangdaily.com/business/banks-boost-defenses-after-ailinked-hacks/12913975) | japan_korea_taiwan |
| 14 | M-Trends: 2025 not "the year where breaches were the direct result of AI" | P1 | against | [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026) | this file |
| 15 | BADBOX 2.0 millions of devices (2025-06-05); router botnets from end-of-life devices | P1 | mass device compromise happens without AI | [FBI IC3](https://www.ic3.gov/PSA/2025/PSA250605); [THN](https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html) | ot_iot |
| 16 | CISA KEV consumer-device additions 19 (2025) → 6 (2026 YTD) | P1 | against an imminent surge (weak) | [CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | this file |
| 17 | UK pentest contract median £550 → £590; 90th percentile £675 → £775; ads 248 → 274 (to 12 Nov 2026) | P2 | against "rates fall first" | [ITJobsWatch](https://www.itjobswatch.co.uk/contracts/uk/penetration%20testing.do) | this file |
| 18 | G-Cloud median £1,000/day vs autonomous tiers ~$3,000/yr (2026) | P2 | for (low-end substitution) | [Stingrai](https://www.stingrai.io/blog/penetration-testing-price-index-2026) | this file |
| 19 | NCC Technical Assurance +0.2% cc (H1 FY26); NA −11.3% from large tech clients | P2 | volume pressure, not price cuts | [NCC interims](https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf) | ai_discovery |
| 20 | Internet Bug Bounty −76% to −89%; curl, Nextcloud, Google OSS VRP closed or paused; Chrome base $500 | P2 | for (routine-finding prices falling) | [The Register](https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458); [ForkLog](https://forklog.com/en/the-end-of-bug-bounties/); [Malwarebytes](https://www.malwarebytes.com/blog/news/2026/10/google-pauses-open-source-bug-bounty-program-after-rise-in-ai-submissions) | ai_discovery |
| 21 | HackerOne payouts $89.1M (FY to Jun 2026), +26% in H1 2026 [company claim] | P2 | against a broad price fall | [HackerOne](https://www.hackerone.com/report); [Help Net Security](https://www.helpnetsecurity.com/?p=389850) | ai_discovery |
| 22 | Android memory-safety share <20% (2025); KEV memory-safety share 32.7% → 14.0% (2022 → 2026) | P2 | for (class shrinking as a share) | [Google](https://blog.google/security/rust-in-android-move-fast-fix-things/); [CISA KEV](https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json) | this file |
| 23 | CryptoProver proof for $467 in 11.4h vs 15 person-months (Aug–Oct 2026) | P2 | for (mechanism) | [arXiv](https://arxiv.org/abs/2608.00965) | code_supply_chain |
| 24 | 13 vulnerabilities escaped verified crypto libraries (ePrint 2026/192) | P2 | against (verification moves bugs to the boundary) | [IACR](https://eprint.iacr.org/2026/192) | code_supply_chain |
| 25 | Gartner 2026 $247.5B (+13.6%), 2027 $276.1B (+11.6%), CAGR 10.8% to 2030 | P2; P3 | for (no shrink; demand growing) | [Software Strategies Blog](https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/) | this file |
| 26 | IDC 2026 $310.42B (+13.2%) | P3 | for | [IDC](https://www.idc.com/resource-center/blog/security-budgets-are-up-ceos-still-rank-it-their-top-tech-risk/) | this file |
| 27 | IANS 2026: average +5%, 45% flat, 10% cut; 64% expect a 2027 increase | P3 | mixed | [TechTarget](https://www.techtarget.com/cybersecurity/news/366650512/Cyber-budgets-flatline-as-CISOs-shift-new-spending-to-AI) | this file |
| 28 | 2008 +18%; 2009 ~+7% (unverified); 2022–23 vendors +25–106% growth while multiples fell | P3 | for (resilience in slowdowns) | [techpartner.news](https://www.techpartner.news/news/security-software-market-ignores-the-recession-148317); [StockAnalysis](https://stockanalysis.com/stocks/crwd/financials/ratios/) | us_platforms |
| 29 | China listed specialists' revenue RMB 27.5bn → 24.2bn (2023 → 25) | P3 | against (demand fell in a budget squeeze) | [Eastmoney](https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22688561%22)) | china_vendors |
| 30 | Q3 2026 growth spread −30% to +34% across regions | P3 | resilience uneven | table in section 4 | all regional files |
| 31 | Memory-chip cost and price effects; PANW LLM customer; Fortinet pull-forward | P3 | 2026 growth partly AI-cycle-linked | [Fortinet 10-Q](https://www.sec.gov/Archives/edgar/data/1262039/000126203926000027/ftnt-20260930.htm); [GuruFocus](https://www.gurufocus.com/news/9063501/palo-alto-networks-inc-panw-q4-2026-earnings-call-highlights-record-rpo-surpasses-20-billion-ngs-arr-soars-63) | fortinet_checkpoint; us_platforms |
| 32 | Gated access: PANW and CRWD in all three programmes; Cisco in two; others as listed in section 1 | Open question | access concentrated | [Anthropic](https://www.anthropic.com/glasswing); [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); [DeepMind](https://deepmind.google/fairwind-program/) | model_makers |
| 33 | US Commerce directive cut all foreign-national Mythos 5/Fable 5 access, 12–30 Jun 2026 | Open question | non-US access contingent | [Tech Policy Press](https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/); [CNBC](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html) | model_makers |
| 34 | Model makers' statements: Anthropic "far outpace the efforts of defenders" (Apr 2026); Google "the defender's edge comes from shrinking the time between detecting a flaw and patching it" (Sep 2026); Microsoft "AI compresses the window" (Apr 2026) | Open question | companies concede near-term attacker gains | [Fortune](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/); [Google blog](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/); [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3) | model_makers |
| 35 | Defender wins: Mozilla patched 271 Firefox flaws found with Mythos Preview (21 Apr 2026); Google paid $250K for XBOW's AI-built Chrome chain (2026-10-13) | Open question | for defenders, where fixes close the loop | [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]; [CyberInsider](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/) | model_makers; ai_discovery |

### Inferences

#### Verdict table (as of 2026-11-12)
| Prior | Prior probability | Evidence for (dated) | Evidence against (dated) | Verdict | Key sources (dates) |
|---|---|---|---|---|---|
| **P1:** a mass compromise of consumer or industrial devices is attributed to AI-built exploits by end-2027 | 60% | LLM-written IoT botnet with exploit modules (Unit 42, 2026-07-15); AI-orchestrated espionage with AI-written exploit code (Anthropic, 2025-11-13); AI-augmented compromise of 600+ firewalls (Amazon, 2026-02-20); AI-found flaws now exploited (14 of 1,061; VulnCheck, 2026-07-28); open-weight exploit-writing at about $20 (claim, Sep 2026); labs warn of large-scale attacks in 2026 (Apr 2026) | No credible attribution of a mass device compromise to AI-built exploits as of 2026-11-12. Mandiant: 2025 not the year of AI-caused breaches (2026-03-23). The Amazon case used no exploit. TuxBot ~70% functional, known CVEs, no infection count. AI-found flaws exploited at baseline 1.3%. CISA consumer-device KEV additions fell (19 → 6). Large device compromises came from supply-chain malware and end-of-life devices (FBI, 2025-06-05; Apr 2026). | **Partly supported:** precursors observed; event not observed; 60% looks generous given attribution friction | Unit 42 2026-07-15; Anthropic 2025-11-13; AWS 2026-02-20; Google Cloud 2026-03-23; VulnCheck 2026-07-28; FBI IC3 2025-06-05; CISA KEV 2026-11-10 |
| **P2:** human pentest rates fall first; find-and-patch spending shrinks only after 2030, if verified software removes whole bug classes | 35% | No forecaster projects a shrink before 2030 (Gartner CAGR 10.8%; IDC 12.5%; Sep–Nov 2026). Memory-safety class shrinking as a share (Android <20%, 2025; KEV 32.7% → 14.0%). AI proofs far cheaper (CryptoProver, Aug–Oct 2026). Routine-finding prices falling (IBB cut May 2026; OSS bounty closures Jan–Oct 2026; Chrome base $500). Autonomous tests ~$3,000/yr (2026). | UK contractor day rates rose (median +7.3%, 90th percentile +14.8%, ads +10%; to 2026-11-12). NCC human assurance flat, not cut-price (Jun and Oct 2026). Total bounty payouts up (+26% H1 2026). CVEs doubled and backlogs grew (2026). Verified code still had 13 escapes (ePrint 2026/192). CRA mandates vulnerability handling (from Sep 2026 and Dec 2027). | **Partly supported:** the second leg is consistent with the data; the first leg is **contradicted so far** for day rates and supported only for bounty-priced routine work | ITJobsWatch 2026-11-12; Stingrai 2026-06-05; NCC 2026-06-11 and 2026-10-27; HackerOne 2026; The Register 2026-05-21; Google 2025-11-13; arXiv 2608.00965; IACR 2026/192; Software Strategies Blog 2026-11-09 |
| **P3:** security demand holds in an AI-spending pause, because cheap models are enough for attackers | none given | Forecasts +11–13% for 2026–27 (Gartner, IDC, Omdia; Aug–Nov 2026). 64% of CISOs expect 2027 increases (IANS, Sep 2026); 60% expect ≥5% security budget rises (Forrester via secondary, Jul 2026). Security grew through 2009 and 2022–23. Attackers already use cheap or open models (ARTEX 2026-11-05; Amazon 2026-02-20); open-weight lag 4–8 months at ~1/100 cost (Jul–Sep 2026). Breaches raise budgets (KB +16% for 2027). | No pause has occurred to test. Median CISO budget flat; 55% flat or down (IANS 2026). China's security revenue fell 2023–25 in a budget squeeze. Q3 2026 dispersion −30% to +34% (Check Point −1%, Rapid7 −2.5%, Trend Micro +3% cc, Quick Heal −22%). Part of 2026 growth is AI-cycle-linked (memory-driven prices, PANW's LLM customer). The hardest attacks still need frontier models (CAISI, Jul–Sep 2026). | **Partly supported:** mechanism supported for opportunistic attacks; "demand holds" too strong as a universal claim; cannot be tested directly | Software Strategies Blog 2026-11-09; IDC 2026-10-28; TechTarget 2026-09-16; techpartner.news 2009-06-23; CPR 2026-11-05; CSA 2026-07-31; Eastmoney filings Oct 2026; SEC filings Aug–Nov 2026 |
| **Open question:** do defenders or attackers gain more from the same models, and which vendors have gated access? | none given | **Attackers:** discovery outruns repair (patched 6.1% → 8.4%; backlog ×3.8, May–Oct 2026; kernel 6.4%); HackerOne critical backlog +123%; TTE −7 days (2025); open weights 4–8 months behind at ~1/100 cost; gate leakage (Apr 2026); labs concede attacker gains. **Defenders:** exploitation not scaling with discovery (KEV +36% vs CVE +136% YTD 2026); share exploited on or before publication day fell (28.93% → 23.43%); AI-found flaws exploited at baseline; months of gated lead; Mozilla's 271 fixes. | No independent net measurement exists. KEV is lagging and detection-limited. The CVE surge's AI share is unknown. | **Cannot assess the net effect.** Short-run lean: attackers gain at least as much, because repair capacity is the binding constraint; defenders gain where fixing is automated. **Access:** Palo Alto Networks and CrowdStrike (all three programmes); Cisco (Anthropic, OpenAI); Fortinet, Sophos, Akamai, Cloudflare, NCC Group, SpecterOps (OpenAI); Okta, Trend Micro, Booz Allen, Rubrik, HackerOne (Anthropic); Wiz, Menlo, Datadog, Snowflake (Google); Dragos (OpenAI evaluation partner); Check Point, Tenable unconfirmed; none found for Zscaler, SentinelOne, Rapid7, Qualys, Snyk, Socket, Bugcrowd or OT specialists; Chinese firms barred; Korean access disputed | VulnCheck 2026-07-28; CISA KEV 2026-11-10; NVD 2026-11-12; CSA 2026-06-07; SIG 2026-10-15; Help Net Security 2026-08-11; DeepMind 2026-11-12; Anthropic 2026-04-07 and 2026-11-09 |

#### Where the evidence plainly contradicts the background
- **P1:** the closest real "AI mass device" case, about 600 firewalls, used no exploit at all (Amazon). Mandiant says AI did not directly cause 2025's breaches.
- **P2:** UK human pentest day rates rose in 2026 rather than falling first.
- **P3:** security demand has already fallen in one large market (China, 2023–25), and the median CISO budget has been flat for two years without any AI pause.
- **Open question:** gated access is not a lasting defender monopoly. The lead is four to eight months, and the US government closed the gate to all non-US nationals for 18 days in June 2026.

### Gaps
- **Not verified this session:**
  - Gartner's own 3Q26 release (Gartner pages returned 403) and Gartner's 2009 actuals (Deccan Herald 403).
  - Dark Reading's coverage of Gartner's 2023 release (403).
  - The full IANS report.
  - Cyentia's 2026 State of Pentesting report.
  - CrowdStrike's reported attribution of the Korean bank attacks.
  - Infection counts for TuxBot.
  - Aisuru and Kimwolf sizes.
  - OT incidents in 2025–26.
  - LAC's post-delisting financials.
  - Indian IT services' cyber-practice revenue.
  - Any client-billing pentest rate series.
  - Canalys forecasts.
  - CVE.org metrics, used as a cross-check on the NVD counts.
  - FIRST EPSS.
  - Independent confirmation of Anthropic's Glasswing counts.
- **Search budget:** WebSearch worked; seven queries were used, plus direct fetches. Firecrawl and Exa were not used, per the session constraints.

#### Dated source list (all accessed 2026-11-12 unless stated; these are sources, placed here so the notes end with them)
**Primary data and primary pages fetched this session**
- CISA, Known Exploited Vulnerabilities catalogue JSON, version 2026.11.10 (released 2026-11-10): https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- NIST NVD, CVE API 2.0 (queried 2026-11-12): https://services.nvd.nist.gov/rest/json/cves/2.0
- VulnCheck, State of Exploitation 1H-2026 (2026-07-28): https://www.vulncheck.com/blog/state-of-exploitation-1h-2026
- Google Cloud / Mandiant, M-Trends 2026 (2026-03-23): https://cloud.google.com/blog/topics/threat-intelligence/m-trends-2026
- Google Cloud / Mandiant, Time-to-exploit trends 2023 (2024-10-15): https://cloud.google.com/blog/topics/threat-intelligence/time-to-exploit-trends-2023
- Google, Rust in Android: move fast and fix things (2025-11-13): https://blog.google/security/rust-in-android-move-fast-fix-things/
- AWS Security Blog, AI-augmented threat actor accesses FortiGate devices at scale (2026-02-20): https://aws.amazon.com/blogs/security/ai-augmented-threat-actor-accesses-fortigate-devices-at-scale/
- Palo Alto Networks Unit 42, TuxBot v3 Evolution (2026-07-15): https://unit42.paloaltonetworks.com/tuxbot-v3-evolution-iot-botnet/
- Security Affairs, TuxBot v3 (2026-07-16): https://securityaffairs.com/195486/ai/tuxbot-v3-the-iot-botnet-built-with-ai-bugs-disclaimers-and-all.html
- Anthropic, Disrupting the first reported AI-orchestrated cyber espionage campaign (2025-11-13): https://www.anthropic.com/news/disrupting-AI-espionage
- Korea JoongAng Daily, banks boost defences after AI-linked hacks (2026-10-11): https://www.koreajoongangdaily.com/business/banks-boost-defenses-after-ailinked-hacks/12913975
- ITJobsWatch, UK penetration testing contracts (data to 2026-11-12): https://www.itjobswatch.co.uk/contracts/uk/penetration%20testing.do
- Stingrai, Penetration Testing Price Index 2026 (2026-06-05; re-read 2026-10-23) [vendor]: https://www.stingrai.io/blog/penetration-testing-price-index-2026
- IDC, Security budgets are up… (2026-10-28): https://www.idc.com/resource-center/blog/security-budgets-are-up-ceos-still-rank-it-their-top-tech-risk/
- Forrester, 2027 Budget Planning Guides press release (2026-07-15): https://www.forrester.com/press-newsroom/forresters-2027-budget-planning-guides/
- IT Brief UK, Gartner securing-AI forecast (2026-08-27): https://itbrief.co.uk/story/gartner-sees-securing-ai-market-hit-usd-4-8bn-in-2027
- Software Strategies Blog, Cybersecurity spending forecasts 2027 compared (2026-11-09) [secondary]: https://softwarestrategiesblog.com/2026/11/09/cybersecurity-spending-forecasts-2027-compared-gartner-idc-forrester-omdia/
- TechTarget, Cyber budgets flatline as CISOs shift new spending to AI (2026-09-16): https://www.techtarget.com/cybersecurity/news/366650512/Cyber-budgets-flatline-as-CISOs-shift-new-spending-to-AI
- techpartner.news, Security software market ignores the recession (2009-06-23): https://www.techpartner.news/news/security-software-market-ignores-the-recession-148317
- LAC Co., Ltd. IR page (delisting 2025-02-25; accessed 2026-11-12): https://www.lac.co.jp/english/ir/

**Pages known only from search-result summaries or titles (not opened, or refused)**
- Gartner press release (2023-09-28; 403): https://www.gartner.com/en/newsroom/press-releases/2023-09-28-gartner-forecasts-global-security-and-risk-management-spending-to-grow-14-percent-in-2024
- ITnews, Gartner $215bn for 2024 (2023): https://www.itnews.com.au/news/worldwide-spending-on-risk-management-to-hit-us215-bn-in-2024-gartner-600860
- Deccan Herald, Gartner security software revenue (c. 2010; 403): https://www.deccanherald.com/business/global-security-software-revenue-cross-2507213
- internetnews, Security Software Revs Grew 19% in 2008 (title only): https://internetnews.com/security/security-software-revs-grew-19-in-2008
- OECD.AI incident entry (2026-07-15; title only): https://oecd.ai/en/incidents/2026-07-15-98ee
- Help Net Security, Mirai variants (2026-04-22): https://www.helpnetsecurity.com/2026/04/22/new-mirai-variants-target-routers-and-dvrs-via-old-flaws/
- IANS blog (2026-04-29): https://www.iansresearch.com/resources/all-blogs/post/security-blog/2026/04/29/large-enterprise-cisos-face-budget-and-expectations-disconnect
- Infosecurity Magazine on the IANS 2026 benchmark: https://www.infosecurity-magazine.com/news/ai-top-priority-new-spend-cyber/
- DeepStrike, pentest statistics (Pentera 2025 survey figure): https://deepstrike.io/blog/penetration-testing-statistics
- Stingrai, pentest cost per hour 2026 (Big Four bands): https://www.stingrai.io/blog/penetration-testing-cost-per-hour-2026
- AlgeriaTech post (conflicting TTE): https://algeriatech.news/?p=30026

**Key sources carried over from the notes files in this folder (publication dates as recorded there)**
- Cloud Security Alliance, Project Glasswing: AI discovery outpaces open-source patching capacity (released c. 2026-06-07): https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity
- The Hacker News, Claude Mythos finds 10,000 (2026-05-23): https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html
- Software Improvement Group, Mythos / Project Glasswing explainer (updated 2026-10-15): https://www.softwareimprovementgroup.com/blog/mythos-project-glasswing-security/
- Wikipedia, Claude Mythos (accessed 2026-11-12) [secondary]: https://en.wikipedia.org/wiki/Claude_Mythos
- Anthropic, Project Glasswing page (2026-04-07; updated 2026-10-06): https://www.anthropic.com/glasswing
- Anthropic, Claude Fable 5.2 and Mythos 5.2 (2026-11-09): https://www.anthropic.com/claude-fable-and-mythos-5-2
- Fortune, Mythos / Glasswing launch (2026-04-07): https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/
- TechCrunch, Glasswing expansion to 15 countries (2026-06-02): https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/
- Tech Policy Press, Commerce directive (2026-06-15): https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/
- CNBC, controls lifted (2026-06-30): https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html
- Unite.AI, CVP three tiers (Oct 2026): https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/
- Help Net Security, OpenAI Daybreak partners (2026-08-11): https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/
- TestingCatalog, GPT-6 Cyber (2026-11-05): https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/
- CyberScoop, GPT-6 Cyber (2026-11-05): https://cyberscoop.com/openai-gpt-6-cyber-security-model/
- Google DeepMind, Fairwind Program (read 2026-11-12): https://deepmind.google/fairwind-program/ ; Google blog (2026-09-02): https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- BankInfoSecurity, post-Mythos rally (2026-09-18): https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191
- Uravation, Hitachi and Trend Micro in Glasswing (Jun 2026): https://uravation.com/media/hitachi-trendmicro-claude-mythos-project-glasswing-japan-2026/
- HackerOne, Mythos integration (2026-09-21): https://www.hackerone.com/press-release/hackerone-bring-anthropics-mythos-exposure-management-lifecycle-discovery-verified
- The Elec, Korean Mythos access (2026-09-18): https://www.thelec.net/news/articleView.html?idxno=14029
- TechTimes, Japan's cyber chief on the US directive (2026-08-10): https://www.techtimes.com/articles/323705/20260810/japans-cyber-chief-confirms-us-ai-export-ban-hit-government-security-scanning.htm
- The Decoder, Anthropic ownership-based ban (Sep 2025): https://the-decoder.com/anthropic-bans-companies-majority-controlled-by-china-russia-iran-and-north-korea-from-claude/
- UK AISI, evaluation of Mythos Preview (2026-04-13): https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
- NIST CAISI, DeepSeek V4 Pro (2026-05-01): https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
- CASRAI, guide to CAISI open-weight assessments [secondary]: https://casrai.org/guides/caisi-open-weight-model-cyber-assessments
- CSA research note, open-weight cyber capability gap (2026-07-31): https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/
- Notebookcheck, GLM-5.3 exploit cost (2026-10-01): https://www.notebookcheck.net/GLM-5-3-China-s-open-AI-model-built-a-Chrome-exploit-for-20.1413141.0.html
- Insurance Journal (Reuters), 360 Tulongfeng (2026-06-26): https://www.insurancejournal.com/news/international/2026/06/26/875418.htm
- iTnews, OpenAI kernel report (Nov 2026): https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145
- Check Point Research, ARTEX (2026-11-05): https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/
- FBI IC3, BADBOX 2.0 PSA (2025-06-05): https://www.ic3.gov/PSA/2025/PSA250605
- The Hacker News, TP-Link suits (Oct 2026): https://thehackernews.com/2026/10/tp-link-sued-by-four-more-us-states.html
- Japan Times, South Korea bank hacks (2026-10-06; paywalled): https://www.japantimes.co.jp/business/2026/10/06/south-korea-bank-hacks/
- Shattered.io (low reliability; Oct 2026): https://shattered.io/crowdstrike-artex-ai-agent-korea-bank-hack-2026/
- Korea Times, telecom security spending (2026-07-13): https://www.koreatimes.co.kr/business/tech-science/20260713/telecoms-step-up-cybersecurity-spending-after-breaches
- The IT Nerd, Finite State raise (2026-11-10): https://itnerd.blog/2026/11/10/finite-state-raises-27-million-to-help-device-makers-fight-the-vulnpocalypse-with-ai-powered-product-security/
- HackerOne report (2026): https://www.hackerone.com/report ; HackerOne press release (Oct 2025): https://www.hackerone.com/press-release/hackerone-report-finds-210-spike-ai-vulnerability-reports-amid-rise-ai-autonomy
- Help Net Security, HackerOne CEO (2026-11-03): https://www.helpnetsecurity.com/?p=389850
- The CyberSec Guru, HackerOne platform data: https://thecybersecguru.com/analysis/what-happened-to-hackerone/
- The Register, Internet Bug Bounty cut (2026-05-21): https://theregister.com/security/2026/05/21/hackerone-takes-an-axe-to-its-bug-bounty-rewards/5244458
- LavX, Internet Bug Bounty cut (2026-05-21): https://news.lavx.hu/article/hackerone-cuts-internet-bug-bounty-payouts-by-over-75-percent-amid-ai-driven-reporting-surge
- Hackaday, curl ends its bounty (2026-01-26): https://hackaday.com/2026/01/26/the-curl-project-drops-bug-bounties-due-to-ai-slop
- ForkLog, The end of bug bounties (2026-07-24): https://forklog.com/en/the-end-of-bug-bounties/
- Malwarebytes, Google OSS VRP pause (Oct 2026): https://www.malwarebytes.com/blog/news/2026/10/google-pauses-open-source-bug-bounty-program-after-rise-in-ai-submissions
- SecurityWeek, Will AI kill the bug bounty industry (2026-06-09): https://www.securityweek.com/will-ai-kill-the-bug-bounty-industry/
- CyberInsider, XBOW Chrome bounty: https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/
- XBOW news (2026-10-13): https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users
- Trail of Bits, Patch the Planet (2026-06-22): https://blog.trailofbits.com/2026/06/22/introducing-patch-the-planet/
- NCC Group H1 FY26 interims (2026-06-11): https://www.directorstalkinterviews.com/wp-content/uploads/2026/06/ncc-interims-h1-fy26-110626.pdf ; HL/Sharecast trading update (2026-10-27): https://www.hl.co.uk/shares/stock-market-news/company--news/ncc-names-new-ceo-as-annual-earnings-beat-expectations
- Horizon3 press release: https://horizon3.ai/news/press-release/horizon3-raises-250m-series-e-at-2b-valuation-to-lead-the-ai-vs-ai-cybersecurity-era/ ; Calcalist (Pentera, 2025-03-12): https://www.calcalistech.com/ctechnews/article/ryvxvby21x ; IT Brief (Synack Sara): https://itbrief.co.nz/story/synack-launches-sara-ai-pentesting-for-wider-coverage
- Synack/Omdia release (Mar 2026): https://www.bolsamania.com/nota-de-prensa/mercados/95-of-enterprises-prioritize-pentesting-yet-only-32-of-attack-surfaces-are-tested-new-synack-and-omdia-research-finds--22105138.html ; ChannelLife (Cobalt/Omdia): https://channellife.news/story/cobalt-launches-autonomous-pentest-for-continuous-testing
- Analytics India Magazine, Indian IT and the labs (2026-05-07): https://analyticsindiamag.com/it-services/indian-its-biggest-ai-partners-are-its-newest-enterprise-threats
- arXiv 2608.00965, CryptoProver (v1 2026-08-02; v2 2026-10-16): https://arxiv.org/abs/2608.00965
- IACR ePrint 2026/192, Verification Theatre (revised 2026-06-25): https://eprint.iacr.org/2026/192
- Signal Shot (2026-04-20): https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/ ; GeekWire, AWS Kiro (May 2026): https://www.geekwire.com/2026/aws-targets-ai-slop-with-new-spec-check-in-kiro-coding-tool-amid-scrutiny-of-agent-reliability/ ; ChainCatcher, Certora AutoProver (Jul 2026): https://www.chaincatcher.com/en/article/2243764
- European Commission, Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Vendor results:
  - Palo Alto Networks 8-K (2026-09-01): https://www.sec.gov/Archives/edgar/data/0001327567/000132756726000019/ex991q426earningsrelease.htm
  - CrowdStrike (2026-08-26): https://www.sec.gov/Archives/edgar/data/1535527/000153552726000029/crwd-20260826xex991.htm
  - Zscaler (2026-09-03): https://www.sec.gov/Archives/edgar/data/0001713683/000171368326000156/zs-07312026_991.htm
  - SentinelOne (2026-08-27): https://s28.q4cdn.com/399982429/files/doc_financials/2027/q2/SentinelOne-Q2-27-Earnings-Press-Release.pdf
  - Fortinet (2026-10-28): https://www.sec.gov/Archives/edgar/data/0001262039/000126203926000024/ftntq3-2026ex991.htm ; Fortinet 10-Q (2026-10-30): https://www.sec.gov/Archives/edgar/data/1262039/000126203926000027/ftnt-20260930.htm
  - JFrog (2026-11-05): https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm
  - GitLab (2026-09-01): https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf
  - Cisco (2026-08-12): https://www.sec.gov/Archives/edgar/data/858877/000085887726000106/exhibit991pressrelease-q4f.htm
  - Qualys (2026-11-09): https://www.sec.gov/Archives/edgar/data/0001107843/000110784326000043/qlys-20261109xex991.htm
  - Tenable (2026-10-28): https://www.sec.gov/Archives/edgar/data/0001660280/000166028026000050/q32026financialresults-ear.htm
  - Rapid7 (2026-11-04): https://www.sec.gov/Archives/edgar/data/0001560327/000156032726000049/q32026rapid78-kex991.htm
  - Check Point (2026-11-02): https://www.checkpoint.com/downloads/investor/check-point-software-third-quarter-2026-financial-results.pdf?v=1.2
  - Trend Micro (2026-11-12): https://www.trendmicro.com/content/dam/trendmicro/global/en/about/investor-relations/reports-presentation/2026/financial-2026-presentation-negi-q3.pdf
  - AhnLab via MTN (2026-10-28): https://news.mtn.co.kr/article/2026102810354690595
  - Qi An Xin (2026-10-31): https://data.eastmoney.com/notices/detail/688561/AN202610301831226150.html
  - Sangfor (2026-10-29): https://data.eastmoney.com/notices/detail/300454/AN202610281831103091.html
  - Yubico (2026-11-05): https://mfn.se/a/yubico/interim-report-july-september-2026
  - secunet (2026-11-12): https://www.secunet.com/fileadmin/user_upload/02_Downloads/IR/Finanzpublikationen/2026/Q3/26_11_12_Q3_Bericht_de_v3.pdf
  - F-Secure (2026-10-28): https://www.placera.se/pressmeddelanden/f-secure-f-secure-interim-report-1-january-30-september-2026-accelerated-growth-driven-by-embedded-security-20261028
  - Wallix AMF filing (2026-07-16): https://echanges.dila.gouv.fr/OPENDATA/AMF/ACT/2026/07/FCACT080594_20260716.pdf
  - Quick Heal via Sahi (2026-10-28): https://www.sahi.com/news/quick-heal-technologies-reports-q2-net-profit-of-5-8-crore-versus-7-9-crore-yoy
- Market and analyst context:
  - GuruFocus, PANW Q4 FY26 call: https://www.gurufocus.com/news/9063501/palo-alto-networks-inc-panw-q4-2026-earnings-call-highlights-record-rpo-surpasses-20-billion-ngs-arr-soars-63
  - Investing.com, Fortinet analysis (2026-10-29): https://www.investing.com/news/stock-market-news/fortinet-earnings-analysis-questions-answered-and-next-catalysts-93CH-4984773
  - Motley Fool, Check Point Q3 2026 transcript (2026-11-02): https://www.fool.com/earnings/call-transcripts/2026/11/02/check-point-chkp-q3-2026-earnings-call-transcript/
  - StockAnalysis, CRWD ratios: https://stockanalysis.com/stocks/crwd/financials/ratios/
  - Eastmoney results data (China): https://datacenter-web.eastmoney.com/api/data/v1/get?reportName=RPT_LICO_FN_CPD&columns=ALL&filter=(SECURITY_CODE%3D%22688561%22)
  - QAX IR record (2026-11-02 call): https://data.eastmoney.com/notices/detail/688561/AN202611051831455238.html
  - Microsoft FY26 Q3 (2026-04-29): https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3

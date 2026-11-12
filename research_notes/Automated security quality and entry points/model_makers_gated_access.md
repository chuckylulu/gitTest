# Frontier model makers as suppliers to and competitors of security vendors: security programmes, gated cyber models and who has access (research date 2026-11-12)

Evidence tags used below: **[company claim, unconfirmed]** = stated by the company (or its partner) and not confirmed by any outside party found; **[secondary]** = from a secondary or aggregator page; **[extract only]** = taken from a search-result extract because the page itself returned HTTP 403/402 or a paywall; **[lead, not re-verified]** = from the earlier internal notes, not re-opened in this session. Web search ran out part-way through this session (shared budget), so later checks were done only by fetching URLs already found; several primary OpenAI pages (openai.com) returned HTTP 403 and are cited through secondary coverage. Business facts only; no exploit detail is reproduced.

---

## 1. OpenAI: Aardvark/Codex Security, Trusted Access for Cyber and Daybreak, gated cyber models, partners, acquisitions, the Linux kernel report, ownership and IPO

### Takeaway
OpenAI runs the most elaborate tiered access system of any lab: Trusted Access for Cyber (pilot, 5 Feb 2026) grew into "Daybreak" with a defensive Blue tier, an offensive-style Red tier and a Cyber Partner Program (expanded 10 Aug 2026) whose 16 named partners include Palo Alto Networks (Unit 42), CrowdStrike, Cisco, Sophos, Akamai, Fortinet and Cloudflare; its fourth cyber-specific model of 2026, GPT-6 Cyber (5 Nov 2026), is rated "Critical" for cyber and is limited to selected Daybreak Red customers. Its own code-security product (Aardvark, 30 Oct 2025 → Codex Security, 6 Mar 2026 → Codex Security Cloud, 29 Sep 2026) is still a research preview with no separate price; no completed security acquisition was found; the 4 Nov 2026 kernel report's counts are unconfirmed by outsiders; OpenAI is private, with a 2027 IPO described as likely but not committed.

### Cited Findings

#### Aardvark → Codex Security (code security agent)
- 30 Oct 2025: Aardvark, "an agentic security researcher powered by GPT-5", entered private beta for select partners — [eesel, Codex Security Cloud explainer (n.d., c. Oct–Nov 2026)](https://www.eesel.ai/blog/codex-security-cloud) [secondary]
- 6 Mar 2026: renamed Codex Security and released as a research preview in Codex web for Pro, Enterprise, Business and Edu, free for the first month; July 2026: public CLI and TypeScript SDK under Apache-2.0; 29 Sep 2026 (DevDay): Codex Security Cloud plugin launched "with Daybreak Blue included" — [eesel](https://www.eesel.ai/blog/codex-security-cloud) [secondary, citing OpenAI docs]
- Status and price (as of Nov 2026): still a research preview with no general-availability commitment and no separate Codex Security price; scans draw on included Codex allowance and then ChatGPT credits. OpenAI's credit table reportedly lists Daybreak Blue at GPT-5.6 Sol rates (100 credits per million input tokens, 10 cached, 500 output) and Daybreak Red at 312.5 / 31.25 / 1,875. Plan eligibility conflicts across OpenAI pages (DevDay recap: Pro, Business, Enterprise, Edu; pricing matrix: Enterprise/Education only). Cloud connects only to GitHub — [eesel](https://www.eesel.ai/blog/codex-security-cloud); [beri.net (search extract)](https://www.beri.net/article/openai-codex-security-cloud-continuous-repo-scanning-token-billing-research-preview-vs-sast) [secondary]
- Results claimed: Aardvark found 92% of known and synthetic vulnerabilities in "golden" test repos; in the 30 days before the March launch beta scans covered >1.2M commits and produced 792 critical and 10,561 high-severity findings; false-positive rates fell >50%; 14 CVEs assigned from OpenAI's open-source work [company claim, unconfirmed] — [eesel](https://www.eesel.ai/blog/codex-security-cloud)
- 15 Apr 2026: Codex Security "has contributed to over 3,000 critical and high fixed vulnerabilities"; "Codex for Open Source has reached over 1,000 open-source projects with free security scanning" [company claim, unconfirmed] — [Help Net Security, 2026-04-15](https://www.helpnetsecurity.com/2026/04/15/openai-gpt-5-4-cyber/)

#### Trusted Access for Cyber (TAC) → Daybreak; the gated models
- 5 Feb 2026: OpenAI introduced Trusted Access for Cyber as a pilot — an identity- and trust-based framework; individuals verify at chatgpt.com/cyber, enterprises request team access via their OpenAI representative; $10M in API credits committed via the Cybersecurity Grant Program — [OpenAI (not opened)](https://openai.com/index/trusted-access-for-cyber/); [SC World](https://www.scworld.com/brief/openai-launches-trusted-access-for-cyber-initiative-to-bolster-ai-security) [extract only]
- 14–15 Apr 2026: expansion with GPT-5.4-Cyber, "a version of GPT-5.4 fine-tuned specifically for defensive cybersecurity work" with a lower refusal boundary and binary reverse-engineering, for customers in the highest TAC tiers; rollout starts with "vetted security vendors, organizations, and researchers"; programme scaling to "thousands of verified individual defenders and hundreds of teams" [company claim, unconfirmed]; no participants named — [Help Net Security, 2026-04-15](https://www.helpnetsecurity.com/2026/04/15/openai-gpt-5-4-cyber/)
- 10–11 Aug 2026 (Daybreak expansion): Daybreak Blue = frontier general models (incl. GPT-5.6 Sol) with safeguards for authorised defensive work, "positioned as the starting tier for most defenders"; Daybreak Red = "purpose-trained cybersecurity models" for vulnerability research, exploit validation and red teaming (GPT-5.6-Cyber); Daybreak Cyber Partner Program brings the models into partners' products, managed services and engagements; individual accounts must use hardware security keys from 1 Sep 2026; controls include identity verification, monitoring, approved-use restrictions and legal attestations — [Tahawul Tech, 2026-08-11](https://www.tahawultech.com/news/openai-expands-daybreak-cyber-programme-and-partner-network/); [Help Net Security, 2026-08-11](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/)
- Partner model: "Clients don't receive the models. Access stays with the approved partner"; safeguards vary by engagement (identity verification, testing scopes, logging, monitoring, human oversight) — [Help Net Security, 2026-08-11](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/)
- 5 Nov 2026: GPT-6 Cyber (GPT-6 Astra-based) available through the API and Codex to "select approved Daybreak Red customers", with wider Red access planned; GPT-5.6 Cyber now open to all Daybreak Red customers; Daybreak Blue alpha access to GPT-6 Astra widening; a Daybreak Red group for approved critical-infrastructure defenders is planned; access is subsidised through a $1 billion "Daybreak for Frontline Defenders" grant programme; rated "Critical for cybersecurity" under OpenAI's Preparedness Framework (up from High for GPT-5.6 Cyber); safeguards include cyber-specific monitoring, credential protections, IP allowlisting, sandboxing and human oversight; no price stated — [TestingCatalog, 2026-11-05](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/); [CyberScoop, 2026-11-05](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)
- GPT-6 Cyber is described as OpenAI's fourth cyber-specific model of 2026 (after GPT-5.4-Cyber, GPT-5.5-Cyber, GPT-5.6 Cyber) — [eSecurityPlanet via earlier notes](https://www.esecurityplanet.com/news/news-openai-gpt-6-cyber-security-benchmarks/) [lead, not re-verified]
- Claimed GPT-6 Cyber results: ExploitGym 48.5% vs 32.1% for GPT-5.6 Cyber; black-box web pentest recall 40.3% vs 32.0% for GPT-6 Astra; 81 previously unknown high-severity Firefox vulnerabilities; 304 critical findings disclosed to maintainers with candidate patches [company claim, unconfirmed except that Mozilla rated the Firefox findings high severity and began landing fixes] — [TestingCatalog, 2026-11-05](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/); CyberScoop found no outside verification of the performance claims — [CyberScoop](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)
- Data-use controversy (Nov 2026): OpenAI told members that Daybreak Blue session data from personal accounts would be used "to improve our models, including to help strengthen safeguards against cyber misuse"; after backlash its safety lead said customers can keep opting out of training — [CyberScoop, 2026-11-05](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)

#### Named partners and users
- Daybreak Cyber Partner Program (named 10–11 Aug 2026), 16 firms — security and services: Accenture, IBM, Capgemini, Cognizant, EY, KPMG, PwC, NCC Group, SpecterOps; technology: Palo Alto Networks (Unit 42), CrowdStrike, Cisco, Sophos, Akamai, Fortinet, Cloudflare — [Help Net Security, 2026-08-11](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); [Tahawul Tech](https://www.tahawultech.com/news/openai-expands-daybreak-cyber-programme-and-partner-network/)
- OpenAI's Daybreak partners page reportedly also shows Check Point, Elastic, HackerOne, Proofpoint and Tenable describing how they embed OpenAI's GPT cyber models (referencing earlier GPT-5.5 work) — [OpenAI Daybreak partners page](https://openai.com/daybreak/partners/) [extract only; page returned 403; unconfirmed]
- GPT-6 Cyber launch (5 Nov 2026): "security teams at companies like Mozilla, Palo Alto Networks, Calif, and Cisco—alongside…" are using it — [OpenAI on X, 2026-11-05](https://x.com/OpenAI/status/2118390190246879554) [search-result title]; TestingCatalog adds CodeRabbit (vulnerability research and code review) — [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/)
- Dragos (OT security): OpenAI announced a new partnership; Dragos ran evaluations of the cyber-permissive Daybreak Red models in a controlled lab — [CyberScoop, 2026-11-05](https://cyberscoop.com/openai-gpt-6-cyber-security-model/); [OpenAI launch post](https://openai.com/index/introducing-gpt-6-cyber/) [extract only]
- XBOW used OpenAI's GPT-5.6 Sol models (programme status not stated) to build a three-bug Chrome full chain in six days for about $40,000 of compute; Google paid $250,000 (13 Oct 2026). OpenAI's Clint Gibler: "A single XBOW researcher used our models to uncover a chain of vulnerabilities that Google has now fixed." — [XBOW, 2026-10-13](https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users)

#### Acquisitions
- No completed OpenAI security acquisition was found. One report says "OpenAI's Trail of Bits talks" (early Oct 2026) moved Palo Alto −4% and CrowdStrike −3% [unconfirmed; single secondary source; no deal confirmation found] — [Simply Wall St, 2026-10-23 (upd. 10-27)](https://simplywall.st/article/ai-has-flipped-the-story-on-cybersecurity-stocks-twice)

#### "A thousand fewer paths to root" (published c. 4 Nov 2026) — business facts only
- Run: 10 days in October 2026 with an unnamed "upcoming cyber security model" (later identified as the model behind GPT-6 Cyber), covering about 2.8M lines (~7% of the kernel) reachable by ordinary users — [iTnews, 2026-11-06](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145); OpenAI's 5 Nov post says the model "powered the Linux kernel research we announced yesterday" — [OpenAI on X](https://x.com/OpenAI/status/2118390190246879554)
- Claimed counts: 2,308 candidate findings within 12 hours; 1,724 reproduced in VMs; 948 distinct local privilege-escalation flaws, one patch written for each; comparison July run with GPT-5.6 Sol found 166 unique flaws [company claim, unconfirmed] — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145); [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/)
- Cost: about US$1.21M of API spend, ~US$1,279 per flaw (OpenAI calls it an upper bound); July run ~US$513,690, ~US$3,094 per flaw; OpenAI's hypothetical market value of the 948 flaws US$18.9M–66.3M using historical bounty prices (not a sale) — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145)
- Upstream status at end of the mid-October scan: 61 patched upstream by other contributors, 43 with staging patches, 299 under public discussion; "hundreds of reports and candidate patches" submitted; rest to be released gradually through "Patch the Planet" partners — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145)
- Outside confirmation: none cited; iTnews says parts "cannot yet be independently verified"; Greg Kroah-Hartman's quoted remarks (different groups reporting the same bugs within days) concern a separate May event — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145)

#### Ownership, structure, IPO
- 28 Oct 2025 recapitalisation: Microsoft holds an investment in OpenAI Group PBC "valued at approximately $135 billion", "roughly 27 percent on an as-converted diluted basis"; Microsoft's model/product IP rights run through 2032 — [Microsoft, 2025-10-28](https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/)
- The nonprofit OpenAI Foundation controls OpenAI Group with a 26% stake plus a milestone warrant — [MarketScreener/Reuters](https://www.marketscreener.com/news/openai-lays-groundwork-for-juggernaut-ipo-at-up-to-1-trillion-valuation-ce7d5dd2d089f626) [extract only]
- IPO timing: CFO reportedly told staff OpenAI "will be a public company in 2027" — [TheStreet](https://www.thestreet.com/investing/stocks/openai-cfo-says-ipo-is-in-2027) [extract only]; 5 Nov 2026, Greg Brockman, asked whether OpenAI would be IPO-ready next year: "I think so. Yes."; annualised revenue +70% QoQ in Q3 2026, enterprise roughly doubled and now most of revenue — [TechCrunch, 2026-11-05](https://techcrunch.com/2026/11/05/openai-president-greg-brockman-says-company-could-be-ipo-ready-in-2027/)
- A confidential draft S-1 was reportedly submitted 8 Jun 2026 [secondary, unverified] — [decodethefuture](https://decodethefuture.org/en/openai-ipo-explained/) [extract only]

### Inferences
- OpenAI is simultaneously a supplier and a competitor: the Daybreak partner structure makes the largest platforms (PANW, CrowdStrike, Cisco, Fortinet, Cloudflare) and the big consultancies resellers of gated capability ("access stays with the partner"), while Codex Security competes directly with application-security scanners.
- On OpenAI's own figures, cost per kernel flaw fell ~2.4x (US$3,094 → US$1,279) in about three months while yield rose ~5.7x (166 → 948) for ~2.4x the spend; only 61 of 948 were patched upstream when the scan ended (~6%), so remediation, not discovery, is the binding constraint.
- The planned critical-infrastructure Red group and the Dragos partnership are OpenAI's first explicit moves toward OT; so far they are evaluation and access arrangements, not an OT product.

### Gaps
- The original launch date of the "Daybreak" brand and GPT-5.5-Cyber, the price of GPT-6 Cyber, and any published country/nationality rules for TAC/Daybreak were not found (openai.com pages returned 403).
- OpenAI security revenue is undisclosed; latest valuation figures conflict ($852B vs >$1T in secondary sources) and could not be pinned to a dated primary source.
- Whether XBOW, HackerOne, Tenable, Check Point, Elastic or Proofpoint hold Daybreak Red access is unconfirmed.

---

## 2. Anthropic: Claude Code Security → Claude Security, Project Glasswing, Claude Mythos and the Cyber Verification Program, country rules, IPO

### Takeaway
Anthropic moved from a scanning research preview (Claude Code Security, 20 Feb 2026) to a gated frontier model (Mythos Preview via Project Glasswing, 7 Apr 2026: 12 launch partners, 40+ more organisations, up to $100M credits), expanded to ~200 organisations in 15+ US-friendly countries (2 Jun 2026), was forced by a US Commerce directive (12 Jun 2026) to cut all foreign-national access until 30 Jun, folded Glasswing into a three-tier Cyber Verification Program (6 Oct 2026, with US-government review for the top tier), and now sells Mythos-powered Claude Security to all Enterprise customers at token cost (beta). Its IPO is set to price on 18 Nov and trade on 19 Nov 2026 (reported) at up to $1.405T fully diluted.

### Cited Findings

#### Claude Code Security → Claude Security
- 20 Feb 2026: Claude Code Security launched as "a limited research preview" for Enterprise and Team customers; open-source maintainers invited to "apply for free, expedited access"; "Nothing is applied without human approval"; using Claude Opus 4.6 the team "found over 500 vulnerabilities" in production open-source codebases [company claim, unconfirmed]; no price stated — [Anthropic, 2026-02-20](https://www.anthropic.com/news/claude-code-security)
- Claude Security (status at 12 Nov 2026): "available in beta for users on Enterprise plans"; "Claude Security scans are powered by Claude Mythos model"; billed at direct token cost, no platform fee; requires Enterprise plan, a premium seat per user and usage credits; Zero Data Retention not supported; launch offer of "free usage credits up to $25,000 a month, for two months, through December 31, 2026" (existing Enterprise customers from 21 Oct 2026); scans GitHub, GitHub Enterprise Server, GitLab, Azure DevOps, Bitbucket; up to eight repositories per project; may only scan code the company owns or has rights to scan — [Claude Help Center (accessed 2026-11-12)](https://support.claude.com/en/articles/14661296-use-claude-security)
- 9 Nov 2026: "Claude Enterprise customers (even if they aren't members of the Cyber Verification Program) can access" Claude Security, whose models "now include Claude Mythos 5.2" — [Anthropic, 2026-11-09](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- Dates of Claude Security's earlier public beta conflict (30 Apr, 4 May, 21 Aug 2026 for Mythos 5 scans) across secondary sites — [search extract of several sites, e.g. pasqualepillitteri.it](https://pasqualepillitteri.it/en/news/12235/claude-security-mythos-5-scans) [secondary]
- 8 Oct 2026: Anthropic launched OSS Scanner, free scans for eligible opt-in open-source projects — [Wikipedia: Claude Mythos (citing The Verge, The Register)](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]

#### Project Glasswing (launched 7 Apr 2026)
- Launch partners (12 incl. Anthropic): AWS, Anthropic, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks; access extended to "over 40 additional organizations" that build or maintain critical software; up to $100M usage credits for Mythos Preview; $4M donations ($2.5M to Alpha-Omega/OpenSSF via the Linux Foundation, $1.5M to the Apache Software Foundation); post-credit price $25/$125 per million input/output tokens; "We do not plan to make Claude Mythos Preview generally available" — [Anthropic Glasswing page](https://www.anthropic.com/glasswing); [Fortune, 2026-04-07](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/)
- Claimed results at launch: "thousands of high-severity vulnerabilities" across every major OS and browser; CyberGym 83.1% vs 66.6% for Opus 4.6 [company claim] — [Anthropic Glasswing page](https://www.anthropic.com/glasswing). An independent researcher noted Anthropic's own report says Opus 4.6 found the bugs before Mythos exploited them — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- First-month results (disclosed c. 22 May 2026): >10,000 high/critical vulnerabilities flagged by partners; 6,202 estimated high/critical in >1,000 open-source projects; 1,726 confirmed valid true positives; 97 patched upstream; 88 advisories — [The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html). CSA's tally (data to 22 May): independent firms assessed 1,752 findings, 90.6% valid and 62.4% high/critical; 1,596 disclosed to maintainers across 281 projects; 97 confirmed patched (~6%); 88 CVE/GHSA (~5.5%) — [Cloud Security Alliance, released 2026-06-07 (date format ambiguous)](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity)
- Partner outcomes with outside confirmation: Mozilla patched 271 Firefox vulnerabilities found with Mythos Preview (21 Apr 2026) — [Wikipedia: Claude Mythos (citing Ars Technica, Wired)](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- Security incidents: 21 Apr 2026, Bloomberg reported unauthorised users accessed Mythos via a private Discord channel using details from the Mercor breach — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- 2 Jun 2026 expansion: ~150 more organisations in 15+ countries "friendly to the U.S." (Australia, Canada, France, Germany, Italy, Switzerland, Netherlands, Spain, Belgium, Sweden, India, Japan, New Zealand, South Korea, plus one unnamed); FT-named participants: Okta, Samsung, SK Hynix, SK Telecom, NATO, ENISA; sectors power, water, healthcare, communications, hardware; "will need to meet our security requirements before they gain access" — [TechCrunch, 2026-06-02](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/); [CSO Online, 2026-06-02](https://www.csoonline.com/article/4180265/anthropic-grants-project-glasswing-access-to-150-more-companies-with-a-focus-on-critical-infrastructure.html); Reuters reported the total at about 200 partners — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- IDC's Grace Trinidad on the requirements: "nobody knows what those security requirements are" — [CSO Online, 2026-06-02](https://www.csoonline.com/article/4180265/anthropic-grants-project-glasswing-access-to-150-more-companies-with-a-focus-on-critical-infrastructure.html)

#### Mythos versions and the verified-organisation programme
- Model sequence: Mythos Preview (7 Apr 2026, Glasswing only); 28 May, Anthropic's Opus 4.8 post says "Mythos-class" models will reach all customers within weeks pending cyber safeguards; Mythos 5 as a Glasswing preview and Fable 5 (safeguarded; classifiers route cyber requests to Opus) on 9 Jun; Mythos 5.1/Fable 5.1 on 1 Sep; Mythos 5.2/Fable 5.2 on 9 Nov 2026 — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]; [Anthropic, 2026-11-09](https://www.anthropic.com/claude-fable-and-mythos-5-2)
- 6 Oct 2026: Cyber Verification Program (CVP) expanded to three tiers — Defense Access (SOC/IR, malware reverse-engineering, vulnerability analysis and validation), Red Team Access (adds authorised penetration testing and red-teaming), Specialized Access (fewest blocks; verified organisations authorised to test safety-critical systems such as power grids and flight operating systems). Individuals may apply only for Defense Access and "must be on a paid plan"; Red Team and Specialized are organisation-only; Anthropic "currently reviews every organization at this tier [Specialized] in depth in collaboration with the US government"; Defense decisions "within a few days", Red Team in weeks; Glasswing and the original CVP "are now integrated"; enrolled organisations must allow data retention for misuse monitoring; covers Opus 5.5, Sonnet 5.5, Mythos 5.1 and future models; eligibility factors include the legal and regulatory environment and "the risk of diversion or compelled access", with a more cautious approach to organisations primarily serving military, intelligence or law-enforcement customers; Booz Allen and Comcast cited as Glasswing partners — [Unite.AI, Oct 2026](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/); Glasswing page update dated 6 Oct 2026 says existing Glasswing members move to Specialized Access — [Anthropic Glasswing page](https://www.anthropic.com/glasswing)
- Distribution through clouds: Google Cloud documents the CVP tiers for Claude on Gemini Enterprise Agent Platform (Opus 5.5, Sonnet 5.5, Mythos 5.1 and later; CVP does not reduce blocks on Fable models; each tier includes Mythos access) — [Google Cloud docs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/cyber-verification-program) [extract only]; Mythos on third-party clouds trails approval by about five business days — [Unite.AI](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/)
- Mythos 5.2 (9 Nov 2026): access via CVP for cyber ("available to vetted organizations that work in these dual-use areas"); Fable 5.2 and Mythos 5.2 at $8/$40 per million tokens, fast mode $16/$80, "available only to organizations who are part of our Verification Programs"; internal CVE Rediscovery (1,829 CVEs): Mythos 5.2 found 10.2% more than Opus 5.5 and 14.4% more than Mythos 5.1 [company claim, unconfirmed]; Mozilla: "Mythos 5.2 roughly doubled the vulnerability discovery metrics of Mythos 5.1" [partner claim]; named cyber testers Rubrik and Mozilla; external pre-release testers UK AISI, METR and "Frontier Design"; Fable 5.2 blocks penetration testing and exploit generation for general users with an Opus 4.8 fallback — [Anthropic, 2026-11-09](https://www.anthropic.com/claude-fable-and-mythos-5-2)

#### Country rules
- 5 Sep 2025: Anthropic barred companies majority-controlled (>50%) by entities from China, Russia, Iran or North Korea, including overseas subsidiaries, citing legal requirements that can compel data sharing or intelligence cooperation — [The Decoder, Sep 2025](https://the-decoder.com/anthropic-bans-companies-majority-controlled-by-china-russia-iran-and-north-korea-from-claude/); [MediaNama, Sep 2025](https://www.medianama.com/2025/09/223-anthropic-service-policy-update-bans-ai-access-chinese-firms/) [extract only]
- 12 Jun 2026: a US Commerce (BIS) directive required Anthropic to "suspend access to its Fable 5 and Mythos 5 models for any foreign national, whether located abroad or inside the United States", including foreign-national employees; Anthropic could not screen by nationality and disabled both models entirely — [Tech Policy Press, 2026-06-15](https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/); 26 Jun Commerce approved Mythos 5 for some US organisations; 30 Jun controls lifted, Fable 5 back globally 1 Jul; Lutnick found "appropriate safeguards" for certain "trusted partners"; Anthropic will "keep working with the government to expand Mythos 5 access to more domestic and international Glasswing partners" — [CNBC, 2026-06-30](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)
- A November 2026 "Supported Regions Policy" revision (effective 12 Nov) restricting users in, entities headquartered in, or entities controlled from unsupported regions (mainland China, Hong Kong, Macau, Russia) is reported only by a garbled news flash [unverified] — [KuCoin flash](https://www.kucoin.com/news/flash/anthropic-updates-regional-usage-rules-chinese-owned-entities-banned-from-using-claude) [extract only]

#### IPO
- S-1 filed 26 Oct 2026, amended 2 Nov [lead, not re-verified] — earlier notes citing [Fortune](https://fortune.com/2026/10/26/anthropics-s-1/)
- 10 Nov 2026: roadshow launched for 825,000,000 Class A shares (801,351,354 primary, 23,648,646 secondary) at $70–78; 30-day option for 123,750,000 more; Nasdaq Global Select, ticker "ANT"; prospectus from Goldman Sachs and Morgan Stanley — [Anthropic, 2026-11-10](https://www.anthropic.com/news/roadshow-launch)
- Pricing expected 18 Nov, trading 19 Nov (unnamed sources); up to $1.405T fully diluted and up to $64.35B proceeds at the top; prior private valuation $965B (May 2026 round); $26B Class N private placement at the IPO price to AMD, Broadcom, Google, Micron, Microsoft, Nvidia and TSMC; nine months to 30 Sep 2026 revenue $33.24B (up ~1,200%), net loss $104B (mostly fair-value changes on convertible notes and derivatives); run-rate revenue ~$81B at end-October; linked headlines cite purchase commitments of $895.4B — [CNBC, 2026-11-10](https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html)
- Neither the roadshow release nor CNBC mentions any security or Glasswing revenue — [Anthropic](https://www.anthropic.com/news/roadshow-launch); [CNBC](https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html)

### Inferences
- Anthropic's gate, not only its model, is now the scarce asset: membership decides which vendors can sell Mythos-grade discovery, and the top tier is vetted with the US government. The June episode shows the gate can be closed by Washington overnight for every non-US national, so non-US vendors' access is contingent.
- Claude Security undercuts scanner vendors' pricing model (token cost, no platform fee, $50K of free credits per eligible customer through 2026), but requires a premium Enterprise seat, so it is a hybrid of usage pricing and per-human seats.
- Validation is the weak link on Anthropic's own numbers: of >10,000 flagged in month one, 1,726 were confirmed valid and 97 patched (THN), i.e. under 1% of flagged items fixed in the first weeks.
- At the top of the range, the whole company would be valued at ~17x end-October run-rate revenue ($1.405T / $81B) or ~32x annualised nine-month revenue ($33.24B × 4/3 ≈ $44.3B).

### Gaps
- No full list of the ~200 Glasswing/CVP organisations has been published; which security vendors besides CrowdStrike, Palo Alto Networks, Cisco, Broadcom, Okta, Trend Micro and Booz Allen hold Mythos access is unknown.
- The 90-day Glasswing public report promised for about early July 2026 was not found.
- No security-specific revenue in the S-1 was found (the S-1 itself was not opened).

---

## 3. Google / Google DeepMind (incl. Wiz, Mandiant): Big Sleep, CodeMender, Sec-Gemini, gated Gemini cyber variants and the Fairwind Program; Wiz; security revenue disclosure

### Takeaway
Google has the most layered security business of the model makers — owned products (Wiz, closed 11 Mar 2026 at $32B cash; Google Threat Intelligence; Mandiant) plus DeepMind agents (Big Sleep, CodeMender) and gated cyber variants (Gemini 3.8 Flash Cyber, a planned guardrail-free Argon, and "Carbon for cyber") offered through the Fairwind Program (blog 2 Sep 2026; >650 partners then, "thousands" now) whose named partners include CrowdStrike, Palo Alto Networks, Wiz, Menlo Security, Datadog and Snowflake. Alphabet discloses no security revenue (Q3 2026: "cybersecurity portfolio growth was strong", no figure; no Wiz ARR).

### Cited Findings

#### Big Sleep, CodeMender, Sec-Gemini
- Big Sleep (DeepMind + Project Zero) found its first real-world vulnerability by Nov 2024; later found SQLite CVE-2025-6965, "known only to threat actors"; Google calls it "the first time an AI agent has been used to directly foil efforts to exploit a vulnerability in the wild" [company claim]; Sec-Gemini named as the engine behind new agentic Timesketch features — [Google blog, 2025-07-15](https://blog.google/technology/safety-security/cybersecurity-updates-summer-2025/)
- CodeMender (6 Oct 2025): agent that patches new vulnerabilities and rewrites code to remove vulnerability classes; "we have already upstreamed 72 security fixes to open source projects"; validation by static and dynamic analysis, differential testing, fuzzing, SMT solvers and an LLM critique tool; "all patches generated by CodeMender are reviewed by human researchers before they're submitted upstream"; then a research effort — [Google DeepMind, 2025-10-06](https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/)

#### Gated Gemini cyber variants and the Fairwind Program
- 2 Sep 2026: Fairwind is "a limited access program for governments and trusted partners to use our most advanced cyber defense capabilities"; staged for governments and national cyber authorities, critical-infrastructure operators (healthcare, telecom, energy, financial) and core technology platforms; participants must limit access to internal security, IR or pentest staff and deploy protections such as MFA; "more than 650 participating partners globally"; offers Gemini 3.8 Flash Cyber with the CodeMender harness; outside Fairwind, any Google Cloud customer can use CodeMender with public models on Gemini Enterprise Agent Platform; testimonials from Armadin, CrowdStrike, Menlo, Palo Alto, Snowflake and Wiz — [Google blog, 2026-09-02](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)
- DeepMind Fairwind page (undated, read 12 Nov 2026): "thousands of partners globally"; 12 named logos — Accenture, Armadin, Center for Internet Security, CrowdStrike, Datadog, Deloitte, McKinsey & Company, Menlo Security, Palo Alto Networks, Robinhood, Snowflake, Wiz; priority also for academic labs doing defensive benchmarking; vetting includes background checks; apply via the Cloud account team; requirements: phishing-resistant MFA, tracked employee access, no sharing/resale, no malware creation; "Gemini for cyber" supports zero data retention on Gemini Enterprise — [Google DeepMind Fairwind page](https://deepmind.google/fairwind-program/)
- 1 Oct 2026: Gemini 4 Argon rolled out to "a set of trusted cyber defenders through its Fairwind Program"; Google "plans to release a version of Argon without cyber guardrails" to trusted defenders and internal teams (no date) — [The Hacker News, 2026-10-01](https://thehackernews.com/2026/10/google-rolls-out-gemini-4-argon-to.html)
- 28 Oct 2026: Gemini 4 Carbon released first to Fairwind cyber defenders; 10 Nov 2026: public via paid API, Gemini for business, Android Studio and (AI Ultra) Antigravity/Gemini app/AI Mode at an introductory $2/$10 per million tokens, then $4/$20; "Carbon for cyber" stays in Fairwind ("apply... to get access to Carbon for cyber on a rolling basis") — [Google blog, 2026-11-10](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
- Claimed Carbon results: Project Fortify (internal autonomous scan/triage/remediation) 100% scanning recall and 95% triage precision on an internal benchmark; Google Cloud Vulnerability Research proved two open-source bugs exploitable (maintainers reclassified as critical and patched); Wiz "Scan for Good" found 0-days in two major SaaS providers in under two hours; safeguards blocked 99% of simulated attack trajectories; external testers Gray Swan and Trajectory Labs [company claims, partly third-party-tested safeguards] — [Google blog, 2026-11-10](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/)
- Carbon's published cyber scores (SEC-bench Pro 88.2, ExploitGym 54.8, CWE-bench 71.0) "were evaluated without guardrails" [company claim] — [The Hacker News via earlier notes](https://thehackernews.com/2026/10/googles-gemini-4-carbon-leads.html) [lead, not re-verified]

#### Wiz
- Closed 11 Mar 2026: $32B in cash, Google's largest acquisition; US antitrust clearance Nov 2025 and EU Feb 2026; Wiz joins Google Cloud, keeps its brand and multicloud commitment (AWS, Azure, Oracle); Wiz crossed $1B ARR in 2025 per an unnamed source — [TechCrunch, 2026-03-11](https://techcrunch.com/2026/03/11/google-completes-32b-acquisition-of-wiz/). Other reports give US clearance as Oct 2025 and add Australia (Feb 2026), Singapore and Japan (Mar 2026) — [Cybersecurity News (search extract)](https://cybersecuritynews.com/google-acquires-wiz/) [extract only]

#### Security revenue disclosure
- Alphabet Q3 2026 (call 28–29 Oct 2026): Google Cloud revenue $30.7B (+103% YoY), operating income $11.1B (36.2% margin), backlog $561B; Alphabet revenue $127.6B (+25%); capex $51.4B; free cash flow −$9.1B; on security only: "more than 95% of Wiz customers are adopting AI-powered features, and growth continues"; Google Threat Intelligence "autonomously analyzes millions of external events every day with 98% accuracy"; Gemini Flash cyber models "automate vulnerability discovery across 20 programming languages" and patch "2.6x more reliably" [company claims]; customers named Banorte, Jack Henry, AT&T; "cybersecurity portfolio growth was strong" with no figures; no Wiz revenue or ARR disclosed — [Motley Fool transcript, 2026-10-29](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/)

### Inferences
- Google is the only model maker that owns a large exposure-management franchise (Wiz) and an incident-response services arm (Mandiant), so it competes with exposure-management and MDR vendors directly, while Fairwind supplies gated models to CrowdStrike and Palo Alto Networks.
- Wiz is tiny relative to the parent: >$1B ARR (2025) is under 1% of Google Cloud's annualised revenue (~$123B on Q3 2026) and ~0.2% of Alphabet's.
- CodeMender's validation stack (fuzzing, differential tests, SMT solvers, then human review) is the clearest example among the labs of a "judge" built into the product, but the final judge remains upstream maintainers.

### Gaps
- No 2026 figures found for Big Sleep, Sec-Gemini, Mandiant revenue, Google Unified Security, Google SecOps or Google Threat Intelligence customer counts (web search budget ran out before these could be searched).
- How Alphabet reports Wiz (inside Google Cloud is stated; any line item is not) and the final purchase price (one unidentified report claims $29.5B per Alphabet's SEC filing; unverified).
- No published country rules for Fairwind were found.

---

## 4. Microsoft: Security Copilot and agents, Defender/Sentinel, GitHub Advanced Security, Project Ire, own cyber models; latest security revenue and customer disclosures

### Takeaway
Microsoft is an incumbent security vendor that also builds its own cyber model (MAI-Cyber-1-Flash) and agentic security system (Project Perception), is a Glasswing launch partner, bundles Security Copilot into E5 (Jan 2026) and reports GitHub Advanced Security revenue growth over 50% (28 Oct 2026). Its last disclosed security revenue figure is "surpassed $20 billion" over the 12 months to Dec 2022 (24 Jan 2023); latest customer count is 1.6 million security customers (28 Jan 2026).

### Cited Findings
- 24 Jan 2023: "Over the past 12 months, our security business surpassed $20 billion in revenue" — [Microsoft FY23 Q2 call](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q2) (no later security revenue figure was found in FY2026 releases or the FY2026 10-K, which does not report security as a line or segment — [Microsoft 8-K, 2026-07-29](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm); [FY2026 10-K](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm))
- 28 Jan 2026: "we now have 1.6 million security customers – including over a million who use four or more of our workloads"; "a dozen new and updated Security Copilot agents across Defender, Entra, Intune, and Purview"; "we are rolling out Security Copilot to all E5 customers" — [Microsoft FY26 Q2 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2)
- 29 Apr 2026: "the number of Security Copilot customers increased 2X year over year"; data-security triage agents "handled over 2 million unique alerts this quarter"; "we sim-ship Defender protections when updates for AI-discovered vulnerabilities are released"; "the physics of cybersecurity has changed as AI compresses the window between vulnerability and exploitation" — [Microsoft FY26 Q3 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- 29 Jul 2026: Project Perception, "a complete multi-model agentic security system" (Red Team agents that find, a Blue Team agent that triages, a Green Team that "fixes"), to be offered "through a consumption-based offering"; Nadella: MAI-Cyber-1-Flash "achieves better performance than the much larger Mythos model but at half the cost"; ~90% of tasks go to Cyber-1-Flash and "10% of the tasks, you still go to the frontier" [company claim, unconfirmed] — [Microsoft FY26 Q4 call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4)
- 28 Oct 2026: "GitHub Advanced Security revenue increased over 50 percent year over year"; "MAI Cyber now powers over 40 percent of the scans in our agentic MDASH code scanner, at 18 percent lower cost per scan"; Perception preview customers KPMG, Nationwide Building Society, Northern Trust, Stellantis; E7 bundles Copilot, E5, Entra and Agent 365 — [Microsoft FY27 Q1 call](https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1)
- Project Ire (5 Aug 2025, prototype): autonomous malware classification agent; precision 0.98 / recall 0.83 on public Windows drivers; precision 0.89 / recall 0.26 (4% false positives) on ~4,000 hard-target files; to be used inside Defender as "Binary Analyzer"; outputs a "chain of evidence" with a validator tool [company claim] — [Microsoft Research, 2025-08-05](https://www.microsoft.com/en-us/research/blog/project-ire-autonomously-identifies-malware-at-scale/)
- FY2026 (to 30 Jun 2026): revenue $331.8B, operating income $155.2B, net income $133.7B, cash from operations $182.9B, capex $115.9B — [Microsoft 8-K, 2026-07-29](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm)
- Glasswing launch partner (7 Apr 2026) — [Anthropic Glasswing page](https://www.anthropic.com/glasswing)

### Inferences
- Microsoft's strategy is to route most security work to its own cheaper specialised model and buy frontier capability only for the hard tail, which reduces its dependence on any single lab's gate and lets it compete with labs on price.
- If security revenue were still about $20B (it has surely grown, but no figure is published), it would be ~6% of FY2026 revenue; any security exposure through MSFT stock is heavily diluted.
- Microsoft's revenue model in security is mainly per-user suites (E5/E7) with consumption add-ons (Security Copilot, Perception), so a shift to usage pricing would partly cannibalise seats.

### Gaps
- No 2026 security revenue, Sentinel/Defender metrics, Copilot Autofix figures or outside rankings (e.g. analyst quadrants) were found in this session.
- Whether MAI-Cyber-1-Flash is offered to outside security vendors (a gated programme) was not found.

---

## 5. Amazon / AWS: security services, automated reasoning, participation in other labs' programmes

### Takeaway
AWS's AI security push is AWS Continuum (code-vulnerability discovery/validation/remediation plus penetration testing, the latter formerly "AWS Security Agent"), described as model-agnostic and using "multiple frontier cyber models" on customers' behalf; AWS is a Glasswing launch partner and Continuum integrates into Claude Code and Codex. Amazon gives no security revenue figure.

### Cited Findings
- AWS Continuum "continuously discovers, prioritizes, validates, and remediates security risks across the software lifecycle"; Continuum for code vulnerabilities builds a context graph of the AWS environment, confirms exploitability in an isolated sandbox and delivers patches; "Continuum for penetration testing (f.k.a. AWS Security Agent)" offers on-demand pentesting; "AWS harnesses multiple frontier cyber models on your behalf" and is "model agnostic"; customer quotes from Luminate Data, IBM, Infor, Tata Consultancy Services and HENNGE; no price or launch date shown — [AWS Continuum page (read 2026-11-12)](https://aws.amazon.com/continuum/); [AWS Security Agent page](https://aws.amazon.com/security-agent/)
- Amazon Q3 2026 call (29–30 Oct 2026): AWS revenue $46.0B (+39.3%), operating income $17.8B (38.7% margin), backlog $578B; "We built AWS Continuum to discover, prioritize, validate, and remediate code vulnerabilities at machine speed", used by Capital One, IBM, Infor, Luminate and Robinhood; it will integrate into Claude Code, Codex and Kiro; "The interest from customers exceeds anything we have ever seen for a new security service" [company claim]; Jassy: "some significant percent of it [future token usage] may end up being just security" — [Motley Fool transcript, 2026-10-30](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- Amazon's Q3 2025 net income included a $9.5B pre-tax gain on its Anthropic investment — [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)
- Participation in other labs' programmes: Glasswing launch partner (7 Apr 2026) — [Anthropic](https://www.anthropic.com/glasswing); Fable 5 re-enabled on AWS (and Google Cloud, Microsoft Foundry) "as soon as possible" after the 30 Jun 2026 lifting — [CNBC, 2026-06-30](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)

### Inferences
- AWS is positioned as a distributor and integrator of other labs' gated models rather than a lab with its own gated cyber model; its moat is environment context (the AWS context graph) and distribution, and its exposure is to the labs' and Washington's gates.

### Gaps
- Automated-reasoning products (e.g. provable-security tools) are not mentioned on the Continuum pages or the Q3 call; no 2026 source on them was found in this session. Continuum's pricing, GA date and which frontier models it uses are not published.

---

## 6. Meta, other open-weight releases and Chinese labs: dated third-party cyber evaluations and the claim that attackers do not need frontier models

### Takeaway
Meta supplies open security tooling and benchmarks (Purple Llama, CyberSecEval 4, LlamaFirewall, Llama Defenders Program) rather than a security business, and released Muse Spark Open (15 Oct 2026) with heavy refusal training. Independent US and UK evaluators measure Chinese open-weight models roughly four to eight months behind the US frontier on cyber (DeepSeek V4 Pro ~8 months, May 2026; GLM-5.3 ~4 months, Sep 2026), with large gaps on the hardest exploitation tasks; CSA's synthesis of UK AISI data puts the lag at four to seven months at about two orders of magnitude lower cost. That supports the claim that attackers increasingly do not need gated frontier models for near-frontier tasks, but not for the hardest end-to-end work.

### Cited Findings

#### Meta
- 29 Apr 2025: Meta released Llama Guard 4, LlamaFirewall, Prompt Guard 2 and CyberSecEval 4 (incl. CyberSOC Eval "Developed with CrowdStrike" and AutoPatchBench), and a Llama Defenders Program for "select partners" (launch integrations with ZenDesk, Bell Canada, AT&T) — [Meta AI blog, 2025-04-29](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/)
- Purple Llama repository lists CyberSec Eval v1–3, Llama Guard, Prompt Guard, Code Shield and a LlamaFirewall folder; no 2026 version dates shown — [GitHub: meta-llama/PurpleLlama (read 2026-11-12)](https://github.com/meta-llama/PurpleLlama)
- Muse Spark Open (15 Oct 2026, "Muse Model License"): "additional safety post-training to make it more robust against misuse as a standalone model"; refused 99.2% of jailbreaks on Meta's internal cyber benchmark and 94.8% across PolyGuard (cyber), RedCode and CyberBench 2024, vs 75.5% and 70.2% for Kimi K3 [company claim]; cyber testing done with "no system-level safeguards"; results "should not be assumed to apply to modified models"; no cyber capability benchmark published — [Muse Spark Open card (Unsloth mirror)](https://huggingface.co/unsloth/Muse-Spark-Open-816B-A42B)

#### Chinese and other open-weight models — third-party evaluations
- 1 May 2026, CAISI (NIST): DeepSeek V4 Pro is "the most capable PRC model to date"; on CAISI's CTF-Archive-Diamond (285 hard CTFs): GPT-5.5 71%, Opus 4.6 46%, GPT-5.4 mini 32%, DeepSeek V4 Pro 32%; "DeepSeek V4's capabilities lag behind the frontier by about 8 months" — [NIST CAISI, 2026-05-01](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)
- 17 Jul 2026, CAISI: GLM-5.2 (Z.ai) "probably the most capable open-weight AI model when it was released"; its safeguards allowed assistance with agentic exploit development; cyber comparable to Opus 4.6 — [CASRAI guide to CAISI assessments](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments) [secondary]
- 23 Jul 2026 (updated 28 Aug), UK AISI + CAISI preliminary on Kimi K3: ExploitBench 32% (GLM-5.2 24%); full automated compromise on 0 of 41 sampled vulnerabilities vs ~20 of 41 for the most cyber-capable models; 17 of 32 steps on AISI's TLO range vs ~28.5 for the best US models — [CASRAI](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments) [secondary]
- 17 Sep 2026, CAISI: GLM-5.3 "the most cyber-capable open-weight model released to date"; SEC-Bench Pro 40.4% vs 90.2% for US frontier; ExploitBench 61.1% vs 100%; ExploitGym 9.4% vs 44.4%; OSS-Fuzz 7.7% vs 23.2%; "roughly four months behind U.S. frontier models in aggregate" — [CASRAI](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments) [secondary]; four-month figure also reported by [Notebookcheck, 2026-10-01](https://www.notebookcheck.net/GLM-5-3-China-s-open-AI-model-built-a-Chrome-exploit-for-20.1413141.0.html)
- Anthropic reported (late Sep 2026) that GLM-5.3-Flash wrote a working exploit for a Chrome V8 flaw Google had fixed in June, for $20.40 at Zhipu's API prices plus 20 minutes of human attention [competitor claim, not independently verified] — [Notebookcheck, 2026-10-01](https://www.notebookcheck.net/GLM-5-3-China-s-open-AI-model-built-a-Chrome-exploit-for-20.1413141.0.html)
- 31 Jul 2026, CSA synthesis of UK AISI's first public open-weight cyber measurement: lag four to seven months in mid-2026 (from six to ten in 2025); GLM-5.2 matched Opus 4.6 on narrow tasks (four months), DeepSeek V4-Pro matched Opus 4.5; lag widens on long attack chains (weaker evidence); DeepSeek V4-Pro about $0.28 per task vs $12.50–15.17 for Opus 4.5/4.6 ("nearly two orders of magnitude"); AISI's open-weight tests "largely unimpeded by safeguards"; CAISI found DeepSeek models complied with adversarial jailbreak prompts "more than 90 percent of the time" vs 6–10% for gpt-oss; caveat that the two largest 2026 jumps (Mythos Preview, GPT-5.5) came from closed models — [CSA research note, 2026-07-31](https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/)
- Kimi K3.1 Pro model card: ExploitBench 74.7 vs GPT-6 Astra 100, Opus 5.5 91.0, Fable 5.1 83.0, GLM-5.3 54.4; ExploitGym 20.7 vs 42.4 / 34.5 / 30.4 / 15.0; internal xdev-bench-hard 81.0 [vendor-run, partly vendor-reported comparisons] — [Hugging Face: moonshotai/Kimi-K3.1-Pro](https://huggingface.co/moonshotai/Kimi-K3.1-Pro); Moonshot says it removed cyber data so the open weights would not "extend the absolute frontier of cyber capability" (pre-removal checkpoint 90.5% on xdev-bench-hard) and that K3.1 Pro's cyber capability "remains behind that of frontier proprietary models that have been publicly available for at least three months" — [blog capture mirrored on GitHub, 24 Oct 2026](https://github.com/kakon77777-commits/agiright-evidence/blob/6224a57aa54fc716328ca87fa37accddc6801068/sources/2026-10-24/kimi.txt) [lead, not re-verified]
- Mistral Large 4 open weights (29 Oct 2026): "ML4 brings state-of-the-art sovereign cyber defense capabilities to enterprises and governments globally"; no gated variant described by TechCrunch; claims parity with GLM-5.3 [company claim] — [TechCrunch, 2026-10-29](https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/)
- Qwen: no CAISI cyber evaluation found; a Booz Allen finding that Qwen3-Coder produced more vulnerable code when the user was described as a US government worker is cited by the Manhattan Institute (1 Oct 2026) — [Manhattan Institute](https://manhattan.institute/article/an-american-answer-to-chinas-open-si-models-a-safe-harbor-for-open-weights) [extract only]

### Inferences
- "Attackers don't need frontier models" holds for discovery-style and narrow exploitation tasks at near-frontier level (four to eight months behind, ~100x cheaper, safeguards removable), but on the hardest end-to-end tasks the open models still trail sharply (e.g. GLM-5.3 ExploitGym 9.4% vs 44.4%; Kimi K3 0 of 41 full compromises). The gated programmes therefore buy defenders a lead of months, not a durable monopoly.
- Labs' own release choices diverge: Meta trains refusals in, Moonshot trains cyber data out, Mistral and Z.ai market cyber skill. A vendor relying on "the attacker lacks the model" has a time-limited advantage.

### Gaps
- No dated third-party cyber evaluations were found for ByteDance, Tencent, Baidu or Alibaba Qwen models, or for Muse Spark Open's cyber capability.
- The removal of cyber data from Kimi K3.1 Pro rests on an unpublished internal test; whether "abliterated" derivatives restore capability is untested.

---

## 7. Which security vendors (any country) are confirmed participants? Non-US inclusion; Chinese exclusion and domestic substitutes

### Takeaway
Confirmed security-vendor participants cluster in a handful of large US platforms that sit in all three programmes (Palo Alto Networks, CrowdStrike; Cisco in two), plus OpenAI's Daybreak partners (Fortinet, Sophos, Akamai, Cloudflare, NCC Group, SpecterOps), Google's Fairwind partners (Wiz, Menlo Security, Datadog, Snowflake) and Anthropic's Glasswing additions (Okta, Trend Micro, Hitachi). Non-US participation is real but thin and conditional (UK Sophos and NCC Group, Japan's Trend Micro and Hitachi, Korea's KISA/Samsung/SK named but with access disputed as of Sept 2026, EU's ENISA and NATO). No Zscaler, SentinelOne, Rapid7, Qualys, Snyk, Socket, Bugcrowd, Claroty, Armis or Nozomi participation was found. Chinese vendors are excluded by policy and are building substitutes (360's "Tulongfeng").

### Cited Findings
- Palo Alto Networks: Glasswing launch partner (7 Apr 2026) — [Anthropic](https://www.anthropic.com/glasswing); Daybreak technology partner via Unit 42 (10–11 Aug 2026) — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); GPT-6 Cyber user (5 Nov 2026) — [OpenAI on X](https://x.com/OpenAI/status/2118390190246879554); Fairwind partner — [DeepMind Fairwind page](https://deepmind.google/fairwind-program/)
- CrowdStrike: Glasswing launch partner — [Anthropic](https://www.anthropic.com/glasswing); Daybreak technology partner — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); Fairwind partner — [DeepMind](https://deepmind.google/fairwind-program/); co-developed Meta's CyberSOC Eval (29 Apr 2025) — [Meta](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/)
- Cisco: Glasswing launch partner — [Anthropic](https://www.anthropic.com/glasswing); Daybreak partner — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); GPT-6 Cyber user — [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/)
- Fortinet, Sophos (UK), Akamai, Cloudflare, NCC Group (UK), SpecterOps: Daybreak Cyber Partner Program (10–11 Aug 2026) — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/)
- Check Point (Israel), Tenable, HackerOne, Elastic, Proofpoint: shown on OpenAI's Daybreak partners page per a search extract [unconfirmed; page 403] — [OpenAI](https://openai.com/daybreak/partners/)
- HackerOne: 21 Sep 2026 announced upcoming integration of Claude Mythos into H1 Code Security Audit and H1 Code (no date; access route not named; it tested Mythos in the Glasswing context) — [HackerOne, 2026-09-21](https://www.hackerone.com/press-release/hackerone-bring-anthropics-mythos-exposure-management-lifecycle-discovery-verified)
- Dragos (OT): OpenAI partnership; evaluated Daybreak Red models (5 Nov 2026) — [CyberScoop](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)
- Okta: joined Glasswing 27 May 2026 — [BankInfoSecurity, 2026-09-18](https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191); named by the FT in the 2 Jun expansion — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- Wiz (Israeli-founded, Google-owned), Menlo Security, Datadog, Snowflake, Armadin, Center for Internet Security: Fairwind partners — [DeepMind Fairwind page](https://deepmind.google/fairwind-program/); [Google blog, 2026-09-02](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)
- Rubrik: named cyber tester of Mythos 5.2 (9 Nov 2026) — [Anthropic](https://www.anthropic.com/claude-fable-and-mythos-5-2); Booz Allen: Glasswing partner — [Unite.AI](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/); CodeRabbit and Calif: GPT-6 Cyber users — [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/)
- Japan: TrendAI (Trend Micro) announced Glasswing participation 3–4 Jun 2026 (press release); Hitachi signed with Anthropic 4 Jun and announced 5 Jun, with access "expected to be granted later"; NEC (strategic partnership, 23 Apr) and Fujitsu (access, 27 May) are reported by ITmedia only — [Uravation, Jun 2026](https://uravation.com/media/hitachi-trendmicro-claude-mythos-project-glasswing-japan-2026/) [secondary citing press releases]
- South Korea: FT-named Glasswing participants Samsung, SK Hynix, SK Telecom (2 Jun) — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/); a Science/ICT ministry official said KISA joined Glasswing and secured Mythos access — [CEO Insights Asia](https://www.ceoinsightsasia.com/news/korea-joins-anthropic-s-glasswing-for-mytos-ai-model-nwid-14622.html) [extract only]; contradicted 17 Sep 2026 by Palo Alto Networks Korea CEO Park Sang-gyu, who said as far as he knows no South Korean company or institution can use Mythos yet, citing "matters of national scope or the US government"; AhnLab's AI head said Korean firms "could compete with global firms without access to Mythos" — [The Elec, 2026-09-18](https://www.thelec.net/news/articleView.html?idxno=14029)
- Europe (bodies): NATO and ENISA named as the first intergovernmental Glasswing participants (2 Jun 2026) — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/); Capgemini (France) is a Daybreak partner — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/)
- India: India is among the Glasswing expansion countries (2 Jun 2026) — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/); TCS appears as an AWS Continuum customer — [AWS Continuum](https://aws.amazon.com/continuum/); no Indian security vendor confirmed in any gated programme.
- XBOW: used OpenAI GPT-5.6 Sol models (programme not stated) — [XBOW, 2026-10-13](https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users); quoted calling Mythos Preview "a major advance", but not shown as a Glasswing partner — [The Hacker News, 2026-05-23](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html)
- China: Anthropic bars Chinese-controlled companies (since 5 Sep 2025) — [The Decoder](https://the-decoder.com/anthropic-bans-companies-majority-controlled-by-china-russia-iran-and-north-korea-from-claude/) [extract only]; in April 2026 Anthropic reportedly declined a Chinese think-tank member's access request (Wikipedia flags this as failed verification) — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- Chinese substitutes: 360 Security unveiled "Yitian Tulong" at ISC.AI 2026 — Tulongfeng (vulnerability discovery, "China's version of Mythos") and Yitianzhen (automated defence and IR); Tulongfeng reportedly found 3,432 vulnerabilities, 105 confirmed by Chinese authorities; Zhou Hongyi: "domestic models still have a 20%-30% gap in base capability"; Reuters "could not independently verify the claims" — [Insurance Journal (Reuters), 2026-06-26](https://www.insurancejournal.com/news/international/2026/06/26/875418.htm); Qi An Xin's chairman (2 Jun 2026 keynote) favoured a "three-in-one vertical defense upgrade framework" over a domestic Mythos-equivalent; Chinese experts estimated in April 2026 Chinese firms could match Mythos "within months" — [Natto Thoughts, 2026-08-26](https://www.nattothoughts.com/p/from-the-frontier-ai-arms-race-to)

### Inferences
- The gated programmes reinforce scale: the three largest US platforms appear in every programme, while mid-cap specialists (Zscaler, SentinelOne, Rapid7, Qualys) do not appear in any published list. This may reflect unpublished membership rather than exclusion.
- Non-US access is mostly via consultancies (Capgemini, Big Four networks), Japanese conglomerates and Korean chaebols, and is subject to the US government's gate (June directive; Specialized Access vetted with the US government).

### Gaps
- No evidence either way for Zscaler, SentinelOne, Rapid7, Qualys, Snyk, Socket, Bugcrowd, Claroty, Armis/ServiceNow, Nozomi Networks/Mitsubishi Electric; for Taiwanese vendors; for Israeli vendors other than Wiz and (unconfirmed) Check Point; or for other European specialists (e.g. Thales, Airbus) — absence from published lists is not proof of non-participation.
- Sangfor, NSFOCUS and Chaitin's AI tools, and Chinese labs' (DeepSeek, Qwen) use by Chinese security vendors, were not covered.

---

## 8. Does access differ by country?

### Takeaway
Yes, in three layers: (1) company policy (Anthropic's Sept 2025 ban on Chinese/Russian/Iranian/North Korean-controlled firms; CVP's "risk of diversion or compelled access" factor); (2) programme design (Glasswing's June expansion limited to ~15 "friendly to the U.S." countries; Specialized Access vetted with the US government; OpenAI and Google publish no country rules but select partners themselves); and (3) US government action (the 12–30 Jun 2026 Commerce directive cut all foreign-national access to Mythos 5/Fable 5). As of Sept 2026 Korean access was still disputed.

### Cited Findings
- Anthropic policy, 5 Sep 2025 (majority-control test incl. overseas subsidiaries) — [The Decoder](https://the-decoder.com/anthropic-bans-companies-majority-controlled-by-china-russia-iran-and-north-korea-from-claude/) [extract only]
- CVP eligibility weighs "the legal and regulatory environment" and "the risk of diversion or compelled access"; Specialized Access reviewed "in collaboration with the US government" (6 Oct 2026) — [Unite.AI](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/)
- Glasswing 2 Jun 2026 expansion: 15+ countries "friendly to the U.S." — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- US Commerce directive (12 Jun 2026) on "any foreign national, whether located abroad or inside the United States"; lifted 30 Jun with access for certain "trusted partners"; international Glasswing expansion to proceed "with the government" — [Tech Policy Press](https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/); [CNBC, 2026-06-30](https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html)
- Korea (17 Sep 2026): no Korean company or institution can use Mythos yet "as far as he knows" (PANW Korea CEO) — [The Elec](https://www.thelec.net/news/articleView.html?idxno=14029)
- Japan: Hitachi's access "expected to be granted later" after signing (Jun 2026) — [Uravation](https://uravation.com/media/hitachi-trendmicro-claude-mythos-project-glasswing-japan-2026/)
- OpenAI Daybreak (Aug 2026) and GPT-6 Cyber (Nov 2026) coverage mentions no country rules — [Tahawul Tech](https://www.tahawultech.com/news/openai-expands-daybreak-cyber-programme-and-partner-network/); [CyberScoop](https://cyberscoop.com/openai-gpt-6-cyber-security-model/); Fairwind states no country restrictions and calls itself global — [DeepMind](https://deepmind.google/fairwind-program/); [Google blog, 2026-09-02](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)

### Inferences
- A non-US vendor's access to Mythos-class capability is contingent on both Anthropic and Washington; OpenAI's and Google's gated models have not (publicly) faced a similar directive, but the June precedent makes that a live risk. US vendors therefore hold a structural access advantage that is policy-made, not merit-made.

### Gaps
- Whether OpenAI or Google apply nationality screening in Daybreak Red or Fairwind, and the current status of Korean, Indian and Japanese Mythos access after September 2026.

---

## 9. Market reaction: security-vendor share prices and valuations after model-maker security launches; analyst commentary

### Takeaway
The pattern is a sharp sell-off on the first headline followed by recovery: Claude Code Security (20 Feb 2026) knocked CrowdStrike −8%/Zscaler −5.5% on the day (−11.6%/−11.3% by 23 Feb) and the Global X Cybersecurity ETF to its lowest close since Nov 2023; the Mythos leak (late March) cut leading names 5–11%; but Glasswing day (8 Apr) saw gains, and from 7 Apr to 18 Sep 2026 broad platforms soared (Okta +130.7%, Fortinet +102%, Zscaler +40%), with Glasswing members CrowdStrike and Palo Alto among the top four. Around GPT-6 Cyber (5 Nov 2026) security stocks fell 8–11% in one session, but the coverage attributes it to a wider AI-trade unwind. Analysts largely called the model-maker scare an overreaction and increasingly frame the labs as suppliers.

### Cited Findings
- 20 Feb 2026 (Claude Code Security): CrowdStrike −8%, Zscaler −5.5%; Global X Cybersecurity ETF lowest close since Nov 2023 — [Bloomberg, 2026-02-20](https://www.bloomberg.com/news/articles/2026-02-20/cyber-stocks-slide-as-anthropic-unveils-claude-code-security) [extract only, paywall]; same day Cloudflare −8.1%, Okta −9.2%, SailPoint −9.4%; JFrog fell nearly 25% (date not given) — [Simply Wall St, 2026-10-23](https://simplywall.st/article/ai-has-flipped-the-story-on-cybersecurity-stocks-twice)
- By 23 Feb 2026: CrowdStrike −11.6%, Zscaler −11.3%, Palo Alto −3.2%; Wedbush: the release "has caused chaos on the cybersecurity sector", "it will prove to be the wrong reaction in the long-term for clear winners such as Palo Alto", CrowdStrike's position "remains firmly unchanged", and other labs including OpenAI are expected to follow — [Yahoo Finance/Proactive, 2026-02-23](https://finance.yahoo.com/news/anthropic-claude-code-security-launch-200400637.html); CrowdStrike's cumulative fall reached ~18% per one report — [TradingView/Cointelegraph](https://www.tradingview.com/news/cointelegraph:b5cdf0b39094b:0-cybersecurity-stocks-fall-after-anthropic-unveils-claude-code-security/) [extract only]
- Barclays reportedly called the sell-off "illogical" because Claude Code Security scans code in development rather than competing with runtime protection [low-quality secondary] — [blog citing Barclays](https://wilsonkumalo.dev/blog/claude-code-security-triggers-historic-cybersecurity-stock-collapse-when-ai-becomes-the-disruption-1772015112869) [extract only]
- Mythos leak (Fortune report, late March 2026): CrowdStrike, Palo Alto Networks, Zscaler, SentinelOne, Okta, Netskope and Tenable fell 5–11% — [Fortune, 2026-04-07](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/); iShares Cybersecurity ETF −4.5% after the 26 Mar leak — [Forbes, 2026-04-14](https://www.forbes.com/sites/jonmarkman/2026/04/14/how-claude-mythos-wiped-billions-out-of-cybersecurity-stocks/) [extract only]
- 8 Apr 2026 (day after Glasswing): CrowdStrike +3.5% (after a stronger prior-session gain), Palo Alto nearly +3%; Zscaler, Cloudflare, Okta, Fortinet, Check Point "notable gains" — [TipRanks, 2026-04-08](https://www.tipranks.com/news/cybersecurity-stocks-rally-as-anthropic-debuts-project-glasswing)
- 7 Apr → 18 Sep 2026 (15 vendors examined): Okta +130.7% (to $32B value); Fortinet +102% ($124.1B); Cloudflare nearly +50%; Zscaler +40% ($32.5B); CrowdStrike second-largest gain, Snowflake third, Palo Alto fourth; Check Point the only decliner; early-2026 fears that labs would displace vendors described as unfounded — [BankInfoSecurity/ISMG, 2026-09-18](https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191)
- 10 Aug 2026: "CrowdStrike, Palo Alto hit records after Black Hat cyber conference illuminates rising AI threat" — [CNBC, 2026-08-10](https://www.cnbc.com/2026/08/10/crowdstrike-palo-alto-stock-black-hat.html) [headline]
- Sep 2026 (Amodei essay and Altman response): CrowdStrike and Zscaler +12%, Palo Alto +11%; early Oct 2026 (reported OpenAI–Trail of Bits talks): Palo Alto −4%, CrowdStrike −3% — [Simply Wall St, 2026-10-23](https://simplywall.st/article/ai-has-flipped-the-story-on-cybersecurity-stocks-twice)
- 2 Nov 2026: CrowdStrike −3%, Fortinet −3%, Palo Alto −2% while the Nasdaq-100 rose 0.6% — [24/7 Wall St, 2026-11-02](https://247wallst.com/investing/2026/11/02/crowdstrike-slides-3-despite-deutsche-bank-upgrade-and-coreweave-deal-fortinet-falls-3-palo-alto-drops-2/) [headline/extract]
- 5 Nov 2026 (GPT-6 Cyber launch day): CrowdStrike −10% intraday "with no news of its own", Palo Alto −8%, Zscaler −9%, Cloudflare −11%, Nasdaq-100 −5% as "investors unwound the AI trade"; the article does not cite model-maker launches; forward P/E CrowdStrike 171x (4 Nov close; ~156x intraday), Palo Alto 84x, Zscaler 46x, Cloudflare 179x; CrowdStrike agreed to buy AI-agent security startups Fiddler and Dreadnode for ~$495M combined; Palo Alto reportedly in talks for Clutch Security (~$500M) — [Yahoo Finance, 2026-11-05](https://finance.yahoo.com/markets/stocks/articles/crowdstrike-sinks-9-palo-alto-181856889.html)
- Supplier framing: many security companies build AI features on the same labs' models, making the labs partly suppliers; unnamed analysts called the February sell-off "excessive" and "a panic-driven, narrative-led selloff"; Palo Alto's and CrowdStrike's CEOs: "AI didn't eliminate the need for security, it actually increased it" — [Simply Wall St](https://simplywall.st/article/ai-has-flipped-the-story-on-cybersecurity-stocks-twice)

### Inferences
- The market punished code-security and identity names most on the Claude Code Security headline (JFrog, SailPoint, Okta), then rewarded broad platforms that became lab partners; inclusion in the gated programmes appears to have been read as a positive signal. The 5 Nov drop coincides with GPT-6 Cyber but no source links the two.
- Stretched multiples (CrowdStrike ~156–171x forward P/E, Cloudflare 179x on 4–5 Nov 2026) leave platform stocks sensitive to any renewed "labs as competitors" headline.

### Gaps
- No exact closing-price series was retrieved; percentages are as reported and mix intraday and close.
- No data were found on private-market valuations of security startups (e.g. XBOW, Socket, Snyk) reacting to model-maker launches; Gemini 4 Carbon and the kernel report produced no traceable stock reaction in the sources found.

---

## 10. How much competitive threat do model makers pose to each sub-segment?

### Takeaway
The threat is highest where the model itself does the work and the output can be checked automatically — automated vulnerability discovery and repair, SAST-style code security, and penetration testing/bug bounty — and lowest where the vendor owns telemetry, device access or physical constraints (detection and response at scale, OT/IoT shielding). Exposure management is contested because Google owns Wiz and AWS builds context graphs. Machine-checked verification is complementary rather than threatened.

### Cited Findings
- Discovery and repair: all three labs and both hyperscalers now ship it — Claude Security (Mythos, beta, token cost) — [Claude Help Center](https://support.claude.com/en/articles/14661296-use-claude-security); Codex Security Cloud (29 Sep 2026) — [eesel](https://www.eesel.ai/blog/codex-security-cloud); CodeMender/Project Fortify — [Google blog, 2026-11-10](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/); AWS Continuum — [AWS](https://aws.amazon.com/continuum/); Microsoft MDASH scanner and Perception — [Microsoft FY27 Q1 call](https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1)
- Code and supply-chain security: JFrog fell nearly 25% and SailPoint −9.4% after Claude Code Security — [Simply Wall St](https://simplywall.st/article/ai-has-flipped-the-story-on-cybersecurity-stocks-twice); GitHub Advanced Security revenue +50% YoY (28 Oct 2026) — [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1)
- Penetration testing and bug bounty: Daybreak Red targets "penetration testing and red teaming" — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); CVP Red Team Access adds "authorized penetration testing" — [Unite.AI](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/); AWS "Continuum for penetration testing" accelerates testing "from weeks to hours" — [AWS](https://aws.amazon.com/security-agent/); HackerOne paused the Internet Bug Bounty (Mar 2026), curl ended its HackerOne programme (Jan 2026; >95% AI-generated junk), Google cut Chrome bounties (30 Apr 2026); HackerOne's CEO: "The total value of the bounty market is growing, not shrinking" — [SecurityWeek, 2026-06-09](https://www.securityweek.com/will-ai-kill-the-bug-bounty-industry/)
- Exposure management: Google owns Wiz (closed 11 Mar 2026) — [TechCrunch](https://techcrunch.com/2026/03/11/google-completes-32b-acquisition-of-wiz/); HackerOne frames Mythos within an "exposure management lifecycle"; its critical MTTR improved >50% while the unresolved critical backlog grew 29x over 12 months (platform data) — [HackerOne, 2026-09-21](https://www.hackerone.com/press-release/hackerone-bring-anthropics-mythos-exposure-management-lifecycle-discovery-verified)
- OT/IoT: Mythos Preview did not complete AISI's "Cooling Tower" OT range (stuck on IT sections) — [UK AISI, 2026-04-13](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities); CSA notes power, water and healthcare patches may need regulatory approval or downtime — [CSA](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity); Dragos is an OpenAI evaluation partner — [CyberScoop](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)
- Detection and response: Daybreak partners include CrowdStrike, PANW (Unit 42) and Sophos MDR ("frontier-grade defense at scale to organizations unable to deploy these models on their own") — [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); Microsoft Defender sim-ships protections for AI-discovered vulnerabilities — [Microsoft FY26 Q3](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- Machine-checked verification: CodeMender validates with SMT solvers, fuzzing and differential testing — [DeepMind, 2025-10-06](https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/)

### Inferences (suggested threat ratings, as of 2026-11-12)
| Sub-segment | Threat from model makers | Why (evidence above) |
|---|---|---|
| Automated vulnerability discovery and repair | **High** | Labs own the gated models and sell scanners at token cost; hyperscalers bundle; vendors' edge narrows to validation, workflow and remediation plumbing |
| Code and supply-chain security | **High (SAST-like); medium (supply-chain/SCA)** | Direct product overlap (Claude/Codex Security, GHAS); supply-chain tools depend on registry/package telemetry the labs do not obviously own (no lab supply-chain product found) |
| Exposure management | **Medium** | Google owns Wiz; AWS Continuum builds environment graphs; others lack asset inventories and scanner footprints |
| OT/IoT shielding | **Low** | Models struggle on OT ranges; unpatchable devices raise demand for segmentation/shielding; labs partner (Dragos) rather than compete |
| Detection and response | **Low from OpenAI/Anthropic; high from Microsoft/Google as incumbents** | Telemetry and endpoint presence are not provided by models; labs supply partners |
| Penetration testing and bug bounty | **High** | Red tiers and AWS pentest agents substitute for billable hours; bounty programmes are already strained |
| Machine-checked verification | **Low (complementary)** | Verifiers act as the "judge" that makes AI output trustworthy; labs use them rather than sell them |

### Gaps
- No market-share data by sub-segment or dated analyst rankings were retrieved, so the ratings are judgements on product overlap, not measured share shifts.

---

## 11. Do defenders or attackers gain more from the same models? Company statements vs independent evidence

### Takeaway
Every model maker claims a defender advantage if patch cycles shrink, and all now concede attackers will get similar capability within months. Independent evidence so far shows discovery has outrun repair: ~6% of Glasswing's disclosed findings were patched by late May 2026 and ~10% of discovered flaws disclosed and <1% fixed by September (per Dark Reading via Wikipedia); open-weight models trail by four to eight months at ~100x lower cost. Whether the gated head start nets out for defenders depends on remediation capacity, not discovery.

### Cited Findings
**Company statements**
- Anthropic (7 Apr 2026): Mythos "presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders"; "The work of defending the world's cyber infrastructure might take years"; Anthropic privately warned officials large-scale attacks were significantly more likely in 2026 (per Axios) — [Fortune](https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/)
- Anthropic (May 2026): the challenge is "the relative ease of finding vulnerabilities compared with the difficulty of fixing them"; "Network defenders should shorten their patch testing and deployment timelines" — [The Hacker News](https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html); (2 Jun) expects other companies soon to build comparable models — [TechCrunch](https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/)
- OpenAI (Nov 2026): for now a low-privileged account on an unpatched system "should be considered functionally equivalent to root access" for a well-resourced actor — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145)
- Google (2 Sep 2026): Fairwind "gives trusted defenders a vital adaptation window"; "The defender's edge comes from shrinking the time between detecting a flaw and patching it" — [Google blog](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/); (15 Jul 2025) AI can "give the advantage back to security defenders" — [Google blog](https://blog.google/technology/safety-security/cybersecurity-updates-summer-2025/)
- Microsoft (29 Apr 2026): "AI compresses the window between vulnerability and exploitation" — [Microsoft FY26 Q3](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3)
- Moonshot (Oct 2026): gradual diffusion of cyber capability "ultimately makes all software more secure" — [blog mirror](https://github.com/kakon77777-commits/agiright-evidence/blob/6224a57aa54fc716328ca87fa37accddc6801068/sources/2026-10-24/kimi.txt) [lead, not re-verified]; Qi An Xin's chairman (2 Jun 2026): AI has worsened the offence–defence imbalance — [Natto Thoughts](https://www.nattothoughts.com/p/from-the-frontier-ai-arms-race-to)

**Independent evidence**
- UK AISI (13 Apr 2026): Mythos Preview 73% on expert CTFs; first model to finish AISI's 32-step TLO range (3 of 10 attempts; avg 22 steps vs 16 for Opus 4.6); ranges lacked active defenders, so "we cannot say for sure whether Mythos Preview would be able to attack well-defended systems"; capabilities "dual use" — [UK AISI](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities)
- CSA (data to 22 May 2026): 97 of 1,596 disclosed findings patched (~6%); bottleneck "has shifted from vulnerability discovery to vulnerability remediation"; maintainers asked Anthropic to slow disclosures; median disclosure-to-weaponised-exploit time fell from 771 days (2018) to single-digit hours; 28.3% of CVEs exploited within 24 hours; an early-2026 AI-orchestrated campaign scanned 2,516 FortiGate targets in 106 countries and compromised >600 devices — [CSA](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity)
- Dark Reading (9 Sep 2026, citing Patrick Garrity): only ~10% of discovered flaws disclosed and under 1% fixed — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]
- SecurityWeek (9 Jun 2026): bug discovery is "cheap and abundant", triage and remediation scarce; half of one hunter's ten AI-found bugs were duplicates — [SecurityWeek](https://www.securityweek.com/will-ai-kill-the-bug-bounty-industry/)
- Kernel: of 948 OpenAI-claimed flaws, 61 patched, 43 staging, 299 under discussion at scan end — [iTnews](https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145)
- Open-weight lag and cost: four to seven months, ~100x cheaper, safeguards largely ineffective — [CSA, 2026-07-31](https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/); DeepSeek V4 ~8 months behind — [NIST CAISI](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro); GLM-5.3 ~4 months — [CASRAI](https://casrai.org/guides/caisi-open-weight-model-cyber-assessments)
- Gate leakage: unauthorised Mythos access via Discord reported 21 Apr 2026 — [Wikipedia: Claude Mythos](https://en.wikipedia.org/wiki/Claude_Mythos) [secondary]

### Inferences
- On current evidence, attackers gain at least as much as defenders in the short run: discovery has scaled by orders of magnitude while confirmed fixes number in the tens to low hundreds per campaign. Defenders' advantage is real only where the vendor closes the loop to a deployed fix (the "judge" plus remediation), which is why validation and remediation vendors look better placed than pure finders.

### Gaps
- No independent study measuring net offence-versus-defence effect (e.g. exploitation incidence attributable to AI-found bugs vs bugs fixed) was found. AISI's investigation of Mythos 5 taking unsanctioned actions in a July 2026 cyber test (published 23 Oct 2026) is a lead from earlier notes, not re-verified here — [AISI](https://www.aisi.gov.uk/blog/investigating-alignment-failures-in-aisis-incident).

---

## 12. Common-framework assessment of each model maker's security business (quality tests, path forward, entry point)

### Takeaway
Judged as security businesses, OpenAI and Anthropic hold the strongest *position* (they own the gated models and the gates) but have no disclosed security revenue and the weakest resilience (private or just-listing, heavy commitments, exposed to US export action). Google and Microsoft have the broadest owned security franchises and strong finances but their security businesses are small slices of very large parents and include labour (Mandiant) or per-seat (E5) models. AWS is a fast-moving distributor dependent on others' models. Meta and the Chinese labs are not security businesses; they shape the threat by releasing open weights.

### Cited Findings
- OpenAI: gated models GPT-5.4/5.5/5.6/6 Cyber, Critical rating, 16 Daybreak partners, $1B grant programme (Nov 2026) — [TestingCatalog](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/); [Help Net Security](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/); independent ranking: GPT-5.5 led CAISI's CTF-Archive-Diamond at 71% vs Opus 4.6 46% (Apr 2026 evaluation) — [NIST CAISI](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro); outside-validated outcome: XBOW's Chrome chain built on GPT-5.6 Sol paid by Google — [XBOW](https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users)
- Anthropic: AISI ranked Mythos Preview first on cyber ranges (13 Apr 2026) — [AISI](https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities); independent firms found 90.6% of 1,752 assessed Glasswing findings valid — [CSA](https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity); Mozilla patched 271 Firefox bugs — [Wikipedia](https://en.wikipedia.org/wiki/Claude_Mythos); financials and IPO — [CNBC, 2026-11-10](https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html)
- Google: Wiz $32B, >$1B ARR (2025, unnamed source) — [TechCrunch](https://techcrunch.com/2026/03/11/google-completes-32b-acquisition-of-wiz/); Q3 2026 Cloud $30.7B revenue, 36.2% margin, Alphabet FCF −$9.1B — [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/); Fairwind >650 partners (Sep 2026) — [Google blog](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)
- Microsoft: >$20B security revenue (CY2022) — [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q2); 1.6M security customers (Jan 2026) — [Microsoft](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2); FY2026 revenue $331.8B, CFO $182.9B — [8-K](https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm)
- AWS: Q3 2026 revenue $46.0B, 38.7% margin, Continuum customers named — [Motley Fool](https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/)

### Inferences (suggested assessments; inferences, not advice)

**OpenAI (security business)**
- (a) Position: owns gated frontier cyber models and the Daybreak gate — the strongest position in the framework; its judges are execution-based (VM reproduction, sandboxed exploit validation) but the final judge (maintainers accepting patches) is outside its control.
- (b) Lead (outside evidence only): CAISI benchmark lead for GPT-5.5 (Apr 2026); Google's paid bounty on a GPT-5.6-built chain (Oct 2026); Mozilla's severity rating of 81 Firefox bugs. No market-share data.
- (c) Revenue model: usage/credit-based (tokens, Daybreak credits); no seats or hours; security revenue undisclosed.
- (d) Financial strength: undisclosed profitability; fast revenue growth (Q3 2026 annualised +70% QoQ per Brockman); cannot assess margins, FCF or concentration.
- (e) Resilience: steady growth (~55%): scales with compute and Daybreak partners; financing-led pause around 2028 (~25%): most exposed group with Anthropic (private, compute-heavy); faster acceleration (~20%): capability up but tighter government gating likely. Export-control exposure: high (June 2026 precedent applied to a peer).
- Transitions: (1) yes — Red tier and partners substitute for pentest hours; (2) yes — Codex Security and kernel pipeline; (3) partly — planned critical-infrastructure Red group, Dragos; (4) it is the supplier; (5) not addressed; (6) not addressed in security. Said vs done: shipped four cyber models, Codex Security (preview), 16 partners, $1B grants, $1.2M kernel run; not done: GA product with price, disclosed revenue, acquisitions. Must go right: patch acceptance by maintainers; no government gating shock; partners not defecting to rivals. **Verdict: coherent** (product, access and partner channel line up), with commercialisation unproven.
- Entry point: private; IPO "ready" in 2027 per Brockman (not committed); listed route via Microsoft (~27% as-converted, Oct 2025), which dilutes heavily. **Label: cannot assess.**

**Anthropic (security business)**
- (a) Position: owns Mythos and the CVP gate; Claude Security includes multi-stage verification but Anthropic does not own the final judge; the gate is co-held with the US government for the top tier.
- (b) Lead: AISI's first-place ranking (Apr 2026); CSA's 90.6% validity of assessed findings; Mozilla's 271 patches. Microsoft claims a cheaper model beats Mythos [unconfirmed].
- (c) Revenue model: token-based usage (Claude Security at token cost; Mythos $8/$40 for 5.2), but premium Enterprise seats required — mixed seat/usage.
- (d) Financial strength: 9M 2026 revenue $33.24B, net loss $104B (largely non-cash), ~$81B run-rate; up to $64B IPO proceeds plus $26B placement; reported purchase commitments $895.4B (headline only).
- (e) Resilience: steady growth: strong; 2028 pause: high fixed commitments are a risk; acceleration: capability lead but more gating. Export-control exposure: demonstrated (12–30 Jun 2026 global suspension).
- Transitions: (1) yes (Red Team tier); (2) yes (Claude Security continuous scans, OSS Scanner); (3) partly (Specialized Access for grids/flight systems); (4) it is the supplier; (5) not addressed; (6) indirect. Said vs done: $100M credits, ~200 organisations, CVP tiers, Claude Security beta with free credits; not done: GA, disclosed security revenue. Must go right: government relations, gate integrity (April leak), remediation throughput. **Verdict: coherent**, but contingent on Washington.
- Entry point: IPO expected to price 18 Nov 2026 at $70–78 (up to $1.405T fully diluted, ~17x run-rate revenue); listed indirect holders Amazon and Alphabet; security share of revenue unknown. **Label: stretched** on whole-company numbers; security exposure itself **cannot assess**.

**Google/Alphabet (security business: Wiz, Mandiant, GTI, SecOps, DeepMind agents)**
- (a) Position: mixed — owns gated models (Carbon for cyber) and a judge-rich repair agent (CodeMender), plus Wiz's exposure graph; Mandiant consulting is billable hours (weakest element).
- (b) Lead: Wiz >$1B ARR (2025, unnamed source) and $32B price; no outside cyber benchmark of Carbon; no analyst ranking retrieved.
- (c) Revenue model: subscriptions/consumption (Cloud, Wiz) plus services hours (Mandiant); shares undisclosed.
- (d) Financial strength: Cloud operating margin 36.2% (Q3 2026); Alphabet FCF −$9.1B in Q3 2026 on $51.4B capex.
- (e) Resilience: strong in steady growth; capex-heavy in a pause; Fairwind global with no published country rules.
- Transitions: (1) partly (Mandiant hours → Gemini agents); (2) yes (CodeMender, Fortify); (3) partly (critical-infrastructure priority); (4) supplier; (5) not found; (6) yes in research (CodeMender's SMT/fuzzing; formal-verification work, lead only). **Verdict: coherent** at product level; partly coherent commercially (no disclosure).
- Entry point: Wiz is <1% of Cloud revenue and ~0.2% of Alphabet's; exposure extremely diluted. **Label: cannot assess** (security-specific).

**Microsoft (security business)**
- (a) Position: owns identity (Entra), endpoint (Defender), SIEM (Sentinel), data (Purview), code (GHAS) and its own cyber model; telemetry is a constraint AI does not remove.
- (b) Lead: company metrics only (1.6M customers); no outside ranking retrieved.
- (c) Revenue model: mostly per-user suites (E5/E7) plus consumption add-ons (Security Copilot, Perception).
- (d) Financial strength: FY2026 operating income $155.2B, CFO $182.9B.
- (e) Resilience: high across scenarios; seat model exposed if agents reduce human headcount.
- Transitions: (1) partly (Perception red-team agents); (2) yes (MDASH, sim-shipped Defender protections); (3) not found; (4) hedged via own models; (5) not found; (6) not found. **Verdict: coherent.**
- Entry point: security ≥ ~6% of revenue if still ~$20B (no recent figure); diluted. **Label: cannot assess** (security-specific).

**Amazon/AWS (security business)**
- (a) Position: distributor/integrator; model-agnostic; dependent on others' gated models; strength is AWS context.
- (b) Lead: named customers only; no outside evidence.
- (c) Revenue model: presumably usage-based (price unpublished).
- (d) Financial strength: AWS Q3 2026 operating income $17.8B, backlog $578B.
- (e) Resilience: hedged across models; exposed to labs' and US gates.
- Transitions: (1) yes (pentest agent); (2) yes (Continuum); (4) dependent; others not found. **Verdict: partly coherent** (new, unpriced, dependent).
- Entry point: negligible share of Amazon. **Label: cannot assess.**

**Meta; Chinese labs**
- No commercial security business found; Meta provides open benchmarks/guardrails, Chinese labs provide open weights that narrow the attacker gap. **Verdict: not applicable / not coherent as a security business. Label: cannot assess.**

### Gaps
- Market-share data, dated analyst rankings and audited security revenue for any model maker were not retrieved; quality test (b) rests on evaluator results and partner outcomes, not share.

---

## 13. Summary tables: gated programmes × confirmed participants; per-model-maker scorecard; dated source list

### Takeaway
Three gated programmes matter (Anthropic Glasswing/CVP, OpenAI TAC/Daybreak, Google Fairwind); Microsoft, AWS and Meta run no comparable external gated cyber-model programme found. The overlap of named security vendors across programmes is concentrated in Palo Alto Networks, CrowdStrike and Cisco.

### Cited Findings

#### Table A — Gated programmes × confirmed security-vendor participants
| Programme (owner) | Gated model(s) and dates | Eligibility (summary) | Confirmed security-vendor participants (source, date) | Other named participants | Country notes |
|---|---|---|---|---|---|
| Project Glasswing → Cyber Verification Program, 3 tiers (Anthropic) | Mythos Preview 7 Apr 2026; Mythos 5 9 Jun; 5.1 1 Sep; 5.2 9 Nov 2026; CVP tiers 6 Oct 2026 | Critical-software orgs; Defense (individuals on paid plans, orgs), Red Team (orgs), Specialized (orgs, US-government-vetted) | CrowdStrike, Palo Alto Networks, Cisco, Broadcom ([Anthropic, 2026-04-07](https://www.anthropic.com/glasswing)); Okta (27 May / 2 Jun 2026, [BankInfoSecurity](https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191)); Trend Micro (3–4 Jun 2026, [Uravation](https://uravation.com/media/hitachi-trendmicro-claude-mythos-project-glasswing-japan-2026/)); Booz Allen ([Unite.AI, Oct 2026](https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/)); Rubrik (tester, [Anthropic, 2026-11-09](https://www.anthropic.com/claude-fable-and-mythos-5-2)); HackerOne integration announced ([HackerOne, 2026-09-21](https://www.hackerone.com/press-release/hackerone-bring-anthropics-mythos-exposure-management-lifecycle-discovery-verified)) | AWS, Apple, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA; Mozilla; Comcast; Samsung, SK Hynix, SK Telecom, NATO, ENISA (FT, 2 Jun); Hitachi (Jun 2026); KISA (reported) | Chinese-controlled firms barred (Sep 2025); expansion to ~15 US-friendly countries; all foreign-national access suspended 12–30 Jun 2026; Korean access disputed (Sep 2026) |
| Trusted Access for Cyber → Daybreak Blue/Red + Cyber Partner Program (OpenAI) | TAC 5 Feb 2026; GPT-5.4-Cyber 14–15 Apr; GPT-5.6-Cyber by 10 Aug; GPT-6 Cyber 5 Nov 2026 | Identity-verified defenders (Blue); approved orgs for exploit work (Red); security firms/consultancies (partners); hardware keys for individuals from 1 Sep 2026 | Palo Alto Networks (Unit 42), CrowdStrike, Cisco, Sophos, Akamai, Fortinet, Cloudflare, NCC Group, SpecterOps ([Help Net Security, 2026-08-11](https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/)); GPT-6 Cyber users PANW, Cisco, Calif, CodeRabbit ([TestingCatalog, 2026-11-05](https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/)); Dragos (evaluation partner, [CyberScoop, 2026-11-05](https://cyberscoop.com/openai-gpt-6-cyber-security-model/)). Unconfirmed: Check Point, Tenable, HackerOne, Elastic, Proofpoint (partners page, 403) | Accenture, IBM, Capgemini, Cognizant, EY, KPMG, PwC; Mozilla | No published country rules |
| Fairwind Program (Google DeepMind) | Gemini 3.8 Flash Cyber + CodeMender (by 2 Sep 2026); Argon to trusted defenders 1 Oct; Carbon 28 Oct; "Carbon for cyber" Fairwind-only after 10 Nov 2026 | Governments, national cyber authorities, critical infrastructure, core tech platforms, defensive academic labs; vetting incl. background checks; via Cloud account team | CrowdStrike, Palo Alto Networks, Wiz, Menlo Security, Datadog, Snowflake, Armadin, Center for Internet Security ([DeepMind Fairwind page, read 2026-11-12](https://deepmind.google/fairwind-program/); [Google blog, 2026-09-02](https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/)) | Accenture, Deloitte, McKinsey, Robinhood; >650 partners (Sep 2026) / "thousands" (page) | No published country rules; "global" |
| Llama Defenders Program (Meta) | Not a gated cyber model; early-access/closed tools (29 Apr 2025) | "Select partners" | None named as security vendors; CrowdStrike co-developed CyberSOC Eval ([Meta, 2025-04-29](https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/)) | ZenDesk, Bell Canada, AT&T | — |
| Microsoft / AWS | No external gated cyber-model programme found; Microsoft Perception preview (KPMG, Nationwide BS, Northern Trust, Stellantis; [Oct 2026](https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1)); AWS Continuum customers (Capital One, IBM, Infor, Luminate, Robinhood, TCS, HENNGE; [AWS](https://aws.amazon.com/continuum/)) | — | — | — | — |

#### Table B — Vendor check (✔ confirmed; ? reported/unconfirmed; — none found)
| Vendor (HQ) | Anthropic Glasswing/CVP | OpenAI TAC/Daybreak | Google Fairwind |
|---|---|---|---|
| Palo Alto Networks (US) | ✔ (Apr 2026) | ✔ partner + GPT-6 Cyber user | ✔ |
| CrowdStrike (US) | ✔ (Apr 2026) | ✔ partner | ✔ |
| Cisco (US) | ✔ (Apr 2026) | ✔ partner + GPT-6 Cyber user | — |
| Fortinet (US) | — | ✔ partner | — |
| Zscaler (US) | — | — | — |
| Check Point (Israel) | — | ? (partners page extract) | — |
| SentinelOne (US) | — | — | — |
| Trend Micro (Japan) | ✔ (Jun 2026) | — | — |
| Tenable (US) | — | ? | — |
| Rapid7, Qualys, Snyk, Socket (US) | — | — | — |
| XBOW (US) | — (uses public OpenAI models) | — | — |
| HackerOne (US) | ✔ Mythos integration announced (Sep 2026) | ? | — |
| Bugcrowd (US) | — | — | — |
| Claroty, Armis/ServiceNow, Nozomi/Mitsubishi Electric | — | — | — |
| Dragos (US) | — | ✔ evaluation partner (Nov 2026) | — |
| Okta (US) | ✔ (May–Jun 2026) | — | — |
| Sophos, NCC Group (UK) | — | ✔ partners | — |
| Wiz (Israel-founded; Google) | — | — | ✔ |
| Korean vendors (AhnLab etc.) | — (Samsung/SK/KISA named; access disputed) | — | — |
| Indian, Taiwanese vendors | — | — | — |
| Chinese vendors (360, QAX) | Excluded by policy | — | — |

#### Table C — Per-model-maker scorecard (suggested, as of 2026-11-12)
| Model maker | (a) Position | (b) Lead (outside evidence) | (c) Revenue model | (d) Financial strength | (e) Resilience / export exposure | Transitions applying | Verdict | Entry point & label |
|---|---|---|---|---|---|---|---|---|
| OpenAI | Strongest: owns gated models + gate | CAISI benchmark lead (Apr 2026); Google bounty on GPT-5.6-built chain; Mozilla ratings | Usage/credits | Undisclosed | Weak in 2028 pause; high export risk | 1, 2, 3 (partly), 4 | Coherent | Private; IPO 2027 (not committed); via MSFT ~27% — cannot assess |
| Anthropic | Strongest: owns Mythos + CVP gate (top tier US-vetted) | AISI #1 (Apr 2026); CSA 90.6% valid; Mozilla 271 patches | Usage + premium seats | Rev $33.2B 9M; loss $104B (non-cash heavy); IPO proceeds | Weak in pause; export risk demonstrated | 1, 2, 3 (partly), 4, 6 (indirect) | Coherent, gov-contingent | IPO 18–19 Nov 2026, up to $1.405T — stretched (whole co.); security cannot assess |
| Google | Mixed: gated models + Wiz + judge-rich CodeMender; Mandiant hours | Wiz ARR/price; no outside cyber ranking | Subs/consumption + services hours | Cloud 36.2% margin; Alphabet FCF −$9.1B (Q3 2026) | Capex-heavy in pause | 1 (partly), 2, 3 (partly), 4, 6 (research) | Coherent (product); partly (commercial) | Wiz <1% of Cloud — cannot assess |
| Microsoft | Strong: telemetry + identity + own cyber model | None retrieved | Per-user suites + consumption | FY26 op. income $155.2B | High | 1 (partly), 2, 4 (hedged) | Coherent | Security ~6%+ of revenue (2022 figure) — cannot assess |
| AWS | Distributor; model-agnostic; dependent | None | Usage (unpriced) | AWS op. income $17.8B (Q3 2026) | Dependent on others' gates | 1, 2, 4 (dependent) | Partly coherent | Negligible share — cannot assess |
| Meta / Chinese labs | No security business | — | — | — | Open weights shape attacker gap | — | Not applicable | Cannot assess |

### Inferences
- The programme tables show the gates are reinforcing incumbency among a few US platforms and global consultancies; the most exposed vendors are those absent from all three lists in sub-segments the labs now serve directly (code scanning, pentest/bounty).

### Gaps
- Participant lists are partial by design (Anthropic ~200 orgs, Google >650/"thousands", OpenAI "hundreds of teams"); Tables A and B list only names found in public sources as of 12 Nov 2026.

#### Dated source list (publication date; access notes)
- Anthropic — Claude Code Security (2026-02-20): https://www.anthropic.com/news/claude-code-security
- Anthropic — Project Glasswing page (2026-04-07; update 2026-10-06): https://www.anthropic.com/glasswing
- Anthropic — Claude Fable 5.2 and Mythos 5.2 (2026-11-09): https://www.anthropic.com/claude-fable-and-mythos-5-2
- Anthropic — IPO roadshow launch (2026-11-10): https://www.anthropic.com/news/roadshow-launch
- Claude Help Center — Use Claude Security (read 2026-11-12): https://support.claude.com/en/articles/14661296-use-claude-security
- Unite.AI — CVP three tiers (Oct 2026): https://www.unite.ai/anthropic-expands-cyber-verification-program-to-three-access-tiers/
- Google Cloud docs — CVP for Claude (n.d.; extract only): https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/cyber-verification-program
- Fortune — Mythos/Glasswing (2026-04-07): https://fortune.com/2026/04/07/anthropic-claude-mythos-model-project-glasswing-cybersecurity/
- UK AISI — Mythos Preview cyber evaluation (2026-04-13): https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities
- The Hacker News — Glasswing first-month results (2026-05-23): https://thehackernews.com/2026/05/claude-mythos-ai-finds-10000-high.html
- Cloud Security Alliance — Glasswing discovery vs patching (2026-06-07, ambiguous): https://cloudsecurityalliance.org/artifacts/project-glasswing-ai-discovery-outpaces-open-source-patching-capacity
- TechCrunch — Glasswing to 15+ countries (2026-06-02): https://techcrunch.com/2026/06/02/anthropic-scales-claude-mythos-to-critical-infrastructure-in-15-countries/
- CSO Online — Glasswing +150 organisations (2026-06-02): https://www.csoonline.com/article/4180265/anthropic-grants-project-glasswing-access-to-150-more-companies-with-a-focus-on-critical-infrastructure.html
- Tech Policy Press — Mythos export directive (2026-06-15): https://www.techpolicy.press/did-the-us-government-just-set-an-ai-export-precedent-by-blocking-mythos/
- CNBC — Export controls lifted (2026-06-30): https://www.cnbc.com/2026/06/30/anthropic-says-trump-admin-has-lifted-export-controls-on-claude-fable-5-and-mythos-5.html
- CNBC — Anthropic IPO price range (2026-11-10): https://www.cnbc.com/2026/11/10/anthropic-sets-price-range-of-70-to-78-in-upcoming-ipo.html
- Wikipedia — Claude Mythos (read 2026-11-12; secondary): https://en.wikipedia.org/wiki/Claude_Mythos
- Uravation — Hitachi/Trend Micro join Glasswing (Jun 2026; secondary): https://uravation.com/media/hitachi-trendmicro-claude-mythos-project-glasswing-japan-2026/
- The Elec — PANW Korea CEO on Mythos access (2026-09-18): https://www.thelec.net/news/articleView.html?idxno=14029
- CEO Insights Asia — Korea joins Glasswing (n.d.; extract only): https://www.ceoinsightsasia.com/news/korea-joins-anthropic-s-glasswing-for-mytos-ai-model-nwid-14622.html
- HackerOne — Mythos integration (2026-09-21): https://www.hackerone.com/press-release/hackerone-bring-anthropics-mythos-exposure-management-lifecycle-discovery-verified
- The Decoder — Anthropic China-control ban (Sep 2025; extract only): https://the-decoder.com/anthropic-bans-companies-majority-controlled-by-china-russia-iran-and-north-korea-from-claude/
- MediaNama — same (Sep 2025; extract only): https://www.medianama.com/2025/09/223-anthropic-service-policy-update-bans-ai-access-chinese-firms/
- KuCoin flash — regional policy update (n.d.; unverified): https://www.kucoin.com/news/flash/anthropic-updates-regional-usage-rules-chinese-owned-entities-banned-from-using-claude
- OpenAI — Introducing GPT-6 Cyber (2026-11-05; 403): https://openai.com/index/introducing-gpt-6-cyber/
- OpenAI on X — GPT-6 Cyber (2026-11-05; title only): https://x.com/OpenAI/status/2118390190246879554
- OpenAI — Daybreak partners (n.d.; 403, extract only): https://openai.com/daybreak/partners/
- OpenAI — Trusted Access for Cyber (2026-02-05; not opened): https://openai.com/index/trusted-access-for-cyber/
- OpenAI — A thousand fewer paths to root (c. 2026-11-04; not opened): https://openai.com/index/a-thousand-fewer-paths-to-root/
- TestingCatalog — GPT-6 Cyber (2026-11-05): https://www.testingcatalog.com/openai-launches-gpt-6-cyber-for-daybreak-red-customers/
- CyberScoop — GPT-6 Cyber (2026-11-05): https://cyberscoop.com/openai-gpt-6-cyber-security-model/
- Help Net Security — Daybreak partners (2026-08-11): https://www.helpnetsecurity.com/2026/08/11/openai-daybreak-cyber-models/
- Tahawul Tech — Daybreak expansion (2026-08-11): https://www.tahawultech.com/news/openai-expands-daybreak-cyber-programme-and-partner-network/
- Help Net Security — GPT-5.4-Cyber (2026-04-15): https://www.helpnetsecurity.com/2026/04/15/openai-gpt-5-4-cyber/
- SC World — TAC launch (Feb 2026; extract only): https://www.scworld.com/brief/openai-launches-trusted-access-for-cyber-initiative-to-bolster-ai-security
- eesel — Codex Security Cloud (c. Oct–Nov 2026; secondary): https://www.eesel.ai/blog/codex-security-cloud
- iTnews — OpenAI kernel report (2026-11-06): https://www.itnews.com.au/news/low-privileged-accounts-on-unpatched-systems-as-good-as-root-openai-630145
- TechCrunch — Brockman on IPO (2026-11-05): https://techcrunch.com/2026/11/05/openai-president-greg-brockman-says-company-could-be-ipo-ready-in-2027/
- TheStreet — OpenAI CFO on 2027 IPO (n.d.; 403, extract only): https://www.thestreet.com/investing/stocks/openai-cfo-says-ipo-is-in-2027
- MarketScreener/Reuters — OpenAI IPO groundwork (n.d.; extract only): https://www.marketscreener.com/news/openai-lays-groundwork-for-juggernaut-ipo-at-up-to-1-trillion-valuation-ce7d5dd2d089f626
- Microsoft — Next chapter of the Microsoft–OpenAI partnership (2025-10-28): https://blogs.microsoft.com/blog/2025/10/28/the-next-chapter-of-the-microsoft-openai-partnership/
- XBOW — Chrome full-chain bounty (2026-10-13): https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users
- Google — Summer 2025 cybersecurity updates (2025-07-15): https://blog.google/technology/safety-security/cybersecurity-updates-summer-2025/
- Google DeepMind — CodeMender (2025-10-06): https://deepmind.google/discover/blog/introducing-codemender-an-ai-agent-for-code-security/
- Google — Fairwind Program blog (2026-09-02): https://blog.google/innovation-and-ai/technology/safety-security/fairwind-program/
- Google DeepMind — Fairwind page (n.d.; read 2026-11-12): https://deepmind.google/fairwind-program/
- The Hacker News — Argon to trusted defenders (2026-10-01): https://thehackernews.com/2026/10/google-rolls-out-gemini-4-argon-to.html
- Google — Gemini 4 Carbon now available (2026-11-10): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/
- TechCrunch — Google completes Wiz (2026-03-11): https://techcrunch.com/2026/03/11/google-completes-32b-acquisition-of-wiz/
- Motley Fool — Alphabet Q3 2026 call (2026-10-29): https://www.fool.com/earnings/call-transcripts/2026/10/29/alphabet-googl-q3-2026-earnings-call-transcript/
- Microsoft — FY23 Q2 call (2023-01-24): https://www.microsoft.com/en-us/investor/events/fy-2023/earnings-fy-2023-q2
- Microsoft — FY26 Q2 call (2026-01-28): https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q2
- Microsoft — FY26 Q3 call (2026-04-29): https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3
- Microsoft — FY26 Q4 call (2026-07-29): https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q4
- Microsoft — FY27 Q1 call (2026-10-28): https://www.microsoft.com/en-us/investor/events/fy-2027/earnings-fy-2027-q1
- Microsoft — FY26 Q4 earnings release, 8-K Ex. 99.1 (2026-07-29): https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323632/msft-ex99_1.htm
- Microsoft — FY2026 Form 10-K (2026): https://www.sec.gov/Archives/edgar/data/0000789019/000119312526323660/msft-20260630.htm
- Microsoft Research — Project Ire (2025-08-05): https://www.microsoft.com/en-us/research/blog/project-ire-autonomously-identifies-malware-at-scale/
- AWS — Continuum (read 2026-11-12): https://aws.amazon.com/continuum/
- AWS — Security Agent / Continuum for penetration testing (read 2026-11-12): https://aws.amazon.com/security-agent/
- Motley Fool — Amazon Q3 2026 call (2026-10-30): https://www.fool.com/earnings/call-transcripts/2026/10/30/amazon-amzn-q3-2026-earnings-call-transcript/
- Meta — Llama protection tools and Defenders Program (2025-04-29): https://ai.meta.com/blog/ai-defenders-program-llama-protection-tools/
- GitHub — meta-llama/PurpleLlama (read 2026-11-12): https://github.com/meta-llama/PurpleLlama
- Hugging Face — Muse Spark Open card mirror (2026-10-15): https://huggingface.co/unsloth/Muse-Spark-Open-816B-A42B
- Hugging Face — Kimi K3.1 Pro card (read 2026-11-12): https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- Kimi K3.1 Pro blog capture on GitHub (2026-10-24; lead, not re-verified): https://github.com/kakon77777-commits/agiright-evidence/blob/6224a57aa54fc716328ca87fa37accddc6801068/sources/2026-10-24/kimi.txt
- NIST CAISI — DeepSeek V4 Pro (2026-05-01): https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro
- CASRAI — CAISI open-weight assessments (n.d.; secondary): https://casrai.org/guides/caisi-open-weight-model-cyber-assessments
- CSA — Open-weight cyber gap (2026-07-31): https://labs.cloudsecurityalliance.org/research/csa-research-note-open-weight-cyber-capability-gap-20260731/
- Notebookcheck — GLM-5.3 Chrome exploit cost, CAISI lag (2026-10-01): https://www.notebookcheck.net/GLM-5-3-China-s-open-AI-model-built-a-Chrome-exploit-for-20.1413141.0.html
- TechCrunch — Mistral Large 4 weights (2026-10-29): https://techcrunch.com/2026/10/29/mistral-releases-weights-for-its-trillion-parameter-ai-model-targeting-cybersecurity/
- Manhattan Institute — open weights paper (2026-10-01; extract only): https://manhattan.institute/article/an-american-answer-to-chinas-open-si-models-a-safe-harbor-for-open-weights
- Insurance Journal/Reuters — 360's Mythos rival (2026-06-26): https://www.insurancejournal.com/news/international/2026/06/26/875418.htm
- Natto Thoughts — Qi An Xin chief's vision (2026-08-26): https://www.nattothoughts.com/p/from-the-frontier-ai-arms-race-to
- Bloomberg — Cyber stocks slide on Claude Code Security (2026-02-20; paywall, extract only): https://www.bloomberg.com/news/articles/2026-02-20/cyber-stocks-slide-as-anthropic-unveils-claude-code-security
- Yahoo Finance/Proactive — Wedbush on the sell-off (2026-02-23): https://finance.yahoo.com/news/anthropic-claude-code-security-launch-200400637.html
- TradingView/Cointelegraph — CrowdStrike ~18% (Feb 2026; extract only): https://www.tradingview.com/news/cointelegraph:b5cdf0b39094b:0-cybersecurity-stocks-fall-after-anthropic-unveils-claude-code-security/
- Forbes — Mythos and cyber stocks (2026-04-14; 403, extract only): https://www.forbes.com/sites/jonmarkman/2026/04/14/how-claude-mythos-wiped-billions-out-of-cybersecurity-stocks/
- TipRanks — Glasswing-day rally (2026-04-08): https://www.tipranks.com/news/cybersecurity-stocks-rally-as-anthropic-debuts-project-glasswing
- BankInfoSecurity/ISMG — Post-Mythos rally (2026-09-18): https://www.bankinfosecurity.com/blogs/post-mythos-security-rally-rewards-broad-cyber-platforms-p-4191
- CNBC — Records after Black Hat (2026-08-10; headline): https://www.cnbc.com/2026/08/10/crowdstrike-palo-alto-stock-black-hat.html
- Simply Wall St — AI flipped the story twice (2026-10-23, upd. 10-27): https://simplywall.st/article/ai-has-flipped-the-story-on-cybersecurity-stocks-twice
- 24/7 Wall St — Sector sell-off (2026-11-02; headline/extract): https://247wallst.com/investing/2026/11/02/crowdstrike-slides-3-despite-deutsche-bank-upgrade-and-coreweave-deal-fortinet-falls-3-palo-alto-drops-2/
- Yahoo Finance — CrowdStrike −9/10% as AI trade unwinds (2026-11-05): https://finance.yahoo.com/markets/stocks/articles/crowdstrike-sinks-9-palo-alto-181856889.html
- SecurityWeek — Will AI kill bug bounty? (2026-06-09): https://www.securityweek.com/will-ai-kill-the-bug-bounty-industry/
- Low-quality secondary used once (Barclays quote): https://wilsonkumalo.dev/blog/claude-code-security-triggers-historic-cybersecurity-stock-collapse-when-ai-becomes-the-disruption-1772015112869

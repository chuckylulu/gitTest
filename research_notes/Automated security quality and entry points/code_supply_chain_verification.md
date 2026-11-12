# Code-security, software-supply-chain-security and formal-verification vendors (worldwide excluding Japan, South Korea, Taiwan, China): business quality, path forward and entry point, as of 2026-11-12

Method note (read first): research date 2026-11-12. Every figure carries its own date. "[company claim, unconfirmed]" marks statements no outside party has confirmed. Aggregator data (Sacra, TrueUp, multiples.vc, Dealroom, CB Insights, StockAnalysis private-company pages) are third-party estimates, not company disclosures. The session's shared web-search budget ran out part-way through, so some companies have thin or no 2026 coverage: Apiiro, OX Security, Legit Security, GitGuardian, AbsInt, TrustInSoft, Veridise, plus Checkmarx and Veracode revenue. These are listed under Gaps and not filled from memory. Where background knowledge is mentioned, it is labelled "unverified background". Valuation labels describe price against fundamentals. They are not investment advice.

## 1. Ownership, funding, M&A, revenue/ARR, pricing, customers and analyst positioning (code and supply-chain vendors)

### Takeaway
Private equity and venture capital own most of this sector. Checkmarx belongs to H&F, Veracode to TA, Black Duck to Clearlake/Francisco and Sonatype to Vista; Snyk, Sonar, Semgrep, Endor, Chainguard, Socket and Aikido are venture-backed. Only JFrog and GitLab are listed. In 2026, new capital went to supply-chain and AI-native names: Socket and Aikido at $1B each, plus Corridor, depthfirst and Backslash. Over the same period Snyk shrank to an estimated 7% ARR growth and a ~$3.6–3.7B secondary mark. Outside "lead" evidence still favours incumbents. The October 2025 Gartner AST Magic Quadrant Leaders were Black Duck, Checkmarx, HCLSoftware, OpenText, Snyk and Veracode. The first Gartner Software Supply Chain Security Magic Quadrant (18 June 2026) has announced Leaders JFrog, Sonatype, Chainguard, Cycode, Black Duck and Checkmarx.

### Cited Findings

#### Analyst positioning (cross-vendor)
- Gartner Magic Quadrant for Application Security Testing (AST): the most recent confirmed edition is dated 06 October 2025 per Gartner's abstract. One vendor cites 23 September 2025, so the dates conflict — [Gartner abstract](https://www.gartner.com/en/documents/7027498). Leaders listed by a third party: Black Duck, Checkmarx, HCLSoftware, OpenText, Snyk, Veracode — [Spotlight AR](https://research.oz.spotlightar.com/reports/magic-quadrant-application-security-testing-2025/leaders). Vendor confirmations:
  - Checkmarx: 7th time a Leader; says it was placed furthest for Completeness of Vision — [Checkmarx/BusinessWire, 2025-10-08](https://www.businesswire.com/news/home/20251008500376/en/Checkmarx-Named-a-Leader-in-the-2025-Gartner-Magic-Quadrant-for-Application-Security-Testing-for-Seventh-Time).
  - Black Duck: 8th time a Leader; says it was highest on Ability to Execute — [Black Duck, 2025-10-14](https://news.blackduck.com/2025-10-14-Black-Duck-Named-a-Leader-in-the-2025-Gartner-R-Magic-Quadrant-TM-for-Application-Security-Testing-for-Eighth-Consecutive-Time).
  - Veracode: 11th consecutive time — [Veracode](https://www.veracode.com/?p=23502).
  - OpenText (Fortify): 11th successive year — [OpenText blog](https://blogs.opentext.com/2025-gartner-magic-quadrant-for-application-security-testing-opentext-named-a-leader-11-years-running/).
  - HCLSoftware AppScan — [HCLSoftware](https://hcl-software.com/appscan/gartner-application-security-testing-report-2025).
  - Snyk — [Snyk blog, Oct 2025](https://snyk.io/de/blog/snyk-named-a-leader-in-the-2025-gartner-r-magic-quadrant-tm-for-application/).
- No 2026 AST Magic Quadrant could be confirmed. Invicti's landing page titled "2026 Gartner Magic Quadrant for Application Security Testing" (claiming Visionary) returned HTTP 404 on 2026-11-12 — [Invicti URL](https://www.invicti.com/clp/2026-gartner-magic-quadrant-for-application-security-testing). Checkmarx's own AST citations still reference the October 2025 report — [Checkmarx awards page](https://checkmarx.com/awards/checkmarx-named-a-leader-in-gartner-magic-quadrant-for-application-security-testing/).
- Gartner Magic Quadrant for Software Supply Chain Security (SSCS), the first edition: "Aaron Lord, Johnny Walters, Jason Gross, 18 June 2026" — [Sonatype press release, 2026-06-18](https://www.sonatype.com/press-releases/sonatype-named-a-leader-in-the-2026-gartner-magic-quadrant). Vendors announcing Leader placements:
  - Sonatype (2026-06-18).
  - Checkmarx (2026-06-22) — [Checkmarx](https://checkmarx.com/press-releases/checkmarx-named-leader-2026-gartner-mq-sscs/).
  - Chainguard, which says it was "furthest right for Completeness of Vision" [company claim] — [Chainguard blog, 2026-06-22](https://www.chainguard.dev/unchained/building-a-category-chainguard-named-a-leader-in-the-inaugural-gartner-magic-quadrant-for-software-supply-chain-security).
  - Cycode — [Cycode blog, 2026-06-24](https://cycode.com/blog/cycode-leader-gartner-magic-quadrant-sscs-2026/).
  - Black Duck — [Black Duck blog](https://www.blackduck.com/blog/gartner-magic-quadrant-software-supply-chain-security-leader.html).
  - JFrog, which says it was highest on Ability to Execute [company claim] — [JFrog blog (DE)](https://jfrog.com/de/blog/jfrog-named-a-leader-in-the-gartner-magic-quadrant/).
  
  The full participant list was not verified.
- Gartner Magic Quadrant for DevSecOps Platforms ("Keith Mann, Thomas Murphy, Bill Holz, June 15, 2026"): GitLab a Leader for the 4th consecutive year — [GitLab Q2 FY27 release, 2026-09-01](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf).
- Sonar is reported as a Leader in the 2026 Gartner Magic Quadrant for Technical Debt Management Tools; the date was not verified — [search-result summary of Sonar coverage](https://www.everydev.ai/developers/sonarsource).
- Forrester:
  - SAST Wave Q3 2025: Veracode a Leader; the full list was not obtained — [Veracode, 2025](https://www.veracode.com/press-release/veracode-named-a-leader-in-the-2025-q3-forrester-wave-static-application-security-testing-solutions/).
  - SCA Wave Q4 2024: Snyk and Black Duck Leaders — [Snyk](https://snyk.io/news/snyk-named-a-leader-in-software-composition-analysis); [Black Duck](https://www.blackduck.com/blog/forrester-wave-sca.html).
  - Sonatype's site claims a Forrester SCA Leader placement, with no date given — [Sonatype](https://www.sonatype.com/press-releases/sonatype-named-a-leader-in-the-2026-gartner-magic-quadrant).
  - No 2026 Forrester SAST or SCA Wave was found.
- The only "independent" economic study found is commissioned: a Forrester Consulting TEI for GitLab Duo Agent Platform (400% ROI, $7.5M NPV) — [GitLab release](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf). No independent detection or fix-accuracy benchmark comparing these vendors was found.

#### Checkmarx (Israel; Hellman & Friedman)
- 2020: H&F (with TPG) bought Checkmarx from Insight Partners at a $1.15B valuation — [TechCrunch, 2020-03-16](https://techcrunch.com/2020/03/16/insight-partners-sells-security-firm-checkmarx-to-hellman-friedman-for-1-15b).
- Sept 2024: Calcalist reported that H&F was meeting banks to run a sale, hoping for at least $2.5B — [BankInfoSecurity](https://www.bankinfosecurity.com/blogs/hellman-friedman-wants-to-unload-checkmarx-for-25b-p-3715). No completed sale was found as of 2026-11-12.
- Wikipedia records security incidents involving Checkmarx in March–May 2026; the details were not verified — [Wikipedia](https://en.wikipedia.org/wiki/Checkmarx).
- No 2026 revenue or ARR was found.

#### Veracode (US; TA Associates)
- 2022-03-15: TA Associates growth investment valuing Veracode at $2.5B — [BusinessWire](https://www.businesswire.com/news/home/20220315005831/en/Veracode-Announces-Significant-Growth-Investment-from-TA-Associates). A profile says TA is the majority owner and Thoma Bravo a minority investor (as of 2025) — [OODA Loop](https://oodaloop.com/company-profiles/cybersecurity/veracode/).
- Acquired Phylum's technology (malicious-package detection) — [PrivSource](https://www.privsource.com/acquisitions/deal/q5S7EN).
- 2026 State of Software Security report: "82% of organizations have security debt" [company claim, unconfirmed]. From a search-result summary; the hosting page was not re-read and the attribution to this URL is uncertain — [CIO Influence](https://cioinfluence.com/?p=283971).
- No revenue was found.

#### Sonar (Switzerland; SonarQube)
- 2022: $412M round co-led by Advent International and General Catalyst at a $4.7B valuation — [TechCrunch](https://techcrunch.com/?p=2303504). No later priced round was found.
- 2026-06-30 release: "surpassed $430 million in annual recurring revenue" with "accelerated growth" (no rate given) [company claim, unconfirmed]. Same release: 7M+ developers, 75% of the Fortune 100, 19 of the top 20 banks outside China, and 750B lines of code analysed daily [company claims]. It also launched Sonar Vortex and the SonarQube Remediation Agent — [Sonar](https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/).
- 2026-05-21: acquired Gitar, an AI code-review startup that had emerged a month earlier with a $9M Series A. Terms were undisclosed; CEO Tariq Shaukat — [Sonar](https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/); [SiliconANGLE](https://siliconangle.com/2026/05/21/ai-code-quality-startup-sonar-buys-ai-code-review-startup-gitar/).

#### Semgrep (US)
- Feb 2025: $100M Series D led by Menlo Ventures — [SecurityWeek](https://www.securityweek.com/semgrep-raises-100m-for-ai-powered-code-security-platform/); [Reuters via TradingView](https://www.tradingview.com/news/reuters.com,2025:newsml_L4N3OW1IY:0-application-security-platform-semgrep-raises-100-mln-in-new-funding-round).
- No official valuation. StockAnalysis lists an estimated $799M (2025-02-05) and a Hiive secondary-market data point dated 2026-09-02 (value not captured) — [StockAnalysis private page](https://stockanalysis.com/private/semgrep/). Total raised is about $193M per aggregators — [multiples.vc](https://multiples.vc/private-comps/semgrep).
- No 2026 round was found.

#### Endor Labs (US)
- April 2025: $93M Series B led by DFJ Growth; total raised $188M — [Sacra](https://sacra.com/c/endor-labs/); [Endor Labs](https://www.endorlabs.com/learn/why-we-raised-a-93m-series-b-in-this-market).
- ARR about $15M at end-2025, +131% (Sacra estimate). Net revenue retention 166% is company-reported via Sacra [company claim, unconfirmed]. Average contract value ~$35K (Sacra estimate) — [Sacra](https://sacra.com/c/endor-labs/).
- Customers named: OpenAI, Glean, Cursor, Atlassian, Snowflake. Pricing is not per seat; it depends on scope (developers, repositories or applications covered) — [Sacra](https://sacra.com/c/endor-labs/).
- Products:
  - AI SAST, a multi-agent engine launched early 2026; pilot claims of up to 95% false-positive reduction [company claim].
  - AURI, a free daemon that checks code at generation time.
  - Signed back-ported patches — [Sacra](https://sacra.com/c/endor-labs/).
- Acquisition of "Autonomous Plane" on 2026-02-11 per CB Insights; unverified — [CB Insights](https://www.cbinsights.com/company/endor-labs/financials).

#### Chainguard (US)
- Funding rounds:
  - July 2024 Series C at $1.12B.
  - April 2025 Series D, $356M at $3.5B, co-led by Kleiner Perkins and IVP — [GeekWire](https://www.geekwire.com/2025/cybersecurity-startup-chainguard-lands-356m-now-valued-at-3-5b/); [Fortune, 2025-04-23](https://fortune.com/2025/04/23/exclusive-chainguard-secures-356-million-series-d-as-valuation-soars-to-3-5-billion/).
  - Oct 2025: $280M from General Catalyst's Customer Value Fund at the same $3.5B. Total raised $892M — [Sacra](https://sacra.com/c/chainguard/).
- ARR:
  - $40M in fiscal 2025, up sevenfold, with a target of more than $100M by the end of fiscal 2026 — [Fortune](https://fortune.com/2025/04/23/exclusive-chainguard-secures-356-million-series-d-as-valuation-soars-to-3-5-billion/).
  - Sacra estimates ~$75M at end-2025 and ~$100M in June 2026 — [Sacra](https://sacra.com/c/chainguard/).
- More than 150 paying customers, including ANZ, Canva, GitLab, HPE, Snap, Wiz and Anduril. Pricing moved from per-image to a catalog fee tied to the size of the customer's engineering organisation — [Sacra](https://sacra.com/c/chainguard/).
- Operating claims: 2,500+ container projects rebuilt daily, 30,000+ OS packages, and more than 1B build manifests processed [company claims] — [Chainguard blog, 2026-06-22](https://www.chainguard.dev/unchained/building-a-category-chainguard-named-a-leader-in-the-inaugural-gartner-magic-quadrant-for-software-supply-chain-security).

#### Aikido Security (Belgium)
- 2026-01-14: $60M Series B at a $1B valuation, led by DST Global with PSG Equity, Singular and Notion Capital — [The Next Web](https://thenextweb.com/news/aikido-security-becomes-unicorn); [SiliconANGLE](https://siliconangle.com/2026/01/14/aikido-security-raises-60m-series-b-1b-valuation-unify-application-security/); [SecurityWeek](https://www.securityweek.com/aikido-security-raises-60-million-at-1-billion-valuation/amp/).
- Company claims: "fastest ever European cybersecurity company to reach unicorn status" and "more than 100,000 teams" [company claims, unconfirmed]. Total raised is more than $84M or $86.4M; sources differ — [The Next Web](https://thenextweb.com/news/aikido-security-becomes-unicorn).
- Revenue of about $13M at the round, implying ~77x, per one aggregator (unverified) — [multiples.vc](https://multiples.vc/private-comps/aikido-security). The same aggregator lists an acquisition of "OutKept" dated 2026-10-20; unverified.

#### GitHub Advanced Security (Microsoft; product facts only)
- Third-party guides say GHAS is now split into Secret Protection (~$19) and Code Security (~$30) per active committer per month, and one lists $49 for bundled GHAS. These figures conflict and were not verified against GitHub — [dev.to](https://dev.to/mr_manushukla/github-code-quality-now-costs-10-per-committer-the-2026-billing-model-and-the-audit-to-run-this-2jmj); [Redress Compliance](https://redresscompliance.com/github-enterprise-copilot-negotiation-download).
- GitHub Code Quality is reported to have reached general availability on 2026-07-20 at $10 per active committer per month — [dev.to](https://dev.to/mr_manushukla/github-code-quality-now-costs-10-per-committer-the-2026-billing-model-and-the-audit-to-run-this-2jmj).
- Agentic Autofix requires a Code Security or GHAS licence plus a Copilot licence with the Copilot cloud agent. AI usage is billed as "Code Security AI Credits" plus GitHub Actions minutes — [safeguard.sh](https://safeguard.sh/resources/blog/copilot-security-work-inside-the-plan). It is reported as generally available on 2026-10-15 — [labmemo (Japanese)](https://labmemo.com/?p=59298); [TechEnclave](https://techenclave.com/news/items/github-adds-ai-security-scans-and-draft-fixes-for-vulnerable-code). Another source says it is still in preview, so the status conflicts.

#### Black Duck (US; Clearlake Capital and Francisco Partners)
- In May 2024 the buyers agreed to acquire Synopsys' Software Integrity Group for up to $2.1B, of which up to $475M is contingent on returns. Completion was announced and the business renamed Black Duck Software; CEO Jason Schmitt — [Clearlake](https://clearlake.com/news/clearlake-and-francisco-partners-complete-acquisition-of-black-duck-software-formerly-known-as-synopsys-software-integrity-group/); [PE Hub](https://pehub.com/clearlake-capital-and-francisco-partners-acquire-black-duck-software-for-2-1bn).
- UltraViolet Cyber acquired Black Duck's application-security-testing services business; the date was not verified — [PrivSource](https://www.privsource.com/acquisitions/deal/JOS4ao).

#### Sonatype (US; Vista Equity Partners)
- Vista took a majority interest in Nov 2019 — [Sonatype](https://www.sonatype.com/press-releases/vista-acquires-majority-interest-in-sonatype).
- Leadership: CEO Bhagwat Swaroop — [Sonatype, 2026-06-18](https://www.sonatype.com/press-releases/sonatype-named-a-leader-in-the-2026-gartner-magic-quadrant). Former CEO Wayne Jackson became Executive Chairman (undated item) — [CyberWire](https://thecyberwire.com/newsletters/business-briefing/7/30). A new CRO, CMO and CHRO were named on 2026-06-09 — [IT Brief](https://itbrief.co.uk/story/sonatype-names-new-chiefs-as-ai-demand-drives-growth).
- AI products: Sonatype Guide ("helps developers and agents choose safer packages, dependencies, and models") and an MCP server. No revenue was disclosed — [Sonatype](https://www.sonatype.com/press-releases/sonatype-named-a-leader-in-the-2026-gartner-magic-quadrant).

#### OpenText Fortify (product facts only)
- Gartner AST Leader for 11 successive years (2025 edition) — [OpenText](https://blogs.opentext.com/2025-gartner-magic-quadrant-for-application-security-testing-opentext-named-a-leader-11-years-running/). No Fortify-specific revenue was found.

#### Cycode, Apiiro, OX Security, Legit Security, GitGuardian
- Cycode:
  - Acquired the SAST startup Bearer in March/April 2024 — [TechCrunch](https://techcrunch.com/2024/03/05/cycode-acquires-bearer-to-accelerate-its-move-into-ai-enhanced-security-remediation/amp/).
  - Leader in the 2026 SSCS Magic Quadrant.
  - Markets "Maestro" AI, an "AI fix & remediation agent" and an exploitability agent [company claims] — [Cycode, 2026-06-24](https://cycode.com/blog/cycode-leader-gartner-magic-quadrant-sscs-2026/).
- An undated TechCrunch article (date not visible in results) reports a $40M Legit Security raise. It names Apiiro, Cycode and ArmorCode as rivals and says Apiiro raised $100M "last year" — [TechCrunch](https://techcrunch.com/?p=2597478). That Apiiro released a CLI in April 2026 comes only from listicle-grade sources (low confidence) — [CiphersSecurity](https://cipherssecurity.com/best-aspm-tools-2026/).
- No 2026 funding or M&A was found for Cycode, Apiiro, OX, Legit or GitGuardian.

#### AI-native code-security entrants that rose in 2026
- depthfirst (US):
  - $40M Series A on 2026-01-14, led by Accel.
  - Founders came from Databricks/Amazon, Square and Google DeepMind.
  - Customers include AngelList, Lovable and Moveworks. No valuation was given — [TechCrunch](https://techcrunch.com/2026/01/14/ai-security-firm-depthfirst-announces-40-million-series-a).
- Corridor (US): $25M Series A on 2026-03-18 at a $200M valuation, led by Felicis; partners with Cursor and Factory — [Fortune press release](https://fortune.com/press-releases/corridor-raises-25m-series-a-ai-coding-security-2026-03-18).
- Backslash Security (Israel): $19M Series A on 2026-02-10, bringing the total to $27M; focused on "vibe coding" security — [Help Net Security](https://www.helpnetsecurity.com/2026/02/10/backslash-security-19-million-series-a-funding/).

### Inferences
- Analyst "lead" (test b) clearly favours incumbents in Gartner and Forrester rankings. But the 2025 AST Leaders are mostly the "pattern-matching" scanners that Forrester singled out as most pressured by frontier models (section 4). Ranking leadership and owning a judge are separate things.
- Capital is rotating:
  - toward supply-chain gating (Socket, Chainguard), AI-native agents (depthfirst, Corridor, Backslash) and "verification of AI output" (Sonar, through Gitar and Vortex);
  - away from seat-priced first-generation developer security (Snyk).
- Most incumbents are PE-owned. Outside investors therefore have little direct exposure, and future exits (Checkmarx's stalled sale, a Snyk sale or IPO) are the main liquidity events to watch.

### Gaps
- 2025–2026 revenue or ARR for Checkmarx, Veracode, Black Duck, Sonatype, Cycode, Apiiro, OX, Legit, GitGuardian and Semgrep. Search budget ran out; none was found in what was gathered.
- Funding and valuation history for Cycode, Apiiro, OX, Legit and GitGuardian. Unverified background: GitGuardian raised a ~$50M Series C (Feb 2025, Balderton), Cycode a $56M Series B (2022) and Apiiro $100M (2022). Not confirmed in this session.
- Checkmarx's 2026 product and ownership status, including whether the H&F sale process resumed. Details of the March–May 2026 Checkmarx security incidents.
- Full participant lists for the 2025 AST and 2026 SSCS Magic Quadrants (vendor releases only), whether a 2026 AST Magic Quadrant exists, and full 2025 Forrester SAST Leader list.
- No independent, third-party detection or fix-accuracy test results for any of these vendors were found.

## 2. Machine-speed fixing: who fixes (not just finds), with which models, and who has gated frontier-model access

### Takeaway
The deepest find-validate-patch capability now sits with model makers: Anthropic's Claude Security, OpenAI's Codex Security and Google's CodeMender. Anthropic gave gated access to its strongest cyber model (Claude Mythos Preview, Project Glasswing, 2026-04-07) to platform companies, not AppSec specialists. The launch partners were AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, the Linux Foundation, Microsoft, NVIDIA and Palo Alto Networks. No code-security pure-play in scope was a named launch partner. Among vendors, documented automatic fixing exists at:
- GitHub: agentic autofix;
- Sonar: a remediation agent whose fixes are checked by Sonar's own engine;
- Chainguard: continuous rebuilds;
- JFrog: "Zero-Touch Remediation";
- Endor: back-ported patches;
- Cycode: a remediation agent.

Fixes are mostly delivered as pull requests for human merge.

### Cited Findings
- Anthropic:
  - Claude Code Security launched 2026-02-20 as a limited research preview. It "detects security vulnerabilities, validates findings, and recommends patches for human review and approval" — [Globes, 2026-02-22](https://en.globes.co.il/en/article-1001535714).
  - Renamed Claude Security and opened as a public beta to Claude Enterprise customers on 2026-04-30, running on Claude Opus 4.7. Findings carry confidence, severity, impact and reproduction steps, and proposed fixes open in Claude Code on the Web. Platform partners embedding Opus 4.7: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, TrendAI, Wiz. Services partners: Accenture, BCG, Deloitte, Infosys, PwC. No pricing or accuracy metrics were published — [Claude blog, 2026-04-30](https://claude.com/blog/claude-security-public-beta).
  - An updated public beta on 2026-10-21 added continuous scanning, automatic fix tracking, per-project threat models and an API. This comes from a secondary search-result summary; the specific outlet was not re-verified — [Techzine](https://www.techzine.eu/news/security/140944/anthropic-claude-security-available-to-all-enterprise-customers/); [Enterprise DNA](https://enterprisedna.co/resources/news/anthropic-claude-security-enterprise-codebase-scanning-2026).
  - Secondary sources conflict on pricing: token costs with no separate fee, versus a Mythos-based scanner with trusted-access pricing of $10/$50 per million tokens — [Runtime Wire](https://runtimewire.com/article/anthropic-claude-security-mythos-5-github-scans).
- Project Glasswing (gated frontier model), launched 2026-04-07 with Claude Mythos Preview:
  - Partners: the 12 above (including Anthropic) plus "over 40 organizations" that build or maintain critical software.
  - Up to $100M of usage credits, plus $4M of donations: $2.5M to Alpha-Omega/OpenSSF and $1.5M to the Apache Software Foundation.
  - After credits, $25 per million input tokens and $125 per million output tokens, via the Claude API, Bedrock, Vertex AI and Microsoft Foundry.
  - Reports "thousands of high-severity vulnerabilities". The disclosed examples (OpenBSD, FFmpeg, Linux kernel) are reported and patched.
  - 2026-10-06 update: a Cyber Verification Program with three access tiers. Existing members move to a "Specialized Access" tier, and the update names Claude Opus 5.5, Sonnet 5.5 and Mythos 5.1. The page mentions "the US and its allies" but gives no country list — [Anthropic Glasswing page](https://www.anthropic.com/glasswing).
  - A secondary report says about 150 more organisations were added in June, which conflicts with the page's "40+" — [search-result summary of Glasswing coverage](https://thenewstack.io/anthropic-glasswing-mythos-cybersecurity/).
- OpenAI:
  - Codex Security (formerly Aardvark) launched 2026-03-06 as a research preview for ChatGPT Enterprise, Business and Edu. It builds a threat model and validates findings in isolated environments.
  - Claimed results: over 30 days it scanned 1.2M+ commits and flagged 792 critical vulnerabilities; false positives fell by more than 50% in beta; it contributed to 14 CVEs (OpenSSH, GnuTLS, GOGS, Thorium, Chromium). Free for the first month; later pricing undisclosed — [The Decoder, 2026-03-06](https://the-decoder.com/openai-launches-codex-security-an-ai-agent-designed-to-detect-vulnerabilities-in-software-projects/).
  - "Codex Security Cloud" for GitHub-connected repositories was announced at DevDay on 2026-09-29 as a research preview with token-based billing — [The Decoder](https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/); [beri.net](https://www.beri.net/article/openai-codex-security-cloud-continuous-repo-scanning-token-billing-research-preview-vs-sast).
- Google DeepMind CodeMender (October 2025): "upstreamed 72 security fixes to open source projects" over six months, some in codebases of 4.5M lines. Patches are validated automatically, then reviewed by researchers. Not broadly released; no 2026 update was found — [The Hacker News](https://thehackernews.com/2025/10/googles-new-ai-doesnt-just-find.html); [iTnews](https://www.itnews.com.au/news/google-deepmind-tackles-software-vulnerabilities-with-ai-agent-620875).
- GitHub: agentic autofix (generate and validate fixes) needs a Copilot licence and consumes AI credits; general availability was reported for 2026-10-15 (see section 1). The models used were not disclosed.
- Sonar:
  - The SonarQube Remediation Agent "generates fixes, verifies them with Sonar's analysis engine, and raises 'ready-to-merge' PRs"; the release does not say it auto-merges.
  - Vortex benchmarks were run on Claude Opus 4.8. Sonar claims up to 36% token savings on refactoring tasks [company claim] — [Sonar, 2026-06-30](https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/).
- JFrog: the Q3 2026 release highlights AI Asset Scanning, Agent Guard, support for Microsoft's Agent Package Manager, Zero-Touch Remediation and a Wiz partnership. Models were not disclosed — [JFrog 8-K exhibit, 2026-11-05](https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm). Anthropic and OpenAI were confirmed as JFrog customers on the Q3 call — [Earnings Whispers via Finviz, 2026-11-05](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause).
- Chainguard: daily rebuilds of 2,500+ container projects, and CVE remediation in "hours rather than days" [company claim] — [Chainguard blog](https://www.chainguard.dev/unchained/building-a-category-chainguard-named-a-leader-in-the-inaugural-gartner-magic-quadrant-for-software-supply-chain-security).
- Socket:
  - Socket Firewall blocks risky dependencies before install. The platform combines "AI-assisted analysis with human verification".
  - Socket says it identified the malicious Axios dependency "within six minutes" and onboarded 2,000+ organisations within 24 hours [company claims, unconfirmed] — [Socket, 2026-05-20](https://socket.dev/blog/socket-raises-60m-series-c-press-release).
- Snyk: "Snyk Evo" agents are in beta (MCP scanning, LLM injection monitoring, natural-language policies), and Snyk acquired Invariant Labs (agent security) in June 2025 — [Sacra, 2026-03-08](https://sacra.com/research/snyk-at-326m-arr-growing-7-yoy/).
- GitLab: GitLab Orbit (public beta) is a context graph for agents. GitLab claims agents respond "up to 11x faster with up to 45x fewer hallucinations in internal testing" [company claim] — [GitLab release](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf).
- Forrester (2026-02-23): tools that "constrain, validate, and contextualize remediation" gain value, and the remaining AppSec job is deciding "which fixes are safe, necessary, and valuable" — [Forrester](https://www.forrester.com/blogs/claude-code-security-causes-a-saas-pocalypse-in-cybersecurity/).

### Inferences
- Test (a), the strongest position, means machine-speed find-and-fix with gated frontier access. Inside this scope, only the model makers and the hyperscaler or platform owners meet it: Microsoft (GitHub), Google and AWS are Glasswing partners. No listed or private code-security specialist was named a launch partner. They might reach the "Specialized Access" tier through the October 2026 Cyber Verification Program, but no vendor has disclosed that. The "over 40" additional organisations (reportedly ~150 after June) are unnamed.
- The specialists' defensible role is turning into the judge of machine-generated fixes:
  - Sonar's engine verifies its own agent's fixes.
  - Chainguard's factory rebuilds and attests packages.
  - Socket and JFrog gate packages before installation or release.
  - Endor's reachability analysis says why a finding matters.

  This matches Forrester's "constrain, validate" framing.
- Model makers' products still route fixes through human review, so the "final" step of the judge remains with the code owner. Vendors whose tools sit at that merge or release gate (GitHub, GitLab, JFrog) keep a structural position even if detection commoditises.

### Gaps
- Models behind GitHub agentic autofix, JFrog Zero-Touch Remediation, Snyk Evo, Checkmarx and Veracode AI fixing. Whether any AppSec vendor holds Glasswing or Cyber Verification Program access, or OpenAI's equivalent.
- Merge or acceptance rates for any vendor's automatic fixes. No independent measurement found.
- Whether CodeMender has become a product in 2026, and its patch acceptance rate.
- The promised 90-day Glasswing public report on lessons learned is not shown as published on the page — [Anthropic](https://www.anthropic.com/glasswing).

## 3. Seat exposure: how much revenue is priced per human developer, and the shift to consumption pricing (with dates)

### Takeaway
Per-human pricing is still the main unit for GitHub Advanced Security (per active committer), GitLab (platform seats) and, by all signs, Snyk. Chainguard's catalog fee is tied to engineering-organisation size, which is semi-human. JFrog and Endor are mostly priced by usage or scope. Dated moves toward consumption:
- GitLab Flex (2026-09-01) bundles seats with usage-based "GitLab Credits".
- GitHub bills agentic autofix in AI credits plus Actions minutes (2026).
- Model makers' scanners are token-billed.

If agents write most code, committer and seat counts become the weak link. Vendors with usage meters (credits, artifacts, consumption) are better placed.

### Cited Findings
- GitLab, 2026-09-01:
  - New commercial model "GitLab Flex": "one annual commitment covering platform seats, GitLab Credits, and new eligible capabilities," with monthly reshaping and no contract amendments.
  - GitLab Secrets Manager launched as a "usage-based add-on".
  - Q2 FY27 subscription cost of revenue was $38.3M versus $21.8M a year earlier (+76%). GAAP gross margin was 84% versus 88%, and non-GAAP 86% versus 90% — [GitLab Q2 FY27 release](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf).
- GitHub: GHAS components are per active committer; Code Quality is $10 per active committer from 2026-07-20; agentic autofix uses AI credits plus Actions minutes. All third-party and unverified (see section 1) — [dev.to](https://dev.to/mr_manushukla/github-code-quality-now-costs-10-per-committer-the-2026-billing-model-and-the-audit-to-run-this-2jmj); [safeguard.sh](https://safeguard.sh/resources/blog/copilot-security-work-inside-the-plan).
- JFrog:
  - Cloud revenue was $101.5M, 57% of Q3 2026 revenue (46% a year earlier). "Cloud consumption" is cited as a net-dollar-retention driver — [JFrog 8-K exhibit](https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm).
  - Customers hesitated to convert overages into commitments in H1, but conversion was clearer in Q3. A $76M multi-year SaaS deal with a global telecom included a 167% larger consumption commitment, bundled with AI security and AppTrust. Guidance excludes overage and large deals — [Earnings Whispers via Finviz](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause).
- Snyk: Sacra says bundles from GitHub, Wiz and others "made some Snyk seats easier to cut," and growth slowed to about 7% — [Sacra Snyk profile (search summary)](https://sacra.com/c/snyk/).
- Chainguard moved from per-image pricing to a catalog fee "tied to engineering-org size" — [Sacra](https://sacra.com/c/chainguard/). Endor is "not per-seat"; pricing depends on deployment scope — [Sacra](https://sacra.com/c/endor-labs/).
- Model makers:
  - Codex Security Cloud: token billing, with no per-scan price published — [beri.net](https://www.beri.net/article/openai-codex-security-cloud-continuous-repo-scanning-token-billing-research-preview-vs-sast).
  - Mythos Preview: $25/$125 per million tokens after credits — [Anthropic](https://www.anthropic.com/glasswing).
- Forrester (2026-02-23) frames the risk as renewal: tools adding little beyond a platform agent become "a discretionary decision for the CFO" — [Forrester](https://www.forrester.com/blogs/claude-code-security-causes-a-saas-pocalypse-in-cybersecurity/).

### Inferences
- Rough share of revenue priced per human (inference, not disclosed):
  - GitHub GHAS: near 100% per committer, with AI credits as a new usage layer.
  - GitLab: the majority (seats are the base unit of Flex).
  - Snyk: likely the majority.
  - Checkmarx and Veracode: likely developer- or application-based (unverified).
  - JFrog: low per-seat exposure (tiers plus consumption; 57% cloud).
  - Chainguard: semi-human (organisation size).
  - Endor and Socket: scope- or usage-based, or not disclosed.
- If agents write most code, committer-based meters face two outcomes. Either agent commits are counted, which raises revenue per human, or they are not, and seat counts plateau while code volume rises. GitHub's design (Copilot licence plus AI credits) and GitLab Flex (seats plus credits) both hedge this. The 4-point drop in GitLab's gross margin shows the cost side of serving agents with inference.
- JFrog's revenue is tied to artifact volume and consumption. That links it to code volume rather than headcount, the healthiest meter in the group if agent output keeps growing.

### Gaps
- Official current list prices for GHAS, Snyk, Checkmarx, Veracode, Sonar (unverified background: Sonar prices by lines of code), Socket and Aikido.
- Any vendor's disclosed share of revenue from seats versus usage. None found.
- GitLab's split of seat revenue versus credits. Flex is too new for a disclosure.

## 4. Competition from model makers: churn, pricing pressure and share-price reactions (dated)

### Takeaway
Anthropic's Claude Code Security preview on Friday 2026-02-20 caused the sharpest single-day repricing in the group. JFrog fell about 25% (market cap to ~$4.5B) and GitLab about 8.7%. Forrester called the reaction "both accurate and overreaching". Since then the effects have split:
- JFrog's results disproved the bear case through Q3 2026 (revenue +31%, NDR 124%, AI labs as customers), and its market cap roughly tripled to $13.65B by 2026-11-12.
- GitLab is flat over 52 weeks.
- Snyk is the clearest casualty among private firms: estimated 7% ARR growth, a CEO exit framed around AI, and about 20% of staff cut.

Direct churn data attributable to model makers was not found.

### Cited Findings
- 2026-02-20 market reaction:
  - JFrog fell 24.94%, losing almost $3B to a ~$4.5B market cap, and was down 39.6% year to date — [Globes, 2026-02-22](https://en.globes.co.il/en/article-1001535714).
  - Forrester records JFrog −24.61% and GitLab −8.72%, with Palo Alto −1.10% — [Forrester, 2026-02-23](https://www.forrester.com/blogs/claude-code-security-causes-a-saas-pocalypse-in-cybersecurity/).
  - Okta fell more than 9% and CrowdStrike about 8%; the Global X Cybersecurity ETF hit its lowest since Nov 2023 (secondary) — [CyberSecurityNews](https://cybersecuritynews.com/claude-security-tool-stocks-impacted/).
- Analyst reactions:
  - Barclays called the selloff "illogical" (secondary) — [CyberSecurityNews](https://cybersecuritynews.com/claude-security-tool-stocks-impacted/).
  - Raymond James's Mark Cash: enterprises "may perceive reduced need for downstream package-level controls" — [Implicator, 2026-02-20](https://www.implicator.ai/jfrog-lost-25-in-one-day-ai-native-startups-have-more-to-lose/).
  - Jefferies' Joseph Gallo: "headwinds will increase before there is clarity" — [Globes](https://en.globes.co.il/en/article-1001535714).
- Forrester's assessment: damage concentrated in "the category … most perceived to be dependent on pattern matching" (SAST, SCA, ASPM). Anthropic is not expected to try to "conquer AppSec". AI "will not replace SAST" but will push buyers to consolidate into agentic platform bundles — [Forrester](https://www.forrester.com/blogs/claude-code-security-causes-a-saas-pocalypse-in-cybersecurity/).
- Implicator argues AI-native startups in the middleware layer have more to lose than diversified incumbents. It notes OpenAI's Aardvark launched about four months before Claude Code Security — [Implicator](https://www.implicator.ai/jfrog-lost-25-in-one-day-ai-native-startups-have-more-to-lose/).
- JFrog since February:
  - Q3 2026 revenue +31% and cloud +60%. FY2026 guidance was raised three times, from $623–628M originally to $680–682M — [JFrog 8-K](https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm); [Earnings Whispers via Finviz](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause).
  - On the Q3 call, analysts pressed management on frontier labs building in-house tooling. Management would not quantify security or AI-artifact revenue until year-end — [Earnings Whispers via Finviz](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause).
  - Market cap was $13.65B on 2026-11-12, with a 52-week change of +70.3% — [StockAnalysis](https://stockanalysis.com/stocks/frog/statistics/).
- GitLab's 52-week change is +2.45% as of 2026-11-12 — [StockAnalysis](https://stockanalysis.com/stocks/gtlb/statistics/).
- Snyk:
  - On 2026-02-19 CEO Peter McKay said a successor needs "deep roots in product innovation and AI" — [The Register, 2026-02-20](https://www.theregister.com/2026/02/20/snyk_ceo_stands_down/).
  - Tech.eu describes Snyk as competing with Wiz "and the frontier AI labs" — [Tech.eu, 2026-10-01](https://tech.eu/2026/10/01/snyk-laid-off-over-200-employees-revenues-top-300m/).
  - Growth decelerated to about 7% (Sacra estimate) — [Sacra](https://sacra.com/research/snyk-at-326m-arr-growing-7-yoy/).
- Claude Security's launch partners are platform security firms (CrowdStrike, Microsoft, Palo Alto, SentinelOne, TrendAI, Wiz), not AppSec specialists — [Claude blog](https://claude.com/blog/claude-security-public-beta).

### Inferences
- The model makers' threat is uneven:
  - It hits detection-only, seat-priced vendors hardest: Snyk, and by extension Checkmarx, Veracode, Semgrep and Aikido, though evidence for the last four is indirect.
  - It hits gate and system-of-record owners least: JFrog, GitLab, GitHub, Chainguard, Socket.
  - Socket's and JFrog's customer lists include the model makers themselves (Anthropic, xAI, OpenAI), which suggests the labs still buy third-party supply-chain controls.
- Pricing pressure shows up as bundling, not list-price cuts: Claude Security is included in Enterprise plans at token cost, and GitHub bundles security into Copilot. No direct discounting evidence was found.

### Gaps
- Churn or win/loss data naming Claude Security, Codex Security or CodeMender. None found.
- Whether Wiz Code or Google, after Wiz, is taking AppSec share. Not researched; covered elsewhere.
- GitLab-specific commentary on model-maker competition in its Q2 FY27 call.

## 5. Listed companies: JFrog (Nasdaq: FROG) and GitLab (Nasdaq: GTLB), with results, quality metrics, valuation vs history and peers, consensus and events

### Takeaway
JFrog is the stronger business on growth and cash generation:
- Q3 2026 revenue $179.2M (+31%), FCF margin 37%, NDR 124%, RPO +60%, ~$0.88B cash and no borrowings.
- It now trades at the top of its five-year range: 20.1x trailing and ~16.9x forward EV/Sales, 62x EV/FCF and 87x forward P/E, a premium to Datadog.

GitLab is growing 21% with $1.26B cash and no debt, but its quality signals are weakening:
- Gross margin is down 4 points.
- SBC is about 23–26% of revenue.
- Q2 FY27 adjusted FCF was only $9.8M.
- Q3 guidance sits below Q2 revenue.

GitLab trades near the bottom of its five-year range (6.3x trailing, ~5.5x forward EV/Sales; 31x EV/FCF), roughly in line with Atlassian. No 2026 takeover report was confirmed for either company.

### Cited Findings

#### JFrog: Q3 2026 (quarter ended 2026-09-30; reported 2026-11-05)
- Source for this subsection: [JFrog 8-K exhibit 99.1](https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm).
- Revenue and margins:
  - Revenue $179.2M (+31% YoY); nine-month revenue $496.9M (about +29%).
  - Cloud revenue $101.5M (+60%), 57% of total.
  - Gross margin: GAAP 79.6%, non-GAAP 83.6%.
  - Operating margin: GAAP −1.0% (loss of $1.8M); non-GAAP 22.7% ($40.7M).
  - GAAP net income $6.6M; non-GAAP EPS $0.32.
- Cash flow and balance sheet:
  - Operating cash flow $69.3M; FCF $66.5M (Q3) and $157.5M (nine months).
  - Cash and investments $880.9M; no debt shown on the balance sheet.
  - RPO $812.4M (+60%).
- Retention and customers:
  - Trailing four-quarter NDR 124% (118% a year earlier).
  - Customers above $1M ARR: 112 (71 a year earlier). Customers above $100K: 1,357 (1,121).
  - Enterprise+ subscriptions were 61% of revenue.
- SBC $41.8M in Q3 and $121.0M over nine months. Diluted shares 129.5M.
- Guidance:
  - Q4: revenue $183–185M; non-GAAP operating income $36.2–38.2M; EPS $0.28–0.30.
  - FY2026: revenue $680–682M; non-GAAP operating income $142.5–144.5M; EPS $1.14–1.16.
- Beat consensus: revenue $179.17M versus $165.56M, and EPS $0.32 versus $0.23. Q3 included a $3.6M R&D tax credit. The Q4 outlook implies a sequential margin step-down, cause not given. Anthropic and OpenAI are customers — [Earnings Whispers via Finviz](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause).
- Stock reaction: one report says shares rose 22.5% to $91.49 straight after the results — [Webull](https://www.webull.com/news/15873322845314048). A Barron's headline listed on the Finviz page shows +35.33% on 2026-11-06, so reports conflict on the size of the move — [Finviz](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause).

#### JFrog: valuation (StockAnalysis, price at 2026-11-11 close; page dated 2026-11-12)
- Price, size and multiples:
  - Price $109.51; market cap $13.65B; EV $12.88B.
  - EV/Sales TTM 20.05x; forward P/S 17.86x; EV/FCF 62.1x; P/FCF 65.8x; forward P/E 87.45x.
  - TTM revenue $642.2M; TTM FCF $207.4M (32.3% margin); TTM operating margin −6.75%.
- Balance sheet and shares: net cash $768.9M (StockAnalysis lists $112M of "debt"); shares outstanding 124.6M (+5.79% YoY); beta 1.31.
- Consensus: 23 analysts rate it "Strong Buy", with an average target of $117.68 (+7.5%). Three-year revenue-growth forecast 22.1% — [StockAnalysis statistics](https://stockanalysis.com/stocks/frog/statistics/).
- Five-year history at fiscal year-ends — [StockAnalysis ratios](https://stockanalysis.com/stocks/frog/financials/ratios/):

| Year-end | EV/Sales | EV/FCF | Forward P/E |
|---|---|---|---|
| 2021 | 12.04x | 105x | not shown |
| 2022 | 6.17x | 101x | 290x |
| 2023 | 9.01x | 43.7x | 68.7x |
| 2024 | 6.60x | 26.3x | 47.7x |
| 2025 | 12.69x | 47.5x | 75.1x |
| 2026-11-11 (current) | 20.05x | 62.1x | 87.45x |

  Market cap was $7.39B at end-2025 and $3.28B at end-2024.

#### GitLab: Q2 FY2027 (quarter ended 2026-07-31; reported 2026-09-01)
- Source for this subsection: [GitLab exhibit 99.1](https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf).
- Revenue: $286.3M (+21%), of which subscription $258.3M and licence $27.9M.
- Margins:
  - Gross margin: GAAP 84% (88% a year earlier); non-GAAP 86% (90%).
  - GAAP operating loss $(56.9)M (−20%), including $19.4M of restructuring and $75.0M of SBC.
  - Non-GAAP operating income $42.6M (15%, versus 17%).
  - GAAP net loss $(36.8)M; non-GAAP EPS $0.24.
- Cash flow and balance sheet:
  - Operating cash flow $(3.1)M in Q2 and $146.1M in H1. Non-GAAP adjusted FCF $9.8M (versus $46.5M a year earlier).
  - Cash $226.5M plus short-term investments $1,030.5M, about $1.26B, with no debt.
  - Bought back about 3.5M shares ($104.6M in Q2; $154.7M in H1).
  - Class B shares fell from 16.7M (2026-01-31) to 1.1M (2026-07-31).
- Customers and backlog:
  - Dollar-based net retention 117%.
  - Customers above $100K ARR: 1,571 (+17%). Customers above $5K: 11,114 (+8%).
  - RPO $1.2B (+16%); cRPO $744.7M (+20%).
  - "Net ARR growth exceeding 40%" and "First Order growth of more than 100%" [company claims].
- Guidance:
  - Q3: revenue $281–283M; non-GAAP operating income $35–37M.
  - FY27: revenue $1,129–1,133M; non-GAAP operating income $148–152M; EPS $0.85–0.87.
- Exposure: JiHu, the Chinese joint venture, is a consolidated entity with $46.1M of assets.
- Revenue beat the $273.12M estimate — [Tiger Brokers news](https://www.itiger.com/news/2664869007).

#### GitLab: valuation (StockAnalysis, price at 2026-11-11 close; page dated 2026-11-12)
- Price, size and multiples:
  - Price $47.32; market cap $7.88B; EV $6.63B.
  - EV/Sales TTM 6.28x; forward P/S 6.50x; EV/FCF 31.0x; P/FCF 36.9x; forward P/E 54.2x.
  - TTM revenue $1.06B; TTM FCF $213.7M (20.3%); TTM operating margin −6.05%.
- Balance sheet and shares: net cash $1.26B; shares +3.13% YoY.
- Consensus and events: 28 analysts rate it "Buy", with an average target of $56.13 (+18.6%). Three-year revenue-growth forecast 16.9%. Next earnings 2026-12-01 — [StockAnalysis statistics](https://stockanalysis.com/stocks/gtlb/statistics/).
- Five-year history at fiscal year-ends — [StockAnalysis ratios](https://stockanalysis.com/stocks/gtlb/financials/ratios/):

| Fiscal year-end | EV/Sales | EV/FCF | Forward P/E |
|---|---|---|---|
| FY22 (Jan-2022) | 33.1x | not shown | not shown |
| FY23 | 15.4x | not shown | not shown |
| FY24 | 17.5x | 303x | 218x |
| FY25 | 14.4x | not shown | 92.6x |
| FY26 (Jan-2026) | 4.95x | 21.3x | 36.2x |
| 2026-11-11 (current) | 6.28x | 31.0x | 54.2x |

#### Listed peers (StockAnalysis, price at 2026-11-11 close)
- Datadog (DDOG): market cap $66.6B; EV $62.6B; EV/Sales TTM 14.6x; forward P/S 12.7x; EV/FCF 51.1x; forward P/E 61.9x; FCF margin 28.7%; three-year growth forecast 25.6% — [StockAnalysis](https://stockanalysis.com/stocks/ddog/statistics/).
- Atlassian (TEAM): market cap $38.4B; EV $38.5B; EV/Sales TTM 5.57x; forward P/S 4.97x; EV/FCF 23.1x; forward P/E 28.3x; FCF margin 24.1%; three-year growth forecast 14.9% — [StockAnalysis](https://stockanalysis.com/stocks/team/statistics/).

### Inferences
- Derived forward EV/Sales:
  - JFrog: implied forward revenue = $13.65B ÷ 17.86 ≈ $764M. EV ÷ that ≈ 16.9x; EV ÷ the FY2026 guidance midpoint ($681M) ≈ 18.9x.
  - GitLab: implied forward revenue = $7.88B ÷ 6.50 ≈ $1.21B. EV ÷ that ≈ 5.5x; EV ÷ the FY27 guidance midpoint ($1,131M) ≈ 5.9x.
- SBC-adjusted cash:
  - JFrog: nine-month FCF ($157.5M) minus SBC ($121.0M) = $36.5M, 7.3% of revenue. Q3 SBC was 23.3% of revenue.
  - GitLab: H1 operating cash flow minus capex (~$143.5M) minus SBC ($125.1M) ≈ $18.4M, about 3% of revenue. Q2 SBC was 26.2% of revenue.

  On an owner-earnings basis both are close to breakeven, and headline FCF multiples flatter them.
- What the JFrog price implies: EV of $12.9B equals 25x FCF of ~$515M. At a ~33% FCF margin that needs about $1.56B of revenue, roughly 23% annual growth from the FY2026 guidance to ~2030 before any return. At 20x FCF it needs ~30% growth. The price assumes JFrog stays a 20%+ grower with expanding margins and that model makers do not take the security attach.
- What the GitLab price implies: EV of $6.6B equals 20x FCF of ~$331M. At a 25% FCF margin that needs ~$1.33B of revenue, low-to-mid single-digit growth from FY27. The price discounts sharp deceleration, or persistent SBC and margin pressure.
- GitLab's Q3 guidance ($281–283M) is below Q2's $286.3M, despite "record gross bookings". This suggests Q2 included upfront licence revenue from large self-managed deals, though that is an inference. The implied Q4 is about $297–301M.
- The collapse of Class B shares (16.7M to 1.1M in six months) weakens founder voting control. That would make an unsolicited approach easier (inference). No 2026 takeover report was confirmed (see Gaps).
- Peers: JFrog trades at a premium to Datadog (20.1x versus 14.6x EV/Sales; 62x versus 51x EV/FCF) with a similar three-year growth forecast (22% versus 26%). GitLab trades roughly at Atlassian's level on EV/Sales (6.3x versus 5.6x) but higher on EV/FCF (31x versus 23x) and forward P/E (54x versus 28x).

### Gaps
- JFrog and GitLab customer concentration (no customer above 10%?) and geographic revenue split. 10-K and 10-Q segment data were not retrieved.
- Consensus next-twelve-month revenue and EPS (only implied forward P/S was available). JFrog's Q4/FY2026 report date, expected around February 2027 (not confirmed).
- GitLab takeover or sale reports in 2025–2026. Unverified background: Reuters reported in Dec 2024 that GitLab was exploring a sale with Datadog interest. The search budget ran out before 2026 status could be checked.
- The cause of GitLab's $19.4M Q2 restructuring and the headcount affected.
- JFrog's reason for the Q4 margin step-down.

## 6. Snyk and Socket specifics

### Takeaway
Snyk:
- 2025 revenue was $309M (+11%) with a $189M loss (UK filing). Sacra estimates ARR at $326M (+7%) in February 2026.
- The CEO announced his exit on 2026-02-19, an ex-CFO is reported as interim CEO, and about 203 staff (~20%) were cut in June 2026.
- Valuation marks are about $3.6–3.7B, versus $7.4B in 2022 and $8.5B in 2021.
- It acquired Invariant Labs in June 2025. No IPO or sale report was found.

Socket:
- $60M Series C led by Thrive at a $1B valuation (2026-05-20), after a $40M Series B (October 2024); total about $125M.
- Logos include Anthropic, xAI, Cursor and Replit [company claims].
- ARR was not disclosed, and confirmation of its detections by registry operators was not found.

### Cited Findings
- Snyk financials: the 2025 Companies House filing shows revenue +11% to $309M and losses up from $169M to $189M. About 990 employees at end-2025. A June 2026 reduction of "approximately 203 employees," about 20% of the workforce, with charges up to $13.8M; an earlier wave in July 2025. Snyk has raised more than $1B, with rounds valuing it at $8.5B (2021) and $7.4B (2022) — [Tech.eu, 2026-10-01](https://tech.eu/2026/10/01/snyk-laid-off-over-200-employees-revenues-top-300m/).
- The June 2026 cut was first reported as about 90 jobs, framed as an AI pivot. Over 350 employees were laid off in three rounds in 2022–2023 — [Globes](https://en.globes.co.il/en/article-1001546903); [GovInfoSecurity](https://www.govinfosecurity.com/snyk-reportedly-cuts-90-jobs-to-accelerate-ai-strategy-a-32081).
- Snyk ARR (Sacra estimates): $250M at end-2023, $300M in 2024 and $326M in February 2026 (+7% YoY, down from 27%). Snyk Code is about 40% of ARR. BlackRock's latest mark is $3.7B, about 11x revenue — [Sacra, 2026-03-08](https://sacra.com/research/snyk-at-326m-arr-growing-7-yoy/). Sacra's Endor Labs page separately says "over $400M ARR" for Snyk, which conflicts — [Sacra](https://sacra.com/c/endor-labs/). TrueUp lists a $3.6B secondary valuation on 2026-10-29, "down 52%" (page blocked on fetch; taken from the search summary) — [TrueUp](https://www.trueup.io/co/snyk).
- Leadership: McKay announced on 2026-02-19 that he would step down once a successor was found. The Register credits his tenure with about 4,800 customers and $325M of annual revenue — [The Register](https://www.theregister.com/2026/02/20/snyk_ceo_stands_down/). Secondary reports say CFO Ken MacAskill became interim CEO in April and founder Guy Podjarny returned as chairman. These were not re-verified — [The Stack](https://www.thestack.technology/snyk-ceo-steps-down-better-ai-knowledge/); [GovInfoSecurity](https://www.govinfosecurity.com/snyk-reportedly-cuts-90-jobs-to-accelerate-ai-strategy-a-32081).
- Acquisitions: Invariant Labs (AI agent security), June 2025 — [Tech.eu](https://tech.eu/2026/10/01/snyk-laid-off-over-200-employees-revenues-top-300m/); [Sacra](https://sacra.com/research/snyk-at-326m-arr-growing-7-yoy/). Sacra's Chainguard page also references a Snyk–Enso acquisition, undated — [Sacra](https://sacra.com/c/chainguard/).
- Socket funding: $60M Series C at $1B on 2026-05-20, led by Thrive Capital with a16z, Abstract Ventures and Capital One Ventures. Products: Socket Firewall, certified patches and protection extensions — [Socket](https://socket.dev/blog/socket-raises-60m-series-c-press-release). Total funding $125M; Series B was $40M in October 2024 — [SecurityWeek](https://www.securityweek.com/socket-raises-60-million-at-1-billion-valuation/amp/); [SecurityWeek, 2024](https://www.securityweek.com/socket-raises-40-million-for-supply-chain-security-tech/amp/). Bloomberg Law headline: "Security Firm Foiling Nation-State Hackers Valued at $1 Billion" — [Bloomberg Law](https://news.bloomberglaw.com/private-equity/security-firm-foiling-nation-state-hackers-valued-at-1-billion).
- Socket traction [company claims, unconfirmed]:
  - Customers: Anthropic, xAI, Replit, Cursor, Figma, Vercel, Gusto, Mercado Libre, Cribl and Fortune 100 firms in financial services and media.
  - Axios incident: malicious dependency identified within six minutes and 2,000+ organisations onboarded within 24 hours — [Socket](https://socket.dev/blog/socket-raises-60m-series-c-press-release).
  - Socket's site banner (November 2026): "Mini Shai-Hulud Hits @antv npm Packages, 639 Versions Compromised" — [Socket](https://socket.dev/blog/series-c).
- Socket shares are listed on the secondary platform Caplight — [Caplight](https://www.caplight.com/company/socket).

### Inferences
- On reported revenue ($309M) and the BlackRock or TrueUp marks, Snyk's ~11–12x revenue at single-digit growth is a higher multiple than listed GitLab (~6x at 21% growth). Private marks look slow to reprice, or include an option value on the AI pivot.
- Socket's customer list includes frontier labs and AI coding tools. That is evidence the labs still buy third-party judges for open-source packages, which supports Socket's position. Revenue scale is unknown, so its lead cannot be assessed.

### Gaps
- Snyk: a permanent CEO (none confirmed as of the latest reports, August 2026); 2026 ARR; cash balance; any IPO or sale process; Probely and Helios acquisitions (unverified background).
- Socket: ARR or revenue and growth; Seed and Series A details; the Coana acquisition (unverified background, 2025). Registry operators' (npm/GitHub, PyPI) public confirmation of Socket's detections was not found; the search budget ran out before registry security posts could be checked.

## 7. Verification vendors and AI-made proofs: scale, customers, cost curve, effect on find/patch demand, and standards

### Takeaway
Verification vendors are small:
- Certora's revenue band is $10–50M per an aggregator.
- Kry10 raised $6M in 2024; Veridise and Runtime Verification raised single-digit millions.
- Galois is employee-owned and funded largely by DARPA contracts.

Several are effectively paid for expert hours (audits, research contracts). Strong evidence in 2026 that AI is cutting the cost of proofs:
- An August 2026 arXiv paper (CryptoProver) produced Verus proofs of a production elliptic-curve library in 11.4 hours for $467 of API cost. The original verification took three people five months.
- Certora (AutoProver, July 2026) and AWS (Kiro requirements analysis, May 2026) are shipping LLM plus solver products.

Counter-evidence: a 2026 IACR paper found 13 vulnerabilities that escaped "verified" crypto libraries, including one that caused decryption failures in Signal's post-quantum ratchet. Verification moves bugs to the boundary rather than removing the need to find and patch.

Regulation rewards formal methods mainly in aerospace (DO-178C/DO-333) and high-assurance Common Criteria (EAL7). The EU Cyber Resilience Act mandates vulnerability handling, not formal methods. No evidence was found of Google DeepMind verifying Signal's library. The Signal verification project, "Signal Shot", is run by Signal, the Beneficial AI Foundation and Lean FRO.

### Cited Findings

#### Company facts
- Galois (US):
  - DARPA COOP award HR001125C0300 in October 2024, worth up to $52.8M with expected completion April 2026 — [HigherGov](https://www.highergov.com/contract/HR001125C0300/); [Military & Aerospace Electronics](https://www.militaryaerospace.com/trusted-computing/article/55238957/trusted-computing-design-and-development-tools).
  - Built "Formal Verso" for verifying Stellar Soroban smart contracts — [Galois](https://www.galois.com/project/formal-verso).
  - No revenue found.
- Certora (Israel):
  - $36M Series B led by Jump Crypto (2022) — [The Block](https://www.theblock.co/post/147066/certora-announces-36-million-series-b-funding-round-led-by-jump-crypto).
  - $43.2M raised over five rounds, including a 2026 grant from the Ethereum Foundation's zkEVM formal-verification project — [CB Insights](https://www.cbinsights.com/company/certora/financials).
  - Revenue band $10–50M for an unspecified latest fiscal year, and a 2022 valuation estimate of $100–250M — [Dealroom](https://dealroom.co/companies/certora/).
  - 2026 launches: "AI Composer" (AI coding with formal verification) and "AutoProver" (July 2026; AI agents infer intent, generate specifications and prove them) [company claims; aggregator reporting] — [AI Market Watch](https://www.ai-market-watch.com/news/ertora-s-launch-of-the-omposer-the-first-af-223); [ChainCatcher](https://www.chaincatcher.com/en/article/2243764).
- TrustInSoft (France): €1.2M from Idinvest (2017) and $5.8M led by ACE Management (2019); no 2026 funding or M&A found — [ZoomInfo](https://www.zoominfo.com/financial/trustinsoft/357578909); [CFNews](https://www.cfnews.net/L-actualite/Capital-innovation/Operations/1er-tour/TrustInSoft-verifie-l-entree-d-un-fonds-243021).
- AdaCore (France/US):
  - Strategic investment from Battery Ventures on 2024-03-28 (terms undisclosed), for expansion into static and dynamic analysis, ML, formal methods, certification and cybersecurity — [BusinessWire](https://www.businesswire.com/news/home/20240328498013/en/Battery-Ventures-Announces-Strategic-Investment-in-AdaCore-to-Propel-the-Future-of-High-Integrity-Software-Development).
  - 2025-06-18: definitive agreement to merge with CodeSecure (CodeSonar SAST, formerly GrammaTech's products, also Battery-owned). CEO Franco Gasperoni. Customers span defense, aerospace, medical devices, automotive and industrial automation — [AdaCore](https://www.adacore.com/press/adacore-and-codesecure-merge).
- Cryspen (Germany):
  - Signal's SPQR post-quantum ratchet uses Cryspen's libcrux ML-KEM. Cryspen states that "not all the code in libcrux is formally verified yet" — [Cryspen](https://cryspen.com/post/signal-spqr-verification/).
  - Symbolic Software reported ML-DSA bugs in February 2026, which Cryspen fixed in March — [Symbolic Software](https://symbolic.software/blog/2026-02-17-cryspen-mldsa/).
- Runtime Verification (US):
  - $5.3M round led by IOSG in 2021; before that, funding came from grants and contracts — [CoinDesk](https://hotfix.coindesk.com/markets/2021/06/18/security-audit-firm-raises-53m-from-funds-investing-in-polkadot-cardano-blockchains).
  - Its blog shows activity through November 2026 — [Runtime Verification](https://runtimeverification.com/blog/category/news).
- Veridise (US): seed funding of $4.7M in total; no 2026 news — [CB Insights](https://cbinsights.com/company/veridise).
- Proofcraft (Australia): has "completed the verification of functional correctness for seL4 with MCS" — [seL4 news](https://www.sel4.systems/news/). Silver sponsor of seL4 Summit 2026 — [seL4 Discourse](https://sel4.discourse.group/t/thank-you-proofcraft-silver-sponsor-of-the-sel4-summit-2026/1045).
- Kry10 (New Zealand, founded 2020): $6M pre-Series A (2024) — [CyberSecTools](https://cybersectools.com/companies/kry10.md). Presenting a Software Safety Manual for its seL4-based OS at seL4 Summit 2026 (2026-09-01) — [seL4 Summit 2026 abstracts](https://backend.sel4.systems/Summit/2026/abstracts2026.html).
- AWS automated reasoning (product line):
  - May 2026: Kiro "Requirements Analysis" pairs an LLM with an SMT solver to find contradictions and gaps in specifications before code is written. Former Microsoft executive Shawn Bice leads the Automated Reasoning Group as VP of AI Services — [GeekWire](https://www.geekwire.com/2026/aws-targets-ai-slop-with-new-spec-check-in-kiro-coding-tool-amid-scrutiny-of-agent-reliability/); [The New Stack](https://thenewstack.io/?p=22823378).
  - February 2026: Bedrock Automated Reasoning policies gained source-document references. AWS claims "up to 99%" accuracy [company claim] — [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/02/automated-reasoning-policies-include-references).
  - AWS Startups "Prove It" guide (2026-06-18) — [AWS](https://aws.amazon.com/aws-startups/learn/prove-it-part-3-a-step-by-step-guide-to-automated-reasoning-implementation/?lang=en-US).
- Harmonic (US; AI-generated Lean proofs):
  - $120M Series C at $1.45B post-money (November 2025), led by Ribbit, Sequoia, Kleiner Perkins and Emerson — [Crowdfund Insider](https://www.crowdfundinsider.com/2025/11/256050-robinhood-ceo-backed-harmonic-becomes-unicorn-on-series-c/).
  - $100M Series B at nearly $900M (July 2025) — [SiliconANGLE](https://siliconangle.com/2025/07/10/harmonic-raises-100m-nearly-900m-valuation-scale-ai-model-formal-mathematical-reasoning/).
  - Aristotle: "gold-medal level" IMO performance [company claim]. No 2026 round was found and no security product is documented.

#### Evidence that AI is making verification cheaper
- CryptoProver (arXiv 2608.00965; v1 2026-08-02, v2 2026-10-16; Sun, Fong, Kuang, Jiao, Narodytska, Wu, Dill, Barrett):
  - Synthesises internal specifications and Verus-checked proofs from API contracts without changing executable code.
  - Produced a new independent proof of curve25519-dalek in 11.4 hours at $466.99 of API cost, compared with "a focused five-month, three-person effort" originally. Also verified RustCrypto chacha20 against RFC 8439.
  - Uses "mechanical gates" to reject specification weakening, invented axioms and cross-module breakage.
  - Source: [arXiv](https://arxiv.org/abs/2608.00965).
- Signal Shot (2026-04-20; Signal, Beneficial AI Foundation, Lean FRO):
  - Aims to translate libsignal's Rust into Lean via Aeneas. No verified results yet. AI is expected to handle "autoformalization and routine work".
  - Cites Math Inc.'s agent Gauss formalising sphere packing "in weeks, not years".
  - Google DeepMind is not mentioned — [Leonardo de Moura blog](https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/).
- Google DeepMind's AlphaProof Nexus published a repository of Lean proofs (secondary report) — [Runtime Wire](https://runtimewire.com/article/google-deepmind-alphaproof-nexus-lean-proofs).
- Certora AutoProver (July 2026) and AWS Kiro (May 2026), as above.

#### Does verified software reduce demand for finding and patching?
- Kobeissi, "Verification Theatre" (IACR ePrint 2026/192; received 2026-02-05, revised 2026-06-25):
  - Found 13 vulnerabilities that escaped formal verification in "CE Labs'" libcrux and hpke-rs: nine in unverified code and four in verified specification or proof code.
  - One cross-backend bug "caused real decryption failures in Signal's post-quantum ratchet".
  - The same failure types appear in AWS's verified libcrypto.
  - No author rebuttal is shown — [IACR ePrint](https://eprint.iacr.org/2026/192).
- The EU CRA (below) requires vulnerability handling and security updates for the product lifecycle whatever the development method — [European Commission](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act).

#### Standards and jurisdictions
- EU Cyber Resilience Act, Regulation (EU) 2024/2847 — [European Commission](https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act):
  - In force 2024-12-10; reporting obligations apply from 2026-09-11; main obligations from 2027-12-11.
  - Covers hardware and software "products with digital elements".
  - Requires lifecycle vulnerability handling and updates.
  - The Commission page does not mention formal methods.
- Common Criteria: EAL7 = "formally verified design and tested", used only where high-value assets justify the cost. Example: ProvenRun's ProvenCore OS certified EAL7 by ANSSI in 2019 — [Wikipedia](https://en.wikipedia.org/wiki/Evaluation_Assurance_Level).
- DO-178C (approved December 2011; in use from January 2012): DO-333 is the formal methods supplement. FAA AC 20-115D (2017-07-21) recognises DO-178C as an acceptable means of compliance. The source describes DO-333 as complementing testing — [Wikipedia](https://en.wikipedia.org/wiki/DO-178C).

### Inferences
- Under test (a), formal tools are the strongest kind of judge: fast once a specification exists, faithful under optimisation pressure (a proof checker cannot be talked round), informative through counterexamples, and final. The ePrint 2026/192 findings show the weak point is the specification and the verification boundary, not the checker.
- Value accrues to whoever owns the checker plus distribution:
  - AWS (SMT tooling inside Bedrock and Kiro, and a Glasswing partner).
  - Open ecosystems (Lean, Verus) and tool owners (Certora Prover, TrustInSoft Analyzer, AdaCore SPARK, AbsInt).
- If AI cuts proof cost by roughly 100–1,000x (CryptoProver's 15 person-months versus 11 hours and $467 is one data point, not a trend), consultancies billing proof hours lose out unless they turn into products: Galois, Runtime Verification, Veridise, Proofcraft and Certora's audit arm. The players best placed to gain are those whose checkers become the standard gate for AI-written code.
- "Verified at write-time" (transition 6) looks credible in narrow, high-value components (crypto libraries, microkernels, smart contracts, aerospace). No evidence yet shows it reducing aggregate demand for scanning and patching, and the CRA's vulnerability-handling duty points the other way through 2027.
- The premise that Google DeepMind worked on Signal's library is unconfirmed. The likely referents are Signal Shot (Signal/BAIF/Lean FRO) and the CryptoProver paper. A report writer should not attribute this work to DeepMind.

### Gaps
- Revenue for Galois, AdaCore, AbsInt, TrustInSoft, Cryspen, Runtime Verification, Veridise, Proofcraft and Kry10.
- Galois ownership: a search-result summary quoted an April 2026 lecture bio describing Galois as "an employee-owned research company in Portland, OR" with clients including DARPA and AWS. The URL was not captured, so treat this as unverified.
- AbsInt (Astrée, aiT, CompCert) and TrustInSoft customers and 2026 news. Nothing gathered; search budget ran out.
- Text of ISO 26262 and EN 50128 on formal methods. Unverified background: EN 50128 "highly recommends" formal methods at SIL 3/4, and ISO 26262-6 recommends formal verification for higher ASILs. Not confirmed this session.
- Whether DO-333 allows formal analysis to replace (not only complement) specific test objectives. The Wikipedia summary says "complement", while practitioners report partial substitution credit; unresolved.
- DARPA programme pages (AIxCC results, expMath and others) and Cryspen's or AdaCore's 2026 funding were not retrieved.
- Identity of "CE Labs" in ePrint 2026/192 (relationship to Cryspen not confirmed).

## 8. Private-company entry data: last valuation vs ARR, secondary marks, IPO plans, exposure routes

### Takeaway
Implied private multiples, from the latest available marks:
- Chainguard ~35x estimated ARR (June 2026).
- Snyk ~11–12x revenue (2026 marks, 7–11% growth).
- Sonar ~11x ARR on a stale 2022 price.
- Aikido ~77x (aggregator revenue, unverified).

Socket ($1B), Endor, Semgrep, Corridor ($200M) and Harmonic ($1.45B) have no reliable revenue for a multiple. No IPO filings or confirmed IPO plans were found for any in-scope private company. Outside exposure is limited to:
- secondary platforms (Hiive data on Semgrep, Caplight on Socket, TrueUp on Snyk);
- funds holding marks (BlackRock on Snyk);
- PE funds (H&F, TA, Clearlake/Francisco, Vista);
- indirectly, the listed parents of product lines: Microsoft (GitHub), OpenText (Fortify), Amazon (AWS automated reasoning), Alphabet (CodeMender), HCL Technologies (AppScan).

### Cited Findings
- Snyk: last primary $7.4B (December 2022); BlackRock mark $3.7B, about 11x (Sacra, March 2026); TrueUp secondary $3.6B (2026-10-29) — [Sacra](https://sacra.com/research/snyk-at-326m-arr-growing-7-yoy/); [TrueUp](https://www.trueup.io/co/snyk). 2025 revenue $309M — [Tech.eu](https://tech.eu/2026/10/01/snyk-laid-off-over-200-employees-revenues-top-300m/).
- Chainguard: $3.5B (April 2025 and October 2025); ARR about $100M in June 2026 (Sacra estimate) — [Sacra](https://sacra.com/c/chainguard/).
- Socket: $1B (2026-05-20); ARR undisclosed; listed on Caplight — [Socket](https://socket.dev/blog/socket-raises-60m-series-c-press-release); [Caplight](https://www.caplight.com/company/socket).
- Aikido: $1B (2026-01-14); revenue ~$13M per aggregator — [multiples.vc](https://multiples.vc/private-comps/aikido-security).
- Sonar: $4.7B (2022); ARR above $430M (2026-06-30) [company claim] — [TechCrunch](https://techcrunch.com/?p=2303504); [Sonar](https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/).
- Semgrep: valuation undisclosed; StockAnalysis estimate $799M (February 2025); Hiive data point dated 2026-09-02 — [StockAnalysis](https://stockanalysis.com/private/semgrep/).
- Endor Labs: valuation undisclosed; ARR about $15M (end-2025, Sacra estimate) — [Sacra](https://sacra.com/c/endor-labs/).
- Corridor: $200M valuation at its $25M Series A (2026-03-18) — [Fortune press release](https://fortune.com/press-releases/corridor-raises-25m-series-a-ai-coding-security-2026-03-18).
- PE-owned:
  - Checkmarx: $1.15B in 2020; H&F target of at least $2.5B in 2024 — [TechCrunch](https://techcrunch.com/2020/03/16/insight-partners-sells-security-firm-checkmarx-to-hellman-friedman-for-1-15b); [BankInfoSecurity](https://www.bankinfosecurity.com/blogs/hellman-friedman-wants-to-unload-checkmarx-for-25b-p-3715).
  - Veracode: $2.5B in 2022 — [BusinessWire](https://www.businesswire.com/news/home/20220315005831/en/Veracode-Announces-Significant-Growth-Investment-from-TA-Associates).
  - Black Duck: up to $2.1B in 2024 — [PE Hub](https://pehub.com/clearlake-capital-and-francisco-partners-acquire-black-duck-software-for-2-1bn).
  - Sonatype: Vista majority since 2019 — [Sonatype](https://www.sonatype.com/press-releases/vista-acquires-majority-interest-in-sonatype).
- Harmonic: $1.45B post-money (November 2025) — [Crowdfund Insider](https://www.crowdfundinsider.com/2025/11/256050-robinhood-ceo-backed-harmonic-becomes-unicorn-on-series-c/).

### Inferences
- Against the listed reference points (GitLab ~6x and JFrog ~17–20x EV/Sales; Datadog ~15x), the private marks look like this:
  - Chainguard at ~35x ARR is priced for sustained doubling.
  - Snyk at ~11–12x is rich for ~7–11% growth.
  - Sonar's 2022 price at ~11x current ARR is stale but not obviously demanding if growth "accelerated".
  - Aikido at ~77x of an unverified revenue figure is venture-priced.
- A return of IPO windows would most likely favour Chainguard, Sonar and possibly Socket on growth and positioning. Snyk looks more like a sale candidate.

### Gaps
- No secondary-market prices (Forge, Hiive, Caplight) were captured for Chainguard, Socket, Sonar or Semgrep. Page values were not visible or were blocked.
- No IPO reporting was verified for any company. Unverified background: Snyk long cited as a 2025–2026 IPO candidate.

## 9. Per-company scorecard (framework tests a–e, path forward, entry point), exclusions, and dated source list

### Takeaway
Rough ranking on business quality:
- Strongest within scope (none is a model maker): JFrog (owns the artifact gate, with usage-scaled revenue and strong cash), Chainguard (owns a continuously rebuilding build factory), Sonar (deterministic "verifier" of AI output at $430M ARR) and Socket (fast package-behaviour judge bought by the AI labs).
- Weakest: seat-priced, detection-centric scanners without gated model access (Snyk, and probably Checkmarx, Veracode and Aikido).
- Among verification firms: AWS's automated-reasoning line owns the strongest judge plus frontier access. The small specialists sell strong judges but mostly through expert hours.

Entry points:
- JFrog is stretched.
- GitLab is fair, cheap on history but with weak SBC-adjusted cash.
- Most private names cannot be assessed, with Chainguard and Aikido indicatively stretched.

### Cited Findings
- All facts used in this section are cited in sections 1–8; key figures are repeated inline below with their sources.

### Inferences

#### Scorecard: code and supply-chain vendors
Scenario shorthand for test (e): S = steady growth (~55%), P = financing-led pause around 2028 (~25%), A = faster acceleration (~20%).

**JFrog (FROG; Israel/US)**
- (a) Position: owns the binary and artifact system of record and a release gate (Curation, AppTrust), now also for AI models and MCP packages. Agents cannot remove artifact storage, provenance or distribution, though AI can absorb the detection layer. Not a Glasswing partner; it has the labs as customers.
- (b) Lead: Gartner SSCS Leader in June 2026 (claims highest Ability to Execute); 112 customers above $1M ARR; Anthropic and OpenAI as customers ([Finviz/EW](https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause)).
- (c) Revenue model: recurring subscriptions plus 57% cloud consumption; low per-seat exposure (inference).
- (d) Financial strength: non-GAAP operating margin 22.7%, Q3 FCF margin 37%, RPO +60%, $881M cash and no borrowings. But SBC is about 23% of revenue, GAAP is about breakeven, and shares are up 5.8% YoY.
- (e) Resilience: S — strong (artifact volume follows code volume). P — consumption could slow but stays sticky. A — more agent artifacts help, offset by the risk of model makers bundling package controls. Cycle position: re-accelerating growth at a record multiple. Israel geopolitical exposure; no export-control exposure identified.
- Path forward:
  - Transitions: 2 (machine-speed remediation: Zero-Touch Remediation and Agent Guard shipped), 4 (model-maker competition: the February shock, labs as customers), 5 (CRA and SBOM demand, inference).
  - Said vs done: products shipped, the $76M telecom deal with an AI-security bundle, $881M of cash.
  - Must go right: security and AI attach becoming disclosed and measurable at year-end; consumption commitments continuing.
  - Verdict: **coherent**.
- Entry:
  - $109.51 and $13.65B (2026-11-11/12).
  - EV/Sales 20.1x TTM and ~16.9x forward; EV/FCF 62x; forward P/E 87x — the top of the 2021–2025 year-end range (6.2–12.7x EV/Sales) and a premium to Datadog (14.6x).
  - Implies about 23–30% revenue CAGR to ~2030 at ~33% FCF margin.
  - Next event: Q4/FY2026 results and FY2027 guidance (~February 2027, unconfirmed).
  - Would improve: EV/Sales back toward ~10–13x, or security revenue disclosed.
  - Label: **stretched**.

**GitLab (GTLB; US)**
- (a) Position: owns the code repository and CI system of record where human and agent code lands. That position is real but second to GitHub. Security is a tier feature. No gated frontier access found.
- (b) Lead: Gartner DevSecOps Platforms Leader for the 4th year (June 2026); 1,571 customers above $100K (+17%); DBNRR 117%.
- (c) Revenue model: seat-based subscriptions, now hybrid through GitLab Flex (seats plus credits, 2026-09-01).
- (d) Financial strength: non-GAAP gross margin 86% (−4 points), non-GAAP operating margin 15%, GAAP −20%. SBC about 23–26% of revenue; Q2 adjusted FCF $9.8M; $1.26B net cash; buybacks.
- (e) Resilience: S — adequate. P — seat contraction risk. A — agents erode human seats unless credits scale. GitHub competition. The JiHu China JV is a cross-border exposure. Cycle position: decelerating, with restructuring.
- Path forward:
  - Transitions: 2 (Duo Agent Platform), 4, and seat-to-usage pricing.
  - Said vs done: Flex and Secrets Manager launched, Orbit in beta, $19.4M restructuring.
  - Must go right: credit adoption; gross margin stabilising; Q3 and Q4 delivering the implied ~$298M Q4.
  - Verdict: **partly coherent** (the pricing pivot has started, but margin and seat-model risks are unresolved).
- Entry:
  - $47.32 and $7.88B (2026-11-11/12).
  - EV/Sales 6.3x TTM and ~5.5x forward; EV/FCF 31x; forward P/E 54x — near the bottom of its five-year range (4.95–33x) and close to Atlassian (5.6x).
  - SBC-adjusted FCF about breakeven.
  - Next event: Q3 FY27 results on 2026-12-01.
  - Label: **fair**.

**Snyk (private; US/UK/Israel)**
- (a) Position: detection engines (vulnerability database, Snyk Code), the pattern-matching layer frontier models are absorbing. No owned gate and no gated model access found.
- (b) Lead: Gartner AST Leader (2025) and Forrester SCA Leader (Q4 2024), but growth is down to about 7% (Sacra estimate).
- (c) Revenue model: developer-seat subscriptions, likely the majority (inference).
- (d) Financial strength: 2025 revenue $309M with a $189M loss; 20% staff cut in 2026.
- (e) Resilience: weak in S, P and A; Israel exposure. Cycle position: contraction.
- Path forward:
  - Transitions: 2 (Evo agents, still beta) and 4 (direct competition).
  - Said vs done: Invariant Labs acquired, layoffs, interim leadership; no permanent AI-native CEO confirmed.
  - Verdict: **not coherent yet** (intent stated, execution and leadership unproven).
- Entry: $3.6–3.7B marks, about 11–12x revenue for 7–11% growth; secondary only. Label: **stretched (indicative)**.

**Socket (private; US)**
- (a) Position: a fast judge of package behaviour at install (firewall). The final takedown sits with registries; bought by the labs themselves.
- (b) Lead: Thrive-led $1B round; logos only [company claims]; no analyst ranking or registry confirmation found.
- (c) Revenue model: SaaS; pricing undisclosed.
- (d) Financial strength: unknown; $125M raised, the latest in May 2026.
- (e) Resilience: S and A favourable (AI-driven dependency growth and supply-chain attacks); P — funding risk mitigated by the recent raise.
- Path forward: transitions 2 and 4. Verdict: **coherent (narrow; scale unverified)**.
- Entry: $1B with no ARR. Label: **cannot assess**.

**Chainguard (private; US)**
- (a) Position: owns a continuously rebuilding, attested build factory (machine-speed fixing by rebuild), with no frontier-model dependence.
- (b) Lead: Gartner SSCS Leader (2026); about 2x ARR growth (Sacra estimate); blue-chip customers.
- (c) Revenue model: recurring catalog fee tied to engineering-organisation size (semi-human).
- (d) Financial strength: $892M raised; profitability unknown.
- (e) Resilience: S strong; P — refinancing risk at the valuation; A — opportunity as a default trusted source for agents. US federal/FIPS tailwind.
- Path forward: transitions 2, 5 and partly 6. Said vs done: products shipped, ARR around $100M (estimate), well funded. Verdict: **coherent**.
- Entry: $3.5B at ~35x estimated ARR; no IPO plan found. Label: **stretched (indicative)**.

**Sonar (private; Switzerland)**
- (a) Position: a deterministic analysis engine sold as the "verification" layer for AI-written code. It is a fast and informative judge, not a final one. Its fix agent is checked by its own engine. Uses frontier models (benchmarks on Opus 4.8) but has no gated access.
- (b) Lead: 7M developers and 75% of the Fortune 100 [company claims]; Gartner TDM Leader (2026).
- (c) Revenue model: recurring; pricing basis unverified.
- (d) Financial strength: ARR above $430M [company claim]; margins unknown.
- (e) Resilience: S and P good; A — risk if models self-verify.
- Path forward: transitions 2 and 6 (positioning). Said vs done: Vortex and the Remediation Agent shipped; Gitar acquired. Verdict: **coherent**.
- Entry: 2022 price only, ~11x current ARR. Label: **cannot assess**.

**Checkmarx (private; Israel; H&F)**
- (a) Pattern-matching SAST/SCA/ASPM; no owned gate.
- (b) Strong analyst lead: Gartner AST (2025) and SSCS (2026) Leader.
- (c) Likely developer- or application-based subscriptions (unverified).
- (d) Unknown; PE leverage likely (unverified).
- (e) Weak under A; P hits PE capital structures.
- Path forward: AI agent claims not verified this session; sale attempt (2024) unresolved. Verdict: **cannot verify / partly coherent**.
- Entry: $1.15B (2020); ≥$2.5B ask (2024). Label: **cannot assess**.

**Veracode (private; US; TA)**
- (a) Pattern-matching SAST/SCA plus malicious-package data (Phylum).
- (b) Gartner AST Leader (11th time), Forrester SAST Leader (Q3 2025).
- (c) Subscriptions (basis unverified).
- (d) Unknown.
- (e) Weak under A.
- Verdict: **partly coherent (insufficient evidence)**.
- Entry: $2.5B (2022). Label: **cannot assess**.

**Black Duck (private; US; Clearlake/Francisco)**
- (a) SCA knowledge base plus deep static analysis; divested its testing-services business (fewer billable hours).
- (b) Gartner AST Leader (highest on execution, 2025), SSCS Leader (2026), Forrester SCA Leader (Q4 2024).
- (c) Subscriptions.
- (d) Unknown; up to $2.1B buyout (2024).
- (e) P is a leverage risk; A brings model competition.
- Path forward: transition 1 done (services out); transition 2 unclear. Verdict: **partly coherent**.
- Entry: **cannot assess**.

**Sonatype (private; US; Vista)**
- (a) Repository manager and SCA; Sonatype Guide for agents.
- (b) Gartner SSCS Leader (2026).
- (c) Subscriptions.
- (d) Unknown.
- (e) Moderate.
- Path forward: new CEO and executive team (June 2026). Verdict: **partly coherent**.
- Entry: **cannot assess**.

**Semgrep (private; US)**
- (a) Rules-based SAST engine with AI on top; exposed to model scanners.
- (b) $100M Series D (Menlo, 2025); no 2025 AST Leader placement found.
- (c) Subscriptions (basis unverified).
- (d) Unknown.
- (e) A is a risk.
- Verdict: **cannot verify**.
- Entry: no official valuation. Label: **cannot assess**.

**Endor Labs (private; US)**
- (a) Reachability (informative judge), AI SAST, generation-time checks (AURI), back-ported patches.
- (b) Customers OpenAI, Cursor, Atlassian and Snowflake; NRR 166% [company claim]; ARR ~$15M (estimate).
- (c) Scope-based, not per seat.
- (d) $188M raised; burn unknown.
- (e) P is a funding risk; A could become the judge for agents.
- Verdict: **coherent (small)**.
- Entry: **cannot assess**.

**Aikido Security (private; Belgium)**
- (a) Bundled scanner aggregator for the mid-market; no owned judge.
- (b) "100,000+ teams" [company claim]; no analyst ranking.
- (c) Subscriptions (basis unverified).
- (d) Revenue ~$13M (aggregator).
- (e) Exposed under A; EU base is neutral to positive for data-residency buyers (inference).
- Verdict: **partly coherent**.
- Entry: $1B at ~77x (unverified revenue). Label: **stretched (indicative)**.

**Cycode (private; Israel/US)**
- (a) ASPM plus AI fix and exploitability agents.
- (b) Gartner SSCS Leader (2026).
- (c) and (d) Unknown.
- (e) Exposed under A.
- Verdict: **partly coherent**.
- Entry: **cannot assess**.

**Apiiro, OX Security, Legit Security, GitGuardian**
- Insufficient 2026 evidence for tests (b)–(e).
- (a) ASPM layers are exposed to platform bundling. Secrets detection (GitGuardian) is a fast, near-final judge (a credential is valid or not) but competes with GitHub Secret Protection (inference).
- Verdict and entry: **cannot assess**.

**GitHub Advanced Security (product line; Microsoft)**
- (a) Strongest distribution: it sits where code lands, autofix runs through the Copilot cloud agent, and Microsoft is a Glasswing partner.
- (c) Per active committer plus AI credits.
- Path forward: transitions 2 and 4 done.
- Entry: n/a (Microsoft covered elsewhere).

**OpenText Fortify (product line)**
- (b) Gartner AST Leader for 11 years.
- Entry: n/a (OpenText not assessed here).

**AI-native 2026 entrants (depthfirst, Corridor, Backslash)**
- (a) Agentic find and fix built on third-party models; directly exposed to model makers (Implicator).
- (b) Early logos only.
- Entry: Corridor $200M post-money; others undisclosed. Label: **cannot assess**.

#### Scorecard: verification vendors
**AWS automated reasoning (product line)**
- (a) Owns strong judges (SMT-based policy and spec checks) plus frontier-model access (Glasswing partner, Bedrock) and distribution.
- (b) No adoption data; "99%" accuracy [company claim].
- (c) Usage-priced cloud.
- (e) Correlates with the AI-capex scenarios.
- Path forward: transition 6 in motion (Kiro, May 2026). Verdict: **coherent**.
- Entry: via Amazon only (not assessed).

**Galois (US; reportedly employee-owned, unverified)**
- (a) Strong judge tooling, but revenue is research contracts (billable research hours).
- (b) DARPA awards (COOP up to $52.8M).
- (c) Labour or contract revenue.
- (d) Unknown.
- (e) Tied to US defense R&D more than the AI cycle; likely ITAR/export-control relevant (inference).
- Path forward: transitions 1 and 6; AI-cheapened proofs could commoditise its hours unless it turns into products. Verdict: **partly coherent**.
- Entry: no outside exposure.

**Certora (Israel)**
- (a) Prover (judge) for smart contracts plus AI spec and proof generation (AutoProver) [company claims].
- (b) DeFi clients; Ethereum Foundation grant.
- (c) Audits (labour) plus tooling.
- (d) $43M raised; revenue band $10–50M (aggregator).
- (e) Crypto-cycle exposure is higher than AI-cycle exposure.
- Verdict: **partly coherent**.
- Entry: **cannot assess**.

**AdaCore + CodeSecure (France/US; Battery Ventures)**
- (a) SPARK proofs plus CodeSonar SAST in certified embedded markets (DO-178C, ISO 26262), where a regulator-recognised judge matters.
- (b) Defense, aerospace, automotive and medical customers [company].
- (c) Licences and subscriptions.
- (d) Unknown.
- (e) Resilient to the AI-capex cycle; defense export-control relevance (inference).
- Path forward: transitions 5 and 6. Merger agreed June 2025; integration status not verified. Verdict: **partly coherent**.
- Entry: **cannot assess**.

**Cryspen (Germany)**
- (a) Verified crypto (hax/libcrux) used by Signal's post-quantum ratchet; boundary failures found (ePrint 2026/192).
- (c) Contracts and consulting.
- (d) Tiny.
- (e) Post-quantum migration tailwind.
- Verdict: **partly coherent**.
- Entry: none.

**TrustInSoft (France) and AbsInt (Germany)**
- (a) Sound static analysers: strong judges for C/C++ undefined behaviour and timing.
- (b)–(d) Not verified (search budget).
- Verdict and entry: **cannot assess**.

**Runtime Verification and Veridise (US)**
- (a) Formal tools, but revenue is audit-led (labour).
- (d) Single-digit-million funding.
- (e) Crypto cycle.
- Verdict: **partly coherent** (RV) / **cannot assess** (Veridise).
- Entry: none.

**Proofcraft (Australia)**
- (a) seL4 proof engineering (MCS proof completed); labour-based.
- Verdict: **partly coherent**.
- Entry: none.

**Kry10 (New Zealand)**
- (a) Product built on a verified kernel, addressing transition 3 (shielding devices that cannot be patched) and transition 6.
- (d) $6M raised (2024).
- Verdict: **partly coherent (early)**.
- Entry: none.

**Harmonic (US; AI Lean proofs)**
- (a) Prover model; the Lean kernel is the judge and is not owned by Harmonic.
- (b) IMO claims [company claim]; no security product documented.
- (e) Highly exposed to scenario P (AI funding pause).
- Verdict: **partly coherent (security application unproven)**.
- Entry: $1.45B (November 2025). Label: **cannot assess**.

#### Companies considered and excluded (with reasons)
- Wiz (Google), Palo Alto Networks, CrowdStrike, SentinelOne, Zscaler, Okta: platform or cloud security, covered by other researchers. Used here only for price-reaction context.
- Microsoft overall: covered elsewhere; only GitHub Advanced Security product facts are included.
- HCLSoftware AppScan (India) and Invicti: AST vendors outside the assigned list. HCL is noted as a 2025 Gartner AST Leader. Invicti's 2026 Magic Quadrant claim could not be verified (404).
- Mend.io, Contrast Security, Jit, Arnica, ZeroPath, Corgea, DryRun Security, Pixee, Mobb, Amplify, Aisle, Almanax: plausible AI code-security or remediation players not researched because the search budget ran out. Candidates for a follow-up.
- XBOW, Horizon3.ai, Pentera and other offensive or pentest automation: outside the code and supply-chain scope.
- Theori/Xint (South Korea), Japanese and Taiwanese vendors, and GitLab's JiHu (China) as a separate business: excluded by geography; another researcher covers them.
- Axiom Math, Math Inc (Gauss), Logical Intelligence, Imandra, Atlas Computing, UK ARIA Safeguarded AI: AI-proof or verification players not researched (budget). Math Inc is mentioned only through the Signal Shot blog.
- ProvenRun (France; EAL7 ProvenCore): a verification-based product company not on the list; flagged as a candidate.
- Entire ($60M seed at $300M): developer tooling, not security.

### Gaps
- See the Gaps in sections 1–8. The largest gaps that would change scores:
  - revenue and margins for every private company except Snyk;
  - whether any AppSec specialist has Glasswing or Cyber Verification Program access;
  - independent accuracy tests;
  - JFrog and GitLab customer and geographic concentration;
  - 2026 takeover reports for GitLab;
  - registry-operator confirmations for Socket.

### Dated source list
- Primary or company filings and releases:
  - JFrog Q3 2026 8-K exhibit 99.1 (2026-11-05) — https://www.sec.gov/Archives/edgar/data/0001800667/000119312526449797/frog-ex99_1.htm
  - GitLab Q2 FY27 exhibit 99.1 (2026-09-01) — https://s204.q4cdn.com/984476563/files/doc_financials/2027/q2/Gitlab-Exhibit-99-1-2026-09-1-FY27.pdf
  - Sonar Vortex and ARR release (2026-06-30) — https://www.sonarsource.com/company/press-releases/sonar-launches-sonar-vortex-and-sonarqube-remediation-agent/
  - Sonar acquires Gitar (2026-05-21) — https://www.sonarsource.com/company/press-releases/sonar-acquires-gitar/
  - Socket Series C (2026-05-20) — https://socket.dev/blog/socket-raises-60m-series-c-press-release
  - Sonatype Gartner SSCS release (2026-06-18) — https://www.sonatype.com/press-releases/sonatype-named-a-leader-in-the-2026-gartner-magic-quadrant
  - Chainguard Gartner SSCS blog (2026-06-22) — https://www.chainguard.dev/unchained/building-a-category-chainguard-named-a-leader-in-the-inaugural-gartner-magic-quadrant-for-software-supply-chain-security
  - Cycode Gartner SSCS blog (2026-06-24) — https://cycode.com/blog/cycode-leader-gartner-magic-quadrant-sscs-2026/
  - Checkmarx SSCS release (2026-06-22) — https://checkmarx.com/press-releases/checkmarx-named-leader-2026-gartner-mq-sscs/
  - Checkmarx AST release (2025-10-08) — https://www.businesswire.com/news/home/20251008500376/en/Checkmarx-Named-a-Leader-in-the-2025-Gartner-Magic-Quadrant-for-Application-Security-Testing-for-Seventh-Time
  - Black Duck AST release (2025-10-14) — https://news.blackduck.com/2025-10-14-Black-Duck-Named-a-Leader-in-the-2025-Gartner-R-Magic-Quadrant-TM-for-Application-Security-Testing-for-Eighth-Consecutive-Time
  - Veracode Forrester SAST Q3 2025 — https://www.veracode.com/press-release/veracode-named-a-leader-in-the-2025-q3-forrester-wave-static-application-security-testing-solutions/
  - OpenText AST blog (October 2025) — https://blogs.opentext.com/2025-gartner-magic-quadrant-for-application-security-testing-opentext-named-a-leader-11-years-running/
  - Anthropic Claude Security public beta (2026-04-30) — https://claude.com/blog/claude-security-public-beta
  - Anthropic Project Glasswing (2026-04-07; updated 2026-10-06) — https://www.anthropic.com/glasswing
  - AdaCore–CodeSecure merger (2025-06-18) — https://www.adacore.com/press/adacore-and-codesecure-merge
  - AdaCore and Battery Ventures (2024-03-28) — https://www.businesswire.com/news/home/20240328498013/en/Battery-Ventures-Announces-Strategic-Investment-in-AdaCore-to-Propel-the-Future-of-High-Integrity-Software-Development
  - Clearlake and Black Duck completion (2024) — https://clearlake.com/news/clearlake-and-francisco-partners-complete-acquisition-of-black-duck-software-formerly-known-as-synopsys-software-integrity-group/
  - Veracode and TA (2022-03-15) — https://www.businesswire.com/news/home/20220315005831/en/Veracode-Announces-Significant-Growth-Investment-from-TA-Associates
  - Cryspen and Signal SPQR (October 2025) — https://cryspen.com/post/signal-spqr-verification/
  - AWS Automated Reasoning references (February 2026) — https://aws.amazon.com/about-aws/whats-new/2026/02/automated-reasoning-policies-include-references
  - European Commission CRA page (accessed 2026-11-12) — https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Research and papers:
  - CryptoProver, arXiv 2608.00965 (2026-08-02; v2 2026-10-16) — https://arxiv.org/abs/2608.00965
  - Verification Theatre, IACR ePrint 2026/192 (2026-02-05; revised 2026-06-25) — https://eprint.iacr.org/2026/192
  - Signal Shot blog, L. de Moura (2026-04-20) — https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/
  - Symbolic Software ML-DSA post (2026-02-17) — https://symbolic.software/blog/2026-02-17-cryspen-mldsa/
- Analysts and press:
  - Forrester blog (2026-02-23) — https://www.forrester.com/blogs/claude-code-security-causes-a-saas-pocalypse-in-cybersecurity/
  - Globes, JFrog −25% (2026-02-22) — https://en.globes.co.il/en/article-1001535714
  - Globes, Snyk layoffs (June 2026) — https://en.globes.co.il/en/article-1001546903
  - Implicator (2026-02-20) — https://www.implicator.ai/jfrog-lost-25-in-one-day-ai-native-startups-have-more-to-lose/
  - The Register, Snyk CEO (2026-02-20) — https://www.theregister.com/2026/02/20/snyk_ceo_stands_down/
  - Tech.eu, Snyk filing (2026-10-01) — https://tech.eu/2026/10/01/snyk-laid-off-over-200-employees-revenues-top-300m/
  - The Decoder, Codex Security (2026-03-06) — https://the-decoder.com/openai-launches-codex-security-an-ai-agent-designed-to-detect-vulnerabilities-in-software-projects/
  - The Decoder, DevDay (2026-09-29) — https://the-decoder.com/openai-expands-codex-and-its-api-at-devday-with-security-scans-a-decisions-api-and-ultrafast/
  - The Hacker News, CodeMender (October 2025) — https://thehackernews.com/2025/10/googles-new-ai-doesnt-just-find.html
  - TechCrunch, depthfirst (2026-01-14) — https://techcrunch.com/2026/01/14/ai-security-firm-depthfirst-announces-40-million-series-a
  - Fortune press release, Corridor (2026-03-18) — https://fortune.com/press-releases/corridor-raises-25m-series-a-ai-coding-security-2026-03-18
  - Help Net Security, Backslash (2026-02-10) — https://www.helpnetsecurity.com/2026/02/10/backslash-security-19-million-series-a-funding/
  - The Next Web, Aikido (2026-01-14) — https://thenextweb.com/news/aikido-security-becomes-unicorn
  - SiliconANGLE, Aikido (2026-01-14) — https://siliconangle.com/2026/01/14/aikido-security-raises-60m-series-b-1b-valuation-unify-application-security/
  - SecurityWeek, Socket (May 2026) — https://www.securityweek.com/socket-raises-60-million-at-1-billion-valuation/amp/
  - Fortune, Chainguard (2025-04-23) — https://fortune.com/2025/04/23/exclusive-chainguard-secures-356-million-series-d-as-valuation-soars-to-3-5-billion/
  - GeekWire, Chainguard (April 2025) — https://www.geekwire.com/2025/cybersecurity-startup-chainguard-lands-356m-now-valued-at-3-5b/
  - GeekWire, AWS Kiro (May 2026) — https://www.geekwire.com/2026/aws-targets-ai-slop-with-new-spec-check-in-kiro-coding-tool-amid-scrutiny-of-agent-reliability/
  - SecurityWeek, Semgrep (February 2025) — https://www.securityweek.com/semgrep-raises-100m-for-ai-powered-code-security-platform/
  - TechCrunch, Checkmarx (2020-03-16) — https://techcrunch.com/2020/03/16/insight-partners-sells-security-firm-checkmarx-to-hellman-friedman-for-1-15b
  - BankInfoSecurity, H&F and Checkmarx (September 2024) — https://www.bankinfosecurity.com/blogs/hellman-friedman-wants-to-unload-checkmarx-for-25b-p-3715
  - Crowdfund Insider, Harmonic (November 2025) — https://www.crowdfundinsider.com/2025/11/256050-robinhood-ceo-backed-harmonic-becomes-unicorn-on-series-c/
  - The Block, Certora (2022) — https://www.theblock.co/post/147066/certora-announces-36-million-series-b-funding-round-led-by-jump-crypto
  - HigherGov, Galois DARPA COOP (October 2024) — https://www.highergov.com/contract/HR001125C0300/
- Market data and estimates:
  - StockAnalysis, FROG statistics and ratios (2026-11-12) — https://stockanalysis.com/stocks/frog/statistics/ ; https://stockanalysis.com/stocks/frog/financials/ratios/
  - StockAnalysis, GTLB statistics and ratios (2026-11-12) — https://stockanalysis.com/stocks/gtlb/statistics/ ; https://stockanalysis.com/stocks/gtlb/financials/ratios/
  - StockAnalysis, DDOG and TEAM (2026-11-12) — https://stockanalysis.com/stocks/ddog/statistics/ ; https://stockanalysis.com/stocks/team/statistics/
  - Earnings Whispers via Finviz, JFrog Q3 (2026-11-05) — https://finviz.com/news/418104/jfrog-beats-on-accelerating-cloud-growth-and-raises-again-but-q4-outlook-signals-a-margin-pause
  - Webull, JFrog move (2026-11-05/06) — https://www.webull.com/news/15873322845314048
  - Sacra, Snyk (2026-03-08) — https://sacra.com/research/snyk-at-326m-arr-growing-7-yoy/
  - Sacra, Chainguard (accessed 2026-11-12) — https://sacra.com/c/chainguard/
  - Sacra, Endor Labs (accessed 2026-11-12) — https://sacra.com/c/endor-labs/
  - TrueUp, Snyk (2026-10-29 mark; page blocked) — https://www.trueup.io/co/snyk
  - multiples.vc, Aikido — https://multiples.vc/private-comps/aikido-security
  - StockAnalysis, Semgrep private page — https://stockanalysis.com/private/semgrep/
  - Dealroom, Certora — https://dealroom.co/companies/certora/
  - CB Insights, Certora — https://www.cbinsights.com/company/certora/financials
  - Spotlight AR, 2025 AST Leaders — https://research.oz.spotlightar.com/reports/magic-quadrant-application-security-testing-2025/leaders
- Reference:
  - Wikipedia, Evaluation Assurance Level (accessed 2026-11-12) — https://en.wikipedia.org/wiki/Evaluation_Assurance_Level
  - Wikipedia, DO-178C (accessed 2026-11-12) — https://en.wikipedia.org/wiki/DO-178C
  - Wikipedia, Checkmarx (accessed 2026-11-12) — https://en.wikipedia.org/wiki/Checkmarx

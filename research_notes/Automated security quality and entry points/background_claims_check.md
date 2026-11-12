# Background claims check: seven AI and software-security claims (as of 2026-11-12)

Scope: background claims C2, C3, C4, C6, C7, C8 and C10 (C1 and C9 excluded as instructed). This is a news-brief level check only: who said what, when, in what venue, the headline numbers, and who confirmed it. Each claim gets at most one short quotation from its primary source; publication titles are given in italics. Method: one WebSearch (used for C6), then direct fetches of primary pages on 12 Nov 2026. Company statements that no outside party has confirmed are tagged [company claim, unconfirmed].

## C2. Check Point "ARTEX": 400,791 agent messages, 292 objectives, two weeks of October, under $1,500

### Takeaway
**Verdict: partly confirmed.** Every number appears and each one is Check Point Research's (CPR) own count or estimate, but the claim merges two different campaigns. The 400,791 messages and 292 objectives come from a four-day crypto campaign that CPR estimates cost $145–$300 and that stole nothing. The "two weeks" (14–29 Oct 2026) and the "$1,500" ceiling belong to a separate certificate-theft campaign.

### Cited Findings
- Publisher, venue and date: Check Point Research, *Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns*, research.checkpoint.com, 5 Nov 2026 (no named author). A companion post, *Inside ARTEX: How Autonomous AI Agents Are Being Used in Real-World Cyberattacks*, ran on the Check Point blog the same day, credited to Check Point Research — [CPR report, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/); [Check Point blog, 2026-11-05](https://blog.checkpoint.com/research/inside-artex-how-autonomous-ai-agents-are-being-used-in-real-world-cyberattacks)
- The 400,791 and 292 figures sit in the report's Campaign 2, a failed crypto-draining operation: "Across 292 campaign objectives, 230 findings and 400,791 agent messages, not one cent moved to the attackers pockets." That campaign ran for 4 days, with no calendar dates given. CPR estimates its model cost at $145–$300 from DeepSeek V4 Pro pricing. Elsewhere the report also calls the 292 crypto-payment "domains" and does not reconcile the two uses — [CPR report, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/)
- The two weeks and the $1,500 belong to Campaign 1 (Apple code-signing certificates). It ran from 14 to 29 Oct 2026, and CPR estimates its cost at $700–$1,500 from DeepSeek's published API prices; this is an estimate, not measured spend. A third campaign (gaming accounts) ran about five days at an estimated $180–$360 — [CPR report, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/)
- Where the data came from: CPR analysed exposed databases of misconfigured ARTEX instances. Operators mostly used Chinese models (the DeepSeek family and Kimi K3.1 Pro). Guardrails triggered only on Anthropic's Opus 5.5, after which the operator switched models [company claim, unconfirmed] — [Check Point blog, 2026-11-05](https://blog.checkpoint.com/research/inside-artex-how-autonomous-ai-agents-are-being-used-in-real-world-cyberattacks); [CPR report, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/)
- Outside confirmation: none. Neither page cites authorities, AI vendors or victims confirming the figures. An earlier CrowdStrike blog on criminal ARTEX use is cited only as prior reporting, not as a check on these numbers — [CPR report, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/)

### Inferences
- The merged version probably comes from earlier repo notes. [agents_autonomy_rsi.md](../AI%20capability%20advances%20last%2030%20days/agents_autonomy_rsi.md) puts "campaign Oct 14–29" and "under $1,500" next to the 400,791-message campaign. Correct wording: CPR described three campaigns lasting about 15, 4 and 5 days, with estimated model costs of $700–$1,500, $145–$300 and $180–$360. The largest message count comes from the campaign that failed.

### Gaps
- CPR gives no calendar dates for Campaign 2, so "October" could not be confirmed for the 400,791-message campaign. No outside reproduction of the counts was found.

## C3. Reuters: one hacker breached more than 100 companies using commercial AI agents

### Takeaway
**Verdict: partly confirmed.** Reuters did report this, as an exclusive on 19 Oct 2026. But what it describes is break-ins to the *websites* of more than 100 companies, some of them standalone or vendor-run sites. The story rests on one researcher's observations, which Reuters checked, and Reuters says it could not tell how much data was taken. Outside confirmation is partial: a handful of victims.

### Cited Findings
- Venue, date and byline: Reuters exclusive *How one hacker used AI agents and a few thousand dollars to break into scores of sites*, by Raphael Satter, 19 Oct 2026, 9:58 a.m. EDT. Read through BNN Bloomberg's syndicated copy, which is credited "By Reuters" — [Reuters via BNN Bloomberg, 2026-10-19](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/)
- Headline numbers:
  - Websites of more than 100 companies were breached, in the US, Canada, Australia and Japan, and more than 1,200 sites were attempted.
  - The campaign began on 25 Sep 2026.
  - About US$5,000 was spent on AI usage, roughly $50 per breach.
  - The agents were commercial: reportedly DeepSeek models and Anthropic's Claude Code.

  Source: [Reuters via BNN Bloomberg, 2026-10-19](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/)
- Where the story came from: a report by NorForge principal threat researcher Snorre Fagerland, who observed several hackers. The most prolific was one Chinese-speaking hacker, and Reuters itself reviewed that hacker's platform activity to identify victims — [Reuters via BNN Bloomberg, 2026-10-19](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/)
- What Reuters could not verify: "Reuters could not ascertain the degree to which the breaches resulted in unauthorized extraction of data." — [Reuters via BNN Bloomberg, 2026-10-19](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/)
- Confirmations: three large companies named by Reuters responded; their names are left out here under the brief's no-targets rule.
  - One said it had taken remediation actions and had no indication that sensitive data was accessed.
  - One said the hack hit a standalone product-support site and was contained.
  - One said it was investigating a possible attack on a site run by a third-party vendor.
  - Two smaller businesses acknowledged being compromised, and other victims did not respond.
  - The article carries no comment from DeepSeek or Anthropic and quotes no government authority.

  Source: [Reuters via BNN Bloomberg, 2026-10-19](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/)

### Inferences
- "Breaching more than 100 companies" overstates the story. Accurate wording: Reuters reported (19 Oct 2026) that one hacker broke into websites of more than 100 companies using commercial AI agents for about $5,000. A few victims confirmed incidents, and how much data was taken is unknown.

### Gaps
- The reuters.com original was not fetched; the syndicated copy was used. NorForge's own report was not found. No statement from an AI vendor or an authority was found.

## C4. XBOW's three-bug Chrome chain: Google's confirmation and the "maximum" reward

### Takeaway
**Verdict: confirmed, with caveats.** Three bugs, Google's acceptance and the $250,000 payment are all supported, two of the fixes by Google's own release notes. Two points need care:
- "Maximum" rests on The Hacker News' reading of Google's 2026 rules, because Google's reward table would not load.
- The work was human-directed: one XBOW researcher worked with XBOW's agents on OpenAI's GPT-5.6 Sol over six days. Sources call the result a "full-chain" exploit, not just a sandbox escape.

### Cited Findings
- XBOW's announcement, *XBOW Rewarded for Exploit Affecting a Billion Users* (xbow.com News, 13 Oct 2026, no byline), describes "three separate, previously unknown bugs" and a $250,000 Chrome VRP award, which it calls the first full-chain Chrome award under Google's 2026 rules. It names OpenAI's GPT-5.6 Sol models but neither calls the award a maximum nor says the model is publicly available [company claim, unconfirmed, for the human/AI split] — [XBOW, 2026-10-13](https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users)
- Google's own release notes credit two High-severity Chrome fixes to "Brendan Dolan-Gavitt, XBOW", both listed with reward "[TBD]":
  - CVE-2026-78952: reported 13 Aug 2026, fixed in the 25 Aug 2026 stable update (152.0.7977.64/65).
  - CVE-2026-85045: reported 17 Aug 2026, fixed in the 3 Sep 2026 update (152.0.7977.82).
  - A separate XBOW-credited Medium fix in the 25 Aug notes was reported on 20 Jul 2026 and paid $1,000. It predates the 2–7 Aug work and looks unrelated.

  Sources: [Chrome Releases, 2026-08-25](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0256176589.html); [Chrome Releases, 2026-09-03](https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html)
- CyberInsider (Bill Mann, 14 Oct 2026) reports two things from Google's public issue record: a Google engineer reproduced the three-bug chain, and Google's reward panel approved $250,000 on 31 Aug. It also says the model was publicly available and that Google made no public statement of its own. I did not open the issue record — [CyberInsider, 2026-10-14](https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/)
- The Hacker News (Swati Khandelwal, 14 Oct 2026) makes three points:
  - Chrome's VRP pays up to $250,000 for a full-chain exploit, the most it pays for a single report, and Google paid XBOW that top reward.
  - The model was public.
  - Caution: one of the three bugs has no confirmable public identifier.

  Source: [The Hacker News, 2026-10-14](https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html)
- Google's rules page (bughunters.google.com) served an empty script shell. Chromium's VRP FAQ states no amounts; it only links to the rules — [Google Bug Hunters, Chrome VRP rules (undated)](https://bughunters.google.com/about/rules/chrome-friends/5745167867576320/chrome-vulnerability-reward-program-rules); [Chromium VRP FAQ (latest entry Oct 2026)](https://chromium.googlesource.com/chromium/src/+/main/docs/security/vrp-faq.md)

### Inferences
- Safest wording: Google paid XBOW $250,000 for a three-bug Chrome full chain. The Hacker News calls that the top Chrome VRP award for a single report. The panel approved it on 31 Aug 2026, according to CyberInsider's reading of Google's issue record, and XBOW announced it on 13 Oct 2026. It was human-directed work on a public OpenAI model.

### Gaps
- I could not read the 2026 Chrome VRP reward table, so it is unknown whether bonuses can push a payout above $250,000. Public notes identify only two of the three bugs.

## C6. Linux kernel security list "almost unmanageable" because of AI reports (May 2026)

### Takeaway
**Verdict: confirmed, with wording corrections.**
- **Speaker and venue:** Linus Torvalds, the kernel's lead maintainer, in his Linux 7.1-rc4 release announcement on the Linux Kernel Mailing List (LKML), Sunday 17 May 2026.
- **Wording:** he wrote "almost *entirely* unmanageable", which is stronger than "almost unmanageable".
- **Cause:** he blamed duplicate AI-found reports from many people using the same tools, not "machine-written" reports as such.

### Cited Findings
- Primary text (LKML, subject *Linux 7.1-rc4*, from Linus Torvalds, Sun 17 May 2026): "the continued flood of AI reports has basically made the security list almost entirely unmanageable, with enormous duplication due to different people finding the same things with the same tools." — [LKML mirror (lkml.iu.edu), 2026-05-17](https://lkml.iu.edu/hypermail/linux/kernel/2605.2/01597.html); original [lkml.org link, 2026-05-17](https://lkml.org/lkml/2026/5/17/896) (bot wall in this session)
- In the same email he presented this as one of that week's documentation updates. He said AI-detected bugs are by definition not secret and that treating them on a private list wastes everyone's time. He added that AI tools are fine if they actually help — [LKML mirror, 2026-05-17](https://lkml.iu.edu/hypermail/linux/kernel/2605.2/01597.html)
- Same-day and next-day coverage carried the quote:
  - GamingOnLinux (Liam Squires-Hand, 18 May 2026), fetched.
  - Slashdot (18 May 2026), Tom's Hardware and TechRadar: headlines only, from search results.

  Sources: [GamingOnLinux, 2026-05-18](https://www.gamingonlinux.com/2026/05/linux-head-says-ai-tools-are-great-but-theyre-making-the-security-list-almost-entirely-unmanageable/); [Slashdot, 2026-05-18](https://tech.slashdot.org/story/26/05/18/0238214/); [Tom's Hardware](https://tomshardware.com/software/linux/linus-torvalds-says-ai-bug-reports-have-made-the-linux-security-mailing-list-almost-entirely-unmanageable); [TechRadar](https://www.techradar.com/pro/security/almost-entirely-unmanageable-linus-torvalds-says-ai-bug-hunters-have-ruined-linux-security-mailing-list)

### Inferences
- "Its lead" is right only if read as the kernel's lead, Torvalds. He was not speaking as a designated head of the security list. Greg Kroah-Hartman and Willy Tarreau were not the speakers. The statement is evidence of duplicate volume from AI-assisted finders, not a judgement that the reports were wrong.

### Gaps
- lkml.org showed a bot wall and lore.kernel.org was not attempted; the lkml.iu.edu mirror was used instead. The documentation patch itself was not read. Volume figures attributed to Willy Tarreau appeared only in a search summary and were not verified.

## C7. Anthropic's red team: small open models "months away" from self-replicating on connected devices

### Takeaway
**Verdict: confirmed, with wording notes.**
- **Where the sentence sits:** in the body, not the headline.
- **What it says:** "small AI models", and *capable enough to* self-replicate. It is a capability forecast from a trend line, not an observed event.
- **Where it was published:** anthropic.com/research, under the Frontier Red Team. red.anthropic.com now redirects there.

### Cited Findings
- Post: *AI models may be capable of self-replicating without access to a datacenter*, by William Zhou and Daniel Freeman (Frontier Red Team), anthropic.com/research, 12 Oct 2026 — [Anthropic, 2026-10-12](https://www.anthropic.com/research/self-replicating-ai)
- Key sentence: "small AI models may be months away from being capable enough to self-replicate on commercial internet-of-things (IoT) devices". "Small" means 30B parameters or fewer, and the trend line reaches that level by the end of 2026 — [Anthropic, 2026-10-12](https://www.anthropic.com/research/self-replicating-ai)
- "Open": the models tested were open-weight. The post says only one of them, GLM-5.2, completed full end-to-end replication in its controlled tests [company claim, unconfirmed] — [Anthropic, 2026-10-12](https://www.anthropic.com/research/self-replicating-ai)
- Caveats the authors give:
  - The setup simplifies one step, so results are an upper bound on real-world success.
  - Small models still make mistakes chaining the steps end to end.
  - The capability index is only a proxy metric.
  - The timeline is a rough estimate.
  - They do not yet have a full rogue replicator.
  - Tests ran in a firewalled, emulated environment.

  Source: [Anthropic, 2026-10-12](https://www.anthropic.com/research/self-replicating-ai)
- Venue and outside review: red.anthropic.com returns a 301 redirect to anthropic.com/research/team/frontier-red-team (checked 12 Nov 2026). The post names no outside reviewer or replication — [red.anthropic.com redirect, checked 2026-11-12](https://red.anthropic.com/); [Anthropic, 2026-10-12](https://www.anthropic.com/research/self-replicating-ai)

### Inferences
- Correct wording: Anthropic's Frontier Red Team wrote on 12 Oct 2026 that small models (30B parameters or fewer) "may be months away" from being capable enough to self-replicate on commercial IoT devices. This is an extrapolation from a proxy metric, framed by the authors as an upper bound.

### Gaps
- No outside replication or review by a government institute was found.

## C8. Moonshot: exploit skill follows general coding skill even after security data is removed

### Takeaway
**Verdict: confirmed as Moonshot's own claim [company claim, unconfirmed].** The 90.5%-to-81.0% figures and the "generalize" statement appear in Moonshot's Kimi K3.1 Pro tech blog, not in its Hugging Face model card. "Found" overstates it: Moonshot infers this from one in-house benchmark. Its wording is "cyber tasks", not exploit skill specifically.

### Cited Findings
- Source: *Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence*, kimi.ai (Moonshot AI). The page carries no date; image paths point to 23 Oct 2026, and the post promised weights by 4 Nov 2026 — [Kimi blog, ~2026-10-23](https://www.kimi.ai/blog/kimi-k3-1-pro)
- Figures on Moonshot's in-house xdev-bench-hard (pass@3): 90.5% for the checkpoint trained without the removal measures, against 81.0% for the released K3.1 Pro. The chart shows the predecessor Kimi K3 at 33.3 — [Kimi blog, ~2026-10-23](https://www.kimi.ai/blog/kimi-k3-1-pro)
- Interpretation: "stronger general coding and long-horizon debugging capabilities generalize to cyber tasks even after targeted data removal". The blog says cyber-related data was removed from both mid-training and RL while general coding tasks were kept — [Kimi blog, ~2026-10-23](https://www.kimi.ai/blog/kimi-k3-1-pro); [blog capture mirrored on GitHub, 2026-10-24](https://github.com/kakon77777-commits/agiright-evidence/blob/6224a57aa54fc716328ca87fa37accddc6801068/sources/2026-10-24/kimi.txt)
- The Hugging Face model card lists 81.0 on "xdev-bench-hard (Internal)", but it has no 90.5% figure and no data-removal statement — [Hugging Face model card (no date shown)](https://huggingface.co/moonshotai/Kimi-K3.1-Pro)
- Outside check: none. The blog describes no outside evaluation of these scores. Reuters-sourced coverage dated 24 Oct 2026 relayed the figures, according to earlier repo notes; it returned HTTP 403 in this session — [Rappler/Reuters, 2026-10-24](https://www.rappler.com/technology/moonshot-curbs-hacking-ability-kimi-model/)

### Inferences
- The 9.5-point gap measures what removing the data cost. The claim that skill "follows" coding rests on K3.1 Pro's gain over K3 (33.3) on the same in-house test. Accurate wording: Moonshot said (about 23 Oct 2026) that general coding gains carried over to cyber tasks even after it removed cyber data, citing an internal score of 81.0% against 90.5% without removal.

### Gaps
- Nobody outside Moonshot has replicated xdev-bench-hard. The Reuters text was not re-read.

## C10. Google DeepMind machine-proved security properties of Signal's library (vs Signal Shot and CryptoProver)

### Takeaway
**Verdict: confirmed.** The referent is Google DeepMind's AlphaProof Code, announced 10 Nov 2026 with open artifacts. The repo note that found "no DeepMind evidence" is out of date. Two other efforts also exist, but neither is by DeepMind and neither is a finished proof about libsignal:
- Signal Shot (Signal, Beneficial AI Foundation and Lean FRO; platform ready 20 Apr 2026).
- CryptoProver (an academic paper, Aug 2026, on other cryptographic libraries).

### Cited Findings
- DeepMind's post, *Introducing AlphaProof Code: a breakthrough in verifying complex software at depth*, by Pushmeet Kohli and Swarat Chaudhuri (deepmind.google, 10 Nov 2026), makes these claims [company claim; no independent replication reported]:
  - AI agents proved key security properties of the code behind the Signal protocol.
  - The work produced over six million lines of Lean in about four weeks.
  - Every proof is checked by Lean.

  Source: [Google DeepMind, 2026-11-10](https://deepmind.google/blog/introducing-alphaproof-code/)
- Scope, from DeepMind's artifact repository (Apache-2.0): "two AI-generated proofs of security for compiled AArch64 machine code of `libsignal`". The proofs run in a command-line harness with hooked cryptographic primitives — [GitHub google-deepmind/code-verification (dates not shown; created 26 Oct 2026 per earlier repo notes)](https://github.com/google-deepmind/code-verification)
- Who reviewed it:
  - DeepMind says human experts reviewed every specification and its agents flagged about 1% of the code for human review.
  - It thanks Signal's Rolfe Schmidt, Michael Rosenberg and Ehren Kret for feedback on the method.
  - It quotes Kret, as Signal's CTO, calling the approach a major breakthrough.
  - The repository links to a reviewers' site but names no reviewers.

  Source: [Google DeepMind, 2026-11-10](https://deepmind.google/blog/introducing-alphaproof-code/)
- Signal Shot: *Signal Shot: The Platform Is Ready*, by Leonardo de Moura, 20 Apr 2026. It describes a joint project of Signal (Rolfe Schmidt), the Beneficial AI Foundation (Max Tegmark) and Lean FRO to verify the Signal protocol and its Rust code in Lean. At that date it reported tooling ready but no proved properties, and it does not mention DeepMind — [de Moura blog, 2026-04-20](https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/)
- CryptoProver: *An AI Approach to Verified Production Cryptographic Libraries*, by Sun, Fong, Kuang, Jiao, Narodytska, Wu, Dill and Barrett (arXiv 2608.00965; v1 2 Aug 2026, v2 16 Oct 2026).
  - It verifies curve25519-dalek and RustCrypto's chacha20, not libsignal.
  - It took 11.4 hours and US$466.99, against a five-month, three-person original effort.
  - It mentions neither DeepMind nor AlphaProof.

  Source: [arXiv 2608.00965, 2026-08-02 / 2026-10-16](https://arxiv.org/abs/2608.00965)

### Inferences
- Both leads are partly right. [code_supply_chain_verification.md](code_supply_chain_verification.md) predates or missed the 10 Nov post, so its "no DeepMind evidence" line should be treated as superseded. [google_deepmind.md](../AI%20lab%20views%20on%20AI%20progress/google_deepmind.md) cites "over three million lines", which the post as fetched contradicts: it says over six million.
- Accurate wording: DeepMind says its agents produced machine-checked proofs of key security properties for compiled libsignal code. There are two proofs, with the crypto primitives stubbed out (my reading of "hooked") and the specifications reviewed by humans. Signal staff gave feedback, and no independent replication has been reported.

### Gaps
- I did not read DeepMind's technical paper ([PDF](https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf)) or the reviewers' site, and I did not check Signal's own blog for a statement.

## Verdict table and dated source list

### Takeaway
Of the seven claims, five are confirmed once the wording is corrected (C4, C6, C7, C8 as a company claim, and C10) and two are partly confirmed (C2 and C3). None is contradicted outright. Two corrections matter most:
- **C2:** the "two weeks" and "under $1,500" do not belong to the 400,791-message campaign, which lasted 4 days, cost an estimated $145–$300 and failed.
- **C10:** the repo note denying DeepMind's role is outdated.

### Cited Findings

| Claim | As stated | What the source says | Verdict | Source and date |
|---|---|---|---|---|
| C2 | Check Point logged one campaign: 400,791 agent messages, 292 objectives, two weeks of Oct 2026, under $1,500 | 400,791 messages and 292 objectives come from a 4-day crypto campaign (est. $145–$300) that stole nothing. Two weeks (14–29 Oct) and $700–$1,500 belong to a separate certificate campaign. Costs are CPR estimates from API prices. No outside confirmation | Partly confirmed | [CPR, 2026-11-05](https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/); [Check Point blog, 2026-11-05](https://blog.checkpoint.com/research/inside-artex-how-autonomous-ai-agents-are-being-used-in-real-world-cyberattacks) |
| C3 | Reuters: one hacker breached 100+ companies with commercial AI agents | Reuters exclusive (Satter): websites of 100+ companies hit from 25 Sep for about $5,000, based on a NorForge researcher's findings. Data loss could not be ascertained. Three companies responded and two small firms admitted compromise. No vendor or authority statement | Partly confirmed | [Reuters via BNN Bloomberg, 2026-10-19](https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/) |
| C4 | XBOW built a three-bug Chrome sandbox escape; Google confirmed it and paid its maximum bounty | Three-bug full chain; $250,000 approved 31 Aug 2026 (per CyberInsider); announced 13 Oct 2026. Google's notes credit two XBOW fixes (25 Aug, 3 Sep). The "top award" is The Hacker News' reading; Google's table was unreadable. Human-directed, on GPT-5.6 Sol | Confirmed (with caveats) | [XBOW, 2026-10-13](https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users); [Chrome Releases, 2026-08-25](https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0256176589.html); [The Hacker News, 2026-10-14](https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html) |
| C6 | May 2026: the list's lead called the kernel security list almost unmanageable because of machine-written reports | Linus Torvalds, Linux 7.1-rc4 announcement on LKML, 17 May 2026: "almost entirely unmanageable", blaming a flood of duplicate AI reports from many people using the same tools | Confirmed (wording fixed) | [LKML mirror, 2026-05-17](https://lkml.iu.edu/hypermail/linux/kernel/2605.2/01597.html) |
| C7 | Anthropic red team: small open models may be months away from self-replicating on connected devices | Frontier Red Team post (Zhou, Freeman), 12 Oct 2026. The headline says models may self-replicate without a datacenter. The body says small (≤30B) models may be months from being capable of it on IoT devices. Upper-bound and proxy-metric caveats; no rogue replicator yet | Confirmed (wording fixed) | [Anthropic, 2026-10-12](https://www.anthropic.com/research/self-replicating-ai) |
| C8 | Moonshot found exploit skill follows coding skill even after security data is removed | Kimi K3.1 Pro blog (~23 Oct 2026): in-house xdev-bench-hard 90.5% without removal vs 81.0% released (K3: 33.3). Coding gains "generalize to cyber tasks". The model card shows only 81.0. No outside check | Confirmed [company claim, unconfirmed] | [Kimi blog, ~2026-10-23](https://www.kimi.ai/blog/kimi-k3-1-pro); [HF card](https://huggingface.co/moonshotai/Kimi-K3.1-Pro) |
| C10 | Google DeepMind machine-proved security properties of Signal's library | AlphaProof Code (Kohli, Chaudhuri), 10 Nov 2026: two Lean-checked proofs for compiled libsignal code, 6M+ lines in four weeks. Specs human-reviewed; Signal staff gave feedback. Signal Shot (20 Apr 2026) and CryptoProver (Aug 2026) are separate, non-DeepMind efforts | Confirmed (repo note superseded) | [Google DeepMind, 2026-11-10](https://deepmind.google/blog/introducing-alphaproof-code/); [GitHub](https://github.com/google-deepmind/code-verification); [de Moura, 2026-04-20](https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/); [arXiv 2608.00965](https://arxiv.org/abs/2608.00965) |

### Inferences
- In every case the outside confirmation is thinner than the background implies:
  - C2 and C7 rest on the publishing company alone.
  - C8 rests on an in-house benchmark.
  - C10 has machine-checked proofs, but the confirmation comes from the developer and its collaborator (Signal), not from independent replication.
  - C4 is the only claim with direct confirmation from the vendor whose product was attacked (Google).

### Gaps
- What could not be opened in this session, and the workaround used:

  | Source | Claim | Problem | Workaround |
  |---|---|---|---|
  | lkml.org | C6 | Bot wall | lkml.iu.edu mirror |
  | lore.kernel.org | C6 | Not attempted after the lkml.org block | lkml.iu.edu mirror |
  | bughunters.google.com, Chrome VRP rules | C4 | Script shell, no content | None; the reward cap rests on The Hacker News |
  | Rappler/Reuters | C8 | HTTP 403 | Moonshot's own blog |
  | reuters.com original | C3 | Not fetched | BNN Bloomberg syndication |
  | DeepMind technical paper (PDF) | C10 | Not read | Blog post and GitHub repository |

- The shared web-search budget allowed one WebSearch, which was used for C6.

### Dated source list
- Check Point Research, *Hacking on Autopilot: Inside ARTEX Cybercrime Campaigns* (2026-11-05): https://research.checkpoint.com/2026/hacking-on-autopilot-inside-artex-cybercrime-campaigns/
- Check Point blog, *Inside ARTEX: How Autonomous AI Agents Are Being Used in Real-World Cyberattacks* (2026-11-05): https://blog.checkpoint.com/research/inside-artex-how-autonomous-ai-agents-are-being-used-in-real-world-cyberattacks
- Reuters (Raphael Satter) via BNN Bloomberg, *How one hacker used AI agents and a few thousand dollars to break into scores of sites* (2026-10-19): https://www.bnnbloomberg.ca/business/artificial-intelligence/2026/10/19/how-one-hacker-used-ai-agents-and-a-few-thousand-dollars-to-break-into-scores-of-sites-reuters-exclusive/
- XBOW, *XBOW Rewarded for Exploit Affecting a Billion Users* (2026-10-13): https://xbow.com/news/xbow-rewarded-for-exploit-affecting-a-billion-users
- Google Chrome Releases, *Stable Channel Update for Desktop* (2026-08-25): https://chromereleases.googleblog.com/2026/08/stable-channel-update-for-desktop_0256176589.html
- Google Chrome Releases, *Stable Channel Update for Desktop* (2026-09-03): https://chromereleases.googleblog.com/2026/09/stable-channel-update-for-desktop_01882797386.html
- CyberInsider (Bill Mann), *Google pays $250K bounty for AI-assisted Chrome exploit built in six days* (2026-10-14): https://cyberinsider.com/google-pays-250k-bounty-for-ai-assisted-chrome-exploit-built-in-six-days/
- The Hacker News (Swati Khandelwal), *Researchers Used a Public OpenAI Model to Build a $250,000 Chrome Full-Chain Exploit in Six Days* (2026-10-14): https://thehackernews.com/2026/10/researchers-used-public-openai-model-to.html
- Google Bug Hunters, Chrome VRP rules (undated; did not render): https://bughunters.google.com/about/rules/chrome-friends/5745167867576320/chrome-vulnerability-reward-program-rules
- Chromium, VRP FAQ (undated; latest news entry Oct 2026): https://chromium.googlesource.com/chromium/src/+/main/docs/security/vrp-faq.md
- Linus Torvalds, *Linux 7.1-rc4*, LKML (2026-05-17), mirror: https://lkml.iu.edu/hypermail/linux/kernel/2605.2/01597.html; original: https://lkml.org/lkml/2026/5/17/896
- GamingOnLinux (Liam Squires-Hand), *Linux head says AI tools are great but they're making the security list almost entirely unmanageable* (2026-05-18): https://www.gamingonlinux.com/2026/05/linux-head-says-ai-tools-are-great-but-theyre-making-the-security-list-almost-entirely-unmanageable/
- Slashdot story (2026-05-18; headline only): https://tech.slashdot.org/story/26/05/18/0238214/
- Tom's Hardware (date not shown; headline only): https://tomshardware.com/software/linux/linus-torvalds-says-ai-bug-reports-have-made-the-linux-security-mailing-list-almost-entirely-unmanageable
- TechRadar (May 2026; headline only, from search): https://www.techradar.com/pro/security/almost-entirely-unmanageable-linus-torvalds-says-ai-bug-hunters-have-ruined-linux-security-mailing-list
- Anthropic Frontier Red Team (William Zhou, Daniel Freeman), *AI models may be capable of self-replicating without access to a datacenter* (2026-10-12): https://www.anthropic.com/research/self-replicating-ai
- red.anthropic.com, 301 redirect to anthropic.com/research/team/frontier-red-team (checked 2026-11-12): https://red.anthropic.com/
- Moonshot AI, *Kimi K3.1 Pro Tech Blog: Advancing Open Intelligence* (about 2026-10-23; page undated): https://www.kimi.ai/blog/kimi-k3-1-pro
- Kimi blog capture mirrored on GitHub (2026-10-24): https://github.com/kakon77777-commits/agiright-evidence/blob/6224a57aa54fc716328ca87fa37accddc6801068/sources/2026-10-24/kimi.txt
- Moonshot AI, Kimi K3.1 Pro model card, Hugging Face (no date shown): https://huggingface.co/moonshotai/Kimi-K3.1-Pro
- Rappler/Reuters, Moonshot curbs hacking ability (2026-10-24; HTTP 403 in this session): https://www.rappler.com/technology/moonshot-curbs-hacking-ability-kimi-model/
- Google DeepMind (Pushmeet Kohli, Swarat Chaudhuri), *Introducing AlphaProof Code: a breakthrough in verifying complex software at depth* (2026-11-10): https://deepmind.google/blog/introducing-alphaproof-code/
- Google DeepMind, code-verification repository (dates not shown; created 2026-10-26 per earlier repo notes): https://github.com/google-deepmind/code-verification
- Google DeepMind technical paper PDF (not read): https://deepmind.google/documents/36/Formal_Verification_of_Signal_4.pdf
- Leonardo de Moura, *Signal Shot: The Platform Is Ready* (2026-04-20): https://leodemoura.github.io/blog/2026-4-20-signal-shot-the-platform-is-ready/
- Sun et al., *An AI Approach to Verified Production Cryptographic Libraries*, arXiv 2608.00965 (v1 2026-08-02; v2 2026-10-16): https://arxiv.org/abs/2608.00965

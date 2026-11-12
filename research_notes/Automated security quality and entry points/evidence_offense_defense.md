# AI and software security: verification of the background claims and current evidence on the offense–defense balance (research date 2026-11-12)

**STATUS: INCOMPLETE.** Writing of these notes stopped partway through item 1 of section 1, and the remaining sections were not written. Do not treat this file as a complete or final set of notes.

*Access note for the report writer. Research date: 12 Nov 2026. Partway through this session the shared web-search budget ran out, and the Exa and Firecrawl tools had no credits. Later evidence therefore comes only from direct fetches of known URLs and from two government data feeds (CISA KEV JSON, NVD API) that I queried and counted myself. These hosts refused fetches (HTTP 403): openai.com, lore.kernel.org, phoronix.com, rappler.com, techrepublic.com, gartner.com, my.idc.com. As a result OpenAI's own kernel report, Torvalds' LKML post and the Gartner/IDC forecasts were not read directly; items that rely on them cite secondary sources and say so. No Japanese, Korean, Indian, Chinese, Taiwanese or French agency publications were checked, because of the search budget and language limits. "Global" coverage is therefore limited to UK (NCSC), EU (ENISA), German (BSI), US (CISA, DARPA, NIST data), an Israeli vendor (Check Point), a Norwegian-named research firm (NorForge, via Reuters) and Chinese labs (Moonshot, DeepSeek as used by attackers). Tag used throughout: **[company claim, unconfirmed]** means the company that did the work said it, and no outside party has confirmed it. Wherever the evidence contradicts the background or a prior, the text says **Contradiction with background** or **Contradicts prior**.*

## 1. Background items 1–10: primary source, exact date, status, and discrepancies

### Takeaway
None of the ten items is contradicted outright, but two are only partly confirmed and several need correction before use. OpenAI's kernel report is dated 4 Nov 2026, not October. No maintainer has confirmed it, and only 61 of the 948 flaws had upstream fixes after about ten days. The Check Point figures merge two separate campaigns. The person behind item 6 is Linus Torvalds, the kernel's lead, not a head of the security list. The gated programmes admit vetted individuals as well as organisations. Most items rest on the companies' own reports. The core fact was independently confirmed only for items 3, 4 (as reported), 5 and 6.

### Cited Findings

**Verdict summary** (details and sources in the item blocks below)

| # | Background item | Verdict | Main correction or caveat |
|---|---|---|---|
| 1 | OpenAI: 948 kernel exploits, $1.2M | partly confirmed | Published 4 Nov 2026 (run mid-Oct). 948 = distinct flaws (1,169 working exploits). $1,279 each. No outside check. 61 fixed upstream after ~10 days |
| 2 | Check Point: 400,791 messages, 292 objectives, two weeks, <$1,500 | partly confirmed | Two campaigns merged. The 400,791/292 campaign ran 4 days, cost $145–$300 and stole nothing |
| 3 | Reuters: one hacker, >100 companies | confirmed | Websites of >100 companies. Open-source Cairn agents on DeepSeek plus Claude Code. ~$5,000 in tokens |
| 4 | XBOW Chrome chain, Google max bounty | confirmed (via XBOW and The Hacker News) | Full chain, not only a sandbox escape. Built 2–7 Aug 2026. $250,000. Human-directed |
| 5 | curl closed bounty Jan 2026 | confirmed | Stopped 31 Jan 2026. Valid share fell below 5% |
| 6 | Kernel security list "almost unmanageable", May 2026 | confirmed (secondary sources) | Said by Linus Torvalds, the kernel's lead, in the 7.1-rc4 announcement of 17 May 2026 |
| 7 | Anthropic red team: small open models months from self-replicating | confirmed | Exact wording below. The test used a deliberately trivial exploit step. Stated as an upper bound |
| 8 | Moonshot: exploit skill follows coding skill after data removal | confirmed as Moonshot's claim | 90.5% → 81.0% on an internal, unpublished benchmark (23 Oct 2026) |
| 9 | Gated models at OpenAI, Google, Anthropic | confirmed, with nuance | OpenAI and Anthropic also admit vetted individuals. Strong general models are public |
| 10 | DeepMind machine-proved Signal security properties | confirmed, with nuance | Over 6 million lines of Lean. Compiled AArch64 libsignal with hooked crypto primitives. No independent audit yet |

#### Item 1 — OpenAI kernel pipeline, "A thousand fewer paths to root"
- Primary source: OpenAI, "A thousand fewer paths to root", published **4 Nov 2026**. The page refused my fetch (403), so the figures below come from close secondary summaries of it — [OpenAI post (not opened)](https://openai.com/index/a-thousand-fewer-paths-to-root/); date per [ai-tldr summary of the post](https://ai-tldr.dev/releases/openai-linux-kernel-948-lpe/index.md) and [Cloud Security Alliance research note, 5 Nov 2026](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-industrialized-linux-lpe-exploit-genera/)
- Run: target was the "Latest Linux kernel master, mid-October 2026". Reproduction finished within 30 hours, and the full scan and analysis took about 10 days — [ai-tldr](https://ai-tldr.dev/releases/openai-linux-kernel-948-lpe/index.md); [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-industrialized-linux-lpe-exploit-genera/)
- Model: the post names only "an upcoming OpenAI cyber model" — [ai-tldr](https://ai-tldr.dev/releases/openai-linux-kernel-948-lpe/index.md). CSA describes it as an "unreleased, 'upcoming' cyber-focused model that OpenAI has not named" — [CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-industrialized-linux-lpe-exploit-genera/). BleepingComputer (6 Nov 2026) attributes the Linux work to **GPT-6 Cyber**. That model was announced Thursday 5 Nov 2026, rated "Critical" for cybersecurity under OpenAI's Preparedness Framework, and restricted to "a select group of approved customers in OpenAI's Daybreak Red" — [BleepingComputer](https://www.bleepingcomputer.com/news/security/openais-new-gpt-6-cyber-ai-finds-81-firefox-flaws-948-linux-bugs/)
- Programmes: disclosure is staged through OpenAI
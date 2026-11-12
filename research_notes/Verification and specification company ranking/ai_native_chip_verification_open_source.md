# AI-native chip-verification entrants and the open-source threat to proprietary verification and sign-off tools (worldwide)

Date of research: 12 November 2026. Status: WORK IN PROGRESS (partial save 1; sections are filled progressively).

Tag legend: [PRIMARY] filing, paper or official document; [INDEPENDENT] confirmed by an outside party; [COMPANY CLAIM] stated by the company, not confirmed outside; [SECONDARY] press or analyst report only; [UNVERIFIED] could not be verified.

## PARTIAL NOTES (raw, to be restructured)

### Background claim 1: Arm study and arXiv 2609.05658 (checked 12 Nov 2026)
- The brief conflates TWO different sources.
- (a) arXiv 2609.05658 is NOT an Arm study. Title: "Robustness of LLM-Generated SystemVerilog Assertions to Semantics-Preserving RTL Transformations"; sole author FNU Aditi (no affiliation on abstract page); submitted 4 Sep 2026; cs.LG; 10 pages. Two small open code models (Qwen2.5-Coder-7B, DeepSeek-Coder-V2-Lite), 40 programs / 295 assignment behaviours from VERT dataset; three transformations (operand reordering, identifier renaming, redundant parenthesisation); 9.7%-27.0% of behaviours correct on original RTL become incorrect after a semantics-preserving transformation; DeepSeek accuracy 53.9% -> 63.7% under renaming while 19.5% of originally correct behaviours fail. No "806" or "300" in it. [PRIMARY] https://arxiv.org/abs/2609.05658
- (b) The "806 bugs / up to 300 missed" figure is from an independent study by Vikash Kumar, senior verification architect at Arm, reported by Brian Bailey, "Putting AI To The Test", Semiconductor Engineering, 2 Nov 2026: 25 hand-coded designs, 806 hand-seeded bugs, three models: Claude Opus 5 detected 79.2% (missed 20.8%, ~168), GPT-5.4 76.2% (~192 missed), GLM-5.2 62.8% (close to 300 missed). All three reached 100% of self-defined goals and declared sign-off. Each model run three times with different results. RTL not public. [SECONDARY for the numbers; study is by an individual Arm employee, described as "independent study", linked to his Springer book on the VEGA framework] https://semiengineering.com/putting-ai-to-the-test/
- So "frontier models missed up to 300 of 806" is true only of the weakest model tested (GLM-5.2); the best frontier model missed ~168.

### Background claim 2: July 2026 open-model chip and share falls
- Moonshot AI (China) Kimi K3, announced 16 Jul 2026; shares fell Fri 17 Jul 2026. Investing.com (17 Jul 2026): CDNS and SNPS "roughly 9%"; TIKR: CDNS closed $330.11, -9.47%; other reports SNPS -7.8% to -8.2%. [SECONDARY] https://www.investing.com/news/stock-market-news/cadence--synopsys-slide-as-kimi-k3-designs-chip-in-48h-using-no-proprietary-eda-4798775 ; https://www.tikr.com/blog/cadence-stock-fell-9-in-a-day-on-a-chinese-ai-chip-demo-heres-where-the-stock-could-go-in-2026
- The repository MoonshotAI/nano-kpu README: Verilator 5.x + Yosys (>=0.64) + Nangate45 library; area/timing are pre-layout estimates from yosys/abc mapping, "not validated through backend place & route", "not sign-off values"; no tape-out; "a demonstration of Kimi K3, not an official project by Moonshot AI". [PRIMARY] https://github.com/MoonshotAI/nano-kpu
- Analysts: Niraj Patel (Bloomberg Intelligence): "We see no immediate threat to Cadence and Synopsys' revenue bases"; leading-edge chips "entrenched on Cadence and Synopsys' proprietary engines"; BNP Paribas: reaction overdone. [SECONDARY]

### Background claim 3: Harmonic
- Reuters 27 Oct 2026: Harmonic expands Aristotle to C and Verilog; usage-based pricing; DIII-D fusion lab user; no chip-design customer named. [SECONDARY] https://1027wbow.com/2026/10/27/robinhood-ceos-ai-startup-harmonic-expands-into-software-chip-design-verification/

(More to follow.)

### PARTIAL SAVE 2 (raw facts gathered so far; to be restructured in final version)

NOTE ON METHOD: the shared web-search budget for this session ran out part-way through (after about 35 searches by this researcher). From that point only direct page fetches of known URLs were used; no further free-text searches. Gaps caused by this are flagged.

Company facts (all dates 2026 unless stated):
- ChipAgents (Alpha Design AI), Santa Clara CA, founded 2024. Series A $21M (21 Oct 2025, Bessemer lead); Series A1 $50M (17 Feb 2026, Matter Venture Partners lead, total $74M); Series A2 $60M (29 Jul 2026, B Capital new; total ">$134M"); investors incl. Micron, MediaTek, Ericsson, ScOp; Rambus became strategic investor 22 Oct 2026 (amount undisclosed). Valuation undisclosed. Claims: 6x ARR growth H1 2026; 120+ semiconductor companies (Jul), 200+ "enterprise deployments" (Oct). Named customers/case studies: MediaTek, Micron, Ambiq, Whalechip, Andes, eMemory, Analog Devices, Rambus. Product: IC-star (27 Oct 2026). Integrates with customers' existing tools; no own engines named. https://chipagents.ai/newsroom
- Normal Computing, New York, founded 2022. $50M strategic led by Samsung Catalyst Fund (25 Mar 2026), total >$85M. Normal EDA. Claims >half of top-10 semis (unnamed). Built open-source Verilog simulator on CIRCT with AI (blog 2 Mar 2026).
- Cognichip, Redwood City. $33M seed (2025), $60M Series A (1 Apr 2026, Seligman Ventures lead; Lip-Bu Tan on board), total $93M. ">30 semiconductor companies engaged" (claim).
- Ricursive Intelligence, Palo Alto. $35M seed (Sequoia, late 2025); $300M Series A at $4B (26 Jan 2026; Lightspeed lead; DST, NVentures, Felicis, 49 Palms, Radical AI, Sequoia). No named customers.
- Agentrys, San Jose. $24.5M ($19.1M seed led by Etna Labs + $5.4M pre-seed led by MediaTek), announced 26-27 Aug 2026; founder Mark Ren (ex-NVIDIA Research, ChipNeMo lead). Claims >90% on CVDP.
- Bronco AI: backed by 8VC, Elad Gil, SV Angel (site); amounts unverified. DV debug agents; "no per-seat fees".
- MooresLabAI, Austin TX, founded 2025; VerifAgent; "15+ chip companies"; Breker partnership; 93% on CVDP v1.1 agentic verification track (56 of 62 problems scored) [COMPANY CLAIM].
- Architect Labs, Palo Alto: $24M seed (Jun 2026, Kindred Ventures) - "design and provably verify custom chips".
- VerifAIX, Cupertino: $5M seed (Sep 2026, Bluehill VC + Endiya Partners) - spec-first agentic + formal.
- Hiveware, Israel: $24M Series A (Jul 2026, RTP Global) - EDA, emerged from stealth.
- Chipmind, Zurich: $2.5M pre-seed (Oct 2025, Founderful); CHF 1.37M Innosuisse grant (2026).
- Tattvam AI (UK) $1.7M pre-seed Feb 2026; siliXon (UK) $1.5M pre-seed Apr 2026; Astrus (Toronto) $12M Series A Sep 2026; Mach42 (Oxford) $9.5M Jul 2026.
- ChipStack: acquired by Cadence (announced 10 Nov 2025; terms undisclosed); ChipStack AI Super Agent launched 10 Feb 2026.
Incumbents/model makers:
- Synopsys + OpenAI "GPT-Synopsys" (30 Sep 2026): multi-year; OpenAI licenses Synopsys tools; revenue share.
- Synopsys + NVIDIA autonomous DV workflow (26 Jul 2026): "up to 50X faster time-to-validated RTL", availability H2 2026.
- Siemens Questa One Agentic Toolkit (27 Feb 2026): MCP interfaces; works with GitHub Copilot, Claude Code, Cursor, Cline; "not positioned as a path to fully autonomous IC verification" (DAC 2026).
- Cadence Q3 2026 (26 Oct 2026): >100 active AI Super Agent engagements; MediaTek ChipStack in production (50-70% coverage improvement; 1.4-2x effort reduction).
- Anthropic: The Information (3 Nov 2026): ~15-person chip team uses Claude; SNPS/CDNS fell up to ~4%.
- Harmonic (27 Oct 2026) primary: https://harmonic.fun/news/aristotle-software-hardware-verification/ ; Ibex MUL/DIV (3 Nov 2026).

# Gaps: what was not found, and where it was looked for

As of 21 Nov 2026. Each gap lists where the research looked and what would close it.

"Not found" means the item was searched for and not located. It does not mean the item does not exist.

## Cross-cutting limits

- **Tool budgets ran out.** Late in the work the shared web-search budget was exhausted. Firecrawl credits ran out early (they reset about 22 Nov 2026 08:47 UTC). Items searched after that point rest on known URLs only. The 2023 statement coverage for the Korean makers is thin for this reason.
- **Sites that blocked automated access (HTTP 403/404/503):**
  - Applied Materials IR site, newsroom and Kinex product page;
  - KLA product pages and Investor Day 2026 slides;
  - roic.ai and GuruFocus (ASMPT transcripts); Yahoo transcripts;
  - Yole press release (a repost was used instead);
  - Bits&Chips (some articles);
  - Digitimes (paywalled);
  - semi.org (EVG SEMI deck).
- **Transcripts.** Applied, ASMPT (2025 to early 2026), KLA, Onto, Camtek, Nova and most Besi calls were read through third-party transcripts (class T) or press paraphrase (class S), not company-hosted ones.
- **Rules file.** `research/CLAUDE.md` contains no rules block (placeholder only) and `research/prior/` is empty. The conventions used are stated at the top of `dossier.md`.

## Question 1: orders, revenue, installed base, customers, logic/memory split

| Company | Missing item | Where looked | How to close |
|---|---|---|---|
| Besi | HB order value and units per quarter; TCB order value per quarter (except May 2025: 5 systems, ~$20 m) | All six quarterly releases, webinars, AR 2025, H1-26 report, call transcripts. CEO: "we haven't disclosed units" | Not disclosed by company; only lower-bound cumulative totals (150+ → >215) |
| Besi | Quarterly HB revenue or end-market split | Same | Annual AI and computing shares only |
| Besi | Consistent customer counts | HB customers at end-2025: 18 (Q4-25 release, AR, Nov chart) vs 15 (Q2-26 release). TC Next customers: 6 / 5 / 7 | Ask IR; see review_packet conflicts |
| Applied | Orders, backlog, packaging revenue in $ for FY26, Besi-specific income | Six releases, 10-K, 10-Qs | Not disclosed; only growth rates and aggregate strategic-investment gains/losses |
| Applied | Closing of the ~20% Besi stake (HSR expiry, AFM notification) | Applied release 12 Nov 2026; Besi releases | Check AFM register and Applied 8-K after HSR waiting period |
| ASMPT | TCB and HB bookings or revenue per quarter in currency or units; HB installed base; named memory customers; quarterly AP share | Six results announcements, FY25 annual report, IR pages | Not disclosed; AP share given only for 1H and FY, and the series is not like-for-like (restated 1H25 base) |
| K&S | FY26 TCB revenue (guided ">$100 m", not confirmed in 10-K); HBM-tool qualification outcome after May 2026; "Project W" definition | 10-K FY26, 10-Qs, call transcripts | Earnings slides (events page 404) |
| Hanmi | Unit installed base; Micron orders since Apr 2024; memory vs logic split | DART reports 2025–2026 (company omits undisclosed contracts) | Not disclosed; press proxies only |
| Hanwha Semitech | FY2025 standalone audited results; 2026 TC-bonder order amounts; outcome of SHB2 Nano evaluation at SK hynix | Hanwha Vision DART filings and IR decks | Next DART audit-report filing; Korean press |
| SEMES | Bonder revenue, units, orders | DART quarterly reports (bonders inside "semi/display equipment") | Not disclosed |
| SUSS | Cumulative installed hybrid bonders; hybrid revenue; Q1 2025 call transcript (image-only) | Quarterly statements, annual report, CMD 2025, SUSS-hosted transcripts | OCR of the Q1-25 transcript image |
| TEL | Orders (TEL publishes none); quarterly bonder revenue; installed Synapse Si count; hybrid vs fusion split; customers | 18 earnings PDFs FY25 Q1 to FY27 Q2; Investors Guide | Not disclosed |
| EV Group | Revenue, orders, units, installed base, customer count, memory/logic split | All EVG releases 2023–Sep 2026; product pages; Austrian company register (owner Thallner Privatstiftung, no revenue) | Firmenbuch annual accounts (paid) |
| Piotech | HB orders, units, customers; HB revenue for 2026 periods | 2025 annual report, Q1/H1/Q3 2026 reports | Annual report 2026 |
| Yamaha Robotics (Shinkawa) | TCB units, back-end figures by quarter, HBM customers | Yamaha Motor quarterly releases; SEMI briefing Sep 2026 | Not disclosed |
| Toray Engineering | Any financials; HBM customers | Product pages | Not disclosed (unlisted subsidiary) |
| LG Electronics PRI, Maxwell, NAURA unit, Qinghe Jingyuan, Canon, Bondtech | Orders, units, verified product status | Press (several only as search summaries) | Company filings or releases; Maxwell and Canon items unverified |
| Other Korean makers (Protec, PSK Holdings, Zeus) | Whether they make TC or hybrid bonders for HBM | Not checked (search budget) | Korean press search |

## Question 2: management statements on timing

| Item | Status | Where looked |
|---|---|---|
| ASMPT verbatim CEO statements, Oct 2025 and Mar 2026 calls (16-high/20-high/JEDEC) | Paraphrase and snippet fragments only (class S) | roic.ai and GuruFocus (403); inews24 paraphrase used. ASMPT posts call audio (MP3) on its IR page, not transcribed |
| ASMPT Q1 2026 call | Not covered | Same |
| Hanwha Semitech statement on when HBM moves to HB (generation, stack, year) | Not found; only its own tool dates | Korean press, Hanwha Vision IR decks |
| SEMES named-executive statement on HBM HB timing | Not found beyond a team leader (Aug 2025) | Korean press, DART |
| EVG executive statement on HBM HB timing | Not found in any release; SEMI deck (Jun 2025) blocked | evgroup.com news 2023–2026 |
| TEL statement on HBM HB generation or year | None in any material reviewed | 18 earnings documents, FCMN 2026 deck |
| Applied statement on HBM HB generation or year | None ("future generations") | Call transcripts FY23–FY26 |
| Korean makers' 2023 statements | Not found (search budget) | — |
| SK hynix 2023 statements; Samsung beyond the Oct 2023 blog | Not found | — |
| Micron dated generation or year for HB in HBM | Never stated (not found); HBM4 bonding method not confirmed | Micron prepared remarks, conference coverage |
| Samsung's own Q4-25 call transcript | Not checked directly; quotes come via Asiae, Hankyung and Green Economy | — |
| Samsung Q1–Q3 2026 call remarks on HB | None found | Herald, Asiae coverage |

## Question 3: push/pull facts

| Item | Status |
|---|---|
| JEDEC primary document for 775 µm | The JESD270-4 release (17 Apr 2025) gives no height. 775 µm is from press (ZDNet, TrendForce) and company statements (Besi, Hanmi, ASMPT, SUSS) |
| JEDEC ~900 µm (HBM4E) and up to 1,000 µm (HBM5) | Reported proposals only. No adoption or ballot found as of 21 Nov 2026 |
| "12–13% lower thermal resistance" for Samsung HB (prior repository material) | Not found in any source. Samsung's own figure is ">20%" (P). Besi cites Samsung ECTC 2026 at "up to 30%" (P) |
| HB yield figures for HBM (any maker) | Not disclosed. Only SK hynix's requirement (90–98%) |
| Cost per bit, HB vs TCB/MR-MUF | Not found. Only tool prices, process-cost ratios (Besi ~6x vs reflow; SK hynix guest note 2–3x vs flip chip) and SemiEngineering's qualitative "more expensive per package, not necessarily per bit" |
| HBM-specific throughput comparison (UPH) | Tool-level only (~1,600 die/hr Kinex; Besi "near 2,000"; TCB 500–1,000 die/hr from a 2022 SemiAnalysis excerpt) |
| Primary ECTC/IEDM/ISSCC 2024–2026 papers by Samsung or SK hynix on HBM HB | Not retrieved; secondary summaries only. Chip Scale Review 2024 returned 404 |
| AMD or Google stack-height requirement | Not found. NVIDIA only indirect (Rubin Ultra 8-Hi evaluation; Samsung's statement that NVIDIA asked to accelerate) |
| Fluxless TCB adoption by Samsung or Micron | Not confirmed. A Chinese-language report of a Besi fluxless trial order from Micron was not retrieved and is excluded |
| Status of Samsung–Besi Pyeongtaek order after Jul 2026 | Not found |
| SemiAnalysis bonder-market forecast; Yole 2025 HB base ($152 m) | Paywalled; Yole base seen only in a search excerpt |

## Question 4: inspection and metrology

| Item | Status | Where looked |
|---|---|---|
| Any third-party inspection or metrology supplier named by a bonder maker as integrated in, or qualified with, its line | **Not found for any of the 13 bonder makers** | Bonder product pages (Besi, EVG, SUSS, ASMPT, Shibaura, Toray), Applied/Besi releases, DART product tables (Hanmi, SEMES), searches pairing each bonder maker with KLA, Onto and Camtek |
| Integrated inspection module on ASMPT (LITHOBOLT, FIREBIRD), K&S (APTURA), Hanwha SHB2 Nano, SEMES hybrid bonder, Yamaha, Toray | Not found | Product pages, ECTC 2026 release, Korean press |
| HB-specific inspection revenue or orders at KLA, Onto, Camtek, Nova, PVA TePla, Nordson | Not disclosed (packaging/HBM aggregates only) | Releases and call transcripts |
| KLA hybrid-bonding product pages | Blocked | kla.com |
| Nova Q1 2026 HB "pull-ins" remark; Camtek Q2 2026 Hawk/HB remark | Paraphrase only | Transcripts unreachable |
| Auros HBM IR-overlay qualification status | Analyst report relayed by search; unverified | — |
| Koh Young, Park Systems (Intel NX-Hybrid WLI), Intekplus, Hitachi FineSAT for HB, Excillum nano-CT | Unverified or not fetched | — |

## Question 5: the [I] range

The range rests on statements that are themselves forecasts. Inputs that would tighten it and were not available:
- any memory maker's qualified-customer schedule for a 16-high HBM4E;
- a JEDEC decision on HBM4E/HBM5 height;
- Samsung's confirmed Pyeongtaek tool orders (vendor, count, delivery);
- SK hynix's HB yield against its own 90–98% bar.

## Legal and corporate

| Item | Status |
|---|---|
| Hanmi vs ASMPT dispute | Not found. Hanmi's DART litigation table lists only the two Hanwha cases |
| Legal disputes involving ASMPT, K&S or Japanese makers | Not found in filings. Press not searched (budget) |
| Takeover approaches to Besi (Mar 2026) | Primary Reuters article not retrieved; relayed via TrendForce and Cryptonomist. No later status found |
| Besi strategic review (16 weeks, conclusion "early January" 2027, per CEO, T) | Outcome pending |

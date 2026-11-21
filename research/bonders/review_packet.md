# Review packet: hybrid bonding timing, equipment side

For a reviewer checking `dossier.md` before it is used. It covers:
- the conclusion;
- the claims the conclusion leans on, and how to check each;
- the quotes most at risk of transcription error;
- the conflicts found between sources;
- the inference choices a reviewer may want to challenge.

IDs refer to `evidence.csv`.

## 1. The conclusion under review

**Finding.** Every dated statement found from bonder makers and memory makers between 2023 and Nov 2026 moved hybrid bonding (HB) in HBM later. None moved it earlier. The one partial exception is that two makers lowered the stack-height trigger:
- Besi: ">=12Hi" in Nov 2026;
- Hanmi: "16단 이상" (16-high and above) in its Q3-26 filing.

Both did so while dropping or pushing out a date.

**[I] Range.** First volume use of HB in HBM falls between **2H 2028 and end-2029, most likely 2029**. It rests most on two statements:

| # | Statement | Class | IDs | Role |
|---|---|---|---|---|
| 1 | Besi Q3-26 release, 22 Oct 2026: shortages "extended the use of lower stack heights"; HB adopted "over the next two years" | P | 01-063, 01-064 | Early bound |
| 2 | Hanmi Chairman Kwak Dong-shin, 15 Jul 2026: HB "around 2029" for mass production of "16-high and above" HBM | S, written interview via MK/Daum | 03-046 | Central and late anchor |

**Corroboration (independent sources that agree):**
- ASMPT CEO: "2029, 2030 … or even 2031" (02-040, T);
- Counterpoint: SK hynix HBM5 with HB 2029–2030 (05-051, S);
- Samsung Pyeongtaek line: large-scale HB 2029–2030 (05-034, S);
- Camtek: HB business "in the '28 and onwards" (06-033, T).

**Strongest counter-evidence (would pull earlier):**
- Samsung, Jan 2026: "some commercialization … at the HBM4E stage" (05-030, 03-092, S). Samsung's HBM4E mass production is set for 1H27 (05-036, S).
- Besi's Nov 2026 market slide still says "Hybrid adoption in memory estimated to begin in 2027".

## 2. Load-bearing claims and how to check them

| # | Claim in dossier | IDs | Class | How to verify | If wrong |
|---|---|---|---|---|---|
| 1 | Besi dropped its 2027 HBM date in Oct 2026 | 01-057, 01-059, 01-063 to 01-066, 01-068 | P + T | Read Besi PR_Q3-2026.pdf p.1–2; compare the Jun 2026 Investor Day slide with the Nov 2026 presentation. Check whether "First mover is preparing for HVM in 2027" is truly absent from the Nov deck (the absence is [I] from a slide comparison) | Early bound moves to 2027–1H28 |
| 2 | Hanmi "around 2029, 16-high and above" | 03-046 | S | Open the Maeil Business interview (Daum link) and confirm the Korean sentence and that it is Kwak's written answer, not reporter narrative | Central anchor weakens; ASMPT/Counterpoint still give 2029–30 |
| 3 | ASMPT CEO "maybe 2029, 2030 … or even 2031" and TCB "into HBM5" if JEDEC goes "beyond 900" | 02-040, 02-041 | T (Investing.com) | ASMPT posts call audio (MP3) on its IR site; check against the 28–29 Jul 2026 recording | Removes one corroborating source |
| 4 | Samsung "some commercialization … at the HBM4E stage" and "16-stack … unnecessary" (Q4-25 call, 29 Jan 2026) | 05-030, 03-092 | S (Asiae AI translation; Hankyung) | Samsung's Q4-2025 earnings-call transcript or IR Q&A (Korean). Confirm both sentences and that they are company words | The "earlier" case is stronger or weaker |
| 5 | SK hynix keeps Advanced MR-MUF for HBM4 and 12-high HBM4E | 05-012, 05-020 | P | SK hynix newsroom releases of 12 Sep 2025 and 18 Jun 2026 | Low risk |
| 6 | SK hynix HB yield bar 90–98%, lifetime 3–5 years | 05-025, 03-099 | S | Herald Business 20 Sep 2026 and MTN 24 Sep 2026 both paraphrase a SEMI panel talk by Kim Ji-hoon. Look for the SEMI event slides | Weakens one push factor |
| 7 | JEDEC: 775 µm for HBM4; ~900 µm and up to 1,000 µm proposals | 05-001 to 05-006 | S (except 05-002) | No JEDEC primary gives a height. Treat 775 µm as industry-confirmed (several companies cite it) and 900/1,000 µm as reported proposals only | If 900 µm is adopted, push to 2030 |
| 8 | NVIDIA evaluating or moving to 8-Hi for Rubin Ultra | 05-043, 05-044 | S (TrendForce citing ZDNet) | NVIDIA has not confirmed. Check for any NVIDIA or memory-maker statement | Demand-side push weakens |
| 9 | SK hynix bought an Applied + Besi inline HB system (~KRW 20 bn), "first … intended for mass production" | 05-018 | S (The Elec via TrendForce) | Neither Applied nor Besi named the buyer. Besi's Q1-26 "repeat orders from a memory customer for HBM" (01-023) is consistent | Pull factor weaker |
| 10 | No bonder maker names a third-party inspection supplier in its line | 4.1 matrix; gaps.md Q4 | Absence finding | Absence is only as strong as the search. KLA and Applied pages were blocked. Check kla.com HB pages and the Applied Kinex page manually | Q4 answer changes for that pair |
| 11 | Besi HB customers 23 (logic 12, memory 3, photonics 4, R&D 4) | 01-033, 01-036 | P; split is [I] | The total is from the release. The split was decoded from chart labels on slide 34 of the Nov 2026 deck; re-read the chart | Memory share of HB customers changes |
| 12 | Hanmi revenue and DART order list | 03-001 to 03-027 | P | DART rcpNo given for each row | Low risk |
| 13 | Applied ~20% Besi stake agreed 26 Oct 2026, pending HSR | 01-079 | P (8-K) | SEC EDGAR 8-K; AFM register for closing | Low risk |

## 3. Quotes to spot-check before external use

Many pages were read through a summarising fetch tool. Quotes are verbatim as the tool returned them, but have not been checked character by character.

**Highest priority, used in summary or section 5:**
- **01-063 / 01-064** (Besi Q3-26 release; PDF text; low risk).
- **03-046** (Korean, MK; translation is ours).
- **02-040 / 02-041** (Investing.com transcript; speaker names in that transcript are sometimes garbled, e.g. the new ASMPT CEO is rendered "Bassel Gamal").
- **05-030** (Asiae English AI translation of a Korean call).
- **05-041** (Micron CTO; translated from Chinese by Business Next, then by us).
- **06-033** (Camtek COO; TradingKey transcript).
- **01-054, 01-059** (Besi call quotes; StockAnalysis transcripts).

**Paraphrases presented with quotation marks.** These are reporters' sentences, not company words. The dossier labels them, but check that the labels survived:
- 05-011 (KED: "Starting from 20-layer stacking, however, hybrid bonding is essential, he said.");
- 05-013 (DealSite via TrendForce);
- 05-023 (Bits&Chips);
- 02-027 (inews24 paraphrase of ASMPT CEO).

**Search-snippet only, page not opened:**
- 02-017 (ASMPT Oct 2025 call fragment);
- Maxwell, Canon, Koh Young and Park Systems items (kept out of the evidence rows, or marked).

## 4. Conflicts and contradictions found

| # | Conflict | Sources | Handling in dossier |
|---|---|---|---|
| 1 | Besi HB customers at end-2025: 18 vs 15 | Q4-25 release, AR 2025, Nov 2026 chart (18) vs Q2-26 release and call (15) (01-015, 01-027) | Both shown; 18 used in the series. [I] 15 matches end-2024 |
| 2 | Besi TC Next customers: 6 (Apr 2026) → 5 (Jun 2026 slide) → 7 (Oct 2026 call) | 01-024; Jun 2026 Investor Day slide (URL as 01-057); 01-035 | Shown as reported |
| 3 | Samsung HBM4 volume bonding: EE Times says Samsung "is using hybrid bonding" for HBM4; TrendForce and ZDNet say both makers kept TC for HBM4 | EE Times 12 Jan 2026; TrendForce 7 Jul 2026 | [I] Volume HBM4 on TC-NCF; HB HBM4 = samples (Samsung's own call mentions only samples) |
| 4 | Samsung HB thermal gain: 12–13% (repository prior material) vs >20% (Samsung GTC, P) vs up to 30% (Besi citing Samsung ECTC 2026) vs 35% (SK hynix slide, different baseline: vs MR-MUF) | 07-012, 05-032, 07-005, 05-021 | 12–13% not found anywhere. Dossier uses company figures |
| 5 | TrendForce (Apr 2026, via The Elec) wrote that the industry expected HB "to start with HBM4 … 2H26 or into 2027", which contradicts SK hynix's own positioning (MR-MUF through HBM4E 16-high) in the same period | TrendForce, 29 Apr 2026 (URL as 05-017) | Reported as a press view, not used |
| 6 | Korean analysts (Oct 2025): HB ~50% of HBM output by 2028, vs every 2026 company signal | 05-054 | Shown in push/pull table as a pull forecast; [I] looks stale |
| 7 | Sony first Cu-Cu HB: 2016 (TechInsights) vs 2010 (SK hynix guest note) | 05-056; SK hynix newsroom guest note (URL as 07-008) | 2016 used. [I] 2010 conflates stacking with Cu-Cu |
| 8 | Hanwha first-generation hybrid bonder: delivered 2022 (company) vs 2021 (Money Today) | 03-074 | 2022 used (company statement) |
| 9 | ASMPT AP revenue: 1H25 US$326 m (Jul 2025) vs implied ~US$290 m base for the 1H26 "+17%" | 02-006, 02-036 | Series flagged as not like-for-like |
| 10 | Hanmi wide TC bonder launch: H2 2026 → "early this year" (Money Today, likely error) → end-2026 → H2 2026 → H1 2027 | 03-040 to 03-048 | Shown as drift |
| 11 | LG hybrid-bonder mass production "2028" (press) vs LG: report "premature" | 03-103, 03-104 | Both shown |
| 12 | Besi Nov 2026 deck: drops "First mover … HVM in 2027" but keeps "Hybrid adoption in memory estimated to begin in 2027" | 01-068 (same Nov 2026 deck) | Both shown; [I] read as a softened, not a reaffirmed, 2027 |

## 5. Inference choices a reviewer may challenge

1. **Definition of "first volume use".** Production shipments into a customer's qualified product; samples and qualification lots excluded. A looser definition (first production lot) would move the range earlier, to 2H 2027–2028.
2. **Reading Besi's "over the next two years" (22 Oct 2026) as adoption by about late 2028**, and adoption as preceding volume. Besi could mean qualification or first orders.
3. **Weighting Hanmi despite its incentive.** Hanmi sells TCB, so it benefits from a late HB date. It is still given weight because it is building HB capacity (plant 7, second-generation prototype) and because three other sources land on 2029–2030.
4. **Applied's ~90% packaging growth treated as TCB, TSV and micro-bump driven, not HB.** CFO Hill says "a large portion" is HBM-related packaging (01-098), and no memory maker has HB in volume.
5. **Proxies:**
   - ASMPT revenue from Korea as a proxy for HBM TCB shipments (02-026, 02-039);
   - Hanmi export share as a proxy for Micron (03-013);
   - Hanwha's Q3-26 jump as partly panel-level packaging (03-072).
   All are labelled [I].
6. **Besi customer-segment split decoded from chart labels** (01-036).
7. **Treating K&S's change from "first half of fiscal 2027" to "fiscal 2027 … customer evaluation" as a slip.** It could be wording only.

## 6. Source quality summary

**evidence.csv: 558 rows.**

| Class | Rows | Meaning |
|---|---|---|
| P | 348 | Company primary: releases, filings, DART, slides, product pages, company-hosted transcripts |
| T | 70 | Verbatim call transcripts hosted by third parties |
| S | 140 | Press, analysts, paraphrase |

- The class is derived from the URL and the recorded source type. The original label is kept in `source_type_as_recorded`.
- Third-party transcripts were labelled S by some research passes and P by others. The `source_class` column normalises them to T.
- **Row prefixes** match the research pass that produced them:

  | Prefix | Research pass |
  |---|---|
  | 01 | Besi / Applied |
  | 02 | ASMPT, K&S, Japanese TCB makers |
  | 03 | Korean makers |
  | 04 | EVG, SUSS, TEL, Piotech and others |
  | 05 | Memory makers, JEDEC, analysts |
  | 06 | Inspection and metrology |
  | 07 | Rows added during synthesis for items quoted in the notes' narrative but missing from their tables |

- **Rows with no stable public URL:**
  - DART rows use `dart.fss.or.kr` rcpNo links.
  - Row 07-012 points to a file in this repository (a git path).

## 7. Deviations from the brief

- **Rules file.** `research/CLAUDE.md` has no rules block (placeholder text only), and `research/prior/` is empty. Modules A and B were skipped as instructed. The tagging convention (P/T/S plus [I]) and the file layout were therefore set for this task; re-map them if the intended rules differ.
- **Scope added:**
  - Kulicke & Soffa, Shibaura, Yamaha Robotics (Shinkawa), Toray Engineering, Piotech, NAURA's acquired unit, Maxwell, Bondtech, SET, LG Electronics PRI, Canon (unconfirmed);
  - inspection suppliers on the supply side (KLA, Onto, Camtek, Nova, PVA TePla, Auros, others).
- **"Last 6 reported quarters"** follows each company's own reporting. Exceptions:
  - EVG is private and publishes no periodic figures.
  - SEMES and Hanwha Semitech are reported through DART and parent IR.
  - TEL and Shibaura have March fiscal years.
  - K&S has an October fiscal year.

## 8. Reviewer checklist

- [ ] Re-read Besi PR_Q3-2026.pdf, the Jun 2026 Investor Day deck and the Nov 2026 deck. Confirm the timing wording and the dropped bullet (claim 1).
- [ ] Confirm the Hanmi 15 Jul 2026 Korean quote and its attribution (claim 2).
- [ ] Check the ASMPT 28–29 Jul 2026 call audio for the 2029–2031 quote (claim 3).
- [ ] Find Samsung's own Q4-2025 call wording on HBM4E HB and 16-stack (claim 4).
- [ ] Look for a JEDEC decision on HBM4E/HBM5 height after Jul 2026.
- [ ] Try kla.com and the Applied Kinex page manually for named inspection partners (claim 10).
- [ ] Spot-check five random T rows and five random S rows against their URLs.
- [ ] Confirm the closing of Applied's ~20% Besi stake (AFM register).

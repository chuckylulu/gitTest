# Q findings: second attempt at Q5 (Bruker in X-ray / hybrid metrology since 2026-04-20; Bruker remarks on Onto, Rigaku and X-ray competition)

Scope: Bruker semiconductor metrology only. Bruker's FY ends Dec 31, so FY2026 = Jan-Dec 2026. Research date 2026-11-21.
Evidence rows: `research/out/bruker_semi/parts/Q.csv` (Q001-Q014). `quote_check.py`: 12 FOUND, 2 rows have no quote ([I]). No rows NOT FOUND.
Script: `research/out/bruker_semi/calc/Q_sitemap_scan.py` scans the saved bruker.com sitemap.

## Bottom line
- **After 2026-04-20, Bruker announced no X-ray-metrology or hybrid-metrology partnership, product launch, investment or acquisition.** That covers X-ray CD, X-ray combined with optical or AFM data, and ML-based hybrid metrology [I] Q014.
- **Bruker made no public statement about Onto Innovation, Rigaku, the Onto-Rigaku stake or X-ray competition** in any source read.
- **The second attempt did add Bruker's own 2026 X-ray statements.** Most are from technical talks and trade-press quotes (see section 1).

## 1. What the second attempt added

### Bruker's own 2026 X-ray technical statements
These are FCMN 2026 posters by Bruker staff (Monterey, 16-19 Mar 2026). They come before the window.
- **"Hybrid analysis" in Bruker's own work is X-ray only** [F] Q001. XRR and HRXRD from a Sirius-XRD inline tool are fitted together. The poster reports that this "reduces thickness/composition parameter correlations and improves repeatability".
  - It does not combine X-ray with optical or AFM data, and uses no ML.
  - Micro-XRF and XRDI are described as complementary screening methods [F] Q002.
- **The micro-XRF packaging poster names a "Sirius-FW G2"** [F] Q003.
  - The live product page still calls Sirius-FW a "fourth generation" platform (P014).
  - No release or page for a G2 launch was found.
- **The same micro-XRF poster gives two roadmap statements** [C]:
  - The HBM / advanced-packaging roadmap "dictates ... an aggressive roadmap for metrology equipment development" (Q004).
  - For bumps below 10 µm, "additional solutions are being considered", such as the low-energy Ag Lα line (Q005).

### Inside the window: SemiEngineering quotes of Bruker semi staff [S]
- **2026-08-11 (Q006), J. van der Meer, product marketing manager.** "In X-ray metrology, the holy grail" is patterned-target measurement that matches blanket-wafer results, and "That will require new types of X-ray sources." This is the only post-April statement found about Bruker's X-ray direction. It names no product, partner or date.
- **2026-09-10 (Q007).** Metrology specs must be "in the sub-angstrom range". X-ray diffraction imaging is used to find microfractures in warped wafers.
- **2026-11-10 (Q008), J. Wall, Bruker JV UK.** XRDI full-wafer subsurface inspection runs at "~20wph" for in-line or at-line use. The quote appears in a hybrid-bonding article.
- **None of these mentions Onto, Rigaku, CD-SAXS, ML or hybrid metrology.**

### What Bruker means by "hybrid metrology"
Bruker's own published use of the term is **AFM + optical profilometry**: S. Lesko, SemiEngineering, 2025-08-12 [S] Q009. That predates the window.

### Acquisitions
Bruker's 2026 acquisitions to Sep 30 were [F] Q010-Q012:
- Tofwerk (TOF mass spectrometry), 2026-01-06.
- Mimetas (organ-on-chip), 2026-08-07.
- Small "Other" deals.

Tofwerk and Mimetas are in the BSI BIOS segment; the note does not give a segment for "Other". None is semiconductor X-ray metrology.

### Bruker newsroom
The bruker.com English sitemap lists 28 news items for 2026 [I] Q013. None concerns X-ray metrology, hybrid metrology, Rigaku or Onto. The three semi-related items are:
- the AFM-IR/imec investment (Apr 7);
- the eWARP TKD / XFlash FlatQUAD 2L detectors (Aug 3);
- the XFlash 7200 FIRE EDS detector (Aug 31).

Also listed but out of scope: the D8 ADVANCE HE / DISCOVER HE high-energy XRD launch (Jun 2026), which targets batteries and catalysts, not fabs. The 2026 webinars (113) and event pages (427) include no SEMICON or X-ray-metrology page.

### Related items that are not X-ray
- **Bruker optical (FilmTek), not X-ray.** A 2026-10-27 webinar presents combined multi-angle reflectometry and spectroscopic ellipsometry. In SemiEngineering 2026-07-07, C. Claypool (FilmTek R&D) said the next generation will measure up to 650 µm thick films for bump/pillar packaging. Neither is X-ray, so neither got a Q row. Files are saved: `2026-11-21_bruker_beyond-traditional-ellipsometry--high-accuracy-thi.html` and `2026-07-07_semiengineering_article-inspection-and-metrology-catching-up-for-high.html`.
- **8-Ks read via the us.kabutan.jp mirror.** None is an acquisition or partnership filing (no Item 1.01 or 2.01).
  - 2026-08-14 and 2026-10-29: dividends.
  - 2026-11-05: segment recast effective 2026-07-01. BSI NANO is unchanged. Saved as `2026-11-05_bruker-via-kabutan-mirror_8-K-2026-11-05-segment-recast.html`.
  - 2026-11-12: director appointment and dividend.

## 2. Searches run (modalities)
- **(a) bruker.com.**
  - Read the news and events listing pages (they load results by JavaScript and hold no items) and the en/ja/zh/ko/de sitemaps.
  - Read the 2026 webinar and event slugs, the semiconductor resource library, the RADS software page, and app notes AN5200 (©2024) and AN5201 (©2025). None is a 2026 launch.
  - The "From Structure to Insight" Taiwan event (2026-11-24) covers lab XRD and XRM, not fab metrology.
- **(b) Press releases.**
  - WebSearch on Business Wire and site:businesswire.com found these 2026 Bruker releases: imec AFM-IR (Apr 7), the Q1-Q3 results, the BEST-Luvata superconductor deal (Sep 3), a $600M mandatory convertible, Atinary, MIMETAS, Tofwerk, D8 HE, and the EDS/TKD detectors.
  - None is about semi X-ray or hybrid metrology. No GlobeNewswire use found.
- **(c) Conferences and papers.**
  - Searched: SPIE AL 2026, FCMN 2026 (abstract book read), ECTC 2026, ASMC 2026, IEEE Hybrid Bonding Symposium 2026, and SPIE/JM3 papers with Bruker authors on CD-SAXS or XCD.
  - The X-ray talks found at the Hybrid Bonding Symposium are by Sigray and Excillum, not Bruker. Sigray page saved for reference only: `2026-11-21_ieeetv_HBS-talk-xray-device-reliability.html`, not cited.
- **(d) 8-Ks.** Read via the us.kabutan.jp mirror (see above). There is no cloudfront index, because file names are UUIDs.
- **(e) Trade press.**
  - The SemiEngineering Bruker entity page lists 2026 articles that mention Bruker. All post-April articles that mention Bruker were read (Jul 7, Aug 11, Sep 10, Nov 10).
  - Search found no EE Times, Semiconductor Digest or Electronics Weekly item quoting Bruker on Rigaku, Onto or hybrid X-ray metrology.
  - An Oppenheimer note on Onto-Rigaku (via placera.se snippet) does not name Bruker. It is a lead only and was not saved.
- **Firecrawl search:** daily credits exhausted on first call ("Insufficient credits"); not used further.

## 3. NOT DISCLOSED
- **Any Bruker comment on Onto, Rigaku, the Onto-Rigaku stake or X-ray competition.** NOT DISCLOSED (read: SemiEngineering 2026-07-07, 2026-08-11, 2026-09-10 and 2026-11-10 articles, body; FCMN 2026 abstracts #030/#053 and #052; Q3 2026 10-Q Note 3; 8-K 2026-11-05 Item 8.01; bruker.com 2026 news index via sitemap). Prior pass also read the Q1-Q3 2026 calls, decks, releases and the Q2 10-Q.
- **Bruker X-ray CD (CD-SAXS / XCD) product, launch date or customer in 2026.** NOT DISCLOSED (read: bruker.com semi product pages and sitemap, 2026-11-21; FCMN 2026 abstract book). The 2026 sitemap and product list contain no XCD page.
- **Bruker X-ray + optical/AFM or ML-based hybrid metrology product.** NOT DISCLOSED (read: same documents). Bruker's "hybrid" usage is XRR+HRXRD (Q001) or AFM+optical (Q009).
- **Release date or specification of "Sirius-FW G2".** NOT DISCLOSED (read: FCMN 2026 abstract #030 p188; Sirius-FW product page; 2026 sitemap).
- **Segment of the "Other" 2026 acquisitions.** NOT DISCLOSED (read: Q3 2026 10-Q Note 3).

## 4. NOT RETRIEVED
- **Bruker SPIE Advanced Lithography + Patterning 2026 event page** (San Jose, Feb 22-26; booth 608). Search snippets list two Bruker exhibitor talks on 25 Feb 2026, "Adaptive critical dimension parameter evaluation in x-ray metrology with machine learning" and "Generative adversarial autoencoder for denoising in x-ray critical dimension metrology". These are leads only.
  - Tried: bruker.com en/es/fr URLs (HTTP 404); WebFetch (404).
  - Tried: Wayback snapshot 2026-02-12 (web.archive.org connection reset by the proxy; not worked around).
  - Tried: SPIE program search by title (no hit).
  - The talks would be [F]/[C] if saved, but they predate 2026-04-20 in any case.
- **Bruker job posting 19572, "Senior Application Engineer, X-ray" (Taiwan).** The search snippet says a Taiwan team is "building out X-ray metrology technology". Tried: icims URL (HTTP 410 Gone). Lead only.
- **Bruker exhibitor pages for 2026 shows: SEMICON West (Oct 13-15, San Francisco), SEMICON Taiwan (Sep 2-4), SEMICON Europa and SEMICON Japan.** Tried: bruker.com sitemaps in five languages (no such pages); WebSearch (no Bruker listing; Rigaku's pages appear instead). Bruker's presence is unconfirmed.
- **ir.bruker.com and sec.gov.** Not attempted (refuse scripts). Mirrors were used instead (kabutan for the 10-Q and 8-K).
- **Firecrawl search.** Credits exhausted. **Consensus.** Quota exhausted, not used.

## 5. SECOND ATTEMPT RESULT per gap
- **Bruker X-ray or hybrid-metrology partnership, launch, investment or acquisition after 2026-04-20.** SECOND ATTEMPT RESULT: added nothing. No such event exists in the sources. Evidence of absence is firmer: the sitemap news index (Q013), the 10-Q acquisitions note (Q010-Q012) and the 8-Ks.
- **Bruker remark on Onto, Rigaku or X-ray competition.** SECOND ATTEMPT RESULT: added nothing.
- **Bruker 2026 statements on its own X-ray plans (CD, imaging, packaging).** SECOND ATTEMPT RESULT: added something.
  - FCMN 2026: XRR+HRXRD "hybrid analysis", Sirius-FW G2, HBM roadmap and sub-10 µm bump plan (Q001-Q005).
  - SemiEngineering Aug-Nov 2026 quotes: new X-ray sources needed for patterned targets; sub-angstrom specs; XRDI at ~20 wph (Q006-Q008).
  - Nothing on X-ray CD or X-ray imaging products.
- **ML-based X-ray CD / hybrid metrology talks by Bruker (SPIE AL 2026).** SECOND ATTEMPT RESULT: added nothing. Titles exist only as search leads; the page was NOT RETRIEVED.
- **Bruker at 2026 SEMICON shows.** SECOND ATTEMPT RESULT: added nothing.
- **Bruker 8-K acquisition items (Apr-Nov 2026).** SECOND ATTEMPT RESULT: added nothing. The mirrored 8-Ks carry only Items 5.02 and 8.01.

## 6. Premise notes
- **"Hybrid metrology" in Bruker's own usage** means XRR+HRXRD joint fitting (X-ray only) or AFM + optical profilometry. It does not mean X-ray combined with optical/AFM, or ML. Onto and Rigaku use the term for optical + X-ray (CD-SAXS + Ai Diffract; see R010).
- **A search summary claimed Bruker agreed to buy Jordan Valley in Dec 2025. That is wrong.** The acquisition closed in 2015 (manifest: 2015-11-02 biospace reprint).

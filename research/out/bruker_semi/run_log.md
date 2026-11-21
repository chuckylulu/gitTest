# Run log - Bruker Corporation (BRKR, Nasdaq), semiconductor metrology only

Session date: 2026-11-21. FY ends December 31. Rules: research/CLAUDE.md.

## Setup decisions
- Rules: on this branch research/CLAUDE.md held only a TODO placeholder. The full rules block (tags, Modules A/B, handoff schema, self-check) existed on branch ccr-2b9561fc-mqqdg4 together with research/tools/ (fetch.py, findpage.py, quote_check.py, merge_parts.py). Both were checked out onto this branch and used unchanged.
- prior/: empty (only .gitkeep). The "Bruker Financial and Segment Performance" chat named in the prompt is not in the repo, so no prior/text/ extraction was possible. Group and segment financials were left out anyway, as instructed. Module A skipped, as instructed.
- Scope: semiconductor metrology business only. Handoff row filled only where a business-unit-level figure exists.

## Reachability check (2026-11-21, honest User-Agent "research-script/1.0")
- 200: bruker.com, rigaku.com, fool.com, d18rn0p25nwr6d.cloudfront.net (Bruker's IR-provider CDN, which hosts copies of its SEC filings)
- 403 (refuses scripts, not worked around): sec.gov (needs a contact User-Agent; the user's email was not used, per the privacy rule), ir.bruker.com, investors.ontoinnovation.com
- Timeout/000: businesswire.com
- SEC_UA not set in the environment, so fetch.py logs every sec.gov URL as NOT RETRIEVED.

## Steps
1. Premise scan by web search (leads only): July 1 2026 segment reorganisation, Q2 and Q3 2026 goodwill impairments, Onto-Rigaku 27% stake announced 2026-04-20 all appear in search results. Verified later against saved files.
2. Four parallel research agents, each writing out/bruker_semi/parts/<prefix>.csv and notes/<prefix>_findings.md:
   S = semiconductor metrology size disclosures, segment mapping, impairments, Bruker reaction since April 2026 (Q2, Q5)
   P = product map (Q1)
   R = Bruker vs Rigaku by tool class, Onto-Rigaku facts (Q3)
   H = hybrid bonding metrology (Q4)

# SPECIAL16 — Forensic checkpoint V3
Date: 2026-10-22

## Candidate universe
Frozen before archive research.
Freeze SHA-256:
4200b4ec8bff98c78b5d8995b6d0db6280200867fb4a24e0b21e4ee41b19fd5e

Internal leader:
2h6vn7o256dtvsfp

No candidate was added after archive results were inspected.

## New closure: official Tor archive

Tor Metrics / CollecTor explicitly states that v2 hidden-service descriptors
(`@type hidden-service-descriptor 1.0`) are NOT formally archived.

Consequence:
official Tor archives cannot retrospectively answer whether one of the 18
candidate v2 services published a descriptor in 2014.

## Best public negative

Dargle / September 2019 Common Crawl onion corpus:
- ~39,838 aggregated onion rows;
- project reports ~40,239 unique onions in the complete pass;
- 32,966 v2 onions reported;
- 0/18 frozen candidates;
- positive Cicada controls in same corpus:
  cu343l33nqaekrnw
  avowyfgl5lkzfj3n
  auqgnxjtvdbll3pv

This is informative but late. It cannot exclude a short-lived 2014 service.

## Best historical discriminator

Gareth Owenson / Nick Savage 2014 HSDir collection:
- six-month Tor hidden-service measurement in 2014;
- approximately 80,000 hidden services observed over study;
- Tor-dev, Nov 2014:
  445,994 v2 hidden-service descriptors;
  approximately 70,000 unique hidden services;
  descriptors stored locally as individual files;
  corpus not released en masse due privacy concerns;
  author explicitly willing to run third-party scripts / publish aggregate results
  and to share for bona-fide research.

This is the best known corpus for the exact question:
"Did any of these 18 exact v2 hostnames exist in 2014?"

A boolean membership check requires no descriptor contents or sensitive data.

## Searchlight Cyber route

Gareth Owenson is now CTO/co-founder of Searchlight Cyber.
Searchlight publicly states that its investigation platform contains more than
15 years of historical dark-web data and continuously archived material from
dark-web sites, forums and marketplaces.

Owenson publicly describes the company as having grown out of the large dark-web
dataset he was collecting as an academic around 2014.

No public Searchlight query interface or ChatGPT connector is available here.

## Next decisive action

Submit a membership-only query:

Frozen hostnames:
- 16 SPECIAL16/G032 variants
- physical-order control
- G054 branch

Positive controls:
- ky2khlqdf7qdznac
- cu343l33nqaekrnw
- avowyfgl5lkzfj3n
- ut3qtzbrvs7dtvzp
- q4utgdi2n4m4uim5
- auqgnxjtvdbll3pv

Question:
For the 2014-era historical Tor-v2/HSDir archive only, does any candidate appear?
If yes, return only hostname plus approximate first/last seen.
No raw descriptor, IP, page content or sensitive record requested.

## Decision rule

HIT on one frozen candidate in a pre-discovery 2014 corpus:
    major external support
    -> recover non-sensitive provenance
    -> locate archived page if possible
    -> hash original page bytes against G073

NO HIT across a high-coverage 2014 HSDir corpus:
    materially weakens Tor-v2 address interpretation
    -> return to internal export order/type hypothesis

## G073
The book explicitly asks for a PAGE in the deep web that hashes to the printed
512-bit value. The digest should therefore be treated as a final validator,
not as the address itself.

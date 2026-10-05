# Geo Legal Researcher

- Symbol: NBIS
- Elapsed: 149.9s

---
I have enough verified material across SEC-adjacent filings, Nebius disclosures, and Reuters/Bloomberg/NYT coverage to write the report. Several follow-up searches (Bloomberg/FT archives) were paywalled or returned low-signal results; I flag those gaps explicitly rather than infer.

---

# NBIS — Nebius Group N.V. (NASDAQ: NBIS)
## Geopolitical, Legal & Regulatory Risk Assessment

**Company snapshot:** Amsterdam-headquartered AI-infrastructure group (AI cloud/GPU clusters; Toloka AI data labeling; TripleTen edtech; Avride autonomous vehicles). Formerly **Yandex N.V.** , rebranded Aug 2024 after completing the $5.4B divestiture of its Russian assets (Reuters, Jul 15 2024). Market cap ≈ $56.5B; 2024 revenue $117.5M (+462% YoY); ~$2.45B year-end 2024 cash; FY2024 net loss $396.9M (4Q/FY2024 release, Nebius, Feb 20 2025). Notified foreign private issuer (CIK 1513845); 20-F on EDGAR is the right filing to mine but returned no machine-readable text here.

---

## 1. Geographic Risk Map

The group does **not disclose a clean revenue-by-country split** (revenue is largely concentrated in the Nebius AI-infrastructure line, whose client roster is described only as "AI-native companies"); the map below triangulates disclosure, datacenter/R&D footprints, and news.

| Country / Region | Role & Exposure Signal | Risk Level | Notes |
|---|---|---|---|
| **Netherlands (HQ)** | Corporate domicile, governance, listing | **Medium** | Dutch regulators/intelligence (AIVD/MIVD) scrutiny of the post-Yandex entity is well documented; status requires disclosure-complete read of 20-F risk factors |
| **United States** | Largest strategic market; GPU benchmark (Hopper/Blackwell) supply; Nasdaq listing; KC (5→40MW) + Vineland NJ (~300MW) sites | **High** | Export-control dependency (EPAs/licensing), US federal/DoD customer due diligence on Russian-origin management, binary political tail risk |
| **Finland** | Legacy Yandex datacenter hub (Mäntsälä) now hosts GPU deployment | **High** | Finnish State Security Board revoked Yandex's license on national-security grounds in 2022 — legacy reputational + national-security permit risk |
| **France (Paris)** | Live H200 GPU cluster | **Medium** | Standard EU/GDPR operating risk; EU Commission scrutiny of Russian-linked assets |
| **Israel** | R&D hub (per disclosure) | **Medium-High** | Security/defence-adjacent talent pool; regional conflict disruptions to personnel/backbone |
| **Russia (legacy)** | Fully divested since Jul 2024 (sale to "Infrastructure Investments" consortium) | **Residual / watch** | No current operational exposure, but the *source* of most counterparty, sanctions, and litigation tail risk; buyer consortium was Russian-based |
| **Latin America** | TripleTen edtech student base (+100% YoY) | **Low-Medium** | Minor revenue; currency/remittance friction |
| **Kuwait/broad GCC, Asia** | Not confirmed in current sources | n/a | Any customer-side exposure must be screened for sanctioned-party risk (see flag 1) |

**Takeaway:** this is effectively a **US-benchmarked, EU-domiciled AI-infrastructure company with a Russian born-in legacy** — risk is geographically concentrated in exactly the two jurisdictions where Russian-origin technology assets face the most intense national-security scrutiny (US export-controls, EU intelligence oversight).

---

## 2. Top 3 Geopolitical Risks

**① Sanctions / Russian-legacy scrutiny re-eruption — Probability: Medium | Impact: Very High**
- Volozh was EU-sanctioned (Jun 2022), sanctions **lifted Mar 2024** (NYT; Reuters Feb 21 2024) after he publicly condemned the invasion and severed Russian control; he **renounced Russian citizenship** in Feb 2026 (Bloomberg, Feb 27 2026).
- Reported (paywalled/incompletely verified this session): US prosecutors were said to be examining whether Volozh/Yandex helped Russian entities evade sanctions in prior years. **Not confirmed in source base here — flag for legal vetting.**
- Watch-item: any OFAC/DOJ/EU action against legacy Yandex structures (or a political shift re-litigating the $5.4B divestment and the 2023-24 government commission approvals) would hit NBIS equity value and US federal revenue instantaneously.

**② US AI-compute export-control regime (GPU supply dependency) — Probability: High | Impact: Very High**
- Nebius's entire product is NVIDIA Hopper/Blackwell compute (Paris H200s; >22,000 Blackwells planned for US+Finland in 2025). The US "AI diffusion rule" (Jan 2025) was **rescinded with replacement rules in flux** (Uptime Institute), keeping GPU allocations a discretionary US-government decision.
- Nebius is simultaneously expanding US capacity with high-profile US partners (NVIDIA-backed; Palantir AI partnership reported Sep 2026) — good optics, but it renders the whole growth plan a **function of continued US licensing goodwill** toward a Russian-founded company.

**③ Dutch national-security / sovereign review of the corporate structure — Probability: Medium | Impact: High**
- Finland already revoked a Yandex datacenter license (2022) on security grounds; Dutch intelligence oversight of the post-divestiture group has been reported across the split. Expect continued bespoke conditions (data-access restrictions, board/governance commitments) with periodic escalations tied to Ukraine-war politics and EU-wide Russian-asset rules.

---

## 3. Legal & Regulatory Highlights

| Item | Status | Implication |
|---|---|---|
| **Yandex Russia divestiture** | Closed Jul 2024, ~$5.4B; shareholder-approved Mar 2024 (Reuters) | Structure required EU/US regulatory sign-off; minority-shareholder friction over pricing/value documented |
| **20-F filing discipline** | FPI on Nasdaq; 20-F on EDGAR (FY2024) | Standard SEC regime; must monitor for Item 21 (foreign government) disclosures and risk-factor updates |
| **Capital-markets activity** | $700M Dec 2024 raise (NVIDIA, Accel, Orbis); reported ~$4.2B follow-on and $5.75B convertible notes in 2025; $250B/5GW plan by 2030 | High leverage-and-dilution scrutiny (press flags "balance-sheet and dilution concerns"); not a legal violation, but a litigation magnet in a downturn |
| **Active litigation** | **No material US/EU cases confirmed in this session's sources** | Honest gap: deeper PACER/court-docket review needed before final sign-off |
| **M&A/regulatory** | Inferize acquisition (Oct 2026); Palantir partnership (Sep 2026) | Standard antitrust/HSR + contract risk; monitor |

---

## 4. Compliance Red Flags

1. **Sanctions/OFAC screening of end-customers** — as a GPU/cloud-services provider, NBIS must demonstrate robust screening of clients (esp. any Russian/China-linked AI firms) for SDN/BIS exposure. Any miss = immediate US/EU enforcement risk given its heightened profile.
2. **BIS export-control compliance** — GPU redistribution/resale and international hosting (Finland/EU clusters serving non-US clients) sits inside a volatile US license regime; compliance program quality will be tested, not assumed.
3. **Toloka data-labeling chain** — human-annotation toil handling sensitive/GenAI training data poses **GDPR + US federal-data** privacy exposure; the sector has previously drawn national-security scrutiny.
4. **Governance optics** — a Russian-born founder-CEO (sanction history, though delisted) managing US-government-adjacent AI compute: expect CFIUS-style and congressional-screener scrutiny of every federal/civilian customer win.
5. **Currency/control residue** — the Russian divestment consideration was partly constrained (Russia hard-currency restrictions at close); any residual treasury exposure to Russian-regulated flows needs verification.

---

## 5. Overall Geopolitical/Legal Risk Rating: **HIGH**

**Rationale:** The trend line is improving — full Russian divestment (2024), EU delisting (2024), renounced Russian citizenship (2026), marquee US partners — and there is **no confirmed active enforcement action** in this session's sources. But the structural facts remain: near-total dependency on discretionary US GPU licensing, a founder with a sanctions history that adversaries will keep litigating, Finnish/Dutch national-security oversight over legacy assets, and a revenue base of only ~$100-500M priced at ~$56B market cap (i.e., almost entirely forward-looking optionality that geopolitical shock can eliminate). **High**, with a credible path to Medium if 2025-27 GPU allocations and US/EU screening all stay clean.

**Confidence notes:** Geographic revenue split and detailed 20-F risk factors could not be machine-read (EDGAR 403; 20-F unavailable via tool). The alleged US prosecutorial inquiry into Volozh remains **reported but unverified here** — treat as a high-priority legal-verification item, not established fact.

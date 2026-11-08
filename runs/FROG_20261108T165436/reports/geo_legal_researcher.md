# Geo Legal Researcher

- Symbol: FROG
- Elapsed: 82.5s

---
# FROG (JFrog Ltd.) — Geopolitical & Legal Risk Assessment
*Prepared from SEC filing metadata, company/Q3-26 disclosures, press, and geopolitical news feeds. As-of late 2026.*

---

## 1. Geographic Risk Map

JFrog is an **Israeli-domiciled** company (JFrog Ltd., Israeli company registry; ISIN IL0011684185, CUSIP M6191J100) with a **Sunnyvale, CA HQ** and Nasdaq listing. Its reported geographic segments are **United States, Israel, India, and Rest of World** (TradingView/Finviz company profiles; 10-Q XBRL tags `country:US`, `country:IL`, `frog:RestOfWorldMember`).

| Geography | Role | Revenue exposure | Risk level | Key driver |
|---|---|---|---|---|
| **United States** | Largest revenue market; HQ; federal/DoD customers | Largest single segment — **>50%** (est.; US is the majority contributor and the FY25 10-K confirms US geographic concentration disclosure). FY2025 total revenue **$531.8M**; Q3-26 **$179.2M (+31% y/y)** | **Low–Medium** | Fed budget/DoD procurement, export controls, software-supply-chain mandates |
| **Israel** | Founding/R&D core; ~1,000 employees at war outset, ~15% reservists | **<5%** revenue but **very high share of R&D headcount** (R&D staff "located primarily in our Israel and India offices" — IPO 424B4) | **High** | Active Iran war / missile risk, reservist mobilization, Israeli tax & grant regime |
| **India** | Second R&D hub; "India kept JFrog running when war hit Israel" (Times of India) | APAC revenue within single digits–low teens (est.) | **Low–Medium** | Execution/data-residency, US-India tariff friction |
| **Europe (in RoW)** | Large enterprise/commercial base; swampUP Europe events | ~20% (est.) | **Medium** | EU CRA, GDPR, nascent EU/UK restrictions *on Israel* |
| **Rest of World** | APAC ex-India, LatAm, Middle East | Balance (~15–20% est.) | **Medium** | EM FX, China/US export-control spillover on tooling |

> **Data gap (declared):** SEC EDGAR direct fetches returned HTTP 403 and the 10-K PDF rendered as binary, so exact FY2025 country-level revenue percentages could not be pulled. Segment names are confirmed; revenue weights above are estimates flagged as such. All dollar figures are filing-sourced.

---

## 2. Top 3 Geopolitical Risks

**① Israel-based R&D disruption from the ongoing Iran war / multi-front conflict — Probability: HIGH | Impact: MEDIUM**
- The Middle East war is live as of Nov 2026: *"Risk of Iran war escalation remains high despite Democratic sweep in U.S. midterm elections… Gulf states still bracing for escalation"* (CNBC, 7 Nov 2026); oil/inflation channel is already moving US macro data (Reuters, 6 Nov 2026).
- JFrog's operating history under fire is documented: it **closed its Tel Aviv office** and managed missile-threat disruption to staff (NBC Bay Area), and its CEO flew back to Israel at the war's outbreak (CTech). At that time JFrog had **~1,000 Israel employees, ~15% called up as reservists**, with India absorbing the load (Times of India).
- Why it matters for the model: R&D is the product. A second mobilization round hits release velocity and gross margin (contractor backfill, wage inflation), not revenue directly.

**② Israeli-domicile legal/tax regime + adverse shift in international posture toward Israel — Probability: MEDIUM | Impact: MEDIUM**
- Sept 2026: **UK, France, Canada and nine other countries** announced trade restrictions tied to West Bank settlements (WSJ; CBS News; JD Supra notes emerging **antiboycott** exposure for companies with Israeli nationals/operations). JFrog has no settlement-linked business, so direct exposure is minimal, but headline/sentiment and procurement-screening risk for European public-sector buyers is real.
- Domestically: **Israel Innovation Authority** grants carry "Commitment to the Israeli Economy" obligations (core R&D must stay in Israel, royalty-bearing know-how transfer restrictions) (Lexology) — a structural constraint on offshoring R&D; the 10-Q XBRL tags confirm `frog:IsraeliInnovationAuthorityMember` grant balances. The **Israel Tax Authority is actively re-pricing Israeli R&D centers** (13% cost-plus rulings in 2026; new R&D incentives law) — a live transfer-pricing audit risk for a company whose Israeli entity is a cost-plus R&D center.

**③ US federal procurement / export-control & supply-chain-security regime — Probability: MEDIUM | Impact: MEDIUM (two-sided)**
- JFrog is listed on the **DoD Enterprise Software Initiative** (JFrog press release) and markets a public-sector/FedRAMP-adjacent offering. That ties a slice of US revenue to federal budget cycles, continuing-resolution risk, and to **encryption/export-control classification** of its software (standard for DevOps/binary management).
- Direction of regulation is a **tailwind**: the **EU Cyber Resilience Act** reaches full application from **11 Sept 2026**, with 24h/72h exploited-vulnerability reporting — JFrog is actively productizing CRA/SBOM compliance (jfrog.com/compliance/cyber-resilience-act). Net: compliance cost now, demand pull later.

---

## 3. Legal & Regulatory Highlights

- **Litigation: no material disclosed proceedings identified.** Targeted searches for securities class actions, DOJ/SEC investigations and IP suits against FROG returned **nothing company-specific** (only generic 2026 securities-litigation market data — Cornerstone/Gibson Dunn). Standard 10-Q Part II Item 1 posture (routine, immaterial) is the reasonable read. *Treat as "no known material litigation," not "confirmed zero."*
- **Regulators of record:** SEC (US domestic filer — 10-K/10-Q/8-K/Form 4 stream is current, latest 10-Q filed 6 Nov 2026); Israel Securities Authority/Companies Law (Israeli incorporation, Israeli tax residency and dividend-withholding rules); Israel Tax Authority (transfer pricing on the R&D center); Israel Innovation Authority (grant covenants).
- **Corporate/structural legal items from Q3-26 10-Q:** $300M buyback authorization ($298.0M remaining); a **business-combination earnout/holdback** with shares reserved for issuance (silent on target — worth a follow-up for IP/consent risk); FX forwards designated as hedges (₪/INR/USD exposure).
- **Segment/product concentration:** single reporting segment; subscription + SaaS mix (SaaS 57% of Q3-26 revenue) — cloud-region/data-residency commitments (EU, FedRAMP boundary) are the operative regulatory obligations.
- **Competitive-legal backdrop:** GitLab called out as direct competition (Seeking Alpha) — patent/IP disputes in DevOps have been a recurring sector theme; no FROG action found.

## 4. Compliance Red Flags

| Area | Assessment |
|---|---|
| **Sanctions (OFAC/EU)** | **Low.** No Russia/Iran-sales exposure disclosed; JFrog is a software vendor to enterprises, not a sanctioned-goods business. Residual risk: end-user screening of Middle East/RoW customers. |
| **FCPA / UK Bribery Act** | **Low.** Low-corruption markets dominate revenue (US, Israel, EU, India); channel/partner model in RoW is the only meaningful touchpoint. |
| **Antiboycott (US Commerce Dept.)** | **Watch item.** US antiboycott rules apply directly to a company with Israeli operations, and 2026 European measures create conflicting-compliance friction (JD Supra, Sept 2026). |
| **Data privacy (GDPR/CCPA)** | **Medium.** Global SaaS + AI agents/model artifacts (AI-SEC launch, Oct 2026) raise DPA/data-residency and customer-data-in-model questions. |
| **Export controls (encryption)** | **Medium.** Binary repository/DevOps software has encryption functionality; EAR classification and deemed-export rules for Israeli/Indian engineers matter. |
| **Israel IIA grant covenants** | **Low–Medium.** Royalty/economic-commitment conditions constrain R&D relocation — a contractual-compliance item, not a scandal risk. |
| **Insider/Form 4 cadence** | Heavy but routine Form 4 flow (Sep–Oct 2026); no anomalous 8-K disclosures beyond earnings. |

**No red flag rises to investigative/enforcement grade.** The honest characterization: a clean legal file with structural jurisdictional complexity.

---

## 5. Overall Geopolitical/Legal Risk Rating: **MEDIUM**

**Rationale:** Revenue is overwhelmingly earned in low-risk jurisdictions (US-majority, EU, India) and there is **no known material litigation, investigation, or sanctions exposure** — that alone caps the legal dimension at Low. The rating is pulled to Medium by a single concentrated, non-diversifiable factor: **the company's core R&D is physically in Israel during an active Iran war with elevated re-escalation probability (CNBC, Nov 2026), alongside a tightening Israeli tax/grant regime and newly emergent European restrictions on Israeli-linked entities.** Two-sided regulatory tailwinds (EU CRA, US software supply-chain attestation) partially offset.

**Monitoring triggers that would move this to HIGH:** (1) renewed mass reservist call-ups or physical damage to Israeli/Indian delivery capacity; (2) EU/UK procurement exclusions extending from settlements to Israeli-incorporated vendors; (3) an Israel Tax Authority transfer-pricing assessment against the R&D subsidiary; (4) any securities or IP litigation filing.

**Sources:** SEC EDGAR filing metadata and 10-Q (filed 6 Nov 2026; FY25 10-K `frog-20251231.htm`); JFrog Q3-26 results (Business Wire, 5 Nov 2026); TradingView/Finviz segment profiles; NBC Bay Area, CTech, Times of India (Israel operations/reservists); CNBC 7 Nov 2026 and Reuters 6 Nov 2026 (Iran war escalation); WSJ/CBS News/JD Supra (Sept 2026 European trade measures, antiboycott); Lexology, EY, Tax-at-Hand (IIA grants, 2026 ITA transfer-pricing rulings); jfrog.com CRA compliance page; JFrog DoD ESI announcement.

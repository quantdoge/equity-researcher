# Geo Legal Researcher

- Symbol: FROG
- Elapsed: 65.1s

---
# FROG (JFrog Ltd.) — Geopolitical & Legal Risk Assessment
*Prepared for the investment memo. Pricing/market data: $114.38, ~$13.9bn cap (tool snapshot). Filings referenced: FY2025 Form 10-K (filed 2026, accession 0001193125-26-051382), Q3 2026 Form 10-Q (filed 2026-11-06, accession 0001193125-26-451981).*

## 1. Geographic Risk Map

**Corporate structure note:** JFrog is an **Israeli-incorporated** company (ISIN IL0011684185, CIK 1800667) with operational HQ in Sunnyvale, CA. Investors own shares in an Israeli legal entity, not a Delaware corporation — Israeli Companies Law governs shareholder rights, takeovers, and dividend mechanics.

| Geography | Revenue exposure | Operational exposure | Risk level |
|---|---|---|---|
| **United States** | ~60–64% (est.; largest single market; US was ~64% in FY2020 10-K, ~36% of revenue non-US) | ~400 employees (FY2025 10-K); HQ, go-to-market, federal/public-sector business | **Low–Medium** (federal procurement, CRA/FedRAMP-adjacent compliance, tariffs immaterial for SaaS) |
| **Israel** | Disclosed as a separate geographic revenue line (XBRL: `country:IL`, `GeographicConcentrationRisk`), est. low-to-mid single-digit % of revenue | **~950 of ~1,800 employees (~53%)** located in Israel (FY2025 10-K) — core R&D and engineering | **High** |
| **India** | Not separately disclosed; part of "Rest of World" | ~400–450 staff by implication (1,800 total less Israel/US); documented as the business-continuity site during the Israel war | **Medium** (data-localisation, DPDP Act, wage inflation) |
| **Europe / RoW** | Rest of World is a disclosed segment (`frog:RestOfWorldMember`); Europe is the largest non-US commercial region | Sales/support offices; EU regulatory exposure (GDPR, Cyber Resilience Act) | **Medium** |
| **Russia / Belarus / Iran / Syria** | Immaterial or nil | No disclosed operations | **Low (subject to sanctions screening)** |

**Caveat:** the exact FY2026 US/Israel/RoW revenue percentages could not be extracted — SEC.gov returned HTTP 403 on direct document fetches and the IR-hosted 10-Q PDF did not render as text. The 60/40 US/international split is derived from the last fully extracted disclosure (FY2020 10-K: "approximately 36% of our revenue was generated from customers outside of the United States") and should be refreshed from the geographic note in the FY2026 10-K.

## 2. Top 3 Geopolitical Risks

**Risk 1 — Israel-based workforce concentration in an active multi-front war (Probability: continuing/high; Impact: medium-high)**
- ~53% of employees sit in Israel, and the CEO has disclosed that **~1,000 Israeli staff were affected and "around 15% of them were called by the army to be reservists"**, with the Tel Aviv office closed during missile attacks (Times of India; NBC Bay Area).
- The conflict is now in its fourth year; the IDF is recalling discharged reservists amid a **manpower crisis** (Jerusalem Post, 2026) and reservists report stalled careers and financial strain after three years of war (Times of Israel; Calcalist). This is a persistent productivity/attrition tax on R&D, not a one-off.
- Mitigant: management has explicitly institutionalised India as the failover engineering site ("India kept JFrog running when war hit Israel"). This materially caps the tail risk, but the two-site model still concentrates IP creation in one conflict zone.
- Escalation tail: 2026 reporting references an ongoing **U.S.–Iran war** and regional shipping/supply disruption (Bloomberg, WSJ, Nov 2026), which raises the probability of renewed direct strikes on Israeli infrastructure.

**Risk 2 — Western sanctions and trade measures now being applied to Israel itself (Probability: high and rising; Impact: low-medium but underappreciated)**
- This is a genuinely new vector versus the 2023–24 period: **94 active sanctions/restriction measures against Israel** across 63 countries (Algemeiner, Oct 2026); **twelve Western countries** announced coordinated measures on settlement trade including new UK regulations (Steptoe Sanctions Update, Sept 2026; Guardian, 17 Nov 2026); the **EU has proposed suspending trade benefits covering 37% of Israeli exports** and sanctioning Israeli ministers (Courthouse News).
- JFrog is a software/services exporter, not a settlement-goods exporter, so direct legal exposure is negligible. The transmission channel is **procurement and reputational**: EU/public-sector and university customers adopting vendor-origin restrictions or ESG exclusion screens, plus possible "Made in Israel" optics in RFPs. Given JFrog's push into EU public sector (it markets CRA compliance and FedRAMP-adjacent capabilities), this deserves monitoring.
- Also note the domestic side: proposed changes to Israel's judicial/legal framework have been flagged in JFrog's own risk disclosure ("proposed changes to Israel's…" — Q3 2025 10-Q), a rule-of-law/business-environment signal.

**Risk 3 — Export controls, tariffs, and US–China decoupling on a software supply-chain product (Probability: medium; Impact: medium)**
- JFrog's platform is US-origin technology subject to EAR, sold globally through channel partners and cloud marketplaces (AWS/Azure/GCP). Encryption functionality and enterprise/defense customers create dual-use classification and end-user screening obligations. Channel/reseller intermediation is the classic failure point for deemed-export and sanctioned-party violations.
- 2026 tariff and export-control churn (sweeping Russia/Belarus measures, expanded Iran oil/entity designations, third-country secondary sanctions — Treasury/OFAC, Fenwick, BIS) raises compliance cost and slows deal cycles in Middle East/Asia channels. Direct tariff exposure is minimal for pure SaaS, but hybrid/self-managed deployments with hardware touchpoints carry some.
- Model risk: any customer-mix shift away from US federal/defense or regulated EMEA accounts would show up first in cloud consumption growth (Q3 2026 cloud revenue $101.5M, +60% y/y — the growth engine most exposed to procurement politics).

## 3. Legal & Regulatory Highlights

**Securities litigation (active, unresolved).** Following Q2 2024 results (7 Aug 2024) — when FY2024 guidance was cut on expected cloud-revenue growth — FROG shares fell **$9.37, or 27.5%, to $34.05**. Multiple plaintiff firms have solicited and investigated claims on behalf of purchasers (Pomerantz, Levi & Korsinsky, Howard G. Smith, BG&G, ZLK), and **Portnoy Law Firm was still publicly investigating as of March 2026** (GlobeNewswire). No material litigation accrual or quantified contingency is visible in the Q3 2026 balance sheet (cash $75.2M + short-term investments $805.7M), and the 10-K cross-references "Legal Proceedings" to a financial-statement note rather than a standalone item. **Assessment:** nuisance-to-modest stock-drop exposure in the low single-digit millions; the real risk is discovery-driven disclosure, not the settlement.

**Israeli Innovation Authority (IIA) grants.** JFrog received IIA grants (2009–2015) carrying **royalty obligations and restrictions on transferring know-how or manufacturing/IP outside Israel** without approval. This is a genuine structural constraint: it limits the company's ability to shift R&D out of Israel (including to India or the US) in a crisis, and any future offshoring or M&A-driven IP migration requires IIA consent and possible repayment. This is the single most underappreciated legal-geopolitical coupling in the file.

**Israeli corporate law.** As an Israeli company, JFrog is subject to Israeli Companies Law (board/AGM mechanics, dividend distribution tests, Israeli withholding tax on distributions), not DGCL. This affects activist tactics, buyback/dividend flexibility (buyback authorisation: $300M programme, $298.0M remaining at 30 Sep 2026), and index/eligibility treatment.

**Regulatory tailwind/obligation — EU Cyber Resilience Act (Reg. 2024/2847).** JFrog markets CRA compliance (SBOM generation, vulnerability tracking, release evidence) as a product driver, and is simultaneously itself a "product with digital elements" manufacturer subject to CRA obligations. Regulatory reporting duties phase in from 2026 and full obligations from Dec 2027 — a net demand tailwind for the platform but a new compliance cost line.

**Other.** No FCPA/OFAC/BIS enforcement action, no DOJ/SEC investigation, and no IP litigation of consequence disclosed. Peer context: GitLab's FY26 10-K flags securities class actions as an industry-standard risk — JFrog's profile is comparable, not anomalous.

## 4. Compliance Red Flags

| Flag | Severity | Comment |
|---|---|---|
| IIA grant covenants constraining IP offshoring | **Amber** | Structural; needs IIA approval to relocate R&D out of Israel in a conflict escalation |
| Channel/reseller sanctions & deemed-export screening | **Amber** | Global marketplace + partner sales of encryption-capable US-origin software; no disclosed incident |
| Workforce concentration in a war zone (business-continuity / duty-of-care disclosure) | **Amber** | 53% of staff; 15% reservist call-up rate disclosed |
| Emerging anti-Israel procurement/exclusion measures in EU/UK | **Amber (new)** | Reputational and public-sector RFP risk; monitor EU trade-perk suspension outcome |
| Stock-drop securities claims (2024–2026) | **Yellow** | Solicitation-stage; immaterial reserve |
| Data privacy (GDPR, India DPDP, US state laws) across a multi-tenant SaaS platform | **Yellow** | Standard SaaS exposure; no disclosed breach |
| FCPA/AML | **Green** | No disclosed issues; low-risk sector/geography mix |

## 5. Overall Geopolitical/Legal Risk Rating: **MEDIUM-HIGH**
(On the four-point scale: **High on geopolitical-operational**, **Medium on legal/regulatory**.)

**Rationale:** Revenue is anchored in the US and Europe — the sanctions and conflict exposure does not run through the customer base, which is why this is not "Very High." But the *production function* is concentrated: more than half of employees and most core R&D sit in a country that in 2026 is fighting on multiple fronts, facing an active U.S.–Iran war in its neighbourhood, and — for the first time — absorbing coordinated Western trade and sanctions measures. JFrog has demonstrated real resilience (India failover, cloud revenue +60% y/y through the war years), and near-term legal liabilities look immaterial. The risks that matter for the thesis are (a) a multi-quarter R&D velocity hit from reservist call-ups in an escalation, (b) IIA covenants blocking any rapid IP/workforce relocation, and (c) EU public-sector procurement friction. None of these is currently priced; all three are monitorable.

**Monitoring triggers:** EU vote on suspending Israel trade benefits; expansion of UK/EU entity-level sanctions beyond settlement goods; renewed direct Iran–Israel exchange; changes to Israeli reserve call-up policy; docket activity in the 2024 securities suits; any IIA consent request tied to R&D relocation.

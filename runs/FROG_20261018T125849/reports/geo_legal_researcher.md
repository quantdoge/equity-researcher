# Geo Legal Researcher

- Symbol: FROG
- Elapsed: 287.0s

---
## FROG (JFrog Ltd.) — Geopolitical & Legal Risk Assessment

**Critical structural fact:** JFrog is not a US company. It is **incorporated in the State of Israel** (IRS EIN 98-0680649) with US headquarters at 270 E. Caribbean Drive, Sunnyvale, CA. Source: [FY2025 Form 10-K, filed 13-Feb-2026](https://www.sec.gov/Archives/edgar/data/1800667/000119312526051382/frog-20251231.htm). This dual identity — Israeli legal domicile, American revenue base — is the central axis of the risk profile.

---

### 1. Geographic Risk Map

Segment disclosure is by **United States, Israel, India, and Rest of World** (per [Forbes company profile](https://www.forbes.com/companies/jfrog/)).

| Geography | Rev. exposure | Operational exposure | Risk level | Key driver |
|---|---|---|---|---|
| **United States** | Largest single market (~est. 45–50%) | HQ, go-to-market, JFrog Inc. subsidiary | **Low** | Federal/defence procurement exposure, export-control reach |
| **Israel** | ~est. 8–12% | **~800 of ~1,600 employees; core R&D, long-lived assets** | **High** | Active multi-front conflict, reserve duty, Iranian missile/Houthis threat |
| **Europe (RoW)** | ~est. 30–40% | Sales + EU cloud regions | **Medium** | EU CRA/DORA compliance burden (offset: demand tailwind) |
| **India** | ~est. 3–5% | Large engineering/support headcount | **Low-Med** | Data localisation, US-India trade friction |
| **China / Russia** | Immaterial (post-2022 Russia exit) | Minimal | **Low** | Sanctions screening remains a live obligation |

**Gap disclosure:** exact country-level percentages were not machine-readable in this session (SEC HTML blocks direct fetch; the FY2025 10-K Note 3 "Revenue by geographical region" table was not extracted). Ranges above are estimates triangulated from the segment structure and historical disclosures — **treat as directional, not audited.** The structural asymmetry is nonetheless certain: **Israel is a minority of revenue but a majority of the operating substance**, so its risk transmits through the P&L, not the revenue line.

FY2025 context: revenue $531.8M (+24%), FY2026 guide $623–628M, cloud 48% of Q4 revenue, RPO $565.7M, cash+investments $704.4M, goodwill $371.5M (M&A-driven). Source: [Q4/FY2025 release, 12-Feb-2026](https://investors.jfrog.com/news/news-details/2026/JFrog-Announces-Fourth-Quarter-and-Fiscal-2025-Results/default.aspx).

---

### 2. Top 3 Geopolitical Risks

**① Israeli operational concentration under active, multi-front war — Probability: High / Impact: Medium-High**
The FY2025 10-K explicitly flags "geopolitical tensions, such as the imposition of tariffs… or **regional conflicts**" and shareholder rights "governed by Israeli law." As of mid-October 2026 the region remains hot: Iranian attacks on Strait of Hormuz shipping and Houthi strikes on Saudi Arabia are actively disrupting supply chains and feeding inflation ([Fox Business, 15-Oct-2026](https://www.youtube.com/watch?v=XvYpjLo89us); [Reuters, 16-Oct-2026](https://www.reuters.com/business/us-manufacturing-output-rises-september-2026-10-16/)). Roughly half the workforce is in Israel and subject to reserve call-ups — historically the single most cited operational risk for Israeli-domiciled software issuers. Mitigants: cloud-delivered (48%+ of revenue) rather than on-prem deployment, distributed R&D in India, and demonstrated sector resilience (Israeli high-tech output +8.2% real in 2025 per the Israel Innovation Authority's 2026 report; tech employment >600k in Q1 2026, +7%). Counter-risk: reported **brain drain** of Israeli tech talent amid war strain and AI disruption ([i24NEWS, 2026](https://www.i24news.tv/en/news/innov-nation/artc-israeli-high-tech-faces-mounting-brain-drain-amid-ai-disruption-and-war-strain)) — a slow-burn threat to JFrog's R&D moat.

**② Trade fragmentation, export controls and sanctions — Probability: Medium / Impact: Medium**
The 10-K carries explicit risk-factor language: "We are subject to various governmental export controls, trade sanctions, and import laws and regulations that could **impair our ability to compete**…" (FY2025 10-K). Two channels matter: (a) Artifactory embeds cryptography, triggering EAR/encryption export authorisation obligations and deemed-export rules for foreign-national engineers — heightened when staff sit in Israel and India; (b) customer-side screening, as JFrog's 6,600 customers include defence, government and Fortune 100 accounts that push their own restricted-party obligations down the supply chain. China's expanding dual-use export-control retaliation ([Reuters, 24-Jul-2026](https://www.reuters.com/business/aerospace-defense/china-adds-14-eu-entities-export-control-list-over-russia-related-sanctions-2026-07-24/)) widens this surface.

**③ Israeli domicile: shareholder-rights, index-mandate and tax-incentive risk — Probability: Medium / Impact: Low-Medium**
Israeli corporate law (dividend/distribution rules, minority protections, director duties) differs from Delaware norms, and the 10-K flags this directly. Secondary channels: BDS/ESG-driven exclusion screens at sovereign and pension funds (a persistent, low-grade ownership constraint for Israeli-incorporated issuers), limited Gulf-market contracting ability because some regional buyers will not contract with Israeli entities, and dependency on Israeli tax incentive regimes whose amendment would hit the effective tax rate. None of these is acute; all are structural.

---

### 3. Legal & Regulatory Highlights

- **Litigation:** The FY2025 10-K contains an **Item 3. Legal Proceedings** section (p.53) and a forward-looking caveat on "our ability to successfully defend litigation brought against us." I found **no securities class action, patent suit, or government investigation** against FROG in this session's searches (the searches returned generic securities-litigation commentary, not FROG-specific matters). Absence of evidence is not clean confirmation — Item 3 content was not extracted.
- **Regulatory posture is net *favourable*, unusually so.** JFrog sells the compliance solution, not the problem: the **EU Cyber Resilience Act** (in force Dec-2024, with **mandatory 24-hour vulnerability reporting from 11-Sept-2026**) is a direct demand driver for SBOM/artifact governance, and JFrog is actively marketing CRA compliance tooling ([JFrog CRA compliance brief](https://jfrog.com/solution-sheet/cyber-resilience-act-jfrog-platform-compliance-brief/)). Same dynamic for DORA (EU financial services), US federal software-supply-chain/SBOM requirements, and the SEC cyber-disclosure regime.
- **Public sector:** management guides to "our ability to expand usage of our platform in the **government and commercial sectors**" (FY2025 release). Federal traction raises FedRAMP/StateRAMP and ITAR-adjacent obligations — I could **not verify JFrog's FedRAMP authorisation status** (search returned no relevant results). Flag as a diligence item.
- **IP / open source:** Artifactory's core function is storing, curating and distributing third-party open-source packages. That creates a structural OSS-licence-compliance and **software-supply-chain liability** surface — if a compromised package propagates through JFrog infrastructure, the tail risk is contractual indemnity plus reputational damage, not a statutory fine.
- **Privacy/data protection:** GDPR, UK GDPR, CCPA plus cloud-region data-residency commitments across AWS/Azure/GCP.

---

### 4. Compliance Red Flags

**No confirmed violations, investigations, or sanctions breaches identified.** Monitoring items:
1. **Deemed-export controls** on cryptography-adjacent products with Israel- and India-based engineering staff — the highest-probability technical breach vector for this business model.
2. **Customer-induced sanctions risk** — defence/government accounts and any residual restricted-market end users; JFrog's 2022 Russia exit should be re-verified in the FY2025 10-K for completeness of wind-down.
3. **Israeli Innovation Authority royalty obligations** — if JFrog has received IIA grants, a contingent royalty liability exists (not verified this session).
4. **Supply-chain liability** as the CRA's 24-hour reporting clock starts (Sept-2026): any JFrog-mediated malicious-package incident becomes a regulated event in the EU.

---

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

**Rationale:** Revenue is geographically diversified across the US and Europe with no single-jurisdiction revenue concentration, the balance sheet is fortress-like ($704M cash/investments, no debt signals), and the regulatory environment is a tailwind rather than a threat. The offsetting factors are real but bounded: **~50% of human capital and the bulk of R&D sit in Israel during an active multi-front conflict**, and the Israeli incorporation introduces governance, tax and mandate-exclusion frictions that do not apply to Delaware peers. Escalation of the Iran/Houthis front — currently live, per October 2026 reporting — is the single scenario that would move this rating to High; it would compress R&D velocity and could impair cloud-region resilience, with revenue impact lagging headcount impact by several quarters.

**Diligence gaps to close:** (1) FY2025 10-K Note 3 country-level revenue table; (2) Item 3 Legal Proceedings full text; (3) FedRAMP/IL5 authorisation status; (4) IIA grant exposure and Israeli tax-incentive dependency in the effective tax rate.

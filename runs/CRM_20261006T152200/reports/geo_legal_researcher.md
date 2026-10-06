# Geo Legal Researcher

- Symbol: CRM
- Elapsed: 528.4s

---
I have enough to compile the assessment. Note: the 10-K risk-factor feed returned no data for CRM, and two litigation searches timed out — I've flagged those gaps explicitly rather than fabricating specifics.

---

# Salesforce, Inc. (CRM) — Geopolitical & Legal Risk Assessment
*Date of analysis: Oct 2026 | Data: FY2024 annual report (fiscal year ended Jan 31, 2024) + FY2026 quarterly disclosures*

## 1. Geographic Risk Map

| Country / Region | Revenue Exposure | Risk Level | Notes |
|---|---|---|---|
| **United States** (within Americas) | ~55-60% of total (Americas = $23.3B, 66.8%) | **Low** | Domicile; HQ San Francisco; largest stable base. Federal/state government vertical growing (Agentforce for Public Sector), which cuts both ways (see §3). |
| **Americas ex-US** (Canada, LATAM incl. Brazil) | ~7-12% (within Americas bloc) | **Low–Moderate** | Brazil/Argentina FX and political volatility; Brazil LGPD privacy regime. |
| **EMEA / Europe** | $8.1B, **23.3%** | **Moderate** | Highest regulatory density: GDPR, EU AI Act, Data Act. Macro stress: French debt worries, weak EUR (USD at 17-month high vs EUR → FX drag: EMEA grew +7% reported vs +9% constant currency in Q3 FY26). |
| **Asia Pacific** | $3.4B, **9.9%** | **Moderate** | Japan, Australia, India are high rule-of-law but privacy-law churn (Japan APPI, Australia reform, India DPDP Act 2023). China exposure via Alibaba Cloud only (see §2). |
| **China / Greater China** | <1% (implicit in APAC) | **High** | No direct operations — exclusive delivery through Alibaba Cloud partnership (mainland China/HK/Macau/Taiwan). Single-point geopolitical dependency. |
| **Russia** | ~0% | **Low** | Operations suspended since 2022 (leave-russia.org / Yale tracker); residual sanctions-compliance cleansing risk only. |

*Sources: Increv (citing Salesforce annual report) for the 67/23/10 split; FQ3 FY25 & FQ3 FY26 earnings releases (barchart, s205.q4cdn.com) for regional growth and constant-currency FX drag; frontier-enterprise.com for Alibaba exclusivity in Greater China.*

## 2. Top 3 Geopolitical Risks

**1. US–China tech decoupling → disruption of the Alibaba Cloud-delivered China business**
- Probability: **Medium–High** | Impact: **Low–Moderate** (China is ~1% of revenue)
- Gartner's "First Take: Alibaba Ban Traps Salesforce China Customers" flags platform-continuity, compliance and data-sovereignty risk for multinationals using Salesforce on Alibaba Cloud. US policymakers are reported to be weighing broad software-export curbs on Chinese activity — new licensing regimes would hit exactly this partnership. Salesforce's China strategy is outsourced to a counterparty that is itself a sanctions/export-control target; the strategic option (exit) was already exercised once in 2022.

**2. EU regulatory stack on the 23%-of-revenue EMEA region (GDPR + EU AI Act + macro)**
- Probability: **High** | Impact: **Moderate**
- GDPR: Salesforce sits on both sides — controller for its own data and processor for ~150K customers in regulated industries (financial services, healthcare). The EDPB has launched a fifth coordinated enforcement action (Oct 2025) focused on transparency. The EU–US Data Privacy Framework (which Salesforce relies on for transfers) has already survived one CJEU challenge but remains structurally vulnerable.
- EU AI Act: Agentforce/Einstein (AI agents) and partnerships with OpenAI (±Claudeforce, Gemini Enterprise) draw the full transparency/GPAI-model chain into scope. Compliance cost and product-design constraints, not penalties, are the primary near-term impact.
- Macro overlay: French debt concerns and EUR weakness are pressuring reported EMEA revenue (FX drag already visible in Q3 FY26).

**3. US federal & national-security market: political-budget risk at home**
- Probability: **Medium** | Impact: **Moderate**
- Salesforce is pushing aggressively into government: Agentforce for Public Sector, and "Missionforce National Security — IL5-authorized AI agents" for defense/intelligence (Aug 2026). This growth vector carries three tail risks: (a) DOGE-style federal spending cuts / procurement reviews on ~$793B of FY2025 federal obligations; (b) elevated export-control, dual-use and classified-environment compliance burden (ITAR/FedRAMP IL5); (c) politicization of AI-in-government contracting. Geopolitical escalation (Iran/Strait of Hormuz standoff, G7 reserve releases) adds macro volatility (energy costs, currency) but minimal direct exposure.

## 3. Legal & Regulatory Highlights

- **AI regulation (US states)**: Salesforce is a "deployer/developer" under the **Colorado AI Act** (effective June 1, 2026, high-risk consequential decisions) and California AI transparency rules — new compliance obligations for Agentforce customers and Salesforce itself.
- **EU AI Act**: In-scope as AI deployer/system provider; agentic AI (Agentforce) is the regulatory focal point; underlying-model ties to OpenAI/Anthropic/Google invoke GPAI model obligations up the chain.
- **GDPR / EDPB**: No headline GDPR fine against Salesforce was identified in the reviewed window (recent fines observed went to Uber, OpenAI, Meta, Intesa — not Salesforce). Watch item: EDPB coordinated enforcement on transparency (Oct 2025) and DPF longevity.
- **23andMe-breach litigation**: Salesforce was a data processor for 23andMe, whose October 2023 genetic-data breach (and 2025 Chapter 11) generated consumer class actions. **Verification gap:** two targeted searches for Salesforce's named-defendant status timed out; treat as a litigation watch item pending confirmation. No other material public lawsuit, DOJ/SEC/FTC investigation, or FCPA enforcement against Salesforce was identified.
- **Antitrust**: Salesforce is historically the *complainant* (Slack vs. Microsoft Teams bundling before the EU), not a target. No material competition-law exposure identified.
- **No material Russia/Cuba/etc. sanctions exposure**; Russia ops suspended since 2022.

## 4. Compliance Red Flags

- **China cross-border data rules**: China-hosted operations via Alibaba Cloud implicate PIPL/DSL cross-border transfer and data-sovereignty requirements; any further US export controls on software or Alibaba Cloud could strand that delivery model (Gartner).
- **Federal/defense build-out**: IL5-authorized AI for national security raises export-control classification and supply-chain vetting risk — a compliance surface that barely existed pre-2025.
- **Partner/reseller channel** across emerging markets (standard FCPA/AML exposure); no enforcement history found, but the 150K-customer base with regulated-sector data (healthcare, financial services) raises third-party data-privacy liability through processors.
- **Constant-currency gap** in EMEA/APAC (reported vs. CC growth differing by ~2-3pp) flags FX/currency-control sensitivity in weaker-currency markets.

## 5. Overall Geopolitical/Legal Risk Rating: **MEDIUM**

**Rationale:** The revenue base is exceptionally well-diversified across high rule-of-law jurisdictions (US ~67%, EU ~23%, developed APAC ~10%), Russia exposure is zero, and there is no material public litigation or regulatory enforcement. The rating is held at Medium — not Low — by four structural factors: (1) the EU AI Act/GDPR stack on nearly a quarter of revenue; (2) the Alibaba-clouded China model as a concentrated US-China decoupling dependency; (3) growing federal/defense concentration at a time of politically driven budget volatility; and (4) rising US state AI regulation colliding with an agentic-AI product roadmap.

**Key gaps in this analysis:** (a) primary-source 10-K risk-factor text was unavailable via the filing feed — geographic figures are from the annual report as republished by Increv and earnings releases; (b) verification of Salesforce's named-defendant status in 23andMe-related class actions could not be completed (repeated search timeouts); (c) the 10-K's own litigation-contingency disclosures should be pulled from the March 2026 filing before final investment-memo sign-off.

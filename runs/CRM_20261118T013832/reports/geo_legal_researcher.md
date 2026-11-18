# Geo Legal Researcher

- Symbol: CRM
- Elapsed: 37.4s

---
## Salesforce, Inc. (CRM) — Geopolitical & Legal Risk Assessment

**Snapshot:** $41.5B FY26 revenue (FYE 31-Jan-2026), ~83,300 employees, HQ San Francisco. Sector: Technology / Software-Application. Market cap ~$160B. *(Company profile; Salesforce FY26 Q4 release)*

---

### 1. Geographic Risk Map

FY26 geographic split (FY26 revenue $41.5B) — **Americas $27.19B / Europe $10.02B / APAC $4.32B**. US is ~93% of Americas, i.e. roughly **$25.3B or ~61% of consolidated revenue**. *(Bullfincher, sourced to FY26 10-K; SEC 10-Q crm-20260731 confirms "Americas revenue attributed to the United States was approximately 93 percent")*

| Country/Region | Rev. exposure | FY26 growth | Risk level | Key risk drivers |
|---|---|---|---|---|
| **United States** | ~61% | ~8% | **Low (political) / Medium (legal)** | State privacy patchwork (CCPA/CPRA, CIPA), AI regulation, federal procurement volatility, securities/class-action venue |
| **Europe (EU/UK/EEA)** | 24.1% | ~13% | **Low–Medium** | GDPR enforcement, EU AI Act Art. 50 live since 2-Aug-2026, DSA/data-transfer friction, slower EU growth politics |
| **Japan / Australia / Canada** | within APAC/Americas | ~10–12% | **Low** | Rule of law strong; Japan is the anchor APAC market |
| **Asia ex-Japan (India, SE Asia)** | within APAC 10.4% | ~12% | **Medium** | Data-localisation (India DPDP), currency/convertibility, sales-execution risk |
| **China / Russia** | Negligible/indirect | n/a | **Low but opaque** | No disclosed China data-centre footprint; Russia wind-down; sanctions/export-control screening of partners. *(No material exposure disclosed; not quantified in filings)* |

**Observation:** Europe is the *fastest-growing* major region (+12.7% y/y vs Americas +8%) and is now nearly a quarter of revenue — meaning EU regulatory risk is rising in *revenue-weighted* terms, not falling.

---

### 2. Top 3 Geopolitical / Regulatory Risks

**Risk 1 — Privacy & AI regulatory cascade in the US and EU (Probability: High / Impact: Medium)**
The US privacy-litigation regime has become industrialised: 1,800+ data-privacy class actions filed in 2025 (>150/month), $53.8B of class/enforcement settlements in H1-2026 alone, and a 67% class-certification success rate in privacy cases in 2025. California's CIPA wiretapping wave has produced 4,700+ suits since 2022 at $5,000/violation statutory damages — a direct exposure for Salesforce's Marketing Cloud / Data Cloud tracking-pixel and session-replay surfaces. California AG set a record CCPA penalty in May 2026 (GM, $12.75M). In the EU, **EU AI Act Article 50 transparency duties began applying 2-Aug-2026**; Annex III high-risk obligations were deferred to **2-Dec-2027** under the Digital Omnibus — a delay that reduces near-term cliff risk for Agentforce but not the eventual compliance cost. *(JD Supra/Captain Compliance privacy litigation review, Oct-2026; Salesforce EU AI Act pages; cloudcompliance.app)*

**Risk 2 — 2025 customer data-breach litigation wave (Probability: High that liabilities persist / Impact: Medium-High)**
*In re Salesforce, Inc., Customer Data Security Breach Litigation* — **MDL No. 3164** (and 3170), consolidated in N.D. Cal. by JPML transfer order in Dec-2025 — covers a series of breaches of Salesforce *customers'* org data through 2025, including the Salesloft/Drift OAuth-token theft campaign (UNC6395) that hit Google, Workday and others. Crucially, on **17-Sep-2026 a San Francisco federal judge largely denied Salesforce's motion to dismiss**, sustaining negligence and related claims over its security posture. That materially raises settlement value and discovery exposure. Countervailing: at least one plaintiff (M.K.) voluntarily dismissed her claim, per the Q2-FY27 10-Q. *(Law360; Bloomberg Law; JPML transfer order; CyberNow/Bloomberg)* Note the second-order risk: **reputational and contractual** — enterprise customers increasingly write security warranties and indemnities into renewals.

**Risk 3 — Reliability/security-driven sector repricing and AI-misuse liability (Probability: Medium / Impact: Medium)**
On **17-Nov-2026 CRM fell 9.45% to $194.52** — its worst single day since May-2024 — as a series of high-profile technology outages led investors to conclude software companies may be "particularly vulnerable" to AI misuse. This is a market-structure risk rather than a country risk, but it is the clearest live transmission channel from operational/legal events into valuation. *(MarketWatch; Invezz; Zacks)*

---

### 3. Legal & Regulatory Highlights

- **Active MDL (material):** MDL 3164/3170, N.D. Cal. — MTD largely denied Sep-2026. Largest single disclosed litigation overhang.
- **AI copyright class action:** filed **15-Oct-2025** by Saveri Law Firm on behalf of authors holding registered copyrights, alleging Salesforce trained LLMs on their works. Tracks the broader 2026 AI-copyright docket (Bartz v. Anthropic; fair-use split on training vs. pirated storage). *(Saveri Law Firm case page; Norton Rose Fulbright AI litigation update 2026)*
- **Routine matters:** 10-Q/10-K Note 12/14 "Legal Proceedings and Claims" describes ordinary-course claims; the company characterises these as not material individually. The 10-K was not retrievable via the filing tool (403 on SEC direct fetch) — **gap noted**; figures above are from the 10-Q, the FY26 annual report reference, and secondary reporting.
- **Antitrust:** **No Salesforce-specific antitrust investigation or charge identified** in EU, UK or US coverage. EU/DOJ competition activity in 2025–26 is concentrated on Microsoft, Apple, Meta and Google. Salesforce is historically a *complainant* (it urged the EU to review Microsoft/LinkedIn). This is a genuine positive.
- **Sector consolidation:** Informatica acquisition closed **18-Nov-2025** (~$8B equity value), requiring multi-jurisdictional merger clearances and importing a large new PII/data-governance estate — a GDPR/CCPA exposure multiplier rather than a competition problem.
- **M&A/AI stakes:** holdings in Anthropic and Databricks create governance/value-marking questions and, if Anthropic lists, potential CFIUS/export-control touchpoints. Not a disclosed risk today.

---

### 4. Compliance Red Flags

| Flag | Severity | Comment |
|---|---|---|
| Data-breach liability & security-controls adequacy | **Elevated** | MTD denial converts a "cyber incident" into a live legal theory of negligent security; repeat-incident pattern in 2025 is the aggravating fact |
| GDPR/CCPA processor-vs-controller exposure | **Elevated** | Salesforce sits in the processor seat for millions of data subjects; breach notification duties and customer indemnities are compounding |
| EU AI Act Art. 50 transparency (live Aug-2026) | Moderate | Agentforce disclosure/config obligations now enforceable; high-risk deadline deferred to Dec-2027 |
| CIPA/tracking-pixel statutory damages | Moderate | $5,000/violation arithmetic; partially mitigated by California SB 690 (signed 30-Sep-2026, effective 1-Jan-2027) removing the private right of action for pen-register claims |
| Sanctions / FCPA / AML | **Low** | No disclosed OFAC, DOJ or SEC enforcement; enterprise-software model with channel partners is a lower-risk profile than goods trade |
| AI-output liability | Emerging | No clear safe harbour; Apple's $250M Siri-AI settlement (2026) shows the market is now pricing AI-capability misrepresentation |

---

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

**Rationale:** Revenue is overwhelmingly concentrated in high-rule-of-law jurisdictions (US ~61%, Europe ~24%) with no material sanctions, expropriation, currency-control or nationalisation exposure — so *classic* geopolitical risk is low. The rating is driven up by **legal**, not political, factors: an active MDL whose motion-to-dismiss was largely denied in September 2026, an AI-copyright class action, and operating in the single most litigious privacy environment in the world while simultaneously shipping generative-AI agents into a newly enforceable EU AI Act regime. The absence of any antitrust action against Salesforce is the key offsetting factor.

**What would move this to High:** class certification in MDL 3164; a first Salesforce-attributed GDPR fine of scale; an EU AI Act enforcement action against Agentforce; or a US federal procurement shock given public-sector concentration. **What would move it to Low:** global settlement of the MDL within disclosed accruals plus two clean quarters with no new incident.

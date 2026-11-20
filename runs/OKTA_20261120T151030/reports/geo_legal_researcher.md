# Geo Legal Researcher

- Symbol: OKTA
- Elapsed: 116.3s

---
## OKTA — Geopolitical, Regulatory & Legal Risk Assessment
*As of late November 2026 (latest data: Q2 FY2027, quarter ended 31 July 2026)*

### 1. Geographic Risk Map

Okta is a US-centric business: the FY2026 (ended 31 Jan 2026) 10-K states **"20% of our revenue generated outside of the United States in fiscal 2026"** and that **"other than the United States, no individual country exceeded 10% of total revenue"** ([SEC 10-K FY2026](https://www.sec.gov/Archives/edgar/data/1660134/000166013426000020/okta-20260131.htm); Proxy/Annual Report 2026). International mix is rising modestly: **Q2 FY27 international revenue +12% y/y, 21% of total** ([Q2 FY27 commentary](https://s205.q4cdn.com/566291348/files/doc_financials/2027/q2/Q2FY27PostedCommentaryforwebsite.pdf)).

| Geography | Rev. exposure | Risk level | Key drivers |
|---|---|---|---|
| **United States** | ~$2.32B / ~79% (FY26) | **Medium** | Federal/state cyber regs (SEC Item 1.05, FedRAMP/DoD IL), federal contract & congressional scrutiny after Oct-2026 DHS leak, state breach-notification laws |
| **International total** | ~$598M / ~20–21% | **Low–Medium** | FX, DORA/NIS2, EU data-sovereignty procurement bias |
| Europe/UK (largest intl bloc; no single country >10%) | <10% each (est.) | **Medium** | GDPR (up to 4% global turnover), DORA as ICT third-party to financial entities, NIS2 audits (first deadline 30 Jun 2026) |
| Japan / APAC (partner-led) | <10% each | **Low** | Mature rule of law; limited localisation friction |
| Canada, Australia, Netherlands, Germany, France, Singapore, India | <10% each | **Low–Medium** | India DPDP/localisation; otherwise stable |
| Latin America (Auth0 CIAM base) | Immaterial individually | **Medium** | FX/currency volatility, EM macro |
| Cuba, Iran, North Korea, Syria, Crimea/DNR/LNR | **0% — blocked at network level** | **Low** (compliant) | Okta/Auth0 geo-blocks authentication from OFAC-sanctioned regions (see §4) |
| Russia / China | No material disclosed revenue | **Low** | Geo-blocking and export-control screening; China state-linked cyber targeting is a threat vector, not a revenue exposure |

**Concentration:** benign — no non-US country >10% of revenue; no nationalisation/expropriation or currency-repatriation exposure of consequence.

### 2. Top 3 Geopolitical Risks

**1) Identity provider as a nation-state / hacktivist single point of failure (Probability: High; Impact: Medium–High)**
This is Okta's dominant tail risk and it is *live*, not hypothetical. On 28 October 2026 a hacktivist group claimed data on **>41,000 DHS employees** obtained via DHS's Okta single sign-on ([Politico, 28 Oct 2026](https://www.politico.com/news/2026/10/28/dhs-data-leak-hacktivist-01140028)); Okta "denied any compromise of its core systems" while "questions are emerging about its security posture as a federal contractor" ([Yahoo Finance, 31 Oct 2026](https://finance.yahoo.com/markets/stocks/articles/okta-okta-tied-data-leak-221128500.html)), with reports of related breaches touching FBI data. This follows the October–November 2023 support-case-management compromise, which ultimately affected **all** customer-support-system users (134 customers' HAR files) and prompted FINRA/CISA advisories. Expect congressional/OIG oversight noise, renewal friction in federal accounts, and plaintiff-firm activity — an asymmetric, repeated reputational tax on a "mission-critical" narrative.

**2) US federal/public-sector political & budget risk (Probability: Medium; Impact: Medium)**
Okta's federal franchise (FedRAMP Moderate/High, DoD, Gov Identity Summit) makes it exposed to federal IT budget discipline, procurement-policy shifts and post-incident contract scrutiny. Public-sector is not separately disclosed but is a stated growth vertical; any GSA/agency security review triggered by the DHS episode would hit both revenue timing and headline risk.

**3) EU digital-sovereignty regime tightening (Probability: High; Impact: Medium)**
DORA (in force 17 Jan 2025) makes Okta a regulated **ICT third-party provider** to EU financial entities — driving demands for audit rights, exit plans and register-of-information disclosure; NIS2 transposition (first audit deadline 30 Jun 2026) and the Data Act add localisation pressure. EU competitors explicitly market "sovereign" IAM as the Okta alternative (e.g. [cidaas](https://www.cidaas.com/okta-alternative/)). Net effect: higher EMEA cost-to-serve and slower win rates versus a ~21%-of-revenue international base — a margin/competitive risk more than a legal one.

**Secondary:** US–China tech decoupling and sanctions/export-control volatility are **low** direct-revenue risks (no disclosed China/Russia revenue; software subscription delivery largely outside BIS hardware controls), but raise screening/geo-blocking obligations.

### 3. Legal & Regulatory Highlights

- **Securities class action — RESOLVED.** *In re Okta, Inc. Securities Litigation* (N.D. Cal., filed 20 May 2022, re Auth0 integration and cybersecurity disclosures): **$60M settlement**, final approval 19 Nov 2024 ([case site](https://www.oktasecuritieslitigation.com/); [Bloomberg Law](https://news.bloomberglaw.com/litigation/okta-investors-get-60-million-settlement-over-merger-finalized)). Earlier, claims premised on cybersecurity controls were dismissed in part (2023).
- **Derivative action — RESOLVED.** *In re Okta, Inc. Stockholder Derivative Litigation*, No. 3:22-cv-07480 — settlement stipulation dated 26 June 2025, disclosed via 8-K filed 31 July 2025 ([8-K Ex. 99.2](https://www.sec.gov/Archives/edgar/data/1660134/000166013425000156/okta-7312025_8kxex992.htm)). The derivative case had been stayed through discovery in the securities action; that overhang is now cleared.
- **Post-2023 breach litigation:** plaintiff-firm investigations and consumer class actions were filed after the Nov-2023 disclosure (e.g. [classaction.org](https://www.classaction.org/data-breach-lawsuits/okta-november-2023), [Rosen](https://rosenlegal.com/cases/okta-inc)); no material reserve or adverse judgment publicly disclosed. Watch for renewed filings from the Oct-2026 DHS incident.
- **SEC enforcement (third-party):** on **15 Sep 2026 the SEC announced settled insider-trading charges against former Okta personnel** who traded ahead of a company announcement ([SEC Order 34-106363](https://www.sec.gov/enforcement-litigation/administrative-proceedings/34-106363-s); [Law360](https://www.law360.com/articles/2525817/sec-fines-ex-okta-employees-in-insider-trading-case)). Okta itself was **not** charged — a controls/reputational item, not a liability item.
- **No disclosed DOJ/FTC/EC investigation** of Okta found in searchable sources; note the tool's 10-K/10-Q fetch returned "no filing found" and sec.gov blocked direct retrieval, so *absence of a disclosed investigation is not verified against the primary document* (gap).
- **Regulatory posture (product-driven, favourable):** Okta is a *beneficiary* of SEC cyber-disclosure rules, DORA/NIS2, EU AI Act (GPAI obligations since Aug 2025) and FedRAMP — management explicitly frames "tightening regulatory mandates" as an identity demand driver. Its own commentary flags attribution/AI-agent accountability gaps under GDPR ([Okta blog, Feb 2026](https://www.okta.com/blog/ai/the-attribution-gap-ai-regulation/)).

### 4. Compliance Red Flags

- **Sanctions geo-blocking — managed, one open item.** Okta and Auth0 block authentications originating in **Cuba, Iran, North Korea, Syria, and the Crimea/DNR/LNR regions** of Ukraine (implemented Oct 2022) ([Okta IP Access Policy](https://support.okta.com/help/s/article/Okta-IP-Access-Policy?language=en_US); [Harvard GSS](https://www.globalsupport.harvard.edu/about/news-events/duo-okta-block-authentications-ofac-sanctioned-countries-and-regions); [Iowa State](https://global.ag.iastate.edu/news/2022/okta-international-ip-blocks)). ⚠️ **Open question:** Auth0's own support documentation acknowledges customers asking whether blocking will be lifted for **Syria following the lifting of OFAC's comprehensive Syria program** — i.e. a sanctions-list currency/remediation item ([Auth0 support](https://support.auth0.com/center/s/article/Sanctioned-Country-Access-through-Auth0)).
- **Data-privacy/processor exposure.** Okta processes customer end-user identity data → GDPR processor duties (Art. 28 DPAs), all-50-state breach notification, and contractual liability to enterprise customers. The 2023 and 2026 incidents are the realistic trigger for regulatory inquiry.
- **FedRAMP/DoD continuous-monitoring obligations** — the DHS episode invites scrutiny of Okta's own POA&M disclosures.
- **Insider-trading controls** — two former employees settled SEC charges in Sept 2026.
- **No FCPA/AML/bribery flags identified.** Okta's risk profile is cyber/privacy/contract, not corruption.

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

Revenue geography is low-risk (79% US, no foreign country >10%), sovereign/expropriation/currency-control exposure is negligible, and Okta is a net regulatory *beneficiary*. The Medium rating is driven by (a) elevated and **repeat** cyber-incident frequency at the identity layer with direct federal-government visibility (Oct-2026 DHS episode), (b) litigation/oversight tail risk that re-prices after each incident, and (c) EU sovereignty/DORA compliance costs against a ~21% international book. It is **not** driven by sanctions, corruption, or emerging-market country risk.

**Key evidence gaps:** primary 10-K/10-Q text could not be retrieved (SEC 403; tool reported "No 10-K/10-Q found"), so legal-proceedings and risk-factor language is sourced from SEC-adjacent indices and secondary summaries rather than the filing body; country-level revenue beyond US/non-US is not disclosed by Okta.

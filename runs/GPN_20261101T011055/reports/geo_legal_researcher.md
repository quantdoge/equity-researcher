# Geo Legal Researcher

- Symbol: GPN
- Elapsed: 80.9s

---
## GPN — Geopolitical & Legal Risk Assessment
*Global Payments Inc. | Financial Services / Payment Processing | Atlanta, GA | Mkt cap ~$25.6B, price $96.84*

**Analyst note on data gaps:** GPN's FY2025 10-K (filed 2026-02-20) and Q2 2026 10-Q (filed 2026-08-05) were retrievable only as XBRL-tagged HTML/PDF that my filing tools could not render into prose; `fetch_filing_text` returned no 10-K. Segment/geographic *dollar* tables below are therefore partly estimates, explicitly flagged, triangulated from pre-deal disclosures, the XBRL member tags I could read, and press coverage. Where a claim is sourced, the source is named.

---

### 1. Geographic Risk Map

GPN closed two transformational transactions on **9 January 2026**: the ~$24.25B acquisition of **Worldpay** (including FIS's stake at $6.6B pre-tax) and the **$13.5B divestiture of its Issuer Solutions business to FIS**. This reshuffled the footprint materially toward US/UK/Brazil merchant acquiring and away from US-centric issuer processing. New reporting segments: **Enterprise, Platforms, and Small & Medium Businesses** (SMB split Americas vs. Rest of World), per XBRL members in the Q2 2026 10-Q.

| Country / Region | Est. revenue exposure (post-Worldpay) | Key exposures | Geopolitical risk | Regulatory risk |
|---|---|---|---|---|
| **United States** | ~65–72% | Merchant acquiring, SMB, Platforms, Gaming/iGaming, integrated software | **Low** | **High** — state AGs, CFPB (posture reversed 2025), FTC, card-network rules, interchange litigation |
| **United Kingdom** | ~8–10% | Worldpay legacy merchant book, cross-border e-commerce | **Low** | **High** — FCA, PSR (IFR enforcement, APP fraud reimbursement), BoE |
| **Europe (EU/EEA)** | ~8–10% | Merchant acquiring, Germany JV, Central/Eastern Europe | **Low–Med** | **High** — IFR caps (0.2% debit / 0.3% credit), PSD2/PSD3, GDPR, DSA |
| **Brazil / LatAm** | ~5–8% | Worldpay LatAm merchant book; "Pagos y Servicios S.A." JV | **Medium** — FX volatility, fiscal cycles | **Medium–High** — BCB, Pix competition, interchange caps |
| **Asia-Pacific (incl. Greater China)** | ~5–7% | HK/China merchant acquiring; **stake in China UnionPay Data Co. Ltd** (per FY2025 10-K XBRL member) | **Medium–High** — US-China tensions, data localization, PIPL | **Medium–High** |
| **Middle East (UAE, Saudi, Israel)** | ~2–4% (travel/cross-border skewed) | Cross-border travel & e-commerce processing | **High** — active conflict, Strait of Hormuz disruption | Medium |
| **India / SE Asia** | ~1–3% | Merchant acquiring, "NBGPay" JV | **Medium** — capital controls, licensing | **Medium–High** |

**Supporting facts I could verify:**
- Workforce geography (FY2025 10-K): **~50% Americas, 22% Europe, 28% Asia-Pacific** of ~26,000 employees — pre-Worldpay-close, so post-deal mix skews more Americas/Europe. ([10-K PDF, 02/20/2026](https://investors.globalpayments.com/financial-information/all-sec-filings/content/0001123360-26-000008/0001123360-26-000008.pdf))
- Q2 2026: **adjusted net revenue $3.16B, +4% normalized, GAAP diluted EPS $3.46**, with a **~100bp normalized revenue headwind from the Middle East conflict**; FY2026 outlook cut. ([Fortune transcript](https://fortune.com/company/global-payments/earnings/q2-2026/), [MarketBeat/Yahoo](https://finance.yahoo.com/markets/stocks/articles/global-payments-q2-earnings-call-100349946.html))
- `get_company_profile` confirms operations spanning Americas, Europe, Asia-Pacific.

---

### 2. Top 3 Geopolitical Risks

**Risk 1 — Middle East conflict / Strait of Hormuz and cross-border travel volumes. Probability: HIGH (already occurring). Impact: MODERATE (~1–2% of revenue).**
Management explicitly attributed a **~100bp normalized revenue headwind** and a lowered FY2026 guidance to "continued pressure on travel-related volumes from the Middle East conflict." This is the single most *demonstrated* geopolitical sensitivity in the model — GPN monetizes cross-border travel spread, so Gulf air corridors matter disproportionately to the highest-yield line. The 2026 backdrop is worse than a normal cycle: Iran has conditioned reopening of the Strait of Hormuz on sanctions relief, Treasury has launched an "unprecedented" secondary-sanctions campaign on parties doing business with Iran, and the US imposed additional sanctions on third countries dealing with Iran while de-designating Syria. **Watch:** any Hormuz closure headline hits GPN's cross-border spread before it hits consensus numbers.

**Risk 2 — Post-Worldpay regulatory perimeter expansion across ~40+ jurisdictions. Probability: HIGH. Impact: MODERATE.**
The deal doubled the number of merchant-acquiring licences, sponsor-bank relationships and money-transmission registrations GPN must maintain, in an environment where the CFPB's enforcement posture has swung from active (2022–2024) to case-closing (2025–2026). That creates **asymmetric regulatory risk in both directions**: less federal consumer enforcement now, but state AGs (Virginia already fined Worldpay, LLC $5,000 in 2026 per Violation Tracker) and EU/UK regulators (PSR IFR enforcement, APP-fraud liability) are filling the gap. Synergy delivery assumes no supervisory friction on licence transfers — a live integration risk.

**Risk 3 — US-China / export controls and Greater China data localization. Probability: MEDIUM. Impact: LOW–MODERATE.**
GPN retains a **stake in China UnionPay Data Co. Ltd** and Greater China merchant operations. Escalating US-China tech and data rules, PIPL localization requirements, and the precedent of forced divestitures make this a low-revenue but high-tail-risk item. Secondary sanctions screening obligations (post-2026 Iran escalation) also raise merchant-portfolio KYC cost globally — GPN screens millions of small merchants, where sanctions false-negative exposure is structurally high.

*(Runner-up: LatAm FX — management flagged a "less favorable FX outlook" in the same guidance cut, per Bob Hammel's [note](https://bobhammel.substack.com/p/global-payments-nothing-comes-easy).)*

---

### 3. Legal & Regulatory Highlights

**Penalty history (Violation Tracker, Good Jobs First — parent-level, since 2000):** total **$101.25M across 8 records**, of which **$99.0M is consumer-protection-related**. This is a concentrated, thematically consistent record — GPN's legal risk is *consumer/deceptive-practices*, not FCPA or antitrust.

| Case | Type | Year | Amount |
|---|---|---|---|
| Central Payment Co. | Consumer protection, private federal | 2022 | **$84.0M** |
| Worldpay US, Inc. | Consumer protection, private federal | 2020 | **$15.0M** |
| Heartland Payment Systems | **Investor protection, SEC** | 2018 | $2.16M |
| Worldpay, LLC | Consumer protection, **Virginia state regulator** | **2026** | $5,000 |
| Central Payment / Heartland entities | Wage & hour (DOL) | 2014, 2019 | ~$75K |

**Active / recently resolved matters:**
- **CFPB v. ACTIVE Network, LLC** (GPN-owned): filed 18 Oct 2022 over deceptive "dark patterns" and junk fees in event-registration flows. The court **administratively closed the case on 5 May 2025** — consistent with the CFPB's 2025–2026 wave of enforcement dismissals. Residual exposure: private follow-on litigation and state AG copycats. ([CFPB docket](https://www.consumerfinance.gov/enforcement/actions/active-network-llc/), [Payments Dive](https://www.paymentsdive.com/news/cfpb-federal-lawsuit-active-network-global-payments-junk-fees-deceptive-marketing/634480/))
- **Securities class action** (Oct 31, 2019 – Oct 18, 2022 class period) alleging GPN misled investors about **legal compliance** re: Active Network; settled for **$3.6M**. ([Lowey Dannenberg](https://lowey.com/news/3600000-settlement-on-behalf-of-global-payments-investors-2/), [Stanford SCAC](https://securities.stanford.edu/filings-case.html?id=108085))
- **Legacy data breach (2012)** — intrusion into the processing environment enabling card-data export; the origin of the 2018 SEC action. Still cited in industry breach compendia as a governance reference case.

**Regulatory posture by jurisdiction:**
- **US:** CFPB de-emphasizing enforcement (a *tailwind* through 2026), but **state AGs and state financial regulators** are the live vector (see Virginia 2026 action). Card-network rule changes and merchant-interchange litigation are perennial.
- **UK:** PSR actively enforcing the IFR and moving on APP-fraud reimbursement liability — directly shifts fraud losses toward processors.
- **EU:** IFR caps (0.2%/0.3%), PSD3/PSR proposal, GDPR. Germany JV adds BaFin supervision.
- **Brazil:** BCB oversight of payment institutions; Pix has structurally compressed acquiring economics.

---

### 4. Compliance Red Flags

1. **Consumer-protection recidivism (highest-conviction flag).** $99M of $101M in lifetime penalties are consumer-protection, across *four separate* records spanning two legacy franchises (Central Payment, Worldpay). Post-merger, GPN inherits Worldpay's sales-agent and ISO channel — the exact distribution model that generated the $84M and $15M settlements. **This is the most likely source of the next material legal event.**
2. **Sanctions/AML merchant-onboarding exposure.** As a scaled acquirer across 175+ markets with heavy SMB and card-not-present volume, GPN is a structural target for regulator criticism of merchant-portfolio screening — particularly with 2026's expanded Iran secondary-sanctions regime.
3. **FCPA/third-party risk** in LatAm and Asia distribution (agents, ISOs, JV partners). No disclosed FCPA matter — but the JV/agent structure is the classic vector; I found no evidence of an active investigation.
4. **Data privacy:** GDPR/PIPL/CCPA/state privacy laws across a business that processes card data at massive scale; the 2012 breach remains a reputational anchor.
5. **Integration-related disclosure risk:** the Worldpay/Issuer Solutions transaction accounting (discontinued operations reclassification, purchase accounting) is complex; note the FY2025 10-K includes a **prior-period reclassification adjustment** member — worth monitoring for control weakness commentary.

---

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

**Rationale:**
- **Mitigants:** No mega-litigation overhang (largest open matters are closed or settled for <$4M); no disclosed DOJ/FCPA/OFAC investigation; revenue base concentrated in low-geopolitical-risk US/UK/EU (~85% combined); CFPB enforcement currently quiescent; sanctions/Russia exposure appears immaterial post-2024 restructuring.
- **Aggravants:** A **proven, quantified geopolitical sensitivity** (Middle East travel → 100bp headwind and a guidance cut in the same quarter); the highest-in-class consumer-protection penalty record among payment processors; and a regulatory perimeter that just expanded across dozens of jurisdictions via Worldpay with integration still in-flight.

**Key monitorables into Q3 2026 (results 5 Nov 2026):** (i) whether the Middle East travel headwind is quantified again or reverses; (ii) any state-AG action on Worldpay/legacy ISO channels; (iii) FX guidance revisions (LatAm); (iv) post-deal segment geographic disclosure in the FY2026 10-K — which will finally give a clean revenue-by-geography table.

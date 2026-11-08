# Geo Legal Researcher

- Symbol: TEAM
- Elapsed: 91.0s

---
## Atlassian Corporation (TEAM) — Geopolitical & Legal Risk Assessment

**Company setup:** Atlassian is a US-domiciled (Delaware) software company, Australian-founded, dual-HQ'd Sydney/San Francisco, ~13,300 employees, ~$39B market cap. It is a pure SaaS/subscription business — no hardware, no dual-use technology, no manufacturing supply chain, and no disclosed customer >10% of revenue. That structurally lowers classic geopolitical exposure (sanctions, tariffs, export-controlled goods, expropriation of physical assets) and shifts the risk centre of gravity to **regulation of data, AI, and public-sector procurement**.

**Method note / gap:** `fetch_filing_text` returned "No 10-K found" twice for the FY2026 10-K (filed Aug 2026); only the 10-Q certification exhibit resolved. Geographic revenue below is from FMP-derived FY2026 (ended 6/30/2026) segment data; legal/regulatory items are sourced from court dockets, NLRB records, and news. Direct 10-K risk-factor language could not be quoted.

---

### 1. Geographic Risk Map (FY2026, total revenue $6,572M)

| Country / Region | FY2026 Revenue | % of Total | YoY | Geopolitical Risk | Key drivers |
|---|---|---|---|---|---|
| **United States** | $2,760M | **42.0%** | +26.5% | **Low geo / Medium policy** | Federal procurement volatility (DOGE-era cuts), securities litigation venue, FedRAMP re-badging, state privacy/AI laws |
| **Germany** | $692M | **10.5%** | +28.3% | **Low geo / Medium regulatory** | GDPR enforcement culture, works councils, EU AI Act; fastest-growing major market |
| Other EMEA | $2,003M | 30.5% | +26.3% | **Low–Medium** | UK, Nordics, France, Benelux, Middle East; DORA/NIS2/Data Act; data-sovereignty demands |
| **EMEA total** | **$2,693M** | **41.0%** | +26.8% | **Low geo / Medium regulatory** | Largest regulatory-burden bloc |
| Asia Pacific | $713M | 10.9% | +24.2% | **Medium** | Australia home market (Privacy Act reform), Japan, India (DPDP Act) |
| Other Americas | $406M | 6.2% | +21.2% | Low–Medium | Canada, LatAm (FX, Brazil tax complexity) |

**Operational footprint (not revenue):** Bengaluru, India is the **largest hub outside Australia and the US — 2,500+ employees, ~75% in R&D**, in a new 200k+ sq ft facility (hrtoday.in, businessline). This concentrates engineering delivery in one emerging market — a single-country operational dependency that does not appear in the revenue table. Australia remains the cultural/HQ anchor; the company redomiciled from UK to Delaware in 2022 (explaining stale "Atlassian Corporation PLC" references in some data feeds).

**Exposures materially absent:** No disclosed Russia revenue (exited post-2022), negligible direct China presence (Chinese customers historically served via Data Center/partners), no tariff-sensitive physical goods. US–China decoupling is therefore an indirect (customer-demand) rather than direct revenue risk.

---

### 2. Top 3 Geopolitical / Policy Risks

**Risk 1 — EU regulatory stack + data sovereignty (highest probability × highest impact)**
- **Probability: High (adverse event likely); Impact: Medium (~41% of revenue sits in EMEA)**
- The EU AI Act became **fully applicable August 2, 2026**; DORA (financial-services customers), NIS2, and the EU Data Act layer on top. Atlassian publishes compliance positions for each (atlassian.com/trust/compliance) — a signal that customer assurance demands are now a sales-cycle gate.
- Compounding this: Atlassian **end-of-lifed Data Center sales (no longer sold as of March 2026, "Ascend" initiative)**, removing the on-premises option that sovereign/government customers previously used to sidestep cloud-residency objections. Data residency must now do that work — and "Backup and Restore supports data residency **starting April 28, 2026**," i.e., the capability is recent (Atlassian support docs). Any German, French, or public-sector customer that cannot be satisfied on residency is a migration-to-competitor risk.

**Risk 2 — US public-sector / federal procurement volatility**
- **Probability: Medium; Impact: Medium-low directly, but high narrative sensitivity**
- Atlassian is leaning *into* government (Atlassian Government Cloud, FedRAMP; a 2026 "next chapter of public sector investments" campaign explicitly citing "rising geopolitical" pressure and "shifting data sovereignty requirements"). Expanding into the most politically volatile customer segment as DOGE-driven contract scrutiny and shutdown risk persist (GAO-26-108615 tracks DOGE contract savings through July 2026) is a deliberate but cyclical bet. FedRAMP's **May 4, 2026 renaming to "FedRAMP Certification"** also creates re-authorization administrative drag.

**Risk 3 — AI-transition litigation and labor/regulatory spillover**
- **Probability: High (more filings likely); Impact: Low individually, Medium in aggregate (management distraction, disclosure cost, brand)**
- Two US firms were recruiting shareholders over Atlassian's "AI-driven spiral" in **March 2026** (AFR, 2026-03-30; Portnoy Law investigation, hcamag). No complaint confirmed in my searches — treat as a **live threat, not a filed case**.
- Atlassian is a **serial NPE/patent defendant** (Pherah 2015, Red River 2019, Waco-Texas campaign, and **DataCloud Technologies, LLC v. Atlassian, D. Del. 1:26-cv-01350, filed October 19, 2026**). Nuisance-value suits; no injunction risk to the platform.

---

### 3. Legal & Regulatory Highlights

| Matter | Status | Assessment |
|---|---|---|
| **NLRB Case 16-CA-324971** (Denise Unterwurzacher) | ALJ decision **July 1, 2026**: found §8(a)(1) NLRA violation for firing an engineer over protected concerted activity (Slack clash with leadership); ordered **reinstatement + back pay**; transferred to the Board — appeal pending | **Most substantive active matter.** Precedent risk: scrutinizes employee speech norms at a company whose brand is collaboration. Immaterial financially; reputationally awkward |
| **DataCloud Technologies v. Atlassian** (D. Del., Oct 19, 2026) | Filed; patent infringement, jury demand | Typical PAE suit; low expected value |
| **Securities class action** (In re Atlassian, N.D. Cal., filed Feb 2023) | **Dismissed** Jan 22, 2024 (Judge Orrick); final judgment **Sept 3, 2024** | Closed — clean outcome |
| **2026 shareholder-solicitation activity** | Portnoy Law et al. investigating (Mar 2026) | Not filed; monitor |
| **10-K Legal Proceedings disclosure** | "From time to time, the Company is party to litigation and other legal proceedings in the ordinary course of business" | Standard boilerplate; no material accrued contingency signaled |
| **Antitrust / merger control** | Loom ($975M, 2023) and DX (~$1B, 2025) cleared on customary conditions; no active challenge found | Low — sub-scale for global antitrust concern |
| **2026 restructuring** | ~10% workforce reduction reported in 2026 (TechRepublic) | Raises employment-claim and morale risk; NLRB matter is the leading indicator |

---

### 4. Compliance Red Flags

1. **Default-on AI training on customer content (effective August 17, 2026) — the single sharpest flag.** Jira/Confluence metadata and in-app data flow into AI training on an **opt-out** basis, with "some data [that] cannot be opted out" (Atlassian Data Contribution FAQs; widespread practitioner/Reddit pushback; law.stackexchange debate on GDPR lawfulness). This is precisely the fact pattern that generated **noyb's GDPR complaints against X/Meta** for AI training without consent. Atlassian's DPA and "de-identified" framing are the mitigants, but German/EU DPAs have not been shy here. **No confirmed enforcement action or complaint found — this is prospective risk, not an existing investigation.**
2. **Sovereignty gap from Data Center EOL.** Discontinuing on-prem sales (March 2026) while data-residency tooling matures into 2026 pushes regulated customers onto a US-controlled cloud under a US-parent DPA — the exact objection EU/public-sector buyers raise. Expect longer deal cycles and elevated loss rates in German public sector and EU financial services (DORA).
3. **FedRAMP / government cloud controls** require US-person access restrictions and citizenship-gated support — an operational constraint given heavy non-US (India, Australia) engineering staffing.
4. **FCPA / AML / sanctions: no red flags identified.** Software SaaS with self-serve distribution, no third-party-agent-heavy emerging-market sales model, no dual-use product. Sanctions exposure is limited to partner-channel leakage (re-seller sales into restricted territories), which is a monitoring item, not a disclosed problem.
5. **Data privacy litigation history** (2022 breach of Atlassian's own systems; CISA advisories on Confluence CVEs AA23-289A) creates recurring class-action vectors inherent to the category; none currently active or material.

---

### 5. Overall Geopolitical / Legal Risk Rating: **MEDIUM**

**Rationale:** Jurisdictional diversification is genuinely strong — no single country above 42% and no DM nearshoring/nationalisation exposure — and the legal docket is nuisance-grade (one small NLRB matter, serial PAE suits, a dismissed securities case). What pulls the rating to Medium is not geopolitics but **regulatory density in its two largest markets and the timing of two self-inflicted decisions**: shifting 41% of revenue onto an EU regulatory stack that became fully enforceable in August 2026, while simultaneously (a) making AI training opt-out-by-default on customer data and (b) removing the on-premises escape hatch. Both are manageable, but both convert regulatory trust into a competitive variable rather than a compliance formality.

**What would move it to High:** a GDPR/AI Act complaint or DPA inquiry tied to the August 2026 data-contribution change; a filed 2026 securities class action over AI guidance; or loss of FedRAMP certification/authorization continuity in the federal segment.

**Sources:** Financial Modeling Prep FY2026 segment revenue (via bullfincher.io, updated 6/30/2026); Atlassian FY2027 Q1 8-K/press release (Business Wire 11/5/2026, revenue $1,772M, +24%); SEC EDGAR CIK 0001650372; NLRB case 16-CA-324971 docket; NLRB ALJ decision coverage (NYT 7/10/2026, OnTheLaborFront); Justia dockets (DataCloud v. Atlassian, 1:26-cv-01350); Stanford SCAC case record (dismissal 9/3/2024); AFR 3/30/2026 and hcamag (Portnoy investigation); atlassian.com/trust compliance pages (EU AI Act, DORA, EU Data Act, FedRAMP, Data Contribution FAQs); Atlassian support (data residency, Apr 28 2026); hrtoday.in / The Hindu BusinessLine (Bengaluru 2,500+ employees); GAO-26-108615 (DOGE savings review).

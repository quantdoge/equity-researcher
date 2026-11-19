# Esg Analyst

- Symbol: RBRK
- Elapsed: 80.6s

---
## Rubrik, Inc. (RBRK) — ESG Analysis
**Sector:** Technology / Software – Infrastructure (data security, cyber resilience, AI governance) | **Market cap:** ~$22.6B | **Employees:** 3,797 | **FY26 revenue:** $1.32B | **IPO:** April 2024

*Data note: the filing API returned no 10-K/10-Q/DEF 14A for RBRK, and SEC.gov, rubrik.com and the proxy-vote PDF were blocked (403/raw bytes). Governance and disclosure facts below are drawn from SEC filing snippets surfaced via search, secondary reporting, and company materials. Gaps are flagged rather than filled with assumptions.*

---

### 1. ESG Materiality Map

| Factor | Materiality | Why it hits cash flows / cost of capital |
|---|---|---|
| **Governance — dual-class control & related-party dealings** | **High** | 20 votes/Class B; insiders hold ~46% of voting power. Outside shareholders cannot influence strategy or comp. Warrants a governance discount. |
| **Social — own security posture / breach risk** | **High** | Rubrik *sells* trust. Two own-incident disclosures (2023 Fortra GoAnywhere, 2025 log server) mean reputational damage is a direct revenue risk, not a compliance cost. |
| **Social — product safety & AI governance** | **Medium-High** | Rubrik Agent Cloud (Feb 2026) governs autonomous AI agents. If an agent's actions are wrongly approved/reversed, Rubrik is in the liability chain. AI-washing litigation is a live 2026 theme. |
| **Regulatory — public sector & EU compliance** | **Medium-High** | FedRAMP Moderate, StateRAMP, CJIS, DoD requirements; NIS2/DORA flow-down from financial-services and healthcare customers. |
| **Human capital** | **Medium** | 3,797 employees scaling ~49% revenue growth; attrition and sales-force productivity drive the model. |
| **Environmental (Scope 1/2)** | **Low** | Asset-light software; office electricity only. |
| **Environmental (Scope 3 / hardware)** | **Low-Medium** | Cloud infrastructure (AWS/Azure/GCP) plus appliance manufacturing and e-waste. No disclosed emissions inventory. |
| **CBAM / stranded assets** | **Negligible** | No carbon-intensive goods; IT equipment outside CBAM scope. |

---

### 2. Environmental Risk Assessment: **Low**

- **No standalone sustainability report, no disclosed Scope 1/2/3 emissions, no SBTi or CDP submission found.** Rubrik's ESG function appears to sit within legal/compliance (a sustainability lead is now senior director, corporate legal & compliance) rather than a dedicated function — consistent with a 2024 IPO that has not yet built CSRD-grade reporting.
- **Structural footprint:** cloud-hosted SaaS plus physical appliances sold through manufacturers. The 10-K explicitly flags "reliance on third-party clouds and manufacturers," which is where the Scope 3 concentration sits — AWS/Azure/GCP energy procurement and appliance supply chain.
- **Physical climate risk:** indirect — data-centre water/heat exposure is borne by cloud providers, though customer contracts may push continuity obligations back to Rubrik.
- **No environmental controversies, fines, spills or remediation liabilities identified.**
- **Verdict:** immaterial to valuation today; the real risk is *disclosure* risk (CSRD readiness) rather than physical or transition risk. No CBAM or carbon-tax exposure.

---

### 3. Social Risk Assessment: **Medium**

**The central issue: a security vendor that has had two own-incidents.**

| Incident | Detail | Financial impact |
|---|---|---|
| **Mar 2023 — Fortra GoAnywhere MFT zero-day (CVE-2023-0669)** | Unauthorised access to a non-production IT testing environment; "access information" compromised; customer data not impacted per company. | Vendor-caused; no disclosed fine or customer loss. |
| **Mar 2025 — Rubrik log server** | Anomalous activity on a server containing log files; small number of logs held access information; authentication keys rotated. No customer data affected. | **No measurable market impact.** Stock closed $61.37 (3 Mar) → $61.56 (4 Mar) → $70.64 by 14 Mar. Direct remediation cost de minimis (<$5M est.). |

The 2025 event is the more instructive datapoint: the market *did not* punish it. That tells us investors currently treat Rubrik's own-security risk as low-probability/low-severity — which is precisely why a **real customer-data breach is an underpriced tail risk**. For a company whose entire value proposition is "your data is safe with us," a material breach would plausibly cost several points of ARR growth and 15–25% of market cap. That is the asymmetry to monitor.

**Supporting positives:**
- Product is socially useful: cyber resilience for hospitals (MEDITECH), universities (Internet2), and state/local government — sectors that are chronically under-defended. Membership in the Coalition for Health AI (CHAI) signals responsible-AI positioning.
- "Rubrik Beyond Work" CSR programme since 2018, with 1% of employee time for volunteering.
- Board-level diversity: two of the named directors are women (Yvonne Wassenaar, Rakefet Russak-Aminoach, appointed Aug 2026); CEO Bipul Sinha is a founder of Indian origin.
- Great Place to Work certification on record (87% vs 57% typical US company) — **but the survey source is dated 2021**, so it is stale evidence for a headcount that has roughly doubled.

**Gaps:** no disclosed attrition, pay-equity, or EEO-1 data; no verified union/labour-standards disclosure. Human capital is the weakest-disclosed social pillar.

---

### 4. Governance Quality Score: **5 / 10**

**Structure:** dual-class, 20 votes per Class B share. 157.4M Class A + 44.9M Class B outstanding (Feb 2026); insiders including officers and directors control ~46% of voting power. CEO Sinha holds ~29.5% Class B. No disclosed sunset provision found — a genuine gap.

**Positives (+)**
- Independent Audit, Compensation and Nominating/Governance Committees; separate **Cybersecurity Committee** with its own charter — genuinely uncommon and appropriate for this business.
- **John W. Thompson as Lead Independent Director** (ex-Symantec CEO, ex-Microsoft chairman) — a credible counterweight to founder control.
- Majority-independent board; new director Russak-Aminoach (ex-Leumi CEO) adds financial-services and governance depth.
- Dodd-Frank-compliant clawback policy; restrictions on share pledging; anti-hedging.
- **CEO compensation is well-aligned in structure:** $1.8M total (deliberately low; founder already aligned), with options vesting against **10 stock-price hurdles from $43 to $243**, five achieved by end-FY26. This is a real long-horizon alignment mechanism.
- No short-seller report, securities class action, or regulatory investigation identified as of Nov 2026. The Commvault patent litigation was settled in Sept 2021 and is not an overhang.

**Negatives (−)**
- **CEO/Chairman duality** — Sinha is both. Mitigated by the Lead Independent Director, not eliminated.
- **46% insider voting control with 20:1 votes** — the single largest governance discount factor. Say-on-pay and shareholder proposals are effectively advisory only.
- **Related-party transaction:** the July 2025 **Predibase acquisition ($109M)** included **$34M of stock to Greylock**, whose partner Asheem Chandna sits on the board *and* on the Audit Committee that vetted the terms. Arm's-length vetting was asserted, but this is exactly the pattern that concentrates risk in founder-controlled companies.
- **Compensation metric design:** bonuses are tied "strictly" to New and Expanded ACV, with a **100% payout in FY26**. A pure growth metric with no FCF or margin gate is a mild misalignment at a company still posting a $(348.8)M net loss and a $(3.19)B accumulated deficit.
- **Perquisites:** ~$265k of company funds for the CEO's HSR filing fees plus tax gross-ups — small in dollars, poor in optics.

**Score rationale:** institutional-grade committee architecture and a well-designed founder option package earn real credit, but 20:1 voting, CEO/Chair duality, and a VC-affiliated director approving a deal that paid his own firm pull the score to the middle. Not a governance basket case; not a leader.

---

### 5. ESG Controversies (with financial impact estimates)

| Controversy | Status | Est. financial impact |
|---|---|---|
| 2025 log-server breach (access info, keys rotated) | Disclosed, remediated | <$5M direct; **$0 market impact** |
| 2023 Fortra GoAnywhere vendor breach | Historical, remediated | Negligible; no customer-data loss |
| Predibase / Greylock related-party ($34M stock) | Disclosed, Audit Committee vetted | No loss; governance overhang |
| Commvault patent litigation | Settled Sept 2021 | Resolved, no reserve |
| AI-agent governance efficacy ("no one's measured if the judge is right") | Product-level critique, 2026 | Unquantified; AI-washing litigation risk |

**Net:** no controversy rises to a material financial event. The pattern is *diligent disclosure of small incidents* — which is itself a governance positive.

---

### 6. Regulatory ESG Exposure

- **US:** SEC climate disclosure rule remains in litigation/stay — exposure is currently minimal. **SEC cyber disclosure (Form 8-K Item 1.05)** applies and Rubrik has shown it will disclose incidents promptly. FedRAMP Moderate authorization (Dec 2024), StateRAMP/GovRAMP, CJIS, FERPA and DoD cloud requirements create ongoing audit costs but also a moat. CMMC matters for defence-adjacent customers. Export controls apply to a global customer base.
- **EU:** International revenue was **$364.5M of $1.32B (27.6%)** in FY26. **NIS2** and **DORA** obligations flow down contractually from Rubrik's financial-services and healthcare customers — Rubrik becomes a regulated supplier and must evidence security standards in every renewal. **EU AI Act** is directly relevant to Rubrik Agent Cloud's AI-agent governance and semantic guardrails. **CSRD** is an emerging exposure: a non-EU parent with EU turnover approaching the €150M threshold and EU subsidiaries would be in scope on a delayed timeline; Rubrik is not remotely ready to report at that standard.
- **ESG-linked debt covenants:** none identified.
- **CBAM:** not applicable.

---

### 7. Overall ESG Rating: **Average**

Rubrik is a **governance-constrained average performer**. It is not an ESG leader (no emissions disclosure, no sustainability report, no credible human-capital metrics, 20:1 dual class) and it is emphatically not a laggard or an ESG risk case (no fines, no material controversies, independent committees, a functioning cybersecurity committee, and genuinely long-dated founder incentives). The E pillar is nearly absent — but so is its materiality. The S pillar is where the business model and the risk intersect. The G pillar is where the discount lives.

---

### 8. ESG Investment Implication: **Neutral**

**ESG factors do not move the thesis.** The investment case rests on ~33% ARR growth, >119% NRR, a Rule of 53.4% profile, and AI-governance optionality — none of which ESG analysis materially alters. Three specific considerations for the memo:

1. **Apply a modest governance discount (~5–10%)** for 20:1 dual-class control, CEO/Chair duality, and the Predibase/Greylock related-party deal. Watch for any further related-party transactions with Greylock or Lightspeed affiliates; that would be a sell-side governance trigger.
2. **Treat a customer-data breach as an underpriced tail risk.** Two own-incidents in three years, and the 2025 event produced zero price reaction — the market is not charging for this. A breach that actually hit customer backups would be existential for the franchise and would likely cost 15–25% of market cap. Size positions accordingly.
3. **Monitor AI-governance liability.** Rubrik Agent Cloud puts the company in the chain of custody for autonomous agent actions. If an AI agent reverses or fails to reverse a destructive action, Rubrik inherits the blame — and the EU AI Act plus 2026's AI-washing litigation trend make this a live, if unquantified, exposure.

**Verdict: Neutral.** ESG is not a reason to own or avoid RBRK. The dual-class structure and related-party pattern are the only items that should affect the price paid, and they argue for a small discount rather than an exclusion.

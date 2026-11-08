# Nonfin Risk Analyst

- Symbol: TEAM
- Elapsed: 54.9s

---
# Non-Financial Risk Assessment — Atlassian Corporation (NASDAQ: TEAM)

**Analyst:** Non-Financial Risk Desk | **Price:** $153.68 (close 6 Nov 2026) | **Mkt cap:** $38.9B | **Sector:** Technology — Application Software | **Employees:** ~13,301 (post-RIF)

**Context for this assessment:** TEAM is a highly volatile name in the current tape. 52-week range is **$68.81 (23 Feb 2026) to $229.96 intraday (22 Oct 2026)** — an extraordinary $161 spread. The stock is **-33% from its 22 Oct high** and **-13% over twelve months**, having round-tripped a 50% crash and a ~230% recovery within the same year. Q1 FY27 (5 Nov 2026) delivered revenue of ~$1.8B (+24% YoY), RPO of $4.7B (+44%), cloud +31%, and EPS of $1.65 vs. $1.39 consensus — **yet the stock fell ~16% on cloud-growth deceleration guidance.** This gap between reported results and market reaction is itself a governance/communication risk signal.

---

## 1. Governance Quality Rating: **Adequate — but structurally constrained**

**Supporting evidence (positive):**
- **Independent Chair.** Dr. Shona L. Brown has chaired the board since April 2018 and was re-appointed in September 2026. There is **no CEO/Chairman duality** — a genuine positive, and the proxy explicitly describes the structure as one of an independent chair.
- **Board is majority-independent.** The eight-person board comprises founders Mike Cannon-Brookes and Scott Farquhar plus six independents (Brown, Scott Belsky, Karen Dykstra, Anil Sabharwal, Christian Smith, Steve Sordello). Nine directors stand for election at the 1 December 2026 annual meeting.
- **Completed leadership transition.** The unusual co-CEO structure ended in September 2024; Cannon-Brookes is now sole CEO, with Farquhar remaining as a director/co-chair figure holding Class B stock.
- **No restatement, no material weakness, no auditor dispute.** CEO/CFO certifications in the Q1 FY27 10-Q are clean and unqualified.

**The disqualifying caveat — control concentration:**
- **Dual-class structure with founders holding >88% of voting power against ~43% of economic interest.** Minority shareholders have **no practical ability to influence board composition, compensation, or strategic direction.** The independent board is, in effect, independent by founder consent rather than by shareholder check. This is the single most important governance fact about TEAM and it caps how much credit the independence metrics deserve.
- **Elevated senior turnover in 2026.** A new CFO (James Chuong, ex-CFO of LinkedIn, joined from March 2026) and a **replaced Chief Technology Officer** (announced alongside the March restructuring), on top of 1,600 departures. CFO and CTO transitions inside a single fiscal year, during a strategy pivot, are a classic internal-control and execution risk vector. The new CFO has not yet been tested through a full annual audit cycle.

---

## 2. Regulatory Risk Summary: **Low-to-Moderate (clean on paper, exposed in practice)**

| Item | Status |
|---|---|
| SEC enforcement / DOJ actions | **None.** EDGAR full-text search for enforcement actions referencing TEAM returned zero hits. |
| Active securities class action | **None identified post-2026.** The known securities class action dates to Feb 2023 (cloud-migration disclosures). No new filing surfaced despite the Feb 2026 50% drawdown — but this remains a live risk given the Nov 2026 guidance-driven drop. |
| GDPR / privacy fines | **No enforcement action found.** Atlassian publishes GDPR/DPA commitments; DPA updated effective 17 Aug 2026. |
| Pending approvals | No material FDA/FCC-type gating approvals (not applicable to model). |
| Pricing/consumer-protection exposure | **Rising.** An October 2026 cloud price increase plus **usage-based pricing for AI capabilities effective 3 December 2026** create billing-dispute, contract-renegotiation, and unfair-terms exposure across a very large SMB base — the type of change that attracts regulator and class-action attention. |

**Assessment:** No smoking gun, but note that the *absence* of enforcement is not evidence of low risk in software — Atlassian's largest regulatory exposure is **contractual and privacy-based**, not enforcement-based, and the December AI metering change is a fresh, untested irritant.

---

## 3. Insider Activity Analysis: **Net selling — unambiguously one-directional**

- **~50 Form 4 filings in the trailing twelve months.** Not a single open-market **purchase** by any officer or director was identified. Activity is **100% sales**.
- Sales are conducted under **Rule 10b5-1 plans** (adopted February 2025, per filing disclosures), predominantly by **CEO Mike Cannon-Brookes and trusts/entities affiliated with him**, plus other insiders. Typical size: 7,665–7,765 Class A shares per transaction (~$0.7M–$1.55M each).
- **Price range of executions spans $93 to $167+**, i.e. selling continued mechanically through the crash and the recovery — consistent with a programmatic plan, which mitigates the *information* interpretation.
- **However, the timing is uncomfortable:** Form 4s cluster on **13 Oct 2026, 22 Sept 2026, 31 Aug 2026, 17–20 Aug 2026** — with the October filing landing roughly one week before the 22 Oct all-time high of $229.96 and three weeks before a **-16% single-day gap** and a subsequent 33% decline. Insiders were liquidating into strength immediately ahead of a sharp reversal.
- Post-transaction, Cannon-Brookes' reported holding is roughly **278,605 shares (~$52M)** — still meaningfully aligned, but small relative to a founder's headline economic stake, and the trend line is monotonic selling.

**Verdict:** No evidence of improper trading (plans are pre-scheduled and disclosed), but **sentiment read is negative**: the only informed money moving is moving out. There is no insider "vote of confidence" to offset the guidance-driven selloff. **This is a red flag for escalation, at moderate severity.**

---

## 4. Top Operational Risks

1. **Systemic product security vulnerability — the most material operational risk at TEAM.** **CVE-2026-21589 (CVSS 9.3)** is an unauthenticated path-traversal / arbitrary file read affecting Jira, Confluence, Bitbucket and other Data Center & Server products, escalating to credential/SAML compromise where Crowd SSO is used. It was **exploited within hours of disclosure**, with threat-intel tracking ~89 attacking IPs within days; CERT-EU issued advisory 2026-015. Critically, this is **not a one-off**: the 20 Oct 2026 Security Bulletin lists **162 high-severity and 14 critical third-party vulnerabilities**, and the 15 Sept 2026 bulletin lists **144 high and 17 critical**. A monthly cadence of 150+ high-severity findings in the flagship codebase is a persistent structural weakness — and it strikes directly at the trust proposition of a company selling enterprise collaboration and developer tooling to security-conscious buyers.

2. **Business-model disruption risk tied to AI and seat-based pricing.** The February 2026 "SaaSpocalypse" — an AI-agent-driven ~$2T software de-rating — halved TEAM **despite its fastest revenue growth in six quarters**. The market's question is whether autonomous coding agents compress per-seat demand. TEAM's answer (usage-based AI pricing from 3 Dec 2026, Teamwork Collection bundling, Rovo adoption) is unproven at scale and creates **revenue-model transition risk** layered on top of the already-executing cloud migration. Two simultaneous pricing-model migrations is an operational strain.

3. **Execution risk from simultaneous restructuring and leadership rebuild.** March 2026: **~1,600 roles cut (~10% of workforce)** explicitly to "self-fund" AI investment, alongside a **CTO replacement**; new CFO arriving in the same window. Cutting 10% of headcount while asking the remaining organisation to re-platform pricing, ship AI products, and defend against security exploits is a demanding combination. Attrition, morale, and institutional-knowledge loss in the security and platform engineering functions are the specific concerns — particularly given risk #1.

*Additional:* **Key-person and dual-founder dependency.** Strategy, brand, and public narrative are heavily concentrated in Cannon-Brookes, who is also the principal insider seller. Concentration of both authority and reputational capital in one individual is a genuine continuity exposure.

---

## 5. Reputational Risk Assessment: **Elevated**

- **The layoff narrative is damaging.** The March 2026 cut of 1,600 staff was publicly framed as an **AI-driven restructuring** and announced by video by the CEO — coverage included "The 'SaaSpocalypse' just claimed 1,600 Atlassian jobs" and "'Devastating blow': Atlassian lays off 1,600 workers." Framing mass redundancy as AI-enablement invites durable employer-brand damage and political/regulatory attention (Australian and EU works-council sensitivity is relevant given the Sydney domicile).
- **Security reputation is the sharper edge.** A CVSS 9.3 pre-auth file-read in Jira/Confluence, exploited in hours across a customer base of hundreds of thousands of organisations, is precisely the headline that erodes enterprise trust. Recurring critical bulletins normalise the risk in buyers' minds and strengthen the hand of procurement and of competitors (ServiceNow, GitLab, monday.com, and AI-native challengers).
- **Customer-relations friction is rising:** October 2026 cloud price increase plus AI usage metering from December 2026, on top of a forced cloud migration. Community forums already carry GDPR-compliance complaints. This is a classic compounding of price + migration + trust issues.
- **Sentiment is fragile and reflexive.** A stock that moves +35.3% on 7 Aug and -16% on 5 Nov, on fundamentally similar "beat and raise" results, indicates a market that no longer trusts guidance framing. Sell-side remains constructive (29 brokerages, average target ~$213, "Moderate Buy"), which sets up further disappointment risk.

---

## 6. Overall Non-Financial Risk Rating: **HIGH**

**Rationale:** This is **not** an integrity problem — there are no fraud indicators, no whistleblower signals, no restatement, no material weakness, no SEC or DOJ action, and the board has a genuinely independent chair. The High rating is driven by **operational fragility concentrated in product security**, compounded by a **simultaneous restructuring + CTO/CFO turnover + dual pricing-model migration**, an **unhedged AI disruption narrative**, and a **one-directional insider selling pattern with zero insider buying** into a 33% drawdown. Governance is "Adequate" only on form; **>88% founder voting control against ~43% economic interest** means external shareholders cannot correct course if execution falters.

**Component ratings:** Governance — Adequate (structurally constrained) | Regulatory — Low/Moderate | Operational — High | Reputational — Elevated | Fraud/Integrity — Low (no indicators) | Key-person — High

---

## 7. Red Flags Requiring Escalation

1. **Insider selling into the 52-week high with no offsetting purchases.** October 2026 Form 4s preceded the 22 Oct peak and the subsequent -33% by days. Escalate for a 10b5-1 plan-terms review (adoption date, modification history, cooling-off compliance) and for consideration of a disclosure-quality question around the Nov 5 guidance.
2. **CVE-2026-21589 (CVSS 9.3) exploited in hours, plus 150+ high-severity vulns per monthly bulletin.** Escalate as a thesis-relevant operational risk: quantify customer exposure to Data Center/Server install base and monitor for follow-on breach disclosures, customer attrition, or insurance/litigation events.
3. **CTO replaced and CFO replaced within the same fiscal year, alongside a 10% RIF.** Escalate as an internal-control and execution watch item; request evidence of disclosure-control continuity through the FY27 10-K cycle.
4. **>88% founder voting control vs ~43% economic ownership.** Escalate as a permanent structural discount factor and a limit on all minority-shareholder remedies.
5. **Guidance credibility gap.** A "beat and raise" quarter producing a -16% move, four months after a +35% one-day move, indicates the market has lost confidence in management's forward framing. Monitor for securities-litigation triggers following the Feb 2026 and Nov 2026 drawdowns.

---

**Information gaps (disclosed):** No 10-K risk-factor text or DEF 14A primary document was retrievable via the filing tool (only the 10-Q certification excerpt and third-party proxy summaries); board committee composition, exact director independence determinations, related-party transactions, and precise aggregate insider dollar volumes could not be independently verified from primary filings. Form 4 tool returned filing metadata only, not transaction line items. Some news feeds conflated TEAM with Team, Inc. (NYSE: TISI) — those items were excluded. Conclusions above rest on the 10-Q, the governance page, price data, and corroborated press/threat-intelligence reporting.

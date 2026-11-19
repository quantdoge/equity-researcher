# Nonfin Risk Analyst

- Symbol: OKTA
- Elapsed: 57.1s

---
# OKTA — Non-Financial Risk Assessment
**Okta, Inc. | Technology / Software–Infrastructure (Identity & Access Management) | San Francisco, CA | ~$32.7B mkt cap | 6,366 FTE | CIK 0001660134**
*Assessment date: ~Nov 25, 2026. Data note: SEC direct fetches and the 10-K/10-Q/DEF 14A tools returned errors (no filing text retrievable); risk-factor and insider detail below is drawn from third-party filing aggregators and press. Peer multiple work not run — this is a risk-only memo.*

---

## 1. Governance Quality Rating: **ADEQUATE (with two notable blemishes)**

**Positives**
- **Lead Independent Director exists and is functioning** — Jeff Epstein served as LID from June 2024 until March 2026, when David Schellhase was appointed. Regular rotation, not a vacancy.
- **Board refreshment is active, not stagnant**: Helen Riley (CFO/COO of X) appointed Sept 14/18, 2026, replacing departing Class I director Emilie Choi; Rob Bernshteyn and Paul Sagan added as industry veterans. Recent additions bring operator and cyber/government-domain expertise.
- **Mature shareholder-mechanisms**: annual say-on-pay, equity-plan amendments submitted to a vote (2026 meeting: equity plan amendment passed 144.1M for vs 59.9M against), $1B buyback authorized with $921M remaining — capital return discipline is new for this name.
- **Dual-class structure exists but is not control-conferring**: Class B carries 10 votes but is a small minority of shares; founders do not hold voting control. This is materially better than a founder-controlled sunset structure.

**Blemishes**
- **CEO/Chair duality**: Todd McKinnon is both CEO and Chairperson; co-founder Frederic Kerrest is Vice Chairperson. Two founders occupy the two most senior board roles. Mitigated by the LID, but board independence from management is structurally weaker than peer best practice.
- **~29% shareholder opposition to the equity-plan amendment** (59.9M against) is a real dilution/compensation signal. Combined with heavy SBC in a company that only recently turned GAAP-profitable (FY26 net income $235M vs $28M FY25 vs –$355M FY24), compensation alignment is the weakest governance pillar.
- **Director turnover at a sensitive moment**: Choi's departure and the LID transition both landed in 2026, the same year as the January identity-attack wave and the S&P 500 entry (Nov 4, 2026). Not alarming individually; worth monitoring for loss of institutional memory on the audit/cyber side.

---

## 2. Regulatory Risk Summary: **LOW–MODERATE (no active enforcement; elevated *exposure*, not activity)**

- **No SEC enforcement actions returned** in EDGAR full-text search for OKTA. No DOJ, no FTC action, no open investigation identified.
- **Litigation history is resolved, not live**: the *In re Okta, Inc. Securities Litigation* (Sections 10(b)/20(a), tied to the 2022 Lapsus$ disclosure) settled for **$60M**. This establishes a precedent that Okta's breach disclosures are a securities-litigation magnet — each new incident carries re-litigation tail risk.
- **Privacy/regulatory exposure is rising, by the company's own admission**: the FY2026 10-K reworded its privacy risk factor to state explicitly that Okta *processes personal data on behalf of customers and is itself subject to global data-protection regimes* (GDPR, CCPA, sector rules). That is a meaningful change in framing — from "our vendors might fail" to "we are a regulated data processor." For an IAM provider with 20,000+ customers, one incident can trigger multi-jurisdiction notification, GDPR Article 83 fines, and contractual indemnity at once.
- **Regulatory change risk that hits revenue**: the FY26 10-K added **trade policy, export restrictions and sanctions** to its economic-risk language, and reframed AI risk as "benefits may not arrive cost-effectively or on time" (removing specific EU/U.S. regulation examples). International revenue *declined* from 21% to 20% of total — a soft signal on non-U.S. execution amid fragmenting data-residency rules.
- **Public-sector concentration risk (policy, not enforcement)**: Okta is a significant U.S. federal/state supplier (FedRAMP, ICAM programs, DoD/DHS/VA). DOGE-era procurement scrutiny and continuing-resolution volatility create abrupt, headline-driven revenue risk that is regulatory in nature and unhedgeable.
- **Pending approvals**: none material identified (no FDA/FCC-type gates). S&P 500 inclusion (eff. Nov 4, 2026) adds index-flow but also raises the disclosure/scrutiny bar.

---

## 3. Insider Activity Analysis: **NET SELLING — persistent, programmatic, and unaccompanied by any buying**

**CEO Todd McKinnon — open-market sales (last 12 months and cycle):**

| Transaction date | Shares | Avg price | Value |
|---|---|---|---|
| 2026-09-22 | 48,822 | $193.48 | **$9.45M** |
| 2026-07-08 | 68,936 | $146.62 | **$10.11M** |
| 2026-03-23 | 11,263 | $81.01 | $0.91M |
| 2025-12-22 | 11,286 | $90.96 | $1.03M |
| 2025-09-22 | 31,968 | $92.33 | $2.95M |
| 2025-07-21 | 31,592 | $95.30 | $3.01M |
| 2025-03-20 | 234,289 | $113.27 | $26.54M |

- **Trailing-12-month CEO sales ≈ $21.5M, zero open-market purchases.** Sale cadence (quarterly, near-identical share counts in some periods, plus RSU/option exercise rows at $0 conversion price) is consistent with **Rule 10b5-1 pre-scheduled plans** — this is *not* evidence of opportunistic dumping on inside information.
- **But the signal is still negative in direction**: the CEO sold into strength ($193 in Sept, $146 in July) and did **not buy a single share during the April 2026 drawdown to $63** (a –33% peak-to-trough move from January's $94). Insiders who believe their stock is mispriced typically buy such dips; none did.
- **Insider ownership remains large and aligned**: McKinnon still holds ~6.9M shares (~$1.35B notional). This is a "diversifying founder," not a "heading-for-the-exits founder."
- **June 2026 Form 4 cluster** (22 filings dated 2026-06-22) is consistent with the annual equity grant/vesting cycle, not discretionary activity. Broad executive selling across the group, no buys anywhere in the dataset.
- **No 13D/activist filings, no insider purchases** in the review window.

**Verdict: negative but explainable. Do not treat as a fraud/confidence red flag; do treat as a mild sentiment headwind and a reason to discount management's own optimism.**

---

## 4. Top Operational Risks

- **Okta is a single point of failure for its customers — availability failures are existential, not inconvenient.** 2026 incident log: a **July 24** service disruption (timeouts/login failures, root cause a third-party incident, ~30 min), a **Sept 23** degradation (~6 hours of elevated error reports), and an **Oct 21** degradation that one tracker logged as persisting up to **15 days**. When your product is the front door to every application, downtime equals customer downtime — driving SLA credits, CIO escalation, and, critically, *architectural* diversification toward Microsoft Entra/Hypr. Availability is the #1 churn vector here.
- **Okta is a named, permanent target of sophisticated threat actors — and the soft target is the human layer around the product.** The **January 2026 ShinyHunters voice-phishing (vishing) campaign** compromised Okta SSO credentials across **100+ organizations**, with data leaked and the Okta brand on every headline; Okta's position ("compromise of customer accounts, not of Okta's infrastructure") is legally defensible and reputationally useless. This follows **Lapsus$ (Jan 2022)** and the **Oct 2023 support case-management breach** (initially scoped to 134 customers, later confirmed to affect *all* support users). Three separate eras of the same failure mode — **the support/helpdesk/identity-verification perimeter** — is a systemic control weakness, not bad luck. Recurrence probability is high.
- **Platform expansion (AI-agent identity, Cross App Access) is inflating the attack surface faster than the trust narrative can absorb.** Okta is staking its growth story on securing non-human identities (AI agents, M2M, TrueFoundry/XAA ecosystem). Agents authenticated by long-lived static API keys are precisely the credential class attackers favor, and Okta is now the policy enforcement point for them. Simultaneously, Okta carries **cloud-infrastructure concentration risk** (hyperscaler dependency) and reliance on third-party providers — the July outage was explicitly third-party-caused. Add **key-person dependency on McKinnon and co-founder Kerrest** (the AI-era repositioning is personally branded to McKinnon), and operational fragility is underappreciated relative to the "mission-critical infrastructure" valuation the stock now commands.

---

## 5. Reputational Risk Assessment: **MODERATE–HIGH (structurally impaired by the business model)**

- **The brand is "trust," so negative press is not a marketing cost — it is a valuation input.** January 2026's ShinyHunters coverage ran in mainstream security press with headlines naming Okta, not the victims. Okta's "not our breach" defense has now been deployed three times (2022, 2023, 2026) and is losing credibility with practitioners; sysadmin/Reddit sentiment has been consistently skeptical since 2023.
- **Market has shown it will punish and then forgive**: OKTA fell from ~$94 (Jan 2026) to **$63 (Apr 10, 2026)** — a ~33% drawdown through the January attack wave and a soft guide — then re-rated to **$230 (Oct)** on AI/identity momentum and S&P 500 inclusion, closing recently at **$195.61**. Implication: reputational damage is *episodic and recoverable*, but each episode produces a violent, tradeable drawdown. Beta is low (0.73) but event-risk is not.
- **Competitive weaponization**: Microsoft Entra bundles identity into M365; every Okta incident is a competitive sales cycle. Zscaler/SentinelOne/CrowdStrike comparisons dominate coverage — Okta is judged on growth optics against better-growing peers, so any trust shock compounds a relative-value discount.
- **Positives**: customer count >20,000 and still growing; Okta is *gaining* from identity consolidation and AI-agent security; S&P 500 membership and institutional accumulation (Eurizon +56%, International Assets +442% in Q3) indicate the buy-side has moved past the January incident.
- **ESG/sustainability**: low controversy exposure; note the 10-K *narrowed* its sustainability risk factor to compliance/cost, dropping reputational-impact language — a mild signal management views ESG reputational risk as declining.

---

## 6. Overall Non-Financial Risk Rating: **MODERATE**

**Rationale**: Governance is adequate and improving (real LID, active refreshment, no founder voting control, no related-party red flags); there is **no active regulatory enforcement, no restatement, no whistleblower complaint, and no fraud indicator**; insiders are aligned by ownership if not by purchases. The rating is held at Moderate rather than Low by a single concentrated factor: **Okta's recurrent inability to defend the human/support perimeter around its own product**, which has produced three incidents in five years, a $60M securities settlement, a live January 2026 extortion campaign, and repeated availability failures — all in a business where trust *is* the product. This is a structural, not a fixable-quarterly, risk.

---

## 7. Red Flags Requiring Escalation

1. **Escalate (High): Repeat breach archetype.** Jan 2022, Oct 2023, Jan 2026 all exploited the same vector class — helpdesk/support/vishing. Three iterations is a control-design failure, not operational variance. Request the Audit Committee's cyber-reporting cadence and whether the 2026 vishing campaign was board-reported under Item 1.05 criteria.
2. **Monitor (Medium): CEO/Chair duality + founder concentration** (McKinnon Chair & CEO; Kerrest Vice Chair), with ~29% shareholder rejection of the 2026 equity plan. Watch for say-on-pay support dropping below 70% in 2027 — that would make governance an active thesis risk.
3. **Monitor (Medium): CEO sold ~$21.5M in the last 12 months with zero purchases, including no buy at the April $63 low.** Programmatic and pre-planned, but confirm 10b5-1 adoption dates against the January 2026 incident disclosure timeline — if any plan was adopted or modified within 30 days of a breach disclosure, escalate immediately.
4. **Monitor (Medium): Availability incidents in July, September and October 2026**, including a third-party-rooted outage and one tracker-logged 15-day degradation. Validate against official status.okta.com history; if material credits were triggered, expect disclosure and churn commentary on the **Dec 1, 2026** Q3 FY27 call.
5. **Watch (Low): Director churn** — Choi out / Riley in, plus LID rotation (Epstein → Schellhase) in the same year. Confirm no departures were policy disagreements (8-K language "Departure of Director" is neutral).
6. **Note (Low): No fraud indicators detected** — no restatement, no auditor change, no short-seller report, no SEC/DOJ inquiry in EDGAR full-text. Absence of evidence here is genuinely informative because Okta's disclosure history would make irregularities highly visible.

---
**Data gaps disclosed**: 10-K/10-Q/DEF 14A text unavailable via tools (SEC 403 / tool errors); FY26 risk-factor analysis sourced from a third-party summary of the 10-K filed 2026-03-05 (58 risk factors, 1 new, 12 substantially reworded). Insider detail from a Form 4 aggregator, not raw filings. No peer governance comparison performed. No cross-check of the "15-day" outage claim against Okta's own status page.

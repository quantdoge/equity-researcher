# Nonfin Risk Analyst

- Symbol: CRWD
- Elapsed: 51.2s

---
# CROWDSTRIKE HOLDINGS (CRWD) — Non-Financial Risk Assessment
*As of 23 November 2026 | Price $208.97, market cap ~$214B, beta 1.15, ~11,700 FTE*

**Critical context:** On 22–23 November 2026, CRWD signed a **$43.9B all-stock acquisition of Zscaler (ZS)** (1.135 CRWD shares per ZS share; CRWD holders retain ~84.1% of the combined company; close targeted H2 FY2028). CRWD fell 8.9% on the announcement ($229.44 → $208.97, 42M shares vs. ~8M normal) and sits ~25% below its 6 October high of $278.86. This transaction now dominates the non-financial risk profile.

---

## 1. Governance Quality Rating: **ADEQUATE**

**Positives**
- **No CEO/Chair duality:** Gerhard Watzinger serves as independent Chair; founder-CEO George Kurtz is a director but not Chair. Board of **9 directors, 7 independent** (2026 proxy, filed 5 May 2026); committee leadership held by independent directors (Roxanne Austin, Laura Schumacher).
- **Pay is structurally aligned, not cosy:** FY2026 CEO compensation of **$247.6M** was **98% equity** ($242.1M in stock awards, including a December 2025 TSR-linked PSU with a $289.9M maximum grant-date value). PSU metrics for all NEOs used revenue and non-GAAP EPS. No options-heavy or guaranteed-bonus structure visible.
- **Section 302 certifications clean** in the Q3 FY2027 10-Q (no disclosed material weakness or fraud exception in the certification language).

**Concerns**
- **Compensation magnitude and optics:** CEO pay **+603% YoY** ($35.2M → $247.6M), **CEO-to-median pay ratio 1,391:1** (median $178,015), plus **$2.46M of personal aircraft costs** in "all other compensation." Expect negative proxy-advisor and ESG-rating attention at the 2027 AGM, and a plausible "against say-on-pay" recommendation.
- **Founder concentration:** Kurtz is co-founder, CEO, public face and chief architect of the Zscaler deal — thin separation between strategic conviction and board oversight of a bet equal to ~20% of market cap.
- **Deal-related governance complexity:** Zscaler's Jay Chaudhry (~34% holder, locked up to vote yes) is to **join the CRWD board while continuing to run Zscaler** through close — a structural conflict and related-party-sensitive arrangement.
- **Board refresh / leadership depth:** former CSO Shawn Henry retired 31 March 2025 with no equity/incentive comp in FY2026 — the highest-profile security-credibility departure; board and bench depth beyond the founder should be monitored.

## 2. Regulatory Risk Summary

| Matter | Status | Assessment |
|---|---|---|
| **DOJ criminal + civil probe** — Carahsoft distributor transactions (~$32M IRS-related deal), executive knowledge of deals | **CLOSED, no charges** (notified parties July 2026; reported 25 Sept 2026) | Material de-risking event |
| **SEC investigation** (same accounting/distributor matter) | **Status not publicly confirmed as closed** — reporting explicitly notes uncertainty | **Residual overhang — top regulatory flag** |
| **EDGAR full-text SEC enforcement search for CRWD** | Returned **zero actions** | No formal SEC enforcement proceeding naming the company |
| **Securities class action** (July 2024 outage; W.D. Tex.; NY State Comptroller lead plaintiff) | **Dismissed 12 January 2026** | Cleared |
| **Delta Air Lines v. CrowdStrike** (Fulton County, GA; $500M claim) | Bulk dismissed 16 May 2025 (fraud, intentional misrepresentation, product liability, deceptive practices). Surviving: **negligence and computer trespass**. Damages expected to be **contractually capped in the single-digit millions** under the Subscription Services Agreement | Low financial exposure, but **discovery precedent risk** |
| **Zscaler merger approvals** | Zscaler shareholder vote; **HSR/antitrust filings** (deadline window into January 2027); outside date extends toward FY2028; **$1.4B reverse termination fee payable only by Zscaler** | Antitrust is the main gating item; combined endpoint + SSE/zero-trust share will likely draw a Second Request-level look |
| **Data protection / sovereignty** | No GDPR/CCPA fines identified. Exposure is as a processor for EU/UK/Gov customers (CLOUD Act, EU data residency, FedRAMP) | Contained but structurally rising |

## 3. Insider Activity Analysis: **Heavy net selling, zero buying**

- **CEO George Kurtz: $228.3M sold across 883 sale transactions in 50 Form 4s during 2026; $0 of open-market purchases.** Sales are near-weekly, typically $4–6M tranches, with two larger clusters (≈$11.2M on 4 Nov; ≈$19.5M on 22 Sept).
- **Mitigant:** sales executed under a **Rule 10b5-1 plan adopted 16 January 2026**, i.e., pre-scheduled diversification rather than discretionary opportunism — the plan predates the merger negotiation window.
- **Flag:** selling continued on 13, 17 and 19 November 2026 and a **$4.8M sale was filed 23 November, the day of the deal announcement**, i.e., executed days before signing and into a merger that cut the stock ~9%. Legally insulated by the plan, but optically poor and a likely plaintiff/shareholder-criticism vector.
- **Visibility gap:** numerous other filing agents (directors/other officers) are present in the Form 4 stream, but aggregate director/officer data outside the CEO was not retrievable with available tooling. **No evidence of insider open-market buying around the deal or the October drawdown** — an absence of conviction buying at a 25% discount is itself a soft negative.

## 4. Top Operational Risks

1. **Zscaler integration execution ($43.9B, ~7–9 months to close plus multi-year integration).** Two direct competitors with overlapping zero-trust/cloud-security portfolios must merge sales forces, channel programs and product roadmaps while the deal is in regulatory limbo — a window in which competitors will poach accounts and CRWD's own sellers face uncertainty. Management's **$1B revenue-synergy** claim is unproven; dilution (~15.9% new shares) and integration of two distinct engineering cultures are the key failure modes. Chaudhry running Zscaler while sitting on the CRWD board blurs accountability during integration.
2. **Release-engineering / content-update tail risk (the July 2024 failure mode).** A single faulty Rapid Response Content update to the Falcon sensor disabled >8M Windows devices and grounded airlines, banks and retailers. Remediation (staged deployment, customer-controlled update policies, ring-based rollout) is asserted but has not been independently validated; **another mass-update incident remains the single largest low-probability/high-severity operational risk**, with knock-on contractual, insurance and reputational consequences.
3. **Key-person and talent concentration.** Strategy, security credibility and the entire M&A thesis run through founder-CEO Kurtz; the CSO seat has already turned over once. The deal simultaneously raises retention risk in engineering, threat-intelligence and enterprise sales — precisely the people Zscaler is being bought for — and creates duplicate-role attrition. Secondary: infrastructure dependency on AWS and Windows/Microsoft ecosystems, and customer-side concentration risk from single-agent architecture.

## 5. Reputational Risk Assessment: **Recovered, but newly exposed**

- **2024 outage legacy has largely been rehabilitated:** CRWD was named a **Customers' Choice in the 2026 Gartner Peer Insights** voice-of-the-customer report (most 5-star reviews in category), the securities class action was dismissed, and the Delta case has been narrowed to a capped contract dispute. No 2026 product-caused outage, recall or consumer backlash was identified.
- **New reputational vectors are financial and governance-led, not product-led:** (i) the "overpaying/dilution" narrative around Zscaler (sell-side framing of "familiar concerns about dilution, execution risk and paying too much," Palo Alto/CyberArk precedent comparisons); (ii) a **$247.6M CEO pay package and 1,391:1 pay ratio** that is unusually easy to headline; (iii) **$228M of continuous CEO selling with no insider buying**; (iv) an SEC file that is not publicly closed while the DOJ file is.
- **ESG/ratings risk:** governance pillar will likely weaken on pay magnitude, board independence steady at 7/9, and the deal adds a large-holder director with a concurrent operating role.

## 6. Overall Non-Financial Risk Rating: **MODERATE** *(would be **HIGH** if the SEC matter reopens or a second Falcon update incident occurs)*

**Rationale:** The legacy legal stack has genuinely cleared — DOJ closed, securities class action dismissed, Delta narrowed and capped, no SEC enforcement action on file, no fines. Governance is independent-chaired with majority-independent board and equity-heavy pay. Against that: an unresolved SEC file, an extraordinarily large all-stock integration with asymmetric deal protection, unresolved antitrust timing, a $247.6M CEO pay headline, and one-way insider flow. In aggregate, **Moderate with a distinct negative trajectory into the deal close.**

## 7. Red Flags Requiring Escalation

1. **SEC investigation not publicly confirmed closed** (DOJ closed July 2026). Verify current language in "Legal Proceedings" of the Q3 FY2027 10-Q and the FY2027 10-K. Any SEC subpoena escalation or Wells notice is a re-rating event.
2. **CEO 10b5-1 sales continuing into the merger signing window** (13–19 Nov, plus a 23 Nov filing). Pre-cleared, but a live optics/shareholder-suit vector — escalate to legal-news monitoring.
3. **Asymmetric deal protection:** a $1.4B reverse termination fee payable *only by Zscaler* means CRWD has effectively no walk-away economics — the board has pre-committed shareholders to the deal at 34% premium regardless of antitrust duration or deterioration in ZS performance.
4. **Compensation:** $247.6M CEO pay, +603% YoY, 1,391:1 ratio, $2.46M aircraft benefit — anticipate adverse say-on-pay vote and proxy-advisor pressure; watch for 2027 AGM governance concessions.
5. **Delta negligence/computer trespass claims surviving** — while dollars are capped in the single-digit millions, discovery into release QA processes is a template risk for other enterprise customers disputing contractual liability caps.
6. **Chaudhry board seat + 34% lock-up:** a board member who is simultaneously the acquired company's operating CEO during integration is a conflict-management item for the Nominating/Governance committee.

---

**Evidence gaps (honest disclosure):** The 10-K and DEF 14A were not retrievable through the filing-text tool ("No 10-K/DEF 14A found"); governance and compensation figures above are sourced from the 2026 proxy as reported by third-party summarizers and should be re-verified against the SEC-filed DEF 14A (filed 5 May 2026) before publication. The merger 8-K could not be fetched (403), so termination-fee and closing-condition terms are sourced from deal coverage, not the primary filing. Aggregate director/officer insider data beyond the CEO was unavailable, so the net-selling conclusion is CEO-specific and should not be extrapolated to the full insider cohort.

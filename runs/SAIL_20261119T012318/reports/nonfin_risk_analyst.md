# Nonfin Risk Analyst

- Symbol: SAIL
- Elapsed: 51.2s

---
## Non-Financial Risk Assessment — SailPoint, Inc. (NASDAQ: SAIL)

**Context:** Identity-security software; re-IPO'd Feb 13, 2025 at $23.00 after Thoma Bravo's 2022 take-private ($65.25/share, $6.9B). Market cap ~$12.7B; price ~$22.25; beta 2.08; 3,229 employees. Stock is roughly flat vs. IPO but has traveled $25.70 → $10.49 (Apr 10, 2026) → $22.39 (Oct 27, 2026) — a 59% peak-to-trough decline and a 113% recovery in six months.

---

### 1. Governance Quality Rating: **WEAK**

| Evidence | Assessment |
|---|---|
| **Thoma Bravo owns ~86.2% of common stock** post-IPO (424B4) | Controller status. Public float is a minority with no practical voting influence. |
| **"Controlled company" status** | Exempt from Nasdaq requirements for a majority-independent board and fully independent compensation/nominating committees. The governance guidelines state a majority *shall* be independent "provided..." — a carve-out consistent with the exemption. |
| **Founder-CEO Mark McClain** (co-founder 2005; CEO through the 2017–2022 public era and since Aug 2022) | Concentrated executive power; no disclosed independent chair. Founder-CEO + controlling sponsor is the least-checked governance configuration in the market. |
| **Director resignation:** Nabil Hamade resigned from the board **June 8, 2026** (8-K filed June 12, 2026) | Timing is striking — **one day before** the June 9 guidance shock. No stated reason in the filing. Likely a sponsor-designated seat rotation, but this requires confirmation from the board or company. |
| **Audit/controls:** FY2026 (Jan 31, 2026 FYE) 10-K shows unqualified EY opinions on both financials and ICFR; **no material weakness, no restatement** (per secondary summary — see data gaps) | Genuine mitigant. Note the predecessor 2017 IPO entity disclosed a material weakness at IPO; the current entity has not repeated that. |
| **Sponsor time-horizon misalignment** | Thoma Bravo entered at $65.25 (2022) vs. $22 today. A PE holder ~4 years post-entry with 86% control has strong incentive to distribute/exit, creating supply overhang and pressure for short-horizon "2029 plan" storytelling ($2.1B ARR target). |

**Verdict: Weak.** Not because of ethical failure, but because checks and balances are structurally absent. Independent directors cannot outvote an 86% holder, and the CEO is a founder running a company he has already run once.

---

### 2. Regulatory Risk Summary

- **SEC enforcement actions: NONE.** EDGAR full-text search for enforcement actions mentioning SAIL returned zero results. This is a clean sheet and a meaningful mitigant.
- **Securities-fraud investigations — MULTIPLE, ACTIVE.** Following the June 9, 2026 (~11.5%) drop on weak forward guidance, at least four firms are investigating: **Pomerantz**, **Levi & Korsinsky** (June 11–12), **Schall Law** (June 15), and **Kuehn Law** (Sept 30, 2026). Stated theories: materially misleading statements about "growth trajectory and near-term" outlook and guidance; Kuehn's probe targets whether officers/directors **breached fiduciary duties** (typically a books-and-records/derivative precursor). These are **investigations, not filed complaints** — I found no docketed 10b-5 class action. Escalate but don't over-weight.
- **Regulatory posture (product):** As an identity-governance vendor, SailPoint sits inside customers' GDPR/CCPA/HIPAA compliance perimeter and is increasingly exposed to **EU AI Act** obligations around AI-agent identity controls — net demand tailwind, but it converts into vendor-liability exposure if controls fail.
- **Pending approvals:** None material identified (no FDA/FCC-type gate).

---

### 3. Insider Activity Analysis — **100% selling, 0% buying (12 months)**

Form 4 cadence is **monthly and mechanical** (Jan 8, Mar 6, Apr 9–10, Jun 2–5, Jul 9, Aug 14, Oct 8–9, Oct 28, 2026), consistent with 10b5-1/RSU-vest programs rather than discretionary conviction.

Disclosed October 2026 cluster (all sales, at or below IPO price):
- **CEO Mark McClain:** 103,893 sh @ $20.36 (Oct 6, $2.12M) + 115,356 sh @ $19.71 (Oct 7, $2.27M) ≈ **$4.39M**; retains 7,874,621 sh (~$156M) — still heavily aligned.
- **CFO Brian Carolan:** 52,822 sh @ $19.71 = **$1.04M**; retains 1,626,381 sh.
- **President Matt Mills:** 42,442 sh @ $19.71 = **$0.84M**; retains 2,292,872 sh.

Disclosed cluster total ≈ **$6.3M** in two sessions. Entity filings on June 2/5, 2026 (multiple non-individual CIKs) are consistent with **sponsor-affiliated distributions** — unconfirmed.

**Read:** Net direction is unambiguously negative — no open-market purchases by any insider in the period. Mitigants: selling is programmatic, executives retain large residual stakes, and October sales occurred at $19.71–20.36, i.e., **below the $23 IPO price** — a poor signal on management's own view of near-term value, though also what vesting calendars dictate.

---

### 4. Top Operational Risks

1. **Competitive disintermediation by Microsoft (and Okta).** Microsoft Entra ID Governance is priced as a low-cost per-user add-on (~£5.40–$6/user/month bundle) versus SailPoint's quote-only enterprise pricing. Okta nearly doubled in 2026 while SAIL trades below its IPO price. Third-party commentary (r/IAM, Zluri, Lumos) shows active cost-driven displacement in mid-market. Bundling, not features, is the threat.
2. **Key-person dependency on founder-CEO McClain.** Nearly 35 years' tenure, founder of the 2005 business, steered both public eras. No disclosed succession bench or COO-level heir. An unplanned departure would hit both strategy continuity and the AI-agent narrative he personally fronts.
3. **Own-estate security and platform-transition execution.** On **April 20, 2026 SailPoint detected unauthorized access to a subset of its GitHub repositories**, via a third-party application vulnerability; SEC-disclosed (8-K, reported May 11, 2026), contained, with **no customer production/staging data accessed and no service interruption**. Contained — but for a company whose entire value proposition is "we secure identities," a second incident touching customer data would be existential, not merely costly. Concurrently, the IdentityIQ 9.0 (on-prem) → Identity Security Cloud transition and partner dependency (Radiant Logic integration) create renewal/channel execution risk.

---

### 5. Reputational Risk Assessment — **Moderate**

- **Negatives:** a cluster of securities-fraud law-firm alerts (retail-investor-visible); persistent sub-IPO share price that media explicitly frame against Okta ("something about that gap demands an explanation"); pricing-backlash commentary from practitioners; the repo-breach headline in security trade press — the one audience that matters most for this buyer.
- **Positives:** strong product narrative at Navigate 2026 (Autonomous Agents, A-ISPM, runtime controls); the widely-cited Horizons report (79% of enterprises run AI agents in production, only 2% secured — a demand-generation asset); ARR $1.231B (+25%), SaaS ARR +36%, AI-driven ARR >$70M and >30% of net new ARR; a Zacks upgrade to Buy in Oct 2026.
- **ESG:** low controversy exposure; no environmental footprint issues, no labor or supply-chain controversies identified. Human-capital and data-ethics exposure only.

---

### 6. Overall Non-Financial Risk Rating: **MODERATE** (upper bound — governance sub-risk is **HIGH**)

No fraud indicators, no enforcement actions, no restatement or material weakness, no insider *buying* collapse, and customer data intact. Offsetting these: an 86% controller with an exit incentive, a founder-CEO, guidance-driven double-digit drawdowns twice in six months, a live multi-firm securities investigation, one-directional insider selling, and a genuinely credible Microsoft bundling threat.

---

### 7. Red Flags Requiring Escalation

1. **Securities-fraud / fiduciary-duty investigations (Pomerantz, Levi & Korsinsky, Schall, Kuehn).** Guidance-credibility and disclosure-controls exposure; D&O and derivative-overhang risk. Confirm whether any has converted to a filed complaint.
2. **Two guidance-driven crashes in six months** — Mar 18, 2026 (−15.2% to $12.47 on FY26 results/FY27 outlook) and Jun 9, 2026 (−11.5% to $15.66 on a beat with weak guidance). A pattern of optimistic forward framing is precisely what plaintiffs allege.
3. **Director Hamade's resignation, June 8, 2026** — one day before the guidance shock. Establish reason and whether it reflects sponsor or audit-committee disagreement.
4. **Insider selling at prices below the $23 IPO price**, including ~$4.4M by the CEO in two days (Oct 6–7, 2026), with zero insider purchases in 12 months.
5. **Thoma Bravo 86.2% control + overhang** — controlled-company exemptions, inability of minorities to effect change, and event risk from a block distribution, follow-on, or renewed take-private.
6. **April 20, 2026 GitHub repository breach** — monitor for follow-on disclosure, customer-attrition commentary on the Dec 8, 2026 earnings call, and any regulatory inquiry.
7. **Microsoft Entra bundling** — track net revenue retention and IdentityIQ renewal rates as the leading indicator of disintermediation.

---

### Data Gaps (honest caveats)
- **DEF 14A and 10-K full text were not retrievable** (EDGAR returned 403; the filing tool reported "no 10-K found" despite `sail-20260131.htm` existing). Board independence counts, chair/CEO duality, exact committee composition, and the full risk-factor section are therefore **inferred from secondary sources, not primary filings** — verify before publication.
- Form 4 tool returned filing metadata **without transaction codes**; buy/sell classification rests on press coverage of the October sales and filing cadence. Entity-level (sponsor) filings could not be attributed with certainty.
- The "no material weakness / clean ICFR" conclusion rests on a secondary summary, not the audit opinion itself.
- No primary source located for a filed securities class action — investigations only.

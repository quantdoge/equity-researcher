# Nonfin Risk Analyst

- Symbol: ARM
- Elapsed: 133.2s

---
## Non-Financial Risk Assessment — Arm Holdings plc (NASDAQ: ARM)
**As of 17 Nov 2026 | Price $183.39 | Market cap $195.1bn | Beta 3.94 | FY26 revenue $4.92bn**

⚠️ **Data note:** ARM is a UK-incorporated foreign private issuer — it files a **20-F** (FY end 31 Mar 2026) and **6-Ks**, not 10-K/DEF 14A, so standard risk-factor and proxy pulls returned nothing. Direct SEC and IR static-file fetches were blocked (HTTP 403). Findings below rely on news, EDGAR filing metadata, Form 4 disclosures and secondary reporting. The AGM vote outcome on the pay package could not be confirmed and is flagged as a gap.

---

### 1. Governance Quality Rating: **WEAK**

| Evidence | Assessment |
|---|---|
| **SoftBank (Kronos II) owns ~86–88%** of shares (~$168bn of the $195bn cap) | Controlled company; minority holders have no practical voting influence. Arm relies on FPI + controlled-company exemptions (no DEF 14A, reduced Nasdaq independence requirements). |
| **Masayoshi Son is Chairman**; SoftBank's founder chairs the board of a company he controls | Not independent; CEO/Chair roles are split, but the chair answers to the controlling shareholder, not minorities. |
| **ISS recommended against re-electing both CEO Rene Haas and Chairman Son**, citing insufficient board independence (Aug 2026) | Direct third-party validation of the independence deficiency. |
| **$800m CEO pay plan** (425,000 PSUs, tied to a ~$2trn market-cap aspiration), put to a 9 Sept 2026 vote after proxy-adviser opposition ("excessive") | Pay quantum is ~1.6x FY26 revenue growth in a single grant; incentive horizon is long-dated and market-cap-based, not returns- or royalty-growth-based. |
| **No DEF 14A / limited remuneration disclosure** | Structural information asymmetry versus US peers. |

**Verdict:** Weak. This is a structurally controlled company with a contested executive-pay regime, an adviser-flagged independence deficit, and disclosure standards below US large-cap norms. Minority shareholders are price-takers on governance.

---

### 2. Regulatory Risk Summary — **ELEVATED AND BROADENING**

- **US FTC antitrust probe (reported May 2026):** investigating whether Arm is illegally monopolising semiconductor IP by restricting/downgrading architecture access to rivals — triggered by Arm's launch of its **own AGI/data-centre CPU**, which puts it in direct competition with its own licensees.
- **Korea (KFTC):** Seoul office inspected; licensing practices under investigation.
- **EU:** Qualcomm filed a European Commission complaint (2024) alleging Arm restricted licence access; the EC track has reportedly escalated alongside the US and Korean actions.
- **Qualcomm litigation (Delaware) — adverse liability findings twice:**
  - Nuvia case: jury verdict against Arm (Dec 2024), upheld Sept 2025, **on appeal**.
  - Second trial: **13 Oct 2026 jury found Arm breached Qualcomm's licence and interfered with Qualcomm's Meta deal** — damages nominal ($1 per claim, $2 total), but the liability finding is what matters. Judge Noreika must still rule on Qualcomm's **Section 8.3 remedy allowing suspension of royalty payments and court-setting of commercial terms through 2033**. Reporting indicates the judge is reluctant to set rates — a genuine swing factor, not a resolved item. A separate California unfair-competition claim is pending.
- **China:** Arm China (~16–17% of revenue; **$790.6m** IPLA revenue in FY26) operates independently; Arm is effectively a minority economic holder with a history of boardroom conflict (Allen Wu dispute). PRC regulatory/export-control and audit-rights exposure is structural and unhedgeable.
- **EDGAR full-text enforcement search returned no SEC enforcement actions against Arm** — a genuine clean bill on accounting/securities enforcement. No restatement, no material weakness, no whistleblower suit identified.

**Tone:** the antitrust exposure is not incidental — it targets the *precise strategic pivot* (own silicon) that the bull case rests on. Remedies (behavioural constraints or forced IP/architecture access commitments) could structurally cap the model.

---

### 3. Insider Activity Analysis — **NET SELLING, ZERO BUYING**

- **34+ Form 4s filed Mar–Sep 2026**, including a cluster of ~20 on 19 May 2026. Insiders have been **exclusively sellers; no open-market purchases identified**.
- **CFO Jason Child:** sold 10,400 shares @ $255.33 (27 Aug 2026, ~$2.7m), retaining 163,832 shares.
- **Chief People Officer Charlotte Eaton:** sold 4,000 @ $282.77 (21 May 2026, ~$1.1m).
- Aggregate recent insider sales **>$11.5m**; Barron's pegged ~**$26m** sold between mid-May and early June 2026 — sales that (ironically) preceded the June peak of $439 but still crystallised large gains.
- **The real overhang is SoftBank, not the executives:** SoftBank has repeatedly pledged Arm stock as collateral — margin loans reportedly scaled to **$25bn** ($20bn → $25bn) and once drawn at $13.5bn. Its stake has also trended down (88.1% → ~86.4%).
- **Interpretation:** executive sales are modest relative to $195bn cap and look like scheduled 10b5-1/RSU-tax selling — not a red flag in isolation. **The SoftBank pledge is the flag**: an ~86% holder with a $25bn loan secured on a stock that has fallen **~58% from its $439 June peak** creates a mechanical forced-selling/margin-call channel that no fundamental catalyst can offset. It also raises the related-party question of whether Arm's balance sheet gets enlisted to fund SoftBank's AI ambitions.

---

### 4. Top Operational Risks

1. **Key-person dependency on CEO Rene Haas — acute and now empirically priced.** Nvidia's board approached Haas about succeeding Jensen Huang (FT/WSJ, 13 Nov 2026); ARM fell ~5% on the report and ~8% amid the wider selloff. Arm's own annual report states it is **"particularly dependent"** on him. He is the architect of the licensing→silicon pivot and the $15bn revenue ambition. No public succession plan. Departure would remove both strategy and the story.
2. **Business-model self-cannibalisation / channel conflict.** Selling Arm-branded silicon converts the world's most important chip-design customers (Qualcomm, MediaTek, Apple, Nvidia, Samsung, hyperscalers) into competitors. This simultaneously creates antitrust liability, motivates RISC-V migration, and raises the risk that licence renewals are negotiated under duress — with royalty growth already decelerating (**22% → 8%** in Q2 FY27).
3. **Extreme end-market/customer concentration plus platform and geopolitical chokepoints.** Royalty base remains smartphone-weighted; revenue concentration in a handful of licensees and in Arm China (~16–17%, an entity Arm does not control); "uncontrollable" dependency on TSMC-ecosystem foundry capacity and on US/China export-control policy. Add **beta 3.94** and a 58% drawdown — operationally, this is a business whose value chain is outside its own control.

---

### 5. Reputational Risk Assessment — **MODERATE-HIGH**

- **Pay controversy:** the "$800m payday" was covered by the Telegraph, Yahoo Finance, Seeking Alpha and proxy advisers as "excessive," with ISS opposing the CEO *and* the chairman. This is the classic template for a UK/European governance protest vote and activist-letter campaign.
- **Litigation optics:** being found to have **breached and interfered** with a customer's contract — including allegedly disrupting a Qualcomm–Meta deal — is reputationally worse than the $2 damages suggest. Arm publicly framed the verdict as "favourable," a spin that invited pushback.
- **Customer-relations strain:** suing your largest customer twice while launching a product that competes with them is a reputational position, not just a legal one. Expect public licensee complaints to feed the FTC/EU/KFTC files.
- **Mitigants:** no product recall, no consumer-facing brand, no data-privacy breach disclosed in the period. Arm's developer-ecosystem goodwill and engineering brand remain strong, and the "AI infrastructure" narrative still attracts coverage.
- Valuation credibility is fraying — profits have missed expectations and the stock has halved since June, which amplifies any negative disclosure.

---

### 6. Overall Non-Financial Risk Rating: **HIGH**

Not Critical — there is no fraud indicator, no restatement, no SEC enforcement, no cyber incident, and no going-concern or continuity threat; the franchise (architecture ubiquity, ~$4.9bn revenue, 50% licensing growth) is intact. But governance is weak by construction (86% controlled, adviser-flagged, contested pay), regulatory exposure spans **three major jurisdictions simultaneously** and targets the core growth strategy, an adverse liability finding now sits in the remedy phase, and the single most important executive is being recruited by the industry's most important company while his controlling shareholder has pledged $25bn of stock as collateral.

**Governance and regulatory risks here are not tail risks — they are the operating environment.**

---

### 7. Red Flags Requiring Escalation

1. **🚩 GOV-1 — SoftBank margin-loan cascade.** ~86% ownership pledged against up to $25bn of borrowing, on a stock down 58% from peak. Escalate for: (a) current LTV and pledge disclosures in the 20-F; (b) any Arm-level guarantee, cross-default or intercompany support to SoftBank; (c) forced-sale scenario sizing.
2. **🚩 REG-1 — Concurrent FTC / KFTC / EC antitrust probes into the own-silicon strategy.** Escalate for legal-reserve and remedy-scenario analysis; behavioural remedies could cap the AGI CPU opportunity entirely.
3. **🚩 REG-2 — Qualcomm Section 8.3 royalty-suspension ruling (pending, Judge Noreika).** Unquantified but potentially material recurring-royalty interruption plus a precedent for every other licensee. This is the highest-variance near-term event.
4. **🚩 OPS-1 — CEO retention / key-person.** Nvidia approach confirmed by multiple outlets; "particular dependence" disclosed by the company; no visible succession plan. Escalate to the board-engagement team; request retention and succession disclosure.
5. **🚩 GOV-2 — AGM dissent levels unverified.** ISS recommended against Haas and Son; the 9 Sept 2026 vote result could not be retrieved. **Escalate to verify the actual dissent percentage on the remuneration policy and both director re-elections** — a >20% "against" vote materially changes the engagement case for a UK-incorporated issuer.
6. **🚩 GOV-3 — Related-party / Arm China opacity.** An independently operated entity contributing ~16–17% of revenue, with a history of governance breakdown and no clear audit or control rights, is a disclosure and fraud-risk blind spot in an FPI structure with no DEF 14A.

**Recommended action:** Flag for the investment committee as **"High non-financial risk — position sizing and event-risk governance required."** Specifically: treat the Qualcomm remedy ruling and any FTC action as binary catalysts, and do not underwrite the own-silicon optionality without a haircut for behavioural-remedy risk. Re-run this assessment on the FY27 20-F and on confirmation of AGM dissent levels.

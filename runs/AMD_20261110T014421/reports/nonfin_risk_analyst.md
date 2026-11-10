# Nonfin Risk Analyst

- Symbol: AMD
- Elapsed: 57.8s

---
# AMD — Non-Financial Risk Assessment
**Advanced Micro Devices, Inc.** | Semiconductors | $830B mkt cap | Price $508.58 | Beta 2.49 | CEO: Lisa T. Su | 31,000 employees

---

## 1. Governance Quality Rating: **ADEQUATE** (with two structural blemishes)

**Positives**
- Genuine **Lead Independent Director** structure: Nora Denzel (ex-interim CEO Outerwall, ex-Intuit/HP SVP, NACD Directorship Certified) chairs the Nominating & Corporate Governance Committee — a functional counterweight, not a titular one.
- Board carries real industry/finance depth: Mike Gregoire (ex-Chairman/CEO CA Technologies, now SAP SE Supervisory Board), John Marren (Vice Chairman NA, Temasek), Tim Ryan (appointed 2026).
- Shareholders **backed the full board** at the 2026 annual meeting; no activist campaign, no proxy fight — no evidence of investor revolt.
- CEO/CFO Sarbanes-Oxley §302 certifications clean in the Q3 2026 10-Q (filed Nov 3, 2026); no disclosed material weakness.

**Blemishes**
- **CEO/Chair duality confirmed.** Lisa Su signs filings as "Chair, President and Chief Executive Officer." She has been CEO since Oct 2014 (**12 years**) and Chair since Feb 2022. Power concentration is at the high end for a mega-cap.
- **Severe key-person concentration.** Dr. Su is the architect of the entire turnaround and the public face of the AI roadmap. She simultaneously serves as **Chair of the Semiconductor Industry Association (SIA)**, a member of **PCAST**, and received the National Medal of Science in 2026 — an unusually heavy external load with **no disclosed succession plan**. This is the single most underpriced governance fact at AMD.
- **Incentive alignment has been re-engineered around customers, not shareholders** (see Red Flag #1). AMD is using its own equity — up to ~320M shares at $0.01 to OpenAI and Meta — as customer-acquisition currency. That is a transfer of shareholder value to two counterparties and a governance choice the board should be asked to justify.

---

## 2. Regulatory Risk Summary: **HIGH — the dominant non-financial exposure**

*No active SEC enforcement action identified.* EDGAR full-text enforcement search returned **zero** hits for AMD; litigation profile is routine (Adeia patent suits **settled** Mar 2026; Fermat International case filed Jan 2026). AMD reports no material legal proceedings. That is clean — the risk is forward-looking, not adjudicated.

| Vector | Status | Risk |
|---|---|---|
| **US export controls** | BIS Jan 2026 final rule moved Nvidia H200 / AMD **MI325X**-class licensing to **case-by-case review**; AMD reportedly holds MI308 China licenses and has agreed to a **~15% fee** on those China exports (reported, not confirmed in filings) | High — a policy revocable at will; a de facto government revenue share on China sales |
| **Sweeping new permit regime** | Mar 2026 reporting: US drafting rules requiring permission for **virtually all AI accelerator exports globally** | **Critical if enacted** — would put a licensing gate in front of the fastest-growing business (Data Center $8.5B/qtr, +97% y/y) |
| **China retaliation** | SAMR antitrust action vs. Nvidia; Beijing strategy includes antitrust probes, purchasing bans, customs inspections, mineral controls | Moderate — AMD partially insulated (China Instinct sales described as negligible) but exposed to a blanket ban |
| **Tariffs** | 25% value-based tariff on "covered products" effective Jan 15, 2026 | Moderate |
| **Antitrust — customer incentives** | Intensifying global scrutiny of **bundling, exclusive deals, and market allocation** across the AI chip supply chain | **Underappreciated** — warrant-for-volume agreements with OpenAI/Meta are exactly the arrangement type FTC/DOJ/EU are now probing |
| **Sales-practice scrutiny** | Post-Nvidia board investigation, analysts flag AMD/Broadcom "could also be subject to greater scrutiny over their sales practices" | Moderate, rising |

**Regulatory backdrop matters for valuation:** the Nov 5, 2026 semiconductor rout (worst Nasdaq session in 18 months) was attributed partly to **midterm-election-driven regulatory worries** — AMD is now a policy-sensitive stock, not merely a cyclical one.

---

## 3. Insider Activity Analysis: **HEAVY NET SELLING — ZERO BUYING**

**Net direction: unambiguously negative.** No open-market insider purchases were recorded in the trailing twelve months. Every identifiable Form 4 transaction is a sale or an equity-compensation event.

| Insider | Date | Transaction | Value |
|---|---|---|---|
| **Lisa Su** (Chair/President/CEO) | Sep 10, 2026 | Sold 95,000 sh @ ~$503–515 + gifted 35,000 sh | **~$48.1M** |
| **Lisa Su** | Mar 12, 2026 | Sold 85,000 sh | ~$16.9M |
| **Lisa Su** | Aug 18, 2026 | Sold 2,500 sh | ~$1.2M |
| **Paul Darren Grasby** (EVP) | Aug 17, 2026 | Sold 15,000 sh @ $514.91 | ~$7.7M |
| Various | Aug 11, Aug 18, Aug 20, 2026 | Clustered Form 4s (9+ filers per window) | — |

**Assessment**
- Su retains ~3.7M shares — she remains materially aligned, which prevents this from being a "get out" signal.
- All sales executed under **Rule 10b5-1 plans** (Su's adopted **June 8, 2026**), which legally defuses informed-trading inference.
- **But the pattern deserves escalation:** Su sold ~$48M in September at $503–515; the stock peaked at **$649 on Oct 6** and collapsed to **$402 on Nov 5 (−38%)**. Insiders were net sellers into strength in every window of 2026 and bought **nothing** during a 38% drawdown. That absence of insider buying at a "generational buying opportunity" (per sell-side) is a genuine information signal.
- Early-2026 Form 4 volume shows **176 total filings by Su since 2021** — a monetization program, not opportunistic trading.

---

## 4. Top Operational Risks

1. **Circular financing / customer concentration embedded in the growth story.** Data Center growth is anchored to a handful of counterparties — OpenAI, Meta, Google (5th Gen EPYC selected to power Google Cloud TPU 8tx host infrastructure), Microsoft. AMD is simultaneously **selling chips to and issuing equity to** its two largest AI customers. This entangles revenue with counterparty solvency and speculative financing. If an OpenAI deployment slips, AMD loses revenue *and* books a warrant mark-to-market swing. Concentration disclosure is obscured by anonymized "large customer" reporting — a disclosure gap that governance researchers have specifically criticized.

2. **Working-capital strain and inventory obsolescence.** Q3 2026: revenue $13.4B, net income $2.4B, **operating cash flow only $1.2B, FCF $554M — a 4% cash margin.** Inventory is building aggressively ahead of guidance calling for ~80% revenue growth in 2027. Management frames this as "supply lock-in"; bears call it a red flag. Either way, a demand air-pocket converts this inventory into write-downs, and AMD is **sole-sourced on TSMC leading-edge plus HBM from a three-vendor oligopoly** — no supply redundancy.

3. **Key-person dependency + product-security drag.** The Helios rack-scale ramp and the 2027 outlook (~135% data center growth per Oppenheimer) rest on one executive's roadmap executing flawlessly against Nvidia's annual cadence. Compounding this: a steady CVE cadence — **BadRAM** (physical server compromise via $10 of parts), **CVE-2025-0033** (confidential VM flaw), Zen 5 RDSEED key-predictability, CVE-2026-0465, CVE-2026-43603. Individually minor; collectively they undercut AMD's **confidential-computing pitch**, which is precisely the enterprise AI security claim it is using to win cloud share. Patches exist in each case — no breach disclosed.

---

## 5. Reputational Risk Assessment: **MODERATE-HIGH**

**Negative**
- **Volatility as a brand issue:** beta 2.49; −38% in 30 days; a −17% single session followed by +13% two sessions later (~$100B of market value added in a day). A retail-heavy holder base experiencing this amplitude generates durable shareholder-relations damage and invites litigation-oriented scrutiny.
- **The "circular financing" narrative has gone mainstream** — Reuters, Seeking Alpha, Columbia Business School, Acadian Asset all now cover AMD's warrant structures as a case study in AI revenue quality. This is the reputational risk most likely to compound: it fuses accounting skepticism with AI-bubble skepticism.
- **Earnings-quality critiques are now public and specific:** "Something Doesn't Add Up With AMD," "The Party Is Ending" (FCF at 4% of revenue, rising inventories, dilution from AI warrants). The **$2.4B net income vs. $1.2B operating cash flow** gap will be the focal point of any short thesis.
- **Political exposure of the China arrangement:** paying a reported 15% fee for export access is easily characterized as "paying the government for market access" — a poor look for a company trading on technological leadership.

**Positive offsets**
- Dr. Su's National Medal of Science and TIME CEO of the Year standing; record Q3; Google Cloud design win; Oppenheimer upgrade to Outperform ($600 PT). Brand equity with hyperscalers and developers is genuinely strong (EPYC share gains).
- **No consumer recall, boycott, ESG controversy, or product-liability event identified.**
- AMD is currently a *beneficiary* of Nvidia's governance crisis (Nvidia board probing CEO's ties to an alleged Chinese spy) — but that same scrutiny is a two-way street for sales practices.

---

## 6. Overall Non-Financial Risk Rating: **HIGH**

Not Critical — there is no fraud evidence, no enforcement action, no material weakness, and a credible lead independent director. But the combination of (a) a binary policy risk sitting directly on the growth engine, (b) $1.1B/quarter of stock-price-driven non-cash charges from customer warrant deals, (c) 4% free cash flow margins against $2.4B of net income, and (d) a 12-year Chair/CEO with no disclosed successor, places AMD in the top decile of non-financial risk among mega-cap semis.

---

## 7. Red Flags Requiring Escalation

1. **🔴 Warrant-for-customer agreements (OpenAI ~160M shares; Meta up to ~10% of the company; ~320M shares combined at $0.01).** Q3 2026 carried a **$1.097B non-cash charge** that moves with AMD's own share price. *Escalate to:* exact vesting/pricing triggers; whether revenue recognition milestones coincide with warrant vesting; adequacy of related-party and customer-concentration disclosure. This is a **circular-financing** structure and is now the center of the bear case.

2. **🔴 Cash conversion divergence.** Net income $2.4B vs. operating cash flow $1.2B; FCF $554M (4% of revenue); inventory surging. Combined with the **SEC's new Financial Reporting and Accounting Unit ("FRAU," established Aug 5, 2026)**, which explicitly extends its mandate beyond reporting fraud to "general misconduct," AMD's working-capital accounting sits in a heightened enforcement environment. Watch for channel-stuffing or pull-forward dynamics.

3. **🟠 CEO sold ~$48M in September 2026 at $503–515 — weeks before a 38% drawdown — and no insider bought the dip.** 10b5-1 plans provide legal cover, but the **June 8, 2026 plan adoption date** should be checked against known non-public information flow (Q2 guidance, Helios timing, Google win). Zero insider purchases on a 38% decline is itself the tell.

4. **🟠 Pending US rule requiring permits for virtually all AI accelerator exports.** Binary and unhedgeable. A licensing gate on global AI accelerator sales would impair the 2027 thesis that the entire multiple rests on.

5. **🟠 Antitrust exposure of customer-incentive/exclusivity agreements.** Jurisdictions are actively investigating bundling and exclusive dealing in AI accelerators. AMD's warrant-for-volume contracts are precisely in the crosshairs — simultaneously a regulatory and a reputational vector.

6. **🟡 Succession opacity.** Chair/CEO duality (since Feb 2022), 12-year CEO tenure, SIA Chairmanship, PCAST membership, no disclosed succession plan. Quantify as a discount to the multiple, not a footnote.

---

*Data gaps, disclosed honestly: the 10-K risk-factor section and DEF 14A full text were not retrievable through available tools (10-K not returned; SEC proxy fetch returned HTTP 403), so board-independence counts, executive comp metrics, and related-party disclosures could not be independently verified — governance findings rest on the Q3 10-Q CEO certification, AMD's IR board biographies, and secondary reporting. Insider transaction details derive from Form 4 metadata plus secondary aggregators (StockTitan, secform4, TradingView), not primary XML. The 15% China export fee is reported but unconfirmed in filings. Recommendations: obtain the DEF 14A directly from EDGAR and pull primary Form 4 XML before finalizing the governance score.*

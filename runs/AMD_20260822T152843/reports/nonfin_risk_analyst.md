# nonfin_risk_analyst

_2026-08-22T07:42:00+00:00_

# AMD Non-Financial & Governance Risk Assessment
**Ticker:** AMD | **Date:** August 22, 2026  
**Analyst:** Non-Financial Risk Desk

---

## 1. Insider Trading Signal: **BEARISH**

### Evidence
| Metric | Value | Source |
|---|---|---|
| Q3 2026 (YTD) Acquired/Disposed Ratio | 0.43 | FMP `insiderTrades` / `insider-trade-statistics` |
| Q2 2026 Acquired/Disposed Ratio | 0.19 | FMP `insiderTrades` / `insider-trade-statistics` |
| Q1 2026 Acquired/Disposed Ratio | 0.29 | FMP `insiderTrades` / `insider-trade-statistics` |
| Q3 2026 Total Open-Market Purchases | **0** | FMP `insiderTrades` / `insider-trade-statistics` |
| Q3 2026 Total Sales | 26 | FMP `insiderTrades` / `insider-trade-statistics` |
| Q2 2026 Total Sales | 67 | FMP `insiderTrades` / `insider-trade-statistics` |

**Interpretation:**  
Over the last three quarters, AMD insiders have recorded **zero open-market purchases** while executing dozens of sales. The acquired-to-disposed ratio sits well below 1.0 in every period (as low as 0.19 in Q2 2026), meaning insiders are disposing of shares at roughly 3–5× the rate they acquire them. Recent Form 4 filings show CTO Mark D. Papermaster gifting 25,052 shares and immediately selling additional blocks at ~$466–$468 in August 2026 (FMP `insiderTrades` / `search-insider-trades`). Web search confirms that CEO Lisa T. Su has also been continuously exercising RSUs and unloading shares, including a reported $20.4M sale in 2024.

**Signal:** **Bearish** — persistent, broad-based insider distribution with no offsetting purchases.

---

## 2. Governance Quality Rating: **WEAK** *(with material caveats)*

### Board Structure
- **CEO-Chair Duality:** Dr. Lisa T. Su serves as **Chair, President and CEO** simultaneously (AMD IR Board page; FMP `company` / `profile-symbol`). This concentrates decision-making power in a single individual and is a classic governance red flag.
- **Lead Independent Director:** Nora M. Denzel holds the Lead Independent Director role, which partially mitigates duality but does not eliminate it (AMD IR Board page).
- **Board Committees:** Four standing committees exist — Audit and Finance; Compensation and Leadership Resources; Innovation and Technology; and Nominating & Corporate Governance (AMD IR Governance Documents page).

### Gaps
- **Exact independence breakdown unavailable:** The AMD Board page was truncated during retrieval, and the DEF 14A proxy could not be fetched due to SEC.gov access restrictions. We therefore **cannot confirm** the precise percentage of independent directors or whether the audit committee is 100% independent and financially literate. *This is a flagged data gap.*
- **Related-party transactions:** No related-party transaction data could be retrieved from FMP endpoints or web searches. *Gap flagged.*

### Management Quality
- **CEO tenure & track record:** Dr. Su has led AMD since October 2014 and is credited with turning around the company. She holds elite technical credentials (MIT B.S./M.S./Ph.D. in EE) and was named TIME CEO of the Year in 2024.
- **CFO:** Jean Hu has been EVP, CFO and Treasurer since 2023. Compensation data shows her 2024 total comp at $9.05M (FMP `company` / `executive-compensation`), heavily equity-weighted.
- **Succession risk:** The company is still closely identified with Dr. Su. The recent appointment of Tim Ryan to the board (August 2026 press release) may add depth, but key-person dependency remains elevated.

**Governance Quality Score:** **Weak** due to CEO-Chair duality, lack of verifiable independence metrics, and heavy reliance on a single executive for both strategy and board leadership.

---

## 3. SEC Enforcement or Investigation History

**Finding:** No active SEC enforcement action or DOJ investigation specifically targeting AMD was identified in searches of SEC.gov litigation releases, DOJ press releases, or third-party securities-enforcement trackers.

**Caveat:** The absence of public charges does not guarantee the absence of informal inquiries or Wells notices. AMD is, however, subject to the same semiconductor-industry regulatory scrutiny as peers (NVIDIA, Intel) regarding China export controls and antitrust. No AMD-specific insider-trading scandal or accounting-fraud case was found in the 2024–2026 window.

---

## 4. Regulatory Risk Summary

| Risk | Status | Impact |
|---|---|---|
| **U.S. Export Controls (China)** | Active | Material |
| **Data Privacy / Breach** | Under investigation | Moderate |
| **Antitrust** | No active AMD-specific case | Low |

### U.S. Export Controls — Critical
AMD’s Q2 2025 earnings release explicitly stated that U.S. Government export controls on **AMD Instinct MI308** data-center GPUs forced **~$800 million in inventory and related charges** (AMD IR press release). The Bureau of Industry and Security (BIS) has also indicated that AMD MI325X and comparable chips are now subject to **case-by-case license review** for certain destinations. This is a recurring, structural headwind that can wipe out quarterly gross-margin expansion and strand inventory.

### Data Privacy / Breach
In July 2025, a threat actor named Intelbroker claimed to have breached AMD and posted sensitive employee data (names, phone numbers, email addresses) on a dark-web forum. AMD’s official response: *“We are working closely with law enforcement officials and a third-party hosting partner to investigate the claim”* (The Cyber Express, July 2025). No regulatory fine has been announced, but the incident creates GDPR/CCPA exposure and reputational damage.

---

## 5. Operational Risk Events

1. **Export-Control Inventory Stranding ($800M Charge)**  
   Q2 2025 results included a massive inventory writedown tied to MI308 GPUs blocked from China. This demonstrates extreme sensitivity to geopolitical/regulatory shocks (AMD IR press release).

2. **Alleged Data Breach (July 2025)**  
   Intelbroker’s claimed breach of employee data, if verified, signals potential gaps in third-party hosting security. AMD has not yet confirmed the full scope. *Ongoing monitoring required.*

3. **Supply-Chain / Geopolitical Concentration**  
   As a fabless semiconductor designer, AMD relies on TSMC for leading-edge manufacturing. While no specific TSMC disruption was flagged for AMD in the 2024–2026 window, the export-control dynamics show that **customer concentration in restricted markets** is itself an operational chokepoint.

*No product recalls or manufacturing plant outages were identified.*

---

## 6. Dilution Risk from Stock-Based Compensation (SBC)

| Metric | Value | Source |
|---|---|---|
| Outstanding Shares | 1,630,600,000 | FMP `company` / `shares-float` |
| Float Shares | 1,622,056,292 | FMP `company` / `shares-float` |
| Free Float % | 99.48% | FMP `company` / `shares-float` |

### Share-Count History
- 2024: 1.637B shares (up 0.74% y/y)
- 2025: 1.636B shares (down 0.06% y/y) — *Macrotrends via web search*

### Red Flags on Dilution
- **Massive authorization request:** AMD’s board has reportedly recommended authorizing **1.75 billion additional shares** (Reddit / r/AMD_Stock, citing proxy materials). If executed, this would more than double the current share base.
- **M&A-driven issuance:** Web search references indicate recent deals (e.g., **Taalas acquisition** in August 2026) may require issuing ~320 million shares (Seeking Alpha headline).
- **SBC-heavy comp:** Executive compensation is dominated by equity. For example, Forrest Norrod’s 2025 total comp of **$13.49M** consisted of ~$9.82M in stock awards and ~$1.74M in option awards (FMP `company` / `executive-compensation`). While this aligns pay with long-term performance, it mechanically expands the share count.

**Dilution Risk:** **High.** The combination of existing SBC, pending M&A equity consideration, and a potential 1.75B share authorization creates a significant overhang for existing shareholders.

---

## 7. Reputational Risk Assessment

| Factor | Assessment |
|---|---|
| **Data Breach Headlines** | Moderate — the Intelbroker claim received cybersecurity-media coverage but has not yet escalated to a confirmed, massive consumer-data leak. |
| **Export-Control Narrative** | Moderate — being singled out by U.S. chip restrictions alongside NVIDIA frames AMD as vulnerable to geopolitical swings. |
| **Insider Selling Narrative** | Moderate — continuous CEO/CTO sales are periodically picked up by financial media (Investing.com, Seeking Alpha) and can dampen retail sentiment. |
| **AI Competitive Positioning** | Mixed — AMD must prove it can compete with NVIDIA in AI accelerators; any product-delay headline would compound reputational risk. |

**Overall Reputational Risk:** **Moderate**, with upside sensitivity to any confirmation of the data breach or further export-control restrictions.

---

## 8. Management Quality Assessment

- **Strategic Execution:** Strong. Under Dr. Su, AMD has gained share in servers (EPYC) and PCs (Ryzen), and is now the #2 player in AI accelerators.
- **Capital Allocation:** Concerning. The proposed 1.75B share authorization and M&A equity issuance signal a willingness to dilute existing holders aggressively.
- **Risk Management:** Weak on geopolitical/regulatory foresight. The $800M MI308 inventory charge suggests AMD either underestimated or could not mitigate the speed of U.S. export-control expansion.
- **Insider Behavior:** Poor signal. Zero open-market purchases and persistent high-level selling contradict the bullish narrative management presents on earnings calls.

---

## 9. Overall Non-Financial Risk Rating: **HIGH**

**Rationale:**  
AMD scores poorly on governance (CEO-Chair duality), insider behavior (persistent selling, no buying), dilution (massive potential share authorization + SBC), and regulatory/geopolitical risk ($800M China export-control charge, ongoing BIS scrutiny). The alleged 2025 data breach adds cybersecurity risk. While there is no active SEC fraud case, the confluence of concentrated power, insider distribution, and equity overhang elevates the non-financial risk profile to **High**.

---

## 10. Red Flags Requiring Escalation

1. **CEO-Chair Duality with No Verifiable Independence Firewall**  
   Lisa Su controls both the board agenda and management execution. Without confirmed supermajority independence metrics, minority shareholder oversight is compromised.

2. **1.75 Billion Share Authorization Request**  
   This would more than double the current ~1.63B share base. If approved, dilution could be catastrophic for existing holders. *Escalate to equity strategy desk.*

3. **Zero Insider Purchases + Persistent High-Level Selling**  
   When insiders refuse to buy with their own cash while aggressively selling vested equity, it is a powerful negative signal that should temper any bullish valuation thesis.

4. **$800M Export-Control Inventory Charge & Recurring BIS Risk**  
   This is not a one-off accounting item; it reflects a structural vulnerability. Any further tightening of AI-chip export rules could force additional writedowns.

5. **Unconfirmed but Credible Data Breach (Intelbroker, July 2025)**  
   If the breach is confirmed to include customer IP or sensitive technical data, reputational and legal liabilities could escalate rapidly.

6. **High Beta (2.489)**  
   From FMP `company` / `profile-symbol`. AMD’s stock is nearly 2.5× as volatile as the market, amplifying the impact of any governance or operational shock.

---

## Data Gaps Flagged
- Exact percentage of independent directors and audit-committee composition (DEF 14A inaccessible).
- Full scope and confirmation of the Intelbroker data breach.
- Complete list of related-party transactions for FY2025.
- Detailed terms of the Taalas acquisition and exact share issuance required.
- Real-time ESG controversy scores (FMP Starter plan limits ESG data).

---

*End of Report*

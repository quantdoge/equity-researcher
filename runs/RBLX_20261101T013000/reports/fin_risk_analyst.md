# Fin Risk Analyst

- Symbol: RBLX
- Elapsed: 54.9s

---
## RBLX — Financial Risk Assessment
**Data as of:** FY2025 (period end 2025-12-31, filed 2026-02-11); market data through 2026-02-10

**⚠️ Data conflict flagged:** The company profile reports price $42.98 / market cap $28.8B, while the price history tool shows a 2026-02-10 close of **$71.94** (≈$49.6B on 690M diluted shares). The profile/market-cap figure appears stale. I use **$71.94** for market risk and present FCF yield on both bases. All ratio tools that depend on market cap (`calculate_fcf_yield`) are computed off the stale $42.98 and should be treated as an upper bound.

---

## 1. Credit Risk Assessment: **SUB-INVESTMENT GRADE (with net-cash offset)**

RBLX is a GAAP-loss-making, accumulated-deficit company with near-zero book equity, but it holds **net cash of ~$1.25B** and carries no near-term maturities. It is not a solvency risk today; it is a *cash-flow quality* risk.

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Revenue | $4,890.6M | $3,602.0M | $2,799.3M | +35.8% YoY |
| Gross margin | 78.1% | 77.8% | 76.8% | Expanding |
| Operating margin | **-25.2%** | -29.5% | -45.0% | Improving but deeply negative |
| Net income | -$1,065.1M | -$935.4M | -$1,151.9M | Persistent losses |
| EBITDA (GAAP, post-SBC) | **-$802.2M** | -$670.3M | -$911.0M | Negative |
| SBC | **$1,129.0M** | $1,015.8M | $868.0M | 23.1% of revenue |
| Total debt | $1,802.7M | $1,805.3M | — | Incl. ~$795M operating leases; notes ~$1,008M |
| Cash & ST inv. | $3,055.1M | $2,409.5M | — | |
| **Net cash** | **$1,252.4M** | $604.3M | — | Strengthening |
| Total equity | **$375.0M** | $208.7M | — | 3.9% of assets |
| Retained earnings | -$5,060.7M | -$3,995.6M | — | Accumulated deficit |
| Interest expense | $40.0M | $41.2M | $40.7M | ~4% coupon → likely convertible notes |

**Interpretation of coverage:** Reported interest coverage is **-30.8x** (EBIT -$1,028M / interest $40M). This is an accounting artefact of GAAP losses, not a cash-solvency signal — the $40M of annual interest is covered ~76x by cash on hand. The genuine credit issue is that **GAAP profitability does not exist**, so debt service depends on the cash-conversion cycle and continued access to capital markets.

**Altman Z-Score: -0.589 (Distress zone).** Driven by X2 (-0.53, negative retained earnings) and X3 (-0.11, negative EBIT); X4 (book equity/liabilities) is only 0.04. The Z-score is directionally correct about the *balance-sheet fragility* but overstates bankruptcy risk because it cannot see the $3.06B cash pile or the non-cash nature of deferred revenue liabilities.

**Piotroski F-Score: 7/9 (Moderate).** Positive: operating cash flow, ROA improvement, accrual quality, lower leverage, positive equity change, gross margin expansion, asset turnover improvement. Negative: **F1 = 0 (negative ROA)** and **F7 = 0 (net share issuance — diluted shares 616M → 647M → 690M, +11.9% in two years, ~6%/yr dilution)**.

**Credit rating:** No public agency rating identified (search returned no RBLX rating action). Data gap — CDS spreads and covenant terms unavailable.

---

## 2. Key Financial Risk Metrics

| Category | Metric | Value | Assessment |
|---|---|---|---|
| **Leverage** | Debt / Equity | **4.81x** | Severe, but denominator artifact (equity $375M) |
| | Debt / Assets | 0.19x | Moderate — the fairer measure |
| | Net Debt / EBITDA | -1.56x (net cash) | **Not meaningful** — negative EBITDA makes ratio sign-ambiguous |
| | Net cash position | +$1,252M | **Positive** |
| **Coverage** | EBIT / Interest | **-30.8x** | Negative — GAAP loss |
| | Cash / Interest | ~76x | Adequate |
| **Liquidity** | Current ratio | **0.96x** | Below 1.0 |
| | Quick ratio | 0.96x | (no inventory) |
| | Cash ratio | 0.60x | |
| | Working capital | **-$228.4M** | Negative |
| | Cash / total liabilities | 0.33x | |
| **Solvency** | Assets / Liabilities | 1.04x | Thin cushion |
| | Equity / Assets | **3.9%** | Near-zero book cushion |
| | Altman Z | **-0.589** | Distress zone |
| | Piotroski F | 7/9 | Moderate/improving |
| **Cash generation** | FCF | $1,352.9M (27.7% margin) | Strong headline |
| | FCF yield | 4.56% (at $42.98) / **2.73%** (at $71.94) | Modest |
| | OCF / revenue | 36.7% | |
| | **FCF ex-working-capital** | **-$101.1M** | ⚠️ See below |
| | **FCF ex-SBC & ex-WC** | **-$1,230.1M** | ⚠️ See below |

**Critical nuance on the -$228M working capital and 0.96 current ratio:** RBLX's current liabilities ($5,126M) are dominated by **deferred revenue** — an obligation settled by delivering service, not by paying cash. On a true cash-obligation basis, liquidity is materially better than the headline ratios suggest. I flag this as an *overstatement of risk* in the reported metrics, offset by the FCF-quality issue below, which is an *understatement*.

---

## 3. FCF Sustainability — The Central Risk

Reported FCF has improved dramatically: $124M (2023) → $641M (2024) → $1,353M (2025). **But the improvement is a working-capital artifact, not an earnings event.**

| | FY2023 | FY2024 | FY2025 | 3-Yr Total |
|---|---|---|---|---|
| FCF | $124.0M | $641.3M | $1,352.9M | **$2,118.2M** |
| Change in working capital | $506.8M | $481.0M | **$1,454.0M** | **$2,441.8M** |
| WC as % of FCF | 409% | 75% | **107%** | **115%** |
| FCF ex-WC | -$382.8M | $160.3M | **-$101.1M** | **-$323.6M** |
| SBC | $868.0M | $1,015.8M | $1,129.0M | $3,012.8M |

**Over three years, cumulative working-capital inflow ($2,442M) exceeded cumulative reported FCF ($2,118M).** Strip out the deferred-revenue float and the business has consumed ~$324M of cash cumulatively. Strip out SBC as well and FY2025 free cash flow is **-$1.23B** — essentially identical to operating loss. The shareholder economics are being funded by dilution (6%/yr) and by bookings collected ahead of revenue recognition.

This is not fraud or improper accounting — it is a legitimate feature of a prepaid virtual-currency model. But it makes reported FCF **structurally dependent on bookings growth**. Which brings us to the live catalyst.

---

## 4. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **60.7%** |
| Beta vs SPY (756d) | **1.25** (profile beta: 1.47) |
| Max drawdown (tool, 3y window) | **-74.9%** |
| Drawdown from Sept-2025 peak ($141.56) to Feb-2026 trough ($60.57) | **-57.2%** |
| Current drawdown from peak | **-49.2%** |
| Sharpe ratio (0% rf) | **0.30** |
| Sortino ratio | Not provided by tool — **data gap** |

**Event risk is extreme and quantifiable from the price series:**
- 2025-10-30: **-15.5% in one session** (volume 28M vs ~6M avg)
- 2026-01-29 → 2026-02-05: **-20.1% over 5 sessions** (Q4/FY25 results 2026-02-05)
- 2026-02-06 → 2026-02-09: **+21.3% in two sessions**
- 2025-02-06: -11.1% on one session

A 60.7% vol with 1.25 beta means a 20% SPY drawdown has historically coincided with roughly a **35–50% RBLX drawdown**, and a 3-sigma month is a ~-35% event. Risk-adjusted returns are poor: Sharpe 0.30 for a stock that has drawn down 57% in five months is not compensated volatility.

---

## 5. Downside Scenario Analysis

**Live guidance (per 8-K, Feb 2026): FY2026 guidance pairs +4% to +12% revenue growth with a -10% to -15% YoY bookings decline.** Q4 2025 was the peak comparison (revenue +43% to $1.4B, bookings +63% to $2.2B). The divergence — revenue growing while bookings contract — is the mechanical signature of **deferred revenue unwinding**. This is the scenario I model below.

### Scenario: Bookings -20%, revenue growth decelerates to ~0%

| Line item | FY2025 Actual | Downside | Δ |
|---|---|---|---|
| Revenue | $4,890.6M | $4,400M | -$490M |
| Gross profit (78% GM) | $3,818.3M | $3,434M | -$384M |
| Opex (incl. SBC $1,129M) | $5,050.6M | $4,650M (-8% cut) | -$400M |
| Operating income | -$1,232.3M | **-$1,216M** | roughly flat |
| GAAP EBITDA (post-SBC) | -$802.2M | -$786M | |
| + SBC add-back + D&A | +$1,354.8M | +$1,100M | |
| **Cash EBITDA** | **+$552.6M** | **+$314M** | |
| Capex | -$443.5M | -$250M (deferred) | |
| **Working capital contribution** | **+$1,454.0M** | **-$700M (reversal)** | ⚠️ **-$2,154M swing** |
| **FCF** | **+$1,352.9M** | **≈ -$640M** | **-$2.0B swing** |

**The key result: a 20% bookings decline does not just reduce FCF — it inverts it, because the deferred-revenue float that produced 107% of FY2025 FCF reverses into an outflow.** Reported FCF could swing from +$1.35B to approximately **-$0.6B** on a *mid-single-digit* revenue outcome.

**Liquidity through the downside:**
- Opening cash $3,055M; burn ~$640M/yr; **runway ≈ 4.8 years** with no additional cuts.
- Additional levers: SBC is $1,129M (23% of revenue) — cutting it 30% frees $340M/yr of *cash* comp; capex $443M is discretionary.
- Near-term maturities are minimal ($14.7M short-term; ~$993M long-term). **No refinancing cliff inside the scenario horizon.**
- Peak cash stress: cash troughs near $2.0–2.4B. **The company survives.**

**Verdict on the downside: solvency is not at risk; equity value is.** The $375M book equity cushion means the balance sheet has no buffer, but the $3.06B cash stack means obligations get paid. The damage is to the equity, which at ~$49.6B market cap prices in sustained bookings growth that guidance says is reversing.

---

## 6. Overall Financial Risk Rating: **HIGH**

Rationale: The liquidity position (net cash $1.25B, 4.8-year downside runway, no maturity wall) argues for *Moderate*. The earnings profile (negative EBIT, negative EBITDA, Altman distress zone, near-zero book equity, 6%/yr dilution, SBC at 23% of revenue) argues for *High to Critical*. What tips the overall rating to **High** is the **FCF quality finding**: the entire reported cash-generation story of the last three years is attributable to deferred-revenue float that company guidance indicates is now reversing. The company is financially *solvent* and *liquid*, but it is not yet *self-funding* on an economic basis, and the one metric the market has been underwriting (FCF) is about to stop working.

**Not Critical**, because: $3.06B cash, net cash positive, no refinancing cliff, 78% gross margin, 36% revenue growth, and a demonstrably improving operating margin (-45% → -30% → -25%) and gross margin trajectory. The operating leverage is real even if unrecognized in FCF.

---

## 7. Key Red Flags

1. **🔴 FCF is 107% funded by working capital.** FY2025 FCF of $1,353M vs. WC contribution of $1,454M. Ex-WC FCF is **-$101M**; ex-WC and ex-SBC it is **-$1,230M**. Over 3 years, WC inflow exceeded total FCF. This is the single most important finding in this report.

2. **🔴 Guidance implies deferred revenue reversal.** FY2026 guidance: revenue +4–12% with bookings **-10% to -15%**. Revenue growing while bookings contract is mechanically a deferred-revenue drawdown. The FCF engine inverts.

3. **🟠 Altman Z of -0.589 (distress zone)** and equity/assets of 3.9%. Book equity of $375M against $9.18B of liabilities is a razor-thin accounting cushion. Retained earnings deficit of -$5.06B.

4. **🟠 Interest coverage -30.8x.** Negative EBIT means debt is serviced from balance sheet, not operations. Currently fine ($40M interest vs $3.06B cash), but it means the credit is entirely dependent on the cash pile.

5. **🟠 Dilution:** Diluted shares 616M → 647M → 690M (+11.9% over 2 years, ~6%/yr). SBC of $1,129M is 23% of revenue and 83% of reported FCF. Piotroski F7 = 0.

6. **🟠 Thin liquidity ratios:** Current ratio 0.96x, working capital -$228M. Largely explained by deferred revenue classification, but the *reported* balance sheet offers no headroom if deferred revenue unwinds.

7. **🟡 Extreme market risk:** 60.7% annualised vol, beta 1.25, -74.9% three-year max drawdown, Sharpe 0.30. Multiple single-session moves of -11% to -21% in the last 18 months. Position sizing/volatility-adjusted exposure is a material risk consideration independent of fundamentals.

8. **🟡 No public credit rating identified; covenant terms and revolver capacity not disclosed in available data.** Inability to confirm whether a revolving facility exists is a genuine gap in this liquidity assessment.

### Explicit Data Gaps
- **Sortino ratio** not returned by the volatility tool.
- **CDS spreads** unavailable; **agency credit ratings** not identified via search.
- **Revolver capacity / covenant package** not available — this is the most material gap, as it determines the true liquidity backstop.
- **Deferred revenue line item** not separately broken out in the balance sheet feed; estimated from total liabilities and WC movement.
- **Market cap / price conflict** ($42.98 vs $71.94) unresolved — FCF yield and any valuation-derived metrics carry this uncertainty.
- Peer benchmarking not performed (budget); no cross-sectional read on whether RBLX's leverage or FCF conversion is anomalous vs. gaming peers.

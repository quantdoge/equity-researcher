# Fin Risk Analyst

- Symbol: RIVN
- Elapsed: 172.1s

---
# RIVN — Rivian Automotive, Inc. | Financial Risk Assessment
**Sector:** Consumer Cyclical / Auto Manufacturers | **Price:** $13.19 | **Market Cap:** ~$19.1B | **Report data through Q3 2026 (filed 10/29/26)**

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (implied high-yield / crossover-to-distressed)**

*No agency rating was retrievable — flagged as a data gap below.*

Rivian is a pre-profit, cash-consuming manufacturer. The balance sheet is not levered in the classic sense (net debt only ~$1.9B against $5.5B cash), but **the credit is structurally sub-investment-grade because the company has never generated positive EBIT or positive free cash flow**, and its equity base is being consumed by losses at a rate faster than it is being replenished by capital raises.

The decisive evidence:
- **Altman Z-Score of −2.255 = Distress zone** (threshold <1.81). The score is negative primarily because X2 (retained earnings / total assets) is **−1.81** — accumulated deficit of **−$29.1B** against $15.7B of assets. X3 (EBIT/TA) is −0.225. This is not a borderline grey-zone reading; it is deeply negative on a scale where 2.99 is "safe."
- **Interest coverage of −13.08x** (FY2025 EBIT −$3.35B vs interest $274M). Q3 2026 alone: EBIT −$834M vs interest $74M ≈ **−11.3x**. Interest is being paid out of cash reserves and asset sales, not earnings.
- **Piotroski F-Score of 4/9 — "Weak."** Fails on all three leverage/liquidity tests (negative ROA, negative operating cash flow, rising leverage) and on both dilution tests. Only the four profitability/efficiency improvement tests pass.

**Important mitigating credit fact:** there is **no near-term maturity cliff**. Short-term debt is reported at **$0** across every period shown, and the long-term debt stack ($4.45B) runs to 2029–2030 convertible maturities plus a 10-year VW term loan funded October 2026. Liquidity risk here is *burn-driven*, not *refinancing-driven*. That is a materially better risk profile than a levered issuer facing 2027 maturities.

---

## 2. Key Financial Risk Metrics Table

| Metric | FY2025 (tool output) | Q3 2026 (latest, computed) | Assessment |
|---|---|---|---|
| Total debt | $6,651M | $5,431M | Declining; LTD $4,446M |
| Net debt | $3,072M | $1,922M | Modest vs. cash |
| Debt / equity | 1.45x | 0.95x | Elevated but not acute |
| Debt / assets | 0.45x | 0.35x | Moderate |
| Net debt / EBITDA | **n.m. (EBITDA negative)** | **n.m.** | Tool's −0.22 is sign-distorted and unusable |
| Interest coverage (EBIT/int.) | **−13.08x** | **≈ −11.3x** | **Breach-level; earnings cannot service debt** |
| Altman Z-Score | **−2.255 (Distress)** | — | Deep distress zone |
| Piotroski F-Score | **4 / 9 (Weak)** | — | Fails all leverage & dilution tests |
| Current ratio | 2.33x | 2.18x | Adequate |
| Quick ratio | 1.89x | 1.70x | Adequate |
| Cash ratio | 1.65x | 1.47x | Strong |
| Working capital | $4,899M | $4,396M | Comfortable |
| Cash & ST investments | $6,082M | **$5,502M** | Down $580M over 9M |
| Equity / assets | 31% | 36% | Thin, and loss-funded |
| Total liquidity (mgmt) | — | **$7.1B** | Incl. $5.5B cash + $1B VW term loan |
| FCF (period) | −$2,489M | **−$4,192M TTM** | Deteriorating |
| FCF yield | −15.91% (tool, stale mkt cap) | **≈ −22.0%** | Severe cash burn vs. market cap |
| FCF margin | −46.2% | **≈ −64.7%** | **Worsening despite revenue growth** |

*Note: the ratio tools report FY2025 (12/31/25) as "most recent annual," which lags the Q3 2026 filing by three quarters. I recomputed the Q3 2026 column from the quarterly statements.*

---

## 3. Market Risk Profile

| Metric | 730-day window | 1,095-day (3yr) window |
|---|---|---|
| Annualised volatility | **65.8%** | **68.5%** |
| Beta vs. SPY | 1.39 | **1.51** |
| Max drawdown | −49.1% | **−65.5%** |
| Sharpe ratio (rf=0) | 0.49 | **0.18** |

**Interpretation:** this is a high-beta, high-volatility, drawdown-prone equity. Company-reported beta is 1.62; measured 3-year beta is 1.51. The 3-year Sharpe of 0.18 means **holders have been paid essentially nothing for 68% annualized volatility** — the return stream is speculative optionality, not risk-compensated equity. At 1.5x beta, a 20% SPY drawdown mechanically implies roughly a **30% RIVN decline**, layered on top of company-specific ramp risk. The 65.5% peak-to-trough drawdown is the empirical base case for a bad scenario, not a tail case.

**Macro backdrop is unhelpful:** the yield curve as of 11/03/26 is upward-sloping but at high absolute levels (2Y 4.74%, 10Y 5.13%, 30Y 5.47%, 2Y-10Y spread +0.39, no inversion). A 10Y at 5.13% raises the discount rate on long-duration, cash-flow-negative growth equity and raises the cost of the *next* capital raise — directly relevant since Rivian is a repeat issuer.

---

## 4. Downside Scenario Analysis: Revenue −20%

**Baseline FY2026E:** 9M 2026 revenue $5,194M; Q4'25 actual $1,286M → **TTM revenue ≈ $6,480M**. Guidance: 67,000–70,000 deliveries; adj. EBITDA −$1.75B to −$1.85B; capex $1.4–1.5B.

**Trigger:** demand shock (tariff/credit-driven consumer pullback) or R2 ramp bottleneck — management itself flags supplier ramp limits and rising memory/electronics commodity costs.

| Line item | Baseline | Revenue −20% | Δ |
|---|---|---|---|
| Revenue | $6.48B | $5.18B | −$1.30B |
| Gross margin | ~8–10% (Q3 8.2%) | **−4% to −8%** | Fixed-cost deleverage; automotive GM goes negative |
| Gross profit | ~$0.55B | **−$0.25B to −$0.40B** | −$0.8B to −$0.95B |
| Adjusted EBITDA | −$1.80B | **−$2.6B to −$2.9B** | ~−$0.9B |
| Operating cash flow | ~−$2.9B | **−$3.7B to −$4.0B** | |
| Capex (discretionary) | $1.45B | $1.1B (deferrable) | Partially self-help |
| **FCF** | **−$4.2B** | **−$4.9B to −$5.2B** | |
| Ending liquidity ($7.1B start) | — | **$2.0B–$2.4B after 12 months** | |
| **Cash runway** | ~1.7 yrs | **~1.2–1.4 yrs** | |

**What breaks first:** liquidity does not run out in 2027, but the *financing window* closes before the cash does. At −$1.25B/quarter of FCF, Rivian must return to market within ~12 months — and it would be raising into a demand-shock tape at ~$13/share. A $2.5B raise at that price equals **~190M new shares, +13% dilution**, on top of the **+22% share count increase already booked in the first nine months of 2026** (1,186M → 1,446M shares) and **+56% since FY2022** (913M shares).

**Equity erosion path:** accumulated deficit is −$29.1B against $5.7B of book equity — *all* book equity is paid-in capital. At a ~$2.9B annual net loss run-rate, absent continuous issuance, book equity approaches zero around 2028 and could turn **negative**. That converts a "cash burn" story into a solvency story if the R2 gross-margin inflection fails.

**Partial offsets:** ~$4.5B DOE ATVM loan (downsized from $6.6B, available sooner per reports), $250M Uber equity investment expected by YE2026, ~$0.5B remaining VW JV commitment ($5.3B of $5.8B received) → management's **$13B "total available liquidity" target**. Note this is *availability*, not *cash*; the DOE facility is debt that worsens leverage if drawn.

---

## 5. Overall Financial Risk Rating: **HIGH**

*(Not "Critical": $7.1B liquidity, no 2026–2028 maturities, revenue +38% yoy, gross margin inflecting positive at 8.2%, adj. EBITDA guidance improved $100M. But firmly High: Altman distress, negative interest coverage, −22% FCF yield, and a funding model dependent on perpetual dilution.)*

**Direction of travel — the genuinely encouraging datapoints:**
- Revenue +38% yoy in Q3 2026; R2 best-seller in first full quarter; deliveries +46%.
- Gross margin from **2.7% (FY2025) → 8.2% (Q3 2026)**; automotive gross loss narrowed to −$80M from −$130M.
- Adjusted EBITDA loss narrowed to −$435M from −$602M yoy; guidance improved at the midpoint.
- Capex guided down $300M to $1.4–1.5B — real cash discipline.

**Direction of travel — the deteriorating datapoints:**
- **FCF burn accelerated**: FY2025 −$2.49B → TTM −$4.19B. Q3 2026 FCF −$1,124M vs −$421M a year earlier. FCF margin −46% → −65%.
- The FY2025 FCF figure was flattered by a **+$1.44B working-capital release**; in 9M 2026 working capital was a **−$687M drag**. Underlying cash consumption is worse than the FY2025 headline suggested.
- Operating cash flow −$779M (FY2025) → **−$1.95B annualized** in 2026; Q3 2026 CFO −$758M on adj. EBITDA of only −$435M.
- Stock-based compensation ~$830M annualized — a real, recurring, non-cash-but-dilutive cost.

---

## 6. Key Red Flags

1. **Altman Z of −2.255 — distress zone.** X2 = −1.81 driven by −$29.1B retained earnings. Not a marginal reading.
2. **Interest coverage −13.08x.** EBIT is deeply negative; debt service is funded from reserves.
3. **FCF yield −22% and FCF margin deteriorating to −65%** despite 38% revenue growth — growth is not yet translating into cash.
4. **Chronic dilution.** Shares +22% in 9M 2026, +56% since FY2022. Equity is raised, not earned. Each capital raise at ~$13 is destructive at scale.
5. **Working-capital tailwind exhausted.** The 2025 FCF number depended on a $1.44B WC release that has now reversed — do not extrapolate 2025 burn as "the bottom."
6. **Path to negative book equity.** With ~$2.9B annual losses and only $5.7B of (entirely paid-in) equity, solvency depends on continued access to capital markets at 5%+ long rates.
7. **Supplier/commodity concentration risk** — management explicitly cites R2 ramp constrained by slowest supplier and rising memory/electronics costs. A single-supplier failure stalls the entire gross-margin inflection.
8. **Beta 1.51 / vol 68% / 3yr Sharpe 0.18.** In a market drawdown this position amplifies losses ~1.5x with no historical risk compensation.

## Data Gaps (explicit)
- **No agency credit rating / CDS spread retrieved** — two searches returned only generic Moody's pages. The "Sub-Investment Grade" characterization is my inference from Altman, coverage, and cash-flow data, not a quoted rating. **Treat as unverified.**
- **No explicit contractual debt maturity ladder.** Short-term debt is $0 and LTD is $4.45B with 2029/2030 converts and a 10-year VW term loan; I could not retrieve a year-by-year maturity table or covenant package (DOE ATVM covenants in particular).
- **Peer benchmarking is not meaningful.** The tool returns mega-caps (AMZN, TSLA, HD, BABA, TM) — only TSLA and TM are Auto Manufacturers and both are profitable, investment-grade issuers. No valid EV-startup comparables (e.g., LCID) were available in the sector list.
- **Tool-reported ratios are FY2025-stale.** All `calculate_*` outputs predate the Q3 2026 filing by three quarters; I recomputed Q3 2026 figures manually. The FCF yield tool also uses a stale share count ($15.6B vs. actual ~$19.1B market cap).
- **TTM revenue derived** as Q4'25 + 9M'26 ($6,480M); Q1'25 and Q2'25 revenue were not returned, so a clean four-quarter comparison to prior-year TTM is unavailable.

**Bottom line:** Rivian is a well-liquified but structurally loss-making manufacturer whose credit profile sits in Altman's distress zone with negative interest coverage and a −22% FCF yield. The absence of near-term maturities and $7.1B of liquidity mean **bankruptcy is not the 2027 risk — dilution and equity impairment are.** The single variable that matters is whether R2 delivers a sustained positive automotive gross margin; Q3 2026 (8.2% blended gross margin, −$80M automotive gross loss) is genuine progress but not yet the inflection. Under a −20% revenue scenario, runway compresses to ~1.2–1.4 years and a dilutive raise at ~$13/share becomes near-certain.

# Fin Risk Analyst

- Symbol: RIVN
- Elapsed: 47.2s

---
# RIVN — Financial Risk Assessment
**Rivian Automotive, Inc.** | Consumer Cyclical / Auto Manufacturers | Latest data: **Q3 FY2026 (period ended 2026-09-30)** | Price $10.91, mkt cap ~$15.9B

> **Data note:** the ratio tools (`calculate_leverage_ratios`, `liquidity_ratios`, `z_score`, `f_score`, `fcf_yield`) keyed off **FY2025 annual (12/31/25)**. Since four quarters of FY2026 are now reported, I recomputed all risk metrics on a **TTM through Q3'26** basis below and show both. The `net_debt` field on the balance-sheet endpoint is internally inconsistent (Q3'26 shows $1.92B while cash $5.50B vs. debt $5.43B implies ~net cash); I use debt-minus-cash throughout.

## 1. Credit Risk Assessment — **Sub-Investment Grade (CCC/B-range profile, distress-zone metrics)**

Rivian is a pre-profit manufacturer burning ~$4.2B of free cash annually, with **never-once-positive** operating cash flow in its history as a public company. The credit is not serviceable from operations — interest is paid from the balance sheet. Mitigants are real but structural rather than earnings-based: a **$5.5B cash pile**, ~net-flat debt, **no maturities before the Oct-2030 green convertibles ($1.725B)**, a **$6.6B DOE ATVM facility**, and continued Volkswagen support (**$1B 10-yr term loan at 6.03% drawn Oct-2026**, on top of the $5.8B JV). Liquidity, not solvency, is the binding constraint.

## 2. Key Financial Risk Metrics

| Metric | Q3'26 / TTM | FY2025 (tool) | Assessment |
|---|---|---|---|
| Total debt | $5,431M | $6,651M | +$1.0B VW loan drawn Oct-26 post-period |
| Cash & ST investments | $5,502M | $6,082M | Peak was $9.37B (FY23) |
| Net debt | ~$(71)M (net cash) | $569M | Effectively neutral |
| Debt / equity | 0.95x | 1.45x | Equity shrank, then refilled by raises |
| Debt / assets | 0.35x | 0.45x | Moderate |
| Net debt / EBITDA | **n.m. (negative EBITDA −$1,811M)** | −0.22x | Ratio is meaningless — EBITDA < 0 |
| Interest coverage (EBIT/int.) | **−9.9x** (TTM EBIT −$2,694M / int. $271M) | −13.1x | **Cannot cover from operations** |
| Current ratio | 2.18x | 2.33x | Good |
| Quick ratio | 1.63x | 1.89x | Good, inventory-light support |
| Cash / current liabilities | 1.47x | 1.65x | Strong |
| Altman Z-Score | **−2.26 (Distress)** | −2.26 | Driven by X2 = retained earnings/assets −1.81 |
| Piotroski F-Score | **4 / 9 (Weak)** | 4 | Fails ROA, op CF, leverage, equity, dilution |
| FCF yield | **−26.4%** (on $15.9B cap); −19.2% per tool on stale $12.96B cap | −19.2% | Deeply negative |

**TTM P&L (Q4'25–Q3'26):** revenue $6,480M, **gross profit +$594M (+9.2%)**, SG&A $1,850M, EBIT −$2,694M, net income −$2,973M, D&A $883M, SBC $776M.

**The one genuinely improving line — gross margin:** FY22 −188%, FY23 −45.8%, FY24 −24.1%, FY25 +2.7%, **TTM +9.2%**, with four consecutive positive gross-profit quarters ($120M → $119M → $179M → $176M). Operating margin, however, remains **−41.6% TTM** (−66.6% in FY25): fixed costs — R&D ~$485M/qtr and SG&A — swamp gross profit.

## 3. Market Risk Profile
| Metric | Value |
|---|---|
| Annualised volatility (3Y) | **65.5%** (~4x market) |
| Beta vs SPY — computed / reported | **1.40** / 1.64 |
| Max drawdown (3Y window) | **−51.3%** |
| Sharpe (rf = 0%) | 0.31 |
| Sortino | Not available — data gap, no downside-deviation output from tool |

A beta of 1.4–1.6 on 65% vol means a −20% market drawdown plausibly maps to **−30% to −45%** in RIVN, on top of idiosyncratic execution risk. The 0.31 Sharpe is a *return* statistic on a stock that is roughly flat-to-down over three years — it is not evidence of risk-adjusted quality.

## 4. Downside Scenario: Revenue −20% (≈ $5.18B TTM)
Applied to the TTM base with ~88% variable cost of revenue and fixed-cost absorption loss:

| Line | Base (TTM) | −20% Revenue | Δ |
|---|---|---|---|
| Revenue | $6,480M | $5,184M | −$1,296M |
| Gross profit (margin) | $594M (9.2%) | **−$620M (−12%)** | −$1,214M |
| EBITDA | −$1,811M | **−$2,800M** to −$3,100M | −$1.0 to −1.3B |
| EBIT | −$2,694M | ~−$3,700M to −$4,000M | — |
| Interest coverage | −9.9x | **~−14x** | Worse |
| FCF | −$4,192M | **−$4.8B to −$5.2B** | −$0.6 to −1.0B |
| Quarterly burn | ~$1,048M | **~$1,200–1,300M** | — |

**Cash runway under stress:** $5,502M + $1.0B VW loan ≈ $6.5B / ~$1.25B per quarter ≈ **5 quarters (~Q1 2028)** before external funding is required — versus ~6.2 quarters in the base case (year-end 2027). The DOE $6.6B ATVM facility (construction-tied, phased draws for the Georgia plant) and further VW JV tranches are the swing factor between "funded through R2 ramp" and "emergency equity raise." A stress case likely forces a **$2–3B equity/convertible raise at depressed prices — roughly 15–20% dilution** — which is exactly the pattern already visible: shares outstanding went **913M (FY22) → 1,446M (Q3'26), +58%** in under four years. Covenants: the converts are unsecured with no maintenance tests; **DOE facility financial covenants are not disclosed in my data — explicit gap.**

## 5. Overall Financial Risk Rating: **HIGH**
Not *Critical*, because liquidity genuinely covers ~6 quarters of base-case burn, debt is roughly net-neutral, and there is no maturity wall until 2030. But earnings-based credit metrics are unambiguously distress-zone: negative EBITDA, −10x interest coverage, Z-score of −2.26, F-score of 4, and negative FCF yield of −26%. This is a **liquidity-underwritten credit, not a cash-flow-underwritten one**. The thesis lives or dies on gross margin continuing to climb fast enough that operating leverage turns EBITDA positive before the balance sheet is exhausted — against a 20% revenue shock, that timeline breaks and dilution becomes the base case.

## 6. Key Red Flags
1. **Never generated positive operating cash flow.** Five straight years of negative CFO (−$5.05B, −$4.87B, −$1.72B, −$0.78B, TTM −$2.63B). FY25's improvement did *not* persist into FY26.
2. **Burn is re-accelerating.** FY25 FCF −$2.49B steady-state, but **TTM FCF −$4.19B** (Q1'26 −$1.08B, Q2 −$0.85B, Q3 −$1.12B) — worse despite revenue +38% y/y. Growth is consuming cash, not generating it.
3. **Persistent dilution as a funding model:** +58% share count since FY22; SBC $776M TTM (~12% of revenue) — F-score marks zero on both F6 and F7.
4. **Interest expense tripled** ($103M FY22 → $271M TTM) and now exceeds gross profit's contribution at a 4x multiple.
5. **Retained earnings −$29.1B** against $15.7B of assets — the Altman X2 of −1.81 alone sinks the score, and it worsens every quarter.
6. **Liabilities up $1.6B since FY25** ($8.85B → $10.01B) while equity fell then was replenished by issuance — funding growth with obligations.
7. **Inventory build** ($1.54B → $1.78B over two quarters) into the R2 ramp; a demand miss converts this to write-down risk.
8. **Market-risk overlay:** 65% vol, beta 1.4–1.6, −51% max drawdown — the equity offers no defensive characteristics if the cycle turns.

**Explicit data gaps:** (a) DOE ATVM covenant package and remaining undrawn capacity; (b) full debt maturity ladder — I confirmed the $1.725B 2030 green converts and the converted 2026 VW note but cannot rule out a 2027/2029 tranche from available filings; (c) CDS spreads and formal agency ratings unavailable; (d) Sortino ratio; (e) FY2026 capex and liquidity guidance (the Q3 press release page returned no body text — JS-rendered).

# Fin Risk Analyst

- Symbol: GOOG
- Elapsed: 29.8s

---
I have all the data I need. The volatility tool was unavailable on the plan, so I computed market-risk statistics directly from the 3-year daily price series. Writing the assessment now.

---

# GOOG (Alphabet Inc.) — Financial Risk Assessment
*Data as of FY2025 (period end 2025-12-31); price data through 2025-12-31. Sector: Communication Services / Internet Content.*

## 1. Credit Risk Assessment — **INVESTMENT GRADE (highest quality)**
Alphabet is a net-cash, fortress-balance-sheet borrower. Leverage is negligible, interest coverage is effectively unbounded, and the Altman Z-Score sits deep in the safe zone. There is no plausible near-term credit-stress path.

- **Net cash position:** $126.8B cash & ST investments vs. $59.3B total debt → **net cash ≈ $67.6B** (net debt/EBITDA **−0.37x**). Even counting operating-lease liabilities (~$28.6B implied), leverage stays trivial.
- **Interest coverage:** EBIT $159.6B / interest $0.74B ≈ **217x** (tool-reported **175x**) — no debt-service risk whatsoever.
- **Altman Z-Score: 3.92** (safe zone; >2.99), with book-equity x4 of 2.31.

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Debt / Equity | 0.14 | Very low |
| Debt / Assets | 0.10 | Very low |
| Net Debt / EBITDA | **−0.37x** | Net cash |
| Interest Coverage (EBIT/int.) | **175x** (calc ~217x) | Airtight |
| Current Ratio | 2.01 | Strong |
| Quick Ratio | 2.01 | Strong (no inventory) |
| Cash Ratio | 1.23 | Strong |
| Working Capital | $103.3B | Ample |
| Cash / Liabilities | 0.70 | Strong |
| Equity / Assets | 0.70 | Conservative |
| Altman Z-Score | 3.92 | Safe |
| **Piotroski F-Score** | **6 / 9** | Moderate |
| FCF Yield | 1.86% | Low (valuation-driven) |
| Operating Margin | 32.0% | Elite |
| ROA / profitability | Positive | — |

**Piotroski detail (6/9):** loses points on *leverage increase* (F5=0 — total debt rose to $59.3B from $25.5B and assets grew via heavy capex), *ROA improvement* (F3=0), and *asset-turnover improvement* (F9=0). These are growth-capex artifacts rather than deterioration signals — the balance sheet remains net-cash. Gains on positive ROA, positive operating cash flow, accruals quality, positive equity change, no dilution, and gross-margin improvement.

**FCF sustainability:** FCF $73.3B (flat vs. $72.8B prior year) despite capex nearly doubling to **$91.4B** (2024: $52.5B) — AI/infrastructure buildout. FCF is *stable but not growing* because capex consumes the OCF surge (OCF $164.7B). FCF margin ~18.2% and holding; the risk is capex escalation, not demand. Buybacks ($45.7B) + dividend ($10.0B) are funded from cash flow and cash pile, not debt.

## 3. Market Risk Profile
*Volatility tool unavailable on plan — the following are computed directly from the 3-yr daily adjusted-close series (2022-12-01 → 2025-12-31).*

| Metric | Estimate |
|---|---|
| Annualised volatility | **~30%** (estimated) |
| Beta vs. S&P 500 | **1.20** (vendor-reported) |
| Max drawdown (close basis) | **≈ −26%** (peak $197.00 on 2024-12-16 → trough $145.88 on 2025-04-08) |
| 3-yr price return | ~+212% ($100.32 → $313.18); CAGR ≈ **45%** |
| Sharpe (0% rf, est.) | **≈ 1.3–1.5** |
| Sortino | materially higher (~2+) given upside skew |

Character: a high-beta, momentum-driven mega-cap with a roughly 30% annualised vol. The stock suffered a ~26% drawdown into April 2025, then rallied ~120% off that low — extreme two-way price risk is the dominant market exposure, not credit. Beta 1.20 means a 20% market selloff implies ~24% downside on the equity.

## 4. Downside Scenario — Revenue −20%
Applying a −20% revenue shock to FY2025 ($402.8B → **$322.3B**), modeling cost-of-revenue as variable (~−20%), SG&A + R&D held largely fixed:

| Line item | Base FY2025 | Revenue −20% | Change |
|---|---|---|---|
| Revenue | $402.8B | $322.3B | −20% |
| Gross profit | $240.3B | ~$192.3B | −20% |
| Operating income | $129.0B | **~$81B** | −37% |
| Operating margin | 32.0% | **~25.1%** | −7 pts |
| EBITDA | $180.7B | ~$102B | −44% |
| Net income | $132.2B | **~$64B** | −51% |
| Interest coverage | 175x | ~110x | Still enormous |
| Net debt/EBITDA | −0.37x | still **net cash** | — |
| FCF | $73.3B | **$20–40B** (capex cut assumed) | Lower but positive |

**Conclusion:** Even a severe 20% revenue decline leaves Alphabet *highly profitable* (~25% operating margin), **net-cash**, with coverage >100x and materially positive FCF. No covenant is remotely threatened; no refinancing cliff. The company would comfortably survive a prolonged downturn — the operational leverage on margins is the only meaningful sensitivity, and it takes an extreme shock before earnings pressure becomes a balance-sheet event.

## 5. Overall Financial Risk Rating: **LOW**
Balance-sheet, liquidity, and credit risk are among the lowest in the market. The only material risks are *market/valuation risk* (high beta, ~26% historical drawdowns) and *capex-intensity risk* to FCF (capex up 74% YoY), neither of which threatens solvency.

## 6. Key Red Flags / Watch Items
- **Capex escalation:** capex $91.4B (2025) vs $52.5B (2024) — AI buildout compressing FCF to flat growth. Watch whether FCF margin holds.
- **Rising absolute debt:** total debt up to $59.3B from $25.5B — still immaterial given the cash pile, but the trajectory cost Piotroski points (F5).
- **Valuation / price risk:** low FCF yield (1.86%) and high beta (~1.2) mean the equity is priced for continued growth; a sentiment or rate shock is the real risk vector, not fundamentals.
- **Regulatory/antitrust & AI-disruption of Search** — business-model risk outside the financial statements.

**Data gaps flagged:** (1) `calculate_price_volatility` tool returned an availability error — vol/Sharpe/Sortino are hand-computed estimates from the daily series and should be treated as approximate; max drawdown and beta are reliable. (2) No credit rating/CDS spread data available. (3) Balance-sheet "net_debt" field (+$28.6B) conflicts with the liquidity view (−$67.6B net cash); the difference is operating-lease treatment — either way, leverage is immaterial.

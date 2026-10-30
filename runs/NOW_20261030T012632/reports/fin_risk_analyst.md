# Fin Risk Analyst

- Symbol: NOW
- Elapsed: 22.4s

---
I have sufficient data across credit, liquidity, cash flow, and market risk. Writing the assessment.

---

# ServiceNow (NOW) — Financial Risk Assessment

**As of:** latest close $109.67 (2026-10-29) | **Market cap:** ~$113.4B | **Sector:** Technology / Application Software
*Note on data: the price series ($109.67) and share count (1.037B) reconcile to the reported $113B market cap, so figures are internally consistent. Per-share levels appear adjusted; ratios and percentage moves are unaffected.*

## 1. Credit Risk Assessment — **INVESTMENT GRADE (strongest quartile on balance sheet)**

ServiceNow is a **net-cash** business. It carries only $2.40B of total debt against $6.28B of cash and short-term investments, producing **net cash of ~$3.9B** and **net debt/EBITDA of −1.29x**. Interest expense is just $23M against $1.82B operating income — **interest coverage of 79.3x**. There is effectively no solvency or refinancing risk. The debt is overwhelmingly long-term ($1.49B long-term, $0 short-term), so there is **no near-term maturity cliff**.

The one negative reading is the **Altman Z-Score of 1.675 ("Distress" zone)**, but this is a **known model artifact** for asset-light SaaS: the score is dragged down by near-zero working capital (X1 = 0.001) and low asset turnover (X5 = 0.51) because deferred revenue inflates current liabilities and the business needs little capital. With net cash and 79x coverage, the Z-score overstates bankruptcy risk here. It should be flagged, not taken at face value.

## 2. Key Financial Risk Metrics

| Metric | Value (FY2025) | Assessment |
|---|---|---|
| Debt / Equity | 0.19x | Very low |
| Net Debt / EBITDA | **−1.29x (net cash)** | Fortress |
| Interest Coverage (EBIT/Int.) | **79.3x** | Exceptional |
| Debt / Assets | 0.09x | Very low |
| Current Ratio | 1.00x | Adequate (deferred-revenue skew) |
| Quick Ratio | 1.00x | Adequate |
| Cash Ratio | 0.60x | Healthy |
| Working Capital | $28M | Thin, but not stressed |
| Cash & ST Investments | $6.28B | Large buffer |
| Altman Z-Score | 1.675 (Distress) | ⚠️ Model artifact for SaaS |
| Piotroski F-Score | 5 / 9 (Moderate) | Mixed |
| FCF (FY25) | $4.58B | Strong |
| FCF Margin | **34.5%** | Excellent |
| FCF Yield | 3.99% | Solid |

**Trend (income statement):** Revenue $7.25B → $8.97B → $10.98B → $13.28B (FY22–FY25), ~22% CAGR. Operating margin expanded **4.9% → 8.5% → 12.4% → 13.7%** — clear operating leverage. **FCF: $2.17B → $2.70B → $3.42B → $4.58B** (+34% YoY). This is a high-quality, self-funding cash generator.

**F-Score detail (score 5):** Positives — positive ROA, positive operating cash flow, accruals quality, falling leverage, positive equity change. Negatives — ROA not improving (6.7% vs 7.0%), **share dilution (0 pts)**, no gross-margin improvement, no asset-turnover improvement. The dilution and SBC (=$1.96B, ~15% of revenue) are the notable soft spots.

## 3. Market Risk Profile — **HIGH**

| Metric | Value |
|---|---|
| Annualized Volatility (3Y) | **51.8%** |
| Beta vs SPY | 1.145 |
| Max Drawdown (3Y) | **−64.5%** |
| Sharpe Ratio (0% RF) | **−0.11** |

Unlike the balance sheet, the **equity is high-risk**. The stock peaked at ~$234 (Jan 2025) and bottomed at ~$83 (Apr 2026) — a **−64.5% drawdown** — before recovering to $109.67 (still ~−53% from peak). Volatility of ~52% annualized is roughly 3x the market, and beta of 1.15 understates sensitivity because of the large idiosyncratic risk. **Sharpe is negative** (−0.11): the stock has delivered negative risk-adjusted returns over the window. Several violent single-day gaps (−27% on 2026-10-29, −18% on 2026-04-23, −10% on 2026-07-22) point to **earnings/guidance-driven tail risk** — the dominant threat is valuation and growth-sentiment, not credit.

## 4. Downside Scenario — Revenue −20%

Applying −20% to FY25 revenue ($13.28B → $10.62B), gross margin ~77.5%:

- **Gross profit:** $10.30B → ~$8.24B (−$2.06B).
- **Fixed/cost flex:** total opex ~$8.47B. With **10% cost cuts** → ~$7.62B: operating income ≈ **$0.61B** (5.8% margin) vs $1.82B.
- **No cost cuts:** operating income ≈ **−$0.24B** (slight operating loss).
- **Debt service:** trivial — $23M interest is covered by interest income on the $6.3B cash pile; net cash position *increases* coverage.
- **Cash flow:** even with a mild loss, the $1.96B SBC add-back and deferred-revenue model keep **FCF positive (roughly $1.5–2.5B)**. No covenant, liquidity, or refinancing stress.

**Conclusion:** A 20% revenue shock dents earnings and FCF but the company **survives comfortably** on its $3.9B net cash and minimal debt. The risk in this scenario is **valuation de-rating and multiple compression**, not solvency.

## 5. Overall Financial Risk Rating: **MODERATE**

Split verdict: **Balance-sheet/credit risk = LOW** (net cash, 79x coverage, no maturities); **equity/market risk = HIGH** (52% vol, −64% drawdown, negative Sharpe). Blended: **Moderate financial risk**, driven almost entirely by market/valuation risk rather than fundamental credit deterioration.

## 6. Key Red Flags

1. **Severe equity drawdown & tail risk** — −64.5% peak-to-trough; multiple double-digit single-day gaps (including −27% on 2026-10-29). High valuation (P/B ~8.7x) leaves little room for growth disappointments.
2. **Stock-based compensation dilution** — SBC $1.96B (~15% of revenue) and rising share count cost the F-Score its dilution point; cash-flow quality is flattered by SBC add-backs.
3. **Altman Z in "distress" zone** — model artifact, but a flag if a lender/investor applies it mechanically.
4. **Thin working capital / current ratio of 1.0** — driven by large deferred revenue; not a cash risk but a watch item.
5. **Growth dependence** — the −20% scenario shows a mild cost-cut assumption still halves operating income; the equity's value rests heavily on revenue durability.

**Mitigants:** Net cash of $3.9B, 79x interest coverage, 34.5% FCF margin, expanding operating margins, and a $4.6B annual FCF engine give the company exceptional staying power through a prolonged downturn.

**Data gaps:** No credit rating / CDS spread available via tools; peer-multiple context not gathered (budget). Altman and Piotroski rely on the tool's standard inputs and may embed model-specific adjustments.

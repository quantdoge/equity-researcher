# Fin Risk Analyst

- Symbol: EXPE
- Elapsed: 127.5s

---
I have sufficient data to complete the assessment. The peer set returned is a broad Consumer Cyclical universe (Amazon, Tesla, Home Depot) rather than OTA-specific comps, so I'll flag that as a limitation rather than draw misleading comparisons.

---

# EXPE — Expedia Group, Inc. | Financial Risk Assessment

**Sector:** Consumer Cyclical — Travel Services | **Price:** $285.64 | **Market Cap:** ~$32.7B | **Beta (reported):** 1.36

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (BBB / BBB-)**

Expedia carries investment-grade ratings: **S&P "BBB" (stable, affirmed March 2025)** and **Fitch "BBB-"**, with recent senior unsecured issuance ($1.0B 5.50% notes due 2036). Despite a high **book debt-to-equity of 2.62x**, this is an artifact of a thin book equity base ($2.55B against $24.5B assets) rather than genuine over-leverage. On a net basis the company holds a **net cash position** (~-$627M net debt, i.e., net debt/EBITDA of **-0.27x**), and interest coverage of **6.26x** is comfortable. The debt stack ($6.67B total) is well covered by $7.30B of cash and short-term investments. Credit trajectory is stable; no covenant or refinancing pressure evident.

## 2. Key Financial Risk Metrics Table

| Metric | Value | Assessment |
|---|---|---|
| Debt / Equity (book) | 2.62x | Elevated but book-equity distortion |
| Debt / Assets | 0.27x | Low — conservative |
| Net Debt / EBITDA | **-0.27x** | Net cash — no leverage risk |
| Interest Coverage (EBIT/Int.) | **6.26x** | Adequate (>5x threshold) |
| Current Ratio | 0.73x | **Weak — below 1.0** |
| Quick Ratio | 0.73x | Weak (asset-light, no inventory) |
| Cash Ratio | 0.44x | Acceptable |
| Working Capital | **-$4,458M** | Negative (structural — deferred bookings) |
| Altman Z-Score | **0.843** | Distress zone (distorted — see note) |
| Piotroski F-Score | **5 / 9** | Moderate |
| FCF Yield | **8.25%** | Strong |
| Total Debt | $6.67B | ST $1.69B / LT $4.72B |
| Cash & ST Investments | $7.30B | Fully covers ST debt |

**Critical interpretive note on the Z-Score:** The 0.843 "Distress" reading is heavily distorted by EXPE's structurally **negative working capital** (X1 = -0.18), which is normal for an online travel agency that collects cash from travelers before paying suppliers. The Altman model was not designed for negative-working-capital, asset-light platform businesses. The tool itself flags that X4 uses book equity rather than market cap, further understating health. The genuine credit picture — net cash, 6.3x coverage, BBB rating — is far stronger than the raw Z-score implies.

## 3. Market Risk Profile — **ELEVATED**

| Metric | Value |
|---|---|
| Annualised Volatility (252d) | **50.84%** |
| Beta vs SPY (calculated) | 0.857 |
| Beta (profile reported) | 1.362 |
| Max Drawdown (3yr) | **-37.16%** |
| Sharpe Ratio (0% Rf) | 0.145 |

High absolute volatility (~51%) with a **37% peak-to-trough drawdown** reflects the cyclical, sentiment-driven nature of travel demand. Note the **beta discrepancy**: the calculated 0.857 vs SPY over 252 days conflicts with the reported 1.362. The calculated figure likely understates true sensitivity because the measurement window may have missed the sharp COVID-style travel drawdown episodes; the reported 1.36 is the more appropriate long-run cyclical beta. A Sharpe of 0.145 is poor risk-adjusted compensation. With the 10Y yield at 4.99% (yield curve as of 2026-10-22, +34bp 2s10s, **not inverted**), the equity risk premium offered is thin relative to a ~5% risk-free rate.

## 4. Downside Scenario Analysis — 20% Revenue Decline

Modeled on FY2025 base: Revenue $14.73B, EBITDA $2.30B (15.6% margin), EBIT/OpInc $1.87B (12.7%), interest expense $299M, FCF $3.11B.

| Line Item | Base | -20% Revenue | Commentary |
|---|---|---|---|
| Revenue | $14.73B | **$11.79B** | Travel demand shock (recession/pandemic) |
| Operating margin | 12.7% | ~8.0% | Fixed-cost operating deleverage |
| Operating income | $1.87B | **~$0.94B** | Still positive |
| EBITDA | $2.30B | **~$1.3–1.5B** | Margin compression |
| Interest expense | $299M | $299M | Fixed |
| Interest coverage | 6.26x | **~3.1x** | Drops but remains serviceable |
| Net income | $1.29B | **~$0.45–0.50B** | Positive |
| Free cash flow | $3.11B | **~$1.5–2.0B** | Working-capital unwind partly offsets |
| Net debt/EBITDA | net cash | **still ~net cash/lightly levered** | No breach risk |

**Conclusion:** Even under a severe 20% revenue shock, EXPE remains profitable, generates positive FCF, and retains its net-cash balance sheet. The main risk is **margin compression and earnings volatility**, not solvency. Interest coverage would fall to ~3x — tighter but not covenant-threatening. The company has ample liquidity ($7.3B cash vs $1.69B near-term debt) and demonstrated COVID-era resilience. The real vulnerability is **earnings/valuation risk**, not balance-sheet survival risk.

## 5. Overall Financial Risk Rating — **MODERATE**

Balance-sheet risk is genuinely **Low** (net cash, investment-grade, strong FCF, ample liquidity). The rating is lifted to **Moderate** by: (a) high cyclical revenue exposure to discretionary travel, (b) elevated share price volatility and deep drawdowns, (c) structurally weak reported liquidity ratios (current ratio 0.73), and (d) thin book equity that flatters leverage optics. For a pure solvency lens, this is a low-risk credit; for equity holders, earnings volatility and a ~51% vol profile warrant a Moderate designation.

## 6. Key Red Flags

1. **Current ratio 0.73 and negative working capital (-$4.46B)** — while normal for OTAs (deferred bookings), it means reported liquidity metrics look alarming and the company relies on continued booking cash flow; a demand freeze stresses this.
2. **Altman Z-Score in distress zone (0.843)** — genuinely misleading for this business model, but worth monitoring and disclosing.
3. **Volatility ~51% with -37% max drawdown** — high equity risk; poor Sharpe (0.145) means holders aren't well compensated for the risk taken.
4. **Aggressive capital returns** — $1.93B buybacks + $200M dividends in FY2025 exceed net income, funded partly by working capital; sustainable only while FCF remains robust.
5. **Thin book equity ($2.55B, 10% of assets)** — leverage ratios are optically high; a large goodwill impairment ($7.69B intangibles) or downturn could rapidly erode equity.

**Data gaps flagged:** (1) The yield curve was successfully retrieved but only reflects one snapshot (2026-10-22); (2) Peer set returned broad Consumer Cyclical names (AMZN/TSLA/HD), not OTA-specific comps (BKNG, ABNB, TRIP) — no peer-multiple benchmarking performed; (3) Detailed debt maturity ladder by year not available beyond ST/LT split; (4) No CDS spread data available — credit risk inferred from ratings only.

# Fin Risk Analyst

- Symbol: BABA
- Elapsed: 80.0s

---
# BABA — Complete Financial Risk Assessment

**Alibaba Group Holding Ltd. | Consumer Cyclical / Specialty Retail | China (US ADR)**
Market cap ~US$245.6bn · Price US$105.36 · Focal period FY2026 (ended 31-Mar-2026) + Q1 FY2027 (30-Jun-2026)
*All financials in CNY bn unless stated. Assumed FX USD/CNY ≈ 7.10 (assumption, not from tool).*

---

## 1. Credit Risk Assessment

**Rating: Investment Grade — but on Negative Watch**

Solvency is not the problem; cash *generation* is. The balance sheet remains a net-cash position: at 30-Jun-2026, cash + short-term investments of **CNY 428.4bn** against total debt of **CNY 266.6bn** = **net cash of ~161.8bn (≈US$22.8bn)**. Debt/equity is 0.23 and debt/assets 0.14 — the lowest leverage of any large-cap comp examined. Interest expense of ~CNY 9.8bn is covered **6.1x on operating income** and **14.2x on EBIT**. Maturities are benign: only CNY 30.6bn (11% of debt) is short-term, and the two known convertible issues — **0.50% notes due June 2031** and a **US$3.2bn convertible due September 2032** — sit far outside any refinancing cliff at negligible coupons.

What downgrades the *trajectory*: operating income fell from CNY 140.9bn (FY25) to 59.7bn (FY26), a 58% collapse, and TTM operating income is now only **CNY 44.0bn on CNY 1,044bn of revenue (4.2% margin)**. Total debt has risen 36% in two years (195.6 → 266.6bn) while equity is flat, and free cash flow has been negative for four consecutive quarters. Altman Z of **2.25** (grey zone) and a **Piotroski F-score of 4/9** both say the same thing: not distressed, but deteriorating.

---

## 2. Key Financial Risk Metrics

| Metric | FY2024 | FY2025 | FY2026 | Q1 FY27 / TTM | Assessment |
|---|---|---|---|---|---|
| Revenue | 941.2 | 996.3 | 1,023.7 | 268.2 / 1,044.2 | Stalling (+2.7%, then +8.3%) |
| Operating income | 113.4 | 140.9 | 59.7 | 19.3 / **44.0** | **Severe deterioration** |
| Operating margin | 12.0% | 14.1% | 5.8% | 7.2% / **4.2%** | Below cost of capital |
| Net income | 80.0 | 130.1 | 103.6 | 10.6 / 73.5 | Supported by non-op gains |
| EBITDA (reported) | 164.0 | 190.2 | 186.3 | — | Inflated by investment gains |
| Operating cash flow | 184.0 | 164.8 | 76.2 | 22.9 / **77.9** | **−63% in 2 yrs** |
| Capex | (33.2) | (86.7) | (126.9) | (67.7) / **(155.5)** | Step-change, 15% of revenue |
| **Free cash flow** | **+150.8** | **+78.2** | **(50.7)** | (44.7) / **(77.5)** | **Negative 4 straight qtrs** |
| Debt / Equity | 0.18 | 0.23 | 0.23 | 0.24 | Low |
| Net debt / EBITDA | net cash | net cash | **−0.53x** | net cash | Strong |
| Interest coverage (EBIT) | — | — | 14.2x | 6.1x on op. income | Adequate |
| Current ratio | — | — | 1.28 | **1.36** | Adequate |
| Quick / cash ratio | — | — | 1.28 / 0.75 | 1.36 / **0.80** | Adequate |
| Working capital | — | — | +133.9 | +192.7 | Positive |
| Altman Z-Score | — | — | **2.25 (Grey)** | ~2.62 mkt-cap adj.* | Grey zone |
| Piotroski F-Score | — | — | **4/9 (Weak)** | — | Fails ROA trend, accruals, leverage, margins, turnover |
| Goodwill + intangibles | 286.7 | 276.8 | 263.4 | 259.2 | 23% of equity — impairment risk |

\*Substituting market cap (≈CNY 1.74tn) for book equity in x4 lifts Z to ~2.62 — still grey, upper end.

**Peer context (latest annual):**

| | Debt/Equity | Net Debt/EBITDA | Int. Coverage | Op. Margin | FCF Yield |
|---|---|---|---|---|---|
| **BABA** | **0.23** | **−0.53x** | 6.1x | 5.8% | **−2.9%** (corrected) |
| AMZN | 0.37 | 0.18x | 35.2x | 11.2% | 0.27% |
| HD | 5.10 | 2.54x | 8.7x | 12.7% | 3.59% |

**The critical read-across:** BABA is the *least* levered of the three and yet the only one with negative FCF. The risk has migrated off the balance sheet and onto the income statement and cash flow statement.

> ⚠️ **Data-quality flag:** the FCF-yield tool returned **−20.02%** by dividing CNY-denominated FCF by a USD market cap without FX conversion. Corrected, FY2026 FCF yield is **≈ −2.9%** (−50.7bn CNY ÷ ~1,743bn CNY market cap); TTM is **≈ −4.4%**. Separately, the balance-sheet `net_debt` field (86.1bn / 81.1bn) does not reconcile to cash+STI less total debt (−98.6bn / −161.8bn); the leverage tool's figure is the correct one.

---

## 3. Market Risk Profile

| Measure | Value | Comment |
|---|---|---|
| Annualised volatility (3y) | **45.7%** | ~2.5–3x a broad equity index |
| Beta vs SPY (756d) | 0.82 | vs profile long-run beta 0.40 — divergent; use 0.82 |
| Max drawdown (3y) | **−49.5%** | Peak close 187.62 (2-Oct-25) → trough 94.81 (26-Jun-26) |
| Current vs 3y peak | **−43.8%** | Price has slid further to 105.36 (Jul-26: 122.25) |
| Sharpe ratio | 0.49 (0% rf) | ≈0.39 at the actual 4.74% T-bill — positive but thin |
| Sortino ratio | **Not available** | Data gap |
| Implied systematic share of variance | **~8%** | Beta 0.82 × ~16% market vol ⇒ **~90%+ idiosyncratic** |

**Interpretation:** a beta of 0.82 badly understates the risk. Roughly nine-tenths of BABA's variance is company- and country-specific — AI capex returns, China consumption, ADR/VIE and geopolitical risk — not market direction. Hedging with index shorts will not protect a holder. Macro backdrop is unhelpful but not acute: US 10Y at **5.13%**, 2s10s **+39bp (no inversion)**, which raises the hurdle rate for a negative-FCF ADR without signalling imminent recession.

---

## 4. Downside Scenario Analysis — Revenue −20%

Applied to TTM revenue of CNY 1,044bn (op. income 44.0bn, 4.2% margin, gross margin 39.8%, opex ~372bn):

| Scenario | Op. income | FCF | Net cash & runway | Verdict |
|---|---|---|---|---|
| **Base (TTM)** | 44.0 | −77.5 | +161.8 → 2.1 yrs | Negative cash cycle |
| **A: −20% rev, GM held, opex −10%, capex cut to 80bn** | **≈ (2.0)** | ≈ (60) to (70) | +161.8 → **2.3–2.7 yrs** | Survivable; near breakeven operations |
| **B: −20% rev with capex held at Q1 FY27 run-rate (271bn)** | ≈ (2.0) | ≈ **(260)** | Net cash erased in **~7 months**; must issue ≥150bn or cut capex | Rating-negative, equity-dilutive |
| **C: −30% rev, GM −300bp, capex held** | ≈ (40) | ≈ (280) | Net debt within 12 months | Distress unlikely (asset stakes, converts); downgrade to BBB highly likely |

**Key sensitivity:** every 100bp of gross margin is worth ~CNY 10.4bn of operating income — i.e., **a 4-point gross-margin erosion alone wipes out the entire current operating profit**. The company has lost its margin cushion. But even in the harshest case, cash interest of ~9.4bn is covered ~17x by cash on hand, so no default/refinancing event is plausible inside 24 months. The binding constraint is *funding the capex program*, and capex is ~100% discretionary: a 50% capex cut restores positive FCF immediately.

---

## 5. Overall Financial Risk Rating: **MODERATE** (trend: deteriorating)

- **Solvency / liquidity risk: LOW.** Net cash 161.8bn, 11% short-term debt maturities, 0.80 cash ratio, minimal-coupon converts to 2031/2032.
- **Cash-flow / earnings risk: HIGH.** Negative FCF, 4.2% TTM operating margin, OCF down 63% in two years, 45.7% volatility, Piotroski 4/9.
- **Equity risk: HIGH.** −43.8% from peak; 90%+ idiosyncratic.

I would move this to **High** if TTM operating margin prints below 3% or a fifth consecutive negative-FCF quarter is reported while capex intensity stays above 20% of revenue.

---

## 6. Key Red Flags

1. **Free cash flow negative four quarters running** (−77.5bn TTM); FY2026 was the first negative FCF year in the dataset. Capex up 4.7x in two years (33bn → 155bn TTM).
2. **Operating margin collapse: 14.1% → 5.8% → 4.2% TTM**, including an operating *loss* of CNY 0.85bn in Q4 FY2026. Depreciation from the AI/cloud build is now a permanent P&L burden.
3. **Earnings quality:** FY2026 pre-tax profit depended heavily on non-operating/investment gains (EBIT 139.2bn vs operating income 59.7bn). The Piotroski accruals test fails (F4 = 0).
4. **Operating cash flow −63% in two years** (199.9bn FY23 → 77.9bn TTM). Cash generation, not leverage, is the constraint.
5. **Capex run-rate outrunning

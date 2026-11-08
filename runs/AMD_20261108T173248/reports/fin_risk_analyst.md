# Fin Risk Analyst

- Symbol: AMD
- Elapsed: 70.6s

---
# AMD — Financial Risk Assessment
**As of latest data: Q3 FY2026 (period ended 2026-09-26); market cap ≈ $733.0B; price $449.04**

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (High Quality) — Moody's A1, S&P 'A' (both upgraded in 2025)**

AMD is, on credit measures, one of the strongest balance sheets in the semiconductor industry. The company carries a **net cash position**, not net debt.

| Measure | Value | Read |
|---|---|---|
| Total debt | $4.47B | Trivial vs. scale |
| Cash & ST investments | $10.55B | — |
| **Net debt** | **–$6.08B (net cash)** | Net cash, not leverage |
| Debt / equity | 0.07x | Effectively unlevered |
| Debt / assets | 0.06x | — |
| Gross debt / EBITDA | 0.61x (FY25) | 0.40x on TTM EBITDA |
| Net debt / EBITDA | **–0.84x** | Net cash |
| Interest coverage | 28.2x (EBIT basis, tool); **48x on TTM EBIT $8.27B / $172M** | Minimal debt service burden |
| Altman Z-Score | **3.742 — Safe zone** | See caveat below |
| Piotroski F-Score | **8 / 9 — Strong** | Only miss: F5 (leverage rose) |

Debt rose from $2.21B (FY24) to $4.47B (FY25) and further via an **August 2026 senior unsecured notes issuance (424B5)**, which is the sole reason F5 failed. This is opportunistic term-debt issuance at an 'A' rating, not distress funding — the proceeds sit alongside $10.6B of cash and a $17.5B working capital position.

**Altman Z caveat (analytical adjustment):** The 3.742 score is driven almost entirely by x4 (book equity / total liabilities = 4.52), which accounts for 73% of the score. AMD's $63.0B book equity is **66% goodwill and intangibles** ($41.8B, legacy Xilinx/ZT Systems). Substituting *tangible* book equity ($21.2B) drops x4 to 1.52 and the **Z-Score to ~1.94 — the grey zone, just above the 1.81 distress threshold.** The "safe" verdict is therefore real on a cash-flow basis but thin on a liquidation basis.

---

## 2. Key Financial Risk Metrics

### Leverage & Coverage
| Metric | FY2025 | TTM (Q4'25–Q3'26) | Trend |
|---|---|---|---|
| Revenue | $34.64B | **$45.44B** | +31% YoY (TTM) |
| Gross margin | 49.5% | **53.7%** | Expanding |
| Operating margin | 10.7% | **18.2%** | Expanding sharply |
| EBITDA | $7.28B | **$11.32B** | — |
| EBIT | $4.27B | **$8.27B** | — |
| Net income | $4.34B | **$7.62B** | — |
| Interest expense | $131M | $172M | Rising w/ new notes |

### Liquidity
| Metric | Value | Read |
|---|---|---|
| Current ratio | **2.85x** | Very strong |
| Quick ratio | **2.01x** | Strong ex-inventory |
| Cash ratio | **1.12x** | Cash alone covers all current liabilities |
| Working capital | **$17.49B** | — |
| Assets / liabilities | 5.52x | — |
| Cash runway | **N/A — structural cash generator** | No burn |

**Debt maturity ladder:** only **$874M short-term** vs. $10.55B cash — no refinancing cliff whatsoever. *(Note: total debt $4.472B ≠ STD $874M + LTD $2.973B = $3.847B; a ~$625M residual, likely finance leases. Full maturity schedule not available from tools — flagged data gap.)*

### FCF Sustainability
| | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| OCF | $3.57B | $1.67B | $3.04B | **$7.71B** |
| Capex | $0.45B | $0.55B | $0.64B | $0.97B |
| **FCF** | $3.12B | $1.12B | $2.41B | **$6.74B** |
| **FCF margin** | 13.2% | 4.9% | 9.3% | **19.4%** |

FCF margin has nearly quadrupled from the FY2023 trough. FY2025 FCF/net income conversion = **158%** (high D&A of $3.0B flatters cash conversion). Buybacks $1.32B are covered 5.1x by FCF; no dividend. **SBC is the quality caveat: $1.64B = 4.7% of revenue, 24% of FCF** — share count is nonetheless flat (~1,624M), so net dilution is contained.

**Trailing FCF yield: 0.92%** — the single most important risk metric in this report (see §3).

---

## 3. Market Risk Profile — *This is where the risk lives*

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (3y) | **60.2%** | ~3x market; extreme |
| Beta vs SPY (3y) | **2.38** (5y: 2.49) | A 20% market drawdown ⇒ ~48% AMD drawdown |
| Max drawdown (3y) | **–63.0%** | Realized tail event already occurred |
| Sharpe (0% rf, tool) | 1.065 | See adjustment below |

**Sharpe must be read with caution:** the tool assumes a 0% risk-free rate. With the **10Y UST at 5.13%** and **2Y at 4.74%** (curve positively sloped, +39bp — no inversion, i.e. no recession signal priced), a ~5% risk-free rate against 60% volatility **cuts the excess-return Sharpe to roughly 0.6** — mediocre risk-adjusted return for the volatility taken.

### Yield curve context (2026-11-08)
2Y 4.74% | 5Y 4.93% | 10Y 5.13% | 30Y 5.47% | **2s10s +39bp, not inverted.** Rates at these levels are a direct headwind to long-duration, high-multiple equities — precisely AMD's category. A 5.13% discount rate is unforgiving to a 0.92% FCF yield.

### Valuation risk (my principal concern)
| Metric | Value |
|---|---|
| TTM P/E | **96x** |
| EV / EBITDA (TTM) | **64x** |
| EV / Sales (TTM) | **16.0x** |
| FCF yield | **0.92%** |
| Price / tangible book | **~35x** ($449 vs $12.9/share) |

At 64x EV/EBITDA with a 2.38 beta and 60% volatility, AMD's equity is a **long-duration growth claim whose price is far more sensitive to the discount rate and to growth expectations than to any change in its creditworthiness.**

---

## 4. Downside Scenario Analysis: Revenue –20%

**Base (TTM):** Revenue $45,436M | GM 53.7% | Opex $16,132M | D&A $3,046M | Interest $172M

**Breakeven headroom:** holding gross margin constant, operating income reaches zero at revenue of **~$30.0B, i.e. –34%**. Allowing a realistic 500bp GM compression, breakeven moves to **~–27%**. (On the *older* FY2025 cost structure the breakeven was only ~–21.5% — the operating buffer has materially widened.)

| Scenario | Revenue | GM | Opex | EBIT | EBITDA | Net Cash | Gross Debt/EBITDA |
|---|---|---|---|---|---|---|---|
| Base TTM | $45.4B | 53.7% | $16.1B | $8.27B | $11.32B | $6.08B | 0.40x |
| **–20% rev, GM→50%, opex –10%** | $36.3B | 50.0% | $14.5B | **$3.66B** | $6.70B | ~$9B | 0.67x |
| **–20% rev, GM→45%, opex flat** | $36.3B | 45.0% | $16.1B | **$0.26B** | $3.31B | ~$7B | 1.35x |
| Severe –40% rev, GM→42%, opex –20% | $27.3B | 42.0% | $12.9B | **–$1.46B** | $1.59B | ~$5B | 2.8x |

**Conclusion on solvency:** In every scenario — including an unrecovered 40% revenue collapse — AMD remains **EBITDA-positive, net-cash, and comfortably able to service $4.5B of debt at 28x+ coverage.** There is no plausible operating scenario in which AMD breaches a covenant or faces a refinancing crisis. **Credit/bankruptcy risk is effectively nil.**

**Conclusion on equity:** The damage is all valuation. Under the –20% scenario (EBITDA $6.70B), applying a *still-generous* 25x EV/EBITDA gives an EV of ~$167B versus today's $727B — **an ~77% equity decline.** Even at 40x — double the market multiple — the equity is worth ~$268B, **–63%**, which is exactly the drawdown AMD has already delivered within the last three years. *The historical max drawdown of –63% is the market's own estimate of what this scenario looks like.*

---

## 5. Overall Financial Risk Rating

# MODERATE

**The apparent paradox resolved:** AMD scores as a *low-risk* company on every balance-sheet and cash-flow test, but the **equity security** carries high risk because the market has priced ~96x earnings and 0.92% FCF yield into a 2.38-beta, 60%-volatility stock. Financial risk is bifurcated:

- **Credit / solvency risk: LOW** (net cash, A1/A, 28–48x coverage, 2.85x current ratio, no maturity wall)
- **Equity / market risk: HIGH** (96x P/E, 64x EV/EBITDA, –63% realized drawdown, 2.38 beta)
- **Blended: MODERATE**, leaning high for any holder with a sub-3-year horizon or leverage.

---

## 6. Key Red Flags

1. **🔴 Valuation is the risk, not the balance sheet.** 96x TTM P/E, 64x EV/EBITDA, 16x EV/Sales, **0.92% FCF yield** against a **5.13% 10-year Treasury**. The equity offers a real FCF yield roughly one-fifth of the risk-free rate — a 5.5-point negative spread for taking 60% volatility. This is the single most fragile element of the investment case.
2. **🟠 Goodwill concentration:** $41.8B of goodwill/intangibles = **54% of total assets, 66% of equity**. Tangible book is only $21.2B. A structural AI/datacenter capex slowdown would put Xilinx/ZT carrying values at risk of impairment — a non-cash hit that would nonetheless hit book value and the Z-score. **Tangible-book-adjusted Z-Score ~1.94 (grey zone).**
3. **🟠 Extreme market sensitivity:** beta 2.38, 60.2% annualised vol, –63% 3-year max drawdown. Position sizing, not fundamental analysis, is the primary control here.
4. **🟡 Demonstrated quarterly margin fragility:** Q2 FY2025 gross margin collapsed to **39.8%** (operating loss of –$134M) before recovering to 53.9% two quarters later. With ~$16.1B of largely fixed opex and $9.3B of implied R&D, the operating buffer is wider than it was but still only ~27–34% of revenue.
5. **🟡 Retained earnings of only $6.70B against $63.0B of equity** — **89% of book value is paid-in capital, not accumulated profit.** AMD has historically destroyed and rebuilt book value; the equity cushion is contributed, not earned.
6. **🟡 SBC of $1.64B** (4.7% of revenue, 24% of FCF) — a real, recurring economic cost that GAAP FCF overstates.
7. **🟢 Mitigants:** working capital of $17.5B, cash ratio 1.12x, inventory days improving (160 → 137), F-score 8/9, FCF margin up 4x since FY2023, and a non-inverted yield curve.

---

## Data Gaps (explicitly flagged)
- **Detailed debt maturity schedule** unavailable — only STD $874M / LTD $2.973B aggregates (which do not reconcile to $4.472B total; ~$625M unexplained, likely finance leases).
- **No covenant terms, revolver capacity, or CDS spreads** retrievable from available tools.
- **Customer concentration not quantified in tool data** — AMD's 10-K discloses hyperscaler customers above 10% of revenue; this is a structural single-customer risk I could not measure numerically. Searches returned no AMD-specific figure.
- **No peer multiple benchmarking** was run (NVDA, AVGO, MU, TSM identified as the relevant comparables) — valuation context above is absolute rather than relative.
- FCF, FCF yield, and Z-score are based on **FY2025 annuals**; TTM cash flow was estimated from quarterly income statements only.

**Bottom line:** AMD cannot be killed by its own balance sheet — it is a net-cash, A1-rated, 8/9-F-score company that would survive a 40% revenue collapse without a covenant breach. It *can* be killed by its multiple. The risk is duration, not default.

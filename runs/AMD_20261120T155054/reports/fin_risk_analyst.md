# Fin Risk Analyst

- Symbol: AMD
- Elapsed: 69.5s

---
I have sufficient data. One note: the yield curve came back as of 2026-11-20, so I'll anchor the analysis to the TTM period through Q3 FY2026.

---

# AMD — Financial Risk Assessment
**As of 2026-11-20 | Price $446.84 | Market cap $732.9B | Sector: Technology / Semiconductors**

## 1. Credit Risk Assessment — **INVESTMENT GRADE (High Quality)**

AMD is a **net-cash, essentially unlevered** balance sheet. Total debt of $4.47B against $10.55B cash and short-term investments gives net cash of **–$6.08B** (net debt/EBITDA **–0.84x**). Debt is 6% of assets and 7% of equity. Solvency is not a meaningful risk.

Moody's upgraded AMD's senior unsecured rating to **A1** on 2025-10-10, placing it in the upper-medium investment grade band. *(The rating agency page did not render body content — rating confirmed from headline only; outlook unconfirmed. Treat as indicative.)*

The Altman Z-Score of **3.74** sits comfortably in the safe zone, and that figure is **conservative**: the model uses book equity ($63.0B), whereas market equity would raise the x4 term from 4.52 to ~52.6.

## 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|
| Revenue | $34.64B | $25.79B | $22.68B | +34% YoY |
| Gross margin | 49.5% | 49.4% | 46.1% | Stable/expanding |
| Operating margin | 10.7% | 7.4% | 1.8% | Recovering |
| Debt / Equity | 0.07x | 0.04x | 0.05x | Negligible |
| Net debt / EBITDA | –0.84x | –0.30x | –0.22x | **Net cash** |
| Interest coverage (EBIT/int.) | **28.2x** | 22.6x | 5.6x | Very strong |
| Interest coverage (EBITDA basis) | 55.5x | 57.2x | 39.1x | Very strong |
| Current ratio | 2.85x | 2.62x | 2.51x | Strong |
| Quick ratio | 2.01x | 1.83x | 1.86x | Strong |
| Cash ratio | 1.12x | 0.70x | 0.86x | Cash > current liabilities |
| Working capital | $17.49B | $11.77B | $10.08B | Ample |
| **Altman Z-Score** | **3.74** (Safe) | — | — | Safe zone (>2.99) |
| **Piotroski F-Score** | **8/9** (Strong) | — | — | Only miss: F5 leverage |
| FCF | $6.74B | $2.41B | $1.12B | Inflecting up |
| FCF margin | 19.4% | 9.3% | 4.9% | Strong improvement |
| **FCF yield** | **0.92%** | — | — | **Valuation problem** |
| Capex / revenue | 2.8% | 2.5% | 2.4% | Fab-lite, low intensity |
| SBC | $1.64B | $1.41B | $1.38B | 38% of net income |

**Liquidity detail:** Cash of $10.55B covers **12.1x** short-term debt ($0.87B). With positive and rising FCF and zero dividend, there is **no cash runway constraint** — cash alone funds ~3.1 quarters of total operating expense, but this is academic given positive free cash generation.

**Debt maturity:** Only the split ($0.87B current / $2.97B long-term) is available. **The full maturity ladder is not retrievable from these tools** — a genuine data gap, though immaterial at this leverage level. Refinancing at the current curve (2Y 4.74%, 10Y 5.13%) would be costly in general, but AMD's $4.5B debt stack is small enough that rate exposure is a rounding error.

## 3. Market Risk Profile — **HIGH**

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (756d) | **66.1%** | ~4.2x the S&P's typical ~16% |
| Beta vs SPY | **2.46** | Extreme market sensitivity |
| Max drawdown (3yr) | **–54.7%** | >50% peak-to-trough loss |
| Sharpe ratio | 1.04 | Decent, but flawed methodology |
| Sortino ratio | *not computed* | **Data gap** |

Two caveats that matter. First, the Sharpe ratio assumes a **0% risk-free rate**; against the actual 2Y of 4.74%, the implied ~68.7% annualised return still yields a Sharpe of ~0.96 — so the conclusion holds, but the 68.7% absolute return is the real story: this is a **momentum-driven high-beta name**, not a low-risk compounder.

Second, and critically: **beta 2.46 means a 20% market drawdown mechanically implies a ~49% AMD drawdown.** The historical max drawdown of 54.7% is entirely consistent with that arithmetic. Market risk, not credit risk, is where AMD's downside lives.

## 4. Downside Scenario Analysis — Revenue –20%

Base: Revenue $34.64B, GM 49.5%, opex $13.46B, EBIT $3.69B (operating-income basis), interest $131M.

| Scenario | GM assumed | Opex | EBIT | EBITDA | Int. coverage | Net debt/EBITDA |
|---|---|---|---|---|---|---|
| Base FY2025 | 49.5% | $13.46B | $3.69B | $7.28B | 28.2x | Net cash |
| Mild (–20% rev, 300bp GM compression, 10% opex cut) | 46.5% | $12.11B | **+$0.77B** | ~$3.8B | 5.9x | Net cash |
| Severe (–20% rev, 550bp compression, flat opex) | 44.0% | $13.46B | **–$1.27B** | **+$1.74B** | negative | Net cash |

**Conclusion: AMD survives a –20% revenue shock without solvency stress.** Even in the severe case, EBITDA remains positive at ~$1.7B, net cash of $6.1B is untouched, and there are no debt covenants of consequence given a 0.07x debt/equity. FCF likely falls from $6.7B to $1–2B (working-capital release partially offsets), but stays positive.

The real damage in this scenario is **equity, not credit**: at ~96x TTM earnings, a 20% revenue miss would likely compress the multiple by more than the earnings decline. A –50% to –60% share price is the plausible equity outcome — i.e. **the credit is safe while the stock is not.**

**Asset-quality caveat:** Goodwill and intangibles of **$41.8B** are 66% of equity and 54% of total assets (Xilinx-era). Tangible book value is $21.2B, still 4.7x total debt — adequate. But a downturn pressuring the semi-custom/embedded franchise could trigger a **non-cash impairment** that would materially reduce reported equity. This does not threaten solvency.

## 5. Overall Financial Risk Rating — **LOW**

Credit risk: **Low**. Liquidity risk: **Low**. FCF sustainability: **Low–Moderate** (positive trend, but flattered by SBC and working capital). Market/valuation risk: **High**.

The composite is **LOW financial risk with a HIGH valuation/market risk overlay.** AMD's balance sheet is among the strongest in large-cap semis. Anyone shorting AMD on "financial risk" is looking at the wrong variable.

## 6. Key Red Flags

1. **Valuation, not leverage, is the risk.** FCF yield of **0.92%** (P/FCF ~109x on FY2025 FCF; ~96x trailing P/E on TTM net income of $7.6B). There is essentially **no cash-flow cushion in the price**. This is the single most important finding.
2. **Demonstrated margin fragility.** Q2 FY2025 (June 2025) delivered gross margin collapse to **39.8%** and an **operating loss of –$134M** on $7.69B revenue, versus 51.7% GM the following quarter. A ~1,200bp single-quarter GM swing is evidence of thin operating leverage. **The tools do not disclose the cause** (inventory write-down? ramp costs? — unverified). A repeat would be severely punished at this multiple.
3. **SBC at 38% of net income.** FCF excluding SBC is **$5.10B, not $6.74B** — true FCF yield is **0.70%**, not 0.92%. GAAP cash generation overstates owner earnings by ~24%.
4. **Inventory build.** Inventory +38% YoY to $7.92B vs revenue +34%; inventory days rose from 160 to 165. Not alarming, but the FY2025 working-capital drag of **–$2.38B** is the main reason operating cash flow ($7.71B) undershot the headline.
5. **Leverage doubled** — total debt rose from $2.21B to $4.47B. This is the sole Piotroski miss (F5). Immaterial in absolute terms but worth monitoring as a trend reversal.
6. **Concentration and geopolitical exposure** (export controls, TSMC dependence, hyperscaler AI capex concentration) is **not quantifiable from these tools** and is excluded from the rating above.
7. **Extreme systematic risk:** beta 2.46 and 66% volatility mean AMD is a leveraged bet on the market and the AI capex cycle. Position sizing matters more than fundamental risk here.

## Data Gaps (explicit)
- **Debt maturity schedule** not available — only current/non-current split.
- **CDS spreads** not available.
- **Peer leverage benchmarking** not performed — the peer tool returns market caps only, not financials. NVDA ($3.30T), AVGO ($1.52T), MU ($0.70T) are the relevant comps but no ratio comparison was possible.
- **Sortino ratio** not computed by the tool.
- **Moody's rating confirmed from headline only**; page body failed to render, so outlook is unverified.
- **Internal inconsistency in the data feed:** the balance sheet's `net_debt` field (–$1.07B) conflicts with the computed figure (–$6.08B = $4.47B debt – $10.55B cash). I used the computed figure. Separately, the `ebit` field is inconsistent across periods (FY2025 EBIT $4.27B > operating income $3.69B; Q3 FY2026 EBIT $1.94B < operating income $2.83B). All coverage ratios here use **operating income / interest**, consistent with the ratio tool (28.2x).

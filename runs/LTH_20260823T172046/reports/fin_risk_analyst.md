# fin_risk_analyst

_2026-08-23T09:27:10+00:00_

# Financial Risk Assessment — LTH (Life Time Group Holdings, Inc.)
Ticker: **LTH** | NYSE | Leisure / Consumer Cyclical | Price $45.11

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (High-Yield risk profile, improving trajectory)**

Life Time is a capital-intensive fitness-center operator that has grown revenue aggressively (from $1.32B in FY2021 to $2.995B in FY2025, +127%) and swung from heavy losses to $374M net income in FY2025. The catch is that growth has been **funded with debt and capital leases**, leaving a balance sheet that sits right on the distress boundary.

| Signal | Value | Source |
|---|---|---|
| Altman Z-Score | **1.81** (borderline — distress threshold <1.81) | `statements`/`financial-scores` |
| Piotroski F-Score | **7 / 9** (improving financial strength) | `statements`/`financial-scores` |
| Credit rating / CDS | **Not available** (Starter plan / data gap) | — |

The Piotroski score of 7 reflects genuinely stronger profitability and cash generation in FY2025 — the trend direction is favorable. But the Altman Z at 1.81 is *exactly* on the distress boundary, dragged down by negative working capital and heavy leverage.

---

## 2. Key Financial Risk Metrics (FY2025 unless noted)

| Metric | Value | Interpretation | Source |
|---|---|---|---|
| **Net debt / EBITDA** | **8.25x** (2024: 6.30x, 2023: 9.00x) | Distress-level; includes $2.59B capital leases | `statements`/`key-metrics` |
| Debt / Equity | 2.16x | Highly leveraged | `statements`/`metrics-ratios` |
| Debt / Assets | 0.77x | Most assets debt-financed | `statements`/`metrics-ratios` |
| Total debt | $6,749M | LT debt $4,041M + capital leases $2,594M + ST debt $113M | `statements`/`balance-sheet-statement` |
| Net debt | $6,517M | vs. only $232M cash | `statements`/`balance-sheet-statement` |
| Interest coverage (FY2024) | **2.41x** | Thin — FY2025 figure unreliable (see red flags) | `statements`/`metrics-ratios` |
| **Current ratio** | **0.63x** (Quick 0.52) | Negative *working capital* $-224M | `statements`/`metrics-ratios` |

**Liquidity details (FY2025):** cash $232M, total current assets $386M vs. current liabilities $609M. The company's liquidity is structurally negative — it relies on debt/equity inflows rather than internal near-term cash. Cash rose +$204M in FY2025, driven by financing, not operations.

---

## 3. Market Risk Profile

| Metric | Value | Source |
|---|---|---|
| **Beta** | **1.498** | `company`/`profile-symbol` |
| Current price / 52-wk range | $45.11 / $24.14–$47.24 | `quote` |
| Implied max 12-mo drawdown | **~49%** (computed from 52-wk high→low: 47.24→24.14) | `quote` (computed by analyst) |
| Position vs. 200-d avg | +43% ($45.11 vs. $31.50 avg) | `quote` |
| Annualized volatility, Sharpe, Sortino | **Not computed** — historical daily series unavailable (data gap; tool-call limit on `chart`/`historical-price-eod-full`) | — |

The stock trades near its 52-week high with a beta of ~1.5, meaning it amplifies market moves. Despite strong momentum (+43% above its 200-day average), it showed a ~49% peak-to-trough drawdown within the past year — high tail risk for a single-name position.

---

## 4. Downside Scenario Analysis (Revenue −20%)

**Analyst stress scenario (assertive assumptions, computed from FMP raw data — not an FMP-returned figure).** Baseline FY2025: revenue $2,995M, EBITDA $790M (26.4% margin), net debt $6,517M.

Assuming a −20% revenue shock consumes gross profit roughly in proportion while fixed costs only partially flex (EBITDA compresses ~35% to ~$515M):

| Metric | Baseline | −20% scenario |
|---|---|---|
| Revenue | $2,995M | ~$2,396M |
| EBITDA | $790M | ~$515M |
| **Net debt / EBITDA** | **8.25x** | **~12.7x** |
| Interest coverage (FY24 basis) | 2.4x | ~1.7x |

Under a deeper recession (−40% revenue), net debt/EBITDA would exceed **15x** and interest coverage would fall **below 1x** — a classic refinancing stress situation. With FCF already negative after capex ($891M capex vs. $871M operating cash flow in FY2025), a downturn would force a delay/shrink of the expansion pipeline rather than outright distress, but the equity cushion (debt/equity 2.16x) is thin.

---

## 5. Overall Financial Risk Rating

**HIGH** — with an improving but fragile trajectory.

**Positives:** Revenue and net income compounding strongly; Piotroski 7/9; massive improvement from FY2021's $-579M loss to FY2025's $374M profit; cash built to $232M.

**Negatives dominate the risk profile:** Net debt/EBITDA 8.25x, negative working capital, current ratio 0.63, negative FCF after capex (capex/cash-flow >1x, FCF yield −0.36%), Altman Z at the 1.81 distress boundary, beta 1.5. The operating-lease-heavy model concentrates the balance sheet risk.

---

## 6. Key Red Flags

1. **Net debt/EBITDA of 8.25x** — distress-level leverage (FMP `key-metrics`), worsening from 6.30x in FY2024.
2. **Negative working capital** of −$224M and current ratio 0.63 / quick 0.52 — structural near-term liquidity shortfall.
3. **FCF is negative** (−$21M in FY2025) even after a strong operating year; capex-to-cash-flow 1.02x, capex-to-depreciation 3.0x — the expansion is being funded by financing, not internally.
4. **Altman Z at 1.81** — on the boundary; a modest deterioration pushes it into distress territory.
5. **Beta 1.5 and ~49% 12-month drawdown** — high market sensitivity / tail risk.
6. **FY2025 interest expense reported as $0** in the income statement — inconsistent with $2.4x coverage in FY2024 and $136.9M interest paid in FY2024 cash flow. This is a **data-quality gap**; interest coverage for FY2025 could not be reliably computed. Capitalized interest is likely involved.
7. **No credit rating, CDS, or debt-maturity schedule** available on this plan, and **historical daily prices could not be retrieved** (tool-call limit) — so annualized volatility, Sharpe/Sortino ratios, and refinancing-cliff analysis were not quantified this session.

I recommend the Head of Research route a follow-up to the **quant_engineer** (daily price series from `chart`/`historical-price-eod-full`, plus the debt-maturity schedule from SEC filings) to close the volatility and refinancing gaps before positioning decisions are made.

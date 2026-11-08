# Fin Risk Analyst

- Symbol: FROG
- Elapsed: 61.2s

---
## FROG (JFrog Ltd.) — Financial Risk Assessment

**Context:** Software-Application (DevOps), US/Israel, market cap ~$12.23B, price $100.98, ~121M shares. Fiscal data through FY2025 (period end 2025-12-31); Q3'26 actuals sourced externally.

---

### 1. Credit Risk Assessment — **Investment Grade** (unrated; net-cash balance sheet)

FROG carries **$19.1M of total debt against $705.1M of cash & short-term investments** → **net cash of ~$686M** (≈5.6% of market cap). Debt/equity 0.02, debt/assets 0.01. Interest expense is **$0** — the company is a net interest *recipient*, so **interest coverage is effectively infinite/N/A** (not computable because there is no interest expense denominator).

The only apparent stress signal is **net debt/EBITDA of 16.52** — this is a **mathematical artifact of negative EBITDA** (-$41.5M), not a leverage signal. It should be discarded, not interpreted.

Debt maturity schedule: $5.8M short-term + $6.7M long-term (residual ~$6.6M in finance leases/other) — **there is no refinancing cliff**. Refinancing risk is immaterial for the foreseeable future.

**Ratings/tooling caveat:** Company is unrated, no CDS spread, and no revolving credit facility is disclosed in the data *(data gap)*. On balance-sheet fundamentals it would screen at the high end of investment grade.

---

### 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Revenue ($M) | 531.8 | 428.5 | 349.9 | +24.1% YoY; 3yr CAGR 23.8% |
| Gross margin | 76.8% | 77.1% | 78.0% | Mild compression (3-yr trend) |
| GAAP operating margin | **-16.9%** | -20.8% | -21.5% | Improving, still negative |
| GAAP EBITDA ($M) | -41.5 | -44.4 | -39.2 | Negative |
| **Adj. EBITDA ex-SBC ($M)** | **+115.1** | +86.7 | +55.9 | 21.6% margin — the real economics |
| Net income ($M) | -71.8 | -69.2 | -61.3 | 5th consecutive loss year |
| **Debt/Equity** | **0.02** | 0.03 | 0.05 | Debt-free |
| **Net debt / EBITDA** | **N/M (negative EBITDA)** | N/M | N/M | Not meaningful |
| **Interest coverage** | **N/A (no interest expense)** | N/A | N/A | Net interest income |
| **Current / Quick / Cash ratio** | **2.09 / 2.09 / 1.73** | 2.04 / — / — | 2.46 / — / — | Strong; no inventory |
| Working capital ($M) | 443.2 | 331.7 | 383.6 | Expanding |
| Cash + ST inv. ($M) | 705.1 | 522.0 | 545.0 | Rising |
| **Altman Z-Score** | **1.353 (Distress zone)** | — | — | **Misleading — see below** |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | — | — | Mixed |
| FCF ($M) | **142.3** | 107.8 | 72.2 | +32% YoY |
| **FCF margin** | **26.8%** | 25.2% | 20.6% | Strong, improving |
| **FCF yield (TTM)** | **1.21%** | — | — | Thin vs. 4.7–5.5% risk-free |
| Retained earnings ($M) | **-431.5** | -359.7 | -290.4 | Accumulated deficit |
| Share count (M, diluted) | 116.2 | 109.7 | 103.3 | **+5.9% dilution/yr** |

**Altman Z-score decomposition (Z = 1.353):** X1 (WC/TA) 0.330 ✓, X4 (equity/liabilities) 1.955 ✓, but X2 (retained earnings/TA) **-0.322** and X3 (EBIT/TA) **-0.049** dominate the fail. Both terms mechanically penalize *any* growth-stage company that has burned cash to build a franchise. With net cash and 2.09x current ratio, **the "distress" label is a false positive**; the tool itself flags that X4 uses book equity.

**Piotroski F = 5:** points lost on negative ROA (F1), leverage/liquidity (F5), **dilution (F7)**, and gross-margin trend (F8). Gained on positive operating cash flow, ROA improvement, accruals quality, equity increase, and asset-turnover improvement.

**Forward context (Q3'26 actuals):** Revenue $179.2M (+31% YoY), non-GAAP operating margin **22.7%**, GAAP operating margin **-1.0%** (from -15.8%), GAAP diluted EPS **+$0.05** (first GAAP profit), quarterly FCF $66.5M (37.1% margin → ~$266M annualized). The GAAP inflection is real and underway.

---

### 3. Market Risk Profile — **HIGH**

| Metric | 3-year (756d) | 1-year (252d) |
|---|---|---|
| Annualized volatility | **65.4%** | **87.9%** |
| Beta vs SPY | 1.35 | **1.67** (company-reported 1.31) |
| Max drawdown | **-49.6%** | -37.4% |
| Sharpe (0% rf assumption) | 1.23 | 1.33 |
| Sharpe @ 4.7% rf (2Y UST) | ~1.16 | ~1.27 |

Volatility of 65–88% is roughly **4–5x the market** — this is a high-duration asset whose price is a function of growth-expectation repricing, not cash flow. Beta is **rising** (1.35 → 1.67), meaning sensitivity to drawdowns has *increased* as the stock has run. A 50% peak-to-trough drawdown is not a tail event here — it is the observed 3-year experience, and it has happened once already.

**Valuation is the dominant market risk:** ~$11.5B EV / ~$717M revenue run-rate ≈ **16x EV/Sales**, against a forward FCF yield of only ~2.2%. There is essentially **zero margin of safety** priced in.

*Data gaps:* Sortino ratio, VaR/CVaR, and implied volatility/skew are not available from the toolset.

---

### 4. Downside Scenario Analysis — Revenue -20%

Base case = FY2026 run-rate revenue ~$717M, gross margin ~76.5%, GAAP opex ~77.5% of revenue (~$556M), adj. EBITDA ~22% margin (~$158M), FCF ~$266M annualized.

| Line item | Base | -20% rev, opex flat | -20% rev, opex -10% | -20% rev, opex -20% |
|---|---|---|---|---|
| Revenue ($M) | 717 | 574 | 574 | 574 |
| Gross profit @ 76.0% ($M) | 549 | 436 | 436 | 436 |
| Opex ($M) | 556 | 556 | 500 | 445 |
| GAAP operating income ($M) | ~-1 to +5 | **-120** | **-64** | **-9** |
| EBITDA ($M) | ~30 | -92 | -36 | +19 |
| **Adj. EBITDA ex-SBC ($M)** | 158 | 66 | 122 | 177 |
| **FCF ($M)** est. | 266 | ~20–40 | ~75–95 | ~110–130 |
| **FCF margin** | 37% | 4–7% | 13–17% | 19–23% |
| Net cash ($M) | 686 | ~706 | ~761 | ~796 |

**Conclusions:**
- **No solvency threat under any variant.** Net cash *rises* in every case because FCF stays positive once working-capital normalization is excluded. Cash alone covers ~5 years of the worst-case EBITDA burn (-$92M/yr).
- The FCF hit is **disproportionate to the EBITDA hit** because a stalled growth rate kills the deferred-revenue working-capital inflow that currently funds ~40% of reported FCF. **This is the single most under-appreciated risk in the model.**
- The binding constraint is **GAAP profitability timing**: even the mild downside pushes GAAP breakeven out and would likely re-rate the multiple from ~16x to ~8–10x EV/Sales → **-35% to -50% equity downside**, consistent with the observed 49.6% max drawdown.
- **Stress add-on:** rate environment is unfavorable (2Y 4.74%, 10Y 5.13%, 30Y 5.47%; curve dis-inverted at +39bp). Long-duration software is directly exposed to a rising discount rate — FROG's 1.2–2.2% FCF yield has no duration hedge.

---

### 5. Overall Financial Risk Rating: **MODERATE**

Split the assessment explicitly, because the two halves point in opposite directions:

- **Solvency / liquidity / credit risk: LOW.** Net cash $686M, negligible debt, 2.09x current ratio, 26.8% FCF margin and rising, no maturities, no covenants.
- **Market / valuation / earnings-quality risk: HIGH.** 65–88% vol, beta 1.67, 49.6% max drawdown, 1.2% TTM FCF yield at 16x EV/Sales, and FCF that is *entirely* a function of adding back stock compensation.

**Composite: Moderate.** FROG will not fail. It can lose half its value.

---

### 6. Key Red Flags

1. **FCF is an SBC artifact — the highest-priority flag.** SBC of **$156.7M = 29.5% of revenue**. Reported FCF of $142.3M minus SBC = **-$14.4M**. The company is *not* self-funding on an economic basis; it is funding operations with equity compensation.
2. **Persistent dilution: +5.9% in FY2025, +6.2% in FY2024.** Share count 103.3M → 116.2M in two years. Every "FCF beat" is partly a claim on future shareholders.
3. **Five straight years of GAAP net losses** and an accumulated deficit of -$431.5M (1.9x the entire FY2025 gross profit). GAAP profitability only just achieved in Q3'26 (-1.0% operating margin).
4. **Working-capital dependence of FCF.** Deferred revenue growth contributes $33.5M of the $145.7M operating cash flow; slower growth mechanically compresses FCF faster than revenue.
5. **Gross margin compression:** 78.0% → 77.1% → 76.8%. Small, but a consistent three-year direction consistent with cloud/mix shift.
6. **Beta rising while valuation expands** (1.35 → 1.67): the equity's risk profile is deteriorating even as fundamentals improve — the classic setup for asymmetric downside.
7. **Input-cost/geopolitical:** Israeli-incorporated founder-led entity; enterprise software budgets are the marginal revenue source in a downturn.

**Data gaps flagged:** no credit rating or CDS; no disclosed revolver/covenant terms; no debt maturity ladder detail (only ~$19M residual, so immaterial); no Sortino/VaR/implied vol; no comparable DevOps/SaaS peer set (sector tool returned only mega-cap semis/hardware — **peer multiples unavailable**); annual P&L is FY2025, so FY2026 is reconstructed from Q3'26 disclosures, not from audited full-year data.

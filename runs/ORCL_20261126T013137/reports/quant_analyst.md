# Quant Analyst

- Symbol: ORCL
- Elapsed: 27.2s

---
## ORCL — Quantitative Factor Report
*All data as of FY-end 2026-05-31; price $103.88; market cap $302.7B (profile shows $314.1B — use with care). Peer set = MSFT, NVDA, AVGO (n=4 total incl. ORCL).*

### 1. Factor Scores Table

| Factor | Score / Raw | Peer Rank (of 4) | Signal |
|---|---|---|---|
| **Value** | P/E 17.8x; EV/EBITDA 12.8x; P/B 7.0x; P/FCF **n.m. (−12.8x)** | **1** | **Attractive on earnings, disqualified on cash** |
| **Momentum** | 12-1 return **+1.6%** | 2 | Weakly positive |
| **Quality** | ROE 39.7%; GP/Assets **0.169**; Accruals −5.69%; **ROIC 10.3%** (from 14.8%) | 3 | Deteriorating |
| **Low Vol** | Vol **63.2%**; β 2.27; MaxDD **−58.9%** | **4 (worst)** | **Strongly negative** |
| **Earnings Revision** | +33.3% (tool) — **methodologically contaminated** | 1* | *Discard — see flag R1* |

**Peer raw data used for ranking:**

| | ORCL | MSFT | NVDA | AVGO |
|---|---|---|---|---|
| P/E | **17.8** | 27.3 | 30.5 | 63.1 |
| EV/EBITDA | **12.8** | 17.9 | 25.0 | 43.5 |
| P/FCF | −12.8 | 54.5 | 37.9 | 54.3 |
| ROE % | 39.7 | 30.2 | 76.3 | 28.5 |
| GP/Assets | 0.169 | 0.297 | 0.742 | 0.253 |
| Accruals | −0.057 | −0.065 | +0.084 | −0.026 |
| 12-1 Mom % | +1.6 | **+10.5** | −1.9 | −7.3 |
| Vol % | 63.2 | **34.5** | 56.5 | 50.1 |
| Beta | 2.27 | **0.93** | 2.46 | 1.97 |
| MaxDD % | −58.9 | −23.4 | −47.5 | −39.3 |

ORCL is the **cheapest name in the peer group on both P/E and EV/EBITDA** — the only genuine bull leg. Note P/B of 7.0x against a book value of just $14.78/share is not "cheap" in absolute terms; the low P/E rests on levered equity.

### 2. Price Statistics (252 trading days, 0% rf)

| Metric | Value |
|---|---|
| Annualised return | **−23.62%** |
| Annualised volatility | 63.75% |
| **Alpha (annualised, vs SPY)** | **−48.90%** |
| Beta (1y OLS) | **2.284** (R² 0.332) |
| Beta (profile, long-run) | 1.778 |
| **Sharpe** | **−0.370** |
| **Sortino** | **−0.699** |
| Max drawdown | **−58.93%** |

**Interpretation:** R² of only 0.33 means two-thirds of ORCL's variance is idiosyncratic — this is a **stock-specific story, not a market proxy trade**. The widening gap between Sharpe (−0.37) and Sortino (−0.70) says the damage is concentrated in **downside** semi-deviation: losses are larger and more frequent than gains. Realised alpha of −49% annually is an extraordinary underperformance given beta >2 in an up market — the stock destroyed value *despite* high market exposure. A 59% peak-to-trough drawdown with 63% vol places ORCL in the highest risk decile of large-cap tech.

### 3. Quality Deep-Dive (the decisive evidence)
- **ROIC collapsed 14.80% → 14.13% → 10.34%** (FY24→FY26). Capital employed has ballooned faster than NOPAT.
- **Free cash flow −$23.7B** in FY26 vs −$0.4B FY25 and **+$11.8B FY24**. Capex: **$6.9B → $21.2B → $55.7B**. That is an 8x increase in two years.
- Enterprise value $427B vs market cap $303B ⇒ ~$124B net debt and rising.
- Offsetting positives: accruals −5.7% is the *second best* in peer set (cash earnings exceed reported earnings pre-capex), operating CF +$32.0B (+54% YoY), Piotroski **F-Score 5/9** (moderate). F-Score damage comes from ROA decline, share dilution, no gross-margin improvement, no asset-turnover improvement.
- **Accruals quality is fine; capital allocation is the problem.** ROIC, not accruals, is where quality breaks.

### 4. Composite Quant Signal: **NEUTRAL** (bias: value trap, do not add)

Rank-average ≈ 2.4 of 4. Concretely: one strong positive (value), one weak positive (momentum, +1.6%), one neutral-to-negative (quality trend), one strongly negative (low-vol/risk), one unusable input (revisions). A 17.8x P/E does not compensate for −49% alpha, 63% vol, and a negative FCF yield — in this dataset cheap-and-falling-with-deteriorating-ROIC is the classic value-trap signature.

**What would flip it to Buy:** capex normalisation with FCF returning positive (FY25 comparison suggests FY26 is the trough year of an AI-infrastructure build), and 12-1 momentum crossing above +10% (peer MSFT's level). Sell-side targets ($170–$285, median ~$207) sit 65–175% above spot, so the *consensus view is materially more bullish than the tape* — that divergence is the single most important thing to resolve with fundamental work, and it is not a quant input.

### 5. Key Quant Risk Flags
- **R1 — Earnings revision signal is invalid.** The tool reports period 2031-05-31 (current EPS $27.06) vs a "prior" estimate of $20.29, which is the **FY2030 estimate, not a prior vintage of the FY2031 estimate**. The +33.3% is inter-year growth, not revision momentum. Do not use this in the composite. Only 5–6 analysts cover FY30–FY31 — statistically unreliable regardless.
- **R2 — Momentum reversal / negative-momentum regime.** 12-1 of +1.6% is barely positive and is the residue of a large drawdown; the 21-day exclusion means recent weakness is *not* in the number. Expect the reported momentum to decay if the downtrend persists.
- **R3 — Highest volatility in the peer set plus extreme beta.** β 2.27 ⇒ a 10% SPY decline implies ~23% ORCL decline; the −58.9% max drawdown is live, not hypothetical.
- **R4 — Leverage/financing risk.** ~$124B net debt against negative FCF means continued capital-markets dependency; a credit-spread widening would transmit directly to equity.
- **R5 — Small-sample caveat.** The cross-sectional ranks use n=4 Technology mega-caps. Rank 1/4 on value is not a robust quintile placement — no significance can be attached. Sector-wide factor data (AAPL, TSM, MU, SKHY) was not pulled within budget, and the peer list omitted software-infrastructure names of comparable size.
- **R6 — Data inconsistencies to reconcile before trusting:** market cap $302.7B (valuation tool) vs $314.1B (profile); beta 2.273 vs 2.284 across tools (immaterial); beta 1.778 in profile vs 2.28 1-year regression (1y window is more relevant to current positioning).

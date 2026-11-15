# Quant Analyst

- Symbol: TSEM
- Elapsed: 45.1s

---
## TSEM — Tower Semiconductor Ltd. | Quantitative Factor Report
**Price $146.89 · Mkt Cap $16.67B · Sector: Technology / Semiconductors (Israel) · FY end 2025-12-31**

---

### 1. Factor Scores Table

Peer set for ranking: TSEM, GFS, ON, MU, TSM, AMD (6 semis). Rank 1 = most attractive.

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 75.7 · P/B 5.74 · EV/EBITDA 28.9 · **P/FCF −406 (negative FCF)** | **5 / 6** | **Strongly Negative** |
| **Momentum (12-1)** | **−12.96%** (vs AMD +8.1%, MU −0.3%, TSM −1.1%, GFS −7.1%, ON −8.1%) | **6 / 6** | **Negative** |
| **Quality** | ROE 7.59% · ROIC 6.33% · GP/Assets 10.95% · Accruals −0.053 · F-Score 6/9 | **5 / 6** | **Negative** |
| **Low Vol** | Vol 77.2% (504d) / 92.1% (252d) · Beta 3.08 · MaxDD 58.7% | **6 / 6** | **Strongly Negative** |
| **Earnings Revision** | +31.3% (FY29E $14.26 vs $10.86) | n/a — **n = 1 analyst** | **Positive, low confidence** |

**Value detail — the entire bull case is forward-dated.** Trailing multiples are extreme, but consensus implies a violent EPS ramp: FY25A $1.94 → FY26E $4.07 → FY27E $7.15 → FY28E $10.86 → FY29E $14.26. That is a **60% EPS CAGR**. On that curve the multiple collapses: forward P/E **36.1x (FY26) → 20.6x (FY27) → 13.5x (FY28) → 10.3x (FY29)**; forward EV/EBITDA **18.4x → 12.3x → 8.6x**. Cheap *if* delivered — but only MU (10.5x P/E) and GFS (26.1x) are cheaper today on realized numbers.

**Quality detail — deteriorating, not improving.** Gross margin has fallen **27.8% (2022) → 24.8% → 23.6% → 23.2% (2025)**, −4.6pp in three years. ROIC collapsed **20.6% (2023) → 6.3% (2025)** — note 2023 was inflated by the ~$353M Intel termination fee, so the underlying level is ~6-7%, likely **below WACC**. Revenue has grown only **4.9% CAGR (2023-25)** while D&A runs at 19% of sales. Offsets: accruals are negative (−0.053 = conservative accounting) and F-Score is a moderate 6/9. F-Score deductions: no ROA improvement, **share count rising** (110.3M → 113.6M, +3.0% in 2yrs), no gross-margin improvement.

**Justified P/B check:** with ROE 7.6%, CoE ~10%, g 5% → intrinsic P/B ≈ **0.5-0.7x** vs. actual **5.74x**. The market is paying ~8-10x book value for a 6% ROIC foundry. This is the single most important quantitative flag in the file.

---

### 2. Price Statistics

| Metric | 504-day | 252-day |
|---|---|---|
| Annualized return | **+117.83%** | — |
| Annualized volatility | 77.19% | **92.09%** |
| Beta vs SPY | **3.076** | 3.311 |
| Alpha (annualized) | **+61.18%** | — |
| R² vs SPY | **0.263** | — |
| Sharpe | **1.527** | **0.531** |
| Sortino | **2.448** | — |
| Max drawdown | **−58.66%** | −58.66% |

**Alpha is not statistically significant.** R² of 0.263 means **74% of TSEM's variance is idiosyncratic**. Residual vol ≈ 66%; over 2 years, SE(alpha) ≈ 47%, giving an **alpha t-stat ≈ 1.3** — well short of the ~2.0 threshold. The headline +61% alpha is produced by a handful of extreme days (e.g. +16.7% on 2025-11-10, +14% on 2025-04-09) and should **not** be treated as skill or as a durable premium.

**The Sharpe divergence is the key signal: 1.53 over 2 years vs. 0.53 over 1 year.** Risk-adjusted performance is decaying sharply — the trailing-year return no longer compensates for the volatility being taken.

---

### 3. Composite Quant Signal

**SELL** — weighted composite **≈ 22 / 100**

| Input | Weight | Score |
|---|---|---|
| Value | 25% | 25 |
| Momentum | 25% | 5 |
| Quality | 25% | 25 |
| Low Vol | 10% | 2 |
| Earnings Revision | 15% | 55 |

TSEM ranks in the **bottom quintile of its peer group on four of five factors simultaneously**. There is no factor on which it screens attractively on realized data. The one offsetting input — a +31% upward EPS revision — is the thinnest possible evidence base and is contradicted by the flat realized earnings trend (net income $207.9M FY24 → $220.5M FY25, +6%).

*Confidence: low-to-moderate.* This is a factor-based verdict on a stock whose price is driven by narrative/contract news (SiGe, silicon photonics, capacity deals), which factor models structurally cannot see. Treat it as "the numbers do not support the current price," not as a timing call.

---

### 4. Key Quant Risk Flags

1. **Valuation gap requires flawless execution.** 5.74x book / 75.7x earnings vs. intrinsic ~0.6x book at current ROIC. Consensus needs EPS to **nearly double in FY26 and triple by FY27**; FY25A EPS of $1.94 already came in *below* the $2.18 consensus. Any slippage in the ramp de-rates the stock violently.
2. **Negative free cash flow.** P/FCF of −406x implies FCF ≈ −$41M despite $543M EBITDA — capex is consuming all operating cash. A foundry in a heavy capex cycle with negative FCF and sub-WACC ROIC is a value-transfer risk if the demand doesn't materialize.
3. **Momentum reversal risk is materialized, not prospective.** −12.96% 12-1 momentum, worst in the peer set, with all five peers also negative — this is a **sector-wide momentum unwind** with TSEM the highest-beta casualty. 12-month Sharpe of 0.53 confirms the regime has already turned.
4. **Extreme volatility / beta fragility.** Beta 3.08-3.31 with only 26% R². A 10% SPY drawdown mechanically implies ~30% downside, and max drawdown of 58.7% is already on the record. Position sizing, not conviction, is the binding constraint here.
5. **Factor crowding in the wrong direction.** This is a crowded *growth/expensive-quality* profile that fails value, quality and low-vol simultaneously — precisely the basket that de-rates first when rates rise or risk appetite falls.
6. **Earnings-revision score is likely an artifact.** The tool compares FY2029E ($14.255) to a "prior" of $10.85994 — which is *exactly* the FY2028 consensus, indicating a **period-alignment mismatch** rather than a genuine 3-month revision. Additionally FY2029E is covered by **1 analyst** (vs 7 for FY26/FY27). Do not underwrite the +31% upgrade signal.
7. **Liquidity: NOT a concern.** ~1.3-5.6M shares/day ≈ $200-800M dollar volume on a $16.7B cap. Adequately liquid for institutional positions.

**Data caveats:** TSM's value-factor feed is corrupt (P/E 1.2, EV/EBITDA 0.0) and was excluded from the value ranking. My price history terminates 2026-02-20 ($128.47) while the live quote is $146.89 and analyst notes run to 2026-11-03, so the momentum/revision windows extend beyond my observable series — peer-relative momentum is internally consistent and usable; the absolute level is not independently verifiable.

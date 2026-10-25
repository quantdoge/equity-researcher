# Quant Analyst

- Symbol: MMM
- Elapsed: 77.8s

---
## MMM (3M Company) — Quantitative Factor Report
*Industrials / Conglomerates · Price $171.37 · Mkt cap $88.4bn (tool reports $92.4bn on 539m diluted shares) · Data as of FY2025-12-31*

**Peer set (9 names, Industrials mega-cap):** MMM, CAT, GE, RTX, ETN, PH, TT, GD, DE. Ranks are **1 = best of 9**; use with ±1–2 rank tolerance given the narrow sample.

### 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 28.6 · EV/EBITDA 15.8 · P/FCF 66.2 · P/B 19.5 | **4 / 9** | **Neutral** — cheap on EV/EBITDA (1/9) & P/E (2/9), *most expensive* on P/FCF (9/9) and P/B (9/9) |
| **Momentum** (12-1) | +7.83% | **3 / 9** | **Positive** — above sector median (−2.4%); lags DE +20.1%, ETN +10.1% |
| **Quality** | ROIC 25.8% · ROA 8.6% · ROE 68.5% · GP/A 0.262 · Accruals 0.025 · F-Score 6/9 | **2 / 9** (ROIC), 4/9 (ROA) | **Positive, with caveats** — top-decile ROIC; but tool flags composite `quality_signal: low`, and ROE/P/B are distorted |
| **Low Vol** | Vol 27.3% · Beta 0.71 · MaxDD 18.8% · Sharpe 0.298 | **4 / 9** | **Neutral/slightly positive** — near-median vol & beta; 4th-best drawdown |
| **Earnings Revision** | +5.4% | **n/m** | **Not measurable — see flag** |

### 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | +14.01% |
| Annualised volatility | 26.24% – 27.31% (two modules; minor window/treatment difference) |
| **Alpha (annualised)** | **−2.50%** |
| **Beta** | **0.706** (R² **0.116**) |
| Sharpe | **0.534** (vol module variant: 0.298) |
| Sortino | **1.085** |
| Max drawdown | −18.77% |
| Sortino/Sharpe ratio | 2.03 (good downside symmetry) |

**Beta disagreement:** profile reports 5-yr beta **1.058**; 1-yr daily regression gives **0.706**. With R² = 0.116, only ~12% of MMM's variance is market-driven — the beta estimate has a wide standard error. **Do not use MMM as a low-beta defensive hedge**; the true conditional beta is unstable.

### 3. Composite Quant Signal: **NEUTRAL**
Top-quartile ROIC (2/9) and above-median momentum (3/9) are real positives, but they are offset by: (a) **negative alpha** (−2.5%/yr, i.e. it has underperformed what its beta implies), (b) the **worst FCF multiple in the peer group** (P/FCF 66.2 vs peer median ~41.9), (c) book-based value metrics that are uninterpretable (P/B 19.5, ROE 68%), and (d) an unverifiable revision signal. A composite z-score across the four measurable factors lands mid-pack — no factor is strong enough to overcome the FCF gap.

### 4. Key Quant Risk Flags

1. **FCF quality is the single biggest red flag.** P/FCF 66.2x vs EV/EBITDA 15.8x is a 4.2x divergence — the market is paying for EBITDA that is not converting to cash (FY25 OCF $2.31bn vs net income $3.25bn). The "cheap" EV/EBITDA reading (1/9) and the "expensive" P/FCF reading (9/9) cannot both be right.
2. **Book equity is not economically meaningful.** BVPS $8.81 vs price $171 — P/B 19.5 and ROE 68.5% are artifacts of a near-zero denominator after the 2023 charges (ROE −143.7%, ROIC still +18.7% that year). Discard P/B and ROE from any ranking; rely on ROIC, ROA, GP/A. **Peer sector ranks on Value/Quality are correspondingly softer than stated.**
3. **Revision signal is invalid as computed.** The tool compared the FY2030 estimate ($11.997) against the FY2029 estimate ($11.382) — that "+5.4%" is simply the forward-year growth step, **not a revision for a constant forward period**. Worse, **n = 1 analyst** carries the FY2030 EPS figure (vs 10 on FY2027, 11 on revenue). Treat estimate-revision momentum as **unknown** for MMM; do not credit it in the composite.
4. **Accruals deteriorated then recovered.** 2022: 0.004 → 2023: −0.270 (charge-driven) → 2024: **0.059 (warning)** → 2025: 0.025 (ok). Three-year average is contaminated by the 2023 restructuring; earnings quality is only moderately verifiable.
5. **Momentum reversal risk.** +7.8% 12-1 return on 27% vol with a −18.8% drawdown already recorded in the window; momentum is decelerating relative to DE/ETN. Momentum rank 3/9 is not a durable signal at this volatility.
6. **Idiosyncratic (non-factor) risk dominates.** R² 0.116 means factor-based sizing/hedging will not control risk — MMM's variance is litigation- and restructuring-driven. F-Score components confirm stagnation: 0 points on ROA improvement, accruals quality, gross-margin improvement.
7. **Sample/liquidity:** liquidity is not a constraint (mega-cap), but the peer cross-section is 9 names; all sector ranks above should be treated as indicative rather than statistically precise.

**Bottom line:** Quality (ROIC) and momentum pass, value is contradictory, and the revision signal fails validation. Neutral — the numbers do not justify a Buy, and ROIC strength does not justify a Sell. `Peer gross-profit/assets, peer accruals, and peer revision data were unavailable — Quality and Revision sector ranks rest on ROIC/ROA alone.`

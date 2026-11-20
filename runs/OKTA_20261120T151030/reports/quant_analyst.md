# Quant Analyst

- Symbol: OKTA
- Elapsed: 83.7s

---
## OKTA — Quantitative Factor & Risk Report
*Data verified against adjusted closes through 2026-10-30. Price $208.24; prior close basis used for all return math.*

### 1. Factor Scores

| Factor | Raw Metrics | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|---|
| **Value** | P/E 154.1 · EV/EBITDA 95.9 · P/FCF 41.9 · P/B 5.17 · FCF yield 2.4% · Fwd P/E (FY27E $3.93) 51.4x | **8** | 5/5 broad tech (bottom quintile) — **but 1/4 vs cyber peers** | **Strong Sell** (absolute) |
| **Momentum** | 12-1 = +37.5% (tool); +127.1% 12-mo total return vs SPY +14.3% | **88** | 1/5 | **Buy** (decelerating) |
| **Quality** | ROE 3.4% · ROIC 2.0% · GP/Assets 23.3% · Accruals −6.7% · F-Score **8/9** | **45** | 3/5 | **Neutral** |
| **Low Vol** | Ann. vol 78.2% · Beta 1.41 (1y) / 0.73 (5y) · MaxDD 28.6% | **5** | 5/5 | **Strong Sell** |
| **Earnings Revision** | FY31E EPS 5.57 vs 5.09 (+9.4%) — **only 4 analysts** | **70** | 2/5 (low confidence) | **Buy** (weak evidence) |

**Composite: 43/100 → NEUTRAL.** Momentum and revisions are offset by the worst-in-class valuation and volatility. Mandate-dependent: **Buy for momentum/event books, Avoid for value, quality, or low-vol books.**

**Critical cross-sectional nuance:** on absolute multiples OKTA is indefensible (154x earnings). Within its *actual* peer group it is the cheap one — every cyber comp is more expensive on every measure:

| | OKTA | ZS | PANW | CRWD |
|---|---|---|---|---|
| P/B | **5.2** | 12.4 | 9.9 | 52.4 |
| P/FCF | **41.9** | 37.9 | 65.8 | 178.7 |
| EV/EBITDA | **95.9** | 164.3 | 194.2 | 1,258.5 |

That is the entire bull case in one table — a relative-value trade inside an expensive sector, not a value stock.

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| 12-mo total return | **+127.1%** (91.69 → 208.24) | SPY +14.3%; excess **+112.8pp** |
| Alpha (ann., vs SPY) | **+126.5%** | **t ≈ 1.7 — NOT significant** |
| Beta (1y daily OLS) | **1.415** | t ≈ 3.9; profile 5y monthly beta = **0.733** |
| R² vs SPY | **0.069** | only 7% market-explained |
| Ann. volatility | **78.2%** | ~4.9% daily σ |
| Sharpe | **2.195** | SE ≈ 1.85 over 1yr → indistinguishable from zero |
| Sortino | **4.178** | downside dev ≈ 53% of total σ (positive skew) |
| Max drawdown | **−28.63%** | Jan 28 → Feb 23, 2026 |
| Current drawdown | **−10.3%** | from 52-wk high close $232.13 (Oct 9, 2026) |

**Return attribution is the story.** Two sessions generated the bulk of the year:

- **2026-05-29: +30.1%** (94.72 → 123.27)
- **2026-08-27: +28.6%** (134.42 → 172.91)

Compounded = **+67.4%** from **2 of ~270 trading days (0.7% of observations)**. Excluding both, the year returns **+35.7%** — respectable, but a different asset class of Sharpe (~0.5). This is an event-driven gap machine, not a persistent trend.

**Factor correlations (252d):** CRWD 0.81 · PANW 0.73 · ZS 0.68 · MSFT 0.38. OKTA is a cyber-beta proxy, not a diversifier.

### 3. Fundamental Context (why the multiple exists)
Revenue $2,919M FY26, **+11.8%** YoY vs +15.3% FY25 — **decelerating**. Gross margin improving (77.4% vs 76.3%), operating margin inflected positive (5.1% vs −2.8%), net income $235M, net cash ≈ $2.1B (EV < mkt cap). Recovery is real but growth is slowing into a 51x forward multiple.

### 4. Key Quant Risk Flags

1. **⚠️ Return concentration / event dependence (highest severity).** 67pp of a 127pp year came from two earnings gaps. Strip them and the risk-adjusted profile collapses. Any backtest treating this as a trend signal is overfit to two observations.
2. **⚠️ Alpha is not statistically significant.** t ≈ 1.7 with R² = 0.069. The 126% "alpha" is idiosyncratic jump risk, not skill-signal persistence. Do not size on it.
3. **⚠️ Sharpe/Sortino unreliable at n=1 year.** SE(Sharpe) ≈ 1.85 around a 2.195 estimate. Sortino 4.18 flatters a name with −28.6% peak drawdown.
4. **⚠️ Post-gap fade pattern — momentum reversal risk is live.** After the May gap: −19% (139.79 → 113.03). After the Aug gap: −19% (232.13 → 187.26). Currently **−10.3% off the high**, including a **−10.2% single day on Oct 16**. Recent 21-day return ≈ flat. Short-term momentum has already rolled over.
5. **Beta instability.** 1.41 (1y daily) vs 0.73 (5y monthly) — a 2x swing. Factor exposure is regime-dependent; hedges calibrated on either number will be wrong.
6. **Valuation has no margin of safety.** 154x trailing, 96x EV/EBITDA. With revenue growth already at 11.8%, a single deceleration print compresses the multiple violently — the mirror image of the upside gaps.
7. **Revision signal is statistically hollow.** Built on FY2031 estimates with **n=4 analysts** (±$0.16 spread). Corroboration comes from price targets, not estimates: 10 raises Sept–Oct 2026 to $215–245 (mean **$235.5**, ~13–17% above spot) — directionally supportive, but targets chase price, they don't lead it.
8. **Liquidity is NOT a flag.** ~2.5–3M shares/day, ~$36B cap, deep options market. Note the *inverse* risk: this is a crowded, high-attention name where gap risk is repriced instantly.

### 5. Verdict
**Composite Quant Signal: NEUTRAL (43/100).** Long cyber-momentum, short anything disciplined. The stock is the cheapest asset in an expensive peer group with genuinely inflected fundamentals (F-Score 8, positive operating margin, negative accruals) — but the return stream is two coin-flips, the alpha is statistically indistinguishable from luck, and the post-gap fade pattern is already underway. **Position sizing, not conviction, is the correct expression: half-size with defined gap risk, or wait for the current fade to resolve toward the $170–185 zone (prior gap-fill) before re-engaging momentum.**

*Sample-size caveat: 1-year price statistics (n≈252) support beta inference but not alpha, Sharpe, or Sortino inference. Peer ranks based on n=4 direct comps — indicative, not cross-sectional percentile.*

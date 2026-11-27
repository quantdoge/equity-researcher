# Quant Analyst

- Symbol: DDOG
- Elapsed: 75.6s

---
## DDOG — Quantitative Factor & Risk Assessment
**Datadog, Inc.** | Technology / Software–Application | Price $158.25 | Mkt cap $57.1B | Data as of ~last print 2026-11-25

**Methodology note:** DDOG's GICS Technology sector peers list is dominated by $500B–$5T mega-caps (AAPL, MSFT, NVDA) — not valid comparables for a $57B high-growth software name. I therefore ranked DDOG against a purpose-built cohort of six high-growth infrastructure/observability software peers: **CRWD, SNOW, NET, MDB, ZS**. Ranks below are out of 6 (~terciles, not quintiles — small-n, treat rank granularity as approximate).

### 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank (of 6) | Signal |
|---|---|---|---|
| **Value** | P/E 527.5 · P/B 15.4 · EV/EBITDA 281.6 · P/FCF 57.5 · FCF yield 1.74% | **3 / 6** | **Negative (absolute)** / Neutral (relative) |
| **Momentum** | 12-1 return **+13.17%** | **3 / 6** | **Positive but decaying** |
| **Quality** | ROE 2.89% · ROIC **−0.84%** · GP/Assets 0.412 · Accruals **−0.142** · F-Score 6 | **2 / 6** | **Mixed → top-tercile relative, low absolute** |
| **Low Vol** | Vol 74.5% (1y) / 66.7% (2y) · β 1.31–1.40 · MaxDD 46.3% | **4 / 6** | **Negative** |
| **Earnings Revision** | FY2030E EPS 4.88 vs 4.24 prior = **+15.09%** | n/a (n=5) | **Positive, but statistically thin** |

**Factor detail:** Value is the cohort's *only* profitable name (peers sport negative P/E: CRWD −1308, NET −977, ZS −592, MDB −356, SNOW −68), so relative value rank flatters it. On P/FCF (the one comparable metric) DDOG's 57.5x sits mid-pack (ZS 43.4, MDB 50.9, **DDOG 57.5**, SNOW 80.9, CRWD 160.1, NET 378.8). Forward P/E on FY2026E EPS of $2.746 (n=25 analysts) is **57.6x**; forward EV/EBITDA on FY2026E EBITDA of $1.14B is **≈47.8x** — both deeply growth-priced.

Quality ranks 2/6 because it wins on ROE (only positive in cohort) and gross-profit/assets (0.412, #2 behind MDB 0.470) but finishes **5/6 on accruals** (−0.142 vs SNOW −0.280). Tool labels quality "low" on absolute ROE thresholds; relative to peers it is the best of a weak group. **Piotroski F-Score 6 (moderate)** — fails on ROA improvement (ROA 1.62% vs 3.18%), no-dilution, and gross-margin improvement.

### 2. Price Statistics (β, α, Sharpe, Sortino)

| Metric | 2-Year (504d) | 1-Year (252d) |
|---|---|---|
| Annualised return | **35.82%** | — |
| Alpha vs SPY (ann.) | **+21.60%** | — |
| Beta vs SPY | **1.395** (R² = **0.084**) | 1.307 |
| Sharpe | **0.534** | 0.817 |
| Sortino | **0.840** | — |
| Annualised vol | 66.7–67.1% | 74.5% |
| Max drawdown | **−48.62%** | −46.34% |

**Alpha is not statistically significant.** R² of just 0.084 means only 8.4% of DDOG's variance is market-explained — it trades as a near-idiosyncratic instrument. With residual vol ≈64% over 2 years, the standard error on annualised alpha is ≈45%, giving **t ≈ 0.48 (p ≈ 0.63)**. The +21.6% alpha should be treated as noise, not skill or durable excess return. Beta (t ≈ 30+) is highly significant. Sortino/Sharpe ratio of 1.57 implies downside deviation ≈43% vs 67% total vol — returns are not downside-dominated, but absolute risk is extreme.

**Realised price action (12-month path):** the stock bottomed at $98.01 (Feb 24, 2026), rallied to a **$293.26 close high on Oct 9, 2026**, and has collapsed **−46.0% to $158.25 in ~33 sessions**. Event gaps are violent: **+31.4%** (May 7), **−19.0%** (Aug 6), **−13.6%** (Oct 30), **−14.4%** (Nov 4), **−7.5%** (Nov 5). The trailing month alone is roughly **−12% to −41%** depending on start date.

### 3. Composite Quant Signal: **NEUTRAL** (composite ≈ 58/100)

Weighted cohort-percentile composite: Value 50, Momentum 55, Quality 75, Low Vol 40, Revision 70. The book splits cleanly — **trend and revisions positive, valuation and risk negative** — and the trend leg is decaying fastest, so I cannot underwrite a Buy on this evidence.

**What the numbers actually support:** genuine fundamental cash generation — FY2025 FCF $1.00B on $3.43B revenue (**29.2% FCF margin**), FCF conversion 929% of net income, negative accruals in all four years, and a Rule-of-40 score of **56.9**. Revenue +27.7% FY2025 (vs +26.1% FY2024), with consensus FY2026E +32.2% to $4.53B.

**What kills the bull case:** (a) **SBC of $751M = 21.9% of revenue and 7.0× net income**, growing +31.6% YoY — *faster than revenue*. SBC-adjusted FCF is only **$250M**, a true FCF yield of **0.44%** (P/SBC-adj-FCF ≈ **228×**), and Rule-of-40 falls to ~35. (b) Share count 324M → 336M → 347M (+3.4%/yr dilution, F-Score dilution test failed). (c) GAAP operating income was **negative (−$44M)** in FY2025; the $108M net profit is interest-income-driven. (d) FY2030E revision is a 5-analyst, 5-years-out figure — statistically meaningless as a revision signal.

### 4. Key Quant Risk Flags

1. **Momentum reversal in progress — highest-priority flag.** The +13.17% 12-1 momentum score is entirely a June–October artifact. The excluded recent month is deeply negative and the name is **−46% off its Oct 9 high**. Classic "positive trailing score, broken trend" setup — momentum-factor exposure here is a *fading* leg, not a durable one.
2. **Negative target-price revisions contradict the positive EPS revision.** On Nov 4–5, 2026, Stifel cut PT to $245, Scotiabank to $260, Bernstein to $273, RBC to $270, TD Cowen to $275 — **every one a "lowered"**, none raised. Mean PT ≈$264.6 implies +67% upside, but universally falling PTs into a −46% drawdown is the signature of analysts chasing price down, not leading it. This materially weakens the +15% EPS revision signal.
3. **Volatility/event gap risk.** 74.5% annualised vol, β 1.31–1.40, and four ≥7% single-day earnings gaps in 12 months. Max drawdown 46–49% and largely *realised in the last seven weeks*. Any sizing must assume a 1.4× market beta with roughly 2× market vol.
4. **Factor crowding / valuation fragility.** At 57.6x forward earnings and ~48x forward EV/EBITDA, DDOG carries no valuation cushion — 100% of the return case rests on estimates being met. With R² of only 0.084 there is almost no market beta to hide behind; drawdowns are idiosyncratic.
5. **Liquidity is adequate** — 2.3–26M shares/day, no concern. Not a risk.
6. **Sample-size caveats (explicit):** the revision score rests on **5 analysts** and a **2030** target; cohort ranks use **n=6**, so "3/6" and "4/6" are tercile-level distinctions only. The 1-year momentum/vol estimates use ~252 observations and are reasonably stable; the 2-year alpha with R²=0.084 is not.

**Bottom line:** Statistically, DDOG screens as a **high-quality, high-growth, expensively-valued, high-beta name with a broken short-term trend and insignificant alpha**. The quality and cash-flow evidence justifies coverage; the value, volatility, and momentum-reversal evidence argues against adding here. Neutral until either valuation compresses to a defensible ~35x forward earnings or price momentum stabilises above the Nov lows.

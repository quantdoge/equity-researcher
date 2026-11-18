# Quant Analyst

- Symbol: NOW
- Elapsed: 24.2s

---
## ServiceNow (NOW) — Quantitative Factor Report
*Technology / Software–Application · Price $92.90 (as reported) · Mkt cap ~$97.3B*

---

### 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank | Signal |
|--------|-------------|-------------|--------|
| **Value** | P/E 55.6 · EV/EBITDA 31.1 · P/FCF 21.3 · P/B 7.5 | n/a (see note) | **Negative** — rich on earnings, only middling on cash |
| **Momentum** | +17.34% (12-1 total return) | n/a | **Positive** — trend intact, no reversal signal |
| **Quality** | ROE 13.48% · ROIC 11.87% · GPA 0.395 · Accruals −0.1419 · F-Score 5/9 | n/a | **Mixed** — excellent cash conversion, mediocre margins |
| **Low Vol** | 69.05% annualised vol · β 0.753 · MaxDD −41.56% | n/a | **Negative** — high absolute vol |
| **Earnings Revision** | +23.22% (current vs 3-mo-prior EPS) | n/a | **Positive** — upgrade |

*Sector rank is reported as n/a. The peer set returned is mega-cap Technology across semiconductors/consumer electronics (AAPL, MSFT, NVDA, TSM, AVGO, AMD, MU, ASML, CSCO), which is a poor comparison group for a mid-cap SaaS workflow name. Rather than import a wrong cross-section, I am flagging the gap — a proper rank needs a Software–Application peer universe.*

**Quality detail:** accruals ratio is *negative* in all four years (−0.180, −0.096, −0.139, −0.142), meaning operating cash flow persistently exceeds net income. That is the single strongest quality datapoint here — earnings are cash-backed, not accrual-inflated. Offsetting it: F-Score 5/9 with losses on ROA improvement (F3), gross-margin trend (F8), asset turnover (F9), and **net dilution (F7 = 0)**. ROIC has improved (4.9% → 7.7% → 11.5% → 11.9%) but ROE has *fallen* from 22.7% (2023) to 13.5%, so the returns trend is decelerating on equity.

---

### 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | 5.91% |
| Annualised volatility | 69.05% |
| Beta (vs SPY) | 0.753–0.757 |
| Alpha (annualised) | +3.55% |
| R² | **0.025** |
| Sharpe ratio | 0.085 (0.15 alternate calc) |
| Sortino ratio | 0.106 |
| Max drawdown | −41.56% |

**Read this carefully:** R² of 0.025 means the market explains only 2.5% of NOW's return variance. The +3.55% alpha is therefore **not statistically significant** — with residual vol ≈ 69% over 252 days, the standard error on alpha is ~4.4%, giving a t-stat of roughly **0.8**. This alpha is indistinguishable from zero. Likewise, a Sharpe of 0.085 and Sortino of 0.106 mean the trailing year delivered almost no return per unit of risk taken. The stock earned 5.9% while carrying 69% vol and a 41.6% drawdown — an unattractive realised reward-to-risk profile.

---

### 3. Composite Quant Signal: **NEUTRAL**

Reasoning: the two forward-looking signals are genuinely constructive — positive 12-1 momentum (+17.3%) and a +23.2% upward EPS revision — and these carry the most predictive weight in the framework. Quality on cash conversion is a real positive. But they are offset by: (a) a demanding valuation on earnings (P/E 55.6), (b) high absolute volatility that fails the low-vol screen outright, and (c) risk-adjusted returns (Sharpe 0.085) that are effectively flat. A momentum-plus-revision long is defensible, but it is a beta-lite, high-vol expression with no measurable alpha support. Neutral, not Buy.

---

### 4. Key Quant Risk Flags

- **⚠ Data integrity — price/size inconsistent.** Reported price of $92.90 with 1.047B diluted shares and ~$97B market cap does not reconcile with ServiceNow's actual trading level (~$900/share, ~207M shares). Ratios (P/E, P/B, EV/EBITDA) and all return-based statistics are internally consistent and usable, but **do not rely on the absolute price, market cap, or book value per share** without verification.
- **⚠ Volatility level looks ~2x too high.** 69% annualised vol against a beta of 0.75 is internally contradictory — a sub-1 beta stock rarely carries double the benchmark's volatility. The low-vol and Sharpe/Sortino inputs should be treated as suspect.
- **⚠ Earnings revision is not the standard 12-month forward.** The revision compares estimates for period **2030-12-31**, a long-dated horizon. Directionally bullish, but far more speculative than a conventional 1-year forward revision and not comparable across names.
- **Momentum reversal risk:** +17.3% 12-1 momentum with 69% vol implies a high-vol momentum profile — the most exposed cohort to sharp factor unwinds.
- **Factor crowding:** large-cap software/AI-workflow is a heavily owned thematic; positive momentum and upward revisions here are widely visible, raising crowding risk.
- **Drawdown tolerance:** −41.6% max drawdown over the trailing year requires position sizing for a >40% peak-to-trough loss.

**Sample size note:** 252 trading days / 12 monthly observations. The alpha, Sharpe and Sortino estimates all carry wide confidence intervals at this n; the R² of 0.025 makes the alpha estimate statistically uninformative rather than merely imprecise.

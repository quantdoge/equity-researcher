# Quant Analyst

- Symbol: ASTS
- Elapsed: 79.8s

---
## ASTS — Quantitative Factor & Risk Report
**AST SpaceMobile, Inc.** | Communication Services / Telecom Services | Price $26.02 | Mkt cap $6.66B | 256.0M sh | 2025A revenue ~$58M

---

### ⚠️ Lead finding: the price-derived layer fails internal consistency checks

Before any score, three independent red flags in the price statistics:

| Check | Engine output | Independent OHLCV (`get_price_history`) |
|---|---|---|
| 12-1 momentum | **−36.93%** | +268% (31.63 → 116.37) |
| Max drawdown | **−82.52%** (implies ~$149 peak) | −34.9% (122.09 → 79.51) |
| Annualised return | **−105.32%** | +270% total |

1. **−105.32% annualised return is mathematically impossible** for a long-only equity (floor is −100%). This is the signature of *daily arithmetic returns being summed rather than compounded* — a standard implementation bug that inflates magnitude under high volatility. The same defect contaminates the **−121.7% alpha**.
2. **The OHLCV tape and the fundamental snapshot disagree.** `get_price_history` ends at **$80.20**, but `calculate_valuation_ratios`, the company profile, and `calculate_return_on_capital` all price the stock at **$26.02**. The $26.02 figure is the *internally coherent* one: P/E −19.42 × $26.02 = −$1.34 EPS, which reconciles to 2025 net income of −$342M ÷ 256M shares. P/B 2.78 × BVPS $9.35 = $26.02 exactly.
3. **Benchmark betas are implausible.** The correlation matrix reports **VZ/SPY = −0.178** and **T/SPY = −0.159**. Large-cap telecoms do not carry negative market beta over 252 days. The SPY series used in these regressions is misaligned or synthetic.

**Conclusion: every price-derived statistic below is non-actionable.** I report the engine's numbers as requested, but the fundamental layer is the only trustworthy evidence here.

---

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E −19.4 · P/B 2.78 · EV/EBITDA −17.8 · P/FCF −5.86 | **n/m** | **Meaningless** — negative denominators |
| **Momentum** | −36.93% (12-1) | n/a | Negative *(contradicted by tape)* |
| **Quality** | ROE −14.3% · GP/Assets 0.76% · Accruals −5.39% | n/a | **Low** |
| **Low Vol** | Vol 106.4% ann. · Beta 3.31 · Max DD −82.5% | n/a | **Worst decile** |
| **Earnings Revision** | +97.75% | n/a | "Upgrade" — **statistically void** |

**On each:**

- **Value:** Four of four multiples have negative denominators (loss-making on EPS, EBITDA, and FCF). A value factor cannot be computed on a pre-revenue company — a negative P/E is not "cheap," it is undefined. **Do not treat this as a value signal in either direction.** The only usable valuation anchor is **P/B 2.78x** against book value that is overwhelmingly cash from equity raises, not productive assets.
- **Momentum:** Engine says −36.9%; the tape says +268%. I cannot resolve which is real, so momentum is **unratable**. Note that the recent 21-day window *is* unambiguously negative on the tape (116.37 → 80.20, **−31.1%**), so a sharp near-term reversal is real regardless of which series is correct.
- **Quality:** Genuinely low, but **directionally improving and that is the one constructive datapoint in this report**. ROIC: −77.6% (2023) → −28.8% (2024) → **−6.21% (2025)**. Accruals swung from +0.285 (2022, warning) to **−0.054 (2025, clean)** — earnings are now *understating* cash flow. Piotroski F-score **5/9 (Moderate)**, with F3 (ROA improvement), F4 (accruals quality), F6, F8, F9 all passing.
- **Low Vol:** 106% annualised vol and 3.31 beta put ASTS in the extreme tail. A 3.3 beta means a 10% SPY drawdown mechanically implies ~33% on ASTS. This is a **high-beta convexity bet, not a low-vol holding** — it inverts the factor entirely.
- **Earnings Revision:** The +97.75% "upgrade" compares the **2030** EPS estimate ($3.65) to its value three months ago ($1.85). Per `get_analyst_estimates`, **2030 carries `num_analysts: 1`**. A single analyst revising a five-year-out number is not revision momentum — it is noise. The estimates that *do* have coverage (7–8 analysts) still show losses through 2027: 2026E EPS **−$2.35**, 2027E **−$1.36**, with the first profit only in 2028E (+$0.03). **No genuine revision signal exists.**

---

### 2. Price Statistics (engine-reported — treat as unreliable, see above)

| Metric | Value | Assessment |
|---|---|---|
| Alpha (ann., vs SPY) | −121.7% | Impossible; arithmetic-sum artifact |
| Beta | 3.33 (R² 0.250) | High beta credible; R² low → 75% idiosyncratic |
| Beta (profile) | 2.85 | Conflicts with regression beta 3.33 |
| Sharpe | −0.985 | Negative on both calc methods (−0.898 alt) |
| Sortino | −1.749 | Downside dev ~1.8× total vol |
| Annualised vol | 106.4% | Plausible for this name |
| Max drawdown | −82.52% | Inconsistent with tape (−34.9%) |
| Annualised return | −105.32% | **Mathematically impossible** |

**Sharpe/Sortino:** The Sortino/Sharpe ratio of 1.78 indicates returns are dominated by *downside* dispersion — the return distribution is negatively skewed. With a 0% risk-free assumption and a negative numerator, neither ratio is economically meaningful; both simply confirm "this lost money on a risk-adjusted basis over the window used." **Note: if the OHLCV tape is the correct series, the true Sharpe is strongly positive and these signs are simply wrong.** The sign of the Sharpe is the single most important unresolved question in this report.

---

### 3. Composite Quant Signal

**Mechanical composite: SELL** (4 of 5 factors negative or worst-decile)
**Conviction: LOW — signal not actionable.**

The mechanical score is driven by momentum, low-vol, and quality. Two of those three rest on the corrupted price layer. The one factor that is both reliable and improving (ROIC trajectory, accruals, F-score) is not in the composite. I will not issue a Strong Sell on arithmetic that produces a −105% annual return.

**If forced to act on fundamentals alone: Neutral.** A pre-profit, cash-burning satellite operator at 2.78x cash-heavy book, with ROIC still negative but improving 70 points in two years, is a **binary execution story** — not a factor trade. Factor models have no explanatory power on this security.

---

### 4. Key Quant Risk Flags

1. **🚩 DATA INTEGRITY — SEVERE.** Two mutually exclusive price series in the same dataset ($26.02 vs $80.20); an impossible −105% return; negative SPY correlation for VZ/T. **Do not let any price-derived statistic reach the investment memo.** Re-run required.
2. **Momentum reversal risk — EXTREME.** Even on the bullish tape, ASTS fell −31% in the last month and −34% from its January peak. 106% vol means ±7% daily moves are ~1 sigma.
3. **Factor crowding — LOW, but wrong reason.** ASTS correlation to telecom peers is **negative** (VZ −0.14, TMUS −0.14, T −0.11). It is *not* a telecom exposure and provides no sector diversification benefit; it is a standalone 0.50-correlated-to-SPY idiosyncratic bet. Sector-relative factor ranking is **economically meaningless** — comparing a pre-revenue satellite startup to VZ and T on P/E or ROIC is not a comparison.
4. **Dilution risk — CONFIRMED.** Piotroski F7 (*no dilution*) = **0**. Share count is rising; the company funds itself through equity issuance, so per-share metrics will be structurally diluted. Book value per share is not a floor.
5. **Liquidity — NOT a constraint.** Volume 5–40M shares/day (~$150M–$3B notional). This is one of the few clean readings.
6. **Estimate coverage — THIN.** Zero analyst coverage of profitability before 2028; the 2030 datapoint rests on n=1.

---

**Bottom line:** On the fundamentals, ASTS is a low-quality, high-beta, pre-profit, dilutive growth name with a genuinely improving capital-efficiency trend and no valid value, momentum, or revision signal available. The quantitative output as delivered is **not fit for use** — the price layer must be re-run before this feeds the memo.

# Quant Analyst

- Symbol: CRWD
- Elapsed: 48.6s

---
# CRWD — Quantitative Factor & Risk Scorecard
**CrowdStrike Holdings | Technology / Software–Infrastructure | Price $208.97 | Mkt cap ~$209bn**

## 1. Factor Scores

| Factor | Score / Raw Values | Rank (peer set*) | Signal |
|---|---|---|---|
| **Value** | P/E −1306 (negative EPS, meaningless); EV/EBITDA **1,124x**; P/FCF **159.9x**; P/B **46.9x**; Fwd P/E 130x (FY28E EPS $1.61); EV/Sales ~27.8x (FY28E rev $7.39bn) | **3 of 4** (bottom half) | **Strongly negative** |
| **Momentum (12-1)** | **+20.7%** (252d, ex-last-21d) | **1 of 4** (best) | **Positive / strong** |
| **Quality** | ROE **−3.63%**, ROIC **−5.54%**, ROA −1.47%; GP/Assets **0.324** (2nd best); Accruals ratio **−0.160** (best = high earnings quality) | **2 of 4** | **Mixed / low** |
| **Low Vol** | Ann. vol **63.2%**; Beta **1.058** (vs SPY); Max DD **25.1%** | **3 of 4** on vol, 2 of 4 on beta | **Negative** |
| **Earnings Revision** | FY31E EPS $2.935 vs $2.44 prior (**+20.3%**) | **2 of 4** (1st excl. a PANW data error) | **Upgrade — but see caveat** |
| **Piotroski F-Score** | **4 / 9 (Weak)**: −ROA, +op CF, −ΔROA, +accruals, +leverage, +equity, **−dilution**, −gross margin, −asset turnover | — | **Negative** |

\*Peer set = PANW, FTNT, NET (closest security/infrastructure-software comps). **n=3 is too small for statistically meaningful quintile ranks** — these are ordinal flags, not z-scores. The vendor "sector" universe is Technology mega-caps (AAPL/NVDA/MSFT), which is not a valid comparison cohort for CRWD.

**Peer context used for ranking:** CRWD has the best momentum (+20.7% vs FTNT +14.6%, NET +5.1%, PANW +1.6%) on the highest vol (63.2% vs FTNT 54.0%, PANW 56.8%, NET 71.3%) and the worst EV/EBITDA except NET. Only FTNT screens as a genuine value/quality name (P/E 54, ROE 150%, GP/A 0.527, F-Score-quality "high").

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **130.7%** |
| Annualised volatility | **62.1–63.2%** |
| Beta vs SPY | **1.06** (5-yr profile beta 1.15) |
| Alpha (annualised) | **+100.6%** |
| R² vs SPY | **0.073** |
| Sharpe | **2.10** |
| Sortino | **3.81** |
| Max drawdown | **25.1%** |
| Alpha t-stat (50.6/59.8 residual-IR proxy) | **≈1.7 → not significant at 95%** |

**The alpha is statistically hollow:** R² of 0.073 means only **7.3%** of CRWD's variance is explained by the market. The alpha estimate is a high-variance residual artifact of a single-year, high-idiosyncratic-risk sample (and the low-vol module independently reports Sharpe 1.755 vs 2.103 from the Sharpe module — internally inconsistent return conventions).

## 3. Composite Quant Signal: **NEUTRAL** (tactical momentum tilt only)

Two of five factors score positively (Momentum #1 of 4, Revisions positive), offset by a bottom-half value score on egregious multiples, weak profitability (negative ROE/ROIC, F-Score 4) and above-peer volatility. On this framework's composite, momentum + revision alpha is offset almost exactly by value + quality drag. **Not a Strong Buy** despite the strong 12-1 return: the return quality is unverifiable (R² 0.07, t≈1.7) and the valuation provides zero margin of safety.

## 4. Key Quant Risk Flags

1. **⚠️ Data integrity / price-level conflict (material).** The OHLCV feed ends at **$107.41** (2026-02-13) while the profile/valuation feed prices CRWD at **$208.97** (ratio 1.945x, consistent with an unapplied split adjustment). Consequently the 130.7% annualised return and 62% vol cannot be reconciled with the raw series, which shows only **+23.7%** from 2025-01-02 ($86.84) to 2026-02-13 ($107.41), or ~21% annualised. **Treat all return/alpha/Sharpe magnitudes as unreliable; direction is intact.** Sizing decisions should not be made on these magnitudes.
2. **Momentum reversal already under way.** The raw series peaked at **$139.38 (2025-11-10)** and printed a **−32.4%** trough at $94.29 (2026-02-05) — a drawdown *deeper* than the 25.1% reported by the vol module, and hidden by the 21-day exclusion in the 12-1 calculation. Crude momentum is decelerating into a de-rating.
3. **Revision signal is thin and long-dated.** The +20.3% "upgrade" is measured on **FY2031** estimates with only **5 analysts** (vs 27 on FY2028). Low statistical reliability — this is likely a roll-forward artifact, not conviction buying. Peer PANW's −100% revision is plainly a data error (EPS 0.0), showing the revision feed is noisy.
4. **Valuation compression risk.** At ~28x FY28E sales and 130x FY28E EPS, the stock has no valuation support; multiple de-rating, not fundamentals, is the dominant risk (63% vol, −25% to −32% drawdowns are normal outcomes here, not tail events).
5. **Dilution & accrual-adjusted optics.** F-Score flags share issuance (F7=0) and no asset-turnover improvement. The very negative accruals ratio (−0.160) is flattered by SBC-heavy, non-cash compensation in a loss-making P&L; the accounting quality signal is not corroborated by cash profitability (ROIC −5.5%, deteriorating from −0.06% in FY24).
6. **Liquidity: not a constraint** (~10–20m shares/day, ~$14bn+ daily turnover).
7. **Analyst targets are stale/forward-inconsistent** (dated through Nov-2026 while the last price bar is Feb-2026). Recent 10-target median ≈ **$270** vs $208.97 = +29% implied — supportive, but stale stamps and a 177-to-312 range (≈76% spread) imply low dispersion-adjusted signal value.

**Bottom line:** Strong momentum & positive revisions, but unverified alpha (R² 0.07, t≈1.7), bottom-half value, weak quality (F-Score 4, ROIC −5.5%) and a live −32% momentum reversal. **Neutral — do not add on momentum alone; the quantitative edge is not statistically established.**

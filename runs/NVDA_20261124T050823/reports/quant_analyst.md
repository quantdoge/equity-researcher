# Quant Analyst

- Symbol: NVDA
- Elapsed: 58.9s

---
## NVDA — Quantitative Factor Report
**Price $165.05 (Nov 23, 2026) · Market cap $3.98T · Technology / Semiconductors · 252-day estimation window**

---

### 1. Factor Scores Table

| Factor | Raw Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 33.7 · EV/EBITDA 27.6 · P/FCF 41.9 · composite −33.68 | 9th of 25 (mega-cap universe); **2nd cheapest of 4 semis** | Neutral / mildly positive |
| **Momentum** | 12-1 return **−3.96%** | Not in top 10 of universe | **Negative** |
| **Quality** | ROE 76.3% · ROIC 77.3% · ROA 58.1% · GP/Assets 0.742 · accruals 0.084 | **4th of 25** | **Positive** (with caveat) |
| **Low Vol** | Ann. vol **56.25%** · β 2.44 · Max DD **−47.5%** | Bottom quintile | **Strongly negative** |
| **Earnings Revision** | +25.85% (see flag) | Unreliable | **Neutral — data suspect** |

**Value detail.** Within semiconductors the multiple stack is more attractive than the "expensive AI trade" narrative implies: MU 9.5x P/E → **NVDA 33.7x** → AVGO 65.7x → AMD 171.1x. NVDA is 2nd cheapest of 4 on P/E, EV/EBITDA *and* P/FCF — a consistent 2nd-place finish, not a one-multiple artifact. It is expensive against the broad 25-name universe (negative composite score), but that is a mega-cap-tech-wide phenomenon, not NVDA-specific.

**Quality detail.** ROE 76.3% and ROIC 77.3% are top-decile in absolute terms, and the 4th-of-25 rank confirms it. But the trend is decelerating: **ROIC 90.9% (FY25) → 77.3% (FY26)**, ROE 91.9% → 76.3%. Piotroski F-score only **5/9** (moderate), failing F4 (accruals quality), F3 (ROA improvement), F8 (gross margin), F9 (asset turnover). A 76% ROE with a 5/9 F-score is a company whose *level* of profitability is elite but whose *direction* is no longer improving.

**Momentum detail — critical.** The −3.96% 12-1 figure **excludes the last 21 trading days**, which contained the crash. Measured through today, trailing 12-month total return is **−20.0%** ($206.39 → $165.05). The 12-1 construction is systematically flattering NVDA right now; the true momentum reading is materially worse and would rank in the bottom quintile.

**Revision detail — FLAGGED AS UNRELIABLE.** The +25.85% "upgrade" compares the FY**2031** consensus ($33.19) to a prior estimate of **$26.37175** — which is *numerically identical* to the current FY2030 consensus ($26.37175, 19 analysts). This is a period-alignment artifact, not a genuine revision; the tool appears to have compared a forward year against what is now the adjacent year. Corroborating evidence that true revision momentum is **not** strongly positive: of 8 price targets published Nov 18, UBS and Piper Sandler both **lowered** targets, HSBC and Melius reiterated **Hold**, and Truist titled its note "more questions than answers." Median target $225 (+36% vs spot) still implies upside, but the *direction* of the last print is mixed-to-negative. Treat revision momentum as **neutral, not bullish**.

---

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY) | **−23.21%** |
| Beta (vs SPY) | **2.454** (profile beta 2.25) |
| R² | 0.4885 |
| Annualised return | −7.18% |
| Annualised volatility | 57.07% |
| **Sharpe ratio** | **−0.126** |
| **Sortino ratio** | **−0.221** |
| Implied downside deviation | 32.5% (7.18 ÷ 0.221) |
| Max drawdown | **−47.53%** |
| 52-wk close range | $125.53 – $239.24 |

**Interpretation.** Beta 2.45 with R² 0.49 means NVDA is roughly a 2.5x-levered market bet where half the variance is still idiosyncratic. Alpha of −23.2% annualised over a 252-day window is a large, economically meaningful underperformance — but with R² 0.49 and 57% vol, the standard error on that alpha is wide (approximately ±12–15% at 1 s.e.), so treat it as "significantly negative, magnitude uncertain" rather than a precise −23%.

**Sharpe/Sortino consistency check passes.** Sortino (−0.221) is more negative than Sharpe (−0.126) despite returns being negative — mathematically correct, since downside deviation (32.5%) < total deviation (57.1%) and the numerator is negative. Both ratios confirm the stock destroyed risk-adjusted value over the window: an investor was paid **negative** return for taking 2.5x market risk.

**Drawdown detail.** Peak close $239.24 (Oct 6) → trough close $125.53 (Nov 20) = **−47.5% in 32 trading days**, followed by **+31.5% in a single session** (Nov 20 → Nov 23). A one-day move of that magnitude is a liquidity/dislocation event, not normal price discovery, and it renders the trailing volatility estimate (57%) likely *understated* relative to current realized conditions.

---

### 3. Composite Quant Signal: **NEUTRAL** (negative tilt — "cheap and good, but a falling knife")

The factors split cleanly along a fundamental/price axis:

- **Fundamental factors support the stock**: Quality 4/25 and Value 9/25 (2nd cheapest of 4 semis). A top-quintile quality + top-tercile value combination is genuinely rare and historically the most durable source of excess return.
- **Every price-based factor opposes it**: momentum negative and worse than reported, low-vol bottom quintile, alpha −23%, Sharpe and Sortino both negative.

This is the textbook profile of a high-quality franchise in an active de-rating. The quant framework does not have a factor that resolves "quality cheapening" vs. "momentum breaking" — that requires a catalyst view outside my remit. **Neutral is the honest composite**; it is not a Buy because the price factors are uniformly hostile, and not a Sell because 76% ROE at 34x earnings is not a valuation a quant model can call stretched against 171x AMD or 66x AVGO.

---

### 4. Key Quant Risk Flags

1. **Active momentum reversal / drawdown in progress.** −47.5% peak-to-trough, then a +31.5% single-day snap-back. The 12-1 momentum metric **structurally hides** the worst of this. Do not read −3.96% as "mildly negative" — it is a window artifact.
2. **Accruals deterioration — genuine earnings-quality red flag.** Accruals ratio has risen three consecutive years: **0.025 → 0.079 → 0.084**. FY26 net income $120.07B vs operating cash flow $102.72B — a **$17.35B gap**. This is the single cleanest negative fundamental signal in the dataset and it is corroborated by F-score F4 = 0. Growth in reported earnings is outrunning cash generation.
3. **Data integrity — two failures, disclosed.** (a) Earnings revision score is contaminated by period misalignment (above). (b) **TSM valuation data is unusable** — P/E 1.10, EV/EBITDA −0.06, negative enterprise value — clearly a currency/units error (book value per share $1,040 vs. price $363). The TSM comparison in my peer set is therefore excluded from the value ranking; the 4-name semiconductor comparison rests on MU, AVGO, AMD only.
4. **Factor crowding / index concentration.** $3.98T cap, 4th largest in universe. Correlations: SPY 0.70, TSM 0.71, MU 0.53, AVGO 0.43, AMD 0.45. At β 2.45, any long NVDA position is functionally a 2.5x market-beta position with a semiconductor-cycle overlay. Crowding risk is high; note that MU (the cheapest semi at 9.5x) correlating only 0.53 suggests the market is already differentiating within the complex.
5. **ROIC deceleration.** 90.9% → 77.3% over two years. Still elite, but the quality factor score is a *level* measure and masks the trend. A further 13pt decline would move NVDA out of the top quintile.
6. **Sample-size caveat.** All statistics rest on a single 252-day window — one regime, one drawdown. R² 0.49 means half the return variance is unexplained by market beta, so alpha, Sharpe and Sortino are all estimated with wide confidence intervals. **Nothing here is statistically robust at the 4+ year horizon**; treat the point estimates as directional.
7. **Liquidity: no concern.** 776M shares traded Nov 23; $3.98T cap. This is the one risk flag I can fully dismiss.

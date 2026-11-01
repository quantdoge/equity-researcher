# Quant Analyst

- Symbol: ILMN
- Elapsed: 28.2s

---
# ILMN — Quantitative Factor & Risk Report

**Illumina, Inc.** | Healthcare — Medical Diagnostics & Research | Price $235.99 | Mkt cap $35.6B
Peer set: TMO, WAT, A, RVTY, BIO, MTD (life-science tools/diagnostics; sector tool returned mostly large-cap pharma, so I substituted true comparables)

---

## 1. Factor Scores Table

| Factor | Raw Score | Sector Rank (of 7) | Signal |
|---|---|---|---|
| **Value** | P/E 43.3 · EV/EBITDA 25.9 · P/FCF 39.5 | **4th (50th pct)** | Neutral |
| **Momentum** | 12-1 return **+38.7%** | **1st (100th pct)** | **Strong positive** |
| **Quality** | ROE 31.2% · GP/Assets 0.435 · Accruals −0.0345 | **1st (100th pct)** | **Strong positive** |
| **Low Vol** | 50.5% ann. vol · Beta 1.02 · MaxDD 25.2% | **5th of 5 (0th pct)** | **Strong negative** |
| **Earnings Revision** | +11.5% (2030 consensus) | n/a — data quality poor | Positive (qualified) |
| *Piotroski F-Score* | **8 / 9** (only asset turnover fails) | — | Strong |

**Value detail (rank of 7):** P/E 6th, EV/EBITDA 3rd, P/FCF 3rd. ILMN is cheap on EBITDA and cash flow but expensive on earnings — the P/E gap is the tell, since 2025 is the first profitable year after 2023–24 losses (−$4.4B, −$1.2B). Only BIO (P/E 13.4, EV/EBITDA 8.4) is genuinely cheap in this group.

**Quality detail:** Top of the peer set on ROE (31.2% vs WAT 25.1%, A 19.3%, TMO 12.6%) and second on gross profit/assets behind MTD (whose ROE is meaningless at −3,677% on near-zero equity). Accruals are negative (OCF $1,079M > NI $850M), i.e. cash earnings exceed book earnings — a genuine quality positive.

**Low-vol detail:** Highest volatility in the comparable set — 50.5% vs RVTY 40.2%, WAT 37.9%, A 34.3%, TMO 31.5%. ILMN is a large-cap trading with small-cap risk. This is the single weakest factor.

---

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **+82.2%** |
| Annualised volatility | **50.9%** |
| **Sharpe ratio** | **1.61** |
| **Sortino ratio** | **2.13** |
| **Alpha (annualised)** | **+57.5%** |
| **Beta** | **1.02** |
| **R² vs SPY** | **0.070** |
| Max drawdown | −25.2% |

**Critical caveat on alpha:** R² of just 0.07 means only 7% of ILMN's variance is explained by the market. The +57.5% alpha is therefore very imprecisely estimated — with 252 observations and this much idiosyncratic noise, the standard error on alpha is enormous and it is **not statistically distinguishable from zero at conventional confidence**. It is also nearly collinear with the 82% raw return, i.e. the "alpha" is mostly ILMN-specific idiosyncratic rerating, not a durable skill/factor premium.

**Beta instability flag:** The 1-year daily regression gives beta 1.02; the company profile reports 1.416 (longer-window, likely 5-year monthly). A 40% swing in measured beta across windows signals unstable factor loading — do not rely on either number for risk budgeting.

**Sharpe/Sortino divergence:** Sortino (2.13) is 32% above Sharpe (1.61), indicating downside volatility is materially lower than upside volatility. Positive-skew profile — favourable, but computed on a window with an 82% return and will not persist.

---

## 3. Composite Quant Signal: **BUY**

Rationale: #1-of-7 on both momentum and quality, an 8/9 F-Score, and a mid-pack value score is an unusually clean quantitative profile. Momentum + quality co-ranking in the top quintile is the rarest and most rewarded combination in cross-sectional factor work. Value at the 50th percentile provides no offset, but no drag either.

**Downgraded from Strong Buy on three grounds:** (1) low-vol is dead last — the 50% volatility forces position-size reduction that materially cuts risk-adjusted contribution; (2) the value signal is not confirming (P/E 43x); (3) the alpha statistic fails a significance test.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** +38.7% 12-1 momentum on 50% volatility. High-momentum/high-vol names are the most exposed to sharp reversal and crowding unwinds; the −25.2% max drawdown occurred within this same window. Momentum is the fastest-decaying factor in the model.
2. **Alpha/regression validity — HIGH.** R² 0.070. Treat the +57.5% alpha as noise-contaminated, not as evidence of outperformance skill.
3. **Earnings revision data quality — HIGH.** The revision tool returned **+11.5% on the FY2030 consensus, covered by only 2 analysts** (a 3-month "prior" was actually the FY2029 figure — a period mismatch, not a same-period revision). This is not a reliable signal. **Corroborating softer evidence is genuinely bullish**: recent price targets were raised broadly (Canaccord $205→$300, Guggenheim $226→$305, Leerink $220→$300, Piper $225→$305, Argus $180→$235), though **Barclays' $200 target sits below the current $235.99 price** and Stephens just downgraded to Equal Weight. Target dispersion of $200–$305 (~50% of the mean) confirms high uncertainty.
4. **Quality score is recovery-inflated — MODERATE.** ROE of 31.2% is measured off an equity base depressed by the 2023–24 losses. It will not persist at this level as book equity rebuilds; do not annualise it into a DCF.
5. **Low-vol / liquidity — MODERATE.** 50% vol is bottom-quintile for a $35B medtech; any factor portfolio must halve ILMN's weight versus a TMO-class holding.
6. **Sample-size note.** All statistics are 252-day (1 year), single-window. Factor ranks rest on 7 names, of which only 5 have volatility data. Ranks are indicative, not statistically robust — a 6-peer cross-section cannot establish quintile significance.

**Bottom line:** Strong quality and momentum, weak on volatility and valuation — a high-conviction *directional* buy with a small *risk-adjusted* weight.

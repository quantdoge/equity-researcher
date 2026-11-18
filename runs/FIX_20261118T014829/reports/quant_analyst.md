# Quant Analyst

- Symbol: FIX
- Elapsed: 30.0s

---
# FIX — Comfort Systems USA, Inc.
**Industrials / Engineering & Construction · Mkt cap $38.5B · Price $1,099.02 · Beta (5y monthly) 1.643**

---

## 1. Factor Scores Table

Peer set = mechanical/electrical contracting comparables **EME, PWR, IESC** (n=4). Note: `get_sector_peers` returned broad Industrials megacaps (GE, CAT, RTX, UNP) which are not valid comparables for an MEP contractor; ranks below use the hand-selected E&C set.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 25 / 100 | **3 of 4** | Negative (expensive) |
| **Momentum** | 30 / 100 | **3 of 4** | Negative |
| **Quality** | 90 / 100 | **1 of 4** | Strongly positive |
| **Low Vol** | 25 / 100 | **3 of 4** | Negative |
| **Earnings Revision** | ~55 / 100 | n/a — **invalid, see flag** | Unconfirmed |

**Value detail** — FIX is the second-most expensive name in the quality cohort:

| | P/E | EV/EBITDA | P/FCF | ROE | GP/Assets | Accruals | 12-1 Mom |
|---|---|---|---|---|---|---|---|
| **FIX** | 38.05 | **26.58** | 37.73 | **41.76%** | 0.341 | −0.0254 | −16.5% |
| EME | 22.92 | 16.13 | 24.48 | 34.63% | 0.353 | −0.0031 | −13.2% |
| PWR | 88.02 | 37.48 | 56.01 | 11.39% | 0.148 | −0.0482 | −9.8% |
| IESC | 22.42 | 15.20 | 31.05 | 34.46% | 0.539 | +0.0125 | −35.7% |

**Quality detail** — ROIC has compounded upward four straight years: 18.27% → 27.26% → 37.22% → **44.77%**; ROE 24.6% → 41.8%. Piotroski **F-Score 8/9** (only miss: asset turnover improvement). Accruals negative all four years (−0.025 / −0.069 / −0.096 / −0.021) — earnings are cash-backed, not accounting-driven. Operating CF $1.186B vs net income $1.023B.

---

## 2. Price Statistics (252-day window, daily data)

| Metric | Value |
|---|---|
| Annualised return | **−8.99%** |
| Annualised volatility | **63.43%** |
| Beta vs SPY (1y daily) | **2.449** (R² 0.312) |
| Alpha vs SPY (annualised) | **−21.70%** |
| Sharpe (rf=0%) | **−0.141** |
| Sortino (rf=0%) | **−0.196** |
| Max drawdown | **−53.28%** |

Cross-check: profile 5y-monthly beta is **1.643** vs 1y-daily **2.449**. The gap indicates beta has *risen* materially — recent sensitivity is far above the long-run figure. Use ~2.4 for near-term risk budgeting.

**Statistical significance — the headline finding:** R² is only 0.312, so residual vol = 63.9% × √(1−0.312) = **53.1%**. Standard error on annualised alpha ≈ 53.1%, giving **t ≈ −0.41**. The −21.7% alpha and −0.141 Sharpe are **statistically indistinguishable from zero** at any conventional level on a 252-day sample. Do not present the negative alpha as an established result — only the beta (t ≈ 11) is robustly estimated.

---

## 3. Composite Quant Signal: **NEUTRAL**

Forced ranking: top-quartile quality and F-Score 8 collide with expensive trailing multiples, broken momentum, and a −53% drawdown. Quality is real and durable; the *price* is the problem, and the tape is de-rating the whole group.

**The one number that challenges the "expensive" verdict:** trailing P/E 38x is misleading on a company growing EPS ~94% in FY2026 (consensus $50.93 vs $26.27 FY2025), +31% in FY2027 ($66.91), +20% in FY2028 ($80.49). Forward multiples are **21.6x / 16.4x / 13.7x**. At EME's 22.9x on FY2027 EPS, FIX is worth ~$1,533. The value rank reflects earnings that have outrun the trailing denominator, not structural overvaluation.

---

## 4. Key Quant Risk Flags

1. **⚠️ Revision signal is a tool artifact — do not use it.** `calculate_earnings_revision_score` compared the FY2028 consensus ($80.49, 7 analysts) against the *FY2027* consensus ($66.91, 10 analysts) and labelled the +20.3% gap a "revision." That is **calendar growth, not estimate revision**. No genuine revision data is obtainable from this feed.
2. **Revision direction is actually negative by other evidence.** All six recent notes *lowered* targets into a falling tape (KeyBanc $2,125→$1,979; Goldman $2,159→$1,875; Stifel→$1,808; UBS→$1,900). One note explicitly reads "2027 Estimates Raised" — a split picture, not the clean upgrade the factor score implies. Median target $1,887.50 (+71.7% vs spot) is a stale, downward-trajectory anchor.
3. **Momentum reversal / sector-wide de-rating.** FIX −16.5% but every peer is also negative (EME −13.2%, PWR −9.8%, IESC −35.7%). This is a **factor-level, not idiosyncratic, drawdown** — stock-specific fundamental analysis will not resolve it. FIX ranks 3/4 on momentum, so it is *lagging* its own shrinking group.
4. **Factor crowding in high-beta MEP/data-center capex.** Beta 2.449, vol 63.4%, beta jumped from 1.64 → 2.45. IESC carries beta 2.548/vol 79.3% — this cohort trades as a single high-beta AI-capex proxy. Correlation risk is extreme; FIX offers little diversification against the peer set.
5. **Drawdown magnitude.** −53.3% peak-to-trough within the window implies a prior peak near ~$2,350 (from $1,099). Down 28.7% since the mid-Oct 2026 print of $1,541.68. Recovery to prior high requires +114%.
6. **Liquidity is not a concern** ($38.5B cap), but note that per-name daily-liquidity data was not retrieved.
7. **Sample-size limits:** 252 daily observations for alpha/beta/Sharpe (alpha and Sharpe insignificant, as above); 10-analyst, 3-year-forward consensus; FY2028 figures rest on **7 analysts**. The forward-multiple "cheapness" argument leans on estimates with genuinely thin coverage.

---

**Bottom line:** A genuinely high-quality business (F-Score 8, ROIC 44.8%, negative accruals, ROE #1 in group) trading at a trailing-multiple premium in a broken, high-beta momentum regime with unverifiable revision momentum. **Neutral** — quality passes every test, but the statistical evidence for a positive entry signal is absent (t-stat on alpha and Sharpe both <0.5 in absolute value), and the one factor flagged as bullish is a measurement error.

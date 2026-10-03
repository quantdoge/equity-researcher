# Quant Analyst

- Symbol: XOM
- Elapsed: 537.6s

---
I now have all the required inputs. The rank tool proved unusable (schema contradiction), so I constructed sector ranks directly from the peer factor scores I pulled. Compiling the final quant report.

---

# XOM — Exxon Mobil Corporation — Quantitative Factor Report

**Universe context:** US-listed mega-cap integrated energy. Sector peer set for ranking: CVX, SHEL, TTE, COP, BP, MPC (largest Energy names). Price at analysis: **$160.59** | Mkt cap ≈ **$691B** | Div yield **2.57%**.

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank (of 8) | Signal |
|--------|-------|---------------------|--------|
| **Value** | P/E 24.0, EV/EBITDA 10.7, P/FCF 29.3, P/B 2.59 | **7/8** | **Bearish** |
| **Momentum** | 12-1M return **+11.0%** | **5/8** | **Neutral** |
| **Quality** | ROE 10.8%, GP/Assets 0.156, Accruals −0.052, Piotroski **3/9** | **5/8** | **Weak** |
| **Low Vol** | Vol 28.1% ann., Max DD −20.1% | **6/8** | **Neutral** |
| **Earnings Revision** | Consensus FY30 EPS +**8.4%** (11.88 vs 10.97) | **3/8** | **Bullish** |

**Value (bottom decile of sector).** XOM trades at 24.0x trailing P/E and **29.3x P/FCF** — the most expensive in the peer set on cash-flow yield. European peers are dramatically cheaper: SHEL 6.3x EV/EBITDA & 11.9x P/FCF, TTE 6.0x/18.6x, COP 6.9x/9.5x. Only CVX and MPC are near XOM's P/E. The 2.57% yield partially offsets, but this is not a value stock today.

**Momentum (positive but mid-pack).** +11.0% 12-1M return vs MPC +45.5%, COP +17.1%, CVX +11.9%, SHEL +11.2%. Positive, but XOM has lagged the sector leaders — this is sector beta, not idiosyncratic momentum.

**Quality (deteriorating trend).** ROE has **halved** from 27.5% (2022) → 16.9% → 12.5% → **10.8% (2025)**; ROIC similarly 26.3% → 10.9%. Piotroski F-Score is **3/9 (weak)**: failed on ROA improvement, leverage, equity growth, dilution, margins, and asset turnover. The one genuine positive: accruals are persistently negative (−0.05 avg), i.e., earnings are cash-backed and conservative.

**Low Vol (unfavorable + unreliable beta).** 28.1% annualized vol is higher than CVX (25.4%) and typical integrateds. Beta vs SPY of **−0.78 is a data artifact** — R² = 0.13, statistically meaningless; company-reported beta is 0.18. Treat market sensitivity as unestimated, not negative.

**Earnings Revision (bullish but broad).** +8.4% upgrade to FY30 consensus, in line with a sector-wide upcycle: COP +9.6%, CVX +7.3%, SHEL +7.2%. Positive confirmation, not XOM-specific alpha. *Caution: FY30 consensus rests on only 4 analysts; FY29 on just 2 — modest statistical significance.*

---

## 2. Price Statistics (trailing 252 trading days, vs SPY)

| Metric | Value | Interpretation |
|--------|-------|----------------|
| Annualized return | **+45.6%** | Strong absolute run |
| **Alpha** (ann.) | **+63.2%** | Elevated but **unreliable** (R² = 0.13) |
| **Beta** | **−0.79** | Artifact; R² 13% → not meaningful (see flag) |
| **Sharpe** | **1.61** | Excellent risk-adjusted (0% RF assumption) |
| **Sortino** | **2.45** | Strong downside-risk-adjusted |
| Max drawdown | **−20.1%** | Material tail risk for a "defensive" energy name |
| Annualized vol | 28.1–28.4% | Above historical norm |

---

## 3. Composite Quant Signal: **NEUTRAL (Hold)**

Weights: value 25% (bearish), momentum 20% (neutral), quality 20% (weak), low-vol 10% (neutral), revisions 25% (bullish). The score clears to a **Neutral** with a modest positive tilt:

- **Bull case:** +8.4% estimate revisions with cash-backed earnings, 1.6 Sharpe, 2.45 Sortino, buy-side targets clustering **$172–185** (HSBC $172, Morgan Stanley $177, Piper $185) vs. $160 price, and cheap sector peers making the group a takeout/relative-value beneficiary.
- **Bear case:** XOM is the **most expensive** integrated on FCF yield while its quality metrics are the **weakest in years** (F-score 3/9, ROIC halved). After a +46% year, valuation is paying for a commodity upcycle that is already in consensus estimates.

Net: the estimate-revision tailwind and strong risk-adjusted returns keep us from a Sell, but stretched valuation and quality deterioration block a Buy. **Hold / Neutral.**

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk:** +45.6% trailing return, Sharpe 1.6, and a −20% drawdown profile = extended positioning. XOM's 12-1M momentum (+11%) is below sector leaders, so a commodity pullback hits it with no relative-momentum cushion.
2. **Factor crowding / relative value trap:** the entire sector screens cheap, making XOM's premium (29x P/FCF vs SHEL/TTE ~12–19x) a *sector-relative* headwind — capital rotates toward the cheaper integrateds on any macro wobble.
3. **Beta/alpha not statistically identified:** R² of 0.13 means the −0.79 beta and +63% alpha from the regression are **not significant** (sample effectively one idiosyncratic energy year). Do not extrapolate past outperformance into forward return assumptions.
4. **Estimate-revision sample size:** FY30 consensus from 4 analysts (FY29: 2) — the +8.4% revision is directionally valid but not a high-conviction signal.
5. **Quality deterioration is real, not cosmetic:** Piotroski 3/9 with simultaneous failures on profitability, leverage, and efficiency — the classic sign of peak-cycle margins normalizing.
6. **Liquidity: no concern.** $691B mega-cap, extremely liquid — no liquidity discount applies.

*Limitations: trailing-window stats (252d) capture one commodity cycle; factor ranks are computed against the 8 largest US-listed energy names rather than the full cross-section (rank_universe_by_factor tool was inoperable), so "sector rank" is approximate but directionally reliable.*

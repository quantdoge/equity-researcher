# Quant Analyst

- Symbol: LPLA
- Elapsed: 16.1s

---
## LPLA — Quantitative Factor & Risk Report

**Company:** LPL Financial Holdings · Financial Services / Capital Markets · Market cap ~$21.2B · Price $269.19 (2025-12-31 data)

> **Data caveat:** The `get_sector_peers` feed returned only passive index funds/ETFs (VITSX, VTI, VOO, BRK-A), not operating asset-manager comparables. **True cross-sectional sector ranking is unavailable.** Rankings below are therefore given as (a) intertemporal vs LPLA's own history and (b) rough absolute-band judgment, and are flagged accordingly. Sample: 252 trading days for price stats — adequate but single-year, so alpha/beta carry substantial estimation error.

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 24.7 · EV/EBITDA 12.6 · P/B 4.0 · **P/FCF −21.4** · Div yld 0.45% | n/a (expensive on abs. basis; top-quartile *cost*, i.e. bottom-quartile value) | **Negative** — FCF negative (operating CF −$423M in FY25), so no FCF cushion |
| **Momentum** | 12-1 return **−6.76%** | n/a | **Negative** — underperforming, but no violent reversal |
| **Quality** | ROE 16.2% · GP/Assets 0.235 · Accruals **0.0695 (high)** · ROIC 18.1% | n/a | **Negative** — "low" quality signal; ROIC/ROE in steep multi-year decline (ROE 51%→16% FY23–25) |
| **Low Vol** | Vol **40.7%** · Beta 0.75 (SPY) / 0.48 (profile) · Max DD 32.3% | n/a | **Weak** — beta modest, but *absolute* volatility is very high |
| **Earnings Revision** | Forward (FY29) EPS $42.16 vs $35.98 prior → **+17.2%** | n/a | **Positive — but low-reliability** (see flag) |

### 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|--------|-------|
| Annualised return | **−31.79%** |
| Annualised volatility | 41.1% |
| **Alpha (annualised)** | **−45.25%** |
| **Beta** | 0.75 |
| **R²** | **0.057** (only 5.7% of variance explained by market) |
| **Sharpe** | **−0.773** |
| **Sortino** | **−0.906** |
| Max drawdown | −32.3% |

**Interpretation:** A deeply negative Sharpe/Sortino and ‑45% alpha describe a stock that has destroyed risk-adjusted value over the past year. Critically, **R² of 0.057** means the alpha estimate is dominated by idiosyncratic moves — statistically fragile, one bad year can swing it. Beta ~0.75 is genuinely below-market, but that low beta has not protected on a *total-volatility* basis (41% vol).

### 3. Composite Quant Signal: **SELL**

Four of five factors are negative or weak (Value, Quality, Momentum, Low-Vol), and the sole positive — estimate revisions — rests on a **FY2029** consensus point that is effectively a long-horizon growth assumption, not a near-term revision trend. Quality is deteriorating materially (ROE 51→16%, ROIC 27→18%, F-score **3/9 "Weak"**, operating cash flow swung to **−$423M**, accruals rising 5.3%→7.0%). This is a deteriorating-fundamentals + negative-momentum profile. The low beta and positive long-dated EPS path are the only offsets.

### 4. Key Quant Risk Flags

- ⚠️ **Earnings-quality red flag:** FY25 operating cash flow **negative (−$423M)** while net income was +$863M → accruals ratio 0.0695 (>0.05 = lower earnings quality). P/FCF of −21.4 confirms cash conversion breakdown. Piotroski F2 (positive op CF) = 0.
- ⚠️ **Revision signal is long-dated and fragile:** The +17% "upgrade" is measured on the **FY2029** period — a single long-horizon estimate, not the standard 1-quarter/1-year revision trend. Do not overweight.
- ⚠️ **Momentum reversal risk is asymmetric:** already negative (−6.8%) with high vol — further downside beta to negative sentiment, minimal positive carry.
- ⚠️ **Factor-crowding / illiquidity:** none material — $21B cap, liquid large-cap; crowding not a concern.
- ⚠️ **Statistical reliability:** single 252-day window, R²=0.057 → alpha (−45%) and beta should be treated as low-confidence point estimates; multi-year confirmation needed.
- ⚠️ **Quality trend, not level, is the tell:** absolute ROE (16%) still respectable, but the *direction* (three straight years of decline) is the more predictive signal and it is firmly negative.

**Bottom line:** A quantitatively weak name — expensive-with-no-FCF, deteriorating quality, negative momentum, high vol — with one unreliable positive revision signal. **SELL**, pending any fundamental catalyst that reverses the cash-flow and ROIC deterioration.

# Quant Analyst

- Symbol: TSLA
- Elapsed: 49.7s

---
All data in hand. Compiling the quant report now.

---

# TSLA — Quantitative Factor Analysis
**Tesla, Inc. | Consumer Cyclical / Auto-Manufacturers | Mkt Cap ~$1.42T | Price ~$358**
*As of latest data (price targets through Oct 2026). All statistics on trailing 252 trading days unless noted.*

## 1. Factor Scores Table

| Factor | Raw Value | Universe Rank (n=25) | Signal |
|--------|-----------|----------------------|--------|
| Value | P/E 332.5x, EV/EBITDA 104.7x, P/FCF 203.7x, P/B 15.3x | **25/25 (last)** | **Strong Sell** |
| Momentum | 12-1m return **-10.4%** | 24/25 | **Sell** |
| Quality | ROE 4.6%, GP/Assets 0.124, Accruals -0.080 | 16/25 | **Sell** |
| Low Vol | Vol 44.9% ann., Beta 2.18 vs SPY | Bottom decile | **Strong Sell** |
| Earnings Revision | FY30 EPS est +45.8% (8.39 vs 5.76 prior) | n/a (8 analysts) | **Buy (thin sample)** |

**Cross-sectional context:** TSLA ranks dead last in the 25-name mega-cap universe on **value** (score -332.5 vs median ~-29) and near-last on **momentum** (-10.4% vs leader MSFT +28.7%). Quality sits in the bottom half. The only supportive signal is the estimate-revision upgrade, but it is a **2030-dated** consensus (+45.8% to $8.39) built on just **8 analysts** — statistically fragile and too far forward to anchor a buy.

## 2. Price Statistics (252d, benchmark SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualized) | **-48.8%** |
| Beta | **2.20** (R² = 0.40) |
| Sharpe | **-0.23** |
| Sortino | **-0.33** |
| Max Drawdown | -33.6% |
| Annualized Return / Vol | -10.5% / +45.5% |
| Peer correlation | AMZN 0.32, TM 0.25, HD 0.17, MCD -0.16 (low — idiosyncratic driver) |

The stock generated **-49% alpha** over the last year while carrying ~2.2x market sensitivity — negative return per unit of risk on both Sharpe and Sortino basis. Only 40% of return variance is explained by the market; the rest is Tesla-specific narrative volatility.

## 3. Composite Quant Signal: **STRONG SELL**

Four of five factors are negative (three in the bottom decile/quintile), and every price statistic is adverse (negative alpha, negative Sharpe/Sortino, 34% drawdown). Quality tells the most damning fundamental story: **ROIC collapsed from 26.4% (2022) → 12.2% (2023) → 8.1% (2024) → 4.8% (2025)**, with ROE at 4.6% (Piotroski F-score 5/9, moderate). The stock trades at 332x earnings for a business whose returns are half their 2023 level. The lone positive — the +45.8% far-forward EPS revision — does not offset four bottom-decile factor readings.

## 4. Key Quant Risk Flags

1. **Valuation disconnection / factor crowding risk:** near-zero FCF yield (P/FCF 203.7x) with no dividend — the single most expensive name in the mega-cap universe. Any de-rating is unbacked by fundamentals.
2. **Momentum reversal / squeeze risk:** after a -10.4% 12-1m return and -33.6% drawdown, TSLA is a high-short-interest, high-retail-participation name; a sharp snap-back is possible *against* the quant signal (this is a position-sizing caveat, not a thesis change).
3. **Extreme analyst dispersion:** recent targets span **$157 (HSBC) to $840 (Morgan Stanley bull case)** with price ~$358. That range (~±50% of price) signals exceptional model disagreement — target-mean statistics are unreliable here.
4. **Low peer correlation + high beta:** at 2.2x beta with sub-0.35 sector correlations, the stock is a macro-beta amplifier plus an idiosyncratic event lottery (regulatory credits, China demand, robotaxi/Semi narratives).
5. **Small-sample caveats:** factor ranks are computed on a 25-name mega-cap cross-section (coarse); the revision signal rests on 8 analysts and a 2030 horizon; price statistics use 252 trading days. Direction is consistent across metrics, so the *conclusion* is robust even if the exact ranks are approximate.

**Bottom line:** On pure quant factors, TSLA screens as a Strong Sell — worst-in-universe valuation, negative momentum, deteriorating returns on capital, and -49% alpha — offset only by a fragile, far-dated earnings-revision upgrade. The numbers win: the story is compelling, the data is not.

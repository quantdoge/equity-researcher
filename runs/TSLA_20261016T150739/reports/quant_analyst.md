# Quant Analyst

- Symbol: TSLA
- Elapsed: 60.4s

---
All data collected. Writing the final report.

---

# TSLA — Quantitative Factor Analysis
**Tesla, Inc. | Consumer Cyclical / Auto Manufacturers | Price $360.5 | Mkt Cap $1.42T**

## 1. Factor Scores

| Factor | Score (raw) | Sector Rank* | Signal |
|--------|-------------|--------------|--------|
| Value | P/E 334.5×; EV/EBITDA 105.3×; P/FCF 204.9×; P/B 15.4× | **6 / 6** | **Strong Sell** |
| Momentum | 12-1 mo return **−10.4%** | 5 / 6 | **Sell** |
| Quality | ROE 4.6%; GP/Assets 0.124; Accruals **−0.080** | 5 / 6 | Neutral (mixed) |
| Low Vol | Ann. vol **44.9%**; beta **2.18** | **6 / 6** | **Strong Sell** |
| Earnings Revision | FY2030 EPS est. +45.8% (5.76 → 8.39) | 1 / 6 (caveat below) | **Buy** (low reliability) |

*Rank vs peer set sampled from Consumer Cyclical (TM, AMZN, HD, BABA, MCD); 1 = best.

**Detail vs. peers:** TSLA is the most expensive name by a wide margin (peer median P/E ≈ 21×; TM 4.0× EV/EBITDA, AMZN 16.9×, HD 14.9×). Its gross-profit-to-assets (0.12) is the lowest in the set (HD 0.52, AMZN 0.44), and its volatility/beta are the highest. Piotroski F-Score = **5/9** (moderate): positive accruals quality and profitability, but deteriorating leverage, dilution, and asset-turnover components.

## 2. Price Statistics (252-day window vs SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualised) | **−48.5%** |
| Beta | **2.19** (R² = 0.40; profile beta 1.92) |
| Annualised return / vol | −10.2% / 45.5% |
| Sharpe | **−0.22** |
| Sortino | **−0.32** |
| Max drawdown | **−33.6%** |

Market explains only ~40% of TSLA variance (R² 0.40) — idiosyncratic, event-driven risk dominates (deliveries, margins, robotaxi/Semi news flow).

## 3. Composite Quant Signal: **SELL**

Four of five factors are negative-to-weak, and the two strongest factors (momentum, low-vol) are outright adverse. Tesla fails the top-quintile test on value/momentum/quality simultaneously — it is bottom-quintile or near it on every priced factor. The lone bullish signal (EPS revisions +45.8%) is long-dated and thin (see flags) and cannot offset a 105× EV/EBITDA entry with −48% alpha.

## 4. Key Quant Risk Flags

- **Valuation / factor crowding risk:** 334× trailing P/E and 105× EV/EBITDA with 4.6% ROE means any growth disappointment compresses multiples violently; beta of ~2.2 compounds it. This is the most crowded long in the AI/EV complex — unwinds are disorderly.
- **Momentum reversal risk:** 12-1 momentum is negative (−10.4%) *after* a 33.6% drawdown; with 45% annualised vol, a relief rally can be sharp, but trend followers are net short — don't fight the tape on the long side.
- **Analyst target dispersion / small-sample flags:** FY2030 revision signal is based on **8 analysts only** — statistically fragile. Live targets span **$157 (HSBC) to $840 (MS bull)** around a $360 price; consensus is effectively uninformative. Alpha/R² caveat: 252d sample, single benchmark.
- **Liquidity:** ample (mega-cap) — no liquidity flag; however, high short interest + options skew make gap risk material on earnings.
- **Quality nuance:** accruals ratio −0.080 (conservative accounting, good) partially offsets weak ROE — earnings quality itself is not the problem; the price paid for it is.

*Data through ~Oct 2026; peer ranks based on a 6-name sample, not the full sector — treat ranks as indicative.*

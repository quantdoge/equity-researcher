# Quant Analyst

- Symbol: SITM
- Elapsed: 55.6s

---
# SITM — SiTime Corporation | Quantitative Factor Report

**Sector:** Technology / Semiconductors · **Mkt Cap:** ~$12.5B · **Price:** $416.92 · **Data as of:** 2026-11-06

> **Data caveat (read first):** Two limitations temper the scores below. (1) The `get_sector_peers` universe returned only the 10 largest global tech names (AAPL, NVDA, MSFT, TSM, AVGO…). There is **no true comparable peer set** (mid-cap analog/mixed-signal/timing names) available, so "Sector Rank" figures are *estimated* percentile positions vs the broad semiconductor group, not computed cross-sectional ranks — treat as directional. (2) SITM is GAAP loss-making (2025 EPS −$1.72), so P/E, EV/EBITDA and P/FCF are economically meaningless (division by negative earnings). 252-day regression rests on ~250 daily obs (adequate), but **R² = 0.22 means the beta is imprecisely estimated and most variance is idiosyncratic.**

## 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank (est.) | Signal |
|--------|:---:|:---:|--------|
| **Value** | 5 | Bottom ~5th pct | **Strong Sell** — P/B 9.0, P/FCF 300x, negative P/E (−242) & EV/EBITDA; no earnings support |
| **Momentum** | 42 | ~45th pct (12-1), collapsing | **Neutral / deteriorating** — 12-1 = **+16.0%** positive, but last ~3 months **−45%** |
| **Quality** | 25 | Bottom ~25th pct | **Sell** — ROE −3.7%, ROIC −5.2%, GP/assets 0.135; *offset:* accruals −0.10 (clean), Piotroski F=7 |
| **Low Vol** | 4 | Bottom ~4th pct | **Strong Sell** — vol **94.3%**, beta **3.1**, max DD **60.6%** |
| **Earnings Revision** | 78 | Top ~20th pct | **Buy** — FY2028 EPS est revised **+22.8%** (16.42→20.17) over 3M |

**Quality detail:** Piotroski F-Score = **7** ("Moderate"; 4/4 profitability-adjusted blocks fail on the basic ROA test but cash-flow, accruals, leverage and margin-improvement tests pass). ROIC trend improving: −16.3% (2024) → −5.2% (2025) → still negative.

## 2. Price Statistics (252-day window, benchmark SPY)

| Metric | Value |
|---|---|
| Annualised return | **+41.8%** |
| **Alpha (annualised)** | **+29.9%** |
| **Beta (vs SPY)** | **3.13** (R² 0.22) — profile beta 2.91 |
| Annualised volatility | **93.2%** |
| **Sharpe ratio** | **0.45** |
| **Sortino ratio** | **0.82** |
| Max drawdown (252d) | **−60.6%** |
| **Recent drawdown** | Peak $753 (Jun 22) → $355 (Nov 5) = **−52.9%**; −44.6% from peak to current $416.92 |

**Interpretation:** The headline alpha (+29.9%) and Sharpe (0.45) are driven entirely by a first-half-2026 melt-up that has since fully reversed. Sortino (0.82) > Sharpe (0.45) confirms returns are lumpy and downside-heavy. A 3.1 beta with R² of only 0.22 is a **dangerous combination** — high sensitivity to market *direction* plus ~78% idiosyncratic variance. Correlations are modest (SPY 0.47, AMD 0.54, NVDA 0.46, MU 0.48, TXN 0.49): this is a stock-specific risk, not a clean sector proxy.

## 3. Composite Quant Signal: **NEUTRAL (bearish lean) — speculative, not factor-supported**

The classic factor profile is uniformly weak: **bottom-quintile Value, bottom-quintile Low-Vol, low Quality, fading Momentum.** The only genuine support is **Earnings Revision momentum (+22.8% forward upgrade)** and a fresh Seaport upgrade to Buy ($425 target, 11/6). That is a *narrative/growth* thesis, not a quantitative one — the model does not reward paying 300× FCF and 9× book for negative current earnings. **Net: Neutral, with the balance of factor evidence pointing Sell.**

**Analyst context (low confidence):** Forward estimates imply explosive growth — revenue $327M (2025) → $893M (2026E) → $1.74B (2028E); EPS $2.84 → $20.17. Price targets of $730–$900 were set at $543–$783 and are **now stale** (price $417); only the 11/6 Seaport $425 is current. 2028 EPS dispersion is **very wide ($16.31–$30.35, just 4 analysts)** — high model uncertainty; do not over-weight the revision score.

## 4. Key Quant Risk Flags

- **⚑ Momentum reversal risk (HIGH):** 12-1 momentum of +16% is *backward-looking and stale*. The trailing 1-month return is **−41%** and 3-month **−45%**. Classic "positive 12-1, collapsing recent" — a textbook reversal/short-continuation setup. The +16% masks a violent downtrend.
- **⚑ Extreme volatility / drawdown (HIGH):** 94% annualised vol, 60% 252-day max DD, 3.1 beta. A market−10% day implies roughly −30% here. Position sizing must reflect this.
- **⚑ Factor-profile crowding is *inverse*:** This is a crowded *growth/momentum-melt-up* trade that is unwinding. No value or quality floor beneath it.
- **⚑ Estimate-quality risk (MEDIUM):** Revision score rests on 4 analysts with a $16–$30 2028 EPS spread. GAAP still loss-making (−$1.72 in 2025) vs the +$2.84 adjusted "estimate" — the gap between GAAP reality and non-GAAP consensus is large.
- **⚑ Valuation with no earnings anchor:** Negative EBITDA/P/E make every multiple undefined; downside has no valuation support if growth estimates slip.
- **Liquidity:** Adequate but uneven — base ~$200M/day, spiking to ~$1.2B on events (11/5 traded 3.0M shares). Fine for most mandates, but execution slippage near catalysts.
- **Data gap:** No true peer multiple comparison; sector-rank percentiles are model-estimated, not computed. Confirm with a proper mid-cap semi peer set before relying on relative-value conclusions.

**Bottom line:** Statistically, SITM is a high-beta, high-vol, unprofitable, richly-priced idiosyncratic story whose only positive factor is forward estimate revisions. The quantitative evidence supports **Neutral with a defensive/sell bias** — size for 90%+ volatility and a demonstrated 50%+ drawdown profile.

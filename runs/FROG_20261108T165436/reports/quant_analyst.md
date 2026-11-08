# Quant Analyst

- Symbol: FROG
- Elapsed: 33.7s

---
# FROG (JFrog Ltd.) — Quantitative Factor Report

**Price $100.98 | Mkt cap $12.23B | Technology / Software–Application | 252-day window (~1yr daily data)**

---

## 1. Factor Scores Table

Peer group = bespoke DevOps/application-software set (n=9): DDOG, TEAM, S, ESTC, GTLB, MDB, SNOW, ZS. *(Note: `get_sector_peers` returns mega-cap Technology — AAPL/NVDA/MSFT — which are invalid comparables for a $12B loss-making software name; I built a hand-matched peer set instead.)*

| Factor | Score (0–100) | Sector Rank | Signal |
|--------|---------------|-------------|--------|
| **Value** | 18 | **8 / 9** | **Negative** — P/FCF 82.5x (7th cheapest of 9), P/B 13.2x, P/E −162.9 and EV/EBITDA −266x (GAAP loss-making ⇒ multiples undefined) |
| **Momentum (12-1)** | 50 | **6 / 9** | **Neutral** — +30.4% absolute, but *lags* peer median (+47.8%) by 17.4pp |
| **Quality** | 34 | **7 / 9** | **Negative** — ROE −8.1%, GP/Assets 0.304 (2nd worst), ROIC −9.9%; offset by good accruals (−0.162) |
| **Low Vol** | 8 | **9 / 9** | **Strong Negative** — 87.9% ann. vol (highest in group), β 1.667 (2nd highest), 37.4% max DD |
| **Earnings Revision** | 65 | **2 / 6** | **Positive but LOW CONFIDENCE** — +25.1% (see caveat) |

**Peer factor detail (FROG vs group):**

| Metric | FROG | Peer median | Peer best | FROG rank |
|---|---|---|---|---|
| 12-1 Momentum | +30.4% | +47.8% | TEAM +110.8% | 6/9 |
| P/FCF | 82.5x | 50.8x | ESTC 28.7x | 7/9 |
| ROE | −8.1% | −5.2% | ESTC +28.8% | 7/9 |
| GP/Assets | 0.304 | 0.412 | TEAM 0.914 | 8/9 |
| Accruals ratio | −0.162 | −0.168 | SNOW −0.280 | 5/9 |
| Ann. vol | 87.9% | 74.5% | S 58.1% | 9/9 |
| Beta vs SPY | 1.667 | 1.31 | TEAM 0.76 | 8/9 |
| EPS revision | +25.1% | +16.9% | SNOW +28.2% | 2/6 |

**Quality cross-checks:** Piotroski F-Score = **5/9 (Moderate)**. Component failures: negative ROA (F1), rising leverage (F5), share dilution (F7), no gross-margin improvement (F8). Positives: positive operating CF, ROA improvement, clean accruals, asset-turnover improvement.

---

## 2. Price Statistics

| Statistic | Value |
|---|---|
| Beta vs SPY (252d OLS) | **1.676** (company-reported 5y β: 1.306) |
| Alpha, annualised | **+100.3%** |
| R² vs SPY | **0.073** |
| Annualised return | +128.46% |
| Annualised volatility | 88.03% |
| **Sharpe ratio** | **1.459** |
| **Sortino ratio** | **2.341** |
| Max drawdown (252d) | **−37.41%** |
| Correlation vs SPY | 0.269 |
| Correlation vs GTLB / DDOG / SNOW / TEAM | 0.489 / 0.473 / 0.387 / 0.277 |

**Critical statistical caveat:** R² of **0.073** means the market factor explains only 7% of FROG's variance — 93% is idiosyncratic. Residual vol = 88.03% × √(1−0.073) ≈ **84.8%**. With only ~1 year of data, standard error of alpha ≈ 84.8%/√1 ≈ **84.8pp**, giving **t(alpha) ≈ 1.18 — NOT statistically significant**. The +100% alpha is statistically indistinguishable from noise. Likewise Sharpe t-stat ≈ 1.46 for a 1-year window falls short of the ~2.0 significance threshold. **Do not treat these as established risk-adjusted outperformance.**

---

## 3. Composite Quant Signal: **NEUTRAL**

Weights (Value 15%, Momentum 30%, Quality 20%, Low Vol 10%, Revisions 25%):

`0.15(18) + 0.30(50) + 0.20(34) + 0.10(8) + 0.25(65) = 42.3 → NEUTRAL`

The book is split cleanly: a **positive momentum + revision** leg versus a **deeply negative value + quality + vol** leg. FROG is a high-beta, expensive, GAAP-loss-making growth asset that is *rising but underperforming its own peer group* — not a factor-aligned long.

**Analyst PT overlay (supportive, secondary):** 10 recent PTs (Guggenheim $125, Oppenheimer $125, UBS $125, RBC $118, RJ $120, DA Davidson $115, Truist $110, Stifel $102) → mean ≈ **$117.5, +16.4% vs spot**. Every PT revision in the series was *raised*, none cut.

---

## 4. Key Quant Risk Flags

1. **⚠️ SEVERE SHORT-TERM REVERSAL RISK (highest-priority flag).** 1-year return +128.5% but 12-1 momentum only +30.4% ⇒ the **trailing 21 trading days contributed ≈ +75%**. Price ran from ~$74.6 to ~$101 within the PT-revision window. This is the textbook setup for short-term mean reversion, and it inflates both the Sharpe and the alpha computation. The 12-1 momentum figure is the *honest* signal and it is merely mediocre.

2. **Factor crowding / dispersion.** Correlation with DDOG 0.47, GTLB 0.49 — FROG trades as part of the high-multiple DevOps complex, not on idiosyncratic merit. Peer group spans 12-1 momentum from +9.2% (DDOG) to +110.8% (TEAM) — extreme dispersion means cross-sectional ranks are unstable and will rotate fast.

3. **Volatility is worst-in-class.** 87.9% ann. vol and β 1.67 make FROG the riskiest name in a group that is already risk-heavy. Position sizing at equal weight would materially over-risk the book — vol-scaling implies roughly a **0.55× notional haircut** vs the peer average.

4. **Earnings-revision signal is methodologically weak.** The +25.13% is measured on **FY2028**, carries only **3 analysts**, and the range is $0.50–$2.05 (±54% around the mean). The apparent "upgrade" reflects the rolling forward-period shift (2027 $1.146 → 2028 $1.434) as much as genuine estimate hikes. **Treat as low-confidence; do not size on it.** (The TEAM −100% revision is a degenerate data artifact — zero estimate — and should be excluded, not read as a downgrade.)

5. **Quality is optically misjudged by accruals alone.** Accruals −0.162 (5/9, clean) makes FROG look better than it is: operating CF of +$146M against net income of −$72M is SBC-driven, not cash-generation strength. Negative ROE (−8.1%), negative ROIC (−9.9%), and 8/9 GP/Assets are the more reliable quality reads.

6. **Valuation offers no downside support.** P/FCF 82.5x, P/B 13.2x, EV/EBITDA −266x. There is no valuation floor — the entire investment case rests on the growth trajectory holding, which is precisely the leg with the weakest statistical support in this dataset.

**Sample-size disclosure:** factor ranks rest on n=9 cross-section and ~252 daily observations (1 year). Quintile-level significance is **not** achievable; ranks should be read as descriptive, not inferential. Alpha/beta/Sharpe/Sortino are single-window estimates and are not shown to be statistically robust.

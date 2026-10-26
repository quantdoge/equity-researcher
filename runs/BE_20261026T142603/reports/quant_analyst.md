# Quant Analyst

- Symbol: BE
- Elapsed: 31.6s

---
## Bloom Energy (BE) — Quantitative Factor & Risk Analytics

**Company:** Bloom Energy Corp · Industrials / Electrical Equipment & Parts · San Jose, CA · Price **~$200.41**, mkt cap **~$48.7–59.2B** *(discrepancy: valuation model uses 240.4M diluted shares → $48.7B; profile reports $59.2B on a different share count — I use $48.7B as the audited figure)*

### 1. Factor Scores Table

| Factor | Score | Sector Rank (1=best) | Signal |
|--------|-------|----------------------|--------|
| **Value** | P/E n.m. (−547.9), P/B 61.4x, EV/EBITDA 2,457x, P/FCF 852x | **4 of 4** (worst) | **Strong Sell** |
| **Momentum** | +22.29% (12-1m); 12m total return +98.5% | **1 of 4** (best) | **Buy** |
| **Quality** | ROE −11.15%, GP/Assets 0.134, accruals −0.046, F-Score **4/9** (Weak), ROIC 1.92% | **3 of 4** | **Sell** |
| **Low Vol** | 110.2% ann. vol, β 4.23, max DD 52.7% | **4 of 4** (worst) | **Strong Sell** |
| **Earnings Revision** | +17.87% (low-confidence — see flag) | 2 of 4 | **Buy (qualified)** |

**Peer set** (genuine comps, not the mega-cap sector list): GEV, GNRC, PLUG.

| Metric | **BE** | GEV | GNRC | PLUG |
|---|---|---|---|---|
| EV/EBITDA | **2,457x** | 60x | 26x | n.m. |
| P/FCF | **852x** | 62x | 42x | n.m. |
| P/B | **61.4x** | 18.8x | 4.2x | 1.6x |
| ROE | **−11.2%** | 39.7% | — | — |
| Ann. vol | **110.2%** | 51.5% | 60.6% | 80.2% |
| Beta | **4.23** | 1.98 | 2.24 | 2.31 |
| 12-1m momentum | **+22.3%** | −10.2% | −4.5% | −14.3% |

### 2. Price Statistics (252 trading days, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+21.40%** — *statistically insignificant* |
| Beta | **4.254** |
| R² | **0.2524** (only 25% of variance is market-explained) |
| Annualised return | +98.49% |
| Annualised volatility | 111.04% |
| **Sharpe ratio** | **0.887** |
| **Sortino ratio** | **1.550** |
| Max drawdown | **−52.65%** |
| Downside deviation (derived) | 63.55% (Sortino/Sharpe = 1.75) |

**Derived risk decomposition:** residual (idiosyncratic) vol ≈ **96.0%**; systematic vol ≈ 55.8%. Alpha t-statistic ≈ **0.22** (±1σ standard error ≈ 96pp over a one-year sample) — **the +21.4% alpha is not distinguishable from zero.** The 98% return is overwhelmingly a 4.25x-beta exposure to a rising market plus 75% stock-specific variance, not demonstrated skill. The 0.887 Sharpe is a leveraged-market outcome.

### 3. Composite Quant Signal: **NEUTRAL**

A pure factor composite is unambiguous here: BE is **bottom-quintile on three of five factors** (Value, Low Vol, Quality) and top-quintile on only one (Momentum). The single genuine positive is far-dated EPS revision momentum. Two offsetting extremes → **Neutral**, with the character of a high-beta speculative growth position, not a factor-supported holding. **Not a Buy** — nothing in the value, quality or volatility data supports it. **Not a Sell** on momentum alone, given the sector-leading 12-1m return and the real fundamental inflection (revenue +37% to $2.02B, operating income positive at $72.8M vs $22.9M, OCF +$113.9M, ROIC improving −18.7% → 1.1% → 1.9% since 2022).

**Valuation cross-check:** trailing multiples are economically meaningless (EBITDA is only $20.5M against a $49B EV). On forward estimates the picture is less absurd: **2026E EV/EBITDA ≈ 44x** ($1.11B EBITDA), 2027E ≈ 27x — roughly GNRC's current 26x. But this requires *implied revenue to grow ~50% CAGR to $15.6B by 2030* and 2026E revenue +117%. The multiple is a bet on flawless execution of a five-year hockey stick.

### 4. Key Quant Risk Flags

1. **Beta 4.25 / R² 0.25 — extreme market sensitivity with 75% idiosyncratic risk.** A 10% SPY drawdown implies a ~42% BE drawdown on beta alone. Position sizing must treat this as ~4x market exposure.
2. **Alpha is not statistically significant (t ≈ 0.22, 1-year sample).** Do not attribute the +98% return to manager-relevant skill. Requires a 3–5 year window to test.
3. **Max drawdown −52.65% within the trailing year** while still returning +98% — the return path is violent. Sortino 1.55 vs Sharpe 0.887 shows returns are carried by a few large upside tail days; remove them and the profile deteriorates sharply.
4. **Earnings revision score is low-confidence.** The tool compared the **2030** consensus EPS ($12.82) against $10.88 — a mis-aligned prior period that is in fact the **2029** estimate. So the +17.87% is partly a *horizon mismatch*, not a clean 3-month revision. Additionally: only 13 analysts, and 2030E EPS dispersion is **$9.41–$15.95 (±25%)**. Treat revision momentum as directionally positive but statistically weak.
5. **Momentum reversal risk is elevated.** A 110%-vol name with beta 4.25 that has just run +98% is the classic setup for a sharp mean-reversion; the 12-1 measure excludes only the last 21 days. Crowding into the "data center power / fuel cell" theme is a real factor-crowding exposure.
6. **Quality is structurally thin:** F-Score 4/9, ROE negative in all four years, net income still −$88.4M on $53.9M of interest expense, and share count rising (227.4M → 240.4M, F7 dilution flag = 0). GAAP profitability remains elusive despite improving ROIC.
7. **Peer-set caveat:** the sanctioned Industrials peer list is dominated by mega-cap diversified industrials (CAT, GE, RTX, UNP, DE, BA, SPCX) with no fuel-cell analog. Sector ranks above use the economically comparable GEV/GNRC/PLUG set; a full 40-name Electrical Equipment screen would firm up the quintile placement.
8. **No dividend, no buyback support** (yield n.m.) — zero valuation floor from capital return.

# Quant Analyst

- Symbol: PANW
- Elapsed: 60.5s

---
## PANW — Quantitative Factor Report
**As of 2026-11-18 | Price $339.92 | Mkt cap ≈$278B | FY26 (Jul) annuals filed 2026-09-10**

### 1. Factor Scores

| Factor | Score / Raw Input | Sector Rank (cyber peer set) | Signal |
|---|---|---|---|
| **Value** | P/E **849.8x**; EV/EBITDA **186.3x**; P/FCF **63.1x**; P/B 9.45x | **4th / 5** (~25th pct) — cheaper only than CRWD (1278x EV/EBITDA) | **Strong negative** |
| **Momentum** | 12-1 = **+69.0%** (recomputed); 6-mo +37.3%; 3-mo **−9.1%** | n/a — peer momentum not retrievable | **Positive but decelerating** |
| **Quality** | ROE **1.12%**, ROA 0.63%, ROIC **2.32%**; GP/A **0.167**; accruals **−0.088** | **4th / 5** (~25th pct); engine label "low" | **Negative** |
| **Low Vol** | Ann. vol **56.0%**; beta 1.331; max DD 26.3% | **2nd / 3** measured (FTNT 53.8%/0.99; CRWD 62.0%/1.47) | **Negative** (high absolute vol) |
| **Earnings Revision** | Tool output invalid (see flag); realized EPS FY26 $0.40 vs FY25 $1.60 = **−75%**; **7 of 8** recent price targets *raised* (median ~$415, +22% upside) | n/a | **Mixed / Neutral-positive** |

Peer detail used for ranks: FTNT (P/E 54.5, EV/EBITDA 42.7, P/FCF 45.3, ROE 149.8%, GP/A 0.527, quality "high") · CHKP (16.0, 15.3, 14.4, ROE 36.7%, GP/A 0.303, "high") · CRWD (−, 1278, 181, ROE −3.6%, GP/A 0.324, "low") · ZS (−, 161, 37.2, ROE −2.4%, GP/A 0.327, "low").
*Caveat: 5-name peer set makes each rank worth 25 percentile points — ranks are directional, not statistically precise.*

### 2. Price Statistics (252d, SPY benchmark, 0% rf)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+96.6%** (arithmetic; see caveat) |
| Beta vs SPY | **1.338** (R² **0.118** — 88% idiosyncratic) |
| Ann. return / vol | 126.6% / 56.2% |
| **Sharpe** | **2.253** |
| **Sortino** | **3.934** |
| Max drawdown | **−26.3%** (peak-to-trough) |
| Current DD from 52-wk high ($419.91, 2026-10-06) | **−19.0%** |
| 52-wk range | $141.67 – $419.91 |
| 126d (recent) Sharpe / Sortino | **0.748 / 1.38** — sharp deterioration |

Correlations: CRWD **0.868**, FTNT 0.742, ZS 0.650, CHKP 0.412, SPY 0.342.

### 3. Composite Quant Signal: **NEUTRAL**
Only momentum supports the stock, and it is rolling over. Value and Quality both sit in the **bottom quintile** of the cyber group — 186x EV/EBITDA and 849x trailing P/E leave zero valuation cushion, and ROIC of 2.3% (vs 15.2% in FY25) means capital is not currently earning its cost. Piotroski F-score **5/9**. The genuine positive: cash generation is real — OCF $4.55B, accruals **−0.088** (negative accruals = earnings backed by cash), and sell-side targets were raised 7 of 8 times. That earns a Neutral rather than Sell, but there is no factor-based case for adding here.

### 4. Key Quant Risk Flags
1. **Momentum reversal — triggered, not hypothetical.** 3-month return −9.1%, −19% off the Oct high, and the 126-day Sharpe collapsed from 2.25 to **0.75** with vol *rising* to 62.6%. Classic deceleration pattern.
2. **Valuation compression risk.** 63x P/FCF vs FTNT 45x and CHKP 14x. Any growth disappointment re-rates hard; beta 1.34 with only 12% R² means a wide, unpriced tracking-error band.
3. **Earnings quality / dilution.** Revenue +24.5% but net income −73%; D&A jumped to $855M from $343M and diluted shares +7.7% (765M vs 709M) — large acquisition integration. Gross margin fell ~300bp to 70.4%. F-score loses points on ROA trend, dilution, margin and turnover.
4. **Factor crowding.** 0.868 correlation with CRWD — PANW offers little diversification within a cyber basket; a growth-momentum unwind hits both.
5. **Liquidity:** not a constraint — ADV ~5–20M shares, mega-cap. No liquidity flag.

### Data Integrity Notes (material — read before using these numbers)
- **Momentum tool is inconsistent with the raw OHLCV series.** The tool reports −9.52% (12-1) and −7.56% (−14.63% on 63d), but the price file shows $205.25 (2025-11-14) → $346.95 (2026-10-19), i.e. **+69.0%**. I report the raw-price recomputation as primary; the sign convention of the tool output does not reconcile to the underlying series and should not be relied on.
- **Earnings revision score is unusable.** It returned forward period 2031-07-31 with current EPS 0.0 vs prior 6.22 (−100%) — a long-dated row with no live data. `get_analyst_estimates` also failed (not on subscription plan). Revision signal above is proxied from price targets and realized EPS.
- **Alpha/Sharpe are flattered by methodology.** Arithmetic annualisation of a 56%-vol series yields a 126.6% "return" vs a ~65.6% geometric realized 12-month return. On a geometric, ~4% rf basis, Sharpe ≈ **1.10** and Sortino ≈ **1.9–2.0** — still respectable, roughly half the headline.
- Sample: 252 daily observations — sufficient for vol/beta. R² 0.118 means the alpha estimate carries a very wide standard error; treat +96.6% alpha as noise-dominated.

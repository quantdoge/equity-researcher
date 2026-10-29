# Quant Analyst

- Symbol: GOOG
- Elapsed: 128.0s

---
# Alphabet Inc. (GOOG) — Quantitative Factor Report
*Data as of 2026-10-21 close ($330.95). Ratio tool reference price $321.89. Market cap ≈ $3.94T.*

## 1. Factor Scores Table

Peer set: META, NFLX, SPOT, DIS, VZ, TMUS (Communication Services; n=6 comparables — **small sample, ranks are ordinal not statistically robust**).

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 29.8 · P/B 9.5 · EV/EBITDA 21.4 · **P/FCF 53.7** · Div yield 0.27% | **6 / 7** (14th pctile) | **Bearish — most expensive cash-flow multiple in peer group** |
| **Momentum** | −1.51% (12-1) | **6 / 7** (14th pctile) | **Bearish — only TMUS (−14.0%) worse** |
| **Quality** | ROE 31.8% · GP/Assets 0.404 · Accruals **−5.5%** · ROIC 27.2% · F-Score 6/9 | **3 / 7** (71st pctile) | **Bullish** |
| **Low Vol** | Vol 31.5% · Beta 1.351 · MDD 21.2% | **4 / 7** (~50th pctile) | Neutral by vol, **worst beta in peer set** |
| **Earnings Revision** | +19.1% (see caveat) | n/a — no peer data | **Strongly bullish, but metric is flawed** |

**Value — the weakest leg.** GOOG is the single most expensive name in its peer group on P/FCF (53.7x vs peer median ~28.3x) and second-most expensive on EV/EBITDA and P/E. Only VZ (9.3x FCF), TMUS (10.9x), DIS (19.6x) offer genuine value. Premium is not anomalous for the franchise, but there is no valuation cushion.

**Quality — the strongest leg.** Negative accruals (−5.5%, stable at −5.6%/−7.0%/−8.6% prior three years) mean earnings are fully cash-backed — no accrual quality flag. Gross-profit/assets of 0.404 is top-tier. Two cautions: **ROIC declined from 32.1% (2024) to 27.2% (2025)**, and the F-Score lost points on ROA improvement, leverage, and asset turnover (6/9, "Moderate" not "Strong").

**Revision caveat (important).** The tool compared the **FY2030** consensus ($25.90) against the **FY2029** consensus ($21.74) — that is a +19.1% *cross-period growth rate*, not a same-period 3-month revision. True revision momentum is unmeasured. Corroborating evidence is nonetheless positive: 8 of 10 recent sell-side actions were target **raises**, and revenue estimates build $500B (2026) → $625B (2027) → $758B (2028). Treat the +19.1% as directionally right, numerically untrustworthy.

## 2. Price Statistics

| Metric | 504-day (2yr) | 252-day (1yr) |
|---|---|---|
| Annualised return | **+49.7%** | ≈ +5% |
| Annualised volatility | 29.6% | 31.5% |
| Beta vs SPY | **1.284** | 1.351 |
| Alpha (annualised) | **+25.7%** | — |
| R² vs SPY | **0.275** | — |
| **Sharpe** | **1.681** | **0.16** |
| **Sortino** | **2.929** | — |
| Max drawdown | **−21.2%** | −21.2% |

**Statistical significance — read this before using the alpha.** Residual vol = 29.56% × √(1−0.275) = 25.2%. Standard error of the annualised alpha over 2 years = 25.2/√2 = **17.8%** → **t ≈ 1.44**. Sharpe SE ≈ 1.10 → **t ≈ 1.53**. **Neither the +25.7% alpha nor the 1.68 Sharpe is significant at 95%.** The point estimates flatter GOOG; do not underwrite them as proven skill.

**The 2-year/1-year divergence is the central fact.** Excellent two-year records (Sortino 2.93, alpha +25.7%) sit on top of a flat last twelve months (Sharpe 0.16, momentum −1.51%). Recent price action confirms: $372 (Aug 3) → $330.95 (Oct 21), **−11.1%**, breaking down through the $337–345 shelf that held for six weeks. The strong long-window statistics are almost entirely legacy of the 2025 run.

**Low market correlation.** SPY 0.556, QQQ 0.461, META 0.351, NFLX 0.174. Unusually low for a $3.9T mega-cap — real diversification value, and low factor crowding with mega-cap tech.

**Sell-side:** recent target median **$442.5** (range $350–$515) vs $330.95 = **+33.7% implied upside** — a strong bullish signal that is *inconsistent* with the negative price momentum. One dissenter (KeyBanc cut to $410 on "lower Google Services earnings") and D.A. Davidson at $350 on rising capex.

## 3. Composite Quant Signal: **NEUTRAL** (slight Buy tilt)

Weighted composite (Momentum 25%, Quality 25%, Value 20%, Revision 20%, Low Vol 10%) of percentile-mapped scores ≈ **−0.04 → neutral**.

This is a textbook **quality-growth-at-a-premium with broken momentum**: elite quality (+), credible earnings revision direction (+), expensive cash-flow valuation (−), negative and deteriorating price trend (−). The bullish factors are structural and slow-moving; the bearish factors are the ones currently driving the tape. The +33.7% consensus upside is a 12-month argument, not a 1-month one.

**Trigger for upgrade to Buy:** 12-1 momentum crossing above zero (price recovery through ~$360) with revisions confirmed on a true same-period basis.
**Trigger for downgrade to Sell:** loss of the $326 support / drawdown exceeding −25% from the ~$375 high.

## 4. Key Quant Risk Flags

1. **Momentum reversal / trend risk (highest severity).** 12-1 momentum −1.51%, 1-year Sharpe 0.16, and −11.1% over the last three months with a fresh breakdown on Oct 21 (heavy 19.3M volume, close near low). Every peer except TMUS is outperforming on 12-1.
2. **Valuation risk.** P/FCF 53.7x is the highest in the peer set. If FCF conversion disappoints, this multiple has the furthest to fall.
3. **Capital efficiency erosion.** ROIC 32.1% → 27.2%; F-Score fails leverage, asset turnover, and ROA-improvement tests. Consistent with the capex/AI-spend escalation that D.A. Davidson flagged as a target-cut driver.
4. **Alpha/Sharpe are not statistically significant** (t = 1.44 / 1.53 on 504 days). Insufficient sample to reject zero alpha. Any model treating GOOG's historical alpha as established is overfitting a two-year window.
5. **Highest beta in the peer group (1.351)** with rising 1-year beta vs 2-year (1.284) — market sensitivity is *increasing* into a weak momentum regime. Low R² (0.275) means 72% of variance is idiosyncratic: this is a **stock-specific bet**, not a market proxy.
6. **Peer sample too small for rigorous cross-sectional inference** (n=6). Sector ranks are indicative only. **Earnings-revision factor is period-mismatched** and should not be used quantitatively until re-pulled on a same-forward-period basis.

**Bottom line:** Quality and estimate direction make GOOG a defensible long-term hold; value, momentum, low-vol, and statistical significance all argue there is no urgency to add here. Neutral, size modestly, wait for the trend to turn.

# Quant Analyst

- Symbol: WSM
- Elapsed: 49.0s

---
## WSM (Williams-Sonoma) — Quantitative Factor Report
**Data as of 2026-11-20 close: $218.42 | Mkt cap $25.8–26.9bn | Sector: Consumer Cyclical / Specialty Retail**

---

### 1. Factor Scores

Sector rank = position within the tightest comparable set (WSM, HD, LOW, TJX), 1 = most attractive. **N=4, so these are ordinal ranks, not quintiles — treat sector-relative percentiles as indicative only.**

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 24.71 · EV/EBITDA 16.23 · P/FCF 25.49 · P/B 12.92 | **3 of 4** | **Neutral / slight negative** — trades at peer-median on EV/EBITDA, premium on P/E; only P/FCF (25.5x vs HD 27.1x, TJX 32.1x) screens well. P/B 12.9x leaves no asset cushion. |
| **Momentum** | 12-1 return **+4.45%** | **1 of 4** | **Positive but stale / invalidated.** Peers: HD −5.71%, LOW −8.38%, TJX −5.69%. WSM is the *only* positive absolute return in the group — but the metric excludes the last 21 days, and **WSM fell −15.2% on 2026-11-19**. Trailing 20-day return is **≈ −14%**. |
| **Quality** | ROE 52.3% · ROIC **40.0%** · GP/Assets **0.666** · Accruals **−0.042** | **1 of 4** (level basis) | **Positive, with a caveat.** Best gross-profit-to-assets in the group (HD 0.52, LOW 0.53, TJX 0.52), negative accruals (clean earnings). **But Piotroski F-Score = 4/9 ("Weak")** — see divergence flag below. |
| **Low Vol** | Ann. vol **38.51%** · Beta **1.27** · Max DD 21.2% | **4 of 4** (worst) | **Negative.** Beta/vol are ~1.9x TJX (25.9% vol, 0.30 beta) and ~1.9x HD's beta. Fails the low-vol screen outright. |
| **Earnings Revision** | +15.36% "revision" | n/a | **Positive, but the metric is contaminated — see caveat.** Independent check: **9 of 10** price-target actions Aug–Nov 2026 were raises; mean PT **$259.70** vs $218.42 = **+18.9%** implied upside. |

**⚠️ Revision-score data artifact:** the tool compared the FY**2031** EPS estimate ($15.02, 5 analysts) against the FY**2030** estimate ($13.02, 2 analysts). That is **cross-period growth, not a 3-month same-period revision**. Coverage is thin (2–5 estimates on the out-years). The +15.36% should not be read as revision momentum; the price-target tape ($190→247 UBS, $210→240 MS, $250→270 KeyBanc, $259→286 Piper, $240→255 Evercore, $230→250 Argus, $260→285 Telsey) is the more reliable revision evidence.

---

### 2. Price Statistics (252-day window, vs SPY)

| Metric | WSM | HD | LOW | TJX |
|---|---|---|---|---|
| Annualised return | **+19.19%** | −5.44% | −19.39% | −10.82% |
| Annualised vol | **38.51%** | 28.37% | 31.13% | 25.90% |
| **Sharpe** | **0.505** | −0.189 | −0.623 | −0.415 |
| **Sortino** | **0.689** | −0.392 | −1.209 | −0.687 |
| Beta vs SPY | **1.274** | 0.674 | 0.589 | 0.298 |
| Alpha (ann.) | **+5.15%** | — | — | — |
| R² vs SPY | **0.233** | — | — | — |
| Max drawdown | 21.2% | 26.5% | 36.9% | 26.8% |

- **Risk-adjusted performance is best-in-class** on a relative basis: WSM is the only comp with positive Sharpe/Sortino. Sortino (0.689) > Sharpe (0.505) confirms downside deviation is contained relative to total vol.
- **Alpha is not statistically significant.** R² of 0.233 means 77% of WSM's variance is idiosyncratic. Standard error of annualised alpha ≈ 38.0 × √(1−0.233) ≈ **33.3pp**, giving **t ≈ 0.15**. The +5.15% alpha is economically meaningless noise at this window length — do not build a thesis on it.
- **Max drawdown (21.2%) is the current, live drawdown** — the stock is at its 252-day low *momentum state*, having peaked at $274.45 (Nov 5) and closed at $218.42.
- Correlations: SPY 0.48, HD 0.62, LOW 0.60, TJX 0.36. WSM is more market-sensitive than its own comps (SPY corr 0.48 vs HD's 0.35) — it is **not** a defensive retail holding.

---

### 3. Composite Quant Signal: **NEUTRAL** (downgrade from Buy)

**Weighted factor score: +0.5** — Quality +1.5, Revision +1.5, Value 0.0, Momentum −0.5 (nominal +0.5, haircut for post-crash break), Low Vol −2.0.

The setup is genuinely split. On **fundamental/factor levels** WSM earns a Buy: top-quartile quality (40% ROIC, 0.67 GP/assets, negative accruals), positive revision breadth, and the only positive Sharpe in the peer set. On **price dynamics** it earns a Sell: highest beta and volatility, worst low-vol score, a 4.4x-volume −15.2% capitulation, and a Piotroski score of 4 that says the quality *trend* is deteriorating even as the *level* stays high. A 1-cent EPS miss producing a −15% move is a de-rating event, not noise.

**Resolution requires the post-Q3 estimate reset.** Until FY2027 ($9.50) and FY2028 ($10.45) consensus is reset, the revision signal is measuring 2031 dreams, not 2027 reality. On FY2028 EPS of $10.45 the stock trades **20.9x** — a full multiple with no margin of safety if the eight-quarter beat streak is genuinely over.

---

### 4. Key Quant Risk Flags

1. **Momentum signal is stale — reversal already realized.** The +4.45% 12-1 score *excludes* the −15.2% (Nov 19) gap. Do not screen WSM as a momentum winner; the 20-day return is ≈ −14%.
2. **Quality-level vs quality-trend divergence.** ROIC 40% and GP/assets 0.666 but **F-Score 4/9**: failing on ROA improvement, leverage, equity change, gross-margin improvement, and asset-turnover improvement. High levels on a deteriorating treadmill — classic value-trap signature.
3. **Worst low-vol characteristics in the peer group.** 38.5% vol, 1.27 beta, 1.9x the beta of HD/LOW. Crowding/rotation risk is high; the stock has already de-rated violently in a weak retail tape.
4. **Alpha statistically insignificant** (R² 0.23, t ≈ 0.15). Any "WSM generates alpha" claim is unsupported at 252 days.
5. **Fundamental staleness.** Value and quality scores use the FY ending **2026-02-01** — roughly 10 months stale, pre-dating the Q3 miss entirely. Recompute after the 10-K.
6. **Small-sample revision data.** 2–5 analysts on FY2030/31 lines; 10 price-target notes. Directionally fine, statistically thin.
7. **Valuation gives no cushion.** 24.7x trailing, 12.9x book, 20.9x FY2028E. Downside beta is asymmetric into any further guidance cut.

**Sample-size caveat:** with 4 peer names and 1 year of daily data, all cross-sectional ranks and risk-adjusted ratios carry wide error bands. Directional conclusions (high quality, high vol, positive revision tone) are robust; specific percentile placements are not.

**Peer gap noted:** no direct home-furnishings comparable (RH, ARHS, W, ETD) was available in the sector feed, so the peer set over-weights big-box home improvement and off-price — both structurally different business models. Value and quality ranks should be read with that structural mismatch in mind.

# Quant Analyst

- Symbol: TSCO
- Elapsed: 99.2s

---
## TSCO — Tractor Supply Company | Quantitative Factor Report
*Price $33.16 (16-Oct-2026) · Mkt cap $17.6B · EV $23.4B · Consumer Cyclical / Specialty Retail*

**Data note up front:** two of my inputs came from different data vintages. The momentum factor tool returned a window ending ~Feb-2026 (+7.69%), while the vol/alpha tools ran through the current price ($33.16). I recomputed momentum by hand off the OHLC series; both numbers are shown below. Per-share figures are on the provider's split-adjusted basis (532M diluted shares).

### 1. Factor Scores Table

| Factor | Score | Sector Rank (of 4)* | Signal |
|---|---|---|---|
| Value | **Strong.** P/E 16.1 · EV/EBITDA 11.9 · P/FCF 23.8 · FCF yield 4.2% · Div yield 2.86%. Cheapest on all three multiples vs HD/TJX/SBUX | **1 / 4** (top quartile) | **Buy** |
| Momentum | Raw tool: **+7.69%** (12-1, stale window) → **recomputed −39.1%** (53.87 → 32.82) | **1 / 4** stale → **4 / 4** current | **Strong Sell** |
| Quality | ROE 42.5% · ROA 10.0% · ROIC 17.2% · GP/Assets 0.472 · Accruals −4.9% (best of 4) · F-score 6/9 | **2 / 4** | **Hold** (decaying) |
| Low Vol | Ann. vol 35.4% (highest of 4) · β 0.437 but **R² = 0.026** · MDD 47.1% | **4 / 4** | **Sell** |
| Earnings Revision | Tool: **+9.23%** — but on **FY2030E** ($2.585 vs $2.367), **n = 3 analysts** | n.m. | **Neutral / weak** |

\*Peer set is only three names (HD, TJX, SBUX — TSCO's "Consumer Cyclical" peer list is dominated by AMZN/TSLA mega-caps and is not a usable comp group). Percentile ranks over n=4 are **directional only, not statistically meaningful.**

*Value detail:* P/B of 6.84 is not a red flag here — it reflects a 42% ROE and aggressive buybacks (shares 561M → 532M since 2022), not leverage.
*Quality detail:* **ROIC has fallen every year: 22.7% → 20.6% → 19.1% → 17.2% (2022–25).** F-score fails on ROA improvement, gross-margin improvement and asset-turnover improvement. This is a deteriorating quality factor, not a stable one.
*Revision detail:* the +9.23% "upgrade" is unusable for a 12-month view — 3 analysts on a 5-year-out number. The near-term consensus is *down*: FY2026E $1.936 vs FY2025A $2.06 = **−6.0%**. Sequentially: FY27E +5.4%, FY28E +10.1%. Sell-side targets were all cut (MS 45→35, Argus 52→41, Guggenheim 50→40, Telsey 40→38, GS 43→38, Mizuho 32→28); mean $35.88 = **+8.2% upside**.

### 2. Price Statistics (252d, vs SPY)

| Metric | Value | Read |
|---|---|---|
| Annualised return | **−48.81%** | Severe loss |
| Annualised vol | 35.8% | 1.6× HD, 1.6× TJX |
| Beta | **0.44** | Low — but see R² |
| Alpha (annualised) | **−54.88%** | **Not significant: t ≈ −1.5** |
| R² | **0.0265** | 97% of variance is idiosyncratic — alpha/beta are statistically empty |
| Sharpe | **−1.364** | vs HD −0.709, TJX −0.229, SBUX +0.674 |
| Sortino | **−1.802** | Worse than Sharpe ⇒ fat left tail |
| Max drawdown | **−47.05%** | Close-to-close peak-to-trough: $61.18 (Aug-25) → $28.94 (Jun-26) = −52.7% |

**Path:** flat $50–61 through Feb-2026, then a −45% collapse to $29 by early June-2026 (two gap-downs: −8.5% on 29-Jan and −12% on 21-Apr on 2–3× normal volume), now basing $29–35 for four months. Last 3 months +7.7% off the low.

**Correlations:** TSCO–SPY **0.16** (near-zero market linkage), TSCO–HD **0.48** (HD is the real comp, not the sector label), TSCO–TJX 0.12, TSCO–SBUX 0.24.

### 3. Composite Quant Signal: **NEUTRAL** (value-tilted, momentum-vetoed)
Value is top-quartile and quality is above-median, and that is genuinely rare at a 4.2% FCF yield. But it is offset by the worst momentum in the comp set, the highest volatility, a four-year ROIC decay, and negative near-term revisions. This is a **contrarian value/quality name, and a short-candidate for momentum or low-vol models** — the two frameworks disagree, so the composite lands at Neutral rather than Buy or Sell. Trigger to upgrade: two consecutive quarters of positive EPS revisions plus ROIC stabilisation.

### 4. Key Quant Risk Flags
1. **Momentum reversal already realised, not pending** — −39% 12-1, −53% peak-to-trough. Classic de-crowding of a former quality-compounder consensus long. Do not read the +7.7% tool output as positive momentum; it is a stale-vintage artefact.
2. **Alpha/beta are statistically meaningless** — R² = 2.6%. The 0.44 beta understates true market sensitivity, and the −54.9% alpha has a t-stat of roughly −1.5. Do not build hedges or risk budgets off these.
3. **Factor decay, not factor stability** — ROIC down 5.5pts in four years; GP/Assets 0.472 vs 0.52+ for HD and TJX; F-score 6/9 with all three deterioration flags tripped. Cheap for a reason.
4. **Revision signal has no statistical power** — n=3 on a FY2030 estimate. Ignore the "+9.23% upgrade."
5. **Small-sample ranking** — sector ranks are out of 4. Treat as ordinal colour, not percentile.
6. **Liquidity is fine** (~$400M/day notional); no crowding or capacity constraint.

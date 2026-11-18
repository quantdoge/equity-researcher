# Quant Analyst

- Symbol: NXT
- Elapsed: 36.5s

---
## NXT (Nextpower Inc.) — Quantitative Factor Report
**Price $78.48 (2026-11-17) | Mkt cap $11.98B | Energy / Solar | Beta ~2.6 | Vol 71%**

⚠️ **Data note:** an initial price pull truncated at 2026-06-01 ($145.02); the series actually runs to 2026-11-17. All figures below are anchored to the **$78.48** close, which reconciles exactly with the valuation-ratio and price-target feeds.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 2 / 5 | ~3rd of 5 solar peers (all-energy: bottom quintile) | **Weak / Neutral** |
| **Momentum** | 1 / 5 | Bottom decile | **Strong Sell** |
| **Quality** | 3 / 5 | Top tier absolute, bottom tier trend | **Neutral (deteriorating)** |
| **Low Vol** | 1 / 5 | Bottom quintile | **Strong Sell** |
| **Earnings Revision** | 3 / 5 | n=4 analysts (fragile) | **Mild Buy** |

**Value — raw:** P/E 20.4x, P/B 5.13x, EV/EBITDA 14.7x, P/FCF 23.4x, no dividend.
vs. true solar cohort: FSLR 10.8x/1.72x/6.5x; ENPH 17.9x/2.86x/12.4x; SHLS 35.2x/1.98x/18.7x; ARRY n.m./2.43x/25.5x.
NXT sits **exactly at the peer median EV/EBITDA (14.65x)** and slightly above median P/E (19.2x), but is the **most expensive on P/B in the group**. *However* — forward curve is materially better: FY27E EPS $4.79 → **16.4x**, FY28E $5.79 → **13.6x**, FY29E $7.01 → **11.2x**, against ~21–25% EPS growth (PEG ≈ 0.78). Trailing multiples understate the value case; the market isn't paying for the growth.

**Quality — raw:** ROE 25.1%, ROIC 29.2%, ROA 14.4%, GP/Assets 28.5%, accruals 0.72% (clean). **But trajectory is the story:**

| | FY24 | FY25 | FY26 |
|---|---|---|---|
| ROIC | 50.6% | 38.5% | **29.2%** |
| ROE | 30.9% | 31.3% | 25.1% |
| Gross margin | 27.7% | 33.7% | 32.6% |

Piotroski **F-Score 4/9 (weak)** — fails on ROA improvement, accrual quality, gross-margin improvement, asset-turnover improvement, and dilution (share count 143.5M → 148.0M → 152.7M, **+6.4% YoY**). Latest Q2 FY27 GAAP gross margin **31.1% vs 35.9% YoY (–480bp)** on record revenue — margin compression is the key quality defect. The tool returned `quality_signal: "low"`, which I regard as a methodology artifact: the composite penalizes the margin trend and dilution while underweighting a genuine 25% ROE / 29% ROIC. I score it mid, not low.

**Revision:** tool reports **+8.28%** (FY2031 $8.43 vs $7.79 prior) — I discount this heavily: it is a **2031 estimate built from only 4 analysts**, and the near-term revision direction is *not* available. Counter-evidence: the late-Oct PT cycle was dominated by **cuts** (Susquehanna 150→145, Roth 175→140, Northland→138, Needham→143, BMO→108), offset by Mizuho (→104) and Truist reiterating Buy at 145. **Median PT $141.50 across 8 notes = +80% implied**, but a $104–$158 spread (50% width) signals very low consensus confidence.

---

### 2. Price Statistics

| Metric | 252d (1y) | 126d | 504d (2y) |
|---|---|---|---|
| Annualised return | **–26.92%** | –67.54% | — |
| Annualised vol | **71.4%** | 69.2% | ~65% |
| **Beta vs SPY** | **2.62** | — | **2.38** |
| R² | 0.280 | — | 0.215 |
| **Alpha (annualised)** | **–55.17%** | — | **+6.46%** |
| Sharpe | **–0.376** | –0.976 | — |
| Sortino | **–0.648** | –1.602 | — |
| **Max drawdown** | **–51.1%** (tool) / **–53.8%** measured | | |

Drawdown detail: peak **$163.13 (2026-05-29)** → trough **$75.41 (2026-10-23)**, current $78.48 = **+4.1% off the low, –51.9% below the high.** Beta estimates cluster 2.38–2.62 (vendor profile shows 1.93 on a longer monthly window) — **use ~2.5**.

**⚠️ Alpha is not statistically significant.** With 71% daily noise and n=252: SE(alpha) ≈ 0.283%/day vs alpha of –0.219%/day → **t ≈ –0.8**. The 2-year alpha t-stat is ≈ 0.14. **Neither the –55% nor the +6.5% alpha is distinguishable from zero.** One year of 71%-vol data has almost no power to detect skill. Treat NXT's alpha as *unmeasurable*, not as –55%.

**Momentum (12-1, ex-last-21d):** **–23.2%**. Corroborated at every horizon: 126d **–0.95%**, 63d **–6.25%**. No sign of a base.

**Correlations (252d):** SPY **0.527** · ARRY **0.664** · SHLS **0.615** · FSLR **0.571** · ENPH **0.554**. ~0.55–0.66 within solar, 0.53 to the market → high sector co-movement, limited diversification benefit.

---

### 3. Composite Quant Signal: **NEUTRAL (negative tilt)**

Factor average 2.0/5. The fundamental (value-on-forward-growth, 25% ROE) and the price-based (momentum, vol, drawdown) factors point in **opposite directions**, and the price factors are far more statistically reliable here. **For any mandate with momentum or volatility constraints, this is a Sell** — bottom-decile momentum, bottom-quintile vol profile, Sharpe –0.38. There is no quant basis for adding to the position until momentum stabilises.

---

### 4. Key Quant Risk Flags

1. **Beta 2.5–2.6 = amplified market risk.** A 10% SPY drawdown mechanically implies ~25% NXT downside. Position sizing must be on beta-adjacent-risk, not notional.
2. **Gap risk exceeds model risk.** NXT fell **–11.3% on 2026-11-17** while renewables fell –6.9% — a 1.6x idiosyncratic amplification in a single session. Normal-distribution VaR systematically understates this.
3. **Factor crowding / single-shock exposure.** 0.55–0.66 correlation with FSLR/ENPH/ARRY/SHLS means solar policy or rate shocks hit the whole book at once. There is no "defensive solar" hedge inside the cohort.
4. **Quality deceleration is the real fundamental risk.** ROIC 50.6% → 29.2% in three years, F-Score 4, gross margin –480bp YoY, +6.4% annual dilution. High *level*, negative *second derivative*.
5. **Statistical power is inadequate.** 252 observations at 71% vol ⇒ |t| < 1 on alpha. Any strong conclusion drawn from NXT's one-year track record is over-fitting. A 3-year window is the minimum for a defensible view.
6. **Estimate/revision data quality.** The revision signal rests on a 2031 figure from 4 analysts; PT dispersion is $104–$158. Consensus is not a tight anchor.
7. **Liquidity: not a constraint.** ~2.0M shares/day (~$200M notional); the 27.2M-share print on 2026-06-26 was a rebalance, not a liquidity event. Ignore it in ADV calcs.

**Bottom line:** fundamentals retain the shape of a good business (25% ROE, 29% ROIC, 0.7% accruals, 13.6x FY28E) but momentum, volatility, drawdown and quality-trend are all bottom-quintile. The stock is a falling knife where the *valuation* argument is forward-looking and unproven and the *risk* argument is observable and current. Neutral, biased Sell.

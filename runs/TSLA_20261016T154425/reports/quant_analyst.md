# Quant Analyst

- Symbol: TSLA
- Elapsed: 49.7s

---
All data gathered. Here is the quantitative assessment.

---

# TSLA — Quantitative Factor & Risk Assessment
**Sector:** Consumer Cyclical / Auto Manufacturers | **Mkt Cap:** ~$1.27T | **Price:** ~$360 | **Data as of latest close**

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E 333.6x, EV/EBITDA 105.0x, P/FCF 204.3x, P/B 15.3x, 0% div yield | Bottom decile (most expensive in auto group — GM/F/TM trade ~7–8x P/E) | **Strong Sell** |
| **Momentum** | 12-1m total return **−10.4%** | Bottom half | **Sell** |
| **Quality** | ROE 4.6%, ROIC 4.8%, GP/Assets 12.4%, Accruals −0.08 (clean) | Bottom quartile; profitability collapsing | **Sell** |
| **Low Vol** | Vol 44.9% ann., Beta 2.18 vs SPY, MaxDD −33.6% | Bottom decile (highest-beta mega-cap) | **Strong Sell** |
| **Earnings Revision** | FY2030E EPS revised **+45.8%** (8.39 vs 5.76 prior), 8–9 analysts | Top quintile, but low coverage + long-dated | **Buy** |

**Quality deterioration detail (annual):** ROIC fell from **26.4% (2022) → 12.2% (2023) → 8.1% (2024) → 4.8% (2025)**; net income collapsed from $12.6B (2022) to **$3.8B (2025)**. Piotroski F-Score: **5/9 (moderate)** — profitability and asset-turnover components are failing. This is a margin-compression story, not a quality story.

## 2. Price Statistics (252-day window, benchmark SPY)

| Statistic | Value |
|-----------|-------|
| Alpha (annualised) | **−48.2%** |
| Beta | **2.19** (R² = 0.40 — 60% of variance idiosyncratic) |
| Sharpe ratio | **−0.22** |
| Sortino ratio | **−0.32** (downside worsens risk-adjusted picture) |
| Annualised return / vol | −10.0% / 45.5% |
| Max drawdown | **−33.6%** |

The stock produced a **negative 1-year absolute return with ~2.2x market beta** — deep negative alpha with double the market's risk. R² of 0.40 means factor/crowding explanation is weak; moves are largely Tesla-specific.

## 3. Composite Quant Signal: **SELL**

**4 of 5 factors are negative; the single positive (estimate revisions) has low statistical weight.**
- Value, Low Vol, and (currently) Quality are strong sells — extreme valuation (105x EV/EBITDA), extreme volatility/beta, and halved profitability.
- Momentum is negative (−10.4%) — price is not confirming the fundamental or revision story.
- Revision momentum is genuinely positive (+46%) but rests on FY2029–2030 estimates with only **8–9 contributing analysts** — small sample, and the consensus build (FY2028E $3.16 → FY2030E $8.39) embeds aggressive 2026/2030 volume-and-robotaxi assumptions. Flag as **insufficient sample size for high conviction**.
- Price targets are violently dispersed: $157 (HSBC) to $840 (Morgan Stanley bull case); recent revisions split both directions (UBS raised to $391, Stifel cut to $491, RBC cut to $480). Dispersion this wide signals elevated estimation risk, not a clean upgrade cycle.

## 4. Key Quant Risk Flags

1. **Momentum-reversal / valuation-reversion risk (HIGH):** 333x trailing earnings with negative 12-month price momentum is the classic "falling knife with a rich tag" setup; −48% annualised alpha shows the market has been repricing this multiple all year.
2. **Factor crowding / composition risk (MODERATE):** TSLA's pairwise correlations with autos are low (TM 0.25, GM 0.27, F 0.32, RACE 0.30; AMZN 0.32) and only 40% of variance loads on SPY — it is an idiosyncratic, momentum-tilted holding with heavy retail/options retail crowding embedded in the beta.
3. **Liquidity / drawdown risk (ELEVATED):** 45% annualised vol, −33.6% max drawdown, and 2.2x beta mean a 10% SPY selloff implies ~22% TSLA downside beta-wise; Sortino (−0.32) confirms downside participation is worse than the flat Sharpe suggests.
4. **Earnings-quality watch:** Despite collapsing income, operating cash flow remains strong ($14.7B) and accruals are negative (−0.08) — the balance sheet quality is fine; the problem is **profitability trajectory**, with F-score profitability components (ROA improvement, asset turnover) already failing.
5. **Estimate-revision caveat:** The bullish revision signal is computed on 8–9 long-dated analyst estimates; the cross-sectional dispersion (low $6.97 / high $10.25 on FY2030) means the signal's information content is low.

**Bottom line:** Quantitative evidence is unambiguously negative on value, volatility, momentum, and current profitability. The only bullish pillar is long-dated estimate momentum with thin coverage. **Composite: SELL** — do not interpret the +46% revision as a buy catalyst unless price begins confirming (momentum turns positive and drawdown repairs).

*Note: Sector ranks for Momentum/Quality are estimates — exact cross-sectional peer factor scores were not computed this pass; Value rank is robust from reported multiples.*

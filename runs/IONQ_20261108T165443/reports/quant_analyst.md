# Quant Analyst

- Symbol: IONQ
- Elapsed: 51.8s

---
## IONQ — Quantitative Factor & Risk Report
**Price $31.90 (2026-02-20) | Sector: Technology / Computer Hardware | No dividend**

### 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| Value | 1 / 10 | n/a — no valid comps | **Strong negative.** P/E −17.9, EV/EBITDA −14.3, P/FCF −30.5 (all negative → screen fail). Only usable anchor P/B 2.35. EV/Sales 25.4x on 2026E, **89x trailing**. Top-decile expensive. |
| Momentum | 3 / 10 | n/a | **Headline positive, trend negative.** 12-1 = +11.5%, 126d = +2.2%. But 1M **−34.0%**, 3M **−33.4%**, 12M −5.5%. |
| Quality | 2 / 10 | n/a | **Weak.** ROE −13.4%, GP/assets 0.008, F-Score **3/9**. Gross margin **52.2% → 40.4%** (deteriorating). |
| Low Vol | 0 / 10 | n/a | **Worst decile.** Vol 96.3% (252d) / 91.0% (504d); beta **3.65**; max DD **63.3%**. |
| Earnings Revision | **Unreliable — N/A** | n/a | Tool reports +80.4% "upgrade" but compares **FY2030 vs FY2029** estimates with **1 analyst**. Not a valid signal. |

**Composite Quant Signal: SELL** (4 of 5 factors negative; the one positive factor is stale and reversing)

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY) | **−17.97%** |
| Beta | **3.651** (R² **0.2887**) |
| Annualised return (252d) | +31.41% |
| Annualised vol | 94.35% (252d) / 91.0% (504d) |
| **Sharpe** | **0.333** |
| **Sortino** | **0.690** (Sortino/Sharpe 2.07 → positively skewed) |
| Max drawdown | 63.33% (252d) / **67.8%** (504d) |
| Peak-to-trough (measured) | $82.09 (2025-10-13) → $30.43 (2026-02-05) = **−62.9%** |
| Recovery to prior peak | requires **+157%** |

Note: the low-vol module returns a Sharpe of 0.189 (≈18%/96.3%) vs 0.333 from the dedicated module — an arithmetic-vs-geometric annualisation difference. Use 0.333 for absolute, 0.189 for conservative comparability.

### 3. Fundamental Cross-Check (FY2025 10-K, filed 2026-02-25)

Revenue $22.0M → $43.1M → **$130.0M** (+95%, +202%); 2026E **$456.2M** (+251%). Genuine hyper-growth. But net loss widened $331.6M → **−$510.4M**, OCF −$283.2M, and **diluted shares +31.6% y/y** (213.0M → 280.3M; F-Score F7 = 0). Consensus still models losses through FY2029 (EPS −1.29 / −1.37 / −1.20 / −0.69), first positive EBITDA 2029–30. Accruals ratio −0.0346 is negative, but that reflects large non-cash charges, not conservative accounting quality. Sell-side median PT ~**$51** (range $43–$85), but the recent action is **4 cuts / 4 raises** — a distribution being chased downward, with price now below the lowest target.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** The only positive factor is backward-looking. Trailing 1-month −34% against 12-1 +11.5% is textbook momentum reversal; the Sep–Oct 2025 run is fully unwound. Do not treat the momentum score as a buy input.
2. **Factor/sector crowding — HIGH.** Correlation **0.853 vs QBTS, 0.870 vs RGTI**, but only **0.535 vs SPY**. Despite R² of just 0.29 vs the market, this is *not* idiosyncratic risk — it is one crowded quantum-theme factor. Zero diversification benefit within the theme and simultaneous de-risking is likely.
3. **Beta estimation error.** Beta readings cluster 3.31–3.65 across windows (profile 3.30). At R² = 0.29, the confidence interval is wide; do not size hedges off beta 3.65 as if it were precise.
4. **Negative alpha.** −18.0% annualised on a +31% raw return — beta-adjusted underperformance. The return is compensation for extreme vol, not skill.
5. **Data inconsistency on market cap.** Profile $14.0B (≈429M shares) vs valuation module $9.14B (stale 280.3M diluted count). EV/Sales on 2026E is **25.4x or 14.9x** depending on which is right — a wide band around the single most important valuation input. Treat the multiple as uncertain.
6. **Liquidity — NOT a flag.** ~15M shares/day (~$480M notional) is ample. Note it can gap, not trap.
7. **Stale/incorrect labels.** Analyst PT `published_date` fields (2026-05 to 2026-11) post-date the price series ending 2026-02-20; `price_when_posted` values are consistent, so dates are mislabelled. Peer tool returns AAPL/NVDA/MSFT for "Technology" — **not valid comparables**; all sector ranks above are therefore marked n/a rather than fabricated.
8. **Sample size caveats.** 252d ≈ 250 daily observations — adequate for vol, marginal for beta at R² 0.29. FY2030 EPS rests on **1 analyst**; FY2025 fundamentals were filed 5 days *after* the price series ends and are not yet in the tape.

**Bottom line:** A statistically extreme asset — 96% vol, beta 3.65, −18% alpha, 63% drawdown — currently screening negative on four of five factors with its only positive signal reversing. The revenue trajectory is real, but no factor in the model pays for it at 25x forward sales, and the crowding correlation means the risk is not diversifiable by owning another quantum name.

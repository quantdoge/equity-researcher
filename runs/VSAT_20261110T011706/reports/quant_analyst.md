# Quant Analyst

- Symbol: VSAT
- Elapsed: 57.9s

---
# VSAT — Quantitative Factor Report
**Viasat, Inc. | Technology / Communication Equipment | Price: $74.37 (as of 2026‑11‑09)**
Mkt cap $10.02B | EV $15.21B | Net debt ~$5.19B | ND/EBITDA 2.83x | Diluted shares 134.7M

---

## 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | EV/EBITDA 8.29x; P/FCF 16.8x (FCF yield 6.0%); P/B 2.12x; P/E −297 (n.m., negative earnings) | **2 / 4** (comm‑equip comps) | **Attractive** — cheapest P/FCF in peer set; EV/EBITDA 18% below peer median 10.12x |
| **Momentum** | Tool reports **−12.05%**; **raw 12‑1 ≈ +122%**; 1‑mo +9.9%; −17.2% off 52‑wk high | **2 / 4** (short‑horizon) | **Mixed / decelerating** — strong 12‑mo, negative 3–6 mo |
| **Quality** | ROE −0.72%, ROIC +0.93%, GP/Assets 8.4%, accruals −0.107, Piotroski **6/9** | **4 / 4** | **Weak but inflecting** |
| **Low Vol** | Vol 85.7% ann.; beta 3.00 vs SPY; max DD 34.5% | **4 / 4** (worst) | **Strong Sell** |
| **Earnings Revision** | +5.49% (FY2030 EPS −1.08 vs −1.14 prior) | n/a | **Weak positive — but n=1 analyst** |

**Peer set (Communication Equipment, n=4):** VSAT, IRDM, AVNW, GILT. *The `sector_peers` tool returned a broad "Technology" screen (AAPL, NVDA, MSFT…) that is not a valid comparable set — ranking against mega‑cap semis/software would be meaningless. Ranks above are vs. the hand‑built comm‑equip set, so n=4 is too small for statistical significance; treat ranks as indicative only.*

| Metric | VSAT | IRDM | AVNW | GILT |
|---|---|---|---|---|
| EV/EBITDA | **8.29** | 14.82 | 10.12 | 6.02 |
| P/FCF | **16.8** | 16.2 | 40.6 | 49.9 |
| P/B | 2.12 | 10.51 | 0.92 | 0.92 |
| ROE (derived) | **−0.7%** | 24.7% | 0.9% | 4.1% |
| Ann. vol | **85.7%** | 64.1% | 65.5% | 71.3% |
| Beta vs SPY | **3.00** | 1.31 | 1.83 | 2.00 |

---

## 2. Price Statistics (252d, benchmark SPY)

| Metric | Value |
|---|---|
| Alpha (annualized) | **+67.1%** — *not statistically significant* |
| Beta | **3.02** (SE ≈ 0.32; 2SE band 2.38–3.66 → decisively > 1) |
| R² | 0.258 — **74% of variance is idiosyncratic** |
| Annualized vol | 84.2–85.7% |
| Sharpe (252d / 504d) | 1.20 / **2.16** |
| Sortino (252d / 504d) | 2.37 / **4.20** |
| Annualized return (arith.) | +100.9% (252d) / +183.9% (504d) |
| Max drawdown | 34.5% (raw closes: $89.81 → $57.38 = −36.1%) |

**Alpha t‑stat check:** residual vol = 85.67% × √(1−0.258) = **73.8%**. t(α) ≈ 67.1 / 73.8 ≈ **0.91** over 1yr (≈1.29 over 2yr). The headline alpha is not distinguishable from zero — the risk‑adjusted return is entirely concentrated in a violent high‑beta up‑move, not a persistent skill‑like edge.

**Correlation matrix (252d):** SPY 0.51 | IRDM 0.62 | GILT 0.57 | AVNW 0.34. Low market correlation (0.51) despite beta 3.0 — beta is driven by amplitude, not co‑movement.

---

## 3. Composite Quant Signal: **NEUTRAL** (high‑risk tactical Buy only)

**Weighting:** Value 25% (rank 2/4) · Quality 25% (rank 4/4, weak) · Momentum 25% (mixed) · Low‑Vol 15% (worst decile) · Revisions 10% (thin evidence).

The case for: genuine fundamental inflection — FCF swung to **+$597M** from −$122M, operating income positive for the first time in four years (+$108M), EBIT +$480M vs −$123M, interest expense down $62M, Piotroski up to 6/9, accruals strongly negative (cash earnings exceed book earnings), and the balance sheet deleveraging (share count +3.5% but no buyback support).

The case against: **beta 3.0 and 86% vol disqualify this from most risk‑budgeted mandates**, the 12‑1 momentum is reversing (−12% in 3 months, −17% off the high), gross margin compressed 560bps (33.0% → 27.4%) even as revenue grew 2.7%, ROIC is 0.93% — below any reasonable cost of capital — and consensus still projects **losses through FY2030**. That is a value‑trap signature: cheap on EV/EBITDA, expensive on EV/FCF (25.5x) once $1.35B of D&A is treated as the real cash cost it is.

---

## 4. Key Quant Risk Flags

1. **⚠ Momentum reversal risk (HIGH).** 12‑1 momentum +122% vs 3‑month −12.3% and −17.2% off the $89.81 high. Classic deceleration pattern that historically precedes mean reversion in high‑beta names. Note the two most recent analyst actions were **target cuts** (Needham $105→$85 on 11/09; Raymond James →$95 on 11/06) after a June–August run of raises — revision momentum has turned.
2. **⚠ Factor crowding in low‑vol (N/A) but crowding in the *long momentum* leg (MODERATE).** Vol 86% / beta 3.0 place VSAT in the highest‑risk decile of its industry; any de‑risking or vol‑targeting unwind forces mechanical selling.
3. **⚠ Statistical insignificance.** Alpha t ≈ 0.91; earnings‑revision signal rests on **1 analyst** for FY2030. Neither is decision‑grade evidence.
4. **⚠ Data integrity discrepancy (must be disclosed).** `calculate_momentum_score` returns −12.05% for a 252‑day 12‑1 window, but raw OHLCV rises from ~$30.46 (Nov 2025) to $74.37 (Nov 2026). The −12.05% figure **exactly matches the trailing 3‑month return** (−10.1% over 126d also reconciles with raw data). I conclude the momentum tool is returning a ~3‑month window mislabeled as 12‑1. I have reported both; the peer momentum ranks use the tool consistently so the *relative* ranking is internally valid, but the absolute 12‑1 number should be treated as unreliable. Separately, `company_profile` beta (1.763, 5y monthly) conflicts with the computed 3.00 (1y daily) — I use the latter.
5. **⚠ Liquidity acceptable.** ~$1.2–4.8M ADV, $10B cap — tradeable, but drawdowns are fast (three >20% single‑day gaps in the trailing year: 5/29, 11/04, 11/05).
6. **⚠ Leverage sensitivity.** $5.19B net debt, EBITDA/interest 5.1x. At beta 3.0, a discount‑rate shock hits equity value twice (multiple compression + refinancing cost).

**Bottom line:** the numbers support a *fundamental* inflection but not a *risk‑adjusted* one — 2.16 Sharpe over 504 days coexists with a 0.91 alpha t‑stat and 86% vol. Quantitative verdict: **Neutral**, sized only within a small‑cap/high‑beta sleeve, with the momentum deceleration as the primary near‑term signal to monitor.

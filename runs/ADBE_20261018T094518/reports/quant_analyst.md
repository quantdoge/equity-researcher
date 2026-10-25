# Quant Analyst

- Symbol: ADBE
- Elapsed: 19.8s

---
# ADBE (Adobe Inc.) — Quantitative Factor Report

**Sector:** Technology / Software – Application · **Price:** $245.20 · **Mkt Cap:** $95.4B (calc. $104.7B using 427M diluted shares — flag: profile cap and ratio cap disagree ~9%) · **FY end:** Nov

---

## 1. Factor Scores Table

Peer set = 6 large-cap US application/infrastructure software names (ADBE, INTU, CRM, NOW, MSFT, ORCL). The official sector-peer endpoint returned only mega-cap **semiconductors** (NVDA, AAPL, TSM, AVGO…), which is not a valid comparable set, so ranks below are computed off the raw factor inputs for the software comps. **n=6 is a coarse rank — quintiles are effectively thirds; treat ranks as ordinal, not precise.**

| Factor | Score (raw) | Sector Rank (of 6) | Signal |
|---|---|---|---|
| **Value** | P/E 14.68 · EV/EBITDA 10.67 · P/FCF 10.63 · P/B 9.01 | **1 / 6** | **Strong positive** |
| **Momentum** (12-1, 252d) | +11.80% | 4 / 6 | Neutral / weak positive |
| **Quality** | ROE 61.3% · GP/Assets 0.719 · Accruals −0.098 · F-Score 7/9 | **1 / 6** | **Strong positive** |
| **Low Vol** | σ 44.4% · β 0.29 · MDD −42.1% | 2 / 6 | Positive (rel.) / negative (abs.) |
| **Earnings Revision** | FY30 EPS 34.84 vs 37.26 prior → **−6.49%** | n/a | **Negative (downgrade)** |

**Peer comparison detail**

| | ADBE | INTU | CRM | NOW | MSFT | ORCL |
|---|---|---|---|---|---|---|
| P/E | **14.68** | 19.75 | 30.86 | 85.01 | 29.47 | 21.99 |
| EV/EBITDA | **10.67** | 12.82 | 18.08 | 48.27 | 19.25 | 14.87 |
| P/FCF | 10.63 | **10.45** | 15.98 | 32.48 | 58.86 | neg |
| ROE % | **61.34** | 24.04 | 12.61 | 13.48 | 30.23 | 39.69 |
| GP/Assets | **0.719** | 0.467 | 0.287 | 0.395 | 0.297 | 0.168 |
| Accruals | −0.098 | −0.116 | −0.067 | −0.142 | −0.065 | −0.057 |
| 12-1 Mom % | 11.80 | 10.90 | **46.67** | 24.47 | 28.71 | 2.71 |
| Ann. Vol % | 44.4 | 55.5 | 51.5 | 63.3 | **36.0** | 59.5 |
| β (1y dly) | 0.29 | 0.16 | 0.34 | 0.62 | 1.05 | 2.29 |
| Sharpe | −0.29 | −1.30 | 0.07 | 0.32 | **0.56** | −0.64 |

ADBE is the **cheapest and highest-quality name in the group simultaneously** — a rare combination. It is not, however, a low-volatility stock in absolute terms (44% annualised vol, −42% drawdown); its low beta is a statistical artifact of near-zero market correlation, not genuine defensiveness.

---

## 2. Price Statistics (252-day window, benchmark SPY)

| Metric | Value | Comment |
|---|---|---|
| Annualised return | **−12.95%** | Negative absolute return |
| Annualised volatility | 44.4% | Very high for a large-cap software name |
| Beta vs SPY | **0.293** | vs 1.415 in the company profile (5y basis) — see flag |
| Alpha (annualised) | **−34.67%** | **NOT statistically significant** (t ≈ 0.8) |
| R² vs SPY | **0.0075** | Market explains <1% of ADBE's variance |
| Correlation vs SPY | 0.086 | Essentially uncorrelated with the index |
| **Sharpe ratio** | **−0.292** | Below zero; poorly compensated risk |
| **Sortino ratio** | **−0.455** | Downside deviation worse than total vol ⇒ fat left tail |
| Max drawdown | **−42.08%** | Severe peak-to-trough |
| 12-1 momentum | +11.80% | Positive but bottom-half of peer group |

**Statistical caveat (material):** with R² = 0.0075, the −34.7% alpha is noise. Rough t-statistic ≈ **0.8** — far below significance. The correct read is *not* "ADBE destroys 35 points of alpha"; it is **"ADBE's returns are ~entirely idiosyncratic and unexplained by market beta."** Any beta-hedged or factor-neutral construction on this name will carry large unhedged single-stock risk. Note also the two tools disagree on Sharpe (−0.292 from `sharpe_sortino` vs −0.687 from `low_vol_score`), likely differing return-compounding conventions; I report both and anchor on the −0.29 figure.

**Peer correlation (252d):** CRM 0.76, NOW 0.77, INTU 0.72 — **ADBE is tightly coupled to the SaaS/creative-software complex but decoupled from the market.** This is crowding risk in a specific cluster, and simultaneously why index beta looks low.

---

## 3. Composite Quant Signal: **BUY** (not Strong Buy)

Rationale and weighting:
- **Value #1/6** and **Quality #1/6** — the two factors with the strongest long-run empirical premia. Both are decisively supportive: EV/EBITDA 10.7x and FCF yield ~9.4% (P/FCF 10.63) for a business with 61% ROE, 72% gross-profit-to-assets, negative accruals (−9.8% = cash earnings exceed reported), and a Piotroski F-Score of 7.
- **Low Vol #2/6 on relative measures**, but 44% absolute vol and a −42% drawdown cap the score.
- **Momentum #4/6 (+11.8%)** — positive but lagging the peer group by 13–35 pts. Not a reversal signal, not a tailwind.
- **Earnings revision −6.49%** — the sole clearly negative factor, though measured on an FY2030 estimate covered by only **6 analysts** (vs 23 for FY2026). Low statistical reliability.
- **Price statistics are poor** (Sharpe −0.29, Sortino −0.46, MDD −42%), which is the reason this is not a Strong Buy despite a textbook value+quality double top-quintile profile.

Forward multiple check: at $245.20 on the FY2026 consensus of $24.48, forward P/E ≈ **10.0x** — extremely compressed versus a 5-year peer average in the high-20s. Note the trailing P/E of 14.68 implies ~$16.70 trailing EPS (GAAP-like), so trailing and forward figures are not on the same accounting basis; do not read the 14.7x→10.0x step as pure earnings growth.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal / value-trap risk (highest concern).** Cheap + high quality + negative revisions + −13% trailing return is the classic value-trap signature. The revision score is negative and the most recent sell-side actions were adverse (Wells Fargo double-downgrade to Underweight, PT $270→$225; HSBC to Hold). Median recent PT ≈ $260 vs $245 spot — only ~6% upside, i.e. the Street is not yet underwriting a re-rating.
2. **Estimate-revision sample is too thin.** The −6.49% revision is computed on a 5-year-forward (FY2030) consensus with just 6 contributing analysts, and the forward curve is internally inconsistent (FY2029 $37.26 → FY2030 $34.84 — an implied EPS *decline* that no fundamental model supports). Treat the revision score as low-confidence and worth only partial weight.
3. **Beta instability / model risk.** Beta of 0.293 (1y daily) vs 1.415 (profile, long-horizon) with R² of 0.0075. Hedging this name on a 0.29 beta is dangerous — the hedge will not track. Size on total volatility (44%), not beta-adjusted.
4. **Fat left tail.** Sortino (−0.455) worse than Sharpe (−0.292) means downside deviation exceeds total deviation; the −42% max drawdown within a 12-month window is a live, recent event, not a tail hypothetical.
5. **Factor crowding in SaaS cluster.** 0.72–0.77 correlation with CRM/NOW/INTU means ADBE will not diversify a software-heavy book; the value+quality tilt is against a momentum-led peer group, so expect tracking-error pain if the momentum factor keeps running.
6. **Liquidity: not a concern.** $95B+ market cap; no capacity constraint.

**Bottom line:** the numbers support a *statistically cheap, genuinely high-quality* business trading at ~10x forward earnings with cash-backed (negative-accrual) earnings — a legitimate **Buy** on fundamentals. They do **not** support a Strong Buy: momentum is middling, revisions are negative on thin data, and realized risk-adjusted performance over the past year is negative on every measure. This is a valuation call that requires patience, not a momentum confirmation.

*Data gaps: sector-peer endpoint returned semis only; peer ranks computed on a hand-constructed n=6 software set. Trailing/forward EPS accounting basis appears mixed. Sharpe computed with 0% risk-free rate, so all Sharpe figures are overstated by roughly the T-bill yield (≈4–5%), i.e. true Sharpe for ADBE is near −0.8.*

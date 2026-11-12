# Quant Analyst

- Symbol: SE
- Elapsed: 66.4s

---
# SE (Sea Limited) — Quantitative Factor & Risk Report

**Price $73.39** | Mkt cap ~$44.9B | Singapore / Consumer Cyclical (Specialty Retail) | Data as of 2026-11-12

---

## 1. Factor Scores

| Factor | Score / Raw | Rank vs Direct Peers* | Signal |
|---|---|---|---|
| **Value** | P/E 29.1x, P/B 3.71x, EV/EBITDA 14.0x, **P/FCF 10.4x** | 2 of 4 on P/E; 2 of 4 on P/FCF | **Neutral** (cheap on cash flow, rich on earnings) |
| **Momentum (12-1)** | **−15.15%** | **4 of 4 — worst** | **Strong Negative** |
| **Quality** | ROE 12.48%, GP/Assets 0.349, Accruals **−0.118**; composite label "low" | 3 of 4 on ROE & GP/A; **1 of 4 on accruals** | **Neutral-to-Positive** (see caveat) |
| **Low Vol** | Vol **53.1%**, beta 1.16 vs SPY, max DD 44.2% | **4 of 4 — worst** | **Strong Negative** |
| **Earnings Revision** | +23.76% vs 3-mo prior | n/a | **Mild Positive — low confidence** |
| **Piotroski F-Score** | **8 / 9 (Strong)** | — | Positive |

\*Measured comparison set: AMZN, BABA, PDD (largest Specialty Retail / e-commerce peers). Full 13-name sector rank **not** computed — see data gaps.

**Factor detail:**
- **Value:** Forward multiples are far more attractive than trailing: FY26E P/E 20.0x ($3.67), FY27E 16.4x ($4.49), FY28E 12.9x ($5.68). P/FCF of 10.4x is genuinely cheap for a business growing revenue +36% yoy. Trailing 29.1x is the drag.
- **Quality — the composite label conflicts with its own inputs.** ROE 12.5% sits below the model's threshold, which is what drives the "low" tag. But GP/Assets 0.349 (top-tier, Novy-Marx) and accruals of **−0.118** (net income well below operating cash flow — very high earnings quality) both argue the opposite way. ROIC trajectory is the strongest datum: **−14.5% → 2.0% → 5.3% → 11.7%**. F-score 8/9. I treat Quality as **improving, mid-pack**, not weak. Sole F-score miss: **F7 no-dilution** — diluted shares 594M → 604M → **638M (+7% yoy)**.
- **Earnings Revision — discount heavily.** The +23.8% figure compares FY**2030** EPS ($6.98 vs $5.64) on **6 analysts**. That is a long-dated, thin-coverage estimate, not a forward-12m revision, and its standard error is large. The corroborating evidence is mixed: price targets were **cut hard** in November ($156→$142 Jefferies, $153→$110 BofA) and New Street **downgraded to Neutral** at a $70 target.
- **Momentum — the −15.15% score understates the damage.** The 12-1 convention excludes the last 21 trading days, and that window is where the crash happened: **$95.88 (Oct 12) → $73.44 = −23.4%**. Full 12-month return is ≈ **−35%**. Oct 20 alone: **−9.1% on 18.9M shares (~4.7x average volume)** — an earnings-driven gap, not drift.

---

## 2. Price Statistics (252-day window, vs SPY, rf = 0%)

| Metric | Value |
|---|---|
| Annualised return | **−35.81%** |
| Annualised volatility | **53.56%** (vs AMZN 36.1, BABA 40.7, PDD 34.1) |
| Beta vs SPY | **1.166** (profile beta 1.563 — 5-yr basis) |
| Alpha (annualised) | **−52.87%** |
| R² | **0.0997** |
| Sharpe | **−0.669** |
| Sortino | **−1.058** |
| Downside deviation (implied) | 33.9% |
| Max drawdown | **−44.16%** (peak $131.51 on Aug 11 → $73.44) |
| Current drawdown from peak | **−44.2%** |

**Interpretation:**
- **The alpha is not statistically significant.** R² = 0.10 means SPY explains only 10% of SE's variance; residual volatility is ≈51%, giving a t-stat on alpha of roughly **−1.0**. A −53% alpha headline is a point estimate with a ±50pp standard error over a one-year window. Do not quote it as evidence of manager/stock skill or the absence of it.
- **Sortino (−1.058) worse than Sharpe (−0.669)** despite downside deviation (33.9%) being *below* total vol (53.6%): the damage is concentrated in a handful of gap days rather than broad-based. That is gap/event risk, not grind-lower risk — relevant for position sizing and stop placement.

---

## 3. Composite Quant Signal

### **NEUTRAL — with a negative momentum overlay**

**On a pure cross-sectional factor model this is a Sell/underweight.** SE ranks in the bottom decile on the two factors with the strongest short-horizon empirical record (momentum, low-vol) and is only mid-pack on value and quality. It would fail a long-only multi-factor screen.

**It is not a Strong Sell** because three things cut against the momentum signal: (1) F-score 8/9 with deeply negative accruals — earnings are cash-backed; (2) ROIC quadrupling in three years with operating margin expanding from −12.0% (2022) to 8.1% (2025); (3) a forward P/E of 16.4x on FY27E for a +36% revenue grower. Median analyst PT across the last 10 notes is **$133.50** (+82% vs spot), range $70–$156.

**The honest read:** this is a *broken-momentum, high-beta, post-guidance-cut* name. The negative momentum is real and recent (−44% in three months), which historically carries a meaningfully higher probability of short-term reversal than of continued decline — but that reversal is a **trade, not a factor signal**, and it requires an event catalyst to time. Factor discipline says wait for momentum to inflect.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (two-sided).** −15.15% 12-1 momentum *plus* −23% in the last month is a classic knife-catch setup. Shorting here is fighting mean reversion; buying here is fighting momentum. Both are low-conviction at this price.
2. **Highest volatility in the peer group (53.1%) with beta 1.16–1.56.** A 2-sigma event is ±6.7%/day. Gap risk is demonstrated, not theoretical (Oct 20: −9.1% on 4.7x volume).
3. **Alpha is unmeasurable at this sample size.** R² 0.10 over 252 days. Any performance attribution to SE's "alpha" is noise. The 252-day window spans exactly one rally-and-crash cycle — **regime-dependent, n≈1**.
4. **Earnings-revision score is structurally unreliable** (FY2030, 6 analysts). Weight the *price-target* trend (falling) over the EPS revision score (rising) — the PT trend is the more timely signal.
5. **Dilution.** +7% diluted shares yoy, the only F-score failure. Offsets part of the ROIC improvement on a per-share basis.
6. **Data quality gaps (explicit):**
   - BABA (P/E 2.15, EV/EBITDA 0.69, P/FCF −4.49) and PDD (P/E 1.18, EV/EBITDA −3.08) multiples are **not credible** — likely stale share counts or currency mismatch. Value ranking therefore rests effectively on AMZN alone; treat the peer value rank as **indicative only**.
   - Full 13-name Consumer Cyclical sector rank not computed (12-name peer list returned; only 3 scored). Sector Rank column reflects the 4-name e-commerce subset.
   - Beta conflict: 1.166 (252d daily) vs 1.563 (profile). Use 1.16 for short-horizon risk, 1.56 for cost-of-equity.
   - No dividend; dividend-yield comparisons n/a.

---

**Bottom line:** Factor-implied rating **Neutral / underweight**. The quality trajectory and cash-flow-based valuation are real and improving; the price, momentum, and volatility factors are uniformly poor. Quantitatively this is a **watchlist name pending a momentum inflection**, not a factor buy at $73.39.

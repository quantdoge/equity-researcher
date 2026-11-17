# Quant Analyst

- Symbol: TSCO
- Elapsed: 105.2s

---
## TSCO — Quantitative Factor Report
**Price $37.95 (close 2026-11-16) · Mkt cap $20.2B · Consumer Cyclical / Specialty Retail**
Peer set for cross-sectional ranks: **HD, LOW, TJX, DG** (n=5 incl. TSCO — small sample; ranks are indicative only, not statistically robust)

### 1. Factor Scores

| Factor | Score | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 18.4 · EV/EBITDA 13.2 · P/FCF 27.3 · FCF yld 3.67% · div 2.53% | **2** | **Buy** — cheapest P/E and EV/EBITDA in comp set (HD 24.4/16.3, TJX 26.9/18.1). Only LOW screens cheaper; FCF multiple is the weak link (27.3x vs LOW 16.5x, DG 12.6x) |
| **Momentum** | 12-1m **−37%** (recomputed from validated closes) · 1m +14.4% · 3m +10.2% · 6m +21.4% | **5 / 5 on 12-1**; 1–3m best | **Sell** — deep negative 12-1 (bottom decile), but violent short-term reversal off the June low. Mature downtrend, nascent uptrend |
| **Quality** | ROE 42.5% · ROA 10.0% · **ROIC 17.2%** · GP/assets 0.472 · accruals **−0.049** | **3** | **Neutral/Improving-risk** — clean earnings (negative accruals = cash > income), but GP/assets is 4th of 5 and **ROIC has fallen 4 straight years** (22.7→20.6→19.1→17.2) |
| **Low Vol** | Vol 36.0% · beta 0.21 (R²=0.007 — **meaningless**) · **Max DD −46.4%** | **4** | **Sell** — beta-based score flatters it; realized vol is 2nd-highest and drawdown is the **worst in the comp set** (HD −26.5, TJX −26.8, DG −34.6, LOW −36.9) |
| **Earnings Revision** | **+9.47%** (FY2030 EPS 2.443→2.674) | n/a | **Weak Buy / low confidence** — only 5 analysts, **5 years forward**. Near-term is the opposite: FY2026 EPS $1.956 = **−6.6% YoY**; FY2027 +5.1%, FY2028 +10.4%. 8 PT raises in 48h (Oct 22–23), but median PT **$35.5 = −6.5% vs spot** |

Piotroski **F-Score 6/9** (moderate): fails ROA improvement, gross-margin improvement, and asset-turnover improvement — all three efficiency deltas negative.

### 2. Price Statistics
| Metric | Value |
|---|---|
| Annualized return (252d) | **−34.4%** |
| Annualized vol | **36.0%** (comp median ~30.9%) |
| Sharpe | **−0.953** |
| Sortino | **−1.381** |
| Alpha (ann., vs SPY) | **−38.4%** — *but R² = 0.007* |
| Beta (vs SPY) | **0.21** (tool) vs **0.484** (company profile) |
| Max drawdown | **−46.4%** (close-basis 54.66 → 28.94 = **−47.1%**) |
| 52-wk range | $28.94 – $54.66; **spot at 35th percentile** |
| Off high / off low | **−30.6%** / **+31.1%** |
| Liquidity | ~10M sh/day ≈ **$380M ADV** — no constraint |

Sortino worse than Sharpe (−1.38 vs −0.95) ⇒ downside deviation 24.9% < total vol 36.0%: the volatility is unusually *two-sided*, driven by single-day gaps (**Apr 21 2026: −11.7% on 25.9M sh, ~4x normal volume**; Oct 22 +6.2%). Return distribution is fat-tailed, not gradually eroding.

### 3. Composite Quant Signal: **NEUTRAL** (score ≈ −0.5 of ±5)
Sum of tilts: Value **+1.5**, Quality **+0.5**, Revisions **+0.5**, Low-Vol **−1.5**, Momentum **−1.5**.
Cheap, cash-generative, and stabilizing — but this is a **broken-momentum, deteriorating-returns name trading above consensus fair value**. Not a quant Buy until either (a) 12-1 momentum inflects, or (b) ROIC stabilizes. Absolute-quality long only at/below ~$33 (FY26 P/E <17x).

### 4. Key Quant Risk Flags
1. **⚠ Benchmark statistics are unreliable.** TSCO–SPY correlation = **0.083** while TSCO–HD = 0.53, –LOW = 0.53, –DG = 0.49. A large-cap retailer cannot have near-zero market correlation when its peers run 0.28–0.35. The whole alpha/beta/R² block (beta 0.21, R² 0.7%, alpha −38%) is therefore **circular and overstated** — 99.3% of return variance is "unexplained." Use **beta ≈ 0.48**. Note the true alpha vs a retail peer basket is smaller than −38%: part of the decline is sector-wide (HD −12.2%, LOW −12.3%, TJX −8.4% 12-1 momentum), but TSCO's is **3x worse** — the excess decline is genuinely idiosyncratic.
2. **⚠ Factor-tool price series conflict.** `calculate_momentum_score` returns **−4.40%** (252d) and **−3.02%** (126d) — nearly identical for two very different windows, which is a degenerate signature. Recomputed from the raw close series (validated: 2026-10-22 close $34.73 and 2026-10-23 close $33.42 exactly match independent analyst "price when posted" records), true 12-1 momentum is **−37%** and 6-month momentum is **+21%**. I use the recomputed figures. Do not rely on the momentum tool for this ticker.
3. **Momentum-reversal / falling-knife risk (high).** −37% 12-1 momentum with a +21% six-week bounce. The bounce is unconfirmed by volume or revisions; buying strength here is buying a countertrend rally in an intact downtrend.
4. **Return-on-capital decay (highest-conviction fundamental flag).** ROIC −5.5pp over 4 years, with F-score explicitly failing gross margin and asset turnover. The 42.5% ROE is **leverage-and-buyback manufactured** (ROA 10.0% × 4.24x; P/B 7.8x). Net debt/EBITDA **≈2.9x** on $5.7B net debt — thin cushion if comps weaken.
5. **Factor crowding: not a concern** (negative-momentum, out-of-favour name). The opposite risk applies — **value trap**.
6. **Estimate-revision quality is poor.** The +9.47% "upgrade" is a FY2030 number from 5 analysts. The actionable near-term signal (FY2026 −6.6% YoY, tight $1.94–1.98 range across 11 analysts) says consensus is *confident about earnings decline*, not improvement.
7. **Sample-size caveat:** n=5 for ranks, 252d single-window regressions, ~5–11 analysts on forward estimates. No statistical significance claimed.

**Bottom line:** Value and balance-sheet quality say cheap; momentum, ROIC trend, and drawdown say don't catch it yet. Neutral,

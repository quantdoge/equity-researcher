# Quant Analyst

- Symbol: BE
- Elapsed: 58.7s

---
# Quantitative Factor Report — BE (Bloom Energy Corp.)

**Sector:** Industrials / Electrical Equipment & Parts | **Price:** $203.17 (last close 2026-10-30) | **Mkt cap:** $49.7B (240.4M diluted sh.) | **Beta (regression, 252d):** 4.31

---

## 1. Factor Scores Table

| Factor | Score | Sector / Universe Rank | Signal |
|---|---|---|---|
| **Value** | Deeply negative composite. P/E n.m. (**−558.8x**, net loss), P/B **62.7x**, EV/EBITDA **2,506x** (EV $50.2B ÷ LTM EBITDA $20.1M), P/FCF **869x** | **Bottom quintile.** Not in ranked top-25; multiples are far worse than the worst listed name (TSLA −363.4) | **Strong Sell** |
| **Momentum** | **+96% 12-1** (own calc: $113.28 → $222.30); but **−18.7% 6-mo**, **−26.8% 1-mo**, **−41.3%** off 6/22 high. Tool output (0.84% / −8.58%) is internally inconsistent — see flags | ~**16–25 of 25** (absent from momentum top-15) | **Neutral → Sell** (reversing) |
| **Quality** | ROE **−11.2%**, ROA −2.0%, ROIC **+1.9%**, GP/Assets 0.134, accruals **−0.046** (good), Piotroski **F = 4/9** | **Bottom quintile** — below lowest listed (TSLA 4.58) | **Sell** |
| **Low Vol** | Vol **112.9%**, beta **4.29**, max DD **−52.7%**, Sharpe 0.78 | **Bottom decile** — highest-risk decile of any screen | **Strong Sell** |
| **Earnings Revision** | Median PT **$260** vs $203 (+28%); 6 of 10 PTs raised in last 2 wks. Tool's "+23.41% upgrade" is an **artifact** (compares 2030 $13.78 to 2029 $11.16 — different fiscal years, not a revision) | n/a | **Neutral / mildly positive** |

---

## 2. Price Statistics

| Metric | 252-day | 126-day |
|---|---|---|
| Annualised return | **+114.3%** | **−65.4%** |
| Annualised volatility | 112.5% | 112.8% |
| **Alpha (ann., vs SPY)** | **+24.3%** | **−35.3%** |
| **Beta** | **4.313** (SE ≈ ±0.42, t ≈ 10.4) | **4.669** |
| R² | **0.302** | 0.352 |
| **Sharpe** | **1.016** | **−0.579** |
| **Sortino** | **1.769** | **−0.970** |
| Max drawdown | **−52.65%** ($345.85 6/22 → $163.75 7/29) | — |

**52-week range:** $76.97 (12/17/25) – $345.85 (6/22/26). Current $203.17 = **46.9th percentile of range**; +164% off low, −41.3% off high.

**Correlations (252d):** GEV **0.60**, ETN **0.57**, SPY **0.55** — BE is the high-beta expression of the AI/datacenter power complex.

**Significance notes:** Beta is significantly >1 (t≈10.4), but R²=0.30 means **70% of variance is idiosyncratic** — market-hedging BE with SPY leaves most risk on the table. The 252d alpha (+24.3%, SE ≈ 6–7%) is nominally significant (t≈3.5) but **flips to −35.3% over 126d** — alpha is regime-dependent, not a stable characteristic. Cross-sectional ranks rest on a **25-name mega-cap universe** (only ~10 true Industrials) — too small for reliable sector percentiles.

---

## 3. Composite Quant Signal: **SELL**

Bottom quintile on **value, quality, and low-volatility simultaneously** — a textbook short-side quant profile. Tempering it to Sell (not Strong Sell): 12-1 momentum is genuinely positive (+96%), accruals are negative four years running, and sell-side targets are being raised. Nothing in the data supports the current multiple.

Weighted: Value 30% (Strong Sell) · Momentum 25% (Neutral/Sell) · Quality 25% (Sell) · Low Vol 10% (Strong Sell) · Revision 10% (Neutral) → **Sell**.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal in progress (highest conviction).** 12-1 momentum +96% but 6-mo −18.7% and 1-mo −26.8%. This is the classic *momentum-crash* signature: a crowded high-beta winner turning over. Rebound of +5.1% in the final week on 36M/21M share volume (vs ~13M avg) looks like distribution, not accumulation.
2. **Beta instability / asymmetry.** Beta 4.31 (252d) vs 4.67 (126d) vs 3.64 (profile). At β≈4.5, a −10% SPY drawdown implies ≈−45% on BE. R² of 0.30 means the 4.5x is a poor hedge ratio.
3. **Factor crowding.** 0.60 correlation with GEV (β ~1.5) and 0.57 with ETN. BE is the levered leg of a very consensus theme; theme unwinds hit BE ~3x harder than the peer group.
4. **No valuation anchor.** EV/EBITDA of 2,506x on $20M of LTM EBITDA. Even the *nearest* consensus year (2027 EPS $5.34) gives a **38x** forward P/E; it is only "cheap" on **2030** ($13.78 → 14.7x), which requires revenue to compound from $2.02B (2025A) to **$15.57B** — 7.7x — with flawless margin expansion. Discount-rate sensitivity is extreme.
5. **Interest coverage & dilution.** EBIT −$30.5M vs interest expense $53.9M — EBIT does not cover interest. Diluted shares 227.4M → 240.4M (+5.7% y/y); Piotroski F7 (no dilution) = 0, F5 (lower leverage) = 0.
6. **Liquidity is NOT a risk.** ADV ≈ 13M shares ≈ **$2.6B/day**; institutional-size positions are easily exited. This is the one risk factor that scores well.
7. **Data-integrity flags (verify before publishing):**
   - `momentum_return_pct` of **0.84%** (252d) and **−8.58%** (126d) cannot be reconciled with the OHLCV series (+96% and −18.7%). Momentum factor likely defective — I used computed values.
   - `earnings_revision` +23.41% compares 2030 EPS to 2029 EPS (levels across fiscal years), **not** a revision of one period.
   - Share-count conflict: 240.4M (valuation module, $49.7B mkt cap) vs ~295M implied by profile's $61.1B. Verify before quoting either.
   - Only 13–16 analysts cover the long-dated EPS years; 2029/2030 consensus is thin.

**Genuine positives worth carrying forward:** accruals ratio −0.046 (cash earnings exceed accounting earnings, 4 consecutive years), operating cash flow +$114M, gross margin 29.0% up from 14.8% in 2023, revenue +37% y/y. The business is improving — the *price* has run far ahead of it.

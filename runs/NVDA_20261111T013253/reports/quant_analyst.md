# Quant Analyst

- Symbol: NVDA
- Elapsed: 58.5s

---
## NVIDIA (NVDA) — Quantitative Factor Report
**Price $168.89 | Mkt Cap ~$4.07T | Sector: Technology / Semiconductors | Fiscal year ends late Jan**

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 34.5x · P/B 26.3x · EV/EBITDA 28.3x · P/FCF 42.8x · FCF yield 2.3% | **10 / 25** (median) | **Neutral** — expensive on trailing, cheap on forward |
| **Momentum (12-1)** | **+10.71%** | **6 / 25** (top quartile) | **Neutral** — positive 12-1 but reversing violently |
| **Quality** | ROE 76.3% · ROIC 77.3% · GP/Assets 0.742 | **3 / 25** (top decile) | **Positive (caveat: accruals)** |
| **Low Vol** | Vol 40.6% · β 1.79 · Max DD 29.4% | **3 / 10** semis peers | **Negative** — high vol/beta in absolute terms |
| **Earnings Revision** | **+29.65%** (FY2031 EPS $25.60 → $33.19) | n/a (n=10 analysts) | **Positive but LOW confidence** |

**Piotroski F-Score: 5/9 (Moderate).** Fails on ROA improvement, accruals quality, gross-margin improvement, and asset-turnover improvement — a coherent "growth deceleration" cluster.

**Accruals ratio 8.39% (warning):** net income $120.07B vs operating CF $102.72B — a $17.4B gap. Trend is deteriorating: 2.54% (FY24) → 7.88% (FY25) → 8.39% (FY26). This is why the quality engine tags the signal "low" despite a 76% ROE. Working-capital build (inventory/receivables) is absorbing earnings.

---

### 2. Price Statistics (252-day window)

| Metric | Value |
|---|---|
| Beta vs SPY | **1.789** (252d daily) — profile shows 2.216 5-yr |
| Alpha (annualised) | **−24.90%** |
| R² vs SPY | 0.406 (59% idiosyncratic) |
| Sharpe | **−0.136** |
| Sortino | **−0.205** |
| Annualised return | −5.42% |
| Annualised vol | 39.9% (40.6% alt calc) |
| **Max drawdown** | **−29.41% — and it is LIVE** |

**The drawdown is not historical — it is current.** Peak $239.24 (6-Oct-26) → $168.89 (10-Nov-26) = **−29.4%**, and the stock is sitting at its 12-month low. Recent returns: 1M **−26.3%**, 3M **−22.3%**, 12M **−14.9%**. The 10-Nov decline came on 426M shares and 9-Nov on 463M — roughly **3x** the ~120–180M typical volume. High-volume breakdown with no confirmed reversal signal.

**Statistical significance flags:**
- The −24.9% alpha has a standard error of ≈31.3% (residual vol 31.3%, n=252) → **t ≈ −0.80, NOT significant.** One year of data cannot distinguish this alpha from zero. Directionally damning, statistically unproven.
- Sortino (−0.205) is worse than Sharpe (−0.136), implying downside deviation (26.4%) is *below* total vol (39.9%) — i.e. the trailing year was positively skewed overall and the Nov crash is a fresh event not yet reflected in the downside-deviation term.
- 12-1 momentum is measured on data through ~9-Oct; the **entire 26% loss falls in the excluded final month.** The +10.71% headline is stale by one month.

---

### 3. The Value Paradox (most important cross-sectional finding)

Trailing multiples look rich; **forward multiples are not**, *if* estimates hold:

| Period | EPS Est | Fwd P/E @ $168.89 | EPS Growth |
|---|---|---|---|
| FY2026 (Jan-26) | $4.69 | 36.0x | — |
| FY2027 | $9.29 | **18.2x** | +97.9% |
| FY2028 | $15.81 | **10.7x** | +70.1% |
| FY2029 | $21.38 | 7.9x | +35.2% |
| FY2030 | $25.60 | 6.6x | +19.8% |
| FY2031 | $33.19 | 5.1x | +29.7% |

FY2027 carries 33 analysts with a very tight range ($9.00–$9.70, ±4%) — that estimate is credible. FY2031 carries only 10 analysts with a range of $23.82–$38.80 (±23%) — **that is the period the +29.65% revision score is computed on, the noisiest data in the set.** Treat the revision signal as weak evidence.

**Countervailing signal:** the two most recent analyst actions (9–10 Nov 2026) were *price-target cuts* to $250 (Mizuho) and $300 (Wells Fargo). Median target across the last 10 notes is **$300** (+77.6% vs spot), but the *direction* of revision has turned down even as the long-dated EPS revision score reads positive. I weight the target cuts more heavily — they are dated and near-term.

---

### 4. Composite Quant Signal: **NEUTRAL**

The factors genuinely conflict, and I will not paper over it:

- **Cross-sectional composite: attractive.** Averaging the three rankable factors (momentum 76th pct, quality 88th pct, value 60th pct) gives a **~75th percentile** score — top quartile. On a pure factor-screen basis, this is a Buy.
- **Time-series/risk composite: poor.** Negative alpha, negative Sharpe, negative Sortino, β 1.79, at a 12-month low inside a live 29% drawdown on 3x volume.
- **Overlay that breaks the tie:** the top-quartile momentum rank is an artifact of the 21-day exclusion window. Strip that and the trend is down.

**Net: Neutral.** Quality is real and top-decile; valuation is defensible on FY2027. But you are catching a falling knife — no price-based evidence of a bottom, and the accruals trend undermines the quality case.

---

### 5. Key Quant Risk Flags

1. **Momentum reversal risk — HIGH.** +10.71% 12-1 masks −26.3% in the last month. Classic momentum-crash signature (high-beta, high-momentum names reverse hardest). Rank-6 momentum is a stale signal.
2. **Factor crowding — HIGH.** Mega-cap AI/semis is the most crowded trade in the universe; β 1.79 vs SPY with R² of only 0.41 means large idiosyncratic drawdowns that diversification will not offset.
3. **Earnings-quality decay — MEDIUM-HIGH.** Accruals 8.4% and rising three years running; Piotroski fails on accruals, ROA trend, gross margin, and asset turnover. ROIC has fallen 90.9% → 77.3%.
4. **Estimate-revision fragility — MEDIUM.** The bullish revision score rests on FY2031 (n=10, ±23% range). Near-term targets were cut in the last two weeks.
5. **Liquidity risk — LOW.** ~$4T cap, 100M+ ADV. Not a concern.
6. **Sample-size caveats:** the ranking universe is only **25 symbols**, so "sector rank" is really rank among mega-caps, not the true semiconductor universe — ranks are indicative, not precise. Alpha t-stat ≈ −0.80 is insignificant.

**What would change the call to Buy:** a confirmed reversal (close back above the ~$200 level on normalising volume) combined with the Nov target cuts proving to be one-offs. **What would confirm Sell:** accruals breaching 10% or FY2027 EPS estimates moving below ~$8.50.

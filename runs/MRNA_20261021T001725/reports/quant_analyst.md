# Quant Analyst

- Symbol: MRNA
- Elapsed: 109.8s

---
## MRNA (Moderna, Inc.) — Quantitative Factor Report
**Sector:** Healthcare / Biotechnology · **Price (2026-01-30 close):** $44.07 · **Shares:** ~389M · **Mkt cap:** ~$17.2B

### ⚠️ First: a material data-integrity finding

Three of the factor tools returned values that are **arithmetically irreconcilable with the raw price series**. Verified against daily OHLCV:

| Metric | Tool output | Recomputed from raw series | Verdict |
|---|---|---|---|
| 12-1 momentum | **+172.4%** | **−25.2%** (29.49 vs 39.42) | Wrong sign |
| Annualized return | **+339.8%** | **+11.8%** geometric (39.42→44.07) | ~29x overstated |
| Annualized vol | **217.1%** | **~62%** | ~3.5x overstated |
| Max drawdown | **−34.2%** | **−48.0%** close-to-close | Understated |
| Beta vs SPY | **2.14** | **0.95** | Overstated 2.3x |
| Alpha | **+354.5%** (R²=0.017) | **+12.3%** (R²=0.027) | Overstated ~29x |
| Profile price / mkt cap | $242.08 / $96.6B | $44.07 / ~$17.2B | ~5.5x overstated |

The ~5.5x price distortion almost certainly comes from a **series splice**, and a single spurious jump of that size is exactly what manufactures a fake +450% return, a 217% vol, and a spurious max-drawdown figure. Peer checks confirm the engine *itself* works (VRTX 29.5% vol, BNTX 50.8% vol — both plausible); **MRNA's series is the specific problem.** All figures below use my recomputation. The valuation tool's negative multiples (P/E −33.3, EV/EBITDA −35.4) are computed on the bad $242 price; on the real price, **P/B ≈ 2.0x** (equity ~$8.65B implied from ROE/ROA).

### 1. Factor Scores Table

| Factor | Score (raw) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E −33.3, EV/EBITDA −35.4, P/FCF −8.3x on real mkt cap; **P/B 1.98x** | **Bottom quintile** (5/5) | **Sell** — no positive earnings/FCF to value; only book is "cheap," and book is being burned |
| **Momentum** | **12-1 = −25.2%**; 12-mo +11.8% vs SPY +16.3%; 1-mo **+49.4%** | **Bottom quintile** (5/5) | **Sell** — but 1-month thrust is contradicting it (see flags) |
| **Quality** | ROE −32.6%, ROIC −29.1%, GP/assets 8.7%, F-score 3/9, accruals −7.7% | **Bottom quintile** (5/5) | **Sell** — VRTX (ROE +21.2%, F-score strong) vs BNTX (−5.7%) bracket it; MRNA is worst |
| **Low Vol** | σ 62% (vs VRTX 29.5%, BNTX 50.8%), **β 0.95, R² 2.7%** | **Bottom quintile** (5/5) | **Sell** — market-like beta, but 97% of risk is idiosyncratic |
| **Earnings Revision** | Tool: +595.3% "upgrade" | **Not meaningful** | **No signal** — see below |

**The +595% revision "upgrade" is a false positive.** The tool compared the **FY2030** estimate ($3.4174) against the **FY2029** estimate ($0.4915) — not the same forward period 3 months apart, as the methodology requires. The +595% simply reflects the modeled loss-to-profit crossover between two different years. The actual consensus path is deteriorating near-term:

| FY | 2026E | 2027E | 2028E | 2029E | 2030E |
|---|---|---|---|---|---|
| EPS est. | **−8.31** | −4.75 | −2.74 | +0.49 | +3.42 |
| Revenue est. ($B) | 2.10 | 2.43 | 3.42 | 5.57 | 7.56 |
| # analysts | 17 | 17 | 15 | 9 | 6 |

FY2026 consensus EPS of **−$8.31 is worse than FY2025's actual −$7.26**, on revenue growth of only +8% ($1.94B → $2.10B). Analyst coverage thins from 17 to 6 by FY2030 — the long-dated numbers carry no statistical weight. **Near-term revisions are negative, not positive.**

### 2. Price Statistics (12 months to 2026-01-30)

| Metric | Value | Note |
|---|---|---|
| Realized return (geometric) | **+11.8%** | vs SPY **+16.3%** → **−4.5pts underperformance** |
| Annualized return (arithmetic monthly mean) | +27.3% | Distorted by a single +49.4% Jan-2026 month |
| Annualized volatility | **~62%** | σ_monthly 18.2% × √12; n=12, small sample |
| **Beta vs SPY** | **0.95** | Monthly regression, n=12 |
| **Alpha (annualized)** | **+12.3%** | t ≈ **0.18** → not significant |
| **R² vs SPY** | **2.7%** | 97% of variance is idiosyncratic |
| Correlation vs SPY | ~0.17 | Effectively uncorrelated |
| **Sharpe** | **0.43** (arith.) / **0.19** (geometric) | 0% rf assumed |
| **Sortino** | **0.89** | Downside dev 30.7% annualized, zero target |
| **Max drawdown** | **−48.0%** | Close-to-close, 2025-01-07 (47.53) → 2025-04-17 (24.72); intraday −52.7% |

**A critical measurement caveat:** the positive alpha is an artifact of averaging. SPY beat MRNA by 4.5 points point-to-point, yet the arithmetic monthly mean shows +1.0%/mo alpha purely because compounding is asymmetric and one +49.4% month dominates a 12-observation sample. **Treat alpha as zero, not +12%.** With t = 0.18 and R² = 2.7%, beta is likewise statistically indistinguishable from 0, 1, or 2 — the market explains essentially none of this stock's return, so "beta 0.95" should not be used for cost-of-equity or hedging work.

### 3. Composite Quant Signal: **SELL**

Bottom-quintile on **all four** classical factors (value, momentum, quality, low-vol) — the mirror image of the rare top-quintile-sweep that earns a Strong Buy. Fundamentals corroborate: FY2025 revenue $1.944B (**−39% YoY**, from $6.85B in FY2023 and $18.9B in FY2022), net loss −$2.822B, EPS −$7.26, **FCF −$2.065B**. The FY2022 ROIC of +46.4% is now −29.1%.

Not a **Strong Sell** for three quantified reasons: (1) accruals ratio is **−7.7%**, i.e. losses overstate cash burn quality-wise (OCF −$1.87B is better than net income −$2.82B); (2) gross margin *improved* to 55.3% from 54.2%, one of the three F-score points earned; (3) the +49.4% one-month move and −25% twelve-month momentum are in direct conflict, which is a classic setup for a **momentum reversal** in either direction rather than a clean continuation.

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — two-sided and acute.** 12-1 momentum at −25% says downtrend; the last month at +49.4% (Jan 2026, $29.49 → $44.07) says inflection. Whichever factor model you run, **you are on the wrong side of one of them.** Factor crowding risk is low (this name is a liquid large-cap, ~11M shares/day average, so no liquidity constraint), but signal conflict is at a maximum.
2. **Idiosyncratic risk is ~97% of total return variance.** R² of 2.7% vs SPY means hedging, factor exposure, or market-neutral construction gives essentially no protection. Position sizing must be done on 62% vol, not on beta.
3. **Capital-raise / dilution risk is the dominant quant hazard.** ~$8.65B equity against −$2.07B annual FCF implies roughly **4 years of runway** before external financing, absent a revenue inflection. F-score component F7 (no dilution) already fails, and FY2025 SBC of $483M adds non-cash dilution on top. This is the single largest driver of tail risk and makes the −48% drawdown repeatable.
4. **Estimate-revision signal is unusable as delivered.** Any model consuming the tool's +595% "upgrade" will generate a spurious bullish tilt. Near-term consensus (FY2026 EPS −8.31 vs −7.26 actual) points the other way.
5. **Sample-size limits.** Beta/alpha/Sharpe rest on **12 monthly observations** — well below the ~36 months needed for significance. Volatility is estimated with wide error bars. The daily-vol tool's own 217% figure

# Quant Analyst

- Symbol: EFX
- Elapsed: 123.9s

---
# EFX (Equifax Inc.) — Quantitative Factor Report
**Price $176.54 | Mkt cap ~$20.7bn | Industrials / Consulting & Information Services | Data as of 2026-10-20**

Peer set: I overrode the tool's sector list (which returned aerospace/rail/machinery mega-caps — not comparables for a credit bureau). Ranks below are against 5-name information-services comps: **SPGI, MCO, VRSK, TRU**. n=5 is a *minimum* for ranking; treat ranks as indicative, not statistically robust.

---

## 1. Factor Scores Table

| Factor | Raw Score | Sector Rank (of 5) | Signal |
|---|---|---|---|
| **Value** | P/E 33.2 · EV/EBITDA 14.4 · P/FCF 19.3 · P/B 4.6 | **2** (73rd pct) | **Bullish** |
| **Momentum** | 12-1 return **−7.16%** | **4** (20th pct) | **Bearish** |
| **Quality** | ROE 13.9% · GP/A 0.289 · Accruals **−8.05%** | **3** (60th pct) | Neutral |
| **Low Vol** | Vol **44.0%** · Beta 0.59 · MaxDD **−37.5%** | **4** (30th pct) | **Bearish** |
| **Earnings Revision** | FY30 EPS +1.86% (n=2 analysts) | **3** (~50th pct) | Neutral — *low confidence* |

**Value detail (EFX is cheapest on cash flow):** P/FCF 19.3 is the lowest in the peer group (SPGI 24.5, MCO 33.2, VRSK 22.3, TRU 23.3); EV/EBITDA 14.4 is 2nd cheapest (TRU 13.5). Only on P/E (33.2) is EFX mid-pack behind VRSK 29.4 and SPGI 29.9. **Critical overlay:** on FY26 consensus EPS of $8.50, forward P/E is **20.8x**, and on FY27 ($9.84) **17.9x** — a ~40% discount to its own trailing multiple. The value factor looks materially better than the trailing screens imply.

**Quality detail:** Four-year ROIC trend is *improving*: 8.98% (2023) → 10.49% (2024) → **11.14% (2025)**; ROE 11.6% → 12.3% → 13.9%. Accruals of **−8.05%** (net income $660m vs OCF $1,616m — cash conversion 2.4x) is the second-best in the group and is genuinely high-quality; the model's "low" quality label is driven by ROE/GP-A percentile, not by earnings quality. Piotroski **F-Score 7/9** (fails F5 leverage, F6 equity change — D&A is climbing as tech migration spend amortizes). EBITDA margin expanded 30.0%→30.3%→30.8%.

**Revision detail — flag:** the tool compared **FY2030** estimates (13.00 vs 12.76, +1.86%) using only **2–3 analysts**. That is not a usable revision signal. The more informative reads: FY25→FY26 EPS +11.5%, FY26→FY27 +15.8%; but sell-side **price targets have been cut relentlessly** — Barclays 200→155, Goldman 199→171→148→169, RBC 194→177, Mizuho 210→185. Median of 10 recent targets ≈ **$174 vs $176.54 spot = ~0% upside**. Revisions on the tape are negative even though the EPS ladder is rising.

---

## 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY, 252d) | **−27.5%** |
| Beta (vs SPY) | **0.588** |
| R² | **0.031** |
| Annualised vol | **43.97%** |
| Max drawdown | **−37.52%** |
| Sharpe (0% rf) | **−0.307** |
| Sortino | **−0.429** |
| Annualised return | −13.57% |
| Downside deviation (implied) | ~31.6% (71.6% of total vol) |
| Sortino/Sharpe ratio | 1.40 |

**Statistical warnings — these numbers are weaker than they look:**
- **Alpha is not significant.** R² = 0.031 means 97% of EFX's variance is unexplained by the market. With ~1 year of data, the standard error on annualised alpha ≈ residual vol ≈ **43.5%**, giving **t ≈ −0.63**. A −27.5% alpha is statistically indistinguishable from zero. Do not present it as evidence of skill or of destruction.
- **Beta t-stat ≈ 2.8 (significant) but unstable.** The 252-day estimate of 0.59 contradicts the 2-year profile beta of **1.341** and the peer read (TRU 0.92, MCO 0.54, SPGI 0.41). EFX's correlation to SPY is only **0.174** — extraordinarily low for a $20bn S&P constituent. Treat 0.59 as a low-confidence point estimate; true sensitivity is likely higher.
- **Sharpe is not distinguishable from zero.** SE of a 1-year Sharpe ≈ 1.0, so −0.31 carries no weight. Two tools disagree (−0.307 vs −0.425) because of mean-daily vs cumulative-return methodology; report the range, not a point.
- **Sortino is more negative than Sharpe** — correct arithmetic (downside dev < total vol), but it means the pain is concentrated in a few violent down-legs rather than diffuse volatility.

**Price path context (this is the most important qualitative caveat):** EFX closed at **$137.24 on 2026-09-30** — a ~41% drawdown from the late-2025 closing high of $231.15 — then rallied **+28.6% off the low in 14 sessions**, including a **+11.4% single-day gap on 2026-10-20** on 4.0m shares. The 12-1 momentum score (−7.16%) deliberately excludes the last 21 trading days, so it **entirely misses this reversal**. Realized vol/Sharpe/alpha are also likely computed through the prior session and therefore stale. YTD 2026: −17.9%; 2-year: ~−38%.

---

## 3. Composite Quant Signal: **NEUTRAL** (upgrade-bias; trend still Sell)

Equal-weighted percentile composite: (73 + 60 + 20 + 30 + 50) / 5 ≈ **47th percentile**.

The setup is a genuine cross-current: **cheap on cash flow (2nd of 5) + improving ROIC + excellent accruals** against **worst-in-class momentum (4th of 5), highest volatility, deepest drawdown, and ~zero analyst target upside**. No factor pair (value + quality + momentum) confirms — the classic "top-quintile on all three" screen fails decisively on momentum. Note that all five peers have *negative* 12-1 momentum (SPGI −7.9%, VRSK −11.0%, TRU −5.6%, MCO −5.1%) — this is a **sector-wide de-rating, not idiosyncratic weakness**, which makes EFX's own rank less damning but does not create a buy signal.

What would flip this to Buy: sustained 1–3 month momentum above ~$195 (reclaiming the Jan-2026 high), which would also validate the Oct-20 gap.

---

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (two-sided).** 12-1 momentum is negative *and* the stock has just gapped +28.6% off a 41% drawdown. Either the reversal continues (positive) or it is a dead-cat bounce inside a two-year downtrend (negative). The factor model is structurally blind to this — the last 21 days are excluded by construction. Highest-conviction watch item.
2. **Alpha estimate is noise.** t ≈ −0.63, R² = 0.031. Any memo statement citing "−27.5% alpha" must carry the significance caveat.
3. **Beta instability / near-zero market correlation (ρ = 0.174).** 0.59 (1-yr) vs 1.341 (profile). Poor hedge, poor benchmark-relative risk model; 97% idiosyncratic variance means position sizing should be driven by the 44% vol, not by a market-beta overlay.
4. **Factor crowding in the comp group.** EFX–TRU correlation is **0.859**, highest in the peer matrix, and 0.53–0.60 vs SPGI/MCO/VRSK. An EFX position is largely a bet on the whole credit-bureau complex; do not size alongside TRU/SPGI as if diversified.
5. **Highest volatility, deepest drawdown in the peer group.** 44.0% vol vs MCO 29.7% / SPGI 34.5% / VRSK 37.9%; −37.5% max drawdown vs MCO −23.6%. On a risk-adjusted basis EFX is the worst or second-worst name in the comp set (Sharpe −0.31 vs TRU −0.01, MCO −0.34).
6. **Estimate revision signal is underpowered** (FY2030, n=2). Do not act on the +1.86%; the actionable evidence is the target-price cut cluster (median $174 ≈ spot).
7. **Liquidity is adequate** — 1.0–4.0m shares/day, $20.7bn cap. Not a constraint.
8. **Sample-size caveat across the board:** 252 trading days ≈ one observation year. All risk-adjusted ratios, alpha, and beta have standard errors too wide to support a Strong Buy/Strong Sell call. Any conviction must rest on the valuation/quality spreads, not the return statistics.

**Bottom line:** Value and cash-based quality say "cheap and improving"; momentum, volatility, and the analyst tape say "don't catch it yet." Neutral, with the forward P/E of 20.8x (FY26) the single most compelling number in the analysis and the 12-1 momentum trough the single biggest impediment.

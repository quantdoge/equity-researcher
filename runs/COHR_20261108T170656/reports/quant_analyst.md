# Quant Analyst

- Symbol: COHR
- Elapsed: 73.3s

---
## COHR — Quantitative Factor Report
**Coherent Corp. | Technology / Hardware | Price $192.81 | Mkt cap $37.7B**

⚠️ **Data note first:** the analyst-target feed reveals published prices through **Nov 2026** (price-when-posted $195.09, with the stock at $368.65 as recently as Jul-2026). So "today" is ~Nov 2026, the stock is **~48% below its Jul-2026 high**, and FY2026 (Jun-26 fiscal year-end) is *actual*, not estimated. My price slice ended Feb-2026, so I could not independently verify the 12-month return/Sharpe inputs — flagged where it matters.

---

### 1. Factor Scores Table

| Factor | Score | Sector Rank* | Signal |
|---|---|---|---|
| **Value** | P/E 46.8 · P/B 3.35 · EV/EBITDA 25.2 · **P/FCF −36.6** | 4 / 6 | **Weak** |
| **Momentum** | 12-1 = **+25.5%** · 6-mo = +18.2% | 3 / 6 | **Neutral-positive** |
| **Quality** | ROE 7.2% · GP/A 0.146 · Accruals **+0.0396** · F-score **6/9** | 5 / 6 | **Weak** |
| **Low Vol** | Vol **95.5%** · Beta **3.47** · Max DD **−60.2%** | 6 / 6 | **Very Weak (worst)** |
| **Earnings Revision** | +18.69% (see caveat) | 2 / 6 | **Positive — low confidence** |

\*Ranks are against a hand-built 6-name optical/photonics comp set (COHR, LITE, FN, IPGP, MTSI, AVGO). The platform's "Technology sector" peers are all mega-caps (AAPL, NVDA, MSFT) and are not valid comparables. **n=6 is too small for statistical significance — treat ranks as directional only.**

**Peer detail used for ranks:**

| | P/E | EV/EBITDA | ROE | GP/A | Accruals | 12-1 Mom |
|---|---|---|---|---|---|---|
| COHR | 46.8 | 25.2 | 7.2% | 0.146 | **+0.040** | +25.5% |
| LITE | neg | neg | −149% | 0.172 | −1.052 | +59.2% |
| FN | 25.1 | 17.6 | 19.3% | 0.142 | +0.055 | +10.7% |
| IPGP | 89.5 | 17.5 | 1.5% | 0.157 | −0.018 | −7.8% |
| MTSI | 49.0 | 34.9 | 19.8% | 0.332 | −0.009 | +32.7% |
| AVGO | 61.6 | 42.5 | 28.5% | 0.253 | −0.026 | −6.6% |

---

### 2. Price Statistics

| Metric | Value |
|---|---|
| Alpha (annualised, vs SPY) | **−1.54%** |
| Beta (vs SPY) | **3.49** (regression) / 3.47 (vol model) |
| R² | **0.269** — 73% idiosyncratic |
| Sharpe | **0.155** |
| Sortino | **0.244** (Sortino/Sharpe 1.57 — downside vol contained) |
| Annualised return | 14.78% |
| Annualised volatility | **95.5%** |
| Max drawdown | **−60.2%** |
| Return on capital trend | ROIC 6.1% → 4.4% → 1.0% → 2.4% (FY26→FY23), i.e. **improving but still below cost of capital** |

**On alpha:** with 95.5% vol and R² of 0.27, the standard error on annualised alpha is roughly **±80pp**. A t-stat of ~0.02 means **alpha is statistically indistinguishable from zero** — the −1.54% is noise, not evidence of underperformance. Equally, no positive alpha can be claimed. This stock is a high-beta beta-delivery vehicle, not an alpha generator.

---

### 3. Composite Quant Signal: **NEUTRAL** (risk-adjusted tilt: negative)

The factor book is **internally contradictory**, and that is the honest read:

- **Momentum is the only positive factor (+25.5%, rank 3/6)** — but it is *stale* momentum. It is measured on a trailing 12-1 basis and is entirely backward-looking: the stock peaked near $368 in Jul-2026 and now sits at $193. The recent trend has decisively rolled over. This is **classic momentum-reversal risk**, and it is the single most important quant flag here.
- **Quality and low-vol are the worst in the comp set.** 95.5% vol, beta 3.47, −60% max drawdown is not a stock you can size meaningfully in a factor portfolio without accounting for the vol drag.
- **Value gives no support**: EV/EBITDA 25.2x is mid-pack for expensive optical, but **P/FCF of −36.6x means free cash flow is negative**. The factor cannot score this as cheap.
- **Risk-adjusted performance is poor**: Sharpe 0.155 and Sortino 0.244 mean you were paid ~15bp of return per unit of risk over 12 months. That is below cash-equivalent compensation for a 60% drawdown.

**The one genuinely bullish data point is forward-looking, and the value factor is blind to it:** consensus FY2027 EPS is **$9.81** vs FY2026 actual ~$4.12. On that basis the stock is **~19.7x forward FY2027** and **~12.8x FY2028 ($15.01)** — not expensive at all. But this is an aggressive ramp (+52% revenue, requiring material margin expansion) resting on 11 analysts for FY2027 and only 4 by FY2029. The market's 48% de-rating since July suggests the market is already discounting that ramp.

**Verdict: Neutral.** Positive trailing momentum and a cheap forward curve vs. the worst-in-class vol/quality/accruals profile. A quantitative case for an outright Buy is not supported; the numbers do not license an outright Sell either.

---

### 4. Key Quant Risk Flags

1. **🔴 EARNINGS QUALITY — SEVERE.** FY2026 net income of **$805M** against operating cash flow of only **$79.5M** — a $726M gap. Accruals ratio flipped from **−3.9% (FY25) and −4.8% (FY24)** to **+4.0% (FY26)**. Piotroski sub-score F4 (accruals quality) = **0 (fail at 0.05 risk)**. Prior years generated more cash than earnings; this year the earnings are not cash-backed. This is the strongest and most negative signal in the entire dataset, and it directly explains the negative P/FCF.
2. **🔴 MOMENTUM REVERSAL.** 12-1 momentum of +25.5% is measured to ~1 month ago and masks a ~48% drawdown from the Jul-2026 peak. Trend-following books get stopped out on crossovers like this, and the positive factor score will mechanically decay next month.
3. **🔴 DILUTION.** Piotroski F7 (no new shares issued) = **0 (fail)**. Diluted shares 195.4M are rising, so per-share growth understates net-income growth.
4. **🟠 VOLATILITY / FACTOR CROWDING.** 95.5% annualised vol with beta 3.47 and 73% idiosyncratic variance. In any risk-off tape COHR is a 3.5x-amplified short. Also a crowded AI-optics trade — correlations within the optical complex (LITE, FN, MTSI) are high, so "diversifying" across these names provides little risk reduction.
5. **🟠 ESTIMATE REVISION DATA IS UNRELIABLE.** The +18.69% headline compares the **FY2030** estimate ($25.21) to the **FY2029** estimate ($21.24) — different periods, not a like-for-like revision — and FY2030 carries **n=1 analyst**. This is a methodology artifact, not evidence of upward revision momentum. Corroboration is mixed: price targets were raised repeatedly through Aug-2026 ($371→$435, $375→$420, $290→$330, $170→$230) but **cut** as the stock broke ($425→$350, and Rosenblatt "lowered to $400"). Median PT ~$400 implies large upside, but PTs are lagged and converging down.
6. **🟡 LIQUIDITY — ADEQUATE, NOT A CONSTRAINT.** 5–13M shares/day on a $37.7B cap; no liquidity flag warranted. Note the recurring volume spikes (28.9M on 2025-08-14, 13.4M on 2026-02-04) coincide with the outsized gap moves.
7. **🟡 SMALL-SAMPLE CAVEAT.** Every "sector rank" above rests on 6 names. The alpha t-stat is insignificant, the revision score has n=1, and FY2030 EPS has n=1 analyst. Treat the composite as a qualitative synthesis, not a statistically robust factor rank.

---

**Bottom line:** Long-run ROIC improvement (1.0% → 6.1%) is real and the forward EPS curve is steep, but **you are being asked to pay for it with 95% volatility, a negative FCF profile, deteriorating accruals, and dilution — with only stale momentum in support.** Composite: **Neutral**. Any re-rating must wait for the accruals gap to close and for cash conversion to confirm the earnings ramp.

# Quant Analyst

- Symbol: VRT
- Elapsed: 55.5s

---
## VRT — Quantitative Factor & Risk Report (Vertiv Holdings)
*Sector: Industrials / Electrical Equipment & Parts · Price used: $203.56 (close 2026‑10‑20) · Mkt cap ~$93.5B*

**⚠️ Data integrity flag first:** the profile/valuation feed returned a reference price of **$242.94**, but the price history and analyst-target "price when posted" data both confirm the live price is **$203.56**. The reference price is ~19% stale, so trailing multiples below are shown **as-reported** and **stale-price-adjusted (×0.838)**. Everything else uses market data through 2026‑10‑20.

---

### 1. Factor Scores Table

Peer set for rank = purest electrical/data-center comps (ETN, TT, PH, GEV); ranks are of 5. Values shown are VRT's.

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 71.2 (adj **59.7**); EV/EBITDA 45.1 (adj **37.8**); P/FCF 50.3 (adj **42.1**); P/B 24.1 (adj 20.2); div yield 0.1% | **4 of 5** (bottom quintile) | **Negative** |
| **Momentum** | 12‑1 return **−20.7%**; 6M −5.6% | **5 of 5** (worst) | **Strong negative** |
| **Quality** | ROE 33.8%; GP/A 0.304; accruals **−0.064**; ROIC 26.5%; Piotroski 6/9 | **2 of 5** | **Positive** |
| **Low Vol** | 71.0% annualised vol; β 2.82 (SPY); max DD **48.3%** | **5 of 5** (highest risk) | **Strong negative** |
| **Earnings Revision** | FY2030 consensus EPS +13.7% vs 3M prior | n/a (n=4 analysts) | **Positive but low-confidence** |

**Peer comparison (the quantitative crux):**

| | P/E | EV/EBITDA | P/FCF | ROE | GP/A | 12‑1 Mom | Vol | Beta | Max DD |
|---|---|---|---|---|---|---|---|---|---|
| **VRT** | **71.2** | **45.1** | **50.3** | 33.8 | **0.304** | **−20.7%** | **71.0%** | **2.82** | **−48.3%** |
| ETN | 37.6 | 26.4 | 43.1 | 21.0 | 0.250 | +6.9% | 42.4% | 1.88 | −20.4% |
| GEV | 49.6 | 63.4 | 65.3 | 39.7 | 0.120 | −11.9% | 51.8% | 2.00 | −30.6% |
| TT | 34.6 | 24.5 | 35.7 | 33.9 | 0.360 | −3.6% | 30.7% | 1.22 | −16.1% |
| PH | 32.0 | 21.2 | 29.9 | 23.7 | 0.262 | −0.2% | 27.9% | 0.90 | −19.3% |

VRT is the **most expensive, the highest-beta/most volatile, has the deepest drawdown, and the worst momentum** in its comp group — but also the **best operating-quality profile after TT**. Every peer is trading at or near its drawdown with positive momentum. VRT is the only one still unwinding.

**Quality detail (the bull case, and it is real):** ROIC 4.7% → 17.8% → 24.8% → **26.5%** (2022→2025E), a genuine step-change in capital efficiency. Accruals have been negative four years running (FY2025 −6.4% of assets), CFO/NI = **1.59×** — earnings are cash-backed, not accounting-driven. F‑Score 6/9 is capped by a **failing F7 (share dilution)**, no gross-margin improvement, and no asset-turnover improvement. Growth is being bought partly with equity.

---

### 2. Price Statistics (252d, vs SPY)

| Metric | Value |
|---|---|
| Annualised return | **+61.4%** |
| Annualised volatility | **72.0%** |
| Beta (OLS) | **2.834** (profile β 2.048 — rising) |
| Alpha (annualised) | **+13.97%**, R² **0.268** |
| Sharpe | **0.85–0.95** (two engines) |
| Sortino | **1.32** |
| Max drawdown | **−48.3%** |
| Correlation: ETN / GEV / TT / PH / SPY | 0.75 / 0.61 / 0.57 / 0.41 / 0.51 |

Interpretation, precisely:
- **R² of 0.27 is the most important number here.** 73% of VRT's variance is idiosyncratic. This is not a market proxy — it is a single-theme bet. A 2.83 beta means a 1% SPY move maps to ~2.8% in VRT, and the *unexplained* 73% can move it further on its own.
- **The alpha is statistically present (t ≈ 3.5 nominal) but not stable.** It is measured over a window containing a +$379 peak and a −46% collapse. Annualised return of +61% and annualised vol of 72% describe the same fact: not an edge, a range.
- **Sortino (1.32) >> Sharpe (0.85–0.95)** means the return distribution here is hurt far more by variance than by downside deviation — i.e., the return was earned with violent, two-sided swings, not a clean drift. Sharpe/Sortino on 252d with vol this high is noisy; treat as directional only.
- **Momentum has broken down and is accelerating:** −19.6% in the last 13 sessions alone ($253.62 on 10/02 → $203.56 on 10/20); −30% from mid‑July ($291.60); −46.4% from the 5/14/26 high ($379.78). This is not a stalled trend, it is a live downtrend.

---

### 3. Composite Quant Signal: **NEUTRAL (tactical Sell)**

Equal-weight quintile composite: Value 2, Momentum 1, Quality 4, Low Vol 1, Revision 3.5 (discounted for thin data) → **2.3 / 5**.

This is an unusually conflicted profile: **the fundamentals are top-quintile and the tape is bottom-quintile.** Per the framework, when quality and price disagree, do not fight the momentum while the terminal multiple is still 38× EV/EBITDA and 42× FCF (adjusted). At **$203.56 the forward math is far better than trailing suggests** — FY26E EPS $6.91 → **29.5×**, FY27E $9.46 → **21.5×**, FY28E $11.93 → **17.1×**, on +31%/+21% revenue growth. Consensus PT median ≈ **$334 (+64%)**. So the *valuation case improves as the price falls* — but every PT in the record is being **cut** (MS $350→330, RBC $418→337, Baird $370→320). Revisions to targets are down even as revisions to EPS are up.

**Verdict:** do not add on the way down. Wait for 12‑1 momentum to stop making lower lows, or for the multiple to compress toward GEV/ETN on EV/EBITDA. The quality factor is a multi-year reason to own it; the momentum and low-vol factors are a 1–2 quarter reason to size it at zero-to-underweight today.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal — highest severity.** Worst 12‑1 in the comp group (−20.7%) with the decline steepening into October. No reversal signal yet.
2. **Factor crowding / thematic concentration.** r=0.75 with ETN, 0.61 with GEV. Any "AI data-center power" basket is effectively one risk factor; VRT is the high-beta expression of it. Position sizing must net these out, not stack them.
3. **Volatility/beta sizing.** 71–72% vol, β 2.8, R² 0.27, max DD −48.3%. A 1/3-sized position delivers full-market-like risk.
4. **Valuation risk if estimates slip.** 42× P/FCF (adj) embeds the +31% FY27 growth consensus. PEAD and revision data are supportive, but the margin for error is nil.
5. **⚠️ Earnings-revision signal is statistically weak.** The tool compared the **FY2030** EPS estimate ($16.24 vs $14.28) using **only 4 analysts**. That is not a revision signal, it is noise. The FY2026/2027 estimates (16–17 analysts) have no prior snapshot available in the feed — **the revision factor is effectively unmeasured here.** Treat it as neutral, not positive. FY2026 estimate range ($6.87–$6.96) is implausibly tight, another feed-quality concern.
6. **Dilution.** Piotroski F7 fails; share count rising alongside the growth story.
7. **Liquidity: NOT a flag.** ~$93.5B cap, 3–21M shares/day, tight spreads. Passes.
8. **Stale reference price in vendor feed** ($242.94 vs $203.56) — any screen run on that field is overstating VRT's multiples by ~19% and would rank it as less expensive than it is.

*Sample-size caveats: all price stats are 252 trading days — one year, one regime, no full-cycle test. Alpha/beta R² of 0.27 and annualised vol of 72% mean the alpha estimate should not be extrapolated. Revision factor has no usable sample. Factor ranks are against a 4-name hand-selected comp set, not the full Industrials sector (~700 names), so treat quintile labels as directional.*

# Quant Analyst

- Symbol: QXO
- Elapsed: 112.0s

---
## QXO, Inc. — Quantitative Factor & Risk Report
**Price: $11.97 (2026-11-25) · Mkt cap $7.34B · EV $8.89B · Sector: Industrials / Building Products Distribution**

⚠️ **Data note first.** My initial price pull was truncated at Feb-2026 ($25.54), which made the snapshot tools look stale. Re-pulled to present: latest close is **$11.97**, fully consistent with all ratio/return tools and with `price_when_posted` on the analyst notes. All figures below use $11.97.

---

### 1. Factor Scores Table

| Factor | Score (0–100) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | 28 | **3 / 3** | Negative (ex-book) |
| **Momentum** | 12 | **3 / 3** | Strongly Negative |
| **Quality** | 15 | **4 / 4** | Strongly Negative |
| **Low Vol** | 5 | **4 / 4** | Strongly Negative |
| **Earnings Revision** | 45 | 2 / 3 | Mixed / low-confidence |

Peer set = true distribution comps (**BLDR, GMS, WSO**), not FMP's default Industrials list (GE/RTX/CAT — invalid comps for a roofing distributor).

**Value — mixed, and the P/B is a trap.** P/B **0.76x** (BVPS $15.83) looks like deep asset value, but goodwill & intangibles are **$8.93B of $9.71B equity** → tangible book ≈ **$0.78B, ~$1.27/sh**, i.e. tangible P/B ≈ **9.4x**. On cash-flow multiples it is the *most expensive* name in the group: EV/EBITDA **34.3x** vs BLDR 8.9x, WSO 14.7x; P/FCF **40.1x** vs BLDR 8.0x, WSO 22.0x; P/E **–19.0x** (meaningless, loss-making). Trailing EBITDA ($259.5M) is post-merger-depressed — the 34x only normalizes to ~13.5x on FY26E EBITDA of $647M, which is a synergy-delivery bet, not a valuation fact.

**Momentum — negative on every horizon.** 12-1 momentum **–37.4%** (16.99 → 10.64); trailing 12m **–29.5%**; YTD-2026 **–38.0%**; peak-to-current **–55.8%** (27.07 → 11.97). Worst of the peer set (BLDR –17.4%, WSO –6.2%). **Counterpoint:** short-term reversal is live — **+12.5%** over the last month and **+18.0%** off the 2026-10-19 low of $10.14.

**Quality — weakest in the group, structurally.** ROE **–2.88%** (vs BLDR 10.0%, GMS 8.1%, WSO 15.4%); ROIC **–1.8%**; ROA **–1.76%**. Gross profit/assets **9.9%** vs 39–46% for peers — but this is largely acquisition accounting (assets inflated by Beacon goodwill), so it overstates the operational gap. One genuine positive: **accruals ratio –3.4%** (cash earnings exceed accounting earnings; operating CF +$261M vs net income –$279M). Piotroski **F-Score 4/9 (Weak)**: fails on ROA, leverage, dilution, and margin trends.

**Low Vol — the single worst factor.** Annualized vol **67.7%**, beta **2.44** vs SPY, **R² 0.34**, max drawdown **61.9%**. Beta is corroborated three ways (regression 2.45, low-vol engine 2.44, profile 2.36) — this is a high-beta, high-idiosyncratic-risk instrument, not a defensive distributor.

**Earnings Revision — the one "bullish" reading is not investable.** The engine reports **+36.0%**, but it compares the **FY2030** EPS estimate ($1.773 vs $1.304 prior) — a 4-year-out number from **5 analysts**. That is not revision momentum. The near-term tape says the opposite: 2026 price targets were cut repeatedly (Truist $26→$15, RBC $27→$18, Wells $18→$16→$15, D.A. Davidson $26→$20). Recent median PT **$17** (~+42% vs spot) — a wide, falling-target distribution, not an upgrade cycle.

---

### 2. Price Statistics

| Metric | 252-day | 126-day | Source reliability |
|---|---|---|---|
| Beta vs SPY | **2.45** | 2.36 | ✅ High (consistent across methods) |
| R² | 0.336 | 0.317 | ✅ High |
| Annualized vol | **68.6%** | 71.6% | ✅ High (reconciles to raw data) |
| Max drawdown | **–61.9%** | — | ✅ High (raw series: 27.07→10.14 = –62.5%) |
| Sharpe (rf=0) | **–0.94** | –0.62 | ⚠️ Return input unreliable |
| Sortino (rf=0) | **–1.88** | –1.25 | ⚠️ Return input unreliable |
| Alpha (ann.) | –100.0% | –48.8% | ❌ **Not reconcilable** |
| Annualized return | –64.3% | –44.5% | ❌ **Not reconcilable** |

**Flag — alpha and annualized return fail validation.** The provider's return/alpha series cannot be reproduced from the raw daily OHLCV: my price-derived trailing 12m return is **–29.5%**, not –64.3%. Volatility and max drawdown *do* reconcile, so the engine is sound on dispersion but its return series appears contaminated by QXO's pre-Oct-2024 price history (the 2024 meme-spike regime). **Treat alpha (–100%) as unusable; treat beta (2.4) as solid.**

**Return set I would actually defend (raw daily closes):** 12m **–29.5%** · 12-1 momentum **–37.4%** · YTD **–38.0%** · peak-to-trough **–62.5%** · 1-month **+12.5%** · since 2024-10-01 **–18.2%**.

**Sortino < Sharpe in both windows** (–1.88 vs –0.94) — downside deviation exceeds total deviation, i.e. a left-tail-dominated return distribution. Combined with 68% vol, this is a fat-left-tail profile, not merely a volatile one.

---

### 3. Composite Quant Signal: **SELL**

Weighted composite (Value 25%, Momentum 25%, Quality 25%, Low-Vol 10%, Revision 15%) = **21 / 100**.

Four of five factors are in the bottom quintile of their peer group and **no factor ranks in the top quintile** — the "value + momentum + quality" conjunction that would justify a contrarian Buy is entirely absent. The only quant-visible supports are the **negative accruals** (real cash generation), the **$0.78B tangible equity cushion**, and a **+18% short-term reversal** off the October low. These support "not a short," not "a buy." This is a **fundamental turnaround/synergy-execution bet that the quant framework cannot validate** — the 13.5x FY26E EBITDA only works if Beacon integration delivers.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal risk — two-sided.** 12-1 momentum is –37%, but the last month is +12.5%. Short-term reversal against a falling 12-month trend is the classic bear-market-rally pattern; expect whipsaw. Stop discipline matters more than usual at 68% vol.
2. **Left-tail dominance.** Sortino materially worse than Sharpe; a –62% realized drawdown in the last 12 months is the base rate, not the tail case.
3. **Beta 2.4 with R² only 0.34** — 66% of variance is idiosyncratic. Hedging with index shorts is inefficient here; single-name risk dominates.
4. **Factor crowding / style risk.** Deeply negative momentum + high beta + negative earnings is the archetypal *anti-quality, anti-momentum* short-crowd profile. Sharp squeezes on synergy or M&A headlines (the stock moved +9% on 2026-11-09 volume of 42M) are a live risk to any short position.
5. **Small-sample warning — genuine.** Beacon closed April 2025, so quality/fundamental factors cover **~7 months** of combined-entity operations (FY2025 is the first full year). Piotroski F=4 and ROIC=–1.8% are **not yet statistically meaningful** as steady-state measures. Only 5 analysts carry the FY2030 estimate.
6. **Goodwill impairment risk is the un-priced quant tail.** $8.93B goodwill against $9.71B equity and a 0.76x P/B means the market is already discounting ~24% of book. A write-down would not change cash flow but would invalidate the only "value" support in the model.
7. **Liquidity is adequate, not a constraint** — ~$55M/day notional at recent volumes (5–30M shares/day). No liquidity flag.

**Bottom line:** The numbers do not support the story. Value is book-only (and the book is goodwill), momentum is negative across every horizon, quality is last in its peer group, and volatility is the highest of any comparable. Composite **Sell**, with the caveat that the alpha figure in the provider feed is invalid and the quality factors rest on a thin 7-month post-merger sample.

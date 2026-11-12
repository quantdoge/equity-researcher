# Quant Analyst

- Symbol: NTES
- Elapsed: 48.7s

---
## NTES — Quantitative Factor Report
Price $123.18 (last close 2026‑01‑30: $126.30) · Mkt cap $79.5B · 645.6M ADS · Financials reported in **CNY**

---

### ⚠️ Data Integrity Flag (material — read first)
`calculate_valuation_ratios` divides a **USD** price by **CNY** per-share financials. It returns P/E of **2.36** and EV/EBITDA of **−1.88**; both are artifacts (check: $123.18 ÷ ¥52.25 = 2.36). Net income is ¥33.76B, not $33.76B. All multiples below are **recomputed by me at USD/CNY 7.10** and should be used instead of the tool output.

---

### 1. Factor Scores

| Factor | Score / Raw Value | Sector Rank (n=25) | Signal |
|---|---|---|---|
| **Value** | P/E **16.7x** (fwd 14.2x); ex‑net‑cash P/E **12.0x**; EV/EBITDA **9.4x**; P/B 3.4x; FCF yield **8.6%**; net cash = **28% of mkt cap**; EBIT/EV 10.1% | Not in top‑12 of 25 → bottom half of engine's universe | **Strong Buy** (cheap, cash‑backed) |
| **Momentum** | 12‑1 mo **+37.4%** (my calc from OHLCV); 12‑mo price **+50.6%** | Not in top‑12 | **Buy, decaying** — tool printed −0.38%, see below |
| **Quality** | ROIC **20.9%** (→14.3→18.7→19.1→20.9, 4yr uptrend); ROE 20.4%; GP/assets 0.327; accruals **−7.0%** (CFO ¥49.4B > NI ¥33.8B); F‑Score **8/9** | Not in top‑12 | **Strong Buy** |
| **Low Vol** | Ann. vol **34.3%**; beta 0.256 (1y) but **R² = 0.012**; mkt‑cap beta 0.766 | — | **Neutral** — low beta ≠ low risk |
| **Earnings Revision** | Tool: +12.29% "upgrade" — **invalid**, see below. Estimate ladder: 2026E ¥61.62 → 2027E ¥71.53 → 2028E ¥77.58 → 2029E ¥87.12 (**+12.2% CAGR**, 13 analysts) | — | **Mild Buy** (positive growth path, no true revision data) |

**Two more tool defects:** (a) the revision "3‑month prior" figure (¥77.582) is *identical* to the **2028E** consensus — it compared 2029E vs 2028E, i.e. one year of forecast growth, not a revision. (b) The value engine did not even surface NTES in a 25‑name universe top‑12 despite the fake 2.4x P/E, so that ranking is unreliable in both directions.

---

### 2. Price Statistics

| Metric | Value | Note |
|---|---|---|
| Alpha (ann., vs SPY) | **−0.73%** | R²=0.0116 → **statistically zero**, t‑stat ≈ 0.4 |
| Beta (1y daily) | **0.256** | Not usable; SE large given R²=1.2% |
| Beta (5y monthly, profile) | **0.766** | Prefer this for cost of equity |
| Sharpe | **0.33** | Tool's other calc printed 0.09 — inconsistent; 0.33 = 11.18/33.9 |
| Sortino | **0.525** | Downside vol ~21%; ratio only modestly better than Sharpe |
| Ann. vol | **34.3%** | High vol, near‑zero market correlation |
| Max drawdown | **−16.1%** (tool) / **−18.8%** peak‑to‑current | Peak $155.57 (2025‑09‑17) → $126.30 |
| Realized 12‑mo return | **+50.6%** | 83.85 → 126.30; conflicts with tool's 11.18% |

**Return series tension:** the tool's annualized return (11.18%) is irreconcilable with the raw OHLCV (+50.6% Jan‑to‑Jan, +27.5% over the trailing ~248 sessions). I trust the OHLCV; on that basis **realized Sharpe is far higher than 0.33**, but I will not publish a restated ratio without a clean return series. Treat 0.33 as a **lower bound**.

---

### 3. Composite Quant Signal: **BUY** (leaning strong on value + quality)

- **Value: 5/5 verdict.** 16.7x earnings for a 12%‑growth, 21% ROIC franchise with ¥160.7B net cash (28% of cap). EV/EBITDA 9.4x, FCF yield 8.6%, dividend covered 3.6x by FCF.
- **Quality: 5/5 verdict.** Cleanest earnings quality in the name: four straight years of negative accruals (CFO exceeds net income by ~46%), ROIC compounding upward, no dilution, leverage falling. F‑Score 8/9 (only asset‑turnover fails).
- **Momentum: 3/5.** Excellent 12‑month, but **−7.0% over 3 months and −8.3% over 1 month**, −18.8% off the September high. The trend is rolling over.
- **Revision: 2.5/5** on the evidence actually available.

Top‑quintile on value **and** quality simultaneously is the rare combination worth paying attention to; momentum is the only leg that fails.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal in progress** — 12‑1 looks great only because of the May 2025 (+15% in one day, 4.2M vol) and Sep 2025 run. Three consecutive months of decline and a lower‑high structure; the 12‑1 signal is stale and about to flip.
2. **Beta is a lie / factor diversification is not what it seems** — R² of 1.2% vs SPY means NTES carries **no** market beta hedge value; 34% vol is ~99% idiosyncratic. Do not size as a low‑beta defensive position. A 0.26 beta with 34% vol is the signature of China policy/ADR‑delisting/CNY event risk, not stability.
3. **Currency & ADR regime risk, not captured by any factor** — the same CNY/USD split that broke the multiple engine (−7% move on FX alone re-rates every metric) is unhedged in the factor scores. VIE/delisting tail risk sits outside all five factors.
4. **Sector rank is non‑computable.** The peer set returned is US mega‑cap semis/hardware (AAPL, NVDA, MSFT, AVGO) — not gaming or China internet. Any "Technology sector rank" for NTES is noise. Flagging rather than fabricating.
5. **Thin analytics universe (n=25)** — the ranking engine covers only 25 names; quintile claims are not statistically supportable.
6. **Liquidity adequate, not deep** — 0.14–1.9M ADS/day, occasional 4–5M spike days on news; ~$17–230M daily notional. Fine for most books, would matter at scale.
7. **Sample sizes:** 1y (252 daily obs) for alpha/beta is too short given R²=0.0116; revision signal rests on 4–13 analysts per horizon. Neither supports a high‑confidence factor call on its own.

**Bottom line:** the numbers support the value and quality case emphatically and contradict the low‑volatility and revision claims. Buy on fundamentals, but time entry — momentum is negative at the margin and the risk is country/regime, not valuation.

# Quant Analyst

- Symbol: INSM
- Elapsed: 42.9s

---
# INSM — Insmed Incorporated | Quantitative Factor Report
**As of 2026-11-20 · Price $146.99 · Mkt Cap ~$31.4B · Sector: Healthcare / Biotechnology**

---

## 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E n/m (−22.9x), EV/EBITDA n/m (−26.2x), P/FCF n/m (−32.5x), **P/B 42.5x**, EV/Sales 50.7x | **Bottom decile** | **Strongly Negative** |
| **Momentum (12-1)** | **−26.07%** (252d, ex-last-21d) | **Bottom quintile** | **Negative** |
| **Quality** | ROE −172.8%, ROIC −78.1%, ROA −56.4%, GP/Assets 0.213, Accruals −0.151 | **Bottom decile** | **Negative** |
| **Low Vol** | Vol 70.75% (252d) / 63.87% (504d); beta 0.31–0.39; max DD 56.5% | **Bottom decile** | **Strongly Negative** |
| **Earnings Revision** | Tool: +54.4% ("upgrade") — **see artifact flag** | Not rankable | **Neutral (data unreliable)** |

**⚠️ Earnings Revision artifact:** The tool reports 2030E EPS $10.003 vs "prior" $6.479 — but **$6.4785 is exactly the current 2029E consensus**, not a 3-months-prior 2030E estimate. The +54.4% is a **period-mismatch artifact**, not a genuine revision. Do not use.

**Genuine estimate picture (consensus, not revision):** A steep back-end-loaded ramp — 2025A −$6.41 → 2026E −$1.62 → 2027E $0.68 → 2028E $3.20 → 2029E $6.48 → 2030E $10.00. Revenue $606M → $6.24B (2030E), EBITDA −$1.17B → +$2.94B. This is a launch-ramp hockey stick, and its credibility rests on brensocatib. Dispersion is enormous (2028E EPS range $0.62–$6.05, 10x spread; only 8–9 analysts out on 2029/30E).

**Countervailing signal:** Analyst **price targets were cut sequentially** through Oct–Nov 2026 (Mizuho $195→$154; Barclays $237→$207; Morgan Stanley $218→$213; Raymond James $187→$173; Guggenheim/Stifel cut to $201/$195). Target *levels* ($154–$213) still imply 5–45% upside vs $146.99, but the *direction of change* was negative.

---

## 2. Price Statistics

| Metric | 504-day (~2yr) | 252-day |
|---|---|---|
| Annualised return | **+42.88%** | — |
| Annualised volatility | **59.51%–63.87%** | **70.75%** |
| Beta vs SPY | **0.312–0.313** | **0.388** |
| Alpha (annualised) | **+61.95%** | — |
| R² vs SPY | **0.004** | — |
| **Sharpe** | **0.721** | 0.319 |
| **Sortino** | **1.071** | — |
| Max drawdown | **−56.54%** | −44.28% |

**⚠️ Two tool inconsistencies flagged:** (a) `calculate_sharpe_sortino` gives Sharpe 0.721 / vol 59.51% while `calculate_price_volatility` gives Sharpe 1.042 / vol 63.87% over the *same* 504-day window — I report the Sharpe/Sortino tool as primary and treat the true figure as **0.72–1.04** (both mediocre-to-poor for 60%+ vol). (b) `get_company_profile` shows beta 0.808 (likely 5-yr monthly) vs 0.31–0.39 on daily data.

**⚠️ Alpha is statistically meaningless.** R² = 0.004 means SPY explains **0.4%** of INSM's variance. The +61.9% annualised alpha has a standard error of roughly ±30%+ under these conditions — it is indistinguishable from zero. Read beta as "low and unstable," not as a usable hedge ratio. Correlation to SPY is only **0.080**; to biotech peers 0.11–0.31 (BMRN 0.308 highest). **INSM is a pure idiosyncratic/catalyst bet — no factor hedge exists.**

### Return decomposition (computed from daily closes)
| Window | Return |
|---|---|
| 1-year (199.64 → 146.99) | **−26.4%** |
| 12-1 momentum | −26.1% |
| YTD (174.04 → 146.99) | −15.5% |
| 3-month (125.08 → 146.99) | **+17.5%** |
| 1-month (95.67 → 146.99) | **+53.6%** |
| Peak (211.41, 2025-12-01) → Trough (91.88, 2026-06-10) | **−56.5%** |
| Off trough | **+60.0%** |
| Last 2 sessions (119.80 → 146.99) | **+22.7%** on 14.4M shs |

---

## 3. Composite Quant Signal: **NEUTRAL** (factor-pure: SELL; event-driven: BUY)

Factor-pure scoring puts INSM at **~2/10**: bottom-decile Value, Quality, Low-Vol, and negative 12-1 Momentum. On my framework alone this is a **Sell**. Three things stop me short of that:

1. **Momentum has inflected violently.** 12-1 is −26.1% but the last month is +53.6% and the last two sessions +22.7% on 14.4M shares (~10x ADV) — a genuine catalyst re-rating, not drift. Classic **momentum-reversal setup**: 12-1 stay negative while 1M and 3M turn sharply positive. My momentum factor is structurally blind to this (it excludes the last 21 days by design).
2. **Accruals are strongly negative (−0.151)** — the one genuinely high-quality reading. Cash burn ($−954M OCF est.) is materially better than net income (−$1,277M), and the balance sheet is fortress-grade: **$1.43B cash, $0.77B debt, net debt $0.26B, current ratio 3.83**.
3. **Valuation is only absurd on trailing numbers.** EV/EBITDA n/m today, but **EV/2030E EBITDA = 10.5x, P/E 2030E = 14.7x, EV/Sales 2030E = 5.0x**. The entire thesis is whether 2030E $10.00 EPS is real — an 8-analyst, 10x-dispersion forecast.

**Score: 2/10 raw factors → NEUTRAL composite.** Upgrade to Buy requires sustained 3-month momentum confirmation and at least one upward EPS revision; downgrade to Sell if the post-catalyst move fades below ~$120.

---

## 4. Key Quant Risk Flags

- **Momentum reversal risk — TWO-SIDED, elevated.** 56.5% drawdown already realized, +60% off the trough, +22.7% in two days. Either the reversal is real and early, or this is a dead-cat bounce off a broken trend. Position sizing, not conviction, is the answer here.
- **No factor hedge available.** Beta 0.31 with R² 0.004 — you cannot hedge this with SPY, XBI proxies, or peer baskets (max peer corr 0.308 to BMRN). Idiosyncratic risk is ~99.6% of total variance.
- **Factor crowding: low, but irrelevant.** No value/quality/momentum screen owns this — it is *absent* from factor portfolios. That is a liquidity/positioning risk, not a crowding risk.
- **Dilution risk — realized, not hypothetical.** Shares outstanding 164.0M → 213.6M (+30.2% YoY); Piotroski F7 "no dilution" = 0. F-Score 5/9 ("Moderate"), with **negative ROA (F1=0), negative operating CF (F2=0), no ROA improvement (F3=0)**. Two of the three profitability tests fail outright.
- **Liquidity: adequate.** ~1.5–4M shares/day, occasional 15–34M spike days. A 734k-share final bar suggests the last print may be a **partial session** — treat the $146.99 close as provisional.
- **Single-asset clinical/regulatory concentration.** $31.4B market cap on $606M revenue = 50.7x EV/Sales, entirely underwritten by brensocatib in bronchiectasis. Any Phase 3/launch disappointment de-rates the 2030E terminal value, which is where ~90% of the NPV sits.
- **Sample-size warning:** 8–9 analysts on 2029–2030E, 10x EPS dispersion at 2028E. Any "consensus" statistic on this name beyond 2027 is a low-confidence estimate.

**Bottom line:** The numbers do not support the story *today* — but the numbers also can't yet see the catalyst. This is a binary, size-it-small, monitor-the-3-month-momentum name, not a factor-portfolio holding.

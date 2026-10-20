# Quant Analyst

- Symbol: CBRS
- Elapsed: 95.9s

---
## CBRS — Cerebras Systems Inc. | Quantitative Factor Report
**Price $120.66 (2026-10-19) · Mkt Cap $27.33B · EV $25.12B · Sector: Technology / Semiconductors**

### ⚠️ Sample-Size Warning (read before the tables)
CBRS IPO'd **2026-05-14**. The entire price series is **109 trading days (~5.2 months)**. Every "252-day" statistic returned by the factor library is therefore a **partial-window extrapolation, not a 1-year estimate**. Financial statements are as of **2025-12-31 (pre-IPO, ~10 months stale)** and do not reflect IPO proceeds. I flag statistical validity per metric below; treat the composite as *directional*, not rigorous.

### 1. Factor Scores

| Factor | Score | Sector Rank (of 10 semis) | Signal |
|---|---|---|---|
| **Value** | P/E 294.3x · EV/EBITDA 89.9x · P/FCF **−66.1x** (neg. FCF) · P/B n/a (BVPS **−$2.69**) | **10 / 10** | **Strongly expensive** — most expensive name in group on EV/EBITDA |
| **Momentum** | −3.1% (tool, 12‑1) / **−36.2%** reconstructed (311.07→198.37) · **−39.2% last 21d** | **9 / 10** | **Negative & deteriorating** |
| **Quality** | ROE **−41.1%** · GP/Assets **0.086** · Accruals **0.107** (high) · F‑Score 5/9 | **9 / 10** | **Low** — poor earnings quality |
| **Low Vol** | Vol **114.6%** · Beta **3.00** · MaxDD **−61.2%** | **10 / 10** | **Worst in sector** (highest vol) |
| **Earnings Revision** | Tool: +542.8% — **INVALID** | n/m | **Unmeasurable** |

**Earnings Revision — why the +542.8% is a data artifact:** the tool compares FY**2028** EPS ($7.97) against FY**2027** EPS ($1.24) — *different forecast periods*, not a revision of the same period. The true picture is: FY2026E EPS **−$0.52 (loss)**, FY2027E $1.24, FY2028E $7.97, from revenue of $510M (2025A) → $885M (2026E) → $2.85B (2027E) → **$7.54B (2028E)** — a 14.8x revenue ramp in three years that assumes near-perfect execution. Coverage is **3–6 analysts on EPS** (insufficient for a reliable revision signal). Red flag: FY2025 consensus was **$1.639 vs. GAAP actual $0.41** — a >70% overshoot, i.e. this sell-side has *historically over-estimated* this name. Cross-check: forward P/E is 97.3x on FY2027 but only **15.1x on FY2028** — valuation is entirely a bet on the out-year.

### 2. Price Statistics
| Metric | Value | Validity (n=109) |
|---|---|---|
| Beta vs SPY | **3.03** (profile: 1.85) | 95% CI **[1.33, 4.72]** — SE≈0.85, *not reliably estimated* |
| R² vs SPY | **0.105** | Market explains only **10.5%** of variance |
| Alpha (annualised) | **−178.9%** | SE≈165% → **t≈−1.1, NOT statistically significant** |
| Volatility (annualised) | **114.6%** | Reasonably robust (~4.7x SPY) |
| Sharpe (0% rf) | **−1.362** arithmetic / **−0.78** geometric | Negative |
| Sortino | **−2.676** | Downside dev < total vol, so worse than Sharpe |
| Max Drawdown | **−61.2%** close-to-close · **−68.8%** intraday | Peak = day 1 (IPO) |
| Realised return | **−61.2%** cum. / **−88.8%** geometric ann. | −156.0% "annualised" is arithmetic mean × 252 — inflated convention |
| Correlations | SPY **0.36** · MU 0.44 · AMD 0.43 · NVDA 0.42 · AVGO 0.34 | Idiosyncratic; behaves as a standalone, not a semi proxy |

### 3. Composite Quant Signal: **STRONG SELL** (low conviction — see caveat)
Bottom-decile on **all four measurable factors** (value, momentum, quality, low-vol), revision signal unmeasurable. There is **no factor in this model that supports ownership at $120.66**.

**Caveat:** the −178.9% alpha and 3.0 beta are *not* statistically significant, and 5 of 5 scores rest on a 109-day, post-IPO window dominated by post-IPO drift and presumed lock-up/expiry dynamics. The honest read: **"zero quantitative support"**, not a statistically validated short.

### 4. Key Quant Risk Flags
1. **Sample size / IPO bias** — 109 days; alpha t-stat ≈ −1.1. Do not size on these betas. Pre-IPO financials (2025‑12‑31) ignore ~$8B+ of IPO proceeds that likely cured the **negative book equity (−$2.69/share)**.
2. **Earnings-quality distortion** — FY2025 net income **+$237.8M** vs. **operating income −$145.3M** and **operating CF −$10.1M**. ~$383M of non-operating benefit drives the "profit." ROIC of 45.9% and F‑Score profitability points are artifacts — ignore them.
3. **Momentum reversal / crash risk** — −39.2% in the last 21 days alone; 114.6% vol ⇒ daily σ ≈ 7.2%. Every 1σ day is ±~$8.70.
4. **Factor crowding — none.** Correlations 0.34–0.44: no crowding benefit, but also **no diversification value** given the vol.
5. **Capital intensity** — FY2025 capex **$382.7M** vs. revenue $510M (75% of sales); FCF **−$392.8M**. Funding gap will require repeated external capital → dilution risk (offset: F7 already scores no-dilution on share count frozen at 215.2M).
6. **Liquidity** — adequate (~$0.5–1.8B daily dollar volume) but volume spiked to 21M shares on 2026‑06‑24 and 18M on 2026‑10‑12; distribution-style volume into weakness.
7. **Analyst target divergence** — median target **~$302** (range $270–$330) vs. spot $120.66 (+150% implied), but **all targets were raised in June–August** when the stock traded $200–262 and none reflect the subsequent −50%. Stale, lagging targets — the sell-side has not marked down.

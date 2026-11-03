# Quant Analyst

- Symbol: CRWV
- Elapsed: 22.4s

---
## CRWV — CoreWeave, Inc. (Quantitative Factor Report)

**Critical data caveat up front:** CRWV IPO'd 2025‑03‑28, so only **~193 trading days** of history exist versus the 252‑day window these tools assume. Every factor labelled "252‑day" is therefore estimated on a **short, post‑IPO sample** and includes lock‑up/volatility distortions. Several tools also return **internally inconsistent figures** (a stale price reference of **$50.15** vs. the actual 2025‑12‑31 close of **$71.61**; annualized return of −19.9% from the Sharpe tool vs. +79% actual price move). Treat all price‑statistics as **directional, not precise**. No dividend, no long history, and the sector peer set (AAPL, NVDA, MSFT… mega‑caps) is **not a valid comparable universe** for a GPU‑cloud pure‑play — sector ranks below are qualitative.

### 1. Factor Scores Table

| Factor | Score | Sector Rank | Signal |
|--------|-------|-------------|--------|
| **Value** | P/E −17.9 (unprofitable); P/B 6.54; EV/EBITDA 19.3; P/FCF −3.0 (cash-burning) | Bottom tercile | **Negative** — expensive on earnings/FCF; EV/EBITDA only "moderate" for growth |
| **Momentum** | +21.6% (12‑1 style) | Top tercile of available data | **Positive but fragile** — masks a −49% collapse from June peak (~$187→$72) |
| **Quality** | ROE −35.0%; gross profit/assets 7.5% (low); accruals −8.6% (clean) | Bottom quintile | **Low** (Piotroski F=5) |
| **Low Vol** | Vol 98.1% ann.; **beta 3.71**; max DD **−63.7%** | Bottom decile | **Strong Sell** — extreme volatility |
| **Earnings Revision** | +154.7% (FY2030 EPS $6.36→$16.20) | n/a | **Nominal "upgrade" but LOW reliability** — 5‑yr‑out estimate, noisy |

### 2. Price Statistics

| Metric | Value | Note |
|--------|-------|------|
| Alpha (ann., vs SPY) | **−86.9%** | Poor risk‑adjusted excess return |
| Beta (vs SPY) | **3.71–3.73** | Extreme market sensitivity; profile beta 7.67 |
| R² | 0.25 | Only 25% of variance explained by market |
| Annualized volatility | **97.9–98.1%** | ~6× market |
| Sharpe ratio | **−0.20** | (tool also reports −0.41 on alt window) |
| Sortino ratio | **−0.35** | Worse downside than upside; negative both |
| Annualized return (est.) | −19.9% (tool) / **+79% actual since IPO** | Contradiction flagged |
| Max drawdown | **−63.7%** | June peak ~$187 → Dec trough ~$64.6 |
| Price (2025‑12‑31 close) | $71.61 | Stale ref in valuation: $50.15 |

### 3. Composite Quant Signal: **SELL** (low‑conviction)

The one true positive — 12‑1 momentum (+21.6%) — is a **sample artifact**: it captures the massive April–June ramp while the most recent quarter shows a **sequential breakdown** (−49% off highs, most of the decline recent). Netting the factors: **deeply negative quality, worst‑decile volatility, negative value on cash flow, and negative alpha** overwhelm a single momentum print. This is a high‑beta, cash‑burning story stock — a **trading vehicle, not a factor‑investable position**. Recommendation: **Sell / Avoid on a quant basis**; any long thesis must be discretionary and thesis‑driven, not factor‑supported.

### 4. Key Quant Risk Flags
- **⚠️ Small sample / data integrity:** <252 trading days post‑IPO; multiple tools internally inconsistent (stale $50.15 price, conflicting returns/Sharpe). Statistical significance is **not established** on any metric.
- **⚠️ Momentum reversal risk: SEVERE** — recent 3‑month collapse; 12‑1 signal is backward‑looking and likely to flip.
- **⚠️ Factor crowding:** AI‑infrastructure/GPU‑cloud is a heavily crowded, high‑sentiment theme; beta 3.7 means brutal drawdowns in risk‑off.
- **⚠️ Liquidity/float:** post‑IPO lock‑up overhang; daily volumes already volatile (e.g., 76M shares on 2025‑11‑11).
- **⚠️ Estimate quality:** the "+154.7% revision" is on a **FY2030** number — essentially un‑informative for near‑term signal.
- **Fundamental fragility:** negative FCF (P/FCF −3.0), ROE −35%, EV $47.7bn on ~$21.8bn mkt cap → levered, capital‑intensive build‑out.

*Bottom line: All-weather quant read is negative except a stale momentum print. Highest‑conviction flags are extreme volatility and data unreliability — do not over‑weight any single number here.*

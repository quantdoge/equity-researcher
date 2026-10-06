# Quant Analyst

- Symbol: ACN
- Elapsed: 150.9s

---
All required data collected. The picture is sharply bifurcated — cheap, high-quality fundamentals against catastrophic trailing price dynamics — so let me be precise about the reconciliation before scoring.

Key evidence from the direct price series (most granular, 2024-06 → 2026-10): ACN peaked ≈$381 (Feb-25), suffered a −24% single-day shock on 41.7M volume Jun-18-26 (≈$165→$126), troughs at ≈$123 (Jun-30-26), and has since recovered to ≈$195 (Oct-6-26) with an +18% spike on Oct-1-26. The raw momentum score (+40%) is not consistent with the price-history-derived 12-month return (−20% to −28%); the tool windows appear to be anchored on different vintages — I flag this explicitly rather than paper over it.

---

## ACN (Accenture plc) — Quant Factor Report

*Price $194.89 · Mkt cap $119.3B · Sector: Technology / IT Services · data through 2026-10-06*

### 1. Factor Scores

| Factor | Score | Sector Rank (Tech) | Signal |
|---|---|---|---|
| **Value** | P/E **14.4**, EV/EBITDA **8.6**, P/FCF **10.4**, P/B 3.6, Div yld **3.4%** | Est. top decile (cheapest of mega-cap tech; NVDA/MSFT/CRM names trade 2–3× richer) | **Strong Buy** |
| **Momentum** | Tool: **+40.5%** (12-1, positive) — **conflicts with** realized −20–28% 12-mo return and −56.5% drawdown | Bottom decile on realized basis | **Weak / contested** |
| **Quality** | ROE **25.2%**, Gross profit/assets **0.32**, Accruals **−0.054** (low = high quality); Piotroski **6/9** | Upper-middle (MSFT/GOOG tier on ROE) | **Buy** |
| **Low Vol** | Ann. vol **53.0–53.4%**; trailing beta **0.13** vs long-run 1.10 | Bottom decile | **Strong Sell** |
| **Earnings Revision** | **+12.1%** upgrade (FY30 EPS $19.43 vs $17.34 prior); path 14.69 → 15.97 → 17.34 → 19.43 (FY27–30) | Top quartile | **Buy** (small sample — 3 analysts on FY30) |

### 2. Price Statistics (252-trading-day window vs SPY, 0% rf)

| Stat | Value |
|---|---|
| Alpha (annualised) | **−27.9%** |
| Beta | **0.127** (R² = 0.001); profile long-run beta 1.10 |
| Sharpe | **−0.52** (vol-tool approx −0.48) |
| Sortino | **−0.73** |
| Max drawdown | **−56.5%** |
| Annualised return / vol | **−27.9% / 53.4%** |

Sector peer return correlations (252d): IBM 0.50, ADP 0.64, CRM 0.60, ORCL 0.14, CSCO **−0.02** — a name behaving far more idiosyncratically than its sector.

### 3. Composite Quant Signal: **NEUTRAL**

This is a textbook value/quality vs. price-dynamics split. Value is genuinely top-decile (cash-flow multiples half of mega-cap tech peers, 3.4% yield), quality is high (25% ROE, negative accruals), and forward EPS estimates are being raised. But the realized numbers are unambiguous: 252-day alpha −28%, Sharpe −0.52, Sortino −0.73, −56.5% drawdown, and returns with essentially **zero** market correlation (R² = 0.001). The June-26 −24% single-day de-rating (on 41M+ volume) followed by a sharp V-recovery means the momentum factor is unstable and cannot be trusted as bullish. For a pure factor screen this nets to Neutral — cheap-and-good on paper, but the market is aggressively repricing the story, and that repricing is entirely idiosyncratic, i.e., unhedgeable. Do not treat this as a Buy until the revision momentum is confirmed by realized results (or a second consecutive estimate upgrade lands on a full-sample FY27/FY28 vintage).

### 4. Key Quant Risk Flags

1. **Momentum reversal risk (HIGH):** Raw momentum (+40.5%) and realized return (−28%) disagree across tools; the stock swung ±20%+ in days both ways within 2026 (Jun-18 −24%; Oct-1 +18%). The "momentum" signal is a V-recovery artifact, not a durable trend.
2. **Idiosyncratic / unhedgeable risk (HIGH):** Trailing beta 0.13 with R² ≈ 0.001 vs. long-run beta 1.10 — the factor model cannot attribute recent moves to the market, and sector correlation is mixed-to-zero (CSCO −0.02, ORCL 0.14). Size positions on a no-hedge assumption.
3. **Cheap-for-a-reason / factor crowding:** The low multiples partly price in the Jun-26 guidance shock (services/AI demand risk). The 3.4% dividend yield is income support but also a symptom of the −49% drawdown from peak ($381 → $195); the low-vol factor fails badly here.
4. **Small samples:** Sector ranks are directional — `rank_universe_by_factor` only evaluated the 25 largest mega-caps and did **not** include ACN, so Technology-decile placement is an estimate from observed peer multiples. FY30 EPS revision rests on **3 analysts** (vs 17 for FY27); R² = 0.001 means alpha/beta carry little explanatory power. Statistical confidence on the far-forward upgrade is limited.

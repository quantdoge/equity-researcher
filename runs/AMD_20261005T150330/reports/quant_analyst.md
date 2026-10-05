# Quant Analyst

- Symbol: AMD
- Elapsed: 79.9s

---
All data gathered. Cross-sectional ranks are assembled from direct peer multiples (the `rank_universe_by_factor` tool rejects both list and string universes — a spec bug I flag rather than burn more budget on). Writing the report now.

---

# AMD — Quantitative Factor Report

**Universe:** Technology / Semiconductors (peer set: NVDA, TSM, AVGO, MU, INTC, MRVL, QCOM, ASML, AMAT, LRCX, TXN, KLAC, ADI). Price refs: $629.90, MCap ≈ $1.03T, FY ends late December.

## 1. Factor Scores

| Factor | Score (raw) | Sector Rank | Signal |
|--------|-------------|-------------|--------|
| Value | P/E 238.1 · EV/EBITDA 141.0 · P/FCF 153.2 | Bottom decile — worst of peer set | **Strong Sell** |
| Momentum | 12-1 mo return **−10.3%** | Bottom half (sector tailwind from AI semis; AMD lagging) | **Sell** |
| Quality | ROE 6.9% · ROIC 5.5% · GP/Assets 0.22 · accruals −0.044 · Piotroski 8/9 | Lower half; ROE ≈ 1/11th of NVDA's 76% | **Neutral** |
| Low Vol | Ann. vol **71.2%** · beta **3.18** (vs SPY) | Bottom decile | **Strong Sell** |
| Earnings Revision | FY2030 EPS $44.75 vs $31.45 prior = **+42.3%** upgrade | Top decile (caveat: n=9 analysts, 5-yr horizon) | **Strong Buy** |

**Peer value context (same tool, latest FY):** NVDA P/E 48.4 / EV-EBITDA 39.9; MU 14.4 / 10.8; INTC unprofitable (neg P/E, P/B 4.5). AMD's EV/EBITDA is **~3.5× NVDA's and ~13× MU's**; even vs the richest-quality AI name, AMD prices as if it has already delivered 4× the FY2025 EPS of $3.96. *(TSM multiples excluded — P/B 0.46 / EV-EBITDA 0.16 is an ADR share-count artifact.)*

## 2. Price Statistics (252-trading-day window vs SPY, r_f = 0)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+111.5%** |
| Beta | **3.20** (R² = 0.34 — high idiosyncratic drift) |
| Sharpe | **2.38** |
| Sortino | **4.03** |
| Volatility (ann.) | 71.2% |
| Max drawdown | −26.5% |
| Trailing annualized return | +171.3% |

## 3. Composite Quant Signal: **SELL** (leaning Sell; not a Strong Sell only on revision + tape strength)

Weighted view: 2× Strong Sell (value, low-vol), 1 Sell (momentum), 1 Neutral (quality), 1 Strong Buy (revisions) ⇒ below the Neutral midpoint. The elite Sharpe/Sortino/alpha are **not compounding-quality evidence — they are the tail of a ~1-month squeeze** (trailing return +171% while 12-1 momentum was **−10%** as of last month). The framework's attractor — top-quintile value AND momentum AND quality — is absent on all three. Estimate revisions are real and rising (+42% on FY30, EPS ladder $7.6→$15.9→$23.0→$31.5→$44.8 across FY26–30), but that is exactly the perfection the 238× P/E already prices.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (HIGH):** −10.3% 12-1 momentum vs +171% recent tape = the entire current P&L is a fresh, unproven spike. Beta 3.2 means the gain is ~3× leveraged to the AI-semi tape and will reverse 3× on a sector de-rating.
2. **Factor crowding (HIGH):** pairwise correlations AMD–INTC 0.69, AMD–TSM 0.65, AMD–MU 0.61, AMD–NVDA 0.48. AMD is a crowded-trade copy of the semi complex; no differentiated quant edge, and a sector-wide de-rate hits hardest on the highest-beta name.
3. **No margin of safety:** EV/EBITDA 141 / P/FCF 153 with FCF yield ~0.7% — a modest estimate haircut or multiple de-rate has outsized downside. Max DD 26.5% is understated for this vol regime.
4. **Small revision sample:** the +42% upgrade rests on 9 analysts for a FY2030 target; lower vintages (FY27–28, n=17–21) are the more trustworthy but materially smaller revisions.

*Sample-size note: all statistics use one 252-day window (one drawdown/Sharpe observation — not a significance test), and the cross-sectional rank tool was non-functional (rejects list **and** string universes), so ranks are derived from direct peer-multiple comparison. Liquidity: none — mega-cap, $1.03T, trades daily at depth.*

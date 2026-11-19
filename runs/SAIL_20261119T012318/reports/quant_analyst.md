# Quant Analyst

- Symbol: SAIL
- Elapsed: 61.5s

---
## SAIL (SailPoint, Inc.) — Quantitative Factor Dossier

**Critical data note up front:** the vendor's reference price is **$22.25** (market cap $12.5bn), but its own OHLC tape has the last close at **$15.92 (2026-02-13)** — a 28% stale-price gap. All vendor return/vol/momentum/alpha figures below are therefore reproduced alongside my own recomputation from the raw daily tape. Where they conflict, the tape wins.

---

### 1. Factor Scores

Peer set is **hand-built** (OKTA, CRWD, ZS, NET, PANW — identity/security software). The tool's "Technology" sector list returns AAPL/MSFT/NVDA mega-caps, which are not valid comparables for a $9bn identity-security SaaS name.

| Factor | Score (raw metric) | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/B 1.31x adj (vendor 1.83x @ $22.25); P/FCF **173x** adj (241.6x vendor); EV/EBITDA negative; EV/S FY27E 6.8x | **3/6** — cheapest on P/B, 5th of 6 on P/FCF | Neutral |
| **Momentum** | Vendor 12-1: **+3.25%**; recomputed 12-mo **−27.6%**, 3-mo **−17.0%**, 1-mo **−17.6%** | **4/6** (OKTA +38.8%, ZS +29.6%, CRWD +7.9% > SAIL > NET +0.1%, PANW −9.5%) | **Negative** |
| **Quality** | ROE **−3.9%**; GP/Assets **9.1%** (6th of 6); accruals −4.5% (least negative of group); Piotroski **6/9** | **6/6** | **Weak / Sell** |
| **Low Vol** | Realised vol **70.0%** (peers 56.0–78.1%); beta 1.24 (252d), 2.08 reported (5y — not credible on 12mo of history) | **3/6 on vol, 2/6 on beta** | Neutral |
| **Earnings Revision** | Vendor **+24.45%**, but flagged unreliable (below) | n/a | **Unverified** |

**Earnings-revision caveat (important):** the tool compared FY2030 consensus EPS of **$0.63** against the FY2029 figure of **$0.506** — a *different fiscal period*, not a like-for-like revision — and the FY2030 number rests on **n = 1 analyst**. That "+24.45% upgrade" is a period-roll artifact, not a revision signal. What the estimate ladder does show is an intact growth consensus with no downgrade: revenue FY27E $1.269bn → FY28E $1.512bn → FY29E $1.800bn (~19–20% p.a., 14–20 analysts), EPS FY26E $0.234 → FY27E $0.324 (+39%) → FY28E $0.402 (+24%). Treat revision momentum as **neutral/unmeasured** — no historical snapshot exists to compute direction.

---

### 2. Price Statistics

| Statistic | Vendor | Recomputed / assessment |
|---|---|---|
| Beta vs SPY (252d) | 1.248 | β = 1.25, but **R² = 0.066** — 93% of variance is idiosyncratic; beta is a poor risk descriptor |
| Alpha (annualised) | +62.3% | **Statistically insignificant**: daily residual σ ≈ 4.3%, n ≈ 250 → t(α) ≈ **0.9**. Not evidence of skill |
| Sharpe (0% rf) | 1.209 | ≈ **−0.45** on a −27.6% realised 12-mo return |
| Sortino (0% rf) | 1.905 | ≈ **−0.6** (approximate, downside-deviation basis) |
| Annualised vol | 70.0% | Consistent order of magnitude; recomputed ≈ 55–65% for the full post-IPO sample |
| Max drawdown | −36.6% | **−43.0%** close-to-close ($25.70 → $14.65); **−48%** intraday ($26.35 → $13.72) |
| Annualised return | +84.6% | **Contradicted by tape**: $22.00 (IPO 2025-02-13) → $15.92 = **−27.6%** |

Vendor alpha/return are inconsistent with its own price file (likely a mis-specified or stale window). Do not use the +84.6% return or +62.3% alpha.

---

### 3. Composite Quant Signal: **NEUTRAL (with negative trend bias)**

Weighted: Value neutral (P/B support, FCF valuation indefensible) 30% · Quality weak 25% · Momentum negative 25% · Low-vol neutral 10% · Revision unverified 10%.

The bull arithmetic: **EV ≈ $8.6bn** ($8.94bn mkt cap + $0.34bn net cash) on **FY27E revenue $1.269bn = 6.8x EV/S** for a ~19% grower at the *low end* of identity-security comps, with operating cash flow inflecting positive (**+$70.6m FY26 vs −$106.4m FY25**) and accruals improving four years running (−0.0015 → −0.0448). The bear arithmetic: **$52m of FCF on ~$9bn of equity (173x)**, GP/assets of 9.1% (worst in peer set — opex intensity and take-private goodwill), a −43% drawdown, and a −17.6% one-month slide with no valuation floor from earnings.

**Not a Strong Sell** (cash-flow inflection + genuine P/B/FCF improvement + intact 19% growth consensus), **not a Buy** (momentum broken, quality last in group, alpha statistically indistinguishable from zero).

---

### 4. Key Quant Risk Flags

1. **Sample size / statistical power — severe.** IPO 2025-02-13 → ~250 trading days. All factor ranks are ordinal among 6 names; the value, quality and revision "ranks" have no meaningful confidence interval. Beta R² = 0.066 and alpha t ≈ 0.9 mean the risk/return statistics are effectively descriptive noise.
2. **Momentum reversal / trend breakdown.** −17.6% in the last month, −17.0% over 3 months, −27.6% since IPO, and −43% peak-to-trough. Everything above $16 is underwater; the stock is in a persistent downtrend with no momentum cushion.
3. **Data integrity.** Vendor price $22.25 vs tape $15.92; vendor P/B, P/FCF, EV and return/vol statistics are all stale or internally inconsistent. Any screen using this feed will mis-rank SAIL on both value and momentum. Vendor revision score is a period-mismatch artifact (n=1).
4. **Earnings-negative → valuation-factor exclusion.** P/E −42.8x, EV/EBITDA negative. SAIL is automatically excluded from most value/GARP screens and scores at the maximum penalty on earnings-based factors.
5. **Factor crowding / idiosyncratic risk.** 70% annualised vol, single-name event risk (quarterly SaaS prints, lock-up expiry dynamics on a 2025 IPO, 3,229 employees against $1.07bn revenue = heavy SBC dilution — Piotroski flag F7 "no dilution" = 0).
6. **Liquidity is adequate but thinning.** Median daily volume ~1.5–2.0M shares (~$25–30m at $16); acceptable for institutional sizing but volume spikes on down days (Jan 29: 4.8M, Feb 3: 5.4M) indicate distribution.
7. **Capital-return history distorted.** ROE +181% (FY23) / +73% (FY24) are pre-IPO thin-equity artifacts; ROIC −31.8% → +4.2% → −4.5% is not a clean series. Use FY26+ only.

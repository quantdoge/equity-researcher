# Quant Analyst

- Symbol: FTNT
- Elapsed: 13.1s

---
# FTNT — Quantitative Factor Analysis

**Fortinet, Inc.** | Technology → Software-Infrastructure (Cybersecurity) | Price $139.10 | Mkt Cap ~$104B | Data as of FY2025-12-31

## 1. Factor Scores Table

| Factor | Score / Raw | Sector Rank* | Signal |
|--------|-------------|--------------|--------|
| **Value** | P/E 57.2 · P/B 84.3 · EV/EBITDA 41.2 · P/FCF 46.8 | **#1 of 4** (cheapest) | **Neutral** — rich in absolute terms, but cheapest & only profitable name in peer group |
| **Momentum** | 12-1 ret **+15.3%** | #3 of 4 | **Neutral/Positive** — positive but trailing CRWD (+41%), PANW (+18%) |
| **Quality** | ROE 149.8% · GP/Assets 0.529 · Accruals −0.071 | **#1 of 4** (highest) | **Strong Buy** — best-in-class profitability, clean (negative) accruals |
| **Low Vol** | Ann. vol 52.7% · Beta 0.98 (SPY) · MaxDD 28.6% | Mid | **Weak** — beta ≈ market but *absolute* vol very high (52.7%) |
| **Earnings Revision** | Forward EPS +6.24% vs 3-mo prior | n/a | **Positive** — upgrade |

\*Peer set = FTNT, PANW, CRWD, ZS (direct cybersecurity comps; broad sector list returned mega-caps, not comparable).

**Peer cross-check (the value/quality story):**
| | P/E | EV/EBITDA | P/FCF | ROE | Quality |
|---|---|---|---|---|---|
| **FTNT** | 57.2 | 41.2 | 46.8 | **149.8%** | High |
| PANW | 864.9 | 208.6 | 70.7 | 1.1% | Low |
| CRWD | neg | 1453 | 205.8 | −3.6% | Low |
| ZS | neg | 204.2 | 46.6 | neg | — |

FTNT is the **only peer with a normal P/E, positive earnings, and a high-quality signal** — it screens cheapest *and* highest-quality simultaneously, a rare top-quintile combination.

## 2. Price Statistics (252-day window, vs SPY)

| Metric | Value |
|--------|-------|
| Alpha (annualised) | **+76.0%** |
| Beta | **0.988** |
| R² | **0.059** (only ~6% of variance market-explained) |
| Sharpe ratio | **1.63** |
| Sortino ratio | **2.15** |
| Annualised return | 86.8% |
| Annualised volatility | 53.4% |
| Max drawdown | −28.6% |

Supporting fundamentals: ROIC 93.2%, ROA 17.8%, Piotroski F-Score **6/9 (Moderate)**; accruals consistently negative 4 yrs (−0.05 to −0.14) = high earnings quality.

## 3. Composite Quant Signal: **BUY**

Rationale: FTNT ranks top-quintile on **Quality** (best ROE/GP-assets, clean accruals) and top on **relative Value** (cheapest profitable name in peer set), with **positive momentum (+15%)** and **upward estimate revisions (+6.2%)**. Strong Sortino (2.15) confirms favourable risk-adjusted returns. Absolute valuation (P/E 57, P/B 84) and very high volatility cap it below Strong Buy.

## 4. Key Quant Risk Flags

1. **Alpha estimate not statistically robust.** R² = 0.059 is very low — the +76% "alpha" is almost entirely idiosyncratic noise; the *beta* (≈0.99) is the only reliable regression output here. Do not treat 76% alpha as repeatable.
2. **Short-term reversal / momentum-spike risk.** Trailing 12-month return (86.8% arithmetic-annualised) vastly exceeds 12-1 momentum (+15.3%), implying a large share of gains concentrated in the most recent month — elevated reversal risk.
3. **Factor crowding.** Quality + low-beta software names are crowded; a rotation to deep-value/cyclicals would pressure the multiple.
4. **Absolute valuation rich.** Even as peer-group "value," 57× earnings / 84× book offer no downside cushion; high multiple + 53% volatility = large drawdown potential.
5. **Thin revision sample.** Earnings-revision signal compares a single long-dated (2030) consensus figure covered by only **4 analysts** — low statistical confidence; treat directionally only.
6. **Low-beta signal is weak.** Beta 0.99 ≈ market, but *absolute* volatility (52.7%) is far above a genuine low-vol candidate — not a defensive holding.

**Data-quality note:** `sharpe_sortino` annualised return (86.8%) is an arithmetic annualisation inflated by volatility drag and is inconsistent with the compounded 12-1 figure; I rely on the 15.3% momentum number as the operative input.

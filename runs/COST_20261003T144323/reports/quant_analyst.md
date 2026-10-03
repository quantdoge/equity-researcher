# Quant Analyst

- Symbol: COST
- Elapsed: 169.4s

---
All data gathered. I verified momentum direction directly from price history and confirmed the low beta/R² is real (COST's last 12 months were dominated by idiosyncratic moves — +30% vs +14% for SPY in H2'24–H1'25, then −11% vs +18% in H2'25). Writing the report now.

---

# COST — Costco Wholesale Corp. (Consumer Defensive / Discount Stores)
**Quant Factor & Risk Report** — price ref $920.65, mkt cap $408B | Data: price history thru 2026-01-30; fundamentals FY2023–FY2026

## 1. Factor Scores

| Factor | Score | Sector Rank (n≈10) | Signal |
|--------|-------|---------------------|--------|
| **Value** | P/E 44.4x · EV/EBITDA 27.6x · P/B 11.4x · P/FCF 43.6x · Div yld 0.6% | **Bottom quintile (9–10/10)** | **Very unattractive** |
| **Momentum** | 12-1m return **−3.6%** (vs SPY ≈ +15% over same window) | Mid-low (6–7/10) | **Negative** |
| **Quality** | ROIC 26.3% · ROE 25.8% · Gross profit/assets 0.44 · Accruals **−7.4%** · F-Score 6/9 | **Top (1/10)** | **Strong buy-side signal** |
| **Low Vol** | Ann. vol **20.4%** (high for staples) · β (5y) ≈ 0.86 · Max DD **−18.2%** (1y) | Bottom half (7–8/10) | **Unattractive** |
| **Earnings Revision** | FY31 EPS est **$32.63 vs $29.80** prior → **+9.5%** in 3mo (consensus: upgrade) | Top quartile | **Strong positive** |

**Supporting fundamental detail:** 4-yr ROIC trend 22.8% → 27.7% → 26.4% → 26.3% (durable); accruals consistently negative (−5.7% to −7.4%) = very high earnings quality; F-Score 6 (moderate — misses on ROA change, margin, and asset-turnover improvement in the latest year).

## 2. Price Statistics (252-day window vs SPY)

| Metric | Value | Note |
|---|---|---|
| Alpha (annualised) | **+12.2%** | *Not statistically meaningful*: R² = 0.01 |
| Beta | **−0.16 (1y OLS)** / 0.86 (5y, profile) | 1y beta ≈ 0 is real, not a data error — see below |
| R² vs SPY | **0.01** | COST's recent path is almost entirely idiosyncratic |
| Sharpe | 0.46 | 0% rf |
| Sortino | 0.70 | Upside vol dominates (Feb'25 blowoff) |
| Ann. return / vol | +9.4% / 20.4% | |
| Max drawdown (1y) | −18.2% | Peak ~$1,067 (Feb'25) → trough ~$856 (Dec'25) |
| Correlations (252d) | WMT 0.65 · KO 0.43 · PEP 0.42 · MO 0.40 · PG 0.32 · MNST 0.15 | Paired with **WMT** (0.65), low vs staples staples |

**Beta caveat (important):** the 1-year OLS beta of −0.16 with R² = 0.01 is not a statistical fluke of bad alignment — it is economically real. Over the last ~19 months COST returned +30% while SPY returned +14%, then −11% while SPY returned +18%. The stock has traded on company-specific factors (Feb'25 euphoric run to $1,067, then a ~20% grind down through 2025 despite steady fundamentals). The 0.86 beta from the profile is the longer-horizon figure; treat the 1y beta with heavy caution either way.

## 3. Composite Quant Signal: **NEUTRAL**

This is the textbook "quality compounder, wrong price, wrong tape" setup:
- **For:** Elite, durable quality (top-decile ROIC, negative accruals), strong +9.5% estimate-revision momentum, near-zero market beta, abundant liquidity, ~14% implied upside to the ~$1,050 average recent price target.
- **Against:** Valuation in the 93rd–97th percentile of its own history and the priciest mega-cap in the sector (P/E 44x vs WMT ~33x, KO ~22x, PG ~25x, PEP ~21x, MO ~13x); 12-1 momentum **negative** while the market is up; above-average vol for the sector; low R² means no market tailwind.

Net: strong-quality/high-revision vs. weak-value/negative-momentum offsets → **Neutral**. The revision momentum is the one dynamic factor that could flip this to Buy if price stabilises; the valuation argues against chasing.

## 4. Key Quant Risk Flags

1. **Momentum reversal risk (HIGH):** Negative 12-1 momentum in a rising market. The Dec'25–Jan'26 bounce (~$856 → ~$960) is only ~+12% off the low and has not repaired the 12-month damage. No momentum confirmation until 12-1 turns positive.
2. **Valuation / factor crowding (HIGH):** COST is a consensus "quality compounder" holding; P/E 44x, P/FCF 43.6x, yield 0.6%. In its sector it sits in the bottom quintile on value — the factor most negatively correlated with future 12-month returns at these extremes.
3. **Idiosyncratic concentration (MEDIUM):** R² = 0.01 vs SPY over 1y. Positive read-through: effectively zero market-beta exposure. Negative: returns are hostage to company-specific news; a comp/growth/membership miss has no diversification cushion, and 20% vol at a 44x multiple is a high risk-adjusted-cost entry.
4. **Liquidity (LOW risk):** ~$1.5–2B+ ADV and $408B market cap — no liquidity concern; flagged only that low float turnover makes the name prone to outsized single-day moves (note the 10M-share volume spike on 2025-12-19).

**Data caveats:** Analyst estimates for FY2030–31 rest on only 5–9 covering analysts (small sample — treat the +9.5% revision with moderate confidence); OLS alpha/beta statistics over 252d have negligible explanatory power (R² = 0.01) and should be read qualitatively; peer multiples cited are approximate sector benchmarks, not freshly pulled comps.

# Quant Analyst

- Symbol: ALNY
- Elapsed: 138.3s

---
## ALNY — Quantitative Factor Report

**⚠️ Data integrity caveat (read first).** The feeds disagree on ALNY's price level by ~2x, and this materially affects every return-based statistic:

| Source | Price | As-of |
|---|---|---|
| `get_price_history` (OHLCV) | **$336.19** | 2026-02-20 |
| `calculate_valuation_ratios` / risk tools | **$174.00** | later vintage (price-target notes quoting $177–$266 posted Aug–Oct 2026) |

The risk-model outputs are also internally broken: **beta 0.028 with r² = 0.000**, correlation to SPY of **0.098**, and **−99.9% annualized return over a 126-day window** (arithmetically impossible on the OHLCV path, which shows −26.7% over the same 6 months). I therefore report tool outputs **and** my own price-derived statistics, and I do not use the OLS alpha/beta in the composite.

---

### 1. Factor Scores

| Factor | Score / Raw Value | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E 74.7 · EV/EBITDA 34.5 · P/FCF 50.4 · P/B 29.7 | **3rd of 4** (worst P/E; AMGN 32.4x, GILD 24.4x cheaper) | **Negative** (bottom-quartile) |
| **Momentum** | Tool 12-1: **−13.4%** · Raw OHLCV 12-1: **+41.6%** · Last 3m: **−24.6%** | 4th of 4 on tool basis (AMGN +11.9%, GILD +13.8%, LLY −1.0%) | **Negative / decaying** (sign conflict — see note) |
| **Quality** | ROE 39.8% · GP/Assets **0.6115** · Accruals **−4.24%** · F-Score **7/9** | **1st of 4** on GP/Assets and accruals | **Strong positive** (top quartile) |
| **Low Vol** | Vol 58.0% (252d) / 71.3% (126d) · Beta 0.44 (profile: 0.269) | n/a — peer vols not pulled | **Negative** (very high vol despite low beta) |
| **Earnings Revision** | Tool: +18.1% "upgrade" — **invalid** | n/a | **Not scoreable** (see below) |

**Revision score is an artifact, not a signal.** The tool compared the **FY2030** consensus EPS ($16.56) against the **FY2029** estimate ($14.03) — two different forward periods. That is the analyst ladder, not a revision of a fixed period. Consensus ladder (13–15 analysts): FY26 $6.49 → FY27 $9.64 → FY28 $11.91 → FY29 $14.03 → FY30 $16.56 (~26% CAGR, 4+ years out). FY26 dispersion is tight ($6.11–$6.90), implying low estimate risk near-term. No revision history vintage exists in this feed → **flagged unavailable**.

**Momentum note:** the two price vintages explain the conflict. Raw OHLCV (peak $491 on 2025-10-20 → $336) gives positive 12-1 momentum but a clearly deteriorating tape. If $174 is the live price, trailing 12m is roughly **−64%** and the tool's negative momentum is the correct read. Either way, the *direction* is unambiguous: **sharp downtrend since Q4-2025**.

---

### 2. Price Statistics

| Metric | Tool output | My estimate from OHLCV |
|---|---|---|
| Annualized return (252d) | −70.4% | **+33.9%** (251.00 → 336.19, Feb-25→Feb-26) |
| Alpha (annualized, vs SPY) | −84.4% (r²=0.0096) | **Unusable** — not statistically identifiable |
| Beta vs SPY | 0.441 / 0.028 | 0.27–0.44 (report a **0.3–0.45 range**) |
| R² vs SPY | 0.0096 / 0.000 | Implausibly low for a large-cap — data defect |
| Volatility (annualized) | 58.0% / 71.3% | High; consistent with biotech regime (50–70%) |
| Sharpe (0% rf) | −1.19 (252d) / −1.37 (126d) | **≈ +0.6** on the +33.9%/58% vintage |
| Sortino (0% rf) | −1.12 / −1.17 | Not computable without full return series |
| Max drawdown | −53.0% / −46.2% | **−37.2%** ($491.22 → $308.48); **≈ −65%** if $174 is live |

Sharpe/Sortino and alpha/beta are **not usable as reported**. The r²=0.0 means alpha is entirely noise; the sign of Sharpe flips depending on which price vintage you trust. Any portfolio construction decision must not lean on these numbers.

---

### 3. Composite Quant Signal: **NEUTRAL** (high signal dispersion)

- **Quality is the one clean, high-conviction factor:** 2025 was ALNY's first profitable year (NI $313.7M vs −$278.2M in 2024), ROIC-generating, best-in-group gross profit/assets, negative accruals (cash flow $524M > net income → earnings are cash-backed, not accounting-driven). F-Score 7/9, docked for share dilution (F7) and no gross-margin improvement (F8).
- **Valuation provides no offset:** 74.7x trailing earnings, 29.7x book, 34.5x EV/EBITDA. The bull case rests entirely on the FY26→FY30 EPS ramp; on FY26E the multiple is ~26.8x, which is defensible but not cheap for a name with this volatility.
- **Momentum and price action are the swing factor and they are negative.** A −37% to −65% drawdown with no base formation is a trend that fights the quality signal.
- Quality (top quartile) + Value (bottom quartile) + Momentum (negative) is the classic **"quality at a still-unproven price"** profile — not the rare top-quintile-on-all-three setup that justifies a Buy.

---

### 4. Key Quant Risk Flags

1. **Data-integrity / model risk (highest severity).** Two conflicting price levels ($174 vs $336); r² = 0.0 and SPY correlation 0.098 on a $23–45B large cap. Do not size a position off these risk statistics; re-pull from a single as-of date.
2. **Momentum reversal already realized, not prospective.** −37% from the Oct-2025 peak (−65% if $174 is live). Downside momentum is persistent; there is no evidence of a volatility contraction or base yet.
3. **Factor crowding — not a concern.** ADTV ~1.0–1.5M shares (~$300M+); liquidity is ample, no crowding flag.
4. **Valuation risk is duration risk.** 74.7x trailing depends on an FY2030 estimate with 13 analysts; a single ATTR-CM competitive read-through (cf. Jefferies' Aug-2026 note on AstraZeneca data) compresses the terminal multiple faster than the EPS ladder compounds.
5. **Small-sample warning.** Sector ranks are computed against **n = 3 peers** (LLY, AMGN, GILD) — the top-10 sector list is large-cap pharma, not RNAi/biotech. Percentile ranks carry **no statistical significance**; treat as directional only.
6. **Earnings quality is genuinely good, but single-period.** Negative accruals in 2025 (−4.24%) follows three years of losses — one profitable year is too short a sample to establish a durable accrual trend.

**Bottom line:** the only statistically clean factor is **quality (strong)**, offset by **value (poor)** and **momentum (negative)**. Two of five factor signals are unscoreable or defective, so the honest composite is **Neutral pending price-data reconciliation** — not a Buy on quality alone, and not a Sell while the cash generation is this real.

# Quant Analyst

- Symbol: AKAM
- Elapsed: 76.1s

---
## AKAM Quantitative Factor Report
**Sector:** Technology / Software–Infrastructure · Price used by data module: $80.29 · Last close in raw series (2025-12-31): $87.25 · Mkt cap ≈ $11.8B · EV ≈ $17.53B · No dividend

⚠️ **Up-front data-integrity warning.** The risk-statistics module is internally inconsistent with AKAM's own raw OHLC series. Reported vol (68.3%), max drawdown (51.7%) and annualized return (+0.98%) cannot be reproduced from the price history: peak close 102.10 (2025-02-10) → trough 68.21 (2025-04-08) is **–33.2%**, and 2024-12-02 → 2025-12-31 is **–10.9%**. Peer calibration suggests the module is not globally broken (MSFT 35.0% vol, PLTR 64.7%), so the corruption is AKAM-specific — likely a stale/torn series (note the $80.29 quote vs $87.25 actual close). All risk figures below are reported as-is, then re-based where I can recompute from raw prices.

---

### 1. Factor Scores Table
Peer set = 3 software-infrastructure names (AKAM, MSFT, PLTR). **n=3 — z-scores and "ranks" are indicative only, not statistically meaningful quintiles.** Z-sign convention: positive = attractive.

| Factor | Raw Values | Score (z) | Sector Rank | Signal |
|---|---|---|---|---|
| **Value** | P/E 26.2 · EV/EBITDA 13.1 · P/FCF 16.9 | **+0.81** | **1 of 3** | **Bullish** — cheapest on every multiple (MSFT 30.4/19.8/60.7; PLTR 269/254/207) |
| **Momentum** (12-1) | –11.75% (raw series confirms ≈ –10.4%) | **–1.08** | 3 of 3 | **Bearish** — bottom of group vs MSFT +16.7%, PLTR +69.8% |
| **Quality** | ROE 9.1% · GP/Assets 0.201 · Accruals –0.093 · ROIC 5.3% | **–0.37** | 3 of 3 | **Bearish** — lowest ROE & GP/A; only accruals rank #1 (excellent, negative) |
| **Low Vol** | Vol 68.3% (reported) / ~37% est. · Beta 0.66 (profile) / 1.49 (regression) | **–0.82** (reported) / ≈+0.1 (re-based) | 3 of 3 (unreliable) | **Conflicted** — see note |
| **Earnings Revision** | +17.39% "upgrade" | **n/a** | n/a | **Not usable — see methodology flag** |

**Value:** Genuinely the standout. EV/EBITDA 13.1x at 6.3% EBITDA growth is the only factor with clean, non-contaminated support.

**Quality:** The weakest link, and not just a ranking artifact. ROIC has fallen four consecutive years: **8.98% → 6.98% → 5.61% → 5.29%** (2022→2025). ROIC is now roughly at/below cost of capital. Gross margin compressed **59.4% → 54.7%** (−470bp) as cost of revenue rose +17.6% against revenue +5.4% (to $4.21B). Net income fell –10.5% to $452M despite revenue growth. Piotroski F-Score **5/9** (fails: ROA improvement, leverage, gross margin, asset turnover). The one genuine quality positive: accruals ratio **–0.093**, negative and stable for four years — cash conversion is excellent (OCF $1.52B vs NI $452M, 3.4x), so earnings are high-quality and understated relative to cash.

**Low Vol — call this factor void.** The 68.3% reported annualized vol exceeds PLTR's 64.7%, which is not credible for a $12B CDN/security name with published beta 0.664. Recomputing sum-of-squared returns from the raw daily series gives daily σ ≈ 2.4%, i.e. **~37% annualized** (earnings-gap driven: –21.7% on 2025-02-21, –10.8% on 2025-05-09, +14.7% on 2025-11-07). At ~37% AKAM ranks **#2 of 3**, slightly above MSFT (35.0%). Factor crowding into low-vol is not a risk here; single-name event gap risk is.

**Earnings Revision — methodology flag, do not use the +17.39%.** The tool compares `current_eps_estimate 13.40` (FY**2030**) against `prior_eps_estimate 11.415` (FY**2029**). That is forward-*year growth*, not a same-period revision over 3 months as documented. It also rests on only **4 analysts**, and the implied path (FY25 actual $3.07 → FY27 $6.73 → FY30 $13.40, ~34% 5-yr CAGR) is implausible for a low-teens grower. **The real revision signal points the other way:** of six recent broker actions, all are *lowered* targets (UBS 90, RBC 85, FBN 120, MS 149, Evercore 150, KeyBanc 175) against posting prices of $77.84–$92.72. Direction of revisions = **negative**, contradicting the tool's "upgrade" label.

---

### 2. Price Statistics

| Metric | As Reported | My Re-based Estimate | Assessment |
|---|---|---|---|
| Alpha (ann., vs SPY) | –19.72% | — (cannot recompute without SPY series) | Bearish but low-confidence |
| Beta (252d) | 1.496 (R² 0.0996) | ~0.66–1.0 plausible | Regression beta unreliable — R² 0.10 |
| R² | 0.0996 | — | **~90% idiosyncratic**; market beta explains almost nothing |
| Sharpe (252d) | 0.014 | ≈ –0.25 to –0.30 | Weak either way |
| Sortino (252d) | 0.022 | ≈ –0.35 | Weak either way |
| Ann. return | +0.98% | **–10.2%** (raw: –10.9% over 13mo) | Reported sign is wrong |
| Ann. volatility | 69.21% | **~37%** | Overstated ~1.9x |
| Max drawdown | 51.69% | **–33.2%** close / –34.9% intraday | Overstated |

**Interpretation:** Even setting aside the corrupted feed, the qualitative conclusion is robust — AKAM delivered roughly **–10% total return with ~37% volatility against a rising tape**, i.e. negative alpha and a negative Sharpe. Reported Sharpe 0.014 / Sortino 0.022 (ratio 1.6) implies downside deviation ≈ 64% of total deviation — no meaningful positive skew to compensate. The exceedingly low R² (0.10) means AKAM's returns are driven by company-specific earnings events, not market exposure; that makes beta-based risk budgeting almost useless here and puts event-gap risk at the center of the risk case.

---

### 3. Composite Quant Signal: **NEUTRAL (leaning Sell)**

Weighted composite (value 25%, momentum 25%, quality 25%, low-vol 15%; revisions excluded as unusable): **z ≈ –0.32** (≈ –0.16 if low-vol is re-based to ~37%). Slightly below peer median.

The factor set is almost perfectly internally hedged: **#1 of 3 on value, #3 of 3 on momentum and quality.** Cheap-and-deteriorating is a classic value-trap configuration, and I weight that negative: the four-year ROIC decline (9.0% → 5.3%) and 470bp gross-margin compression are the causal mechanism behind the multiple being 13x EV/EBITDA — the discount is largely *deserved*, not mispriced. What prevents a "Sell" is real balance-sheet cash generation (accruals –0.093, OCF 3.4x net income) and genuine multiple support at 13x EV/EBITDA / 16.9x P/FCF.

**I would need two things to upgrade to Buy:** (1) evidence of gross-margin stabilization or inflection in the compute/delivery mix, and (2) at least one quarter of positive same-period EPS revisions. I would need a break below the April 2025 low (~$68) on deteriorating fundamentals to move to Sell.

---

### 4. Key Quant Risk Flags

1. **Momentum reversal / value-trap risk (highest severity).** 12-1 momentum –11.8%, ranked last of 3, with price 15% below the Feb 2025 close high. Cheapest name in the group with the worst momentum and worst quality — the empirical signature of a value trap, not a value opportunity.
2. **Earnings-event gap risk (severity: high, not captured by the vol feed).** Three single-day moves of –21.7%, –10.8% and +14.7% in 12 months. With R² of only 0.10, essentially all risk is idiosyncratic — position sizing on market beta will materially understate true risk.
3. **Quality decay / ROIC below hurdle.** ROIC 5.29% and falling 4 straight years; leverage flag on Piotroski negative. EV $17.53B vs mkt cap $11.80B implies **~$5.7B net debt ≈ 4.3x EBITDA** — unusual for a software-infrastructure name and a cap on re-rating.
4. **Factor crowding: not a concern.** AKAM sits at the crowded *short* end of momentum and is a value-tilted contrarian name; crowding risk is low, contrarian crowding-out risk (persistent derating) is the live one.
5. **Liquidity: adequate.** ~1.5M avg daily volume, ~$130M/day traded — no capacity constraint for most mandates.
6. **Data-quality flags (must be disclosed in the memo).** (a) Risk module vol/drawdown/return irreconcilable with raw OHLC; (b) quote mismatch $80.29 vs $87.25 close — valuation ratios (P/E 26.2, EV/EBITDA 13.1) are computed on a stale price and should be refreshed; (c) revision score mis-specified as cross-period growth on a 4-analyst sample; (d) peer set limited to n=3, so all ranks/z-scores lack statistical significance and should not be used for quintile portfolio construction.

**Bottom line:** Quant case is *cheap but broken* — Neutral, tilt Sell. Value is the only factor with untainted support; momentum, quality and the genuine broker-revision direction are all negative, and the headline "+17.4% upgrade" signal is a calculation artifact rather than evidence of rising estimates.

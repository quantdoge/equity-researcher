# Quant Analyst

- Symbol: MU
- Elapsed: 58.7s

---
# MU (Micron Technology) — Quantitative Factor & Risk Report

**Reference price:** latest close **$1,064.94** (2026-09-30). ⚠️ See data-integrity note — the valuation module supplied a stale $594.51.

---

## 1. Factor Scores

| Factor | Score / Raw | Sector Rank (est.) | Signal |
|---|---|---|---|
| **Value** | P/E **14.4**, P/B **8.80**, EV/EBITDA **10.8**, P/FCF **20.6** (at $1,064.94) | Top quintile vs semis (NVDA/AVGO/TSM trade 25–40× earnings) | **Positive** |
| **Momentum** | +688% 12‑1 (raw series) vs **−7.6%** (tool) — irreconcilable | Top decile on raw price data | **Positive, unreliable** |
| **Quality** | ROE 61.4%, ROA 43.4%, ROIC 69.2%, GP/A 0.549, accruals −2.4%, **F-Score 8/9** | Top quintile | **Strong positive** (peak-cycle caveat) |
| **Low Vol** | Vol 88.9% ann., beta **3.44**, max DD 51% | **Bottom quintile** | **Strong negative** |
| **Earnings Revision** | Tool: −100% → **artifact** (see note) | n/a — cannot rank | **Neutral / unverifiable** |

**Value detail:** the reported P/E of 8.0 / EV/EBITDA of 5.89 use $594.51. Restating at the actual close: P/E 8.0 × (1064.94/594.51) = **14.4**; P/B **8.80**; EV/EBITDA **10.8**; P/FCF **20.6**. It is cheap on trailing earnings, but that earnings base is the cyclical peak.

**Quality trajectory (the key nuance):** ROIC −9.9% (FY23) → 2.2% (FY24) → 14.1% (FY25) → **69.2% (FY26)**. An F-Score of 8 is genuinely earned, but this is *peak-cycle* quality in a memory upcycle, not structural quality. Only F7 (no dilution) fails.

**Momentum conflict:** the tool's −7.6% is contradicted by the OHLCV series (2025‑09‑03 $118.51 → 2026‑09‑01 $933.29 ≈ **+688%**; +11% in the last month; −12% off the 52‑week high of $1,213.18). I cannot reconcile the tool output and treat it as unusable; on raw data momentum is strongly positive.

**Revision artifact:** the −100% "downgrade" compares FY2031 (EPS $0.00, 8 analysts, **zero EPS coverage**) against FY2030's $267.29. Meaningless. The genuine estimate curve is steeply upward: FY26 $73.85 (22 analysts, ±5% dispersion → high confidence) → FY27 $175.61 → FY28 $211.13 → FY29 $217.90 → FY30 $267.29 (**only 6 analysts — thin**). No valid 3-month revision history was obtainable.

---

## 2. Price Statistics (252‑day window, vs SPY)

| Metric | Value |
|---|---|
| Alpha (annualised) | **+79.0%** — but t ≈ **1.1**, *not statistically significant* (see below) |
| Beta | **3.454** (SE ≈ 0.29 → significant); profile 5y beta 2.37 |
| R² | **0.346** — only 35% of variance is market; 65% idiosyncratic |
| Sharpe (0% rf) | **0.971** (≈0.94 at a 4% risk-free rate) |
| Sortino | **1.571** — downside/upside asymmetry is favourable |
| Annualised return / vol | 87.2% / 89.8% |
| Annualised volatility | 88.9% |
| Max drawdown | 51.0% |

**Alpha significance test:** residual vol = 89.9% × √(1−0.346) = **72.6%**; SE(alpha) ≈ 72.6%/√1yr → t = 79.0/72.6 = **1.09**. The headline alpha is *statistically indistinguishable from zero* — with a 3.45 beta, what looks like alpha is largely levered cyclical market exposure over a single, favourable 252-day regime. **One window, one regime — no multi-period robustness.**

---

## 3. Composite Quant Signal: **BUY**

Three of five factors are strongly positive (quality top quintile, value top quintile, momentum top decile on raw data) — the rare triple the framework rewards. Held back from Strong Buy by a **bottom-quintile low-vol score** and by the fact that the quality and value signals are the *same* bet: peak-cycle memory earnings. Composite ex-volatility = Strong Buy; risk-adjusted composite = **Buy**.

---

## 4. Key Quant Risk Flags

1. **Peak-cycle earnings risk (highest).** P/E is 14.4 on FY26 EPS but **6.1 on FY27** and ~4.0 on FY28. The market is already discounting deceleration. If FY26–27 estimates are cycle peaks, the entire value factor score is an illusion — this is the classic memory trap. 69% ROIC is not sustainable.
2. **Momentum reversal / drawdown.** ≥4 separate >20% corrections in 12 months; a **−39% peak-to-trough** (peak $1,213 → $739) in Jul 2026. Momentum + beta 3.45 is precisely the profile that suffers violent reversals.
3. **Factor crowding / thematic concentration.** Beta 3.44 and R² 0.35 mean MU is a levered, non-diversifying bet on the AI capex cycle. Highly correlated with the same crowded semis complex.
4. **Volatility vs. risk budgets.** 88.9% annualised vol → a risk-parity or vol-targeted sleeve will size this to near-zero. Max drawdown 51%. Do not size by market-cap weight.
5. **Estimate coverage cliff.** FY27 has 25 analysts, FY28 23, FY30 only 6, FY31 none. Beyond two years the "growth" in the estimate curve is not investable information.
6. **Data integrity (material):**
   - Valuation module price $594.51 vs. $1,064.94 last close → **P/E, P/B, EV/EBITDA all understated ~1.79×**. Market cap reports $672–680B; at the true close it is **~$1,217B** on 1.143B diluted shares.
   - Reported max drawdown of 51% is inconsistent with the OHLCV series (max observed ≈ −39%). Stat-tool series appears to differ from the price feed.
   - **MU is absent from all three `rank_universe_by_factor` outputs** (universe_size 25, only 16–24 names scored) despite top-quintile quality metrics — so **true cross-sectional quintile ranks could not be computed**. Sector ranks above are inferred from peer multiples (NVDA, AVGO, TSM, AMD, SKHY), not from a genuine cross-sectional z-score. This is the largest analytical gap in this report.
7. **Sample size.** All risk statistics are single-window, 252 trading days, in a once-a-decade upcycle. Sharpe, Sortino, beta, and alpha should be treated as regime-specific, not as expectations.

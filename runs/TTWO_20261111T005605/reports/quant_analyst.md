# Quant Analyst

- Symbol: TTWO
- Elapsed: 40.0s

---
# TTWO — Quantitative Factor Report
**Take-Two Interactive Software, Inc.** | Technology / Electronic Gaming & Multimedia | Price used by ratios engine: **$224.64** | Mkt cap **$41.6B** | EV **$42.6B**

> ⚠️ **Data integrity note up front:** the price history pull ends 2026-03-31 at **$197.50**, while the valuation engine uses **$224.64** — a ~+13.7% gap implying the stock has rallied since. All return/risk statistics below are reported as returned by each tool, and I flag where they disagree materially. Do not treat the momentum number as current.

## 1. Factor Scores

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | P/E n/a (GAAP loss), EV/EBITDA **34.3x**, P/FCF **90.2x**, P/B **11.85x** | **Not computable** (peer multiples corrupt — see below) | **Negative / Expensive** |
| **Momentum** | **-18.29%** (12-1, 252d); **-6.08%** (6-1, 126d) | **5 of 5** | **Negative** |
| **Quality** | ROE **-8.49%**, ROIC **-1.68%**, GP/Assets **0.406**, accruals **-0.098** | **4 of 5** | **Neutral-negative** (negative ROE, but conservative accruals) |
| **Low Vol** | Vol **36.9%**, Beta **0.477**, MaxDD **26.4%** | **3 of 5** (2nd lowest beta ex-EA) | **Neutral / Mild positive on beta** |
| **Earnings Revision** | **-19.35%** on FY2031 EPS (9.46 vs 11.73) | n/a | **Downgrade — but unreliable** |

**Peer group (5):** TTWO, EA, RBLX, SONY, NTDOY. *Why not the sector list:* `get_sector_peers` returns "Technology" = AAPL/NVDA/MSFT/TSM — mega-cap semis, not gaming. Even within the true peer set the data is broken:
- **EA:** P/E, EV/EBITDA, P/FCF all `null`; vol 6.21%, beta **-0.045** → price pinned by the pending take-private. **Excluded from vol/momentum ranking.**
- **SONY / NTDOY:** P/E **-0.49** and **0.14**, EV/EBITDA **-0.14** → corrupted ADR/cross-currency fields. **Unusable for value.**
- **RBLX:** negative EBITDA, ROE -284% → not a multiple-based comp.

⇒ **No valid cross-sectional value rank exists.** Treat the value assessment as absolute, not relative.

**Revision signal caveat:** the tool compared FY**2031** consensus ($9.46, only **4 analysts**) against $11.73 — which is the FY**2030** estimate, i.e. **different fiscal years**. That is a period mismatch, not a revision. The cleaner read is the **deterioration in sell-side targets**: UBS cut to $295, BTIG cut to $262, Wedbush cut to $280 in Nov 2026 — directionally negative, magnitude modest.

## 2. Price Statistics

| Metric | 252-day | 504-day |
|---|---|---|
| Alpha (annualised, vs SPY) | **+2.74%** | **-4.97%** |
| Beta (vs SPY) | 0.479 | 0.519 |
| **R² vs SPY** | **0.035** | **0.043** |
| Sharpe | 0.812 | 0.098 |
| Sortino | **1.449** | 0.143 |
| Annualised vol | 34.9% | 32.0% |
| Annualised return | +28.33% | +3.14% |
| Max drawdown | 26.41% | 27.68% |

**The single most important number here is R² = 0.035–0.043.** Only **3–4% of TTWO's variance is explained by the market.** Beta 0.48 says "defensive," but 36% annualised vol says "high risk." Both are true: the risk is **almost entirely idiosyncratic** (GTA VI timing/execution), not market risk. That is why a low beta coexists with a Sharpe below 1 and a Sortino that is the only genuinely attractive risk statistic (1.45 — downside deviation is well-contained relative to upside).

**Tool disagreement flag:** `calculate_price_volatility` returns Sharpe **0.227** (252d) where `calculate_sharpe_sortino` returns **0.812** for the same window — a 3.6x discrepancy from differing return-averaging conventions. The 504d pair (0.143 vs 0.098) is closer. **Conclusion: Sharpe is somewhere in 0.1–0.8; the true figure is probably ~0.2–0.4.** Do not quote a single Sharpe without this range.

**Drawdown verified from raw prices:** peak close **$262.29** (2025-10-20) → trough **$189.69** (2026-03-27) = **-27.7%**, matching the 504d figure. 52-week closing range **$189.69–$262.29**; price sits ~**2.5% off the 52-week low**.

## 3. Composite Quant Signal: **NEUTRAL**

**The factors disagree, and that disagreement is the finding.**

**Bearish:** worst-in-peer momentum (-18.3%), trailing multiples that are indefensible on GAAP numbers (P/FCF 90x, P/B 11.9x), negative ROE/ROIC, negative revision drift in price targets, price 12% below an approximate 200-day mean and 2.5% off the 52-week low.

**Bullish/offsetting:**
- **Forward multiples compress violently.** FY2027E EPS $7.06 → fwd P/E **31.8x**; FY2028E $10.12 → **22.2x**; FY2028E EBITDA $3.19B → EV/EBITDA **13.4x**. The "34x EBITDA" headline is a trailing artifact of a pre-launch release schedule.
- **Consensus PT $292.5 (median), range $262–$330 → ~+30% above spot.** Every one of the six targets sits above the current price, even the lowest.
- **Cash generation is real:** OCF **+$624M** vs net income **-$298M**; accruals **-0.098** (negative = conservative, high-quality earnings). F-Score **7/9**.
- **Sortino 1.449** — the risk-adjusted profile is better than the Sharpe suggests.

**Ranks: Value 5/5, Quality 4/5, Low-Vol 3/5, Momentum 5/5.** No factor confirms a buy; the PT gap and forward estimates prevent a sell. Neutral.

## 4. Key Quant Risk Flags

1. **Momentum reversal / falling knife.** -18.3% on 12-1, -6.1% on 6-1, and still deteriorating into the latest data. Negative momentum in a name with 3.5% R² has no market beta to bail it out. **No momentum confirmation exists for entry.**
2. **Single-catalyst concentration risk (the dominant risk).** With R² = 0.04, ~96% of variance is firm-specific. That is functionally a binary bet on one product launch, not a diversified equity exposure. Any factor model will systematically **understate** this name's risk because beta-based risk models cannot see it.
3. **Factor crowding: LOW — but so is liquidity of the signal.** Peer correlations are remarkably low (TTWO–EA **0.14**, TTWO–SONY **0.25**, TTWO–NTDOY **0.26**; highest is TTWO–RBLX **0.41**). There is no gaming-sector factor cluster to be crowded in. The trade-off: no sector factor to hedge with, and **no peer-based valuation anchor** since comparable multiples are unavailable.
4. **Negative book equity trajectory.** ROE -8.49% looks mild only against FY2025's **-209.5%** and FY2024's **-66.1%** — those are goodwill-impairment artifacts. ROIC has been negative in **all four** annual periods (-1.68%, -11.84%, -12.43%, -9.18%). Capital destruction is improving but not resolved.
5. **Dilution.** F-Score component F7 (no dilution) = **0**; shares at 185.3M. Combined with F1 (positive ROA) = 0, this caps the F-Score at 7 and means per-share value creation is being partially offset by share issuance.
6. **Small-sample revision data.** FY2031 estimate rests on **4 analysts**; FY2030 on 3. Statistically meaningless for a revision-momentum signal — I would not weight it.
7. **Model risk in the data itself.** Three independent discrepancies this run (price $197.50 vs $224.64; Sharpe 0.227 vs 0.812; ADR multiples negative). Any backtest using these feeds needs cross-validation before capital is committed.

---
**Bottom line:** TTWO scores poorly on every factor that is reliably measurable (value, momentum, quality) and adequately only on beta — which is misleading given 96% idiosyncratic variance. It is a **negative-momentum, expensive-on-trailing-numbers, cash-generative, negative-ROIC** name where the entire thesis rests on forward estimates not yet proven. **Neutral, not Buy.** For a factor portfolio, TTWO is a *short on momentum and value* and a *long only on the estimate-revision reversal that has not yet occurred*. The quant case would turn positive on: (a) 12-1 momentum crossing zero, or (b) two consecutive upward FY2027 EPS revisions. Neither is present.

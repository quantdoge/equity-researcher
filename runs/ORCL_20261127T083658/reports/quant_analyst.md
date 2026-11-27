# Quant Analyst

- Symbol: ORCL
- Elapsed: 52.7s

---
# ORCL — Quantitative Factor & Risk Report
**As of last close: $103.88 (2026-11-25) | Mkt cap $302.7B | EV $427.0B | Sector: Technology / Software–Infrastructure**

---

## 1. Factor Scores

Scores are normalized 0–100 (50 = sector median). Ranks are ordinal within the fetched mega-cap comparable set (**n = 4**: ORCL, MSFT, AVGO, NVDA/AMD partial) — these are **not true sector quintiles**; treat rank as directional only.

| Factor | Score | Sector Rank | Signal |
|---|---|---|---|
| **Value** | **60** | **1 / 4** (cheapest on earnings) | **Positive, conditional** — P/E 17.8 & EV/EBITDA 12.8 vs MSFT 27.3/17.9 and AVGO 63.1/43.5. But P/FCF **−12.8** (negative FCF) invalidates the cash-based leg. |
| **Momentum** | **35** | **2 / 4** | **Negative / deteriorating** — 12-1 momentum +1.6% (rank 2 of 4: MSFT +10.5%, ORCL +1.6%, NVDA −1.9%, AVGO −7.3%), but last 21 sessions **−20.4%**. The positive 12-1 print is a stale artifact of the exclusion window. |
| **Quality** | **45** | **3 / 4** | **Deteriorating** — ROIC 10.3% (14.8→14.1→**10.3** over FY24–FY26), GP/assets 16.9% vs MSFT 29.7%, Piotroski **5/9**. Offsets: ROE 39.7%, accruals **−5.7%** (strong cash conversion). |
| **Low Vol** | **8** | **4 / 4** (worst) | **Strongly unattractive** — vol 63.4%, beta 2.27, max DD −58.9% (vs MSFT 34.6% / 0.93 / −23.4%). |
| **Earnings Revision** | **65** *(low confidence)* | **1 / 4** | **Upgrade (+33.3%)** — but computed on **FY2031** EPS (27.06 vs 20.29), a **6-analyst** far-dated estimate. Do **not** treat as a near-term revision signal. |

**Estimate trajectory (current vintage, all same-date — no true revision series available):** FY26 7.49 → FY27 8.15 → FY28 11.10 → FY29 15.77 → FY30 20.29 → FY31 27.06 = **+29.3% EPS CAGR**. Revenue FY26 $67.3B → FY31 $264.0B (+31.5% CAGR). Analyst coverage decays from 24–25 (FY26–28) to **6 (FY31)** — the long tail of the consensus is thinly supported.

Forward multiples at $103.88: FY27 **12.7x**, FY28 **9.4x**, FY29 **6.6x**, FY30 **5.1x**, FY31 **3.8x**.

---

## 2. Price Statistics

| Metric | Value |
|---|---|
| Trailing 12m return | **−27.31%** (annualised, 252d) |
| Alpha vs SPY (annualised) | **−49.49%** |
| Beta vs SPY | **2.28** (2.272 / 2.283 across two estimators); 5yr monthly β 1.78 |
| R² vs SPY | **0.332** → **67% idiosyncratic** |
| Annualised vol | **63.4%** |
| Sharpe (0% rf) | **−0.428** (alt. annualisation: −0.497) |
| Sortino (0% rf) | **−0.809** → downside deviation ~33.8% |
| Max drawdown | **−58.93%** — peak close $246.38 (2026-06-01) → trough $101.19 (2026-11-20), ~5.7 months |
| Current vs trough | +2.7% off the low |

*Consistency check:* α = −49.5% with β = 2.28 implies the benchmark returned ≈ **+9.7%** over the window — consistent with MSFT's +10.5% 12-1 momentum. The decomposition is internally coherent; the underperformance is stock-specific, not market-driven.

**Momentum character:** the 12-month loss is almost entirely concentrated in the last month (−20.4% in 21 sessions). This is the signature of a **momentum crash** following a parabolic ramp (Feb–Jun 2026: ~$140 → $246), then a −59% round trip. Momentum factor exposure is currently *negative in realization but positive in raw score* — a classic trap.

---

## 3. Composite Quant Signal

**Composite = 0.25·Value + 0.25·Momentum + 0.25·Quality + 0.10·LowVol + 0.15·Revisions**
= 15.0 + 8.75 + 11.25 + 0.8 + 9.75 = **45.6 / 100**

### → **NEUTRAL** (band 40–60), with negative skew

The score is held up entirely by *cheapness on accounting earnings* and a *thin, stale revision print*. Every risk-based and trend-based factor is negative. This is not a factor-cluster you should add beta to; it is a **cheap-on-GAAP-earnings, expensive-on-cash, high-beta name in an active downtrend**.

**Analyst cross-check (informational, not a factor):** median price target across the 6 most recent notes ≈ **$211** (+103% vs spot), range $170–$285. Dispersion is extreme (coefficient of range ≈ 54% of median) and **all targets predate the 2026-11-20 crash to $99** — they are stale. Ratings skew positive (Stephens upgrade to Overweight, Baird Outperform, Citizens Market Outperform, Melius Buy) with targets being *cut* (Scotiabank → $205, Wells Fargo → $250). Wide dispersion + falling targets + positive ratings = disagreement, not conviction.

---

## 4. Key Quant Risk Flags

1. **Negative free cash flow — the dominant risk.** P/FCF **−12.78** implies FCF ≈ **−$23.7B** against OCF of $32.0B, i.e. **capex ≈ $55.7B**, up from ~$2.4B of FCF headroom in prior years. Earnings are real (accruals −5.7%, OCF > NI by $14.9B) but they are being fully re-invested and then some. Funding gap implies continued debt issuance (sell-side already flags "high leverage"). **Any value thesis must be underwritten on FCF inflection, not P/E.**

2. **Momentum reversal — partially realized, not resolved.** −58.9% peak-to-trough with the last month −20.4% and no basing pattern. Do not assume mean reversion; high-beta, high-vol names in drawdown exhibit continuation (vol 63.4% ⇒ ~4% daily σ).

3. **Factor crowding / AI-capex proxy contamination.** ORCL's correlation with NVDA is **0.484** — *higher than NVDA's correlation with MSFT (0.216)*. Average ORCL peer correlation **0.471**, the highest in the group. ORCL is trading as an **AI-infrastructure capex proxy**, not as defensive software. It offers no diversification against an AI-capex de-rating.

4. **Quality destruction is measurable and accelerating.** ROIC −446bp YoY (14.1% → 10.3%); ROA 7.39% → 6.53%; gross margin and asset turnover both failed their Piotroski tests. ROE (39.7%) is flattered by a shrinking equity base — not a quality signal.

5. **Estimate fragility / small sample.** The +33.3% "revision" rests on n = 6 analysts for FY2031; FY29–31 estimates carry 6–13 analysts vs 24–30 for near years. A +29% 5-yr EPS CAGR is priced *nowhere* in a 12.7x FY27 P/E — implying the market either disbelieves the ramp or is discounting the financing cost of it. Both readings argue for wide outcome dispersion.

6. **Liquidity: not a constraint.** ~$10.8B ADV (38.5M shares on the last session) — institutional-size entry/exit available. No liquidity flag.

---

## Data Gaps (honest disclosure)
- **True sector quintile ranks unavailable** — peer factor scores fetched for only MSFT/AVGO/ANT/NVDA/AMD. Ranks above are ordinal on n=4, not quintiles.
- **Near-term revision momentum not measurable** — no time series of FY27/FY28 consensus; the revision tool returned a far-dated, thin-coverage figure only.
- **53-week price series truncated** to 2026-03→11-25; the pre-March 2026 peak is inferred from the −58.93% max-drawdown identity (reconciles exactly to closes of $246.38 / $101.19), not directly observed.
- Sharpe reported by two tools at −0.428 and −0.497 (differing annualisation conventions); both are equally consistent with a −27% return and 63–64% vol.

**Bottom line: Neutral (45.6/100). The only defensible long case is a value-on-forward-earnings case at 12.7x FY27 with a 29% implied EPS CAGR — and it requires believing the capex cycle inflects before the balance sheet does. The quant evidence does not yet support that; it supports watching for a stabilisation in FCF and a break in the downtrend.**

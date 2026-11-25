# Fin Risk Analyst

- Symbol: ALAB
- Elapsed: 73.9s

---
# ALAB — Astera Labs, Inc. | Complete Financial Risk Assessment

**As of:** 20 Nov 2026 | **Price:** $180.35 | **Mkt cap:** ~$31.4B (174.1M sh) | **Sector:** Technology / Semiconductors
**Latest financials:** Q3 FY2026 (period end 30 Sep 2026, filed 4 Nov 2026). IPO 20 Mar 2024 — limited history.

> ⚠️ **Methodology note:** the ratio tools (`calculate_leverage_ratios`, `calculate_liquidity_ratios`, `calculate_altman_z_score`, `calculate_piotroski_f_score`, `calculate_fcf_yield`) all resolve to the **FY2025 annual period (31 Dec 2025)** — three quarters stale. ALAB has transformed since then. Where material I recompute on TTM through Q3 FY2026 and show both.

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (effectively debt-free / fortress balance sheet)**

| Item | Value (Q3 FY2026) |
|---|---|
| Total debt | **$0** (FY2025: $35.1M of what appear to be lease obligations) |
| Cash, equivalents & ST investments | $1,378.2M |
| Net cash | +$1,378.2M (≈4.4% of market cap) |
| Total liabilities | $300.9M (13.1% of assets) |
| Equity / assets | 0.87 |
| Interest expense | $0 — **interest coverage is N/A (infinitely covered)** |
| TTM EBIT | $397.1M |

There is **no refinancing cliff, no maturity schedule, no covenants, and no credit rating or CDS spread** (unrated — a data gap, though a rating is largely moot with zero debt).

**Critically, net interest income is a *positive* earnings contributor, not a cost.** In Q2 FY2026 net income of $153.1M exceeded operating income of $89.2M by ~$64M — implying roughly **$250M/yr of non-operating interest income**, ~14% of pre-tax earnings. This is a hidden vulnerability: falling short rates are an earnings headwind, and it means GAAP net margin (29.6%) overstates operating quality.

**Altman Z-Score: 6.86 (FY2025, Safe zone)** — I re-ran it on Q3 FY2026 TTM and get **Z ≈ 6.39**, still deep in the safe zone (>2.99). Both readings understate safety: x4 uses *book* equity ($2.0B) versus ~$31.4B market value; on market equity the Z-score is orders of magnitude above threshold. Bankruptcy probability is effectively nil.

**Interest coverage reported as `null`** by the tool — this is not a data failure in the usual sense; it reflects the genuine absence of interest expense.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (tool) | TTM Q3 FY2026 (recomputed) | Assessment |
|---|---|---|---|
| Debt / equity | 0.03 | **0.00** | Negligible |
| Net debt / EBITDA | **-5.13x** (net cash) | Net cash | ⬤ Excellent |
| Debt / assets | 0.02 | 0.00 | Negligible |
| Interest coverage | n/a | n/a (no debt) | ⬤ Excellent |
| Current ratio | 10.24 | **8.03** | ⬤ Excellent |
| Quick ratio | 9.79 | **7.20** | ⬤ Excellent |
| Cash ratio | 8.94 | **5.66** | ⬤ Excellent |
| Working capital | $1,228.9M | $1,711.6M | ⬤ Excellent |
| Altman Z | 6.86 Safe | ~6.39 Safe | ⬤ Excellent |
| **Piotroski F** | **6 / 9 "Moderate"** | not computed (stale) | ◐ Mixed |
| Operating margin | 20.3% | **25.5%** | ⬤ Improving |
| Gross margin | 75.7% | 73.9% | ◐ Compressing |
| FCF (TTM) | $281.8M | **$344.7M** | ⬤ Strong |
| FCF margin | 33.0% | 22.2% | ◐ Declining |
| ROA | — | 20.1% (TTM) | ⬤ Strong |

**Piotroski detail (FY2025, score 6).** Points earned: positive ROA, positive operating cash flow, ROA improvement, accruals quality, positive equity change, asset-turnover improvement. **Points lost — all three deserve attention:**
- **F5 lower leverage (0):** leverage rose (lease obligations, FY2025 vs FY2024)
- **F7 no dilution (0):** share count is rising
- **F8 gross margin improvement (0):** GM fell 76.4% → 75.7% in FY2025, and has continued to 73.9% TTM

The F-Score is directionally understated because it predates FY2026's step-change, but the dilution and margin-compression deductions are *structural*, not timing artifacts.

**Growth context (why margins matter):** Q3 FY2026 revenue $584.9M, **+153.7% YoY** and **+49% QoQ**. FY2025 revenue $852.5M (+115% YoY). This is hyper-growth decelerating gross margin — a classic signature of scaling into a concentrated, price-sensitive hyperscaler customer base.

---

## 3. Market Risk Profile — **This is where the risk lives**

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (252d) | **105.7%** | Top-decile; ~6x broad market |
| **Beta vs SPY** | **4.13** (profile: 3.86) | Extreme systematic sensitivity |
| **Max drawdown (252d)** | **-62.8%** | And it is **currently live**, not historical |
| Sharpe ratio (0% rf) | 1.06 | Looks adequate, but see caveat |
| Sortino ratio | **Not available** | Data gap — no downside-deviation tool |

**Drawdown is contemporaneous, not historical.** 52-week high $483.02 (30 Jun 2026) → $180.35 today = **-62.7%**, i.e. the stock is sitting *at* its max-drawdown low. It is simultaneously **+80% off** the March 2026 closing low of $100.27. This is a security that has round-tripped a 5x advance and a 63% collapse inside twelve months.

**Path of the collapse is instructive:** a -19.6% single-session gap on 5 Nov 2026 (12.0M shares, 2x normal volume — the post-Q3 earnings reaction), a rebound to $230.91 by 11 Nov, then -14.8% on 20 Nov to close at $180.35 on 7.97M shares. Daily realized moves of 10–20% are routine. Liquidity is adequate ($0.8–1.5B daily dollar volume) — no liquidity risk in the tradable sense.

**Sharpe caveat:** with 105.7% volatility, the arithmetic-mean-based Sharpe of 1.06 implies an annualised arithmetic mean return near +112%, which is wildly divergent from the actual buy-and-hold outcome (-5.9% from Nov 2025 to Nov 2026). The ratio is being distorted by the volatility denominator and should **not** be read as evidence of good risk-adjusted returns.

**Beta of 4.13 means a garden-variety 10% market drawdown implies ~-41% on ALAB**, before any idiosyncratic event.

---

## 4. Downside Scenario Analysis — Revenue -20%

Base TTM: Revenue $1,556.2M | Gross margin 73.9% | Opex $752.8M (48.4% of revenue; SG&A $226.6M + R&D ~$526M) | EBIT $397.1M (25.5%) | **Operating leverage = GP/EBIT = 2.90x**

*A 20% revenue decline mechanically cuts EBIT ~58% if gross margin holds and opex is frozen.*

| Scenario | Revenue | GM | Opex | EBIT | Margin | FCF (est.) | Cash runway |
|---|---|---|---|---|---|---|---|
| **Base (TTM)** | $1,556M | 73.9% | $753M | **$397M** | 25.5% | +$345M | n/a (net cash) |
| **A: -20% rev, GM held, opex flat** | $1,245M | 73.9% | $753M | **$167M** | 13.4% | ~+$97M | No issue |
| **B: -20% rev, GM→70%, opex +10%** | $1,245M | 70.0% | $828M | **$43M** | 3.5% | ~breakeven | No issue |
| **C: -40% rev (AI capex bust), GM 68%** | $934M | 68.0% | $753M | **-$118M** | -12.6% | ~-$152M | **~9 yrs** |

**Conclusion: every realistic downside is a P&L and equity-valuation event, not a solvency event.** In the harshest case (Scenario C) the company burns ~$152M/yr against $1,378M of cash with zero debt — roughly nine years of runway, no covenant triggers, no forced refinancing. It could survive a prolonged multi-year downturn on the current balance sheet alone.

**The real downside is valuation, not viability.** At $180.35 the market still pays:
- **72.8x EV/EBITDA** (EV $30.0B / EBITDA $412.6M)
- **68.1x P/E** (TTM NI $461.3M)
- **20.2x P/S** (TTM revenue $1,556M)
- **FCF yield 1.10%** — and just **0.34%** on SBC-adjusted FCF

A -20% revenue scenario compresses *both* the earnings base (EBIT -58%) and the multiple simultaneously. Cutting 58% of EBIT alongside a de-rating from 68x to a still-generous 25x P/E implies **~-85% downside on the equity** while the company remains perfectly solvent. That asymmetry — not default risk — is

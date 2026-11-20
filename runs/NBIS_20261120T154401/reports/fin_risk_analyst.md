# Fin Risk Analyst

- Symbol: NBIS
- Elapsed: 73.7s

---
I have enough to complete the assessment. Note the core tension: NBIS is a **hyper-growth, debt-funded AI infrastructure build** where "distress" metrics and "strong" metrics coexist. Here is my assessment.

---

# NBIS — Nebius Group N.V.
## Financial Risk Assessment | Data as of Q3 2026 (period end 2026-09-30) | Price $87.28, Mkt Cap $20.9B

> **Data note:** The platform's ratio tools (`calculate_leverage_ratios`, `calculate_liquidity_ratios`, `altman`, `piotroski`, `fcf_yield`) all keyed off **FY2025 (2025-12-31)** and are therefore **nine months stale** — a critical span in which total debt tripled from $5.0B to $16.1B. I have recomputed TTM/current metrics from the Q3 2026 filings below and present tool values only for comparison.

---

## 1. Credit Risk Assessment

**Rating: Sub-Investment Grade (high-risk build-finance credit)**

Leverage is the dominant risk. Total debt went **$0.05B (FY2024) → $5.0B (FY2025) → $9.6B (Q1'26) → $10.1B (Q2'26) → $16.1B (Q3'26)**, with the $16.1B including ~$5.75B of convertible notes closed in August 2026. Net debt: **$8.65B**. Against TTM adjusted EBITDA of just **$547M**, that is **15.8x** — an unsustainable multiple on trailing earnings, though it falls to **~5.3x** on annualized Q3 EBITDA of $1.62B (Q3'26 was the first quarter of positive operating income).

The more damning metric is **interest coverage on an EBIT basis**. Q3'26 D&A annualizes to ~$1.42B against ~$1.62B of run-rate EBITDA — EBIT is only ~$200M. Forward cash interest is ~$560M/yr (16.1B at a ~3.5% blended cost, low because the bulk is low-coupon convertibles). **EBIT/interest ≈ 0.4x.** The company does not service interest out of earnings; it services it from financing proceeds. That is a financing-model credit, not a cash-flow credit.

**Mitigants that prevent a Distress classification:** no near-term maturity wall (**short-term debt only $187.5M vs $7.43B cash**); convertibles are long-dated and low-coupon; operating cash flow is **positive** (+$5.07B TTM, +$4.23B in 9M'26); **$38.7B RPO backlog**; and $9B+ of expected 2026 customer prepayments, which management cites as funding ~70% of Q2 deals.

---

## 2. Key Financial Risk Metrics

| Metric | Q3'26 / TTM (recomputed) | Tool value (FY2025, stale) | Assessment |
|---|---|---|---|
| Total debt | $16,072M | $4,973M | **3.2x in 9 months** |
| Net debt | $8,647M | $1,295M | — |
| Debt / equity | **1.31x** | 1.08x | Moderate, but rising fast |
| Debt / assets | **0.41x** | 0.40x | Stable |
| Net debt / EBITDA (adj.) | **15.8x** | 2.63x | **Severe on trailing** |
| Net debt / EBITDA (Q3 annualized) | **5.3x** | — | High but improving |
| Interest coverage (EBIT) | **≈0.4x fwd / −1.6x TTM** | −9.95x | **Does not cover** |
| Interest coverage (EBITDA) | ~1.75x TTM | — | Thin |
| Current ratio | **5.31x** | 3.08x | Very strong |
| Quick ratio | **5.31x** | 3.08x | Very strong |
| Cash ratio | **2.99x** | 2.41x | Very strong |
| Working capital | **$10,680M** | $3,184M | — |
| Altman Z-Score | **0.76** (mkt-cap variant 0.95) | 1.096 — Distress | **Distress zone** |
| Piotroski F-Score | ~6–7 (est.) | **8 — Strong** | Stale; F5/F7 now fail |
| FCF (TTM) | **−$12,421M** | −$3,681M | Worsening |
| FCF yield (TTM) | **−59.3%** | −16.85% | Extreme burn |
| Operating cash flow (TTM) | +$5,066M | +$385M | Positive & improving |

**Altman Z caveat:** the Z-Score is structurally biased against this business model. X5 (sales/assets) is only 0.057 because $21.5B of PP&E has been installed against just $2.19B of TTM revenue (asset turnover **0.10x**). Altman penalizes the build phase of an asset-heavy startup precisely when it is behaving rationally. Treat the 0.76 as a signal of *capital intensity and thin revenue coverage of the asset base*, not literal bankruptcy probability. **But it is corroborated directionally by the 15.8x leverage and sub-1x EBIT coverage.**

**Piotroski caveat:** the reported 8/9 is FY2025. Since then, F5 (leverage) remains failed and **F7 (no dilution) now clearly fails** — diluted shares went 251.8M → 298.0M, **+18% in nine months**, including $2.8B raised via ATM in Q2'26 alone.

---

## 3. Market Risk Profile

| Metric | Value | Interpretation |
|---|---|---|
| Annualized volatility (3y) | **114.6%** | ~3–4x a typical large-cap; extreme |
| Beta vs SPY | **2.95** | A 20% market drawdown implies ~59% |
| Max drawdown (3y) | **−69.2%** | Full-scale de-rating already realized |
| Sharpe ratio | 1.184 | High, but entirely return-driven |
| Sortino ratio | **n/a — data gap** | Downside-adj. quality unquantified |

The Sharpe of 1.18 is misleading: with 114.6% volatility, that ratio is earned by extraordinary upside, not stability. Beta of 2.95 on an already 69% max drawdown means **this is a levered bet on the AI capex cycle, not a defensive holding**. The stock has also fallen ~30% in a single month at least once during 2026, and sell-side Buy ratings collapsed from 9 to 3 between March and September 2026 even as price targets rose — a classic divergence signalling rising conviction risk.

---

## 4. Downside Scenario: Revenue −20%

Base: Q3'26 run-rate revenue ~$3.9B (annualized), gross margin 77.6%, run-rate adj. EBITDA $1,620M, D&A $1,419M, interest ~$560M.

| Line item | Base | Revenue −20% | Effect |
|---|---|---|---|
| Revenue | $3,900M | $3,120M | −$780M |
| Gross profit (77.6%) | $3,026M | $2,421M | −$605M |
| Adj. EBITDA | $1,620M | **~$1,015M** | −37% (operating leverage) |
| D&A (fixed) | $1,419M | $1,419M | inflexible |
| **EBIT** | ~$200M | **~−$404M** | **swings negative** |
| Interest | $560M | $560M | fixed |
| Net debt / EBITDA | 5.3x | **8.5x** | likely covenant pressure |
| EBIT coverage | 0.4x | **negative** | — |

**Second-order risks that make the linear math too kind:**
1. **Operating leverage is brutal.** Revenue is capacity-driven (sold-out GPU clusters). A 20% demand shock means utilization collapse, not a proportional cost cut — D&A on $21.5B of PP&E is fixed and rising.
2. **The funding model is pro-cyclical.** 2027 capex of **$40–45B** is planned to be 75–85% funded by **customer prepayments and asset-backed financing**. A demand shock cuts prepayments *and* closes the ABS/convertible market simultaneously — the exact "altnet" failure mode cited by Edward Chancellor and Jim Chanos.
3. **Impairment risk.** Equity is $12.3B against $21.5B of PP&E. A 30% GPU-asset write-down (−$6.4B) **halves book equity** and would likely trigger a technical default if leverage covenants exist.
4. **Convertible duality.** Below conversion price, ~$10B of converts stay as debt and must be cash-settled at maturity — at $87 (vs. $291 average PT) much of this stack is likely out-of-the-money, so it behaves as straight debt, not equity.

**Severe case — capex shutdown:** if buildout halts and growth capex goes to zero, TTM operating cash flow of **+$5.07B** turns the company cash-generative. This is the key asymmetry: **the burn is discretionary expansion capex ($15.4B in 9M'26), not an operating cash deficit.**

---

## 5. Overall Financial Risk Rating: **HIGH**

Not Critical — the liquidity position is genuinely fortress-like (current ratio 5.3x, $7.4B cash, no 12-month maturity wall, positive OCF, $38.7B RPO). But the leverage trajectory (3.2x debt growth in three quarters), sub-1x forward EBIT interest coverage, −59% TTM FCF yield, 114.6% volatility, and explicit dependence on continuous capital-markets and prepayment access place this firmly in the high-risk bucket.

**Cash runway technically:** $7.43B / $3.73B average quarterly 2026 FCF burn = **~2.0 quarters** (~1.0 quarter at the Q3'26 burn of $7.57B). This is *not* a solvency signal — it is a statement that **NBIS must raise external capital roughly every two quarters**, which is precisely what it has been doing via convertibles ($4.3B, $5.75B), ABS ($775M GPU-backed), and ATM equity ($2.8B).

---

## 6. Key Red Flags

1. **EBIT does not cover interest (~0.4x forward).** EBITDA barely exceeds D&A; the entire earnings-to-interest relationship depends on continued scale-up.
2. **Debt $5.0B → $16.1B in nine months**, with net debt/EBITDA at 15.8x trailing.
3. **−$12.4B TTM free cash flow (−59% of market cap)** and accelerating: quarterly FCF −$0.21B → −$3.41B → −$7.57B through 2026.
4. **18% diluted-share growth in nine months** — the F-Score's "no dilution" pass is obsolete.
5. **Funding circularity:** 75–85% of 2027 capex relies on customer prepayments and asset-backed debt; both are cycle-dependent and correlated with the same AI demand shock that would hurt revenue.
6. **Reported EBITDA is flattered.** TTM reported EBITDA of $1,380M includes a ~$807M Q1'26 non-operating gain (net income +$621M on an operating loss of −$128M). Adjusted EBITDA is $547M — **2.5x lower**. Any covenant or screen using reported EBITDA overstates coverage.
7. **Asset turnover of 0.10x** — $21.5B PP&E supporting $2.2B TTM revenue. Impairment risk is structural, not hypothetical.
8. **Beta 2.95 / vol 114.6%** — near-total correlation with the AI capex narrative.

## 7. Explicit Data Gaps
- **No credit rating** found; convertibles of this scale typically imply unrated/high-yield — unconfirmed.
- **No debt maturity schedule** and **no covenant detail** in the available data — this is the single largest blind spot for refinancing-cliff analysis.
- **No convertible coupon/conversion-price terms** — critical for distinguishing debt-like from equity-like treatment.
- **Q3'26 cash flow statement reports D&A = 0 and SBC = 0** (unpopulated fields); Q1/Q2'26 working-capital swings (+$2.1B, +$0.8B) do not reconcile cleanly to net income + D&A, so **operating cash flow quality is unverified** despite being the crux of the bull case.
- Minor inconsistency: FY2025 net income $82.5M (income statement) vs $101.7M (cash flow statement).
- **Sortino ratio unavailable.**

**Bottom line for the memo:** NBIS is a solvency-*adequate*, leverage-*aggressive*, cash-flow-*negative* growth build. The balance sheet can survive a 20% revenue miss for 2–3 quarters, but not a simultaneous prepayment slowdown and capital-markets closure. The equity is best underwritten as a **high-beta, dilution-exposed option on AI infrastructure demand**, not as a financially resilient compounder.

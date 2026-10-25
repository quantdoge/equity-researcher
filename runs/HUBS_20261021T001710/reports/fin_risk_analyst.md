# Fin Risk Analyst

- Symbol: HUBS
- Elapsed: 135.4s

---
# HUBS — Financial Risk Assessment
**HubSpot, Inc.** (Technology / Software–Application) · Price $250.74 · Mkt cap $12.84B
Financials through **Q2 FY2026** (filed 2026-08-05); TTM = Q3'25–Q2'26 unless noted.

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively AAA-quality balance sheet)**

HUBS has **no funded debt**. `short_term_debt = 0` and `long_term_debt = 0` in every period shown; the $236.9M "total debt" line is lease obligations (FY25: $262.3M). There are **no financial covenants, no revolver draw, and no refinancing cliff** — the entire maturity schedule is empty. Cash & short-term investments of **$1,338M** exceed total debt by **$1,101M**.

Interest expense for FY2025 was **$0.876M** on $3.13B of revenue. The company could service its obligations with a ~99% decline in EBIT. Solvency risk is, for practical purposes, zero.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| Total debt / equity | 0.14 (FY25: 0.13) | Negligible |
| Debt / assets | 0.07 | Negligible |
| Net debt / EBITDA | **-3.3x** (net cash $1.10B) | Net cash |
| Interest coverage | 13.0x (tool) / ~80x raw EBIT | No burden |
| Current ratio | **1.38** (12/31/25: 1.67) | Adequate, **deteriorating** |
| Quick / cash ratio | 1.38 / 0.87 | Adequate |
| Working capital | **$584M** (12/31/25: $982M) | **-$399M in 6 months** |
| Cash / total liabilities | 0.72x | Strong |
| Altman Z-Score | **1.598 — "Distress"** | Artifact; see below |
| Piotroski F-Score | **7 / 9** | Strong (fails dilution + GM trend) |
| FCF yield (TTM FCF $767M) | **6.0%** | Good |
| SBC-adj. FCF yield | **2.0%** | Weak — core red flag |
| Equity / assets | 0.47 | Goodwill = 35% of equity |

**On the Altman Z-Score (1.598, "Distress"):** this is a false positive and should not be read as bankruptcy risk. The score is dragged down by two structural items: X2 = **-0.196** (retained earnings/TA, i.e., accumulated deficit of -$678M from years of SBC-funded GAAP losses) and X3 = 0.018 (thin GAAP EBIT/TA). X1 (0.255), X4 (1.156) and X5 (0.812) are all healthy. Substituting **market capitalization** for book equity in X4 — Altman's *original* formulation — gives X4 = 6.95 and a Z of **≈5.07 (safe zone)**. The tool itself flags that it uses book equity and is "indicative only."

---

## 3. Market Risk Profile — **VERY HIGH**

| Metric | Value |
|---|---|
| Annualised volatility (756d) | **59.4%** |
| Beta vs SPY (756d) / profile beta | **1.136 / 1.235** |
| Max drawdown (3y) | **-79.2%** |
| Sharpe (rf = 0%) | **-0.241** |
| Sortino | *Not returned by tool — data gap*; negative Sharpe implies negative Sortino |

**Peak-to-trough:** $819.71 close (2025-02-13) → $170.28 close (2026-06-25) = **-79.2%**. Current $250.74 is +47% off the low but still **-69% below the peak**.

**Earnings gap risk is the dominant exposure**, not gradual drift:
- 2026-08-06: **-19.1%** (Q2 FY26, 8.6M shares)
- 2026-05-08: **-19.0%** (Q1 FY26, 6.5M shares)
- 2025-11-06: **-15.0%** (Q3 FY25)
- 2026-02-11 / 2026-02-03: -9.8% / -10.5%

Parametric 1-day 99% VaR at 59% vol is ~8.7%; **realized tail events reached -19%, roughly 2.2x parametric 99% VaR.** Empirical tails are far fatter than the normal assumption — size positions on gap risk, not VaR. A beta of ~1.14 understates downside participation: HUBS fell 79% while SPY was near highs, so market-neutral hedging would not have protected the book.

---

## 4. Downside Scenario Analysis — Revenue -20%

TTM revenue $3,448.6M @ 83.2% gross margin; opex $2,738.6M of which **$514.7M is SBC** (cash opex $2,223.9M).

| Line | Base (TTM) | -20% revenue | -40% (severe) |
|---|---|---|---|
| Revenue | $3,448.6M | $2,758.9M | $2,069.2M |
| Gross profit loss | — | -$573.8M | -$1,148.0M |
| Cash-opex action assumed | — | -12% (-$266.9M) | -25% (-$556.0M) |
| **FCF (pre-WC)** | **$767.2M** | **$460.3M** | **$175.2M** |
| Deferred-revenue unwind (est.) | — | -$135 to -$180M | -$200 to -$270M |
| **FCF (post-WC)** | **$767.2M** | **~$280–325M** | **~$0–50M** |
| Net cash | $1,101M | $1,101M (cushion) | $1,101M |
| Interest coverage | ~nil interest | unchanged | unchanged |

**Conclusions:** Even a 20% revenue decline leaves HUBS generating ~$300M of FCF (8.7% yield on current cap) with **zero refinancing need**. A -40% decline brings FCF to roughly breakeven — and the $1.1B net cash position plus a fully discretionary $515M SBC line (easily halved) means the company could absorb that for **5+ years without raising capital**. **There is no scenario in which the balance sheet breaks.**

The genuine downside vulnerability is *not* solvency but the **deferred-revenue unwind**: subscription billing front-loads cash, so a bookings slowdown converts a growth tailwind into a working-capital drain. Deferred revenue is not broken out in the feed — I've estimated the balance at ~$900M; treat the WC drag as indicative (**data gap**).

---

## 5. Overall Financial Risk Rating: **MODERATE**

Split by risk type — the single rating masks two very different realities:

| Risk category | Rating | Driver |
|---|---|---|
| Solvency / credit | **LOW** | No debt, $1.1B net cash, nil interest burden |
| Liquidity | **LOW–MODERATE** | Ample cash, but current ratio 1.67→1.38 and WC -$399M in 6 months |
| Earnings quality (SBC) | **MODERATE–HIGH** | SBC = 14.9% of revenue; SBC-adj FCF yield only 2.0% |
| Equity / market risk | **VERY HIGH** | 59% vol, -79% drawdown, -0.24 Sharpe, repeated -19% gaps |
| Business-model disruption | **HIGH (unquantified)** | GM compression + AI-pricing questions drove the de-rating |

---

## 6. Key Red Flags

1. **SBC distorts the cash story.** TTM FCF of $767M is flattered by a $514.7M non-cash add-back. SBC-adjusted FCF is **$252.5M (7.3% margin)**. On $12.84B cap that's a **2.0% yield** — priced like a growth asset, not a cash compounder. *Mitigant: SBC/revenue is falling (16.9% FY25 → 14.9% TTM).*
2. **Buybacks running at ~2x FCF.** H1 FY26 repurchases **$743M vs FCF $386M (192%)**; Q2 alone $536M vs $203M FCF (264%). Cash fell $366M in six months and **working capital fell $399M**. This is discretionary capital consumption, not a debt problem — but it is the reason liquidity ratios deteriorated.
3. **Gross margin is compressing.** Q2 FY26 82.4% vs Q2 FY25 83.9% (**-150bps YoY**); FY25 full-year GM fell 120bps. Piotroski F8 = 0. Combined with the "AI pricing" narrative behind the 2026 selloffs, this is the most important fundamental trend to monitor.
4

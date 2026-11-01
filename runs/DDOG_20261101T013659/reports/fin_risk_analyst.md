# Fin Risk Analyst

- Symbol: DDOG
- Elapsed: 44.7s

---
# DDOG — Financial Risk Assessment
**Datadog, Inc.** | Technology / Software–Application | Price $235.27 (30-Oct-2026) | Mkt cap **$84.5B** | FY end Dec; latest reported = Q2-2026 (6-Aug-26)

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE (effectively: net-cash, unrated)**

DDOG carries essentially no credit risk in the conventional sense. At FY25 year-end it held **$4.47B cash & short-term investments** against **$1.54B total debt** → **net cash of ~$2.94B** (≈$8.3/share, ~0.85x revenue). The debt stack is largely **$1.0B of 0.00% convertible senior notes due 2029** (priced Dec-2024), plus ~$0.5B of residual convertible/lease obligations; FY25 cash interest expense was only **$11.1M**.

Important: the tool-reported **interest coverage of −4.0x** uses *operating income* (−$44.4M), not EBIT. On reported EBIT ($138.1M) coverage is **~12.5x**, and on a *net* basis the company earns more interest on its cash than it pays (net income of $107.7M vs. an operating loss). **No financial maintenance covenants, no near-term maturities** (next scheduled cash event: 2029 converts). There is no public rating or CDS to reference (data gap — the company is unrated; typical for net-cash software issuers).

## 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|
| Revenue ($M) | 3,427.2 | 2,684.3 | 2,128.4 | +27.7% y/y |
| Gross margin | 79.96% | 80.79% | 80.74% | Slight erosion |
| Operating margin | **−1.29%** | +2.02% | −1.57% | Thin GAAP; H1-26 +0.6% |
| Net margin | 3.14% | 6.85% | 2.28% | Interest income dependent |
| EBITDA ($M) | 193.8 | 265.9 | 111.0 | — |
| Total debt / Equity | 0.41x | 0.68x | 0.45x | Low |
| Debt / Assets | 0.23x | 0.32x | 0.23x | Low |
| **Net debt / EBITDA** | **−15.2x (net cash)** | net cash | net cash | No leverage |
| Interest coverage (EBIT / int.) | 12.5x | 29.9x | 10.6x | Adequate |
| Interest coverage (op. income) | −4.0x | 7.7x | −5.3x | Structurally negative on GAAP |
| Current / Quick / Cash ratio | 3.38x / 3.38x / 2.81x | 2.64x | 3.17x | Very strong |
| Working capital | $3.79B | $3.05B | $2.18B | Strong |
| Altman Z (book equity) | **2.07 — Grey** | — | — | Artifact: book-equity x4 = 1.28; using $84.5B market cap, **x4 = 29.0 → Z ≈ 30 (Safe)** |
| Piotroski F-Score | **6 / 9 (Moderate)** | — | — | Fails: ROA improvement, no-dilution, GM improvement |
| FCF ($M) | 1,005.6 | 835.9 | 632.4 | +20% y/y |
| FCF margin | 29.3% | 31.1% | 29.7% | Plateauing |
| **FCF yield** | **1.17%** | — | — | Very low (valuation) |
| SBC / Revenue | **21.9%** ($750.7M) | 21.3% | 22.7% | **Key red flag** |
| SBC-adjusted FCF margin | **~7.4%** | ~9.9% | ~7.0% | "Free" cash flow is mostly SBC add-back |

**The honest read:** leverage and liquidity risk are **negligible**; the Z-score's grey-zone reading is a book-equity artifact, not a distress signal. Diluted shares grew 2.1% (347.3M vs 336.2M weighted) — persistent dilution offsets part of per-share value creation. Cash flow quality improved (OCF/NI = 9.7x, accruals quality score positive), but ~75% of FY25 FCF is the non-cash SBC add-back. If comp expense were cash, FCF would be ~$255M, not $1.0B.

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (3y daily) | **58.1%** | ~97th percentile risk for large-cap |
| Beta vs SPY (3y) | **1.30** | Profile 5y beta 1.51 |
| Max drawdown (3y) | **−48.6%** | Feb-2026 low ~$98 from ~$199 (Nov-25) |
| Sharpe (rf=0) | **0.91** | Decent return, brutal path |
| 52-week range | ~$98 → $300.68 | Now $235 (−20% from 9-Oct high of $293) |
| 1-day 95% VaR / adv. move | ≈ **−6%** | Earnings gaps far fatter: +31% (7-May-26), **−19% (6-Aug-26)**, +14% (10-Feb-26) |
| 1-month 95% VaR (√t scaled) | ≈ **−28%** | Fat tails mean true tail worse |
| EV / TTM revenue (EV $81.5B / $3,967M) | **~20.5x** | Multiple compression is the dominant risk |

Business-model beta exceeds statistical beta: revenue is **usage-based** (per-host, per-log, per-GB), so it is implicitly levered to customers' cloud consumption, which is itself cyclical. Q2-26 revenue grew **+35.6% y/y to $1.12B** and guidance was raised, yet the stock fell ~17% on the print after roughly doubling in 2026 — the market is pricing *expectations*, not fundamentals. This is a valuation-risk story, not a balance-sheet story.

## 4. Downside Scenario: Revenue −20%

FY25 revenue base $3,427M; cost structure: COGS $687M (~70% variable, largely cloud hosting), R&D ~$1,549M, SGA $1,236M, SBC $751M.

| Line ($M) | Base FY25 | **−20% revenue** (with 12% opex cut) | Δ |
|---|---|---|---|
| Revenue | 3,427 | **2,742** | −685 |
| Gross profit (78.5% mgn) | 2,740 | 2,151 | −589 |
| Opex (post-cut) | 2,784 | 2,450 | −334 |
| Operating income | (44) | **(299)** | −255 |
| EBITDA | 194 | **(240)** | −434 |
| OCF (add back SBC ~650 + D&A 60) | 1,050 | **~410** | −61% |
| Capex | 50 | 45 | |
| **FCF** | **1,006** | **~365** | **−64%** |
| Cash + investments | 4,474 | ~4,700 | |
| Gross debt / FCF | 1.5x | **4.2x** | Still comfortable |

**Verdict on the downside:** a 20% revenue shock produces a GAAP operating loss of ~$300M and an SBC-adjusted FCF near zero — but the company still generates positive reported FCF, still holds ~$4.7B of cash, has **>12 years of burn coverage even at a $300M–400M annual deficit**, and faces no maturity before 2029. **There is no liquidity or solvency path to distress from a demand shock**; the damage is entirely to the equity multiple (a 20x EV/sales name going to 10–12x sales on a de-rating is a 40–50% price hit, exactly the Feb-2026 template). A −40% cumulative two-year scenario still leaves net cash >$2.5B and full coverage of the 2029 converts from cash alone.

## 5. Overall Financial Risk Rating: **LOW (solvency) / HIGH (market & valuation) → Composite: MODERATE**

- **Credit risk: Low.** Net cash $2.94B, 3.38x current ratio, no maturities before 2029, zero-coupon converts.
- **Liquidity risk: Very Low.** No runway constraint; $4.5B liquidity vs. negligible cash interest.
- **Market risk: High.** 58% vol, 1.3–1.5 beta, −49% three-year drawdown, 20x EV/sales, double-digit earnings-day gaps.
- **FCF sustainability: Moderate.** FCF is growing and 29% of revenue, but 74% of it is SBC add-back; gross margin has slipped ~80bps since FY23 and opex growth (SGA +28.5% y/y) is tracking revenue growth, so operating leverage is not yet converting.

## 6. Key Red Flags

1. **SBC at 21.9% of revenue** — GAAP operating margin is −1.3%; the entire FCF story rests on adding back $751M of non-cash comp while share count grows ~2–3%/yr. This is the single largest quality-of-earnings issue.
2. **Valuation-driven drawdown risk** — the largest realistic loss driver is multiple compression, not fundamentals: 20x EV/sales with a 1.17% FCF yield leaves no valuation cushion.
3. **Consumption-based revenue model** — revenue is levered to customers' cloud spend; a cloud-optimization cycle hits growth faster than a seat-based model.
4. **Negative interest coverage on operating income** — not a credit problem (no cash coupon), but it means the company cannot self-fund a downturn from GAAP earnings, only from cash reserves.
5. **Gross margin erosion** (80.8% → 80.0%) — worth monitoring as AI/observability workloads shift the hosting cost mix.
6. **Convertible overhang** — the $1.0B 2029 zeros are likely in-the-money at $235 (issued Dec-2024 at a typical 30–35% premium), so dilution risk in an upside case; if out-of-the-money, $1B cash repayment in 2029 is fully covered by cash.

**Data gaps flagged:** (i) no credit rating/CDS available — DDOG appears unrated; (ii) the balance-sheet "net_debt" field ($1.13B) is internally inconsistent with reported cash ($4.47B) and debt ($1.54B) — I used the computed **net cash of $2.94B**, corroborated by the leverage tool; (iii) exact convertible conversion prices / capped-call coverage could not be verified; (iv) no peer-multiple benchmarking was performed within budget; (v) FY26 balance sheet not yet published (Q2-26 only), so leverage metrics are FY25 year-end.

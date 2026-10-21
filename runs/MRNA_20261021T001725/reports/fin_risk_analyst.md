# Fin Risk Analyst

- Symbol: MRNA
- Elapsed: 81.3s

---
# Moderna, Inc. (MRNA) — Financial Risk Assessment

**As-of:** FY2025 audited financials (period end 2025-12-31) + Q2 2026 interim data (filed 2026-07-31) + market data through 2026-02-20 / pro-forma events to Aug 2026.

---

## ⚠️ Data Integrity Notes (read first)

Three conflicts in the source data materially affect the risk math. I resolved them and am flagging the revisions:

| Item | Tool value | Verified value | Resolution |
|---|---|---|---|
| Share price / market cap | Profile: $242.08 / **$96.65B** | Price series close **$49.87** (2026-02-20); 398M shares → **~$19.8B** | Profile field is **stale/bad**. A 52-week-high article cites $50, confirming the price series. **All ratios below restated on ~$19.8B market cap.** |
| FCF yield | **-2.19%** (on $94.2B cap) | **-10.4%** (-$2,065M FCF / $19.8B) | Tool's yield was **understated ~5x** by the bad cap. |
| Beta | Profile: 0.899 | Computed 1.439 vs SPY (756d) | Use **1.44** (computed from actual returns); profile beta appears to be a legacy vendor figure. |
| Max drawdown | Tool: -72.6% (756d) | Observed peak-to-trough in series: $170.47 (2024-05-24) → $22.28 (2025-11-21) = **-86.9%** | −86.9% is the more faithful 2024→2025 drawdown; tool's window starts earlier. |

Also note: **net debt sign convention** — the leverage tool reported net debt of **-$3,883M**, i.e. *net cash*. The balance sheet's "net_debt: -679M" line is inconsistent with its own components ($5,799M cash − $1,916M debt = +$3,883M net cash). I use **net cash $3.9B**.
**Gaps:** no agency credit rating or CDS spread available; no balance sheet after YE2025 (interim liquidity taken from company guidance/web); no peer comparison (budget).

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE** (no formal agency rating obtained — this is my own assessment)

Moderna is a **solvent but structurally loss-making** issuer. The nuance that separates it from a typical junk credit: it holds **net cash of ~$3.9B**, a current ratio of 3.29, and **no debt maturity before 2032**. Default risk in the next 24 months is negligible. The risk is not insolvency — it is **perpetual dilution and cash exhaustion by ~2028**.

**What is broken:** the income statement.
- FY2025 revenue **$1,944M**, down **-71% from $18,875M in 2022** and -39% YoY.
- FY2025 EBIT **-$2,768M**, EBITDA **-$2,553M**, net loss **-$2,822M** (EPS -$7.26).
- Cumulative FY2023–25 net losses: **-$11.1B**; cumulative FCF: **-$9.9B**.
- **EBIT/interest = -277x** (tool: -307x). Negative and meaningless as coverage — but note *cash* interest is only $10M because the converts carry a **0% coupon**. No cash-flow solvency squeeze from debt service.
- Implied R&D (residual) ≈ **$3,132M = 161% of revenue**. The $4.15B R&D+SG&A base against $1.9B revenue is the entire problem.

**The mitigating structural feature:** debt is long-dated, zero-coupon, and convert-heavy. $3.0B of 2032 convertible senior notes were raised Aug 2026 (with capped calls), on top of ~$597M LT debt at 6/30/26. Pro-forma debt ≈ **$3.6B**, virtually all due **2032**. Convert strikes sit far above the current ~$50 share price, so **treat the converts as straight debt, not equity**. Converts typically carry **no financial maintenance covenants** → covenant-breach risk is low. There is **no refinancing cliff**.

**Verdict:** Balance-sheet credit quality (net cash, no maturities) = investment grade. Business credit quality (EBITDA deeply negative, no visibility to breakeven) = distressed operating profile. Blend = **Sub-Investment Grade**, with the caveat that the binding constraint is *runway*, not *leverage*.

---

## 2. Key Financial Risk Metrics

| Metric | Value | Assessment |
|---|---|---|
| **Leverage** | | |
| Debt / Equity | **0.22x** | Low — not a leverage story |
| Debt / Assets | 0.16x | Low |
| Net debt / EBITDA | **Net cash $3.9B** (tool's 1.52x is \|net cash\|/EBITDA, not leverage) | Strong |
| Total debt (pro-forma Aug-26) | ~$3.6B (0% coupon, 2032) | Long-dated, no cliff |
| **Coverage** | | |
| Interest coverage (EBIT/int.) | **-277x** | No operating debt-service capacity |
| Operating margin | **-158.1%** | Severe |
| Gross margin FY25 | 55.3% (vs 54.2% FY24) | Improving but volatile — Q1-26 was **-146%** (COGS $955M on $389M revenue) |
| **Liquidity** | | |
| Current ratio | **3.29x** | Strong |
| Quick ratio | 3.22x | Strong (low inventory) |
| Cash ratio | **2.92x** | Strong |
| Working capital | **$4,557M** | Strong |
| Cash & ST investments (YE25) | **$5,799M** | 47% of total assets |
| Cash to liabilities | 1.57x | Strong |
| **Solvency / quality** | | |
| Altman Z-Score | **2.087 — GREY zone** | x3 (EBIT/TA) is -0.224 and drags it; x4 uses book equity. On a market-cap x4 the score jumps to ~3.9, but that reflects option value, not earning power — **treat grey zone as the honest read.** |
| Piotroski F-Score | **3 / 9 — WEAK** | Fails on negative ROA, negative OCF, rising leverage, equity issuance, falling asset turnover. Only accruals quality, ROA direction, and gross margin improve. |
| Retained earnings | +$7,223M | Still positive — a legacy of 2022 profits; shields x2 |
| **Cash generation** | | |
| FCF FY25 | **-$2,065M** (OCF -$1,873M; capex -$192M) | Negative 3 straight years |
| FCF FY24 / FY23 | -$4,055M / -$3,825M | **Improving** (burn down ~49% YoY) — the one genuine positive |
| FCF yield (restated) | **-10.4%** | Deeply negative |
| SBC FY25 | $483M (12% of revenue) | Non-cash, but real dilution |

---

## 3. Market Risk Profile

| Metric | Value | Read |
|---|---|---|
| Annualised volatility (756d) | **140.7%** | Extreme — ~7x the market. Single-asset tail risk |
| Beta vs SPY | **1.44** (computed) / 0.899 (vendor) | High systematic sensitivity *plus* huge idiosyncratic risk |
| Max drawdown | **-86.9%** ($170.47 → $22.28); tool: -72.6% | Catastrophic; a full decade of returns erased |
| Sharpe ratio | 0.794 (0% rf) | **Misleading.** Positive Sharpe on a stock down ~70% is a volatility-blowup artefact (large symmetric daily moves inflate the numerator relative to arithmetic vol). Do not read this as quality |
| Sortino | Not available from tools | — gap flagged |
| Price (2026-02-20) | $49.87; 52-wk high ~$50, low ~$22 | Recovery off the Nov-2025 low (+123%), still -71% off the May-2024 peak |

**Interpretation:** This is a **binary-outcome, event-driven** security. 140% vol means a ±1 standard deviation annual move is larger than the entire market cap band in which the equity trades. Position sizing, not fundamental analysis, dominates realised P&L here. The stock behaves like a call option on pipeline data readouts (flu/RSV/oncology/CMV), not like a vaccine cash-flow business.

---

## 4. Downside Scenario: Revenue −20%

Base case for the model: FY2025 revenue $1,944M, COGS $868M (44.7%), R&D+SG&A $4,150M.

**Critical modelling point:** Moderna's COGS is **substantially fixed** (idle manufacturing capacity + write-downs). Q1-2026 proves it: revenue fell to $389M and COGS came in at $955M — a **-146% gross margin**. So a revenue decline does *not* scale gross profit linearly.

| Line | Base (FY25A) | Stress: rev -20% | Note |
|---|---|---|---|
| Revenue | $1,944M | **$1,555M** | -$389M |
| COGS (35% variable / 65% fixed) | $868M | ~$807M | GM compresses **55.3% → 48%** |
| Gross profit | $1,076M | **$748M** | -$328M |
| R&D + SG&A (no cuts) | $4,150M | $4,150M | Stress case assumes management *cannot* cut fast enough |
| **EBIT** | -$2,768M | **-$3,402M** | Deteriorates $634M |
| **EBITDA** | -$2,553M | **~-$3,187M** | |
| **FCF** | -$2,065M | **~-$3,000M** | Burn re-accelerates |

**Liquidity path through the stress:**
- Cash & investments guided to **$4.7–5.2B at YE2026** (post the Aug-2026 $3.0B convert). Midpoint **$4.95B**.
- Stress burn ~**$3.0B/yr** → **$1.95B at YE2027**, **cushion breached during 2028**.
- Company's practical operating floor is roughly $1.5B; **the stress case forces a capital raise by late 2027 / early 2028** — either dilutive equity at depressed prices or another convert tranche.

**Transmission mechanism — this is the key insight:** a 20% revenue shortfall does *not* threaten default (no maturities until 2032, zero coupon, no covenants). It **pulls forward the dilution event by roughly 12–18 months** and compresses runway from ~1.8 years to ~1.4 years. The equity, not the debt, absorbs the damage. Each raise at ~$50/share against a 398M share count is ~5–8% dilution per $1B.

**Worse-than-modelled tail:** if gross margin goes *negative* again (as in Q1-26, on inventory write-downs and demand collapse), the loss widens by a further $500M–$1B and runway compresses toward **~12 months**. That is the true bear case, and there is direct precedent in the last four quarters.

---

## 5. Overall Financial Risk Rating: **HIGH**

Not *Critical* — the $3.9B net cash position, 3.29x current ratio, zero-coupon 2032 debt, and absence of covenants mean there is **no 24-month solvency event**. But it is unambiguously High: three consecutive years of $2–4B FCF burn, a Piotroski score of 3/9, EBITDA of -$2.6B, an FCF yield of -10.4%, and 140% realised volatility with an 87% peak-to-trough drawdown.

**The single sentence:** Moderna is a **balance-sheet-rich, income-statement-broken** company whose equity is a levered bet on pipeline readouts before the cash runs out around 2028.

---

## 6. Key Red Flags

1. **Revenue collapse with a fixed cost base.** Revenue -71% since 2022 to $1.9B, against $4.15B of R&D+SG&A. The profitability gap is structural, not cyclical.
2. **Verified negative gross margin (Q1-2026: -146%).** This is the most alarming single datapoint — it means COGS does not flex with demand. Any revenue miss hits gross profit disproportionately.
3. **Recurring, escalating cash burn.** -$3.8B / -$4.1B / -$2.1B FCF in FY23–25, and 1H-2026 operating loss of -$2,203M was *worse* than 1H-2025 (-$1,957M) despite cost cuts. The "improvement" narrative is not yet holding intra-year.
4. **Serial dilution.** Shares 382M → 398M (+4.2%) in three years, with the 2023 $1.15B buyback now looking like capital misallocation ahead of the downturn. SBC $483M/yr.
5. **Convertible overhang treated as equity by the market.** $3.0B of 2032 converts struck far above spot. These will **not** convert — they are a $3.0B cash repayment obligation in 2032 that arrives precisely when runway math is tightest.
6. **Piotroski 3/9 and Altman grey zone (2.09)** — both confirm deteriorating fundamentals despite the strong liquidity ratios.
7. **140.7% volatility / 1.44 beta / -86.9% drawdown** — drawdown risk on this position is effectively unhedgeable and un-diversifiable at normal sizing.
8. **Guidance opacity.** YE2026 cash guidance of $4.7–5.2B is a $500M-wide band post a $3B raise — implying management itself has wide uncertainty on burn.

**Positive offsets (must be stated for balance):** burn is genuinely down ~49% YoY; YE2026 cash guidance was *raised*; no debt matures before 2032; zero coupon; no maintenance covenants; current ratio 3.29x; FY25 gross margin actually improved 110bps to 55.3%.

---

## Monitoring Triggers

- Any quarter with **negative gross margin** → downgrade to Critical.
- **YE2026 cash < $4.5B** (below guidance) → runway model breaks, dilution pulled forward.
- **Annualised burn > $3.5B** → raise required within 4 quarters.
- Successful Phase 3 readout (flu/RSV/oncology/CMV) is the only path that plausibly re-rates the equity before 2028 — it is a **binary catalyst, not a financial-risk mitigant**.

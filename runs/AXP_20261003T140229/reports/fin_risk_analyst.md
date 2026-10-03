# Fin Risk Analyst

- Symbol: AXP
- Elapsed: 75.6s

---
I have all the data I need. The 10-K maturity table PDF was unparseable (binary), and the specific agency rating confirmations were not directly retrievable — I'll flag those as data gaps. Here is the complete assessment.

---

# FINANCIAL RISK ASSESSMENT — American Express Company (NYSE: AXP)

*Data as of FY2025 (period ended 2025-12-31), price $302.78, market cap ≈ $204.5B. Sector: Financial Services (Credit Services). Analyst: Risk & Stress-Test Desk.*

---

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE** (low-A equivalent; see data gaps below on agency notches)

AXP is a deposit-funded, bank-style financial institution — balance sheet total $300.1B, of which only **$57.8B is true debt** (public notes/ABS; ST debt just $1.4B). The remainder of the liability stack is **card-member deposits (~$120B+)** — sticky retail funding, not arms-length credit. On the *debt* (non-deposit) stack:

- **Net debt/EBITDA = 0.59x** (net debt $9.2B = $57.8B debt − $48.5B cash). Even gross debt of $57.8B is only **3.7x EBITDA** — comfortable.
- **Interest coverage = 1.68x** (EBIT $13.8B / interest $8.2B). Headline-thin, but the $8.2B interest bill **includes ~$8B of customer funding/deposit cost** — the economic coverage against *external* debt service is materially higher. Treat 1.68x as conservative, not alarming, for this business model.
- **FY25 profitability is compounding:** revenue $80.5B (+8.4% YoY), operating income $13.8B, net income $10.8B, EPS $15.41 — a 5-year run of record results.
- **Card credit book is well-behaved (Q4-2025):** US consumer 30-day delinquency **1.3%**, NCO 2.1%; SMB 1.7% / 2.7%; securitized Lending Trust net default rate 1.2%. Stable, modestly normalizing.

Ratings context derived from agency press activity: parent is solidly in the **A/BBB+ band** (senior unsecured); the separately-listed travel arm (Amex GBT) sits much lower (~Baa2 area, D/E ~4.8x). AXP itself is nowhere near sub-investment grade.

---

## 2. Key Financial Risk Metrics (FY2025)

| Metric | Value | Reading |
|---|---|---|
| **Debt / Equity** | 1.73x | Elevated vs industrials; normal-low for card bank |
| **Debt / Assets** | 0.19x | Low |
| **Net debt / EBITDA** | 0.59x | Very strong (bank-model adjusted) |
| **EBITDA margin** | 19.4% | Strong |
| **Interest coverage (EBIT/Int)** | 1.68x | Thin headline; incl. deposit cost |
| **Current / Quick / Cash ratio** | 0.28 / 0.28 / 0.28 | **Artifact** — see red flag #1 |
| **Cash & ST investments** | $48.5B | Deep buffer (~10.5 qtrs of OpCF; 6.0x LT-debt maturities) |
| **Working capital** | −$122.3B | Model artifact (deposit-funded) |
| **Altman Z** | **0.125 (Distress)** | **Model inapplicable** — see red flag #2 |
| **Piotroski F** | **7/9 — Moderate/Strong** | Points lost on ROA improvement & asset turnover only |
| **Equity / Assets** | 11% | Thin regulatory-style cushion ($33.5B equity vs $300B assets) |
| **FCF yield** | **7.59%** | Excellent cash generation |
| **FCF** | $16.0B (+32% YoY) | Covers distributions ($2.3B div + $5.8B buyback) ~2x |

---

## 3. Market Risk Profile (252-day window vs SPY)

| Metric | Value |
|---|---|
| Annualised volatility | **26.8%** |
| Beta vs S&P 500 | **0.93** (profile beta 1.05) |
| Max drawdown (3-yr) | **−23.8%** |
| Sharpe (0% RF) | **−0.95** |
| FCF yield | 7.59% |

Risk-adjusted returns over the trailing year are **negative** — the stock de-rated while fundamentals improved (FCF +32%, NI +7%), i.e., multiple compression rather than earnings deterioration. Volatility is mid-pack for a financial name; the drawdown (−23.8%) is notable but not tail-extreme. The financing environment is restrictive but normalized: 2Y 4.65% / 10Y 4.99%, curve **not inverted** (2s10s +34bp) — no immediate inversion signal, but refinancing stays expensive.

---

## 4. Downside Scenario — Revenue −20% (severe 2008/COVID-class recession)

Base: Rev $80.5B | EBITDA $15.6B | EBIT $13.8B | Interest $8.2B | NI $10.8B | FCF $16.0B

| Line | Base (FY25) | Stress (−20% rev) |
|---|---|---|
| Revenue | $80.5B | $64.4B |
| EBITDA margin | 19.4% | ~9% (sticky cost + provisioning spike) |
| EBITDA | $15.6B | ~$5.8B |
| EBIT | $13.8B | ~$4.0B |
| Interest expense | $8.2B | ~$8.2B (rates sticky) |
| **Interest coverage** | **1.68x** | **~0.5x** |
| Net income | $10.8B | **≈ −$3B** (pre-tax −$4.2B) |
| FCF | $16.0B | ~$5–6B |
| FCF yield | 7.6% | ~2.5% |

**Verdict: survivable, but earnings go negative and the equity cushion does heavy lifting.** This is consistent with 2020, when a milder revenue dip still cut AXP net income ~55%. Under this scenario: 1–2 notch downgrade (to BBB+/Baa1 band), EPS ~ −$4, valuations trash, but **no insolvency** — $48.5B cash + $6.0B committed revolver (matures Sep-2028, per 10-Q) + sticky $120B deposit base + retained earnings $25.5B absorb the shock. Covenant-breaching is **remote**: senior notes carry standard covenants; the secured trusts are over-collateralized (Lending Trust NCO 1.2%).

---

## 5. Overall Financial Risk Rating: **MODERATE**

**Justification:** Investment-grade credit (low-A), 7.6% FCF yield, Piotroski 7/9, negligible net leverage on the true-debt stack, no maturity cliff (LT debt $56.4B amortizes; revolver out to 2028), and a deep cash buffer argue **Low**. The uplift to **Moderate** comes from: (a) a thin headline coverage ratio (1.68x) that breaks below 1.0x in a −20% revenue shock; (b) rate-sensitive funding cost that has grown ~6.4x since 2021 ($1.3B→$8.2B) into a 4.6–5.4% yield environment; (c) only 11% equity/assets loss-absorption; (d) a normalizing consumer credit cycle; and (e) negative trailing risk-adjusted returns. Not High — the cash, FCF, and funding-stickiness defenses are genuinely strong.

---

## 6. Key Red Flags

1. **Headline liquidity ratios (0.28) are misleading.** Current liabilities ($170.8B) are dominated by card-member deposits — funding that matches the loan book. The raw quick ratio implies insolvency that the $48.5B cash + $6.0B revolver and stable NCOs simply do not support. Use deposit-run and coverage-based liquidity lenses instead.
2. **Altman Z = 0.125 "Distress" is a model misapplication.** The Z model is calibrated for manufacturers; the negative working-capital term (−$122B) is a deposit-funding artifact, and x4 uses book equity ($33.5B vs $204B market cap). Do **not** read this as near-bankruptcy (the tool's own note concurs). Included for transparency; should be excluded from AXP monitoring.
3. **Credit-cycle exposure:** consumer NCO 2.1% / SMB 2.7% with 30-dpd ticking at 1.3–1.7% — normalized, not cyclically cheap. A downturn multiplies provisions, which is the single biggest earnings swing factor.
4. **10.5-quarter cash runway is overstated for a bank** — most cash is regulatory/clearing liquidity, not free capital; real loss-absorption is the 11% equity/assets (book equity $33.5B ≈ 1.6x annual FCF).
5. **Thin economic coverage under stress (≈0.5x)** and bank-type leverage at regulatory limits leave little margin if the −20% scenario persists beyond 2 years.
6. **Trailing Sharpe −0.95 / −23.8% drawdown:** the equity has repriced downward; valuation risk, not operating risk, has been the live danger.

---

## Data Gaps & Caveats (explicit)

- **Agency credit rating:** exact live notches (Moody's/S&P/Fitch) for the *parent* were not independently retrievable in-session; rating characterized as low-A/BBB+ band from agency action history and deal pricing. Amex GBT (Baa2-zone, D/E 4.8x) is a separate entity and **not** representative of AXP's risk.
- **CDS spreads:** not available in tools; proxy used = IG bond pricing environment (2Y 4.65% / 10Y 4.99%, non-inverted).
- **Debt maturity table (10-K Table 8.3):** the filing PDF returned unparseable binary; annual maturities approximated from disclosure (LT debt $56.4B amortizing, revolver to Sep-2028, no near-term cliff). Exact 2026–2030 maturity buckets unverified.
- **Peer multiples** (card-issuer D/E, P/E, coverage): sector screen returned index funds rather than issuer comparables; cross-company leverage benchmarks not computed.
- Altman Z and current-ratio artifacts are flagged and should be excluded from any AXP covenant/scorecard logic.

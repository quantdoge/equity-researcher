# Fin Risk Analyst

- Symbol: MRVL
- Elapsed: 64.4s

---
# MRVL — Financial Risk Assessment
*Marvell Technology, Inc. | Semiconductors | Data as of Q2 FY2027 (qtr ended 2026‑08‑01); FY2026 annual (ended 2026‑01‑31)*

---

## 1. Credit Risk Assessment — **INVESTMENT GRADE**

**Rating: Investment Grade.** Fitch rates the senior unsecured notes **BBB+** (per a June 2026 rating action covering a $500M 4.75% 2030 note offering). Leverage is low, coverage is comfortable, and there is no refinancing cliff.

| Leverage / coverage | FY2026 (1/31/26) | Q2 FY2027 (8/1/26) |
|---|---|---|
| Total debt | $4,790M | $5,286M |
| Cash & ST investments | $2,639M | $3,933M |
| **Net debt** | **$2,152M** | **$1,353M** |
| Debt / equity | 0.33x | 0.29x |
| Debt / assets | 0.21x | 0.19x |
| Net debt / EBITDA (reported adj.) | 0.47x | ~0.48x (TTM) |
| Net debt / EBITDA (GAAP: EBIT + D&A) | 0.82x | ~0.48x (TTM) |
| Interest coverage (EBIT / interest) | 6.6x (GAAP basis) / 16.0x (adj. EBIT) | 7.4x |
| Net debt / market cap | — | ~0.6% |

Note: the tool's FY2026 net debt/EBITDA of 0.47x uses an adjusted EBITDA of $4,540M, which is ~$1.9B above GAAP EBITDA ($2,629M) — the gap is acquisition-related amortization. **Both bases are investment-grade**; I use the GAAP-conservative basis in stress tests below.

**Maturity profile / refinancing:** Short-term debt fell from $500M to **zero** — the 1.65% notes due April 2026 were repaid from the 4.75% 2030 note proceeds. Long-term debt of $4,963M has no material maturities before the 2028 notes (~$913M combined legacy/exchanged). *Gap: I could not retrieve the full contractual maturity ladder from the 10‑K (the Fitch page body was inaccessible); the schedule above is reconstructed from offering documents and the balance sheet.*

**Important caveat on the Altman Z-Score:** 2.185 (**grey zone**) is *mechanically* misleading. The score uses **book** equity and is penalized by (a) low retained earnings ($1.59B, reflecting years of GAAP losses) and (b) $16.2B of goodwill/intangibles. Substituting market capitalization (~$232B) into X4 raises the Z-Score to **~16 (deep safe zone)**. **Distress probability is negligible; the grey zone is an accounting artifact, not a solvency signal.**

**Piotroski F-Score: 6/9 (Moderate)** — profitable (ROA+, CFO+), improving ROA/gross margin/asset turnover; fails on accruals quality, leverage trend, and "no dilution."

---

## 2. Key Financial Risk Metrics

| Metric | Value | Read |
|---|---|---|
| Current ratio | 2.01x → **3.17x** | Strong, improving |
| Quick ratio | 1.58x → **2.62x** | Strong |
| Cash ratio | 0.82x → 1.57x | Very strong |
| Working capital | $3,240M → $5,420M | Ample |
| Equity / assets | 0.64x → 0.67x | Solid |
| Altman Z | 2.19 (grey) / ~16 on market cap | No distress |
| Piotroski F | 6 / 9 | Moderate |
| Operating margin | 16.3% → 16.7% | Stable, thin for semis |
| FCF (FY26) | $1,396M (17.0% margin) | Good |
| FCF (Q2 FY27 annualized) | ~$1,915M (17.5% margin) | Improving |
| **FCF yield** | **0.94%** (on $149B mcap as supplied) | ~0.6% at latest close — very expensive |
| Net debt / tangible equity | ~180% → ~59% | Improving |

**FCF sustainability:** Cash generation is real and growing (FCF $1.02B → $1.39B → ~$1.9B run-rate), and FCF covers the ~$215M dividend ~6.5x. **However, FY2026 capital returns ($2,040M buyback + $205M dividend = $2,245M) were 161% of FCF**, funded by balance-sheet capacity and incremental debt. That is a discretionary, reversible outflow — not a solvency threat, but it removes the buffer that a downturn would otherwise find.

---

## 3. Market Risk Profile — **HIGH**

| Metric | Value |
|---|---|
| Annualised volatility | **75.5%** |
| Beta vs S&P 500 | **2.61** (tool, 3-yr daily) / 2.26 (profile) |
| Max drawdown (3-yr) | **−60.8%** |
| Sharpe (0% rf assumption) | 0.94 |
| Price (latest close, 2026‑09‑30) | $264.15 |
| 52-week range | ~$46.89 (Apr 2025) to ~$324 (Jun 2026) |
| Drawdown Jun→Jul 2026 | $324 → $163 = **−50% in under 2 months** |

This is a genuinely high-risk equity. A 2.6 beta means a 20% market drawdown maps to roughly a **52% decline** in MRVL. Realised history confirms it: the stock fell 61% peak-to-trough in early 2025, then rallied ~7x, then halved again within two months of mid‑2026. **Sharpe of 0.94 overstates risk-adjusted quality** — it assumes a 0% risk-free rate (with T-bills near 4%, the excess-return Sharpe is materially lower), and it is the product of a single violent up-move rather than consistent compounding. *No Sortino ratio was available from the tool set.*

> **Data conflict flagged:** the company profile lists price $171.41 / market cap $150.1B, but the price history shows a $264.15 close on 2026‑09‑30 (implying ~$232B market cap). The profile price appears stale. FCF yield of 0.94% is computed on the smaller figure; on the latest close it is **~0.6%**. Either way the equity is priced at roughly **110–170x trailing FCF** — the single largest source of downside risk in this name.

---

## 4. Downside Scenario Analysis (TTM revenue $9,452M; TTM EBIT $1,579M; TTM FCF $1,396M; interest $216M; net debt $1,353M)

**Assumption:** 65% decremental operating margin (vs. 53% gross margin) — semis carry high fixed opex and take inventory write-downs in a demand break.

| Scenario | Revenue | EBIT | Interest coverage | Net debt / EBITDA | FCF | Verdict |
|---|---|---|---|---|---|---|
| Base (TTM) | $9,452M | $1,579M | 7.3x | 0.48x | $1,396M | Solid |
| **−20%** | **$7,561M** | **~$350M** | **~1.6x** | **~0.85x** | **~$350M** (+WC release → ~$750M) | **Survives comfortably.** Dividend still covered; no covenant trigger (IG bonds carry change-of-control puts, not maintenance covenants) |
| **−40%** (AI capex digestion) | $5,671M | **~(£880)M loss** | Negative | ~1.6x | Breakeven to ~−$150M before WC release | **Cash burn modest.** $3.9B cash + cuttable capex + ~$600M WC release = multi-year runway |
| −20% + simultaneous 30% multiple compression | — | — | — | — | — | Equity −50% to −65%; credit unaffected |

**Interpretation:** the P&L and balance sheet can absorb a severe AI-capex air-pocket. **The risk in MRVL is almost entirely equity-duration risk, not credit risk.** The company would remain solvent and liquid through a 40% revenue decline; the stock would not.

---

## 5. Overall Financial Risk Rating — **MODERATE**
*(decomposed: credit risk **Low** · liquidity risk **Low** · market/equity risk **High** · earnings-quality risk **Moderate**)*

Marvell is a conservatively financed, cash-generative semiconductor company with sub-1x net leverage, ~7x GAAP interest coverage, $3.9B of cash, an investment-grade rating, and no near-term maturities. It is not a credit story. It *is* a high-beta, high-expectation equity carrying $16.2B of goodwill and intangibles, 82% top-10 customer concentration, and a valuation that discounts years of flawless AI execution.

---

## 6. Key Red Flags

1. **Valuation is the dominant risk.** FCF yield of 0.6–0.94% (~110–170x trailing FCF). The downside case is a de-rating, not a default — and a 2.6 beta / 75% vol stock re-rates violently (two ≥50% drawdowns in 18 months).
2. **Receivables ballooning — earnings-quality warning.** Net receivables went from **$1,028M (FY25) → $2,187M (FY26) → $2,218M (Q2 FY27)** while revenue grew 42% then 32%. Implied DSO expanded from **~65 days to ~97 days**. Working capital absorbed $516M of FY26 operating cash flow and $449M in Q2 FY27 alone. Part is direct-vs-distributor mix and acquisition consolidation, but **CFO/NI of 0.66 is weak**, and this is the mechanism by which "record revenue" can outrun cash.
3. **Goodwill & intangibles = 59% of assets, ~88% of equity.** Tangible equity is only ~$2.3B against $5.3B of debt. A strategic pivot or AI-narrative break creates impairment risk — and MRVL has already posted GAAP operating losses in FY2024 and FY2025 on exactly this dynamic.
4. **Non-operating earnings distortion.** FY2026 net income of $2,670M sits far above operating income of $1,338M; the Nov‑2025 quarter alone shows net income $1,901M vs. operating income $358M. This appears to be a one-off (likely a tax valuation-allowance release) — **unverified in the data provided** — and it inflates ROE/ROA-based screens including the Z- and F-scores.
5. **Capital returns exceed free cash flow** (161% of FCF in FY2026) and **dilution is real**: diluted shares 856M → 921M y/y (**+7.6%**), consistent with stock-funded M&A (intangibles +$3.1B, equity +$4.2B since January). Piotroski's "no dilution" test flagged 0 despite concurrent buybacks.
6. **Customer/end-market concentration.** Top 10 customers = **82% of FY2026 revenue**; two customers >10%; data center ≈76% of revenue. A single hyperscaler program decision is a material revenue event.
7. **High fixed-cost operating model** — 16–17% GAAP operating margin means limited cushion; a 20% revenue decline compresses coverage from 7.3x to ~1.6x.

### Data gaps (explicit)
- Full debt maturity ladder and covenant terms not retrieved from the 10‑K; schedule reconstructed from offering documents.
- Sortino ratio and CDS spreads unavailable from the tool set.
- Company profile price ($171.41) conflicts with price history ($264.15); both reported, equations run on the tool-supplied market cap.
- The FY2026 non-operating gain and the FY2027 intangible increase are inferred, not confirmed from filing text.

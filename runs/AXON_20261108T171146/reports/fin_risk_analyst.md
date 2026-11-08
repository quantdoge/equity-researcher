# Fin Risk Analyst

- Symbol: AXON
- Elapsed: 52.5s

---
## AXON ENTERPRISE, INC. (AXON) — FINANCIAL RISK ASSESSMENT
**Data as of 2026-11-06 (last close $313.00; market cap $25.43B). Latest filing: Q3 FY2026 (10-Q, 2026-11-06).**

**Critical data note:** the automated ratio tools (`calculate_leverage_ratios`, `calculate_liquidity_ratios`, `calculate_altman_z_score`, `calculate_piotroski_f_score`) are computed on **FY2025 annuals (12/31/2025)**. Three quarters of FY2026 are already reported, so I have rebuilt the key ratios on a **TTM through Q3 FY2026** basis from the underlying statements. Both are shown.

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (crossover BB+/BBB- profile). No public agency rating or CDS spread is available in my data — the rating is assigned on fundamentals, not a quoted market level.**

The credit story is a tale of two P&Ls. On a GAAP basis AXON is barely profitable and levered; on a management-adjusted basis it is conservatively levered. That gap *is* the credit risk.

| Basis | FY2025 | TTM Q3'26 | Net debt / EBITDA |
|---|---|---|---|
| GAAP operating income | **-$62.1M** | +$128.1M | — |
| GAAP EBITDA (EBIT + D&A) | $196.4M | $251.1M | **5.2x** |
| Adjusted EBITDA (+ stock comp $643.7M) | ~$655M | ~$894.8M | **1.5x** |

- Debt has **more than doubled**: $1.40B (FY24) → $1.81B (FY25) → **$2.97B (Q3'26)**, driven by $1.0B 6.125% notes due 2030, $750M 6.25% notes due 2033 (both issued Mar-2025) and a new **$1.0B 0% convertible due 2031** (Q3'26).
- **Interest coverage is the weak link.** FY2025 EBIT/interest = **1.20x**; operating-income/interest = **-0.66x** (the tool's headline). TTM operating income $128.1M / TTM gross interest ~$113.8M = **1.13x**. Adjusted EBITDA/interest = 7.9x; **GAAP EBITDA less capex / cash interest ≈ 1.0x**. Cash interest is ~$108M (coupons only, converts are 0%).
- **Maturity profile is benign — no refinancing cliff.** Nothing material before the 2027 converts (largely exchanged in Mar-2025 and hedge-wrapped), then a clean runway to **2030/2031/2033 ($2.75B of cash maturities vs $1.66B cash today)**. All fixed-rate; no floating-rate exposure. *Gap: no disclosure of revolver size/drawn availability or covenant terms.*
- **Goodwill & intangibles $2.154B = 57% of equity, 24% of assets** (Dedrone/Prepared/Carbyne roll-up). Tangible equity $1.61B → **gross debt/tangible equity 1.85x**. Impairment risk is the second-order credit threat.

**Altman Z-Score — read with care.** Tool output **1.54 (Distress)** uses *book* equity. Substituting the $25.4B market cap and Q3'26 balance sheet gives **x4 = 5.02 → Z ≈ 4.0 (Safe)**. The distress reading is an artefact of a 64%-depressed share price plus a $1.5B goodwill base, not imminent insolvency. My judgement: Z is **not decision-useful here**.

**Piotroski F-Score: 5/9 (Moderate)** on FY2025 — failed on ROA improvement, higher leverage, dilution, asset turnover. On TTM Q3'26 the trajectory improves (positive and rising ROA, positive operating cash flow) — indicative F ≈ 5–6, but this is my estimate, not a tool output.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 (tool) | TTM/Q3'26 | Assessment |
|---|---|---|---|
| Debt / equity | 0.59x | **0.79x** | Moderate |
| Net debt / EBITDA (GAAP) | 1.03x (tool) / 3.6x (BS debt) | **5.2x** | Elevated |
| Net debt / Adj. EBITDA | — | **1.5x** | Low |
| Interest coverage (EBIT) | -0.66x | **1.13x** | **Weak** |
| Cash interest coverage (cash) | — | **15.3x** | Strong |
| Current ratio | 2.53x | **3.00x** | Strong |
| Quick ratio | 2.29x | **2.60x** | Strong |
| Cash ratio | 1.16x | 1.16x | Strong |
| Working capital | $2.24B | **$2.86B** | Strong |
| Cash & STI | $1.707B | $1.655B | Strong |
| Altman Z | 1.54 (book) / ~4.0 (mkt) | — | Misleading on book basis |
| Piotroski F | 5/9 | ~5–6 (est.) | Moderate |
| FCF / margin | $75.1M / 2.7% | **$80.9M / 2.4%** | **Very weak** |
| FCF yield | 0.24% | **0.32%** (guide-implied ~1.5%) | **Very weak** |
| SBC / revenue | 22.8% | **18.8%** | **Very high** |
| Interest expense | $94.2M | ~$114M | Rising fast |
| Goodwill+intangibles / equity | 48% | **57%** | Acquisition-heavy |

**Liquidity explicitly is not the problem.** $1.655B cash covers ~15x annual cash interest and 8+ quarters of the current ~$200M/qtr working-capital drag. **Solvency risk over 24 months: LOW.**

---

## 3. Market Risk Profile

| Metric | Value |
|---|---|
| Annualised volatility (3y, 756d) | **60.5%** — extreme |
| Beta vs SPY | **1.27** (3y tool) / **1.47** (5y, profile) |
| Max drawdown (3y) | **-64.1%** |
| Sharpe ratio | **0.15** — poor risk-adjusted return |
| Sortino | Not available (**data gap**) |
| Peak close → now | $867.12 (2025-08-05) → **$313.00 = -63.9%** |
| Most recent event | **-26% in two sessions** (11/05 $424.18 → 11/06 $313.00) on 5.2M shares — Q3 print + FY26 FCF guidance cut |

AXON is a **high-beta, ~60%-vol, momentum-reversal name**. A beta of 1.27–1.47 means a 20% index drawdown mechanically implies a ~25–30% AXON drawdown, before idiosyncratic risk — which has already been ~3x the market's. With 0.15 Sharpe, holders have been paid almost nothing for that volatility over three years. Note the stock *still* trades at ~7.4x TTM revenue, so the equity — not the balance sheet — is where the downside lives.

---

## 4. Downside Scenario: Revenue −20%

Applied to FY2026E revenue of ~$3.57B (−$714M), gross margin 57% (Q3'26 actual 56.7%), opex cut 10% in defence:

| Item | Base (TTM) | −20% Revenue |
|---|---|---|
| Revenue | $3,417M | $2,850M |
| Gross profit (57%) | $1,948M | $1,625M |
| Operating income | +$128M | **≈ -$164M** |
| GAAP EBITDA | $251M | **≈ -$41M** (negative) |
| Interest expense | ~$114M | ~$114M |
| **EBIT / interest** | 1.13x | **negative — technical covenant breach territory** |
| Net debt / GAAP EBITDA | 5.2x | **undefined / n.m.** |
| Adj. EBITDA (+SBC $644M) | $895M | ~$603M |
| **Net debt / Adj. EBITDA** | 1.5x | **≈ 2.2x** |
| FCF | +$81M | **≈ -$90M** |
| Cash runway on FCF deficit | — | **>15 years on $1.66B cash** |

**Conclusion:** a 20% revenue decline **breaks the GAAP credit math (coverage goes negative, adjusted leverage to ~2.2x) but does not break the company.** Liquidity, 0% converts and a 2030-first maturity wall mean AXON survives a severe downturn without raising equity. The equity, however, would de-rate to 3–4x sales (~$120–160/share, a further -50% to -60%) because FCF is already ~zero at *current* revenue. **The vulnerability is valuation and cash conversion, not solvency.** *Gap: covenant thresholds undisclosed, so an actual breach cannot be confirmed.*

---

## 5. Overall Financial Risk Rating: **MODERATE-HIGH**

Split by risk type, because a single word hides the real dispersion:
- **Liquidity risk: LOW** — 3.0x current, 1.16x cash ratio, $1.66B cash, no near maturities.
- **Credit/solvency risk: MODERATE** — fine on adjusted EBITDA (1.5x), strained on GAAP (5.2x, 1.1x coverage), rising gross debt.
- **Cash-flow quality risk: HIGH** — FCF ~$81M on $3.4B revenue, three consecutive negative-FCF quarters, guidance cut.
- **Market/equity risk: HIGH** — 60% vol, 64% drawdown, 0.15 Sharpe, 7.4x sales.

---

## 6. Key Red Flags

1. **Free cash flow has effectively disappeared.** TTM FCF $80.9M (0.32% yield); 9M FY2026 FCF **-$74.5M** (Q1 -$54.6M, Q2 -$1.0M, Q3 -$18.9M). Management **cut FY2026 FCF guidance to $350–400M**. A 34%-growth company converting ~2% of revenue into cash is the single most important warning here.
2. **Working-capital haemorrhage / inventory build.** WC drained **$607M in 9M'26**; inventory **+69% YoY to $579M** (from $342M). Management frames this as drone/supply-chain buffer that moderates "after 2026" — unproven, and it is the swing factor in FCF normalisation.
3.

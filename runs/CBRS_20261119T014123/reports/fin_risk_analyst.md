# Fin Risk Analyst

- Symbol: CBRS
- Elapsed: 51.6s

---
I have sufficient data. Writing the assessment now.

---

# CBRS — Cerebras Systems Inc. | Financial Risk Assessment

**Price $94.15 · Market cap $21.33B · Sector: Technology / Semiconductors · IPO 14-May-2026 · FY ends 31-Dec · Latest financials: FY2025**

> **Critical framing note:** This is a pre-revenue-scale, recently-IPO'd, essentially debt-free company with an equity story, not a levered credit. Traditional credit-risk tools (leverage, coverage, Z-score) are structurally distorted here — negative book equity from preferred stock capitalization, and net income inflated by non-operating gains. I flag distortions explicitly rather than reporting mechanical outputs at face value. **The dominant risk is concentration and cash-consumption (equity risk), not default risk.**

---

## 1. Credit Risk Assessment

**Rating: SUB-INVESTMENT GRADE (speculative, unrated) — not Distress, despite Altman output**

| Evidence | Reading |
|---|---|
| Total debt FY2025 | $261.8M, **all non-current** (ST debt $0, LT debt $0 as reported — likely lease obligations) |
| Interest expense | **$0** — no funded debt, no interest burden |
| Net cash position | **+$846M net cash** (cash $1,108.2M vs debt $261.8M) |
| Cash at YE2025 | $1,108.2M |
| Book equity | **–$578.7M** (negative) |

The company has **no refinancing cliff and no debt-service obligation**. Default risk over any horizon out to 2–3 years is negligible on the current balance sheet. Altman Z of 0.327 reads "Distress," but this is a **mechanical artifact**: x2 (retained earnings/TA = –0.389) and x4 (book equity/TL = –0.199) are negative only because total liabilities ($2,905M) exceed total assets ($2,326M) — consistent with convertible preferred stock being carried as a liability, which converts to equity post-IPO. On a market-cap basis x4 would be ≈7x. **The Altman score should be disregarded as a bankruptcy predictor for CBRS.** The only genuine signal inside it is x3 (EBIT/TA = 0.105), which is itself inflated by non-operating gains (see §6).

**No public credit rating or CDS spread available — data gap.** As an unrated, debt-free issuer there is no credit curve to read.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | Assessment |
|---|---|---|---|---|
| Revenue | $510.0M | $290.3M | $78.7M | +75.7% YoY; 176% 3-yr CAGR |
| Gross margin | **39.0%** | 42.3% | 33.5% | ⚠️ **Declining** (–330bp) |
| Operating income | **–$145.3M** | –$101.6M | –$133.9M | Operating loss; margin –28.5% |
| Net income | **+$237.8M** | –$481.6M | –$127.2M | ⚠️ Positive only via ~$390M non-operating gain |
| Operating EBITDA (derived) | **–$110.8M** | –$90.1M | –$116.9M | Core EBITDA negative |
| Adj. EBITDA (+SBC) (derived) | **–$61.0M** | –$31.6M | –$90.2M | Improving but negative |
| Reported EBITDA (as filed) | +$279.3M | –$468.1M | –$116.4M | ⚠️ Not a core-operating figure |
| Total debt / equity | –0.45 (n.m.) | — | — | Negative equity distorts |
| Debt / assets | 0.11 | 0.04 | 0.00 | Very low |
| Net debt / EBITDA | –3.03x (net cash) | n.m. | n.m. | Net cash |
| **Interest coverage (EBIT/Int.)** | **N/A** | N/A | N/A | No interest expense — genuinely debt-free |
| Current ratio | 2.15 | 0.87 | 3.89 | Strong |
| Quick ratio | 2.06 | — | — | Strong |
| Cash ratio | 1.54 | — | — | Strong |
| Working capital | **+$824.1M** | –$147.7M | +$157.7M | Reversed from negative |
| Cash / total liabilities | 0.38 | 0.16 | 0.19 | Improving |
| Equity / assets | **–0.25** | –0.87 | –2.48 | ⚠️ Negative but improving sharply |
| Operating cash flow | **–$10.5M** | +$452.0M | –$79.0M | ⚠️ 2024 quality issue (see below) |
| Capex | **–$382.7M** | –$23.4M | –$6.6M | ⚠️ **16x ramp** |
| Free cash flow | **–$392.8M** | +$428.5M | –$85.6M | Negative |
| FCF yield | **–1.94%** | — | — | Cash-consumptive |
| **Altman Z-Score** | **0.327 (Distress)** | — | — | ⚠️ **Distorted — disregard** |
| **Piotroski F-Score** | **5 / 9 (Moderate)** | — | — | Mediocre |

**Piotroski component detail:** F1 positive ROA = 1 (but flattered by non-cash gain) · **F2 positive operating CF = 0** · F3 ROA improvement = 1 · **F4 accruals quality = 0** · F5 lower leverage = 1 · F6 positive equity change = 1 · F7 no dilution = 1 · **F8 gross margin improvement = 0** · **F9 asset turnover improvement = 0**

The two failing sub-scores that matter most — F2 (negative operating cash flow) and F4 (poor accruals quality) — independently confirm the earnings-quality problem: **net income of +$237.8M alongside operating cash flow of –$10.5M**. F9 failing reflects $2.33B of assets now generating only $510M of revenue — capital deployed is not yet productive.

---

## 3. Market Risk Profile

| Metric | Post-IPO (130 trading days) | Full window (756d) |
|---|---|---|
| Annualised volatility | **111.6%** | 113.7% |
| Beta vs SPY | **3.32x** | 2.79x |
| Max drawdown | **–68.8%** | **–73.7%** |
| Sharpe ratio | **–1.13** | **–1.47** |
| Sortino ratio | Not available | — data gap |

**Price action:** IPO 14-May-2026 at $350.00, first close $311.07; intraday high $386.34 (IPO day). Close 18-Nov-2026: **$94.15** — **–69.7% from first close, –75.6% from the high.** Realised max drawdown of ~74% in six months of public life.

**Interpretation:** Beta of 2.8–3.3x means CBRS amplifies a market drawdown roughly threefold. A garden-variety 20% equity-market correction implies a **~55–65% CBRS drawdown**. Annualised vol of ~112% means a 1-sigma monthly move of roughly ±32%. Negative Sharpe confirms holders have been paid nothing for taking this risk. Note the company profile reports beta 1.85 — inconsistent with computed 2.79/3.32; the profile figure is likely peer-derived rather than measured, and I **discount it in favour of the computed values**.

---

## 4. Downside Scenario Analysis — Revenue –20%

Base: revenue $510.0M → **$408.0M**. Opex FY2025 = $344.3M (SGA $101.6M + R&D ≈$242.7M, derived).

| Line | Case A: no cost action, GM held 39% | Case B: GM –300bp to 36%, opex –15% |
|---|---|---|
| Revenue | $408.0M | $408.0M |
| Gross profit | $159.3M | $146.9M |
| Opex | $344.3M | $292.7M |
| **Operating income** | **–$185.0M** | **–$145.8M** |
| + D&A (~$35M) | EBITDA –$150.0M | EBITDA –$110.8M |
| Capex (cut to maintenance) | –$50M | –$50M |
| **FCF** | **≈–$235M** | **≈–$196M** |

**Liquidity survival:** Cash of $1,108M covers a –$196M to –$235M burn for **4.7 to 5.7 years** on pre-IPO cash alone, before any IPO proceeds (IPO priced at a $21B+ valuation in May 2026 — proceeds unverified, but a $1B+ primary raise is the reasonable inference and would extend runway to **8+ years**). **A 20% revenue decline produces a profitability problem, not a solvency problem.**

**Severe scenario — loss of the MBZUAI relationship (~62% of revenue):** revenue falls to ~$195M. Gross profit at 39% ≈ $76M, opex cut 40% to $207M → operating loss ~–$131M, FCF ~–$180M. Still survivable on the cash buffer alone for ~6 years. **But note the step function: this is not a gradual 20% grind, it is a binary contract event.** That asymmetry — not the arithmetic — is the real risk.

**What actually breaks in the downside case is the equity, not the balance sheet.** At 41.8x trailing sales ($21.3B market cap / $510M revenue; EV/sales 40.2x on $20.5B EV), a –20% revenue scenario with negative FCF justifies a multiple several times lower. The downside is a 50–75% further equity impairment and heavy dilution if capex must be funded externally — both consistent with the already-realised 74% drawdown.

---

## 5. Overall Financial Risk Rating

# HIGH

**Rationale.** Not **Critical**: the company holds $1.1B of cash against $262M of non-current, non-interest-bearing obligations, with a 2.15 current ratio and zero interest expense. There is no covenant, no maturity wall, no default path. Survival is not in question on any realistic horizon — including an extreme revenue shock.

But **High** on every other axis: negative core EBITDA (–$110.8M), negative operating cash flow, negative FCF (–$392.8M), negative book equity (–$578.7M), declining gross margin, deteriorating asset turnover, F-score of 5, and 86% revenue concentration in two UAE-linked counterparties — all wrapped in a 112%-volatility, 3.3-beta equity trading at 42x sales. The financial risk here is **equity-impairment and dilution risk, not credit risk.**

---

## 6. Key Red Flags

1. **⚠️ EXTREME CUSTOMER CONCENTRATION — the single dominant risk.** ~**86% of FY2025 revenue from two UAE-linked entities**: MBZUAI (~62%) and G42 (~24%). G42 alone was ~85–87% of FY2024 revenue. This is a **sovereign-adjacent, single-geography, contract-dependent revenue base.** Any non-renewal, renegotiation, or UAE export-control/geopolitical shift is a step-function impairment, not a gradual decline. G42 also held **77.9% of accounts receivable** at YE2025 — concentration extends to collection risk.
2. **⚠️ EARNINGS-QUALITY FAILURE.** Reported FY2025 net income of **+$237.8M** and EBITDA of **+$279.3M** are driven by roughly **+$390M of non-operating gains** (EBIT $244.9M vs operating income –$145.3M), most plausibly mark-to-market on preferred/warrant instruments. FY2024 shows the mirror image: a ~**–$378M non-operating loss**. Core operating income is **–$145.3M**. Independently corroborated by Piotroski F4 (accruals quality) = 0 and F2 (positive operating CF) = 0. **Do not underwrite this company on its reported bottom line.**
3. **Negative book equity of –$578.7M**; total liabilities ($2,905M) exceed total assets ($2,326M) by $262M. Retained deficit –$905.3M. Largely preferred-stock mechanics that reverse on IPO conversion — but the GAAP-reported capital structure is technically insolvent, which will trigger false positives in screening tools.
4. **Capex explosion with unproven returns.** Capex went $6.6M → $23.4M → **$382.7M** in three years (16x in one year), driving FCF to –$392.8M. Asset turnover deteriorated (F9 = 0) and gross margin fell 330bp — the capital being deployed is not yet converting into margin or velocity.
5. **2024 operating cash flow of +$452M was low quality** — flattered by a **+$443M working-capital inflow** (customer prepayments/deferred revenue). Strip that out and OCF was ~+$9M. The 2025 swing to –$10.5M is the underlying reality asserting itself.
6. **Declining gross margin** 42.3% → 39.0%, in a business that needs operating leverage to justify a 42x sales multiple.
7. **$38.1M of share repurchases in FY2025** while burning $393M of cash and carrying negative equity — poor capital allocation; likely compensation-related withholding, but not disclosed as such.
8. **Market risk: –76% from IPO high, 112% vol, 3.3 beta, –1.47 Sharpe.** Institutional risk limits (position-level vol caps, beta-adjusted exposure) will force selling independent of fundamentals.
9. **Valuation leaves no margin for error:** 41.8x trailing sales, 107x gross profit, negative FCF, on a revenue base that is 86% concentrated in two counterparties.

---

## Data Gaps & Caveats (explicit)

- **No post-IPO quarterly financials available** — tools returned annual data only. Current (Q3-2026) burn rate, cash balance, and IPO net proceeds are **unverified**. Runway figures use FY2025 cash of $1,108.2M and exclude IPO proceeds; true runway is materially longer.
- **No credit rating or CDS spread** — issuer is unrated.
- **No debt maturity schedule or covenant detail.** Total debt of $261.8M shows zero short- and long-term debt components, implying lease/financing obligations whose terms are not disclosed here. Covenant-breach risk therefore **cannot be fully excluded**.
- **Internal inconsistency:** the leverage tool reports net debt of –$846.4M (net cash) while the balance sheet row reports net_debt of –$439.9M. I use the **–$846.4M net cash** figure (derived directly from cash $1,108.2M less total debt $261.8M) and flag the discrepancy as unresolved.
- **No Sortino ratio, no peer comparables.** The sector peer tool returned mega-cap semis (NVDA, TSM, AVGO, AMD) whose scale and capital structure make them non-comparable to a $510M-revenue, 708-employee startup. **Relative valuation is not assessable from this data.**
- **Operating EBITDA / R&D expense derived, not reported** — calculated as operating income + D&A, and gross profit less operating income less SGA respectively.
- Beta conflict: profile reports 1.85; computed values are 2.79 (full) and 3.32 (post-IPO). Computed values used.

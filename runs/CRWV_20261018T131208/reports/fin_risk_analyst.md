# Fin Risk Analyst

- Symbol: CRWV
- Elapsed: 50.5s

---
# CoreWeave (CRWV) — Financial Risk Assessment
*Data as of latest filings (Q2 2026, period end 2026-06-30) and market data; equity quote $61.39 (market cap $33.9B), last daily close in feed $74.92 (2026-03-10).*

## 1. Credit Risk Assessment — **Sub-Investment Grade (Deep Junk / Distressed-Tier)**

CoreWeave is a levered AI-infrastructure build-out, not a cash-generative software business. Trailing-twelve-month (TTM) revenue is $7.59B with **EBITDA of $3.94B (51.9% margin)** but **EBIT of −$49M** — D&A of $3.99B (nearly all of it depreciation on GPU/DC assets) consumes the entire EBITDA. Every dollar of "profitability" is an accounting artifact of the depreciation schedule, and the capital structure is being financed at equity-like costs: the 9.75% 2031 notes traded near **78 cents for a ~16.4% YTM** and the 9.625% 2032 notes at **~14.8% YTM** (Oct-2026), i.e. the market prices this credit at distressed levels well inside a B/CCC band. Reported agency rating is B+ (single source, unverified) — the bond market is telling you it is weaker than that.

Solvency is entirely a function of continued access to capital markets. Net debt has compounded from $1.8B (2023) → $9.3B (2024) → $25.9B (2025) → **$45.2B (Q2 2026)** in roughly 30 months.

## 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | Q2'26 / TTM |
|---|---|---|---|---|
| Revenue ($M) | 229 | 1,915 | 5,131 | 7,590 (TTM) |
| EBITDA ($M) | (427) | 480 | 2,468 | 3,941 (TTM) |
| EBIT ($M) | (530) | (383) | 14 | (49) (TTM) |
| Net income ($M) | (594) | (863) | (1,167) | (1,926) TTM est.¹ |
| Total debt ($M) | 2,000 | 10,620 | 29,822 | **51,608** |
| Net debt ($M) | 1,783 | 9,259 | 25,876 | **45,211** |
| Debt / Equity | 3.4x | n.m. (neg. equity) | 8.94x | **10.3x** |
| Net debt / EBITDA | n.m. | 19.3x | 10.5x | **11.5x** |
| EBIT / Interest | n.m. | (1.06x) | **0.01x** | **(0.03x)** |
| EBITDA / Interest | n.m. | 1.33x | 2.01x | **2.10x** |
| Interest expense ($M) | 28 | 361 | 1,229 | **1,875 (TTM)** |
| Current ratio | 0.50 | 0.39 | 0.46 | **0.46** |
| Cash / current liabilities | 0.22 | 0.27 | 0.24 | **0.31** |
| Working capital ($M) | (496) | (3,047) | (8,952) | **(11,397)** |
| Equity / assets | neg. | neg. | 6.8% | **6.5%** |
| Altman Z-Score | — | — | **−0.14 (Distress zone)** | — |
| Piotroski F-Score | — | — | **5 / 9 (Moderate)** | — |
| FCF ($M) | (1,110) | (5,953) | (7,251) | **(13,655) TTM** |
| FCF yield | — | — | −27.2% | **≈ −40%** |

¹ Sum of Q3'25–Q2'26 net income: (110) + (452) + (740) + (626).
F-Score detail: 6 of 9 points pass, but **no positive ROA, dilution, gross-margin deterioration, and declining asset turnover** all fail — the "moderate" score flatters a business with negative EBIT.

**Data gaps flagged:** (i) `total_debt` ($51.6B) does not reconcile to short-term + long-term debt ($8.1B + $27.6B = $35.7B); the ~$15.9B difference is likely lease/finance obligations — treat gross obligations as ≥$51.6B. (ii) The Altman Z uses book equity, which mechanically punishes CRWV; the score is directionally correct but not literal. (iii) No CDS, no maturity-by-maturity schedule from the toolset — maturity ladder below is therefore not verified.

## 3. Market Risk Profile — Severe

| Metric | Value |
|---|---|
| Annualised volatility (252d) | **97.7%** |
| Beta vs SPY (252d) | **3.48x** |
| Beta (provider, longer window) | 7.32x — *conflicts with computed 3.48x; flag as unreliable* |
| Max drawdown (tool, 252d) | **−55.9%** |
| Max drawdown (close-to-close, since IPO) | $183.58 (6/20/25) → $64.55 (12/17/25) = **−64.8%** |
| Sharpe (0% rf) | 0.12 |
| Drawdown to current quote ($61.39) from IPO-era peak | **≈ −67%** |

A 3.5x beta with ~98% vol means a 20% SPY drawdown maps to a roughly 70% CRWV drawdown; the observed −65% peak-to-trough is consistent with this. This is a levered, single-theme, high-duration equity — it behaves like an option on AI capex sentiment, not a compounder (Sortino/Sharpe of 0.12 = no compensation for the risk taken).

## 4. Downside Scenario: −20% Revenue

Applied to TTM revenue of $7.59B (Q2 gross margin 65.9%):

- Revenue falls $1,518M; at ~66% contribution margin, **EBITDA drops ~$1,000M to ~$2.94B**.
- D&A is fixed and rising ($3.99B TTM, annualising Q2's $1.39B → ~$5.6B as the $63.3B PP&E base depreciates) → **EBIT ≈ −$2.6B**, interest coverage deeply negative.
- EBITDA/interest falls to **~1.6x**; with interest expense still climbing ($640M in Q2 alone, +$103M q/q), coverage approaches 1.0x within four quarters.
- **FCF worsens from −$13.7B toward −$15B**, against $6.41B of cash → a **funding gap of roughly $9B over twelve months** that must be raised in the debt or equity markets. Equity at $60/share for $9B = ~150M new shares on 551M outstanding (**+27% dilution**); debt at 15%+ coupons adds ~$1.35B of annual interest, compounding the problem.
- **Covenant/ratings risk:** with LTM EBITDA static and gross debt up ~$16B in six months, secured-leverage and minimum-liquidity tests would tighten materially. Downgrade → collateral calls / higher margins → reflexive spread widening.

**Key mitigant:** revenue backlog of **~$104B as of 6/30/26** (plus >$25B of commitments signed in Q3'26, per company filings). This is the single strongest argument against near-term default — but backlog is back-end-loaded, concentrated in a handful of AI labs/hyperscalers, and worthless if a counterparty's own funding stalls. The −20% scenario is therefore less likely to arrive via demand shortfall than via **counterparty renegotiation or customer concentration shock**; the toolset does not provide the customer-level revenue breakdown (flagged as a gap).

## 5. Overall Financial Risk Rating: **CRITICAL**

The thesis collapses if capital markets close. FY2025 and H1'26 show a business with:
- Negative EBIT and negative $13.7B TTM free cash flow, funded ~100% by new debt;
- Current ratio 0.46, negative working capital of $11.4B, and cash equal to **~1.1 quarters of the Q2 burn rate** ($6.41B cash vs $5.74B Q2 FCF deficit);
- Net leverage of 11.5x TTM EBITDA with EBITDA/interest of only 2.1x;
- Z-score in the distress zone and equity at 6.5% of assets (a ~7% asset write-down wipes out book equity).

The $104B backlog and demonstrated ability to raise tens of billions of secured debt are why this is *not* an imminent-default call — but bonds at 78 cents and 15–16% yields are the market's verdict on the refinancing path, and the equity is the cushion that gets consumed first.

## 6. Key Red Flags

1. **Liquidity cliff, not a leverage problem per se.** ~$6.4B cash against $5.7B quarterly FCF burn → <1 quarter of self-funding. Solvency is a function of the credit window, not operations.
2. **Interest coverage of ~0.0x on EBIT, 2.1x on EBITDA** — and interest expense is growing ~20% per quarter ($311M → $388M → $536M → $640M). Capitalised interest during construction likely understates true economic interest cost.
3. **Distressed bond pricing.** 9.75% '31 notes at ~78 (16.4% YTM), 9.625% '32 at 14.8% YTM — sub-investment-grade credit deteriorating *while* raising more debt. A $500M bridge obligation and reports of lenders passing on a $4B financing on the B+ rating are consistent with a narrowing funding runway.
4. **Massive dilution risk.** Share count 435M (FY25) → 551M (Q2'26), +27% in six months; another large equity raise at distressed prices is the likely marginal funding source.
5. **Depreciation leverage.** D&A = 101% of EBITDA; if useful-life assumptions on GPUs shorten (or residual values fall as next-gen silicon arrives), reported EBIT and any EBITDA-minus-maintenance-capex metric deteriorate instantly.
6. **Balance-sheet opacity.** $15.9B of obligations sit outside reported STD/LTD; PP&E grew $24.5B in H1'26 against only $14.1B of capex, implying a large lease/asset-acquisition channel whose terms are not visible in the data.
7. **Counterparty concentration.** Undisclosed at the tool level; the 20% downside case runs through customer renegotiation, not through GPU prices.
8. **Beta of 3.5x with −65% realized drawdown** — position sizing risk alone justifies a risk-premium far above what the 0.12 Sharpe implies.

**Bottom line:** Investment-grade quality is absent on every axis — leverage, coverage, liquidity, cash generation, credit spreads, and volatility. This is a Critical-risk, capital-markets-dependent credit with a genuine solvency question in any 12-month window where financing conditions tighten materially, offset only by a very large contracted backlog that the data tools cannot independently verify.

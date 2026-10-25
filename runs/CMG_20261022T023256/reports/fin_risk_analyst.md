# Fin Risk Analyst

- Symbol: CMG
- Elapsed: 593.5s

---
All data gathered. Writing the assessment now.

---

# CHIPOTLE MEXICAN GRILL (CMG) — FINANCIAL RISK ASSESSMENT

**Sector:** Consumer Cyclical / Restaurants · **Market cap:** ~$35.5–37.8B · **Price:** $28.09 · **Period basis:** FY2025 annual + Q2-2026 LTM

## 1. Credit Risk Assessment

**Rating: INVESTMENT GRADE (implied) — but with a structural caveat**

The single most important finding: **CMG carries zero funded debt.** Every period from 2021 through Q2-2026 reports `interest_expense = 0`, and the balance sheet shows `short_term_debt = 0` and `long_term_debt = 0`. The reported "total debt" of $5,075.8M is therefore **operating lease liabilities under ASC 842**, not borrowings. This is confirmed by the absence of any interest expense (operating leases produce straight-line rent in operating expense, not interest).

Consequences:
- **Interest coverage ratio is effectively infinite** (EBIT $2,012.8M vs. ~$0 interest). The tool returns `null` because the denominator is zero — this is a strength, not a gap.
- **No refinancing cliff and no financial covenants.** There is no debt maturity schedule to breach, because there is no funded debt. The only fixed obligations are lease payments on ~4,000+ restaurants, which are matched to revenue-generating assets.
- The high `debt_to_equity` of 1.79x is a **lease-accounting artifact**, not a solvency signal. On a funded-debt basis, CMG is net-cash-positive historically; the "net debt" of $4.03B is the capitalized value of its lease book.

**Weakness within the credit story:** the equity cushion is being deliberately shrunk. Total equity fell from $3,655.5M (FY24) to $2,830.6M (FY25), a −22.6% decline, driven by $2,425.5M of buybacks against $1,447.6M of FCF. That is the reason the Piotroski F-Score loses its leverage and equity-change points. Leverage is rising not because debt is being added for growth, but because capital is being returned faster than it is earned.

**Peer context (MCD, the only valid restaurant comp in the peer set):** CMG is materially stronger on every balance-sheet dimension — net debt/EBITDA 1.7x vs. MCD 3.68x; current ratio 1.23 vs. 0.95; equity/assets 0.31 vs. **−0.03** (MCD has negative book equity); cash/liabilities 0.17 vs. 0.01. CMG's credit profile is superior; its *market* risk is not (see §3).

## 2. Key Financial Risk Metrics Table

| Metric | CMG FY2025 | Benchmark / Comment |
|---|---|---|
| Debt / Equity | 1.79x | Lease-driven; funded debt = $0 |
| Debt / Assets | 0.56x | 92%+ of "debt" is lease PV |
| Net Debt / EBITDA | 1.70x | 2.08x on LTM H1-26 EBITDA ($2,274M) |
| Interest Coverage (EBIT/Int.) | N/A (≈∞) | Interest expense = $0 in all periods |
| Altman Z-Score | **2.47 — Grey zone** | ~5.9 if market cap substituted for book equity |
| Piotroski F-Score | **6 / 9 — Moderate** | Fails F5 (leverage), F6 (equity), F8 (gross margin) |
| Current Ratio | 1.23 | vs. MCD 0.95 |
| Quick Ratio | 1.19 | vs. MCD 0.94 |
| Cash Ratio | 0.88 | Cash & ST inv. $1,044.6M |
| Working Capital | **+$278.8M** | vs. MCD −$198M |
| Cash / Total Liabilities | 0.17 | Low, but no funded debt to service |
| FCF (FY25) | $1,447.6M | Down from $1,511.5M in FY24 |
| FCF Yield | 3.83% | Modest; ~2.4% in downside case |
| FCF Margin | 12.1% | 13.4% (FY24) → 12.4% (FY23) → 12.1% (FY25) |
| Capex | $666.3M | +12.2% YoY; 5.6% of revenue |
| Buybacks | $2,425.5M | **1.68x FCF** — funded partly from cash |
| Cash balance change | $1,422.9M → $1,044.6M | −$378.3M despite positive FCF |

**Note on the Altman score:** the grey-zone reading is mechanically distorted. The x4 term uses book equity ($2,830.6M), giving 0.459. Substituting market capitalization (~$37.75B) gives x4 ≈ 6.12, which lifts Z to **≈5.9 — deep in the safe zone.** Economically, bankruptcy risk is negligible; the grey zone is an artifact of a lease-heavy, buyback-shrunk balance sheet. I present both readings rather than relying on the tool's headline.

**Leverage trajectory:** Net debt/EBITDA moved from ~1.5x (FY23) to 1.7x (FY25) to 2.08x on LTM H1-2026, as EBITDA declined while lease liabilities grew with new units. This is a genuine but slow-moving trend.

## 3. Market Risk Profile

| Metric | CMG | MCD (peer) |
|---|---|---|
| Annualised volatility (3Y) | **38.07%** | 18.58% |
| Beta vs. SPY | 0.806 (3Y) / 0.958 (5Y, profile) | 0.148 |
| Max drawdown (3Y) | **−57.5%** | −30.98% |
| Sharpe ratio (3Y, rf=0%) | **−0.655** | −0.179 |

CMG's beta is below 1.0 (0.81 on the 3-year window), which superficially suggests defensive characteristics. **The drawdown and Sharpe numbers contradict that reading.** A −57.5% peak-to-trough decline against an S&P drawdown of roughly half that magnitude, combined with 38% annualised volatility — more than double MCD's 18.6% — means CMG's risk is overwhelmingly **idiosyncratic**, not systematic. The negative 3-year Sharpe (−0.655) means shareholders have not been compensated for that volatility even at a 0% risk-free assumption. For a risk function, this is the most important market observation: **low beta is not low risk here.** Position sizing should be driven by the 38% vol and −57.5% tail, not the 0.81 beta.

## 4. Downside Scenario Analysis — 20% Revenue Decline

Applied to FY2025 base revenue of $11,925.6M → **$9,540.5M**. Fixed costs held at FY25 levels (SG&A $652.0M, D&A $361.4M).

| Line | Base FY25 | −20% Revenue | Δ |
|---|---|---|---|
| Revenue | $11,925.6M | $9,540.5M | −20.0% |
| Gross margin | 25.38% | 25.38% (held) | — |
| Gross profit | $3,026.2M | $2,421.4M | −20.0% |
| SG&A + D&A (fixed) | $1,013.4M | $1,013.4M | 0% |
| **EBIT** | **$2,012.8M** | **$1,408.0M** | **−30.0%** |
| EBITDA | $2,374.2M | $1,769.4M | −25.5% |
| Net debt / EBITDA | 1.70x | **2.28x** | +0.58x |
| FCF (capex cut to ~$450M) | $1,447.6M | **~$900M** | −38% |
| FCF yield | 3.83% | ~2.4% | −143bps |

**The critical mechanic is operating leverage.** A 20% revenue decline produces a 30% EBIT decline because ~$1.01B of cost is fixed — roughly 40% of gross profit. Each 100bps of gross margin is worth ~$119M of EBIT and ~$91M of net income (~$0.07 EPS).

**With realistic margin compression** (gross margin falling a further 200bps to 23.5%, consistent with the observed −215bps YoY trend in Q2-2026): EBIT ≈ $1,229M (−39%), net income ≈ $938M, diluted EPS ≈ $0.72 vs. $1.14 (−37%).

**Severe stress case (−35% revenue, gross margin 21%):** revenue $7,752M, gross profit $1,628M, EBIT ≈ $615M, EBITDA ≈ $976M → net debt/EBITDA ≈ **4.1x**, FCF near breakeven (~$100M). Even here there is **no default trigger**: no funded debt maturities, no covenants, and $1,044.6M of cash. The binding constraint is not solvency — it is the **$2.43B buyback program**, which would have to be suspended (freeing ~$2.4B/yr of discretionary cash) and which in the base case is already drawing down the cash balance.

**Verdict on the downside:** CMG survives a prolonged 20–35% revenue contraction without credit event. The damage is to earnings and the buyback, not to solvency. Liquidity risk is low; earnings risk is high.

## 5. Overall Financial Risk Rating

# **MODERATE**

**Rationale.** The balance sheet is close to fortress-grade on the dimensions that cause default: zero funded debt, no covenants, no refinancing maturities, positive working capital, $1.04B cash, and $1.45B of FCF. Lease-adjusted leverage of 1.7x compares favorably to MCD's 3.68x. That precludes a High or Critical rating.

It is not Low for three reasons: (1) **margin compression is now measurable and accelerating** — operating margin fell from 18.8% (Q2-25) to 15.7% (Q2-26) while revenue *grew* 9.3%; (2) **FCF is declining while revenue grows** ($1,511M → $1,448M) and FCF yield is only 3.8%; (3) **equity is being consumed by buybacks** at 1.68x FCF, thinning the buffer exactly as leverage drifts up. Add 38% volatility and a −57.5% three-year drawdown, and "Moderate" is the correct band — solid credit, fragile equity narrative.

## 6. Key Red Flags

1. **Operating margin compression against revenue growth (highest concern).** Q2-2026 revenue +9.3% YoY but operating income −8.6%; gross margin −215bps YoY (27.36% → 25.22%). H1-2026 operating margin 14.7% vs. 18.0% in H1-2025. This is the pattern that precedes a de-rating, and it is already visible in the −57.5% drawdown.
2. **FCF erosion.** FCF $1,511.5M (FY24) → $1,447.6M (FY25) on 5.4% revenue growth; FCF margin 13.4% → 12.1%; capex up 12.2%. Growth is consuming more capital per dollar of cash generated.
3. **Buybacks exceeding FCF.** $2,425.5M repurchased vs. $1,447.6M FCF = 1.68x. Cash fell $378.3M and total equity fell 22.6% in one year. Financial flexibility now depends on sustained FCF — a procyclical structure.
4. **Revenue growth deceleration.** FY2025 +5.4% vs. +14.6% (FY24), +14.3% (FY23). The growth engine that justified a premium multiple is slowing.
5. **Market/tail risk.** −57.5% max drawdown, 38.1% vol, Sharpe −0.655. Beta of 0.81 understates real risk; this is an idiosyncratic-risk name.
6. **Altman grey zone (2.47)** — artifact of book-equity x4 and lease-heavy structure, not a genuine distress signal, but worth monitoring as equity shrinks.

## 7. Data Gaps (explicitly flagged)

- **Credit rating and CDS spreads:** not available in the dataset. Rating is *inferred* from balance-sheet fundamentals, not observed.
- **Debt maturity schedule:** no itemized schedule returned. **Materiality is low** — funded debt is zero, so there is no maturity ladder to assess. Lease maturity profile (weighted-average term not disclosed) is the only fixed-obligation schedule.
- **Revolving credit facility size / availability:** not disclosed. Would matter for liquidity backstop assessment.
- **US Treasury yield curve:** the `fetch_yield_curve` tool failed twice (data-feed error) — noted as unavailable. Immaterial for CMG specifically, since it has no floating-rate funded debt; would matter only for discount-rate/cost-of-capital framing.
- **News/qualitative risk factors:** web search returned entirely irrelevant results (unrelated "sales" pages), so no external commentary on cost inflation, tariffs, or food-safety litigation was incorporated. **The margin-compression diagnosis is drawn purely from reported financials.**
- **Peer set limitations:** the sector peer list is "Consumer Cyclical" and includes AMZN, TSLA, HD, BABA, TM — only MCD is a meaningful restaurant comparable. Peer multiples/relative valuation unavailable.
- **Internal inconsistencies:** net debt is reported as $4,031.2M by the leverage tool but $4,725.3M on the balance-sheet row (the latter does not reconcile to total debt − cash); market cap is $35.55B in the profile vs. $37.75B in the FCF-yield calc. Ratios above use the reconciling figure ($4,031M) and note both market caps; differences do not change any rating conclusion.

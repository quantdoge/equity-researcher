# Fin Risk Analyst

- Symbol: RVMD
- Elapsed: 142.3s

---
## RVMD — Revolution Medicines, Inc. | Financial Risk Assessment
*Clinical-stage precision oncology (RAS-driven cancers). Data as of FY2025 10-K (12/31/25) and latest quarter 6/30/26. Price $196.55; market cap ≈$42.1B.*

---

### 1. Credit Risk Assessment: **Investment Grade *balance sheet* / Unrated issuer — Sub-Investment-Grade (pre-revenue) with fortress liquidity**

RVMD has **no revenue, no earnings, and no debt-service capacity from operations** — it is funded entirely by equity and, since April 2026, a small convertible. In a rating-agency sense this is a speculative-grade, unrated credit. But the *default math* is benign: debt is $642M against $3,939M of cash and investments (**net cash ≈ $3.30B**), there are no near-term maturities, and the only bond ($500M, 0.50% converts **due 2033**, conversion price ≈$198.80 — essentially at-the-money vs. today's $196.55) is far more likely to convert into equity than to be repaid in cash.

**Default risk through 2028: negligible.** Altman Z of **-0.995 ("Distress")** must be rejected as mechanically invalid here: X5 (asset turnover) = 0.00 and X2 (retained earnings/TA) = -1.22 because the company has deliberately zero revenue and a $3.97B accumulated deficit by design. Same for the **Piotroski F-Score of 1** — a pre-revenue biotech fails F1–F3, F5, F6, F8, F9 structurally; only F7 (dilution) is a genuine signal.

### 2. Key Financial Risk Metrics

| Metric | FY2023 | FY2024 | FY2025 | Q2'26 (6/30/26) |
|---|---|---|---|---|
| Revenue | $11.6M | $0 | $0 | $0 |
| Net income | -$436M | -$600M | **-$1,131M** | -$644M (qtr) |
| Free cash flow | -$358M | -$568M | **-$914M** | -$390M (qtr) |
| Cash & investments | $1,853M | $2,289M | $2,026M | **$3,938M** |
| Total debt | $88M | $136M | $159M | **$642M** |
| Net cash (cash − debt) | $1,765M | $2,153M | $1,867M | **+$3,296M** |
| Debt / equity | 4.8% | 6.0% | 9.7% | **24.6%** |
| Debt / assets | 4.3% | 5.3% | 6.7% | **14.8%** |
| Current ratio | 13.1x | 14.2x | 7.1x | **11.4x** |
| Quick / cash ratio | 13.1x | 14.2x | 7.1x / 6.97x | **11.4x / 11.1x** |
| Working capital | $1,735M | $2,164M | $1,785M | **$3,674M** |
| Interest coverage (EBIT/int.) | NM | NM | **-45.7x** | NM |
| Net debt / EBITDA | NM (negative EBITDA) | NM | NM | NM (net cash) |
| Altman Z | — | — | **-0.995 (Distress)** | — |
| Piotroski F | — | — | **1 / 9 (Weak)** | — |
| FCF yield | — | — | **-2.45%** | -3.3% (TTM) |
| Equity / assets | 88.6% | 88.5% | 69.3% | 60.3% |

**Liquidity / cash runway (the binding constraint).** Burn is accelerating fast: FCF of -$154M (2021) → -$914M (2025), a **56% CAGR**, with 2025 alone up **+61% YoY**. Quarterly FCF: -$211M (Q3'25) → -$276M (Q4'25) → -$356M (Q1'26) → -$390M (Q2'26). TTM burn = **-$1,232M**; Q2'26 annualised run-rate = **-$1,558M**.
- Runway at current run-rate: **$3,938M / $1,558M ≈ 2.5 years (≈Q4 2028)**
- Runway on TTM burn: **≈3.2 years**
- On guidance (FY2026 GAAP opex **$1.6–1.7B**, +35–44% vs. FY2025 opex of $1,182M) with compounding burn: **cash lasts roughly to mid-2028**, implying one more raise in 2027–28.

RVMD has repeatedly demonstrated capital access: a $600M equity raise (Dec-2024) and an **upsized ~$2.2B concurrent offering (April 2026)** — 10.56M+ shares plus $500M of 0.50% converts. Shares outstanding rose 167.7M → 190.1M (2025) → **210.9M (Q2'26)**, i.e. **+13% then +11% dilution**. Dilution, not default, is the cost of this balance sheet.

### 3. Market Risk Profile

| Measure | Value |
|---|---|
| Annualised volatility (756d) | **56.9%** |
| Beta vs SPY (3y regression) | **1.10** (FMP 5-yr beta: 1.40) |
| Max drawdown (3y) | **-48.6%** |
| Sharpe (3y, rf=0) | **1.49** |
| Sortino | *Not available from tools — data gap* |

Volatility of ~57% is extreme even for biotech (typical 35–50%), and the 48.6% peak-to-trough drawdown shows the equity is priced on binary clinical readouts, not cash flows. The strong 1.49 Sharpe reflects the enormous re-rating of the RAS(ON) franchise, not low risk — the return distribution is acutely right-skewed with fat left tails. A beta of 1.1 understates true drawdown risk in a market selloff, because the idiosyncratic component (which dominates total variance) is uncorrelated with the market and therefore *additive* to market beta losses.

### 4. Downside Scenario Analysis

**The mandated "20% revenue decline" test is non-binding:** revenue is already **$0**, so a 20% cut to zero is economically a no-op. I have substituted the stresses that actually matter for this issuer:

| Scenario | Mechanics | Financial impact | Solvency consequence |
|---|---|---|---|
| **A. 20% burn expansion** (Phase 3 scale-up / enrolment slippage raises FY27 opex to ~$2.1B+) | Burn $1.56B → $1.87B | Runway 2.5y → **2.1y**; raise pulled forward to 2027 | None — still net cash ~$2B |
| **B. Loss of partnership economics** (Sanofi/other collaboration income, $16.6M cost-of-revenue royalty obligation) | Immaterial at 0.5% of the balance sheet | <2% of cash | None |
| **C. Macro drawdown: market -20%** | Beta 1.10 × (-20%) = -22% expected; plus 57% idiosyncratic vol | Plausible path **-35% to -45%** | None — no margin/covenant linkage |
| **D. Lead-asset (daraxonrasib/RMC-6236) clinical failure — the real tail** | Equity repriced to option value on remaining pipeline | **-60% to -80%** vs. 48.6% observed max DD | Debt unimpaired ($3.9B cash vs $642M debt); converts go out-of-the-money → no cash claim, but future capital access and terms deteriorate sharply |

**Note on the 2026 financing:** the April 2026 offer was struck at a $198.80 conversion price — essentially today's spot. If the stock falls 40%+, that $500M becomes straight debt maturing 2033; still trivially covered by cash. If it rises, it converts and self-liquidates. This is a well-structured liability, not a refinancing cliff.

### 5. Overall Financial Risk Rating: **MODERATE**
Split view: **Credit & liquidity risk = LOW** (net cash $3.3B, 11x current ratio, no maturities before 2033, no financial covenants identified). **Market/binary risk = HIGH** (57% vol, -49% drawdown, single-franchise concentration). Blended: **Moderate for the enterprise, High for the equity.** The 2025/2026 step-up in leverage (debt/equity 9.7% → 24.6%) is a genuine trend but remains trivial in absolute terms.

### 6. Key Red Flags

1. **Burn acceleration is structural, not one-off.** FCF worsened 61% in 2025 and another ~40% annualised into Q2'26; FY2026 opex guide of $1.6–1.7B (+35–44%) confirms further step-up. Runway of ~2–2.5 years requires recurring capital markets access.
2. **Unexplained non-operating charges — verify before relying on any earnings figure.** Reported interest expense reached **$23.8M in a single quarter** (~$95M annualised) against a $500M convert bearing a **0.50% coupon (~$2.5M/yr cash)** — roughly $90M/yr is unexplained and cannot be lease interest on $642M of debt. Separately, Q2'26 net loss of -$644M vs. operating loss of -$505M implies **~$115M of non-operating expense**. This needs 10-Q footnote confirmation; treat all coverage ratios as unreliable until resolved.
3. **Persistent dilution:** +13% shares (2025), +11% to Q2'26; ~$2.2B raised in April 2026. Equity holders bear the funding cost of the balance-sheet strength.
4. **Binary concentration:** enterprise value rests on a single RAS(ON) franchise; 48.6% drawdown already realised within 3 years.
5. **Negative gross profit:** $16.6M cost of revenue against $0 revenue in FY2025 (contractual royalty obligations on in-licensed IP) — an unusual, recurring cash charge with no offsetting revenue.
6. **$3.97B accumulated deficit**; retained earnings/TA of -1.22 mechanically disables standard distress screens.

**Data gaps flagged:** (a) no credit rating or CDS spread available — the company is unrated; (b) Sortino ratio not computable from available tools; (c) the balance-sheet feed's `net_debt` field is internally inconsistent (reports -$225M for FY2025 and -$174M for Q2'26 vs. -$1,867M / -$3,296M computed from cash less total debt) — all net cash figures above are my own computation; (d) Q2'26 stock-based compensation was reported as 0 (vs. $87.3M in Q1'26), likely a feed omission, so non-cash add-backs for that quarter are unverified; (e) indentures/covenant packages not reviewed.

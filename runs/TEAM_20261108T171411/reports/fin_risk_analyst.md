# Fin Risk Analyst

- Symbol: TEAM
- Elapsed: 92.1s

---
# TEAM (Atlassian Corporation) — Financial Risk Assessment
**Data as of FY2026 (fiscal year ended 30-Jun-2026, filed 14-Aug-2026); market data through 31-Jul-2026**

---

## 1. Credit Risk Assessment

**Rating: Investment Grade, with a negative watch bias**

The 2024 S&P issue-level rating on Atlassian's senior unsecured notes was **'BBB'** (the only agency action retrievable; *no Moody's/Fitch rating, issuer-level rating, or CDS spread could be sourced — data gap, and the rating predates the FY26 deterioration and the 2026 equity collapse*).

The credit is structurally sound on a cash basis but optically weak on a GAAP basis:

| Signal | Reading |
|---|---|
| Net debt | **–$6.6M** (net cash; cash $1.240B vs debt $1.233B) — down from –$1.274B net cash in FY25 |
| Gross leverage | 5.8x debt/EBITDA (EBITDA only $212M because GAAP earnings are near zero) |
| Interest coverage | **0.21x** on operating income (vendor calc: $10.4M / $49.5M); 1.4x on EBIT; **4.3x EBITDA**; **26.6x FCF** |
| Altman Z | **–0.31 ("Distress")** — driven almost entirely by x2 (–1.00, retained earnings –$6.105B accumulated deficit) |

**Critical interpretive point:** the Altman distress score and the 0.21x coverage ratio are artifacts of SBC-driven accumulated deficits and non-cash interest amortisation, not cash insolvency. On a market-capitalisation basis x4 becomes 5.21–7.71 (vs 0.21 book), lifting Z to **~2.69 (grey zone) at $101/share, or ~4.19 (safe zone)** at the vendor's $153.68 mark. Coverage on the metric that actually matters — FCF/interest — is 26.6x. The convertibles carry low cash coupons; the $49.5M "interest expense" (up 62% YoY from $30.6M) is substantially amortisation of issuance costs. **Conclusion: not a credit-impaired business, but one with essentially no GAAP earnings buffer to absorb a shock.**

---

## 2. Key Financial Risk Metrics

| Metric | FY2024 | FY2025 | FY2026 | Risk Read |
|---|---|---|---|---|
| Revenue ($M) | 4,358.6 | 5,215.3 | 6,572.3 | +26.0% YoY — strong |
| Gross margin | 81.6% | 82.9% | 84.8% | Improving |
| Operating margin | –2.7% | –2.5% | **+0.16%** | Barely breakeven |
| Net income ($M) | –300.5 | –256.7 | –53.8 | Persistent losses |
| EBITDA ($M) | 27.4 | 24.0 | 212.2 | Thin vs. $1.23B debt |
| **Debt/Equity** | 1.21x | 0.92x | **1.16x** (book) | High on book only; ~0.05x at market |
| **Net debt/EBITDA** | –0.76x | –1.27x | **–0.03x** | Net-cash — de minimis |
| **Interest coverage** | 0.21x | 0.21x | **0.21x** (EBIT basis) | Weakly covered on GAAP |
| **Current ratio** | 1.18x | 1.22x | **0.78x** | Sub-1 (deferred-revenue effect) |
| Quick / cash ratio | 0.99x / 0.42x | 1.05x / 0.55x | **0.78x / 0.35x** | Cash/liabilities 0.25x |
| Working capital | –$1.339B | +$710M | **–$774M** | Negative |
| Equity/Assets | 19.8% | 22.3% | **17.3%** | Thin |
| **Altman Z** | — | — | **–0.31** (book) / 2.7–4.2 (mkt) | Book-distorted |
| **Piotroski F** | — | — | **6 / 9** | Moderate; fails ROA (F1), leverage (F5), equity change (F6) |
| **FCF ($M)** | 1,415.0 | 1,415.5 | **1,319.1** | Absolute FCF flat/declining |
| **FCF margin** | 32.5% | 27.1% | **20.1%** | **Deteriorating hard** |
| FCF yield | — | — | **3.3%** (vendor mkt cap) – **5.0%** (at $101.02) | See data-gap note |
| Tangible equity ($M) | –555 | –204 | **–1,677** | Negative; goodwill 45% of assets |

**Liquidity verdict:** The 0.78x current ratio and –$774M working capital look alarming but are a billings-model artefact — $3.571B of current liabilities are dominated by deferred revenue (line item not returned by the feed; **inferred, flagged as gap**). Cash is pre-collected, not owed to lenders. Real liquidity: **$1.240B cash + $1.319B annual FCF = ~$2.56B of near-term coverage**, minimal short-term debt (**$48.5M, only 3.9% of total debt**), and $989.6M long-term. **No refinancing cliff.** But the cash buffer fell 58% in one year ($2.937B → $1.240B).

---

## 3. Market Risk Profile

*The volatility tool is unavailable on the current data plan (FMP `historical-price-eod/dividend-adjusted` not subscribed); the figures below are computed manually from the daily close series — treat as coarse estimates.*

| Metric | Value | Comment |
|---|---|---|
| **Max drawdown (3y)** | **–82.3%** | $322.94 (10-Feb-2025) → $57.15 (10-Apr-2026) |
| Current price | $101.02 | Still **–69%** below the Feb-2025 peak |
| **Annualised volatility** | **~65% (estimate, range 55–90%)** | Monthly-return estimator 90%; 3-4x the index |
| **Beta** (vendor) | **1.14** | But R² likely low — risk is idiosyncratic, not market |
| 3-year cumulative return | **–47.3%** (from $191.74) | Annualised ≈ **–15.7%** |
| **Sharpe (3y, rf=0%)** | **≈ –0.24** | Negative; risk-adjusted returns are value-destructive |
| Sortino | Negative / not meaningful | Downside deviation swamps upside |
| Single-month moves (trailing 12m) | **+56.9% (May-26), –36.4% (Feb-26), –27.7% (Jun-26), –27.1% (Jan-26)** | Extreme gap risk |

**Interpretation:** this is a high-beta-to-itself, earnings-event-driven equity. The Jan–Apr 2026 collapse (–75% in four months, on ~14M-share volume spikes) occurred while revenue was *growing 26%* — a pure multiple compression event (from ~25x EV/S to ~4x). **The specific trigger is unverified (searches returned no usable news — data gap).** For a creditor this matters because a depressed share price converts an equity-settled convertible into a cash obligation.

---

## 4. Downside Scenario: Revenue –20%

FY26 base: revenue $6,572M, gross margin 84.8%, total opex $5,565M (SG&A $2,296M + implied R&D ~$3,269M = 84.7% of revenue), interest $49.5M, cash $1,240M.

**Case A — no cost action** (revenue $5,258M, GM holds at 84.8%)
- Gross profit $4,458M – opex $5,565M = **EBIT –$1,107M**; EBITDA –$966M
- Interest coverage: **negative**. FCF: roughly **–$35M to –$295M** before a deferred-revenue unwind (billings shrink ⇒ ~–$300M working-capital cash hit in year 1)
- **Total cash burn ~$350–600M in year 1** vs $1.24B cash → **~2 years of runway**, and that competes directly with the $990M long-term notes

**Case B — 12% opex reduction** (realistic; Atlassian can cut S&M/hiring)
- Opex → $4,897M; **EBIT –$439M**, EBITDA –$298M; FCF **≈ –$100M to –$200M** → **4–6 years of coverage**

**The decisive mitigant:** share repurchases of **$1.800B in FY26 (27% of revenue)** are wholly discretionary. Suspending them frees more cash than the worst-case FCF shortfall in a single year. Combined with the $1.24B cash balance and net-cash position, **a 20% revenue decline is a growth/equity problem, not a solvency problem.** Deferred revenue of ~$2.4B provides a liquidity *cushion* in a downturn (customers still pay annually in advance) but reverses on the way out.

**Covenant risk:** no covenant terms, revolver capacity, or maturity schedule detail is available in the data — **critical gap**. The unsecured BBB structure suggests light maintenance covenants, but this is unconfirmed.

---

## 5. Overall Financial Risk Rating

# MODERATE
*(Credit risk: Investment Grade / Low-Moderate. Market & equity risk: HIGH.)*

The balance sheet is net-cash, FCF is $1.3B, and leverage is effectively nil. What keeps this from "Low" is a structural earnings-quality problem: **GAAP operating margin of 0.16% and interest coverage of 0.21x mean there is no accrual cushion**, and cash generation is *declining* while revenue grows. What keeps it from "High" is that the cash, the discretionary buyback, and the deferred-revenue model give it multiple years of room under any realistic stress.

---

## 6. Key Red Flags

1. **FCF margin collapse: 32.5% → 20.1% in two years.** Operating cash flow *fell* $107M YoY to $1,353M while revenue rose $1,357M. Incremental revenue is being generated at negative cash contribution — the most important deterioration in the dataset.
2. **SBC of $1.607B = 24.4% of revenue, exceeding FCF.** SBC-adjusted FCF is **–$288M**. FY26 buybacks ($1.800B) exceeded SBC ($1.607B); that treadmill is what actually consumed the cash pile.
3. **Cash buffer –58% in one year** ($2.937B → $1.240B) after $1.800B of buybacks at an average price far above today's $101 + ~$1.2B of M&A (goodwill & intangibles $1.549B → $2.735B). **Buying back stock at $200+ with FCF at $1.3B was value-destructive and consumed the liquidity cushion.**
4. **Negative tangible equity: –$1.677M million** — goodwill/intangibles are 45% of $6.104B total assets. Post-crash, **impairment risk on the FY26 acquisition is material** and would be a non-cash but optically damaging hit to already-thin book equity (17.3% of assets).
5. **Convertible-overhang ambiguity:** $990M long-term debt with the stock 69% below its peak is very likely deep out-of-the-money, forcing cash settlement rather than equity — against a $1.240B cash balance. Conversion terms, put dates, and maturity schedule are **unavailable**; this is the single largest unquantified risk.
6. **Interest expense +62% YoY** ($30.6M → $49.5M) while debt was flat — check for a new higher-cost facility or accelerated amortisation.
7. **–82.3% max drawdown and ~65% annualised vol with negative Sharpe** — high cost of equity, limited ability to use stock as acquisition currency, and reflexive risk (low price ⇒ convert settles in cash ⇒ liquidity strain).

**Explicit data gaps:** (a) vendor market cap ($38.9B at $153.68) is **inconsistent** with the last close ($101.02 × ~260M diluted shares ≈ **$26.3B**) — FCF yield is therefore presented as a 3.3%–5.0% range; (b) no deferred revenue, revolver, maturity schedule, or covenant line items; (c) no Moody's/Fitch rating or CDS spread; (d) volatility/beta recomputed manually due to plan limits; (e) cause of the Jan–Apr 2026 collapse unverified.

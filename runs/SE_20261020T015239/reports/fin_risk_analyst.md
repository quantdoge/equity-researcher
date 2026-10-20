# Fin Risk Analyst

- Symbol: SE
- Elapsed: 122.4s

---
I have sufficient data. Writing the assessment now.

---

# Sea Limited (SE) — Financial Risk Assessment

**Price $88.47 · Market cap $54.19B · FY2025 (period end 2025-12-31) · Reporting ccy USD · Singapore-domiciled, EM/global revenue**

---

## 1. Credit Risk Assessment

### Rating: **INVESTMENT GRADE (balance-sheet basis) — unrated by agencies**

Sea carries **more net cash than gross financial debt**, with interest coverage above 55x. On pure credit metrics this is an IG-quality balance sheet. Two important qualifications:

- **No public agency rating was found** (Moody's/S&P/Fitch) in my searches — Sea is effectively an *unrated* issuer. This is normal for high-growth Asian internet platforms, but it means **no rating-driven forced-selling or index-membership support**, and no independent credit opinion to lean on. *Data gap flagged.*
- Business-risk is emerging-market consumer internet (Indonesia, Brazil, Thailand, Vietnam, Philippines) with a growing consumer lending book. Even a pristine balance sheet would not earn an IG *issue* rating in this cohort — I'd estimate **BB+ / Ba1** on a through-the-cycle business-risk view, i.e. one notch below IG, with the balance sheet as the offsetting strength.

**Key credit observations:**

| Item | Value | Read |
|---|---|---|
| Gross financial debt (ST + LT) | $2,212M | Trivial vs. cash |
| Total debt incl. leases (feed) | $3,330M | |
| Cash & ST investments | $12,789M | |
| Net cash (broad: cash&STI − total debt) | **+$9,459M** | Net cash equal to 3.5x EBITDA |
| Net cash (narrow: cash equiv. − financial debt) | **+$3,045M** | Most conservative definition — still net cash |
| Net debt / EBITDA | **(3.55x)** net cash | |
| Debt / equity | 0.26x | |
| Debt / assets | 0.11x | |
| **Interest coverage (EBIT/interest)** | **55.5x** (feed) / 68.3x (recomputed EBIT $2,296M ÷ $33.6M) | Effectively debt-insensitive |
| Effective interest rate on debt | **~1.01%** ($33.6M ÷ $3,330M) | Convertible-driven, not bank debt |

**Rate-refinancing sensitivity:** if Sea had to term out its entire $3.33B stack at market (5Y UST 4.80% + ~250bp EM-tech spread ≈ 7.3%), annual interest would rise to ~$243M — about **10% of EBIT**. Rate risk is **immaterial** to solvency. The yield curve is upward-sloping and **not inverted** (2Y 4.65%, 10Y 4.99%, 30Y 5.37%, 2s10s +34bp), so the refinancing window is open, just not cheap.

---

## 2. Key Financial Risk Metrics

| Metric | FY2025 | FY2024 | FY2023 | FY2022 | Assessment |
|---|---|---|---|---|---|
| Revenue ($M) | 22,938.5 | 16,819.9 | 13,063.6 | 12,449.7 | +36.4% YoY, accelerating |
| Gross margin | 44.66% | 42.84% | 44.66% | 41.65% | Stable/expanding |
| Operating margin | **8.13%** | 3.94% | 1.72% | −11.95% | Improving sharply |
| EBITDA ($M) | 2,667.8 | 1,197.0 | 783.5 | (704.2) | |
| Net income ($M) | 1,578.1 | 444.3 | 150.7 | (1,651.4) | 3 straight years positive |
| **FCF ($M)** | **4,514.0** | 2,955.8 | 1,821.4 | **(2,032.0)** | Inflection complete |
| FCF margin | 19.68% | 17.57% | 13.94% | −16.3% | Rising 4 yrs |
| **FCF yield** | **7.99%** | — | — | — | Genuine cash generator |
| Debt/Equity | 0.26x | 0.49x | 0.67x | — | Deleveraging |
| Net debt/EBITDA | **(3.55x)** | (1.44x) | (2.11x) | — | Net cash |
| Interest coverage | 55.5x | 21.1x | 8.3x | n/m | 6.7x improvement in 2 yrs |
| Current ratio | 1.58x | 1.49x | 1.44x | — | Adequate, improving |
| Quick ratio | 1.57x | — | — | — | No inventory dependence |
| Cash ratio | 0.87x | — | — | — | $12.8B cash |
| Working capital | +$8,569M | +$5,562M | +$3,605M | — | Positive & growing |
| Cash / short-term debt | **7.5x** | 6.7x | 18.0x | — | No near-term pressure |
| **Altman Z-Score** | **1.53 (Distress)** | — | — | — | **⚠ Artifact — see below** |
| **Piotroski F-Score** | **8 / 9 (Strong)** | — | — | — | Only F7 (dilution) fails |
| Assets / liabilities | 1.76x | 1.60x | 1.55x | — | Thickening |

### Critical caveat on the Altman Z-Score (1.53, "Distress")

I regard the distress reading as a **model artifact, not a credit signal.** Two mechanical problems:

1. **x4 uses book equity**, not market cap. Book equity is $12.65B vs. $54.19B market cap. Substituting market cap (x4 = 3.241 instead of 0.756) lifts the Z-score to **~3.02 — just inside the safe zone**.
2. **x2 (retained earnings / assets) = −0.224** because Sea carries a **$6.58B accumulated deficit** from its 2017–2022 cash-burn era. That deficit is permanent and will depress the Z-score for years regardless of current profitability.

**Validation of the model bias:** I ran MercadoLibre (MELI) — a high-quality, consistently profitable operator — through the same model and got a Z of **1.351, also "Distress."** Any asset-light platform with historical losses lands in the distress zone. I therefore **discount the Z-score and weight the Piotroski F-Score (8/9) and FCF trajectory far more heavily.**

### Peer leverage context

| Company | D/E | Net debt/EBITDA | Int. coverage | Op. margin | Z-score | F-score |
|---|---|---|---|---|---|---|
| **Sea (SE)** | **0.26x** | **(3.55x) net cash** | **55.5x** | 8.13% | 1.53* | **8** |
| MercadoLibre (MELI) | 1.69x | 1.34x | 21.6x | 11.08% | 1.35* | 5 |
| Coupang (CPNG) | 1.00x | (1.40x) net cash | 5.5x | 1.37% | n/a | n/a |

**Sea has the strongest leverage profile in the peer set** — 6.5x less levered than MELI on D/E, with the highest coverage ratio and highest F-score.

---

## 3. Market Risk Profile

**Rating: HIGH**

| Metric | Value | Interpretation |
|---|---|---|
| Annualised volatility (756d) | **48.51%** | ~3.2x the S&P 500's typical ~15%; extreme |
| Beta vs SPY (756d) | **1.294** | Amplifies market moves 29% |
| Beta (FMP 5Y monthly) | **1.547** | Longer lookback shows *higher* sensitivity |
| **Max drawdown (3Y)** | **−60.22%** | A 60% peak-to-trough loss occurred within 3 years |
| Sharpe ratio (rf = 0%) | **0.304** | Poor risk-adjusted return — 0.30 of return per unit of 48.5% vol |
| Sortino ratio | **Not available** | *Data gap — no downside-deviation metric from tools* |

**Interpretation:** Sea delivers equity-market-adjacent upside but with **triple the volatility and a bet that has historically suffered 60% drawdowns.** A Sharpe of 0.30 on 48.5% vol means the return stream does not compensate for the risk taken — this is a high-beta, high-variance instrument, not a defensive compounder. The divergence between the 3Y beta (1.29) and 5Y beta (1.55) suggests vol has *moderated* but remains extreme.

**Implication for a portfolio:** at beta 1.29–1.55 and 48.5% vol, SE would consume roughly **3x the risk budget** of an average position. Position sizing must be materially smaller than a core holding, and tail-risk hedging (puts, or pairing against a short in a lower-beta EM consumer name) is warranted.

---

## 4. Downside Scenario Analysis

Base FY2025 operating structure ($M): Revenue 22,938.5 → Gross profit 10,243.7 (44.66%) → SG&A 7,222.6 → Other opex 784.9 → D&A 372.2 → **Operating income 1,864.0** → EBITDA 2,667.8.

**The critical structural finding: Sea's cost base is ~93% fixed relative to revenue at current margins.** SG&A ($7.22B) plus other opex ($785M) consumes 34.9% of revenue against a 44.66% gross margin — leaving only an **8.1-point operating buffer**. A relatively modest revenue decline therefore produces a violently disproportionate EBITDA decline.

| | **Base (FY25A)** | **Case 1: Mild −20%** | **Case 2: Hard −20%** | **Case 3: Severe −35% + credit shock** |
|---|---|---|---|---|
| Revenue | 22,938.5 | 18,350.8 | 18,350.8 | 14,910.0 |
| Gross margin | 44.66% | 44.66% (held) | 41.66% (−300bp) | 40.00% |
| Gross profit | 10,243.7 | 8,195.5 | 7,644.9 | 5,964.0 |
| SG&A | 7,222.6 | 6,644.8 (−8%) | 7,006.0 (−3%) | 6,000.0 (−17%) |
| Other opex | 784.9 | 784.9 | 784.9 | 785.0 |
| D&A | 372.2 | 372.2 | 372.2 | 372.0 |
| **Operating income** | **1,864.0** | **393.6** | **(518.2)** | **(1,193.0)** |
| **EBITDA** | **2,667.8** | **765.8** | **(146.0)** | **(821.0)** |
| EBITDA change | — | **−71%** | **−105%** | **−131%** |
| Extra fintech credit provision | — | — | — | **(413.0)** |
| Net income (20% tax) | 1,578.1 | ~$315 | ~$(415) | ~$(1,290) |
| Interest coverage (EBIT/int.) | 68.3x | 11.7x | **Nil** | **Nil** |
| Net cash position | +$9,459M | +$9,459M | +$9,459M | +$9,459M |
| FCF | 4,514.0 | ~$1,200M | ~$(200)M | ~$(1,600)M |

### The central conclusion: **liquidity is never the binding constraint; earnings volatility is.**

Even in Case 3 — a 35% cumulative revenue collapse compounded by a fintech credit shock — Sea retains **$9.46B of net cash** (or $3.05B on the narrowest definition). At a $(1.6)B annual burn, that is **~5.9 years of runway on broad cash, ~1.9 years on narrow cash.** No plausible operating scenario produces a liquidity event.

**However, the equity is highly exposed:**
- A mere **20% revenue decline cuts EBITDA by 71–105%.** The stock trades at ~20x EBITDA; if EBITDA goes to zero, the equity's support is asset value, not earnings.
- In Case 2, a 20% revenue decline with only a 300bp gross-margin slip and modestly sticky SG&A produces an **EBITDA-negative, covenant-relevant outcome** — a ~$54B market cap supported by essentially nothing on an earnings basis, and a plausible 50%+ drawdown (consistent with the observed −60% max drawdown).
- Case 3 wipes out ~$1.3B/year. Two years of that consumes $2.6B — survivable, but the equity would rerate toward book/net-cash value.

**Why the downside may be shallower than modelled:** SG&A at Sea is heavily *variable* (Shopee marketing, fulfillment, and incentives scale with GMV), so the −8%/−3% flex assumptions are deliberately conservative. Management demonstrated in 2022–2023 that it can cut to profitability fast — FCF went from **−$2.03B (2022) to +$4.51B (2025)** in three years, a $6.5B swing. That is the strongest single argument against a true distress outcome.

---

## 5. Overall Financial Risk Rating

# **MODERATE**

**Composition of the rating:**

| Risk dimension | Rating | Weight | Rationale |
|---|---|---|---|
| **Credit / solvency** | **LOW** | 30% | Net cash $9.46B, coverage 55x, D/E 0.26x, interest cost ~1%. Best-in-peer-set. |
| **Liquidity** | **LOW** | 25% | Current ratio 1.58x, cash/ST-debt 7.5x, $8.57B positive WC, multi-year runway. |
| **FCF sustainability** | **LOW–MODERATE** | 20% | 7.99% FCF yield, margin expanding 4 consecutive years. Quality caveats below. |
| **Market / equity risk** | **HIGH** | 25% | 48.5% vol, beta 1.29–1.55, −60% max DD, Sharpe 0.304. |

**The distinction that matters for the investment memo:** Sea is **not a credit risk — it is an equity-volatility risk.** The company will almost certainly survive any plausible downturn; the question is at what share price. Balance-sheet risk is genuinely low. Price risk is extreme.

---

## 6. Key Red Flags

1. **Operating leverage is thin and asymmetric.** An 8.1% operating margin is the entire buffer against a 45% gross margin. A 20% revenue decline reduces EBITDA by 71–105%. This is the single largest financial vulnerability and explains the 60% historical drawdown.

2. **$6.58B accumulated deficit — the company has never cumulatively earned money.** Equity of $12.65B is entirely paid-in capital. There is no retained-earnings cushion; the balance sheet is strong only because investors funded it, and this permanently distorts the Altman Z-score.

3. **Refinancing concentration: 51% of debt is short-term.** Short-term debt is $1,701M of $2,212M financial debt, consistent with the **$2.5B 0.25% convertible senior notes due 2026** identified in SEC filings. Covered 7.5x by cash, so not a solvency event — but it is a *dilution* event: diluted shares of 638.2M vs. basic 595.0M imply a **7.3% dilution overhang**, and this is the one Piotroski test Sea fails (F7, no dilution — shares rose from 575.0M to 595.0M, +3.5% YoY).

4. **SeaMoney's $8.26B loan book is the most underappreciated risk.** Net receivables grew **+37.7% YoY** to $8,259M — **28% of total assets** — now larger than the company's entire equity cushion in absolute terms and 2.5x its gross debt. This is a consumer credit book across Indonesia, Brazil, Thailand, and the Philippines with no disclosed vintage or delinquency data in my feed. In a genuine EM consumer downturn, credit losses here hit earnings *directly* and *simultaneously* with the e-commerce slowdown — precisely the correlation modelled in Case 3.

5. **Cash-flow quality is not fully reconciled — treat FCF with some caution.** Operating cash flow of $5,028M versus net income of $1,578M is a 3.19x gap. Net income + D&A + working capital changes only explains ~$3,055M, leaving **~$1,973M unexplained** by the standard reconciliation. Additionally, **stock-based compensation is reported as exactly $0 for FY2025**, versus $716M in FY2024 — almost certainly a data error, since the diluted share count rose. *Both are data gaps I cannot close with available tools.* The 7.99% FCF yield is directionally right but not fully verified.

6. **Geographic, FX, and regulatory concentration.** Revenue is concentrated in Indonesia, Vietnam, Thailand, Philippines, Taiwan, and Brazil. Currency depreciation, VAT/take-rate regulation of e-commerce marketplaces, and gaming-licence risk are unquantifiable from the available tools. No geographic revenue breakdown was retrievable. *Data gap flagged.*

7. **Piotroski's one failure is the forward-looking one.** The F-Score is a backward-looking 8/9 — driven by ROA improvement, accrual quality, and falling leverage. The single miss (share dilution) is the metric that persists into the future.

### Data Gaps — Explicitly Flagged
- **No public credit rating** located (issuer appears unrated)
- **Sortino ratio** not computable from tools
- **Debt maturity schedule by year** unavailable — only ST/LT split; FY2026 convert maturity inferred from a 2021 SEC filing, not confirmed against the latest 20-F
- **SBC for FY2025 reported as $0** — implausible, likely feed error (FY2024: $716M)
- **~$1.97B OCF reconciliation gap** unexplained
- **Geographic revenue split** and **SeaMoney delinquency/vintage data** unavailable
- Peer set from the sector tool returned mega-cap Consumer Cyclical names (AMZN, TSLA, HD, BABA); I substituted MELI and CPNG as the genuinely comparable EM/Asia e-commerce platforms. **Formal peer multiples were not available** from the tools.

---

## Bottom Line for the Memo

**Sea Limited is a financially sound company wrapped in a volatile stock.** Net cash of $9.46B, interest coverage above 55x, a 0.26x debt/equity ratio, a four-year FCF expansion from −$2.0B to +$4.5B, and an 8/9 Piotroski score make the *solvency* case close to airtight. The Altman Z-score's "Distress" label is a mechanical artifact of book-equity and accumulated-deficit inputs, and I explicitly reject it — a validation run on MercadoLibre produces the same false signal.

**The real risks are two.** First, an **8.1% operating margin against a 45% gross margin** means a 20% revenue decline cuts EBITDA by 71–105% — the equity has no earnings cushion, which is the mechanism behind the observed −60% drawdown. Second, the **$8.26B SeaMoney loan book (28% of assets, +38% YoY)** is a credit cycle Sea has not yet been tested through, and it is correlated with the e-commerce cycle rather than diversifying it.

**For sizing: this belongs in the portfolio as a high-beta, high-volatility equity position at reduced weight — not as a defensive holding** — with the balance sheet providing genuine downside protection against permanent capital loss but *not* against a 50%+ mark-to-market drawdown.

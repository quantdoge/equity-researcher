# Fin Risk Analyst

- Symbol: CHRW
- Elapsed: 61.1s

---
I have what I need. Two decisive, non-obvious facts change this from a routine "investment-grade broker" story: an **unaccrued $711M judgment** and a **$5.8B debt-funded acquisition**. Writing the assessment now.

---

# C.H. Robinson Worldwide (CHRW) — Financial Risk Assessment

**Price $127.60 | Market cap $14.73B | Sector: Industrials / Integrated Freight & Logistics | Latest data: Q3 2026 (9/30/26)**

## 1. Credit Risk Assessment

**Rating: Investment Grade — S&P BBB+ (upgraded Aug 2025, stable), Moody's stable.** But the IG rating is *backward-looking*. Two off-balance-sheet and forward events mean the rating no longer describes the risk.

| Metric (FY2025 audited) | Value | Read |
|---|---|---|
| Debt / Equity | 0.88x | Moderate |
| Net Debt / EBITDA | 1.65x | **Low — strong** |
| Interest coverage (EBIT/int.) | 12.5x (tool 12.6x) | **Very strong** |
| Debt / Assets | 0.32x | Moderate |
| Altman Z-Score | 5.98 (Safe) | Safe, but flattered |
| Piotroski F-Score | 7/9 (Moderate) | Good |

The FY2025 picture is genuinely solid: leverage of 1.65x and coverage of 12.5x are comfortable IG metrics. **But the latest balance sheet has already deteriorated:** at 9/30/26 total debt is $2,152M vs $1,629M at YE25 (+32%), equity fell to $1,579M (buybacks), lifting D/E to **1.36x**. On trailing-twelve-month EBITDA of ~$947M, net debt/EBITDA is **~2.07x**, up from 1.65x in nine months.

Caveats on the Z-score: x4 uses *book* equity (indicative only), and x5 (asset turnover 3.21x) is structurally inflated by the low-margin brokerage model — a $16B revenue base on $5B of assets. For asset-light brokers, Z-score systematically overstates safety. Piotroski's two misses (F7 no dilution, F9 asset turnover) are consistent with buyback-funded EPS growth rather than operational improvement.

## 2. Key Financial Risk Metrics

| Risk Dimension | Metric | Value | Assessment |
|---|---|---|---|
| **Leverage** | Net debt/EBITDA | 1.65x → **2.07x** (TTM) | Deteriorating |
| | Debt/Equity | 0.88x → **1.36x** | Rising |
| | Tangible equity | **$279M** | ⚠️ Very thin |
| **Coverage** | EBIT/Interest | 12.5x | Strong |
| **Liquidity** | Current ratio | 1.53 → **1.34** (Q3'26) | Adequate, weakening |
| | Quick ratio | 1.53 | No inventory — clean |
| | Cash | $161M → $193M | Thin vs $2.15B debt |
| | Cash ratio | 0.09 | Low |
| | Revolver | $1.0B undrawn, matures **11/19/2027** | Key backstop |
| **Solvency** | Altman Z | 5.98 | Safe (flattered) |
| | Piotroski F | 7/9 | Moderate |
| **FCF** | FCF (FY25) | $894.9M | Strong |
| | FCF yield | 5.8% (tool) / **6.1%** at $14.73B | Healthy |
| | FCF after dividends+buybacks | $238.8M | Payout = 73% of FCF |

**⚠️ Tangible equity of just $279M** (goodwill + intangibles $1,566M = 85% of book equity, 31% of assets) against $1.6B of debt is the structural soft spot. Book equity is largely accounting goodwill, not loss-absorbing capital.

## 3. Market Risk Profile

| Metric | Value | Comment |
|---|---|---|
| Annualised volatility (756d) | **39.5%** | High for logistics; well above market |
| Beta vs SPY (computed) | **0.65** | Defensive on this window |
| Beta (vendor profile) | 0.95 | ⚠️ **Data conflict** — I report both |
| Max drawdown (3y) | **38.8%** | Severe |
| Sharpe (0% rf) | 0.50 | At a realistic ~4% rf, ≈0.1 — **no excess return for the risk** |
| Sortino | Not available | **Data gap** |

The beta conflict matters: computed 0.65 vs vendor 0.95. The 756-day window is dominated by idiosyncratic events rather than market sensitivity, which mechanically depresses measured beta. **For downside stress-testing, the 0.95 vendor beta is the more prudent assumption.** Event risk is proven, not theoretical: the RXO announcement took the stock down **10.85% in one session and another 4.72% the next day**.

## 4. Downside Scenario Analysis — Revenue −20%

Base FY2025: revenue $16,233M, net revenue $1,359M (8.37%), SG&A $564M, D&A $103M, EBIT $786M, interest $63M. I model SG&A as ~55% variable (brokerage comp is volume-linked) and net revenue margin flat.

| Line | Base FY25 | Revenue −20% | Change |
|---|---|---|---|
| Revenue | $16,233M | $12,986M | −20% |
| Net revenue | $1,359M | $1,087M | −20% |
| SG&A | $564M | $502M | −11% |
| D&A | $103M | $103M | — |
| **EBIT** | **$786M** | **$482M** | **−39%** |
| Interest | $63M | $63M | — |
| **Coverage** | **12.5x** | **7.6x** | Still IG-comfortable |
| EBITDA | $888M | $585M | −34% |
| **Net debt/EBITDA** | **1.65x** | **2.51x** | Manageable |
| FCF (est.) | $895M | ~$395M | −56% |
| Dividend cover | 3.0x | **1.3x** | Buybacks → $0 |

**Conclusion: the operating business survives a 20% revenue shock comfortably.** Operating leverage is real (−20% revenue → −39% EBIT) but the balance sheet absorbs it. *The downside risk is not the core business — it is the two balance-sheet events below.*

**Combined stress (revenue −20% + $711M judgment paid):** cash of $193M is wiped out, requiring a revolver draw of roughly $520M+ against a $1.0B facility maturing **Nov 2027**. Liquidity survives, but the 2027 refinancing becomes a genuine cliff — and it must be re-cut anyway to fund RXO.

## 5. Overall Financial Risk Rating: **MODERATE — trending HIGH**

The *reported* financials merit "Low-Moderate." The *off-balance-sheet and announced* facts merit "High." I weight the latter, because they are near-certain to crystallise within 12–18 months.

## 6. Key Red Flags

1. **🔴 $604M jury verdict (Montgomery v. Caribe Transport II), upheld by the Texas judge, now >$711M with interest, reportedly approaching $1B.** Against $1,579M of book equity and only **$279M of tangible equity**, this single item could erase roughly half of book equity. Critically, the Q2 2026 10-Q discloses only an **"immaterial accrual"** and states no reasonable estimate of excess loss can be made — i.e. **the judgment is essentially unprovided for**. Net income stayed positive ($187M in Q2'26, $198M in Q3'26), confirming no charge was taken. This is my single largest concern and a precedent risk for the whole brokerage model ("retained control" liability).
2. **🔴 $5.8B RXO acquisition (announced 10/5/26), cash-and-stock, closing H1 2027.** Funded partly with new debt. Management targets 1.75x–2.25x net debt/EBITDA, but my arithmetic says reaching even 2.25x on ~$5.3B pro forma net debt would require ~$2.35B of EBITDA — roughly **2.5x CHRW's current ~$947M**. Either the cash component is smaller than the headline implies, or the target rests on a non-comparable EBITDA definition. **Unresolved — treat the stated leverage target with scepticism until the proxy/financing terms are filed.** S&P has publicly taken a "more cautious" stance than the sell-side.
3. **🟠 Thin tangible equity ($279M)** — 85% of book equity is goodwill/intangibles. Little buffer for either shock above.
4. **🟠 Refinancing cliff:** $1.0B revolver matures **11/19/2027**; ~$600M of senior notes outstanding. Both need addressing amid deal financing.
5. **🟠 Cash generation increasingly shareholder-directed:** 73% of FY25 FCF went to dividends+buybacks; a $355M buyback in 2025 while debt rose 32% into 2026 is the same policy S&P criticised in 2023.
6. **🟠 Working-capital drag:** receivables $3,547M with DSO ~57 days; WC consumed $470M across Q1–Q3 2026, which is why FCF fell to $107M in Q3'26 despite $198M of net income.
7. **🟡 Elevated volatility (39.5% vol, 38.8% max drawdown, Sharpe ≈0.1 at realistic rf).**

## Data Gaps & Conflicts (explicitly flagged)
- **Quarterly dataset is internally inconsistent** and I have discounted it: Q2/Q3 2026 gross margins of ~15% vs FY2025's 8.4%; SG&A of $132M in Q1'26 vs $482M in Q2'26; interest expense reported as **$0** in Q2/Q3 2026. Conclusions rest on audited annuals plus the Q3'26 balance sheet.
- **Goodwill and retained earnings report as 0** in the 9/30/26 balance sheet — vendor data gap, not economic reality.
- **S&P/Moody's and SEC pages returned HTTP 403**; rating and judgment details come from secondary sources (FreightWaves, S&P headline, 10-Q search excerpts) rather than primary filings.
- **Debt maturity schedule by year not obtained** — only the revolver (Nov 2027) and ~$600M notes are confirmed.
- **No peer comparison, CDS spread, or Sortino ratio** available from the toolset.
- One search result (S&P "outlook negative") was dated **June 2023**, not current — I verified and excluded it; the current stance is BBB+/stable from the Aug 2025 upgrade, with caution expressed on the RXO deal.

**Bottom line:** CHRW is a high-quality, IG-rated, cash-generative franchise whose core operations would comfortably survive a 20% revenue decline. The investment risk is not operating leverage — it is a **>$711M unaccrued litigation judgment colliding with a $5.8B debt-funded acquisition**, against tangible equity of only $279M. Risk is **Moderate today, High on a 12–18 month view**; the key monitoring triggers are the appeal outcome, and the RXO financing terms and pro forma leverage disclosure.

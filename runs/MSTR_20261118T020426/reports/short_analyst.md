# Short Analyst

- Symbol: MSTR
- Elapsed: 64.5s

---
# MSTR (Strategy Inc.) — Forensic Short-Seller Analysis
*Data as of ~Nov 18, 2026. Price $96.50; FD market cap ~$43.9B; 850,849 BTC.*

## Framing: what this company actually is

Strategy Inc. is **not a software company** — it is a Bitcoin holding vehicle with a small, decaying legacy analytics business attached. FY2025 balance sheet: total assets $61.64B, of which **$58.85B (95.5%) is "goodwill and intangibles"** (i.e. Bitcoin carried at fair value under ASU 2023-08), $2.30B cash, $75.8M of PP&E. Revenue is $477M — **0.8% of assets**. Asset turnover (Altman x5) is 0.0077.

**This matters enormously for forensics: every standard manipulation screen is structurally blind here.** The screening output below is reported for completeness, but I flag it as a false negative — the risk in MSTR is not accounting manipulation, it is capital-structure mechanics and valuation.

## 1. Earnings Quality Assessment: **LOW** (but not "Fraudulent Risk")

| Metric | Result | Read |
|---|---|---|
| Earnings Quality Score | **10/100** | Genuinely informative |
| Cash conversion (OCF/NI) | **1.7%** | Reported earnings carry no cash |
| FCF conversion | **2.9%** | Operating business is cash-negative |
| FY2025 OCF | **−$67.2M** | Negative for 2 straight years |
| FY2025 FCF | **−$112.5M** | Negative for 4 straight years |

**The core finding: reported net income is a pure mark-to-market derivative of one asset and is economically meaningless.** Under fair-value accounting:
- FY2025: net loss **−$3.85B** (impairment/marks)
- 9M 2026: net loss **−$1.23B**
- Q3 2026 alone: net income **+$19.1–19.5B**, diluted EPS **+$44.75**, driven by a **$20.91B Bitcoin fair-value gain**

A company with a $44B market cap "earned" $44.75/share in a quarter and lost money over nine months. Any analyst anchoring on EPS or P/E is being misled. Note that FY2025 shareholders' equity *rose* $32.8B (from $18.2B to $51.0B) while the company *lost* $3.85B — that is capital-markets issuance plus an accounting transition, not value creation.

## 2. Key Red Flags Found

1. **BTC-per-share fell while BTC holdings rose 32.4%.** Holdings went from ~640,232 BTC (Q3'25) to 850,849 BTC (+33%), but shares went from ~300–310M to ~433M basic / ~455M fully diluted. On my reconstruction: **gross BTC/share fell from ~2.07–2.13 to ~1.87–1.97 (−5% to −11%)**. The "accretive ATM" thesis is empirically false over the trailing year. (Share counts are reconstructed, not filed — treat as an estimate, but the direction is robust.)
2. **Senior claims now consume 36% of the pile.** Debt + preferred = **$19.7B notional**, equivalent to **306,023 of the 850,849 BTC**. Only **544,826 BTC** actually back the common. The "gross mNAV" of 0.80x and the "CEBE mNAV" of 1.26x differ by exactly this capital-stack effect. Preferred-funded BTC purchases lift the gross line and leave net exposure flat — "phantom growth."
3. **Preferred dividend obligation ~$588M/yr, up from $0 in 2024.** FY2025 cash dividends paid jumped to $381M from zero; the annualised run-rate is now ~$588M. Plus ~$65M interest. Against FY2025 OCF of −$67M. The dividend is funded by *new securities issuance*, not cash flow.
4. **STRC's 12.00% coupon resets monthly** to keep the perpetual near par. This is functionally a variable-rate liability that reprices *against* the company as confidence erodes — a reflexive cost spiral. Dividends were also moved from quarterly to daily/semi-monthly: optically yield-maximising, disclosure-minimising.
5. **Gross margin contracting sharply:** 77.8% (2023) → 72.1% (2024) → **68.7% (2025)**. ~450bp/yr of pricing power loss, coincident with the "AI analytics" pivot.
6. **Revenue decelerating to negative.** +11.9% (Q1'26) → +6.9% (Q2'26) → **−2.5% (Q3'26)**. Three-year revenue: $499M → $477M (−4.4% cumulative).
7. **Receivables outgrowing revenue:** AR +13.6% vs revenue +3.0% (FY2025). DSO 135 days (2023) → 143 → **157 days**. Weak collection quality on top of a declining book.
8. **95% of assets in one mark-to-market position; ~zero tangible productive assets.**
9. **Six-ticker capital structure** (MSTR, STRK, STRF, STRD, STRC, STRE) plus converts. Complexity of this order reliably obscures the true senior-claim waterfall from retail holders — a legitimate governance flag.

## 3. Beneish M-Score and Accruals Analysis

**Beneish M-Score = −2.522 → "Low risk." Verdict: NOT APPLICABLE / false negative.**

Components: DSRI 1.103 (receivables outpacing revenue — real), GMI 1.049 (margin deteriorating — real), AQI 0.97, SGI 1.03, DEPI 0.717, SGAI 0.958, **LVGI 0.584**, **TATA −0.0613**.

The "clean" score is manufactured by two indices: LVGI collapses because equity ballooned from the fair-value transition, and TATA is negative because impairment losses are *conservative* accruals. Beneish models operating-company income manipulation; it cannot see a company whose income statement is a BTC price feed. **Do not take comfort from this score.**

**Accruals ratio = −0.0613 ("ok")** — same artifact. FY2023, the last "normal" year, printed a **+0.0874 warning** signal. The honest accrual read is not the ratio but the raw fact: **four consecutive years of negative free cash flow** (−$287M, −$1,893M, −$56M, −$112M).

**Altman Z = 2.79 ("Grey")** — x4 uses $51B book equity marked at BTC. This is a BTC-price derivative mislabelled as a credit model. x3 (EBIT/TA) = −0.089. **Piotroski F = 3 ("Weak")**, and two of those three points (F5 leverage, F6 equity change) are accounting artifacts, not improvement. The genuine operating F-score is ~1.

## 4. Competitive Threat Assessment: **Severe (structural, not competitive)**

The threat is not a rival software vendor. It is that **the product — levered Bitcoin exposure — is now available far cheaper elsewhere.**
- Spot BTC ETFs at ~25bp, zero premium, zero leverage, zero governance risk.
- The company's own gross mNAV has collapsed from **~3.0x (Nov 2024: ~$

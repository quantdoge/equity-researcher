# Short Analyst

- Symbol: IT
- Elapsed: 63.9s

---
# Gartner, Inc. (NYSE: IT) — Forensic Short-Seller Analysis

**Price used:** $207.19 (company profile quote; market cap $13.08B, ~63.1M shares). **Data caveat:** the daily price feed I pulled terminated 2026-02-20 at $153.73, while the fundamental data extends through Q3 FY2026 (filed 2026-11-03). I anchor on the profile quote but flag the vintage mismatch. I did **not** run Altman Z — negative book equity makes it mechanically meaningless here, so I'd rather omit it than mislead.

---

## 1. Earnings Quality Assessment: **HIGH**

| Metric | FY2025 | FY2024 | FY2023 | FY2022 |
|---|---|---|---|---|
| Accruals ratio | **-0.069** | -0.027 | -0.035 | -0.040 |
| Cash conversion (OCF/NI) | 1.77x | 1.18x | 1.31x | 1.36x |
| FCF conversion (FCF/NI) | 1.61x | 1.10x | 1.19x | 1.23x |
| Beneish M-Score | **-2.88** | — | — | — |

Negative accruals in every year of the sample and cash conversion far above 1.0x is the signature of a genuinely cash-generative subscription business. Cash keeps arriving ahead of recognised revenue via deferred revenue — the opposite of the accrual-heavy profiles I look for. The composite "earnings quality score" of 45/100 from the built-in model **contradicts its own components** (1.77x cash conversion, -0.069 accruals); I treat the 45 as a model artifact and weight the raw ratios.

**The one income-statement distortion worth knowing:** FY2024 net income of $1,254M sits above FY2024 operating income of $1,156M. Q3 FY2024 alone shows net income of $415M against operating income of $246M. That is a one-off tax benefit, not operating prowess. Normalising FY2024 to a ~24% tax rate gives ~$13.5 EPS, not the reported $16.12. Symmetrically, FY2025's $9.65 EPS was cratered by the Q3 FY2025 charge (operating income collapsed to $86M; net income $35M). **The reported 40% EPS decline from 2024 to 2025 is largely an accounting bridge between two distorted years — it is not a bear data point, and I won't pretend it is.**

---

## 2. Key Red Flags Found

1. **Revenue is now shrinking — three consecutive quarters.** YoY: Q4'24 +8.1% → Q1'25 +4.2% → Q2'25 +5.7% → Q3'25 +2.7% → Q4'25 +2.2% → **Q1'26 -1.5% → Q2'26 -0.6% → Q3'26 -1.3%.** This is the first sustained top-line contraction in Gartner's public history outside 2009.
2. **Contract value growth decelerating toward zero** — the leading indicator, reported at ~2.5% (down from ~5%, previously ~7%), with management indicating a 4% exit pace is unlikely. Revenue follows CV with a 1–2 quarter lag; CV of 2.5% is inconsistent with the +3.7% FY2027 revenue growth consensus requires.
3. **Negative operating leverage in SG&A.** SG&A/revenue rose from 45.5% (FY2021) → 45.7% (FY2023) → 46.0% (FY2024) → **47.2% (FY2025)**. The 2026 margin recovery came from gross margin (Q1'26 71.6% vs Q1'25 69.0%), not from SG&A discipline.
4. **Capital destruction via buybacks.** FY2021–Q3'26 repurchases total **~$7.25B** (~103% of five-year FCF). Share count fell from 85.0M to 63.9M — roughly **$333/share average cost versus $207 today**, implying ~$2.7B of value destroyed (~21% of current market cap). EPS "growth" in 2026 is denominator-driven while revenue falls.
5. **Shareholders' equity is now negative** (-$34.7M at Q3'26) and **tangible equity is ~-$3.05B**. Goodwill and intangibles of $3.01B are 42% of assets and ~87x book equity, carried with no impairment despite a shrinking top line.
6. **Serial guidance disappointment.** Two single-day collapses: **-28% on 2025-08-05** (4.5M shares) and **-21% on 2026-02-03** (7.3M shares). A pattern of management over-promising revenue trajectories is itself a red flag.
7. **Insider filings:** 13 Form 4s clustered on 2026-10-05 plus a steady stream through October. I could not verify transaction direction from the metadata available — most likely RSU vesting/tax withholding, so I explicitly do **not** count this as an insider-selling signal.

**Not found (and I looked):** receivables growing faster than revenue (**-0.69% vs +3.67% in FY2025 — no channel stuffing**); rising inventory days (no inventory); aggressive capitalisation (D&A/revenue stable ~3.1%); revenue recognised ahead of collections. On every classic manipulation tell, Gartner is clean.

---

## 3. Beneish & Accruals

M-Score **-2.877**, well below the -2.22 soft threshold — "Low risk." The sub-indices are almost all benign: DSRI 0.958 (receivables *lagging* sales), GMI 1.001 (gross margin flat), AQI 0.988, SGI 1.037, DEPI 0.903, TATA -0.069. The only mildly adverse index is **LVGI 1.142** (leverage increase) — consistent with the debt-funded buyback, not with earnings manipulation.

**Conclusion: no accounting fraud case exists here.** A forensics-driven short cannot be built on these numbers.

---

## 4. Competitive Threat Assessment

**The bear case is real but is a business-model question, not an accounting one.**

- Gartner's Research product monetises *asymmetric information* — benchmark data, Magic Quadrant vendor rankings, and analyst access. Generative AI attacks precisely the "read a report / synthesise a market view" layer of that value stack at near-zero marginal cost.
- Selling, general & administrative costs at 47% of revenue, on a 20,000-person headcount, is exactly the fixed-cost-intensive distribution model an AI-native entrant can undercut.
- The offsetting bull argument is stronger than bears admit: the cash-generating asset is not the written report, it is (a) the proprietary benchmark dataset that AI models cannot synthesise, (b) the Magic Quadrant's role as a social/ procurement ritual in enterprise vendor selection, and (c) high switching costs with a ~80%+ revenue renewal base. Client-count erosion has been attributed by management to **small tech vendors** — a cyclical, venture-funding-driven cohort, not the enterprise core.
- Gross margin *expanded* YoY in all three FY2026 quarters. If pricing power were collapsing, that is the first place it would show. **It isn't showing yet.**

---

## 5. Management & Governance

Eugene Hall's tenure has been operationally excellent (revenue $4.7B → $6.5B, EBIT margin ~20%) but the capital-allocation record is poor: buying back 100%+ of FCF at an average ~$333 against a current $207 is textbook value-destructive financial engineering, and it converted a fortress balance sheet into negative book equity. No related-party, auditor-change, or disclosure-opacity issues surfaced. Language has been promotional relative to delivery on CV growth — a credibility discount is warranted, not a fraud allegation.

---

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, but it is a value-trap thesis, and it is late.**

The credible bear case: Gartner is a decaying annuity. Contract value growth of 2.5% and falling, revenue down ~1% YoY for three quarters, and EPS growth manufactured from cost cuts and a shrinking share count. Consensus FY2026 EBITDA of $1.639B implies a **25.5% margin — near the all-time peak of 27.5% (itself flattered) — on a declining revenue base**, and FY2027 requires +3.7% revenue growth that CV of 2.5% cannot deliver. If CV growth crosses zero, deferred revenue unwinds and cash flow falls *faster* than revenue. On a bear case of -4% revenue and 20% EBITDA margin, EV/EBITDA re-rates from ~9x to ~11x on lower EBITDA — another 25–35% down.

**The other side, and it is strong:** the stock is already down ~63% from its ~$552 peak (Nov 2024) and ~72% at the Feb-2026 trough of $153.73. At $207 it trades at **~13.9x FY2026E EPS ($14.93), ~8.8x EV/EBITDA**, with a **~10% FCF yield** and ~$1.3B of annual free cash flow. That is deep-value territory for a 25%-margin, high-renewal franchise. Accounting is spotless (Beneish -2.88, negative accruals, 1.6x FCF conversion), there is no fraud catalyst, ~$400M/quarter of buyback still bids the stock, and margin execution is currently *beating* expectations. Negative tangible equity is a buyback artifact, not distress — interest coverage is ~9x and debt is modest against $1.6B of cash.

Notably, a short here has no informational edge: every input above is public, priced, and heavily discussed. The two crashes already happened.

---

## 7. Contrarian Rating: **NO EDGE — Reject Short Thesis at $207**

This is

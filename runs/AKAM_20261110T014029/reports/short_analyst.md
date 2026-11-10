# Short Analyst

- Symbol: AKAM
- Elapsed: 66.7s

---
# AKAM — Forensic Short-Seller Analysis

**Data note:** My price feed ends 2026-02-25 ($100.04); the company profile field shows a stale $80.29; the most recent externally observable quote is **~$122 (25-Sep-2026)**, 24% below the May-2026 high of $161.14. I use ~$122 for valuation and flag the gap. Financials are current through Q3 2026 (filed 06-Nov-2026).

---

## 1. Earnings Quality Assessment: **LOW** (but *not* Fraudulent)

| Metric | Reading | Verdict |
|---|---|---|
| Beneish M-Score | **−2.80** (threshold −1.78) | Low manipulation risk |
| Accruals ratio | **−0.093** (NI < OCF) | Genuinely high quality |
| Cash conversion (OCF/NI) | 3.36x | Inflated by D&A, but real |
| Composite quality score | 60/100 | Mediocre |
| Piotroski F-Score | **5** | Deteriorating |
| Altman Z (Dec-25) | **1.556 — Distress** | Confirmed |

**The fraud thesis fails and I will not pretend otherwise.** Cash exceeds accounting earnings every single year; there is no channel-stuffing signature in the annual series; no auditor turnover; no related-party self-dealing visible. This is not an Enron.

**But the earnings quality is poor for a different and more important reason: the reported numbers no longer describe the business.**

- **Non-GAAP is 2.2x GAAP.** Q1 2026: GAAP net income $106m vs non-GAAP $239m. Q2 2026: GAAP EPS $0.52 vs non-GAAP $1.59. The entire "beat and raise" cadence — and the entire sell-side EPS estimate of $6.67 for 2026 — is built on a number that excludes **$459m of 2025 stock comp (10.9% of revenue, rising to 13.3% in Q2 2026)** plus acquisition amortisation.
- **SBC is now 102% of GAAP net income.** In 2025 Akamai paid employees $459m in stock to generate $452m of GAAP profit. Management is compensated in a currency excluded from the metric management is judged on.
- **True owner earnings are ~$240m, not $699m.** FCF ($699m) is flattered because SBC is a non-cash add-back. FCF minus SBC = $240m in 2025, $441m in 2024, $657m in 2021 — owner earnings have **fallen 63% in four years** while revenue rose 22%.

**Rating: Low.** Cash-backed, but structurally overstated by compensation that is real.

---

## 2. Key Red Flags

1. **Gross margin has collapsed 830bps in four years: 63.3% (2021) → 54.7% (2025) → 55.0% (Q3 2026).** COGS grew **+50.2%** (2021→2025) against revenue **+21.6%**. This is the unmistakable signature of CDN commoditisation plus a mix shift into low-margin compute. Pricing power is gone.

2. **GAAP operating margin halved: 22.6% (2021) → 14.9% (2025) → 7.3% (Q2 2026).** Q2 2026 GAAP operating income fell **47% YoY**. Adjusted EBITDA fell 6%. This is not a growth company; it is a melting ice cube wearing a growth company's multiple.

3. **The core is shrinking.** Q2 2026 segment detail: Security $604m (+10%), Cloud Infrastructure $99m (+39%), **Delivery & other $396m (−6% YoY)**. Delivery is still **36% of revenue** and in structural decline against Cloudflare/AWS CloudFront/Google.

4. **Free cash flow has gone negative.** Q3 2026 FCF = **−$172m** (OCF $433m − capex $605m). Nine-month 2026 FCF = **+$49m** versus $699m for all of 2025. Full-year 2026 FCF likely **−$1.0bn to −$1.1bn**.

5. **Capex is being detonated.** 2026 capex guidance **$2.445–2.645bn** (vs $820m in 2025); 2027 guide **$3.462bn+**. That is **57% and 66% of revenue** respectively, versus 19.5% in 2025. Akamai has become a capital-intensive infrastructure builder.

6. **Debt is exploding to fund it.** Total debt: $6.91bn (Dec-25) → $9.45bn (Sep-26), **+37% in nine months**; net debt $5.98bn → **$8.30bn**. Net debt/equity **1.61x**; net debt/(EBITDA − SBC) **9.4x**. Recalculated Altman Z at Q3 2026 ≈ **1.17 — deep distress**.

7. **Receivables running hot in 2026 (the annual screen missed this).** AR $794m (Dec-25) → $958m (Sep-26) = **+20.8%** against revenue +5.8%. DSO 67 → 78 days. ~$130m of cash flow is being propped up by slower collections. Not fraud, but a working-capital warning.

8. **Buybacks were badly timed and then abandoned.** $800m repurchased in 2025 (exceeding $699m of FCF, partly debt-funded), $616m in H1 2026 — including into the $161 May-2026 high — then **$0 in Q3 2026** when cash tightened. Equity rose ~$400m in Q3 2026 despite negative FCF and zero buybacks, implying fresh issuance.

9. **Goodwill + intangibles $3.94bn = 77% of equity.** Growth has been bought, not built, and the amortisation is excluded from non-GAAP.

---

## 3. Beneish & Accruals Analysis

| Index | Value | Read |
|---|---|---|
| DSRI | 1.034 | Slight receivables build — watch |
| GMI | 1.085 | Gross margin deterioration |
| AQI | 1.030 | Asset quality worsening (capex-heavy) |
| SGI | 1.054 | Modest growth |
| DEPI | 1.131 | **Depreciation slowing relative to capex — capitalised cost is front-running the P&L** |
| SGAI | 1.060 | Opex growing faster than sales |
| LVGI | 1.070 | Leverage rising |
| TATA | −0.093 | Clean accruals |

M-Score **−2.80** is comfortably below the −2.22 soft warning. **Conclusion: no manipulation.** But note DEPI at 1.131 — the D&A charge is lagging a 3x capex increase. When $2.5bn+ of 2026–27 capex begins depreciating (7-year life → ~$360m/yr of incremental depreciation), GAAP earnings get hit again and the non-GAAP/GAAP gap widens further.

---

## 4. Competitive Threat Assessment: **SEVERE**

- **Cloudflare** is winning the developer/edge narrative and the security bundle at a fraction of Akamai's price; **AWS CloudFront and Google Cloud CDN** treat delivery as a loss-leader for compute. Delivery is a commodity and Akamai's −6% decline is the proof.
- **The moat is being attacked from both ends**: down-market by Cloudflare's bundled pricing, up-market by hyperscalers owning the AI workloads.
- **Security (+10%) is the one genuine moat** — sticky, high-switching-cost, embedded in customer infrastructure. But it has decelerated from 20%+ growth and is now carrying the entire P&L.
- **The Anthropic deal is not a moat; it is a capital commitment.** See below.

---

## 5. Management & Governance Red Flags

1. **The Anthropic contract (Sept 2026) is the centrepiece of the bear case.** $11.6bn over 7 years (~$1.66bn/yr), expandable to ~$20bn, for dedicated **CPU cloud capacity** — i.e. **hosting, not software**. Akamai guided a **$1.7bn capex increase in 2026 alone** with "no impact to 2026 revenue guidance." Do the arithmetic: ~$3.5–4bn of build for ~$1.66bn/yr of low-margin hosting revenue. At a generous 40% gross margin that is ~$660m of gross profit against ~$570m/yr of depreciation — **roughly break-even at the operating line before incremental opex.** A mid-teens gross return on invested capital, financed with debt at 5–6%.
2. **They paid for the contract with equity.** Akamai granted Anthropic **warrants for up to ~5% of common stock** (~$880m of value at $122). Consideration payable to a customer should economically reduce revenue; watch whether any charge flows through the P&L. This is the one genuine accounting-forensics question in the file.
3. **Catastrophic counterparty concentration.** A single, cash-consuming AI lab now represents the entirety of the growth narrative and a large share of future capex. Anthropic is dependent on continued external funding and has hyperscaler relationships (Google TPUs, AWS) that could displace Akamai. If Anthropic re-routes or re-prices, Akamai owns **stranded, purpose-built, depreciating capex** against $9.4bn of debt.
4. **Insider filings:** 25 Form 4s in 2026, densely clustered — **eight separate filings on 2026-05-14**, plus clusters in March, June and September 2026, bracketing the $161 May high. *Caveat: my feed returned filing metadata only, not transaction direction, so I cannot confirm these are sales rather than vesting/grants. Flagged as suggestive, not proven.*
5. **Promotional framing vs delivery:** the market re-rated the stock **+15% in one session** on an $11.6bn headline that carries negative free cash flow, +37% debt, 5% dilution and zero 2026 revenue benefit. That is narrative outrunning arithmetic — the classic setup.

---

## 6. Short Thesis Summary

**The bear case is credible and, unusually, already visible in the reported cash flows.**

Akamai was an asset-light, 63%-gross-margin, 23%-operating-margin CDN. It is becoming a leveraged, 55%-gross-margin, 7%-operating-margin **AI datacenter landlord** with a single customer, at precisely the moment its legacy Delivery business shrinks 6% a year. The transition is being funded with debt (net debt $8.3bn, +39% in nine months), warrants (5% dilution) and the abandonment of buybacks.

**The numbers that matter:**
- 2026E FCF: **−$1.1bn**; 2027E FCF: **−$1.7bn** (capex $3.46bn+ vs OCF ~$1.8bn)
- Cumulative 2026–27 funding gap ~**$2.8bn**, on top of $8.3bn net debt → net debt likely $11–12bn by end-2027 vs equity ~$5.5bn
- EV ~**$25.9bn** = **37x** 2025 FCF and **~108x** owner earnings (FCF − SBC)
- Altman Z ≈ **1.17**; GAAP EPS falling (−27% in Q2 2026); SBC 13% of revenue and rising

**The market is capitalising $11.6bn of low-margin hosting revenue as if it were software, ignoring that it requires $3.5–4bn of debt-funded capex, earns a mid-teens gross return, and comes with 5% of the equity attached.**

**Where I could be wrong — the bull case is not weak:**
- **No fraud.** Beneish −2.80, negative accruals, cash conversion >3x. Nothing here is fake; it's a capital-allocation and business-model problem, which markets can tolerate far longer than fraud.
- **CIS +39% and Security +10%** are real franchises; if CIS scales toward the ~$2.2bn/yr the Anthropic deal implies, the mix shift could eventually re-accelerate growth to double digits.
- **The $20bn expansion option** and the possibility of further hyperscaler/neocloud contracts could turn Akamai into a genuine AI-infrastructure franchise — the market is already voting that way (+43% YTD as of Sept 2026).
- **Liquidity is adequate** ($3.5bn cash) — this is not an imminent solvency event.
- **The stock is 24% off its high and extremely squeezy** — 25 moves >5% in twelve months. A short here can be directionally right and still be carried out on a stretcher.

---

## 7. Contrarian Rating: **SHORT**

High conviction on the fundamentals, deliberately **not** "Strong Short."

The deterioration is no longer a forecast — it is in the Q3 2026 cash flow statement (FCF −$172m), the Q2 2026 GAAP P&L (operating income −47%), the segment table (Delivery −6%), and the balance sheet (debt +37% in nine months, Altman Z ~1.17). The Anthropic contract converts a slow-motion margin erosion story into a leveraged, single-counterparty capital cycle bet, and the equity has been re-rated *up* on it.

I stop short of Strong Short for three honest reasons: **there is no accounting fraud to detonate** (Beneish and accruals are clean, so there is no catalyst date), the **balance sheet still has $3.5bn of cash**, and the **Anthropic narrative can generate violent squeezes** in a stock that has moved >5% twenty-five times in a year.

**What would make me cover:** capex guidance cut or pushed onto a third party (sale-leaseback/JV), a second and third anchor tenant signed at similar economics, Anthropic funding secured long-term with prepayments, Delivery returning to growth, or SBC falling below 8% of revenue. **What would make this a Strong Short:** any sign of Anthropic deferring capacity, a debt raise at distressed terms, or a further step-down in 2027 revenue guidance.

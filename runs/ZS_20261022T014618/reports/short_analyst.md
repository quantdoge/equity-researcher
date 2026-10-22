# Short Analyst

- Symbol: ZS
- Elapsed: 520.0s

---
# ZS — Forensic Short-Seller Analysis
**Zscaler, Inc. | Technology / Software – Infrastructure | Market cap ≈ $37.7B | Price ≈ $231 (profile) / $199.42 close 30-Sep-26**

---

## 1. Earnings Quality Assessment: **LOW** (structural, not fraudulent)

The single most important finding is that **Zscaler's reported free cash flow is almost entirely funded by stock-based compensation.** FY2026 FCF was $852.4M; SBC was $821.9M. Adjusted for SBC, economic FCF was **$30.4M — a 0.9% margin** on $3.35B of revenue. That is the forensic core of this name.

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Revenue ($M) | 1,617 | 2,168 | 2,673 | 3,353 |
| Gross margin | 77.6% | 77.9% | 76.9% | 76.8% |
| GAAP net income ($M) | −202.3 | −57.7 | −41.5 | −63.2 |
| Operating cash flow ($M) | 462.3 | 779.8 | 972.5 | 1,129.7 |
| Capex ($M) | 128.7 | 194.9 | 245.8 | 277.3 |
| FCF ($M) | 333.6 | 585.0 | 726.7 | 852.4 |
| **SBC ($M)** | **444.8** | **527.7** | **661.4** | **821.9** |
| **SBC % revenue** | **27.5%** | **24.3%** | **24.7%** | **24.5%** |
| **FCF less SBC ($M)** | **−111.2** | **57.3** | **65.3** | **30.4** |

Over four years Zscaler reported **$2.50B of cumulative FCF** and expensed **$2.46B of cumulative SBC**. Essentially 100% of the "cash generation" story has been recycled into employee compensation. Diluted shares rose from 144.9M (FY23) to 160.2M (FY26) — **+10.6%, or ~3.4%/year**, so per-share growth is ~22%, not the 25.4% headline.

**On the quality score of 0/100:** this is mechanically driven by a negative net-income denominator (cash conversion ratio of −17.9 is meaningless when NI < 0). I do not treat it as evidence of manipulation — see §3. The genuine quality problem is not accruals; it is compensation.

---

## 2. Key Red Flags Found

1. **Organic growth is decelerating and is being masked by M&A.** Reported FY26 revenue +25.4%, but ARR of $3.525B was up 25% — and only **21% excluding Red Canary's ~$127M contribution**. Organic growth went 34% (FY24) → 23% (FY25) → **~21% (FY26)**. The company's FY27 ARR guide of $4.40–4.43B again implies ~25% only because of acquired revenue. The "25% grower" label is increasingly a roll-up story.
2. **Deferred revenue / billings proxy is lagging revenue badly.** Total liabilities (dominated by deferred revenue) grew **+14.0%** ($4,620.6M → $5,268.5M) against revenue **+25.4%**. For a growing subscription business, deferred revenue should grow *at or ahead of* revenue. Change in working capital was only **+$53M** on $679M of revenue growth. This corroborates the May-2026 "billings decline" disclosure that triggered a −32% single-day drop.
3. **FY2025 receivables red flag (since normalized).** AR grew **+34.7%** vs revenue +23.3% in FY25 — the classic channel-stuffing/billings-timing signature. FY26 corrected (AR +15.8% vs revenue +25.4%). DSO: 124 days (FY24) → 135 (FY25) → **125 (FY26)**. Elevated but consistent with annual enterprise billing; directionally now improving. **Verdict: one-year anomaly, not a persistent pattern.**
4. **Gross margin compression.** 77.9% → 76.8% over two years (−106bps). Cost of revenue grew +28.9% in FY25 vs revenue +23.3% — materially faster. FY26 roughly in line (+25.8% vs +25.4%). Modest but consistent erosion, not the "software margin" narrative.
5. **Goodwill ballooned from $465M to $1,432M (+$967M)** — the Red Canary MDR acquisition (reported around $675M deal value). Asset Quality Index in the Beneish model jumped to **1.779**, one of the few elevated inputs. Capital allocation is shifting from organic build to buying growth — a classic late-cycle signal for a maturing platform.
6. **D&A up +58%** ($121M → $192M) versus revenue +25%, driven by acquisition amortisation and the data-centre build (ZEN nodes). Zscaler is more capital-intensive than the "asset-light SaaS" narrative implies (capex 8.3% of revenue).
7. **Heavy Form 4 activity** — 25 filings Mar–Oct 2026, clustered on vesting dates (7 filings on 17-Sep-26, 3 on 20-Oct-26). Consistent with routine 10b5-1/RSU liquidation. **Honest gap: I could not verify net buy/sell direction from the filing metadata; no open-market insider buying is evident.**
8. **Altman Z-Score 0.813 = "Distress."** I view this as a **mechanical artifact**: negative retained earnings (−$1.25B) and modest book equity depress the score. With ~$3.47B cash/investments against ~$1.86B total debt (net cash ~$1.6B) and $1.13B OCF, there is no solvency risk. Flag it only as evidence of cumulative GAAP losses.

---

## 3. Beneish M-Score & Accruals Analysis

**Beneish M-Score: −2.698 → "Low risk" (threshold −1.78).** This is a clean result and I will not pretend otherwise.

| Index | Value | Read |
|---|---|---|
| DSRI | 0.923 | Receivables growing *slower* than sales — good |
| GMI | 1.001 | Gross margin essentially flat |
| AQI | 1.779 | **Elevated** — acquisition-driven asset growth |
| SGI | 1.254 | Strong sales growth |
| DEPI | 0.905 | Depreciation rate rising |
| SGAI | 0.952 | SG&A leverage improving |
| LVGI | 0.931 | Leverage down |
| TATA | −0.152 | **Negative accruals — conservative** |

**Accruals ratio: −0.152** (FY26), −0.158, −0.178, −0.184 across the series. Cash earnings exceed accounting earnings in every year. Signal: "ok." The mechanical reason is negative net income, but the economic read is genuinely favourable — **there is no evidence of aggressive revenue recognition or accrual inflation.** This is not an accounting-fraud short.

**The forensic conclusion:** Zscaler's accounting is *honest*. Its problem is *economic*, not criminal — a business whose GAAP losses and huge SBC mean reported profitability is an illusion, while cash flow looks robust only because the compensation bill is settled in newly printed shares.

---

## 4. Competitive Threat Assessment

Zscaler's moat — a single-tenant, in-line cloud proxy architecture (ZIA/ZPA) — was genuinely differentiated. It is now being attacked from four directions:

- **Platform bundlers:** Palo Alto Networks (Prisma Access) is pursuing "platformisation" with aggressive bundling/free-trial tactics; Microsoft Defender/Entra is bundled into E5 seats already owned by the enterprise. Bundling is the classic commoditisation vector for point SSE vendors.
- **Direct SSE competitors:** Netskope (now public), Broadcom/Symantec, Cisco, Forcepoint, Cloudflare. The zero-trust network access category has 10+ credible vendors.
- **Endpoint-adjacent expansion:** CrowdStrike and SentinelOne moving from endpoint into network/identity — Zscaler's partnership strategy is a hedge, not a moat.
- **TAM maturation signal:** buying into **MDR (Red Canary)** is an admission that the core SSE market is maturing. Vendors that start acquiring adjacent categories to sustain growth are usually past the steepest part of the S-curve.

Evidence of erosion in the numbers: organic growth ~21%, gross margin −106bps, growth now M&A-assisted. **Verdict: moat narrowing, not broken.** Switching costs in security are real (multi-year contracts, architecture embedded in network path), which caps the downside — this is why the gross margin is still 77%.

---

## 5. Management Red Flags

- **Guidance credibility:** the May-2026 Q3 FY26 print saw billings slow and FY27 outlook disappoint, sending the stock down 32% in one session ($184.60 → $126.41 on 27-May-26). That is the "promotional language vs delivery" gap in action.
- **Reaffirmed FY27 ARR guide of $4.40–4.43B** at investor day — implies ~25% growth, but again relies on acquired revenue. Management is choosing to guide on an ARR metric that flatters the organic trend.
- **SBC discipline:** no evidence of intent to reduce SBC below ~24% of revenue. Four years of 24–27% SBC with no downward trajectory is a governance choice, and it transfers ~3.4%/yr of shareholder value to employees.
- **Capital allocation:** ~$675M+ acquisition with ~$967M of new goodwill, immediately after a growth scare. Acquisition-driven growth plus negative GAAP earnings is a combination that historically precedes write-downs.
- **No related-party or auditor-change red flags found.** No 10-K text was retrievable through the filing tool (only Form 4 metadata available) — an honest gap in this analysis.

---

## 6. Short Thesis Summary — is there a credible bear case?

**Yes — a credible quality-of-earnings and valuation case, but NOT a fraud case.**

The bear thesis in one line: *Zscaler is an 11x-sales, 25%-headline-growth security vendor whose organic growth is ~21%, whose gross margin is quietly eroding, whose "25% FCF margin" is a fiction created by adding back 24.5%-of-revenue stock compensation, and whose economic free cash flow is roughly zero — leaving investors paying ~1,240x true earnings.*

Supporting math:
- EV/FY26 revenue ≈ **11.3x** (EV ≈ $38.6B)
- P/FCF = **44x**; **P/SBC-adjusted FCF ≈ 1,240x**
- Non-GAAP EPS (adding back SBC ≈ $5.13/share) implies a ~45–50x forward P/E — expensive but not extreme for 25% growth
- To earn 10%/yr from here, market cap must reach ~$55B by FY2030; on the FY2030 consensus net income of $1.19B, that is **~46x 2030 earnings** — the multiple must persist for four years while organic growth decelerates
- Cumulative 4-year SBC ($2.46B) ≈ cumulative FCF ($2.50B); shareholders have funded their own dilution

### The other side — the bull case is genuinely strong
I will not overstate this short. Zscaler has:
- Best-in-class zero-trust architecture,

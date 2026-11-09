# Short Analyst

- Symbol: COHR
- Elapsed: 103.6s

---
## COHR — Forensic Short-Seller Analysis

**Data caveats up front (material):** The FY2026 *annual* balance-sheet row reports `ppe_net` of $21,286M against total assets of $18,299M — impossible. The quarterly series shows $2,999M, so the annual line is corrupted. This poisons the Beneish DEPI (9.5) and AQI (−0.89) inputs. Similarly, the Q1 FY27 cash-flow row was mis-scaled 1000x in the feed; I verified the true figures from the company's release (operating activities **used $92.7M**). Conclusions below rest on the sane data.

---

## 1. Earnings Quality Assessment: **LOW** (but not Fraudulent Risk)

| Metric | FY2023 | FY2024 | FY2025 | FY2026 |
|---|---|---|---|---|
| Revenue ($M) | 5,160 | 4,708 | 5,810 | 7,118 |
| Gross margin | 34.6% | 30.9% | 35.4% | **37.5%** |
| Net income ($M) | −259 | −156 | 49 | **805** |
| Operating CF ($M) | 634 | 546 | 634 | **80** |
| Capex ($M) | 436 | 347 | 441 | **1,110** |
| Free cash flow ($M) | 198 | 199 | 193 | **−1,031** |
| Cash conversion (OCF/NI) | 2.4x | neg | 12.8x | **0.10x** |

Composite earnings-quality score: **22/100**. FCF conversion **−128%**. In Q1 FY27 the deterioration accelerated: net income $384.7M, operating cash flow **−$92.7M**, capex $775.5M (vs $103.9M a year earlier), **FCF ≈ −$868M in a single quarter**.

This is the single best fact in the bear case: at ~$385M of quarterly GAAP profit, the company burns ~$870M of cash per quarter.

## 2. Key Red Flags Found

1. **Working capital is eating all the profit.** FY2026 change in working capital **−$1,102M** on revenue of $7,118M. Inventory alone absorbed ~$1,143M. Q1 FY27 added another **−$644M** — the drag is *widening*, not normalising.
2. **Inventory up 105% YoY vs revenue +49.9%.** Inventory $3,341M (Sep-26) vs $1,633M (Sep-25). Inventory days: 137.6 (FY23) → 139.8 (FY25) → **211.7 (FY26)** → ~211 (Q1 FY27). At a 39% gross margin, a 20% write-down would be ~$670M pre-tax — roughly two quarters of current GAAP operating income.
3. **Capex 5.3x depreciation.** Q1 FY27 capex $775M vs D&A $147M; annualising ~$3.1B of capex against ~$590M of D&A. The depreciation cliff is *ahead*, not behind — a mechanical gross-margin headwind arriving FY27–FY28 regardless of demand.
4. **~30% dilution in five quarters.** Diluted weighted shares 155.5M (Q4 FY25) → 195.4M (FY26) → **202.0M (Q1 FY27)**. Equity rose $3.18B from Jun-25 to Sep-26 against cumulative net income of ~$1.19B, implying ~$1.8–1.9B of net share issuance. Basic 196.2M vs diluted 202.0M signals a convertible overhang. Piotroski F7 (no dilution) = 0. **Per-share value creation is materially worse than headline growth.**
5. **Guidance re-engineered on "pro forma" basis.** On 14 Oct 2026 the company agreed to sell its Materials Processing Tools division to Bystronic, then guided FY27 to ">60% pro forma revenue growth." Divesting a business mechanically raises the growth rate on a smaller denominator. "First $3B quarter by FY-end, first $4B quarter in FY2028, >45% non-GAAP GM before end-CY2028" is a promotional stack of ever-dated promises.
6. **Non-GAAP gap of ~730bps.** Q1 FY27 GAAP operating margin 15.9% vs non-GAAP 23.2% — ~$173M/quarter (~$690M/yr) of add-backs, ~30% of GAAP operating income. Note GAAP operating margin **fell** YoY (16.4% → 15.9%) even as non-GAAP rose 368bps.
7. **Intangibles stretched.** Goodwill + intangibles $7,264M = 36% of assets, 62% of equity. The FY2026 10-K discloses a *quantitative* impairment test of the "Coherent" trade name — management itself flagged the carrying value as close to the line.
8. **Insider selling, no buying.** 14 open-market sales totalling ~$9.95M over six months, clustered in the days immediately after the 7 Aug 2026 peak ($379). A director sold 2,200 shares at $268 on 2 Sep 2026 **outside a 10b5-1 plan**. Dollar size is modest for a $38B cap — a yellow flag, not red.

**Where the red flags are notably *absent*:** receivables. Annual AR grew 31.7% vs revenue 22.5% (flag triggered), but this has fully normalised — at Q1 FY27 receivables grew **49.6% vs revenue 49.9%**, with DSO flat at ~62 days year-over-year. There is no channel-stuffing signature. Gross margin is *expanding* (30.9% → 37.5% → 39.1%), the opposite of pricing-power erosion.

## 3. Beneish M-Score & Accruals Analysis

- **M-Score: −1.803** — inside the "possible manipulator" band (−2.22 to −1.78), barely.
- **But the score is not usable as evidence.** DEPI of 9.515 implies the depreciation rate collapsed ~90% (actual: D&A/revenue ≈ 7.3% vs 9.5% prior year) and AQI of −0.887 is off an impossible PP&E figure. Strip out the two corrupted indices and the *reliable* components are benign: **GMI 0.944** (gross margin index below 1.0 = margins improving — anti-manipulation), **DSRI 1.075** (receivables days +7.5%, modest, and now reversed), **LVGI 0.895** (leverage falling), **SGI 1.225**, **TATA 0.0396**.
- **Accruals ratio: +0.0396** — positive and a ~+0.079 swing from FY25's −0.039, but still *below* the 0.05 warning threshold. On a balance-sheet basis this is high-normal for a company ramping capacity 50%+, not manipulation.
- **Piotroski F-Score: 6/9** (moderate). Failures: accruals quality, no dilution, asset turnover.

**Verdict: earnings are low-quality, but they are not fabricated.** The cash gap is *fully explained by disclosed line items* — inventory and capex — not by revenue recognition, capitalised opex, or related-party fiction. A Chanos-style "the cash isn't there" short requires the cash to be *missing*; here it is *visibly spent*.

## 4. Competitive Threat Assessment

- **Real, and structural, but slow-moving.** NVIDIA's Spectrum-X co-packaged optics is now in full production, claiming 4x fewer lasers and 5x lower power than pluggables. CPO is the long-term cannibalisation risk for pluggable transceiver volume. However, the CPO market is ~$165M in 2026 — immaterial against Coherent's $7.1B base. TrendForce expects transceivers *and* CPO to both grow through the decade.
- **Coherent's position is upstream of the contested layer.** Its moat is InP epitaxy, EMLs, and owned fabs — not module assembly, where Chinese vendors (Innolight, Eoptolink, Zhongji) dominate and compete hardest. That is defensible. Transceivers were ~30% of FY25 revenue and are the commoditisation-exposed piece.
- **Margin evidence contradicts the erosion thesis.** Four consecutive quarters of gross-margin expansion (36.6% → 36.9% → 37.7% → 38.5% → 39.1%). Datacenter & Comms revenue +79% YoY to $1,951.7M while Industrial *declined* — mix is improving, not degrading.

**Competitive score: moat intact near-term, under genuine 2028+ threat.** This is not a 2026 short catalyst.

## 5. Management Red Flags

| Flag | Assessment |
|---|---|
| Insider selling at scale | ~$9.95M / 14 sales / 0 buys, clustered post-peak; one non-10b5-1 director sale. **Mild concern.** |
| Related-party transactions | None identified in filings reviewed. |
| Auditor changes | None identified. Auditor signed off on controls; CEO/CFO certification clean. |
| Promotional language vs delivery | **Yes.** "Pro forma" growth guidance post-divestiture, multi-year dated targets (45% GM "before CY2028 ends"), 730bps GAAP/non-GAAP gap. Aggressive but common in this cohort. |
| Equity issuance | **Yes — the strongest governance criticism.** ~$1.8–1.9B raised in five quarters while guiding ~$3B annual capex. Management is funding the growth story with shareholders' capital at these prices, then selling on the same tape. |

## 6. Short Thesis Summary — Is there a credible bear case?

**A credible *quality* bear case, yes. A credible *fraud* case, no.**

**The bear case that holds:**
> COHR is an AI-optics capex supercycle play consuming ~$870M of cash per quarter at peak narrative. It funds a $3B/yr capex program with negative FCF and ~30% dilution, and its 211 days of inventory is 50% above its own historical norm. The depreciation cliff from that capex arrives in FY27–FY28 and compresses margins mechanically. GAAP operating margin already fell YoY in the best growth quarter in company history. At 3.8x FY27E EV/sales with negative free cash flow, any hyperscaler order digestion produces violent de-rating — the stock fell 20% on 14 Aug 2025 and ~19% on 27 Jan 2025 for exactly this reason.

**The bull case is stronger on the fundamentals, and I must say so:**
Revenue accelerated to +49.9% YoY (from 17.3% three quarters earlier) with gross margin up 254bps — that is the *opposite* of a decelerating, channel-stuffed story. Datacenter & Comms +79%. Management guided Q2 to $2.55–2.75B (a further +8–16% sequentially) and FY27 pro forma growth >60%. Receivables days are flat, so the revenue is being collected. The Altman Z-Score of 1.902 looks alarming only because the tool uses *book* equity; recomputed with market capitalisation (X4 = 4.42) the Z-Score is **~3.8 — the safe zone**. Net debt is $2.79B, leverage is falling (LVGI 0.895), and the industrial divestiture removes a low-margin drag.

**And critically — the short has already paid.** Price is $192.81 vs a 7 Aug 2026 peak of $379.13: **−49%**. It fell 12% on the Q1 FY27 print alone. At ~19.7x FY27E EPS of $9.81 and ~12.8x FY28E EPS of $15.01, this is no longer a crowded-multiple short. Adding fresh short exposure here means betting against a 50–80% grower with expanding margins at a mid-teens forward multiple, to capture a *further* leg of a de-rating that is already two-thirds done.

## 7. Contrarian Rating: **NO EDGE** — Reject the Short Thesis

I cannot certify this as a forensic short. Cash conversion of 10% is genuinely poor and the dilution is shareholder-hostile, but every dollar of the cash gap is traceable to disclosed inventory build and disclosed capex — the signature of a capacity ramp mis-timed against an order book, not of accounting fraud. There is no receivables divergence, no margin collapse, no auditor or related-party event, no restatement, and no solvency issue.

**Positioning:**
- **Do not short for accounting reasons.** The manipulation hypothesis fails on the evidence. GMI of 0.944 and flat DSO are explicit disconfirmations.
- **Do not own it either.** Accruals quality, 211 inventory days, a 5x capex/depreciation ratio and ~30% dilution mean reported EPS materially overstates per-share economics. If the AI datacom order book pauses for even two quarters, the inventory write-down plus depreciation ramp produces an EPS air-pocket that consensus FY28E of $15.01 does not contemplate.
- **The only honest trade is tactical and cyclical, not forensic:** a valuation/beta short on hyperscaler capex digestion, sized small, and only on a rally back toward $260–300. That is a macro bet, not the forensic bet I was asked to underwrite.

**Single most valuable thing to monitor next:** whether Q2 FY27 operating cash flow turns positive as the working-capital build annualises. If inventory passes $4B while revenue growth decelerates below 40%, the bear case upgrades from "quality concern" to **Short**. If OCF flips positive and inventory days compress toward 150, the bull case is vindicated and the stock is cheap. That one line item decides it.

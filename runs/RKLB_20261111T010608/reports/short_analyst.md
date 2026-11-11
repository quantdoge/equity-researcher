# Short Analyst

- Symbol: RKLB
- Elapsed: 95.2s

---
## RKLB — Forensic Short-Seller Analysis
**As of Nov 10, 2026 — $62.71 | Market cap $37.5B | EV ~$33.0B**

---

## 1. Earnings Quality Assessment
### Rating: **MEDIUM** (no manipulation evidence — but low-quality in the "cash" sense)

The critical distinction up front: **there is no accounting fraud here.** The red flags in RKLB are *economic* (valuation, dilution, capital intensity, execution), not *forensic*. I want to be explicit about that because a forensic lens on this name produces a clean bill of health on the fraud question and a damning verdict on the valuation question.

| Metric | FY25 | Signal |
|---|---|---|
| Accruals ratio (NI–OCF)/assets | **-0.0141** | Negative accruals = conservative. Good. |
| Cash conversion (OCF/NI) | **0.835** | Below 100%, weak in absolute terms |
| FCF conversion | 1.624 | Artifact of negative NI — ignore |
| Receivables growth vs revenue | Rev +38.0% vs AR +10.3% | **No channel stuffing** |
| Inventory days | 146.5 (from 135.8) | Mildly adverse |
| Composite quality score | **27/100** | Poor — driven by FCF, not accruals |

The 27/100 composite is the honest number: it is not measuring accounting tricks, it is measuring the fact that this business consumes cash. TTM free cash flow is **-$191.8M**, and TTM operating cash flow of -$191.8M... turned structurally only in Q3'26, when OCF printed **+$7.2M** — and even that was aided by $18.3M of stock comp add-back and a +$16.1M working capital release. Strip those and operating cash was still negative.

**Working capital is a real tell on growth quality.** Change in WC was **-$51.8M (Q1'26), -$84.0M (Q2'26), -$44.8M (Q4'25)** before reversing +$16.1M in Q3'26. A $84M working capital drain quarter on $234M of revenue is what scaling a hardware business looks like — not a fraud signal, but a structural cash tax on growth that bulls systematically underwrite.

---

## 2. Key Red Flags Found

**RED FLAG #1 — Neutron is now 3+ years late, with a second distinct manufacturing failure.** Announced 2021, targeted first flight 2024. First flight is now **2027**. The Oct 15, 2026 slip was caused by *voids between carbon fiber layers* in the first-stage propellant domes — traced to a design change made after a **tank ruptured during a hydrostatic pressure test in January 2026**, itself blamed on a third-party manual layup at a "critical join." Beck's own framing: Neutron's first stage is "the largest pressurized structure ever made out of carbon composite," requiring novel out-of-autoclave cure cycles. This is not a schedule slip; it is a **process-industrialization problem on the single asset that justifies the enterprise value.**

**RED FLAG #2 — Gross margin compressing sequentially despite 73% growth.**
Q1'26 **38.2%** → Q2'26 **36.1%** → Q3'26 **33.6%** GAAP. That is -460bp in two quarters in a period of record revenue. Management framed it as mix (space systems outgrowing launch) and beat its own 29–31% guide — but a company with genuine pricing power does not lose 460bp of margin at the moment of peak demand. Also note the GAAP-to-non-GAAP gap of **480bp** (33.6% vs 38.4%): the "beat" is partly a stock-compensation exclusion. SBC runs **$84M TTM, 9.5% of revenue.**

**RED FLAG #3 — Chronic dilution, and the latest raise is underwater.** Shares outstanding: 481.8M (FY23) → 505.6M (Q1'25) → 629.7M (Q2'26) → **652.3M (Q3'26)**. That is **+35% in under three years (~11%/yr)** — and Piotroski F-Score component F7 confirms "dilution." The company sold **$1.94B of stock (~29.3M shares at ~$66)** to fund Iridium, against a **$3B ATM authorization** still live. The stock now trades at **$62.71 — below the raise price**, down **-58% from the $150.23 May 27, 2026 peak**. Shareholders have absorbed both multiple compression and supply.

**RED FLAG #4 — Inventory growing faster than revenue.** Inventory **$280.9M, +88% YoY** vs revenue +72.7%. Annual inventory days 146.5 vs 135.8 prior year vs 203.8 in 2023. Not yet a demand-weakness signal at this growth rate, but the direction is wrong and worth watching through 2027.

**RED FLAG #5 — Goodwill/intangibles up ~5x in five quarters** ($124.9M Q2'25 → $609.3M Q3'26) via Geost, Mynaric and now Iridium. Serial M&A during a period of negative FCF and unproven integration capability. Beneish AQI of **1.192** captures this asset-quality deterioration.

---

## 3. Beneish M-Score & Accruals Analysis

**M-Score: -2.193** → "MODERATE RISK — possible manipulator" (softer threshold -2.22, hard threshold -1.78). It sits right on the softer line.

**I judge this flag to be a false positive, and I want to show the work:**

| Index | Value | Interpretation |
|---|---|---|
| DSRI | **0.799** | Receivables growing *slower* than sales — **anti-manipulation** |
| GMI | **0.773** | Gross margin *improving* YoY — **anti-manipulation** |
| AQI | 1.192 | Asset quality deteriorating (acquisitions/PPE) — mild adverse |
| **SGI** | **1.380** | **High sales growth — the dominant driver of the negative score** |
| DEPI | 1.208 | D&A rate declining — mild capitalization watch |
| SGAI | **0.911** | SG&A falling as % of sales — **anti-manipulation** |
| LVGI | **0.383** | Leverage collapsing — **anti-manipulation** |
| TATA | **-0.0141** | Negative total accruals — **anti-manipulation** |

Six of eight indices point away from manipulation. The score is being dragged down by SGI — a **known false positive in hypergrowth companies**, where high sales growth mechanically inflates the score. Combined with negative accruals in all four years (FY22 -0.030, FY23 -0.089, FY24 -0.119, FY25 -0.014) and receivables *lagging* revenue, there is **no earnings-manipulation case to make.** Revenue recognition is clean.

**Altman Z: 1.613 ("Distress")** — I explicitly discount this. It is computed on *book* equity, and the company holds $4.6B of cash against $120M of debt. X4 of 2.857 understates a market equity of $37.5B. Pre-Iridium, solvency risk is nil. **Post-Iridium it is a different conversation** (see below).

---

## 4. Competitive Threat Assessment

**The moat is real but narrow, and it is being purchased rather than built.**

- **Electron** is the dominant Western dedicated small-launch vehicle. Genuine franchise, genuine switching costs in national-security workflows.
- **Neutron** is the entire medium-lift thesis: the only credible Western alternative to Falcon 9. That scarcity value is real — but *scarcity value that has not flown*. Every quarter Neutron slips, SpaceX's Falcon 9 rideshare pricing and Starship cadence further commoditize the exact medium-lift market Neutron is being built for.
- **The Iridium deal ($8.0B EV, $54/share, $27 cash) is the tell.** Rocket Lab is paying ~16x EBITDA for a mature, low-growth satellite operator ($871.7M revenue, $495M operating EBITDA, 57% margin in 2025) — a business whose handheld/consumer franchise faces direct structural threat from **Starlink Direct-to-Cell**. This reads far more like a CEO buying revenue diversification to defend a multiple than a CEO with a durable launch moat. It also imports a capital-intensive constellation refresh cycle (Iridium NEXT cost ~$3B) on top of Neutron's funding needs.
- Gross margin contraction is the classic signature of **pricing power loss** — and it is occurring now.

---

## 5. Management & Governance Red Flags

- **Insider selling:** 25 Form 4 filings since May 28, 2026, including a **cluster of 12 filings between June 1–18, 2026** (immediately around the May peak at ~$150 and the capital raise) and **6 filings on Aug 26, 2026**. Programmatic 10b5-1 is the charitable read; the uncharitable read is that the June cluster landed within days of the all-time high. **Notably: zero insider purchases during the -58% drawdown.** That is the opposite of conviction.
- **Promotional cadence vs delivery:** Neutron has now missed every publicly stated first-flight date since 2021 (2024 → 2025 → 2026 → 2027). Guidance credibility is impaired independent of the underlying engineering.
- **Capital allocation:** raising $1.94B of equity at ~$66 while the stock had already fallen from $150, with a $3B ATM still authorized, is shareholder-value-destructive timing at exactly the moment insiders were selling.
- **Mitigating:** no auditor changes, no restatements, no related-party red flags surfaced, founder-CEO with large retained equity stake. Governance is unconventional and promotional, not fraudulent.

---

## 6. Short Thesis Summary

**The bear case is credible but it is a *multiple-and-duration* case, not a fraud case.**

1. **Valuation leaves no room for error.** $37.5B cap on $881.9M TTM revenue = **42.5x TTM**, ~32x FY26E (~$1.16B), **~27.5x FY27E** ($1.364B consensus), **~20.5x FY28E** ($1.832B). Even on analyst numbers **three years out**, you are paying 20x sales and ~330x FY28 net income of $113M — for a company that has never posted a GAAP profit and has burned $192M of FCF in the last twelve months. Pro forma for Iridium, EV/EBITDA is roughly **110–120x**.
2. **Neutron is a binary event with a poor prior.** Two distinct composite-manufacturing failures in ten months. Industry base rate for first launches of new orbital rockets is failure-prone. A first-flight failure from 42x sales could compress the multiple by half.
3. **Iridium converts a fortress balance sheet into a leveraged, slower-growth, capital-hungry conglomerate** precisely as its core consumer franchise faces Starlink D2C.
4. **Dilution is a permanent, compounding tax** — 11%/yr, with a live $3B ATM.

**The other side — and it is strong, so I'll state it plainly:** revenue growth is *accelerating*, not decelerating: **32% → 36% → 48% → 36% → 63% → 62% → 73% YoY**. **Backlog is $3.57B, +137% YoY — 4.0x TTM revenue.** Q3'26 beat on revenue *and* gross margin, Q4 guided to $270–290M with GM *up* to 34–36%. Operating cash flow turned positive for the first time. There is $4.6B of cash and almost no debt. This is a genuinely scarce Western defense-space prime with Electron, Neutron optionality, and national-security tailwinds. **A momentum investor looking at backlog and the acceleration series has the better near-term argument,** and the stock has already fallen 58% from its peak — meaningfully de-risking the multiple.

---

## 7. Contrarian Rating

### **SHORT** — conviction moderate, *not* Strong Short

**Rationale:** As a forensic short, this fails — the books are clean (negative accruals, no receivables divergence, Beneish flag driven by benign SGI). As a **valuation short**, it succeeds: 20x FY28E revenue with unproven medium-lift execution, 11%/yr dilution, and a transformative acquisition that turns a net-cash story into a leveraged one while buying a business facing direct-to-cell disruption.

**Sizing and structure guidance:**
- Do **not** short this as an accounting/quality fraud — there is nothing there, and the $4.6B cash pile plus $3.57B backlog makes a naked short dangerous.
- The asymmetric expression is **event-driven around Neutron's first launch** (2027): buy downside convexity rather than carry a naked short into a backlog-driven melt-up.
- The real confirmation signal to watch is **gross margin at Q4'26/Q1'27** — if GAAP GM breaks below 33% while growth stays >60%, the pricing-power thesis is confirmed and this escalates toward Strong Short.
- **Kill the short thesis if:** Neutron reaches the pad and flies successfully, or backlog converts to operating cash flow above $100M/quarter. Either event invalidates the duration argument, and the momentum case wins.

**Honest bottom line:** I would not be short RKLB today at $62.71. The forensic evidence is exculpatory, and the fundamental momentum is real. I would be *structurally underweight* and wait to short strength into the Neutron launch window — where a binary, verifiable, pre-identified catalyst gives the bear case the convexity it currently lacks.

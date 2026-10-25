# Value Researcher

- Symbol: FROG
- Elapsed: 158.3s

---
# JFrog Ltd. (FROG) — Value Investment Analysis
*Price: $84.31 (Oct 16, 2026 close) | Market cap ~$10.3B | Net cash ~$0.75B | EV ~$9.5B*

**Data caveats up front:** The `calculate_intrinsic_value_dcf` tool mis-parsed WACC/TGR (it discounted at 1,000%), so I built the DCF by hand. `get_sector_peers` returned semiconductor mega-caps, which are useless as comparables for a DevOps platform; peer multiples below are therefore benchmarked qualitatively against high-growth infrastructure software, and I flag that gap honestly.

---

## 1. Business Quality Assessment — Moat: **Narrow**

JFrog is the de facto system of record for software binaries: Artifactory stores and versions every artifact, Xray/Curation scan them, Distribution ships them, and the newer AI Catalog / Agent Guard / MCP Registry extend the same control plane to AI models and agent primitives. Once a Fortune 2000's build pipelines, retention policies and release governance are wired into Artifactory, ripping it out is a multi-quarter engineering project. That is a real **switching-cost** moat, reinforced by a **universal-format** advantage (one repository for npm, Docker, PyPI, Maven, Helm, models) that point solutions like AWS CodeArtifact or Docker Hub don't replicate well.

Evidence the moat exists: 77–78% gross margin sustained for five years; 27% trailing FCF margin; enterprise logo expansion; cloud revenue $87.5M in Q2'26 (+53% YoY, 53% of total).

Evidence the moat is **not widening**: gross margin has *drifted down* from 79.8% (2021) to 76.8% (2025) — hosting/AI compute COGS are eating some of the mix shift, i.e. pricing power is good but not expanding. Competition is well-capitalized (GitHub/Microsoft, GitLab, Sonatype, Cloudsmith, hyperscaler-native registries). And decisively: **the company has never earned a GAAP operating profit in six years as a public company.**

| Moat test | Result |
|---|---|
| ROIC > WACC consistently? | **No** on GAAP (ROIC −9.9% in FY25). Only ~10–35% on non-GAAP depending on whether cumulative SBC (~$600M) is treated as invested capital |
| Margin stability | Gross margin stable-to-declining; GAAP op margin improving (−33% → −8%) |
| Pricing power | Moderate; universal-format lock-in, but no evidence of margin expansion |

---

## 2. Financial Quality Score: **6 / 10**

| Metric | FY23 | FY24 | FY25 | TTM (Q2'26) |
|---|---|---|---|---|
| Revenue ($M) | 349.9 | 428.5 | 531.8 | 600.0 |
| Growth | +24.9% | +22.5% | +24.1% | +25% (Q2 +28.7%) |
| Gross margin | 78.0% | 77.1% | 76.8% | 77.9% |
| GAAP op margin | −21.5% | −20.8% | −16.9% | −8% |
| Non-GAAP op margin | ~6% | ~12% | ~17% | ~18% (FY26 guide 18.1%) |
| FCF ($M) | 72.2 | 107.8 | 142.3 | 169.7 |
| FCF margin | 20.6% | 25.2% | 26.8% | 28.3% |
| SBC ($M) | 95.2 | 131.1 | 156.7 | 161.0 |
| **FCF − SBC ($M)** | **−23.0** | **−23.3** | **−14.4** | **+8.7** |

Strengths: excellent FCF conversion, net cash of ~$750M (debt $19M), no inventory, revenue highly predictable (recurring subscriptions + cloud consumption), receivables clean (DSO ~66 days), gross margin in the top decile of software.

The single blemish that keeps this out of the 8–9 bucket: **stock-based comp is 25–30% of revenue**, and diluted shares have gone 103.3M → 121.8M in three years — **~5.6% annual dilution**. On a Buffett owner-earnings basis (FCF less SBC), the business only *just* crossed into positive territory this year (+$8.7M TTM). Reported "free cash flow" is essentially the SBC add-back recycled. That is improving fast (SBC 30.6% → 24.2% of revenue) but it is not yet a cash-generating business in the owner sense.

---

## 3. Valuation Analysis — price implies ~21% FCF growth for a decade

At $84.31: EV/Sales (FY26E $650M) **14.6x** · EV/TTM FCF **56x** · P/TTM FCF **60x** · FCF yield **1.7%** · EV/FY26E non-GAAP operating income ($118M) **80x** · P/E on non-GAAP EPS (~$1.02) **~83x** · P/B 11x.

Note the round trip: the stock traded at **$34.75 on Feb 23, 2026** (6.3x EV/FY26 sales) and re-rated to $84–$104 between May and October on cloud/AI reacceleration. Nothing about the *business* tripled; the *multiple* did. That is precisely the condition in which a value buyer should get more cautious, not less.

**Hand-built DCF** (FCF base $170M, net cash $750M, 121.8M shares, 10% WACC, 3% terminal):

| Scenario | FCF growth | Equity value/share |
|---|---|---|
| Bear | 15% × 5y, 5% × 5y | **$42** |
| Base | 18% × 5y, 8% × 5y | **$51** |
| Bull | 22% × 5y, 12% × 5y | **$66** |
| **Market-implied** | **~21% CAGR × 10 years** | **$84** |

Intrinsic value range **$42–$66**, midpoint **~$54**. The current price sits **above even my bull case** and requires roughly two decades-perfect execution at 20%+ compounding with terminal economics intact. Analyst targets ($102–$125) are momentum-reflexive, not margin-of-safety exercises.

**Buy zone: $38–45** (25–30% discount to midpoint IV). At $84 this is not a purchase.

---

## 4. Management Quality Assessment — **Good, with reservations**

- **Founder-led:** Shlomi Ben Haim (co-founder/CEO, 3.6%, ~$431M of stock) with co-founders Fred Simon and Yoav Landman still in technical leadership. Insiders hold ~18%. Alignment is real, not rented.
- **Balance sheet discipline:** never levered, $750M net cash, funded the Qwak (MLOps) and Vdoo (security) tuck-ins from cash without dilution — both strategically coherent (they became Xray Advanced Security and the AI/ML model registry).
- **Capital allocation, newly attentive:** authorized a **$300M buyback** in Q1 2026 (first ever — a genuine signal management believes the franchise is durable). Execution so far is token ($2.0M in Q2). At 80x non-GAAP earnings, a buyback buys back very little; better to let the cash compound or buy assets.
- **Watch item:** routine 10b5-1 selling (CEO sold 15,000 shares Oct 7 at ~$97). Not a red flag, but not a signal of undervaluation either.
- **Grade: B+.** Honest, owner-minded, strategically consistent; the deduction is for a decade of SBC-funded "profitability" and a comp structure that pays in dilution rather than cash discipline.

---

## 5. Investment Verdict: **HOLD** (do not initiate; trim on strength)

This is a genuinely good business — narrow moat, 77% gross margins, 28% FCF margins, net cash, reaccelerating growth, and an AgentSecOps/AI-catalog story that is producing real revenue (+53% cloud). Ten years from now it will very likely be larger and more entrenched.

But Buffett's rule is not "buy good businesses"; it is "buy good businesses at a discount to intrinsic value." Here the arithmetic fails:

- Base-case IV ~$54 vs. $84.31 price → **~55% premium to fair value**.
- The price **already embeds my bull case**; there is zero margin of safety and negative optionality.
- Owner earnings (after SBC) are ~$9M against a $10.3B market cap. The 60x FCF multiple is being paid on a cash-flow figure that excludes 25% of revenue in compensation cost.
- A 22%-growth guide for FY26 against a Q2 print of 29% already tells you deceleration is expected; the multiple has no room for a miss, and this stock has twice fallen 25–35% in a single session in the past 12 months (Feb 20, 2026; Feb 5, 2025).

**Action:** If owned from lower levels, hold the core position and let the moat compound, but trim above $95–100. If not owned, wait — patience is the entire edge. Revisit at **$45 or below**, or if FCF (ex-SBC) annualizes above ~$100M while growth holds >20%, which would legitimately raise my IV.

---

## 6. Key Risks to the Value Thesis

1. **Multiple compression (primary risk).** At 14.6x EV/sales and 56x EV/FCF, a shift to a 10x sales/35x FCF regime — entirely normal for 20%-growth software in a risk-off tape — is a 30–40% drawdown with no change in fundamentals.
2. **SBC and dilution.** 25% of revenue paid in stock; 5.6% annual share growth. If the $300M buyback isn't scaled up, per-share value creation lags the business's growth.
3. **Competitive bundling.** GitHub/Microsoft and GitLab can give artifact management away to win the broader platform; hyperscalers (AWS CodeArtifact, Google Artifact Registry) can price near zero. Gross margin already slipping 300bps over five years is the early tell.
4. **Cloud/AI concentration of the growth story.** Cloud is 53% of revenue and growing 53%; a slowdown in AI-driven developer budgets hits the highest-multiple component first, and consumption-based revenue can decelerate faster than seat-based.
5. **Never-profitable-GAAP risk.** If growth decelerates to the mid-teens before GAAP operating margin turns positive, the "profitable growth" narrative unwinds and the terminal-value assumption (~80% of my DCF value) collapses.
6. **Geopolitical/structural.** Israeli-headquartered with significant R&D there; USD/ILS and regional risk are permanent, if modest, drags.

---

**Bottom line:** Wonderful product, narrow moat, honest founder-management, improving unit economics — priced for perfection and then some. **Hold, with a $45 buy trigger.** A great business at a demanding price is still a bad investment; that distinction is the whole job.

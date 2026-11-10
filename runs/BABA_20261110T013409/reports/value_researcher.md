# Value Researcher

- Symbol: BABA
- Elapsed: 144.4s

---
I have what I need. Writing the report now.

---

# Alibaba Group (BABA) — Value Investment Analysis
**Price: $105.38/ADS | Market cap: $253.4B (RMB ~1,804B) | Date: ~Nov 9, 2026**

> **Data note:** The platform's `calculate_valuation_ratios` / `compare_peer_valuations` outputs (P/E 2.4, P/B 0.23, EV/EBITDA 0.83) are corrupted — they divide RMB financials by a USD market cap (253.4 ÷ 103.6 = 2.4). I have rebuilt all multiples manually from the raw statements at RMB/USD ≈ 7.12. Ignore the reported peer premium/discount of −91.5%.

---

## 1. Business Quality Assessment — Moat: **NARROW** (downgraded from Wide)

Alibaba is really three businesses with three different moats:

| Segment | Moat | Evidence |
|---|---|---|
| **China e-commerce (Taobao/Tmall)** | **Narrow, eroding** | Still ~RMB 160B annualized adj. EBITA (Q1 FY27 ITA EBITA RMB 39.7B, −1% YoY) — a formidable cash cow. But share has been ceded to Pinduoduo and Douyin, and the company is now subsidizing quick commerce (RMB 49.5B revenue, +45%) against Meituan and JD. Pricing power is gone; this is now a capital-intensive share defense. |
| **Cloud (Alibaba Cloud)** | **Narrow, widening** | Revenue +45% YoY to RMB 48.4B in Q1 FY27 — the single best datapoint in the file. #1 share in China, Qwen is a leading open-source model family, and AI compute demand is real. This is the one segment where the moat is strengthening. |
| **International / local services / DME** | **None** | Structurally loss-making, sub-scale vs. local champions. |

**The five-year test:** ROIC has gone from 10.5% (FY25) to **4.3% (FY26)** against a WACC that, for a China-domiciled equity, I'd put at 10–12%. **ROIC < WACC is the definitive hallmark of a moat that is not currently being defended profitably.** Gross margin has held (~40%), but operating margin collapsed from 14.1% to 5.8% — the economics are being competed away at the operating line.

**Verdict: Narrow moat.** The e-commerce franchise is still excellent but no longer "set-and-forget"; the cloud franchise is genuinely improving but is being bought with enormous capital.

---

## 2. Financial Quality Score: **5 / 10**

| Metric (RMB, FY to Mar 31) | FY2024 | FY2025 | FY2026 |
|---|---|---|---|
| Revenue | 941B | 996B | 1,024B (+2.7%) |
| Gross margin | 37.7% | 40.0% | 39.8% |
| **Operating margin** | **12.0%** | **14.1%** | **5.8%** |
| Operating income | 113B | 141B | 60B |
| Net income | 80B | 130B | 104B |
| Capex | 33B | 87B | **127B** |
| **Free cash flow** | **+151B** | **+78B** | **−51B** |
| Owner earnings | 91B | 86B | **24B** |
| ROIC | 8.6% | 10.5% | **4.3%** |

**What's good:** Gross margin is remarkably stable at ~40% — the core marketplace still has real pricing power at the gross level. Revenue is predictable and diversified. The balance sheet is solid: RMB 358B cash/short-term investments vs. RMB 259B debt → **~RMB 99B net cash** (though total debt rose from 205B to 259B in one year to help fund capex). Diluted shares fell from 2,545M to 2,404M over two years.

**What's broken:**
- **Earnings quality is poor.** FY2026 net income of 104B sits *above* operating income of 60B — roughly RMB 80B of non-operating gains are propping up the GAAP number. Reported "EBITDA" of 186B includes these. Do not use it.
- **FCF conversion has gone negative.** OCF of 76B against capex of 127B. In Q1 FY27 alone, capex was **RMB 67.7B** — a ~RMB 270B annualized run-rate, or ~26% of revenue. Adjusted EBITDA that quarter was only RMB 27.3B, down 30% YoY.
- **This is the crux of the investment case.** Alibaba is spending more than 2x its EBITDA on AI infrastructure that depreciates in 3–5 years. D&A (currently 47B) will roughly double. Owner earnings of RMB 24B in FY2026 are a fraction of the RMB 86–91B the business generated in FY24–25.

Score: **5/10** — high-quality assets, deteriorating financial output.

---

## 3. Valuation Analysis

**Currency-corrected multiples at $105.38:**

| Metric | Value |
|---|---|
| Market cap | RMB 1,804B ($253B) |
| Net cash | RMB ~99B ($14B) |
| Enterprise value | RMB ~1,705B ($240B) |
| P/E (FY26 GAAP, inflated) | 17.0x |
| **P/E (normalized net income ~RMB 112B)** | **~16.1x** |
| **P/E ex-net-cash (core)** | **~15.6x** |
| P/B | 1.61x (BVPS RMB 467) |
| P/TBV | ~2.1x (ex-RMB 263B goodwill/intangibles) |
| EV/adj. EBITDA (RMB ~110B run-rate) | ~15.5x |
| FCF yield | **negative** |

**Normalized earnings build:** China e-commerce EBITA ~160B + cloud ~20B − quick-commerce losses ~50B − DME/other ~15B − corporate/SBC ~25B ≈ **RMB 110–120B operating income** mid-cycle. After tax and recurring interest/equity income → **~RMB 112B net income ≈ $6.40/ADS**.

**Sum-of-the-parts (my preferred lens here):**

| Component | Conservative | Base |
|---|---|---|
| China e-commerce (RMB 160B EBITA) | 6x → 960B | 8x → 1,280B |
| Cloud (RMB ~200B run-rate rev, +45%) | 3x sales → 600B | 5x sales → 1,000B |
| Quick commerce / intl / local | 0 | 150B |
| Net cash | 99B | 99B |
| Investment stakes (Ant ~33% + others), post-holdco discount | 150B | 250B |
| **Total equity value** | **RMB 1,809B → $102/ADS** | **RMB 2,779B → $157/ADS** |

**Intrinsic value estimate: ~$115–125/ADS base case** (blending SOTP base with a 15–17x normalized-earnings cross-check), with a bear case near $80 (capex produces no returns, quick-commerce losses persist) and a bull case above $160 (cloud becomes a genuine Wide-moat compounder).

**Current price of $105.38 sits at roughly a 10–15% discount to base-case intrinsic value.**

That is *not* a margin of safety. My discipline requires 20–30%. On a $118 midpoint, a 25% margin of safety implies a buy price of **~$88 or below** — which is where the stock traded as recently as September–October 2026.

**What the current price implies:** ~16x normalized earnings with cloud growing 45% is not demanding, but it is also not the "cheap China tech" trade of 2024. The market is already paying for a meaningful amount of AI success. It is *not* pricing in a depreciation cliff.

---

## 4. Management Quality Assessment — **Mixed / Cautiously Positive**

**Positives:**
- **Portfolio discipline improved.** Divested non-core assets (Sun Art, Intime) and cancelled value-destructive spin-offs (Cainiao, Cloud) when market conditions didn't cooperate. That is rational, not empire-building.
- **Shareholder returns were excellent, then stopped.** Buybacks of RMB 89B (FY24) + RMB 87B (FY25) shrank the share count by 5.5%. An annual dividend was initiated and raised to $1.05/ADS (~1.0% yield; the 2.9% "yield" quoted by the platform includes a one-off $2.00 special).
- **FY2026 buybacks collapsed to RMB 7.6B.** Capital was redirected wholesale into capex. Defensible if AI returns materialize; a red flag if they don't. Shareholders have effectively been converted from owners receiving cash to financiers of a build-out.
- CEO Eddie Wu (since 2023) has sharpened strategy around "user first, AI-driven" — coherent, but the org has been restructured repeatedly.

**Negatives:**
- **The RMB 270B/yr capex commitment is the largest capital-allocation decision in the company's history**, made with no disclosed return-on-invested-capital framework and against a 4.3% current ROIC. Management talks about payback periods; they have not published the math. I treat this as unproven.
- Governance overhang: partnership-controlled board, VIE contractual structure (no direct ownership of the operating licenses), and demonstrated state influence (Ant Group's Golden Share). These are permanent, uninsurable discounts.
- Debt-funded capex (total debt +RMB 54B in FY26) reduces the net-cash cushion that made this name defensible.

---

## 5. Investment Verdict: **HOLD**

Alibaba today is a tale of two franchises. The China e-commerce business is a still-profitable but visibly narrowing moat burning cash to defend share in quick commerce. The cloud business is genuinely accelerating and may be worth a great deal. But the company is currently converting ~RMB 86B of prior-year owner earnings into **negative free cash flow**, with ROIC of 4.3% below its cost of capital, and it has stopped buying back stock to fund a RMB 270B annualized AI build-out whose returns are unproven and whose depreciation has not yet hit the P&L.

At $105, you are paying a fair price for a good-but-not-great business with a genuinely uncertain capital-allocation outcome. **A fair price is not a buy.**

- **Not a Sell:** 1.6x book, ~16x normalized earnings, RMB 99B net cash, a 45%-growth cloud franchise, and a management team that has shown real portfolio discipline. The downside is supported by hard assets and a strategic stake in Ant Group.
- **Not a Buy:** no margin of safety, negative FCF, ROIC below WACC, and a moat that is narrowing in the segment that pays the bills.

**Actionable levels:**
- **Buy at ≤$88** (25% discount to base intrinsic value). At $80–85 the risk/reward inverts decisively.
- **Trim / Sell at ≥$150** absent evidence that cloud EBITA is scaling faster than depreciation.
- **The trigger to upgrade to Buy at current prices:** two consecutive quarters showing (a) quick-commerce losses approaching breakeven, (b) cloud revenue growth ≥40% with cloud EBITA margin expanding, and (c) capex guidance held flat rather than raised. Any two of three would materially raise my intrinsic value estimate.

---

## 6. Key Risks to the Value Thesis

1. **The depreciation cliff (largest risk).** Capex of RMB 270B/yr against ~RMB 110B adjusted EBITDA. Even at a 5-year life, D&A could double from RMB 47B toward RMB 90–110B, compressing EBIT toward zero. The P&L damage has barely begun. If AI demand disappoints, this becomes stranded capital with a 3–5 year obsolescence clock.
2. **No proof of AI returns.** Cloud is growing 45%, but management has not articulated a ROIC framework for the build-out. Chinese cloud pricing is competitive, and US export controls restrict access to leading-edge Nvidia silicon — a structural cost/performance handicap versus US hyperscalers.
3. **Quick-commerce war.** Fighting Meituan and JD simultaneously in instant retail. Losses have narrowed ("halved by October vs. July/August"), but this is a subsidy contest with no structural winner, funded from the e-commerce cash cow.
4. **Core moat erosion.** Pinduoduo and Douyin continue to take share in China commerce. ITA EBITA was −1% YoY in Q1 FY27 — stable, but no longer growing, while the segment is asked to fund everything else.
5. **China policy and geopolitics.** Antitrust, "common prosperity," data security, and state influence via special shares. ADR delisting risk is mitigated (HK primary listing) but not eliminated; VIE structures leave holders with contractual, not ownership, rights.
6. **Currency and disclosure.** RMB reporting vs. USD trading; conglomerate disclosure makes segment economics hard to verify independently.
7. **Data-quality risk in this analysis.** Peer multiples were unavailable in usable form (the comparison tool is currency-corrupted), and the equity-investment portfolio (Ant Group, etc.) is estimated from memory rather than from the FY2026 filing's investment schedule. The SOTP's investment-stake line (RMB 150–250B) is the softest number in this report; a 10-K review would tighten it materially.

---

**Bottom line:** A narrow-moat, high-quality asset base temporarily generating sub-cost-of-capital returns and negative free cash flow while making its largest-ever capital bet. Worth owning at $88 or below. At $105, watch and wait.

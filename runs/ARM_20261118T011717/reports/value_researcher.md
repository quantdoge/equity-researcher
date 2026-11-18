# Value Researcher

- Symbol: ARM
- Elapsed: 107.1s

---
I have sufficient data. Writing the analysis now.

---

# ARM Holdings plc (NASDAQ: ARM) — Value Investment Analysis

**Price: $183.39** (close 17-Nov-2026) · **Market cap: ~$195.9B** · **Net cash: $2.29B** · **EV: ~$192.7B**
Latest reported period: **FY2026, ended 31-Mar-2026** (Q2 FY2027 reported 4-Nov-2026)

---

## 1. Business Quality Assessment

**Moat rating: WIDE — but the moat is being actively re-engineered by management, which is itself a risk.**

Arm licenses CPU instruction-set architecture (ISA) and physical IP. Customers (Apple, Qualcomm, MediaTek, NVIDIA, Amazon, Google, Microsoft) design chips on top of it. The moat sources are real and unusually durable:

| Moat source | Evidence |
|---|---|
| **Intangible assets / ecosystem** | ~99% of smartphone CPUs; 20M+ developers; the toolchain, compilers, EDA flows and OS support are built around Arm. This is a two-decade accumulation that cannot be bought. |
| **Switching costs** | Re-architecting silicon is a 3–5 year, nine-figure decision with software-validation risk. Customers re-up rather than defect — hence the annuity-like royalty stream. |
| **Efficient scale** | R&D is ~$2.7B/yr on a $4.9B revenue base (55% of sales). No single licensee can spread that across its own volume; Arm amortises architecture cost over the entire industry. |
| **Pricing power** | Gross margin **92.5%**. Royalty revenue was $2,613M in FY2026, **+20.5% YoY** — pricing/mix, not just unit volumes. |

**Has the moat widened?** In reach, yes: data-centre royalties *doubled* YoY in Q2 FY27 (Grace, Graviton, Axion, Cobalt), plus automotive and IoT. In **purity**, it has arguably narrowed — two structural changes concern me:

1. **Royalty quality is deteriorating.** Royalties — the annuity — grew just **+8% to $670M** in Q2 FY27 versus a ~$721M consensus. The 27% total revenue beat was carried by **licensing +50% to $773M**, which is lumpy, negotiated, and lower-quality earnings. You are paying a royalty-machine multiple for a licensing-business mix shift.
2. **Arm is becoming a competitor to its own customers.** Management is investing heavily in Compute Subsystems and its own AGI silicon. Capex jumped to $545M in FY2026 (from $219M) largely for this. Arm's entire bargaining power rests on neutrality — a merchant supplier that does not compete with its licensees. Building chips monetises faster but taxes the moat. This is the single most important strategic question for the next decade and it is unresolved.

**Verdict on moat:** Wide, and among the best in semiconductors. But a wide moat is a *precondition* for a value purchase, not a justification for any price.

---

## 2. Financial Quality Score: **6 / 10**

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | FY2026 | Assessment |
|---|---|---|---|---|---|---|
| Revenue ($M) | 2,703 | 2,679 | 3,233 | 4,007 | **4,920** | 19.4% 4-yr CAGR; 3-yr CAGR ~22.8%. Excellent. |
| Gross margin | 91.9% | 92.7% | 92.8% | **94.9%** | 92.5% | Elite, but ticking down 240bp on mix. |
| GAAP operating margin | 25.2% | 25.3% | 3.1%* | 20.6% | **18.5%** | *FY24 depressed by IPO SBC. Structurally ~19–25%. |
| Net income ($M) | 549 | 524 | 306 | 792 | **904** | +14% on +23% revenue — margin compression. |
| FCF ($M) | — | 646 | 947 | 178 | **979** | Violently volatile: −$1,465M working capital in FY25. |
| Owner earnings ($M) | — | 601 | 325 | 756 | **608** | **Down 20% YoY.** This is the number that matters. |
| ROIC | — | 15.9% | 1.8% | 11.5% | **10.4%** | Barely at WACC. Ex-cash & ex-goodwill ≈ 29%. |
| ROE | — | 12.9% | 5.8% | 11.6% | **10.9%** | Low for a 92%-gross-margin business. |
| Net cash ($M) | — | 1,335 | 1,697 | 1,729 | **2,294** | Fortress. Zero long-term debt. |

**The single most important number on this page: owner earnings fell from $756M to $608M while revenue grew 23%.** Owner earnings (NI + D&A − maintenance capex) now *equate to 12.4% of revenue*, versus 18.9% a year ago.

Why? **Stock-based compensation of $1,052M — 21% of revenue and larger than net income.** GAAP operating income of $908M is struck after a $1.05B non-cash charge that is nonetheless a genuine transfer of owner value: share count has drifted from 1.026B to 1.068B (+4.1% over three years, ~1.3%/yr dilution) with **zero buybacks to offset it**. Cash flow from operations also swung on a −$602M working-capital drag (receivables up 30% to $2.47B — licensing deals booked but not yet collected).

Strip SBC out and you get a more flattering ~$1.6B of "cash earnings"; include it and you get $608M. The truth is in between, but any owner-earnings analysis must penalise a company that pays a fifth of revenue in stock and never retires a share.

**Score rationale:** 10/10 on gross margin and balance sheet; 3/10 on cash conversion and capital efficiency. Blended: **6/10**. A wide-moat business that converts only 67% of net income to FCF and earns ~10% ROIC is a good business running below its theoretical potential.

---

## 3. Valuation Analysis

This is where the case collapses.

| Multiple | ARM | Peer median (8 semis) | Premium |
|---|---|---|---|
| P/E | **215.8x** | 31.7x | **+580%** |
| EV/EBITDA | **137.1x** | — | — |
| P/FCF | **200.1x** | — | — |
| P/Sales | **~35x** | ~6x | ~6x |
| FCF yield | **0.50%** | — | vs 10-yr UST ~4% |
| Owner-earnings yield | **0.31%** | — | — |
| Dividend | **None** | — | — |
| P/B | 23.6x | — | — |

**DCF (my model, not the tool's).** The provided DCF engine returns $34.7B intrinsic value (~$32/share) on trailing FCF of $979M, 14.9% growth, 10% WACC, 3% terminal. That base FCF is depressed by the working-capital swing, so I rebuilt it on a normalised base of ~$1.3B FY2027 FCF:

| Scenario | FCF CAGR (yr 1–5 / 6–10) | WACC | Terminal | **Value/share** |
|---|---|---|---|---|
| Bear (royalty stalls, RISC-V bites) | 12% / 6% | 10% | 3% | **~$40** |
| **Base (consensus-like)** | **20% / 10%** | **9%** | **3%** | **~$56** |
| Bull (data-centre royalty ramp works) | 25% / 12% | 9% | 3% | **~$83** |
| Blue-sky (30% CAGR for 7 yrs, then 15%) | 30% / 15% | 9% | 3% | **~$145** |

**Intrinsic value range: $50–$90, midpoint ~$65.**

**The current price of $183 is 2.8× my base-case value and exceeds even my blue-sky case — which requires ARM to compound free cash flow at 30% annually for seven consecutive years.**

**What is the market actually implying?** At $195.9B, to earn a 9% return with 3% terminal growth, ARM must eventually produce ~$11.4B of FCF — roughly **eleven times** today's cash earnings, and ~2.3× current *revenue*. At a 25% FCF CAGR that is a decade of flawless execution, after which you still only earn your cost of capital. There is **no margin of safety; there is a negative margin of safety.**

For calibration, the sell-side is split precisely along this fault line: Goldman Sachs **Sell, $160**; HSBC **$215**; TD Cowen **$250**; RBC **$300**; Barclays **$325**; Raymond James **$641** (an outlier I would disregard). The dispersion — a 4x spread between high and low targets — is itself the tell of a stock priced on narrative rather than cash flows. Even the median bull target of ~$260 requires my blue-sky case plus a further 80% re-rating.

**Price context:** ARM bottomed near $104 in January 2026, ran to **$439 on 18 June 2026** (+143% YTD), and has since fallen **58%** to $183 — including a **−13% drop on 5 November** on the royalty miss. Beta is **3.94**. This is a stock that moves 10% on a Tuesday. That volatility is not opportunity when the starting valuation is 200× FCF; it is the mechanism by which momentum holders transfer wealth to each other.

---

## 4. Management Quality Assessment

**Grade: Good operator, poorly aligned with the outside shareholder.**

**Positives**
- Rene Haas has executed a genuine strategic re-rating: shifting Arm from a passive ISA licensor to selling Compute Subsystems (higher royalty per chip), penetrating data centre and automotive, and raising royalty rates on v9+. Royalty revenue compounding 20.5% in FY2026 is evidence the strategy works.
- Balance sheet discipline: net cash grew to $2.29B, no long-term debt, no empire-building M&A (goodwill flat at ~$1.8B).
- Consistent beats and raises on revenue; FY2027 Q3 guided to $1.54B ±$50M.

**Serious negatives**
1. **SoftBank controls ~87–90% of the shares.** Arm represents **more than 40% of SoftBank Group's invested assets**. The minority holder is a guest in SoftBank's balance sheet; further sell-downs are a live, recurring overhang. Float scarcity is precisely why the beta is 3.94.
2. **SBC of $1.05B (21% of revenue) with zero buybacks.** Shareholders are diluted ~1.3%/yr and management has shown no inclination to offset it. In Buffett terms, this is management paying itself in the currency owners hold.
3. **Zero capital returned** — no dividend, no repurchase, ever as a public company.
4. **Capital allocation is now being redirected into competing with customers.** Capex tripled to $545M. If Arm's own silicon succeeds, it monetises; if it alienates Qualcomm/MediaTek, it destroys the neutrality premium that justifies the royalty. Management has not articulated how it will hold both.
5. **The Qualcomm/Nuvia licensing dispute** revealed that Arm's most important contracts are contestable. The near-term litigation risk has receded but the precedent has not.

**Insider ownership** is effectively SoftBank's, so the usual "owner-operator" test is passed only in the sense that a controlling shareholder with its own liquidity needs sits above you.

---

## 5. Investment Verdict: **SELL** (Avoid new capital; do not short)

**Explicitly: this is a valuation verdict, not a quality verdict.** ARM is a genuinely wonderful business — arguably a 9/10 business — trading at a 10/10 price. Buffett's rule is that a great business at a fair price beats a fair business at a great price; it says nothing about a great business at three times fair value.

- **Business quality:** Wide moat, 92% gross margins, net cash, structural AI/data-centre tailwind. **Pass.**
- **Financial quality:** 6/10. Owner earnings *declining* while revenue grows; 10.4% ROIC ≈ WACC; 21%-of-revenue SBC. **Marginal.**
- **Valuation:** $183 vs intrinsic value of ~$65 (range $50–90). 216× earnings, 200× FCF, 0.5% FCF yield, 580% P/E premium to peers. **Hard fail.**

A business trading at a fair price is not a buy. A business trading at **2.8× intrinsic value** is a sell.

**What would make me a buyer:** Roughly **$80–90/share** (a 25–30% discount to my *bull* case), which would still be ~110× forward earnings — a price I would only pay in size if royalty growth re-accelerates above 15%, the licensing mix shift reverses, SBC falls below 12% of revenue, and Arm credibly commits to neutrality or spins out its silicon ambitions. Until then I will watch from the sidelines. This is a superb business at an uninvestable price.

---

## 6. Key Risks to the Value Thesis

**Risks to my SELL call (i.e., where I could be wrong — and they are real):**

1. **The royalty rate story is optionality I may be under-modelling.** If Arm's v9/CSS transition doubles the royalty per chip *and* data-centre unit volumes compound, ARM's revenue could reach $12–15B by FY2032 rather than the ~$10B my bull case assumes. In that world, $183 is merely expensive rather than absurd. This is the strongest argument against me, and I respect it — it is why I say Sell, not Strong Sell.
2. **AI capex super-cycle.** Data-centre royalties doubled YoY. If Arm captures a meaningful slice of AI accelerator CPUs (not GPUs, where NVIDIA owns the world), the TAM expands faster than my 20% base case.
3. **Scarcity premium.** With SoftBank holding ~87–90%, the free float is small, index inclusion is recent, and passive/momentum flows can keep a stock divorced from fundamentals far longer than a value investor can stay solvent. Being right early is indistinguishable from being wrong.
4. **Take-private / strategic bid.** SoftBank has explored using Arm in transactions. Any bid would come at a premium to market — a genuine risk to a short position, but not to a decision to simply not own it.

**Risks to owning it at any price (the reason I won't):**

5. **Royalty deceleration is the thesis killer.** Royalties are the annuity; licensing is the spot market. Q2 FY27 royalties +8% vs licensing +50% says the annuity is growing at high-single digits, not 20%. A royalty machine growing 8% does not deserve 200× FCF.
6. **Competing with customers.** Own-silicon ambitions against Qualcomm/MediaTek/NVIDIA threaten the neutrality that is the moat's foundation. Under-appreciated and binary.
7. **RISC-V.** Open-source ISA is no longer a science project — it is shipping in microcontrollers, automotive and Chinese SoCs. Ecosystem gravity is strong, but a decade is a long time and Chinese mandates make adoption a policy choice, not an economic one.
8. **China exposure (~20–25% of revenue)** through the separately governed Arm China JV — opaque, geopolitically exposed, and outside management's clean control.
9. **Customer concentration** — a handful of licensees drive a large share of revenue; each negotiation is a re-litigation of the moat.
10. **Dilution and SBC** — ~1.3%/yr with no offset, compounding against owners indefinitely.
11. **Valuation risk itself.** At 200× FCF, any growth disappointment does not cause a 15% drawdown; it causes a 50%+ de-rating. The stock has already fallen 58% from its June high and remains 2.8× intrinsic value. **Falling a lot is not the same as falling enough.**

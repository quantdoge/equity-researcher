# Value Researcher

- Symbol: CBRS
- Elapsed: 135.5s

---
## Cerebras Systems (CBRS) — Value Investment Analysis
**Price $177.65 (Sept 30, 2026 close) | ~225M shares | Market cap ≈ $40.0B | Est. EV ≈ $34B (post-IPO net cash ~$6B)**

*Data notes up front: the vendor profile's $120.66 price / $27.3B cap is stale — I use the Sept 30, 2026 close. No 10-K has been filed yet (IPO 2026-05-14), so FY2025 figures are from the annual series and Q1/Q2 2026 from earnings releases. Q1/Q2 2026 revenue and margin detail is partly reconstructed from press-release text; treat as directional.*

---

### 1. Business Quality Assessment — Moat Rating: **Narrow (and not widening)**

Cerebras builds wafer-scale AI processors (WSE-3: an entire silicon wafer as one chip, 44GB on-chip SRAM, massive memory bandwidth) and sells them as rack-scale systems plus a "Fast Inference Cloud." The technical achievement is real, and on inference benchmarks (tokens/sec on Llama-class models) it has repeatedly shown leadership.

But a moat is about *durable pricing power*, and the evidence points the wrong way:

| Moat test | Evidence | Verdict |
|---|---|---|
| Pricing power | GAAP gross margin 39.0% in FY25 — vs Nvidia ~70%+. Core gross margin **compressed 49% → 41% → guided 36–38%** through 2026. GAAP GM fell to **14%** in Q2'26 (vs ~26% consensus). | **Fails** |
| Switching costs | Inference workloads are more portable than training; customers can dual-source GPUs. Cerebras' SDK is PyTorch-compatible precisely because it must reduce switching friction. | **Weak** |
| Intangible assets | Genuine patents and a unique wafer-scale manufacturing route (TSMC partnership). A real but narrow technical lead. | **Modest positive** |
| Cost advantage | None demonstrated. Capex was **75% of revenue** in FY25 ($383M). Owning datacenters converts a capital-light systems business into a capital-intensive one. | **Fails** |
| Competitive intensity | Nvidia CUDA lock-in + annual cadence; hyperscaler ASICs (TPU, Trainium, MTIA); Groq, SambaNova. Cerebras must win on perf/$ every refresh — a treadmill, not a moat. | **Negative** |

**Customer concentration is the single most serious quality defect.** G42 (UAE) was **87% of FY2024 revenue**; two customers were **86% of FY2025 revenue**; one customer was **78% of year-end 2025 receivables**. A $24.6B backlog — heavily tied to a reported ~$10B OpenAI commitment — is the bull case, but OpenAI is itself cash-consumptive and multi-sources silicon. This is a business whose revenue depends on a handful of sovereign and frontier-lab capital-spending decisions.

ROIC: the reported 45.9% for FY25 is an artifact of a negative equity base and a one-off gain. On an operating basis the business earns **negative returns on capital** and has cumulative losses of ~$905M. The "ROIC > WACC consistently" test is not met.

---

### 2. Financial Quality Score: **3 / 10**

| Metric | FY2022 | FY2023 | FY2024 | FY2025 | Q1'26 | Q2'26 |
|---|---|---|---|---|---|---|
| Revenue | $24.6M | $78.7M | $290.3M | **$510.0M** | $193.4M | $209.9M |
| YoY growth | — | +220% | +269% | **+75.7%** | +94% | +103% |
| GAAP gross margin | 11.7% | 33.5% | 42.3% | **39.0%** | ~49% core | **14% GAAP / 41% core** |
| GAAP operating margin | −726% | −170% | −35.0% | **−28.5%** | −7.8% | n/a |
| Core operating margin | — | — | — | — | — | **−16%** (vs −42% LY) |
| Free cash flow | −$175M | −$86M | +$429M* | **−$393M** | n/a | n/a |
| Owner earnings | −$176M | −$123M | −$494M | **−$110M** | — | — |
| SBC | $17M | $27M | $59M | $50M (9.8% of rev) | — | — |

\*FY24 FCF is inflated by a **+$443M working-capital swing**; operating cash flow was +$452M against a −$482M net loss. It is not repeatable operating cash generation.

Positives: revenue is compounding spectacularly; gross margin has structurally improved from 12% to ~40%; core operating margin improved from −42% to −16% YoY; and the IPO (~$5.6B raised) leaves roughly **$6B of net cash**, so there is no solvency risk for years.

Why the score is still low:
- **FY2025 net income of +$238M is not real earnings.** Operating income was **−$145M**; the ~$390M bridge to positive net income is non-operating/non-cash (operating cash flow was −$10.5M). Any screen showing a 294x P/E or "profitable in 2025" is misleading.
- **FCF is deeply negative** (−$393M) and capex-intensive by design. The pivot from selling systems to owning an inference cloud is a strategy shift that consumes capital and takes on utilization risk.
- **Negative shareholders' equity** (−$579M) pre-IPO, with retained deficit of $905M.
- GAAP gross margin of 14% in Q2'26 shows how quickly margin evaporates when mix shifts and depreciation on owned capacity lands.

---

### 3. Valuation Analysis — **No margin of safety; the price discounts perfection**

Current multiples on my ~$40B cap / ~$34B EV:
- **EV/Sales (FY26E ~$860M): ~40x**; P/S ~46x
- **P/E (GAAP, distorted): 294x** vs **sector-peer median 44.3x** — a ~564% premium (per the peer screen)
- **EV/EBITDA (reported): ~90x**
- **P/FCF: negative** — no FCF-based valuation anchor exists

**My own DCF (10-yr, 12% WACC, 3% terminal, on revenue/FCF-margin assumptions):**

| Case | Revenue CAGR '26–'36 | 2036 revenue | FCF margin | PV of EV | + net cash | **Value/share** |
|---|---|---|---|---|---|---|
| Bear (share loss to GPUs/ASICs) | 15% | $3.5B | 12% | ~$4B | $6B | **~$44** |
| **Base** | **25%** | **$8.0B** | **18%** | **~$7B** | **$6B** | **~$59** |
| Bull (backlog converts, cloud scales) | 35% | $17.3B | 22% | ~$18B | $6B | **~$107** |
| "Perfection" (what today's price needs) | ~40% | ~$25B | 25% | ~$34B | $6B | **~$178** |

The tool-based DCF is unusable here (negative base FCF, growth assumption floored at 5%), so the above is my construction. The conclusion is robust across methods: **to justify $177.65, Cerebras must compound revenue at ~40% for a decade, hold 25% FCF margins, and fend off Nvidia while its two largest customers become a broad base.** My base case implies **~$59/share**; a generous bull case implies **~$107** — still ~40% below the current quote.

Requiring a 25–30% margin of safety to my *bull* case, the buy price would be roughly **$75–80**. The stock would need to fall another ~55–57% before entering that zone.

Analyst price targets ($270–330) are clustered at 1.5–1.9x the current price, but they are all post-IPO initiation targets from the underwriting syndicate era and are momentum/backlog-driven, not intrinsic-value-driven. I give them little weight.

---

### 4. Management Quality Assessment — **Mixed-to-Good (B−)**

**Strengths:**
- **Founder-led.** Andrew Feldman (co-founder/CEO) previously founded SeaMicro (sold to AMD). CTO Sean Lie co-founded. Deep technical conviction and a 10-year head start on wafer-scale integration.
- **Visionary capital raising** — took a capital-hungry hardware bet public at a ~$55B valuation, funding the balance sheet for years.
- **Commercial validation** of a $24.6B backlog and sovereign-AI relationships.

**Concerns:**
- **Ownership is modest.** Feldman holds ~10.3M shares (~4.6%) post-IPO — enough to care, not enough to be a true owner-operator. Much of the equity sits with VCs and G42, whose interests may diverge from public holders.
- **Insider selling.** Reports of the CEO and CTO selling **over $240M** under pre-arranged 10b5-1 plans shortly after IPO. Legal, but a value investor should note the signal.
- **Capital allocation is unproven where it matters most.** Deploying IPO proceeds into owned datacenters (FY25 capex = 75% of revenue) puts management in the position of forecasting AI inference demand and utilization — a business with far lower returns on capital than selling chips. Also unclear: the ~$38M of FY25 share repurchases alongside a cash-burning model.
- **No dividend, no buyback policy, no FCF track record.** Owner-orientation is aspirational at this stage.

---

### 5. Investment Verdict: **SELL / AVOID** (do not initiate; no position warranted)

This is a genuinely impressive technology company and one of the most important new listings in AI semiconductors. It is **not** a value investment by any Buffett standard:

1. **Outside the circle of competence for durable forecasting.** The 10-year economics of a single-architecture AI chip vendor competing against Nvidia's ecosystem and hyperscaler custom silicon are not predictable with the confidence a concentrated value position requires.
2. **No moat that protects capital.** Volatile, compressing gross margins (14% GAAP in Q2'26) and 86% revenue concentration in two customers are the opposite of pricing power and predictability.
3. **Financial quality is poor** — negative FCF, negative operating returns, capital intensity rising, SBC ~10% of revenue, a headline 2025 "profit" that isn't operating earnings.
4. **Valuation offers no margin of safety whatsoever.** ~40x EV/FY26E sales and ~3x my base-case intrinsic value. The market price already requires the bull-to-perfection scenario; there is no scenario in which a conservative investor is paid for the risk taken.

**If you already own it:** the position was never margin-of-safety-backed; the 43% drawdown from the IPO close has not made it cheap, only less absurd. Trimming into strength post-print remains sensible.

**What would change my mind (a watchlist trigger, not a buy trigger yet):** (a) price below ~$80 (my bull-case minus a 25% discount); (b) gross margin stabilized above 45% GAAP for four consecutive quarters; (c) no customer >30% of revenue; (d) positive operating cash flow excluding working capital for a full year; (e) evidence that the $24.6B backlog converts at contracted prices rather than renegotiated ones.

---

### 6. Key Risks to the Value Thesis

**Risks to owning it (bear case reinforces my avoid):**
- **Customer concentration / counterparty risk** — G42 and OpenAI drive the P&L and the backlog. A single deferred deployment or renegotiation can halve revenue visibility. Also geopolitical (UAE export controls, US–China rules).
- **Margin structure is deteriorating, not just lumpy** — core GM guided down to 36–38% with capex-heavy cloud mix; depreciation is now a permanent cost line.
- **Competitive displacement** — Nvidia's inference roadmap plus hyperscaler ASICs could compress perf/$ leadership within 18–24 months; wafer-scale also carries single-supplier (TSMC) and yield risk.
- **Capital intensity / utilization risk** — owning datacenters turns a product company into a capacity-betting business; idle capacity destroys returns.
- **Dilution** — SBC at ~10% of revenue plus future raises.

**Risks to my *bearish* call (be intellectually honest — these are real):**
- The $24.6B backlog (≈29x FY26E revenue) is extraordinary and, if it converts at contracted economics, revenue could exceed my bull case by a wide margin. This is the single strongest argument against me.
- Backlog conversion plus a shift to higher-margin inference-as-a-service at scale could produce FCF margins above 25%, which is what the current price assumes.
- Strategic scarcity value: Cerebras is one of the few credible non-Nvidia merchant AI compute platforms, and could be an acquisition or sovereign-partnership target at a premium.
- Extreme scarcity premium and index inclusion flows can keep a $40B AI name elevated well beyond fundamental value for long stretches.

**Bottom line:** A great technology at a price that assumes flawless execution for ten years, with a balance sheet that funds the attempt but a P&L that has never produced durable free cash flow. Buffett's rule applies exactly here: *"For the investor, a too-high purchase price for the stock of an excellent company can undo the effects of a subsequent decade of favorable business developments."* **Pass.**

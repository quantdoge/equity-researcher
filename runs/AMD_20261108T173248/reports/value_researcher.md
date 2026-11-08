# Value Researcher

- Symbol: AMD
- Elapsed: 50.8s

---
# AMD — Value Investment Analysis

**Price: $449.04 | Market cap $734.6B | EV ~$728B | 1.636B diluted shares | Net cash ~$6.1B**

*Data note: the valuation tool reports $449.04 (current). My price history pull was truncated at 2026-02-20 ($200.15), and my quarterly-income-statement request defaulted to annual. I've reconstructed FY2026 progress from the earnings calendar (Q1–Q3 actuals + Q4 estimate). Flagging these gaps rather than smoothing over them.*

---

## 1. Business Quality Assessment — Moat: **Narrow** (widening in server CPU, unproven in AI)

AMD is a genuinely transformed company. Lisa Su took it from ~$2/share and near insolvency in 2015 to $34.6B of FY2025 revenue. But moat is a structural question, not a narrative one.

**What is real:**
- **x86 duopoly with Intel** in PC and server CPU. Intel's foundry mis-execution handed AMD durable share gains; EPYC server share has compounded for eight straight years. Switching costs exist (socket/platform qualification cycles of 12–24 months), but x86 is an open standard — the advantage is design execution plus TSMC access, not lock-in.
- **Semi-custom franchise** (PlayStation/Xbox) — sticky, multi-year design wins, but a mature, low-growth console cycle.
- **Fabless model** — capital-light (capex just $974M on $34.6B revenue = 2.8% of sales), high asset turns.

**What is not real (or not yet):**
- **No software moat in AI.** CUDA is the actual fortress in accelerated computing, and AMD doesn't own it. ROCm remains a follower. AMD's position is "credible second source," which caps pricing power.
- **Revealed weakness in bargaining power:** winning the OpenAI anchor deal reportedly required warrant/equity economics. A business with a wide moat does not pay its customers in equity to adopt its product. Nvidia's ~70%+ gross margin versus AMD's 49.5% is the quantitative expression of this gap.
- **No manufacturing moat** — 100% dependent on TSMC for leading edge, behind Nvidia and Apple in allocation priority.
- **Gross margin of 49.5%** is a good semiconductor margin but nowhere near a toll-bridge. It has improved only ~500bps in five years.

**The decisive moat test — ROIC vs WACC — FAILS:**

| | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|
| ROIC | 2.19% | 0.68% | 3.18% | **5.47%** |
| ROE | 2.41% | 1.53% | 2.85% | 6.88% |

Against a WACC of ~10%, AMD has destroyed economic value on a reported basis every year for four years. The mitigating fact — and it matters — is that $41.8B of goodwill and intangibles (66% of $63.0B book equity) sits on the balance sheet from the $49B all-stock Xilinx deal. Excluding that acquisition premium, operating capital is only ~$15B against ~$5.5–5.9B of pre-amortization operating income, implying **~20–25% ROIC on the underlying business**. So: the *operations* are moated; the *capital allocation* is what has failed to earn its cost.

**Verdict: Narrow moat, 5-year durability questionable.** Widening in server CPU against a wounded Intel; narrowing-or-unclear in AI accelerators where the competitor is stronger, richer and owns the software layer.

---

## 2. Financial Quality Score: **7 / 10**

| Metric | FY2022 | FY2023 | FY2024 | FY2025 |
|---|---|---|---|---|
| Revenue ($B) | 23.6 | 22.7 | 25.8 | **34.6** |
| Growth | +43.6% | −3.9% | +13.7% | +34.3% |
| Gross margin | 44.9% | 46.1% | 49.4% | **49.5%** |
| Operating margin | 5.4% | 1.8% | 7.4% | **10.7%** |
| FCF ($B) | 3.12 | 1.12 | 2.41 | **6.74** |
| SBC ($B) | 1.08 | 1.38 | 1.41 | 1.64 |

**Strengths:** Revenue CAGR of 31.4% over five years with gross margin expanding ~500bps — that is real operating leverage. FCF of $6.74B is 155% of net income, comfortably above the 80% quality threshold (partly because $3.0B of mostly acquisition-related D&A overstates economic depreciation). Balance sheet is fortress-grade: $10.55B cash, $4.47B debt, current ratio 2.85, net cash.

**Deductions:**
- **Volatility, not predictability.** Operating margin went 22.2% (2021) → 1.8% (2023) → 10.7% (2025). A −3.9% revenue year in 2023 reminds you this is a cyclical. Buffett wants predictability; AMD sells it in bursts.
- **Earnings quality is soft at the margin.** FY2026 TTM net income (~$10.9B on ~$45.4B revenue) exceeds what operating income would support — implying non-operating gains (investment marks, tax items) are flattering the EPS line. I would not capitalize the current EPS at a market multiple.
- **Working capital bleeding:** change in WC was −$2.38B in FY2025, and inventory days have risen to ~165 (from ~160). Inventory build ahead of the MI400/MI450 ramp could be prudent or could be a demand air pocket. Unknowable today; a red flag worth watching.
- **SBC of $1.64B = 4.7% of revenue.** Owner earnings after SBC are ~$5.1B, not $6.7B. Real, recurring, and dilutive.

---

## 3. Valuation Analysis — **Intrinsic value ~$290; price $449. Negative margin of safety.**

**Current multiples (price $449.04):**

| Metric | Value |
|---|---|
| P/E (TTM, EPS ~$6.65) | **67.5x** |
| P/E (FY2026E, EPS ~$8.03) | **55.9x** |
| P/B | 11.7x |
| P/Tangible book ($21.2B) | **~34x** |
| EV/EBITDA (FY2025 $7.28B) | **100x** |
| EV/EBITDA (TTM est. ~$11B) | ~66x |
| FCF yield (FY2025) | **0.92%** |
| FCF yield (TTM est. ~$11B) | ~1.5% |
| Peer median P/E (8 semis) | 38.1x → **+345% premium** |

The business has genuinely accelerated: Q3 FY2026 revenue $13.38B (+45% YoY), Q4 guided ~$17.0B (+65%), FY2026 revenue tracking ~$52B (+51%). But the stock has *more* than doubled from ~$200 in February 2026 to $449 — the multiple expanded faster than the earnings. You are now paying 56x forward for a cyclical hardware company that competes against the best business in the world.

**DCF scenarios** (base = ~$10B normalized owner FCF, 10% WACC, 3% terminal, 10-yr explicit):

| Scenario | FCF growth (10 yr) | Equity value | Per share |
|---|---|---|---|
| Conservative | 8% | $229B | **$140** |
| Base | 15% | $399B | **$244** |
| Bull | 25% | $883B | **$539** |

Probability-weighted (~25/50/25): **~$292/share** — roughly **35% below the current price**.

Two independent cross-checks:
- The automated DCF tool, using the trailing 3-year FCF CAGR of **29.3% compounded for ten straight years** (a wildly generous input) with 10% WACC / 3% terminal, returns $681.5B of intrinsic value. Market cap is $734.6B. **Even the most aggressive mechanical DCF available says AMD is overvalued.**
- Analyst targets from early November 2026 clustered at $540–$675 against a $484 price — the Street is underwriting the bull case in full, which means no cushion exists if the ramp slips one quarter.

**What the price requires:** ~25%+ FCF growth sustained for a full decade with no cyclical interruption, no Nvidia price response, and no customer insourcing. Deliver all of that and you earn ~20%. Miss by two years and you lose 40%+. That is the wrong asymmetry.

---

## 4. Management Quality — **8/10 operating, 5/10 capital allocation**

**Lisa Su** is one of the finest operators in semiconductors, full stop, and the board's decision to retain her is the single best thing about this equity. Culture is engineering-driven and execution-obsessed. Insiders hold well under 1% — normal for a $700B company but not an owner-operator signature.

**Capital allocation is the weak link:**
- **No dividend** (appropriate for a growth company) and modest buybacks: $1.32B in FY2025, $1.59B in FY2024, $1.41B in FY2023. Repurchasing stock at 50–170x earnings is not value-accretive — it is the mechanical offset of SBC dilution, nothing more.
- **The Xilinx deal** ($49B in stock, closed 2022) was strategically coherent (FPGA + embedded + adaptable SoC) but financially unproven: four years later, $41.8B of goodwill and intangibles remain against a segment generating roughly $4–5B of revenue. Through 2023–2024 that capital earned a low-single-digit return. Judged on ROIC, it was a large, expensive bet funded with equity at a favorable moment — good timing, mediocre returns.
- **Customer equity/warrant economics** in the OpenAI arrangement are a form of paying for revenue. Defensible strategically; not something a wide-moat business must do.
- Balance sheet is conservatively managed — net cash in a capex-heavy cycle is exactly right.

**Net:** trust the operator, discount the allocator, and note that the current buyback program is buying the most expensive shares in the company's history.

---

## 5. Investment Verdict: **SELL / AVOID**

This is a **good business at a very bad price** — which is not a buy, and not a Hold if you own it at a cost basis anywhere near current levels.

- Moat: **Narrow**, and the AI half of the story does not yet meet the moat test.
- ROIC has been below WACC for four consecutive years (5.47% vs ~10%).
- Financial quality is solid (7/10) but cyclical, and TTM earnings are flattered by non-operating items.
- Intrinsic value **~$290** (range $140–$539); price **$449**, a **~55% premium** to my base case.
- Required entry for a 25–30% margin of safety: **$200–$215** — remarkably, roughly where the stock traded in February 2026 before the AI re-rating.

I may well be wrong about the size and duration of the AI data-center cycle; AMD's revenue is compounding at 50% and that deserves respect. But a great business bought at 34x tangible book and a 1.5% FCF yield is a speculation on the terminal value, not an investment in it. **Wait for the price to meet the value.**

---

## 6. Key Risks to the Value Thesis (i.e., what would make me wrong — in both directions)

**Risks that could make the stock worth even less than my $290:**
1. **Nvidia's cadence and CUDA.** If Nvidia keeps a one-generation lead and full-stack software lock, AMD stays a price-taking second source indefinitely.
2. **Custom silicon insourcing.** Google TPU, Amazon Trainium, Broadcom/Marvell ASICs. If hyperscalers conclude merchant GPUs are a bad deal, AMD's TAM shrinks structurally — this hits AMD harder than Nvidia because AMD has no software moat to fall back on.
3. **Customer concentration.** A handful of hyperscalers plus one anchor AI customer drive the growth. One delayed deployment stalls the model.
4. **Cyclicality.** PC and gaming are mature and inventory is building (165 days). 2023's −3.9% revenue year is the template.
5. **Taiwan/TSMC geopolitical exposure** — an unhedgeable tail risk for a fabless leader.
6. **Multiple compression alone.** Returning to the peer-median 38x on FY2026 EPS of $8.03 implies ~$305 — a 32% decline with zero operational deterioration.

**Risks that could prove me too conservative:**
1. **FY2026 FCF may materially exceed my $10B normalized base.** If Q4's guided $17.0B quarter carries high incremental margins and working capital reverses, TTM FCF could approach $15B+ — which would lift my base case toward $350. Still not $449, but the gap narrows.
2. **Genuine AI share gains** — MI450 wins beyond OpenAI, plus EPYC server share crossing 40%, could sustain 25%+ growth into 2030. That is the $539 bull case, and it requires near-perfect execution.
3. **Intel's continued weakness** in server CPU is a durable, free tailwind I may be underweighting.

**Monitoring triggers that would change my rating:** a price below ~$240 (my base intrinsic value) on unchanged fundamentals → Hold; below ~$200 → Buy. Conversely, evidence that ROCm has become a genuine second ecosystem with hyperscaler-standard adoption would widen the moat rating and justify a higher terminal value.

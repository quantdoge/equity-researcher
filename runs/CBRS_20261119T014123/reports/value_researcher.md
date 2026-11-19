# Value Researcher

- Symbol: CBRS
- Elapsed: 46.1s

---
I have enough to complete the analysis. One important correction surfaced: the "GAAP gross margin" of ~20% versus management's "core" gross margin of ~41% — a 21-point gap that is central to the thesis.

---

# Cerebras Systems (CBRS) — Value Investment Analysis

**Price (Nov 18, 2026): $94.15 | Market cap ≈ $22.5B (238.9M diluted sh.) | Net cash ≈ $5.9B | EV ≈ $16.6B**
*Stock is –70% from its $311 IPO-day close (May 14, 2026) and –55% in the last 30 days. IPO'd just six months ago.*

---

## 1. Business Quality Assessment — Moat Rating: **Narrow at best; today, None proven**

Cerebras builds the Wafer-Scale Engine (WSE-3), a single chip spanning an entire silicon wafer, avoiding the chip-to-chip interconnect bottleneck that constrains GPU clusters. In raw memory bandwidth and inference latency, this is genuine, differentiated engineering. That earns the technology my respect. It does not earn the business a moat.

Buffett's moat test is not "is the product clever?" It is **"can they price without losing the customer?"** The income statement answers that unambiguously:

| Period | GAAP Gross Margin |
|---|---|
| FY2023 | 33.5% |
| FY2024 | 42.3% |
| FY2025 | 39.0% |
| Q1 2026 | 44.6% |
| Q2 2026 | **14.2%** |
| Q3 2026 | **19.9%** |

A semiconductor company with pricing power earns 50–65% gross margins (NVIDIA ~75%, AMD ~50%). Cerebras earns **20%**. That is the profile of a hardware integrator buying revenue, not a moated franchise. Management reports a "core gross margin" of ~41% — the 21-point gap to GAAP is *excluded real cost*, and the exclusion is growing.

**Moat scorecard:**
- **Switching costs — benefit NVIDIA, not Cerebras.** CUDA is the industry's deepest moat; Cerebras must pay to overcome it. A PyTorch-native SDK is a feature, not a lock-in.
- **Cost advantage — none.** 708 employees against NVIDIA's ~30,000. Subscale in a scale-driven industry.
- **Intangibles — narrow.** Real patents, real first-mover in wafer-scale, but no brand pricing power at 20% margins.
- **Network effects — none.**
- **Vertical integration into cloud is moat-destroying, not moat-building.** Cloud services were $142M in Q3 (+265% YoY). Renting compute is capital-intensive, low-ROIC, and pits them against AWS, Azure, GCP, and CoreWeave — entities with far cheaper cost of capital.

**Verdict: the moat has, if anything, *narrowed* over the last five years as the mix shifted from chips to low-margin cloud.** That is the opposite of what I require.

---

## 2. Financial Quality Score: **3 / 10**

| Metric | Reading | Assessment |
|---|---|---|
| Revenue growth (FY25) | +75.7% (from +269%) | Strong but sharply decelerating |
| Revenue TTM | ~$756M | Real, and Q3 core +103% YoY |
| Operating margin FY25 | –28.5% | Q2'26: –265%; Q3'26: –106% |
| TTM operating income | **≈ –$750M** | Deepening, not narrowing |
| Owner earnings FY25 | **–$110M** | Negative |
| FCF, 4 years | –175, –86, **+429**, –393 ($M) | The one positive year was a $443M **working-capital inflow** (customer prepayments), not operations |
| FCF conversion | Not meaningful (negative) | Fails outright |
| Net cash (Q3'26) | ~$5.9B ($7.36B cash vs $1.45B debt) | **Genuine strength** |
| Equity | $9.16B (from **–$579M** pre-IPO) | Fortified by IPO proceeds only |
| Cash burn Q3'26 | **–$1.25B in one quarter** | ~$2.2B/yr capex into owned capacity |

**Two quality-of-earnings flags that must be stated plainly:**

1. **FY2025's "+$238M net income" is an accounting artifact.** Operating income was **–$145M**, yet EBIT is reported at **+$245M** — implying ~$390M of *non-operating* gains (warrant/derivative revaluation). Operating cash flow was **negative**. Presenting a GAAP profit on a cash-burning year is precisely the kind of presentation I discount heavily.

2. **Negative tangible book pre-IPO (–$579M) was masked by preferred securities in liabilities.** The $9B equity today exists because investors wrote a check, not because the business earned it.

The balance sheet is the single bright spot: ~$5.9B net cash funds roughly 3–4 years of current burn. But a fortress balance sheet is not a business — it is a runway.

---

## 3. Valuation Analysis — **Price still requires perfection**

The trailing-FCF DCF tool returns a **negative intrinsic value** (–$4.9B), which is the honest answer: a discounted cash flow cannot be computed on negative owner earnings with no defined inflection point. So I reverse-engineer what the price demands.

At **$16.6B EV** (giving full credit for the $5.9B cash pile), against **$224M of TTM gross profit** (74x EV/gross profit) and **–$750M TTM operating income**:

**Reverse DCF — what must be true to earn a 10% return from here:**
To justify $16.6B, Cerebras needs roughly **$1.2–1.4B of sustainable free cash flow** within ~5 years. At a generous 60% FCF conversion, that requires ~**$2.0–2.3B of NOPAT** → ~**$2.6–2.9B of EBIT**. On a very optimistic $6B revenue base, that is a **~45% operating margin** — a margin no hardware or cloud-compute business in history has sustained, and one this company is currently ~150 points away from.

**Bull case, quantified honestly:** Revenue $800M → $3.0B by 2031 (30% CAGR), gross margin recovers to 45%, opex discipline delivers 20% operating margin → $474M NOPAT → ~$285M FCF → 25x terminal = ~$7.1B, PV ≈ **$4.6B total**. That is **less than a third of today's EV** — and the bull case itself is generous.

**Intrinsic value estimate: $30–40/share** (roughly $7–10B equity value), with a wide band. Even my optimistic scenario leaves the stock ~60% above fair value. There is **no margin of safety here — there is a margin of optimism.** As I have said many times: a wonderful business at a fair price is far better than a fair business at a wonderful price. This is neither.

---

## 4. Management Quality Assessment — **Mixed, with candor concerns**

**Positives:** Andrew Feldman is a founder-CEO with a genuine technical vision and an owner-operator's long horizon. Retention of the founder through IPO is a real asset.

**Concerns:**
- **Quality of disclosure.** The "core" vs. GAAP gross margin gap (41% vs. 20%) is extraordinarily wide and widening. The FY2025 GAAP profit was presented while operating cash flow was negative. I weight what management *emphasizes* as heavily as what it reports.
- **Capital allocation.** FY2025 saw a **$38M share buyback** at a cash-burning, pre-profit company — an odd use of capital. Meanwhile $2.2B/yr of capex is converting a capital-light chip designer into a capital-heavy landlord.
- **IPO timing.** Coming public in May 2026 into peak AI enthusiasm, with the stock now –70%, is a lesson in the cost of selling equity at inflated prices — good for the company, not for the shareholders who bought.
- **Not verifiable:** insider ownership and lock-up structure were not retrievable from available filings (no 10-K on file; the 10-Q excerpt returned only an exhibit). I flag this as a gap rather than assume favorably.

---

## 5. Investment Verdict: **SELL / AVOID**

CBRS fails every one of my core tests:

| Test | Result |
|---|---|
| Within circle of competence | Marginal — technology is understandable; durability is not |
| Durable economic moat | ✗ Marginal product, 20% gross margin, no pricing power |
| Consistent ROIC > WACC | ✗ Operating income negative 4 years running |
| Positive owner earnings | ✗ –$110M FY25; FCF negative 3 of 4 years |
| Margin of safety | ✗ Price ~2.5–3x even an optimistic intrinsic value |
| Management candor | ⚠️ Core-vs-GAAP gap, non-operating "profit" |

**Recommendation: Sell / Avoid.** For existing holders, the fortress balance sheet ($5.9B net cash) is the only reason this is not a Strong Sell — it provides time, not value. The stock could easily trade back to $30–40 and still leave the company well-funded.

---

## 6. Key Risks to the Value Thesis

**Risks that make the price too LOW (the honest bull case):**
1. **A mega-contract could re-rate the stock overnight.** Sovereign AI deals (G42/MBZUAI) are lumpy; a single $1B+ order compresses the multiple.
2. **Inference is the growth market**, and Cerebras' latency advantage is most valuable there. If AI demand shifts decisively from training to inference, WSE-3's architectural edge could translate into real pricing power.
3. **The cash pile ($5.9B) and post-IPO equity ($9.16B)** provide a multi-year runway that most high-growth peers lack.

**Risks that make the price too HIGH (my primary concern):**
1. **Margin structure may be structurally broken.** If cloud-heavy mix means 20% GAAP gross margins are the new normal, the terminal economics never support a $16B EV.
2. **Customer concentration and geopolitics.** The flagship disclosed purchase order runs through MBZUAI (UAE), with the amendment explicitly navigating US export controls and a delivery location outside the UAE. A single regulatory decision on advanced AI compute exports to the Middle East could remove a large share of revenue.
3. **NVIDIA.** Jensen's CUDA ecosystem, annual cadence, and balance sheet are an existential competitive threat to a 708-person challenger.
4. **Burn rate.** –$1.25B of cash in one quarter against $7.4B means roughly 3–4 years at current spend — and they have begun borrowing.
5. **Six months of public history.** No evidence of through-cycle behavior, no recession test, no proof the moat exists.

---

**Bottom line:** Cerebras is a real technology company run by a real founder, and it passes the "does it matter?" test. It fails the "is it a *business*?" test — 20% gross margins after a decade of development, negative owner earnings, and a share price that still discounts a future I cannot underwrite with any confidence. Great technology is frequently a poor investment when purchased at a price that assumes no competition and no friction. **I will watch this one, and I will not own it at $94.** My buy point would require evidence of sustained gross margins above 40% *plus* a price near $35–40.

*Data gaps: no 10-K on file (recent IPO); insider ownership and lock-up terms unavailable; peer comps reflect a distorted median P/E (30.8x) against CBRS's non-meaningful multiple; the vendor's headline P/E (229x) and market cap ($20.4B) were computed on stale or pre-IPO share counts and should be disregarded in favor of my figures above.*

# Sector Researcher

- Symbol: CBRS
- Elapsed: 51.7s

---
I have sufficient data. Writing the brief now.

---

# Sector Brief: Cerebras Systems (CBRS)
### AI Accelerators / Semiconductors — Prepared for Investment Memo

---

## 1. Sector Overview

Cerebras competes in the **AI accelerator / merchant silicon** market — the fastest-growing sub-segment of the $1.5T global semiconductor industry (WSTS: ~$1.51T in 2026, +27% forecast for 2027 to ~$1.9T). The AI accelerator TAM was **$151B in 2025 and is forecast to reach $443B by 2030 (~24% CAGR)**, with custom ASICs growing faster still (~43% CAGR) and projected to surpass GPU unit shipments by 2028. Critically, the demand centre of gravity is shifting from **training to inference**: the inference market was $103.7B in 2025 and is forecast to reach $312.6B by 2031, and inference rewards throughput-per-watt and memory bandwidth rather than raw FLOPS — precisely Cerebras's wafer-scale thesis. Structure is **highly concentrated**: NVIDIA holds ~58% of accelerator revenue (and ~85–90% of merchant GPU share), with TSMC as an effective sole-source foundry and SK Hynix/Samsung/Micron controlling HBM supply. Barriers to entry are extreme — full-wafer 5nm fabrication, custom packaging and power delivery, and an 8+ year software/compiler stack (Cerebras has 708 employees and ~$5.6B of IPO proceeds against incumbents spending that on capex per quarter).

---

## 2. Key Tailwinds

- **Hyperscaler capex is still accelerating, not decelerating.** Consensus 2026 capex for the five largest US hyperscalers sits at **~$844B, up 81% YoY**. This is the single dominant demand driver and it remains in expansion, not harvest.
- **Inference inflection favours non-GPU architectures.** As workloads shift from training to serving, the buying criteria move to latency and tokens-per-dollar-per-watt. Wafer-scale integration (44GB on-chip SRAM, no off-chip memory bottleneck) is architecturally advantaged for large-model inference — Cerebras's cloud revenue nearly quadrupled YoY in Q3 2026.
- **Custom ASIC / merchant-silicon share gains vs. NVIDIA.** ASIC shipments are projected to triple by 2027 vs. 2024, and Cerebras has converted this into landmark wins: an **OpenAI contract reported at $20B+**, an AWS agreement, and a Microsoft cloud deal — taking contracted backlog/RPO to **~$24.6–26.1B, roughly 30x forward revenue**.

---

## 3. Key Headwinds

- **Customer concentration remains acute, and diversification is expensive.** FY2025 revenue was **86% from two Abu Dhabi entities** (MBZUAI and G42). Q3 2026 improved (MBZUAI 38%, OpenAI 34%, G42 7%), but the new hyperscaler/cloud business is *lower margin* — see the gross margin collapse below.
- **Supply chain is single-point-of-failure and buyer power is extreme.** TSMC sole-sources the wafer-scale engine; HBM is a three-supplier oligopoly; and buyers are a handful of hyperscalers who routinely dual-source and design in-house (TPU, Trainium, MTIA). This caps Cerebras's pricing power permanently.
- **The AI capex cycle is entering its "show-me" phase.** CBRS has fallen **~72% from its $386 IPO-day peak** (to $108.72) *despite* record quarterly revenue and a raised outlook — evidence that the market is now de-rating AI infrastructure names on capex-ROI doubts rather than rewarding growth. Beta is 1.85; expect continued violent volatility.

---

## 4. Peer Comparison Table

*Latest reported fiscal year; margins are annual.*

| Company | Mkt Cap | Revenue | YoY Rev Growth | 3-Yr Rev CAGR | Gross Margin | Operating Margin | EV/Sales (trailing) |
|---|---|---|---|---|---|---|---|
| **CBRS** | $24.6B | $0.51B | **+75.7%** | **174.6%** | **39.0%** | **−28.5%** | **48.3x** (~29x annualised) |
| NVDA | $3,924.7B | $215.9B | +65.5% | 100.1% | 71.1% | +60.4% | 18.2x |
| TSM | $2,068.0B | n/a | n/a | n/a | n/a | n/a | n/a |
| AVGO | $1,656.5B | $63.9B | +23.9% | 24.4% | 67.8% | +39.9% | 25.9x |
| MU | $880.6B | n/a | n/a | n/a | n/a | n/a | n/a |
| AMD | $875.9B | $34.6B | +34.3% | 13.6% | 49.5% | +10.7% | 25.3x |
| MRVL | n/a | $8.2B | +42.1% | 11.5% | 51.0% | +16.3% | n/a |
| **Peer median (NVDA/AVGO/AMD/MRVL)** | — | — | **+38.2%** | 18.0% | **59.4%** | **+28.1%** | ~25.6x |

**Read-across:**
- **Growth: clear #1.** CBRS's +75.7% beats the peer median (+38.2%) by ~2x, and its 3-yr 174.6% CAGR is the highest in the group. No peer is growing faster at the top line.
- **Margins: clear last.** Gross margin of 39.0% is **20pts below the peer median**, and operating margin of −28.5% is **57pts below**. This is partly structural (Cerebras sells complete rack-scale systems and cloud capacity, not chips — COGS includes memory, networking and power) but the trend is the problem: **quarterly gross margin fell from 44.6% (Q1'26) to 14.2% (Q2'26) to 20.0% (Q3'26)** — 9-month 2026 GM of just 26.3%. Growth is being bought with margin.
- **Valuation: still at a premium.** At ~29x annualised Q3 revenue versus a ~25x peer median, CBRS trades in line-to-above peers while earning a fraction of their margins. The de-rating has compressed the multiple but not eliminated the premium.

---

## 5. Target Company's Competitive Position: **AVERAGE** (differentiated technology, sub-scale economics)

**Why not strong:** Cerebras has genuinely unique IP (the only commercial wafer-scale engine) and the best growth rate in its peer set, backed by a ~$25B contracted backlog that de-risks revenue for years. That is a real, defensible niche.

**Why not weak:** It is a $0.5B-revenue company competing against a $216B-revenue incumbent that spends more on R&D annually than Cerebras's entire lifetime funding. It has **negative operating margins (−28.5%)**, a **gross margin 20pts below peers**, **86% historical customer concentration**, single-source foundry dependency, and — most concerning — **deteriorating unit economics as it scales** (Q3'26 GM 20.0% vs 44.6% in Q1'26). Cerebras is winning contracts by being the differentiated alternative, but it is not yet demonstrating it can convert that differentiation into peer-like profitability.

**Verdict:** A credible #3/#4 architectural challenger with best-in-class growth and a fortress backlog, but structurally inferior margins, subscale, and heavily dependent on a concentrated set of counterparties. **Average overall — strong on technology and demand capture, weak on profitability and durability.**

---

## 6. Sector Rating: **ATTRACTIVE**

**Rationale:** On fundamentals the AI accelerator sector is the most attractive growth pool in public equities — a $151B→$443B TAM (~24% CAGR), hyperscaler capex up 81% in 2026, an inference mix shift that structurally expands the addressable market beyond NVIDIA's CUDA moat, and custom ASIC growing at ~43% CAGR. The sector is in **late-stage hypergrowth (cycle year ~4)**, not maturity.

**Two important caveats for the memo:**
1. **Attractive sector ≠ attractive stock.** The cycle is late enough that the market has begun punishing execution risk — CBRS fell 72% from peak on *record* results. Volatility, not demand, is the binding constraint.
2. **Cycle position is a risk, not a comfort.** Capacity is being added aggressively across memory and packaging, hyperscaler capex is being debt-financed in places, and depreciation cycles are shortening. A capex digestion phase in 2027–28 is the key sector-level downside scenario, and Cerebras — subscale, loss-making, high-beta (1.85) — would be among the most exposed.

---

*Data gaps: FMP's sector-aggregate endpoint returned corrupted output (company_count=1, mismatched period ends), so sector benchmarking was reconstructed from individual peer financials. TSM and MU growth/margin data were not retrieved within budget; MRVL market cap unavailable. Q3'26 D&A reported as zero (likely a data artifact), so EBITDA-based comparisons were avoided.*

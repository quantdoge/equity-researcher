# value_researcher

_2026-08-22T07:43:28+00:00_

# AMD (Advanced Micro Devices, Inc.) — Comprehensive Buffett-Style Value Investment Analysis

*Data as of August 2026. All figures traceable to FMP endpoints or disclosed web sources.*

---

## 1. Business Quality Assessment & Economic Moat

**Moat Rating: None**

AMD operates two segments—Computing & Graphics (CPUs, GPUs for PCs) and Enterprise, Embedded & Semi-Custom (server processors, SoCs, game-console silicon). The business is technologically competent, but a durable moat requires pricing power, switching costs, or efficient scale that produces **ROIC consistently above the cost of capital**. AMD fails that test.

**Evidence:**
- **ROIC vs. WACC**: FY2025 ROIC was **5.40%**; FY2024 was **2.49%**; FY2023 was **0.65%** (*statements/key-metrics*). With a beta of **2.489** (*company/profile-symbol*), AMD’s cost of equity is extremely high—conservatively 15–18%+. Even a blended WACC of 10–12% dwarfs these returns. A business earning 5.4% on capital while costing double-digit percent to finance is **destroying economic value**, not compounding it.
- **Gross Margin / Pricing Power**: TTM gross margin is **53.2%** (*statements/metrics-ratios-ttm*). This is decent but below NVIDIA’s ~74% (*web search: Stock Rover*) and Qualcomm’s ~55% (*web search: AlphaQuery*). AMD’s gains in data center (EPYC) and AI accelerators (MI300) have largely come from undercutting Intel and NVIDIA on price/performance, not from brand premium.
- **Switching Costs & Network Effects**: Negligible. NVIDIA’s CUDA software ecosystem creates massive lock-in for AI workloads. AMD’s ROCm is a distant alternative. In x86, Intel’s installed base remains vast. Console wins (Xbox/PlayStation) are low-margin, non-recurring design contracts.
- **R&D Intensity**: R&D/revenue was **23.4%** in FY2025 and **25.0%** in FY2024 (*statements/key-metrics*). This is not a moat; it is the cost of staying alive in a race against better-capitalized rivals.

**Moat Trend**: **Narrowing relatively**. AMD gained share while Intel stumbled on process technology. As Intel executes its IDM 2.0 recovery and NVIDIA vertically integrates (Grace CPUs, NVLink ecosystems), AMD lacks a durable defense.

---

## 2. Financial Quality Score: 4 / 10

AMD’s financials are a study in contrasts: a fortress balance sheet paired with dismal capital efficiency.

| Metric | Value | Source |
|---|---|---|
| **Current Ratio** | 2.61x | *statements/metrics-ratios-ttm* |
| **Debt/Equity** | 0.064x | *statements/metrics-ratios-ttm* |
| **Interest Coverage** | 44.1x | *statements/metrics-ratios-ttm* |
| **Altman Z-Score** | 27.78 | *statements/financial-scores* |
| **Piotroski F-Score** | 8 | *statements/financial-scores* |
| **Net Debt/EBITDA** | –0.15 (net cash) | *statements/key-metrics FY2025* |
| **ROE** | 6.88% (FY2025) | *statements/key-metrics* |
| **ROIC** | 5.40% (FY2025) | *statements/key-metrics* |
| **Gross Margin** | 53.2% (TTM) | *statements/metrics-ratios-ttm* |
| **Operating Margin** | 15.7% (TTM) | *statements/metrics-ratios-ttm* |
| **Net Margin** | 15.6% (TTM) | *statements/metrics-ratios-ttm* |
| **FCF Yield** | 1.93% (FY2025) | *statements/key-metrics* |
| **Earnings Yield** | 1.24% (FY2025) | *statements/key-metrics* |

**Balance Sheet: Excellent (9/10)** — Net cash, low leverage, pristine short-term liquidity, and a Piotroski score of 8 indicate no financial distress.

**Profitability & Capital Efficiency: Poor (2/10)** — ROIC of 5.4% is unacceptable for a semiconductor company. FCF yield is below 2%, meaning the business returns very little cash to owners relative to its $771 billion market cap. Growth is lumpy: FY2023 revenue fell –3.9% and operating income collapsed –68.3%, only to rebound sharply in FY2024–2025 (*statements/financial-statement-growth*). This cyclicality is the opposite of the predictable, annuity-like cash flows Buffett demands.

**Blended Score: 4 / 10**

---

## 3. Valuation vs. Intrinsic Value

| Valuation Approach | Estimate | Source |
|---|---|---|
| **Current Price** | $473.25 | *company/profile-symbol; discountedCashFlow/dcf-advanced* |
| **DCF (Advanced)** | $48.35 | *discountedCashFlow/dcf-advanced* |
| **DCF (Levered)** | $47.90 | *discountedCashFlow/dcf-levered* |
| **P/E TTM** | 120.1x | *statements/metrics-ratios-ttm* |
| **EV/EBITDA TTM** | 71.9x | *statements/metrics-ratios-ttm* |
| **P/B TTM** | 11.5x | *statements/metrics-ratios-ttm* |
| **P/S TTM** | 18.7x | *statements/metrics-ratios-ttm* |

**Intrinsic Value Gap**: The stock trades at roughly **10×** FMP’s DCF estimate. Even if one argues the model is conservative by 50%, the stock would still be **5×** intrinsic value. There is **no margin of safety**; the margin is deeply negative.

**What the Market is Pricing In**: A P/E of 120x and EV/EBITDA of 72x imply the market expects AMD to sustain 30%+ revenue growth and significant margin expansion for most of a decade. Given NVIDIA’s software moat, Intel’s manufacturing recovery, and the threat of custom silicon from hyperscalers (Amazon, Google, Microsoft), those expectations are heroic.

---

## 4. Owner Earnings Analysis

FMP returned **quarterly** owner-earnings data (*statements/owner-earnings*), not annual aggregates. The trajectory is:

| Quarter | Owner Earnings |
|---|---|
| Q1 2024 | $389M |
| Q2 2024 | $480M |
| Q3 2024 | $584M |
| Q4 2024 | $1,219M |
| Q1 2025 | $890M |
| Q2 2025 | $1,882M |
| Q3 2025 | $2,102M |
| Q4 2025 | $2,594M |

**Qualitative Trend**: Owner earnings have exploded, particularly from Q4 2024 onward, coinciding with the MI300 data-center accelerator ramp. This is genuine operational improvement.

**Explicit Gap**: To compute **annual owner earnings**, **annual owner-earnings growth rates**, and **normalized owner-earnings margins**, a **quant_engineer** must aggregate these quarterly values (summing maintenance capex and owners earnings across quarters) and compare to annual revenue. I am not computing these myself per instructions.

Even without precise annualization, the absolute level of owner earnings (~$2.6B in the most recent quarter) is tiny relative to a $771 billion market cap. On an annualized run-rate basis, the stock trades at roughly **75× owner earnings**—an extraordinary multiple for a business with no moat.

---

## 5. Key Value Metrics vs. 5-Year History & Peers

### AMD Historical Trend (Key Metrics)
| Fiscal Year | ROIC | ROE | FCF Yield | Earnings Yield | EV/EBITDA |
|---|---|---|---|---|---|
| 2025 | 5.40% | 6.88% | 1.93% | 1.24% | 47.8x |
| 2024 | 2.49% | 2.85% | 1.19% | 0.81% | 38.3x |
| 2023 | 0.65% | 1.53% | 0.47% | 0.36% | 57.1x |

*Source: statements/key-metrics*

The trend shows improving but still abysmal capital returns. Multiples have expanded faster than fundamentals.

### Peer Comparison
| Metric | AMD | NVIDIA | Qualcomm | Intel |
|---|---|---|---|---|
| **P/E (TTM)** | 120.1x | ~49x (falling) | ~21.3x | 148.6x (or neg EPS) |
| **EV/EBITDA** | 71.9x | 31.4x (FY2026) | Not available | 267.8x (aberrational) |
| **Gross Margin** | 53.2% | ~74.2% | ~55.4% | ~38.6% |
| **Operating Margin** | 15.7% | ~64.0% | ~23.3% | Not available |
| **ROIC** | 5.4% | 62.9% | Not available | 5.22% |
| **Debt/Equity** | 0.064 | Near zero | Not available | 0.58 |

*Sources: AMD data from FMP statements endpoints. NVIDIA ROIC/EV/EBITDA from statements/key-metrics (NVDA). NVIDIA gross/operating margin from web search (Stock Rover, Seeking Alpha). QCOM metrics from web search (Trading Economics, AlphaQuery, ChartMill). INTC metrics from web search (Macrotrends, GuruFocus).*

**Peer Verdict**: AMD is the worst of both worlds—lower profitability than QCOM and NVDA, yet a higher valuation multiple than all but the most distressed Intel (which has aberrational multiples due to collapsed earnings). NVIDIA justifies a premium with 63%+ ROIC; AMD does not.

*Note: Detailed FMP peer data for INTC and QCOM were unavailable due to tool-call limits; web-sourced figures are approximate and directional only.*

---

## 6. Margin of Safety Assessment

**Margin of Safety: None. Negative.**

Buffett requires a 20–30% discount to intrinsic value. AMD trades at a **~900% premium** to FMP’s DCF value. A 50% price decline would still leave the stock at ~$236—roughly 5× the DCF estimate and 60× earnings. The concept of a margin of safety does not apply here; the security is priced for a fantasy.

A defensible entry point would require either:
1. A share price below **$70–$100** (where it might approach 15–20× normalized owner earnings and a modest premium to tangible book), or
2. A fundamental transformation that produces **sustained ROIC > 15%** for multiple years, proving the emergence of a real moat.

Neither condition is met today.

---

## 7. Management Quality Assessment

**CEO**: Lisa T. Su (*company/profile-symbol*). Dr. Su has executed a remarkable operational turnaround, restoring AMD’s technical credibility against Intel.

**Grades:**
- **Operational Skill**: A. She rescued AMD from near-bankruptcy and built competitive product lines.
- **Capital Allocation**: C+. 
  - **Stock-Based Compensation**: SBC/revenue was **4.7%** in FY2025 and **5.5%** in FY2024 (*statements/key-metrics*). At a $770B market cap, this is colossal dilution.
  - **Dividend**: **$0** (*statements/metrics-ratios-ttm*). No cash is returned to owners.
  - **M&A**: The Xilinx acquisition (2022) expanded the portfolio but left intangibles at **54.4%** of total assets in FY2025 (*statements/key-metrics*). High goodwill is fragile.
  - **Buybacks**: Not prominent in fetched data; with the stock at 120× earnings, any buyback would be value-destructive.

Dr. Su is honest and capable, but she is managing a **tough business** that requires perpetual, massive R&D reinvestment just to maintain position. As Buffett says, "When a management with a reputation for brilliance tackles a business with a reputation for bad economics, it is the reputation of the business that remains intact."

---

## 8. Durability of Competitive Advantage

**Durability: Fragile.**

AMD’s recent gains rest on:
1. Intel’s process stumbles (allowing EPYC share gains).
2. NVIDIA supply constraints (allowing MI300 sales).
3. TSMC’s manufacturing leadership (which AMD rides as a fabless designer).

None of these are durable:
- Intel is investing heavily to regain process parity.
- NVIDIA is expanding its software/hardware ecosystem and vertically integrating into CPUs.
- Hyperscalers are designing their own AI silicon (TPU, Trainium), bypassing merchant vendors.

Without a proprietary ecosystem, AMD’s advantage is transitory.

---

## 9. Investment Verdict: **STRONG SELL**

AMD is a **good company operationally but a terrible investment at this price**.

- **No economic moat**: ROIC < WACC, no pricing power, no switching costs.
- **Financial quality is mixed**: excellent balance sheet, terrible capital efficiency.
- **Valuation is speculative**: 10× FMP DCF, 120× earnings, 72× EV/EBITDA.
- **No margin of safety**: even a 70% decline would not create one.
- **Management is skilled but not enough to overcome the business economics and valuation**.

Buffett’s maxim applies: *"It's far better to buy a wonderful company at a fair price than a fair company at a wonderful price."* AMD is neither wonderful nor fairly priced.

---

## 10. Key Risks to the Value Thesis

1. **AI Accelerator Hypergrowth**: If MI300/MI350 captures 20–30% of AI training market share, revenue/earnings could inflect. Probability is low given NVIDIA’s CUDA moat.
2. **Intel Manufacturing Failure**: If Intel’s 18A process flops, AMD could entrench x86/server dominance for years.
3. **Custom Silicon Windfalls**: Mega-custom chip wins (Microsoft, Meta, Amazon) could spike revenue unpredictably.
4. **Bubble Momentum**: In a speculative frenzy, multiples can detach from fundamentals for years. Buffett does not play this game.
5. **DCF Model Assumptions**: FMP’s DCF may use conservative terminal growth/WACC. A custom DCF with aggressive inputs could raise intrinsic value, but bridging a 10× gap is nearly impossible without assuming AMD becomes the next NVIDIA.

**Bottom Line**: Avoid AMD at $473. Revisit only if the share price collapses to a level where normalized owner earnings can be purchased at a rational multiple, or if the company demonstrates sustained ROIC above 15% for multiple years. Until then, patience is the only prudent course.

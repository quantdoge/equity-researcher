# Value Researcher

- Symbol: CHTR
- Elapsed: 98.9s

---
I now have a coherent picture. One important note: the price/ratios feed I was given is internally inconsistent, so let me document what I resolved before the analysis.

**Data integrity note:** My `calculate_valuation_ratios`/profile feeds returned a $138.39 price against a stale 137.7M diluted share count (FY2025) → $19.1B market cap. The daily price history confirms $138.39 as the 13 Nov 2026 close (the earlier file was simply truncated at Feb 2026). With ~117M shares outstanding post-buybacks (Q3'26 weighted average 116.9M), the true market cap is ≈**$16.2B**, not $19.1B. All multiples below are recomputed on that basis. The `calculate_intrinsic_value_dcf` tool also mis-parsed my WACC input (treated 7.5 as 750%), so I built the DCF by hand.

---

# Charter Communications (CHTR) — Value Analysis
*Price $138.39 (13-Nov-2026) | Market cap ≈$16.2B | Est. net debt ≈$120–130B post-Cox | EV ≈$140B*

**The situation in one line:** Charter has just closed the $34.5B Cox merger and the Liberty Broadband roll-up, simultaneously took an ~$8.6B goodwill impairment (Q3'26 net loss of $2.4B, GAAP EPS –$20.50 vs. +$8.94 expected), and is losing broadband subscribers while cutting residential ARPU. The stock fell from $420 (mid-'25) to $102 (late-Oct '26) before rallying 35% to $138 on a $2B cost-cut plan. The equity is now priced as a melting ice cube.

## 1. Business Quality Assessment — Moat: NARROW and NARROWING

Cable's moat is genuine but local and physical: an owned HFC plant to ~59M passings, franchise/right-of-way advantages, high switching friction on a bundled triple-play, and efficient local scale (the classic "efficient scale" moat). But the 2026 evidence shows it is being breached:

| Evidence of moat erosion | Latest data |
|---|---|
| Internet subscribers | 29.39M, **–1.7% YoY**; –172k in Q2'26 |
| Residential revenue/customer | **$117.52 vs. $119.70, –1.8%** — *pricing power has inverted* |
| Penetration of passings | 53.4% vs. 55.7% (–2.3pts) |
| Customer relationships | 31.5M, –1.7% YoY |
| Revenue (ex-Cox) | –1.7% YoY |

Fixed-wireless access (T-Mobile/Verizon) has taken the low-end and fiber overbuilders (AT&T, Frontier) the high-end. When a monopolist's *revenue per customer falls*, the moat is narrowing — that is the single most important fact in this analysis. The one growth engine, Spectrum Mobile (12.5M lines, +15.5% YoY), is a wholesale-MVNO product with materially lower margins and no moat of its own.

**ROIC vs. WACC:** ROIC ≈11.3% (2022–2025, remarkably stable) against an estimated WACC of ~6.5–7%. The business still creates value — but ROIC is now pressured by a larger, lower-return asset base (Cox) and by declining EBITDA. Note this ROIC is flattered by $97.6B of goodwill and intangibles that management itself has now written down.

**Verdict: Narrow moat, actively narrowing.** This is a good local utility turning into a competitive pipe.

## 2. Financial Quality Score: **4 / 10**

| Metric | Value | Comment |
|---|---|---|
| Revenue (FY25 / Q2'26 pro forma) | $54.8B / –1.7% | Flat-to-declining; 6-yr CAGR only 3.0% |
| Gross margin / EBITDA margin | 46.3% / ~38.7% | Stable, but EBITDA –4.3% YoY in Q2'26 |
| Capex intensity | **21% of revenue** ($11.7B) | The core problem: enormous, semi-permanent network spend |
| FCF (FY25) | $4.42B (8% margin) | Q2'26 FCF only $969M, –$77M YoY |
| Owner earnings (NI + D&A – capex) | **$2.04B** | vs. $5.14B in 2022 — a 60% collapse in owner earnings |
| FCF / net income | 88% | Good conversion, but off a capex-heavy base |
| Net debt | $96.6B (FY25) → est. **$120–130B** | ~4.6x → ~4.8–5.0x EBITDA |
| Interest expense | $5.04B FY25; $1.34B in Q3'26 alone | ~24% of EBITDA consumed by interest |
| Goodwill | $97.6B, now **impaired ~$8.6B** | Management conceding asset value |

The score is dragged down almost entirely by the balance sheet and by capex. Leverage near 5x into a declining revenue base is the opposite of a margin of safety. Capex *can* be cut to ~$9–10B quickly if needed (it's partly discretionary), which is the equity's main escape hatch.

## 3. Valuation Analysis

**Current multiples (recomputed, $16.2B market cap):**
- EV/EBITDA ≈ **5.4x** (≈$140B EV / ~$26B pro forma EBITDA)
- EV/unlevered FCF ≈ **13x**
- **Equity FCF yield ≈ 30%+** (≈$5–6B FCF vs. $16.2B cap)
- P/E ≈ 3.8x (on depressed GAAP earnings); P/B ≈ 0.9x — but book is now post-impairment

**Scenario DCF (equity-level, 10% discount rate for leverage):**

| Scenario | Key assumptions | Equity value | Per share |
|---|---|---|---|
| **Bear (25%)** | EBITDA declines 5%/yr to ~$19B; capex cut to $9.5B; interest $6.5B; exit at 4.5x | ~$85B EV – $125B debt ≈ **$0** | **~$0–40** |
| **Base (50%)** | $2B synergies + Cox offset core erosion; EBITDA ~$25.5B in '28; capex $11.5B; FCF ~$6B; 6.5x exit | ~$41B | **~$330** |
| **Bull (25%)** | Broadband stabilizes, capex falls to $10B, FCF $8B, re-rates to 7.5x | ~$70B | **~$550** |

**Probability-weighted intrinsic value ≈ $230–240/share** vs. $138.39 today — a **~40% discount**, which clears my 20–30% margin-of-safety hurdle.

**Reverse DCF — what is the price implying?** At 5.4x EV/EBITDA, the market is capitalizing Charter as a permanently declining asset: it implies EBITDA falling roughly 5–6% per year forever, or that the ~$125B debt stack is refinanced at punitive rates. That is a *plausible* but not *certain* outcome. The gap between price and base-case value is the entire investment case — and the bear case is not a drawdown, it is a wipeout.

## 4. Management Quality — Mixed, leaning to "aggressive"

- **Chris Winfrey (CEO)** is operationally credible and candid ("we operate in a competitive environment across all of our products").
- **Capital allocation is the concern.** Share count fell from 183M (2021) to ~117M (–36%) — an excellent per-share record *while it worked*. But it was funded with debt, and in Q2'26 alone Charter bought 4.0M shares for $838M (**~$210/share**) *and* repurchased $1.2B of its own notes. Buying equity at $210 with 5x leverage, three months before the stock traded at $102, is not disciplined; it is balance-sheet-dependent financial engineering.
- **No dividend**, ever. **M&A:** the Cox deal at $34.5B and the Liberty Broadband roll-up are empire-building-adjacent, though the $2B cost-cut target is the right response. The $8.6B impairment immediately after closing is a poor look on deal pricing.
- No family/owner-operator stake of note; the controlling influence of John Malone'sLiberty complex has now been unwound.

**Verdict: competent operator, over-levered allocator.** Grade: C+.

## 5. Investment Verdict: **BUY — but speculative, small size only (≤2–3%)**

I want to be precise about why this is a Buy and why it is not a *good* business.

By my quality standards this fails: moat narrowing, pricing power gone, ROIC falling, and ~5x leverage. On quality alone I would pass. But my job is price versus value, and the price has detached from any reasonable non-apocalyptic valuation: **~$230 probability-weighted value against $138**, a 40% discount, with a ~30% equity FCF yield and an EV at 5.4x EBITDA

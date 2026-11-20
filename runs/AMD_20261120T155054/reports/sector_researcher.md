# Sector Researcher

- Symbol: AMD
- Elapsed: 59.2s

---
# SECTOR BRIEF — SEMICONDUCTORS (AMD)

**Data note:** AMD's sector is Technology; the peer list returned is super-sector-wide (AAPL, MSFT, ORCL…). I benchmark only against the true industry comparables (Semiconductors), which is the economically relevant set. The `get_sector_financials` endpoint returned corrupted aggregates (each row `company_count=1`, mixing fiscal periods from Jan–Oct; e.g. a $11.5B and a $478.8B revenue "quarter" in the same series) — discarded. All figures below are built bottom-up from individual filings. Latest data: Q3 CY2026; market data to 20-Nov-2026.

---

## 1. Sector Overview

Semiconductors are in the most extreme upcycle in the industry's history: WSTS puts the 2026 market at **~$1.51T, +90% YoY**, after H1 2026 revenue of **$702B (+102% YoY)**. Growth is not broad-based — it is a **memory/HBM supercycle**: IDC sees DRAM revenue at **$418.6B in 2026 (+177%)** against supply growth of only 16%, and J.P. Morgan estimates DRAM prices have risen **>400% from early 2024 to end-2026**. The AI accelerator pool (NVDA, AVGO custom silicon, AMD Instinct) is the second engine, with NVDA alone running at a **$463B annualised revenue run-rate** (Q ended 25-Oct-26: $115.8B, +103% YoY). Crucially, the sector has just shifted from a "growth" regime to a **growth-plus-geopolitics regime**: a 14–15% two-day drawdown in AMD (Hunterbrook short report on China exposure, 19-Nov), Taiwan's worst week since 1991, a US licensing regime that approved 879,000 NVDA/AMD chips for China in six months, a December congressional hearing, and the abrupt resignation of NVIDIA's Jensen Huang. Valuation dispersion is the tell — MU trades at ~8x trailing earnings, NVDA ~15x, AVGO ~40x, AMD ~96x — i.e. the market is already differentiating between cycle winners with visible cash flow and story stocks priced on 2027 optionality.

## 2. Key Tailwinds

- **Capex is being pulled, not pushed.** WSTS +90% to $1.51T in 2026 with all regions and product categories growing; AI server demand continues to outgrow supply (IDC). Hyperscaler orders are multi-year and contracted (AMD's Oracle Helios win alone is ~50,000 MI455X GPUs), which converts sector froth into revenue visibility.
- **Memory scarcity is a pricing tailwind that spills into logic.** DRAM supply +16% vs demand growth far higher; TrendForce sees DRAM prices holding through 2027 and the most acute constraint in Q4'26–Q2'27. Scarcity rents accrue to anyone with leading-edge or HBM-enabled content per box — AMD's Instinct rack-scale (72 GPUs + 18 EPYC Venice CPUs + Pensando NICs per Helios cabinet) maximises attach.
- **A credible second source is now a procurement requirement.** The inference shift favours price-performance and open stacks (ROCm, UALink), and hyperscalers are actively de-risking single-supplier dependence on NVDA — accentuated by the NVIDIA leadership vacuum. AMD's 2026 share-price gain (>250% per press coverage, vs NVDA's 51%) reflects that re-rating.

## 3. Key Headwinds

- **Peak-cycle arithmetic.** A +90% sector year off a +100%+ first half is, by construction, not repeatable; 2027 brings capacity additions into a market whose marginal buyer has been pre-buying against shortages. Any capex-digestion quarter compresses multiples far faster than estimates.
- **Memory cost inflation is a direct gross-margin tax on AMD.** AMD is fabless and must buy HBM/DRAM into a market where prices are up >400% since 2024. This is the structural reason AMD's gross margin is 53.7% versus NVDA's 74.8% — the scarce input's supplier (MU, SK hynix) captures the rent, not the assembler.
- **China export control and political risk.** A licensing regime with a December hearing plus a short-seller report on blacklisted-customer links erased AMD's entire post-earnings gain in one session. Sector-wide, this is a recurring, un-hedgeable discount-rate shock.

## 4. Peer Comparison Table

Latest reported quarter unless noted (CY/Q3-2026 for AMD, NVDA, AVGO; FY for MU, TSM, ASML).

| Company | Rev growth YoY | Gross margin | Op margin | Net margin | P/S (TTM) | P/E (TTM) | Position |
|---|---|---|---|---|---|---|---|
| **NVDA** | **+103.2%** (Q Oct-26) | 74.8% | 66.9% | 56.4% | 9.1x | **14.6x** | Share donor? No — still the standard |
| **MU** | **+256%** (FY Sep-26) | **80.7%** | **74.6%** | 63.8% | 5.3x | **8.3x** | Biggest share/rent gainer |
| **AVGO** | +64.3% (Q Aug-26) | 69.1% | 53.9% | 44.2% | 17.0x | 39.6x | Custom ASIC share gainer |
| **AMD** | +44.7% (Q Sep-26) | 53.9% | 21.2% | 18.1% | **16.1x** | **96.2x** | Share gainer, margin laggard |
| **TSM** | +31.6% (FY25, TWD) | 59.9% | 50.8% | 44.6% | n/a | n/a | Toll-taker, capacity-constrained |
| **ASML** | +15.6% (FY25, EUR) | 52.8% | 34.6% | 29.4% | n/a | n/a | Slowest grower; EUV monopoly |
| **Peer median** | **+64.3%** | **69.1%** | **53.9%** | 44.2% | — | — | — |

AMD TTM basis (four quarters to Sep-26): revenue $45.44B, gross margin 53.7%, operating margin 17.7%, net income $7.62B, market cap $733B.

**Read-across:** AMD is **below the peer median on growth (44.7% vs 64.3%) and below on both margin lines (53.9% vs 69.1% GM; 21.2% vs 53.9% OM) — it is the only name in the set that is both slower than median and less profitable than median, yet trades at the highest earnings multiple (96x vs 8–40x).** AMD's growth *is* accelerating (FY25 +34.3% → +50.1% in Q2'26 → +44.7% in Q3'26) and its margin trajectory is improving (FY25 OM 10.7% → 21.2%), but it is monetising the boom at roughly one-third of peer profitability. The dispersion says the market is paying AMD for 2027–28 share gains rather than current economics; NVDA and MU are being priced for cash flow.

## 5. Target Company's Competitive Position: **AVERAGE (improving)**

- **Supporting "average":** ~$45B TTM revenue against NVDA's $362B; operating margin 21% vs a 54% peer median; the shoulders of AMD's P&L sit under the memory-cost squeeze rather than on top of it. ROCm/CUDA remains an ecosystem gap that caps attach rates at the high end.
- **Improving toward strong:** AMD is the **only credible merchant second source** for rack-scale AI, and the 2026 evidence is concrete — Helios with MI455X, 6th-gen EPYC "Venice" in volume from Q3'26, and named deployments at OpenAI, Meta, Microsoft, Oracle and Anthropic. Q3'26 revenue of $13.38B is a record and up 44.7% YoY; margins have nearly doubled in six quarters. That is share gain, not just cycle.
- **The catch:** the stock has already banked much of it — +108% YTD 2026 and **-31% from its 6-Oct-2026 high of $649.42**. Competitive momentum is real; the equity's margin of safety is not.

## 6. Sector Rating: **ATTRACTIVE — but late-cycle**

Fundamentals (order books, pricing, unit demand) are unambiguously the best in the sector's history, and AMD's specific exposure to inference share gain and rack-scale attach is the right side of the trade. But the rating carries an explicit cycle warning: a +90% industry year with record margins and 400% input-cost inflation is a peak signature, memory tightness is forecast to break in 2027, and geopolitical/short-seller shocks are now hitting individual names by 15% in a session. **Position sizing and entry price matter more than sector direction from here — for AMD specifically, the sector is attractive while the stock's 96x trailing earnings already discounts the share gains I would otherwise argue for.**

# Value Researcher

- Symbol: SPCX
- Elapsed: 448.7s

---
# SPCX — SpaceX: Value Investment Analysis

**Current price:** $159.31 (Oct 21, 2026) | **Sector:** Industrials / Aerospace & Defense | **CEO:** Elon Musk | **IPO:** June 2026

> **Data caveats up front:** SPCX is a very recent listing (June 2026), so no 10-K was retrievable and dividend history is empty. The company profile reports a **~$2.1T market cap**, while price × reported diluted shares (2.926B) implies **~$466B**; the ~4.5x gap implies ~13.2B fully diluted shares. I present ratios on the reported share count and flag where fully diluted math changes conclusions. The automated DCF tool returned corrupted output (WACC entered as 950%), so all valuation work below is my own manual modeling.

---

## 1. Business Quality Assessment

**Moat rating: NARROW — and widening**

SpaceX is two businesses under one roof:

**Launch (Falcon 9 / Falcon Heavy / Starship):** The moat here is a genuine **cost advantage**, the most durable kind. Reusability reset the cost-per-kilogram to low Earth orbit versus expendable incumbents (Ariane, ULA) by roughly an order of magnitude, and the cadence — launch frequency — compounds that advantage. Falcon 9's flight heritage creates a self-reinforcing reliability record that customers pay for in insurance and schedule certainty. Regulatory launch slots (FAA), range access, and vertical integration in Merlin/Raptor engines and avionics add efficient-scale barriers. This is a real moat.

**Starlink (broadband + Starshield government):** The moat is a mix of **intangible assets** (spectrum licenses, orbital slots, government security clearances), **efficient scale** (the capital required to field thousands of satellites is prohibitive), and nascent **network effects** (more satellites → better latency/coverage → more subscribers → more capital for satellites). Starshield's government integration creates switching costs on the defense side.

**Where the moat is thinner:** consumer Starlink switching costs are low; terrestrial fiber/5G and Amazon's Kuiper are well-funded challengers; Chinese state-backed constellations are emerging. Technology risk on Starship is existential to the cost curve. Moat has widened over five years (from launch niche to broadband platform), but it is contestable — hence Narrow, not Wide. Critically, the moat has not yet translated into **ROIC above WACC**: ROIC was 1.18% in 2024 and **-4.03% in 2025**. That is the single most important fact in this analysis. A moated business should earn excess returns; SpaceX's moat is currently being paid for with enormous capital outlays, not harvested.

---

## 2. Financial Quality Score: **4 / 10**

| Metric | 2023 | 2024 | 2025 |
|---|---|---|---|
| Revenue ($B) | 10.39 | 14.02 | 18.67 |
| Revenue growth | — | +34.9% | +33.2% |
| Gross margin | 41.2% | 43.0% | 49.4% |
| Operating margin | -33.7% | +3.3% | **-13.9%** |
| Net income ($B) | -4.63 | +0.79 | -4.94 |
| EBITDA ($B) | -0.83 | 3.31 | 4.29 |
| Capex ($B) | 4.42 | 11.16 | 20.74 |
| Free cash flow ($B) | +0.11 | -5.39 | **-13.95** |
| Owner earnings ($B) | -6.41 | -6.55 | -18.97 |
| ROIC | n/a | 1.18% | -4.03% |

**The good:** Revenue growth is exceptional and consistent (34.1% two-year CAGR), and gross margin expanded ~820bps over two years — evidence of operating leverage and pricing power in Starlink. The balance sheet is adequately capitalized: $24.7B cash vs. $22.9B total debt, i.e. **~$1.9B net cash** at end-2025, though that flipped from $2.4B net debt in 2024 and was achieved while burning $14B of FCF. Goodwill and intangibles are $13.4B (~15% of assets) — worth watching for impairment risk. Accumulated deficit is -$37.0B.

**The bad:** Operating margin **deteriorated** in 2025 despite revenue growth — Starship development, Starlink build-out, and $1.95B of stock-based compensation overwhelmed the gross-margin gains. Free cash flow is deeply negative and worsening (-$0.1B → -$5.4B → -$14.0B), driven by capex that tripled in two years to $20.7B. Owner earnings are -$19.0B. FCF conversion is meaningless because there are no earnings to convert. **The 2024 net profit of $791M is an earnings-quality red flag**: EBIT that year was -$519M, meaning the positive net income came from non-operating items (interest income, gains), not operations. Excluding that fluke, SpaceX has never reported a profitable operating year in this dataset. Reported quarterly figures in 2026 suggest a sharp inflection — Q3 2026 revenue of ~$14.6B (versus FY2025's $18.7B total) and positive EPS of $0.35 — but the trajectory is too new to underwrite as durable, and capex is still running ahead of cash generation.

---

## 3. Valuation Analysis

**Intrinsic value estimate: ~$120B–$300B (base to aggressive bull)** vs. reported market cap of ~$466B (basic) to ~$2.1T (fully diluted).

Because trailing FCF is negative, a standard DCF is impossible; I modeled forward scenarios instead.

| Scenario | Revenue path | Net margin | FCF at horizon | Terminal multiple | PV of value |
|---|---|---|---|---|---|
| **Base** | $60B by 2030 (26% CAGR) | 15% | ~$8B | 22x | **~$120B** |
| **Bull** | $120B by 2032 (30% CAGR) | 20% | ~$20B | 25x | **~$305B** |
| **Hyper-bull** | $250B by 2035 | 25% | ~$55B | 25x | **~$655B** |

All discounted at 9.5% with 2.5% terminal growth. Even the **hyper-bull case — flawless execution for a decade — supports only ~$50/share on a 13.2B fully diluted count** (or ~$224 on 2.926B shares). The base case implies ~$9–$41/share. Today's $159.31 price requires outcomes beyond the hyper-bull case.

**Reverse DCF:** To justify ~$466B at a 9.5% discount rate and 2.5% terminal growth, SpaceX must reach roughly **$20B+ of sustainable FCF within about a decade**. To justify the profile's ~$2.1T, it needs **~$90B of annual FCF** — more than Apple or Microsoft generate today. That is not a reasonable underwriting assumption for a company currently burning $14B a year.

**Current multiples are not meaningful on earnings:** P/E -94.3x (loss-making), EV/EBITDA **108x**, P/B **11.3x**, FCF yield **-3.0%**. On fully diluted shares those multiples are ~4.5x higher still (P/B ~50x, EV/EBITDA ~490x). Peer median P/E is 38.6x — SpaceX's "premium" is not a premium, it is a different valuation regime. Sell-side targets ($176–$345, median ~$225) are momentum-and-narrative driven, not fundamentals-driven; they imply $2T–$4.5T market caps.

**Margin of safety: negative ~35% to ~85%.** There is no discount to intrinsic value — there is a large premium. A value investor cannot buy this at $159.31, and could not buy it even at half the price.

---

## 4. Management Quality Assessment

**Rating: Visionary operator, poor fit for a value-investor's capital-allocation test.**

**Strengths:** Musk is a founder-operator with enormous skin in the game and a demonstrated record of executing impossible engineering programs. The company's launch-cost leadership and Starlink's speed to market are direct evidence of exceptional operating capability. Ownership alignment is strong in the sense that the founder's wealth and identity are tied to the company.

**Concerns:** (1) **Governance** — a controlled/dual-class structure limits shareholder influence; board independence is questionable; key-man risk is extreme. (2) **Capital allocation** — capex of $20.7B against negative FCF reflects an empire-building appetite (Mars, Starship, satellite constellations, and reported related-party entanglements such as xAI) rather than disciplined return-on-capital management. Spending $1.1B on buybacks in 2025 while burning $14B of free cash flow is difficult to justify. (3) **Related-party risk** — Musk's other ventures create potential conflicts. (4) **No dividends**, and none expected. (5) Accumulated deficit of $37B means no distributable earnings for years. For Buffett-style underwriting — honest, rational, return-on-capital-focused stewardship — this is a mixed-to-poor score despite the operating brilliance.

---

## 5. Investment Verdict: **SELL / AVOID**

SpaceX is a genuinely great operating business with a real, widening cost and scale moat — arguably the most important aerospace franchise of the century. But greatness and valuation are separate questions. The company:

- has **never produced a sustainable operating profit** in the data provided,
- is burning **~$14B of free cash flow annually** with capex still accelerating,
- earns **negative ROIC** — the moat is not yet converting into excess returns,
- and trades at **~25x FY2025 sales** on basic shares (over 100x on the fully diluted count) with **negative FCF yield**.

Intrinsic value in my base-to-bull range is **$120B–$305B**; the market pays **$466B–$2.1T**. The price embeds decades of flawless execution and then some. Under the Buffett framework — circle of competence, durable excess returns, and a 20–30% margin of safety — this fails the price test decisively. The correct action is to **avoid new capital and sell existing positions**; revisit only if the price falls toward the bull-case intrinsic value or if FCF inflects to sustainably positive with ROIC clearly above WACC.

---

## 6. Key Risks to the Value Thesis

*(Risks both to the business and to my bearish call — I hold both.)*

1. **Valuation compression risk (primary):** At 25x+ sales and negative FCF yield, any slowing of growth or a shift in sentiment toward cash-generative peers could halve the stock without any change in fundamentals. The 2026 price action (swinging $138–$176 within ten weeks) already shows fragility.
2. **Capital intensity and funding risk:** $20.7B capex against negative FCF; continued reliance on debt and equity markets. Net cash of $1.9B is thin relative to burn.
3. **Starship execution risk:** The entire cost-curve thesis depends on Starship achieving reliability and cadence. Failures, FAA grounding, or delays push profitability out and raise capital needs.
4. **Competition:** Amazon Kuiper, Blue Origin, and Chinese state-backed constellations could erode Starlink's first-mover advantage and launch pricing.
5. **Key-man and governance risk:** Musk's attention is divided across ventures; dual-class control and related-party transactions create minority-shareholder risk.
6. **Regulatory/spectrum risk:** Orbital debris rules, spectrum allocation, and national-security export controls could constrain operations.
7. **Dilution risk:** The ~4.5x gap between basic and fully diluted share counts means per-share economics are worse than headline figures suggest; further equity raises are likely.
8. **Risk to my bear case (i.e., the bull argument):** Starlink could become a utility-like cash machine with 10M+ subscribers, Starship could collapse launch costs again and unlock point-to-point and defense contracts, and government spending (Starshield, NASA, national security) could prove far stickier than modeled. If revenue truly runs at a $60B+ annualized rate by 2026–27 and margins reach 25%+, my bull case is too conservative. Even so, the current price would require the hyper-bull case, which leaves no margin for error.

**Bottom line:** Wonderful company, dangerous price. Pass.

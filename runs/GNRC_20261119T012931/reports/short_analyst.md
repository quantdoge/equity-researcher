# Short Analyst

- Symbol: GNRC
- Elapsed: 77.1s

---
I have enough to write. Two data caveats I'll flag: the SEC Form 4 tool returns filing metadata only (no transaction direction), and the annual vs. quarterly balance-sheet files disagree on goodwill/PP&E classification for FY2025.

---

# GNRC — Forensic Short-Seller Analysis
**Price $205.45 | Mkt cap $12.12B | Net debt $940M | EV ~$13.06B | Beta 1.86**

## 1. Earnings Quality Assessment: **MEDIUM**

This is an important starting point, and it cuts **against** the short: Generac's reported numbers are *not* fraudulent. Accruals are negative in three of four years, cash conversion is >100%, and Beneish flags nothing. The problem with GNRC is not that the earnings are fake — it's that the **revenue being capitalised is not the revenue generating the margin**, and consensus is modelling a trajectory the company's own guidance does not support.

| Metric | FY2025 | FY2024 | FY2023 | Read |
|---|---|---|---|---|
| Accruals ratio | −5.0% | −8.1% | −6.3% | Clean |
| Operating CF / NI | 2.75x | 2.28x | 2.40x | Clean |
| FCF / NI | 1.68x | 1.86x | 1.81x | Clean |
| Beneish M-Score | **−2.81** | — | — | Low manipulation risk |
| Piotroski F | **5/9** | — | — | Moderate |
| Altman Z | **2.48** | — | — | Grey zone |

Cash conversion looks flattered because the FY2025 denominator (net income) was depressed. The genuinely informative numbers: the **earnings quality composite is 60/100** and Piotroski loses all four growth/quality points (no ROA improvement, no gross-margin improvement, no asset-turnover improvement, leverage rising).

## 2. Key Red Flags Found

**Flag 1 — The four-year operating-leverage failure nobody prices.** Revenue FY2021 → FY2025: $3.74B → $4.21B, a **+12.6% cumulative** gain (3.0% CAGR). Operating income over the same span: $721M → $269M, **−63%**. The cause is visible in SG&A as a share of revenue, which has risen every single year:

> SG&A/Revenue: **12.4% (2021) → 15.2% (2022) → 17.4% (2023) → 18.9% (2024) → 23.2% (2025)** — +1,083bp.

Beneish's SGAI of **1.229** is the single worst input in an otherwise clean model. This is a company that has been getting structurally *less* efficient at scale while the market pays for the opposite.

**Flag 2 — Receivables outrunning revenue, right now.** This is the freshest and most concerning accounting signal, and it post-dates the Beneish window (FY24→FY25), so the model cannot see it:

- Net receivables: $602.7M (12/31/25) → $846.0M (9/30/26) = **+40.4%**
- Revenue 9M26 vs 9M25: $3,528M vs $3,117M = **+13.2%**
- Sequential Q3: AR **+26.4%** vs revenue **+10.3%**
- Implied DSO ~**50 days → ~59.5 days**

Note this is a *recurring* pattern, not a one-off: the receivables screen already flagged **FY2023** (AR +2.8% against revenue −11.9%) and **FY2024** (AR +13.9% vs revenue +6.8%). The benign explanation — a mix shift to hyperscalers on milestone billing — is credible. The sceptical explanation (quarter-end pull-forwards into the Amazon ramp) cannot yet be excluded. Watch it.

**Flag 3 — Inventory days jumped 32 days in FY2025.** FY2024 143.2 → FY2025 **175.5 days** (+22.6%), in a year residential revenue fell 7%. *The tool labelled this "stable_or_falling" — that is wrong; the series is 168.6 → 160.4 → 143.2 → 175.5 and the latest move is a sharp increase.* Inventory has since stayed roughly flat (~$1.25–1.29B) while revenue accelerates, which partially redeems it — but it suggests FY2025 built stale residential stock ahead of a quiet storm season.

**Flag 4 — The Q2 2026 "beat" was largely a one-time item, and margins then rolled over.** Q2 2026 adjusted EBITDA margin of 24.8% included a **~$71M tariff refund credit**; ex-credit, ~**18.8%**. Gross margin then fell **44.5% → 39.9%** sequentially in Q3, and Q3 revenue *missed* consensus despite the +16.2% headline. That is why the stock fell **−17.7% over 4–5 November** on heavy volume. Consensus models anchored on Q2 are anchored on a credit.

**Flag 5 — Q4 2025 was a classic big-bath.** SG&A spiked to $319.0M (+33.5% QoQ) against revenue down 2.1%, producing a $9.3M operating loss and $24.5M net loss. Driver: a **$104.5M product-liability settlement** on a portable generator. Ex-settlement, operating income still fell ~27%. Charges clustered into a quarter the market had already abandoned.

**Flag 6 — "Up to $8 billion" is a warrant-vesting milestone, not an order book.** The September 2026 Amazon agreement is **$2.4B of deliveries across 2027–2028** (~$1.2B/yr). The $8B figure is the *cumulative purchase threshold* that vests Amazon's warrants — not a commitment to buy $8B. Headlines ($8B deal, +35% pre-market) conflated the two. Amazon has the right to buy **1,693,745 shares at $200.9266** (2.9% dilution; 307,954 vesting immediately, the balance on cumulative payments).

**Flag 7 — Generac is paying for revenue with equity.** A customer taking 2.9% of the equity as a function of purchase volume is economically a rebate booked in stock, not a clean arm's-length sale. It aligns incentives in a way that is *mutually* supportive of booking volume, and it means the true economic margin on Amazon business is below the reported C&I margin. Combined with the fact that the stock now sits at **$205.45 — barely above Amazon's $200.93 strike** — the entire "deal premium" has already evaporated. The 17 September session opened at $229.50 and closed at $207.23 on 8.05M shares (≈13% of float): a gap-and-fade distribution pattern, not accumulation.

**Flag 8 — Goodwill and intangibles are ~39% of assets and ~76% of book equity.** Tangible equity ~$0.69B against $13.1B EV. Altman grey zone (2.48), with EBIT/Total Assets of just 0.048.

## 3. Beneish & Accruals Analysis

Beneish **M-Score −2.81**, comfortably below both the −2.22 and −1.78 thresholds. Component profile: DSRI 1.005 (no receivables-driven revenue inflation at the annual level), GMI 1.013, AQI 0.928, SGI 0.98, DEPI 0.907, LVGI 1.03, TATA **−0.05**. Only SGAI (1.229) is adverse, and that reflects cost growth, not manipulation.

**Conclusion: the accounting is clean.** The one caveat worth stating plainly: Beneish is an annual, backward-looking model computed on FY24→FY25. It structurally cannot detect the 2026 receivables surge in Flag 2. I would re-run it on FY2026 data before dismissing that flag — but I will not oversell it. There is no fraud case here, and any short pitched as fraud will lose.

## 4. Competitive Threat Assessment

This is the heart of the bear case, and it is arithmetic, not opinion.

**The TAM does not support the consensus build.** The *entire global* data-center generator market is ~**$8.57B in 2026, growing to $9.79B by 2031 — a 2.7% CAGR** (MarketsandMarkets). The entire market adds roughly **$1.2B of revenue over five years combined.** Generac's own 2026 data-center business is ~**$450M**. Against that, Amazon alone is contracted for ~$1.2B of deliveries per year in 2027–28 — meaning Generac must capture a sum larger than the whole industry's five-year growth, in one year, from a standing start.

**And Generac is the share *taker*, not the leader.** C&I large-generator share: **Cummins ~30–35%**, **Caterpillar ~20–25%**, **Generac ~5–10%**. Winning hyperscale volume against those two incumbents requires price — which is precisely why C&I adjusted EBITDA margin is **14.6%** versus **34.7%** for Residential.

**Which creates the central paradox of the bull case: growth is margin-dilutive.** Residential is 54% of revenue at 34.7% margin; C&I is 35% at 14.6%. Every dollar of data-center revenue mathematically dilutes the blended margin. The bull story is "operating leverage on scale"; the segment math says the opposite.

**Residential is a melting ice cube with weather beta.** 54% of revenue, **−7% in FY2025** on a quiet hurricane season, −2% in Q2 2026, at just **6.75% US household penetration** with a maturing dealer channel (~10,000 partners) and rising battery/VPP substitution. Management itself cut FY2025 guidance citing weak residential demand. Beta of 1.86 is the market's acknowledgment that this P&L is a hurricane derivative.

**Capacity is the binding constraint — and consensus exceeds it.** Management guides >**$1.25B of large-MW capacity by Q4 2026**, tripling to ~**$3.75B by Q3 2027**. Now build FY2027 from the company's *own* segment guidance: C&I ("up 30%+") ~$2.5B, Residential flat ~$2.3B, Other ~$0.5B → **~$5.3B**. Consensus FY2027 revenue is **$6.89B (+42.7%)**. **Consensus sits ~$1.6B (≈30%) above what management's own guidance arithmetic implies** — and clearing it requires C&I to roughly double in a single year, against a $8.6B TAM growing 2.7%. Note also that capex is only ~3.5% of sales ($170M FY2025, $127M 9M26) — there is no balance-sheet signature of a company actually building the capacity the story requires.

## 5. Management Red Flags

- **Insider filings are dense and rhythmic.** ~30 Form 4s in ~7 months, clustering immediately after each earnings release (five on 3 Nov 2026; four on 4 Aug 2026; four on 5 May 2026). That cadence is the signature of programmatic 10b5-1 selling rather than conviction buying. **Honest gap: the filing tool returns metadata only, not transaction direction or size, so I cannot state a net-selling figure.** I flag the pattern, not a conclusion.
- **Promotional framing versus delivery.** "Up to $8 billion" led the press release and the tape; $2.4B across two years is the actual commitment. Management also disclosed $1.6B of data-center backlog including a second hyperscale contract whose committed volumes are *not* in the backlog — a framing that maximises perceived optionality.
- **Product liability:** the $104.5M portable-generator settlement plus the earlier PWRcell class action ($15M) indicate recurring quality-control costs in the low-margin product lines.
- No auditor changes or related-party self-de

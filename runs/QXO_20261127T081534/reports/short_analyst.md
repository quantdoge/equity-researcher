# Short Analyst

- Symbol: QXO
- Elapsed: 123.1s

---
# QXO, Inc. (NYSE: QXO) — Forensic Short-Seller Analysis
**Price $11.97 | Market cap $12.5B | Beta 2.36 | Analysis date: late Nov 2026**

**Framing note before the numbers:** QXO's reported financials are the output of four acquisitions in 18 months (Beacon ~$11B, Apr-2025; Kodiak ~$2.25B, 2026; TopBuild ~$17B, closed 1-Jul-2026; plus a lost bid for GMS). Almost every forensic ratio below is distorted by merger artifacts — in *both* directions. My job is to separate mechanical noise from economic signal, because a naive screen would call this company either a fraud or a cash machine depending on which line you look at.

---

## 1. Earnings Quality Assessment

**Rating: LOW — but *not* Fraudulent Risk. Aggressive, disclosed, roll-up accounting. No evidence of fraud.**

The GAAP-vs-"adjusted" gap at QXO is the widest of any distributor I can point to. Q3-2026: revenue $4,895M, GAAP operating income **+$2M**, GAAP net loss **–$123M**, yet "Adjusted EBITDA" of **$557M (11.4% margin)** and adjusted EPS of $0.13. Both are "true" simultaneously only because ~$1.5B/yr of intangible amortization, $316M/yr of stock comp, and recurring "one-time" integration costs sit outside the metric management sells.

**The single most important number in this report:** TTM (Q4-25 → Q3-26) adjusted EBITDA run-rate ≈ **$2.2B**; TTM operating cash flow = **$41.6M**; TTM free cash flow = **–$97.8M** (and ≈ –$506M once deal outlays are included, per company-sourced figures). Adjusted EBITDA converts to free cash at roughly **negative** — a 0% conversion rate on a $2.2B claim.

**Cash bridge (TTM, my estimates, ±10%):**

| Item | $M |
|---|---|
| Adjusted EBITDA (annualized run-rate) | ~2,200 |
| Cash interest (Q3 $163M × 4) | (652) |
| Capex | (200) |
| Preferred dividends (Q3 $66M × 4) | (240) |
| Working capital absorption (Q2 –418, Q3 –285) | (457) |
| Cash taxes (est., losses shield) | (50) |
| **Implied residual cash** | **~600** |
| **Actual TTM operating cash flow** | **42** |

**~$550–650M/yr of cash costs are being excluded from "Adjusted EBITDA"** — integration, transaction, and severance items that have appeared in *every single quarter* since the Beacon close. That is the crux of the forensic case: the adjustments are not non-recurring, they are the cost of the business model.

---

## 2. Key Red Flags Found

1. **Goodwill + intangibles = $25.3B = 73% of total assets and 136% of total book equity.** Tangible common equity is roughly **–$9.7B (–$9/share)** if ~$3.0B of preferred sits inside equity (company has a commitment for up to $3.0B of convertible preferred; drawn amount unverified). The entire common equity is an accounting construct resting on purchase-price allocations struck at cyclical premiums.
2. **Organic margin compression in the acquired base.** Q2-2026 adjusted EBITDA margin **8.4% vs 10.7% a year earlier** — *before* TopBuild's higher-margin mix flattered Q3 to 11.4%. Legacy Beacon roofing volumes softened; Beacon sales were reportedly down ~2.5% YoY. The asset they paid 12x for is shrinking organically.
3. **GAAP interest coverage ≈ 0.01x.** Q3 operating income of $2M against $163M of quarterly interest. Coverage only exists on an adjusted basis. Annualized interest ~$652M vs GAAP EBIT ~$13M.
4. **Debt quadrupled in nine months:** total debt $3.91B (Dec-25) → $10.28B (Sep-26), of which only ~$9.0B is conventional debt per company disclosure. Net debt **$9.75B**, cash **$528M** — cash equals ~10 days of revenue and 0.16x current liabilities. Liquidity is revolver-dependent.
5. **Leverage: 4.4x net debt / annualized adjusted EBITDA; ~5.7x including preferred.** Against management's own $4B 2030 target this is fine; against *actual cash generation* it is uninvestable as a credit.
6. **Persistent recurring losses:** TTM net loss ~$495–676M (mine: –$495M; company-sourced TTM figure –$676M, difference likely preferred/dividend attribution). Retained earnings –$950M and falling.
7. **Working capital hemorrhage:** –$418M (Q2-26), –$285M (Q3-26). Partly acquisition-driven, but it means revenue growth is consuming cash, not producing it.
8. **Gross margin is not comparable period-to-period:** 15.5% (Q2-25), 17.5%, 16.9%, **14.2% (Q1-26)**, 24.7%, **28.2% (Q3-26)**. Swings of 1,400bp in two quarters are purchase-accounting inventory step-ups and mix shift, not operating reality. Any analyst building a margin trend off these numbers is building on sand.
9. **Data-quality caveats (disclosed, not hidden):** FY2025 and Q1-26 `ppe_net` of $1.38M and $1.33M are implausibly small versus $2.36B in Q3-26 — a scaling error in the feed. FY2025 `total_debt` $3.91B vs `long_term_debt` $3.06B implies ~$857M of leases/current maturities not itemized. Inventory days (103.7 in 2025 → ~66 in Q3-26) is a **mix artifact** from TopBuild, *not* a demand signal — do not read it as either bullish or bearish.

---

## 3. Beneish M-Score and Accruals Analysis

**Beneish M-Score: 257.9 — "HIGH RISK." This number is garbage, and I will not present it as evidence.**

Attribution: AQI **415.8** (intangibles now dominate non-current assets), SGI **120.3** (sales +11,931%), LVGI **43.7** (debt +6,800%). DSRI 0.967, TATA –0.034, DEPI 0.616, SGAI 0.125 are all unremarkable. The model was calibrated on firms that did not grow revenue 120-fold in twelve months; it is measuring the merger, not manipulation. **Verdict: false positive on fraud, true positive on "the financial statements have stopped being comparable across periods"** — which is itself the analytical problem.

**Accruals:**
- Reported accruals ratio FY2025: **–0.034** ("ok"); TTM 2026: **≈ –0.021**. Negative accruals normally signal *conservative* earnings.
- This is mechanical, not flattering evidence of quality: ~$1.5B of annual intangible amortization is added back against only ~$0.5B of net loss.
- **Adjusted accruals** (adding back amortization to get cash earnings of ~$985M TTM): accruals flip to **≈ +0.037 of assets** — positive, and cash conversion of *economic* earnings is the problem.
- Cash conversion ratio: **–0.08** (OCF/net income). FCF conversion: **–0.20**. Composite earnings-quality score: **0/100.**

**Supporting models:** Altman Z **1.606 — Distress zone** (x2 retained earnings/assets –0.025, x3 EBIT/assets –0.010). Piotroski F **4/9 — Weak** (fails: positive ROA, ROA improvement, lower leverage, no dilution, gross-margin improvement). Note both were computed on FY2025 data and predate the TopBuild debt; the current picture is *more* levered, not less.

---

## 4. Competitive Threat Assessment

- **Cost of capital is the real moat question.** QXO's two largest competitors in effect are Home Depot (owns SRS Distribution, and beat QXO for GMS in 2025) and ABC Supply (private, #1). Losing GMS to a AAA-rated strategic is direct evidence QXO does not win auctions on price or certainty. A 4.4x-levered acquirer with a 2.36-beta currency cannot outbid a AA-rated retailer indefinitely.
- **Pricing power: absent.** Roofing/insulation distribution is a logistics-and-credit business with fragmented contractor customers, no switching costs worth naming, and gross margins that move 1,400bp on accounting mix. There is no evidence in the numbers of the "tech-enabled" margin uplift that justifies a premium multiple — SG&A of $1,024M absorbed Q3's margin gain (Truist's read: in line only).
- **Cycle position: wrong.** Elevated mortgage rates, tariff uncertainty, weak new residential construction, soft repair-and-remodel. QXO has concentrated its portfolio into *new residential* exposure (TopBuild) at exactly the point in the cycle where that is worst.
- **Commoditisation risk:** none technological; the risk is that "tech-enabled distribution" is a narrative with a 3-5 year payback that must be financed by a balance sheet that cannot currently fund it from operations.

---

## 5. Management Red Flags

1. **Targets wildly disconnected from the sell-side.** Management: "$4B adjusted EBITDA by 2030 from businesses we already own," long-term ">$50B revenue." Consensus 2030 EBITDA estimate: **$1.63B — 59% below management.** The street does not believe the guidance it publishes. Worse, the estimates are internally inconsistent ($31.2B 2030 revenue at a 5.2% EBITDA margin vs 11.4% actual; 2028 revenue range $15.9B–$28.0B, a 76% spread). **The consensus number is a deal-cadence extrapolation, not a forecast** — treat both management's $4B and the street's $1.6B with suspicion.
2. **Non-GAAP architecture excludes stock-based compensation** (confirmed in the Q3-26 release: "Adjusted EBITDA … excluding … stock-based compensation"). SBC was $79M in Q3 alone (~$316M/yr, ~2.5% of market cap, ~14% of adjusted EBITDA). This is a real, recurring, dilutive cost being presented as an add-back.
3. **Structural dilution and per-share value destruction.** Diluted weighted shares: 451M (Q1-25) → 716M (Q4-25) → 1,081M (Q3-26): **+139% in six quarters, +51% in three.** TopBuild was ~55% stock; Kodiak included ~13M shares; a Jan-2026 common offering raised $749M net. Issuing equity at $11–20 against ~$17 book is a slow transfer of value away from existing holders. The tell: **Q2-26 adjusted EBITDA rose 33% ($272M vs $204M) while adjusted diluted EPS fell 27% ($0.08 vs $0.11).** EBITDA grows, per-share value shrinks.
4. **$500M buyback authorised (Nov-2026) while FCF is negative and leverage is 4.4x.** That is not capital allocation; it is dilution management and price support during equity-funded M&A. It ranks behind $10B of debt and ~$240M/yr of preferred dividends.
5. **Recurring "one-time" costs** (~$550–650M/yr) — the definitional red flag of the serial-acquirer model.
6. **Senior management churn mid-integration:** new COO (Ken West, start Sep-2026) and new CFO (Dev Ahuja, Nov-2026), with predecessor moved to vice chairman. Not disqualifying, but a CFO change during the largest integration in company history is a watch item.
7. **Insider activity — GAP, disclosed.** Form 4 filings cluster heavily: 5 on 2026-01-05, 8 on 2026-05-07, 2 on 2026-07-17, plus 2026-09-17, 2026-10-13, 2026-10-19. The metadata returned does not resolve transaction direction or size, so **I cannot assert net insider selling, and I will not.** The clustering coincides with deal closings and the January offering and warrants scrutiny of the actual Forms 4.

---

## 6. Short Thesis Summary — is there a credible bear case?

**Yes, on solvency-and-dilution grounds. No, on fraud grounds.**

**The bear case in one line:** QXO is a 4.4x-levered consolidator of a declining-cycle, no-moat distribution business whose goodwill is 136% of equity, whose "earnings" are ~$2.2B of adjusted EBITDA that converts to *negative* free cash flow, and whose per-share value is diluted ~50% every three quarters to keep the machine running. A housing downturn or a closed capital market turns a 0.8x-book equity into a 0.3x-book equity.

**But the market already knows most of this.** The stock is **–45.7% YTD, –33.5% over one year**, at ~0.8x common book and <1x sales, near 52-week lows (~$10.70 close on 20-Nov-2026). EV including preferred ≈ $25.3B / $2.23B adjusted EBITDA ≈ **11.3x** — roughly what QXO itself pays for assets, i.e. no premium, and ~13x on 2027 consensus. That is not a bubble multiple; it is a "show-me" multiple. **The naive short — "roll-up, levered, GAAP losses" — has already been paid out.**

**The other side, stated at full strength (and it is strong):**
- Brad Jacobs has built five multibillion-dollar companies the same way (United Rentals, United Waste, XPO, GXO, RXO). Writing this off as a fraud ignores the best roll-up track record of the last 30 years.
- He and aligned investors have billions of their *own* equity in the structure — the alignment argument is real.
- $12B of revenue, ~28,000 employees, #1/#2 position in a $200B+ fragmented market with private competitors who lack QXO's acquisition currency.
- Integration costs *should* roll off in 2027; if they do, FCF inflects mechanically and the deleveraging story becomes self-funding.
- 19 of 20 analysts rate Buy, average target ~$23. Uniform sell-side enthusiasm is a contrarian negative — but it also means squeeze fuel in a 2.36-beta name with a $500M buyback.
- Shorting a stock already down 46% at below book value, into an authorised repurchase, is how short sellers get carried out.

**Verdict on the thesis:** the forensic red flags are *real but already legible*; the remaining downside requires a macro/credit catalyst I cannot date. That is not an edge — it is a leveraged bet on US housing.

---

## 7. Contrarian Rating

# NO EDGE
*(Bear case credible; short not actionable at $11.97. No fraud found.)*

**Re-arm the short — with size — if any two of the following occur:**

| Trigger | Why it matters |
|---|---|
| Net debt / adj EBITDA > 5.0x, or cash < $300M with revolver drawn | Liquidity event risk |
| Any equity issuance below $11.50, or further stock-funded M&A | Confirmed per-share value destruction spiral |
| Goodwill impairment of any size, or a new "adjusted" metric definition | Marks the end of the accounting runway |
| Adjusted EBITDA margin < 9% for two consecutive quarters (clean base) | Proves organic erosion, not mix |
| Integration/transaction costs still >$400M/yr in FY2027 | Proves "one-time" costs are recurring — the core thesis |
| CFO exit within 12 months of appointment | Governance |
| Covenant amendment or secured/bridged financing at >8% | Credit stress |

**Cover the short / turn bullish if:** FCF turns sustainably positive for two quarters with leverage falling below 3.5x, or TopBuild/Beacon organic volumes inflect while SBC falls below 10% of adjusted EBITDA.

**Monitoring gaps (honest disclosure):** no 10-K retrievable via my tools (10-Q exhibits only), so debt covenant terms, maturity ladder, preferred drawn amount, and purchase-price allocations are unverified; peer trading multiples not obtained; insider Form 4 direction unresolved. The three I would close first: **preferred liquidation preference and dividend terms, the debt maturity wall, and whether SBC is excluded from the "adjusted EPS" too.** If the maturity wall is short-dated and floating, I would move to **Short** on leverage alone.

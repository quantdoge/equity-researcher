# Geo Legal Researcher

- Symbol: CRDO
- Elapsed: 73.2s

---
# CRDO — Geopolitical, Regulatory & Legal Risk Assessment
*Prepared [Oct 2026] | All figures USD unless noted*

## Company Structure — the Frame for Everything Else
Credo Technology Group Holding Ltd is a **Cayman Islands exempted company** (country: KY; CIK 0001807794) with **no operations of its own** at the parent level; it is headquartered in San Jose, CA, with stated operational reach in the **United States, Mexico, mainland China, Hong Kong and other international markets** (company profile; [10-K FY2024](https://www.sec.gov/Archives/edgar/data/1807794/000162828024029629/crdo-20240427.htm)). Critically, the group structure routes physical product through Asia: **"CTGL purchases wafers from TSMC, and then sells these wafers to its subsidiary in Hong Kong"** ([S-1/A exhibit 10.17, EDGAR Online](https://content.edgar-online.com/ExternalLink/EDGAR/0001628280-22-000985.html)). That single sentence creates three of the four risks below: foundry single-point-of-failure (Taiwan), an offshore trading/channel hub (Hong Kong), and trade-compliance exposure on onward sales.

## 1. Geographic Risk Map

Revenue is reported on a **ship-to / customer-domicile basis**, which materially distorts the picture versus where end demand actually sits (US hyperscalers) and where product physically flows (Asia ODMs/contract manufacturers).

| Geography | Revenue exposure | Basis / source | Risk level |
|---|---|---|---|
| **United States** | ~15% (FY25) → est. **~70%** (FY26, ~$941M) | 10-K FY2025: "15% North America, 85% rest of world, primarily Asia" ([TradingView 10-K summary](https://www.tradingview.com/news/tradingview:c0391fa6b2af1:0-credo-technology-group-holding-ltd-sec-10-k-report/)); FY26 US$940.7M per [Simply Wall St aggregation](https://simplywall.st/stocks/us/semiconductors/nasdaq-crdo/credo-technology-group-holding/past) (secondary, unverified) | **Low** |
| **Hong Kong** | est. **~30%** (FY26, ~$395M) | Same secondary source; HK is the group's trading/distribution subsidiary under the S-1 structure | **Medium-High** |
| **Mainland China** | Residual within FY25's 85% "rest of world"; not separately quantified in accessible filings | FY2025 10-K geographic note | **High** |
| **Taiwan** | No disclosed revenue; **critical single-source input** (TSMC wafers) | S-1/A Ex. 10.17; 10-K cites reliance on third-party manufacturers "primarily in Asia" | **High (tail)** |
| **Mexico** | Not disclosed; listed operating location | Company profile | **Low-Medium** |
| **Cayman Islands (domicile)** | n/a — parent only | 10-K FY2024 | **Low structurally / tax-policy sensitive** |

**Concentration is the amplifier:** FY2025 sales to the **top 10 customers ≈ 90%** of revenue, with **two customers ≥10%** ([10-K FY2026 filing text](https://www.sec.gov/Archives/edgar/data/1807794/000162828026043303/crdo-20260502.htm)); in FY2025 **a single customer was 67% of revenue**; by Q4 FY2026 **four hyperscalers each contributed ≥10%** ([Yahoo Finance/Zacks](https://finance.yahoo.com/markets/stocks/articles/credos-diversification-push-cut-customer-164800401.html)). Diversification is real but has shifted concentration from one name to a handful of US mega-caps whose demand is politically mobile.

## 2. Top 3 Geopolitical Risks

**Risk 1 — US–China trade/export-control escalation and tariffs. Probability: High (ongoing). Impact: Medium-High.**
The 10-K explicitly flags that "**U.S. tariffs and trade restrictions, particularly those affecting China, may increase costs and limit component availability**" and cites compliance with "export controls and sanctions laws, customs regulations and local trade" regimes (10-K FY2026 / FY2025 [TradingView summary](https://www.tradingview.com/news/tradingview:c0391fa6b2af1:0-credo-technology-group-holding-ltd-sec-10-k-report/); SEC snippet). The live mechanism is **Section 232**: a presidential proclamation (Jan 2026) imposed an **immediate 25% ad valorem tariff on certain advanced computing chips and derivative products**, effective **15 Jan 2026**, with a phased expansion ([White House proclamation](https://www.whitehouse.gov/presidential-actions/2026/01/adjusting-imports-of-semiconductors-semiconductor-manufacturing-equipment-and-their-derivative-products-into-the-united-states/); [EY](https://globaltaxnews.ey.com/news/2026-0209-us-section-232-proclamation-imposes-25-percent-tariff-on-certain-semiconductors); [White & Case](https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced)). Because Credo's AECs/DSPs are assembled in Asia and imported into the US for US hyperscalers, a broadening of scope is a **direct gross-margin hit** (~68% GAAP GM leaves room to absorb, but pricing power against hyperscalers is limited). Offset: the Jan 2026 policy loosened licensing for H200/MI325X-class exports to China ([CFR analysis](https://www.cfr.org/articles/new-ai-chip-export-policy-china-strategically-incoherent-and-unenforceable)), which supports Chinese AI capex but does not de-risk Credo's own classification.

**Risk 2 — Taiwan Strait / single-source foundry. Probability: Low (12–24m). Impact: Severe.**
Wafers come from **TSMC** (S-1/A structure disclosure); there is no disclosed second source at leading nodes. A blockade, quarantine exercise, or shipping/insurance disruption halts AEC output regardless of demand. Compounding: **Taiwan is criminalising unauthorised AI-chip exports to China** under the Feb 2026 US–Taiwan Agreement on Reciprocal Trade ([WITA](https://www.wita.org/taiwan-to-criminalize-unauthorized-ai-chip-exports/)) — this raises diligence obligations on Credo's Taiwan-based partners and any onward China-bound flows.

**Risk 3 — Chinese regulatory retaliation / localisation of demand. Probability: Medium. Impact: Medium.**
Beijing has expanded its **anti-sanctions toolkit** to hit back at US/EU controls ([Al Jazeera, Jul 2026](https://www.aljazeera.com/news/2026/7/10/china-expands-anti-sanctions-toolkit-raising-risks-for-foreign-firms)) and is drafting **trade-secret rules including export bans and investment restrictions on foreign firms** ([SCMP](https://www.scmp.com/economy/policy/article/3372161/china-drafts-rules-protect-trade-secrets-foreign-entities)). Credo's IP-licensing line (3% of FY25 revenue) and its China-based engineering/ops footprint are the exposed edges. The structural offset is that Credo's revenue mix has rotated decisively toward US hyperscalers, reducing — but not eliminating — China policy sensitivity.

## 3. Legal & Regulatory Highlights

- **IP litigation overhang has been cleared.** Credo settled its **Active Electrical Cable patent disputes with Amphenol** — "all patent disputes between the two companies" ended, lawsuits to be dismissed ([Credo IR](https://investors.credosemi.com/news-events/news/news-details/2025/Credo-and-Amphenol-Reach-Settlement-in-Active-Electrical-Cable-Patent-Infringement-Disputes/default.aspx)) — and separately settled with **Volex** (Aug 26, 2025), with suits "promptly dismissed" ([Credo press release](https://credosemi.com/news/credo-and-volex-reach-settlement-in-active-electrical-cable-patent-infringement-dispute/)). This *lowers* litigation risk but confirms Amphenol as a well-resourced direct competitor in AECs with demonstrated willingness to litigate.
- **No active securities class action, SEC subpoena, or DOJ/FTC investigation surfaced** in our searches — a clean finding, though absence of evidence is not evidence of absence given limited filing-text access (see Gaps).
- **Export-control/customs compliance**: EAR/OFAC and customs-classification obligations are disclosed risk factors. The material question is not Credo's own licence requirements but **diversion risk** through Hong Kong and China-based ODMs.
- **Tax/structuring**: Cayman parent → HK trading subsidiary → Asia ODMs, with wafer purchase/resale at each hop. This invites **transfer-pricing scrutiny, HK offshore-claim/FSIE analysis, PRC permanent-establishment risk, and Pillar Two (15% global minimum tax) top-up exposure** as HK/Cayman regimes tighten. Structured to be tax-efficient; structurally fragile under policy change.
- **Shareholder rights**: Cayman exempted-company status means limited statutory remedies versus a Delaware charter.

## 4. Compliance Red Flags

| # | Flag | Severity |
|---|---|---|
| 1 | **~30% of revenue booked through Hong Kong** (the group's own trading subsidiary), adjacent to restricted destinations for advanced computing since the Oct-2022 EAR rules — diversion/enforcement risk under heightened US and now Taiwanese scrutiny | **Elevated** |
| 2 | **Section 232 25% duty** on US-bound advanced-chip imports; scope expansion is the key swing variable to gross margin | Elevated |
| 3 | **Customer concentration** (top 10 ≈ 90%; FY25 single customer 67%) means one customer's geopolitical re-sourcing decision is a revenue event, not a mix shift | Elevated |
| 4 | **Cayman/HK/China intercompany structure** — transfer-pricing and PE exposure; Pillar Two adoption timeline | Moderate |
| 5 | **No disclosed FCPA/AML issue**; data-privacy exposure low (PILOT network software telemetry in customer data centres) | Low |

## 5. Overall Geopolitical / Legal Risk Rating: **HIGH**

**Rationale:** Legal (litigation) risk has *declined* materially — the Amphenol and Volex patent wars are settled and no regulatory investigation is evident. But geopolitical/trade risk is *structurally high and rising*: a Taiwan-single-sourced supply chain, a Hong Kong trading hub carrying roughly a third of revenue, a 25% Section 232 tariff already in force on advanced-chip imports with scope-expansion risk, and extreme customer concentration among hyperscalers whose geographic placement is politically determined. The mitigation is genuine — the revenue base has migrated toward US-domiciled hyperscalers, shrinking direct China exposure versus the FY2022–23 era — which is why this is **High, not Very High**.

**Gaps / limitations:** SEC.gov direct fetch returned **403 Forbidden**, so exact FY2026 risk-factor language and the audited **revenue-by-geography table are quoted from search snippets and secondary aggregators, not the filed document**; the ~70% US / ~30% Hong Kong FY2026 split (Simply Wall St) should be re-verified against the FY2026 10-K geographic note before use in a model. Mainland China revenue is not separately quantified in any accessible source.

# Short Analyst

- Symbol: BSP
- Elapsed: 146.8s

---
I have enough. The forensic picture is clear — and notably, it is **not** a fraud case. Writing up now.

---

# BSP — Bending Spoons S.p.A. Forensic Short Analysis
**Price $46.29 | Mkt cap $29.4B | Net debt ~$4.0B (Q3'26) | Tech / Software-Application | Italy / Nasdaq**

---

## 1. Earnings Quality Assessment: **MEDIUM**

Let me be direct: **the accounting here is clean. The business model is not.** The forensic tools throw several alarms, but most are artifacts of acquisition accounting rather than manipulation. Separating those is the whole job.

| Metric | 2023 | 2024 | 2025 |
|---|---|---|---|
| Net income | $160.8M | $89.5M | **-$0.14M** |
| Operating cash flow | $59.2M | $204.9M | **$290.6M** |
| Accruals ratio | +10.9% ⚠️ | -6.1% | -6.1% ✅ |
| Cash conversion (OCF/NI) | 37% | 229% | n/a (NI≈0) |

The composite **earnings-quality score of 0/100 is a mechanical artifact** — the cash-conversion ratio divides by net income of ~$0, producing -2,137. Do not read that as "terrible earnings quality." The opposite is closer to true: over 2024–25 **cash flow materially exceeded reported earnings**, accruals were negative, and receivables days *fell* (DSRI 0.865 — receivables +68% vs revenue +95%). There is no channel stuffing, no accrual inflation, no revenue-recognition game visible. On pure earnings-quality forensics, BSP passes.

The genuine quality concern is **profitability opacity**, not manipulation: 2025 operating income of $277.9M less interest of $142.6M implies ~$135M pre-tax profit, yet net income was **-$136K**. A ~100% effective tax rate on a pre-tax profit. That gap needs explaining — likely non-deductible IPO/convertible fair-value items — and it means "we're profitable" is doing a lot of unexamined work.

**Data-quality caveat:** the reported 2025-12-31 *quarterly* row shows revenue of $1,691.8M — larger than the full-year $1,306.4M — with zero shares and zero D&A. That row is mis-tagged and I have discarded it. Any model built on it is broken.

## 2. Key Red Flags Found

1. **Organic growth is 3%.** Confirmed in Q2 2026 (+126% reported, **3% organic**) and Q3 2026 (+125% reported, **3% organic**). 97%+ of growth is purchased. This is the single most important number in the file.
2. **Reported growth already decelerating:** Q2'26 +171.9% → Q3'26 +150.8% YoY. As acquisition comps lap, reported growth converges toward 3%.
3. **"Adjusted Operating Income" excludes amortization and impairment of acquired intangibles** — confirmed in the company's own 6-K definition. Q3'26: adjusted **$424M** vs GAAP operating income **$216M**. The adjusted figure is ~2x GAAP, and the excluded item is *the cost of the assets they bought*.
4. **D&A of $157M against PP&E of only $11M** (2025). Essentially all depreciation is acquired-intangible amortization. Confirms #3 — the "adjusted" number is an acquisition-cost exclusion, not a cleanliness adjustment.
5. **Goodwill & intangibles = $3.50B = 73.6% of total assets**, and ~3.5x book equity of $995M. Post-Airtable/Mailchimp this is far higher. Impairment risk is concentrated and correlated with the roll-up's own execution.
6. **Leverage doubled in one year:** net debt $629M (2024) → $2.04B (2025) → ~$4.0B (Q3'26) → ~$5B+ post-Mailchimp. Blended cost of debt ~9%. Interest expense run-rate ~$433M; Q3'26 interest of $108.3M consumed **50% of GAAP operating income**.
7. **Capex of $501K on $1.31B revenue** with 2,187 employees. Anomalously low for a company whose stated model is rewriting every acquired codebase in Python/FastAPI/TypeScript. Either development is expensed (conservative — supports gross margin) or capitalized into intangibles (inflates adjusted OI and FCF). Open question; I lean expensed given D&A is pure acquisition amortization, but it deserves a footnote in any bull model.
8. **Consensus credibility:** 2026E net income $892M vs **$295M actual through 9M** implies ~$597M in Q4 — more than double the entire first nine months. Either estimates are adjusted-basis and mislabeled, or they are wrong.
9. **2027 consensus revenue $4.35B ≈ 2026's $3.08B + Mailchimp's ~$1.27B.** The entire 2027 growth line is one acquisition. Zero organic growth is embedded in the consensus.
10. **Lock-up expires 12/27–12/28/2026 — roughly 32 days out.** Eight Form 4s already filed (five on 9/25, three on 11/23). The 11/23 cluster lands precisely on the local high ($47.27 close); the next session fell 9.3% to $42.86 on 10.7M shares. **Honest gap: the filing metadata does not disclose buy/sell direction, so I cannot confirm net insider selling.** Timing warrants scrutiny; direction does not.

## 3. Beneish M-Score & Accruals

**M-Score: -2.122** — "MODERATE RISK" band (-2.22 to -1.78). I will not overstate this. The score is driven almost entirely by **SGI 1.947** (sales growth index ~1.95) and **LVGI 1.194** (rising leverage). For a serial acquirer, SGI inflates mechanically whenever revenue doubles via M&A — it is not evidence of manipulation. The components that *would* indicate manipulation point the other way: **DSRI 0.865** (receivable days falling — no channel stuffing), **TATA -0.0611** (negative total accruals — conservative), **GMI 0.974** (gross margin improved, 65.6% vs 63.9%). **Verdict: no manipulation signal. The M-Score flag is an acquisition-accounting artifact.**

**Accruals:** -6.1% in both 2024 and 2025 — high-quality, cash-backed earnings. The 2023 warning (+10.9%) resolved. **This is not a fraud.**

## 4. Competitive Threat Assessment

The moat question is unusual: BSP's moat is not product, it is **capital allocation and cost surgery**. That is a real, transferable capability — but it is a *harvesting* moat, not a *compounding* one.

- **Gross margin is holding (65.6%, up 30bps)** — pricing power is intact on paper. But note the mechanism: BSP's playbook is buy, cut costs, raise prices. If organic revenue growth is 3% *while actively raising prices*, then **unit volume is declining mid-to-high single digits.** That is moat erosion wearing a margin-improvement mask.
- **The asset base is declining legacy software:** AOL, Vimeo, Evernote, WeTransfer, Meetup, StreamYard, Airtable, Mailchimp. These are not franchises; they are harvestable cash flows with churn.
- **The buying has gotten more expensive relative to what it buys:** Mailchimp at $3.68B for ~$1.3B revenue (2.8x) — cheap vs Intuit's $12B, but Intuit's asset was already in decline. Airtable at ~$2.25B vs an $11B peak is a genuine discount, but also a signal that the counterparty knew something.
- **The arbitrage math is the crux:** $3.68B at ~9% debt costs ~$331M/yr. If Mailchimp yields a 20% FCF margin ($260M), the deal is **value-destructive** at the current cost of capital. At a 40% margin ($520M) it is accretive. The entire equity story reduces to whether cost surgery can produce 40% margins on declining assets, repeatedly, at scale. That is an execution bet, not a moat.

## 5. Management Red Flags

- **Promotional framing:** headline "125% growth" alongside a footnote 3% organic is the classic roll-up disclosure pattern. Not illegal; deliberately unhelpful.
- **Heavy non-GAAP reliance:** Adjusted Operating Income excludes acquired-intangible amortization — the recurring cost of the strategy.
- **Aggressive acquisition pace:** ~$4.6B deployed 2023–Q1 2026, plus Airtable (~$2.25B) and Mailchimp ($3.68B) — integration risk is stacking faster than it can be validated.
- **No related-party, auditor-change, or restatement red flags found.** No insider-selling direction confirmed (data gap).
- **Mitigant:** all term loans are fully hedged and liquidity is $3.36B — near-term refinancing risk is genuinely low. I am not alleging distress.

## 6. Short Thesis Summary — Is There a Credible Bear Case?

**Yes, but it is a de-rating thesis, not a fraud thesis.** The bear case:

> BSP is a $29.4B company whose underlying businesses grow 3% organically, funded by ~$5B of 9% debt, where "profit" is defined to exclude the cost of the assets acquired, and where 2027 consensus revenue growth is 100% one acquisition. The moat is cost-cutting on declining assets — a strategy that consumes capital and eventually exhausts its targets. The 12/28/2026 lock-up expiry and the lapping of 2025–26 acquisition comps are near-dated catalysts that will force the organic 3% into the headline.

**Valuation:** EV ≈ $33.4B. 11.3x 2026E revenue, 7.7x 2027E; 21x 2026E adjusted operating income; **~38x GAAP operating income**; 33x 2026E EPS, 21.5x 2027E. For a 3%-organic, 9%-cost-of-debt roll-up, that is full — though 21.5x 2027E is not egregious *if* estimates are met.

**Altman Z of 0.654 "Distress" is misleading and I will not lean on it.** x4 uses book equity ($995M) rather than market cap; substituting the $29.4B market cap lifts Z to ~5.2 (safe zone). The signal is leverage, not bankruptcy risk.

**The bull case is genuinely strong and I will not strawman it:**
1. **Berkshire Hathaway owns 4%** — $930M invested across July and October at ~$33–35. The most careful capital allocator alive did diligence and bought. That is a real anchor and a real rebuttal to "fraud."
2. **Cash generation is real and clean** — OCF $290.6M vs ~$0 net income, negative accruals, no receivables games. The company *does* convert.
3. **Genuine capital-allocation skill** — buying at 2.8x revenue what others paid 9x for is a real discount discipline.
4. **Interest fully hedged, $3.36B liquidity, no maturity wall** — the balance sheet is levered but not fragile.
5. **Adjusted operating margin of 54%** in Q3'26 is genuinely high.

**If the bull case is right, it is right for one reason:** BSP buys mediocre assets cheap and manufactures margin. That has worked. My bear case is not that it stops working — it is that at 21x adjusted operating income and 33x earnings, with 3% organic growth and 32 days to lock-up expiry, the market is paying for the *next* acquisition to work before the *last* one has been integrated.

## 7. Contrarian Rating: **SHORT** (moderate conviction — not Strong Short)

**Why not Strong Short:** no fraud indicators, clean cash conversion, hedged debt, and a Berkshire anchor. The forensic tools that would justify a Strong Short (M-Score, accruals, receivables) all come back clean. Reflexive bearishness here would be wrong, and I'd rather be right.

**Why Short:** 3% organic growth disclosed against a 125% headline, adjusted profit that excludes acquisition cost, 73.6% of assets in goodwill, ~50% of operating income consumed by interest, a 2027 consensus that is entirely one acquisition, and a lock-up expiry in ~32 days.

**Catalysts:** (1) 12/28/2026 lock-up expiry; (2) lapping of 2025–26 acquisition comps through 2027 — reported growth decays toward 3%; (3) Mailchimp close in early 2027 and the first honest look at its margin; (4) any goodwill impairment on Airtable/Mailchimp.

**What would make me wrong:** Mailchimp delivering 40%+ margins, organic growth inflecting above 10%, or Berkshire adding materially. Watch the organic-growth disclosure line each quarter — that single number is the entire thesis.

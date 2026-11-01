# Short Analyst

- Symbol: RDDT
- Elapsed: 50.7s

---
# RDDT — Forensic Short-Seller Analysis

**Price used: $91.67 (current), mkt cap ~$17.6B | Diluted ~202M shs | Net cash ~$3.0B | EV ~$15.5B**
*Note: the stock is down ~65% from its Sept-2025 peak of ~$259. Any short thesis must be judged against that, not against the old price.*

---

## 1. Earnings Quality Assessment: **MEDIUM-HIGH (not a fraud)**

Bluntly: I looked for a fraud and did not find one. The accounting is, on most measures, better than the average hypergrowth SaaS/ad name. Two genuine blemishes (tax, SBC) — but neither is manipulation.

| Metric | Value | Read |
|---|---|---|
| Accruals ratio (FY25) | **−0.0498** | Negative accruals = cash-backed earnings. Clean. |
| Cash conversion (OCF/NI) | **1.30x** | Well above the 1.0x quality bar |
| FCF conversion | **1.29x** | Clean |
| Gross margin | 91.2% FY25 → 91.5% Q3'26 | **Expanding**, not eroding |
| AR growth vs revenue FY25 | +68.8% vs +69.4% | In line — no channel stuffing |
| DSO | 80.9d (Q3'25) → 74.2d (Q3'26) | **Improving** |
| Piotroski F-Score | 7 | Moderate-strong |
| Altman Z | 7.66 | Safe zone |
| Beneish M-Score | −2.204 | "Moderate" flag — **but see below** |

The composite Earnings Quality Score returned **36/100**, which directly contradicts the cash-conversion data. I treat that as a model artifact rather than evidence: when OCF/NI is 1.30x, FCF/NI is 1.29x and accruals are negative, a "low quality" verdict is not supported by the underlying items. I'm flagging the disagreement rather than pretending it resolves.

**The Beneish flag is a false positive and I'll say so plainly.** Decomposing it:
- **SGI = 1.694** — this is the entire reason the score is elevated. A company growing sales 69% mechanically fails the sales-growth index. That's growth, not manipulation.
- **TATA = −0.0498** — *negative* total accruals, the strongest possible "not manipulating" input.
- **AQI = 0.65** — asset quality *improving*.
- **SGAI = 0.576** — SG&A falling sharply relative to sales (leverage, not expense deferral).
- DSRI = 0.997 — receivables perfectly tracking sales.

A manipulator shows high DSRI, high TATA, high AQI. RDDT shows the opposite on all three. **Verdict: no fraud signal.**

---

## 2. The Two Real Earnings-Quality Flags

**Flag 1 — The effective tax rate is ~0%, and this materially flatters the P/E.**
Q3'26: operating income $261.6M → net income $283.3M. Net income *exceeds* operating income. Same in every quarter (Q2'26: 231.7→252.8; Q1'26: 182.9→204.0; Q4'25: 231.8→251.6). The gap is ~$21M/quarter of net interest income plus an essentially **zero cash tax rate** (NOL/deferred-tax-asset release).
Normalizing TTM to a 23% tax rate: net income falls from **$992M to ~$764M** — a 23% haircut. The headline **17.8x P/E is really ~24x on normalized earnings**, and the NOL shield is finite. Consensus 2027 EPS of $6.87 is very likely also pre-normalization. This is my single best forensic finding.

**Flag 2 — SBC is enormous and "FCF" overstates distributable cash.**
TTM SBC **$385.8M = 12.5% of revenue, 39% of net income**. Q3'26 SBC alone was $131.3M (+57% YoY — growing faster than revenue).
- Reported TTM FCF: **$1,198M**
- SBC-adjusted FCF: **~$812M** → the real EV/FCF is **~19x, not 12.9x**
- SBC-adjusted Q3'26 operating margin: **14.6%**, versus 29.2% reported. Half the margin is stock, not cash.

**Capital allocation red flag:** TTM buybacks $340M vs TTM SBC $386M — the repurchase program covers only **88% of dilution**, and basic shares still rose from 188.0M to 192.6M. Worse, $234.6M was bought in Q2'26 at roughly $180–200/share — now $91.67. That is ~$100M+ of shareholder value destroyed buying stock at 2x today's price, while insiders sold into the same strength.

---

## 3. Competitive Threat Assessment: **SEVERE — this is the real thesis**

The bear case is not accounting. It is **single-point-of-failure distribution dependency**.

- **Google AI Overviews / AI Mode is disintermediating Reddit.** On the Q3'26 call (Oct 29–30, 2026) management said search-driven traffic was **"down meaningfully"** in the quarter. The stock fell **25–30% in one session** to a 1-year low.
- **DAUq growth collapsed to +12% YoY** while revenue grew 53%. Revenue growth is coming from **ARPU/ads-per-user and pricing**, not user growth. That is the classic late-cycle signature: monetizing the existing base harder while the top of the funnel leaks.
- **The proposed login-requirement test is a two-edged sword.** Gating content behind login may lift logged-in ARPU but attacks the very SEO loop that built Reddit's traffic. If public-content indexing shrinks, so does the Google referral flywheel — permanently.
- **Q4'26 guidance: $1.00–1.03B vs $1.05B consensus.** Midpoint implies **+40% YoY** — a hard step-down from +53%. Consensus 2027 revenue of $4.37B requires +29% on top of a decelerating, traffic-impaired base. I think that number is at risk.
- **Bing/OpenAI, Perplexity and ChatGPT are substituting for "search + Reddit thread" research behavior** at exactly the use case that drives Reddit's logged-out traffic.

Revenue deceleration is now unambiguous: **77.7% → 67.9% → 69.7% → 69.1% → 61.1% → 53.0% → ~40% guided.**

Gross margin is expanding and operating leverage is real — the *business model* works. The *distribution channel* is being taken away by Reddit's own largest licensing partner and largest traffic source simultaneously. That is a terminal-value problem, not a one-quarter problem.

---

## 4. Management & Governance Red Flags: **SIGNIFICANT**

1. **Persistent, programmatic insider selling with zero insider buying.** Form 4 density is extreme: **7 filings on 2026-10-07**, **5 on 2026-08-24**, plus recurring filings roughly every 2–3 weeks. CEO Steve Huffman (CEO, President, **10% owner**) sold repeatedly through 2026: ~$2.6M on Feb 27, ~$3.1M in July at $167–176, ~$3.09M and ~$2.5M in late September. All characterized as Rule 10b5-1 — which explains the pattern but does not change the direction. **The most damning datapoint: after a 65% drawdown, not one insider has bought a share.** If the risk/reward were as good as the multiple suggests, that is when you'd see it.
2. **Controlled company.** Advance Publications holds control via dual-class shares. Public holders have structurally limited influence; the "controlled subsidiary" status is disclosed in the profile.
3. **Promotional guidance vs. delivery.** Q3 beat on EPS ($1.40 vs $1.35) while guiding Q4 below consensus and disclosing the traffic deterioration — a beat-and-raise-until-you-can't pattern.
4. **Buying back stock at 2x the current price** while insiders sell — poor capital allocation at best, portfolio-management-at-the-top at worst.
5. No auditor changes, no related-party red flags, no restatements, no aggressive capitalization (capex is a trivial ~$1.2M/quarter; D&A is tiny and consistent). **The financial reporting itself is clean.**

---

## 5. Short Thesis Summary: Is there a credible bear case?

**Yes — but it is a *growth-duration* bear case, not a *fraud* bear case, and much of it is already paid for.**

**The credible bear case:**
- Google AI Overviews structurally caps logged-out traffic → DAUq decelerates toward single digits → ad impression growth converges to ARPU growth, which converges to pricing power against Meta/TikTok/Amazon with 91% gross margins but zero user tailwind.
- Q4 guide of +40% is the first step in a glide path to ~20%. 2027 consensus of $4.37B revenue / $6.87 EPS is too high.
- Normalized tax rate cuts EPS ~23%. SBC cuts economic FCF ~32%. **Stack the two: the stock is on ~24x normalized earnings and ~19x SBC-adjusted EV/FCF — not 17.8x and 12.9x.** For a business with a shrinking distribution channel, that is not cheap; it is fair-to-full.
- The login-wall test could break the SEO flywheel permanently.
- No insider conviction buy at a 65% discount.

**The other side — which is genuinely strong:**
- **$3.0B net cash = 17% of market cap.** No debt ($31M). Altman Z 7.66. This company will not be a zero.
- 91.5% gross margin, **expanding**; operating margin 23.7% → 29.2% YoY. Operating leverage is real and underappreciated.
- Negative accruals, 1.30x cash conversion, receivables in line, DSO improving. **There is no accounting shoe to drop.** A Hindenburg-style report here would have nothing to write about.
- **International ARPU is still deeply underpenetrated vs. US** — a multi-year monetization runway that doesn't need DAU growth.
- AI licensing revenue (Google, OpenAI) is high-margin and growing, even if it is also the source of the disintermediation risk.
- At **~5.0x TTM EV/Sales and ~4.6x on 2026E**, versus 53% growth and 91% gross margins, the multiple is no longer heroic. The bubble has largely deflated.

**Where I land:** the accounting-fraud short is dead on arrival. The "50x sales momentum" short was the right trade — and it already happened (−65%). Shorting a net-cash-rich, cash-generative, 91%-gross-margin business at 4.6x forward sales *after* a 30% single-day capitulation is how shorts get run over on the first stabilization quarter. The Google dependency is a legitimate reason to **never own this at size** and to keep a structural short bias on any rally back toward $140+ — but not to initiate here.

---

## 6. Contrarian Rating: **NO EDGE — Reject the Short Thesis (at $91.67)**

**Reject. Not a short here.** Reasoning, in order of weight:

1. **No fraud, and I checked hard.** Negative accruals, 1.30x cash conversion, DSRI 0.997, expanding gross margin, clean balance sheet. The Beneish flag is an SGI artifact from 69% growth. There is no forensic edge — the thing my mandate specializes in simply isn't present.
2. **The thesis is consensus and the price reflects it.** −65% from peak, −30% in one day, DAUq +12% already public, Q4 guide already cut. The information advantage is gone.
3. **The bear case is quantitatively mild.** Even after my two haircuts (tax normalization → ~24x, SBC adjustment → ~19x EV/FCF), the stock is not egregiously priced for a 91%-gross-margin franchise with $3.0B net cash. There is no 50%-downside air pocket left.
4. **The catalysts are spent.** The bad news is out. Insider selling is 10b5-1 and therefore already in the tape.

**What would change my mind and make this a Short:**
- A re-rating back above **~$150–160** (7.5x+ forward sales) without a DAUq re-acceleration — that's where I would re-engage.
- **Q4'26 DAUq print showing an outright sequential *decline***, or Google referral traffic down >25% YoY — that converts "deceleration" into "shrinking asset" and breaks the terminal-value math.
- Evidence the **login-wall test is being rolled out broadly** (flywheel self-harm confirmed).
- Any 2027 guidance reset below $4.0B revenue.
- A first **insider buy** would actually be a *bullish* tell here — its absence is the tell I'm watching.

**Honest one-line summary:** *Clean books, dirty channel, deflated multiple. I can't short it and I can't own it. This is a structurally impaired franchise that has already been repriced — the forensic short has no ammunition, and the momentum short has already been paid.*

# Nonfin Risk Analyst

- Symbol: CRWV
- Elapsed: 73.9s

---
# CoreWeave, Inc. (CRWV) — Non-Financial Risk Assessment
**As of ~November 23, 2026 | Price $48.33 | Market cap ~$26.9B | Beta 7.67**

> **Data gaps declared up front:** `fetch_filing_text` returned no 10-K and no DEF 14A for CRWV (FY25 10-K exists but was not retrievable through the filing tool; the 10-Q pull returned only an exhibit — the Nov 9, 2026 Change-in-Control Severance Plan). Board composition and insider dollar amounts are sourced from the investor site (JavaScript-only, no content), Boardroom Alpha, Bloomberg and Form 4 summaries rather than primary filings. `search_regulatory_actions` returned **empty** — meaning no EDGAR litigation release names CRWV, which does **not** rule out informal SEC/DOJ activity. Treat dollar figures as reported approximations.

---

## 1. Governance Quality Rating: **WEAK**

| Factor | Evidence |
|---|---|
| **Controlled company** | Dual-class structure with **10 votes/share** on Class B. Co-founders Intrator, Venturo, McBee held **~79.9% of voting power at IPO** (~71% of votes on roughly **one-fifth of the economics** as of April 2026). This qualifies CRWV for the controlled-company exemptions: no majority-independent board, no fully independent comp committee, no ability for public holders to influence any vote. Minority shareholders have effectively zero governance recourse. |
| **CEO/Chair duality** | Michael Intrator is **co-founder, Chair and CEO** simultaneously. No independent chair. |
| **Board thinness** | Only **three outside directors**, all of whom joined just before the March 2025 IPO — Glenn Hutchins (lead independent, chairs comp), Karen Boone (audit chair), Meg Whitman (nominating). A three-person outside cohort checking three co-founders who are all former commodity traders is structurally insufficient. |
| **Audit chair alignment** | Boone reportedly bought ~$500K pre-IPO and has **sold ~$1.2M** — the person chairing the audit committee is a net seller. |
| **Related-party web** | FY25 10-K carries a dedicated Note 14 for related-party transactions. "Strategic financing" is run by **Rogers and Damrat, formerly of Magnetar** — an early lender now inside the financing function. Related-party + lender + supplier (Nvidia is both GPU vendor and shareholder) overlap is exactly where disclosure quality degrades. |
| **Incentive structure** | New **Amended & Restated Senior Executive Change in Control and Severance Plan (effective Nov 9, 2026)**: 12 months salary + prorated target bonus + **100% acceleration of all unvested equity** on a CIC qualifying termination. Adopted mid-drawdown (~67% off peak). Defensible as retention, but it materially raises the cost of any change of control and reads at least partly as entrenchment/wealth-protection for the same executives selling heavily into the market. |

**Verdict:** Governance is not merely "adequate-but-imperfect" — the combination of super-voting control, founder CEO/Chair, a three-person outside board, and $3.3B of founder liquidity with zero open-market buying is a **Weak** rating.

---

## 2. Regulatory & Legal Risk Summary

**Active litigation (material, not speculative):**
- **Securities fraud class action** on behalf of purchasers **March 28, 2025 – December 15, 2025** (lead-plaintiff deadline March 13, 2026). Allegations: CoreWeave **overstated its ability to meet customer demand** and failed to disclose **data-center construction delays** (the Denton, TX / Core Scientific site), while Core Scientific had reportedly been flagging delays from February 2025. The claimed damages event is a **~$14B market-cap loss** (peak $139.93 on Oct 29, 2025 → $52.28 on Dec 16, 2025 after WSJ reporting). Firms involved include Hagens Berman, Kessler Topaz, Rosen, KMT and ZLK — this is a well-resourced, multi-firm consolidated action, not a nuisance suit.
- **Second wave of securities investigations (opened Oct 2026)** concerning whether CRWV **adequately disclosed the borrowing-cost risk** of its debt-funded expansion. Trigger: Oct 13, 2026 reports that yields on CRWV **unsecured bonds hit 15%** (closing record 14.5%), after capex guidance was raised to **$35–39B** (from $31–35B) on Aug 11 and the Sept 17 convertible notes offering was upsized from $3.0B to **$3.7B**. Stock fell 7.74% on Oct 14 and >15% intraday.
- **Merger fallout:** Core Scientific terminated the merger agreement Oct 30, 2025 after insufficient shareholder votes — an unusual and reputationally costly failed acquisition that sits inside the class period.

**Regulatory/enforcement backdrop (sector-wide but pointed at CRWV's model):**
- **SEC enforcement posture on AI disclosure.** Enforcement Director David Woodcock (Oct 30, 2026): the agency's "principal concern is that people are making accurate disclosures about material information"; where disclosure is absent, "**enforcement will be present**." Explicit focus on **circular financing** — supplier-financed demand that makes it hard to distinguish genuine end-demand from vendor-funded purchases. CRWV (Nvidia supplier + Nvidia shareholder + customer prepayments + 15% bond yields) is the archetype of this disclosure problem.
- **Export controls:** new U.S. curbs (Nov 2026) threatening neocloud business in **Southeast Asia** — a direct revenue-path risk for GPU capacity exports.
- **Environmental enforcement:** Denton facility faces **pending TCEQ air-quality enforcement** for alleged emissions violations.
- **State-level moratorium risk:** post-2026 midterm political shifts create **Texas data-center moratorium risk**.
- **No CRWV-specific SEC/DOJ action found in EDGAR.** Absence of a litigation release is not absence of an investigation; the Oct 2026 firm investigations are private, and formal SEC/DOJ process would likely surface first in an 8-K or 10-Q legal-proceedings footnote.

---

## 3. Insider Activity Analysis — **STRONGLY NET SELLING (severe red flag)**

| Insider | Role | Net activity since Mar 2025 IPO |
|---|---|---|
| Brian Venturo | Co-founder, CSO, Director | **Sold ~$1.21B** (>1/3 of IPO holdings) |
| Brannin McBee | Co-founder, Dev Chief | **Sold ~$1.08B** (~40% of IPO holdings) |
| Michael Intrator | Co-founder, **Chair & CEO** | **Sold ~$975M** (~1/6 of IPO holdings) |
| Nitin Agrawal | CFO | Sold ~$64M (~half for taxes) |
| **Total** | | **~$3.3B sold; $0 of open-market purchases by any officer or director since IPO** |

- **Cadence is the tell:** roughly **40 Form 4s between August and November 2026 alone** — sustained, mechanical, 10b5-1-plan selling straight through a 67% drawdown and through the Oct 2026 bond-yield shock. Insiders did not step up to buy the dip that they publicly called "irrational."
- **The one counter-signal:** Venturo reportedly put **~$30M into CoreWeave bonds** (Nov 2026). Read this carefully — it is a **credit** view (secured/recovery-oriented, senior in the capital structure), **not** an equity endorsement. An insider buying the debt while selling the stock is arguably a *bearish* signal on equity: it says "the assets are worth something, the residual may not be."
- **Interpretation:** Insiders are converting a growth narrative into personal liquidity at ~4x the IPO price while retaining voting control. This is the single cleanest governance red flag in the file.

---

## 4. Top Operational Risks

1. **Refinancing / liquidity risk is existential, not theoretical.** ~**$46.9B of debt** against Q3 2026 interest expense of **$846M** (Q2: $640M interest vs **$128M** adjusted operating income) and 2026 capex guided to **$35–39B**. Unsecured bonds yielding **~15%**, CDS above **10% of notional per year** — a level S&P Global Market Intelligence characterized as a sign of **credit distress**. Growth is funded by the capital markets; if access closes, the backlog cannot be built. Beta of **7.67** confirms the equity is a levered proxy on this single variable.
2. **Customer concentration remains acute despite improvement.** Top customer = **30% of Q3 2026 revenue** (Microsoft), down from 36% and from **67% in FY2025** — real progress, but the $132.5B backlog is still concentrated in a handful of hyperscalers/OpenAI, several of whom are themselves the counterparties on prepayments. A single hyperscaler capex revision (Microsoft already spooked the group once) can invalidate a large share of contracted revenue.
3. **Delivery execution and single-source supply chain.** Core Scientific's Denton buildout ran months late (TCEQ-violating, ~130MW live vs. contracted expectations), guidance was cut in Nov 2025, and management has admitted a "capacity crunch." 4.6GW of contracted power must be converted to live revenue on schedule; every quarter of slippage pushes revenue recognition out while interest accrues. GPUs are **single-sourced from Nvidia** — a supplier that is simultaneously an investor, creating both allocation risk and related-party optics. **Cybersecurity** exposure is high inherent-value (critical AI infrastructure) with no disclosed material incident — a genuine blind spot, not a clean bill of health.

---

## 5. Reputational Risk Assessment: **HIGH**

- **CRWV is the designated proxy for the "AI bubble."** Michael Burry publicly named CoreWeave, Nvidia and Nebius and declared "I told you so" as the selloff spread (Nov 19–21, 2026). Being the named short thesis of the most famous bear investor of the cycle is a durable brand tax on institutional sponsorship.
- **~67% below its June 2025 peak**, ~30% down in October 2026 alone, with 20%+ single-day swings in both directions (Nov 23: +22% on Nvidia news). A stock that moves on Nvidia personnel headlines rather than its own disclosures signals a narrative-driven shareholder base.
- **The "$3.3B founders' cash-out" story is now a mainstream press narrative** (Bloomberg, 24/7 Wall St., Boardroom Alpha), landing directly against a shareholder base sitting on losses. That is precisely the sentiment that fuels class actions, activist pressure and hostile press cycles.
- **ESG/environmental friction:** TCEQ emissions enforcement at Denton, data-center power and water backlash, and state moratorium risk after the midterms — CoreWeave is a natural target for local opposition because its facilities are large, loud and grid-intensive.
- **Genuine offsets:** revenue +168% to $3.66B in Q3 2026, backlog **$132.5B (+138% YoY)**, RPO $132.3B, 4.6GW contracted, adjusted operating margin ~10.35% ahead of expectations, and guidance met or beaten every quarter of 2026. Management has delivered operationally. But reputational capital has been spent on the disclosure missteps, not on execution.

---

## 6. Overall Non-Financial Risk Rating: **HIGH** (upper end of the band; **Critical** on any confirmed enforcement action or failed refinancing)

The rating is driven by the **coincidence**, not the sum, of three weaknesses: (a) **Weak** governance with ~71–80% founder voting control, CEO/Chair duality and a three-person outside board; (b) an **active securities fraud class action** alleging concealment of construction delays, with a **second investigation wave** on debt-cost disclosure and an SEC explicitly signaling AI-disclosure enforcement; and (c) **credit-market distress** (15% unsecured yields, >10% CDS) that makes the growth model dependent on continued capital access. Layer on $3.3B of insider selling with zero insider buying and no shareholder mechanism to discipline any of it. Non-financial risk here is not a tail — it is the primary determinant of equity value.

**Why not outright Critical today:** no formal SEC/DOJ enforcement action is documented, audits are unqualified to our knowledge, no restatement has occurred, and operating execution (revenue, backlog, margin) has been genuine. Those are real mitigants.

---

## 7. Red Flags Requiring Escalation

1. **$1.3B reclassified out of deferred revenue into "customer liabilities" (Q1 2026) with essentially no explanatory narrative.** This is my top escalation. Deferred revenue is the accounting proxy investors use to validate the "contracted backlog = revenue visibility" thesis. Moving $1.3B to a less-transparent liability bucket — where refund, return-to-deferred-revenue, or recognition treatment is unclear — **weakens the audit trail between the $132.5B headline backlog and reported revenue**. Combined with a class action alleging disclosure of exactly this kind, and an SEC focused on AI infrastructure accounting, this footnote deserves forensic review. No restatement has occurred; that is not the same as "clean."
2. **Securities fraud class action with a hard-evidence timeline** (Core Scientific flagged delays Feb 2025; CoreWeave public statements contradicted; WSJ Dec 16, 2025; $14B cap loss). Multi-firm, class period through Dec 2025, with discovery running 2026–2027. Escalate for reserve/settlement modeling and for D&O insurance adequacy.
3. **Second investigation wave on borrowing-cost disclosure (Oct 2026)** overlapping a 15% bond yield and a $0.7B convertible upsizing. Disclosure chronology (capex raise Aug 11 → convert upsized Sept 17 → yield spike revealed Oct 13) is the kind of sequence regulators examine for selective or delayed disclosure.
4. **$3.3B founder selling against zero insider purchases**, executed mechanically through the drawdown — while a new CIC severance plan grants **100% equity acceleration**. Insiders are simultaneously de-risking personally and raising their payout on a takeover. Materially misaligned with public shareholders.
5. **Governance structure removes all shareholder recourse:** 10-vote Class B shares, ~71–80% founder control on ~20% of economics, CEO/Chair duality, three outside directors. No proxy contest, no say-on-pay defeat, no independent oversight is achievable. Treat management statements as un-auditable by shareholders.
6. **Credit distress signals with an insider credit-only purchase.** Venturo's ~$30M bond buy alongside equity sales is a structural signal that recovery value sits above the equity. Escalate to credit desk for cross-check.
7. **Policy/regulatory overhangs with concrete revenue paths:** Southeast Asia export curbs, Texas moratorium risk post-midterms, TCEQ enforcement at Denton. These are asymmetric and largely outside management control.
8. **Nvidia person-dependency and circular-financing optics.** The Nov 23 +22% move was driven by Nvidia's CEO reinstatement, not CoreWeave news — evidence the equity is priced off a counterparty's governance. Combined with Nvidia being supplier, shareholder and demand enabler, CRWV sits at the center of the circular-financing disclosure issue the SEC has publicly targeted.

---

**Bottom line for the investment memo:** CRWV's financial risk is well understood and heavily debated; its **non-financial** risk is underappreciated. A controlled company with a three-person outside board, a sitting securities fraud class action, a 15% cost of capital, and founders who have extracted $3.3B while retaining voting control offers public shareholders **no governance mechanism to protect themselves if the backlog fails to convert**. Any position requires explicit sizing for governance-driven downside and monitoring triggers on (i) 8-K/10-Q legal-proceedings language, (ii) deferred-revenue/customer-liability footnote evolution, (iii) bond yields and CDS, and (iv) any further Form 4 selling.

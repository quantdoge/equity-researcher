# Nonfin Risk Analyst

- Symbol: OKTA
- Elapsed: 74.2s

---
# OKTA — Non-Financial Risk Assessment
**As of: November 2026 | Okta, Inc. (NASDAQ: OKTA) | Technology / Software–Infrastructure | Market cap ≈ $33.7B | 6,366 FTEs | CEO & Chair: Todd McKinnon**

---

## 1. Governance Quality Rating: **ADEQUATE** (trend: improving, with residual concentration)

**Board composition (7 directors, 5 independent ≈ 71%):**
- Non-independent: Todd McKinnon (co-founder, **Chair + CEO**) and Frederic Kerrest (co-founder, Vice Chair).
- Independent: Tony Bates, Rob Bernshteyn, Helen Riley, Paul Sagan, David Schellhase (**Lead Independent Director**).
- Refresh is genuine: Bernshteyn and Sagan were added in 2026; Bates and Schellhase were the Class III nominees re-elected at the June 18, 2026 AGM. Boardroom Alpha grades the board **B‑**.

**Positives:**
- Lead Independent Director exists and is not a figurehead — Schellhase made the only open-market insider purchase in the last 12 months (see §3), i.e., he is eating his own cooking.
- Compensation architecture is shareholder-aligned on paper: multi-year **PSUs with relative TSR tranches**, payout caps, true-up mechanics, clawback policy, stock ownership guidelines, independent comp consultant, and **removal of single-trigger change-in-control cash** payments. Say-on-Pay support was **94.6% in 2025**; all four 2026 ballot items passed.
- Equity plan amendment **removed the automatic evergreen share increase** (a pro-shareholder change), and E&Y was ratified as auditor (FY ending Jan 31, 2027).

**Concerns:**
- **CEO/Chair duality held by a co-founder** — the single clearest governance weakness. Mitigation (LID + 71% independence) is real but structurally weaker than an independent chair.
- **Dual-class structure persists.** Per the 2026 annual-meeting 8-K, Class B holders were still entitled to **ten votes per share**. Founder super-voting blunts the practical force of the independent majority. *Gap: I could not retrieve the charter's sunset trigger — worth confirming whether a 10-year post-IPO sunset (≈April 2027) is imminent, which would be a positive catalyst for governance quality.*
- **Pay optics:** the 2026 proxy discloses a "substantial CEO base salary increase" (framed as bringing him into market range) plus other NEO raises and a share increase to the 2017 plan — while the company has run **three consecutive years of restructuring/layoffs** (7%/≈400 roles in 2024; ≈180 roles in Feb 2025). That combination is a live proxy-advisor and reputational irritant, even with strong historical support.

---

## 2. Regulatory & Legal Risk Summary — **Moderate, de-escalating**

**Active company-level enforcement: none found.** EDGAR full-text search for SEC enforcement actions naming OKTA returned zero results. No open securities class action: the principal case, *In re Okta, Inc. Securities Litigation* (Exchange Act §§10(b)/20(a), alleged inadequate cybersecurity controls and misleading Auth0/sales-turmoil disclosures), **settled for $60M with final judgment November 19, 2024**. A separate 2023 cyber-related suit was dismissed.

**The material live item is a former-employee matter, not a company charge:** on **September 15, 2026**, the SEC announced settled insider-trading charges against **Andrew T. Neller** and **Jack E. Alexander**, two former Okta sales managers, for trading ahead of Okta earnings announcements. Okta is not a defendant, but this is a **repeat pattern of MNPI leakage from the revenue organization** — read it as an information-barrier/internal-controls finding, not merely a third-party event.

**Structural regulatory exposure (no fines identified, but real):**
- Okta acts as a **processor/custodian of authentication data for 20,000+ organizations**, including government and regulated financial clients → GDPR/CCPA, FedRAMP/public-sector obligations, and EU **DORA** third-party-ICT requirements land on Okta as a critical vendor.
- Post-2023 breach, customer contracts and regulators increasingly demand security-assurance artifacts; contract renewals carry implicit compliance conditions.
- *Gap: I could not retrieve the 10-K/10-Q legal-proceedings footnote through available tooling — no confirmed new subpoenas or DOJ inquiry, but this is unverified rather than cleared.*

---

## 3. Insider Activity Analysis — **BEARISH SIGNAL (one notable exception)**

**Trailing 12 months to Nov 19, 2026: 7 insiders sold $58.1M across 26 filings; one director bought $267.4K.** Sell:buy ratio ≈ **217:1 in dollars, 26:1 in filings.** Critically, **26 of 26 sales were pre-arranged 10b5-1** — no evidence of opportunistic, event-timed dumping.

| Insider | Role | Sold | Notes |
|---|---|---|---|
| Todd McKinnon | CEO/Chair | **$21.5M** (4 filings) | 10b5-1 plan adopted **April 8, 2026**; last sale Sep 22 @ $193.48 |
| Brett Tighe | CFO | **$21.4M** (3 filings) | 80,000 sh @ $160.97 (Sep 2); 65,000 sh @ $117.25 (Jun 8) |
| Larissa Schwartz | Officer | $5.2M (8) | Disciplined monthly-style trimming |
| Eric Kelleher | Officer | $4.6M (7) | — |
| Shibu Ninan | CAO | $3.3M (2) | Most recent sale Oct 7 @ $217.80 |
| J. Addison | CRO | $1.8M (1) | — |
| **David Schellhase** | **Director/LID** | — | **Bought $267.4K @ $72.04 (Apr 16, 2026)** |
| Shellye Archambeau | Director | $212.5K (1) | Small, 10b5-1 |

**Interpretation:** The complete absence of discretionary open-market buying from the CEO or CFO — despite a 131% one-year TSR and S&P 500 inclusion — is the relevant signal. Insiders sold into strength at $117–$218, mostly *below* today's ~$207, so this is diversification rather than a bearish call on near-term fundamentals. But the **CFO's $21.4M of sales in his first years in seat**, the CAO selling at the highs in October, and the near-total absence of buys mean management's revealed preference is to reduce exposure. The LID's April purchase at the cycle low is the one genuine counter-signal and is worth weighting.

---

## 4. Top Operational Risks

- **Availability as an existential single point of failure.** A **major Okta outage began November 12, 2026**, degrading cells and MFA with full recovery reported roughly **two days later** (third-party status trackers; Okta's own status page is the primary source and I could not parse it). For a product that *is* the login gate for 20,000+ customers, a multi-day authentication degradation is a direct revenue/SLA-credit/churn event and, per the November 18–19 coverage, the market is now explicitly trading cybersecurity names on outage news. Secondary email-delivery incidents (August 2026) suggest reliability hygiene, not just bad luck.
- **Breach history concentrated in the support layer.** LAPSUS$ (March 2022, third-party support engineer) and the **September–October 2023 support case-management breach, which ultimately exposed data on effectively all support-system customers**, both originated in customer support/third-party access — the same soft spot. No confirmed 2026 breach in my searches, but the pattern (not the one-off) is the risk: privileged support tooling plus contractor access remains the attack surface most likely to produce the next trust-destroying event.
- **Key-person and talent erosion.** The founder-CEO-Chair remains the strategic and cultural center of gravity; simultaneously the company has cut headcount three years running while its CAO, CRO, and other officers sell stock. Institutional knowledge loss in security, support, and customer-success functions is exactly where controls degrade silently.

*(Supporting context: Q2 FY27 revenue $805M, +11% y/y; cRPO +14%; RPO +17%; $1M+ ACV customers +22% — the franchise is healthy, which is why these risks are about durability, not solvency.)*

---

## 5. Reputational Risk Assessment — **Elevated but currently improving**

- **"Trust" is the entire brand.** Okta sells identity assurance; a breach or a multi-day outage is not a product defect, it is a category-level credibility event. The 2023 disclosure sequence (134 customers, then effectively all) did measurable damage to that asset.
- **The 2026 "SaaSpocalypse" was a narrative shock, not a fundamental one.** The February 2026 AI seat-compression rout wiped ~$1T from software; OKTA traded between **$62.93 and $232.13** over twelve months (~19 moves >5%) before recovering to ~$207 with **+131% 1Y TSR**. The lesson: OKTA's multiple is hostage to a narrative about whether AI agents obviate per-seat identity pricing. Okta's counter-positioning (Cross App Access protocol, AI-agent identity) is the right strategic answer but has not yet removed the narrative risk.
- **Sentiment is event-driven and reflexive** — the stock rallied 3.6% on November 19 partly on *rival/industry* news and infrastructure-outage anxiety. That cuts both ways on the next Okta incident.
- No consumer-backlash, ESG, or product-liability controversy of note; layoff-related employee sentiment (Glassdoor) is a mild culture signal.

---

## 6. Overall Non-Financial Risk Rating: **MODERATE**

Justification: no active company-level regulatory enforcement, no open securities litigation, no evidence of accounting irregularity or material weakness, a majority-independent board with a functioning LID, and genuinely shareholder-aligned compensation design — these rule out High. But the combination of a **CEO/Chair-founder with super-voting stock**, a **~two-day authentication outage nine days ago**, a **support-layer breach history**, and **26 filings of insider sales with essentially no discretionary buying** rules out Low.

---

## 7. Red Flags Requiring Escalation

1. **Nov 12, 2026 outage (~2 days to full recovery).** Demand the post-incident review, blast radius (cells/regions, MFA), SLA credits, any customer attrition, and whether an 8-K/Item 1.05 cyber disclosure was triggered. This is the highest-urgency, lowest-visibility item on the list.
2. **Repeat MNPI leakage from the sales organization** — SEC settlements against two former sales managers (Sept 15, 2026). Ask for evidence of remediation of information barriers and pre-earnings trading surveillance; a third case would suggest a control failure the board is not fixing.
3. **Insider selling profile.** 26:1 sell:buy filings, $58.1M out, zero discretionary CEO/CFO purchases; the CEO's 10b5-1 plan was adopted April 8, 2026 (near the drawdown low). Confirm whether any plan was modified during the year and whether Tighe's 80,000-share sale reflects 10b5-1 exhaustion (i.e., is more supply coming?).
4. **Governance concentration.** Vote/engagement stance on CEO-Chair duality and the Class B 10-vote structure; confirm the sunset trigger. Also flag the CEO base-salary increase concurrent with multi-year headcount cuts — a proxy-advisor flashpoint despite 94.6% prior support.
5. **Equity plan amendment** expanding the 2017 Plan share reserve (evergreen removed, but gross dilution increased) — monitor burn rate and share-based comp as a % of revenue.

---

### Confidence and Data Gaps
**High confidence:** board composition/independence, LID identity, annual-meeting outcomes and pay design, insider transaction detail (per-insider dollar values, 10b5-1 status), SEC enforcement search (nil at company level), Sept 2026 former-employee settlements, $60M securities settlement final in Nov 2024, price/volatility history, S&P 500 inclusion (Oct 28, 2026), Q2 FY27 fundamentals.
**Not verified — treat as gaps:** 10-K/10-Q/***DEF 14A* text was unavailable through the filing tool (all three returned "not found"), so the legal-proceedings footnote, any disclosed material weakness, restructuring charges, and the 2026 Say-on-Pay actual percentage are unconfirmed (2025 = 94.6%). The Nov 12 outage duration comes from third-party status trackers, not Okta's own disclosure — verify directly. No GDPR/FTC/DOJ/state-AG action was found, but absence in search is not absence in fact. Class B sunset mechanics are unconfirmed.

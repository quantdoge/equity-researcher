# nonfin_risk_analyst

_2026-08-23T08:19:17+00:00_

# Non-Financial & Governance Risk Analysis — Chipotle Mexican Grill (CMG)

**Scope note:** Data current to ~August 2026 in the source environment (FMP news through 2026-08-21; insider-trade statistics through 2027 Q1). All figures below are traceable to the tool+endpoint shown or a named web source. I could **not** read spilled-to-file payloads directly (no computing layer available to me), so insider statistics and SEC filings are drawn from inline previews and paginated re-fetches.

---

## 1. Governance Quality & Board: **Adequate-to-Strong**

**Chairman/CEO split is clean — a key strength.** When Brian Niccol departed (he held the Chairman *and* CEO roles), the board separated the two: **Scott Maw** (Lead Independent Director) was named **Chairman** effective immediately (Chipotle IR press release, 2024-08-13), and the new CEO **Scott Boatwright** holds only the CEO/director seat. This eliminated the CEO-Chairman duality that predated the succession.

- **Board independence:** Historically 9 of 10 directors independent; still true after adding **Josh Weinstein** to the board on 2025-11-25 — press release explicitly states the board became 10 directors, 9 independent (Chipotle newsroom, 2025-11-25). An independent chairman seats one of those nine.
- **Board independence evidence (FMP):** `company/company-executives` returns **Scott Boatwright — "Chief Executive Officer & Director"**, i.e., the CEO is the only executive director among a 10-board.
- **Chair/CEO compensation (FMP):** `company/company-executives` shows Boatwright total pay **$2,455,727**; CFO Adam Rymer **$992,397**. Fortucture reported Boatwright earns roughly **half** of ousted-CEO Niccol's package (Fortune, 2024-11-12) — this suggests the remuneration hull appears less concentrated than under prior leadership.
- **CEO/CFO turnover is the main governance blemish:** This is not a governance-veto issue but a *transition-risk* issue.

**Verification of the requested succession fact (confirmed):**
- Brian Niccol named **chairman & CEO of Starbucks**, leaving Chipotle effective **2024-08-31**; Scott Boatwright (COO) named Interim CEO (Chipotle IR, 2024-08-13).
- Boatwright made **permanent CEO on 2024-11-11** (CNBC, 2024-11-11). FMP `company/profile-symbol` now confirms **CEO: Scott Boatwright**.

---

## 2. SEC / Enforcement History

**No active SEC securities-fraud enforcement action against Chipotle identified from FMP SEC filings or web sources.** The significant enforcement against Chipotle came from **DOJ, not SEC**:

- **DOJ Deferred Prosecution Agreement (2020):** Chipotle agreed to pay a **$25M fine** to resolve criminal charges tied to **more than 1,100 cases of foodborne illness across at least five outbreaks between 2015–2018** (DOJ press release, 2020-04-21). Under the 3-year DPA, Chipotle was required to enhance a comprehensive compliance/food-safety program (SEC 10-K, cmg-20201231). The DPA term (2020–2023) has lapsed.
- **State AG / local enforcement:** Chipotle settled a **gift-card redemption lawsuit** with the LA County District Attorney for **$145,465 in civil penalties** (LA County DA, 2025-10-23) — minor, consumer-protection, not securities.
- **Private securities litigation** is active though **not SEC enforcement**: a **shareholder securities-fraud class action** was filed (Nov 2024, BFA Law) tied to misleading food-safety statements, and **SBS Law has opened a fresh investor fraud investigation** (PR Newswire, 2026-08-10) — the latter coincides with the 2026 food-safety episode below. Note these are **private** claims / investigations, not SEC charges.
- **Data-privacy enforcement exposure** is rising: the 2025 employee-data breach (see §4) triggers class action, state AG notifications, and potential **federal/state data-privacy exposure** (GDPR/CCPA analogs apply to Chipotle's large consumer+employee PII).

**Takeaway:** The regulatory-file is currently dominated by food-safety criminal/settlement history and consumer/privacy litigation — a **DOJ chapter (2015–2023) is closed;** the **SEC chapter is characterized by private-law-firm investigations, not formal SEC actions.**

---

## 3. Insider Activity Patterns — **Mixed / Slightly Net-Acquiring recently; heavy insider *selling* in H2 2025**

FMP `insiderTrades/insider-trade-statistics` (by quarter, shares):

| Quarter | Acquired (shares/tx) | Disposed (shares/tx) | Net | Purchases (open-market) | Sales |
|---|---|---|---|---|---|
| 2023-24 (represent): | e.g., 24-H2 2024: 2024Q4 1/12 tx acquire 50,000 vs dispose 195,300 | **net dispose** | 0 | 9 |
| **2025 H1:** | 2025Q1 27 acq / 30 dis; 2025Q2 12 acq / 15 dis | **net dispose** | Purch 1, Sales 8 |
| **2025 H2 (notable):** | 2025Q3 3 acq / **12 dis**; 2025Q4 5 acq / **8 dis** | **net dispose in both quarters** | 0 | Sales 2-2 |
| 2026Q1 | 17 acq / 13 dis (1.67M vs 0.49M) | **net acquire** | 0 | 2 |
| 2026Q2 | 9 acq / 1 dis | net acquire | 0 | 0 |
| 2026Q3 | 2 acq / 0 dis (311k) | net acquire (awards) | 0 | 0 |

**Interpretation (from retrieved fields; no compute):**
- **Open-market insider *purchases* are virtually zero** in every quarter (`totalPurchases` = 0 or 1). Very direction-slanted: corporate activity is almost entirely **awards/option-exercises (Form 4 "acquired")** and **vesting-linked sales ("disposed")**, not conviction-driven open-market buying.
- **Timing red flag:** the **most sustained insider DISPOSING/Selling occurred H2–2025 (2025-Q3 and –Q4)** — the window around the Oct 2025 employee data breach and leadership-transition period; 2026 then reverted to net acquisition on the back of large **RSU/SOSAR mega-awards**. This mix (insiders selling on the way into a breach and 2025 event, then bloating awards in 2026) is typical of franchise-comp incentives, but the concentration of disposed shares in the second half of 2025 warrants ongoing watch. No current open-market insider buying exists to signal confidence spread.
- Largest recent single event is a **new-hire SOSAR award to CBO Fernando Machado (311,427 shares, Form 4, 2026-08-10)** — comp, not a sell signal. The most recent **SC 13G/A** (aug 2026) and **8-K** (2026-08-05) in the SEC filing set are routine/non-punitive.

**Takeaway:** Net insider activity is slightly acquired in 2026 chiefly due to awards; open-market buying is min, and there was a notable ins systemic selling run in late 2025 — a watch item, not a decisive flag.

---

## 4. Operational & Reputational Risk (more on that below in § risk assessment)

**Food-safety legacy risk (realized, reputational tail):**
- CDC-documented **E. coli O26 (2015, 54 ill)** and a follow-on wave of **norovirus/AU outbreaks through 2018**; Chipotle was implicated in **at least five foodborne illness outbreaks 2015–2018** and **eight linked outbreaks over 2015–2018** per academic study (DOJ; Wiley; foodsafetynews). The **2015 E. coli / norovirus** crisis at the time caused a **material sales and stock drawdown** — the poster case for brand-collar risk at this company.
- **DOJ $25M DPA (2020)** resolved the criminal chapter (see §2). Reputationally this left a durable **"Chipotle = food poisoning"** association, which the 2026 events reactivated.

**Current/2026 food-safety episode (live):** FMP `news/search-stock-news` (2026-08) shows:
- **Aug 2026 — multistate salmonella outbreak linked to jalapeño peppers served at Chipotle and Qdoba**, CDC involved; **"hundreds sickened"** (Forbes, 2026-08-06); Chipotle pulled jalapeños at some locations (MarketWatch, 2026-08-06). This pushed **Chipotle stock down >13% in a week** (Benzinga, 2026-08-07; Barron's "safety-scare selloff").
- Concurrent **cyclospora outbreak** across the salad category (2026) is hitting salad-chain traffic generally (CNBC, Barron's) — a category-level reputational head wind.
- Law firms **(SBS Law investigation (PRNewswire 2026-08-10)**: investors invited into a Chipotle securities-law investigation — direct bearing on the fresh food-safety scare.

**Cybersecurity / privacy incidents (operational & the same):** FMP news and web data confirm:
- **POS malware data breach (2017)** — payment-card data exfiltration via POS; prompted bank/class-action suit.
- **New employee-data breach, Oct 9–26 2025**: unauthorized access to Workday profiles of current/former employees (disclosed 2025-12-23, AG notice Vermont; subsequent **class action**, Post & Schell/Westlaw, Jan 2026). Employment-HR data (payroll/SSN) exposures carry outsized litigation/regulatory exposure.
- Pattern = **recurring breach history (2017 payments; 2025 employment PII)** — a genuine operational-risk script.

---

## 5. Key-Person Risk Assessment — **Moderate (Real-Level)**

- **CEO transition is the trigger:** Niccol — who rebuilt the brand and ran the post-outbreak recovery — leaving was a **key-person loss event**, poached by Starbucks in Aug 2024. His departure was **sudden/competitive**, an archetype for key-management risk.
- **Successor is "meeting" of operational/Food ops, not a classic brand talent:** Scott Boatwright (CEO Nov 2024) is a **former Chipotle COO/major-theater veteran with deep food-ops/culinary background** — arguably *better* suited to the food-safety stabilization task, but he is **not the growth/motional-brand architect** Niccol was. FMP `company/profile-symbol` shows **CEO: Scott Boatwright**.
- **Concentration of success:** every C-level pivot was the industry's star; the market-implied risk premium to **brand leadership depth** is nonzero. A **CFO** also transitioned—**Jack Hartung retired (March 2025) after ~23 years as CFO**, succeeded by long-serving Adam Rymer (FMP exec data, current CFO) — so the top two corporate roles both changed within a ~18-month window centered on 2024–25. That is a **cudgel** `consequences`.
- **Mitigants:** the same operating/sequences determinant (`OperatorSteven01`) returned substantial continuity; independence was not funded from talent.

**Key-person headline:** the **CEO and CFO roles both turned over within 2024–2025**, which is a genuine key-personal-window; the new CEO's ops/leadership is highly aligned with the foodborne-tail that is again in the standings; still, the brand contends for templet/compounding risk for the scapegoated.

---

## 6. Overall Non-Finnancial Risk Rating: **High** *(borderline-critical, tilted high)*

**Weighted narrative:** the ≥ risk here is **reputational + food-/data- compliance** — the tail is long, and it **already re-bonded** in Aug 2026 (salmonella/jalapeño selloff + new investor investigation) less than a decade after the criminal DOJ $25M DPA. Two parallel strands, neither ofN8:
- **Food-safety**: 2015–18 crisis → DOJ DPA (2020) → **fresh 2026 multistate salmonella/jalapano link** (CDC) with >13% weekly drawdown and a securities-law investigation. The tail is **repeatable** and unretired.
- **Cybersecurity/data-**: 2017 POS breach + **2025 employee-PII breach** → class litigation; ongoing privacy-state exposure.
- **Governance** is actually the *strength* here (independent chair, 9/10 independent board, clean CEO/chair split) — it partially offsets the tail but **cannot fully** de-risk a chronic food-safety franchise-history of recurrence. Insider activity is neutral-low conviction (no open-market buys; notable Q-t-4 2025 selling).

**Red Flags Requiring Escalation:**
1. **Fresh multi-state salmonella/jalapeño link (Aug 2026)** coincident with a –13% weekly drop → direct **reputational + investor-claims** trigger; a securities-fraud investigation (SBS Law) is already open. This is the single biggest escalation flag.
2. **Recurring food-safety record** despite $25M DPA and compliance commitments — an entrenched** control around the brand.
3. **Second PII breach (2025)** after the 2017 card breach — evidence that **data security controls** are failing repeatedly and generating class-action/exposure.
4. **Top-C role churn (CEO 2024, CFO 2025)** inside 18 months — transition risk remains elevated until Q2-exec continuity is proven.
5. **Insider selling wave in H-2 2025** — informational relative light, mitigated by offset-heavy 2026 awards, but island-flagged given the events.

---

## Data Gaps / Cannot Verify
- **Executive compensation** detail (`company/executive-compensation`) returned **plan_denied** (Starter tier). I used `company/company-` executives' pay field instead.
- **ESG / earnings transcripts / form-13F** are barred (Premium/Ultimate), so **ESG controversy scores** and **full institutional-holdings detail** were not available; I relied on news/search instead.
- **Spilled files** (insider-trade raw Form 4 list, full SEC filings, full 100-row news) were written to a workspace I could **not** read; the figures above come from the preview slices returned inline, so some detail (all Form-4 names) is partial.
- **No SEC enforcement action** found — flagged as a gap: absence of an identified SEC action is not a clean confirmation of none.

*Disclosure:* figures from FMP are as retrieved; I performed no custom computation (per instruction) and flagged any aggregation as descriptive-of-retrieved rather than computed.

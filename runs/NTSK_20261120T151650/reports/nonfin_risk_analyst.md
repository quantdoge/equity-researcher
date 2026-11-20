# Nonfin Risk Analyst

- Symbol: NTSK
- Elapsed: 46.6s

---
# Netskope, Inc. (NASDAQ: NTSK) — Non-Financial Risk Assessment

**Company snapshot:** Cloud/SASE security provider (Netskope One), IPO 2025-09-18, ~$9.8B market cap, 3,281 FTE, founder-led. FY ends Jan 31. Beta 2.99. Domiciled US (Santa Clara, CA).

---

## 1. Governance Quality Rating: **Adequate** (structurally weak, ownership-aligned)

**Evidence of concern:**
- **Combined CEO/Chairman:** Co-founder Sanjay Beri holds both roles — power concentration typical of founder-led IPOs.
- **Dual-class share structure:** Public float is Class A; Beri holds Class B (1,940,620 shares direct + 22,288,889 via the 2012 Sanjay Beri trust per 13G/A; ~10.4% reporting stake) with super-voting rights. Founder/VC Class B bloc controls outcomes irrespective of Class A economics.
- **Staggered/classified board:** 2026 annual meeting elected only two Class I directors (Beri and Arif Janmohamed) to serve until 2029 — anti-takeover entrenchment in year one of listing.
- **Sponsor-captured board seats:** Will Griffith (ICONIQ founder) and Janmohamed (Lightspeed) sit as VC-designated directors while simultaneously executing large share sales (see §3). Their interests are liquidity and fund-return timing, not Class A holders.
- **Thin independent bench** disclosed publicly (Kimberly Alexy is the most visible independent). Board only ~18 months into public-company discipline; first proxy not yet retrievable.

**Mitigants:** High insider/founder ownership (~10%+ CEO, sponsors ~60%+ combined) means genuine skin-in-the-game; CEO certification under SOX 302 executed cleanly with no disclosure of material weaknesses or fraud in the Sept 2, 2026 10-Q; no restatements, no auditor turnover, no whistleblower disclosures surfaced.

**Data gap:** DEF 14A and FY2026 10-K were not retrievable through available feeds (EDGAR returned 403; tool reported "no 10-K/DEF 14A found"). Compensation structure, related-party transactions and full board independence could not be verified. **Treat governance compensation alignment as unconfirmed.**

---

## 2. Regulatory Risk Summary

| Vector | Status |
|---|---|
| SEC enforcement / DOJ | **None found.** EDGAR full-text search for enforcement actions returns zero hits. |
| Securities litigation | **Watch item.** Johnson Fistel (Mar 11, 2026) publicly announced a securities investigation into whether Netskope officers' statements complied with federal securities law, citing FY2026 GAAP operating loss of **$652.6M vs $255.7M prior year** (‑92% GAAP operating margin) disclosed despite continued revenue growth. No filed complaint or appointed lead plaintiff confirmed. Low-to-moderate probability of formal class action; typical IPO-year nuisance suit profile. |
| Privacy/data regulation | Structural exposure — as a security processor for enterprise data, any GDPR/CCPA failure is company-critical, not incidental. No enforcement action found. |
| Pending approvals | None identified (no FDA/FCC-style gates). |
| IP / patent | **PTAB proceeding IPR2026-00474** (filed Sept 15, 2026) naming Netskope — patent validity challenge in the SASE/zero-trust space. Immaterial today, monitor for competitor-driven IP conflict. |
| Export/antitrust | No active matters found. |

Regulatory posture is **clean but unseasoned** — no fines, no subpoenas, no consent orders. The risk is prospective (disclosure quality during a volatile first year), not retrospective.

---

## 3. Insider Activity Analysis — **Net selling, directionally negative**

Form 4 activity over the trailing 12 months (aggregated; dollar amounts estimated at reported average prices):

**Sales (~$36M):**
- **CEO Sanjay Beri:** 630,321 sh @ $17.16 (~$10.8M, 12/31/25) + 210,076 sh @ $17.20 (~$3.6M, 1/6/26) — **~$14.4M**
- **CFO Andrew Del Matto:** 149,210 sh @ $17.20 (~$2.57M) + 49,875 sh @ $17.16 (~$0.86M) — **~$3.4M**
- **CRO Raphael Bousquet:** 10,239 sh @ $16.67 (~$0.17M)
- **Lightspeed entities / director Janmohamed:** 1,650,000 sh @ $9.1513 (~$15.1M, 6/12/26); 229,696 sh @ $12.21 (~$2.8M, 7/8/26); 10,621 sh @ $14.90 (~$0.16M, 9/11/26) — **~$18.1M**

**Purchases (~$11M disclosed; ~4.0M shares across 8 filings per press):**
- **ICONIQ Strategic Partners VIII / director W. Griffith:** 306,399 sh @ $11.82 (~$7.2M, 7/8/26) + 306,399 sh @ $12.29 (~$3.8M, 7/10/26)

**Interpretation — three flags:**
1. **Timing:** CEO and CFO sales clustered at $17.16–$17.20 in late Dec 2025/early Jan 2026, roughly ten weeks before the March 11 FY2026 print that triggered a **‑21% single-day drop** ($12.13 → $9.55) and a slide to $7.73 by Mar 27. Presumably 10b5-1 plans adopted at/after IPO, but the optics are poor and are precisely what the plaintiff bar is probing.
2. **Selling is now below the IPO price:** Lightspeed sold at $9.15 in June — sponsors took liquidity 40% below issue. That is a signal about sponsor conviction, not valuation discipline.
3. **New overhang:** On Sept 22, 2026 ICONIQ **distributed 3.09M shares in-kind to its LPs** for no consideration. This converts a stable block into ~3M dispersed holders free to sell — mechanical supply pressure independent of fundamentals.

**Offsetting positive:** ICONIQ's open-market buying at $11.82–$12.29 in July, near the trough, is the single most credible insider signal in the dataset — informed money stepping in at the low.

---

## 4. Top Operational Risks

- **Key-person dependency on the founder.** Beri is co-founder, CEO *and* Chairman, and the public narrative is fused to him. There is no disclosed succession plan and no COO of equivalent public profile. Departure or health event would be a double hit (leadership vacuum + loss of controlling Class B vote anchor).
- **Product-trust risk inherent to being a security vendor.** Netskope sits inline on customer traffic; a compromise of Netskope One is an existential reputational event, not a contained incident. Public CVE history is real but unremarkable: **CVE-2025-15641** (Netskope Client for Windows privilege escalation/anti-tamper bypass) and **CVE-2024-7401** (IdP enrollment authentication bypass). Independent posture score is strong (UpGuard 822/950, grade A). No breach of Netskope itself found. But note the recursive risk: an inline SSE provider is a high-value target precisely because compromising it compromises every tenant.
- **Growth durability / go-to-market churn.** ARR growth decelerating to ~27% with net new ARR at $54M (+10% YoY), against Zscaler, Palo Alto and Cloudflare on all sides. Recent senior GTM turnover and rebuild — a new SVP of Global Channel Sales (Carrie Francey, Nov 10, 2026) and expanded BT International channel reliance — points to a distribution model in transition. Channel dependence concentrates counterparty risk in a small number of global integrators/telcos.

---

## 5. Reputational Risk Assessment: **Moderate**

- **The share-price record is the story.** $22.49 IPO → $7.73 trough (−66% from issue, −72% from the $27.99 intraday high) → $26.52 by Oct 28, 2026 → ~$24 now. A full round trip in 13 months with beta ~3.0. This amplifies every other risk: each drawdown invites plaintiff-firm marketing (Johnson Fistel is already in market), press scrutiny, and employee retention pressure via underwater equity.
- **No ESG/consumer controversy, no product recall, no customer-visible outage campaign found.** Sentiment in coverage is split but fundamentally product-positive — bulls cite differentiated AI-agent security (AgentSkope, Skylight Agent Action Control), bears cite valuation and decelerating ARR.
- **Analyst sentiment is choppy** (Zacks #1 Strong Buy Oct 27; Seeking Alpha downgrade to Hold Nov 19 after a 60%+ rally). Not a reputational issue, but it feeds volatility.
- **Media/legal-marketing risk is the live vector** — the March 11 investigation announcement is indexed permanently against the ticker and will resurface with any guidance miss.

---

## 6. Overall Non-Financial Risk Rating: **MODERATE** (with upward bias)

Nothing here is broken: no enforcement action, no fraud finding, no breach, no restatement, and insider ownership is genuinely high. What keeps this out of "Low" is the *combination* of an unseasoned public company with entrenched dual-class founder control, a securities investigation in market, sponsor insiders selling below IPO price, and a security-product trust profile where a single incident would be company-defining. The rating moves to **High** on either trigger in §7.

---

## 7. Red Flags Requiring Escalation

1. **[HIGH] CEO/CFO sales at $17 in late Dec 2025/Jan 2026, ten weeks before a ‑21% earnings-day collapse.** Establish whether 10b5-1 plans were adopted pre-IPO and confirm no acceleration/modification occurred in Q4 FY2026. If plans were amended in the window, upgrade to Critical. This is the specific fact pattern the Johnson Fistel investigation is built on.
2. **[MEDIUM-HIGH] FY2026 GAAP operating loss widened 155% to $652.6M (‑92% margin)** while revenue grew. Confirm the driver is non-cash SBC/IPO-related and not expense capitalization or ARR recognition practice. Request the FY2026 10-K critical accounting estimates and revenue-recognition footnote — **not obtainable in this pass; retrieve before publishing the memo.**
3. **[MEDIUM] Dual-class + staggered board + CEO/Chairman + two sponsor-director seats** = Class A holders have no practical governance recourse. Any related-party transaction or secondary offering approved by this board deserves independent scrutiny.
4. **[MEDIUM] ICONIQ's Sept 22, 2026 in-kind distribution of 3.09M shares** — quantify the free-float increase and monitor subsequent Form 144s/Form 4s for LP-driven supply.
5. **[MEDIUM] Pretax cash-flow optics:** guidance of only $10–20M FY free cash flow against a $9.8B cap leaves no cushion; any operational stumble transmits directly to financing risk.
6. **[LOW] PTAB IPR2026-00474** — identify petitioner and challenged patent family; confirm core SASE patent claims are not at risk.

**Coverage gaps to close:** FY2026 10-K risk factors, definitive proxy (comp structure, board independence, related parties), customer-concentration disclosure, and confirmation of whether any securities class action has actually been filed. SEC EDGAR returned HTTP 403 on direct fetch; these should be pulled from a terminal before the memo is finalized.

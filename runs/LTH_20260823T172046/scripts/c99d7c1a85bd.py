import json, math
from collections import defaultdict

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

out = {}

# ---------- 2. Debt correction & leverage series ----------
# As-reported balance sheets (authoritative XBRL-parsed)
ar = sorted(load("lth_asreported_balance.json"), key=lambda r: r["date"])
print("=== AS-REPORTED BALANCE SHEETS ===")
asrep = {}
for r in ar:
    d = r["data"]
    fin_debt = (d.get("longtermdebtcurrent") or 0) + (d.get("longtermdebtnoncurrent") or 0)
    oplease  = (d.get("operatingleaseliabilitycurrent") or 0) + (d.get("operatingleaseliabilitynoncurrent") or 0)
    cash = d.get("cashandcashequivalentsatcarryingvalue") or 0
    asrep[r["date"][:4]] = {"fin_debt": fin_debt, "op_lease": oplease, "cash": cash}
    print(f"FY{r['date'][:4]} (filed {r['date']}): fin_debt={fin_debt/1e6:8.1f}M  op_lease_liab={oplease/1e6:8.1f}M  cash={cash/1e6:7.1f}M")

# verify the FY2025 double-count identity
fy25 = [r for r in ar if r["date"].startswith("2025")][0]["data"]
ident = (fy25["longtermdebtnoncurrent"] or 0) + (fy25["operatingleaseliabilitynoncurrent"] or 0)
print(f"\nDouble-count check FY2025: longtermdebtnoncurrent + operatingleaseliabilitynoncurrent = {ident/1e6:.1f}M vs standardized longTermDebt = 4041.5M -> {'MATCH (bug confirmed)' if abs(ident-4041452000)<1e6 else 'no match'}")

# Standardized annual + quarterly for the series
bs_a = sorted(load("lth_balance_annual.json"), key=lambda r: r["date"])
bs_q = sorted(load("lth_balance_quarterly.json"), key=lambda r: r["date"])
q226 = bs_q[-1]
fin_debt_q226 = q226["shortTermDebt"] + q226["longTermDebt"]
lease_q226 = q226["capitalLeaseObligationsCurrent"] + q226["capitalLeaseObligationsNonCurrent"]
print(f"\nQ2'26 standardized: fin_debt(ST+LT)={fin_debt_q226/1e6:.1f}M  lease_obligations={lease_q226/1e6:.1f}M  cash={q226['cashAndCashEquivalents']/1e6:.1f}M  totalDebt(FMP)={q226['totalDebt']/1e6:.1f}M")

# Annual EBITDA for leverage
inc_a = sorted(load("lth_income_annual.json"), key=lambda r: r["date"])
ebitda_a = {r["date"][:4]: r["ebitda"] for r in inc_a}
int_a   = {r["date"][:4]: (r["interestExpense"] or 0) for r in inc_a}
ebit_a  = {r["date"][:4]: r["ebit"] for r in inc_a}

print("\n=== CORRECTED LEVERAGE (financial debt = ST+LT debt, excl. operating leases) ===")
lev_series = []
for yr in ["2022","2023","2024","2025"]:
    if yr in asrep:
        fd, ol, ca = asrep[yr]["fin_debt"], asrep[yr]["op_lease"], asrep[yr]["cash"]
        ebd = ebitda_a[yr]
        lev_series.append({"year": yr, "fin_debt": fd, "op_lease": ol, "cash": ca, "ebitda": ebd})
        print(f"FY{yr}: fin_net_debt/EBITDA = {(fd-ca)/ebd:5.2f}x   lease_incl = {(fd+ol-ca)/ebd:5.2f}x   (fin_debt={fd/1e6:.0f}M, op_lease={ol/1e6:.0f}M, cash={ca/1e6:.0f}M, EBITDA={ebd/1e6:.0f}M)")

# TTM
ttm_ebitda = 933246000  # computed last step; recompute quickly
inc_q = sorted(load("lth_income_quarterly.json"), key=lambda r: r["date"])
ttm_ebitda = sum(r["ebitda"] for r in inc_q[-4:])
fd26, ol26, ca26 = fin_debt_q226, lease_q226, q226["cashAndCashEquivalents"]
print(f"TTM Q2'26: fin_net_debt/EBITDA = {(fd26-ca26)/ttm_ebitda:5.2f}x   lease_incl = {(fd26+ol26-ca26)/ttm_ebitda:5.2f}x")

print("\n=== FMP standardized FY2025 (WRONG, for the record) ===")
b25 = [r for r in bs_a if r["date"].startswith("2025")][0]
print(f"standardized totalDebt={b25['totalDebt']/1e6:.0f}M netDebt={b25['netDebt']/1e6:.0f}M -> ND/EBITDA={b25['netDebt']/ebitda_a['2025']:.2f}x  [double-counts op leases]")
print(f"corrected FY2025: fin ND/EBITDA={(asrep['2025']['fin_debt']-232169000)/ebitda_a['2025']:.2f}x, lease-incl={(asrep['2025']['fin_debt']+asrep['2025']['op_lease']-232169000)/ebitda_a['2025']:.2f}x")

# ---------- 3. Interest & coverage ----------
print("\n=== INTEREST EXPENSE & COVERAGE ===")
for r in inc_a:
    yr = r["date"][:4]
    if yr >= "2022":
        ie = r["interestExpense"] or 0
        print(f"FY{yr}: interestExpense={ie/1e6:6.1f}M  EBIT/int={ebit_a[yr]/ie if ie else float('nan'):5.1f}x  EBITDA/int={ebitda_a[yr]/ie if ie else float('nan'):5.1f}x")
ttm_int = sum((r["interestExpense"] or 0) for r in inc_q[-4:])
ttm_ebit = sum(r["ebit"] for r in inc_q[-4:])
print(f"TTM Q2'26 (mapped): interest={ttm_int/1e6:.1f}M  EBIT/int={ttm_ebit/ttm_int:.1f}x  EBITDA/int={ttm_ebitda/ttm_int:.1f}x")
print(f"  [note: Q4'25 quarterly row maps interestExpense=0; annual FY25 file shows {int_a['2025']/1e6:.1f}M]")
# effective interest rate on financial debt
avg_fd_25 = (asrep["2024"]["fin_debt"] + asrep["2025"]["fin_debt"]) / 2
avg_fd_26 = (asrep["2025"]["fin_debt"] + fd26) / 2
print(f"effective interest rate FY25 = FY25 int/{avg_fd_25/1e6:.0f}M avg fin debt = {int_a['2025']/avg_fd_25*100:.2f}%")
print(f"effective interest rate TTM  = {ttm_int/1e6:.1f}M / {avg_fd_26/1e6:.0f}M avg fin debt = {ttm_int/avg_fd_26*100:.2f}%")

json.dump({"lev_series": lev_series}, open("data/_tmp_lev.json","w"))

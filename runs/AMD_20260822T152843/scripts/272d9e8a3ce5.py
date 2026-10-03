import json

# Load balance sheet
with open("data/amd_balance_sheet.json") as f:
    bs = json.load(f)
    
# Load income statement
with open("data/statements_income-statement.json") as f:
    inc = json.load(f)
    
# Load cashflow
with open("data/statements_cashflow-statement.json") as f:
    cf = json.load(f)

# Show relevant fields for FY2025, FY2024, FY2023
for row in bs:
    if row["fiscalYear"] in ["2025", "2024", "2023"]:
        print(f"BS {row['fiscalYear']}: netReceivables={row.get('netReceivables')}, totalCurrentAssets={row.get('totalCurrentAssets')}, propertyPlantEquipmentNet={row.get('propertyPlantEquipmentNet')}, totalAssets={row.get('totalAssets')}, longTermDebt={row.get('longTermDebt')}")

for row in inc:
    if row["fiscalYear"] in ["2025", "2024", "2023"]:
        print(f"INC {row['fiscalYear']}: revenue={row.get('revenue')}, costOfRevenue={row.get('costOfRevenue')}, grossProfit={row.get('grossProfit')}, sellingGeneralAndAdministrativeExpenses={row.get('sellingGeneralAndAdministrativeExpenses')}, depreciationAndAmortization={row.get('depreciationAndAmortization')}, netIncome={row.get('netIncome')}")
        
for row in cf:
    if row["fiscalYear"] in ["2025", "2024", "2023"]:
        print(f"CF {row['fiscalYear']}: netIncome={row.get('netIncome')}, operatingCashFlow={row.get('operatingCashFlow')}, stockBasedCompensation={row.get('stockBasedCompensation')}, depreciationAndAmortization={row.get('depreciationAndAmortization')}")

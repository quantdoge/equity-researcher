
import json

# Read peers
peers = json.load(open('data/cmg_peers.json'))
print("Peers:")
for p in peers:
    print(f"  {p['symbol']}: {p['companyName']} (mktCap=${p['mktCap']:,.0f})")

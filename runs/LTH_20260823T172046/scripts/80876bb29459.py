import json

def load(p):
    with open("data/"+p) as f:
        return json.load(f)

for f in ["news_stock-news.json", "news_search-stock-news.json"]:
    news = load(f)
    news = [n for n in news if n.get("symbol") == "LTH"]
    print(f"=== {f} ({len(news)} LTH rows) ===")
    for n in sorted(news, key=lambda x: x["publishedDate"], reverse=True)[:20]:
        print(f"{n['publishedDate'][:10]}  {n['title'][:105]}")
    print()

# Peer table from screener
scr = load("search_search-company-screener.json")
peers = ["LTH","PLNT","PTON","XPOF","PRKS","FUN","PLAY","LUCK","GOLF"]
print("=== PEER TABLE (screener, 2026-08-21) ===")
print(f"{'sym':5s} {'mcap $M':>9s} {'price':>7s} {'beta':>6s}")
for s in peers:
    r = [x for x in scr if x["symbol"] == s]
    if r:
        r = r[0]
        print(f"{r['symbol']:5s} {r['marketCap']/1e6:9,.0f} {r['price']:7.2f} {str(r['beta']):>6s}")

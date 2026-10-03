import os
print("cwd:", os.getcwd())
print("ls .:", sorted(os.listdir(".")))
for p in ["/workspace", "workspace", "/workspace/lime_valuation.py"]:
    print(p, "->", os.path.exists(p))
if os.path.exists("/workspace"):
    print("ls /workspace:", sorted(os.listdir("/workspace"))[:20])
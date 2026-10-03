import os, json, glob
print("cwd:", os.getcwd())
print("contents:", os.listdir("."))
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".json"):
            print(os.path.join(root, f))
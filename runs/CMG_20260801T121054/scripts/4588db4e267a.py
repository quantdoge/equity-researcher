import os, json
print("Current dir:", os.getcwd())
print("Contents:", os.listdir())
if 'data' in os.listdir():
    print("Data dir:", os.listdir('data'))

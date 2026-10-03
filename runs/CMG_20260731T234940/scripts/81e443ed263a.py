import os, glob
print("CWD:", os.getcwd())
print("Files in cwd:", os.listdir('.'))
if os.path.isdir('scripts'):
    print("Scripts dir contents:", os.listdir('scripts'))
if os.path.isdir('data'):
    print("Data files:", glob.glob('data/*'))
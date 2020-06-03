import os

def scan_dir2(path):
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            for path in scan_dir2(fullpath):
                yield path
    else:
        yield path

start_dirs = ['C\\Users','D:','E:','F:']

for path in [p for p in start_dirs if os.path.exists(p)]:
    for filename in scan_dir2(path):
        print('',filename)



#掃A-Z[chr(c)+':'for c in range(ord('A'),ord('Z')+1)]

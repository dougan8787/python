import os
import platform
import sys

def scan_dir3(path):
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            for path in scan_dir3(fullpath):
                yield path
    else:
        yield path
        
windows_dirs = ['C:\\Users','D:','E:','F:']
linux_dirs = ['/etc','/home','root']

all_start_dirs={'Windows': windows_dirs,
                'Linux': linux_dirs}

start_dirs = all_start_dirs.get(platform.system(),[])

save_dir = 'C:\\temp' if platform.system() == 'Windows' else '/tmp'

for start_dir in start_dirs:
    for filename in scan_dir3(start_dir):
        #handler.send_file(filename) //需要變數handler
        print(filename)

import os

def scan_dir_cb2(path,callBackFunc,param):
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            scan_dir_cb2(fullpath,callBackFunc,param)
    else:
        callBackFunc(path,param)

def print_filename(filename,message):
    print(message,filename)

scan_dir_cb2('.',print_filename,':')

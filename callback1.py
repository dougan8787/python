def scan_dir_cb(path,callBackFunc):
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            scan_dir_cb(fullpath,callBackFunc)
    else:
        callBackFunc(path)

        scan_dir_cb('.',print) #print被拿來做為call back

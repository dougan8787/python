def scan_dir(path):
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            scan_dir(fullpath)
    else:
        print(path)

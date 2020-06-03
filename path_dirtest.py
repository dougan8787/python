def scan_dir(path):
    if os.path.isdir(path):
        for name in os.listdir(path):
            fullpath = os.path.join(path,name)
            yield from scan_dir(fullpath)  #python3
    else:
        yield path

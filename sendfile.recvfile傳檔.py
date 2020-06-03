def recv_file(self):
    result = ()
    while True:
        tag = self.recv_tag()
        if not tag or tag in [FILE_END_TAG,FILE_ABORT_TAG]:break
        data = self.recv_data
        if not data:break
        print(tag,data)
        result[tag] = data
    return result

def send_file(self,path):
    filename = path
    filesize = os.path.getsize(path)
    filedata = open(path,'rb').read()
    try:
        self.send_tag(FILE_NAME_TAG)
        self.send_data(filename)
        self.send_tag(FILE_SIZE_TAG)
        self.send_data(filesize)
        self.send_tag(FILE_CONTENT_TAG)
        self.send_data(filedata)
        self.send_tag(FILE_END_TAG)
        return True
    except Exception as e:
        print(str(e))
        self.send_tag(FILE_ABORT_TAG)
        return False

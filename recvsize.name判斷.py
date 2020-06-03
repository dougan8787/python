def recv_size(self):
    size = self.recv_data()
    if not isinstance(size,int):#判斷是否為int
        raise TypeError('invalid size type %s'% type(size))
    return size
def recv_name(self):
    path = self.recv_data()
    if not isinstance(path,str):#判斷是否為str
       raise TypeError('invalid name type %s'% type(path))
    namelist = path.splist('\t')
    if '..' in namelist:
        raise ValueError('dangerous path')
    name = os.path.join(*namelist)
    return name

def nbyte_to_data(self):
    size_info = {'B':1,'H':2,'L':4,'Q':8}
    btag = self.read_raw(1)
    if not btag:
        return None
    exceptFlag = False
    if btag == self.exceptTag #如果是特別標籤
    exceptFlag =True         #設定特別旗標為True
    btag = self.read_raw(1)   #再讀一次取得資料標籤
    if not btag:              #沒讀到東西就是斷線了
        return None
    tag   = btag.decode('utf-8')

    if exceptFlag:
        #是特別標籤時不用return ,而是用raise exception
        #有無特別標籤的差別僅僅是回傳的方法而已
        raise InOutException(result)
    return result


def data_to_nbyte(self,n,exceptFlag=False):
    exceptFlag = self.exceptTag if exceptFlag else b''
    if isinstance (n,int):
        if n<(1<<8): tag = 'B'
        elif n < (1<<16) : tag = 'H'
        elif n < (1 <<32): tag = 'L'
        else:              tag = 'Q'
        n = struct.pack('!'+tag,n)
        nbyte = tag.encode('utf-8')+n

        return exceptTag + nbyte #nbyte是基本標籤和資料

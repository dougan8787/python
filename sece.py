import struct


def int_to_nbyte(n) :
    if n < ( 1 << 8 ) :
        #數值小於256的byte就足夠
        tag = 'B'
    elif n < (1 << 16 ) : #數值小於65536的用word就足夠
        tag= 'H'
    elif n < ( 1 << 32 ):
                #數值小於4294967296的用long就足夠了
        tag ='L'
    else:
                    #超過4294967296就用long long 'Q'了
         tag = 'Q'
    return tag.encode('utf-8')+struct.pack('!'+tag,n)


def nbyte_to_int(source):
    
    #定義標籤代表bytes長度
    
    size_info ={'B':1,'H':2,'L':4,'Q':8}
    
    #將資料切成兩斷
    
    btag,source = source[:1],source[1:]

    #轉成str

    tag = btag.decode('utf-8')
    
    #如果標籤不是我們定義的，就產生例外
    
    if not tag in size_info:
        
        raise TypeError ('Invalid type'+type(tag))
    
    #取得標籤代表的byte長度
    
    size =size_info[tag]

    #在次將資料切成兩斷

    bnum,source = source [:size],source[size:]

    #傳回

    return struct.unpack('!'+tag,bnum)[0],source
        

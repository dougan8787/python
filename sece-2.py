import struct


def int_to_nbyte(n) :
    if n < ( 1 << 8 ) :#數值小於256的byte就足夠
        
        tag = 'B'
        
    elif n < (1 << 16 ) : #數值小於65536的用word就足夠
        
        tag= 'H'
        
    elif n < ( 1 << 32 ):#數值小於4294967296的用long就足夠了
                
        tag ='L'
        
    else:
                    #超過4294967296就用long long 'Q'了
         tag = 'Q'
         
    return tag.encode('utf-8')+struct.pack('!'+tag,n)


def nbyte_to_int(source):
    
    read_bytes = lambda d,s:(d[:s],d[s:])#定義讀取方式
    
    read_file = lambda d,s:(d.read(s), d)

    read_socket = lambda d, s:(d.recv(s),d)

    reader = {
        
        bytes: read_bytes,
        
        io.IOBase: read_file,
        
        socket.socket: read_socket,
        
        }
       
    size_info ={'B':1,'H':2,'L':4,'Q':8} #定義標籤代表bytes長度
 
    reader = readers[type(source)] #由參數來決定用哪一個 lambda

    btag,source = source[:1],source[1:]  #將資料切成兩斷

    tag = btag.decode('utf-8')#轉成str
    
    if not tag in size_info: #如果標籤不是我們定義的，就產生例外
        
        raise TypeError ('Invalid type'+type(tag))
    
    size =size_info[tag] #取得標籤代表的byte長度

    bnum,source = source [:size],source[size:]#在次將資料切成兩斷
  
    return struct.unpack('!'+tag,bnum)[0],source #傳回
        

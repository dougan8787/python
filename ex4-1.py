#父類別
class INOUT:
    def __init__(self,handle):
       self.handle = handle
#data_to_nbyte 把檔案轉byte
       def data_to_nbyte(self,n):
         if isinstance(n,int):
          if n < ( 1 << 8 ): tag = 'B'
           elif n < ( 1 << 16 ):tag = 'H'
            elif n < ( 1 << 32 ):tag = 'L'
             else: tag ='Q'
             n=struct.pack('!'+ tag , n )
             return tag.encode('utf-8') + n
          elif isinstance(n,bytes):
              tag = 's'
              return tag.encode('uft-8')+ self.data_to_nbyte(len(n)) + n
            elif isinstance(n,str):
                tag = 'c'
                n = n.encode('utf-8')
                return tag.encode('utf-8')+self.data_to_nbyte(len(n)) + n
            raise TypeError('Invalid type:' + type(tag))
        #nbyte_to_data把byte轉檔案
        def nbyte_to_data(self):
            size_info = {'B':1,'H':2,'L':4 ,'Q':8}
            btag = self.read_handle(1)
            if not btag:
                return None
            tag =btag.decode('utf-8')
            if tag in size_info:
                size =size_info[tag]
                bnum = self.read_handle(size)
                result = struct.unpack('!' + tag,bnum)[0]
            elif tag in ['s','c']:
              size =self.nbyte_to_data()
              if size >= 65536:
                   raise ValueError('length too long' + str(size))
                 bstr =self.read_handle(size)
                 result =bstr if tag == 's' else bstr.decode('utf-8')
              else:
                  raise TypeError ( 'Invalid type' + tag )
              return result
            #
         def read(self):
             return self.nbyte_to_data()
         def write(self,d):
             byte_data = self.data_to_nbyte(d)
             self.write_handle(byte_data)
         def close(self):
             return self.close_handle()
            #這裡就是子類別定義的地方
         def read_handle(self,n):
             return b''
         def write_handle(self,d):
             print(d)
             return len(d)
         def close_handle(self):
             return self.handle

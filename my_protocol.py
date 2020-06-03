import socket
import struct
import io

def data_to_nbyte(n):
    
    if isinstance(n,int):     #值小於256的用byte就足夠
        
       if n < ( 1 << 8 ):
                
        tag = 'B'
        
       elif n < (1<< 16):    #值小於65536的用word就足夠
           
         tag = 'H'
         
       elif n < (1 << 32):   #值小於4294967296的用long就足夠

         tag = 'L'
         
       else:                 #值大於4294967296的用long long就足夠 'Q'

         tag = 'Q'

       n =struct.pack('!' + tag , n )

       return tag.encode(' utf-8 ') + n
    
    elif isinstance( n , bytes ):

        tag = 's'

        return tag.encode('utf-8') + data_to_nbyte(len(n)) + n

    elif isinstance ( n , str ):

        tag = 'c'

        n = n.encode('utf-8')

        return tag.encode('utf-8')+data_to_nbyte(len(n)) + n

    raise TypeError('Invalid type:' + type(tag))

def nbyte_to_data(source):

    read_bytes = lambda d, s: (d[ :s],d[s: ])

    read_file = lambda d , s:(d.read(s),d)
    
    read_socket = lambda d , s:(d.recv(s),d)

    readers = {

        bytes : read_bytes,

        io.IOBase: read_file,

        socket.socket : read_socket,

        }
    size_info = {'B':1 ,'H':2 ,'L':4 ,'Q':8}

    reader = readers[type(source)]

    btag,source = reader(source,1)

    if not btag:
        
        return None,source

    tag = btag.decode('utf-8')

    if tag in size_info:

        size =size_info[tag]

        bnum,source =reader(source,size)

        result = struct.unpack('!' + tag, bnum)[0]

    elif tag in ['s','c']:

        size,source = nbyte_to_data(source)

        if size >=65536:

            raise ValueError ('length too long' + str(size))

        bstr,source =reader(source,size)

        result = bstr if tag == 's' else bstr.decode('utf-8')

    else:
     raise TypeError('Invalid type :' + tag )
    
    return result,source
                                                     

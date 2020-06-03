import socket
from my_protocol import data_to_nbyte,nbyte_to_data

clientsocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)#開啟一個socket


clientsocket.connect((socket.gethostname(),1234,))#連向伺服器，tuple參數第一個欄位是伺服器或ip

fp = open('client-2.py','rb')

while True:    #讀取到break

 data = fp.read(16)#接收伺服器端傳來的資料 一次讀取16bytes


 if not data:
    
    break

  #傳送訊息給SEVER 
    
clientsocket.send(data_to_nbyte('Happy Birthday'))#每次傳送16bytes

clientsocket.send(data_to_nbyte(5201314))


fp.close()

#data =clientsocket.recv(1024)

#print('receive',data)


clientsocket.close()#關閉socket

import socket


clientsocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)#開啟一個socket


clientsocket.connect((socket.gethostname(),1234,))#連向伺服器，tuple參數第一個欄位是伺服器或ip

fp = open('client-2.py','rb')

while True:    #讀取到break

 data = fp.read(16)#接收伺服器端傳來的資料 一次讀取16bytes

 if not data:
    
    break

clientsocket.send(data)#每次傳送16bytes


fp.close()

#data =clientsocket.recv(1024)

#print('receive',data)


clientsocket.close()#關閉socket

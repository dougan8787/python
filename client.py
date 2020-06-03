import socket

#開啟一個socket
clientsocket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#連向伺服器，tuple參數第一個欄位是伺服器或ip
clientsocket.connect((socket.gethostname(),1234,))

#傳送bytes 型態字串
clientsocket.send(b'hello ,0926')

#接收伺服器端傳來的資料
data = clientsocket.recv(1024)
print('receive',data)

#關閉socket
clientsock.close()

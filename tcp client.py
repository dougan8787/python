import socket

terget_host = "www.google.com"
terget_port = 80

#建立socket物件
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#讓client連線
client.connect((terget_host,terget_port))

#傳送一些資料
client.send("GET / HTTP/1.1\r\rHost:google\r\n\r\n")

#接收一些資料
response = client.recv(4096)

print response

import socket


target_host = "127.0.0.1"
target_port = "5555"

#建立socket物建
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#傳送資料
client.sendto("AABBBCCC",(target_host,target_port))

#接收資料
data,addr = client.recvfrom(4096)

print data

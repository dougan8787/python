import socket
#socket.AF_INET和socket.SOCK_STREM
#表示這是保證傳到網路傳輸TCP
seversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind()參數是一個tuple,放的是主機名和阜號
seversocket.bind((socket.gethostname(),1234,))

#設定最多等待5個連線
seversocket.listen(5)

while True:
    #當有連線來道,用accept()取得和客戶端溝通的socket
    #accept()傳回來的是一個tuple,後面傳回是客戶端位置
    conn,addr = seversocket.accept()
    print('connect from',addr)

    #讀取1024bytes,要注意recv()傳回的資料型態是bytes
    #而不是
    data = conn.recv(1024)
    #將收到的資料用send()傳回，同樣參數型態只能是bytes
    conn.send(data)
    #關閉和客戶端連線的socket
    conn.close()
#關閉伺服器的網路服務
seversocket.close()

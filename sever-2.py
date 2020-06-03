import socket


seversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#socket.AF_INET和socket.SOCK_STREM#表示這是保證傳到網路傳輸TCP


seversocket.bind((socket.gethostname(),1234,))#bind()參數是一個tuple,放的是主機名和阜號


seversocket.listen(5)#設定最多等待5個連線

while True:    #當有連線來道,用accept()取得和客戶端溝通的socket
    
    
    conn,addr = seversocket.accept()#accept()傳回來的是一個tuple,後面傳回是客戶端位置
    print('connect from',addr)


   
    data = conn.recv(2048)#讀取2048bytes,要注意recv()傳回的資料型態是bytes
    
    if not data:
        
        break
    
    print (data)
    
   # conn.send(data)#將收到的資料用send()傳回，同樣參數型態只能是bytes
    
    conn.close()#關閉和客戶端連線的socket


seversocket.close()#關閉伺服器的網路服務

import os

def receive_thread(conn,addr,path):
    handler = NetAPI(conn)
    while True:
        conn,addr = serverSocket.accept() #等待連線
        print('send banner')
        conn.send(BANNER)
        new_threads=[]
        for thread in threads:      #去除以結束的執行緒
            thread.join(0.1)        #等待0.1秒
            if thread.is_alive():   #執行緒其實還沒結束  #檢查執行緒是否結束
                new_threads.append(thread)  #等下在join一次 #加入等待
        threads=new_threads
        if len(threads)<MAX_CONN:   #未超過最大客戶端數量，產生執行緒
            thread = threading.Thread(target = receive_thread, \args = (conn,addr , target_dir,))

            thread.start()          #執行緒啟動執行
            threads.append(thread)  #加入執行中的執行緒列表
        else:
            conn.close()            #關閉conn api
        data = handler.recv_file()
        if not data :break
        filename = os.path.join(path,addr[0])
        save_file(data,filename)
    
conn,addr = serverSocket.accept()


import os

def receive_thread(conn,addr,path):
    handler = NetAPI(conn)
    while True:
        data = handler.recv_file()
        if not data :break
        filename = os.path.join(path,addr[0])
        save_file(data,filename)
    conn.close()
conn,addr = serverSocket.accept()
thread = threading.Thread(target = receive_thread, \args = (conn,addr , target_dir,))

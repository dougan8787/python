import threading

threads = []

def print_message(m):
    for i in range(10):  #印10次訊息
        print(m, i)

for i in range(10):     #產生 10個thread
    thread = threading.Thread(target=print_message ,args=('Thread-'+str(i),))
    threads.append(thread)

for thread in threads:
    thread.start()      #啟動thread，也就是讓thread開始執行

for thread in threads:
    thread.join()       #用join()等待thread一個個結束

import urllib2
import threading
import Queue
import urllib

threads       =50
target_url    =                #目標網址
wordlist_file ="/tmp/all.txt"  #from SVNDigger
resume        = None           #恢復
user_agent    =                #網頁版本


def build_wordlist(wordlist_file): #暴力破解網頁路徑


    #載入檔名列表
    fd = open(wordlist_file,"rb") #fd打開一個文件
    raw_words = fd.readlines()    #raw_words讀取數據
    fd.close()  	          #關閉fdhandle

    found_resume    = False
    words           =Queue.Queue()#列隊


    for word in raw_words:        #重覆讀取數據

        word = word.rstrip()      #刪除string字串末尾的指定字符
        

        if resume is not None:    #如果resume不等於None狀況

            if found_resume:      #if為假

                words.put(word)   #將word放入隊列中

            else:
                if word == resume:#word == None
                    found_resume = True     	#found_resume = True
                    print("Resuming wordlist from: %s"% resume)
                    
        else:

            words.put(word)      #將word放入隊列中

    return words                 #回傳words



def dir_bruter(word_queue,extensions=None):

    while not word_queue.empty():                   #如果陣列為空循環true=false，false=ture

        attempt  = word_queue.get()                 #從陣列移除並返回

        attempt_list = []                           #空的list


                                                    #檢查是否有檔名結尾，如果沒有，嘗試檢察查一個目錄，例如:.php、.pdf
        if "." not in attempt:                      #如果在指定序列沒找到返回值true，否則false
            attempt_list.append("/%s/" % attempt)   #加入attempt_list字串沒掃完繼續掃
        else:
            attempt_list.append("/%s" % attempt)    #加入attempt_list字串掃到則停止
            

                                                    #如果要暴力檢查檔名結尾
        if extensions:

            for extension in extensions:            #檢查當前結尾

                attempt_list.append("/%s%s" %(attempt,extension) #加入attempt_list

        for brute in attempt_list:   #逐一處理嘗試對象直到沒有為止

                url="%s%s" %(target_url,urllib.quote(brute))   #url=目標網址+目標檔案列(brute符號編碼)

                try:
                    headers = {}               #headers=字典(Dictionary)
                    headers["User-Agent"] = user_agent #把User-Agent 設定成普通內容
                    r=urllib2.Request(url,headers = headers) #r等於url+headers字典
                    response = urllib2.urlopen(r)           #response 等於開啟網頁

                    if len(response.read()):  #把response讀進來

                        print("[%d] => %s" % (response.code,url)  #把回應200就顯示url

                 except urllib2.URLError,e:  #如果URLError錯誤讀進來

                    if hasattr(e,'code') and e.code !=404:  #判断对象是否包含对应的属性或 e.code !=404

                        print("!!! %d => %s"%(e.code,url))  #顯示url

                    pass

word_queue = bulid_wordlist(wordlist_file)  #載入暴力解密列表
extensions = [".php",".bak",".orig",".inc"] #建立檢查檔案結尾
                              
for i in range(threads):        #在啟動一批亂數取threads
    t=threading.Thread(target=dir_bruter,args=(word_queue,extensions,)) #啟動多線程(目標等於dir_bruter,args=這些檔案列表)
    t.start()  #啟動

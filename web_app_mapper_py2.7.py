import Queue
import threading
import os
import urllib2

threads     = 10
target      = "http://www.blackfire.mobi" #目標網址
directory   = "D:/joomla-cms/joomla_3.9.5" #目錄
filters     =[".jpg",".gif",".png",".css"]

os.chdir(directory)

web_paths = Queue.Queue() #把稍後想檢查目標是否擁有的檔名加到裡面

for r,d,f in os.walk("."):  #接著用os.walk函式走訪本基web應用程式下所有目錄
    for files in f:         #files = f數值
        remote_path = "%s/%s" %(r,files)  #
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():

    while not web_paths.empty():
        path = web_paths.get()
        url  = "%s%s" %(target,path)


        request = urllib2.Request(url)

        try:
            response = urllib2.urlopen(request)
            content  = response.read()

            print"[%d] => %s"% (response.code,path)
            response.close()

        except urllib2.HTTPError as error:

            #print"Failed %s"% error.code
            pass

for i in range(threads):

    print("Spawning thread: %d"% i)
    t = threading.Thread(target = test_remote)
t.start()

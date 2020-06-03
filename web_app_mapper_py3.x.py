import queue
import threading
import os
import urllib
import http
from urllib import request
from urllib import error


threads     = 10
target      = "http://www.blackfire.mobi" #目標網址
directory   = "D:/joomla-cms/joomla_3.9.5" #目錄
filters     =[".jpg", ".gif", ".png", ".css"]

os.chdir(directory)

web_paths = queue.Queue()   #把稍後想檢查目標是否擁有的檔名加到裡面

for r,d,f in os.walk("."): #接著用os.walk函式走訪本基web應用程式下所有目錄
    for files in f:
        remote_path = "%s/%s" %(r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
        if os.path.splitext(files)[1] not in filters:
            web_paths.put(remote_path)

def test_remote():

    while not web_paths.empty():
        
        path = web_paths.get()
        url  = "{}{}".format(target,path)


        #request = urllib.request.Request(url)

        try:
            response = urllib.request.urlopen(url)
            content  = response.read()

            print("[%s] => %s"% (response.code,path))
            response.close()

        except urllib.error.HTTPError as error:

            #print("Failed {}".format(error.code))
         #except:
            pass

for i in range(threads):

    print("Spawning thread: %s"% i)
    t = threading.Thread(target = test_remote)
t.start()

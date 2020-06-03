import urllib2

url = "http://www.nostarch.com"  #目標網址

headers = {}    	#定義headers字典
headers['User-Agent'] = "Googlebot" #讓python script看起來像是Googlebot

request  = urllib2.Request(url,headers = headers) #建立request物件，傳入url以及header字典
response = urllib2.urlopen(request) #response 物件傳給uplopen函式

print response.read() #回傳一個file-like物件，讓我們讀取
response.close()  #關閉response物件

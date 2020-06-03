import urllib2

body = urllib2.urlopen("http://www.nostarch.com") #把url傳給uplopen

print body.read() #它會回傳一個file-like物件，讓我們讀取

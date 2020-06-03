import re
import zlib
import cv2

from scapy.all import *

pictures_directory =""
faces_directory    =""
pcap_file          =""

def http_assembler(pcap_file):      

    carved_images = 0
    faces_detected= 0
    a= rdpcap(pcap_file)        #先打開pcap檔
    sessions      =a.sessions() #用scapy自動開各tcp串流
    for session in sessions:    #放到字典裡
        http_payload = ""       #把所有http流量存進來
        for packet in sessions[session]:
            
            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:

                    #重組stream
                    http_payload += str(packet[TCP].payload)
            except:
                    pass

        headers = get_http_headers(http_payload)#分析函數

        if headers is None:     	#逐一檢察
            continue

        image,image_type = extract_image(headers,http_payload)   #確定是圖像抽出

        if image is not None and image_type is not None:

            #儲存影像
            file_name = "%s-pic_carver_%d.%s" %(pcap_file,carved_images,image_type)

            fd = open("%s/%s"%(pictures_directory,file_name),"wb")

            fd.write(image)
            fd.close()

            carved_image +=1

            #然後嘗試辨識人臉
            try:
                result = face_detect("%s/%s"%(pictures_directory,file_name),file_name)

                if result is True:
                    faces_detected +=1
            except:
                pass
        return carved_images,faces_detected
    
carved_images,faces_detected = http_assembler(pcap_file)
print("Extracted : %d images" % carved_images)
print("Detected : %d faces" % faces_detected)

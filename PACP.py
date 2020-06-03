import re
import zlib
import cv2

from scapy.all import *

pictures_directory = "D:/pic_carver/pictures"
faces_directory    = "D:/pic_carver/faces"
pcap_file          = "bhp.pcap"


def face_detect(path,file_name):

    img     =cv2.imread(path)   #能載入的影像
    cascade =cv2.CascadeClassifier("haarcascade_frontalface_alt.xml") #人臉分類器
    rects   =cascade.detectMultiScale(img,1.3,4,cv2.cv.CV_HAAR_SCALE_IMAGE,(20,20)) #偵測之後，它會傳回影像座標值


    if len(rects) == 0:
        return False
    
    rects[:,2:] += rects[:,:2]

    #凸顯影像裡的人臉，在實際範圍畫上框框
    for x1,y1,x2,y2 in rects:
      
      cv.rectangle(img,(x1,y1),(x2,y2),(127,255,0),2)
      
    cv2.imwrite("%s/%s-%s"%(faces_directory,pcap_file,file_name),img)

    return True
    
def get_http_headers(http_payload):

    try:
        #如果是Http流量，就把headers切出來
        headers_raw = http_payload[:http_payload.index("\r\n\r\n")+2]

        #把headers切開
        headers = dict(re.findall(r"(?P<name>.*?):(?P<value>.*?)\r\n",headers_raw))
    except:

        return None
    if "Content-Type" not in headers:

        return None

    return headers

def extract_image(headers,http_payload):    #判斷影像本體進行判斷

    image       =None
    image_type  =None

    try:
        if "image" in headers['Content-Type']:     #為影像'Content-Type'，如果是就抓出來

            #抓出影像型別與本體
            

            image_type = headers['Content-Type'].split("/")[1]

            image      =http_payload[http_payload.index("\r\n\r\n")+4:]

            #如果偵測到傳輸壓縮，就先解開
            
            try:
                if "Content-Encodeing" in headers.keys():

                    if headers['Content-Encodeing'] == "gzip":    

                        image = zlib.decompress(image,16+zlib.MAX_WBITS)

                    elif headers['Content-Encodeing'] == "deflate":

                        image = zlib.decompress(image)

            except:
                pass
    except:

        return None,None

    return image,image_type

def http_assembler(pcap_file):

    carved_images  = 0
    faces_detected = 0
    a = rdpcap(pcap_file)  #先打開PCAP檔以便處理

    sessions = a.sessions()

    for session in sessions:

        http_payload=""  #創建http_payload物件

        for packet in sessions[session]:

            try:
                
                if packet[TCP].dport == 80 or packet[TCP].sport == 80: #自動分開各個TCP串流
                    
                    #重組stream
                    http_payload += str(packet[TCP].payload)

            except:
                                
                pass

        headers = get_http_headers(http_payload) #放到字典裡。

        if headers is None:  #接著用它濾出HTTP流量，然後把所有HTTP流量的資料串到同一個暫存區

               continue

        image,image_type = extract_image(headers,http_payload) #提取headers,http_payload

        if image is not None and image_type is not None: #確定是影像檔，會把影像抽取出來


            #儲存影像
            file_name = "%s-pic_carver_%d.%s" %(pcap_file,carved_images,image_type)

            fd = open("%s/%s"%(pictures_directory,file_name),"wb")

            fd.write(image)
            fd.close()

            carved_images +=1

            #然後嘗試辨識人臉

            try:
                result = face_detect("%s/%s"%(pictures_directory,file_name),file_name)

                if result is True:
                     faces_detected +=1

            except:
                pass
            
    return carved_images,faces_detected

carved_images,faces_detected = http_assembler(pcap_file)

print("Extracted: %d images"% carved_images)

print("Detected:%d faces" %faces_detected)

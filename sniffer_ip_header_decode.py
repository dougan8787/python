import sys
import socket
import os
import struct
from ctypes import *

#要監聽的主機
host ="192.168.0.102"

#我們的IP header

class IP(Structure):
    _fields_ = [
        ("ihl",             c_ubyte, 4),
        ("version",         c_ubyte, 4),
        ("tos",             c_ubyte),
        ("len",             c_ushort),
        ("id",              c_ushort),
        ("offset",          c_ushort),
        ("ttl",             c_ubyte),
        ("protocol_num",    c_ubyte),
        ("sum",             c_ushort),
        ("src",             c_ulong),
        ("dst",             c_ulong),
        ]

    def __new__(self,socket_buffer=None):
        return self.from_buffer_copy(socket_buffer)  #接收一個RAW暫存區，填寫結構

    def __init__(self,socket_buffer=None):

        #把協定常數對應到名稱
        self.protocol_map ={1:"ICMP",6:"TCP",17:"UDP"}

        #人類可讀的IP 位址
        self.src_address = socket.inet_ntoa(struct.pack("<L",self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L",self.dst))

        #人類可讀的協定
        try:
            self.protocol = self.protocol_map[self.protocol_num]
        except:
            self.protocol = str(self.protocol_num)

#看過前一個範例的話應該很眼熟
if os.name == "nt":
    socket_protocol = socket.IPPROTO_IP
else:
    socket_protocol = socket.IPPROTO_ICMP

sniffer = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket_protocol)

sniffer.bind((host,0))
sniffer.setsockopt(socket.IPPROTO_IP,socket.IP_HDRINCL,1)

if os.name == "nt":
    sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_ON)
try:
    while True:
        #讀取一個封包
        raw_buffer = sniffer.recvfrom(65565)[0]

        #從暫存區開頭20 bytes建立 IP header
        ip_header = IP(raw_buffer[0:32])

        #顯示偵測到的協定與主機
        print("Protocol: %s %s -> %s"%(ip_header.protocol,ip_header.src_address,ip_header.dst_address))
        
#處理 CTRL-C
except KeyboardInterrupt:
    #如果我們用的是windows,就關掉混雜模式
    
    if os.name == "nt":
         sniffer.ioctl(socket.SIO_RCVALL,socket.RCVALL_OFF)
        

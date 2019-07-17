#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# import os
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import scapy.all as scapy
from scapy.layers import http
from optparse import OptionParser
import sys
import os

request = http.HTTPRequest
response = http.HTTPResponse

def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath

def find_tcp_stream(pcap,request):
    pcap = scapy.rdpcap(pcap)
    
    i = 0
    for p in pcap:
        if p.haslayer(request):
            i = i + 1
    return i
           

def main():
    pcap = filePath('-f')
    
    # step1 对有多个请求的报文按流进行切分
    tcp_stream = find_tcp_stream(pcap,request=request)
    tshark_path = "/usr/bin/tshark"
    j = 0
    for j in range(tcp_stream):
        os.system(tshark_path + ' -r %s -Y "tcp.stream eq %s" -w %s.pcap' %(pcap,j,j)) 

  
if __name__ == '__main__':
    main()

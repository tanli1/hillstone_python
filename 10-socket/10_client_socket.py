#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# import os
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import socket
import re
import scapy.all as scapy
from optparse import OptionParser
import sys
import commands

def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath

def request_load(pcap):
    
    request_list = []
    for p in pcap:
        if 'Raw' in p :
            request_load = p['Raw'].load
            req = '^(?:OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) '
            if re.search(req, request_load):
                request_list.append(request_load)
    return request_list
            
def client_socket(request_list):
    print ('我是客户端')

    (status, output) = commands.getstatusoutput('ifconfig eth0 | grep \"inet addr\"')
    HOST = output.split(':')[1].split(' ')[0]                          # 服务器的ip
    PORT = 50077                                                       # 需要连接的服务器的端口
    addr = (HOST,PORT)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(addr)                                                    # 链接指定的计算机的端口
    
    for i in range(len(request_list)):
        s.sendall(request_list[i])                                      # 发送‘Hello，world’给服务器
        data = s.recv(1024000)                                             # 从服务器接收数据
        print "接收到的数据:\r\n ", repr(data)                          # 打印从服务器接收回来的数据

    s.close()
    


def main():
    pcap = filePath('-f')
    pcap = scapy.rdpcap(pcap)
 
    request_list = request_load(pcap)
    c_socket = client_socket(request_list)


if __name__ == '__main__':
    main()
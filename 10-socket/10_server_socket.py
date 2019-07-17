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

def response_load(pcap):
    
    response_list = []
    for p in pcap:
        if 'Raw' in p :
            response_load = p['Raw'].load
            req = 'HTTP/1.1 200 OK'
            if re.search(req, response_load):
                response_list.append(response_load)
    return response_list

def server_socket(response_list):
    print ('我是服务端！')
    (status, output) = commands.getstatusoutput('ifconfig eth0 | grep \"inet addr\"')
    HOST = output.split(':')[1].split(' ')[0]                          # 服务器的ip
    #HOST = '10.160.11.100'
    PORT = 50077
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象
    s.bind((HOST, PORT))                                   # 绑定地址
    s.listen(1)                                            # 监听TCP，1代表：操作系统可以挂起(未处理请求时等待状态)的最大连接数量。该值至少为1
    conn, addr = s.accept()                                # 开始被动接受TCP客户端的连接。
    print "连接的地址: ", repr(addr)  

    for i in range(len(response_list)):
        conn.sendall(response_list[i])                     # 把从客户端接收来的数据完整的，发送给客户端
        while 1:
            data = conn.recv(4096)                         # 接受TCP数据，1024表示缓冲区的大小
            if not data: break
            print "接收到的数据:\r\n ", repr(data)

    conn.close()


def main():
    pcap = filePath('-f')
    pcap = scapy.rdpcap(pcap)

    response_list = response_load(pcap)
    s_socket = server_socket(response_list)


if __name__ == '__main__':
    main()
#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# import os
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import re
import scapy.all as scapy
from scapy.layers import http
from optparse import OptionParser
import sys

def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath

def get_info(pcap,info):
    seq = ''
    srcip = ''
    dstip = ''
    srcport = ''
    dstport = ''
    
    for p in pcap:
        if 'Raw' in p:
            request_load = p['Raw'].load           
            if re.search(info, request_load):
                seq = p['TCP'].seq 
                srcip = p['IP'].src
                dstip = p['IP'].dst
                srcport = p['TCP'].sport
                dstport = p['TCP'].dport  
                  
    return seq, srcip, dstip, srcport, dstport
    
def seq_sort(pcap, seq, srcip, dstip, srcport, dstport):
    seq_list = [seq]
    for i in pcap:
        if i['IP'].src ==srcip and i['IP'].dst == dstip and i['TCP'].sport ==srcport and i['TCP'].dport == dstport and 'Raw' in i:
            seq = i['TCP'].seq
            if seq not in seq_list:
                seq_list.append(seq)   # 去重
    return seq_list.sort()             # 返回排序后的list

def load(seq_list, pcap):
    request = ''
    for i in range(len(seq_list)):
        for p in pcap:
            if ('Raw' in p and p["TCP"].seq == seq_list[i]):
                request += p['Raw'].load
    return request

def main():
    pcap = filePath('-f')
    pcap = scapy.rdpcap(pcap)
    # step1 请提取出报文中的请求信息
    seq, srcip, dstip, srcport, dstport = get_info(pcap, '^(?:OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT) ') 
    seq_list = seq_sort(pcap, seq, srcip, dstip,srcport, dstport)
    request = load(seq_list, pcap)
    if request:
        print '请求信息：\r\n',"\033[1;32;40m" + request + "\033[0m" 
    else:
        print '请求信息： \r\n',"\033[1;32;40m" + request + "\033[0m" 
        
    # step2 请提取出报文中的响应信息
    seq, srcip, dstip, srcport, dstport = get_info(pcap, 'HTTP/1.1 200 OK') 
    seq_list = seq_sort(pcap, seq, srcip, dstip,srcport, dstport)
    response = load(seq_list, pcap) 
    if response:
        print '响应信息：\r\n',"\033[1;32;40m" + response + "\033[0m" 
    else:
        print '响应信息： \r\n',"\033[1;32;40m" + response + "\033[0m" 

  
if __name__ == '__main__':
    main()

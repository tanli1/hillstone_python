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

def seq_sort(pcap):
    seq_list = []
    for p in pcap:
        if 'Raw' in p:
            if p['TCP'].seq not in seq_list:
                seq_list.append(p['TCP'].seq)   # 去重
    return seq_list.sort()                      # 返回排序后的list

def load(seq_list, pcap):
    result = ''
    for i in range(len(seq_list)):
        for p in pcap:
            if ('Raw' in p and p["TCP"].seq == seq_list[i]):
                result += p['Raw'].load
    return result

def main():
    pcap = filePath('-f')
    pcap = scapy.rdpcap(pcap)

    # step1 请提取出报文中的信息
    seq_list = seq_sort(pcap)
    print 'request seq_list ==',seq_list
    result = load(seq_list, pcap)
    if result:
        print '报文中的信息：\r\n', "\033[1;31;40m" + result + "\033[0m" 
    else:
        print '报文中的信息： \r\n',"\033[1;31;40m" + result + "\033[0m" 

  
if __name__ == '__main__':
    main()

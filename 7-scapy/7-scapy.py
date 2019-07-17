#!/usr/bin/env python
#encoding=utf-8
# Copyright (c) 2006-2019 Hillstone Networks, Inc.
# author: ltan
# create_time: 2019/5/28
#

import scapy.all as scapy
import ast
from optparse import OptionParser
import sys


def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath   

def main():
    pcap = filePath('-f')
    packets = scapy.rdpcap(pcap)  # 读取pcap文件
    
    print 'TCP分片报文内容如下：\r\n'
    for p in  packets:  
        for f in p.payload.payload.payload.fields_desc:       # [<Field (Raw,Padding).load>]
            fvalue = p.payload.payload.getfieldval(f.name)    # f.name -> load  fvalue -> value
            print "\033[31;40m" + fvalue  + "\033[0m" 

if __name__ == '__main__':
    main()

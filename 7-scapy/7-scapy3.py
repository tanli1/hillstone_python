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
    
    print "\033[31;40m" + 'TCP分片报文内容如下：\r\n' + "\033[0m"
    for p in  packets:  
        for f in p.payload.payload.payload.fields_desc:        # [<Field (Raw,Padding).load>]
            fvalue = p.payload.payload.getfieldval(f.name)     # f.name -> load  fvalue -> value
            #print "\033[32;40m" + fvalue + "\033[0m" 
            reprval = f.i2repr(p.payload.payload, fvalue)      # 转换成十进制字符串
            print 'type - reprval=======',type(reprval)
            print reprval
            #reprval = ast.literal_eval(reprval)                # 字符串转换成原有类型
            #print reprval
    

if __name__ == '__main__':
    main()

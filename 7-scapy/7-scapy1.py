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

def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath

def step1(pcap):
    pcap = scapy.rdpcap(pcap)
 
    flag = 0

    for p in pcap:     
        if p.haslayer(http.HTTPRequest):
            flag = 1
            print '************ request *********'
            http_header = p[http.HTTPRequest].fields
            request_headers = http_header['Headers']

            Method = p[http.HTTPRequest].Method
            Path =  p[http.HTTPRequest].Path
            version = http_header['Http-Version']
            request_line = Method + " " + Path + " " + version

            if 'Raw' in p:
                request_body = p['Raw'].load
            else:
                request_body = None

        if p.haslayer(http.HTTPResponse):
            flag = 0
        if p.haslayer("HTTP") and flag == 1 and  'Raw' in p:
            request_body = request_body + p['Raw'].load

    return request_line, request_headers, request_body
       


def step2(pcap):
    pcap = scapy.rdpcap(pcap)

    flag = 0

    for p in pcap:
        if p.haslayer(http.HTTPResponse):
            flag = 1
            print '************ response *********'
            http_header = p[http.HTTPResponse].fields
            response_headers = http_header['Headers']
            Status_Line = http_header['Status-Line']

            if 'Raw' in p:
                response_body = p['Raw'].load
            else:
                response_body = None

        if p.haslayer(http.HTTPRequest):
            flag = 0

        if p.haslayer("HTTP") and flag == 1 and 'Raw' in p:
            response_body = response_body + p['Raw'].load

    return Status_Line, response_headers, response_body

def main():
    pcap = filePath('-f')
    
    # step1 请提取出test.pcap中的HTTP请求报文中的请求行，请求头，请求体
    request_line,headers,request_body = step1(pcap) 
    if request_line:
        print '请求行：\r\n',request_line
    else:
        print '请求行返回错误',request_line
    if headers:
        print '请求头：\r\n',headers
    else:
        print '请求头返回错误',headers
    if request_body:
        print '请求体：\r\n',request_body
    else:
        print '请求体为空'

    # step2 请提取出test.pcap中的HTTP响应报文中的响应行，响应头，响应体
    response_line,headers,response_body = step2(pcap) 
    if response_line:
        print '响应行：\r\n',response_line
    else:
        print '响应行返回错误',response_line
    if headers:
        print '响应头：\r\n',headers
    else:
        print '响应头返回错误',headers
    if response_body:
        print '响应体：\r\n',response_body
    else:
        print '响应体为空'

  
if __name__ == '__main__':
    main()

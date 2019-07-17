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

request = http.HTTPRequest
response = http.HTTPResponse

def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath

def step1(pcap,request=0,response=0):
    pcap = scapy.rdpcap(pcap)
    
    for p in pcap:
 
        if p.haslayer(request):
            print("*********request******")
            http_header = p[request].fields
            headers = http_header['Headers']
            
            Method = p[request].Method
            Path =  p[request].Path
            version = http_header['Http-Version']
            request_line = Method + " " + Path + " " + version

            if 'Raw' in p:
                request_body = p['Raw'].load
                return request_line, headers,request_body
            else:
                return request_line, headers, None

        if p.haslayer(response):
            print("*********response******")
            http_header = p[response].fields
            headers = http_header['Headers']
            Status_Line = http_header['Status-Line']

            if 'Raw' in p:
                response_body = p['Raw'].load
                return Status_Line, headers ,response_body
            else:
                return Status_Line, headers ,None

def main():
    pcap = filePath('-f')
    
    # step1 请提取出test.pcap中的HTTP请求报文中的请求行，请求头，请求体
    request_line,headers,request_body = step1(pcap,request=request) 
    if request_line:
        print '请求行：',request_line
    else:
        print '请求行返回错误',request_line
    if headers:
        print '请求头：',headers
    else:
        print '请求头返回错误',headers
    if request_body:
        print '请求体：',request_body
    else:
        print '请求体为空'

    # step2 请提取出test.pcap中的HTTP响应报文中的响应行，响应头，响应体
    response_line,headers,response_body = step1(pcap,response=response) 
    if response_line:
        print '响应行：',response_line
    else:
        print '响应行返回错误',response_line
    if headers:
        print '响应头：',headers
    else:
        print '响应头返回错误',headers
    if response_body:
        print '响应体：',response_body
    else:
        print '响应体为空'

  
if __name__ == '__main__':
    main()

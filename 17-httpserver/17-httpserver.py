#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import socket
import re
from multiprocessing import Process
import commands


# 设置静态文件根目录
root_dir = "/root/test/"


def handle_client(client_socket):
    """
    处理客户端请求
    """
    # 获取客户端请求数据
    request_data = client_socket.recv(1024)
    print "请求数据:\r\n", request_data
    request_lines = request_data.splitlines()
    # 解析请求报文
    request_start_line = request_lines[0]
    # 提取用户请求的文件名
    file_name = re.match(r"\w+ +(/[^ ]*) ", request_start_line.decode("utf-8")).group(1)

    if "/" == file_name:
        file_name = "/index.html"
    try:
        file = open(root_dir + file_name, "rb")  # 打开文件，读取内容
    except IOError:
        response_start_line = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: Myself server\r\n"
        response_body = "The file is not found!\r\n"
    else:
        file_data = file.read()
        file.close()

        # 构造响应数据
        response_start_line = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: Myself server\r\n"
        response_body = file_data.decode("utf-8")

    response = response_start_line + response_headers + "\r\n" + response_body
    print "响应数据:\r\n", response

    # 向客户端返回响应数据
    client_socket.send(response.encode("utf-8"))

    # 关闭客户端连接
    client_socket.close()


if __name__ == "__main__":
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    (status, output) = commands.getstatusoutput('ifconfig eth0 | grep \"inet addr\"')
    HOST = output.split(':')[1].split(' ')[0] 
    PORT = 8000

    server_socket.bind((HOST, PORT))
    server_socket.listen(128)

    while True:
        client_socket, client_address = server_socket.accept()
        print "\033[31;40m" + "[%s, %s]用户连接上了" %client_address + "\033[0m" 
        handle_client_process = Process(target=handle_client, args=(client_socket,))
        handle_client_process.start()
        client_socket.close()
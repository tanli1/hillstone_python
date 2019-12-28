#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:tan
#

import pexpect
import re

def ftp():
    script_log = "script.log"
    ftp_server = raw_input('请输入要连接的ftp服务器地址：')
    name = raw_input('请输入ftp的用户名：')
    password = raw_input('请输入ftp的密码：')
    out = open(script_log,'wb+')
    out.write("=============== Log Title: ftp download file ================")
    
    ftp_conn = pexpect.spawn('ftp %s' %ftp_server)  
    ftp_conn.logfile = out
    index = ftp_conn.expect(["(?i)Name", "(?i)Unknown host", pexpect.EOF, pexpect.TIMEOUT])
    if (index == 0):              
        ftp_conn.sendline(name)
        index = ftp_conn.expect(["(?i)Password",pexpect.EOF,pexpect.TIMEOUT])
        if (index != 0):
            print "ftp login failed"
            ftp_conn.close(force=True)
        ftp_conn.sendline(password)
        index = ftp_conn.expect(["ftp>","Login incorrect","Service not available",pexpect.EOF,pexpect.TIMEOUT])
        if (index == 0):      #匹配到了 'ftp>'，登录成功
            print "Congratulation! ftp login correct!"
            ftp_conn.sendline("ls")
            index = ftp_conn.expect(["test.txt",pexpect.EOF,pexpect.TIMEOUT])
            if index == 0:
                ftp_conn.sendline("bin")      #发送 'bin',使用二进制模式来传输文件
                print "getting a file!"
                ftp_conn.sendline("get test.txt")
                index = ftp_conn.expect(["Transfer complete.",pexpect.EOF,pexpect.TIMEOUT])
                if (index == 2):     #匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出.
                    print "failed to get the file"
                    ftp_conn.close(force=True)
                print "successfully received the file"   #匹配到了 'Transfer complete.*ftp>'，表明下载文件成功，打印成功信息，并输入 'bye'，结束 ftp session.
                ftp_conn.sendline("bye")
                out.close()
            else:
                out.close()
                exit(-1)
        elif index == 1:
            print "Login incorrect"
            ftp_conn.close(force=True)
            out.close()
        elif index == 2:
            print "Service not available"
            ftp_conn.close(force=True)
            out.close()
        else:
        	print "Login failed, due to TIMEOUT or EOF"
            ftp_conn.close(force=True)
            out.close()
    # 匹配到了 "(?i)Unknown host"，表示 server 地址不对，程序打印提示信息并退出
    elif index == 1:   
        print "ftp login failed, due to unknown host"
        ftp_conn.close(force=True)
        out.close()
    # 匹配到了 pexpect.EOF 或 pexpect.TIMEOUT，表示超时或者 EOF，程序打印提示信息并退出
    else:    
        print "ftp login failed, due to TIMEOUT or EOF"
        ftp_conn.close(force=True)
        out.close()

def main():
    ftp()

 
if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import os

def read_file(path, file_name, list_content):
    if os.path.isdir(path):                    # os.path.exists(path)  
        if not os.path.isfile(file_name):
            f = open(path + '/' + file_name, 'w')
            for i in range(len(list_content)):
                f.write(list_content[i]+ '\n')
            f.close()
            print '写文件关闭！'
    else:
        os.mkdir(path)
        #os.chdir(path)       # 改变当前工作目录
        f = open(path + '/' + file_name, 'w')
        for i in range(len(list_content)):
            f.write(list_content[i]+ '\n')
        f.close()
        print '写文件关闭！'

def file_bak(path, file_name, bak):
    if os.path.isdir(bak):                         
        if not os.path.isfile(file_name):
            f = open(path + '/' + file_name, 'r')
            f_content = f.read()

            w = open(bak + '/' + file_name, 'w')
            w.write(f_content.title().replace(', ', '\n'))

            f.close()
            w.close()
            print '读、写文件关闭！'
    else:
        os.mkdir(bak)
        f = open(path + '/' + file_name, 'r')
        f_content = f.read()
        #f_content.replace(', ', '\n')

        w = open(bak + '/' + file_name, 'w')
        w.write(f_content.title().replace(', ', '\n'))  #str.title() 所有单词首字母修改为大写    str.capitalize() 第一个字母大写
        r = open(bak + '/' + file_name, 'r')

        f.close()
        w.close()
        print '读、写文件关闭！'


def main():

    list_content = ['Bob, Lucy, Nancy, Joy, darren, kevin','Lily, Tony, andy','Candy, Wendy, Jay, Locus']
    read_file('./practice', 'lesson8', list_content)
    file_bak('./practice', 'lesson8', './bak')
    
    
if __name__ == '__main__':
    main()


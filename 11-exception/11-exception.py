#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import os

def IO_Error(filename):
	# 错误写法，程序会退出并报错 -->  IOError: [Errno 2] No such file or directory: 'notExistFile.json'
    # with open('notExistFile.json') as f_name:
    #         contents = f_name.read()
    
    # 正确写法,程序不会报错退出
    try:
        with open(filename) as f_name:
            contents = f_name.read()
            contents.close
            print contents
    # except FileNotFoundError:                # python3使用的文本不存在异常处理方法
    except IOError:                            # 输入/输出操作失败  # 在python2.7中使用IOError
        msg = "文件: " + filename + "不存在"
        return msg

def Name_Error():
    # NameError: global name 'a' is not defined
    # for i in range(10):
    #     print a
    
    try:
        for i in range(10):
            print a
    except NameError as e:                         # 未声明/初始化对象 (没有属性)
        print '错误类型: NameError -> 未声明/初始化对象 (没有属性)'
    	return e

def Type_Error():
    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
    # operand = 1 + 'a'

    try:
        operand = 1 + 'a'
        print "1 + 'a'计算结果为",operand
    except TypeError as e:                         # 对类型无效的操作
        print '错误类型: TypeError -> 对类型无效的操作'
        return e

def Index_Error(index):
    # IndexError: list index out of range
    # a = range(10)
    # print a[20]
    
    try:
        a = range(10)
        print a[index]
    except IndexError as e:                        # 序列中没有此索引(index)
        print "错误类型: IndexError -> 序列中没有此索引(index)"
        return e

def Attribute_Error():
    # AttributeError: 'str' object has no attribute 'list'
    # '1'.list

    try:
    	print '1'.list
    except AttributeError as e:                  # 对象没有这个属性
        print "错误类型: AttributeError -> 对象没有这个属性"
        return e

def getValue(index):
    try:
        mylist = ["Bob", "Steven", "Nancy", "Vicent", "Kevin"]
        return mylist[index]
    except IndexError:
        print '\033[1;32;40m序列中没有此索引(index)\033[0m'
        return None

# def read_file(filename):
#     if not os.path.exists(filename):
#         os.mknod(filename)
#     try:
#         r_file = open(filename,'r')
#         try:
#             r_file.write('往只读文件中写入数据')
#             raise Exception,"往只读文件中写入数据错误"  # 不会被执行，执行的是try exception
#         except IOError as e:              # File not open for writing        
#             return e
#         finally:
#             r_file.close() 
#             print '\033[1;32;40mfile %s had close \033[0m' %filename
#     except Exception as e:                     # IOError: [Errno 2] No such file or directory: 'hahah.txt'
#         return e

def read_file(filename):
    if not os.path.exists(filename):
        os.mknod(filename)
    try:
        r_file = open(filename,'r')
        try:
            r_file.write('往只读文件中写入数据')          
        except IOError as e:              # File not open for writing
            raise Exception,"往只读文件中写入数据错误" 
        finally:
            r_file.close() 
            print '\033[1;32;40mfile %s had close \033[0m' %filename
    except Exception as e:                     # IOError: [Errno 2] No such file or directory: 'hahah.txt'
        return e

def read_file2(filename):
    if not os.path.exists(filename):
        os.mknod(filename)
        raise Exception,"使用raise测试文件%s不存在,新建文件!!" %filename    
    try:
        r_file = open(filename,'r')
        r_file.write("往只读文件中写入数据")
    except IOError as e:     #python2 File not open for writing   #python3 not writable
        print(e)
    finally:
        r_file.close() 
        print '\033[1;32;40m文件 %s 已经被关闭\033[0m' %filename  


def main():
    
    print '##########   热身开始  ############'
    # 1.尝试读取一个不存在的文件notExistFile.json，确认其异常类型
    result = IO_Error('notExistFile.json')
    if result:
        print '报错信息',result
    else:
        print "运行失败,返回结果: ",result

    # 2.复制以下代码到python命令行看会出现什么结果
    result = Name_Error()
    if result:
        print '报错信息',result
    else:
        print "运行失败,返回结果: ",result

    # 3. 尝试输入1+'a'，查看异常类型
    result = Type_Error()
    if result:
        print '报错信息',result
    else:
        print "运行失败,返回结果: ",result

    # 4. a=range(10)，尝试获取a[20]，查看异常类型
    result = Index_Error(20)
    if result:
       print '报错信息',result
    else:
        print "运行失败,返回结果: ",result

    # 5.尝试'1'.list，了解其异常类型
    result = Attribute_Error()
    if result:
       print '报错信息',result
    else:
        print "运行失败,返回结果: ",result


    print '\r\n\033[1;32;40m##########   作业正式开始  ############\033[0m'
    # 1. 尝试读取一个不存在的文件，文件不存在，脚本并不会退出，而是打印错误信息，该文件不存在
    result = IO_Error('notExistFile.json')
    if result:
        print '\033[1;32;40m%s\033[0m\r\n' %result
    else:
        print "\033[1;32;40m运行失败,返回结果: %s\033[0m\r\n" %result

    # 2. 为如下函数添加异常处理，使其在调用getValue(index=20)时不会出错退出，而是返回None
    result = getValue(20)
    if result==None:
        print '\033[1;32;40m返回结果设置为None成功\033[0m\r\n'
    else:
        print "\033[1;32;40m返回结果设置为None失败,返回结果: %s\033[0m\r\n" %result

    # 3. 以只读方式打开一个文件，尝试向其写入任意字符，捕获异常，使用raise提示错误，无论如何，在finally中将文件句柄关闭
    
    result = read_file('11_test.txt')
    if result:
        print '\033[1;32;40m返回结果: %s\033[0m\r\n' %result
    else:
        print "\033[1;32;40m运行失败,返回结果: %s\033[0m\r\n" %result

    try:
        read_file2('11_test.txt')
    except Exception as e:
        print '\033[1;32;40m异常信息是: %s\033[0m\r\n' %e
    
if __name__ == '__main__':
    main()

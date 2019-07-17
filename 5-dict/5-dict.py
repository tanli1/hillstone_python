#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import string
import random
import yaml
import ast

def read_yamlfile(yamlfile):
    """read yaml file"""

    f = open(yamlfile)
    cfg = f.read()
    f.close()
    testcase = yaml.safe_load(cfg)

    return testcase

def step1():
    # list1是从1到200，一共200个元素的list;示例list1 = [1,2,...,199,200]

    list1 = []
    for i in range(1,201):
        list1.append(i)
    
    # list2是从string.ascii_letters+string.digits中随机取值，组成一共200个元素的list。要求：元素为1个字符的元素共20个，元素为2个字符的元素共20个，...，元素为10个字符的元素共20个，一共200个元素。示例list2 = ['a','c','1','0D','Ss','ac','dFgT0','dfgHtY6570',...]
    list2 = []
    for i in range(1,11):
        for j in range(0,20):
            char = string.ascii_letters + string.digits         # string
            string_var = string.join(random.sample(char, i)).replace(" ","")  
            list2.append(string_var)

    return list1,list2

def step2(yaml_file):
    # 1. 读取test1.yaml文件的内容，并将所有内容赋值给一个字典dict1，并打印字典dict1

    dict1 = {}
    yaml_dict = read_yamlfile('%s' %yaml_file)   # yaml_dict type islist
    for i in range(len(yaml_dict)):
        dict1 = dict(dict1.items() + yaml_dict[i].items())
    return dict1


def step3(dict2,key1,key2):

    dict_new = {}
    test = dict2[key1]
    for i in test:
        dict_new.update(i)
    string = dict_new[key2]           # 取字典中key为body的值
    list1 = ast.literal_eval(string)  # 字符转列表  # ast.literal_eval()将字符串型的列表，元组，dict转变成原有的类型
    for i in list1:
        dict_new.update(i)
    
    return dict_new

def step4(dict2,list1,list2):
    
    for key, value in dict2.items():
        if isinstance(dict2[key], str):
            dict2[key] = random.choice(list2)
        elif isinstance(dict2[key], int):
            dict2[key] = random.choice(list1)
        elif isinstance(dict2[key], list): 
            for i in value:
                step4(i,list1,list2)
    return dict2

def main():

    #1. 打印字典dict1
    list1,list2 = step1()
    if list1 and list2:
        print '1. 创建list1: ',list1
        print '1. 创建list2: ',list2
    elif not list1:
        print '1. 生成list1失败 ',list1
    elif not list2:
        print '1. 生成list2失败 ',list2

    #2. 读取test1.yaml文件的内容，并将所有内容赋值给一个字典dict1，并打印字典dict1
    dict1 = step2('./test1.yaml')
    if dict1:
        print '2. 打印字典dict1: ',dict1
    else:
        print '2. 生成字典dict1错误: ',dict1

    # 3. 将dict1中的key:body的value部分转换成一个字典dict2，并打印字典dict2
    dict2 = step3(dict1,key1='test',key2='body')
    if dict2:
        print '3. 打印字典dict2: ',dict2
    else:
        print '3. 生成字典dict2错误: ',dict2
    
    # 4. 对dict2进行处理,得到新字典dict3，并打印字典dict3
    dict3 = step4(dict2,list1,list2)
    if dict3:
        print '4. 打印字典dict4: ',dict3
    else:
        print '4. 生成字典dict4错误: ',dict3

  
if __name__ == '__main__':
    main()

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import ast
import yaml

def read_yamlfile(yamlfile):
    """read yaml file"""

    f = open(yamlfile)
    cfg = f.read()
    f.close()
    testcase = yaml.load(cfg)
    #print type(testcase)
    return testcase

def step1(yaml_file):
    # 1. 读取yaml文件的内容，将test部分生成一个字典dict1
    yaml_dict = read_yamlfile('%s' %yaml_file)
    #print type(dict(test[1]))
    #return dict(yaml_dict[1])    # 知道数据结构和要查询的数据的位置

    if isinstance(yaml_dict, dict):
        for i in range(len(yaml_dict)):
            if 'test' in yaml_dict[i].keys():
                return yaml_dict[i]
    elif isinstance(yaml_dict, list):
        for i in range(len(yaml_dict)):
            if isinstance(yaml_dict[i], dict):
                if 'test' in yaml_dict[i].keys():
                    return yaml_dict[i]

def step2(dict1):
    # 将url query的取值部分转换成一个字典dict2
    dict1_value = dict1['test'][1]
    url_value = dict1_value['url']
    dict2 = url_value.split('=')[1]
    dict2 = ast.literal_eval(dict2)  # 字符串转成字典

    return dict2

def step3(dict2):
    # 对dict2进行处理：所有键值对中，值为str类型的key的值都设置成‘test’，值为int类型的key的值都设置成100。得到新字典dict3
    for key, value in dict2.items():
        if isinstance(dict2[key], str):
            # dict2['test'] = dict2.pop(key)     # 替换成key, 删除key,对应的value = dict2.pop(key)
            dict2[key] = 'test'
        elif isinstance(dict2[key], int):
            # dict2[100] = dict2.pop(dict2[key])  # 替换成key
            dict2[key] = 100
        elif isinstance(dict2[key], list): 
            for i in range(len(dict2[key])):             
                if isinstance(dict2[key][i], dict):                # list中的值为字典，把里面的所有值都遍历一下
                    for key1, value1 in dict2[key][i].items():     # 这里不能写key, value不然和上面的key,value混淆了
                        if isinstance(dict2[key][i][key1], str):
                            dict2[key][i][key1] = 'test'
                        elif isinstance(dict2[key][i][key1], int):
                            dict2[key][i][key1] = 100
        elif isinstance(dict2[key], dict):
            for key2, value2 in dict2[key].items():
                if isinstance(dict2[key][key2], str):
                    dict2[key][key2] = 'test'
                elif isinstance(dict2[key][key2], int):
                    dict2[key][key2] = 100
    
    return dict2

def main():

    #1. 打印字典dict1
    dict1 = step1('./test.yaml')
    if dict1:
        print '1. 打印字典dict1: ',dict1
    else:
        print '1. 生成字典dict1错误: ',dict1

    #2. 打印该字典示例dict2 = {"conditions":[{"field":"name","operator":0,"value":"test"}],"start":0,"limit":20,"page":1}
    dict2 = step2(dict1)
    if dict2:
        print '2. 打印字典dict2: ',dict2
    else:
        print '2. 生成字典dict2错误: ',dict2

    # 3. 打印处理后的新字典dict3。示例dict3 = {"conditions":[{"field":"test","operator":100,"value":"test"}],"start":100,"limit":100,"page":100}
    dict3 = step3(dict2)
    if dict3:
        print '3. 打印字典dict3: ',dict3
    else:
        print '3. 生成字典dict3错误: ',dict3
  
   
    
if __name__ == '__main__':
    main()

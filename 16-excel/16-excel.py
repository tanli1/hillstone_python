#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#
# https://www.jianshu.com/p/f2c9dff344c6

import xlrd
import json
import sys
from optparse import OptionParser

reload(sys)
sys.setdefaultencoding('utf8')

def filePath(file_para):
    parser = OptionParser()
    parser.add_option(file_para,dest="filePath")
    (options, args)= parser.parse_args()
    return options.filePath

def open_excel(excel_file):
    try:
        data = xlrd.open_workbook(excel_file)
        return data
    except Exception,e:
        print str(e)

def read_excel(file,colnameindex=0,rownameindex=0, by_name=u'Sheet1'):  #colnameindex：表头列名所在行的索引,rownameindex:表头列名所在列的索引, by_name：Sheet1名称
    dict1 = {}
    
    workbook = open_excel(file) #打开excel文件
    sheet1_is_load = workbook.sheet_loaded(sheet_name_or_index=0)  # 通过index判断sheet1是否导入
    if sheet1_is_load:
        sheet1_object = workbook.sheet_by_index(0)   # 通过index获取第一个sheet对象
        nrows = sheet1_object.nrows   # 获取sheet1中的有效行数
        ncols = sheet1_object.ncols   # 获取sheet1中的有效列数

        for i in range(rownameindex+1,nrows):
            list1 = []
            for j in range(colnameindex+1,ncols):
                if sheet1_object.cell_value(rowx=i, colx=j) == '':   # 判读表格中的值是否为空，是就把值设置为0
                    value = 0
                else:
                    value = sheet1_object.cell_value(rowx=i, colx=j)
                list1.append(value)
            dict1[sheet1_object.row_values(rowx=i)[rownameindex]]=list1
           
        return dict1

        
def list_add(dict1):
    dict2 = {}
    
    for key, value in dict1.items():
        count = 0
        for i in range(len(dict1[key])):
            count = count + dict1[key][i]
        dict2[key] = count
    
    return dict2


def main():
    excel_file = filePath('-f')

    result = read_excel(file=excel_file, colnameindex=0,rownameindex=0, by_name=u'Sheet1')
    if result:
        print "读取excel表格中的数据，将其保存在一个字典中，字典如下："
        print json.dumps(result, ensure_ascii=False, encoding='UTF-8')    # 字典中中文打印不乱码
    else:
        print "读取excel表格中的数据失败!" 
    result = list_add(result)
    if result:
        print '每行计算总和后的值: '
        print json.dumps(result, ensure_ascii=False, encoding='UTF-8')
    else:
        print "计算excel每行的数据失败!"


  
if __name__ == '__main__':
    main()

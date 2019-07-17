#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2006-2019 Hillstone Networks, Inc.
# author: ltan
#


import sys
type = sys.getfilesystemencoding()  # 为了在dos窗口能正确显示正文，显示正文需要在中文后加.decode('utf-8').encode(type)


def main():
    def l_print(explain, variable):
        if type == "UTF-8":
            print "\033[31;40m%s: \033[0m\033[32;40m%s\033[0m" %(explain, variable) 
        else:
            print explain.decode('utf-8').encode(type), variable
            
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']

    l_print("1. 第一个列表是", list1)
    l_print("1. 第二个列表是", list2)

    list1.extend([11,12])
    list1.insert(0,0)
    l_print("2. 对第一个列表进行操作，分别在头部增加0和尾部增加11,12", list1)

    #list2.remove(20)
    #l_print("3. 对第二个列表进行操作，删除20", list2)

    for i in range(len(list2)/2):
        if i >= 1:
            del list2[i]
    l_print("3. 对第二个列表进行操作，每隔1个元素，删除1个，比如['a','c','e',...]", list2)

    list1.extend(list2)
    l_print("4. 将列表1与列表2合并为一个列表", list1)

    # 第一种方法
    new_list = []
    for i in range(0, len(list1), 3):
        new_list.append(list1[i])
    l_print("5. 从合并后的列表中每3个元素取出一个，形成一个新列表", new_list)

    # 第二种方法
    new_list = list1[0::3]
    l_print("5. 从合并后的列表中每3个元素取出一个，形成一个新列表", new_list)

    new_list.reverse()
    l_print("6. 对新列表进行逆序操作", new_list)

    obj = 11
    try:
        var = new_list.index(obj)
    except ValueError:
        var7 = "%s 不在新列表中" %obj
    else:
        var7 = "列表中包含11"
    l_print("7. 查找列表中是否包含11", var7)

    var8 = len(new_list)
    l_print("8. 计算当前列表长度", var8)

    l_print("9. 打印新列表中的每一个元素", new_list)
    for i in range(var8):
        l_print("第%s个元素" %i, new_list[i])


if __name__ == '__main__':
    main()




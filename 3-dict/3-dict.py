#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

#import sys
#import string
import operator


dict1 = {}
dict2 = {}

def step1():    
    # step1:  创建2个字典： dict1 = {'a':'97','b':'98','c':'99','d':'100',...,'v':'118'}----22个键值对 dict2 = {'a':'222','d':'111','z':'122'}
    key = [chr(i) for i in range(97,119)]
    #value = list(range(97,118))
    value =[str(i) for i in range(97,119)]
    dict1 = dict(zip(key,value))
    print '1. 字典dict1是: ',dict1
    
    dict2 = {'a':'222','d':'111','z':'122'}
    print '1. 字典dict2是: ',dict2
    return dict1,dict2
 
def step2(d): 
    # step2 dict1中插入两个元素，x=120，y=121后的字典
    d['x'] = 120
    d['y'] = 121
    print '2. dict1中插入两个元素，x=120，y=121后的字典为: ',d
 
def step3(dict1):
    # step3 更新dict1元素b=99
    dict1['b'] = 99
    print '3. 更新dict1元素b=99后: ',dict1
 
def step4(dict1): 
    # step4 删除dict1元素c
    dict1.pop('c')
    print '4. 删除dict1元素c后: ',dict1
 
def step5(dict1,dict2):
    # step5 使用dict2更新dict1：dict1.update(dict2)
    dict1.update(dict2)
    print '5. 使用dict2更新dict1：dict1.update(dict2): ',dict1
    
def step6(dict1):
    # step6 判断dict1如果含有元素w，然后判断w的值，如果没有此元素就添加w元素，值为234，然后判断如果元素值为234，就删除w元素
    if dict1.get('w') == 234:
        dict1.pop('w')
    else:
        dict1.setdefault('w',234)
        dict1.pop('w')
    print '6. 判断dict1如果含有元素w，然后判断w的值，如果没有此元素就添加w元素，值为234，然后判断如果元素值为234，就删除w元素: ',dict1
    
def step7(dict1):
    # step7 在步骤6的基础上，将字典的元素按value排序
    #第一种方法：sorted_x=sorted(dict1.items(),key=operator.itemgetter(1))         #按照item的第二个字符排序，即value排序
    print '7. 在步骤6的基础上，将字典的元素按value排序: ',sorted(dict1.items(),key = lambda x:x[1])
    
def step8(dict1):
    # step8 在步骤6的基础上，将字典的元素按key排序
    #第一种方法：sorted_x=sorted(dict1.items(),key=operator.itemgetter(0))         #按照item中的第一个字符进行排序，即按照key排序
    print '8. 在步骤6的基础上，将字典的元素按key排序: ',sorted(dict1.items(),key = lambda x:x[0])

def main():
    #global dict1
    #global dict2
    
    dict1,dict2 = step1()
    step2(dict1)
    step3(dict1)
    step4(dict1)
    step5(dict1,dict2)
    step6(dict1)
    step7(dict1)
    step8(dict1)
    
if __name__ == '__main__':
    main()

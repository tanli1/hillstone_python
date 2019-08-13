#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

def clockAngle(hour, minute):
    hour_origin = hour
    if hour >= 12:
        hour = hour - 12
    if hour < 12:
        minute_index = float(minute)/60*12
        hour_index = hour + float(minute)/60
        angle = (minute_index - hour_index) * 30 
        if angle > 180:
            angle = 360 - angle
        print('clockAngle(%s, %s)=' %(hour_origin,minute),'{:g}'.format(angle))   # 浮点数尾部无效0和.去掉


def newClockAngle(hour="", minute=""):
    hour_origin = hour
    if hour >= 12:
        hour = hour - 12
    if hour < 12:
        minute_index = float(minute)/60*12
        hour_index = hour + float(minute)/60
        angle = (minute_index - hour_index) * 30 
        if angle > 180:
            angle = 360 - angle
        print('clockAngle(%s, %s)=' %(hour_origin,minute),'{:g}'.format(angle))


def printMsg(name, bonjour, *args):
    a = ''
    for i in range(len(args)):
        a = a + (args)[i] + ' '
    print('%s Say: %s %s' %(name,bonjour, a))


def main():

    print('定义一个计算钟表的时针和分针最小夹角的函数')
    clockAngle(2, 30)
    clockAngle(13, 42) 
    clockAngle(1, 43)
    
    print('\n对上面练习中的函数进行重构')
    newClockAngle(minute=42, hour=13)
    newClockAngle(1, 43)

    print('\n可变长度参数传递，定义一个printMsg的函数,使用*args参数')
    printMsg("Bob", "Hello.")
    printMsg("Kevin", "Hello,", "My", "best", "friend")


    
    
if __name__ == '__main__':
    main()

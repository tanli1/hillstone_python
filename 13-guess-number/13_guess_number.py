#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import random

def guess_number():

    print('=' * 10 + '  猜数字游戏开始啦！  ' + '=' * 10)
    luck_num = random.randint(1,100)
    print('=' * 10 + '  系统已经随机产生了一个1-100的整数！  ' + '=' * 10)
    count = 0
    input_list = []
    while True:
        input_num = raw_input("请输入你猜的数字：")
        if input_num.isdigit():
            if int(input_num) > 100:
            	print("输入的数据超过了最大值100！") 
            elif int(input_num) < 1:
            	print("输入的数据小于最小值1！") 
            else:
                input_list.append(input_num)
                if int(input_num) == luck_num:
                    print("恭喜你，猜对了！")
                    break
                elif int(input_num) > luck_num:
                    print("猜的数字太大啦！")
                elif int(input_num) < luck_num:
                    print("猜的数字太小啦！")
        else:
        	print("输入的数据类型错误！")

    if len(input_list) > 5:
        print("======  嘲笑哟, 你猜了%s 次才猜对!  ======" %len(input_list))
        print("亲，这次你输入的数字有：%s" %input_list)

    else:
        print("======  你好聪明，猜了%s次就猜对了！ ======" %len(input_list))
        print("亲，这次你输入的数字有：%s" %input_list)





def main():

    guess_number()
    
    
if __name__ == '__main__':
    main()
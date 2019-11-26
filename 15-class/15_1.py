#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Copyright (c) 2016-2019 Hillstone Networks, Inc.
#
# Author:ltan
#

import random
import string
import os,sys


class Happy(object):
    def __init__(self):
        #self.gameType = gameType
        self.element = self.getItem()

    def getItem(self):
        # 随机生成一个数字或字符
        print '请输入选择的游戏类型：int是猜数字，string是猜字符，quit退出游戏！'
        self.gameType = self.getInput()
        if self.gameType == 'int':
            init_number = random.randint(1,100)
            return init_number
        elif self.gameType == 'string':
            init_string = random.choice(string.ascii_letters)
            return init_string
        elif self.gameType == 'quit':
            sys.exit(1)
        else:
            return None

    def play(self):
        input_num = ''
        if self.gameType == 'int':
            self.count = 0
            self.input_list = []
            
            while input_num != 'quit':
                input_num = raw_input("请输入你猜的数字：")
                self.count += 1
                if input_num.isdigit():
                    if int(input_num) > 100:
                        print("输入的数据超过了最大值100！") 
                    elif int(input_num) < 1:
                        print("输入的数据小于最小值1！") 
                    else:
                        self.input_list.append(input_num)
                        if int(input_num) == self.element:
                            print("恭喜你，猜对了！")
                            break
                        elif int(input_num) > self.element:
                            print("猜的数字太大啦！")
                        elif int(input_num) < self.element:
                            print("猜的数字太小啦！")
                else:
                    print("输入的数据类型错误！")
        elif self.gameType == 'string':
            self.count = 0
            self.input_list = []
           
            while input_num != 'quit':
                input_num = raw_input("请输入你猜的字符：")
                self.count += 1
                if input_num.isalpha():
                    self.input_list.append(input_num)
                    if input_num == self.element:
                        print("恭喜你，猜对了！")
                        break
                    elif input_num > self.element:
                        print("猜的字符太大啦！")
                    elif input_num < self.element:
                        print("猜的字符太小啦！")
                else:
                    print("输入的数据类型错误！")
        else:
            print '输入选择游戏的值错误，只能输入 int 或者 string'
            sys.exit(1)

    def getInput(self):
        x = raw_input()

        return x

    def show(self):
        print '系统产生的随机值: %s' %self.element

    def finalPrint(self):
        if self.count < 10:
            print '你很棒，猜了%s次就猜对了' %self.count
            print '你猜过的值: %s' %self.input_list
            self.show()
        else:
            print '你要加油，猜了%s次才猜对' %self.count
            print '你猜过的值: %s' %self.input_list
            self.show()



def main():

    myhappy = Happy()
    myhappy.play()
    myhappy.finalPrint()

    
if __name__ == '__main__':
    main()
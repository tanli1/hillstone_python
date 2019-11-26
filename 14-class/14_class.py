import random
import string

class Happy(object):

    def __init__(self):
        self.element = self.getItem()

    def getItem(self):
        # 随机生成一个数字或字符
        H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        return random.choice(H)

    def show(self):
        print self.element


def main():
    

    myhappy = Happy()

    input = ''
    while input != 'quit':
        print '生成的随机数：',myhappy.getItem()
        print '输入quit结束游戏，输入其他任意字符按回车键继续'
        input=raw_input()
    
    
if __name__ == '__main__':
    main()

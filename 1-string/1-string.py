#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
type = sys.getfilesystemencoding()  # 为了在dos窗口能正确显示正文，显示正文需要在中文后加.decode('utf-8').encode(type)

# 打印输入函数
def l_print(explain, variable):
    if isinstance(variable, int) or  isinstance(variable, float):
        variable = str(variable)
    if type == "UTF-8":
        print "\033[31;40m%s\033[0m".decode('utf-8').encode(type) %explain,"\033[32;40m" + variable + "\033[0m" 
    else:
        print explain.decode('utf-8').encode(type), variable
        
l_print("运行平台默认编码是: ",type)

var = "abcdefghijkl123mnopqrstuvwxyz<> 123def4567890 [] #&*"
l_print("1. 生成一个字符串: ", var)

var_len = len(var)
l_print("2. 计算字符个数: ", var_len)

var1 = "+" + var + "-"
l_print('3. 往字符头部添加字符"+"，往字符尾部添加字符"-" : ', var1)

var2 = var.replace('d','\d').upper()
l_print("4. 将字符d替换成\d，将小写字母替换成大写字母: ", var2)

var3 = var.replace(" ","")
l_print("5. 去掉空格: ", var3)

var4 = ""
for para in var:
    if not para.isdigit() and not para.isalpha():
        var4 = var4 + para
l_print("6. 去掉字母和数字: ", var4)

var5 = ""
for i in range(len(var)):
    if i == (len(var)-1):
        var5 = var5 +var[i]
    else:
        var5 = var5 + var[i] + "="
l_print('7. 将每个字符都用"="号隔开: ', var5)

n = 1
var6 = ''
for i in range(len(var)):
    b = n*(n+1)/2 -1
    if b == i:
        var6 = var6 + var[i] + "="
        n = n + 1
    else:
        var6 = var6 + var[i]
l_print('8. 将字符按1/2/3/4/5......个字符,用"="隔开，就"a=bc=def=hijk=......": ', var6)

# [start:end:step] 从start 提取到end - 1，每step 个字符提取一个
var7 = var[::-1]
l_print("9. 字符串反转: ", var7)

var8 = var * 2
l_print("10. 字符串复制n=2次: ", var8)




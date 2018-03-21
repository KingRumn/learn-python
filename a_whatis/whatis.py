#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# This is 廖雪峰的python教程

#-----------------------------------------
#               基础内容
# ----------------------------------------
# 文件名【字母/数字/下划线】.py

# 首行必须指明所需要的解释器，否则无法通过./xx.py的方式执行

# -*- coding:utf-8 -*-指明了编码格式，否则中文无法正常输出


# 输出Python的版本
import platform
print (platform.python_version())

import sys
print (sys.version)
print (sys.version_info)

# python3 必须括号
print ("Hello World.")
print ("你好，Python.")


#-----------------------------------------
#               输入输出
# ----------------------------------------
# 依次打印每个字符串，遇到，会输出一个空格
print('The quick brown fox', 'jumps over', 'the lazy dog.')
# 可打印计算结果
print('100 + 200 = ', 100 + 200)

# input()输入
print('请输入你的名字： ')
name = input()
print('Hello, ', name)


#-----------------------------------------
#               基础语法
# ----------------------------------------
# 以#作为注释
# 缩进4个空格
# 大小写敏感

# 整数
# 可处理任意大小的整数， 0x表示16进制
print(1)
print(2000000)
print(-8876544)
# 浮点数
print(1.23e9)
print(3.24e-19)

# 字符串，以单引号或双引号括起来，互相嵌套，\转义
print("I'm OK, \"Tommy\".")
# 以r''表示内部的内容不转义
print(r"\\\\ok")
# 以'''...'''表示多行内容
print(''' first line.
second line.
third line.''')

# 布尔值 True/False, and/or/not
print(True and False)

# 空值 None, 并非0,0是有意义的

# 变量
# 动态语言类型，变量类型无需定义
a = 'ABBC'
b = a
a = 'XYZ'
print(b)      #ABBC

# 常量
PI = 3.14159

# 地板除和除法
print(10 / 3)   #3.333333
print(10 // 3)  #3
print(-10 // 3)  #取比之小的最大整数 4


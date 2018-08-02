#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "KingRumn"

'''
    进程和线程
    fork进程，multiprocessing跨平台进程，
'''

import subprocess

# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出
print('$ ping www.baidu.com')
r = subprocess.call(['ping', 'www.baidu.com', '-n', '1'])
print('Exit code:', r)

# 如果子进程还需要输入，则可以通过communicate()方法输入
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('gbk'))
print('Exit code:', p.returncode)


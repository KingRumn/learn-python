#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "KingRumn"

'''
    进程和线程
    fork进程，multiprocessing跨平台进程，
'''

from multiprocessing  import Process
import os

# 多进程
# Unix/Linux操作系统提供了一个fork()系统调用，os.fork()封装了fork系统调用，windows系统无法使用
'''
print('Process (%s) start...' % os.getpid())
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''


# multiprocessing模块就是跨平台版本的多进程模块
# multiprocessing模块提供了一个Process类来代表一个进程对象
# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    # start()方法启动子进程
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('Child process end.')
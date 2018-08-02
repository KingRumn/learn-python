#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "KingRumn"

'''
    进程和线程
    fork进程，multiprocessing跨平台进程，进程间通信
'''

from multiprocessing import Process, Queue
import os, time, random


# multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据
# 以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    tq = Queue()
    pw = Process(target=write, args=(tq,))
    pr = Process(target=read, args=(tq,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。
# 由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。

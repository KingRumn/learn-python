#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = "KingRumn"

'''
    进程和线程
    fork进程，multiprocessing跨平台进程，
'''

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    # join()之前必须先调用close(), 之后就不能继续添加新的Process了
    p.close()
    #  join()方法会等待所有子进程执行完毕
    p.join()
    print('All subprocesses done.')
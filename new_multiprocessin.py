#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: new_multiprocessin.py
@time: 2019/2/21 10:41
"""
from multiprocessing import Process, Pool
import os,time,random

def child_target():
    print('child proc is running %s' % os.getpid())

def test_multiprocessing():
    print('parent proc is running %s' %os.getpid())
    p = Process(target=child_target)
    p.start()
    p.join()
    print('proc ended %s' % os.getpid())

def long_time_task():
    print('child proc running %s' % os.getpid())
    st = time.time()
    time.sleep(random.randint(1,3))
    et = time.time()
    print('child proc %s run %s seconds' %(os.getpid(),et-st))

def use_pool():
    print('parent proc is running %s' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(func=long_time_task)
    print('waiting child proc done')
    p.close()
    p.join()
    print('child proc done')

def main():
    # test_multiprocessing()
    use_pool()

if __name__ == "__main__":
    main()




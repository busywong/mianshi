#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: multiprocessing.py
@time: 2019/2/20 14:32
"""
# from multiprocessing import Process

from multiprocessing import Process,Pool
import os,time,random

# 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
def child_process():
    print('child process  is running %s'  %os.getpid())

def do_process():
    print('Parent process is running %s' % os.getpid())
    p = Process(target=child_process, name='test')
    p.start()
    p.join()

def long_time_task():
    print('child proc is running %s' % os.getpid())
    st = time.time()
    time.sleep(random.randint(1,3))
    et = time.time()
    print('child proc running %s  pid is %s' %((et-st),os.getpid()))

def do_pool():
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task)
    print('waiting child proc done')
    p.close()
    p.join()
    print('child proc done')


def main():
    do_pool()

if __name__ == "__main__":
    main()




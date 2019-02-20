#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: use_threading.py
@time: 2019/2/20 11:34
"""
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t1 = threading.Thread(target=loop,name='thread-1')

t.start()
t1.start()
t.join()
t1.join()
print('thread %s ended.' % threading.current_thread().name)

# def main():
#     pass
#
#
# if __name__ == "__main__":
#     main()




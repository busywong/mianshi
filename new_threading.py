#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: new_threading.py
@time: 2019/2/21 10:08
"""
import threading
import time
def loop():
    print('threading proc %s is running ' % threading.current_thread().name)
    n = 0
    while n<5:
        n+=1
        print('threading %s >>> %s' %(threading.current_thread().name, n))
        time.sleep(1)
        # print('threading  %s end' %threading.current_thread().name )



def main():
    print('main threading %s running' % threading.current_thread().name)
    t = threading.Thread(target=loop,name='test_threading')
    t1 = threading.Thread(target=loop, name='test_threading1')
    t.start()
    t1.start()
    t.join()
    t1.join()
    print('thread %s ended' % threading.current_thread().name)

if __name__ == "__main__":
    main()




#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: digui.py
@time: 2019/2/19 9:51
"""
from functools import reduce

def digui(num):
    if num == 1:
        return 1
    else:
        return num * digui(num-1)


def fbnq(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        return fbnq(num-1) + fbnq(num-2)

def add_num(x,y):
    reduce(x+y, range(x))

def main():
    # print(digui(5))
    print(fbnq(5))

if __name__ == "__main__":
    main()




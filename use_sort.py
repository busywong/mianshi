#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: use_sort.py
@time: 2019/2/19 15:23
"""
import re

def str_sort():
    s = 'string'
    s1 = list(s)
    s1.sort()
    b = ''.join(s1)
    print(b)

def case_insensitive_sort2(liststring):
    return sorted(liststring,key = str.lower)

def sort_list():
    l = ['ch9.txt', 'ch10.txt', 'ch1.txt', 'ch3.txt', 'ch11.txt']
    list_a = []
    res = []
    for a in l:
        s= re.search('\d+',a).group()
        list_a.append(int(s))
    list_a.sort()
    for la in list_a:
        sa = 'ch'+ str(la) + '.txt'
        res.append(sa)
    print(res)

def len_sort():
    xs = ['dddd', 'a', 'bb', 'ccc']
    xs.sort(key=len)
    print(xs)
def main():
    # str_sort()
    # r = case_insensitive_sort2(list('string'))
    # print(r)
    # sort_list()
    len_sort()
if __name__ == "__main__":
    main()




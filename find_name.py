#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: find_name.py
@time: 2019/2/26 20:30
"""
import re
def get_name():
    with open(r"C:\Users\wong\Desktop\11.txt",'r') as f:
        # print(f.read())
        res = re.findall("(\w+)@joyware.com", f.read())
        return res


def main():
    get_name()


if __name__ == "__main__":
    main()




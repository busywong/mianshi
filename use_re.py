#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: use_re.py
@time: 2019/2/18 20:17
"""
import  re

def match_a():
    a = "abcd12345ed125ss123456789"
    res = re.findall("\d{1,}", a)  # ^\d{n,}$   \d{1,}
    print(res)
    res_num = []
    for num in res:
        # for n in num:
        print(num)
        i = 0
        while i < len(num):
            # print(int(num[i]))
            if int(num[i]) + 1 == int(num[i + 1]):
                i += 1
                if i == len(num) - 1:
                    res_num.append(num)
                    break
            else:
                break

    print(res_num)
    len_num = []
    for num in res_num:
        len_num.append(int(num))
    print(max(len_num))

def match_url():
    a = 'https://www.baidu.com/kk'   # http|https://www\.\w+\.\w+/
    res = re.findall('http[s]?://www\.\w+\.\w+/',a)  # ^((http://)|(https://))?([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}(/)
    print(res)


def main():
    match_url()
    # match_a()

if __name__ == "__main__":
    main()




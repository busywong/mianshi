#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: sock_cli.py
@time: 2019/2/20 11:08
"""

import socket

def main():
    info = ('127.0.0.1', 6007)
    s = socket.socket()
    s.connect(info)
    # while True:
    s.send(b'aaa')
    s.close()


if __name__ == "__main__":
    main()




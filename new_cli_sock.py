#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: new_cli_sock.py
@time: 2019/2/21 9:51
"""
import socket

def new_cli_sock():
    info = ('127.0.0.1', 6608)
    s = socket.socket()
    s.connect(info)
    s.send(b'aaa')
    s.close()

def main():
    new_cli_sock()


if __name__ == "__main__":
    main()




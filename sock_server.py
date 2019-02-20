#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: sock_server.py
@time: 2019/2/20 11:04
"""
import socket


def main():
    info = ('127.0.0.1', 6007)
    s = socket.socket()
    s.bind(info)
    s.listen(5)
    while True:
        conn,addr = s.accept()
        # while True:
        recv_data = conn.recv(1024)
        print(recv_data)

if __name__ == "__main__":
    main()




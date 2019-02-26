#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: new_server_sock.py
@time: 2019/2/21 9:47
"""
import socket

def my_server_sock():
    info= ('127.0.0.1', 6608)
    s = socket.socket()
    s.bind(info)
    s.listen(5)
    while True:
        conn, addr = s.accept()
    # while conn:
        data = conn.recv(1024)
        print(data)



def main():
    my_server_sock()


if __name__ == "__main__":
    main()




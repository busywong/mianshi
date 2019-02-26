#!/usr/bin/python
# coding:utf-8 
"""@author: wong
@contact: wangjiwen@joyware.com
@software: PyCharm Community Edition
@file: insert_user.py
@time: 2019/2/26 20:14
"""
import pymongo
from mianshi.find_name import get_name

def get_user_col():
    client = pymongo.MongoClient('10.100.23.104', 27017)
    user_col = client.DOClever.users
    # cursor = user_col.find()
    return user_col
    # for user in cursor:
    #     print(user)
def insert_user(name):

    user_col = get_user_col()
    name_list = get_name()
    for name in name_list:
        res = user_col.insert_one({'name': name, 'password':'123456'})
        print(res.raw_result)
def main():
    # conn_mongo()
    # insert_user("wjw2")
    user_col = get_user_col()
    res = user_col.insert_one({'name': 'wx1', 'password': '123456'})
    print(res.inserted_id)
    res.raw_result

if __name__ == "__main__":
    main()




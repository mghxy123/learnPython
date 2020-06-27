#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/8/10 11:00


import redis

db = redis.Redis('192.168.18.181') # 默认0号库


# set 字符串命令kv

# # db.set('s',0b1100010)
# print(db.keys('*')) # 规模大的时候少用
# print(db.get('s'))
#
#
# db.set(0b11, 0x63)
# print(db.keys('*'))
# print('#'*60)
# print(db.get(3))
# print(db.get('3'))
# print(db.get(b'3'))
# print(db.get(0x03))

# db.set('test', 'abc')
# print(db.get('test'))

# db.set('test1', '中')
# print(db.get('test1'))




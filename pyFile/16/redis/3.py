#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.py
# Author: HuXianyong
# Date  : 2019/8/10 14:57

#日活跃用户统计


import redis

db = redis.Redis('192.168.18.181',6379,5) # 默认0号库 ,连接4号库

db.setbit('d:a:190101',101,1)
db.setbit('d:a:190101',103,1)

db.bitcount('d:a:190101')

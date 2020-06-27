#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.py
# Author: HuXianyong
# Date  : 2019/8/10 14:44

# 活跃用户统计
import redis

db = redis.Redis('192.168.18.181',6379,4) # 默认0号库 ,连接4号库

db.setbit('u:1',30,1)
db.setbit('u:1',100,1)

db.setbit('u:2',90,1)
db.setbit('u:2',200,1)


for i in range(3,366,2):
    db.setbit('u:3',i,1)


for i in range(5,366,3):
    db.setbit('u:4',i,1)

userlist = db.keys('u*')
print(userlist,sep='\n')

active = []
inactives = []

for u in userlist:
    logincount = db.bitcount(u)
    print(u,logincount)
    if logincount > 100:

        active.append(u)
        print('{} is active user'.format(u))
    else:
        inactives.append(u)
        print('{} is inactive user'.format(u))
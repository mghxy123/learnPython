#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : az.py
# Author: HuXianyong
# Date  : 2019/7/17 11:58


import  bcrypt

pwd = 'hxy'.encode()

print(1,bcrypt.gensalt())
print(2,bcrypt.gensalt())

salt = bcrypt.gensalt()

x = bcrypt.hashpw(pwd,salt)
y = bcrypt.hashpw(pwd,salt)

print(x)
print(y)

print(bcrypt.checkpw(pwd,x))
print(bcrypt.checkpw(pwd,y))

print('x'*30)

x = bcrypt.hashpw(pwd,bcrypt.gensalt())
y = bcrypt.hashpw(pwd,bcrypt.gensalt())

print(x)
print(y)

print(bcrypt.checkpw(pwd,x))
print(bcrypt.checkpw(pwd,y))

from datetime import datetime
start = datetime.now()
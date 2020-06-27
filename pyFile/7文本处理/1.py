#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/8/15 16:59

f = open('test3','rb') #二进制只读
s = f.read()
print(type(s)) #bytes
print(s)
f.close()

print('-'*60)
f= open('test3','wb') #IO对象
s = f.write('嘿,小伙子'.encode())
print(s)
f.close()

print('-'*60)
f = open('test3','rb') #二进制只读
s = f.read()
print(type(s)) #bytes
print(s.decode())
f.close()
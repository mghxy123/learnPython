#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.初用makefile.py
# Author: HuXianyong
# Date  : 2019/7/7 21:28

# 使用makefile简单的例子

import socket

server = socket.socket()
server.bind(('127.0.0.1',60000))
server.listen(5)

print('*'*30)

s,_ = server.accept()
print('-'*30)
f = s.makefile(mode='rw')

line = f.read(10) # 按行读取要使用readlinefangfa
print('-'*30)
print(line)

f.write('return your msg: {}'.format(line))
f.flush()

f.close()
print(f.closed,s._closed)
s.close()
print(f.closed,s._closed)

server.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.建立一个客户端.py
# Author: HuXianyong
# Date  : 2019/7/7 1:05



import socket

s = socket.socket() # 创建socket对象
s.bind(('127.0.0.1',60000))
s.listen(5)#开始监听,等待客户端连接到来 5的意思是最多5个连接


# 接入一个到来的连接
s1, info = s.accept() # 阻塞知道和客户端成功建立连接,返回一个新的socket对象和客户端地址
print(s1,info)

# 使用缓冲区获取数据
data = s1.recv(1024) #阻塞 1024是接受数据的大小
print(info, data)
s1.send(b'welcome to network! ') # 这里发送的是二进制数据
s1.close()

# 接入另一个连接

s2, info = s.accept()
data = s2.recv(1024)
print(info,data)
s2.send(b'hello python')

s2.close()
s.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 10.客户端代码.py
# Author: HuXianyong
# Date  : 2019/7/7 23:16

import socket



client = socket.socket()
ipaddr = ('127.0.0.1',60000)
client.connect(ipaddr)

client.send(b'hello server!\n')

data = client.recv(1024)
print(data)

client.close()
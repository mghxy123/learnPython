#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 缓冲区.py
# Author: HuXianyong
# Date  : 2019/8/15 17:16

import io

f = open('test4','w+b')
print(io.DEFAULT_BUFFER_SIZE)
f.write('hello world'.encode())
f.seek(0)
f.write('say hello world'.encode())
f.flush()
f.close()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 换行符.py
# Author: HuXianyong
# Date  : 2019/8/17 8:37

f = open('test','w')
# newline缺省为none,windows下会把\n替换为\r\n
f.write('hello\rmy\nfriend\r\nforand')
# 真正的写入的是
#'hello\rmy\r\nfriend\r\r\nforand'
f.close()
newlines=[None,'', '\n','\r\n']
for n in newlines:
    f = open('test', 'r+', newline = n) # 缺省替换所有换行付
    print(f.readlines())
    f.close()


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : readfile.py
# Author: HuXianyong
# Date  : 2019/8/17 8:51

f = open('test4', 'r+')
f.write('magedu')
f.write('\n')
f.write('马哥教育')
print(f.seek(0))
print(f.read(7))
f.close()
# 二进制
f = open('test4','rb+')
print(f.read(7))
print(f.read(1))
f.close()


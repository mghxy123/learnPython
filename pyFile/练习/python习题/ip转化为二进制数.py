#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : ip转化为二进制整形.py
# Author: HuXianyong
# Date  : 2019/8/27 11:16


# def addr(addrp):
#     for i in addrp.split('.'):
#         print(i,bin(int(i))[2:].zfill(8))
#
#
# addr('1.123.99.122')


x = '0b1111011'
# 二进制转换为十进制
n = int(x,2)
# 十进制转换为八进制
# o = '{0:o}'.format(n)
# o = oct(n)[2:]
o = oct(n)
# 十进制转换为十六进制
# h = '{0:x}'.format(n)
h = hex(n)[2:]
print(n)
print(o)
print(h)
print(int('0x12',16))
print(hex(87)[2:])
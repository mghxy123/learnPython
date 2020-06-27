#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 进制转换.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/8/28 0028

i = 100

# 十进制转换为二进制
print(bin(i))
# 不要0b开头
print('{0:b}'.format(i))

# 十进制转换为八进制
print(oct(i))
# 不要0o开头
print('{0:o}'.format(i))

# 十进制转换为16进制
print(hex(i))
#  不要0x开头
print("{0:x}".format(i))


# 二进制转十进制
b = '0b1100100'
print(int(b,2))

# 八进制转十进制
o = '0o144'
print(int(o,8))

# 16进制转10进制
h = '0x64'
print(int(h,16))

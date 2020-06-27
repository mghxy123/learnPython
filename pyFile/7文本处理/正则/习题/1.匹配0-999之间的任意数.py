#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.匹配0-999之间的任意数.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/10 0010


'''
匹配0-999之间的任意数
'''

import re

str1 = '''1
12
995
9999
102
02
003
4d
55555
6786
5346
34
23'''


regex = re.compile('\d{0,3}',re.S)
a= regex.findall(str1)
print(a)
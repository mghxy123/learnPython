#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 字典排序.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/8/28 0028


dic = {'a':6,'c':4, 'd':5, 'b':7, 'e':2, 'h':1}

dic_key = sorted(dic.items(), key = lambda i:i[0])
dic_value = sorted(dic.items(), key = lambda i:i[1])
print(dic_key)
print(dic_value)
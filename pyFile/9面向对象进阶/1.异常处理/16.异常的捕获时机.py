#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 16.异常的捕获时机.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

def parse_int(s):
    try:
        return  int(s)
    except:
        return 0
print(parse_int('s'))
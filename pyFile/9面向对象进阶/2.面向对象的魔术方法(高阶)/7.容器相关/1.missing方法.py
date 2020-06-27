#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.missing方法.py
# Author: HuXianyong
# Date  : 2019/5/25 20:31

'''
__missing__方法是字典或者其子类使用,__getitem__()调用时,key不能存在时执行发方法
'''

class A(dict):
    def __missing__(self, key):
        print("missing key ",key)
        return 0

a = A()
print(a['a'])
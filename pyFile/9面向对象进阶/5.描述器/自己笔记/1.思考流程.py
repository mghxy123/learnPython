#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.思考流程.py
# Author: HuXianyong
# Date  : 2019/5/28 11:26

class A:
    def __init__(self):
        self.a1 = 'a1'
        print('A.init')

class B:
    x = A()
    def __init__(self):
        print('B.init')

print('-'*20)
print(B.x.a1)
print('='*20)
b = B()
print(b.x.a1)


#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.加载父类的初始化方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

class A:
    def __init__(self,a):
        self.a = a

class B(A):
    def __init__(self,b,c):
        super(B, self).__init__(1)
        self.b = b
        self.c = c

    def printv(self):
        print(self.c)
        print(self.b)
        print(self.a)
f= B(2,3)
print(f.__dict__)
print(f.__class__.__bases__)
f.printv()
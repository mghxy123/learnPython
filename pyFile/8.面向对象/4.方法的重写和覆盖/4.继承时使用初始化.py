#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.继承时使用初始化.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

class A:
    def __init__(self,a):
        self.a = a

class B(A):
    def __init__(self,b,c):
        self.b = b
        self.c = c

    def printv(self):
        print(self.c)
        print(self.b)
        print(self.a) #是否会报错？为什么？
        #会报错，应为我们在做B的时初始化的时候没有参数a
        #虽然类A中有参数a但是初始化的时候已经被B类所覆盖了
f= B(2,3)
print(f.__dict__)
print(f.__class__.__bases__)
f.printv()#这里报错了
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.类方法的覆盖行为.py
# Author: HuXianyong
# Date  : 2019/5/28 15:19

class A:
    @classmethod
    def foo(cls): #非数据描述器
        pass
    @staticmethod
    def bar(): #非数据描述器
        pass

    @property
    def z(self): #数据描述器
        return 5

    def getfoo(self): #非数据描述器
        return self.foo

    def __init__(self): #非数据描述器
        self.foo = 100
        self.bar = 200
        # self.z = 300 #property属性是这里无法修改属性

a = A()
print(a.__dict__)
print(A.__dict__)
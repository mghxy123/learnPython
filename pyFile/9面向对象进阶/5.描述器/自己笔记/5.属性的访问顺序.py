#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.属性的访问顺序.py
# Author: HuXianyong
# Date  : 2019/5/28 14:40

class A:
    def __init__(self):
        self.a1 = 'a1'
        self.b = 'b'
    def __get__(self, instance, owner):
        print('get______',self,instance,owner)
        print(self.__dict__)
        return self

class B:
    x = A()
    def __init__(self):
        self.x = 'b.z'

print('-'*20)
print(B.x)
print(B.x.a1)
print('='*20)
b = B()
print(b.x)
# print(b.x.a1) #AttributeError: 'str' object has no attribute 'a1'

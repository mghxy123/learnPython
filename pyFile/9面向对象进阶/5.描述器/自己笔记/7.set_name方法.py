#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.set_name方法.py
# Author: HuXianyong
# Date  : 2019/5/28 15:12

class A:
    def __init__(self):
        self.b = 'b'
    def __get__(self, instance, owner):
        print('get______',self,instance,owner)
        print(self.__dict__)
        return self
    def __set_name__(self, owner, name):
        print('set_name',owner,name,type(name))
        self.name = name
class B:
    x = A()
    y = A()
    def __init__(self):
        pass

b = B()
print(b.x)
b.x= 100
print()

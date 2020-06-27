#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 模式方法set和getattr的综合使用.py
# Author: HuXianyong
# Date  : 2019/5/28 10:37


class B:
    b= 200
class A(B):
    z = 100
    d = {}
    def __init__(self,x,y):
        self.x = x
        setattr(self,'y',y)
        self.__dict__['a']  = 5

    def __getattr__(self, item):
        print('~~~~~~~~~~~~~~',item)
        return self.d[item]
    def __setattr__(self, key, value):
        print(key,value)
        self.d[key] = value
    def __delattr__(self, item):
        print('can not del {}'.format(item))

a = A(3,4)
print(a.__dict__)
print(A.__dict__)
print(a.x,a.y)
print(a.x)
delattr(a,'x')
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 10.模式方法getattribute抛异常.py
# Author: HuXianyong
# Date  : 2019/5/28 11:05

class Base:
    n = 0
class Point(Base):
    z = 6
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        print(self.x,self.y)
    def __getattr__(self,item):
        return 'missing {}'.format(item)
    def __getattribute__(self, item):
        #raise AttributeError("Not Founf")
        # return self.__dict__[item]
        return object.__getattribute__(self,item)

p = Point(2,3)
print(p.__dict__)
print(p.x)
print(p.z)
print(p.n)
print(p.t)
print(Point.__dict__)
print(Point.z)
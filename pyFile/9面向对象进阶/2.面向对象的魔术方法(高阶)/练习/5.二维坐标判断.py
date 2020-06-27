#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.二维坐标判断.py
# Author: HuXianyong
# Date  : 2019/5/25 16:29

'''
    设计二维坐标Point,使其成为可hash类型,并比较2个坐标的实例是否相等.
'''

from collections.abc import Hashable

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __hash__(self):
        return hash((self.x,self.y))
    def __eq__(self, other):
        return self.x == self.x and self.y == self.y

p1 = Point(4,5)
p2 = Point(4,5)
print(1,hash(p1),hash(p2))

print(2,p1 is p2)
print(3,p1 == p2) #True使用__eq__
print(4,hex(id(p1)),hex(id(p2)))
print(5,set((p1,p2)))
print(6,isinstance(p1,Hashable))
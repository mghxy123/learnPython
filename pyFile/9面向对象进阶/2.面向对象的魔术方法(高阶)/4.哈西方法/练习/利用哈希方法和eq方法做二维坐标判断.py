#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 利用哈希方法和eq方法做二维坐标判断.py
# Author: HuXianyong
# Date  : 2019/5/25 16:51

from collections.abc import Hashable


'''
这里为什么要使用`from collections.abc import Hashable`而不是直接使用`from collections import Hashable`,
那是因为在3.8之后都将是这样使用了,不再支持`from collections import Hashable`这样使用,现在用的是可以用,但是会出红,看着难受,就这样使用吧. 
'''
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
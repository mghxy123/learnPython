#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.模式方法delattr.py
# Author: HuXianyong
# Date  : 2019/5/28 10:45

class Point:
    Z = 5
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __delattr__(self, item):
        print('Can not del {}'.format(item))

p = Point(2,3)
del p.x

p.z = 12

del p.z
del p.Z
print(Point.__dict__)
print(p.__dict__)
del Point.Z
print(Point.__dict__)
delattr(p,'x')
print(p.__dict__)

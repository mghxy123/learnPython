#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.为实例动态增加属性.py
# Author: HuXianyong
# Date  : 2019/5/26 16:18

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point({}, {})".format(self.x,self.y)

    def show(self):
        print(self.x,self.y)

p = Point(4,5)

print(p)
print(p.__dict__)
p.__dict__['y'] = 16
print(p.__dict__)
p.z = 10
print(p.__dict__)
print(dir(p)) #ordered list
print(p.__dir__()) #list
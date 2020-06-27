#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.使用内置函数增加属性.py
# Author: HuXianyong
# Date  : 2019/5/26 16:33

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return "Point({}, {})".format(self.x,self.y)

    def show(self):
        print(self.x,self.y)

p1 = Point(4,5)
p2 = Point(10,10)

print(repr(p1),repr(p2),sep='\n')
print(p1.__dict__)
setattr(p1,'y',100)
setattr(p1,'z',150)
print(getattr(p1,'__dict__'))

# 动态调用方法
if hasattr(p1,'show'):
    getattr(p1,'show')()

#动态的增加方法
#为类增加方法
if not hasattr(Point,'add'):
    setattr(Point,'add',lambda self,other:Point(self.x+other.x,self.y+other.y))

print(Point.add)
print(p1.add)
print(p1.add(p2))

#卫诗理增加方法,未绑定
if not hasattr(p1,'sub'):
    setattr(p1,'sub',lambda self,other:Point(self.x-other.x,self.y-other.y))

print(p1.sub(p1,p2))
print(p1.sub)

#add在水里面sub在谁里面?

print(p1.__dict__)
print(Point.__dict__)
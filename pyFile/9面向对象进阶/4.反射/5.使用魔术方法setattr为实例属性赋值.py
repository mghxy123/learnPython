#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.使用魔术方法setattr为实例属性赋值.py
# Author: HuXianyong
# Date  : 2019/5/28 10:28


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
    def __setattr__(self,key,value):
        print('setattr {}={}'.format(key,value))
        self.__dict__[key] = value #字典操作


p = Point(3,4)
print(p.x)
print(p.z)
print(p.n)
print(p.t)
print('外部x实例属性赋值')
p.x = 50
print(p.x)
print(p.__dict__)
p.__dict__['x'] = 60
print(p.__dict__)
print(p.x)
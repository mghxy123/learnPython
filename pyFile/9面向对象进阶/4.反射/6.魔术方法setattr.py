#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.魔术方法setattr.py
# Author: HuXianyong
# Date  : 2019/5/28 10:10

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
        print('setattr {}={}'.format(key,value)) #这里是制作了打印,但是却未作出赋值的操作,古尔,出了类属性和父类属性之外的实例属性都是没有的,
        #应为没有属性故而去找getattr方法就会返回missing的结果.

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
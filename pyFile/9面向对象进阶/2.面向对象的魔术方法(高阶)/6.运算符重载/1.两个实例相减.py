#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.两个实例相减.py
# Author: HuXianyong
# Date  : 2019/5/25 17:23

class A:
    def __init__(self,name,age=19):
        self.name = name
        self.age = age
    def __sub__(self, other):
        return self.age - other.age

    def __isub__(self, other): #如果没有定义__isub,则会去调用__sub__
        return A(self.name,self -other) #这里的self - other,意思就是两个实例相减,也就相当于t-j 然后去调用sub方法,得出结果
    def __repr__(self):
        return '{} {}'.format(self.name,self.age)
t = A('tom')
j = A('jerry',80)
print(t - j)

print(id(t))
t -= j
print(id(t))
print(t)
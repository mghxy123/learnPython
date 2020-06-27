#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 练习,两个向量的运算.py
# Author: HuXianyong
# Date  : 2019/5/25 17:45

'''
练习:
    完成Point类设计,实现判断点相等的方法,并完成向量的加法
    在直角坐标系里面,定义原点为响亮的起点.两个向量和与差分别等于这两个向量相应坐标的和与差,向量表示为(x,y)的形式.
如:
    A(x1,y1) B(x2,y2) 则 A+B = (x1+x2,y1+y2), A-B = (x1-x2,y1-y2)

'''

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return (self.x ==other.x and self.y ==other.y)

    def __sub__(self, other):
        return (self.x-other.x,self.y-other.y)

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)
    add = __add__
a = Point(1,2)
b = Point(2,6)

print(a.add(b))
print(a-b)
print(a+b)
print(a == b)
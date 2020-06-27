#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.利用isub完成坐标相加.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022


class AddPoint:

    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,o):
        return self.__class__(self.x+o.x,self.y+o.y)
    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        return (self.x + other.x, self.y + other.y)



a1 = AddPoint(4,5)
a2 = AddPoint(1,2)

print(a1-a2)
a1 -= a2
print(a1)
print(a1.add(a2))
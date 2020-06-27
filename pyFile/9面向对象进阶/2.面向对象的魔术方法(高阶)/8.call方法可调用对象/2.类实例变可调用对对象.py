#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.类实例变可调用对对象.py
# Author: HuXianyong
# Date  : 2019/5/25 21:33


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __call__(self, *args, **kwargs):
        return '<Point {}:{}>'.format(self.x,self.y)

p = Point(4,5)
print(p)
print(p())


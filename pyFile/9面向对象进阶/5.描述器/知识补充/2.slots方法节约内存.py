#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.slots方法节约内存.py
# Author: HuXianyong
# Date  : 2019/5/28 23:24

class A:
    x = 1
    # __slots__ = 'xy'.split()
    # __slots__ = ('y','z')
    __slots__ = 'y'

    def __init__(self):
        self.y = 5
        # self.z = 6

    def show(self):
        print(self.x,self.y)

a = A()
a.show()
# a.newx = 5 #AttributeError: 'A' object has no attribute 'newx' 这里不允许动态的添加属性了,,应为slots已经固定了

print('A',A.__dict__)
# print('object',a.__dict__) #使用了slots方法就使字典的属性固定了,不能再有多余的属性了
print('A',a.__slots__)

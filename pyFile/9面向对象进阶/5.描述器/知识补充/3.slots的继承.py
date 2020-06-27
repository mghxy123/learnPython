#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.slots的继承.py
# Author: HuXianyong
# Date  : 2019/5/28 23:37

class A:
    x = 1
    __slots__ = ('y','z') #元祖 slots影响的只是属性实例,不能印象类实例

    def __init__(self):
        self.y = 5

    def show(self):
        print(self.x,self.y)

a = A()
a.show()
print('A',A.__dict__)
print(a.__slots__)

class B(A):
    pass
print('B',B.__dict__)
print('B',B().__dict__)
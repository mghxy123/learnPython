#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.算法装饰器.py
# Author: HuXianyong
# Date  : 2019/5/25 20:04

from functools import total_ordering
@total_ordering
class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
    def __gt__(self, other):
        return self.age > other.age

tom = Person('tom',39)
jerry = Person('jerry',19)

print(tom > jerry)
print(tom < jerry)
print(tom <= jerry)
print(tom >= jerry)
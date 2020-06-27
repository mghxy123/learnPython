#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.直接运算符重载.py
# Author: HuXianyong
# Date  : 2019/5/25 20:15


class Person:
    def __init__(self,name ,age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age
    def __gt__(self, other):
        return self.age > other.age
    def __ge__(self, other):
        return self.age >= other.age

tom = Person('tom',39)
jerry = Person('jerry',19)

print(tom > jerry)
print(tom < jerry)
print(tom <= jerry)
print(tom >= jerry)
print(tom == jerry)
print(tom != jerry)
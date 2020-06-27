#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.相同的类实例.py
# Author: HuXianyong
# Date  : 2019/5/25 15:47


class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def __hash__(self):
        return 1

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return '<Person {} {}>'.format(self.name,self.age)

a = Person('tom')
b = Person('tom')
print(hash(a),hash(b))
print(a is b)
print(a == b)
print({a,b})

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.哈希方法.py
# Author: HuXianyong
# Date  : 2019/5/25 15:31


class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def __hash__(self):
        return 1

    def __repr__(self):
        return '<Person {} {}>'.format(self.name,self.age)

a = Person('tom')
b = Person('tom')
print(hash(a),hash(b))
print(a is b)
print(a == b)
print({a,b})
print({'tom','tom'})
print({('tom'),('tom,')})
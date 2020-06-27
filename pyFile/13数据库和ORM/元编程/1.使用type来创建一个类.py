#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Date  : 2019/6/29 14:57


class X(object):
    a = 100
    b = 'abc'


XClass = X

print(XClass)
print(XClass.__name__)
print(XClass.__bases__)
print(XClass.a)
print(XClass().a)
print(XClass.__dict__)

print('-'*50)
XClass = type('X', (object,), {'a':100, 'b': 'abc'})
print(XClass)
print(XClass.__dict__)
print(XClass.__name__)
print(XClass.__bases__)
print(XClass.mro())
# print(XClass.a)
# print(XClass().a)

print(type(XClass()))
print(type(XClass))


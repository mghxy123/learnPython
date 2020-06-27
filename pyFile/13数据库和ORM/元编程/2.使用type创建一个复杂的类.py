#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.使用type创建一个复杂的类.py
# Author: HuXianyong
# Date  : 2019/6/29 16:02

def __init__(self):
    self.x = 1000

def show(self):
    print(self.x)

NewClass = type('newclass', (), {'a':100, 'b':'this is string', 'show':show, '__init__':__init__})

print(NewClass)
print(NewClass.__name__)
print(NewClass.__dict__)
print(NewClass.mro())

NewClass().show()

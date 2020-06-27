#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 13.保护变量.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

'''
保护变量
    在变量名前使用一个下划线，称为保护变量
'''

class Person:
    def __init__(self,name,age=18):
        self.name = name
        self._age = age

tom = Person('Tom')
print(tom._age)
print(tom.__dict__)
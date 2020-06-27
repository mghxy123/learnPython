#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 14.私有方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017


class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def _getname(self):
        return self.name

    def __getage(self):
        return self.age

tom = Person('Tom')
print(tom._getname()) #没有改名
# print(tom.__getage()) #无此属性，改名了会报错的
print(tom.__dict__)
print(tom.__class__)#  tom.__class__等于Person
print(tom.__class__.__dict__)
print(Person.__dict__)
print(tom._Person__getage())#改名了
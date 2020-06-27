#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.实例变量和类变量.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016


class Person:
    age = 3
    def __init__(self,name):
        self.name = name

tom = Person('Tom')#实例化、初始化
jerry  = Person('Jerry')

print(tom.name,tom.age)
print(jerry.name,jerry.age)
print(Person.age)
Person.age=30
print(Person.age,tom.age,jerry.age)
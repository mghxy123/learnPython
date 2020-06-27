#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.类的多参.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def showage(self):
        print('{} is {}'.format(self.name,self.age))

tom = Person('Tom',20)
jerry = Person('Jerry',24)
print(tom.name,jerry.age)
jerry.age +=1
print(jerry.age)
jerry.showage()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 15.属性装饰器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age

    def age(self):
        return self.__age

    def set_age(self,age):
        self.__age = age

tom = Person('Tom')
print(tom.age())
tom.set_age(30)
print(tom.age())
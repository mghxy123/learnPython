#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.静态方法的覆盖.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

class Animal:
    @classmethod
    def class_method(cls):
        print('class_method_animal')

    @staticmethod
    def static_method():
        print('staitc_method_animol')

class Cat(Animal):
    @classmethod
    def class_method(cls):
        print('class_method_cat')

    @staticmethod
    def static_method():
        print('static_method_cat')

c = Cat()
c.class_method()
c.static_method()

print(Cat.__dict__)
print(Animal.__dict__)

Cat.static_method()
Animal.static_method()
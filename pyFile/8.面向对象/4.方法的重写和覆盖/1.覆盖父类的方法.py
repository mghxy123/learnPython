#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.覆盖.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

#覆盖父类的方法
class Animal:
    def shout(self):
        print('Animal shouts')

class Cat(Animal):
    #覆盖了父类方法：
    def shout(self):
        print('miao')


a = Animal()
a.shout()
c = Cat()
c.shout()

print(a.__dict__)
print(c.__dict__)
print(Animal.__dict__)
print(Cat.__dict__)

#覆盖自身的方法
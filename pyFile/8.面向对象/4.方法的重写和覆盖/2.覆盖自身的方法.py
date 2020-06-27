#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.覆盖自身的方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020

#覆盖自身的方法
class Animal:
    def shout(self):
        print('Animal shouts')

class Cat(Animal):
    #覆盖了父类方法：
    def shout(self):
        print('miao')
    #覆盖了自身的方法，显示调用了父类的方法
    def shout(self):
        print(super())
        print(super(Cat,self))
        print(super(self.__class__,self))

a = Animal()
a.shout()
c = Cat()
c.shout()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.继承1.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/20 0020


#不用继承
# class Animal:
#     def shout(self):
#         print('Animol shouts')
#
# a = Animal()
# a.shout()
#
# class Cat:
#     def shout(self):
#         print('cat shouts')
#
# c = Cat()
# c.shout()

# 使用继承
class Animal:
    def __init__(self,name):
        self._name = name
    def shout(self): #一个同吃的方法
        print('{} shouts'.format(self.__class__.__name__))

    @property
    def name(self):
        return self._name
a = Animal('monster')
a.shout()
class Cat(Animal):
    pass

cat = Cat('garfield')
cat.shout()
print(cat.name)

class Dog(Animal):
    pass

dog = Dog('ahuang')
dog.shout()
print(dog.name)
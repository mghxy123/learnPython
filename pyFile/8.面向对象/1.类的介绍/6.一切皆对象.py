#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.一切皆对象.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

class Person:
    age = 3
    def __init__(self,name):
        self.name = name

print('----class----')
print(Person.__class__,type(Person))
print(Person.__class__ == type(Person))#这两个是相等 的，结果为True，他们都是class类
print(Person.__name__)
print(Person.__dict__.items(),end='\n\n') #属性字典

tom = Person('Tom')
print('----instance tom----')
print(tom.__class__,type(tom))
print(tom.__dict__.items(),end='\n\n')

print("-----tom's class------")
print(tom.__class__.__name__)
# print(tom.__name__)#这里会报错，应为实例没有自己的__name__,
print(tom.__class__.__dict__.items(),end='\n\n')
#实例的类的字典等于类的字典
print(tom.__class__.__dict__)
print(Person.__dict__)
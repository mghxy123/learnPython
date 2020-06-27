#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 12.私有属性.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017

'''
私有属性：
    使用双下划线开头的属性名
'''
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.__age = age
    def growup(self,i=1):
        if 0 < self.__age < 150:
            self.__age +=i
        # print(self.__age)
    def getage(self):
        return self.__age
p1 = Person('Tom')
p1.growup(20) #正常范围内
# print(p1.__age) #不能访问
p1.__age = 28
print(p1.__age)
print(p1.getage())
#为什么年龄不一样？__age没有覆盖吗？
print(p1.__dict__) #通过字典可以看到了它们的本质
print('-'*60)
#直接修改私有变量
p1._Person__age = 15
print(p1.getage())
print(p1.__dict__)
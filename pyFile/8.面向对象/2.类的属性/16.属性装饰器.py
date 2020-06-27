#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 16.属性装饰器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/17 0017


# class Person:
#     def __init__(self,age=18):
#         self.__age = age
#     @property #设定公共属性
#     def age(self):
#         return self.__age
#
#     @age.setter #设置属性
#     def age(self,age):
#         self.__age = age
#
#     @age.getter #获取属性
#     def age(self):
#         return self.__age
#
#     @age.deleter #删除属性
#     def age(self):
#         del self.__age
# tom = Person()
# print(tom.age)
# tom.age = 30
# print(tom.age)
# del tom.age




# class Person:
#     def __init__(self,age=18):
#         self.__age = age
#
#     #设置属性
#     def setage(self,age):
#         self.__age = age
#
#     #获取属性
#     def getage(self):
#         return self.__age
#
#     #删除属性
#     def delage(self):
#         del self.__age
# tom = Person()
# print(tom.getage())
# tom.setage(30)
# print(tom.getage())


class Person:
    def __init__(self,age=18):
        self.__age = age

    age = property(lambda self:self.__age)

tom = Person()
print(tom.age)
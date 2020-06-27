#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 10.方法的调用.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

# class Person:
#     def method(self):
#         print("{}'s method".format(self))
#
#     @classmethod
#     def class_method(cls):
#         print('class = {0.__name__} ({0})'.format(cls))
#         cls.HEIGHT = 170
#     @staticmethod
#     def static_method():
#         print(Person.HEIGHT)
#
# print('----------类访问')
# # print(1,Person.method())#可以吗？ 不可以，应为这个没有实例化，并没有传入实例化的对象
# print(2,Person.class_method())#可以吗？ #可以应为类方法默认传入了cls
# print(3,Person.static_method()) #可以吗？可以，静态方法可以直接调用
# print(Person.__dict__)
# print()
# print()
# print('------实例访问')
# print('tom------')
# tom = Person()
# print(4,tom.method())#可以吗？可以应为这是实例访问，传入了实例，和上面的不一样
# print(5,tom.class_method())#可以吗？ 可以这个是类方法，实例和类都可以直接访问
# print(6,tom.static_method())#可以吗？ 可以，静态方法也是类和实例都可以直接访问的
# print()
# print()
# print('------实例访问')
# print('jerry------')
# jerry = Person()
# print(7,jerry.method())#可以吗？可以应为这是实例访问，传入了实例，和上面的不一样
# print(8,jerry.class_method())#可以吗？ 可以这个是类方法，实例和类都可以直接访问
# print(9,jerry.static_method())#可以吗？ 可以，静态方法也是类和实例都可以直接访问的


class Person:
    def method(self):
        print("{}'s method".format(self))


tom = Person()
tom.method()#可以吗 可以这个数类实例的调用，
# Person.method()#可以吗？ 不可以，这个是类直接调用， 没有实例的传入缺少第一参数
Person.method(tom)#可以吗 可以，这里传入了一个实例了
tom.__class__.method(tom)#可以吗 可以 这样调用相于Person.method(tom)这样的调用
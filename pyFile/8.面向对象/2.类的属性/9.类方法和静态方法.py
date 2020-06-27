#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 9.类方法和静态方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

#类中普通函数的方法
# class Person:
#     def normal_method(): #可以吗？ 这样是可以的没有语法上面的问题，执行也没问题，只是大家都默认不这么写
#         print('normal')
#
# # 如何调用?
# Person.normal_method() #可以吗？ 这个是可以的，应为只是直接调用函数
# # Person().normal_method() #可以吗？ 这个不可以，应为这个是实例化，实例化之后类里面的方法需要接受一个类的实例化对象，然而这里并没有传入，self，因此会报错
# print(Person.__dict__)


# # 静态方法
# class Person:
#     @staticmethod
#     def class_method():
#         print('this is staticMethod')
# Person.class_method()
# Person().class_method()

#静态方法

class Person:
    @classmethod
    def class_method(cls): #cls 是什么？
        print('this is class method')
        print('class = {0.__name__}({0})'.format(cls))
        cls.HEIGHT = 170
    @staticmethod
    def static_method():
        print('this is staticMethod')
Person.class_method()
print(Person.__dict__)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.运算符重载.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

#__add__这个叫做运算符重载魔术方法

# class A:
#     def __init__(self,age=10):
#         self.age = age
# a1 = A()
# a2 = A()
# print(a1-a2)
#
# #这样会报错,但是我们要是用减法运算就只有去定义减法了
###########################################################
# class A:
#     def __init__(self,age=10):
#         self.age = age
#     def __sub__(self, other):
#         return self.age -other.age
# a1 = A(9)
# a2 = A()
# print(a1-a2)
# print(a1.__sub__(a2))
# print(a2.__sub__(a1))
###########################################################
#就地加减 a += 1
# class A:
#     def __init__(self,age=10):
#         self.age = age
#     def __sub__(self, other):
#         return self.age -other.age
#
#     def __isub__(self, other):
#         return A(self.age - other.age)
# a1 = A(12)
# a2 = A()
# print(id(a1))
#
# a1 -= a2
# print(id(a1))

#这里的isub使用的是inplace 就是覆盖了,所以id发生了改变

# ###########################################################
# #就地加减 a += 1
# class A:
#     def __init__(self,age=10):
#         self.age = age
#     def __sub__(self, other):
#         return self.age -other.age
#
#     def __isub__(self, other):
#         # return A(self.age - other.age)
#          self.age -= other.age
#          return self
# a1 = A(12)
# a2 = A()
# print(id(a1))
#
# a1 -= a2
# print(id(a1))

#这样id就不会改变了

###########################################################
#
class A:
    def __init__(self,age=10):
        self.age = age
    def __sub__(self, other):
        return self.age -other.age

    def __isub__(self, other):
        # return A(self.age - other.age)
        #  self.age -= other.age
         return A(self -other)
a1 = A(12)
a2 = A()
print(id(a1))

a1 -= a2
print(id(a1))

# 有isub就先实用isub,没有就说那个sub
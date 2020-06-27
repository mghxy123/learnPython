#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.new方法与init方法.py
# Author: HuXianyong
# Date  : 2019/5/25 14:10
# ################################################
# #1
# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         print(args)
#         print(kwargs)
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('this is init')
#         print(self.name)
#         print(self.age)
# a = A('jerry',age = 19)
# print(a)

# ################################################
# #2
# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         print(args)
#         print(kwargs)
#         return 200
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('this is init')
#         print(self.name)
#         print(self.age)
# a = A('jerry',age = 19)
# print(a)
# ################################################
# #3
# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         print(args)
#         print(kwargs)
#         # return 200
#         return super().__new__(cls)
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print('this is init')
#         print(self.name)
#         print(self.age)
# a = A('jerry',age = 19)
# print(a)


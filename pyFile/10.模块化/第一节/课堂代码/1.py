#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.py
# Author: HuXianyong
# Date  : 2019/5/29 16:14

# import os # import后面只能跟模块,不能是类属性,和方法
#
# #这三者在这里都是一样的
# print(dir())
# print(sorted(locals().keys()))
# print(sorted(globals().keys()))

# def a():
#     import os #标识符受作用域的影响
#     print(dir())
#
# a()
# print()
# print(dir())


from os.path import exists
print(exists)

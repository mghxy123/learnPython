#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.Python2和3的类比较.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021

# 以下代码在python2中运行

#古典类（旧式类）
class A:pass

#新式类
class B(object):pass

print(dir(A))
print(dir(B))
print(A.__bases__)
print(B.__bases__)

#古典类
a = A()
print(a.__class__)
print(type(a)) #

#新式类
b =B()
print(b.__class__)
print(type(b))
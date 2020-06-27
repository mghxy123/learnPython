#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.运算符重载中的反向方法.py
# Author: HuXianyong
# Date  : 2019/5/28 23:52

class A:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        print(self,'add')
        return self.x+other.x
    def __iadd__(self, other):
        print(self,'iadd')
        return A(self.x+other.x)
    def __radd__(self, other):
        print(self,'radd')
        return self.x +other.x
class B: #为实现__add__
    def __init__(self,x):
        self.x = x

a = A(4)
b = B(10)

print(a+b)
print(b+a)
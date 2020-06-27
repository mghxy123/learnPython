#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.反向运算符.py
# Author: HuXianyong
# Date  : 2019/5/29 0:21


class A:
    def __init__(self,x):
        self.x = x

    def __repr__(self):
        return "<A {}>".format(self.x)

    def __add__(self, other):
        print('add ~~~~~~~~~~~')
        if hasattr(other,'x'):
            return self.x +other.x
        else:
            try:
                x = int(other)
            except:
                x=0
            return self.x+x
    def __iadd__(self, other):
        print('iadd ~~~~~~~~~~~')
        return A(self.x+other.x)

    def __radd__(self, other):
        print('radd ~~~~~~~~~~~')
        return self+other
a1 = A(4)
a2 = A(5)
print(a1+a2) #add int 9 a1.__add__(a2)
print(a2+a1)
# print(a2+1) #报错 调用的还是add
print(2+a1) #报错,这里调的是radd 等价于1.__radd__(a1) int.a1__radd__(1,a1)

class B:
    def __init__(self,x):
        self.x = x
    def __add__(self, other): #如果b1存在运算法重载,且它是在第一位,就按照他的运算方法来
        return NotImplemented #这里是正常输出10
    #     return 123
b1 = B(6)
print(a1+b1) #可以执行,a1.__add__(b1)
print(b1+a1) #可以执行,b1.__radd__(a1)

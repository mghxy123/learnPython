#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.bool与len.py
# Author: HuXianyong
# Date  : 2019/5/25 16:54

class A:
    def __bool__(self):
        return False
print('bool A',bool(A))
print('bool A()',bool(A()))

class B:pass
print('bool B',bool(B))
print('bool B()',bool(B()))

class C:
    def __len__(self):
        return 0
print('bool C',bool(C))
print('bool C()',bool(C()))

class D:
    def __len__(self):
        return 1
print('bool D',bool(D))
print('bool D()',bool(D()))

class E(A):
    def __len__(self):
        return 0
print('bool E',bool(E))
print('bool E()',bool(E()))

#类实例在算布尔值的时候,有bool先算bool,没有bool就看len
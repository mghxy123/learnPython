#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Date  : 2019/5/24 23:12


class A:
    pass
class B(A):pass

class C(B):pass

c = C()
print(C.__bases__)
print(C.__mro__)
print(C.__dir__)
print(dir())
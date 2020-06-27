#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.self的说明.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

class MyClass:
    def __init__(self):
        print(1,'self in init = {}'.format(id(self)))
    def showself(self):
        print(2,'self in showself() = {}'.format(id(self)))

c  = MyClass() #会调用init
print(3,'c = {}'.format(id(c)))
print('-'*30)
c.showself()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.类的实例化.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

class Person:
    '''this is human class'''
    def __init__(self):
        print('init')
    def name(self):
        pass

print(1,Person) #不会调用init
print(2,Person()) #调用init
tom = Person() # 调用init
jerry = Person()
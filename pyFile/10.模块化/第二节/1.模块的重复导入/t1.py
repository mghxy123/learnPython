#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : t1.py
# Author: HuXianyong
# Date  : 2019/5/30 19:32

print('This is t1 module')

class A:
    def showmodule(self):
        print(1,self.__module__,self)
        print(2,self.__dict__)
        print(3,self.__class__.__dict__)
        print(4,self.__class__.__name__)
a = A()
a.showmodule()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.简单的类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016



class MyClass:
    '''A example class'''
    x='abc'#类的属性
    def foo(self):#类属性foo，也叫作类的方法
        return 'MyClass'

print(MyClass.x)
print(MyClass.foo)
print(MyClass.__doc__)
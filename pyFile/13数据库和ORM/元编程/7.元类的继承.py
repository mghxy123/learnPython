#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.元类的继承.py
# Author: HuXianyong
# Date  : 2019/6/30 23:28



class MetaTest(type):
    def __new__(cls, name, obj, dict:dict):
        print('cls',cls)
        print('name',name)
        print(obj)
        print(dict)
        return super().__new__(cls, name, obj, dict)

class A(tuple,metaclass=MetaTest):
    id = 1000

    def __init__(self):
        print('A.init~~~~~~~~~~')

# 第二种 B继承自A后,依然是从ModeMeta的类型
class B(A):
    def __init__(self):
        print('B.init~~~~~~~~~')


# 第三种 元类可以使用下面就可以的方式创建新的类
C = MetaTest('C',(), {})


# D E 是type的实例
class D:pass # D = type('D', (), {})
E = type('E', (), {})

class F(MetaTest):pass #F是什么


print('-'*30)
print(type(A),A.__bases__)
print(type(B),B.__bases__)
print(type(C),C.__bases__)
print()

print(type(D),D.__bases__)
print(type(E),E.__bases__)

print()
print(type(F),F.__bases__)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.元类参数的作用2.py
# Author: HuXianyong
# Date  : 2019/6/29 17:26
class MetaTest(type):
    def __new__(cls, *args, **kwargs):
        print('cls',cls)
        print('args',args)
        print('kwargs',kwargs)
        return super().__new__(cls,*args,**kwargs)

class A(tuple, metaclass=MetaTest):
    pass

print(type(A))
print(A.__name__)


class MetaTest(type):
    def __new__(cls, *args, **kwargs):
        print('cls',cls)
        print('args',args)
        print('kwargs',kwargs)
        return super().__new__(cls,*args,**kwargs)

class A(tuple,metaclass=MetaTest):
    pass

print(type(A))
print(A.__name__)

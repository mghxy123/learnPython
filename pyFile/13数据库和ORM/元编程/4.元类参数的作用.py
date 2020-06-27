#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.元类参数的作用.py
# Author: HuXianyong
# Date  : 2019/6/29 17:20



class MetaTest(type):
    def __new__(cls, *args, **kwargs):
        print('cls',cls)
        print('args',args)
        print('kwargs',kwargs)


class A(metaclass=MetaTest):
    pass

print(type(A))
print(A.__name__)
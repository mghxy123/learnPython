#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.元类参数解析.py
# Author: HuXianyong
# Date  : 2019/6/29 17:35


class MetaTest(type):
    def __new__(cls, name, obj, keyword:dict):
        print('cls',cls)
        print('name',name)
        print(obj)
        print(keyword)
        return super().__new__(cls, name, obj, keyword)

class A(tuple,metaclass=MetaTest):
    pass

print(type(A))
print(A.__name__)


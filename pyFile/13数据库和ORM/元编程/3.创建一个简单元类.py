#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Date  : 2019/6/29 16:59



class MetaTest(type):
    def __new__(cls, *args, **kwargs):
        print('cls',cls)
        print('args',args)
        print('kwargs',kwargs)


class A(metaclass=MetaTest):
    pass


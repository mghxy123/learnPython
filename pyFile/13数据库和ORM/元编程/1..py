#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1..py
# Author: HuXianyong
# Date  : 2019/6/28 10:08


# 元类指定使用metaclass 来创建元类
class Meta(type):
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        print(kwargs)
        print()

print('-'*39)

class A(Meta):  #这叫继承
    pass

print('~'*30)
class B(metaclass=Meta): #这叫做,修改元类
    pass

# class C(B): # B继承时, 元类也一样继承下来
#     pass
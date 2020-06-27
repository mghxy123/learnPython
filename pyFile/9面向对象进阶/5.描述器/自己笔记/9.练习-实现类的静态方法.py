#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 9.练习-实现类的静态方法.py
# Author: HuXianyong
# Date  : 2019/5/28 15:40

from functools import partial

class ClassMethod:
    def __init__(self,fn):
        self._fn = fn
    def __get__(self, instance, owner):
        ret = partial(self._fn,owner)
        return ret

class StaticMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self,instance,owner)
        return self.fn
#这里的实现方法是使用了描述器,通过描述器把实例属性返回回去,就不用使用第一参数为self了
class A:
    @StaticMethod #stmd = staticmethod(stmd)
    def stmd(x,y):
        print('sssssss',x,y)
    @ClassMethod
    def clmd(cls):
        print('classmethod {}'.format(cls.__name__))
print(A.__dict__)
A.stmd(3,4)
A.clmd()
A().clmd()
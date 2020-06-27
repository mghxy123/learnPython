#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.练习-类方法.py
# Author: HuXianyong
# Date  : 2019/5/27 14:36

from functools import wraps,update_wrapper,partial#偏函数三参变两参

class ClassMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self,instance,owner)
        fn = partial(self.fn,owner)
        # wraps(self.fn)(fn)
        update_wrapper(fn,self.fn)
        return fn

class StaticMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self,instance,owner)
        return self.fn

class A:
    @StaticMethod #stmd = staticmethod(stmd)
    def stmd(x,y):
        print('sssssss',x,y)
    @ClassMethod # clmd = classmethod(clmd)
    def clmd(cls,x,y):
        '''clmd classmethod'''
        print(cls.__name__,x,y)
a=A()
a.stmd(3,4)
a.clmd(3,4)
print(A.clmd.__doc__)
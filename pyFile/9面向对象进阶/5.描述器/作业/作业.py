#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 作业.py
# Author: HuXianyong
# Date  : 2019/5/28 22:51

# 实现property装饰器,类名为Property。
# 基本结构如下：

# class Property:
#     def __init__(self):
#         pass
#     def __get__(self, instance, owner):
#         pass
#     def __set__(self, instance, value):
#         pass
# class A:
#     def __init__(self,x):
#         self._x = x
#
#     @Property
#     def x(self):
#         return self._x
#
#     @x.setter
#     def x(self,value):
#         self._x = value


###############################################################


class Property:
    def __init__(self,fget,fset=None):
        self.fget = fget# 这是实例的属性保持一个函数,不会改变的
        self.fset = fset #fset是经过set处理之后的fn,没经过的就是fget
    def __get__(self, instance, owner):
        if instance:#如果不适用实例访问就直接抛出异常
            return self.fget(instance) #x(self:A)
        raise AttributeError()
    def __set__(self, instance, value):

        if self.fset is None:
            raise AttributeError('can not set attribute')
    def setter(self,fn):
        self.fset = fn
        return self
class A:
    def __init__(self,x):
        self._x = x

    @Property # x = Property(x) 就转变成了x是Property的实例
    def x(self):
        return self._x

    @Property
    def y(self):
        return 1000

    @x.setter # x(属主属性) = x(必须是描述器本身).setter(x)  x = Property(x).setter(x) = Property(fget).setter(fset) #现在被装饰的x是fset
    def x(self,value):
        self._x = value

a = A(10)
print(a.x)
print(a.y)
a.x= 1000
print(a.x)
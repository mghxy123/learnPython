#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.set_name.py
# Author: HuXianyong
# Date  : 2019/5/27 14:12

class A:
    def __init__(self):
        # self.a = 'a'
        self.b = 'b'
    def __get__(self, instance, owner):# instance是owner的实例
        #由于我们第一次访问是直接类访问,所以是None ower是属主类B
        #第二次是是实例b去访问,所以instance就不是None了 ower是属主类B
        print('get______',self,instance,owner)
        print(self.__dict__)
        return self
    def __set_name__(self, owner, name):
        print(owner,name,type(name))
        self.name = name
    # def __set__(self, instance, value):
    #     print('set------',self,instance,value)
    #     # instance.__dict__['x'] = value
    #     # self.data = value
    #     # setattr(instance,'x',value)
    #     # if instance:
    #     #     raise AttributeError('cat\'t set attribute') #如果这样设置了,就和property属性装饰器时候一样的
class B: #B是A的属主 也就是get方法中的  A类叫做描述器
    x = A() #类属性可以,描述器和属主类的属性相关,和属主实例无关,所以下面self.y不会走描述器get方法.
    y = A()
    def __init__(self):
        # self.x = 'b.z' #
        pass

b = B()
print(b.x)
b.x= 100
print()

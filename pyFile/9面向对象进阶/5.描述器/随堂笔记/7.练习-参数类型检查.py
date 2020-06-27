#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.练习-参数类型检查.py
# Author: HuXianyong
# Date  : 2019/5/27 16:07

class TypeCheck:
    def __init__(self,typ):
        self.type = typ

    def __get__(self, instance, owner):
        print('get~~~~~~~~~~~~~~~~~')
        if instance:
            return instance.__dict__[self.name]
        else:
            return self
    def __set_name__(self, owner, name):
        print('set_name~~~~~~~~~~~~~~~')
        self.name = name

    def __set__(self, instance, value):
        print('set~~~~~~~~~~~',self,instance,value)
        if instance:
            if isinstance(value,self.type):
                instance.__dict__[self.name] = value
            else:
                raise TypeError(self.name + '========')

class Person:
    name = TypeCheck(str)
    age = TypeCheck(int)

    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

t = Person('tom',30)

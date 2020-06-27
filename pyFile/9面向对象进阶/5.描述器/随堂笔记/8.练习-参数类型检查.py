#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.练习-参数类型检查.py
# Author: HuXianyong
# Date  : 2019/5/27 16:13
import inspect

class TypeCheck:
    def __init__(self,name,typ):
        self.type = typ
        self.name = name

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.name]
        else:
            return self

    def __set__(self, instance, value):
        print('set----',self,instance,value)
        if instance:
            if instance(value,self.type):
                instance.__dict__[self.name] = value
            else:
                raise TypeError(self.name + '========')

def datainject(cls):
    sig = inspect.signature(cls)
    params = sig.parameters
    for name,param in params.items():
        if param.annotation != param.empty:
            setattr(cls,name,TypeCheck(name,param.annotation))
    return cls
@datainject
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

t = Person('tom',30)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 9.类属性注入.py
# Author: HuXianyong
# Date  : 2019/5/27 16:41

import inspect

class TypeCheck:
    def __init__(self,typ):
        self.type = typ

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.name]
        else:
            return self
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if instance:
            if instance(value,self.type):
                instance.__dict__[self.name] = value
            else:
                raise TypeError(self.name + '========')
class DataInject:
    def __init__(self,cls):
        self.cls = cls
        sig = inspect.signature(cls)
        params = sig.parameters
        for name, param in params.items():
            print(name,param.name,param.name,param.empty)
            if param.annotation != param.empty:
                setattr(cls, name, TypeCheck(name, param.annotation))
    def __call__(self, *args, **kwargs):
        return self.cls(*args,**kwargs)

@DataInject
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age = age

t = Person('tom',30)
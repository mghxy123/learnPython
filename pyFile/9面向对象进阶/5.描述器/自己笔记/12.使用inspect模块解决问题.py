#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 12.使用inspect模块解决问题.py
# Author: HuXianyong
# Date  : 2019/5/28 17:13

import inspect

class TypeCheck:
    def __init__(self,name,typ):
        self.name = name
        self.typ = typ
    def __get__(self, instance, owner):
        print('get~~~~~~~~~~')
        if instance:
            return instance.__dict__[self.name] #获取属性

    def __set__(self, instance, value):
        print('set~~~~~~~~~~~~~~~~')
        if not isinstance(value,self.typ):
            raise TypeError(value)
        instance.__dict__[self.name] = value #获取到了Person类的属性,然后再次的存入到这属主属性里面去,存入属性

def typeinject(cls):
    sig =inspect.signature(cls)
    params = sig.parameters
    print(sig,params)
    for name,param in params.items():
        print(name,param)
        if param.annotation != param.empty: #注入属性
            setattr(cls,name,TypeCheck(name,param.annotation))
    return cls
@typeinject #Person = typeinject(Person)
class Person:
    # name = TypeCheck('name',str) #硬编码
    # age = TypeCheck('age',int) #不优雅
    def __init__(self,name:str,age:int):
        self.name = name
        self.age  = age
p = Person('tom',10)
print(p.__dict__)
print(p.age)

# sig = inspect.signature(Person)
# params = sig.parameters
#
# print(sig)
# print(params)

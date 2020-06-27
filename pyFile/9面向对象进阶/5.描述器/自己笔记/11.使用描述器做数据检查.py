#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 11.使用描述器做数据检查.py
# Author: HuXianyong
# Date  : 2019/5/28 16:51

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
class Person:
    name = TypeCheck('name',str) #硬编码
    age = TypeCheck('age',int) #不优雅
    def __init__(self,name:str,age:int):
        self.name = name
        self.age  = age
p = Person('tom',10)
print(p.__dict__)
print(p.age)
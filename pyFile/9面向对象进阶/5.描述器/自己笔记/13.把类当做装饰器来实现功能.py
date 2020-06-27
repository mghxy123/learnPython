#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 13.把类当做装饰器来实现功能.py
# Author: HuXianyong
# Date  : 2019/5/28 17:31

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

class TypeInject:
    def __init__(self,cls):
        self.cls = cls
        sig =inspect.signature(self.cls)
        params = sig.parameters
        print(sig,params)
        for name,param in params.items():
            print(name,param)
            if param.annotation != param.empty: #注入属性
                setattr(self.cls,name,TypeCheck(name,param.annotation))
    def __call__(self, *args, **kwargs):
        return self.cls( *args, **kwargs) #新构建一个新的Person对象
@TypeInject #Person = typeinject(Person)
class Person:
    def __init__(self,name:str,age:int):
        self.name = name
        self.age  = age
p = Person('tom',10)
p2 = Person('jerry',20)
print(p.__dict__)
print(p.age)
print(p2.__dict__)
print(p2.age)

#查找顺序 1.实例属性查找,
#         2.然后base类上面的set通过set把set获取到的属主属性注入到属主属性之内,
#         3.到base类上的get把找到的类返回过来,交给属主属性.
#         4.属主获得属性
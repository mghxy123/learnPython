#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.查看函数类型注解.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/25 0025


# import inspect #导入检查的模块
# from inspect import Parameter
#
# def check(fn):
#     def wrapper(*args,**kwargs):
#         sig = inspect.signature(add1)
#         parameter = sig.parameters
#         # print(parameter) #OrderedDict([('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
#         for k,v in parameter.items():
#             print(k,v)
#             print(type(v))
#             print('*'*30)
#         ret =  fn(*args,**kwargs)
#         return ret
#     return wrapper
# def add1(x:int,y:int=6) -> int: #定义函数add1的返回值的类型注释为int
#     return x + y
#
# print(add1(2,4))
# print(check(add1)(4,5))




############################################################################################
import inspect #导入检查的模块
from inspect import Parameter

def check(fn):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(add1)
        parameter = sig.parameters
        # print(parameter) #OrderedDict([('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
        for k,v in parameter.items():
            v:Parameter = v
            print(v.name,k,'~~~~~~~name')
            print(v.default)
            print(v.annotation)
            print(v.kind)
            print('*'*30)
        ret =  fn(*args,**kwargs)
        return ret
    return wrapper
def add1(x:int,y:int=6) -> int: #定义函数add1的返回值的类型注释为int
    return x + y

print(check(add1)(4,5))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.函数的类型注解.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/25 0025


# def add(x,y:int,z="zxc",*args,m,n=2,**kwargs):
#     pass
#
# sig = inspect.signature(add)
# parameter = sig.parameters
# # print(parameter) #OrderedDict([('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
# for k, v in parameter.items():
#     v: Parameter = v
#     print(v.name, k, '~~~~~~~name')
#     print(v.default)
#     print(v.annotation)
#     print(v.kind)
#     print('*' * 30)


import inspect
from inspect import Parameter

def check(fn):
    def wrapper(*args,**kwargs):
        sig = inspect.signature(fn)
        parameter = sig.parameters
        # print(parameter) #OrderedDict([('args', <Parameter "*args">), ('kwargs', <Parameter "**kwargs">)])
        # for k,v in parameter.items():
        #     v:Parameter = v
        #     print(v.name,k,'~~~~~~~name')
        #     print(v.default)
        #     print(v.annotation)
        #     print(v.kind)
        #     print('*'*30)

        for x, (k,v) in zip(args,parameter.items()):
            if v.annotation != inspect._empty and not isinstance(x,v.annotation):
                raise TypeError('Wrong param = {} {} {}'.format(k,x,type(x)))
        for k,v in kwargs.items():
            if parameter[k].annotation != parameter[k].empty and not isinstance(v,parameter[k].annotation):
                raise TypeError('Wrong parame = {} {}'.format(k,v))
        ret =  fn(*args,**kwargs)
        return ret
    return wrapper

@check #相当于add = check(add)即 wrapper = check(add),此add已不是之前的add了,同名而已
def add(x:int,y:int=6) -> int: #定义函数add1的返回值的类型注释为int
    return x + y

print(add(4,5))
print(add(x=4,y=5))
print(add(4,y=5))
# print(add(4,'5')) #如果不按照定义的类型传入的话就会抛出我们自己报出的错误




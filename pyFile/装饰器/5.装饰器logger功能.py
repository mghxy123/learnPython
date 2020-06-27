#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.装饰器logger功能.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/23 0023


'''
需求，给一个求和函数增加输出功能

'''


def decorate(func):
    def inner(*args,**kwargs):
        print('before')
        result = func(*args,**kwargs)
        print('end ',result)
        return result
    return inner

@decorate
def add(a,b):
    return a+b

print(add(6,7))
print(add(6,b=17))
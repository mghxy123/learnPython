#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3偏函数与柯里化.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/25 0025

'''
偏函数与柯里化都是把多参函数,减为少参函数

'''

def add(x,y):
    return x+y

'''
这样的一个两参函数,我们的柯里化与偏函数都能把他变为一参函数
'''

#柯里化
def func(fn,x):
    def wrapper(y):
        result = fn(x,y)
        return result
    return wrapper
newadd = func(add,4)
print(newadd(5))

#偏函数
from functools import partial

def add(x,y):
    return x+y

newadd = partial(add,4)
print(newadd(5))

#经过上面例子可以看出这样个都可以吧两参函数变成一参函数
#或者是吧多参函数变成少参函数
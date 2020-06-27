#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.偏函数.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/25 0025

from functools import partial
import inspect

def add(x,y):
    return x+y

newfunc = partial(add,4)#偏函数把,两个参数变成一个参数,和柯里化一样
print(newfunc)
print(inspect.signature(newfunc))
print(newfunc(5)) #这个偏函数,和下面函数的执行结果是一个样的
print(add(4,5))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.上下文处理装饰器.py
# Author: HuXianyong
# Date  : 2019/5/26 14:57

from contextlib import contextmanager

@contextmanager
def foo():
    print('enter') #yield之上相当于__enter__()
    try:
        yield 'yield'#yield 5 yield的值只能有一个,作为__enter__方法的返回值
    finally:
        print('exit') #yield之下相当于__exit__()

with foo() as f:
    raise Exception()
    print(f)
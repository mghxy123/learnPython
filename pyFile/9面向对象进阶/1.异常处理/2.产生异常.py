#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.异常处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021

def foo():
    print('before')
    print(1/0)
    print('after')

foo()


'''
输出结果为:
before
Traceback (most recent call last):
     print(1/0)
ZeroDivisionError: division by zero

'''

# def bar():
#     print('before')
#     raise Exception('my exception') #raise 主动抛出异常
#     print('after')
#
# bar()

'''
输出结果为:
before
Traceback (most recent call last):
    raise Exception('my exception') #raise 主动抛出异常
Exception: my exception
'''
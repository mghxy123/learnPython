#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 类装饰器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/15 0015


def fn(fn):
    def inner():
        # print('f2222')
        fn.NAME = 'test'
        result = fn
        # print(fn.NAME)
        return result
    # print(inner.NAME)
    return inner
@fn
class Person:
    pass

a = Person()
print(a.NAME)

# def test(fn):
#     fn.name = 'hello'
#
# a = test(Person)
# print(a.__dict__)
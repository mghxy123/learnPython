#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : t1.py
# Author: HuXianyong
# Date  : 2019/8/3 17:43

# def tt(p):
#     def decorate(fn):
#         def inner(x=1,y=2):
#             # print(x,y)
#             ret = x+y+p
#             return ret
#         return inner
#     return decorate
#
# @tt(4) #add = fn(add) = fn(inner)
# def add(x,y):
#     return x+y
#     # print(x,y)
#
# print(add(10,20))


# def decorate(a):
#     def warrpe(fn):
#         def inner(x,y):
#             return x+y+a
#         return inner
#     return warrpe
#
# @decorate(2)
# def add(x,y):
#     return x+y
#
# print(add(4,5))


l1 = [1,2,3,4,5,6,7,8]
# l2 = map(lambda x:x*x,l1)
#
#
#
# l4 = filter(lambda x:x*x>10,l1)

print(reduce(lambda x,y:x+y,l1)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.装饰器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/22 0022

'''
装饰器，可以给一个已有功能的函数添加新的功能，
主要的作用是，给一个函数封装好了的函数添加新的功能，而不会改变函数的本身

'''
# #例：我们想给两个数相加的函数add添加显示的功能，我们就可以使用装饰器来完成
#
# def add(x, y):
#     return x+ y
#
# print(add(2,3))
# 5
#这个是函数的主体功能，我们需要添加一些小功能

# #我们正常的添加是：
# def add(x, y):
#     print('这是一个相加函数{} {}'.format(x,y))
#     return x+ y
# print(add(2,3))
#
# '''
# 这是一个相加函数2 3
# 5
# '''

#但是大部分时候我们不能对原有函数进行修改，唯一的办法就是给原有函数加上装饰器，增加新的功能
def add(x,y):
    return x+y

def logger(fn,x,y):
    print('这是一个相加函数{} {}'.format(x,y))
    result = fn(x,y)
    return result

print(logger(add,2,3))

#这样即给原函数加上了新功能有不改变原有函数，这样的功能就叫装饰器










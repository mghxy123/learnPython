#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.装饰器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/22 0022


'''
在原有函数的功能上添加更多的功能


'''

# def add(x,y):
#     return x+y
#
# def logger(fn,*args):#这里的*args是可变的形参
#     print('这是一个求和函数{}'.format(args))
#     #这里使用的是组包，解包的操作，把一个数组传进去
#
#     result = fn(*args)#这里的*args是实参参数的解构
#     print('求和函数结束')
#     return result
#
# print(logger(add,6,7))
######################################***********************
# #与**args
# def add(x,y):
#     return x+y
#
# def logger(fn,*args,**kwargs):#这里的*args是可变的形参
#     print('这是一个求和函数{} | {}'.format(args,kwargs))
#     #这里使用的是组包，解包的操作，把一个数组传进去
#
#     result = fn(*args,**kwargs)#这里的*args是实参参数的解构
#     print('求和函数结束')
#     return result
#
# print(logger(add,6,7))
# print(logger(add,x=6,y=7))
# print(logger(add,6,y=17))
##########################################################################

#柯里化：指的是将原本要接受两个参数的函数变成接受一个参数函数的过程，新的函数返回一个原有的第二参数为参数的函数
#函数柯里化，我们把logger(x,y)函数变成logger(x)(y)这样的过程叫做函数柯里化
def add(x,y):
    return x+y
def logger(fn):
    def inner(*args,**kwargs):
        print('这是一个求和函数{} | {}'.format(args, kwargs))
        result = fn(*args,**kwargs)#这里的*args是实参参数的解构
        print('求和函数结束')
        return result
    return inner

aa = logger(add)
print(aa(6,7))
'''
#这里涉及到了是否覆盖的问题，按理说
add会把函数add给覆盖了，但是实际上却没有覆盖，为什么呢？
应为当我们定义add=logger（add）的时候，我们的函数fn会把内存地址指向add的内存地址，而不是指向add这个变量，
应为函数名也是指向函数的内存地址的，所以这里的add相加函数已经由fn指向了函数的内存地址，所以才不会被覆盖
'''


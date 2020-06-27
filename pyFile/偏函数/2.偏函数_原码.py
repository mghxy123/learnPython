#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.偏函数_原码.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/25 0025

# from functools import partial
#
# def add(x,y,z):
#     return x+y+z
#
# newfunc = partial(add, 3)
# print(newfunc(4,5))

#偏函数
#定义是:通过偏函数把参数通过把其中的一个参数变成默认值,减少一个固定参数的传入,
#从而把函数简单化

##############################################################################
#1.
# def partial1(func,*args,**keywords):
#     def newfunc(*fargs,**fkeywords):
#         newkeywords = keywords.copy()
#         newkeywords.update(fkeywords)
#         print(newkeywords)
#         print(args,fargs)
#         return func(*args,*fargs,**newkeywords)
#     newfunc.func = func
#     newfunc.args = args
#     newfunc.keywords = keywords
#     return newfunc
#
# def add(x,y,z):
#     return x+y+z
# # newfunc = partial1(add, 3)
# # print(newfunc(y=5,z=6)) #newfunc = newfunc((3,) ,(),{'y': 5, 'z': 6})
#
# newfunc = partial1(add, y=3) #newfunc = newfunc((4,5),{y:3})
# print(newfunc(x=4,z=5)) #newfunc = newfunc((), (),{x:4,y:3,z:5})
# print('*'*50)
# print(newfunc(4,z=6)) #newfunc = newfunc((),(4,),{y:3,z:6})


#柯里化
# def parrial(fn,x):
#     def newfunc(y,z):
#         return fn(x,y,z)
#     return newfunc
#
# def cc(a,b,c):
#     return a+b+c
#
# ff = parrial(cc,5)
# print(ff(6,7))

#2.

def partial1(func,*args,**keywords):
    def newfunc(*fargs,**fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        print(newkeywords)
        print(args,fargs)
        return func(*args,*fargs,**newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc

def add(x,y,*args,z,**kwargs):
    return x+y+z
newfunc = partial1(add,1,2,3, z=100)
print(newfunc.func,newfunc.args,newfunc.keywords)
print(hex(id(add)))
print(newfunc(1,3,5,7))
'''
这里的输出结果是103,但是为什么是103呢?
那是因为,我们传给函数func的*args,*fargs,**newkeywords这三个包,分别对应了(1, 2, 3) (1, 3, 5, 7) {'z': 100}
因此x,y在解包的时候分别对应了1,2,z是固定传入的100,其他的都被*args接收了,因此结果是1+2+100=103 
'''


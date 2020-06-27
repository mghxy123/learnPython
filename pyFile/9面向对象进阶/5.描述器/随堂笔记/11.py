#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 11.py
# Author: HuXianyong
# Date  : 2019/5/27 17:32

# class A:
#     # __slots__ = 'x y'.split() #加上slots之后,除了slots定义的属性之外不允许其他的属性存入,在内部和实例中加入否不行.
#     __slots__ = 'y' #slots 是用于实例的属性控制的
#     def __init__(self):
#         self.x = 5
#         self.y = 6
#
# print(A.__dict__)
# print(A().y) #这力不能输出y,应为实例化的时候就已经出错了,不允许有x的属性的存在
# print(A().__dict__)


# class A:
#     # __slots__ = 'x y'.split() #加上slots之后,除了slots定义的属性之外不允许其他的属性存入,在内部和实例中加入否不行.
#     __slots__ = 'y' #slots 是用于实例的属性控制的
#     def __init__(self):
#         # self.x = 5
#         self.y = 6
#
#
# print(A.__dict__)
# print(A().y) #这力不能输出y,应为实例化的时候就已经出错了,不允许有x的属性的存在
# # print(A().__dict__)
#
#
# class B(A): #这里输出正常,应为slots不存在继承性
#     pass
# b = B()
# b.z = 100
# print(b.__dict__)


#利用slots来减少内存的使用

import tracemalloc
tracemalloc.start()

class A:
    # __slots__ = 'x y'.split() #使用slots是34M, #不适用slots是99M
    def __init__(self):
        self.x  =9
        self.y =10

d = [A() for i in range(1000000)]
s = tracemalloc.take_snapshot()
for i in s.statistics('filename'):
    print(i)
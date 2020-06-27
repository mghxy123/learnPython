#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.坐标判断.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

# from random import randint
#
# l1 = [(randint(1,100),randint(1,100)) for _ in range(10) ]
# l2 = [(randint(1,100),randint(1,100)) for _ in range(10) ]
# print(l1,l2)

class Point:

    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __eq__(self, other):
        # return hash((self.a,self.b)) == hash((other.a,other.b))
        return self.a ==other.a and self.b == other.b
    def __hash__(self):
        return hash((self.a,self.b))
    def __repr__(self):
        return '({}, {})'.format(self.a,self.b)

c = Point(1,2)
d = Point(1,2)
print(c == d)
print(c is d)
print(c,d)
print({c,d})

#决定一个类是否可以哈希,就是他的哈希方法来定义的,
#列表为什么不能哈希?那是因为列表里面的哈希方法直接等于了None,所以不能哈希
#object默认是可以哈希的,但是当我们把__hash__=None 的时候我们的类也就不能哈希了
#例子:

# class B:
#     def __hash__(self):
#         return None
# #这样就不能哈希了,
#
# class C:
#     __hash__ =None
#
# #这样这也不能哈希了
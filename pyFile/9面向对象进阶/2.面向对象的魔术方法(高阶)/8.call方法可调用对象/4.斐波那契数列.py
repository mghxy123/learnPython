#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.斐波那契数列.py
# Author: HuXianyong
# Date  : 2019/5/25 21:47

#自己写的最初版
# class Fib:
#     def __init__(self):
#         self.a = 0
#         self.b = 1
#         self.i = 0
#
#     def __call__(self, n, **kwargs):
#         while self.i <n-2:
#             self.a ,self.b = self.b,self.a+self.b
#             self.i +=1
#         return self.b
#
# f = Fib()
# print(f(9))

#自己写的回忆版
# class Fib:
#     def __init__(self):
#         self.ret = [0,1,1]
#
#     def __call__(self,n):
#         if n <3:
#             return 'index error'
#         for i in range(n-2):
#             l = len(self.ret)
#             self.ret.append((self.ret[l-1]+self.ret[l-2]))
#         print(self.ret)
#         return self.ret[n]
#
# b =Fib()
# print(b(3))

#老师的
class Fib:
    def __init__(self):
        self.items = [0,1,1]
    def __call__(self,index):
        if index<0:
            raise IndexError('Wrong Index')
        if index < len(self.items):
            return self.items[index]
        for i in range(len(self.items),index+1):
            self.items.append(self.items[i-1]+ self.items[i-2])
        print(self.items)
        return self.items[index]

b =Fib()
print(b(3))
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.fib斐波那契数列.py
# Author: HuXianyong
# Date  : 2019/5/24 11:01


# 自己写的
class Fib:
    def __init__(self):
        self.a = 0
        self.b = 1
        self.i = 0

    def __call__(self, n, **kwargs):
        while self.i <n-2:
            self.a ,self.b = self.b,self.a+self.b
            self.i +=1
        return self.b

f = Fib()
print(f(9))


######################################################################3
#老师的
class Fib:
    def __init__(self):
        self.iteams = [0,1,1]

    def __call__(self, index):
        if index <0:
            raise IndexError('not negative index')
        elif index<len(self.iteams):
            return self.iteams[index]
        for i in range(len(self.iteams),index+1):
            self.iteams.append(self.iteams[i-1]+self.iteams[i-2])
        return self.iteams[index]

f = Fib()
print(f(9))
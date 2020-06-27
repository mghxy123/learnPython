#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : aa.py
# Author: HuXianyong
# Date  : 2019/5/23 22:00

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

# 0 1 1 2 3 5 8 13 21
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.可迭代的斐波那契数列.py
# Author: HuXianyong
# Date  : 2019/5/25 22:23

class Fib:
    def __init__(self):
        self.items = [0,1,1]
    def __call__(self,index):
        return self[index] #直接调用实例的索引,也就是直接调用getitem然后来计算出结果,返回
    def __iter__(self):
        return iter(self.items)
    def __len__(self):
        return len(self.items)
    def __getitem__(self, index):
        if index<0:
            raise IndexError('Wrong Index')
        if index < len(self.items):
            return self.items[index]
        for i in range(len(self.items),index+1):
            self.items.append(self.items[i-1]+ self.items[i-2])
        print(self.items)
        return self.items[index]
    def __str__(self):
        return str(self.items)
    __repr__ = __str__
fib = Fib()
print(fib(5)) #全部计算
print(fib(10)) #部分计算
print(fib(9)) #不计算,直接到类里面的索引取值
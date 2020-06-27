#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.购物车类练习.py
# Author: HuXianyong
# Date  : 2019/5/25 20:42


class Cart:
    def __init__(self):
        self.items = []
    def __len__(self):
        return len(self.items)
    def additem(self,item):
        self.items.append(item)
    def __setitem__(self, key, value):
        self.items[key] = value
        print(self.items)
    def __getitem__(self, index):
        return self.items[index]

    def __iter__(self):
        return iter(self.items)
    def __call__(self, *args, **kwargs):
        pass
    def __str__(self):
        return str(self.items)
    def __add__(self,other):
        self.items.append(other)
        return self

a = Cart()
a.additem(1)
a[0]= 100
a.additem(10)
#长度bool
print(len(a))
print(bool(a))

#迭代
for x in a:
    print(x)

#in
print(10 in a)
print(1 in a)

#索引操作,
print(a[1])
print(a[1])
a[1] = 'abc'
print(a)

#链式编程实现加法
print(a  + 4 +5)
print(a.__add__(17).__add__(20))
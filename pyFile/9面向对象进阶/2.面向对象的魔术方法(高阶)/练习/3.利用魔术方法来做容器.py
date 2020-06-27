#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.利用魔术方法来做容器.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022


class Cart:
    def __init__(self):
        self.items = []

    def add(self,item):
        self.items.append(item)
        return self

    def __len__(self):
        return len(self.items)
    def __setitem__(self, key, value):
        self.items[key] = value

    def __getitem__(self, index):
        return self.items[index]

    def __repr__(self):
        return "{} {}".format(__class__.__name__,self.items)

    def __iter__(self):
        # return iter(self.items)
        yield from self.items
cart = Cart()
print(len(cart))
cart.add(1).add(2).add(6)
print(cart[1])

cart[0] = 100
print(cart)
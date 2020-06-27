#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.魔术方法gatattr.py
# Author: HuXianyong
# Date  : 2019/5/28 9:56

class Base:
    n = 0


class Point(Base):
    z = 6

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(self.x, self.y)

    def __getattr__(self, item):
        return 'missing {}'.format(item)


p = Point(3, 4)
print(p.x)
print(p.z)
print(p.n)
print(p.t)  # missing
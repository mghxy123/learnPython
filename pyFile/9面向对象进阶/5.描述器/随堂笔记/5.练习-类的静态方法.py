#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.练习.py
# Author: HuXianyong
# Date  : 2019/5/27 14:19


class StaticMethod:
    def __init__(self,fn):
        self.fn = fn

    def __get__(self, instance, owner):
        # print(self,instance,owner)

        return self.fn

class A:
    @StaticMethod #stmd = staticmethod(stmd)
    def stmd(x,y):
        print('sssssss',x,y)
a=A()
a.stmd(3,4)
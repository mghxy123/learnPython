#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : get和set的综合使用.py
# Author: HuXianyong
# Date  : 2019/5/27 10:00

class B:
    b = 200

class A:
    z = 100
    d = {}
    def __init__(self,x,y):
        self.x =x
        setattr(self,'y',y)
        self.y = y

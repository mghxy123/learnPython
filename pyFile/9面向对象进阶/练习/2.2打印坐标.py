#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.2打印坐标.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/18 0018

#我们上一种做法的思路是，当前数与后一位数进行配对，组成坐标，
# 我们现在可以换一种思路，就是每次取10个数两两组合就成了坐标了、

from random import randint
class RandomGen:
    @classmethod
    def generate(self,start=1,end=100,count=10):
        return [randint(start,end) for i in range(count)]

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

r= RandomGen()
l = r.generate(count=20)

points = [Point(x,y) for x,y in zip(r.generate(),r.generate())]

for p in points:
    print("{:2} : {:2}".format(p.x,p.y))
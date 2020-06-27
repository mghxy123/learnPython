#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.1打印坐标.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/18 0018

'''
2、打印坐标
    使用上题中的类，随机生成二十个数字，两两配对，形成二维坐标系的坐标，把这些坐标组织起来，并打印输出

'''

#方法一，一次性生成20个数字，当前数与后一位数进行配对，组成坐标打印输出。

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

points = [(l[i],l[i+1]) for i in range(0,20,2)]
print(points)
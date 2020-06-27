#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.随机数生成类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/16 0016

'''
1、随机数生成类
    可以先设定一批数字的个数，可设定指定生成数值的范围。运行时还可以调整每批生成数字的个数
'''
from random import randint
class randNum:
    def __init__(self,num,start,end):
        self.num = num
        self.start = start
        self.end = end

    def randNum(self):
        numList = [randint(self.start,self.end) for i in range(self.num)]
        return numList
a = randNum(20,10,100)
print(a.randNum())
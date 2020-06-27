#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.1随机整数生成类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/18 0018


#2.作为工具来实现，提供类方法：
from random import randint
class RandomGen:
    @classmethod
    def generate(self,start=1,end=100,count=10):
        return [randint(start,end) for i in range(count)]
print(RandomGen().generate())
print(RandomGen().generate(20,count=20))
print(RandomGen().generate(20,100,20))
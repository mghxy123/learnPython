#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.1随机整数生成类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/18 0018


#同样使用生成器实现，我们之前的思路是用生成器一个一个的生成然后去去取值，
# 现在我们的实现方法修改为，生成一批值，然后去获取：
from random import randint
class RandomGen:
    def __init__(self,start=1,end=100,count=10):
        self.start = start
        self.end = end
        self.count = count
        self._gen = self._generate()

    def _generate(self):
        while True:
            yield [randint(self.start,self.end)  for i in range(self.count)]

    def generate(self):
        return next(self._gen)

print(list(RandomGen().generate()))
print(list(RandomGen(20,count=20).generate()))
print(list(RandomGen(20,100,5).generate()))
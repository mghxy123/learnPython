#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.把类当做装饰器来实现.py
# Author: HuXianyong
# Date  : 2019/5/26 11:29

from time import sleep
from datetime import datetime

class Timeit:
    def __init__(self,fn):
        self.fn = fn

    def __enter__(self):
        self.start = datetime.now()
        return self.fn

    def __exit__(self, exc_type, exc_val, exc_tb):
        print((datetime.now() - self.start).total_seconds())

    def __call__(self,*args,**kwargs):
        start = datetime.now()
        ret = self.fn(*args,**kwargs)
        print((datetime.now() - start).total_seconds())
        return ret

@Timeit
def add(x=5,y=6):
    sleep(2)
    return x+y

print(add(2,3))
print(add(5,11))
print(add())
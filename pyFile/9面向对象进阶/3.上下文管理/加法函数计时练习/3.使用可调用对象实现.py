#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.使用可调用对象实现.py
# Author: HuXianyong
# Date  : 2019/5/26 11:25


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

    def __call__(self, x,y):
        return self.fn(x,y)

def timeit(fn):
    def wapper(*args):
        start = datetime.now()
        ret = fn(*args)
        print((datetime.now() - start).total_seconds())
        return ret
    return wapper

@timeit #add_new = timeit(add_old)  add_old的参数是传到了 timeit.wapper里面
def add(x=5,y=6):
    sleep(2)
    return x+y


with Timeit(add) as a:
    print(a(2,3))
    print(a())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.使用装饰器.py
# Author: HuXianyong
# Date  : 2019/5/26 10:29

from time import sleep
from datetime import datetime

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

print(add(2,3))
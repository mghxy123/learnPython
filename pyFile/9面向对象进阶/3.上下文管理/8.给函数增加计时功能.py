#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.给函数增加计时功能.py
# Author: HuXianyong
# Date  : 2019/5/26 15:59

from contextlib import contextmanager
from datetime import datetime
from time import sleep

@contextmanager
def add(x,y):
    start = datetime.now() #yield之上相当于__enter__()
    try:
        sleep(2)
        yield x+y#yield 5 yield的值只能有一个,作为__enter__方法的返回值
    finally:
        print ((datetime.now() - start).total_seconds())

with add(4,5) as f:
    print(f)
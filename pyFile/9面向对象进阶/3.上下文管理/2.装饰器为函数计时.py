#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.装饰器为函数计时.py
# Author: HuXianyong
# Date  : 2019/5/24 14:34

import time
import datetime



def addtime(fn):
    def inner():
        start = datetime.datetime.now()
        ret = fn
        end = datetime.datetime.now() - start
        print(end)
        return ret
    return inner()
@addtime # add = addtime(add)
def add(x=6,y=8):
    time.sleep(2)
    return x+y


print(add())
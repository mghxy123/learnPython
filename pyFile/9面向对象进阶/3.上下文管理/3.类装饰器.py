#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.类装饰器.py
# Author: HuXianyong
# Date  : 2019/5/24 15:22

import datetime,time
from functools import wraps,update_wrapper

class Timeit:
    '''timeit  ssss'''
    def __init__(self,fn):
        self.fn = fn
        # print(self.fn.__doc__)
        # self.__doc__ =fn.__doc__
        # self.__name__ =fn.__name__
        # update_wrapper(self,fn)
        wraps(fn)(self)


    def __call__(self, *args, **kwargs):
        start =  datetime.datetime.now()
        ret = self.fn(*args,**kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()

        print(delta)
        return ret



@Timeit
def add(x,y):
    '''add  dddd'''
    # time.sleep(2)
    return x+y
# print(add(4,5))
print(add.__doc__)
print(add.__name__)
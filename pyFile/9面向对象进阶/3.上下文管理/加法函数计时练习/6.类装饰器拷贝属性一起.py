#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.类装饰器拷贝属性一起.py
# Author: HuXianyong
# Date  : 2019/5/26 11:37

from time import sleep
from datetime import datetime
from functools import wraps

class Timeit:
    '''this is Timeit class'''
    def __init__(self,fn):
        self.fn = fn
        #把函数对象的文档字符串赋给类
        #self.__doc__ = fn.__doc__
        # update_wrapper(self,fn)
        wraps(fn)(self)#这一句和上面的依据作用是一样的
        #这样就实现了属性的拷贝了,
        #这个不同于函数的装饰器,函数装饰器直接@wraps就OK了,类里面你保护知道该怎么覆盖,就只能把wraps当做函数来覆盖了

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
    '''this is add function'''
    sleep(2)
    return x+y

print(add(2,3))
print(add.__doc__)
print(Timeit(add).__doc__)
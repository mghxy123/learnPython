#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.异常处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021

def foo():
    try:
        print('befor')
        c = 1/0
        print('after')
    except:
        print('error')

    print('catch the exception')
foo()
print('end','='*30)
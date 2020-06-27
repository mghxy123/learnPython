#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.捕获指定的异常.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


def foo():
    try:
        print('before')
        print(1/0)
        print('after')
    except ArithmeticError: #指定捕获的异常类型
        print('error')

    print('catch the exeption')
foo()
print('end','+'*39)


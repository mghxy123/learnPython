#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 12.异常的传递.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022


def foo():
    return 1/0

def bar():
    print('bar start')
    foo()
    print('bar end')

bar()
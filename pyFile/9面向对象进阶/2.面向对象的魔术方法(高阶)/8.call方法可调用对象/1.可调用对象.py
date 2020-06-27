#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.可调用对象.py
# Author: HuXianyong
# Date  : 2019/5/25 21:26

def foo():
    print(foo.__module__,foo.__name__)
foo()
# 等价于
foo.__call__()
#这两个的输出结果是相通的
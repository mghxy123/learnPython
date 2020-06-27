#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.exit获取异常信息.py
# Author: HuXianyong
# Date  : 2019/5/26 10:21

class Point:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(1,exc_type)
        print(2,exc_val)
        print(3,exc_tb)
        print('exit end ---=--')

p = Point()
with p as f:
    print('in with ---------')
    print(1/0)
    print('with end')

print('='*30)
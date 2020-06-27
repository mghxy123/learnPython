#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.理解as字句.py
# Author: HuXianyong
# Date  : 2019/5/26 10:04


class Point:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')
        return self #增加返回值

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')


f = open('4.py')
with f as p:
    print(f)
    print(p)
    print(p is f)
    print(p == f)

print('*'*50)
p = Point()
with p as f:
    print('in with =========')
    print(p == f)
    print('with over')

print('end','---'*10)
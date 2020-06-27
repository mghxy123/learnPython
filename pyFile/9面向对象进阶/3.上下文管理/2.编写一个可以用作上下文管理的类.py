#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.编写一个可以用作上下文管理的类.py
# Author: HuXianyong
# Date  : 2019/5/26 9:24

from time import sleep

class Point:
    def __init__(self):
        print('init _____')
        sleep(2)
        print('end init ')
    def __enter__(self):
        print('enter now ')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('now exit over')

with Point() as p:
    print('in with -------')
    sleep(2)
    print('with is over')
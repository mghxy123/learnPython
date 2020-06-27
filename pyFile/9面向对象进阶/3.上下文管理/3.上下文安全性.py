#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.上下文安全性.py
# Author: HuXianyong
# Date  : 2019/5/26 9:39

# from time import sleep
# import sys
#
# class Point:
#     def __init__(self):
#         print('init _____')
#         sleep(2)
#         print('end init ')
#     def __enter__(self):
#         print('enter now ')
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('now exit over')
#
# with Point() as p:
#     print('in with -------')
#     raise Exception('error')
#     sleep(2)
#     print('with is over')


from time import sleep
import sys

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
    sys.exit(1)
    sleep(2)
    print('with is over')

#上面的两个例子的exit都顺利的执行了,说明上下文管理是很安全的.
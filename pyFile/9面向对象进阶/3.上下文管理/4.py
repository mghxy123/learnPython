#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.py
# Author: HuXianyong
# Date  : 2019/5/26 9:56

class Point:
    def __init__(self):
        print('init')

    def __enter__(self):
        print('enter')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')

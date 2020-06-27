#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/30 0030

def aa(ignore=None):
    names = ['a','b','c','d']
    if ignore is not None:
        ignored_names = ignore('ff', names)
    else:
        ignored_names = set()
    print(ignored_names)

def igone_fn(src, names):
    pass


print(aa(ignore=('b')))
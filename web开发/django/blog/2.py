#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.py
# Author: HuXianyong
# Date  : 2019/7/18 16:01


def func(num:int,defaule:int,size:int=None):
    try:
        if size:
            num = num if num > 0 and num <size else defaule
        num = num if num >0 else defaule

    except Exception as e:
        num = defaule

    return num

print(func(-1,2))
print(func(102,20,101))
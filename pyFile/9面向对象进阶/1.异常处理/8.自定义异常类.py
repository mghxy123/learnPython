#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 8.自定义异常类.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


class MyException(Exception):
    pass

try:
    raise MyException()

except MyException:#捕获自定义异常类
    print('catch the exception')
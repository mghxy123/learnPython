#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 15..py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

# 当异常在内部无法被捕获到,且内部有finally或者break的时候就会中断异常的向外抛出,从而使代码正常的向外执行下去.

# eg:
def foo():
    try:
        ret = 1/0
    except KeyError as e:
        print(e)
    finally:
        print('inner fin')
        return #异常被丢弃,程序继续往下执行

try:
    foo()
except:
    print('outer catch')
finally:
    print('outer fin')

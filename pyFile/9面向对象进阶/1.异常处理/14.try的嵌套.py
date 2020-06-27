#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 13.try的嵌套.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

try:
    try:
        ret = 1/0
    except KeyError as e:
        print(e)
    finally:
        print('inner fin')
except:
    print('outer catch')
finally:
    print('outer fin')
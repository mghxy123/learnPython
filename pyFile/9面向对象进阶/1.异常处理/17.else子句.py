#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 17.else子句.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

try:
    ret = 1*0
except ArithmeticError as e:
    print(e)
else:
    print('ok')
finally:
    print('fin')
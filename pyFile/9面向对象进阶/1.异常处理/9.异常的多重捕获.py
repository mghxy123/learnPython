#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 9.异常的多重捕获.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


import sys

class MyException(Exception):pass

try:
    a = 1/0
    raise MyException()
    open('a')
    sys.exit(1)
except ZeroDivisionError:
    print('zero')

except ArithmeticError:
    print('ari')

except MyException:
    print('myexc')

except Exception:
    print('exc')

except:
    print('sysexit')
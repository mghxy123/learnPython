#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.系统异常.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021


import sys

print('before')
sys.exit(1)
print('Sysexit')
print('outer') #是否能执行?

# try :
#     sys.exit(2)
# except SystemExit: #换成了Exception 能否捕获?
#     print('Systxit')
# print('outer') #是否执行?
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 9.搜索顺序.py
# Author: HuXianyong
# Date  : 2019/5/30 19:15

import sys

print(*sys.path,sep='\n')
#这两个输出的结果是一样的,只是上面的结果是结构输出的
# for  p in sys.path:
#     print(p)
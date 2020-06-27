#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 7.名词空间.py
# Author: HuXianyong
# Date  : 2019/5/30 17:29

from pathlib import Path #导入Path模块

print(1,Path,id(Path))

import pathlib as p1 #导入模块使用别名
print(2,dir())
print(3,p1)
print(4,p1.Path,id(p1.Path))
#可以查看出导入的名词空间Path和p1.Path是同一个对象
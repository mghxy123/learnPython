#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.from.py
# Author: HuXianyong
# Date  : 2019/5/30 17:10

from pathlib import Path,PosixPath #在当前名词空间导入该模块指定的成员
print(1,dir())

from pathlib import * #在当前名词空间导入该模块所有公共成员(非下划线开头成员,)或指定成员
print(2,dir())

from functools import wraps as wr,partial #别名
print(3,dir())
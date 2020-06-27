#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.仿照打开文件方法,写一个上下文管理.py
# Author: HuXianyong
# Date  : 2019/5/26 9:07

# with open('test') as f:
#     pass


# 仿照上面的例子写一个自己的类,实现上下文管理

class Point:
    pass

with Point() as p: #AttributrError: __exit__
    pass
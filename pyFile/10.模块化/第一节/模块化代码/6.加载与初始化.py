#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.加载与初始化.py
# Author: HuXianyong
# Date  : 2019/5/30 17:16

from os.path import exists #加载.初始化os,os.path模块,exists加入本地命名空间并绑定

if exists('dir'):
    print('found')
else:
    print("not found")

print(dir())
print(exists)

import os
#4种方式获得同一个对象exists
print(os.path.exists)
print(exists)
print(os.path.__dict__['exists']) #字符串
print(getattr(os.path,'exists')) #字符串

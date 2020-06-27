#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.模块的导入.py
# Author: HuXianyong
# Date  : 2019/5/30 17:03

def testimport():
    import os.path
    print(dir())

testimport()
print(globals().keys())
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 上下文管理.py
# Author: HuXianyong
# Date  : 2019/8/17 19:16


f1 = open('test')
with f1:
    f1.write('acc') # 文件只读 写入失败
# 测试f是否关闭
f1.close() # f的作用域
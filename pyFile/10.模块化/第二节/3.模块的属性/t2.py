#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : t2.py
# Author: HuXianyong
# Date  : 2019/5/30 22:26

import t1

for k,v in t1.__dict__.items():
    print(k,str(v)[:80])
print('-'*100)
print(dir(t1))
print(getattr(t1,'__builtins__').keys())
print('-'*100)
for name in dir(t1):
    print(name,str(getattr(t1,name))[:80])

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : t3.py
# Author: HuXianyong
# Date  : 2019/5/30 18:37

#t3.py file
print('This is t3 module')
from t1 import A as cls

print()
print(__file__)
print('='*60)
a = cls()
a.showmodule()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : t2.py
# Author: HuXianyong
# Date  : 2019/5/30 19:35

import t1
import sys

print('local module')
import t1
import t1
import t1
import t1
print(sys.modules.keys())

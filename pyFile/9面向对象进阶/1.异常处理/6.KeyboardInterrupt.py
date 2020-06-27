#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 6.KeyboardInterrupt.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/21 0021

#这个是捕获用户中断行为Ctrl+c

try:
    import time
    while True:
        time.sleep(1)
        print('111')
except KeyboardInterrupt:
    print('ctrl + c')
print('+'*30)
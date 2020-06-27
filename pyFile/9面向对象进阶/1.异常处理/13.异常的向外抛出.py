#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 12.异常的向外抛出.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

#线程中测试异常

import threading
import time

def foo():
    return 1/0

def bar():
    time.sleep(3) #两秒后抛出异常
    print('bar start')
    foo()
    print('bar end')

t = threading.Thread(target=bar)
t.start()

while True:
    time.sleep(1)
    print('Everything OK')
    print(threading.enumerate()) #打印当前所有线程
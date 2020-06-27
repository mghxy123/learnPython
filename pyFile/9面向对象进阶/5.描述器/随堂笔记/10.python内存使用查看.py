#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 10.python内存使用查看.py
# Author: HuXianyong
# Date  : 2019/5/27 17:22

import tracemalloc

tracemalloc.start() #开始跟踪分配

d = [dict(zip('xy',(4,5))) for i in range(1000000)] #134M
t = [tuple(zip('xy',(4,5))) for j in range(1000000)] #107M
snapshot = tracemalloc.take_snapshot() #快照当前内存分配
stats = snapshot.statistics('lineno') #快照当前对象
# stats = snapshot.statistics('filename')

for s in stats:
    print(s)

#通过这个模块可以查看字典和列表占用内存的大小

'''
C:/Users/abc/Desktop/learnPython/pyFile/9面向对象进阶/4.描述器/随堂笔记/10.python内存使用查看.py:11: size=134 MiB, count=1999995, average=70 B
C:/Users/abc/Desktop/learnPython/pyFile/9面向对象进阶/4.描述器/随堂笔记/10.python内存使用查看.py:12: size=107 MiB, count=3000002, average=37 B
C:/Users/abc/Desktop/learnPython/pyFile/9面向对象进阶/4.描述器/随堂笔记/10.python内存使用查看.py:13: size=348 B, count=1, average=348 B
C:\software\python3\lib\tracemalloc.py:532: size=36 B, count=1, average=36 B


'''
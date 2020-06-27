#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.tracemalloc模块.py
# Author: HuXianyong
# Date  : 2019/5/28 17:49

import tracemalloc

'''
使用tracemalloc模块来跟踪内存,
我们就可以很清楚的看到了字典和元祖的内存消耗的情况比较了
'''
tracemalloc.start() #开始跟踪内存分配

d = [dict(zip('xy',(5,6))) for i in  range(1000000)] #134M
f = [tuple(zip('xy',(5,6))) for j in  range(1000000)] #107M
snapshot = tracemalloc.take_snapshot() #快照,当前内存分配
top_stats = snapshot.statistics('lineno') #快照对象的统计

for stat in top_stats:
    print(stat)
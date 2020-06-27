#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 二叉树.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/13 0013


list1 = [1,2,3]

l = [[' ']* len(list1) for i in range(len(list1)) ]
print(*l,sep='\n')
for i,c in enumerate(list1):
    if 2**i > len(list1):
        for j,k in enumerate(list1):
            if j == 2**i:
                print(k)
            else:
                print(' ')

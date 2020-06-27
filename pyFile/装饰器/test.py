#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : test.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/23 0023


'''
打印出数字三角形
                         1
                       2 1
                     3 2 1
                   4 3 2 1
                 5 4 3 2 1
               6 5 4 3 2 1
             7 6 5 4 3 2 1
           8 7 6 5 4 3 2 1
         9 8 7 6 5 4 3 2 1
      10 9 8 7 6 5 4 3 2 1
   11 10 9 8 7 6 5 4 3 2 1
12 11 10 9 8 7 6 5 4 3 2 1
'''
#方法一,左边加空格

def triangle1(n):
    for i in range(1,n+1):
        for j in range(n,0,-1):
            if i >= j:
                print('%-2s'%j,end=' ')
            else:
                print('   ',end='')
        print()
triangle1(12)

#方法二,左边加空格(这样的效率不高)
def triangle2(n):
    for i in range(1,13):
        for j in range(12,0,-1):
            print(' '*len(str(j)) if j > i else j,end=' ')
        print()

#方法三，右对齐
#
# def triangle3(n):
#
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 阶层.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/24 0024

'''
求任意数的阶乘,

'''

#方法一: 利用for循环求出阶乘
#正向for循环
def factorial1(n):
    sum_result = 1
    for i in range(1,n+1):
        sum_result *= i
    return sum_result
# print(factorial1(8))

#反向for循环
def factorial2(n):
    sum_result = 1
    for i in range(n,0,-1):
        sum_result *= i
    return sum_result
# print(factorial2(8))


#方法二,利用递归求阶乘

def factorial3(n):
    return 1 if n < 2 else n*factorial3(n-1)
# print(factorial3(8))


def factorial4(n):
    if n<2:
        return 1
    return n*factorial4(n-1)

# print(factorial4(8))

def factorial5(n=8,ret=1):
    ret *= n
    if n == 1:
        return ret
    return factorial5(n-1,ret)
print(factorial5())
print(factorial5(6))
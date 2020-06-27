#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 斐波那契数列.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/24 0024

import datetime

'''
斐波那契数列的样子是第三个数等于前两个数之和
1 1 2 3 5 8 13 21.....n=(n-1) +(n-2)
'''

# 使用循环来实现斐波那契数列(这种方法相对于下面两种方法效率搞高)
def fib1(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+ b
    return a

# 利用函数压栈来实现斐波那契数列(这个的实现效率比上面的循环略低)
def fib2(n, a=0, b=1):
    a, b= b, a+b
    if n == 1:
        return a
    return fib2(n-1, a, b)

# 利用迭代来实现斐波那契数列这样效率最低
# 它的效率底那是因为每次函数都会压栈,每次压栈都会再次使用内存,这样会消耗大量的内存用于计算
# 而循环则是循环一次使用一次,再次开始新循环的时候释放上次的,在申请使用一次,这样效率要比迭代的要高
# def fib3(n):
#     if n < 3:
#         return 1
#     return fib3(n-2) + fib3(n-1)
# print(fib3(10))

def fib4(n):
    return 1 if n < 3 else fib4(n - 1) + fib4(n - 2)


# 使用生成器实现斐波那契数列(这样的效率也很高)
def fib5(n):
    a,b = 0, 1
    count = 0
    while True:
        a, b = b, a+ b
        count +=1
        if n<= count:
            yield a
            break
    return a

print(next(fib5(30)))
print(fib1(30))
# starTime = datetime.datetime.now()
# for j in range(2000):
#     next(fib5(30))
#
# time = datetime.datetime.now() - starTime
# print(time)

# lis = [fib1,fib2,fib4]
# for i in lis:
#     starTime = datetime.datetime.now()
#     for j in range(200):
#         i(30)
#     time = datetime.datetime.now() - starTime
#     print(time)
#
# print(fib1(10))
# print(fib2(10))
# print(fib4(10))
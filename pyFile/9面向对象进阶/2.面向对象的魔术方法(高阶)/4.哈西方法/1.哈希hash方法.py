#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.哈希hash方法.py
# Author: HuXianyong
# Date  : 2019/5/25 15:17

'''
类的hash方法可以加快类的检索
hash是先开辟内存空间,然后再把值丢进去,只要hash值相同里面的内容就是相同的,
这是一个key,value,所以速度很快,但是很消耗内存,这是一种空间换时间的方法
'''

#观察一下的哈希值的变化

print(hash(1))
print(hash(200))
print(hash(200000))
print(hash('tom'))
print(hash(('tom',)))

#结论是:
#整数的哈希算法用的是余数取模法,这也是最简单的哈希算法
# print(1%4,2%4,3%4,4%4,5%4)#这就叫取模
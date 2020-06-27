#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 插入排序.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/24 0024

from random import randint
l = [19, 20, 19, 9, 3, 14, 3, 6, 17, 14]
# list1 = [ randint(1,20) for i in range(10)]
# print(list1)
l = [None] +l

for i in range(2,len(l)):#这里面的是循环出无序区的所有数字
    l[0] = l[i] #把无序区的数字以此赋值给列表第一位
    j = i-1 #j属于有序区的下标
    if l[0] < l[j]: #如果有序区的数字小于,无序区的数字,就把这个数字掉到有序区来一一和有序区的数字作比较
        while l[0] < l[j]:#如果 这个数字小于有序区的数字,那么,有序区的数字在这个数字插入的时候,右边整体向右挪一位
            l[j+1] = l[j]
            j -= 1
        l[j+1] = l[0] #这里是为了把无序区的数字调过来,作比较,然后一次循环
print(l[1:])

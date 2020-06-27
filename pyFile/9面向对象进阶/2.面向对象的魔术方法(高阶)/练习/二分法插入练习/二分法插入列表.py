#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 二分法插入列表.py
# Author: HuXianyong
# Date  : 2019/5/24 19:50


'''
一个列表,先对其跑徐输出新链表.
分别尝试插入20,40,41到这个新序列中找到合适的位置,保证其有序.

思路:
排序后二分法找到适当的位置插入数值.
排序使用sorted解决,假设升序输出.
查找插入点,使用二分法查找完成,
假设全场为n,首先在大致的重点元素开始和待插入数比较,如果大,则和右边区域的的额重点继续比较,如果小,就和左边区域的重点进行比较,以此类推.
直到找到适合的位置


'''
# from random import randint
# l = [randint(10,100) for _ in range(10)]
# print(l)

# lst = [86, 40, 22, 71, 80, 20, 57, 73, 59, 93]
# lst = sorted(lst)
# print(lst)

lst = [20, 22, 40, 57, 59, 71, 73, 80, 86, 93]

def insert_sort(orderList,n):
    ret = orderList[:]
    head = 0
    end = len(lst)
    while head < end:
        mid = (head + end) // 2
        if ret[mid] < n:
            head = mid + 1 #说明n大了,往右找,调整下限
        else:
            end = mid #说明n小于等于了,往左查找,调整上限,
    # print(head,n)
    ret.insert(head,n)# head为插入点

    return ret #返回修改之后的列表
    # return head #返回插入节点,就可成为二分查找法
print(insert_sort(lst,42))
l = [40,20,41,100]
for i in l:
    new_list = insert_sort(lst,i)
    print(new_list)

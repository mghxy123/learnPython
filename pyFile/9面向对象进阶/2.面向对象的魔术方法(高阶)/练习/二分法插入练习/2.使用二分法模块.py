#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.使用二分法模块.py
# Author: HuXianyong
# Date  : 2019/5/24 19:57


'''
* bisect模块提供的函数有:
    - `bisect.bisect_left(x,y lo=0,hi=len(a))`
    查找在有序列表a中插入的index.lo和hi用于指定列表的区间,默认使用整个列表.如果x已经存在,再沸器左边插入.返回值index.
    - `bisect.bisect_right(a,x,lo=0,hi = len(a))`或`bisect.bisect(a,x,lo=0,hi = len(a))`
    和bisect_lift类似,但是如果存在,在其左右插入.
    - `bisect.insort_lift(a,x,lo=0,hi = len(a))`
    在有序列表a中插入x.等同于a.insert(bisect.bisect_left(a,x,lo,hi),x).
    - `bisect.insort_right(a,x,lo = 0,hi=len(a))`或者`bisect.insort(a,x,hi=len(a))`
    和insort_left函数类似,但是如果x已经存在了,在其右边插入.

函数可以分为两类:
bisect系,用于查找index.
insort系,用于实际插入.
默认重复时从右边插入.

'''
import bisect

lst = [20, 22, 40, 57, 59, 71, 73, 80, 86, 93]

newlst = sorted(lst)#升序

print(newlst)
print(list(enumerate(newlst)))
# bisect系用于查找适合插入的下标位置的index
# bisect 默认是right
print(20,bisect.bisect(newlst,20))
print(30,bisect.bisect(newlst,30))
print(40,bisect.bisect(newlst,40))

print('='*40)
print(20,bisect.bisect_left(newlst,20))
print(30,bisect.bisect_left(newlst,30))
print(40,bisect.bisect_left(newlst,40))
print('='*40)

# insort系用于再适合的位置直接插入,不会返回下标了
bisect.insort(newlst,20)
print(20,newlst)
bisect.insort(newlst,30)
print(30,newlst)
bisect.insort(newlst,40)
print(40,newlst)
print('='*40)
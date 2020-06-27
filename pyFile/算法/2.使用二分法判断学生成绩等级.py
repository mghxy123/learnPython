#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.使用二分法判断学生成绩等级.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

import random
import bisect
# l = [random.randint(30,100) for i in range(10)]
# print(l)

l = [64, 97, 31, 65, 63, 73, 59, 54, 75, 59]

def get_grade(score):
    break_points = [60,70,80,90]
    grades = 'EDCBA'
    return grades[bisect.bisect(break_points,score)]
for x in l:
    print(x,get_grade(x))

'''
二分查找法来判断学生成绩低等级的方法是,
利用了二分查找法可以快速的找到与分数范围内相对应的索引位置,
也就是我们在上面的定义的分数等级范围break_points,当分数在某个范围内我们就能找到
相对于的索引,通过等级字符串取得等级
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.应用二分法模块.py
# Author: HuXianyong
# Date  : 2019/5/24 20:08

import bisect
lst = [20, 22, 40, 57, 59, 71, 73, 80, 86, 93]

# '''
# 判断学生成绩,成绩登记A-E,其中,90分以上的为A,80-89的为B,70-79为C,60-69分为D,60分一下的为E
#
# '''
#
# # 普通方法
# def get_grade(score):
#     if score >= 90:
#         return 'A'
#     elif 80 <= score <90:
#         return 'B'
#     elif 70 <= score <80:
#         return 'C'
#     elif 60 <= score <70:
#         return 'D'
#     else:
#         return 'E'
# for i in lst:
#     print('{} => {}'.format(i, get_grade(i)))



#上面利用if判断,太过啰嗦了,我们可以使用二分法来做,就可以简单很多,

'''分析:
    在分数区间内查找适合的插入分数的位置,这就是我们等级的位置了,
    [E,60,D,70,C,80,B,90,A]
    当我们找到了适合的位置就变成了这个样子了

'''

def get_grade(score):
    breakpionts = [60,70,80,90]
    grades = 'EDCBA'
    return grades[bisect.bisect(breakpionts,score)]
for i in lst:
    print('{} => {}'.format(i,get_grade(i)))


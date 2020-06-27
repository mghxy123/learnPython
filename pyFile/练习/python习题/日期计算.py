#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 天数计算.py
# Author: HuXianyong
# Date  : 2019/8/18 16:45

'''
要求: 输入年月入,能直接输出这是某年的第几天
解题思路: 做一个天数的列表,索引月数-1,得到某月的天数再加上几日,就是当前的天数
如果遇到的闰年就再在之前的基础上再加上1就是当前的天数
'''


# year = int(input('请输入年份: '))
# month = int(input('请输入月年份: '))
# days = int(input('请输第几天: '))
#
# months = [0,31,59,90,120,151,181,212,243,273,304,334] #按月份统计该月份前的天数
#
#
# if 0 < month < 13 :
#     mon = month - 1
#     someday = months[mon] + days
# else :
#     raise ('month type error')
#
#
# # 闰年判断
# if (year % 400 == 0) or ( year % 4 == 0  and  year % 100 !=0 ):
#     day = 1
#
#     if (day == 1) and (month > 2):
#         someday += 1
#
# print('今天是今年的第{} 天'.format(someday))































# year = int(input('请输入年份:  '))
# month = int(input('请输入月份:  '))
# day = int(input('请输入日期:  '))
#
# # 闰年判断
# if (year % 400 == 0 ) or ( year % 4 == 0  and year % 100 != 0):
#
#     ruen = 1
# else:
#     ruen = 0
#
#
# # months = [0,31,59,90,120,151,181,212,243,273,304,334] #按月份统计该月份前的天数
# # 当月天数(非闰年)
# month_days = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304,334]




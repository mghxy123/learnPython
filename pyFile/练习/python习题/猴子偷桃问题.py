#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 猴子偷桃问题.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/24 0024


'''
需求
* 题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个 第二天早上又将剩
* 下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。

#分析:
    每天的数量是下一天的两倍还多一个,到第十天就只剩下了1个了
    day10 -- 1
    day9 -- 3
    .
    .
    day2 -- day3*2 + 1
    day1 -- day2*2 + 1
这样一来就明白了

'''


#用递归的方法去做
# def monkey(n=10,total=1):
#     if n == 0:
#         return 1
#     print(f'day{n} --> num: {total}')
#     return monkey(n-1,2*(total + 1))
#
# monkey()

def monkey2(n=10,total=1):#这个循环计算了10次

    print(f'day{n} --> num: {total}')
    if n == 1:
        return total
    total = 2 * (total + 1)
    return monkey2(n-1,total)

print(monkey2())
#
# def peach(day=10): #day=9
#     if day == 10:
#         return 1
#     return 2*(peach(day+1)+1)
# print(peach(1)) #day=1
#
# #用for循环的方法去做
# num = 1
# for i in range(9):
#     num = 2*(num+1)
# print(num)
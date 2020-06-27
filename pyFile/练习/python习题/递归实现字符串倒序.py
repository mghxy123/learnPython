#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 递归实现字符串倒序.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/4/24 0024

'''
普通的字符串倒序
'''

# string = '1234'
# ##1/使用map来做
# # l = list(map(int,reversed(string)))
# # print(l)
#
# #2/使用循环来做
# t1 = tuple(string)
# l2 =[]
# for i in range(len(t1)-1,-1,-1):
#     # print(i,len(t1))
#     l2.append(t1[i])
# print(l2)
#
# #3/使用切片来做
# print(string[::-1])

# #4/使用递归方法来做
# def revert(data,target=[]):
#     target.append(data[-1])
#     if len(data) == 1:
#         return target
#     return revert(data[:-1])
# print(revert('1234'))
# print(revert.__defaults__)
######
#应为把列表当做缺省值传入函数
target=[]
def revert(data):
    target.append(data[-1])
    if len(data) == 1:
        return target
    return revert(data[:-1])
print(revert('1234'))
print(revert("789"))

# def revert(data,target=[]):
#     target.append(data[-1])
#     if len(data) == 1:
#         return target
#     return revert(data[:-1])
# print(revert('1234'))
# print(revert("789"))

#由于在我们把列表当作缺省值传入函数与把列表当做全局变量的时候会出现函数没被执行完,缺省值会一直被记录,
#从而污染我们的下一个数据,这样得不偿失,还需要我们进一步的做出改进

# def revert(data,target=None):
#     if target is None:
#         target = list()
#     target.append(data[-1])
#     if len(data) == 1:
#         return target
#     return revert(data[:-1],target)
# print(revert('1234'))
# print(revert("789"))
#

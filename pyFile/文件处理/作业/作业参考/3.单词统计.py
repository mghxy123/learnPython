#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.单词统计.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/6 0006

filename = '../sample.txt'

######################################################################################
# #最简单,最原始的解决办法
# d = {}
# with open(filename,encoding='utf8') as f:
#     for line in f:
#         words = line.split()
#         for word in map(str.lower,words):#不区分大小写
#             d[word] = d.get(word,0) + 1
# print(sorted(d.items(),key=lambda item:item[1],reverse=True))


######################################################################################
# #使用缺省字典
# from collections import defaultdict
# d = defaultdict(lambda :0)#lambda 不传参,默认返回0
# with open(filename,encoding='utf8') as f:
#     for line in f:
#         words = line.split()
#         for word in map(str.lower,words):
#             d[word] += 1
#
# print(sorted(d.items(),key=lambda items:items[1],reverse=True))
# ######################################################################################
# for k in d.keys():
#     if k.find('path') > -1:
#         print(k)

######################################################################################
# def makekey(s:str):
#     chars = set(r'''!@#$%^&*(){}:"<>?. ''')
#     key  = s.lower()
#     ret = []
#     for c in key:
#         if c in chars:
#             ret.append(' ')
#         else:
#             ret.append(c)
#     return ''.join(ret).split()
#
# d = {}
# with open(filename,encoding='utf8') as f:
#     for line in f:
#         for word in makekey(line):
#             d[word] = d.get(word,0) + 1
#
# for k,v in sorted(d.items(),key=lambda x:x[1],reverse=True)[:10]:
#     print(k,v)
######################################################################################
#切片提取单词
import os
def makekey(s:str):
    chars = set('''!@#$%^&*())_-=,.;'[\] ''')
    key = s.lower()
    ret = []
    start = 0
    length = len(key)

    #'abc' ([Path]) ''
    for i,c in  enumerate(key):
        if c in chars:
            if start == i:
                start += 1
                continue
            ret.append(key[start:i])
            start += 1
        else:
            if start < length:
                ret.append(key[start:])

    return ret
print(makekey('os.path.exists(path)'))
######################################################################################
######################################################################################
######################################################################################

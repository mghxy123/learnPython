#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 取单词.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008

# import re
# tr = ['adj', '', 've', 'r' ,'b','n' ,'l', 'vi','p,','t']
# worlds = []
# with open('aaaa.txt','r',encoding='utf8') as f :
#     content = f.read()
#     lines = re.split('[^a-zA-Z]',content)
#     for i in  lines:
#         if len(i) <5:
#             continue
#         else:
#             worlds.append(i)
#
# print(len(set(worlds)),set(worlds))

import re
worlds = set()
def words(filename,encoding='utf8'):
    with open(filename,'r',encoding=encoding) as f :
        content = f.read()
        lines = content.split()
        for i in  lines:
            j= re.match('([a-z]{3,})',i)
            # print(j)
            if j != None:
                # print(j.group(1))
                worlds.add(j.group(1))

    with open('word.txt','w') as f2:
        for i in worlds:
            f2.write(i+'\n')

words('aaaa.txt')
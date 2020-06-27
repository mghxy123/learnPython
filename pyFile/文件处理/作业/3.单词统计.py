#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.单词统计.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/2 0002

'''
有一个文件,对其进行单词统计,并区分大小写,并显示重复最多的10个单词

'''

'''
分析:
    1.首先找到单词的分隔符,
    2.把单词分割开来组成一个列表
    3.对列表进行统计,组成一个字段,
    4,使用lambda函数对字典的value进行排序
    5.取出前十的单词
'''

import  re
# strt = 'The following names have currently been registered: \'posix\', \'nt\', \'java\'.'
#
# print(re.split('\' | ,',strt))
# split_world1 = (chr(x) for x in range(32,64))
# split_world2 = (chr(x) for x in range(91,97))
# split_world3 = (chr(x) for x in range(123,127))
# split_world = split_world1 + split_world2+split_world3
# for i in split_world:
#     print(i)
#
# for i in range(32,64):
#     print(chr(i))
world_dict = {}
with open('sample.txt','r',encoding='utf8') as f:
    line_worlds = f.read()
    list1 = re.split(' |,|;|\.|\'|\"|-|\n|/|\(|\)|=|: ',line_worlds)
    set1=set(list1)
    for i in set1:
        world_dict[i.lower()] = list1.count(i.lower())
# print(world_dict)
new_world_dict  = sorted(world_dict.items(),key = lambda x:x[1],reverse=True)

n = 0
for (word,times) in new_world_dict:
    if word == "":
        continue
    print(word,times)
    n+=1
    if n >9:
        break

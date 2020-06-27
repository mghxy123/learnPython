#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.单词统计和排除.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/2 0002

import re

def ignore_worlds():
    top_worlds = {}
    worlds= input('''
        请输出你不想看到的单词
        例如: a b c d 
        然后按回车确认后开始统计
        请输入:
    ''')
    ignore_list = worlds.split(' ')
    ignore_list.append('')
    # print(ignore_list)
    if len(ignore_list) == 0:
        return None

    n = 0
    new_world_dict = count_worlds()
    for (world,times) in new_world_dict:
        if ignore_list != None:
            if world in ignore_list:
                continue
            print(world,times)
            top_worlds[world] = times
            n+=1
            if n >9:
                break
    print(top_worlds)
    # return ignore_list

def count_worlds():
    world_dict = {}
    with open('sample.txt','r',encoding='utf8') as f:
        line_worlds = f.read()
        list1 = re.split(' |,|;|\.|\'|\"|-|\n|/|\(|\)|=|: ',line_worlds)
        set1=set(list1)
        for i in set1:
            world_dict[i.lower()] = list1.count(i.lower())
    new_world_dict  = sorted(world_dict.items(),key = lambda x:x[1],reverse=True)
    return new_world_dict


ignore_worlds()
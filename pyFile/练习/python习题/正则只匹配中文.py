#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 正则练习.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/8/28 0028



# import re
#
# a = 'not found 404 小李子 22 二货'
# res = re.findall(r'[\u4e00-\u9fa5]+',a)
#
# print(res)

str1 = 'this is 这个是 name 小李子, and his 二货 !'
'''要求只输出中文,不要英文
输出个格式为 
这个是 小李子 二货'''
import re
res = re.findall(u'[\u4e00-\u9fa5]+',str1)
print(res)
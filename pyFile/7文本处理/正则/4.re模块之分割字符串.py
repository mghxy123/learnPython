#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 4.re模块之分割字符串.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008

print('#'*30,'字符串分割','#'*30)
'''
字符串的分割函数split,太难用不能指定对个字符串进行分割
re.split(pattern, string, maxsplit=0, flags=0)
re.split分割字符串
'''

import re

s = '''
os.path.abspath(path)
normapth(join.getcwd(),path()).
'''

print('#'*30,'把每行的单词提取出来','#'*30)

print(s.split())
print(re.split('[\.()\s,]',s))
print(re.split('\W',s))
print(re.split('[^a-z0-9_-]',s))










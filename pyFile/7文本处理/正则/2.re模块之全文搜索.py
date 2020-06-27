#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.全文搜索.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008

#####################全文搜索#########################
"""
re.findall(pattern,string,flags=0)
regex.findall(string,[,pos[,endpos]])
对整个字符串,重左至有匹配,返回所有匹配项的列表

re.finditer(pattern,string, flags=0)
regex.finditer(string[,pos[,endpos]])
整个字符串,从左至有匹配,返回所有匹配项,返回迭代器
注意每次迭代返回的都是match对象

"""

import re
s = '''bottle\nbag\nbig\nable'''

for i,c in enumerate(s,1):
    print((i-1,c),end='\n' if i%10 == 0 else ' ')
print()
print('-'*30)

print('+'*20+'findall方法'+'+'*20)
result = re.findall('b',s)
print(1,result)

regex = re.compile('^b')
result = regex.findall(s)
print(2,result)

regex = re.compile('^b',re.M)
result = regex.findall(s)
print(3,result)

regex = re.compile('^b',re.S)
result = regex.findall(s)
print(4, result)

regex = re.compile('^b',re.M)
result = regex.findall(s, 7, 10)
print(5, result)

print('#'*30+'finditer方法'+'#'*30)
result = regex.finditer(s)
print(6,type(result))

r = next(result)
print(type(r),r) #输出match对象
print(r.start(),r.end(),s[r.start():r.end()])
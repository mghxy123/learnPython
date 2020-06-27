#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.re模块之替换匹配.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008

print('#'*30+'替换匹配'+'#'*30)
'''
re.sub(pattern, replacement, string, count=0, flags=0)
regex.sub(replacement, string, count = 0)
使用pattern对字符串string进行分匹配,对匹配项使用repl替换
replacementent可以是string,bytes,function.
re.subn(pattern,replacement,string,count = 0, flage = 0)
regex.subn(replacement, string,count = 0)
同时sub返回一个元组(new_string, number_of_sube_made)
'''

import re

s = '''bottle\nbag\nbig\napple'''
for i,c in enumerate(s,1):
    print((i-1,c), end='\n' if i%8==0 else ' ')
print()

print('#'*30+'替换方法'+'#'*30)

regex = re.compile('b\wg')
result = regex.sub('hxy',s)
print(1,result)#被替换后的字符串

result = regex.sub('hxy',s,1)
print(2,result) #只替换一次

regex = re.compile('\s+')
result = regex.sub('\t',s)
print(3, result) #被替换后的字符串及替换次数的元组






re.sub























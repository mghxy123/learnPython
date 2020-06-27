#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1.re模块.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/7 0007

import re
s = '''bottle\nbag\nbig\napple'''

for i,c in enumerate(s,1):
    print((i-1,c),end='\n' if i%10==0 else ' ')
print()

#match 方法
print('--match--')
result = re.match('b',s) #找到一个就不找了
print(1,result) #bottle 中的b

result = re.match('a',s) #没有找到,返回None
print(2,result)

result = re.match('^a',s,re.M) #依然重开头开始找,多行模式也找不到 返回None
print(3,result)

result = re.match('^a',s,re.S) #重开头开始找,该用单行模式,依旧找不到 返回None
print(4,result)

#先编译,然后使用正则表达式对象
regex = re.compile('a')
result = regex.match(s) #依然重开头开始找,依旧找不到
print(5,result)

result = regex.match(s,15) #把索引15作为起点开始找,找到了match对象
print(6,result)

#使用search对象
print('---search---')
result = re.search('a',s) #扫描到匹配的第一个位置
print(7,result) #返回一个match对象 apple 的a

regex = re.compile('b')
result = regex.search(s,1)
print(8,result)#bag

regex = re.compile('^b',re.M)
result = regex.search(s) #不管是不是多行,找到就返回
print(8.5,result) #botter

result = regex.search(s,8)
print(9,result) #big


########################################
#fullmatch方法

result = re.fullmatch('bag',s)
print(10,result)

regex = re.compile('bag')
result  = regex.fullmatch(s)
print(11,result)

result = regex.fullmatch(s,7)
print(12,result)

result = regex.fullmatch(s,7,10)
print(13,result)#要完全匹配,少一个都不行




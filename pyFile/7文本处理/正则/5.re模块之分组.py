#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.re模块之分组.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/8 0008

print('*'*30+'分组'+'*'*30)
'''
使用小括号的pattern捕获的数据被放到了住group中.
match,search函数可以返回match对象,findall返回字符串列表;finditer返回一个个match对象
如果pattern中使用了分组,如果有匹配的结果,会在match对象中
    1.使用group(N)的方式返回对应分组,1到N是对应你的分组,0返回整个匹配的字符串,N不写缺省值为0
    2.如果是用了命名分组,可以使用group('name_number')的方式提取分组
    3.也可以使用group的方式返回所有组
    4,groupdict()返回所有命名分组
'''

import re

s = '''bottel\nbag\nbig\napple'''
for i,c in enumerate(s,1):
    print((i-1,c),end='\n' if i%10 == 0 else ' ')
print()

print(''*30+'分组'+'*'*30)
regex = re.compile('b\w+')
result = regex.match(s)#指定从头匹配一次
print(type(result))
print(1,'match',result.groups())

result = regex.search(s,1)#从指定位置匹配一次
print(2, 'search',result.groups())

print('*'*30+'命名分组'+'*'*30)

regex = re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
result = regex.match(s)
print(3,'match',result)
print(4 ,result.group(3),result.group(2),result.group(1))
print(5 ,result.group(0).encode()) #返回整个字符串,即match
print(6, result.group('name2'),result.group('name3'))
print(7, result.groups())
print(8, result.groupdict())



result = regex.findall(s)#返回什么?有几项?
for x in result: #有分组里面放的东西不一样
    print(type(x),x)

regex = re.compile('(?P<head>b\w)')
result = regex.finditer(s)
for x in result:
    print(type(x),x,x.group('head'))
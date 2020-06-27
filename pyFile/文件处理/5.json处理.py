#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 5.json处理.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/4 0004

import  json

d = {'a':1,'b':'abc','c':['1','2'],'d':{'e':(50,500),'f':[1,2,3]}}
d1=json.dumps(d)
print(d1)




#loads把字符串改成python认识的类型,传入的,必须是字符串
d2 = json.loads(d1)
print(type(d2),d2)

#loads把字符串改成python认识的类型,传入的,必须是字符串
j1 = '''{'a': '1', 'b': 'abc', 'c': ['1', '2'], 'd': {'e': ['50', '500'], 'f': ['1', '2', '3']}}'''
d3 = json.loads(j1)
print(type(d3),d3)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.可视化.py
# Author: HuXianyong
# Date  : 2019/5/25 14:49

class A:
    def __init__(self,name,age=20):
        self.name  = name
        self.age = age
    def __str__(self):
        return 'str : {} {}'.format(self.name,self.age)
    def __repr__(self):
        return 'repr : {} {}'.format(self.name,self.age)
    def __bytes__(self):
        import json
        return json.dumps(self.__dict__).encode()

print('使用内建函数str')
print(A('tom'))
print('{}'.format(A('tom')))
print([A('tom')],'\n') #使用的是__str__但是其内部使用的是__repr__

print([str(A('tom'))]) #[]使用__str__,其中的元素使用str()函数也调用__str__

print('str:a,1')#字符串直接输出是没有引号的
s = '1'
a = 1
d = 'a'
print(s,a,d)
print([d],(s,))#字符串在基本数据类型内不输出有引号
print({s,d})
print('使用bytes')
print(bytes(A('tom')))
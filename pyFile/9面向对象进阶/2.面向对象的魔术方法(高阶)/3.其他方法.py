#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 3.其他方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

#看到self都是实例相关,看到cls都是
class Person:
    def __init__(self,name,age=18):
        self.name = name
        self.age = age

    def __str__(self):
        return "str: {} {}".format(self.name,self.age)

    def __repr__(self):
        return "repr: {} {}".format(self.name, self.age)

    def __bytes__(self):
        return "repr: {} {}".format(self.name, self.age).encode()

a = Person(name='tom')
print(a)
print(str(a).encode())

print(bytes(a))
print(repr(a))
print('-'*30)


print([a],(a,)) #相当于print(str([]))
print(a)
print(str(a))
print('{}'.format(a))
print('{}'.format(repr(a)))

#默认的打印是str  print,format,str默然使用的都是str
#当没有str方法的时候,本该使用str方法的,就都会去找repr方法,
#当没有repr方法和str方法的时候会都去找bytes方法
#当没有repr方法的时候,本该是repr方法的输出都调用的是bytes方法
#当这三个都没有的时候就回去调用源类的方法


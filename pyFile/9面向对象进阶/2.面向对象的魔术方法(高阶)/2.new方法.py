#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 2.new方法.py
# Author: HuXianyong
# Mail: mghxy123@163.com
# Date  : 2019/5/22 0022

'''
__new__构造实例
__init__初始化实例
new方法实例化一个对象,先实例化对象,然后才是初始化
'''

#`111111111111111111111111111111111111111111111111
# class A:
#     def __new__(cls, *args, **kwargs):
#         pass
#     def __init__(self):
#         pass
#
# a = A()
# print(a)#这里会输出什么?为什么?

#这里面会所输出None,应为我们定义了new方法,但是我们没有给返回值

#`111111111111111111111111111111111111111111111111
# #我们把new方法注释了又会返回什么?
# class A:
##     def __new__(cls, *args, **kwargs):
##         pass
#     def __init__(self):
#         pass
#
# a = A()
# print(a)#这里会输出什么?为什么?

#会输出A的实例对象

#2222222222222222222222222222222222222222
# class A:
#     def __new__(cls, *args, **kwargs):
#         pass
#     def __init__(self,name):
#         self.name = name
#
#
# a = A() #这样调用是否会报错,为什么?
# print(a)

#33333333333333333333333333333333333333333333
#
# class A:
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)
#     def __init__(self,name):
#         self.name  = name
#
# a = A() #这样调用是否会报错,为什么?
# print(a)

#44444444444444444444444444444444444444
# class A:
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls)
#     def __init__(self,name):
#         self.name  = name
#
# a = A(name='tom') #这样调用是否会报错,为什么?
# print(a)

#5555555555555555555555555555555555555555555
# class A:
#     def __new__(cls, *args, **kwargs):
#         print(cls)
#         print(args)
#         print(kwargs)
#         return super().__new__(cls)
#     def __init__(self,name):
#         self.name  = name
#
# a = A(name='tom') #这样调用是否会报错,为什么?
# print(a)
#这里面的kwargs会有tom,但是这里面获得的变量和init里面的无关


#66666666666666666666666666666666666666
class A:
    def __new__(cls, *args, **kwargs):
        print(cls)
        print(args)
        args = ('jerry',)
        print(kwargs)
        kwargs = {'name': 'aaa'}
        return super().__new__(cls)
    def __init__(self,name):
        self.name  = name

a = A(name='tom')
print(a.name) #这样输出的会是什么?

#依旧会输出tom,new方法里面定义args和kwargs与,init里面定义的无关,不会被调用
#777777777777777777777777777777777777777
#动态增加属性
class A:
    def __new__(cls, *args, **kwargs):
        cls.test = 'test'
        return super().__new__(cls)
    def __init__(self,name):
        self.name  = name

a = A(name='tom')
print(a)
print(A.__dict__)
#但是这样增加方法不太好,实例化一次就增加一次